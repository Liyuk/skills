# Liyuk Skills

Reusable AI agent skills for engineering decisions, leadership, communication, and personal knowledge distillation. **English-language documentation.** Works with Claude Code and Codex.

[Quick start](#installation-and-invocation) · [Common tasks](#common-tasks) · [Skill catalog](#skill-catalog) · [Chinese](README.zh-CN.md) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [MIT License](LICENSE)

**Not sure where to start? Ask Liyuk.** This collection turns practical methods into reusable skills for planning, reviews, metrics, retrospectives, communication, experience reviews, relationships, and everyday decisions. Ask Liyuk routes you to a method; each skill handles a focused task.

Current release: **0.5.0 / preview**, with 21 skills. Five engineering skills were migrated from [engineering-decision-skills](https://github.com/Liyuk/engineering-decision-skills), and two relationship skills from [RelationForge](https://github.com/Liyuk/relation-forge). The remaining methods were distilled from blog posts and other source material. Newly distilled methods still need real-world use and author calibration. Skills follow the [Agent Skills file format](https://agentskills.io/specification).

## Installation and invocation

Clone the repository, then copy the skills you need for your client. This example installs Ask Liyuk:

```sh
git clone https://github.com/Liyuk/skills.git liyuk-skills
cd liyuk-skills
```

**Claude Code: invoke a file-installed skill with `/name`.**

```sh
mkdir -p ~/.claude/skills
cp -R skills/ask-liyuk ~/.claude/skills/
```

Then enter:

```text
/ask-liyuk I need to write about a failed project in my self-review. Should I start with a retrospective or draft the review first?
```

If you install through this repository's plugin marketplace, use the plugin prefix: `/liyuk-skills:ask-liyuk`. See [Claude Code's documentation](https://code.claude.com/docs/en/skills#choose-where-skills-load) for the naming rules for file and plugin installations. The plugin manifest passes static checks; installation through the client has not been verified for every platform.

**Codex: invoke a skill with `$name`.**

```sh
mkdir -p ~/.codex/skills
cp -R skills/ask-liyuk ~/.codex/skills/
```

```text
$ask-liyuk I need to write about a failed project in my self-review. Should I start with a retrospective or draft the review first?
```

Codex CLI and IDE can also use `/skills` to select a skill. This is a selection interface; individual skills are not invoked as `/name`. See [OpenAI's invocation guide](https://developers.openai.com/blog/eval-skills#2-create-the-skill).

Installing Ask Liyuk alone gives you recommendations and next steps. To perform a specialized task, also install the corresponding skill directory. If an older skill with the same name is already installed, check its version and choose one source before copying; this avoids overwriting your edits or creating duplicate entry points.

## Your first task

To review a technical proposal, put the proposal after `/tech-review`. If you are unsure whether you need to locate a problem, decide where to invest, or review a proposal, start with `/ask-liyuk`. In Codex, use the corresponding `$name` form.

The following is a constructed example. Install the matching skill and replace the example with your own context:

```text
/situational-leadership
A teammate knows the existing service well but is handling a data migration for the first time and cannot determine the rollback criteria.
They are willing to own it, and the goal and authority are clear. What guidance should I provide, and when can I step back?
```

The skill should identify task-specific evidence, support the manager should provide, what the teammate can continue to own, and signals for adjusting support. Missing information should remain explicit, and the output should be checked against the actual situation.

`ask-liyuk`, `distill-experience`, and `project-diligence` require deliberate invocation. Other methods may be discovered when they match a task. Discovery and invocation depend on the client's capabilities.

## Common tasks

| Task | Claude Code file installation | Codex |
| --- | --- | --- |
| Find the right method | `/ask-liyuk` | `$ask-liyuk` |
| Review a technical proposal | `/tech-review` | `$tech-review` |
| Decide whether to direct, support, or delegate | `/situational-leadership` | `$situational-leadership` |
| Distill a method from your experience | `/distill-experience` | `$distill-experience` |
| Investigate why a plausible solution did not work | `/problem-location` | `$problem-location` |
| Get oriented in an unfamiliar team or business | `/new-context-onboarding` | `$new-context-onboarding` |
| Coordinate multiple leads and teams | `/manager-of-managers` | `$manager-of-managers` |
| Prepare interview follow-ups and organize candidate evidence | `/hiring-assessment` | `$hiring-assessment` |
| Assess a new business or startup project | `/project-diligence` | `$project-diligence` |

After installing a skill, write your question or provide the relevant material after its command. With the Claude Code plugin, prefix these commands with `/liyuk-skills:`.

## Skill catalog

The catalog below lists all 21 skills. Command examples use Claude Code file installation (`/name`); use `$name` in Codex and add the plugin prefix in Claude Code plugin installations.

<!-- skills-catalog:start -->

| Skill | Core judgment | Behavior check |
| --- | --- | --- |
| [/ask-liyuk](skills/ask-liyuk/SKILL.md) · Ask Liyuk · [Usage guide](docs/skills/ask-liyuk.md) | Identify the decision or deliverable, then follow only the path needed now. | Limited instruction smoke check |
| [/tech-planning](skills/tech-planning/SKILL.md) · Technical planning · [Usage guide](docs/skills/tech-planning.md) | Tie technical work to business outcomes and capability gaps; compare it with keeping the status quo. | Behavioral retest pending |
| [/tech-review](skills/tech-review/SKILL.md) · Technical review · [Usage guide](docs/skills/tech-review.md) | Report only evidence-backed issues that affect the decision; pass proposals that are good enough. | Structure check |
| [/metric-decision](skills/metric-decision/SKILL.md) · Metric decisions · [Usage guide](docs/skills/metric-decision.md) | Until definitions and comparability are confirmed, metric changes are not outcome or causal evidence. | Limited instruction smoke check |
| [/management-retro](skills/management-retro/SKILL.md) · Engineering retrospective · [Usage guide](docs/skills/management-retro.md) | Separate facts, explanations, and next actions; do not treat hindsight as root cause. | Behavioral retest pending |
| [/problem-location](skills/problem-location/SKILL.md) · Problem diagnosis · [Usage guide](docs/skills/problem-location.md) | Make evidence jointly inspectable, then distinguish symptoms from deeper causes; do not declare a root cause without investigation. | Limited instruction smoke check |
| [/project-diligence](skills/project-diligence/SKILL.md) · Project diligence · [Usage guide](docs/skills/project-diligence.md) | Use a canvas to check coherence, a pitch to persuade, and diligence to verify independently; keep assumptions distinct from facts. | Limited instruction smoke check |
| [/eng-reporting](skills/eng-reporting/SKILL.md) · Engineering communication · [Usage guide](docs/skills/eng-reporting.md) | Identify the reader’s decision first; do not strengthen uncertain claims or invent benefits. | Behavioral retest pending |
| [/experience-review](skills/experience-review/SKILL.md) · Experience review · [Usage guide](docs/skills/experience-review.md) | Separate team outcomes from personal contribution; missing evidence does not prove a lack of ability. | Behavioral retest pending |
| [/distill-experience](skills/distill-experience/SKILL.md) · Experience distillation · [Usage guide](docs/skills/distill-experience.md) | Keep facts, interpretations, and methods separate; explicit confirmation applies only to the conditions confirmed. | Behavioral retest pending |
| [/new-context-onboarding](skills/new-context-onboarding/SKILL.md) · New-context onboarding · [Usage guide](docs/skills/new-context-onboarding.md) | Limited information does not imply limited ability; learn the context before reporting or requesting resources. | Limited instruction smoke check |
| [/person-deep-analysis](skills/person-deep-analysis/SKILL.md) · Interpersonal analysis · [Usage guide](docs/skills/person-deep-analysis.md) | Form bounded interpretations from the available material; one interaction cannot establish a stable personality. | Limited instruction smoke check |
| [/interaction-risk-analysis](skills/interaction-risk-analysis/SKILL.md) · Interaction risk analysis · [Usage guide](docs/skills/interaction-risk-analysis.md) | Protective action need not wait for proof of malice; impact and benefit do not prove intent. | Limited instruction smoke check |
| [/conflict-alignment](skills/conflict-alignment/SKILL.md) · Conflict alignment · [Usage guide](docs/skills/conflict-alignment.md) | When a peer-level resource or authority deadlock persists, stop repeating persuasion and seek support with the evidence. | Limited instruction smoke check |
| [/conversation-preparation](skills/conversation-preparation/SKILL.md) · Conversation preparation · [Usage guide](docs/skills/conversation-preparation.md) | Clarify first, give feedback next, and make commitments last; a draft is not agreement. | Behavioral retest pending |
| [/one-on-one](skills/one-on-one/SKILL.md) · One-on-one alignment · [Usage guide](docs/skills/one-on-one.md) | Set shared acceptance criteria first; keep ownership with the teammate for resource gaps, and involve the manager for authority gaps. | Limited instruction smoke check |
| [/situational-leadership](skills/situational-leadership/SKILL.md) · Situational leadership · [Usage guide](docs/skills/situational-leadership.md) | Assess the same person by task; distinguish capability and motivation from organizational authority, and adjust support as evidence changes. | Limited instruction smoke check |
| [/relationship-boundaries](skills/relationship-boundaries/SKILL.md) · Relationships and boundaries · [Usage guide](docs/skills/relationship-boundaries.md) | Keep introductions separate from endorsements; declining a request does not require compensatory help. | Behavioral retest pending |
| [/gift-planning](skills/gift-planning/SKILL.md) · Gift planning · [Usage guide](docs/skills/gift-planning.md) | Understand the recipient’s needs before planning a surprise; do not infer preferences from identity labels. | Limited instruction smoke check |
| [/manager-of-managers](skills/manager-of-managers/SKILL.md) · Managing managers · [Usage guide](docs/skills/manager-of-managers.md) | Align decisions, responsibility, and consequences; do not trade away safety, compliance, or fairness for outcomes. | Limited instruction smoke check |
| [/hiring-assessment](skills/hiring-assessment/SKILL.md) · Hiring assessment · [Usage guide](docs/skills/hiring-assessment.md) | Separate observed facts, inferences, and preferences; treat potential as an open hypothesis, not a label. | Limited instruction smoke check |

<!-- skills-catalog:end -->

Source, author calibration, and behavioral verification are tracked separately. Migration does not imply maturity, and a limited smoke check is not evidence of general effectiveness. Each skill's usage guide explains its inputs, outputs, and decision criteria.

Each skill can be copied independently. Ask Liyuk chooses a route based on the task. When only the navigation skill is installed, it can recommend the next step but cannot claim to have run an uninstalled method.

## Why this project exists

Source material includes projects, blog posts, existing skills, and lessons from personal growth. The author contributes experience and calibration; AI helps organize candidate methods and test counterexamples. Sources, facts, and inferences are tracked separately. Gaps remain visible when evidence is missing, rather than being hidden by polished prose.

The project draws on Matt Pocock's skill layering, navigation, and small composable capabilities. The [design analysis](docs/research/2026-10-14-matt-skills-design.md), [v1 design](docs/design/2026-10-14-v1-design.md), [social-method expansion](docs/design/2026-10-14-v0.2-social-design.md), and [method-depth update](docs/design/2026-10-14-v0.3-depth-design.md) explain what was adopted and adapted. The [v0.4 usability design](docs/design/2026-10-14-v0.4-usability-design.md) and [book-perspective research](docs/research/2026-10-14-book-perspectives.md) cover additional work. The [v0.5 blog distillation design](docs/design/2026-10-14-v0.5-blog-distillation-design.md) describes five methods and their source boundaries. [Book recognition and situational leadership research](docs/research/2026-10-14-book-recognition-and-situational-leadership.md) records the available evidence and theory version. Matt's skill content was not copied.

## Validation and maintenance

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_repo.py
.venv/bin/python scripts/sync_catalog.py --check
```

Structural checks do not prove model behavior. Existing cases and completed checks are recorded in the [v0.5 validation report](evals/reports/v0.5.md), with earlier records for [v0.4](evals/reports/v0.4.md), [v0.2](evals/reports/v0.2.md), and [v0.1](evals/reports/v0.1.md). An `expected_output` is a rubric, not a test result. Fixed source revisions and fingerprints are listed in [sources.json](catalog/sources.json).

When changing a method, add cases that reveal whether its judgment changes appropriately. Keep personal source material, company information, and private records in your own workspace; use synthetic or explicitly public material for contributions.

Changes are synchronized through **branch → checks → PR → merge**. Documentation updates and fixes also go through the relevant PR branch; maintainers decide when to merge into `main`. See the [PR synchronization workflow](docs/workflows/pr-sync.md).

## License

Original instructions, code, and documentation in this repository are licensed under the [MIT License](LICENSE). You may use, modify, redistribute, and commercially use them, provided you retain the applicable copyright and license notices. The content is provided as-is, without warranty. The license files in each skill package govern that package. See the [standard MIT text](https://opensource.org/license/mit).

Each skill package includes its own license; keep it when copying a skill independently. Migrated content retains its original copyright and attribution. External books, blog posts, framework diagrams, and trademarks are not relicensed under this repository's MIT license and remain subject to their own terms. This project provides original adaptations and source references; it does not distribute full third-party works.

Content licensing and file format are separate: MIT is the open-source license, while the skill structure follows the Agent Skills specification. Claude Code and Codex invocation syntax is described above.
