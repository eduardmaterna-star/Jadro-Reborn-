# Alpha.6 R2 artifact handoff — local outputs only

Audit date: 2026-11-19. These files are created locally and are **not GitHub Release assets**.

| Artifact | Size | SHA-256 |
|---|---:|---|
| Reviewed R2 source ZIP (133 entries: 132 files + manifest) | 36,858,109 bytes | `297a6596e7051e8467019795f500e69eff97695ca1062e33c60e4990eae436f8` |
| R1 → R2 source patch (24 changed source/test files) | 84,685 bytes | `88e3832f4755ac1f2d653387cb4acc18f79609804d53424be6ec15304af9f1ec` |
| Windows x64 package ZIP (7 files) | 41,819,473 bytes | `726bd551c052c6ba885bf1650bc820d7cec21cb5c96e6466dc31d067552d8d73` |
| SOURCE ZIP (130 source files + SOURCE_MANIFEST.json; 131 entries) | 36,829,720 bytes | `b58929332982865cde50e1b1238d835911f58012ac51d7d3b39089516e5c8439` |
| COMPLETE ZIP (Windows ZIP + SOURCE ZIP + installer) | 81,049,441 bytes | `ea95b9dfd70fffbab8a6c59faf128b36dee2c71d96cbd35f3c0dcc5217133fa4` |
| Online installer | 5,614,592 bytes | `5bb6100944c08a5402c5ab22f487055c38fcf02989761745ec9bd2ca6c12a754` |
| Release SHA256SUMS file | 473 bytes | `acb6998e90d0494cb185ce32c3013225b6804bd4660bd99c02795db96757edad` |

## Verification
- Reviewed source ZIP CRC, duplicate/path safety and all 132 manifest SHA-256/size entries: PASS.
- R1→R2 patch dry-run against clean original archive and byte-for-byte compare of all 24 changed paths: PASS.
- Release SOURCE ZIP 130-file manifest, nested archive SHA-256 and CRC: PASS.
- COMPLETE ZIP nested Windows/SOURCE/installer hashes and CRC: PASS.
- Root `sha256sum -c dist/SHA256SUMS.txt`: 4/4 PASS.
- Windows ZIP contains client/server EXE, README, recovery notes, release report, changelog and RELEASE_SHA256 manifest; CRC + inner SHA-256 PASS.
- Installer embeds exact Windows ZIP SHA-256; Go tests 3/3 and Linux-hosted HTTP integration (download, hash, extraction, overwrite refusal) PASS.

## Build/toolchain limitations
- Locally executed Go toolchain is 1.23.2. Current workflows pin Go 1.27.4, which could not be installed in this environment.
- Cross-builds: Windows amd64, Linux amd64, macOS amd64 and arm64 PASS with Go 1.23.2.
- Actual Windows/Linux/macOS runtime UI/audio, GPU profiling, Authenticode and release hosting are NOT RUN.
- No public release is created. Full source import to GitHub remains blocked because available GitHub actions can write UTF-8 text but do not accept local binary source/media archive uploads.
- The separate supplied Windows R2 EXE package is not part of this singleplayer source candidate: it has no matching VCS commit identity and includes multiplayer issue #22.