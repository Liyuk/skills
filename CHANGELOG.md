# Changelog

## Unreleased

- Name neighboring skills in each entrypoint description, and state the handoff in the skill body where the loaded method could otherwise continue.
- Keep shared evidence-contract and RelationForge reference copies installable inside each skill package, with `shared/` as the only editable source.
- Stop eng-reporting examples from upgrading a note into a stronger role, benefit, or mechanism than the source contains.
- Check that README.md and README.zh-CN.md stay paired, that local Markdown links resolve, and that descriptions include the neighboring skills named in the catalog.
- Make README.md the English default page and keep the Chinese edition at README.zh-CN.md. Generate a Use instead / 改用 column in both catalogs from boundary and boundary_en.
- Pin relation-forge at 10aaf92. The two interpersonal skills match that commit, including handoffs and `reasoning-with-the-user.md`; the 19 shared references match its `shared/common` tree.

## 0.5.0 (2026-10-14)

- Distill five new previews from pinned public blog posts: problem location, new-context onboarding, manager of managers, hiring assessment and project diligence (explicit invocation only).
- Extend eng-reporting, metric-decision and situational-leadership with bounded references from blog sources; keep SLII definitions unchanged.
- Add four conditional Ask Liyuk task flows and a validator check that task-flow skill names exist in the catalog.
- Add 55 rubric cases (41 for the new skills, 14 for extended skills and router routes), record 33 pinned blog source fingerprints and run a small with/without-skill instruction probe on eight skills (24 prompt pairs); it found and fixed two defects and does not prove effectiveness, author calibration or client installation.

## 0.4.0 (2026-10-14)

- Add a situational leadership preview based on bounded public SLII sources, with task-specific recognition criteria, support actions and fourteen additional rubric cases.
- Distinguish book-inspired instructions from demonstrated recognition improvement; record six-probe baseline and forward scope.

- Add clear usage examples, core judgments and separate provenance, author calibration and behavior validation states for all fifteen skills.
- Add four conditional Ask Liyuk task flows and generate catalog artifacts with drift checks.
- Extend nine methods with optional perspectives from five books, using bounded public primary materials and original task adaptations.
- Add thirteen rubric cases, ten generator tests and a five-probe baseline/forward instruction smoke; retain limits rather than claim effectiveness.

## 0.3.0 (2026-10-14)

- Expand seven preview skills with conditional method playbooks and worked synthetic examples.
- Capture bounded author-confirmed conflict escalation and one-on-one support diagnosis methods.
- Add branch-specific cases; keep source-backed principles, author confirmation and AI candidate extensions separate.

## 0.2.0 (2026-10-14)

- Migrate two RelationForge skills with references, invocation policies and 48 synthetic cases.
- Add five preview methods: conflict alignment, conversation preparation, one-on-one, relationship boundaries and gift planning.
- Expand Ask Liyuk routing and synchronize the 15-skill catalog and plugin manifest.
- Record source fingerprints and limited baseline / instruction smoke observations.

## 0.1.0 (2026-10-14)

- Add Ask Liyuk navigation, experience review, and an author-led distillation workflow as previews.
- Migrate five engineering decision skills with their licenses and 39 existing evaluation cases.
- Make migrated shared references self-contained for single-skill copying.
- Add source records, invocation metadata, plugin manifests, structural validation and CI.
- Document the pinned Matt Pocock design analysis and v1 architecture.
