# JÁDRO REBORN — alpha.6 R2 review candidate QA

Datum: 2026-11-19. Aplikační verze zůstává `0.4.0-alpha.6`; R2 je revize lokálního source candidate, nikoli publikované nové herní verze.

## Opravy
- **#16 Save/backup:** nanosekundové názvy nových záloh, kompatibilita se starými názvy, race regression test 30×.
- **#23 SFX:** dig/buy/sell/ladder/wind, pool a cooldown, nezahajovat SFX při skryté stránce.
- **#24 Sound Engine:** samostatné Music/SFX/Ambient volumes; hloubkový mix má nejvýše dvě sousední OGG vrstvy, neaktivní se po fade-out pozastaví, audio se pozastaví při skrytí okna a obnovuje s autoplay retry.
- **#25 Renderer:** odstraněny dva nepotřebné výpočty z per-pixel hot path; bez FPS before/after měření netvrdíme výkonový nárůst.
- **#19 Installer:** opraven alpha.4 → alpha.6 changelog allowlist, přidán regresní Go test.
- **#10 UI:** browser smoke test nyní potvrzuje nákup v obchodě i prodej ve fyzické výkupně (E), připsání peněz a vyprázdnění batohu.
- **Packaging:** čistý source selection, SOURCE manifest, žádné test logy/cache/EXE ve SOURCE ZIP.
- **CI candidate:** Windows x64, Linux x64, macOS amd64/arm64; read-only permissions; Go 1.27.4 v aktivních workflow.

## Lokální QA — PASS
- `python scripts/run_release_tests.py local`: **13/13 PASS**.
- Python unittest: **18/18 PASS**.
- Node regressions #10/#23/#24/#25: PASS.
- Go unit, race, vet, mod verify: PASS.
- Installer Go tests: **3/3 PASS**.
- Chromium hybrid, alpha4 gameplay/audio/shop/sale smoke, backup v0.3.22/v0.3.23, review v0.3.21, metrics: PASS.
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
| Reviewed R2 source ZIP (133 entries) | 36,858,109 B | `297a6596e7051e8467019795f500e69eff97695ca1062e33c60e4990eae436f8` |
| R1→R2 patch (24 files) | 84,685 B | `88e3832f4755ac1f2d653387cb4acc18f79609804d53424be6ec15304af9f1ec` |
| Windows ZIP | 41,819,473 B | `726bd551c052c6ba885bf1650bc820d7cec21cb5c96e6466dc31d067552d8d73` |
| SOURCE ZIP | 36,829,720 B | `b58929332982865cde50e1b1238d835911f58012ac51d7d3b39089516e5c8439` |
| COMPLETE ZIP | 81,049,441 B | `ea95b9dfd70fffbab8a6c59faf128b36dee2c71d96cbd35f3c0dcc5217133fa4` |
| Online installer | 5,614,592 B | `5bb6100944c08a5402c5ab22f487055c38fcf02989761745ec9bd2ca6c12a754` |

## NOT RUN / omezení
- Windows 11, Linux, macOS desktop GUI/runtime a skutečný audio výstup: NOT RUN.
- WebGL2/GPU profiling, renderer before/after performance: NOT RUN.
- Go 1.27.4 nebyl lokálně dostupný; lokální builds použily Go 1.23.2.
- Windows native installer run, Authenticode signing, public hosting and GitHub release publication: NOT RUN.
- GitHub Actions has not run the game build matrix against a complete checked-in game source; the source tree and binary assets remain absent from `main`.
- Separate Windows R2 EXE bundle lacks matching VCS commit provenance and includes deferred multiplayer #22; not merged into this singleplayer candidate.

## Repository status
PR #30 is documentation only; it does not contain the game source tree or binary media. All candidate code/CI changes remain in local archives/patch. No Issue was closed, no release was published, and no commit was merged to `main`. Multiplayer Issues #14/#15/#22 stay open as deferred backlog.