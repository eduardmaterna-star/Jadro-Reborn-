# Import checklist — complete JÁDRO REBORN source

Tento checklist je podmínkou pro odblokování issues, která vyžadují skutečný herní kód. Není to náhrada za zdrojový archiv.

## 1. Co dodat

Dodat úplný zdrojový archiv odpovídající přesně distribučnímu buildu R2. Samotné Windows EXE, changelog, screenshoty ani patch-generator nestačí.

Minimální soubory, které současná release pipeline přímo vyžaduje:

- `launcher/go.mod`
- `launcher/main.go`
- `launcher/web/game.js`
- `scripts/release_version.py`

Dále musí být přítomné všechny skutečně používané zdrojové soubory a závislosti projektu:

- další Go soubory a balíčky launcheru/serveru,
- kompletní webové UI, styly a lokální JavaScript moduly,
- obrázky, textury, fonty a další herní assety,
- WAV/OGG a další zvukové soubory,
- testy, fixture, migrační data a skripty sestavení/instalace,
- licence a notices pro assety a knihovny.

Názvy adresářů nad rámec cest uvedených výše se nesmí domýšlet; zachovat skutečnou strukturu originálního projektu.

## 2. Identita zdrojů a buildu

Přiložit `SOURCE_MANIFEST.md` obsahující:

- přesnou verzi hry a označení R2,
- Git commit, ze kterého zdroj vychází (pokud existuje),
- SHA-256 původního source ZIP,
- SHA-256 Windows klienta a serveru,
- seznam všech souborů v archivu, jejich velikosti a SHA-256,
- instrukce pro reprodukovatelné sestavení,
- seznam testů a skutečné výsledky PASS / FAIL / NOT RUN.

Zdrojový strom a Windows klient/server musí být prokazatelně ze stejného vydání. Pokud to nelze ověřit, označit původ jako neověřený.

## 3. Bezpečné předání

Preferovaný způsob je přiložit zdrojový ZIP jako GitHub Release asset nebo použít Git LFS pro velké binární assety. Samotné vložení ZIPu do běžného Git commitu není nutné.

Po uploadu:
1. stáhnout archiv z GitHubu a ověřit SHA-256,
2. ověřit integritu ZIPu a nepřítomnost duplicitních/absolutních cest či path traversal,
3. rozbalit do čistého pracovního adresáře,
4. ověřit přítomnost minimálních cest z release workflow,
5. porovnat manifest s obsahem a ověřit assety,
6. spustit testy a build bez změny původních souborů.

## 4. Co se nesmí udělat

- Nepřepisovat `main` obsahem, jehož původ není ověřen.
- Nepřepisovat ani znovu nepoužívat existující release tag.
- Neoznačovat issue jako hotové jen podle lokálního reportu.
- Nepublikovat nový Stable release bez Windows QA.
- Neodstraňovat ani nepřevádět legacy save data bez migračních testů.

## 5. Odblokování issues

Po úspěšném importu lze navázat:

- #10 UI a obchodní stánky,
- #12 release pipeline (PR #21 po rebase a plném CI),
- #13 Windows 10/11 QA,
- #14–#18 multiplayer, save, telemetrie a grafika,
- #19 distribuce/instalátor,
- #20 integrace intra,
- #22–#25 session, zvuk a renderer.

Každá oprava musí mít vlastní reprodukční test nebo přesně popsaný ruční test. Issue se zavře až po ověření skutečného buildu.
