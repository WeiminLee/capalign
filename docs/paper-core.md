# 论文核心：把外来科学工作对齐到已有材料 agent

> 本稿是论文核心创新与思想的凝练（团队沉淀版，中文为主）。论文工作语言稿见
> `research/`（brief / abstract / related-work / experiments）。本稿讲清楚
> **主张什么、为什么新、怎么成体系**。配图仍用 `figures/` 的 archify 正稿；
> 图注已按新身份改写，图面邻居集待重绘。
>
> 2026-10-17 的讨论结论在 [`typed-introduction.md`](typed-introduction.md)：
> 终点从「停在差距表」改为「差异类型决定引入和测试」。本稿第 1 节的旧终点仍是仪器行为。
>
> **ACL 写作包（2026-10-18）：** 投稿主张、SciCoQA 差分、Related Work 对照表、
> 最小实验协议、Limitations、Intro 三条与 Figure X caption 见
> [`acl-paper-design.md`](acl-paper-design.md)。
> **英文全稿草稿：** [`acl-draft/paper.md`](acl-draft/paper.md)（typed introduction +
> 洞察段；非差距表终点）。投稿时以 typed introduction + acl-draft 为准；
> 本稿保留为仪器层身份说明。

---

## 1. 一句话主张

**材料领域同时堆积两类对象：已部署的材料 agent，以及不断发表的「论文 + 配套
仓库」。缺的不是再包一层工具，而是把一篇外来科学工作当成能力规格，相对于用户
自己的 agent 做证据门控对齐。** 科学工作 \(W=(\text{paper},\text{repo})\) 是双编码
规格；宿主相对对齐 \(\mathrm{Gap}(H,W)\) 是静态判定过程（不跑参考工具、不实现
缺口）；覆盖是参考条件化的——选 paper 面还是 repo 面，缺口集合不同。cap-align
是该判定过程的测量仪器，不是贡献本身。给 repo 时仪器会回收配套论文，并按身份门
纳入有界邻域（主页优先，必要时 web-search）；邻域是产品完备性，C1–C3 仍钉用户
给的那篇工作 \(W\)。

对齐的对象是**材料能力**：核心是能模拟什么；上限是材料 agent 该暴露的方法
（评测势、微调、蒸馏）。plugin / MCP / 装环境不是缺口。对齐完成的判据是宿主
**自己的**能力面拥有这些动词——可以调用上游科学引擎，不能把参考 agent 嵌进宿主
当运行时。

## 2. 背景与要解决的科学问题

现场里同时发生三件事：

1. **材料 agent 在增殖，接线仍是手工。** MatDiscovery / El Agente Sólido /
   PolyJarvis / Catalyst-Agent 各自重接同一批资产（phonopy / ASE / pymatgen /
   VASP / QE）。MCP 解决传输，不解决「这篇新工作相对我的 agent 覆盖了什么」。
2. **论文与配套仓库成对出现。** 一篇材料计算论文通常带着方法规格；配套 repo
   带着可执行接口。用户拿到的是一对 \(W\)，要问的是：论文里的能力，我的 agent
   已经有哪些、缺哪些、缺的落在哪一层。
3. **复现与生成都没有回答这个问题。** AutoMat（2026）测 agent 能否把一条
   claim 跑通（最好约 53%）；SkillFoundry 从异构科学资源编出新 skill；SciCoQA
   / paper–code consistency 查一篇论文是否匹配**它自己的**代码。BIV 在
   49,943 个 skill 上测包内声明–实现漂移（80%）。没有任何一项把 **已有宿主**
   相对 **外来科学工作** 做成判定对象。

**科学问题**：一篇已发表的科学工作能否作为能力规格，相对于已部署的科学 agent
被对齐——并且 paper 编码与 repo 编码是否给出同一张规格？

「快速」是该判定过程的操作推论：静态、证据分级、不执行参考、不实现缺口。它
坐在生成（SkillFoundry）和复现（AutoMat）之前。

## 3. 核心思想：双编码规格上的宿主相对对齐

![判定过程的仪器：表示 → 对齐 → 验证](figures/capability-engineering-paradigm.html)

> archify 正稿（可交互、可导 SVG/PNG）。此图描述的是**仪器**——如何把 \(W\) 与
> \(H\) 收进同一 IR 并做证据门控判定——不是「闭环本身即贡献」。概念渲染版见
> [images/capability-engineering-paradigm.jpg](images/capability-engineering-paradigm.jpg)。

**规格（Specification）。** 一篇科学工作 \(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\)
诱导两张能力面：paper 编码方法步骤、有效性条件、声称产物；repo 编码 CLI /
模块 / 接口 / 可执行路径。能力 \(C=(\mathrm{id},\tau,\text{契约},E,\mathrm{conf})\)
是与载体无关的对象。两份编码上的同一性用同一谓词：语义匹配 \(\in\{\mathrm{exact},
\mathrm{plugin},\mathrm{subsume}\}\) 且证据强度 \(\ge\theta\)。

**判定（Decision procedure）。** 对象是 \(\mathrm{Gap}(H,W)\)：已有宿主面 \(H\)
相对外来工作 \(W\) 的五态差距（equivalent / partial / missing / host-only /
unknown），带来源、带已验证证据、带落点（新 skill / 新 tool / 扩既有 /
runner 契约 / 跳过）。三条使它成为理论对象：

1. 证据先于分类：低置信参考条目不能单独判 `missing`；
2. 单调性：加证据只允许 `unknown → missing`，无宿主产物不能把 `missing` 翻成
   `covered`；
3. 可复现：同一 \((H,W)\) 上分类有 IRR。

输出停在建议。SkillFoundry 的输出是新 skill；这里的输出是对**这个**宿主的差距
与落点。

**覆盖（Coverage）。** \(\mathrm{coverage}(H,W)\) 依赖于选取哪一份编码：

- \(\mathrm{coverage}(H,W_{\mathrm{paper}})\) 高、\(\mathrm{coverage}(H,W_{\mathrm{repo}})\)
  低：会讲方法，对不上接口；
- 反过来：会调工具，兑现不了论文方法义务。

残差 \(\Delta(W_{\mathrm{paper}},W_{\mathrm{repo}})\) 可测。它解释 AutoMat 最差
工况——只从论文正文重建流程：agent 拿到 \(W_{\mathrm{paper}}\)，工具提供的是
\(W_{\mathrm{repo}}\)。blog 是第三种编码，主文钉 paper / repo，blog 进附录。

## 4. 三点创新

| # | 创新 | 空在哪 | 可证伪点 |
|---|---|---|---|
| **C1** | **科学工作是双编码能力规格。** \(W=(\mathrm{paper},\mathrm{repo})\) 两份编码共用同一性谓词；只认其中一份，规格不完整。 | BIV / SkillConsist / DCI 比的是**同一个包**内部的声明与实现；SciCoQA / paper–code 比的是论文与**它自己的**代码（句/函数级错误）。这里比的是外来工作的两份**能力面**编码。 | 同一资产上 \(W_{\mathrm{paper}}\neq W_{\mathrm{repo}}\)（残差非空、可分类） |
| **C2** | **宿主相对对齐是判定问题。** \(\mathrm{Gap}(H,W)\) 是静态、证据门控、可复现的决策过程：五态 × 三来源 + 落点，不执行 \(W\)、不实现缺口。 | AutoMat 问能否复现一条 claim；SkillFoundry 问资源能否编成 skill。都没有问已有 \(H\) 相对新 \(W\) 覆盖了什么。 | 断言 A（证据单调）+ E1 IRR（同一谓词在 repo 臂与 paper 臂上都可复现） |
| **C3** | **覆盖是参考条件化的。** \(\mathrm{coverage}(H,W_{\mathrm{paper}})\) 与 \(\mathrm{coverage}(H,W_{\mathrm{repo}})\) 系统分叉；残差类型决定落点是「包接口」还是「兑现方法合同」。 | Skill Coverage（2606.20659）量的是轨迹是否跑过 **skill 自己的**约束。这里的轴是外部科学工作。BIV 的 80% 是包内漂移，不作头条去比规模。 | 按 paper 规格装配 vs 按 repo 规格装配，任务增益形状不同（E2）；paper-only 失败与 \(\Delta\) 相关 |

形式主义（Paolucci 匹配、Zhu 测试充分性、CORA 类型）是判定过程的零件，写进
`research/formal-foundations.md`，不进贡献表。Galois / 「能力格」/ 「首次闭环」
不再作为创新点。

**防守性命题。** 匹配本身是旧的（Paolucci / RE）。新的是：**外来科学工作作为
双编码规格，相对于已有宿主的证据门控判定，以及覆盖随编码选择而分叉。** 仪器
是 cap-align；发现是残差与参考条件化覆盖。

## 5. 差异化定位（系统层）

![与系统层邻居的差异定位](figures/capability-engineering-positioning.html)

> archify 正稿。图面邻居集停在 2026-05 前后，正文下表为当前准绳；图待重绘。
> 概念渲染版见 [images/capability-engineering-positioning.jpg](images/capability-engineering-positioning.jpg)。

| 邻居 | 他们的问题 | 我们的问题 |
|---|---|---|
| AutoMat (2605.00803) | agent 能否复现这条 claim（最好 ~53%） | 宿主已经覆盖这篇工作的哪些能力 |
| SkillFoundry (2604.03964) | 异构科学资源能否编成新 skill | 缺口相对**这个**宿主落在哪；停在建议 |
| SciCoQA (2601.12910) / Do Papers Match Code? (2603.22018) | 论文是否匹配它自己的代码（句/函数） | 论文+repo 作为规格，相对**另一个** agent 差在哪（能力面粒度） |
| BIV (2605.11770) / SkillConsist (2608.07639) / DCI (2606.04769) | skill 或 MCP 工具是否匹配自己的实现 | 外来工作是否被宿主覆盖 |
| Skill Coverage (2606.20659) | 轨迹是否跑过 skill 自己的约束 | 宿主对外部科学工作的覆盖 |
| SkillOps (2605.13716) | 库内 merge / repair / retire | 需求侧：新工作相对已有面 |
| ClaimReceipt / TessIndex / Lemons | 声称的凭证、身份、市场机制 | 内容级、宿主相对的证据门控 |
| Externalization (2604.08224) / CDD | 能力外置 / 组织流程上的表示–对齐–验证 | 科学工作 → 已部署科学 agent |

**材料是实例。** agent 多、paper–repo 对多、软件资产被社区互验最深（Lejaeghere
40 代码互验）。方法层零宿主词汇；phonopy ↔ MatDiscovery 是验证实例，不是方法
内容。

## 6. 为什么必须同时对齐 paper 与 repo

![包内声称 vs 已验证（动机图，非头条度量）](figures/promise-drift.html)

> 此图原叙述「承诺漂移」为治理招牌。BIV / DCI / SKILLSCOPE 已把包内声明–实现
> 漂移做成主场。现用作**动机**：声称需要证据门。我们的头条度量是参考条件化的
> `coverage(H,W)`，`promise-drift` 降为相对某一投影的未兑现声称。概念渲染版见
> [images/promise-drift.jpg](images/promise-drift.jpg)。

核心洞察有两层：

1. **用户的问题是宿主相对的。** 读到一篇新材料论文时，要的是「我的 agent 差在
   哪」，不是「把论文编成 skill」或「把 claim 跑通」。
2. **两份编码不是同一张表。** 只对齐 paper 会漏接口；只对齐 repo 会漏方法合同。
   双对齐是测量结论，不是两种输入开关。

Lejaeghere 证明代码之间可以互验；AutoMat 证明 agent 兑现不了论文声称。中间缺的
一层是：论文规格与软件规格在能力面粒度上的残差，以及该残差如何投射到已有宿主。

## 7. 证据计划（见 research/experiments.md）

| 实验 | 服务哪条创新 | 现状 |
|---|---|---|
| **E1** IRR（P1 repo 臂 + P2 paper 臂） | C2：同一谓词跨编码可复现 | P1 κ=0.853，P2 κ=1.000；仍是同模型三 judge |
| **EΔ** 同一工作的 \(W_{\mathrm{paper}}\bowtie W_{\mathrm{repo}}\) | C1 / C3 的命门 | **未跑**；phonopy 论文 methods vs phonopy 仓库是现成一对 |
| **E2** 按 paper 规格补 vs 按 repo 规格补 vs 随机 / 不补 | C3：参考条件化覆盖的任务后果 | 协议就绪；真实层 gold pending |
| **E3** 库级 `coverage(H,W)` 分布 | C3 的库级形状；包内 drift 降为分解项 | 2 个库的包内 drift 已测，需求侧覆盖分布未立 |
| **E4** 自报面相对外来 \(W\) 的偏差 | C2 能否被宿主自审代替 | mini 上 bias=0.0，不可证伪 |

案例资产已在手：phonopy↔MatDiscovery（19 缺口、A–E 分档、三次防伪缺口教训），
37-skill 宿主库。EΔ 需要把 phonopy 的 methods 论文提成 \(W_{\mathrm{paper}}\)，
与已有 \(W_{\mathrm{repo}}\) 对齐。

---

*三张图均有 archify 正稿（`figures/*.html` / `*.svg`）。图 1 改为仪器说明，
图 3 降为动机；图 2 邻居集待按上表重绘。image-gen 概念渲染留在 `images/` 供
汇报。*
