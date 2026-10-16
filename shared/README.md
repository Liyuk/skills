# Shared skill files

These files are the only editable copies of content that more than one skill package needs.

`manifest.json` lists each canonical file and the skill-package paths that must stay identical to it. `scripts/sync_shared_copies.py --write` copies them into those packages. `scripts/sync_shared_copies.py --check` fails when a copy is missing or different.

Skill packages do not link here. A copied skill directory remains installable on its own. Edit the canonical file, then run the sync script. Do not edit the copies by hand.

Files that differ between packages stay in those packages and are not listed here.

`relation-forge/` is the `shared/common` tree from the relation-forge commit pinned in `catalog/sources.json`. Refresh that tree from the pinned commit, then run the sync script. Do not edit those copies as if they were an independent method.
