---
name: ctf-writeup
description: Turn an authorized CTF solve and its evidence into an original, technically precise first-person writeup in the user's point of view, with a clear insight, reproducible proof, honest credits, and event-aware publication rules.
---

# CTF writeup in my point of view

Use this skill when the user asks to draft, revise, or polish a CTF/lab writeup. Follow `ctf-workflow` to solve or verify a challenge only when the user has authorized that work; writing alone does not authorize new challenge-service requests. Check event embargo and flag-sharing rules before preparing a public version. Do not publish without the user's explicit request.

## Gather the real story

Read the supplied notes, commands, code, terminal output, screenshots, challenge files, and any confirmed flag submission. Make a small provenance map: what the user personally did or said, what Hermes/another tool ran, what a teammate or source reported, and what remains unknown. Never invent the user's discovery moment, frustration, travel, teammates, failed attempts, flag submission, or retrospective insight. First-person `I` is for the user's supported actions and interpretations; use neutral wording such as “the local run showed” for agent-run checks. Credit teammates, challenge authors, and earlier researchers when their contributions are known.

If the key pivot or confirmation is missing, write a useful draft with an explicit note outside publish-ready prose. Ask one focused question only if it materially changes the story. A locally derived flag is not a confirmed event solve unless the challenge service accepted it.

## Build an original technical narrative

The user likes the readable, story-led technical structure of [Orange Tsai's *The Art of PHP*](https://blog.orange.tw/posts/2025-08-the-art-of-php-ch/). Take the **method**, not the author's wording, personal history, jokes, or distinctive titles: establish why a detail mattered, pose the question it raised, explain the underlying mechanism, show the decisive experiment, and connect the observation to the solve. If the user supplies their own past writing, prefer its terminology and level of formality for their voice. Use a little personality only when the user's notes support it. Do not pad a short challenge into a memoir.

Organize around the actual turning points rather than a raw command dump. Lead with the challenge's constraint or surprising behavior; show the smallest useful code, diagram, packet, or output near the claim it supports. Explain why the method works before giving the final script. Keep failed hypotheses only when they clarify the eventual insight. Use descriptive headings with some energy where natural, while keeping commands, parameters, versions, and outcomes exact.

## Verify before writing “solved”

Re-run a **local** decoder or check against the supplied artifact when authorized and useful. Record the environment, input hash when relevant, exact command, expected output, observed output, and whether the result was accepted by a challenge service. Mark illustrative code as pseudocode. If verification fails, preserve the contradiction and do not smooth it away in prose. Do not claim real-world vulnerability impact from a CTF mechanic.

Use `templates/ctf-writeup.md` as a flexible outline. Finish with the reusable idea and the limits of what was actually checked. Cite primary docs and credited writeups near the relevant claim; do not copy another author's prose or reproduce a third-party solution as the user's own. Before finalizing, check every first-person sentence against the provenance map, every code/output block against artifacts, and the event's current disclosure rules.
