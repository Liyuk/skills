# Liyuk Skills

把自己的工程经验和判断方法，变成能与 AI 一起使用的小能力。

**不确定该从哪开始，就用 Ask Liyuk。** 整个仓库承载个人方法：规划、评审、指标、复盘、表达、经历自查、人际互动与日常选择。Ask Liyuk 帮你选路，各项技能完成具体任务。

当前版本 **0.4.0 / preview**：共十六项技能，五项工程技能迁自 [engineering-decision-skills](https://github.com/Liyuk/engineering-decision-skills)，两项人际技能迁自 [RelationForge](https://github.com/Liyuk/relation-forge)。新提炼的方法仍需要真实使用与本人校准。中文优先，采用 Agent Skills 文件格式。

## 先用一个

先克隆仓库，再复制所需目录。以下以 Ask Liyuk 为例：

```sh
git clone https://github.com/Liyuk/skills.git
mkdir -p ~/.codex/skills
cp -R skills/skills/ask-liyuk ~/.codex/skills/
```

在 Codex 中使用 `$ask-liyuk`。只安装这个入口时，它推荐方法与下一步；执行专项任务还需要复制对应目录。已安装同名旧技能时先检查版本并选择一个来源，避免覆盖自己的修改或装入重复入口。

```text
$ask-liyuk
我要把一个失败项目写进自评，但不知道先复盘还是先写。请根据已有材料推荐下一步。
```

Claude Code 可以将所需目录复制到自己的技能目录，也可使用仓库提供的插件 marketplace。插件清单目前经过静态检查，客户端插件安装尚未逐一验证。不同宿主的调用与发现行为请以实际结果为准。

## 方法目录

<!-- skills-catalog:start -->

| 技能 | 核心判断 | 行为验证 |
| --- | --- | --- |
| [Ask Liyuk](skills/ask-liyuk/SKILL.md) · [使用说明](docs/skills/ask-liyuk.md) | 先识别要作的决定或交付物，只走当前需要的路径 | 本轮改动待行为重测 |
| [技术规划](skills/tech-planning/SKILL.md) · [使用说明](docs/skills/tech-planning.md) | 技术动作必须对应业务结果与能力缺口，并比较继续现状等选择 | 本轮改动待行为重测 |
| [技术方案评审](skills/tech-review/SKILL.md) · [使用说明](docs/skills/tech-review.md) | 只报告有依据且会影响决定的问题，足够好可以通过 | 结构检查 |
| [指标判断](skills/metric-decision/SKILL.md) · [使用说明](docs/skills/metric-decision.md) | 口径与可比性未确认前，指标变化不能直接充当成果或因果证据 | 有限指令冒烟 |
| [工程复盘](skills/management-retro/SKILL.md) · [使用说明](docs/skills/management-retro.md) | 分清事实、解释与下一轮动作，不把事后解释写成根因 | 本轮改动待行为重测 |
| [工程汇报](skills/eng-reporting/SKILL.md) · [使用说明](docs/skills/eng-reporting.md) | 先确定读者要作的决定，表达不能强化未知或补造收益 | 本轮改动待行为重测 |
| [项目经历 Review](skills/experience-review/SKILL.md) · [使用说明](docs/skills/experience-review.md) | 团队结果与个人贡献分开，材料缺口不等于没有能力 | 本轮改动待行为重测 |
| [蒸馏经验](skills/distill-experience/SKILL.md) · [使用说明](docs/skills/distill-experience.md) | 事实、解释与方法分开，明确确认只覆盖对应条件 | 本轮改动待行为重测 |
| [人际深度解析](skills/person-deep-analysis/SKILL.md) · [使用说明](docs/skills/person-deep-analysis.md) | 按材料形成有限解释，单一片段不能补成稳定人格 | 有限指令冒烟 |
| [互动风险分析](skills/interaction-risk-analysis/SKILL.md) · [使用说明](docs/skills/interaction-risk-analysis.md) | 行动保护不必等到证明恶意，效果和利益不能证明主观意图 | 有限指令冒烟 |
| [冲突对齐](skills/conflict-alignment/SKILL.md) · [使用说明](docs/skills/conflict-alignment.md) | 同层资源权限死结停止重复说服，整理材料上升支持 | 有限指令冒烟 |
| [沟通准备](skills/conversation-preparation/SKILL.md) · [使用说明](docs/skills/conversation-preparation.md) | 先澄清，再反馈，最后承诺；草稿和共识是不同状态 | 本轮改动待行为重测 |
| [1-on-1 对齐](skills/one-on-one/SKILL.md) · [使用说明](docs/skills/one-on-one.md) | 先有共同验收标准；纯资源问题可保留成员负责，权限缺口负责人介入 | 有限指令冒烟 |
| [情景领导力](skills/situational-leadership/SKILL.md) · [使用说明](docs/skills/situational-leadership.md) | 同一个人按任务分别判断；能力投入与组织权限分开，支持随证据调整 | 有限指令冒烟 |
| [关系与边界](skills/relationship-boundaries/SKILL.md) · [使用说明](docs/skills/relationship-boundaries.md) | 介绍渠道与能力背书分开，拒绝不要求补偿性帮助 | 本轮改动待行为重测 |
| [送礼规划](skills/gift-planning/SKILL.md) · [使用说明](docs/skills/gift-planning.md) | 先确认需求再设计惊喜，未知偏好不靠身份标签填补 | 有限指令冒烟 |

<!-- skills-catalog:end -->

来源、作者校准和行为验证分别展示。迁入不等于成熟；有限指令冒烟不等于效果证明。详细输入、产物与判断依据见各项使用说明。

每项技能仍可单独复制；Ask Liyuk 的组合路径按实际需求选择。只有导航入口时，它可以推荐下一步，但不能假装已执行未安装的方法。

## 为什么这样做

素材来自项目、博客、已有技能和成长问题。作者提供经验与校准，AI 帮助整理候选方法与检验反例。来源、事实与推断分别记录；缺少证据时保留缺口，避免把顺畅的表达当成可靠结论。

我们借鉴 Matt Pocock 的技能分层、导航和小能力组合。[设计分析](docs/research/2026-10-14-matt-skills-design.md)、[首版设计](docs/design/2026-10-14-v1-design.md)、[人际扩展](docs/design/2026-10-14-v0.2-social-design.md)和[方法细节补充](docs/design/2026-10-14-v0.3-depth-design.md)说明借鉴和取舍。[本轮入口与目录设计](docs/design/2026-10-14-v0.4-usability-design.md)及[书籍视角与资料范围](docs/research/2026-10-14-book-perspectives.md)记录新的补充。[书籍识别能力与情景领导力](docs/research/2026-10-14-book-recognition-and-situational-leadership.md)说明当前证据与理论版本。没有复制 Matt 的技能正文。

## 验证与维护

```sh
cd skills
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_repo.py
.venv/bin/python scripts/sync_catalog.py --check
```

结构校验不证明模型行为有效。现有案例和本轮实际验证分别记录在 [本轮验证报告](evals/reports/v0.4.md)（[人际扩展记录](evals/reports/v0.2.md)、[首版记录](evals/reports/v0.1.md)）；新增 expected_output 是检查标准，不是运行结果。来源固定版本与指纹见 [sources.json](catalog/sources.json)。

修改方法时补充能观察判断变化的案例。个人原始材料、公司内部信息和私人档案留在自己的工作区；公开贡献使用合成或明确可公开的材料。

项目修改采用 **分支 → 检查 → PR → 合并** 的同步方式。文档补充与修复也在对应 PR 分支提交；由维护者决定合并到 `main`。具体规则见 [PR 同步流程](docs/workflows/pr-sync.md)。

## 许可

MIT，保留迁入技能的原始许可与来源。博客仅作为方法出处，不在技能包里复制整篇文章或第三方参考全文。
