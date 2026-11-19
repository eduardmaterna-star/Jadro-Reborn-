# JÁDRO REBORN — potvrzený rozsah dalšího vývoje

Datum potvrzení: 2026-11-19  
Zdroj rozhodnutí: vyplněný uživatelský dotazník.

## Produktový rozsah

- Primární režim dalšího vývoje: **singleplayer**.
- Multiplayer se v této etapě aktivně nerozšiřuje. Existující multiplayerové Issues se nemažou ani automaticky nezavírají; zůstávají jako odložený backlog, dokud nebude rozhodnuto o návratu multiplayeru.
- Cílové platformy: **Windows 11, Linux a macOS**.
- Požadované oblasti práce: opravy všech otevřených Issues, nové funkce, code review, QA a optimalizace výkonu.
- Vydání nové verze po každém větším, ověřeném balíku oprav.
- Změny se připravují automaticky ve větvích a Pull Requestech. Bez samostatného schválení se nic neslučuje do `main`.

## Pravidla kvality

1. Každá oprava musí být skutečně implementována ve zdrojovém kódu, ne pouze popsána v dokumentaci.
2. Každý PR musí uvádět testy jako PASS / FAIL / NOT RUN a přesný commit.
3. Neuzavírat Issue bez odpovídající implementace a ověřovacích důkazů.
4. Zachovat existující uložené expedice, ekonomiku, inventář, obchod, těžbu a další funkce, pokud se konkrétní oprava netýká jejich změny.
5. Release nevydávat, pokud chybí potřebné zdroje, assety, testy nebo reprodukovatelný build.
6. Podpora Linuxu a macOS je cílový požadavek; nesmí být označena za ověřenou, dokud pro ni neproběhnou reálné buildy a testy.

## Stav verze — nutné rozlišení

Repozitář `CURRENT_RELEASE.md` uvádí jako nejnovější verzi doloženou historií Coding/Code Review `v0.4.0-alpha.6 R1`. Nahraný soubor `Coding.txt` uvádí `v0.3.15`, zatímco `Návrh hry do středu Země.txt` popisuje `v0.3.13`. Tyto záznamy si odporují a žádný z nich sám o sobě nedokládá aktuální spustitelný build na GitHubu. Verze proto zůstává **neověřená** do importu kompletního zdrojového balíčku a kontroly manifestu.

## Aktuální technický blokátor

Na `main` je dostupný `launcher/go.mod`, ale chybí `launcher/main.go` a `launcher/web/game.js`; bez nich nelze sestavit hru ani bezpečně implementovat a regresně ověřit většinu herních Issues. Tento PR je pouze záznamem potvrzeného rozsahu práce, nikoli opravou herního kódu.

## Další pořadí práce

1. Získat a importovat kompletní zdrojový archiv včetně assetů, testů a build skriptů.
2. Potvrdit přesnou verzi pomocí manifestu, Git commitu a SHA-256.
3. Provést audit zdrojů a reprodukovatelné buildy.
4. Opravit singleplayerové UI, ukládání, grafiku, zvuk, výkon a instalaci podle otevřených Issues.
5. Doplnit CI/build matrix pro Windows 11, Linux a macOS.
6. Připravit release až po úspěšném ověření cílových platforem.

