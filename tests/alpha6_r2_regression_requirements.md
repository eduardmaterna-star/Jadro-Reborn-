# Follow-up regression requirements for issues #22–#25

The full updated JavaScript/Go source is in alpha.6 R2 SOURCE ZIP, not yet imported into GitHub.

**#22:** create expedition A/B on the same server, join A/B with distinct tokens, try A on another server, reject already_online after world_ready, verify inactive controls, verify reconnect and no duplicate inventory, simulate separate tabs and browser reload.

**#23:** confirm all five WAV effects play on actual game events; buying and selling must not play success sound when server rejects action; rapid excavation must not produce unbounded overlapping sounds. Test silence at 0% and user-gesture restrictions.

**#24:** verify Music, SFX and Wind volume sliders independently persist. Test music transitions, loop artifacts, pause and hidden tab. Real acoustic listening is required.

**#25:** profile WebGL texImage2D and renderChunk GPU/CPU on 1080p/1440p Windows GPU; don't claim FPS improvements from removing two dead calculations before measuring.

**Release gating:** do not publish or close #11/#12/#19 without full source+media import and successful Windows CI. The Go 1.23.2 cross-build is not equivalent to verified runtime on Windows.
