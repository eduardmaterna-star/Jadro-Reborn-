# Issue #10 — UI hotfix staging

Status: **implemented in local SOURCE patch; not yet merged into the GitHub game repository.**

Changes to `launcher/web/index.html`:
- Remove the `.desktop-brand` title block and version subtitle (keep document `<title>`).
- Remove top-right `quickShop` and `quickSell` buttons (preserve physical shop/sale and other HUD buttons).
- Position the top bar at 18px, or 10px on narrow screens.

Changes to `launcher/web/game.js`:
- Remove removed button references in translation/update and click handlers.
- Keep `salePrompt:'PRODEJ'`, and measure the rendered label using `ctx.measureText(label).width` for the dark prompt background; center vertically.
- Keep station interaction using E untouched.

Verification: `node --check launcher/web/game.js`, `node tests/test_issue10_ui.cjs`, `python scripts/verify_game_sources.py`, `go test ./...`, Python unit tests — PASS. Browser runtime/Windows runtime — NOT RUN.

The original screenshot was supplied in a ChatGPT conversation, and GitHub's current connector only supports creating UTF-8 text files, not uploading that original binary PNG. Screenshot must be manually attached to the issue. No signed EXE has been produced.

Issue: https://github.com/eduardmaterna-star/Jadro-Reborn-/issues/10
