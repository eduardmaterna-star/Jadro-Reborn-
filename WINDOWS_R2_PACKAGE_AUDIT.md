# Audit samostatného Windows R2 balíčku

Datum: 2026-11-19  
Soubor: `JADRO_REBORN_ALPHA6_R2_WINDOWS.zip`  
Velikost: 41,779,647 bytes  
SHA-256: `b6b87ccb77d951d537cd08fffaa1cfe3ad899a544a90aa4afcb8dd2d80a0c532`

## Integrita a obsah
- ZIP test: PASS; 3 položky, bez CRC chyby.
- `JadroReborn-v0.4.0-alpha.6-Windows-x64.exe`: 43,137,024 bytes; SHA-256 `b8e731688b171ae458221f07cb8d990d9e2405de3f52df6a2b7fa6c9c76a63d1`.
- `JadroReborn-Server-v0.4.0-alpha.6-Windows-x64.exe`: 6,259,712 bytes; SHA-256 `fe3727ba8ccd13f5e15eabfdfd2d7091f21ffc6b683bd1d0154f42bb0d12b693`.
- `ISSUES_FIXES_ALPHA6_R2.md`: 2,840 bytes; SHA-256 `2e98bf155cf0e96c222ffdb6c6e07f2f83355dce57d0e45770772a7d8a1f0691`.
- Oba EXE jsou PE32+ pro Windows AMD64. Go build metadata: `go1.23.2`, `GOOS=windows`, `GOARCH=amd64`, `CGO_ENABLED=0`, `GOAMD64=v1`.

## Provenance a omezení

Tento balíček obsahuje binárky a issue report, nikoli zdrojový kód. Build metadata neobsahují identifikátor VCS commitu, kterým by bylo možné tyto binárky svázat s revidovaným source ZIPem. Přiložený report uvádí také multiplayer Issue #22; multiplayer je v aktuálně potvrzeném rozsahu vývoje odložen. Tento Windows balíček se proto vede samostatně a jeho multiplayerové změny se nepřebírají do singleplayerového R2 kandidáta.

Windows runtime, grafika, audio, podpis, installer, upgrade a skutečný HW výkon nebyly v tomto prostředí testovány. Balíček není publikovaným GitHub Release assetem.