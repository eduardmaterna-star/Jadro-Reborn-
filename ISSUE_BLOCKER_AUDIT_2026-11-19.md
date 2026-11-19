# Stav otevřených issues — ověřeno 2026-11-19

Tento repozitář byl zkontrolován přes GitHub API včetně všech 12 existujících větví, hlavní větve, otevřených PR, release, workflow runů a dostupného stromu souborů.

## Kritický blokátor: kompletní herní zdrojový strom není dostupný na GitHubu

Na `main` je 24 položek; ve složce `launcher/` je pouze `go.mod`. Chybí zejména `launcher/main.go`, `launcher/web/game.js`, serverový zdrojový kód, původní PNG/WAV/OGG assety a testovací sada hry. Stejný problém je v R2 větvi PR #26, která přidává pouze tři textové soubory dokumentace/testů. Prohledány byly všechny aktuálně dostupné větve a GitHub Releases; jediný release `v0.3.6` nemá žádné assety. GitHub code search pro `game.js` nic nevrátil.

Bez těchto zdrojů nelze bezpečně implementovat ani spustit regresní testy herních issues #10, #14–#20 a #22–#25. Neuzavírat je na základě dokumentace či lokálních tvrzení.

## Konkrétní stav

- **#10 UI** — blokováno: chybí `game.js` a `index.html`; nelze upravit ani ověřit fyzické stánky.
- **#11 source/assets import** — blokováno: úplný zdrojový archiv není v dostupných GitHub branchech ani release assetech.
- **#12 release pipeline** — PR #21 podporuje alpha/beta/RC validaci, obsahuje 5 regresních testů a validační workflow má PASS; ale hlavní release workflow stále nemůže dokončit build kvůli chybějícím herním souborům. PR #21 zůstává draft.
- **#13 Windows QA** — NOT RUN: nejsou k dispozici úplné zdroje/balíček a zde nelze spustit Windows 10/11 GUI/GPU QA.
- **#14 multiplayer technologie a voda** — blokováno: chybí klient/server implementace.
- **#15 internet multiplayer 2–4 hráčů** — NOT RUN: žádná plná implementace/serverový zdrojový kód ani reálné internetové session.
- **#16 save/migrace/zálohy** — blokováno: chybí save zdrojový kód a historické fixture.
- **#17 telemetrie/benchmark** — blokováno: chybí aktuální hra, API a benchmarkový harness.
- **#18 grafika/žebřík/vegetace** — blokováno: chybí herní JS a assets; Windows visual QA NOT RUN.
- **#19 online instalátor/release balíček** — blokováno: release v0.3.6 má nulové assety, kompletní ověřený Windows ZIP není v dostupných releasech.
- **#20 THE DESCENT** — pouze samostatný 12s prototyp; dokumentace výslovně říká, že integrace do reálného tlačítka Nová expedice a Windows vizuální test nejsou provedeny. Není hotovo.
- **#22 session tokens/already_online** — PR #26 popisuje lokální opravu, ale změněný klient/server kód a plné testy nejsou v PR ani na main.
- **#23 SFX** — PR #26 uvádí lokální zapojení, ale WAV assety a herní obslužný kód nejsou na GitHubu; audio test není reprodukovatelný.
- **#24 Sound Engine** — jen textový popis částečných lokálních úprav; není ověřitelná implementace.
- **#25 renderer/GPU profiling** — testovací JS soubor v PR #26 závisí na chybějícím `launcher/web/game.js`; GPU profiling nebyl proveden.

## CI a PR

- PR #21: 5/5 lokálních Python testů hlášených v PR a GitHub validační workflows PASS; skutečný release workflow NOT RUN. Zůstává draft a neslučuje se.
- PR #26: draft, 3 textové soubory, nikoli kompletní implementace; neslučovat.
- Poslední workflow runs pro větve #21/#26 ověřují jen cinematic/hotfix patcher, ne celý game release.

## Co znamená „opraveno“

Issue lze zavřít až poté, co je skutečná implementace committnutá v GitHubu, příslušné automatické testy projdou a scénáře vyžadující Windows/GPU/audio/internet jsou zdokumentovány jako skutečně provedené. Tento audit žádné blokované issue nezavírá.

## Nejkratší cesta od blokace

Do repozitáře je třeba dostat kompletní zdrojový strom a assety odpovídající aktuálnímu R2 (ne jen Windows EXE). Poté lze provést implementaci #10, #14–#18 a #22–#25, napojit intro #20, upravit a spustit CI/release #12/#19 a následně udělat Windows QA #13.