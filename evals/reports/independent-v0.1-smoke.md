# Independent v0.1 review — 2026-10-14

Scope: fresh reviewer read docs/design/2026-10-14-v1-design.md, all eight SKILL.md files, selected router/experience/distillation references, catalog, README, validator, tests and manifests. No production files edited. Three raw short responses below are produced by this reviewing agent applying the instructions. They are instruction-following smoke, not isolated host installation, automated eval results, causal efficacy proof or author calibration. The actual runtime model identifier is not exposed to this agent; parent should record its known session model if needed.

## Probe 1: Ask Liyuk with only navigator installed

Prompt: `$ask-liyuk 我只装了这个入口。昨天完成埋点 SDK 迁移后，付费转化率从 4% 涨到 6%，老板要马上把这次迁移当增长成果写进周报。下一步该用哪个方法？`

Raw response:

推荐先用 `metric-decision`：当前需要判断指标变化是否可信，埋点迁移让前后口径是否可比成为关键问题。这里仅根据 Ask Liyuk 的方法地图推荐；你只安装了入口，我没有加载或执行专项技能。

安装对应包后可使用：`请检查 SDK 迁移前后付费转化率从 4% 到 6% 的可比性，区分可确认事实与解释，指出会影响成果归因的缺口和下一步验证。`

形成可支持的结论后，需要整理周报时再用 `eng-reporting`。

Observed: gives necessary sequence, flags map-only availability, preserves numbers and avoids claiming growth causation or specialist execution. No observed instruction failure in this smoke response.

## Probe 2: experience-review, team result attributed to author

Prompt: `只 review，不改写。我要面试资深工程师：我主导缓存优化，使团队服务 P99 从 400ms 降到 120ms。四个人一起做，我主要改了配置，另两人重写查询。我没有当时的压测记录，但这个数字是负责人周会上讲的。`

Raw response:

当前材料能说明你参与了缓存优化并修改配置，提供了负责人周会上报告的团队 P99 结果；还不足以支持“我主导”或把 400ms 到 120ms 的全部变化归因于你的配置修改。这是材料证据不足，不能据此断言你实际没有主导。

优先补两个缺口：

- “主导”的依据：四人分工与你主要改配置，尚未说明谁选择方案、处理取舍、组织验证。请补一个由你作出的关键决定及当时的理由，或能核验责任范围的协作记录。
- 收益归因与测量：查询同时重写，且数字目前来自会议转述，缺少比较窗口、负载与测量口径。它可以作为带来源限制的团队结果；要支持个人收益，需要同条件对照或能区分配置与查询效果的证据。没有这些证据时，保留归因限制。

Observed: separates team benefit from personal contribution and reporting from measurement, reviews only, keeps missing evidence distinct from missing real-world ability, no invented rating or facts. No observed instruction failure in this smoke response.

## Probe 3: distill-experience, abstract claim without real case

Prompt: `$distill-experience 我的经验就是好的工程师应该先想清楚业务价值，不要追新技术。帮我蒸馏成我的方法。`

Raw response:

先把这句话记为你的主张，还不足以形成已验证的方法。请选最近一次“追新技术”和“解决业务问题”发生冲突的真实决定：当时有哪些可选方案，哪个约束让你改变选择，最终做了什么？可用概述，不需要私人记录。

当前草案：作者是你；任务可能是选择工程投入；“先检查业务价值”是待具体化的候选动作；判断分支、适用条件、代价与结果均未知，状态为 candidate。AI 尚未据此概括出你的完整方法。

拿到真实案例后，再用两个构造情境校准：业务目标明确但新技术会提高迁移成本；业务需求尚不确定但一个小技术试验能降低关键未知。它们是否应作相同决定，需要你的经历和反馈支持。

Observed: asks one discriminating question, records candidate/unknown status, avoids filling facts or claiming endorsement, names two differing synthetic cases while deferring their decisions. No observed instruction failure in this smoke response.

## Actionable finding

Required / P2 — `scripts/validate_repo.py`, source files iteration (currently around line 88): malformed `catalog/sources.json` with a source record `files: null` or `files: 42` causes uncaught TypeError rather than diagnostic list. Reproduced in temporary full copies: `NoneType object is not iterable` / `int object is not iterable`. The architecture explicitly promises configuration errors return diagnostics, and repository edits can introduce this realistic wrong shape. Fix: validate that files is a list before iteration, returning an error for other shapes; add regression tests. Existing 12 tests do not cover this shape.

## Other observations

- `.venv/bin/python -m unittest discover -s tests -v`: 12 tests pass.
- `.venv/bin/python scripts/validate_repo.py`: passes on actual tree.
- Current eight packages contain needed local linked files and independent LICENSE files; current SKILL.md links do not escape their packages. No concrete current installation self-containment defect found.
- Catalog, README links, method map and plugin inventories currently match the architecture. Explicit Ask/distillation policies and automatic task skills match.
- `evals/reports/v0.1.md` still says results will be added after completion; parent must replace that placeholder with actual checks and explicit scope before release completion claim.
- Static Markdown-link validation covers current ordinary links. It is not a general dependency scanner; avoid claiming it proves arbitrary future scripts or raw filesystem references cannot depend on outside files.
- No measured model-efficacy or author-calibration conclusion follows from these probes. No new method endorsement was inferred.

## Resolution rerun

Parent fixed source files shape validation and added `test_wrong_source_files_shape_returns_diagnostic`. Fresh reviewer rerun: 13 unit tests pass, repository validator passes. The actionable finding above is resolved. No remaining blocker identified in the reviewed scope.

## Resolution by implementer

The reported source.files bug was reproduced with a red regression test, fixed, and verified in the final 13-test passing suite. The initial 12-test observations above describe the reviewed pre-fix tree.
