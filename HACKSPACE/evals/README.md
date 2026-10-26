# Offline finding-judgment evaluation

The six cases in `cases/` are synthetic evidence packets. They test whether an agent distinguishes a supported boundary failure from a status-only signal, stale-session contradiction, out-of-scope asset, and agent-output-only prompt injection. No case sends target traffic.

Run `python3 HACKSPACE/scripts/eval_findings.py list`, then `python3 HACKSPACE/scripts/eval_findings.py run --profile proof --limit 2`. The runner invokes the selected local Hermes profile and writes raw replies plus score data to Git-ignored `HACKSPACE/data/evals/`. It evaluates exact verdict, existing artifact citations, required controls, and prohibited overclaims. `false_confirmations` counts supported verdicts on cases where the expected verdict differs. A passing synthetic benchmark does not prove performance on a live program.

To rescore an existing run, use `python3 HACKSPACE/scripts/eval_findings.py score --responses HACKSPACE/data/evals/<run>/responses.jsonl`. To add cases, preserve a clear expected verdict, a small set of decisive evidence IDs, and claims that would overstate the evidence. Keep new cases synthetic or fully redacted and authorized; raw bounty evidence belongs in `HACKSPACE/private/`.
