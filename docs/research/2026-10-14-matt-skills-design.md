# Matt Pocock Skills 设计分析

分析日期：2026-10-14。固定版本：`49dd158d1076134a641b33efb035946536778336`。
源码：https://github.com/mattpocock/skills/tree/49dd158d1076134a641b33efb035946536778336 。本轮读取 README、AGENTS、SCOPE、调用策略、插件清单、版本配置与 CI，并抽样阅读 ask-matt、grill-with-docs、to-spec、implement、codebase-design、teach 等技能。分析公开设计与指令，不推测作者内部系统。

## 1. 总体模型

仓库是作者日常方法的集合。一个技能处理一种任务，共享方法与术语可以在多个任务中复用。Ask Matt 负责告诉用户选哪个技能、如何连接流程，不替代各项能力。

主流程是理解意图 → 必要的原型验证 → 规格 → 可执行任务 → 实现与测试 → 评审 → 环境复盘。排障、任务分诊、架构调查等从不同起点进入这条流程。不是每次都运行所有步骤。

出处：[Ask Matt](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/ask-matt/SKILL.md)。

## 2. 分层与调用

| 层 | 例子 | 职责 |
| --- | --- | --- |
| 用户入口 | ask-matt、grill-with-docs、to-spec、implement | 人主动选择目标和工作流 |
| 可复用方法 | tdd、grilling、code-review、domain-modeling | 对应任务时可以由模型使用 |
| 术语和参考 | codebase-design、各技能参考文件 | 让不同阶段理解一致 |
| 工作区产物 | GLOSSARY、ADR、spec、tickets、handoff | 保存任务上下文和已经形成的决定 |
| 分发维护 | README、插件、调用元数据、版本与更新脚本 | 让用户找到、安装并更新成熟能力 |

用户调用技能同时设置 Claude 的 `disable-model-invocation: true` 和 Codex 的 `policy.allow_implicit_invocation: false`。方法技能默认允许自动发现。Ask Matt 可以推荐用户入口，不能假定能自动调用这些入口；引用其他方法前需要读取真实技能入口。支持调用工具的宿主与只能读取文件的宿主应分别适配。

出处：[调用约定](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/.agents/invocation.md)。

## 3. 内容结构与发布

技能按 engineering、productivity、misc、in-progress、deprecated 分桶。插件明确列出 engineering 与 productivity 的成熟技能，README 与 human-facing docs 同步。未成熟技能不进入正式插件。

插件版本和 package.json 同步，用 Changesets 维护版本；安装方式分为受管理的插件和可修改的文件副本。作者本地使用符号链接保持源码与安装内容一致，但符号链接是否能经过插件缓存复制，需要单独验证。

出处：[仓库约定](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/AGENTS.md)、[插件清单](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/.claude-plugin/plugin.json)。

## 4. 有效机制与适用限制

以下是设计分析，不是对流行原因或总体效果的实证结论：

- 入口说清“什么时候用”，减少记忆整套技能的负担。
- 方法按任务组织；复用同一个推理动作，避免每个技能重复一套大流程。
- 用户保有方向与阶段选择权，技能提供具体执行纪律。
- 状态保存在任务工作区，技能目录保存方法，二者职责分开。
- 检验围绕可观察行为；复盘把实际失误转为环境改进。
- 分发目录、调用元数据和路由保持一致，否则入口会推荐不存在或职责已变化的能力。

这些设计也有维护成本：路由与文档存在重复；技能间依赖需要安装配套能力；部分流程要求特定调用工具、任务跟踪器和上下文操作。固定版本中的旧 ADR 仍记载推迟 Codex 插件，但当前 README 已列出 Codex 插件安装，说明历史决策不能代替现行行为依据。实际客户端安装仍需验证。

## 5. 应借鉴什么

Liyuk 的首要资产是工程判断、结果与证据、成长自查和表达方法。因此采用入口＋独立方法＋参考＋案例的结构，而不是复制 Matt 的整套编码工作流。保留五项现有工程技能，新增经历审查与本人经验蒸馏；Ask Liyuk 做导航和最少必要的问题澄清。

第一版采用平铺成熟技能目录，实验候选在 docs 中管理；暂不引入 bucket、Changesets、issue 状态机或平台专用配置系统。成熟技能不足十项时，这些复杂度还没有实际收益。插件清单显式列出发布技能，单项安装保持自包含。

整个仓库承载“蒸馏 Liyuk”，Ask Liyuk 是统一入口。新增方法的作者立场需要本人确认；项目的存在不等于已经提炼出可迁移的方法。
