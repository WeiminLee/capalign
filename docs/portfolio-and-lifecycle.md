# 设计结论：组合准入与能力生命周期

> 2026-10-23。本文是 [`../research/portfolio-lifecycle.md`](../research/portfolio-lifecycle.md)
> 的中文设计稿：把行级 \(\lambda\to I\) 扩到**宿主能力组合**。证据与引用以研究笔记为准；
> 本文只写设计，不写未跑的实验结论。
>
> 关系：`typed-introduction.md` 决定「这一行改不改」；本文决定「这一组新能力能不能
> 一起进宿主，以及进完之后库怎么维护」。两者共用同一套槽位、标签和测试合同。

## 1. 为什么要加这一层

行级正确不等于宿主安全。已部署宿主不是产物集合，是有名字、有描述、互相竞争的
**能力组合**。新增一条行级正确的卡，仍可能让宿主在原有任务上选错。

2026 的证据一致（数字均为他人测量）：

| 结果 | 数字 | 来源 |
|---|---|---|
| 已知有用技能集扩到 202-skill 库，通过率下降 | 最多 **21%** | Skill Shadowing, 2605.24050 |
| 其中归因于**选错**（shadowing）而非上下文 | 最多 **68%**；context overhead 与零不可分 | 同上 |
| 工具选择准确率，候选 <30 → 11,100 | **>90% → 13.6%** | RAG-MCP, 2505.03275 |
| 选择准确率随库大小（5–200） | **非线性相变**；语义混淆驱动，不是单纯数量 | Single-Agent Skills, 2601.04748 |
| 大工具空间、长工具输出导致的性能下降 | 最多 **85% / 91%** | Tool-Space Interference, Microsoft 2026 |
| 过早退休 | **−1.9pp**（主动伤害） | Library Drift, 2605.19576 |

两个限定。第一，Skill Shadowing 的 "context overhead" 是**固定**的描述税，不是
工具输出的**可变**税；后者可以极大（最重的 MCP 工具平均 557,766 tokens）。第二，
21% 是 202-skill 库上的数；材料宿主约 37 skills，可能低于拐点。论文必须报宿主
规模，不能直接搬数字。

结论不是「少装技能」，而是：

> **准入是集合的性质，不是行的性质；删除和新增一样危险。**

## 2. 对象

\[
H=(P_H,\;K_H,\;\Sigma_H,\;\rho_H,\;\beta_H)
\]

- \(P_H,K_H\)：能交的产物、已执行的作废检查（不变）。
- \(\Sigma_H\)：条目 \(\sigma_i=(name_i,d_i,P_i,K_i,prov_i)\)。\(d_i\) 是路由看到的
  **选择描述**；\(P_i\) 是它交付的产物；\(K_i\) 是检查；\(prov_i\) 是来源（工作、
  commit、包版本、证据根、refresh signal）。
- \(\rho_H\)：选择策略。不假设可观测，用探针测。
- \(\beta_H\)：预算——默认上下文 tokens、活跃工具数、延迟；固定描述税与输出税分开记。

一篇工作 \(W\) 产生卡 \(C(W)=\{c_1,\dots,c_n\}\)，每张卡有 \(\lambda\)。行级准入是
现有 \(\lambda\) 表；**组合准入**是对「拟加入条目集合 + 生命周期计划」的谓词。

## 3. 探针与两个条件

探针是声明式元组：

\[
q=(qid,\;text,\;owner,\;expected,\;kind),\qquad
kind\in\{\text{route},\text{deliver},\text{validity}\}
\]

- 宿主每个现有条目至少一条 `route` 探针；每张 install 卡至少一条 `deliver`
  探针；有 \(t_v\) 的加一条 `validity` 探针。
- 探针**在看结果前声明**，跨运行保留；skill 只写探针，不执行。执行归宿主或
  实验 harness，零捆绑/只建议的合同不变。

候选集 \(A\) **可准入**，当且仅当：

1. **交付（行）。** 每张卡按 \(\lambda\) 可装，合同是 fail-before → green →
   destroy-red。
2. **组合（集合）。** 加入 \(A\) 并执行生命周期计划 \(L\) 后：
   - 每条保留探针仍路由到 owner 并通过；
   - 每条新探针路由到新条目并通过；
   - 共存的卡之间没有 \(\kappa_H(a,b)=1\)（宿主级做法冲突）；
   - 默认面不超 \(\beta_H\)（超了用 `demote`，不是硬塞）；
   - 没有一条 live obligation 失去最后一个交付者（§5）。

主张因此变成两层：

> 一个交付的数只有在论文定义了该量、且运行在该量的作废条件内执行了该定义时才算数
> ——**并且，新能力准入后，宿主仍然选得中、交得出它原有的能力。**

短句：**green is not the paper's result; correct is not yet admissible.**

## 4. 非组合命题

**命题（非组合）。** 在「准确率随两两语义干扰 \(\mathcal{I}(\Sigma)\) 单调不增、
且 \(\mathcal{I}\) 在重叠对上超加」的声明选择模型下，行级可准入不封闭于并集：
存在 \(a,b\)，使 \(\{a\}\)、\(\{b\}\) 各自可准入，而 \(\{a,b\}\) 不可。

*见证。* 保留探针 \(q\) 的 owner 为 \(o\)，余量 \(m(q,\Sigma)>0\)。加 \(a\) 损失
\(\delta_a<m\)，加 \(b\) 损失 \(\delta_b<m\)，但交叉项 \(\gamma(a,b)>0\)（描述共享
facet，或做法冲突）使
\(m(q,\Sigma\cup\{a,b\})=m-\delta_a-\delta_b-\gamma<0\)。同一构造也可以越过
scaling law 的容量阈值，即使两次单独加入都没有越过。

代数很浅，设计后果不浅：**必须做集合测试**。我们不声称 scaling law 或干扰项是
自己的；模型来自 2601.04748，经验 regime 来自 2605.24050。

第二种、非选择型：两张卡各自与宿主 doctrine 一致，合起来却规定不兼容的做法
（例如一个把平衡体积钉在 0 K，一个钉在有限 \(T\)）。这是 \(\kappa_H(a,b)=1\)，
是**组合冲突**，不是 shadowing。两者都只有集合测试能抓到。

## 5. 生命周期动作与保留不变量

| 动作 | 触发 | 需要的证据 | 测试 |
|---|---|---|---|
| `bind` | 两侧齐，产物新 | 论文产物 + 仓库入口 | 改前败 → 改后过 → 删动作再败 |
| `author` | 义务缺入口 | 论文步骤 | 同上；不得伪造入口编号 |
| `extend` | 两侧齐，与现有条目同一问题 | 双向路由探针 | 老问题仍路由；邻居不吞新问题 |
| `add_validator` | 缺有效性 | 单侧作废句 | 违反条件的输入失败 |
| `merge` | 两条目**同一产物、同一做法、同一有效域**（即 `duplicate`）；检查并集覆盖双方 live obligations | 双方探针 + 无独有产物丢失 | 双方老探针仍过；条目数下降；干扰不升 |
| `demote` | 条目仍有用但遮蔽风险高 | 与 owner 的重叠 + 探针余量 | 默认面变小；显式调用仍可用 |
| `upgrade` | 新工作严格强于旧条目 | 新旧合同 | 新探针过；老探针过或显式退休 |
| `downgrade` | 新证据把旧条目的有效域**收窄**（仍有用，但不在它声称的全部范围） | 新作废句 + 老探针 | 收窄域内老探针过；域外失败或路由到 fallback |
| `retire` | 条目无 live obligation，且无保留探针依赖 | 来源 + 最后义务记录 | 删除不改变任何保留探针 |
| `quarantine` | 做法冲突，或有效性未评 | 冲突记录 | 默认不可选；不静默选边 |
| `refuse` | 入口缺义务 | 论文沉默 | 宿主不变 |

**保留即可达性。** 令 \(O\) 为所有**活跃工作**的义务并集；条目 \(\sigma\) 交付
\(o\) 时连边 \(o\to\sigma\)。则：

- **安全性：** 没有 live obligation 失去最后一个交付者。
- **活性：** 每条 live obligation 至少有一个交付者。
- **retire** 只允许用于没有来自 \(O\) 的入边、且没有保留探针的条目。
- **merge** 只允许在产物与检查的并集覆盖双方 live obligations、且合并描述降低
  干扰时。
- **upgrade** 只允许在新条目交付旧产物的超集、且通过旧探针时。

这就是按义务做的可达性 GC。它解释 Library Drift 的 −1.9pp：过早退休删掉了一个
仍然 live 的交付者，违反活性。生命周期因此有证明义务，而不是日程。

### 5.1 融合：先判关系，再选动作

**条目签名。** 宿主条目和引入卡片都先写成同一个声明式记录：

\[
\sigma=(Q,P,\mathrm{Pre},\mathrm{Post},R,\mathrm{Proc},K,\mathrm{Prov}),
\]

其中 \(Q\) 是触发问题，\(P\) 是交付产物集，\(\mathrm{Pre}/\mathrm{Post}\) 是前置/
后置条件，\(R\) 是**具名有效域**（不是自由散文），\(\mathrm{Proc}\) 是做法，
\(K\) 是检查/作废条件集，\(\mathrm{Prov}\) 是证据来源。字段必须声明；融合关系
只能从这些声明（以及下面列出的 witness）算出，不能从描述相似度猜。

**九种关系。** `same_product` 表示产物集有交集且交付的是同一个可索要结果；
`same_procedure` 把做法的前置/后置条件也算进去；`regime_subset` / `regime_overlap`
比较具名有效域。

| 关系 | 判定 | 允许的动作 | 含义 |
|---|---|---|---|
| `covered` | `same_product ∧ same_procedure ∧ regime_subset ∧ ¬checks_missing` | `no-op` | 新条目已被旧条目覆盖 |
| `partial` | `same_product ∧ same_procedure ∧ (¬same_regime ∨ checks_missing)` | `add_validator` / `upgrade` / `downgrade` / `split` | 同做法，但域不同或检查不全 |
| `duplicate` | `same_product ∧ same_procedure ∧ same_regime ∧ ¬checks_missing` | `merge` | 真重复，可合并 |
| `variant` | `same_product ∧ ¬same_procedure ∧ ¬regime_overlap` | `split` / `demote` | 同产物，不同做法，域不相交 |
| `hard-conflict` | `same_product ∧ ¬same_procedure ∧ regime_overlap` | `quarantine` / `refuse` | 同产物，不同做法，域重叠 |
| `subsumes` | `products_superset ∧ checks_superset ∧ regime_superset` | `upgrade` | 新条目严格强于旧条目 |
| `subsumed` | `products_subset ∧ checks_subset ∧ regime_subset` | `no-op` | 新条目被旧条目严格包含 |
| `adjacent` | `¬same_product ∧ question_overlap` | `extend` / `new-entry` | 不同产物，问题相邻 |
| `unrelated` | `¬same_product ∧ ¬question_overlap` | `new-entry` / `no-op` | 无关 |

融合层的 `covered` **不是**差距表的 `equivalent`。差距表仍用六态
`equivalent | partial | missing | agent-competence | host-only | unknown`；
`equivalent` 说的是宿主已经在回答同一个问题，融合层的 `covered` 说的是新旧两个
条目之间可省掉一个。两个判断不能互相替代。

**三个区分。**

1. **描述相似 ≠ 重复。** 两段描述都出现 “equation of state” 或 “thermal
   conductivity” 只说明它们可能争夺同一个路由，是 shadowing 信号；由保留探针、
   `demote` 或 `split` 处理，永远不构成 `merge` 的理由。
2. **同产物 + 不同做法 = `variant` 或 `hard-conflict`。** 有效域不相交是
   `variant`（可以并存，按域分流）；有效域重叠是 `hard-conflict`（不静默选边）。
   不能因为“同一个可观测量、另一个计算器”就写成 `duplicate`。
3. **同做法 + 不同有效域 = `partial`，不是 `variant`。** 新条目更强则
   `upgrade`，更窄则 `downgrade`，并列则 `split`；只缺检查则
   `add_validator`。

**决策树。** 先算见证布尔值，再按此顺序读取（树不是第二套规则）：

1. **一方是否严格更强？** 产物、检查、有效域都是超集，且至少一项是真超集。
   新条目强 `subsumes`（`upgrade`）；旧条目强 `subsumed`（`no-op`）。
2. **交付同一产物？** 否 → 问题是否重叠？是 `adjacent`（`extend` /
   `new-entry`）；否 `unrelated`（`new-entry` / `no-op`）。
3. **同一做法（含前置/后置条件）？** 否 → 有效域是否重叠？是
   `hard-conflict`（`quarantine` / `refuse`）；否 `variant`（`split` /
   `demote`）。
4. **同一有效域且无缺失检查？** 是 `duplicate`（`merge`）。
5. **有效域是子集且无缺失检查？** 是 `covered`（`no-op`）。
6. **其余** → `partial`（`add_validator` / `upgrade` / `downgrade` /
   `split`）；前置/后置不可同时成立时归入 `hard-conflict`。

**先补检查，再合并。** 只缺一条检查时，`add_validator` 优先于 `merge` / `split`：
SkillOps 的消融里 validator 插入是最有价值的单一维护操作，而 merge 或 repair
单独使用效果有限、组合使用才显著。cap-align 的动作顺序因此是“先修检查，只对
真冗余合并”。

**merge 语义（只对 `duplicate`）。**

- 产物和检查取并集；不能丢掉任何一方独有的产物或 live obligation。
- 有效域取交集（保守：合并后的条目只承诺双方都成立的范围）。
- provenance 取并集，两边的证据都保留。
- 双方 test contract 都保留；合并条目要能分别重放两边的 fail-before /
  pass-after / destroy。
- 描述重写成**一条**问题，不是两段描述的拼接；重写后重跑双方的路由探针。
- 条目数下降，但 portfolio coverage 不下降；干扰不上升。
- 写 rollback：恢复两个源条目、它们的描述和探针。
- 并集不能覆盖双方 live obligations 时，不许 merge；改 `split` 或 `demote`。

**融合的证据阶梯（2026-10-23 增补）。** 综述里的结构压缩派给出了一条可借的
失败模式：删掉的往往不是“不重要的内容”，而是“什么情况不该做”的豁免规则。
SkillZip Pro 的实测是，无证据保护的 71–76% 压缩丢 18–26 个准确点，且是单侧
假阳性。cap-align 因此把 merge 从“字段并集”升级为**可审计的删除**：

1. **每条删除恰好一条 witness。** W1 字面包含 ≻ W2 覆盖 witness ≻ W3 受限
   蕴含（冻结 checker）。挂不上 witness 就否决，无论能省多少 token；同一条目
   挂两条 witness 也算错。被删的源条目本身是一条删除
   （`entry:<card_id>`），必须有自己的 witness。
2. **W3 不碰义务与输出。** obligations、output_fields，以及带
   prohibition/exemption/output 标记的单元，只允许 W1/W2。这是 SkillZip Pro
   的失败点，也是我们最不能省的一类单元。
3. **锁定残差。** 解析不了或证不了的单元不是删掉，而是逐字放进
   `locked_residual`（`unit`、`reason`、`verbatim`）。压缩不足是可接受的失败，
   静默删除不是。
4. **硬覆盖。** 双方 surface 的五类单元（trigger / workflow edge / tool
   requirement / obligation / output field）取并集，必须等于
   `coverage ∪ removed_units ∪ locked_residual`；coverage 不能声明两边都没有的
   单元。产物和检查的并集看起来完整、但某个触发或输出字段消失，是这一条要
   挡的。
5. **提交门。** 双方保留探针都进 `recall_probes`，逐条声明、逐条有观测结果；
   任一 `passed: false` 否决。这是 SkillGLoW commit gate 的最小可静态化版本：
   合并结果按“能否保住旧行为”单独测，不看压缩期的软分。
6. **交互检查。** `interaction.beta < -0.15` 必须附一次扩展回归检查及其证据，
   否则拒绝。`beta: 0` 的含义是“没有估计”，不是“已证明独立”；共现稀疏时
   不许把零先验写成零交互。
7. **never-inflate。** `surface_tokens_after > surface_tokens_before` 就不合并；
   退回 no-op、`split` 或 `demote`。审计通过但目标没有改进，不是合并的理由。
8. **证据等级不冒认。** `evidence_level` 只能是
   `constructive | model | statistical`；`statistical` 需要
   `causal_evidence = {design: randomized, n_trials > 0}`。相似度、压缩前后的
   均值差、未随机化的 A/B 都不是因果证据。

**刻意不采用。** SkillGLoW 的“整轮提交、失败则库原封不动”在 cap-align 里是
**建议级**的 rollback 记录，不是执行语义：本 skill 不执行合并。SkillSmith 的
合并没有回滚语义，我们反过来把 rollback 设为准入前置条件。SkillZip 的
“结构保真”也不等于“行为保真”，所以结构检查通过只说明没有已知的静默丢失，
不说明模型读合并文本后的行为不变；后者只能在宿主上测，E5/E6 尚未跑。

**冲突政策。**

- `hard-conflict` 不裁决。记录双方 \(\mathrm{Proc}\)、有效域和证据，
  `quarantine`，默认路由器不可选；不静默选论文或仓库的一侧。
- 表面冲突先按有效域拆：同产物、不同做法但域不相交，落成两个 `variant`
  条目，路由按域显式分流。
- \(\mathrm{Pre}/\mathrm{Post}\) 冲突视为做法不同，归 `hard-conflict`；
  不能靠改描述掩盖。
- `env_conflict`（依赖版本、安装环境、路径）不是科学冲突；记录为宿主
  环境问题，不进入 `quarantine`，也不改写科学条目。

**worked example：phonopy × MatDiscovery。**

- `qha` / `eos`：`qha` 交付的是在体积网格上最小化 \(F(V,T)\) 得到的热膨胀；
  `eos` 交付 \(E(V)\) 拟合的 \(V_0/B_0\)。同属状态方程问题但产物不同 →
  `adjacent` → `new-entry`，目标 `eos`，保留探针 `q-eos-route`。描述都含
  “equation of state”，但不是 `duplicate`。
- `lattice-kappa`（BTE） / `heat-flow`（BTE）：同产物、同做法、有效域不同
  （低温 vs `bulk, T>=300K`）→ `partial` → `split`（缺检查时
  `add_validator`）。这是“同做法、不同域”，不是 `variant`。
- Slack 模型的 `kappa-slack-bulk` / `heat-flow`：同产物、不同做法、域重叠 →
  `hard-conflict` → `quarantine`；若 Slack 只覆盖 `T<100K` 且与 `heat-flow`
  不相交，则 `variant` → `split` / `demote`。
- `band-structure`：宿主没有声子色散这个问题 → `unrelated` → `new-entry`。
- `force-constants`、`phonon-dos`：论文沉默、仓库有入口，行级是 `refuse`；
  组合层是 `unrelated` → `no-op`，宿主不变。
- 联合遮蔽：`qha` 和 `kappa-bte-lowT` 各自让 `q-heat-flow-route` 的余量
  下降 0.2，余量是 0.3；单看都安全，add-all 是 \(0.3-0.2-0.2=-0.1\)，
  集合测试失败；`demote` `qha` 后回到 0.1，通过。两条行级安全的卡不封闭于
  并集，这是必须做集合测试的原因。

**融合指标。**

| 指标 | 定义 |
|---|---|
| duplicate rate | 判定为 `duplicate` 的候选×条目对 / 全部检查过的候选×条目对 |
| merge compression | merge 前后条目数之比（或 \(1-\text{after}/\text{before}\)） |
| hard-conflict count | `hard-conflict` 对数；不合成单一分数 |
| post-fusion retention | 计划执行后仍通过的保留探针 / 计划前的保留探针 |
| regime-gap count | 同产物、同做法但有效域不交或非子集的候选×条目对 |
| description ambiguity | 描述高度重叠但产物不重叠的对数（shadowing 信号） |
| orphan count | 无 live obligation 且无保留探针的条目 |

## 6. 指标

| 指标 | 定义 | 用途 |
|---|---|---|
| **Retention** | 加入前后保留探针通过率之差 | 组合条件本身 |
| **Shadowing risk** | 新条目相对 owner 的最大相关度/余量下降 | 静态代理；**不叫** shadowing 测量 |
| **Interference** | 高于阈值的两两描述重叠计数与最大值 | 干扰图，不给单一分数 |
| **Context tax** | 默认面新增 tokens（progressive disclosure 下只算路由行） | 与干扰分开报 |
| **Portfolio coverage** | 有交付者的 live obligations / live obligations | 活性 |
| **Orphan rate** | 无 live obligation 且无探针的条目 | 退休候选 |
| **Churn** | 每准入一个工作的生命周期动作数 | 自进化成本 |

\(t_v\)、FI、Miss、fail-before/destroy-red 不变。

## 7. 实验

- **E5（横截面，C4 的证据）**：宿主库 20–40 条目；加入一个工作的卡。四臂：
  add-all / oracle（只加新条目）/ portfolio-gated（按需 merge/demote）/
  refuse-new；可加 retrieve-only（RAG 短名单）。报 retention、新能力 pass、
  probe flip、interference、context tax。预测：add-all 掉 retention；
  portfolio-gated ≈ oracle。
- **E6（纵向，C5 的证据）**：replay 5–8 个工作或同一工作的连续版本。四臂：
  no-lifecycle / retire-only / merge-only / reachability-gated。报 pass@1、
  coverage、size、orphan。预测：no-lifecycle 漂移；按日程退休伤人；
  可达性门控保留。
- **E7（机制复现，可选）**：在材料宿主上复现 Skill Shadowing 的分解。
  这是 sanity check，不是贡献。

ACL 最低包：E5 + 一个 worked lifecycle example（一次 merge、一次 retire、
一次 upgrade）。E6 可以留作 follow-up；没有跑就不写经验结论。

## 8. 与现有文稿的关系

- `typed-introduction.md` 的 \(\lambda\) 与命题 1–5 不变；组合准入是同一算子在
  集合层的闭包条件。
- `acl-paper-design.md` 的 C1–C3 不变；C4（组合准入）与 C5（证据门控生命周期）
  标 provisional。页数紧时 C5 折进 C4 的「维护」一段。
- 论文头条不变：**green but not the paper's result**。加的是第二半句：
  **correct but not yet admissible**。
- 邻居：Skill Shadowing / Single-Agent Skills 测量退化；Library Drift / SkillOps
  管库内健康；Repo-To-Skill / SkillFoundry 从源生成；我们做的是「外来科学工作
  的证据 → 这个宿主的集合准入与生命周期」。

## 9. 不要做

- 不要说 context 是瓶颈；证据指向选择。
- 不要说在材料宿主上测到了 shadowing；没有。
- 不要提出新的 scaling law；2601.04748 的，借用。
- 不要把 cap-align 做成运行时路由或执行器；它只出计划。
- 不要按日程 merge/retire；−1.9pp 是反例，可达性是门。
- 不要把 plugin 安装、MCP 传输、装环境算进组合；scope 规则不变。
- 不要把 `demote` 的条目算作已进默认面；两个数分开报。
- 不要在没有「可能失败的探针」时给准入结论。

## 10. 落码清单

详细到文件与验收的清单见
[`../research/portfolio-lifecycle.md`](../research/portfolio-lifecycle.md) §6。
摘要：

| 优先级 | 改动 |
|---|---|
| P1 | `SKILL.md` 新增 step 7「组合准入」，报告变 step 8；`references/portfolio-admission.md`；卡片加 `portfolio.action` / `portfolio.retention_probes`；报告契约加 Portfolio 节；schema 加 `portfolio`；Layer-1 加 19–21 |
| P2 | `tests/fixtures/mini-library/`（两条各自安全、联合遮蔽 `heat-flow`）；`mini-retire/`（upgrade + retire）；gold 与 21 项通过条件 |
| P3 | `research/tools/portfolio-model.py`（纯 stdlib）：重叠图、干扰、可达性、生命周期计划 |
| P4 | 论文 v0.5：C4 + 一个 worked example；E5 跑完再写经验结论 |
