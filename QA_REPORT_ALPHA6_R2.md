# JÁDRO REBORN — QA report alpha.6 R2 review candidate

Datum: 2026-11-19. Aplikační verze: 0.4.0-alpha.6. Singleplayer candidate derived from the user-supplied R1 source archive.

## Source integrity
- Original R1 archive: 36,818,565 bytes; SHA-256 `1f7ef0f2c4b38d2f06ad602c821ef3ccc5af8d7b13cd5e37ec07c47e303b4453`.
- 169 original ZIP entries; CRC PASS; no duplicate, absolute or traversal paths or symlinks.
- All 24 original asset hashes match `ASSET_SHA256.json`.
- Historical `ZDROJE_MANIFEST_SHA256.json` has 29/89 mismatches; it is retained as history. The reviewed R2 archive has a fresh complete SHA-256/size manifest.
- Reviewed R2 source archive: 130 entries including manifest (129 source files), CRC and every manifest hash/size PASS.
- Unified patch applies to a clean R1 extraction and all 17 patch-managed files match the reviewed working tree byte-for-byte: PASS.

## Candidate fixes
- #16: nanosecond backup names and regression test; tie-order race tests 30× PASS.
- #23/#24: SFX hooks for dig/buy/sell/ladder/wind, small audio pool/cooldown, independent persisted Music/SFX/Ambient settings.
- #25: removed two unused per-pixel render calculations; no FPS gain is claimed without before/after profiling.
- #10: UI test remains in local release runner; legacy browser test selector fixed to interact with the in-world station via E.
- #19: fixed installer allowlist mismatch (alpha.4 changelog name in alpha.6 package); added Go regression test.
- Packaging: generated log/cache directories and EXEs excluded from SOURCE package; release SOURCE now contains its own `SOURCE_MANIFEST.json`.

## Verification
- `python scripts/run_release_tests.py local`: 12/12 PASS.
- Python unit suite: 13/13 PASS.
- Go unit/race tests, go vet, go mod verify: PASS.
- Installer Go tests: 3/3 PASS.
- Targeted Chromium hybrid, backup, review, metrics, alpha4 feature and visual test scripts: PASS. Visual test used Canvas2D fallback because WebGL2 context was unavailable.
- Linux amd64 build and Windows amd64 / macOS amd64+arm64 Go cross-builds: PASS.
- Windows game/server cross-build and packaging: PASS; Windows ZIP has 7 files, ZIP CRC and SHA manifest PASS.
- Online installer: 5,614,592 bytes (under 9 MB), pinned to the Windows ZIP SHA-256.
- Installer integration using a native Linux build, local HTTP server and actual generated Windows ZIP: PASS — hash verified, both Windows PE binaries extracted, existing installation overwrite rejected.
- SOURCE ZIP: 127 files plus self-describing SHA-256/size manifest; COMPLETE ZIP nested hashes and CRC PASS; root `sha256sum -c dist/SHA256SUMS.txt` PASS.
- Headless telemetry benchmark: 24/24 samples. Median RAF FPS (overlay OFF/ON): Potato 60.0/59.2, Low 60.3/59.6, Medium 48.0/49.6, High 41.2/41.9.

## Limitations / NOT RUN
- Real Windows 11, Linux and macOS desktop GUI/runtime/audio: NOT RUN.
- Windows installer was not executed under Windows; integration test ran Linux build of the installer against a local HTTP server.
- WebGL2/GPU context and GPU profiling, renderer before/after FPS comparison: NOT RUN.
- Go 1.27.3 toolchain from workflow unavailable locally; build toolchain here was Go 1.23.2.
- Authenticode signing, signed workflow, GitHub release upload/publication: NOT RUN.
- Multiplayer/WSS work remains outside current singleplayer scope.

## Repository status
This report is local QA evidence, not a claim that the source ZIP has been imported. The actual game source and binary assets are still absent from GitHub `main`; this PR is documentation only. No Issue was closed, no release was published, and nothing was merged to `main`.