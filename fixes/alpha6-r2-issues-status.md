# Alpha.6 R2 — Issues #22, #23, #24, #25 (staging)

This documents a **locally tested SOURCE archive**, derived from the 169-file alpha.6 R1 SOURCE. The full changed source tree and all original 24 binary media assets are **not yet present in the GitHub branch**. The matching complete alpha.6 R2 SOURCE/Windows ZIP archives are available as conversation attachments, not as GitHub release assets.

## Implemented locally

- **#22**: Per-server/per-room session token registry (sessionStorage, maximum 24 sessions, v1 migration), correct join token, terminal `already_online` / handshake rejection resets `active`, `canAct`, lobby controls, and world bridge. Regression browser test switches between two rooms and simulates rejection.
- **#23**: Five WAV effects (dig, ladder, buy, sell, wind) added to existing gameplay; per-effect voice pool/cooldown and browser autoplay handling. Multiplayer buy/sell only play when an authoritative new `trade_result` message indicates success. Added server test for success vs rejected purchase.
- **#24 (partial)**: Independent persisted music/SFX/ambient volume sliders. OGG mixing, long-term playback and Windows listening tests are pending.
- **#25 (partial)**: Remove genuinely unused `ratio(wy)` and `smoothNoise(wx,wy,160)` calculations from `renderChunk`. Full GPU profiling, fps benchmark, texture streaming and screenshot review are pending.
- Issue #10's existing UI fixes are preserved.

## Verification in the local Linux environment
- `go test ./... -count=1`: PASS
- `go test -race ./...`: PASS
- `go vet ./...`, `go mod verify`: PASS
- JavaScript syntax: PASS for game.js and multiplayer.js
- Node tests: 3/3 PASS
- Python unit tests: 11/11 PASS
- Chromium mock browser multiplayer tests: PASS, including new session isolation and audio integration tests
- Original assets: all 24 file sizes and SHA256 matched ASSET_SHA256.json
- Cross-compiled Windows x64 game and multiplayer server with Go **1.23.2**: PASS; this Go version is outdated.

## Known blockers
- Repo main is missing the entire game source and binary assets (#11), thus this branch only stages the verification and issue-specific tests; **do not merge/publish as a working release**.
- GitHub connector in this run can only write UTF-8 text files and cannot upload the necessary PNG/WAV/OGG binaries or release assets.
- Windows 10/11 runtime, GPU performance, real audio listening, internet WSS with 2–4 clients, Go upgrade: NOT RUN.
- Other issues (#14 water/power shared world, #19 public installer and #20 cinematic integration) remain unfinished.

## Local checksums
- R2 SOURCE SHA256: `f4ae929ca06f462066b705923f6c58599884ba0aa8f58f8586c6b002ca1e31c8`
- R2 WINDOWS SHA256: `b6b87ccb77d951d537cd08fffaa1cfe3ad899a544a90aa4afcb8dd2d80a0c532`
- R2 code-only ZIP SHA256: `44c0ea84cb6dddf2b22babd09b550011bf5a836e473df4065b2264b50cdd3084`

All issues remain open until their full acceptance criteria and on-GitHub implementation are verified.
