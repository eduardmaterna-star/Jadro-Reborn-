# JÁDRO REBORN — v0.4.0-alpha.4

**Status: Alpha, not Stable.**

This branch is a staging area for importing the current game from the verified local source package. **The complete game has NOT been uploaded yet**: the GitHub connector currently cannot transfer the 36 MB local ZIP or its large binary PNG/WAV/OGG assets. Do not run the signing/release workflows from this incomplete branch.

Current changes in the game:
- Audible adaptive music and animated tree foliage
- Smoother weather and temperature display
- Generator, cable power, bucket, powered water pump and deep-mine seepage (single-player only)
- Multiplayer lobby, shared dig events and multiplayer state from earlier alpha releases
- Existing single-player saves preserved

Original source ZIP SHA-256:
`2eed9062b2087951eff91c6fb040bfdb51146cdf0fe9bbb594b1e17e76501aee`

Existing unsigned Windows ZIP SHA-256:
`5bcf16ba8ebf604e575df423d6be97f0138bff89f974cd3e00bef719ef910171`

**Remaining task:** upload all 109 source-archive entries including binary media to this branch, compare SHA-256, run Windows CI, then merge or release. The game/installer are not digitally signed.
