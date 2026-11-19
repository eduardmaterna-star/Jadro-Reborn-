# Lokální review zdrojového archivu alpha.6 R1 — kandidát R2

Datum: 2026-11-19

## Zdroj
Uživatel dodal `JADRO_REBORN_V0400_ALPHA6_R1_SOURCE.zip`.

- 169 původních položek, 36.8 MB.
- ZIP CRC PASS; bez duplicitních cest, traversal cest a symlinků.
- SHA-256 uploadu: `1f7ef0f2c4b38d2f06ad602c821ef3ccc5af8d7b13cd5e37ec07c47e303b4453`.
- Všech 24 původních assetů odpovídá `ASSET_SHA256.json`.
- Starý `ZDROJE_MANIFEST_SHA256.json` má 29/89 hashů neodpovídajících aktuálním souborům; revidovaný archiv proto obsahuje nový úplný `SOURCE_ARCHIVE_MANIFEST.json`.

## Lokální opravy připravené v kandidátním R2 archivu

- **#16 Save/backup:** nanosekundové timestampy nových záloh, kompatibilita se starým názvem, regresní test. Kritické testy pořadí záloh pod race detektorem prošly 30×.
- **#23 Audio SFX:** zapojení WAV efektů dig/buy/sell/ladder/wind, audio pool a throttling.
- **#24 Sound Engine:** samostatné hlasitosti Music / SFX / Ambient, ukládané v nastavení.
- **#25 Renderer:** odstranění dvou nepoužitých výpočtů z per-pixel hot path; přidán statický regresní test. FPS zlepšení nebylo změřeno.
- **#10 UI:** stávající regresní test PASS.
- Test runner nyní spouští Node testy pro #10, #23 a #25.

## Testy

`python scripts/run_release_tests.py local`: **12/12 PASS** (verze, assety, JS syntax, metrics, UI #10, audio #23, renderer #25, Python 11 testů, Go unit, vet a race).

Dále:
- native hybrid integration: PASS;
- Go build Linux amd64: PASS;
- Go cross-build Windows amd64: PASS;
- Go cross-build macOS amd64 a arm64: PASS;
- zdrojový patch `ALPHA6_R2_REVIEWED_FIXES.patch` se aplikuje na čistou extrakci původního archivu: PASS.

## Omezení / NOT RUN

- Windows 11, Linux a macOS GUI/runtime/audio testy: NOT RUN.
- FPS/GPU profiling: NOT RUN.
- Browser suite nedoběhla; starý `test_alpha4_browser.py` navíc čeká na odstraněný selector `#quickShop`.
- Telemetry benchmark timeout v tomto prostředí.
- Release build, installer a GitHub Actions release: NOT RUN.

## Důležité

Tento PR přidává pouze auditní dokumentaci. Zdrojový kód ani binární assety z lokálního ZIPu **nejsou tímto PR importovány** do GitHub `main`. Žádné Issues se nezavírají a žádný release se nevydává. Kandidátní revidovaný ZIP je samostatný lokální výstup.
