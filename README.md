# Liyuk Skills

把自己的工程经验和判断方法，变成能与 AI 一起使用的小能力。

**不确定该从哪开始，就用 Ask Liyuk。** 整个仓库承载个人方法：规划、评审、指标、复盘、表达、经历自查、人际互动与日常选择。Ask Liyuk 帮你选路，各项技能完成具体任务。

当前版本 **0.3.0 / preview**：共十五项技能，五项工程技能迁自 [engineering-decision-skills](https://github.com/Liyuk/engineering-decision-skills)，两项人际技能迁自 [RelationForge](https://github.com/Liyuk/relation-forge)。新提炼的方法仍需要真实使用与本人校准。中文优先，采用 Agent Skills 文件格式。

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

### 用户主动调用

- [ask-liyuk](skills/ask-liyuk/SKILL.md)：根据问题选择方法和必要顺序。
- [distill-experience](skills/distill-experience/SKILL.md)：与作者还原真实经历，形成待确认的方法卡。

### 任务匹配时可使用

- [tech-planning](skills/tech-planning/SKILL.md)：业务约束下选择技术投入、优先级与验证路径。
- [tech-review](skills/tech-review/SKILL.md)：检查已有方案的证据、取舍与交付准备。
- [metric-decision](skills/metric-decision/SKILL.md)：核对指标口径、解释边界和下一步行动。
- [management-retro](skills/management-retro/SKILL.md)：从已完成工作中选择下次保留、改变或停止什么。
- [eng-reporting](skills/eng-reporting/SKILL.md)：把已有判断组织成读者能决策的汇报或总结。
- [experience-review](skills/experience-review/SKILL.md)：检查项目经历的个人贡献、判断、结果与证据。

### 人际、沟通与日常

- [person-deep-analysis](skills/person-deep-analysis/SKILL.md)：依据材料理解需求、立场与互动，不给现实人物定型。
- [interaction-risk-analysis](skills/interaction-risk-analysis/SKILL.md)：拆解可疑互动的要求、行为效果、风险和核验缺口。
- [conflict-alignment](skills/conflict-alignment/SKILL.md)：项目冲突先对齐共同目标、事实与决策权。
- [conversation-preparation](skills/conversation-preparation/SKILL.md)：把澄清、反馈、请求和可兑现承诺组织成谈话。
- [one-on-one](skills/one-on-one/SKILL.md)：上下级对齐目标、预期、支持与授权。
- [relationship-boundaries](skills/relationship-boundaries/SKILL.md)：明确求助、介绍、推荐、信息分享和承诺的边界。
- [gift-planning](skills/gift-planning/SKILL.md)：先理解人和场合，再选通用、定制或体验礼物方向。

以上均可按任务匹配使用。两项迁入技能保留已有方法；五项新提炼技能标为 preview，先用再调整。七项较薄的方法已补入按情境读取的详细方法与构造正反例；冲突升级与1-on-1支持诊断含本人确认的条件判断。例：`$ask-liyuk 朋友请我给不熟的人写推荐，我想帮忙但不想背书。该从哪开始？`

每项包都附带必要参考和许可，可单独复制。基本执行不要求能访问博客，也不依赖本仓库的其他目录。组合任务按实际需求选择，用户主动调用入口不会被自动串成工作流。

## 为什么这样做

素材来自项目、博客、已有技能和成长问题。作者提供经验与校准，AI 帮助整理候选方法与检验反例。来源、事实与推断分别记录；缺少证据时保留缺口，避免把顺畅的表达当成可靠结论。

我们借鉴 Matt Pocock 的技能分层、导航和小能力组合。[设计分析](docs/research/2026-10-14-matt-skills-design.md)、[首版设计](docs/design/2026-10-14-v1-design.md)、[人际扩展](docs/design/2026-10-14-v0.2-social-design.md)和[方法细节补充](docs/design/2026-10-14-v0.3-depth-design.md)说明借鉴和取舍。没有复制 Matt 的技能正文。

## 验证与维护

```sh
cd skills
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_repo.py
```

结构校验不证明模型行为有效。现有案例和本轮实际验证分别记录在 [本轮验证报告](evals/reports/v0.3.md)（[人际扩展记录](evals/reports/v0.2.md)、[首版记录](evals/reports/v0.1.md)）；新增 expected_output 是检查标准，不是运行结果。来源固定版本与指纹见 [sources.json](catalog/sources.json)。

修改方法时补充能观察判断变化的案例。个人原始材料、公司内部信息和私人档案留在自己的工作区；公开贡献使用合成或明确可公开的材料。

## 许可

MIT，保留迁入技能的原始许可与来源。博客仅作为方法出处，不在技能包里复制整篇文章或第三方参考全文。
