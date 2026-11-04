# JÁDRO REBORN — stav verzí k 4. 11. 2026

**Nejnovější verze doložená chaty Coding a Code Review:** `v0.4.0-alpha.6 R1` — **Alpha, ne Stable**.

**Nejnovější release dokumentace dříve dostupná na GitHub main:** `v0.4.0-alpha.4`. Repo dosud **neobsahuje úplnou hru alpha.6 R1, všechny binární assety ani spustitelný Windows balíček**. Tento update je pouze dokumentační — žádný nový herní EXE ani GitHub Release nebyl zveřejněn.

## Co je nového od alpha.4

- **Alpha.5:** stabilizace serverových stavů, save/backup, rate-limit, reconnect, sjednocení verzí a vypínání serveru.
- **Alpha.6:** potvrzování multiplayerového save (`save_request/save_result`, `requestId`), oprava tlačítek po chybné URL, reconnect a `world_ready`.
- **Alpha.6 R1:** aktualizovaný Windows balíček v šesti částech pro lokální spojení a samostatně analyzovaný source ZIP s 169 položkami, 24 mediálních assetů. Zdrojový ZIP nebyl v tomto chatu dostupný k uploadu.

## Otevřené P1 chyby

- [#22](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/22) — obnovovací tokeny expedic a `already_online` při odpojeném WebSocketu.
- [#23](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/23) — existující SFX `dig/buy/sell/ladder/wind` nejsou spouštěny herním JS.
- [#11](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/11) — chybějící úplné aktuální zdroje/asset balíček v GitHubu.
- [#12](https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/12) — neověřená release pipeline; rozpracovaný [PR #21](https://github.com/eduardmaterna-star/Jadro-Reborn-/pull/21).

## Ověření

Dle konverzací lokální kontroly ZIP, 24 mediálních assetů a vybrané automatické testy byly PASS. **Reálné Windows 10/11, 2–4 hráči přes internet, aktualizované GitHub CI a kompletní alfa build z GitHub main jsou NOT RUN / NOT VERIFIED.** Code Review upozornilo na Go sestavení 1.23.2 oproti deklaraci 1.27.3.

Podrobný záznam: [UPDATES_2026-11-04.md](UPDATES_2026-11-04.md). Starší historická dokumentace alpha.4: [CHANGELOG_V0400_ALPHA4.md](CHANGELOG_V0400_ALPHA4.md).

## Původní alpha.4 kontrolní součty (archivní, NE alpha.6 R1)

Zdrojový ZIP SHA-256: `2eed9062b2087951eff91c6fb040bfdb51146cdf0fe9bbb594b1e17e76501aee`

Windows ZIP SHA-256: `5bcf16ba8ebf604e575df423d6be97f0138bff89f974cd3e00bef719ef910171`

**Nezaměňovat tyto hashe za balíček alpha.6 R1.**