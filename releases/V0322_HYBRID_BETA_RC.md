# JÁDRO REBORN v0.3.22 — HYBRID BETA RC

**Status:** Beta Release Candidate (not stable).  
**Date:** 2026-10-29  
**Source basis:** recovered original 0.3.15 + hybrid 0.3.21.

## Changes

- Authenticated Go API supports explicit restoration of any listed `pre-reset-*.json` archive, not only the latest.
- Backup management displays size, date and validation status, with player-confirmed manual deletion.
- Original expedition is archived before restoration; no automatic pruning of backups.
- Backup names are checked against an exact allowlist and validated filename format, protecting arbitrary files.
- Backup ordering uses filesystem modification time, fixing ambiguous random suffixes from multiple resets within the same second.
- CI workflow includes Chromium regressions `test_review_v0321.py` and `test_backup_v0322.py`.
- Original graphics, soundtracks and mining mechanics unchanged.

## Local verification

PASS: `go test ./... -count=1`, `go vet ./...`, `node --check`, 5 asset tests, Chromium smoke test, v0.3.21 regression test, new backup UI test, real Go API/Chromium integration, cross-compiled Windows PE x64, ZIP CRC and SHA-256.

Limitations: Browser integration emits `TargetClosedError` warnings on shutdown; the integration assertions passed. Full Windows 10/11 execution, long-term performance and manual end-to-end playthrough **not verified**.

## Locally assembled archives

| Archive | SHA-256 |
|---|---|
| `JADRO_REBORN_V0322_HYBRID_WINDOWS.zip` | `dc878b4ae618734222f28414d0ee05d225d5f2319ec89e13583dfdaacf915060` |
| `JADRO_REBORN_V0322_HYBRID_SOURCE.zip` | `fe6c30467eae40fd9abdd4f43b28099dd1f2073f6fc02d084da0b330e2a1db6a` |
| `JADRO_REBORN_V0322_HYBRID_COMPLETE.zip` | `872b693921d37a3ecfed3b3c5df52a2592f5453a38d56abb1b018594fd8cddf6` |

## GitHub upload blocker

**These archives and the complete game sources/assets are NOT yet uploaded to this repository.** The GitHub connection in this environment does not offer an upload of 35+ MB binary file trees/Release assets. This file is a traceable release-candidate record, not a published build.

**Do not create a stable GitHub release or version tag** until all sources are actually committed and the Windows CI build and manual Windows smoke tests pass.

## Next actions

1. Add complete `launcher/`, `tests/`, `scripts/`, game assets/music and workflows from verified v0.3.22 source ZIP to a branch.
2. Run repository Windows CI and verify generated binary and SHA-256 checks.
3. Run/save/reset/restore/quit smoke test on actual Windows 10/11.
4. Publish `v0.3.22-beta.1` GitHub prerelease and attach the tested ZIPs.
