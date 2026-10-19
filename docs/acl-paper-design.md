> **Innovation lock (2026-10-18): DECIDED.** Coverage fork + principled refusal + \(K_H\)/\(t_v\) — see [`acl-draft/innovation-proposals.md`](acl-draft/innovation-proposals.md). Contribution bullets in §0–§1 below are authoritative; `paper.md` **v0.4.1** bulk-rewritten to match; Figure X regenerated.

# ACL 文稿设计补充：typed introduction

> **Insight research (2026-10-18):** deep-web + AgentRepo notes → `paper.md` **v0.4.1** thick C1–C3 rewrite (see `acl-draft/CHANGELOG-v0.4.md`); bibliography map in `docs/acl-draft/insights-research.md`.


> 更新：2026-10-18。本稿把仓库里已有的设计结论收成**面向 ACL 投稿的写作包**：贡献怎么钉、Related Work 怎么拆邻居、最小实验协议、Limitation、Intro 三条、Figure X。
>
> **不发明实验结果。** 凡未跑完的实验一律标 `TODO`。契约与命题见 [`typed-introduction.md`](typed-introduction.md) 与 [`../research/introduction-operator.md`](../research/introduction-operator.md)；旧仪器身份见 [`paper-core.md`](paper-core.md)（终点是差距表，不再是论文主张）。
>
> 目标 venue 叙事：scientific NLP / agent methodology（宿主相对、类型决定编辑），不是「材料领域工具说明」。材料是第一语料实例。

---

## 0. 一句话身份（投稿用）— **DECIDED 2026-10-18**

**EN.** Dual encoding forks host coverage; product-typed residual \(\lambda\) selects introduction *and refusal* on deployed \(H=(P_H,K_H)\), including validity checks \(K_H\), under a fail-before / destroy acceptance contract that wrap-repo and paper-only violate on FI, Miss, or \(t_v\). Fast (call count) is optional until measured.

**ZH.** 双编码会在宿主上分叉覆盖；产物类型残差 \(\lambda\) 决定对已部署 \(H\) 的引入*与原则性拒绝*（含有效性检查 \(K_H\)），并用改前必败/破坏测试验收；只接仓库/只抄论文会在误引入（FI）、漏义务（Miss）或有效性（\(t_v\)）上违约。调用次数（更快）有表再报。

**与旧稿分界。** [`paper-core.md`](paper-core.md) 的终点是「停在差距表 + 只建议」。那是 skill 仪器行为。论文主张钉在 **覆盖分叉 → \(\lambda\to I\)（含拒绝与 \(K_H\)）→ FI/Miss/\(t_v\)+destroy**；若仍停在检测/建议，会与 SciCoQA（ACL 2026 Main, SAC Highlight）正面撞车。不把「六类 λ」当头条贡献。

---

## 1. 贡献框架：Detect vs Typed Introduction

### 1.1 差分钉死（对审稿人）

| 轴 | SciCoQA（检测） | 本文（类型引入） |
|---|---|---|
| 输入 | 一篇论文 + **它自己的**代码 | 外来工作 \(W=(W_p,W_r)\) + **已部署宿主** \(H\) |
| 问题 | 论文与代码是否不一致 | 残差类型决定**对 H 改什么、测什么** |
| 输出 | 差异检测 / 分类（Difference, Paper Omission, Code Omission） | 编辑 \(I(H,\lambda)\) + 改前必败测试 |
| 粒度 | 句 / 函数级语义冲突 | 产物槽位单元 \(u=(p,s,e,v_p,v_r,\kappa)\) |
| 成功标准 | 召回真实差异（最好真实召回约 46.7%） | FI=0（命题 2）、相对 \(W_{\mathrm{rap}}\) 的 Miss/FI 计数（命题 3）、缺有效性上 \(t_v=1\)（命题 4）、打乱非空（命题 5） |
| 宿主 | 无 | 必须；拿掉宿主主张退回检测 |

SciCoQA 的三种差异 ≈ 本文标签里的做法冲突 / 义务缺入口 / 入口缺义务。**重合的是残差 taxonomy 的前半；差分是后半：对宿主的类型引入。** Related Work 与 Intro 必须用同一句把这点写死。

### 1.2 Locked Intro contributions (C1–C3) — **DECIDED**

> **Contributions.**
>
> 1. **C1 — Coverage-fork residual (model + insight).** Independent paper/repo inventories are merged by *product identity* into units \(u=(p,s,e,v_p,v_r,\kappa)\); the induced paper-face and repo-face host-gap sets can be *disjoint*. Unique type \(\lambda\) partitions residual (including validity-gap and procedure-conflict). Dual encoding is not two adapters for one coverage number—a detection taxonomy without host \(H\) cannot state this fork.
> 2. **C2 — Typed introduction \(I\) with principled refusal and \(K_H\).** \(\lambda\) maps to edits of \(H=(P_H,K_H)\) *or* to non-introduction (entry-sans-obligation / procedure-conflict / incongruent). Counting: \(\mathrm{FI}(I)=0\); wrap-repo FI/Miss equal omission-type counts; only \(I\) installs \(t_v=1\) on validity-gap (Props. 2–4). Label permutation \(\pi\) is a non-vacuous ablation (Prop. 5). Refusal is part of correctness, not a failed run.
> 3. **C3 — Contract acceptance protocol.** Against wrap-repo (\(W_{\mathrm{rap}}\) / MCP-attach), paper-only (\(P_{\mathrm{aper}}\)), and write-directly, report Effective (FI, Miss, \(t_v\)) and Testable (fail-before → green → destroy-red); Fast (calls to green) only when measured. Materials (or any domain with public products + enumerable host) is instance one; \(\lambda\) frozen. Reproduction fidelity and detection recall are the wrong scalars for host introduction.

**中文一行（审稿自用，勿当贡献表）。**

| # | 一行中文 |
|---|---|
| **C1** | 双编码会在宿主上分叉覆盖；产物身份合并后，论文面与仓库面的缺口集合可以不相交。 |
| **C2** | \(\lambda\) 既决定对 \(H\) 的编辑，也决定原则性拒绝；有效性缺口必须装上 \(K_H\)（\(t_v=1\)）。 |
| **C3** | 用 FI / Miss / \(t_v\) 与改前必败→破坏测试验收引入；不跟检测召回或复现准确率抢榜。 |

### 1.3 现在**不要**声称的（claim scope）

| 不要写 | 原因 | 可写的诚实替身 |
|---|---|---|
| 「empirically shown residual on N papers」 | **EΔ 未跑**；phonopy/mini 是规则例子，不是结果表 | 「slot model illustrated on mini-ref and phonopy; multi-work measurement TODO」 |
| 「human IRR κ=…」 | E1 现有 κ 是**同模型三 judge**；无人类、无第二模型 | 「same-model pilot κ reported as lower bound; true IRR TODO」 |
| 「faster / more accurate / more trustworthy in user studies」 | 无用户实验；「更快更准更可信」须绑定定义好的三个数 | Fast=call count；Effective=FI/Miss/\(t_v\)；Testable=destroy-test |
| 「outperforms SciCoQA on detection」 | 本文不是检测榜；比检测 F1 是错误战场 | 「orthogonal: they detect; we introduce on H」 |
| 「SOTA paper→code reproduction」 | 不与 SA-Bench / LMR-BENCH / SciReplicate 比执行准确率 | 「not a generation/reproduction benchmark」 |
| 「八步闭环 / 能力格 / 首次…」 | 旧叙事；审稿人会当地盘声明 | 仪器描述可提 workflow；不进贡献表 |
| 「包内 drift 80% 对照我们的规模」 | BIV 已占包内主场；E3 是分解项 | 附录或动机一句即可 |
| 「LLM judge 已校准」 | 同模型互相同意 ≠ 人标一致（ARR M1 风险） | Limitations 写明；补人标后再声称 |

---

### 1.4 预期审稿质疑与答辩（2026-10-19 讨论沉淀）

**质疑 A：「提取单元 → 分类 → 按类操作」没有创新。**
承认：分类-路由是通用模式，\(\lambda\) 的前三类与 SciCoQA 的 taxonomy 重合。答辩三点：
(1) **问题提法本身是空生态位**：SciCoQA 停在检测，SA-Bench/SciReplicate 不管宿主已有啥，BIV/SkillConsist 是包内自查；「外来 \(W\) 对已部署 \(H\) 装什么、不装什么」没人占。分类只是回答该问题的中间件。
(2) **分类之后承诺的是「不动作」且可证伪**：EO 类不装、CF 类不许选边；「装得越多覆盖越高」由此被证明为可计数的错误（命题 3：wrap-repo 的 FI 恰好等于 EO 类基数）。把直觉上正确的做法证明为算术恒等式错误，是表之外的增量。
(3) **好处从定义推出，不是跑出来的**：FI(\(I\))=0 等是计数恒等式；实验的角色是检验实现有没有守住合同，不是证明有效。

**质疑 B：「受控编辑」是工程常识。**
答辩：控在三个点上——(i) 改哪个由 \(\lambda\) 选择，无类型生成是基线不是方法；(ii) 落点是两个存储 \(P_H\) / \(K_H\)，作废条件是一等编辑对象；(iii) 验收方向反转：测试改前写定、改前必红、删掉规定动作必须再红（destroy 检查针对 TestPrism 指出的「检查本身写错」），SkillRevise 只有「改后绿了才收」。单零件都有先例，闭包没有：触发、落点、验收、拒绝四件事由一个 \(\lambda\) 推出，且验收本身被验收。

**软肋（主动披露）。** (a) 若 EΔ 实测残差接近零，分叉动机塌——EΔ 是第一优先级的原因。(b) Faithful 不覆盖补丁生成质量；动作细化（§算子 4.1）把 Faithful 变成 \(\pi\in\mathrm{Adm}(\lambda)\) 的静态审计，缓解但未消除。(c) 别把六标签当卖点——头条永远是分叉与拒绝。

---

## 2. Related Work 对照表（论文可贴）

表意：**他们的问题 / 我们的问题**。详细引用库仍以 [`../research/related-work.md`](../research/related-work.md) 为准；下表补上 ACL 审稿最可能拿来撞的邻居（含 SciCoQA Main 与 paper→code 复现线）。

| Work | Venue / ID | Their question | Ours | Shared surface | Diff |
|---|---|---|---|---|---|
| **SciCoQA** | ACL 2026 Main (long); arXiv:2601.12910 | Detect paper–**own**-code discrepancies | Type residual then **introduce** on host \(H\) | Taxonomy: Difference ≈ procedure-conflict; Paper/Code Omission ≈ obl.-sans-entry / entry-sans-obl. | They stop at detection; we map \(\lambda\to I\) + fail-before tests; host is required |
| Dude (on SciCoQA) | (follow-up detection) | Raise detection F1; warns grain mismatch | Units merge by **product Id** before typing | Cross-modal QA | We refuse sentence-level residual that invents host gaps |
| **SA-Bench** (SemanticAlign-Bench) | Findings EMNLP 2026; arXiv:2608.24252 | Fidelity of **generated** paper→code (SAU drift) | Edit contract on **existing** host | Spec faithfulness | Generation/reproduction eval ≠ typed introduction |
| **LMR-BENCH** | EMNLP 2025; arXiv:2506.17335 | Fill masked functions from NLP papers | Do not regenerate a repo; bind or write **host-owned** capability | Paper as spec | Masked-repo repair ≠ host-relative \(I\) |
| **SciReplicate-Bench** | COLM 2025; arXiv:2504.00255 | Agent algorithmic reproduction from papers | No claim-execution success as endpoint | Paper→code agents | Execution accuracy is their metric; ours are FI/Miss/\(t_v\) |
| **ReproAgent** | EMNLP 2026 Findings | Contract-guided Prepare–Plan–Generate–Repair reproduction | Typed edits from \(\lambda\), not free repair loop | Contracts / tests | Their loop optimizes reproduction; ours selects **which** edit by residual type |
| AutoMat | arXiv:2605.00803 | Can an agent reproduce a materials **claim** | We do not run the reference experiment | Materials instance | Claim success ≠ host coverage / introduction |
| SkillFoundry | arXiv:2604.03964 | Compile resources → **new** skills | Gaps relative to **this** \(H\); type must choose the edit | Scientific resources → skills | Untyped generation is a **baseline**, not the method |
| BIV / SkillConsist / DCI | 2026 skill/MCP audits | Package vs **its own** implementation | Incoming \(W\) vs deployed \(H\) | Drift / inconsistency language | Intra-artifact audit ≠ host-relative typed intro |
| Skill Coverage | arXiv:2606.20659 | Trajectory vs a skill’s **own** constraints | Coverage of external work \(W\) (paper vs repo projections) | Word “coverage” | Different axis; name carefully in text |

**写作纪律。** 不要借 SciCoQA 的六种 ML 流水线类别词表。不要把「更好的检测器」写成贡献。第一段 Related Work 用上表前两行（SciCoQA + SA-Bench 或 LMR）把差分说完。

---

## 3. 最小实验协议（ACL 证据门槛）

完整旧计划见 [`../research/experiments.md`](../research/experiments.md) 与 [`progress.md`](progress.md)。本节是**冲 Findings / Main 的最小可投稿包**，指标对齐 typed introduction（FI / Miss / \(t_v\) / call count），不是只报五态 κ。

### 3.1 总览

| ID | 问什么 | 服务哪条贡献 | 现状 | 投稿最低门槛 |
|---|---|---|---|---|
| **EΔ** | 同一工作 \(W_p\bowtie W_r\) 残差非空且可打 λ | C1 / 标签非空 | **TODO 未跑**（phonopy 槽例已有，非测量） | ≥1 真实对独立双盲盘点；残差非空且不可用「漏扫」解释 |
| **E1′** | Id / λ / 投影的人标 IRR | 标注可信 | 旧 E1：同模型 κ 试点；**真人 IRR TODO** | ≥2 人标；报 Cohen/Fleiss κ + raw agreement；同模型数只作附录下限 |
| **E2′** | \(I\) vs \(W_{\mathrm{rap}}\) vs \(P_{\mathrm{aper}}\) vs write-directly（+ 打乱 \(\pi\)） | 有效；命题 2–5 的经验对应 | 旧 E2 协议偏「按报告装配涨分」；**typed 对照 TODO** | 同一批人标单元上四臂；按标签拆开报 FI/Miss/\(t_v\) |
| **Fast** | 到测试变绿的调用/改动 | 「更快」 | **TODO** | 与 write-directly 同任务比 call count（及可选人工改动次数） |
| **Testable** | 改前红 → 改后绿 → 删规定动作再红 | 「更可信」 | 合同已写；**批量测量 TODO** | 报 destroy 后仍绿的比例（测试写错率） |

命名：文中可用 EΔ / E1 / E2；与旧 `experiments.md` 冲突处以**本节指标为准**，旧五态 IRR 降为仪器附录。

### 3.2 语料与标注

1. **单元。** 按 [`typed-introduction.md`](typed-introduction.md) §5：产物行，两侧分开盘点，合并靠 Id，槽位抄原文位置。
2. **规模（Findings 最小）。** 先 8 对 paper–repo 把规则练到第二个人能独立标出相同 `filled` 与 λ；再扩大。会场认的最小结果：一批人标单元 + 三列对照 + 一项打乱 + 负例误报（见 typed-introduction §11）。
3. **冻住。** 宿主清单 \(H\)、标签集、测试，在看结果前冻住。中途不改。
4. **Id / κ。** 人先标一小批；模型后标须报与人的一致率。判断不了的 κ 保持 0。**同模型互相同意不算校准。**

### 3.3 基线

| 符号 | 行为 | 用来打哪条命题 |
|---|---|---|
| \(I\) | 按 λ 编辑 + 写 \(K_H\)（方法） | 命题 2, 4 |
| \(W_{\mathrm{rap}}\) | 凡 \(e=1\) 接入；不写 \(K_H\) | 命题 3, 4 |
| \(P_{\mathrm{aper}}\) | 凡 \(s=1\) 按论文写；不绑入口、不写 \(K_H\) | 命题 4；两侧齐上破坏测试对不上入口绑定 |
| write-directly | 论文+仓库一起交给模型写宿主能力，不看 λ | Fast；Effective 对照 |
| \(\pi\) | 对调义务缺入口 ↔ 入口缺义务后再套 \(I\) | 命题 5 |

### 3.4 指标定义（禁止口号）

| 名 | 定义 | 对应口语 |
|---|---|---|
| **FI** | 被加入 \(P_H\) 但 \(s=0\) 的产物数 | 误引入 |
| **Miss** | \(s=1\)、事先 \(p\notin P_H\)、算子未加入的产物数（做法冲突故意不加入须单列） | 漏义务 |
| **\(t_v\)** | \(\mathbf{1}[p\in P_H]\cdot\mathbf{1}[(p,v)\in K_H]\) | 有效性检查是否装上 |
| **Fast** | 到达「改前失败且改后通过」为止的模型调用次数（可附输入规模、人工改动次数） | 更快 |
| **Effective** | 分标签的 FI、Miss、\(t_v\)（及相对基线的差） | 更准 |
| **Testable** | 改前失败 ∧ 改后通过 ∧ 删掉规定动作后再次失败；报「删后仍绿」比例 | 更可信 |

实现守住 \(I\) 且宿主事先无这些产物时，FI(\(I\))=0、命题 3 的计数由定义决定。**模型跑完对不上，查的是实现，不是定义。** 论文须分开报「合同计数」与「实现遵守率」。

### 3.5 TODO 清单（禁止填假数）

- [ ] EΔ：≥1（建议 ≥2）真实 paper–repo 独立盘点，残差类混与 Jaccard
- [ ] E1′：≥2 人类 annotator；κ + disagreement 分析（partial/missing、Id 边界）
- [ ] E2′：四臂 + \(\pi\)；分 λ 报 FI/Miss/\(t_v\)
- [ ] Fast：与 write-directly 对齐的 call-count 表
- [ ] Testable：destroy-test 误报率
- [ ] （可选，Main 加分）第二可盘点宿主或第二计算领域，**同一套 λ 一字不改**

---

## 4. Limitations / 诚实边界（论文 Limitations 草稿）

合并 [`progress.md`](progress.md) §5、[`typed-introduction.md`](typed-introduction.md) §10/§14、旧 E1 污染披露。英文段落可直接贴 Limitations。

**English (draft).**

> **Limitations.** (1) *Unrun residual measurement.* Multi-work EΔ quantifying \(\Delta(W_p,W_r)\) beyond illustrative phonopy / mini-ref slots is not yet complete; dual-encoding remains partially hypothetical until that table exists. (2) *Annotation reliability.* Existing classification agreement is a same-model three-judge pilot, not human IRR; Id and \(\kappa\) require human protocols before claims of calibrated labeling. (3) *Faithful patches.* Counting theorems assume edits realize the operator table; we do not prove that a given LLM writes such patches—experiments must report both green-rate and destroy-test failures. (4) *Domain scope.* Public product names, dual encodings of one process, and an enumerable host surface must co-hold; we do not claim arbitrary chat agents. (5) *Neighbor metrics.* We do not compete on SciCoQA detection recall or on paper→code execution accuracy (SA-Bench / LMR-BENCH / SciReplicate). (6) *Intra-package drift* numbers are decomposition context, not headline results. (7) *Contamination risk* in pilot judging (methodology prose entering context) requires line-bounded reads in the released protocol.

**中文要点（勿删）。**

- EΔ 未跑 → 双编码残差在测量上仍是假说加强例。
- E1 同模型 κ ≠ 真 IRR；须披露。
- Faithful 是假设；报实现遵守率，不假装定理覆盖模型能力。
- 领域三条件同时成立；不为会场放开到任意 agent。
- 不跟检测召回、不跟复现执行准确率抢榜。
- 包内 drift、八步仪器、闭环词不进贡献。
- 试点污染：方法论全文进上下文 → 协议强制行界读取。

---

## 5. Figure X：位置与 caption

### 5.1 文件

| 文件 | 用途 |
|---|---|
| [`figures/typed-introduction/cap-align-typed-introduction.pdf`](figures/typed-introduction/cap-align-typed-introduction.pdf) | 投稿矢量（优先） |
| [`.svg`](figures/typed-introduction/cap-align-typed-introduction.svg) | 矢量备选 / 编辑 |
| [`.png`](figures/typed-introduction/cap-align-typed-introduction.png) | 300 dpi 预览 |
| [`render_typed_introduction_figure.py`](figures/typed-introduction/render_typed_introduction_figure.py) | 可复现渲染 |
| [`…-figure-notes.md`](figures/typed-introduction/cap-align-typed-introduction-figure-notes.md) | 面板说明、符号表、生产注记 |

版式：双栏 Method 主图，约 7.0 in × 5.15 in；英文标签；黑白友好。主张终点是 **typed edits + tests**，不是八步仪器。

### 5.2 Caption（英文，建议定稿）

> **Figure X.** Coverage fork and typed introduction for dual-encoded scientific work. (a) Independent paper/repo encodings are merged by product identity into unit \(u\); unique \(\lambda\) partitions residual (partition engine, not contribution headline). (b) **Coverage fork:** the same \(\lambda\) projects to disjoint host-gap sets on paper vs repo faces—illustrated on mini-ref / phonopy-style slots `qha` (obl.-sans-entry → gap/absent) and `band` (entry-sans-obl. → absent/gap). (c) Operator \(I\) maps \(\lambda\) to edits on \(H=(P_H,K_H)\) *or* principled refusal; validity-gap installs \(K_H\) (\(t_v\)). (d) Against wrap-repo (\(W_{\mathrm{rap}}\) / MCP) and paper-only (\(P_{\mathrm{aper}}\)), contract metrics Effective (FI, Miss, \(t_v\)) and Testable (fail-before→destroy); Fast optional until measured.

**Caption 纪律。** 不发明经验残差率；`qha`/`band` 只作示意槽模式。若审稿要求减密：把 (c) 表压成符号箭头，细节进附录表（见 figure-notes）。

### 5.3 正文引用句（可贴）

> Figure X summarizes the method: dual encoding → product-Id merge → coverage fork → operator \(I\) with principled refusal and \(K_H\), evaluated against wrap-repo / paper-only on FI, Miss, and \(t_v\) under fail-before / destroy-tests.

---

## 6. 文稿地图（改哪里）

| 文件 | 角色 | 与本稿关系 |
|---|---|---|
| [`acl-draft/paper.md`](acl-draft/paper.md) | **ACL 英文全稿草稿**（Intro→Ethics，C1–C3 厚稿） | 投稿正文骨架 **v0.4.1**（~5.4k words）；与本稿 §1.2 锁定贡献对齐 |
| [`acl-draft/README.md`](acl-draft/README.md) | 草稿目录说明 | 指向 paper.md 与 Figure X |
| [`typed-introduction.md`](typed-introduction.md) | 设计结论正文（λ、I、命题、例子） | 权威定义；本稿是 ACL 写作层 |
| [`paper-core.md`](paper-core.md) | 旧仪器身份（差距表终点） | 保留；投稿主张以 typed + acl-draft 为准 |
| [`progress.md`](progress.md) | 实证状态与开放边界 | Limitations / TODO 的事实源 |
| [`../research/brief.md`](../research/brief.md) / `abstract.md` | 英文 brief / abstract **v0.3** | 已按本稿 §1 改贡献表（typed introduction） |
| [`../research/related-work.md`](../research/related-work.md) | 引用库 | 补 SA-Bench / LMR / ReproAgent / SciReplicate 条目时与本稿 §2 对齐 |
| [`../research/experiments.md`](../research/experiments.md) | 旧 E1–E4 | 保留；投稿最小包以本稿 §3 为准 |
| [`../research/introduction-operator.md`](../research/introduction-operator.md) | 算子合同 | Method 形式化附录 |

---

## 7. 投稿前检查清单

- [ ] Intro 三条 = §1.2；无「检测 SOTA」「复现 SOTA」
- [ ] Related Work 首段拆 SciCoQA（detect）vs \(I\)（introduce）
- [ ] Method 主图 = Figure X；caption 无假数
- [ ] Experiments 只报已跑数字；其余写 TODO / future
- [ ] Limitations 含：EΔ、真人 IRR、Faithful、领域范围、不跟检测/复现榜比
- [ ] 贡献表不出现八步闭环、能力格、包内 drift 头条
- [x] `research/brief.md` / `abstract.md` 与 typed 主张一致（v0.3，2026-10-18）
- [x] `docs/acl-draft/paper.md` 英文全稿草稿已立（洞察段已织入 Intro / Method / Discussion）

---

*本稿是 ACL 写作包；英文全稿见 [`acl-draft/paper.md`](acl-draft/paper.md)。不代替实验。下一优先：EΔ 与 E1′ 人标协议落地，再填 §3.5 的勾选框。*