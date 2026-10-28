# Vydávání verzí JÁDRO REBORN na GitHubu

Každá dokončená verze hry se publikuje samostatně pod tagem `vMAJOR.MINOR.PATCH`, například `v0.3.18` nebo `v0.3.19`. Starší tagy a vydání se nemažou ani nepřepisují.

## Obsah vydání
- Zdrojové soubory (`launcher/`, `scripts/`, `tests/`, herní grafika a zvuky).
- Spustitelný balíček pro Windows x64.
- Zdrojový ZIP archiv konkrétní verze.
- SHA-256 součty obou ZIPů.
- Popis změn a skutečných výsledků testů, včetně neověřených scénářů.

## Postup
1. Nahrát kompletní aktuální zdrojovou verzi hry do repozitáře. **Tento repozitář zatím obsahuje hlavně filmové nástroje a starší opravy, ne úplný herní projekt v0.3.18.**
2. Ověřit `node --check launcher/web/game.js`, `python -m unittest discover -s tests -v`, `go test ./...` a `go vet ./...` ve složce `launcher`.
3. Změnit číslo verze v kódu a dokumentaci, provést code review a uložit commit.
4. Vytvořit nový tag na ověřeném commitu, například `git tag v0.3.19` a `git push origin v0.3.19`.
5. Workflow `.github/workflows/release-game.yml` spustí kontroly, sestaví EXE a vydá GitHub Release s dvěma ZIPy a SHA-256.
6. Nechat otevřené poznámky k omezením, pokud nebylo možné ověřit hru na skutečném Windows počítači.

**Pozor:** Publikace samotného postupu neznamená, že zdroje, Windows EXE nebo ZIP v0.3.18 už byly nahrány. Nejprve je nutné doplnit herní soubory z ověřeného zdrojového archivu. Staré soubory `cinematics/` a `tools/` zůstávají nedotčené.

Workflow lze testovat také ručně přes Actions → Game release → Run workflow (takový běh pouze nahraje testovací artefakty a nevytvoří veřejné vydání).
