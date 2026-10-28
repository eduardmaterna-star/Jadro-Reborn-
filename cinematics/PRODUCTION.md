# JÁDRO REBORN — THE DESCENT
## Produkční podklady, verze 0.1 (28. 10. 2026)

**Záměr:** 60sekundový filmový úvod s fotorealistickou 3D grafikou, originální epickou hudbou, zvukovými efekty a českým vypravěčem. Spouští se **jen při nové expedici**. Klávesa **Esc** přeskočí intro a pokračuje do hry.

**Aktuálně dodáno:** skutečně naprogramovaná offline HTML/Canvas2D sekvence Země 0–12 s, základní syntetický ambient a pokus o český hlas přes systémové Web Speech API. **Nejde zatím o finální fotorealistický 3D render ani profesionální dabing.** Finální hudba, dabing a zbývající 3D záběry se musí vyrobit samostatně.

### Technické parametry finálního videa
- Obraz: 1920×1080, 16:9, 30 FPS (alternativně 60 FPS)
- Střih: 60,0 s; H.264 MP4, sRGB/Rec.709; přehrávání v HTML5 `<video>`
- Zvuk: 48 kHz stereo, AAC v MP4; samostatné WAV stopy 48 kHz/24-bit pro mix
- Cílová hlasitost: cca -16 LUFS integrovaně, true peak pod -1 dBTP
- Jazyk: čeština, titulky dostupné i při vypnutém zvuku
- Optimalizace: lokální soubor v balíčku hry, bez streamování z internetu
- Volitelné: 720p náhradní soubor pro režim Potato

### Časová osa a režijní plán
| Čas | Scéna | Kamera a světlo | Zvuk / český vypravěč |
|---|---|---|---|
| 00–12 | Země z vesmíru | Široký 3D záběr, pomalý přílet, atmosférický okraj, východ slunce | Hluboký ambient, smyčce. „Po miliony let ukrývala Země tajemství hluboko pod svým povrchem.“ |
| 12–22 | Pod zemskou kůrou | Filmový průlet geologickými vrstvami a jeskyněmi; volumetrický prach | „Místa, kam se člověk nikdy neodvážil proniknout.“ |
| 22–35 | Těžební základna | Ranní mlha, reflektory, detail helmy a rukavic; příprava na sestup | Rozjezd strojů. „Dnes však začíná expedice, která změní všechno.“ |
| 35–49 | Sestup | Kamera za průzkumníkem, čelovka, tmavé tunely a žhnoucí horniny | Rostoucí rytmus. „Každý metr hlouběji znamená větší nebezpečí. Ale také větší objevy.“ |
| 49–56 | Cíl | Obrovská žhavá komora, tepelné zkreslení, krátké ztišení před vyvrcholením | „Cíl je jediný. Dostat se až k samotnému jádru.“ |
| 56–60 | Logo | Černý kámen, praskliny s oranžovým světlem, logo JÁDRO REBORN | Orchestrální úder. „JÁDRO REBORN.“ |

### Zadání pro první finální 3D scénu (00:00–00:12)
**Záběr:** Realistická Země viděná z oběžné dráhy. Kamera pomalu letí směrem k planetě. Noční polokoule se slabými světly měst přechází do ranního osvětlení. Detailní oblačnost, Rayleighův rozptyl v atmosféře, přirozené barevné podání, jemný film grain, žádný text vypálený do videa. Poslední 2 s lze použít pro přechod do geologického průletu.

**3D scéna:** Koule se satelitní texturou, samostatná vrstva oblačnosti, atmosférický shader, jedna směrová světelná složka (Slunce), pomalý pohyb kamery na spline, filmové motion blur a expozice. Použít legálně licencované mapové textury; licence uchovat v projektu.

**Negativní omezení:** Žádná kostkovaná planeta, Minecraft styl, nadměrný lens flare, nerealistické kontinenty, text v obraze, trhavý zoom nebo výrazné rozostření planety.

**Přechod:** V 00:10–00:12 přibližování atmosférou; další scéna začíná geologickým řezem. Střih a zvuk se mají překrýt alespoň 0,5 s.

### Sound design
- 00:00: hluboký nízkofrekvenční drone a slabý vítr.
- 00:02: první replika vypravěče, střídmé smyčce.
- 00:08: nástup smyčců a sub-bass pulsu.
- 00:12: krátký přechodový whoosh.
- 00:22: těžební mechanika, relé a elektrické světlo.
- 00:35: rytmické údery synchronizované se sestupem.
- 00:49: velký sub-bass hit, pak krátké ztišení.
- 00:56: finální hudební akord a logo impact.
- Hudba musí být originální nebo řádně licencovaná, nikoli převzatá z existujícího filmového soundtracku.

### Organizace souborů pro finální render
```
cinematics/
  preview-earth-12s.html       # fungující první interaktivní prototyp
  intro-integration.js         # volitelná integrace do nové expedice
  PRODUCTION.md                # tento plán
  renders/
    shot01_earth_00-12.mp4
    shot02_geology_12-22.mp4
    shot03_base_22-35.mp4
    shot04_descent_35-49.mp4
    shot05_core_49-56.mp4
    shot06_logo_56-60.mp4
  audio/
    voiceover_cs.wav
    music_original.wav
    effects.wav
  intro.mp4                    # finální export; zatím NEEXISTUJE
```

### Integrace do skutečné hry
1. Přenést `preview-earth-12s.html` a `intro-integration.js` do `launcher/web/cinematics/`.
2. Přidat do `launcher/web/index.html` `<script src="cinematics/intro-integration.js" defer></script>`.
3. **Pouze** ve skutečném obslužném kódu tlačítka „Nová expedice“, **před** resetem a uložením staré expedice, zavolat `await window.JadroCinematics.playNewExpeditionIntro();`.
4. Teprve po návratu Promise pokračovat stávající, otestovanou logikou založení nové expedice. Esc znamená „přeskočit film“, **ne** „zrušit novou expedici“.
5. Nikdy nepřipojovat tento kód ke startu aplikace, tlačítku „Pokračovat“ nebo automatickému načtení pozice.
6. Po dokončení finálního videa vyměnit prototyp za lokální HTML5 video; zachovat stejné API pro dokončení/přeskočení.

### Testovací scénáře před nasazením
- Nová expedice: intro se otevře a po dokončení začne nová hra.
- Esc v sekundě 0, 5 a 11: intro zmizí a nová hra se zahájí právě jednou.
- „Pokračovat“: intro se vůbec neotevře.
- Opakované založení nové expedice: intro se přehraje znovu.
- Chybějící český systémový hlas: zobrazují se titulky, hra funguje.
- Vypnutý zvuk / režim Potato: film lze dokončit i přeskočit.
- Původní uložená pozice se nepřepisuje **před** potvrzeným zahájením nové expedice.

### Známá omezení prototypu
- Vizuál je procedurální 2D Canvas aproximace Země, nikoli filmový 3D render.
- Ambient jsou jednoduché generované tóny, ne finální epická hudba.
- Web Speech API může použít jiný hlas nebo nemusí mít češtinu.
- Prototyp má 12 sekund; zbývajících 48 sekund ještě není animováno.
- Prohlížeč může omezovat automatické spuštění zvuku; proto prototyp obsahuje tlačítko Spustit.
- Integrace je připravená jako samostatný modul, ale dosud nebyla zapojena do skutečného `game.js` ani otestována na Windows.
