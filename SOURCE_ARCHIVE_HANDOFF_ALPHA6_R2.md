# Alpha.6 R2 artifact handoff — local outputs only

Audit date: 2026-11-19. These files are created locally and are **not GitHub Release assets**.

| Artifact | Size | SHA-256 |
|---|---:|---|
| Reviewed R2 source ZIP (133 entries: 132 files + manifest) | 36,857,446 bytes | `5eb81f4d7c3acb42e51154a797475ae96a90bdd7eee4616cdea04f9e35b95134` |
| R1 → R2 source patch (24 changed source/test files) | 83,272 bytes | `f421b3216c018687b4e7ab2317bd6aa91b01f8600aaca8bdfba0267167e60cb5` |
| Windows x64 package ZIP (7 files) | 41,819,385 bytes | `4c1c21b34e32c2de0d5a8822b4d8e17d47f423292feab7264d4719f45ed8f950` |
| SOURCE ZIP (130 source files + SOURCE_MANIFEST.json; 131 entries) | 36,829,412 bytes | `7f21d46920bae92cf5ed80f73df700e62d022d91afb4cb5b19e0016575ab78c6` |
| COMPLETE ZIP (Windows ZIP + SOURCE ZIP + installer) | 81,049,182 bytes | `4dc5b6df6f724a0e95c9641dc06ae196470ff66c764ee1dd3a05c1921da039fe` |
| Online installer | 5,614,592 bytes | `9e873e8bb529003054aba614cfec36f1be2b145129345d26de1a328c4c36e137` |
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