# JÁDRO REBORN — alpha.6 R2 review candidate QA

Datum: 2026-11-19. Aplikační verze zůstává `0.4.0-alpha.6`; R2 je revize lokálního source candidate, nikoli publikované nové herní verze.

## Opravy
- **#16 Save/backup:** nanosekundové názvy nových záloh, kompatibilita se starými názvy, race regression test 30×.
- **#23 SFX:** dig/buy/sell/ladder/wind, pool a cooldown, nezahajovat SFX při skryté stránce.
- **#24 Sound Engine:** samostatné Music/SFX/Ambient volumes; hloubkový mix má nejvýše dvě sousední OGG vrstvy, neaktivní se po fade-out pozastaví, audio se pozastaví při skrytí okna a obnovuje s autoplay retry.
- **#25 Renderer:** odstraněny dva nepotřebné výpočty z per-pixel hot path; bez FPS before/after měření netvrdíme výkonový nárůst.
- **#19 Installer:** opraven alpha.4 → alpha.6 changelog allowlist, přidán regresní Go test.
- **Packaging:** čistý source selection, SOURCE manifest, žádné test logy/cache/EXE ve SOURCE ZIP.
- **CI candidate:** Windows x64, Linux x64, macOS amd64/arm64; read-only permissions; Go 1.27.4 v aktivních workflow.

## Lokální QA — PASS
- `python scripts/run_release_tests.py local`: **13/13 PASS**.
- Python unittest: **18/18 PASS**.
- Node regressions #10/#23/#24/#25: PASS.
- Go unit, race, vet, mod verify: PASS.
- Installer Go tests: **3/3 PASS**.
- Chromium hybrid, alpha4 gameplay/audio smoke, backup v0.3.22/v0.3.23, review v0.3.21, metrics: PASS.
- Visual alpha.3 browser test: PASS via Canvas2D fallback; WebGL2 GPU context unavailable.
- Cross-platform workflow YAML parse + static tests: **5/5 PASS**.
- Windows amd64, Linux amd64, macOS amd64/arm64 client/server cross-builds: PASS using local Go 1.23.2.
- Source patch applies to a clean R1 extraction; all 24 changed files match byte-for-byte.
- Installer integration against the final Windows ZIP: download, pinned SHA-256 verification, archive extraction and refusing overwrite of an existing version: PASS. Integration used the Linux installer build and a local HTTP server, not Windows runtime.
- Release packaging: Windows ZIP 7 entries, SOURCE ZIP 130 files + manifest, COMPLETE ZIP (3 nested artifacts); CRC, manifests and `sha256sum -c dist/SHA256SUMS.txt`: PASS.
- Headless telemetry benchmark: 24/24 samples; not a physical GPU/hardware benchmark.

## Finální lokální artefakty
| Artefakt | Velikost | SHA-256 |
|---|---:|---|
| Reviewed R2 source ZIP (133 entries) | 36,857,446 B | `5eb81f4d7c3acb42e51154a797475ae96a90bdd7eee4616cdea04f9e35b95134` |
| R1→R2 patch (24 files) | 83,272 B | `f421b3216c018687b4e7ab2317bd6aa91b01f8600aaca8bdfba0267167e60cb5` |
| Windows ZIP | 41,819,385 B | `4c1c21b34e32c2de0d5a8822b4d8e17d47f423292feab7264d4719f45ed8f950` |
| SOURCE ZIP | 36,829,412 B | `7f21d46920bae92cf5ed80f73df700e62d022d91afb4cb5b19e0016575ab78c6` |
| COMPLETE ZIP | 81,049,182 B | `4dc5b6df6f724a0e95c9641dc06ae196470ff66c764ee1dd3a05c1921da039fe` |
| Online installer | 5,614,592 B | `9e873e8bb529003054aba614cfec36f1be2b145129345d26de1a328c4c36e137` |

## NOT RUN / omezení
- Windows 11, Linux, macOS desktop GUI/runtime a skutečný audio výstup: NOT RUN.
- WebGL2/GPU profiling, renderer before/after performance: NOT RUN.
- Go 1.27.4 nebyl lokálně dostupný; lokální builds použily Go 1.23.2.
- Windows native installer run, Authenticode signing, public hosting and GitHub release publication: NOT RUN.
- GitHub Actions has not run the game build matrix against a complete checked-in game source; the source tree and binary assets remain absent from `main`.
- Separate Windows R2 EXE bundle lacks matching VCS commit provenance and includes deferred multiplayer #22; not merged into this singleplayer candidate.

## Repository status
PR #30 is documentation only; it does not contain the game source tree or binary media. All candidate code/CI changes remain in local archives/patch. No Issue was closed, no release was published, and no commit was merged to `main`. Multiplayer Issues #14/#15/#22 stay open as deferred backlog.