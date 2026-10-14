# Repository guidance

This repository distills Liyuk's practical methods. Ask Liyuk is the navigator; the collection carries the experience. Read docs/design/2026-10-14-v1-design.md for the base architecture and docs/design/2026-10-14-v0.2-social-design.md for the current social expansion; older planning notes are historical.

- Keep each skills/<name> package self-contained. Local runtime links must stay inside it; no links to another skill or repository-only shared files.
- catalog/skills.json owns released names, paths, invocation modes and source IDs. Update README, Ask Liyuk's method map, plugin manifests and metadata together when that map changes.
- Explicit entries use disable-model-invocation: true and policy.allow_implicit_invocation: false together. Task methods remain discoverable unless the user changes policy.
- Preserve facts, numbers, attribution and unknowns. Distinguish source-backed methods from new AI-generated candidates. Only explicit author confirmation is author endorsement.
- Review and rewriting are separate unless the user requests both. Findings require evidence and impact; do not manufacture a fixed count.
- Method changes require realistic cases, including missing or conflicting information. Expected output is a rubric, not an execution result.
- Keep licenses with independently installable skills. Preserve provenance of migrated files. Shared decision-contract copies must stay identical.
- Publish only authorized source material and safe examples. Do not introduce workstation paths, private transcripts, or full third-party archives.
- Run python -m unittest discover -s tests -v and python scripts/validate_repo.py in the configured environment before committing.
