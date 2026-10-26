---
name: evidence-capture
description: Prepare screenshots, short screen recordings, request-response pairs, and a traceable evidence ledger for authorized security research.
---

# Evidence capture

Identify the exact claim each artifact needs to support before recording. Capture a controlled baseline and the minimal changed result, with role/account labels and timestamps. Prefer a redacted HTTP pair plus a short screen recording when a workflow is hard to understand from text alone.

Use macOS Shift-Command-5 or OBS as described in `docs/recording.md`. Save raw evidence privately outside the public repository. Check every frame and the recording's audio for tokens, cookies, personal data, unrelated tabs, and private program details. Make a redacted sharing copy without altering the relevant outcome.

Add artifact path, SHA-256 hash, date, actor/role, what it shows, what it cannot show, and redactions to `templates/evidence-ledger.md`. Do not claim a screenshot demonstrates an outcome it does not display.
