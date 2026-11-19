# JÁDRO REBORN v0.3.25 — Performance Monitor (Beta RC)

**Status:** Beta Release Candidate — NOT Stable. Windows 10/11 runtime metrics have not yet been verified on real Windows hardware.

## Changes from the actual v0.3.25 source archive
- Optional performance overlay in Settings, available in Czech and English: FPS, RAM, CPU and GPU.
- FPS is derived from rendered frames. RAM/CPU/GPU percentages represent the whole machine, **not** this game's process.
- On Windows the Go launcher queries Windows CIM and GPU Engine performance counters. If a metric is unavailable the overlay shows `—`; no guessed values.
- OS metrics are refreshed about every 5 seconds without holding the save mutex.
- On Linux or in standalone web mode CPU/GPU/RAM metrics are not available.
- No changes to excavation mechanics or the expedition save format.

## Verified local distribution archive SHA-256
```
59a672264e8b59fbbcee6993b50d9af3f1475353fe3c560c669d0e57ab7a1f88  JADRO_REBORN_V0325_HYBRID_SOURCE.zip
71af46bd113a387802c78ce70f92ef0c244ed8b4e9e92ed929a9c1e9018d1b1c  JADRO_REBORN_V0325_HYBRID_WINDOWS.zip
53ddbd6739e800216ef7ffd99abe36409c673ea393c583a8cceda73db13d5735  JADRO_REBORN_V0325_HYBRID_COMPLETE.zip
```

These hashes were calculated from local archive bytes on 2026-10-30. The archives are **not** hosted in this repository.

## Full-source upload required
The verified source ZIP has 63 files including `launcher/` (Go source), `launcher/web/` (HTML, CSS, JS, PNG and WAV/OGG), `tests/`, `scripts/`, and `.github/workflows/`.

**GitHub connector limitation:** this branch currently contains only this release note, not the source files, game media or Windows executable. Do not merge or advertise a GitHub downloadable game on this basis.

### To complete upload without rewriting history
1. Download and extract the source ZIP.
2. Upload its **contents** to this repository on the branch `release/v0.3.25-performance-monitor` (not the ZIP as the only source).
3. Ensure the complete folder tree is preserved, including hidden `.github` workflow files.
4. Run Go tests, JavaScript and Chromium regressions in GitHub Actions and confirm Windows x64 build.
5. Publish an optional **prerelease**, not Stable, once the ZIP assets are actually uploaded and verified.

## Windows Smart App Control
Windows EXE is currently unsigned; Smart App Control might reject it. Do not disable protection to run the build.
