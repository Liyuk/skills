# Social skill baseline — no draft instructions

Generated 2026-10-14 by the delegated evaluator before reading any of the seven skill drafts. One sample per task, in a shared conversation context; this is not an independent repeated benchmark. All scenarios are synthetic.

## 1. Conflict
Prompt: 产品坚持既定上线日期，工程说现有容量不可能按期完成。帮我解决双方冲突。没有更多信息。

Response: 先把争论转换为可决策的取舍：日期为什么不能动、必须上线的最小范围是什么、工程容量判断基于哪些任务和依赖。当前只有双方的立场，不能判断谁对。安排一次短对齐，双方先确认共同目标，再把日期、范围、质量和资源放到同一张表里。准备三个方向：缩减范围保日期、保范围调整日期、补资源并检查交接成本。工程给每个方案列出估算依据和风险，产品说明业务损失；最终由拥有上线取舍权的人明确选择并记录承担的风险。可以开场说：“我们先对齐这次上线必须实现的结果，再看现有容量下哪些组合成立。”

## 2. Conversation preparation
Prompt: 同事总在最后一刻请我帮忙，我想拒绝反复出现的临时请求。帮我准备这次谈话。

Response: 先明确边界：你愿意提供哪种帮助，什么时候能接，哪些临时请求不能接。谈话用具体事件和对工作安排的影响，不评价同事的人品。可以说：“最近几次临时请求让我需要调整已经安排好的工作。我以后无法默认当天接下这类任务。你可以提前告诉我需求和截止时间，我会根据当时安排确认；特别紧急的情况我们一起找负责人排优先级。”如果对方说只是帮一次，可以回答：“我理解着急，但这次我无法承诺完成。我可以告诉你下一步找谁确认。”你没有提供具体频次和影响，谈话时只使用你能确认的事实。

## 3. One-on-one
Prompt: 下属希望接核心工作，经理以为他是想晋升。我要准备这次一对一。

Response: 先把经理的猜测当作待核实信息。开场：“你提到希望做核心工作，对你最重要的是技术挑战、业务影响、成长机会，还是别的东西？”接着问期待承担什么责任、需要什么支持和怎样判断工作适合。若对方明确希望晋升，再说明晋升标准与当前差距；若没有，不把谈话强行转成晋升讨论。谈话可以落在一次可控的核心任务尝试，明确范围、决策权限、支持人和回顾时间。任务、晋升和岗位变动都应按实际权限承诺。

## 4. Recommendation boundary
Prompt: 朋友请我推荐一个我不认识的人。我怕拒绝伤感情，该怎么办？

Response: 把介绍渠道和能力背书分开。你可以帮助转达信息，但不能推荐你不了解的人适任。可以说：“我愿意帮你看看怎么联系，但我不认识他，也没有合作经验，所以没法做能力推荐。如果你有履历和具体机会，我可以征得对方同意后转发，并说明我没有验证他的能力。”若机会要求真实的推荐意见，直接说目前无法提供。给出能做的帮助，无需为了保关系替未知情况背书。

## 5. Gift
Prompt: 想给同事送个惊喜礼物，预算适中，但不知道个人喜好。帮我想想。

Response: 先确认场合、预算上限、你们关系的熟悉程度，以及公司是否有相关规定。喜好未知时，选择金额适当、使用门槛低、容易退换或让对方自己选的礼物方向，配一句与实际合作有关的感谢。可以从办公日常、小型可共享礼物、可自主选择的礼物形式中筛选；不要根据性别或职位猜偏好。若想保留惊喜，可以用闲聊了解平时使用习惯，或只让包装和感谢成为惊喜。食物要先确认限制；没有这些信息时不宜定具体产品。你可以先提供场合和预算，我再缩小方向。

## Assessment

No clear unsafe or fabricated-fact failure appeared in these five responses. The baseline already separates assumptions from facts, does not manufacture motives or named products, and uses reasonable boundaries.

Observed omissions rather than asserted failures:
- Conflict response does not make follow-up ownership and observation conditions explicit.
- Conversation response gives a draft immediately; it does not explicitly distinguish private desired outcomes from mutually observable success criteria, and doesn't ask what commitments the user genuinely wants to offer.
- One-on-one mentions authority but lacks a specific check that both parties understand the same agreed action.
- Recommendation response is sound but offers no explicit post-boundary relationship maintenance step beyond practical help.
- Gift response remains generic; no source-specific Liyuk method can be assessed without the source and instructions.

These are candidate improvement dimensions, not evidence that each new skill is necessary or author-endorsed. A single contextual sample cannot establish improvement, consistency, or robustness under pressure. Forward smoke should report compliance with supplied instructions only.
