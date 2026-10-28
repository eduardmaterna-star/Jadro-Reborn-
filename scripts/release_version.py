#!/usr/bin/env python3
"""Package current tagged sources and Windows executable as separate verified ZIPs."""
import argparse
import hashlib
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(part)
    return h.hexdigest()

def make_zip(dest, entries):
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for disk, name in entries:
            z.write(disk, name)
    with zipfile.ZipFile(dest) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError(f"Corrupt ZIP entry: {bad}")
        if set(z.namelist()) != {name for _, name in entries}:
            raise RuntimeError("Unexpected ZIP entries")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    import re
    if not re.fullmatch(r"\d+\.\d+\.\d+", args.version):
        raise ValueError("Release version must be X.Y.Z")
    DIST.mkdir(exist_ok=True)
    exe = DIST / f"JadroReborn-v{args.version}-Windows-x64.exe"
    if not exe.is_file() or exe.stat().st_size < 1_000_000:
        raise RuntimeError("Windows executable missing or suspiciously small")
    windows = DIST / f"JADRO_REBORN_v{args.version}_WINDOWS.zip"
    files = [(exe, exe.name)]
    for extra in ("README.md", "REVIEW_FIXES_V0318.md"):
        p = ROOT / extra
        if p.is_file():
            files.append((p, p.name))
    make_zip(windows, files)

    source = DIST / f"JADRO_REBORN_v{args.version}_SOURCE.zip"
    result = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True).stdout
    tracked = sorted({Path(p.decode("utf-8")) for p in result.split(b"\0") if p})
    entries = []
    for p in tracked:
        if p.parts[0] == "dist" or p.suffix.lower() == ".exe":
            continue
        disk = ROOT / p
        if disk.is_file() and not disk.is_symlink():
            entries.append((disk, p.as_posix()))
    if not any(name == "launcher/web/game.js" for _, name in entries):
        raise RuntimeError("Game source is missing from Git index")
    make_zip(source, entries)

    sums = DIST / "SHA256SUMS.txt"
    sums.write_text("".join(f"{digest(p)}  {p.name}\\n" for p in (windows, source)), encoding="utf-8")
    print(f"Verified release v{args.version}: {windows.name}, {source.name}")

if __name__ == "__main__":
    main()
