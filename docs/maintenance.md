# Maintenance and freshness

This setup was reviewed on 2026-10-26. Re-check release notes, Daybreak model support, and program rules before a new engagement. A newer version is not automatically the right version for a live project; preserve a working rollback path.

## Review versions

```sh
hermes --version
hermes profile list
/opt/homebrew/bin/codex --version
caido-mcp-server --version
semgrep --version
trivy --version
gitleaks version
brew outdated --formula
brew outdated --cask
codex mcp get caido
python3 scripts/catalog.py check
```

Use [Hermes release notes](https://github.com/NousResearch/hermes-agent/releases), [Caido releases](https://github.com/caido/caido/releases), [Caido MCP releases](https://github.com/c0tton-fluff/caido-mcp-server/releases), [ProjectDiscovery docs](https://docs.projectdiscovery.io/), [Semgrep](https://semgrep.dev/docs/update), [Trivy](https://github.com/aquasecurity/trivy/releases), [Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases), [OBS releases](https://github.com/obsproject/obs-studio/releases), and [OpenAI's Daybreak model table](https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview) as primary sources. Check compatibility and release signatures or digests before replacing a community MCP binary.

For Homebrew-managed tools, upgrade selected packages with `brew upgrade <formula>` or `brew upgrade --cask <name>`. Use Hermes's supported updater for its source installation. Re-run the verification commands in [setup](setup-macos.md) after changing Hermes, Caido, or the MCP server.

After a Codex CLI or Hermes update, retest one prompt in each model profile and one read-only Caido MCP call. Recheck the profile-local launchers; the Daybreak flag, workspace permission, and Semgrep sandbox workaround were verified only against the dated versions in [the report](../REPORT.md). Start the Caido instance before declaring its MCP connection broken.

## Catalog updates

Add only public, stable publisher links to `catalog/resources.csv`. Note when access needs an account or when a feed contains summaries rather than full reports. Run `python3 scripts/catalog.py check` for structure and `python3 scripts/catalog.py build` for the Markdown index. Review changed links and claims manually; the script does not validate that a historical disclosure remains public or that every writeup is licensed for copying.
