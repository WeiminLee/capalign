# 论文核心：Material Capability Engineering —— 能力工程范式

> 本稿是论文核心创新与思想的凝练（团队沉淀版，中文为主）。论文工作语言稿见
> `research/`（brief / abstract / related-work / experiments）；本稿聚焦"讲清楚
> 我们主张什么、为什么新、怎么成体系"，并引用 `images/` 下的说明图。

---

## 1. 一句话主张

**材料（计算）软件是半个世纪社区验证的"科学能力资产"；材料 agent 的能力面本质
是这些资产的接口层。我们提出把"表示 → 对齐 → 验证"做成一个自指闭环的
**能力工程（Capability Engineering）范式**，让 agent 的能力面第一次成为可表示、
可对齐、可验证、可治理的一阶计算对象。**

## 2. 背景与要解决的科学问题

三个被证据支撑的现象：

1. **碎片化重复接线。** 每个材料 agent（MatDiscovery / El Agente Sólido / PolyJarvis /
   Catalyst-Agent…）都在手工重接同一批资产（phonopy / ASE / pymatgen / VASP / QE）。
   MCP 只解决传输层，不解决"能力语义层"——范式上是"每个 agent 重新发明一遍接线"。
2. **承诺漂移（claim drift）是普遍、被实测的问题。** BIV 审计 49,943 个技能：
   **80.0% 的声明与实现偏离**；Lejaeghere 等（Science 2016）证明 40+ 个代码可以
   互验同一物理量；而 AutoMat（2026）证明 agent 复现论文声称仅 ~53%。**"代码之间
   可以互验"与"agent 兑现不了声称"这两条线，隔了十年，从未被接起来。**
3. **三种知识形态无法统一。** 同一个能力（"算热容"）以三种形态存在：**代码**
   （phonopy 的实现）、**论文**（methods 的方法描述）、**经验**（博客的 recipe）。
   现有工作各做各的：BIV 只审 skill、ChatExtract 只抽数据、MatPROV 工序图里没有
   软件节点、博客侧完全空白。

**科学问题**：agent 的能力面能否作为一种一阶计算对象被工程化管理——而非一次次
手工装配的产物？对齐的"有效性"本身又能否被验证？

## 3. 核心思想：三层闭环的能力工程范式

![能力工程范式：表示→对齐→验证 三层闭环](figures/capability-engineering-paradigm.html)

> 上图是 archify 生成的正稿（可交互浏览、可导出 SVG/PNG；定稿时直接作为论文 Figure 1）。
> 概念渲染版见 [images/capability-engineering-paradigm.jpg](images/capability-engineering-paradigm.jpg)（汇报/宣传用途）。

**Represent（表示）** —— 把"能力"从散落在代码/论文/经验里的隐含性质，变成显式的
**能力中间表示（Capability IR）**：typed（compute / tool / workflow / data /
interface / concept）+ evidence（可 grep 的指向）+ confidence + source kind。
三种知识形态经统一抽取算子归一进同一个**能力格**（语义锚点：CORA/IEEE 1872
能力本体 + OWL-S/WSMO 契约）。

**Align（对齐）** —— 宿主能力面与参考能力面的**双边对齐**：产出五态差距
（equivalent / partial / missing / host-only / unknown）× 三来源
（宿主自审 / 参考物对比 / 领域推断）+ 落点建议。匹配维度有成熟先例（Paolucci
ISWC'02 四档匹配、RE 追踪五态），我们的增量是**自指 + 跨源 + 证据门控**：
agent 审计自己的面，差距判定叠加证据阈值（epistemic graded subsumption）。

**Verify（验证）** —— **验证先于分类**：每个疑缺口先 grep 宿主代码/查产物 spec
再定性；每跑强制 8 项自检、合成 fixture 金标验收、同输入重跑确定性。产出两个
**库级度量**：`coverage@reference`（对参考物的能力覆盖，区分 coverage 与
adequacy）与 `promise-drift rate`（|声称 − 已验证| / |声称|）。

三环闭环：装配后**再盘点 → 再对齐 → 再验证**，让能力面**可治理**（入库准入 /
漂移检测 / 修剪依据）。

## 4. 四大创新点

| # | 创新 | "空在哪" | 理论锚点 |
|---|---|---|---|
| 1 | **跨形态统一能力格**（repo/paper/blog → 同一 IR） | BIV 单形态；ChatExtract 只抽数据；MatPROV 无软件节点；博客侧空白 | CORA 类型 + DL 概念格 |
| 2 | **Epistemic graded subsumption**：差距判定 = 语义匹配 ∧ 证据阈值（双谓词判定） | Paolucci 四档纯语义；RE 五态纯语义 | Paolucci × 测试充分性（Zhu 1997） |
| 3 | **能力声明的证据义务层**（claim-as-contract + 生命周期：断言→验证→过期→复审） | 凭证/注册表层管"谁签的"；行为验证层管"代码对不对"；中间的"声明↔证据对质"无人系统化；漂移只有测量无机制 | BetterBench × ClaimReceipt × 复现性义务 |
| 4 | **coverage@reference / promise-drift rate**：需求侧库级度量 | 现有度量全是任务侧成功率 | 测试充分性 × FCA/Galois 连接 |

**防守性命题**（防"匹配不新"的质疑）：主张不是"首次能力匹配"——那是 Paolucci/
RE 的地盘——而是**"首次把表示-对齐-验证三环节闭环到自指 agent 上的能力工程"**。
每一层复用既有社群的形式主义，**闭合成环才是新贡献**。

## 5. 差异化定位（系统层，不是 skill 层）

![与系统层邻居的差异定位](figures/capability-engineering-positioning.html)

> archify 正稿（可导 SVG）；概念渲染版见 [images/capability-engineering-positioning.jpg](images/capability-engineering-positioning.jpg)。

| 邻居 | 系统层定位 | 我们的差异 |
|---|---|---|
| Externalization (2604.08224) | "能力外置=基础设施"最成熟论述 | 无科学软件、无参考锚定；我们给它材料领域完整实例化 |
| SkillOps / SkillFoundry | 技能库=软件生态治理；异构资源→技能生成 | 我们做对齐/差距/落点，不做生成/运维 |
| AutoMat (2605.00803) | 论文→流程→验证，53% 复现率 | 只评测不表示/对齐；我们把它与 Lejaeghere"代码互验"接起来 |
| CDD（企业能力工程） | 表示+对齐+验证三环节齐的唯一先例 | 面向组织流程，不面向自指 agent |
| TessIndex / LEGIT / Lemons | 能力验证进身份/凭证/信任（机制层） | 我们做内容级证据验证 |

**材料锚定**：材料领域拥有最集中、最标准化、被社区互验最深的软件资产池
（Lejaeghere 40 代码互验）——能力工程闭环实例化的最优试验场。

## 6. 承诺漂移：为什么这件事重要（核心洞察）

![承诺漂移：声称能力面 vs 可验证能力面](figures/promise-drift.html)

> archify 正稿（可导 SVG）；概念渲染版见 [images/promise-drift.jpg](images/promise-drift.jpg)。

核心洞察：**在一个能力无法被验证的世界里，技能的"市场"会劣币驱逐良币**（Lemons
理论），而**在一个材料计算工具已经互验了半世纪的世界里，"验证能力真值"的资源是
现成的**——只是从未被架到 agent 能力治理上来。capalign 把 BIV 的 80% 漂移率、
Lejaeghere 的代码互验、AutoMat 的 53% 复现率缝合进同一条治理闭环：**声称必须带
证据，证据必须可重跑，重跑必须确定性。**

## 7. 证据计划（见 research/experiments.md）

- E1 差距/来源分类的人工一致性（IRR，κ）
- E2 按报告装配 vs 随机装配 vs 原库的任务增益（对标 SoK curated +16.2pp）
- E3 coverage@reference / promise-drift 在真实库演化的时序曲线 + stale-skill 召回
- E4 自指审计的可靠性校准（自报面 vs 验证面的校准——理论空白）

案例资产已在手：phonopy↔MatDiscovery 全程记录（19 缺口、A–E 分档、三次防伪缺口
教训），真实 37-skill 库，SKILLS-AUDIT 作为承诺漂移真实语料。

---

*三张图均有 archify 正稿（`figures/*.html`，可导 SVG 作论文 Figure 1–3）；三份 SVG 已提取到
`figures/*.svg` 可直接进排版。image-gen 概念渲染版保留在 `images/` 供汇报/宣传。*