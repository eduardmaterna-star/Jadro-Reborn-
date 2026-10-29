# JÁDRO REBORN v0.3.21 — Hybrid Recovery RC

**Status: Release Candidate; NOT a stable release.** Created 29 October 2026 from the user-provided original v0.3.15 Windows game plus the v0.3.20 hybrid save backend.

## Changes since v0.3.20
1. Fixed DOM exception on successful Save & Quit and stopped the animation loop on confirmed quit.
2. Desktop mode now blocks starting a new expedition when `/api/session` is unavailable; browser storage fallback remains only for standalone preview.
3. Separated video and audio preferences from large expedition saves. Volume slider writes are debounced 400 ms; legacy save settings are migrated only if no independent settings exist.
4. Clears premium CanvasPattern references and bitmap image cache when entering Potato.
5. 60 Hz fixed physics step can catch up 8 steps per rendered frame (was 5), improving behavior at 10–15 FPS while maintaining a CPU cap.
6. End-of-game trigger and HUD now agree on 6,371 km.
7. Version synchronized to 0.3.21 across launcher, HTML, scripts, and Windows packaging.

## Locally executed validation
- Go `go test ./...` + `go vet ./...`: passed.
- `node --check launcher/web/game.js`: passed.
- Media source verification: 27 required files passed; 5 Python original-asset tests passed.
- Chromium game smoke test: passed.
- Chromium regression for native HTTP 503, isolated settings, low-FPS physics budget, victory depth, and Potato CanvasPattern eviction: passed.
- Chromium-to-real-Go API test: save/load, reset, restore, migrated excavations, authenticated safe quit: passed; Playwright HTTP relay occasionally logs a target-closed warning while the test completes.
- Cross-compiled Windows x64 PE: passed.
- ZIP CRC and SHA-256: passed.

## Archive SHA-256
```
115a09dc53ad811dcb644b1f5c28987ee95649585e8cc7b80d67cb19d4a544c6  JADRO_REBORN_V0321_HYBRID_WINDOWS.zip
3d6c6092d3432160763b7d6a21c9d0b8d9d359bc40a43c958c30a05b61c41d46  JADRO_REBORN_V0321_HYBRID_SOURCE.zip
ec078dafe2c64563eedae1f97645213b506477ee4c673658e6144dba40641a86  JADRO_REBORN_V0321_HYBRID_COMPLETE.zip
```

## Publication blocker
The main repository is still missing the full game sources, original large PNG/WAV media, and Windows binary. **This note does NOT upload those files or mean that GitHub Actions built them.** Do not create a version tag or publish a stable release until the complete source archive is committed and the real Windows CI build and Windows 10/11 smoke tests pass.

## Manual release tests still required
1. Start Windows EXE from a clean extraction.
2. Test save, reset backup, recovery, shutdown, relaunch, and Windows file permissions.
3. Test native save-session failure and recovery, longer digging and FPS at 10–15.
4. Complete a full expedition to the center.
