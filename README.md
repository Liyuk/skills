# Liyuk Skills

Reusable AI agent skills for engineering decisions, leadership, communication, and personal knowledge distillation. **English-first, with a complete Chinese version below.** Works with Claude Code and Codex.

[Quick start](#installation-and-invocation) · [Common tasks](#common-tasks) · [Skill catalog](#skill-catalog) · [中文版本](#中文版本) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [MIT License](LICENSE)

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

The shared catalog below lists all 21 skills. Command examples use Claude Code file installation (`/name`); use `$name` in Codex and add the plugin prefix in Claude Code plugin installations. Skill names and links are usable in English; the catalog's decision summaries and verification labels are currently maintained in Chinese.

<!-- skills-catalog:start -->

| 指令 / 技能 | 核心判断 | 行为验证 |
| --- | --- | --- |
| [/ask-liyuk](skills/ask-liyuk/SKILL.md) · Ask Liyuk · [使用说明](docs/skills/ask-liyuk.md) | 先识别要作的决定或交付物，只走当前需要的路径 | 有限指令冒烟 |
| [/tech-planning](skills/tech-planning/SKILL.md) · 技术规划 · [使用说明](docs/skills/tech-planning.md) | 技术动作必须对应业务结果与能力缺口，并比较继续现状等选择 | 本轮改动待行为重测 |
| [/tech-review](skills/tech-review/SKILL.md) · 技术方案评审 · [使用说明](docs/skills/tech-review.md) | 只报告有依据且会影响决定的问题，足够好可以通过 | 结构检查 |
| [/metric-decision](skills/metric-decision/SKILL.md) · 指标判断 · [使用说明](docs/skills/metric-decision.md) | 口径与可比性未确认前，指标变化不能直接充当成果或因果证据 | 有限指令冒烟 |
| [/management-retro](skills/management-retro/SKILL.md) · 工程复盘 · [使用说明](docs/skills/management-retro.md) | 分清事实、解释与下一轮动作，不把事后解释写成根因 | 本轮改动待行为重测 |
| [/problem-location](skills/problem-location/SKILL.md) · 问题定位 · [使用说明](docs/skills/problem-location.md) | 先让材料可被共同检查，再区分表层与底层；没有调查不宣布根因 | 有限指令冒烟 |
| [/project-diligence](skills/project-diligence/SKILL.md) · 项目判断 · [使用说明](docs/skills/project-diligence.md) | 画布查自洽、路演是说服、尽调才独立验证；假设不能讲成事实 | 有限指令冒烟 |
| [/eng-reporting](skills/eng-reporting/SKILL.md) · 工程汇报 · [使用说明](docs/skills/eng-reporting.md) | 先确定读者要作的决定，表达不能强化未知或补造收益 | 本轮改动待行为重测 |
| [/experience-review](skills/experience-review/SKILL.md) · 项目经历 Review · [使用说明](docs/skills/experience-review.md) | 团队结果与个人贡献分开，材料缺口不等于没有能力 | 本轮改动待行为重测 |
| [/distill-experience](skills/distill-experience/SKILL.md) · 蒸馏经验 · [使用说明](docs/skills/distill-experience.md) | 事实、解释与方法分开，明确确认只覆盖对应条件 | 本轮改动待行为重测 |
| [/new-context-onboarding](skills/new-context-onboarding/SKILL.md) · 新环境入场 · [使用说明](docs/skills/new-context-onboarding.md) | 信息不足不等于能力不足；先获取信息，再汇报，再要资源 | 有限指令冒烟 |
| [/person-deep-analysis](skills/person-deep-analysis/SKILL.md) · 人际深度解析 · [使用说明](docs/skills/person-deep-analysis.md) | 按材料形成有限解释，单一片段不能补成稳定人格 | 有限指令冒烟 |
| [/interaction-risk-analysis](skills/interaction-risk-analysis/SKILL.md) · 互动风险分析 · [使用说明](docs/skills/interaction-risk-analysis.md) | 行动保护不必等到证明恶意，效果和利益不能证明主观意图 | 有限指令冒烟 |
| [/conflict-alignment](skills/conflict-alignment/SKILL.md) · 冲突对齐 · [使用说明](docs/skills/conflict-alignment.md) | 同层资源权限死结停止重复说服，整理材料上升支持 | 有限指令冒烟 |
| [/conversation-preparation](skills/conversation-preparation/SKILL.md) · 沟通准备 · [使用说明](docs/skills/conversation-preparation.md) | 先澄清，再反馈，最后承诺；草稿和共识是不同状态 | 本轮改动待行为重测 |
| [/one-on-one](skills/one-on-one/SKILL.md) · 1-on-1 对齐 · [使用说明](docs/skills/one-on-one.md) | 先有共同验收标准；纯资源问题可保留成员负责，权限缺口负责人介入 | 有限指令冒烟 |
| [/situational-leadership](skills/situational-leadership/SKILL.md) · 情景领导力 · [使用说明](docs/skills/situational-leadership.md) | 同一个人按任务分别判断；能力投入与组织权限分开，支持随证据调整 | 有限指令冒烟 |
| [/relationship-boundaries](skills/relationship-boundaries/SKILL.md) · 关系与边界 · [使用说明](docs/skills/relationship-boundaries.md) | 介绍渠道与能力背书分开，拒绝不要求补偿性帮助 | 本轮改动待行为重测 |
| [/gift-planning](skills/gift-planning/SKILL.md) · 送礼规划 · [使用说明](docs/skills/gift-planning.md) | 先确认需求再设计惊喜，未知偏好不靠身份标签填补 | 有限指令冒烟 |
| [/manager-of-managers](skills/manager-of-managers/SKILL.md) · 管理管理者 · [使用说明](docs/skills/manager-of-managers.md) | 决定、责任和代价要一起落地；安全合规公平不能用结果交换 | 有限指令冒烟 |
| [/hiring-assessment](skills/hiring-assessment/SKILL.md) · 招聘评估 · [使用说明](docs/skills/hiring-assessment.md) | 反馈分事实、推断与偏好；潜力是开放假设，不是标签 | 有限指令冒烟 |

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

---

## 中文版本

把工程判断、团队管理和沟通经验，变成可以直接调用的 AI 技能。

[快速开始](#安装与调用) · [常用指令](#常用指令) · [方法目录](#方法目录) · [更新记录](CHANGELOG.md) · [贡献方法](CONTRIBUTING.md) · [MIT 许可](LICENSE)

**不确定该从哪开始，就用 Ask Liyuk。** 整个仓库承载个人方法：规划、评审、指标、复盘、表达、经历自查、人际互动与日常选择。Ask Liyuk 帮你选路，各项技能完成具体任务。

当前版本 **0.5.0 / preview**：共二十一项技能，五项工程技能迁自 [engineering-decision-skills](https://github.com/Liyuk/engineering-decision-skills)，两项人际技能迁自 [RelationForge](https://github.com/Liyuk/relation-forge)，其余从博客等素材提炼。新提炼的方法仍需要真实使用与本人校准。英文为主，中文提供完整对照；采用 [Agent Skills 文件格式](https://agentskills.io/specification)。

## 安装与调用

先克隆仓库，再按客户端复制所需技能。以下以 Ask Liyuk 为例：

```sh
git clone https://github.com/Liyuk/skills.git liyuk-skills
cd liyuk-skills
```

**Claude Code：用 `/名称` 调用。**

```sh
mkdir -p ~/.claude/skills
cp -R skills/ask-liyuk ~/.claude/skills/
```

安装后输入：

```text
/ask-liyuk 我要把一个失败项目写进自评，但不知道先复盘还是先写。
```

如果通过本仓库的插件 marketplace 安装，则带插件前缀：`/liyuk-skills:ask-liyuk`。文件安装与插件安装的命名规则见 [Claude Code 官方说明](https://code.claude.com/docs/en/skills#choose-where-skills-load)。插件清单经过静态检查，客户端插件安装尚未逐一验证。

**Codex：用 `$名称` 调用。**

```sh
mkdir -p ~/.codex/skills
cp -R skills/ask-liyuk ~/.codex/skills/
```

```text
$ask-liyuk 我要把一个失败项目写进自评，但不知道先复盘还是先写。
```

Codex CLI/IDE 也可通过 `/skills` 选择技能；它是选择入口，不是将每项技能写成 `/名称`。[OpenAI 官方调用说明](https://developers.openai.com/blog/eval-skills#2-create-the-skill)

只安装 Ask Liyuk 时，它推荐方法与下一步；执行专项任务还需要复制对应目录。已安装同名旧技能时先检查版本并选择一个来源，避免覆盖自己的修改或装入重复入口。

## 第一次怎么用

例如你要评审一个技术方案，把方案材料接在 `/tech-review` 后；如果还没分清是要定位问题、选择投入还是审查方案，先问 `/ask-liyuk`。Codex使用相应的 `$名称`。

下面是构造的输入示例，安装对应技能后可替换成自己的材料：

```text
/situational-leadership
成员维护现有服务很熟练，第一次负责数据迁移却判断不了回滚条件。
他愿意负责，目标和权限已清楚。我该补哪些指导，什么时候可以减少干预？
```

预期得到具体任务的判断依据、负责人要补的支持、成员继续负责的部分与调整信号。缺少资料时保留未知；输出仍需结合实际情况核对。

`ask-liyuk`、`distill-experience`、`project-diligence` 需要主动选择；其他方法可以在任务匹配时被发现。具体发现与调用以客户端实际能力为准。

## 常用指令

| 要做什么 | Claude Code 文件安装 | Codex |
| --- | --- | --- |
| 不知道该用哪个方法 | `/ask-liyuk` | `$ask-liyuk` |
| 评审已有技术方案 | `/tech-review` | `$tech-review` |
| 判断该指导、支持还是授权 | `/situational-leadership` | `$situational-leadership` |
| 把自己的经历蒸馏成方法 | `/distill-experience` | `$distill-experience` |
| 方案看似正确却没解决问题 | `/problem-location` | `$problem-location` |
| 刚进入陌生团队或业务 | `/new-context-onboarding` | `$new-context-onboarding` |
| 统筹多位负责人和团队 | `/manager-of-managers` | `$manager-of-managers` |
| 准备面试追问、整理候选人证据 | `/hiring-assessment` | `$hiring-assessment` |
| 主动判断新业务或创业项目 | `/project-diligence` | `$project-diligence` |

安装对应技能后，在指令后直接写问题或材料即可。Claude Code 插件安装时，以上 `/名称` 改为 `/liyuk-skills:名称`。

## 方法目录

下表以 Claude Code 文件安装的 `/名称` 展示；Codex 对应 `$名称`，插件调用需加上述前缀。

完整技能目录见上方英文主版的 [Skill catalog](#skill-catalog)，包含全部技能名称、使用说明链接与验证状态。

来源、作者校准和行为验证分别展示。迁入不等于成熟；有限指令冒烟不等于效果证明。详细输入、产物与判断依据见各项使用说明。

每项技能仍可单独复制；Ask Liyuk 的组合路径按实际需求选择。只有导航入口时，它可以推荐下一步，但不能假装已执行未安装的方法。

## 为什么这样做

素材来自项目、博客、已有技能和成长问题。作者提供经验与校准，AI 帮助整理候选方法与检验反例。来源、事实与推断分别记录；缺少证据时保留缺口，避免把顺畅的表达当成可靠结论。

我们借鉴 Matt Pocock 的技能分层、导航和小能力组合。[设计分析](docs/research/2026-10-14-matt-skills-design.md)、[首版设计](docs/design/2026-10-14-v1-design.md)、[人际扩展](docs/design/2026-10-14-v0.2-social-design.md)和[方法细节补充](docs/design/2026-10-14-v0.3-depth-design.md)说明借鉴和取舍。[本轮入口与目录设计](docs/design/2026-10-14-v0.4-usability-design.md)及[书籍视角与资料范围](docs/research/2026-10-14-book-perspectives.md)记录新的补充。[v0.5博客方法蒸馏](docs/design/2026-10-14-v0.5-blog-distillation-design.md)说明新增五项方法及来源范围。[书籍识别能力与情景领导力](docs/research/2026-10-14-book-recognition-and-situational-leadership.md)说明当前证据与理论版本。没有复制 Matt 的技能正文。

## 验证与维护

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_repo.py
.venv/bin/python scripts/sync_catalog.py --check
```

结构校验不证明模型行为有效。现有案例和本轮实际验证分别记录在 [v0.5验证报告](evals/reports/v0.5.md)（[v0.4记录](evals/reports/v0.4.md)、[人际扩展记录](evals/reports/v0.2.md)、[首版记录](evals/reports/v0.1.md)）；新增 expected_output 是检查标准，不是运行结果。来源固定版本与指纹见 [sources.json](catalog/sources.json)。

修改方法时补充能观察判断变化的案例。个人原始材料、公司内部信息和私人档案留在自己的工作区；公开贡献使用合成或明确可公开的材料。

项目修改采用 **分支 → 检查 → PR → 合并** 的同步方式。文档补充与修复也在对应 PR 分支提交；由维护者决定合并到 `main`。具体规则见 [PR 同步流程](docs/workflows/pr-sync.md)。

## 许可

仓库原创指令、代码和文档采用 [MIT License](LICENSE)。允许使用、修改、再分发与商用，复制或分发时须保留相应版权及许可声明；内容按现状提供，不作担保。条款以各包的LICENSE原文为准。[MIT标准文本](https://opensource.org/license/mit)

各技能包带有自己的LICENSE，独立复制时一并保留。迁入内容保留原始版权与来源；外部书籍、博客原文、框架图表及商标不因被引用而转为本仓库MIT授权，仍按各自条款处理。本项目提供原创方法适配与出处，不分发第三方全文。

内容许可与文件格式是两件事：开源许可用MIT，技能组织遵循Agent Skills规范；Claude Code与Codex的调用写法见上方安装说明。
