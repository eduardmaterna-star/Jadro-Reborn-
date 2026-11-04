# JÁDRO REBORN — historie vývoje a code review

 > Převod dostupných podkladů z chatů **Coding** a **Code Review**, aktualizace 2026-11-04. Historické tvrzení „lokální test PASS“ není potvrzením, že aktuální soubor leží v GitHub `main`. Tento přehled **není** novým herním buildem.

## Aktuální stav

- Repo: [Jadro-Reborn-](https://github.com/eduardmaterna-star/Jadro-Reborn-).
- Nejnovější balíček doložený chaty: **v0.4.0-alpha.6 R1**, status **Alpha** (úplná hra na GitHubu zatím není). Podrobnosti: [UPDATES_2026-11-04.md](UPDATES_2026-11-04.md).
- [CURRENT_RELEASE.md](CURRENT_RELEASE.md) potvrzuje, že **úplné zdroje, binární assety ani Windows distribuční ZIP nejsou dosud nahrány do `main`**. PR #9 dodal release dokumentaci, nikoliv všechny soubory hry. Dokud nebude hotovo [#11](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/11), není správné považovat GitHub za kompletní zdroj hry.
- Neověřené: koncové testy Windows 10/11, reálná vícehráčská session přes internet, GPU telemetrie, CI pro aktuální úplnou verzi. **Neoznačovat Stable bez ověření.**

## Přehled dosavadních verzí a práce

| Verze/období | Historie Coding / Code Review | Status ověření |
|---|---|---|
| v0.3.12–v0.3.13 | Safe Exit: pozastavit hru, dokončit save, potvrdit ukončení; ochrana při selhání save, HTTP hlavičky a regresní testy. | Historické lokální výsledky. Neprokazuje Windows provoz v aktuální verzi. |
| v0.3.15–v0.3.16 | Review verzování, save/reset/migrace a WebGL viditelnosti postavy; připraven zdrojový hotfix generator, nikoli hotový Windows release. | Dokumentace [HOTFIX_V0316_README.md](HOTFIX_V0316_README.md), PR #1. |
| v0.3.18 | Návrh verzovaných GitHub Releases/Windows CI a kontrol assetů. | PR #3–#5: workflow není samo o sobě úplná hra. |
| v0.3.19–v0.3.22 | Nativní save/restore/reset/backup manager, rollback a regresní testy; review upozorňovalo na retenci záloh, blokování save při validaci a crash scénáře. | Část lokálních testů hlášena PASS; Windows end-to-end neověřeno. |
| v0.3.25–v0.3.31 | FPS/RAM/CPU/GPU panel, `/api/metrics`, stale stav, build/version kontrola a 24vzorkový benchmark. | U v0.3.31 24/24 lokálních benchmarků PASS; skutečné GPU/Windows testy NOT RUN. PR #8 obsahoval jen dokumentaci. |
| v0.4.0-alpha.1 | Multiplayer lobby / soukromé místnosti max. 4 hráčů. | Lobby místně testováno; v této iteraci nebylo hotové sdílené kopání. |
| v0.4.0-alpha.2 | V Coding popisováno serverem potvrzené kruhové kopání, sdílený terén, pohyb, oddělený inventář/peníze a reconnect. | Lokální testy; chyběla autoritativní fyzika a synchronizace některých technologií. |
| v0.4.0-alpha.3 | Požadavky na žebřík jen přes Space, trávu, umístění skal, viditelné entity, shadery a výkonový HUD. | Bez úplného aktuálního zdrojového stromu nepotvrzeno, že vše bylo zapracováno. |
| v0.4.0-alpha.4 | Hlasitější adaptivní hudba, animované listy, pomalejší počasí/plynulejší teplota; přenosný generátor, kabely, kýbl, pumpa a lokální průsaky. Malý online instalátor (nutný hosting kompletního ZIPu). | Podle [CHANGELOG_V0400_ALPHA4.md](CHANGELOG_V0400_ALPHA4.md); nové voda/energie **zatím nejsou synchronizované v multiplayeru**. |
| v0.4.0-alpha.5–alpha.6 | Stabilizace relací a ukládání, `save_request/save_result`, reconnect a opravy UI při chybné URL. | Dílčí lokální testy PASS; skutečný multiplayer/Windows NOT RUN. |
| v0.4.0-alpha.6 R1 | Nový lokální Windows balíček rozdělený do šesti částí; SOURCE ZIP podle Code Review 169 položek, 24 assetů. | Audit identifikoval P1 tokeny/online stav a nenapojené SFX; [podrobnosti](UPDATES_2026-11-04.md). |

## Původní požadavky na hru

Hra je o **kopání směrem k zemskému jádru**. Při změnách zachovat těžbu, fyziku terénu, inventář, obchod/prodej, ekonomiku, grafiku/zvuky a **kompatibilitu starých expedic**. V dřívějších návrzích se požadovala přírodnější zemina (ne pouze kostky), lokální kruhové odkopávání a ukryté rudy; později fyzické stánky ve světě místo duplicitních tlačítek v horním HUD.

## Evidence na GitHubu — aktuální priority

### P1 — před dalším stabilním vydáním
- [#11](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/11) Importovat všech 109 položek aktuálního zdrojového archivu a média.
- [#12](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/12) Podpora prerelease verzí v release workflow, přesné verze a CI.
- [#13](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/13) Windows 10/11 end-to-end testy a instalační scénáře.
- [#14](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/14) Multiplayer synchronizace energie/vody a serverová autorita.
- [#15](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/15) Internetový test 2–4 hráčů, reconnect a WebSocket zátěž.
- [#16](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/16) Ukládání, migrace, rollback/reset a zálohy.

### Další otevřená práce
- [#10](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/10): UI hotfix „PRODEJ“, odstranění horních Obchod/Prodej a titulu. **Lokálně připraveno**, úplné herní soubory a Windows vizuální test v repozitáři dosud nejsou.
- [#17](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/17) (P2): FPS/RAM/CPU/GPU, skutečné `/api/metrics`, 24 vzorků a testy stale stavu.
- [#18](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/18) (P2): shadery, viditelnost postavy, vegetace, žebřík, culling a vizuální kontrola.
- [#19](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/19) (P2): online instalátor, ověřený Windows ZIP, hash, bezpečný upgrade a dostupnost hostingu.
- [#20](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/20) (P3): THE DESCENT intro; [PR #2](https://github.com/eduardmaterna-star/Jadro-Reborn-/pull/2) je pouze 12s prototyp, nikoli hotové 60s video.

### Nová evidence z 4. 11. 2026
- [#22](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/22): P1 tokeny multiplayerových relací a `already_online`.
- [#23](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/23): P1 chybějící vazba herních zvuků.
- [#24](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/24): P2 řízení OGG a oddělené hlasitosti.
- [#25](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/25): P2 výkon `renderChunk` a textur.

## Dohodnutý proces pro Coding a Code Review

1. **Coding**: nová funkce / oprava → nová větev, změny verzovat, zachovat staré savy; neoznačovat opravu jako nahranou bez skutečného commitu.
2. **Code Review**: zkontrolovat kód, závažnost P1/P2/P3, reprodukci, testy a nesrovnalosti; evidovat na Issues, bez duplicit.
3. **Testování**: rozlišovat **PASS / FAIL / NOT RUN** a jednotkové testy vs. skutečné Windows 10/11 + multiplayer internet.
4. **GitHub**: přidat číslo verze, changelog, zdroje, assety, artefakty a SHA-256; až pak vydat tag/release. Staré tagy ani uložené expedice nepřepisovat.
5. **Uzavření Issue**: až když je oprava v repozitáři, propojena s commitem/PR a ověřená odpovídajícím testem.

## Omezení tohoto přenosu
Podklady tvoří dostupná historie obou chatů, existující GitHub dokumentace a PR/Issues; nejde o úplný audit všech původních lokálních ZIPů. Historické opravy není správné znovu vykazovat jako aktuální regresi bez reprodukce. Úplné soubory hry na GitHub nelze nahradit tímto dokumentem.
