# JÁDRO REBORN — potvrzený rozsah dalšího vývoje

Datum potvrzení: 2026-11-19  
Zdroj rozhodnutí: vyplněný uživatelský dotazník.

## Produktový rozsah

- Primární režim dalšího vývoje: **singleplayer**.
- Multiplayer se v této etapě aktivně nerozšiřuje. Existující multiplayerové Issues se nemažou ani automaticky nezavírají; zůstávají jako odložený backlog.
- Cílové platformy: **Windows 11, Linux a macOS**.
- Požadované oblasti práce: opravy otevřených Issues, nové funkce, code review, QA a optimalizace výkonu.
- Nová verze po každém větším, ověřeném balíku oprav.
- Změny se připravují ve větvích a Pull Requestech. Bez samostatného schválení se nic neslučuje do `main`.

## Pravidla kvality

1. Oprava musí být implementována ve zdrojovém kódu, ne pouze popsána v dokumentaci.
2. Každý PR uvádí testy jako PASS / FAIL / NOT RUN a přesný commit.
3. Issue se nezavírá bez implementace a odpovídajících ověřovacích důkazů.
4. Zachovat uložené expedice, ekonomiku, inventář, obchod a těžbu, pokud se změna netýká jejich chování.
5. Release nevydávat bez zdrojů, assetů, testů a reprodukovatelného buildu.
6. Windows 11, Linux a macOS jsou cílové platformy; podpora není ověřená, dokud neproběhnou runtime testy na daném OS.

## Potvrzená zdrojová verze

Uživatel dodal archiv `JADRO_REBORN_V0400_ALPHA6_R1_SOURCE.zip`. V jeho `launcher/main.go`, `ALPHA6_REVISION1_FIX.md` a README je doložena aplikace **v0.4.0-alpha.6**, revize zdrojového archivu **R1**. Starší `Coding.txt` (v0.3.15) a původní návrh (v0.3.13) jsou historické podklady, nikoli aktuální zdrojový build.

Původní upload SHA-256:
`1f7ef0f2c4b38d2f06ad602c821ef3ccc5af8d7b13cd5e37ec07c47e303b4453`

## Stav zdrojů a GitHubu

Zdrojový archiv byl lokálně ověřen: 169 původních položek, ZIP CRC PASS, 24 asset hashů PASS. Lokálně byly připraveny opravy záloh, zvuků a renderer hot-path; kompletní lokální sada po těchto změnách prošla. Revidovaný zdrojový ZIP a QA report jsou připravené jako samostatné výstupy.

**GitHub `main` stále nemá kompletní zdrojový strom.** Archiv zatím není importován do repozitáře, proto se lokální opravy nepovažují za GitHub implementaci a Issues zůstávají otevřené. PR #30 zaznamenává pouze audit a QA; herní zdrojový kód neimportuje.

## Další pořadí práce

1. Importovat revidovaný zdrojový archiv do GitHubu bez ztráty assetů a historie.
2. Potvrdit přesnou verzi pomocí manifestu, Git commitu a SHA-256.
3. Spustit CI a reprodukovatelné buildy.
4. Dokončit singleplayerové UI, ukládání, grafiku, zvuk, výkon a instalaci podle Issues.
5. Ověřit Windows 11, Linux a macOS včetně runtime/audio/GUI.
6. Připravit release až po úspěšném ověření cílových platforem.
