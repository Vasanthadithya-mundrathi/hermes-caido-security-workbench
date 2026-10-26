---
name: local-code-security
description: Review an authorized local codebase or CTF artifact with Semgrep, Trivy, Gitleaks, and Ghidra as appropriate, then validate findings against source and runtime evidence.
---

# Local code and artifact review

Confirm that the repository or artifact is owned, supplied, or explicitly in scope. Record its revision, language, build context, and the user's question. Keep unpublished source and scan outputs in a private workspace.

Start with a narrow source search and a concrete trust boundary. Choose one relevant free tool:

- `semgrep-offline --config <local-rule.yml> <path>` for local static patterns in the macOS Hermes workspace. The wrapper disables registry/metrics traffic and handles sandbox-local cache and certificate paths. A rule match is a lead, not proof of reachability.
- `trivy config <path>` for local infrastructure configuration checks; inspect the exact resource and deployed context before claiming exposure. Use `trivy fs` only when dependency or secret scanning is relevant, and note database freshness.
- `gitleaks dir <path> --redact` for candidate secrets. Never print, validate, or publish a candidate credential without explicit authorization; redact output and verify whether it is a fixture or active material by permitted means.
- `ghidraRun` or `analyzeHeadless` for binaries the user supplied. Hash originals, work on copies, and isolate untrusted programs before execution.

Preserve tool version, rule/check ID, command, exit status, and relevant file/line. If a tool fails, report the failure rather than claiming zero findings. Read the source or artifact around each result and seek a controlled way to falsify the proposed security consequence. Use `finding-validation` for live or supplied evidence and `ywh-reporting` or `evidence-based-reporting` for a report draft. Do not infer severity from a scanner label.
