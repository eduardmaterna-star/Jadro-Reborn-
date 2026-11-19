# Alpha.6 R2 source and release artifact handoff

Audit date: 2026-11-19. These are generated local artifacts; they are not GitHub release assets.

| Artifact | Size | SHA-256 |
|---|---:|---|
| Reviewed R2 source archive (132 ZIP entries: 131 files + manifest) | 36,852,994 bytes | `e1a69dac330cc0a2341607153e9163a81e3e8ca15065457485980dfab5b53f11` |
| R1 → R2 unified source patch (19 files) | 72,813 bytes | `576e6a92d573c7343f6dc8703c2b997054a7b29752c796cd82818f09ee25ccec` |
| Packaged Windows x64 distribution (7 entries) | 41,819,147 bytes | `a8ad1a9bab0f3abed0b28bedcf055d6dd17cb1c3148d2cfceb4bf32ec11e58fe` |
| Packaged SOURCE ZIP (129 source files + SOURCE_MANIFEST.json) | 36,826,738 bytes | `a1b92e2bc7f03fd9dfecd0139572d10b4a227365a3985931ed9f85b019d084e6` |
| COMPLETE ZIP (Windows + SOURCE + installer) | 81,045,999 bytes | `2486f65a88573e61fbc7cbc4c76f125597d7f3f15150f04d5c148dc704b35fd4` |
| Windows online installer | 5,614,592 bytes | `e673cc17fb7bc8da21dae735a22b38f31c11762b17ee39e41609bfe741f40f45` |

## Local verification
- Local release runner: 12/12 steps PASS.
- Python test suite: 16/16 PASS; cross-platform workflow tests 3/3 PASS.
- `.github/workflows/cross-platform-ci.yml` YAML parse PASS. Matrix: Windows x64, Linux x64, macOS Intel (amd64), macOS Apple Silicon (arm64); Go client/server builds, Python/Node/Go tests, Linux race job. Permissions are `contents: read`; no release publishing.
- Local Go 1.23.2 cross-builds of client and server: Windows amd64, Linux amd64, macOS amd64 and arm64 PASS.
- Patch applies to a clean R1 extraction and all 19 changed files match the review tree byte-for-byte.
- SOURCE manifest, nested archive hashes and CRC, and `sha256sum -c dist/SHA256SUMS.txt`: PASS.

## Important limitations
- Build artifacts were created locally with Go 1.23.2, not Go 1.27.3 pinned in workflows.
- The cross-platform workflow was syntax-checked and unit-tested locally but has not run on GitHub against the game source. `main` still lacks the complete source tree and binary assets.
- Actual Windows 11/Linux/macOS GUI/runtime/audio testing, GPU profiling, Authenticode signing and release publication remain NOT RUN.
- The installer was integration-tested as a Linux build against a local HTTP endpoint and actual Windows ZIP; this is not a Windows runtime test.
- No release has been uploaded or published. The complete source + media still need to be imported into GitHub before Actions can validate the real game commit.
- Separate Windows R2 package includes multiplayer issue #22 and cannot be tied to this source commit; its multiplayer content was deliberately not mixed into the singleplayer candidate.