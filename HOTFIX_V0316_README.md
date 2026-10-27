# JÁDRO REBORN — v0.3.16 hotfix candidate

This branch contains a **source-code patch generator**, not a rebuilt game or a Windows executable.

## Using the patch

1. Extract the original `JADRO_REBORN_V0315_GRAPHICS_ZDROJOVE_KODY.zip` to a local directory.
2. Download `tools/apply_v0316_fixes.py` from this branch and run:
   ```powershell
   py -3 tools/apply_v0316_fixes.py "C:\path\to\extracted\JADRO_REBORN"
   ```
3. The script writes a **new sibling directory** named `*_FIXED_V0316`; the old source is preserved.
4. In the generated directory, run the Node.js tests, `go test ./...` and `go vet ./...`, Python installer tests, then `python scripts/package_release.py`.
5. Test the resulting executable on Windows with **shaders Low and Cinematic**, especially the previously invisible character.

## Changes supplied by generator

- Correct GitHub Release archive lookup and expanded JS tests.
- Version label normalization to 0.3.16.
- Dedicated native pre-reset save snapshot, separate from rolling `.bak`.
- Longer HTTP drain on exit and shorter autosave interval. Unexpected crashes can still lose progress not yet saved.
- 60 Hz fixed-step simulation with work cap for low FPS.
- Avoid whole-save writes whenever graphics/audio sliders move.
- Experimental WebGL2 **opaque overlay disabled** on Windows; Canvas2D shader pack stays enabled.
- Reject unexpected nested files during Windows upgrades.

## Important release status

**Not tested against an extracted source tree in the current environment.** The original source archive has not been uploaded to GitHub, and this branch is not a complete playable build. Run all tests and verify the game visually before merging/releasing.