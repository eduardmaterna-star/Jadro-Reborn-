# QA report — Jádro Reborn v0.4.0-alpha.6 R2 candidate

Date: 2026-11-19

## Source archive
- Input: `JADRO_REBORN_V0400_ALPHA6_R1_SOURCE.zip`
- Size: 36,818,565 bytes
- SHA-256: `1f7ef0f2c4b38d2f06ad602c821ef3ccc5af8d7b13cd5e37ec07c47e303b4453`
- 169 original ZIP entries; CRC passed; no duplicate paths, traversal paths, absolute paths, or symlink entries.
- All 24 asset hashes matched `ASSET_SHA256.json`.
- Historical `ZDROJE_MANIFEST_SHA256.json`: 29 of 89 hashes differ from the current archive. A new complete manifest was generated in the reviewed local archive.

## Candidate code changes (local reviewed archive)
- Issue #16: nanosecond timestamps for new save backups; legacy backup names remain supported. Added regression coverage. Focused race tests passed 30 consecutive runs.
- Issues #23/#24: connected dig, buy, sell, ladder and wind WAV effects; added audio pooling/throttling and independent Music, SFX and Ambient volume settings.
- Issue #25: removed two unused calculations from the per-pixel render hot path; added a static regression test. No FPS improvement is claimed because profiling was not run.
- Issue #10: UI regression test included in the release test runner.

## Test results
- `python scripts/run_release_tests.py local`: **12/12 PASS**
- Go unit tests: PASS
- Go race tests: PASS
- `go vet ./...`: PASS
- JavaScript syntax checks: PASS
- Python unit tests: 11 PASS
- Native hybrid integration: PASS (non-fatal Playwright TargetClosed warnings appeared)
- Linux amd64 build: PASS
- Windows amd64 cross-build: PASS
- macOS amd64 and arm64 cross-builds: PASS
- Source verification: 31 mandatory files and referenced assets verified
- Patch dry-run and clean-archive application comparison: PASS

## NOT RUN / limitations
- Windows 11, Linux and macOS desktop runtime, GUI and audio testing: NOT RUN.
- GPU profiling and measured FPS benchmark: NOT RUN.
- Full browser regression suite did not complete; legacy alpha.4 browser test waits for obsolete selector `#quickShop`.
- Telemetry benchmark timed out in this environment.
- Go 1.27.3 workflow toolchain was not available locally; local Go was 1.23.2.
- Installer build, signed release and GitHub Actions release: NOT RUN.

## Repository status
This report documents local validation only. The reviewed source archive and its binary assets have **not** been imported into this repository by this PR. The local candidate fixes are not yet part of GitHub `main`. No Issues are closed and no release is created.