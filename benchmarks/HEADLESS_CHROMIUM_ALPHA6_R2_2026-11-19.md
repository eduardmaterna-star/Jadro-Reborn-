# Headless Chromium telemetry — alpha.6 R2 candidate

Datum: 2026-11-19  
Stav: 24/24 vzorků dokončeno.

Metodika: 4 grafické presety (Potato / Low / Medium / High) × overlay OFF/ON × 3 opakování, každé 1,6 s. Dva navazující headless Linux Chromium běhy; stejné lokální prostředí a browser config.

| Preset | Overlay | Median RAF FPS | Min | Max | Median renderer task CPU (s) |
|---|---:|---:|---:|---:|---:|
| Potato | OFF | 60.0 | 54.9 | 60.4 | 0.9613 |
| Potato | ON | 59.2 | 58.6 | 60.6 | 0.8913 |
| Low | OFF | 60.3 | 59.8 | 60.6 | 0.4138 |
| Low | ON | 59.6 | 59.4 | 60.3 | 0.4628 |
| Medium | OFF | 48.0 | 46.7 | 51.4 | 1.6581 |
| Medium | ON | 49.6 | 46.2 | 50.0 | 1.6618 |
| High | OFF | 41.2 | 38.7 | 42.7 | 1.6517 |
| High | ON | 41.9 | 40.6 | 42.3 | 1.6636 |

**Interpretace:** Toto je headless browser benchmark, nikoli měření fyzické GPU nebo skutečného FPS na Windows. Výsledky neizolují vliv optimalizace `renderChunk()` a nepodporují tvrzení o zlepšení výkonu po opravě. Skutečný GPU profiling, WebGL2 context a hardwarový before/after test zůstávají NOT RUN.