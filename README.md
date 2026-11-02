# JÁDRO REBORN ⛏️

Hra o postupném kopání do hlubin Země s terénem, surovinami, obchodem, fyzikou a výpravami. Projekt se rozvíjí v chatech **Coding** (implementace) a **Code Review** (kontrola a opravy).

## Stav projektu — 2. listopadu 2026

**Poslední zdokumentovaná verze:** `v0.4.0-alpha.4` · **Alpha / vývojová**, **ne Stable**.

⚠️ **Repozitář zatím neobsahuje úplný zdrojový strom současné hry, všechna média ani kompletní Windows vydání.** Release dokumentace je na GitHubu, ale funkční distribuční hra z tohoto `main` zatím není ověřena. Viz [Issue #11](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/11) a [aktuální stav vydání](CURRENT_RELEASE.md).

**Co popisuje poslední verze:** adaptivní hudba, pohyblivé listy, plynulejší počasí a teplota, přenosný generátor, kabely, kýbl, pumpa a počáteční průsaky vody; multiplayer max. 4 hráči je ve vývoji. Nové funkce vody a energie zatím nejsou synchronizované mezi hráči.

## Přehled a dokumentace

| Oblast | Odkaz |
|---|---|
| Historie Coding + Code Review a úkoly | [DEVELOPMENT_HISTORY.md](DEVELOPMENT_HISTORY.md) |
| Stav posledního vydání | [CURRENT_RELEASE.md](CURRENT_RELEASE.md) |
| Změny alpha.4 | [CHANGELOG_V0400_ALPHA4.md](CHANGELOG_V0400_ALPHA4.md) |
| Pravidla sestavení / vydávání | [GAME_RELEASES.md](GAME_RELEASES.md) |
| Původní hotfix v0.3.16 | [HOTFIX_V0316_README.md](HOTFIX_V0316_README.md) |
| Všechny úkoly, chyby a návrhy | [GitHub Issues](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues) |
| Pull requesty / kontrola změn | [GitHub Pull Requests](https://github.com/eduardmaterna-star/Jadro-Reborn-/pulls) |

## Priority vývoje

- **P1 — před Stable:** [zdroje a média #11](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/11), [release CI #12](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/12), [Windows QA #13](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/13), [multiplayer synchronizace #14](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/14), [síťové testy #15](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/15), [save a obnova #16](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/16).
- **P2 — další ověření a zlepšení:** [výkon a telemetrie #17](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/17), [grafika #18](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/18), [online instalátor #19](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/19).
- **P3 — budoucí obsah:** [filmové intro #20](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/20).
- **Původní UI úprava:** [#10](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/10) má lokální opravu, ale zatím ne ověřené kompletní herní soubory na GitHubu.

## Pravidla pro Coding / Code Review

1. Nový model hry: zvýšit verzi, zapsat změny, nahrát **skutečné soubory hry a média**, uvést SHA-256 a link na commit/PR.
2. Review: každému problému přiřadit P1/P2/P3; připojit kroky pro reprodukci, akceptační kritéria a výsledky **PASS/FAIL/NOT RUN**.
3. **Nemažte ani nepřepisujte starší vydání nebo uložené expedice.** Zachovat terén/kopání, ekonomiku, inventář, obchod, fyziku i zvuky, pokud se změna netýká výslovně těchto mechanik.
4. Issue neuzavírat pouze na základě tvrzení „opraveno v chatu“; vyžaduje ověřenou opravu v repozitáři a odpovídající test.
5. Označení **Stable** až po testech skutečné aplikace na Windows 10/11 a při relevantních změnách i testech multiplayeru.

Tento repozitář obsahuje kód, částečnou dokumentaci a historii vývoje; **nepředstírá kompletní veřejný build alpha.4**.
