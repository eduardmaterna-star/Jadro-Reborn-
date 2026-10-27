#!/usr/bin/env python3
"""JADRO REBORN 0.3.16 source hotfix generator.

Usage:
    python tools/apply_v0316_fixes.py PATH_TO_EXTRACTED_V0315_SOURCE

The script copies the source to a new sibling folder and patches that copy.
It never silently changes the original project. Run the included tests and
build script on the resulting folder before publishing any release.
"""
from pathlib import Path
import re
import shutil
import sys

TARGET_VERSION = "0.3.16"

def replace_once(source, old, new, label):
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, got {count}")
    return source.replace(old, new, 1)

def substitute_once(source, pattern, repl, label, flags=0):
    new, count = re.subn(pattern, repl, source, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: pattern not found")
    return new

def update(root, filename, transform):
    path = root / filename
    if not path.is_file():
        raise FileNotFoundError(path)
    old = path.read_text(encoding="utf-8")
    new = transform(old)
    if old == new:
        raise RuntimeError(f"No changes made: {filename}")
    path.write_text(new, encoding="utf-8", newline="\n")
    print("PATCHED", filename)

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python apply_v0316_fixes.py EXTRACTED_SOURCE_DIRECTORY")
    original = Path(sys.argv[1]).expanduser().resolve()
    if not (original / "launcher/web/game.js").is_file():
        roots = list(original.glob("*/launcher/web/game.js"))
        if len(roots) != 1:
            raise SystemExit("Could not uniquely find launcher/web/game.js. Pass the extracted project folder.")
        original = roots[0].parents[2]
    dest = original.parent / (original.name + "_FIXED_V0316")
    if dest.exists():
        raise SystemExit("Output already exists, refusing to overwrite: " + str(dest))
    shutil.copytree(original, dest)
    (dest / "VERSION").write_text(TARGET_VERSION + "\n", encoding="utf-8")

    def package(s):
        s = replace_once(s, "VERSION='0.3.14'",
            "VERSION=(ROOT/'VERSION').read_text(encoding='utf-8').strip()",
            "release version")
        s = replace_once(s, "dist.mkdir(parents=True)",
            "dist.mkdir(parents=True)\n    shutil.copy2(ROOT/'VERSION', dist/'VERSION')",
            "include VERSION in installer")
        return s
    update(dest, "scripts/package_release.py", package)

    def go_version(s):
        if "0.3.14" not in s:
            raise RuntimeError("launcher/version.go does not have expected version")
        return s.replace("0.3.14", TARGET_VERSION)
    update(dest, "launcher/version.go", go_version)

    def py_installer(s):
        if "0.3.6" not in s:
            raise RuntimeError("installer Python has unknown version")
        s = s.replace("VERSION = '0.3.6'",
            "VERSION = (ROOT / 'VERSION').read_text('utf-8').strip() if (ROOT / 'VERSION').is_file() else '0.3.16'")
        return s.replace("0.3.6", TARGET_VERSION)
    update(dest, "installer/instalator.py", py_installer)

    for name in ("installer/instalovat_unix.sh",
                 "installer/INSTALOVAT_WINDOWS.ps1"):
        update(dest, name, lambda s: s.replace("0.3.6", TARGET_VERSION)
            if "0.3.6" in s else (_ for _ in ()).throw(RuntimeError("Missing version in " + name)))

    def windows(s):
        anchor = "    return $true\n}\n\ntry {"
        # Prevent overwriting files nested in a previous installation.
        check = """    $expectedWeb = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($p in $files.PSObject.Properties) {
        if ($p.Name.StartsWith('web/')) { [void]$expectedWeb.Add($p.Name.Substring(4)) }
    }
    $installedWeb = Join-Path $path 'web'
    if (Test-Path -LiteralPath $installedWeb) {
        foreach ($existing in Get-ChildItem -LiteralPath $installedWeb -Recurse -File -Force) {
            if ([bool]($existing.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
                throw "Symbolicky odkaz v instalaci: $($existing.FullName)"
            }
            $relative = $existing.FullName.Substring($installedWeb.Length + 1).Replace('\\', '/')
            if (-not $expectedWeb.Contains($relative)) {
                throw "Cizi soubor uvnitr web/: $relative. Aktualizace zastavena."
            }
        }
    }
    return $true
}

try {"""
        return replace_once(s, anchor, check, "Windows nested-file safety")
    update(dest, "installer/INSTALOVAT_WINDOWS.ps1", windows)

    def html(s):
        # Only the public UI version marker, not historical changelog comments.
        if "v0.3.13" in s:
            s = s.replace("v0.3.13", "v0.3.16")
        elif "0.3.13" in s:
            s = s.replace("0.3.13", TARGET_VERSION)
        else:
            raise RuntimeError("UI version marker could not be located")
        return s
    update(dest, "launcher/web/index.html", html)

    def save_api(s):
        anchor = "if err = s.writeAtomic(body); err != nil {"
        guard = """// Explicit new-expedition save: preserve the preceding expedition
    // separately from the rotating .bak file.
    if r.Header.Get("X-Jadro-Reset-Backup") == "1" {
        previous, readErr := readValidSave(s.file)
        if readErr == nil {
            backupPath := filepath.Join(filepath.Dir(s.file), "expedition-before-reset.json")
            if err := writeAtomicFile(backupPath, previous); err != nil {
                http.Error(w, "reset backup failed: "+err.Error(), http.StatusInternalServerError)
                return
            }
        } else if !errors.Is(readErr, os.ErrNotExist) {
            // Never reset if the existing expedition cannot be safely backed up.
            http.Error(w, "previous expedition invalid; reset refused", http.StatusConflict)
            return
        }
    }
    """
        return replace_once(s, anchor, guard + anchor, "native reset backup")
    update(dest, "launcher/save_api.go", save_api)

    def game(s):
        # Keep the Canvas2D shaders; suppress the experimental WebGL2 overlay.
        # Its opaque overlay may present a blank frame, hiding the miner.
        pattern = r"function applyGPUShader\(\)\{[\s\S]*?\n\}\n\n(?=// VYSVĚTLIVKA: Nastaví rozlišení)"
        replacement = """function applyGPUShader(){
 // Windows-safe renderer: do not overlay a second opaque WebGL canvas.
 // drawShaderPackPass already provides bloom, grading and vignette in Canvas2D.
 const output=document.getElementById('shaderOutput');
 if(output)output.style.display='none';
}

"""
        s = substitute_once(s, pattern, replacement, "shader visibility")
        # Do not store a full expedition every time a graphic or volume slider moves.
        s = replace_once(s,
            "if(currentPage!=='intro'&&!loadError&&!resetInProgress)save().catch(()=>{});}",
            "}",
            "settings save storm")
        # Preserve native pre-reset backup only for explicitly requested resets.
        s = replace_once(s, "async function nativePut(data){",
            "async function nativePut(data,beforeReset=false){", "native backup argument")
        s = replace_once(s,
            "'X-Jadro-Token':nativeToken,'Content-Type':'application/json'},body:JSON.stringify(data)});",
            "'X-Jadro-Token':nativeToken,'Content-Type':'application/json',...(beforeReset?{'X-Jadro-Reset-Backup':'1'}:{})},body:JSON.stringify(data)});",
            "native reset header")
        s = replace_once(s, "function queueSaveData(copy){",
            "function queueSaveData(copy,beforeReset=false){", "queue backup argument")
        s = replace_once(s, "await nativePut(copy);",
            "await nativePut(copy,beforeReset);", "queue native forwarding")
        s = replace_once(s, "const saved=await queueSaveData(fresh);",
            "const saved=await queueSaveData(fresh,true);", "request native pre-reset backup")
        # Stable fixed step even on 10 FPS / low-powered hardware.
        s = substitute_once(s,
            r"let lastPotatoFrame=0;function animate\(ts\)\{[^\n]*\}",
            """let lastPotatoFrame=0,physicsDebt=0;
function animate(ts){
 const cap=settings.fps||0;
 if(cap&&ts-lastPotatoFrame<1000/cap-1){requestAnimationFrame(animate);return}
 lastPotatoFrame=ts;
 const dt=Math.max(0,Math.min(.25,(ts-prev)/1000||.016));
 prev=ts;vw=innerWidth;vh=innerHeight;
 if(!paused){
   physicsDebt+=dt;
   let steps=0;
   while(physicsDebt>=1/60 && steps<15){
     update(1/60);physicsDebt-=1/60;steps++;
   }
   if(steps===15)physicsDebt=0;
 }else physicsDebt=0;
 render();requestAnimationFrame(animate);
}""",
            "fixed timestep")
        s = replace_once(s, "saveTimer>30", "saveTimer>10", "more frequent autosave")
        return s
    update(dest, "launcher/web/game.js", game)

    def launcher(s):
        return replace_once(s,
            "context.WithTimeout(context.Background(), 2*time.Second)",
            "context.WithTimeout(context.Background(), 8*time.Second)",
            "wait for accepted disk writes on browser close")
    update(dest, "launcher/main.go", launcher)

    def workflow(s):
        s = replace_once(s,
            "          node test_save_safety.cjs",
            """          node test_save_safety.cjs
          node test_potato.cjs
          node test_graphics_settings.cjs
          node test_safe_exit.cjs
          node test_shader_visibility.cjs""",
            "CI regression coverage")
        s = replace_once(s,
            "JadroReborn-0.3.7-all-platforms",
            "JadroReborn-all-platforms",
            "CI artifact label")
        s = s.replace("dist/JADRO_REBORN_INSTALLER_0.3.7.zip",
            "dist/JADRO_REBORN_INSTALLER_*.zip", 1)
        old = """          gh release view "$GITHUB_REF_NAME" >/dev/null 2>&1 && gh release upload "$GITHUB_REF_NAME" dist/JADRO_REBORN_INSTALLER_0.3.7.zip --clobber || gh release create "$GITHUB_REF_NAME" dist/JADRO_REBORN_INSTALLER_0.3.7.zip --generate-notes --verify-tag"""
        new = """          test "$GITHUB_REF_NAME" = "v$(cat VERSION)" || { echo "Tag/version mismatch"; exit 1; }
          archive="$(find dist -maxdepth 1 -type f -name 'JADRO_REBORN_INSTALLER_*.zip' -print -quit)"
          test -s "$archive" || { echo "Release archive missing"; exit 1; }
          if gh release view "$GITHUB_REF_NAME" >/dev/null 2>&1; then
            gh release upload "$GITHUB_REF_NAME" "$archive" --clobber
          else
            gh release create "$GITHUB_REF_NAME" "$archive" --generate-notes --verify-tag
          fi"""
        return replace_once(s, old, new, "GitHub Release actual filename")
    update(dest, ".github/workflows/build-release.yml", workflow)

    (dest / "test_shader_visibility.cjs").write_text("""const fs=require('fs'),assert=require('node:assert/strict');
const src=fs.readFileSync(__dirname+'/launcher/web/game.js','utf8');
const fn=src.match(/function applyGPUShader\\(\\)\\{[\\s\\S]*?\\n\\}/);
assert(fn,'GPU fallback function missing');
assert(fn[0].includes("output.style.display='none'"),'Broken opaque WebGL layer must be hidden');
assert(!fn[0].includes('gl.drawArrays'),'Opaque WebGL overlay must stay disabled');
assert(src.includes('drawShaderPackPass();'),'Canvas2D shader effects should remain active');
assert(src.includes('drawPerson();'),'The miner must still be rendered');
console.log('PASS shader fallback: Canvas2D effects remain and character overlay is not obscured');
""", encoding="utf-8")

    (dest / "HOTFIX_NOTES.md").write_text(
        "# JÁDRO REBORN 0.3.16 — source hotfix candidate\n\n"
        "- GitHub Actions discovers the produced installer archive and runs all JS checks.\n"
        "- Package and installer version labels changed to 0.3.16; VERSION used by release build.\n"
        "- Native reset protects expedition-before-reset.json independently of .bak.\n"
        "- Browser shutdown allows accepted requests 8 seconds to finish; autosaves every 10 seconds.\n"
        "- Physics uses fixed 60 Hz steps, up to 15 per frame to prevent spiral of death.\n"
        "- Settings no longer trigger whole-expedition saves on every slider change.\n"
        "- WebGL2 overlay is temporarily disabled: Canvas2D shader effects remain, miner stays visible.\n"
        "- Windows installer rejects unexpected files nested within web/.\n\n"
        "UNVERIFIED: Run tests and a real Windows playtest before publishing. "
        "Sudden process termination can never guarantee saving progress not yet received by the launcher.\n",
        encoding="utf-8")
    print("\nGenerated:", dest)
    print("Run: node test_shader_visibility.cjs && node test_game_vm.cjs")
    print("Run: node test_potato.cjs && node test_graphics_settings.cjs && node test_safe_exit.cjs")
    print("Run: (cd launcher && go test ./... && go vet ./...)")
    print("Run: python -m unittest discover -s installer/tests -v")
    print("Build Windows x64 after tests. Existing executable in v0.3.15 ZIP is NOT modified.")

if __name__ == "__main__":
    main()
