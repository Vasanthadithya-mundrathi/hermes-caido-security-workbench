# Codex security workbench

For bug bounty research in this repository, start with [HACKSPACE](HACKSPACE/README.md). Prioritize AI agent and AI application security: third-party prompt injection with demonstrated cross-user impact, tool/MCP trust boundaries, retrieval and document injection, data exfiltration, unauthorized actions, tenant separation, and sandbox or infrastructure escape. Read [the AI security brief](HACKSPACE/research/AI-SECURITY.md) and use `hackspace-research`, `bug-bounty-workflow`, and `finding-validation`.

Search the local link library with `python3 scripts/library.py search '<term>'` and check the original report before citing a payout or technical claim. Bulk CVE/OSV/GHSA/NVD archives are advisories and overlap by alias; they are not 5 GB of paid bug bounty reports. Keep private notes, raw data, proxy sessions, and unpublished findings outside public Git.

An old report, a jailbreak that changes only model wording, or an advisory is a lead or prior art. A finding requires current program scope, a distinct root cause or regression, an authorized controlled test, and direct evidence of a security boundary failure. Public research cannot rule out a private duplicate. Use the user's `ywh-reporting` skill for pre-submission triage and reports. This file authorizes no live target testing or external submission.

For publish-ready reports and CTF writeups, put the actual validation command, output, and supported conclusion together. Keep provenance and evidence gaps in editor notes instead of adding self-referential disclaimers, “Check and limit” sections, or paragraphs listing actions that did not happen. Claim remote acceptance only when it is recorded.
