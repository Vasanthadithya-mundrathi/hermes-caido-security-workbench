---
name: caido-research
description: Use Caido MCP for scoped HTTP research, project organization, traffic review, and evidence capture in an authorized program or lab.
---

# Caido research

Before interacting with traffic, establish the current Caido project, local instance URL, user authorization, program/CTF scope, rate limits, and allowed techniques. A public writeup is background information, not permission to contact its historical target. If those facts are unavailable, read existing project data only and ask for the missing scope before active testing.

Use the connected `caido` MCP server to list projects and inspect requests/responses. Prefer read-only tools while forming a hypothesis. Label each observation with project, host, role, timestamp, request ID, and source. Existing browser history can include unrelated traffic; avoid reading or quoting it outside the chosen project.

When active testing is authorized, make a bounded comparison between a controlled baseline and one changed input or role. Respect exclusions and rate limits. Stop at the smallest proof of a boundary failure; avoid unnecessary data access or changes. Treat automated findings as leads requiring manual verification.

Capture a redacted request/response pair and use `templates/evidence-ledger.md` from this repository. Do not store credentials or Caido OAuth tokens in reports or Git. Clearly distinguish direct observations, researcher-provided notes, inference, and unknowns. Use the reporting skill for a final draft.

If MCP authentication fails, tell the user which check failed and refer to `docs/setup-macos.md`. Do not request or print raw OAuth tokens.
