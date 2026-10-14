# situational-leadership 重点审查

## 实际范围与结论

只读检查新包 SKILL.md、两个 references、10例 evals、agents/openai.yaml、catalog/skills.json 对应项、生成 docs/skills、README、插件清单、Ask Liyuk 正文／地图／task-flows及验证报告。使用 code-review-and-quality 的正确性与边界框架。没有修改仓库，没有真实管理执行，也没有读完整书或认证课程。

未发现可确认的阻断问题。四种典型组合与已核对公开SLII概念相符；新包与one-on-one按选择支持方式／整理谈话的分工清楚。包内运行参考保持本地，目录和导航可找到方法。不能将此结论推广为所有情境都不会错分。

## 可执行建议（非阻断，未在十题观察到实际错误）

1. **把D4的信心条件写进表格，消除与D3的匹配重叠。** SKILL.md:25把信心波动列为D3，:26却只要求“可靠独立完成且愿承担”。愿意继续但信心反复的成员可能同时满足两行；目前:19已提醒分开记录意愿与信心，典型第3题也正确选支持，因此不能报成已发生错分。可将D4改为“可靠独立完成、愿承担且当前信心稳定／支持需求较少”，并增加“可靠独立完成、很愿意但反复担心”的相邻反例，以确认不会因为意愿高减少所需支持。

2. **补一个明确拒绝或非典型组合探针，验证不强配分支。** :28已经明确信息不匹配时不强配，但现有10题主要为四类典型、外部阻塞和材料冲突。可加“会做且持续明确拒绝该任务，原因尚未确认”或“尚未尝试、不会做且不愿承担”，要求先确认拒绝原因、职责与条件，不能仅按编号把所有拒绝写成D2，不能编造同意继续练习。当前文本能够容纳此边界，但尚无该场景的原始响应证据。本次未将新增审查候选当成已运行用例。

## 来源与归属

实际打开并核对三个公开页面：

- [Ken Blanchard, Explore the Versatility of SLII](https://www.kenblanchardbooks.com/explore-the-versatility-of-slii/)支持任务特定D分类与四种风格；本包没有把任务状态当整个人等级。
- [Randy Conley, Four Reasons Why Flexing Your Leadership Style Builds Trust](https://www.blanchard.com/blog/four-reasons-why-flexing-your-leadership-style-builds-trust)支持可迁移能力、动机与信心区分以及指导／支持组合。当前表格大体相符，上述D4条件建议针对简写的歧义。
- [CLS, The Four Leadership Styles of Situational Leadership](https://situational.com/blog/the-four-leadership-styles-of-situational-leadership/)足以核对它采用Hersey/Performance Readiness与Telling／Selling语言，以及低支持不等于失联。该页不是SLII出处；包内只用作版本边界，未把其S1/S2说明拼进SLII判断。

本包在正文开头、references/sources和例子中明确标记：公开概念来自Blanchard；工程判据与例子为AI候选适配；Liyuk确认只覆盖共同验收、资源责任、权限／跨层介入与一线进度原则。没有发现作者确认被扩大到D分类或全部管理动作的明确声称。目录的distilled／partial和通用“素材提炼”展示较粗，但文档链接有清楚范围，本次不把它报成具体错误。

## 未知及行为证据限制

十题原始响应见 situational-forward.md。六题基线见 situational-baseline.md。前向新增显式支持组合与复看语言，典型题没有观察到硬配等级；但同一代理有基线上下文且读过expected_output，本次非盲测，不证明因果增益或现实效能。四个新增题没有旧包对照。拒绝任务等未匹配情境未实际重复评测，按正文可以处理，不等于已验证。

## 结构检查

在收到父侧避免重复广泛测试的消息前，本代理已执行一次：

- 普通shell的 `python` 不存在，三条命令最初均exit 127；未当作通过。
- 改用仓库配置 `.venv/bin/python -m unittest discover -s tests -v`：23 tests，OK，exit 0。
- `.venv/bin/python scripts/validate_repo.py`：包、参考、来源、调用策略、用例及插件清单验证通过，exit 0。
- `.venv/bin/python scripts/sync_catalog.py --check`：Checked 35 catalog artifacts，exit 0。

随后未重复广泛检查。以上验证结构和清单一致性，不运行10个管理行为用例，也不证明建议效果。

## 本次修订复查（2026-10-14）

父侧已处理上述两项非阻断建议。本代理仅读取修订后的SKILL.md与新增 `willing-but-needs-support`、`explicit-refusal-not-d2` 两项eval，并实际输出建议；没有重跑前十题或广泛测试。

- D4表格现明确要求“已可靠独立完成、愿承担且当前信心足够”。新增第11题实际响应区分了愿意与信心，提供风险讨论与有限支持，没有因可靠积极就默认D4低支持。原先指出的条件简写重叠已被处理。
- 不匹配分支现明确“成员明确拒绝任务时先核对原因、职责与条件，不把拒绝统一解释成缺信心，也不编造同意练习”。新增第12题实际响应未强配D2，未编造能力缺口、练习意愿或同意承担。原先缺少明确拒绝的实际响应记录已补充。

当前记录累计12题实际文本响应，前十题来自初次新包版本，两题来自本次修订；不是最终版本全量12题重测。两题均可见expected_output，不能宣称盲测、因果增益或真实执行。以上重点建议已处理，本次未发现新增可确认的阻断问题。
