# JÁDRO REBORN — QA report alpha.6 R2 review candidate

Datum auditu: 2026-11-19  
Aplikační verze: `0.4.0-alpha.6`  
Zdrojová revize: lokální kandidát R2, odvozený z dodaného zdrojového archivu R1.

## 1. Integrita zdrojů

- Původní upload `JADRO_REBORN_V0400_ALPHA6_R1_SOURCE.zip`: 36,818,565 bytes; SHA-256 `1f7ef0f2c4b38d2f06ad602c821ef3ccc5af8d7b13cd5e37ec07c47e303b4453`.
- Revidovaný ZIP: 175 položek včetně manifestu; ZIP CRC PASS.
- `SOURCE_ARCHIVE_MANIFEST.json`: 174 souborů, **0 chybějících souborů a 0 nesouladů SHA-256/velikosti**.
- Všech 24 původních assetů odpovídá `ASSET_SHA256.json`.
- Starý `ZDROJE_MANIFEST_SHA256.json` má 29 z 89 historických hashů odlišných od aktuálního archivu. Zůstal zachován jako historický podklad; pro R2 je přidán nový úplný manifest.
- Patch se aplikuje na čistou extrakci R1: PASS; obsah upravených souborů po aplikaci odpovídá revidovanému stromu.
- Revidovaný source ZIP SHA-256: `b25509f4dfdfbaaa760cbe3b9688f1cd5d91dfa9cebe29489f530562bb5f53db`.
- Patch SHA-256: `f6be6b6bb37a2d292c5af8db9b8795cbe7d9d38dc45ee98d79a79d9e61fa7912`.

## 2. Lokální změny v kandidátu R2

- **#16 Save/backup:** nanosekundová časová značka nových záloh, kompatibilita se starým názvem, regresní test; opakované testy pořadí při shodném mtime prošly 30× pod race detektorem.
- **#23 SFX:** propojení `dig`, `buy`, `sell`, `ladder`, `wind`; pool hlasů, cooldown a ošetření chyb audio přehrávání.
- **#24 Audio settings:** samostatná a perzistentní hlasitost Music / SFX / Ambient. Nejde o kompletní revizi normalizace všech OGG přechodů.
- **#25 Renderer:** odstranění dvou skutečně nepoužitých výpočtů z per-pixel `renderChunk()`; bez měření se netvrdí FPS zlepšení.
- **#10 UI:** regresní test UI zůstává součástí test runneru.
- **Browser test harness:** `tests/test_alpha4_browser.py` čekal na odstraněné `#quickShop`. Test byl opraven tak, aby otevřel obchod aktuálním způsobem — přes fyzickou stanici a klávesu E. Hra kvůli tomu měněna nebyla.

## 3. Automatické testy — PASS

- `python scripts/run_release_tests.py local`: **12/12 PASS** (opakováno po posledních úpravách).
- `go mod verify`: PASS.
- `go test ./... -count=1`: PASS.
- `go test -race ./... -count=1`: PASS.
- `go vet ./...`: PASS.
- `node --check launcher/web/game.js` a `node --check launcher/web/multiplayer.js`: PASS.
- Python unit tests: 11/11 PASS.
- `tests/test_issue10_ui.cjs`, `tests/test_issue23_sfx.cjs`, `tests/test_issue25_render_hotpath.cjs`: PASS.
- Chromium `test_hybrid_browser.py`: PASS.
- Chromium `test_review_v0321.py`: PASS.
- Chromium `test_backup_v0322.py`: PASS.
- Chromium `test_backup_v0323.py`: PASS.
- Chromium `test_metrics_browser.py`: PASS.
- Chromium `test_alpha4_browser.py`: PASS po opravě zastaralého selektoru v testu.
- Chromium `test_visual_alpha3_browser.py`: PASS; samotný WebGL2 GPU kontext nebyl v tomto prostředí dostupný, test pokračoval v Canvas2D fallbacku.
- Native hybrid integration (`test_hybrid_native.py`): PASS; při zavírání browser contextu se objevila nefatální Playwright `TargetClosedError` varování.
- Go build Linux amd64: PASS.
- Go cross-build Windows amd64: PASS.
- Go cross-build macOS amd64 a arm64: PASS.
- `verify_game_sources.py`: PASS — 31 povinných cest a odkazovaných assetů ověřeno.

## 4. Headless telemetry benchmark — 24/24 vzorků

Čtyři grafické presety × overlay výkonu zapnutý/vypnutý × tři vzorky po 1,6 s. Měření bylo kvůli limitu běhového prostředí rozděleno do dvou navazujících běhů; všechny kombinace mají tři vzorky.

| Preset | Overlay vypnutý — median RAF FPS | Overlay zapnutý — median RAF FPS |
|---|---:|---:|
| Potato | 60.0 | 59.2 |
| Low | 60.3 | 59.6 |
| Medium | 48.0 | 49.6 |
| High | 41.2 | 41.9 |

Výsledky jsou pouze headless Linux Chromium `requestAnimationFrame` a DevTools Performance metriky. Nejde o skutečné Windows FPS, GPU utilization, ani přímé srovnání před/po optimalizaci `renderChunk()`. Jsou uvedené jako orientační měření testovacího prostředí, ne jako výkonová garance. Souhrn a jednotlivé sample jsou přiložené jako QA artefakt v lokálních výstupech.

## 5. Samostatný Windows R2 balíček — oddělená identita

Dodaný `JADRO_REBORN_ALPHA6_R2_WINDOWS.zip` má SHA-256 `b6b87ccb77d951d537cd08fffaa1cfe3ad899a544a90aa4afcb8dd2d80a0c532`, ZIP CRC PASS a tři položky: Windows klient, dedikovaný server a `ISSUES_FIXES_ALPHA6_R2.md`.

- Klient PE32+ Windows AMD64, Go `1.23.2`, `CGO_ENABLED=0`; SHA-256 `b8e731688b171ae458221f07cb8d990d9e2405de3f52df6a2b7fa6c9c76a63d1`.
- Server PE32+ Windows AMD64, Go `1.23.2`, `CGO_ENABLED=0`; SHA-256 `fe3727ba8ccd13f5e15eabfdfd2d7091f21ffc6b683bd1d0154f42bb0d12b693`.
- Balíček obsahuje jen dvě `.exe` a report, nikoli úplný zdrojový strom nebo assety.
- Je to samostatný Windows artifact s multiplayerovým obsahem #22 v přiloženém reportu. Není prokázáno, že vznikl ze stejného zdrojového commitu jako tento singleplayerový R2 review ZIP. Multiplayerové změny proto nejsou převzaty do aktuálního singleplayer rozsahu.
- Windows runtime, UI, audio, podpis a reprodukovatelnost těchto binárek: NOT RUN.

## 6. NOT RUN / omezení

- Skutečné GUI/runtime/audio na Windows 11, Linux a macOS: NOT RUN.
- WebGL2 GPU kontext nebyl k dispozici; žádné reálné GPU profiling měření.
- FPS před/po renderer opravě, `texImage2D` profiling, dlouhodobý běh a reálný HW benchmark: NOT RUN.
- Instalátor, Authenticode podpis, signed release, GitHub release build: NOT RUN.
- Windows Go toolchain `1.27.3` z workflow nebyl lokálně dostupný; místní buildy použily Go `1.23.2`.
- Skutečná 2–4 hráčská WSS session a multiplayer regresní testy: mimo aktuální singleplayer rozsah.

## 7. Stav GitHubu

Tento report dokumentuje lokální review a testy. Revidovaný zdrojový strom a původní binární assety zatím nejsou importovány do GitHubu. PR #30 obsahuje dokumentaci, nikoli herní zdrojový kód. Lokální opravy proto nejsou součástí `main`; žádné Issue se nezavírá a žádný release se nevydává.