# Alpha.6 R2 source and release artifact handoff

Audit date: 2026-11-19. These are generated local artifacts; they are not GitHub release assets.

| Artifact | Size | SHA-256 |
|---|---:|---|
| Reviewed R2 source archive (130 ZIP entries incl. manifest; 129 files) | 36,848,249 bytes | `64cfe0e8f77e651802f8d4a870e44f776661c33a93a634b88e57ed10497121a7` |
| R1 → R2 unified source patch (17 files) | 65,941 bytes | `5d47849932996983b50ff88b677f5b7ffef1241cd957f1feae6793e970eeb219` |
| Packaged Windows x64 distribution | 41,819,147 bytes | `a8ad1a9bab0f3abed0b28bedcf055d6dd17cb1c3148d2cfceb4bf32ec11e58fe` |
| Packaged SOURCE ZIP (127 source files + SOURCE_MANIFEST.json) | 36,823,964 bytes | `9853f3b470eeb0c3dba8e31f6edac7c8a1db474b557cdc2a3c0f3591241a8cb3` |
| COMPLETE ZIP (Windows + SOURCE + installer) | 81,043,369 bytes | `3a1bc91b594baedb72a499dd1619747648b06aefac2e5b3923e88ca7af790d97` |
| Windows online installer | 5,614,592 bytes | `e673cc17fb7bc8da21dae735a22b38f31c11762b17ee39e41609bfe741f40f45` |

## Important
- Windows and source build artifacts were created locally using Go 1.23.2, not the Go 1.27.3 version pinned by workflows.
- Cross-build/package/checksum/installer integration checks passed. Actual Windows 11 runtime, UI, audio, signing and public download remain NOT RUN.
- The installer was integration-tested as a Linux build against a local HTTP endpoint; it is not a Windows runtime test.
- No release has been uploaded or published. The source tree and media still need to be imported into GitHub before CI can validate the real game commit.
- Multiplayer content in the separate Windows R2 package was intentionally not merged into the singleplayer candidate.