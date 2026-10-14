# v0.4 forward instruction smoke

Same evaluation agent as baseline, after reading updated entries and scenario-needed book references. Five exact constructed baseline prompts repeated once. These are actual agent-authored responses, not CLI-host sessions, independent fresh-model samples, real-world outcomes, full inventory executions, a control experiment, or efficacy evidence. No external action performed.

## 1. Metric decision

Prompt: 保存成功率在埋点改版后从 81% 升到 94%，老板据此要马上批准整个保存链路的重写预算。没有分子分母、版本样本量和用户侧验证。请用指标判断给一个简短建议。

Response:
报表从81%升到94%是观测，用户保存成功是否改善仍未知。先核对两版的分子分母、去重与覆盖，尝试在同一批可关联任务上统一口径；无法统一则标记前后不可比。再查用户最终保存结果与超时重试，不能把数字直接作为整链路重写依据。为避免只找支持老板解释的证据，可预先问：如果重算后旧版也接近94%，或用户侧结果没变，这会否定什么？这项反证思路是外部决策视角的候选适配，不是测量验证的替代。先做能区分采集变化与产品变化的最小核验，后续预算仍需损失、瓶颈和方案代价。阈值和批准状态都不能凭空补。

Observation: 仍先做口径与用户结果核验；新增具体可推翻当前解释的观测。一次响应不能证明方法更有效。

## 2a. Conflict, constraints unclear

Prompt: 同级产品团队坚持全量上线，研发坚持分期上线，两边都说“业务最重要”。老板让我去说服研发，但我还不知道业务日期是否硬约束、剩余容量和验收结果。帮我判断下一步。

Response:
现在看到的是全量与分期的立场，还不知道各自需要保护什么，不能先认定研发不配合或存在权限死结。先确认客户/业务必须结果及日期依据、研发剩余容量与验收证据，并让双方说清哪些承诺能调整。再问共同用什么标准评选方案，例如被确认的必须结果与风险容忍，而非先要求接受某个方案。诉求和评价标准的提示来自外部谈判视角，不能据此替当事人猜动机。若关键事实仍可核验，做最小核验；只有已证明确实无同层调整空间且缺权限/资源，才上升。当前最小动作是拿到这几项决定性信息，不是又安排一轮说服。

Observation: 更显式区分立场、待验证诉求与共同标准，未提前升级或猜动机。新增问题仍可能与旧版一般推理重叠。

## 2b. Conflict, known deadlock

Prompt: 补充：客户合同要求月底完整交付，研发已经验明至少还要三周；两边都不能改合同、加人或改跨团队优先级。同级协调三轮，事实无新增。下一步？

Response:
新增事实已表明当前层级没有可改变的合同、人员与优先级边界，且三轮无新增信息，应停止重复协调。整理共同结果、合同要求、已验工作量、不可调整边界、可选取舍及影响，再向有对应权限的上层提出具体决定与支持请求。上层究竟选择改承诺、改范围或给可用资源待其决定，不能预写批准或承诺加人有效。谈判中的诉求/标准探索不能制造授权，也不应成为继续追问同级的理由。原双方保留能做的准备与执行，负责人承担授权范围内的跨层取舍。

Observation: 保留作者确认的上升支持规则，外部谈判视角没有延迟升级或制造资源。

## 3a. One-on-one, coaching

Prompt: 成员要写架构决策文档，双方已明确验收：覆盖三个方案、成本与风险、推荐依据，并由产品和研发认可。他说没写过，已有资料能拿到，权限足够，希望我给路径；我很想自己写省时间。1-on-1 怎么处理？

Response:
目标、资料和权限已明确，先看具体任务能力缺口。可以问一两个会改变支持方式的问题：“已有尝试是什么，最难判断哪一步？你希望我先补路径还是看你的初步比较？”看答案后给相应结构、参照或反馈；成员明确请求指导时直接给必要路径，不强制问完一套问题。这种先保持好奇的提醒是外部教练视角的候选适配。成员仍负责文档与判断，经理可参与评阅一小段，不因省时间直接接管。收尾让他讲清下一步如何比较、何时需要支持，再共同确认复看范围。

Observation: 先问有限支持需求再给路径，并保留用户要指导可直接给的例外；未把固定问句顺序当强制。

## 3b. One-on-one, authority

Prompt: 同一成员已经能写文档，但需要两个上级部门确定优先级、开放受限信息。他无法调动这些部门，也无授权参加高层讨论。经理是否继续只给建议，让他自己想办法？

Response:
这是明确授权与跨层协调缺口，不能继续只问“你打算怎么办”。经理要介入需要上级决定的优先级和受限信息访问，把请求送到具有对应权力的负责人，确认授权范围及仍未取得的支持；该原则来自作者已确认分支。成员可以继续整理现有证据、提出选项和完成已授权的工作，经理介入不等于包办全文。教练式提问不能替代必须的支持，负责人还需掌握核心一线进度。未确认的授权与部门承诺仍列未知，不写成已落实。

Observation: 授权缺口触发负责人介入；明确候选教练视角不得代替作者支持原则。

## Limits

No hard violation observed in these five contextual responses. Baseline already handled the key safety and authority branches. Different wording cannot establish causal improvement or broad validation. Attribution language is especially visible here because this agent also reviewed provenance; actual host behavior may not include it automatically.
