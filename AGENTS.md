# Repository guidance

This repository distills Liyuk's practical methods. Ask Liyuk is the navigator; the collection carries the experience. Read docs/design/2026-10-14-v1-design.md for the base architecture and docs/design/2026-10-14-v0.2-social-design.md for the social expansion, and docs/design/2026-10-14-v0.3-depth-design.md for current method depth and bounded author calibration; older planning notes are historical.

## Git synchronization: pull requests

- Make changes on a dedicated branch based on the latest `origin/main`. Preserve existing local changes when switching or updating branches.
- Run the required checks, commit, push the working branch, and open or update a PR targeting `main`. Direct pushes to `main` are not the synchronization workflow, including documentation-only follow-ups.
- Keep subsequent fixes and verification records on the same PR branch while it is open. A merged change starts a new branch and PR.
- Report the PR URL, changes, checks and remaining limitations. Leave merging to the user unless they explicitly authorize it; opening a PR does not authorize merging or auto-merge.
- Read [the synchronization workflow](docs/workflows/pr-sync.md) when preparing a branch, synchronizing changes or closing out a task. Historical direct-push records describe previous releases and do not override this policy.

## Skill maintenance

- Keep each skills/<name> package self-contained. Local runtime links must stay inside it; no links to another skill or repository-only shared files.
- catalog/skills.json owns released names, paths, invocation modes and source IDs. Update README, Ask Liyuk's method map, plugin manifests and metadata together when that map changes.
- Explicit entries use disable-model-invocation: true and policy.allow_implicit_invocation: false together. Task methods remain discoverable unless the user changes policy.
- Preserve facts, numbers, attribution and unknowns. Distinguish source-backed methods from new AI-generated candidates. Only explicit author confirmation is author endorsement.
- Review and rewriting are separate unless the user requests both. Findings require evidence and impact; do not manufacture a fixed count.
- Method changes require realistic cases, including missing or conflicting information. Expected output is a rubric, not an execution result.
- Keep licenses with independently installable skills. Preserve provenance of migrated files. Shared decision-contract copies must stay identical.
- Publish only authorized source material and safe examples. Do not introduce workstation paths, private transcripts, or full third-party archives.
- Run python -m unittest discover -s tests -v and python scripts/validate_repo.py in the configured environment before committing.
