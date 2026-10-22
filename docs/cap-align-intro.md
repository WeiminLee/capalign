# cap-align — 能力对齐（Capability Alignment）项目介绍

> 本文介绍本仓库的**功能职责**与**运行逻辑**：cap-align 是什么、解决什么问题、
> 装进宿主 agent 后如何一步步运转、靠什么纪律保证"对齐结果可信"。
> 配图为 image-gen 生成的概念渲染版（正稿 SVG/HTML 见 `figures/`）。

---

## 1. 项目是什么

**cap-align 是一个可插拔、框架无关、零捆绑的"能力对齐" skill。** 核心能力：

> 给定一篇材料论文（及其配套仓库），把其中的**材料能力**对齐到用户自己的材料
> agent，产出三样东西：**能力清单**、**差距表**、**引入卡片**。
> 该装的才写宿主自有的 skill / tool，并带改前必败的测试合同；该拒绝的写明宿主不改。
> 对齐完成 = 宿主自己拥有这些动词；把参考 agent 嵌进宿主不是对齐。这一轮不改宿主。

仓库与论文是同一科学工作的两份编码；skill 对两份编码走同一套判定。博客是第三
种编码，产品支持，论文主文钉 paper / repo。

- **可插拔**：装进任何支持 `SKILL.md` + `references/` 的 agent 框架
  （Claude Code / Anthropic Agent Skills / DeepSeek Harness / Cursor / .agents …），
  不调用任何框架专有 API。
- **零捆绑**：不预装任何脚本与依赖，盘点命令由 agent 用宿主环境现成的
  bash / python3 即席执行。
- **只到建议为止**：对齐的终点是落点建议，不是动手实现缺口——"建不建"是宿主
  及其人类的产品/工程决策（报告以固定结语声明这一点）。
- **只对齐材料能力**：核心是能模拟什么物理量；上限是材料 agent 方法（评测势、
  微调、蒸馏）。plugin / MCP / lockfile / 装环境不进差距表。同一物理量换计算器
  不算新缺口。
- **宿主自有**：落点写在宿主自己的 skill/tool/runner 上。可以调用上游科学引擎
  （VASP、phonopy、某个势的训练器）；不能 wrap 参考 agent 的 clone / plugin / MCP。

项目同时承载一篇学术论文（主张与创新见 [`paper-core.md`](paper-core.md)）：
把一篇外来科学工作 \(W=(\mathrm{paper},\mathrm{repo})\) 当成双编码能力规格，
相对于已有宿主做证据门控判定。skill 是该判定过程的测量仪器；贡献是双编码规格、
宿主相对判定、参考条件化覆盖——「闭环」是仪器形状，不是创新点。

![cap-align 执行过程：三种参考物输入 → 八步工作流（盘点参考 → 盘点宿主 → 归一化 → 验证 → 分类 → 落点 → 报告 → 自检）→ 输出报告与 IR。图为 archify 交互图](images/cap-align-principle.png)

---

## 2. 仓库结构与资产

```
cap-align/
├── SKILL.md                 # skill 本体：frontmatter + 八步工作流（含交叉验证与报告自检）
├── references/              # 规则与契约（methodology / IR / alignment / inventory / report/evaluation）
├── tests/                   # 验收 fixtures（mini-ref / mini-host / mini-paper / mini-blog + gold 金标）
├── research/                # 论文与实证（formal-foundations / experiments / runs / tools）
├── docs/                    # 论文核心稿 + 图（archify 正稿 figures/ + 概念渲染 images/）
└── README.md
```

| 资产 | 位置 | 职责 |
|---|---|---|
| skill 本体 | `SKILL.md` | 八步工作流 + 输出契约 |
| 方法论（三层纪律） | `references/methodology.md` | 通用方法（七阶段）→ 可插拔适配层 → 实例 |
| 中间表示 IR | `references/capability-ir.md` | 统一 schema、类型词表、归一化与粒度边界 |
| 对齐/落点规则 | `references/alignment-rules.md` | 五态差距 × 三来源、范围（材料模拟 / 材料 agent / plumbing）、引入卡片、落点六问、宿主 doctrine 优先 |
| 盘点启发式 | `references/inventory-heuristics.md` | repo/paper/blog/宿主盘点 + §E 配套论文/邻域回收（零捆绑） |
| 评估 | `references/evaluation.md` | Layer-1 每跑自检 + Layer-2 fixture 金标验收 |
| 报告契约 | `references/report-contract.md` | 报告必含字段与 `self_check:` 头块 |
| 实证与论文 | `research/` | E1–E4 协议、断言 A–E 形式化、漂移测量工具 |

---

## 3. 功能职责

### 3.1 输入与输出

| 输入 | 输出 |
|---|---|
| 仓库路径和/或主页（同一工作） | `capability-alignment-report.md`（核心差距表 + 邻域节 + 落点建议）；回收配套论文与有界邻域 |
| 论文文本（paper） | `capability-alignment.json`（IR 机器可读伴侣） |
| 博客/文稿（blog） | 逐条可溯源：每条能力带 evidence 指针，每条落点推荐引用规则号 |

### 3.2 八步工作流（SKILL.md，顺序执行）

1. **盘点参考物** — 按参考物种类套用启发式（repo：CLI 入口 + 顶层模块 + 文档功能页
   + 依赖指纹，然后按 §E 回收配套论文与有界邻域：本地种子 → 主页 → 必要时
   web-search；paper：Methods→步骤分解 + 硬依赖；blog：声称 + recipe + 引文），
   产出参考能力清单（IR）。核心 \(W\) 与邻域 \(N\) 分层，身份门决定去留。
2. **盘点宿主面** — 自动扫描 skill 目录 / `SKILL.md` / 工具注册表；**强制**做宿主
   自审扫描（找 AUDIT/roadmap，宿主自认的缺口打 `host-self-audit` 标）；扫描关不
   上的缺口以纯文本询问调用者，答复按权威宿主 IR 采信。
3. **归一化** — 双侧清单落入同一个能力 IR：语义单元、稳定 id、合并重复、低置信项
   显式标记。
4. **交叉验证疑缺口** — **验证先于分类**：每个疑似 `missing`/`partial` 都要去宿主
   代码/文档里 grep 能力词、读产物 spec、查既有部分路径；比对表只是假设，验证才
   是证据。
5. **差距分类 + 来源标注** — 每项参考能力分类为 `equivalent | partial | missing |
   host-only | unknown`，并打来源标签（`host self-audit | reference-contrast |
   domain inference`）；`missing` 必须 ≥1 条 high/medium 的**已验证**证据，
   低置信证据永远推不出 `missing`。
6. **引入卡片，再落点** — 两侧按产物并成一张卡（`references/introduction-card.md`）。
   标签由槽位算出。只有 `install` 才套落点六问（见 §4.4）；`refuse` 引用规则 7，
   不写技能名，成功是宿主不改。测试合同写在同一张卡上，这一轮不执行。
7. **撰写报告** — 按 report-contract 的必需章节组织，结尾固定结语。
8. **报告自检门** — 跑 Layer-1 十二项自检（含邻域分层、宿主自有落点、卡片路由、测试合同），
   `self_check:` 头块必须全绿，否则整轮无效、回炉重做。

### 3.3 产出物示例形状（IR）

```json
{
  "surface": { "label": "phonopy", "source_kind": "repo", "generated_at": "ISO-8601" },
  "capabilities": [
    {
      "id": "thermal-properties",
      "name": "thermal properties",
      "type": "compute",
      "description": "compute thermal properties from phonon DOS",
      "evidence": [{"kind": "cli", "location": "src/…:123"}],
      "confidence": "high"
    }
  ]
}
```

能力类型词表：`compute | tool | skill | workflow | data | interface | concept`——
能力是"用户可达的语义单元"，不是文件/函数计数（一个仓库归一化后约 10–30 条；更细
是过拆分，更粗是过合并）。

---

## 4. 运行逻辑

### 4.1 数据流与判定主线

![运行逻辑：双盘点 → 归一化 → 验证门 → 五态分类 → 双自检门](images/cap-align-workflow.jpg)

```
参考物(repo/paper/blog) ──┐
                         ├──▶ 归一化到能力 IR ──▶ 交叉验证(证据门) ──▶ 五态差距×三来源
宿主 agent 能力面 ────────┘                          ▲                       │
       ▲                                             └── 只有验证过的证据 ──── ▼
       └────────────────────────────────────────────────────────────── 落点建议(引用规则号)
                                                                    └──▶ 报告 + self_check 自检门
```

### 4.2 三层方法论纪律（references/methodology.md）

| 层 | 放什么 | 可复用性 |
|---|---|---|
| **通用方法** | 七阶段流程 + 纪律规则，中性语言、零宿主/领域词汇 | 任何宿主、任何参考物 |
| **可插拔适配层** | 宿主自己的能力面 doctrine（skill/tool 轴、命名、报告方言）+ 领域词典 | 按宿主/按领域替换 |
| **实例** | phonopy ↔ MatDiscovery 等具体跑次 | 是方法的证据，不是方法本身 |

纪律：通用层写进任何"宿主文件、宿主产物名、某领域词典"的规则都必须上移/下沉，
否则就住错了层。**落点六问、验证先于分类、消错>兑现>扩宽 排序**均以中性语言写进
通用层，phonopy 案例只是首次验证它的实例。

### 4.3 差距判定语义（formal-foundations：语义匹配 ∧ 证据门）

- **covers(h, r) = 语义匹配 ∈ {exact, plugin} ∧ 比较证据强度 ≥ θ** —— 语义判定与
  证据阈值是**双谓词合取**：只说"形态像"不够，还要有 grep 可验证的对质轨迹。
- `partial` 是**严格子集**语义：宿主能力真含盖参考能力的一部分才算；"相邻但不包含"
  不算 partial，记进缺口的 near-miss 注记，缺口仍判 `missing`。
- **同一物理量换计算器是 `equivalent`**，不是 missing。材料 agent 方法（吸附能
  评测协议、微调、蒸馏）仍可单独判 missing。
- `missing` 需要 ≥1 条 high/medium **已验证**参考侧证据；验证不了的缺口是
  `unknown`，绝不硬判 `missing`。
- **反缺口也上报**：宿主有而参考没有的 `host-only` 是信息，不是噪声。

### 4.4 落点六问（alignment-rules §Placement，按序问）

1. **Axis** — 这是"做事的方式"（skill）、"确定性计算"（tool/script）还是
   "设置/界面/服务面"（plugin/server）？裸 `compute` 通常要 tool 或 script，不要
   plugin。
2. **Tool vs script** — 改动次数测试：一处计算多处消费 → 共享 tool；只被一个 skill
   消费 → 放该 skill 的 companion scripts。门禁/渲染/审计/并行需求推到 tool。
3. **新 skill vs 扩既有** — 相同输入契约 + 相邻问题类 → 扩展既有 skill（最小正文 +
   专属 reference 页）；独立路由触发或不同输入契约 → 新 skill。
4. **约束归属** — 每条有效性约束指明由哪层持有：静态可查 → linter/门禁；运行时
   才知 → hook/runner 自报；机械不可判 → agent 判断（写进 skill 正文）。
5. **Never** — 参考侧证据全是 `low` 的能力绝不推荐，标 `unknown`。
6. **宿主自有** — 落点是宿主自己的 skill/tool/runner。参考物若是科学引擎，宿主
   可以调用它；若是 agent/hub，把被驱动的材料动词写成宿主原生能力，可调同一套
   上游引擎，不可 clone / wrap / MCP 挂载该 hub。

### 4.5 三条质量防线

| 防线 | 机制 | 失败后果 |
|---|---|---|
| 交叉验证门（Phase 2） | 分类前必须先验证；E1 首跑 ~25 个疑缺口里 grep 杀掉 4 个假缺口（Grüneisen、群速度实为已有；α 是 partial 不是 missing） | 假缺口进表 = 错误产品 |
| Layer-1 自检门（每跑强制） | 报告头块 `self_check:`，16 项检查（章节齐全 / 证据已验证 / 无 low 推 missing / 规则引用 / 来源标签 / host-only 在场 / 结语精确 / 重跑确定性 / 邻域分层 / 宿主自有落点 / 卡片路由 / 测试合同 / 槽位证据与分叉一致 / 验证诚实性 / agent 能力边界 / 桥而非护栏） | **任一 fail = 整轮无效**，不是"基本完成" |
| Layer-2 金标验收（装机或改规则时） | mini-ref / mini-host / mini-paper / mini-blog 四组 fixture + 手算 gold；零捆绑、无测试框架，径直跑 skill 自己的工作流比对 | 与 gold 的**未登记**差异 = 回归，需裁决修复或登记规则变更 |

### 4.6 零捆绑怎么落地

skill 本体不含任何可执行代码，全部"代码"是给 agent 的指令。例如盘点仓库：
agent 在宿主 shell 里跑 `ls <repo>; cat pyproject.toml; grep -rn console_scripts …`，
用宿主现成的命令完成盘点；跑验收也走同一套指令流程。因此 skill 装进任何框架都
无需适配安装，也不引入供应链依赖。

---

## 5. 论文与实证层（research/）

### 5.1 科学主张：双编码规格上的宿主相对对齐

![判定过程的仪器：表示 → 对齐 → 验证](images/cap-align-paradigm.jpg)

材料领域同时堆积已部署的 agent 与「论文 + 配套仓库」。用户的问题是：这篇论文
里的能力，我的 agent 已经有哪些、缺哪些、缺的落在哪。论文把这件事收成三个对象
（详见 [`paper-core.md`](paper-core.md)）：

1. **双编码规格** \(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\) —— 同一科学工作的
   方法面与接口面；同一性谓词跨编码共用。
2. **宿主相对判定** \(\mathrm{Gap}(H,W)\) —— 静态、证据门控、可复现；不跑参考、
   不实现缺口。这就是「把 paper 能力对齐到用户自己的 agent」的形式。
3. **参考条件化覆盖** —— \(\mathrm{coverage}(H,W_{\mathrm{paper}})\) 与
   \(\mathrm{coverage}(H,W_{\mathrm{repo}})\) 分叉；双对齐是因为两份规格本来
   就不是同一张表。

匹配（Paolucci / RE）与包内漂移测量（BIV）是邻居；「闭环」是仪器形状。贡献是
规格、判定、覆盖随编码分叉。

### 5.2 形式化定义与断言（formal-foundations.md）

| 对象 | 定义 | 可证伪断言 |
|---|---|---|
| 科学工作 \(W\) | 双编码能力规格 \((W_{\mathrm{paper}}, W_{\mathrm{repo}})\) | C1：同一资产上两面残差非空、可分类（EΔ） |
| 能力 IR | `C = (id, τ, l, E, conf, src)`，τ∈六型，E=证据集 | 同一性谓词的载体 |
| covers 判定 | 语义匹配 ∧ 证据强度 ≥ θ | A：判定关于证据单调（加证据可 unknown→missing） |
| \(\mathrm{Gap}(H,W)\) | 五态 × 三来源 + 落点 | C2：同一谓词在 repo 臂与 paper 臂上 IRR（E1） |
| coverage@reference | 分 paper 投影与 repo 投影；raw vs adequacy-gated | B / C3：按哪份规格装配，任务增益形状不同（E2） |
| 自参照偏差 | bias = 自报面 − 相对外来 \(W\) 的验证面 | D：bias ≥ 0 且可校准；否则只能外部对齐（E4） |

包内 `promise-drift`（|声称 − 已验证| / |声称|）降为分解项，不与 BIV 的 80% 比规模。

### 5.3 实证计划（全部跑在 skill 自己的工作流上）

- **E1 IRR**：同一判定在 repo 臂与 paper 臂上可复现。已落地：P1 κ=0.853、
  P2 κ=1.000（同模型三 judge，真 IRR 未达成）。
- **EΔ 跨形态残差**：同一科学工作的 \(W_{\mathrm{paper}}\bowtie W_{\mathrm{repo}}\)
  （phonopy methods vs phonopy 仓库）。**未跑**，C1/C3 的命门。
- **E2 三臂 / 双规格装配**：按 paper 规格补 vs 按 repo 规格补 vs 随机 / 不补。
  协议就绪；真实层 gold pending。
- **E3 库级 coverage(H,W)**：需求侧覆盖分布。已有 2 库包内 drift（K-Dense 30.3%、
  MatDiscovery 11.2%），需求侧分布未立。
- **E4 自参照校准**：自报面相对外来 \(W\)。mini 实测 bias=0.0，fixture 太干净
  不可证伪。

### 5.4 两个研究工具（research/tools/，纯 stdlib）

```bash
python3 research/tools/build-registry.py <repo-root> --out reg.json   # 建能力面 registry
python3 research/tools/drift-meter.py <skills_dir> --registry reg.json --table  # 测承诺漂移
```

### 5.5 首个验证实例（记录在 methodology §3）

phonopy ↔ MatDiscovery：19 个缺口、A–E 成本分档、三次"防伪缺口"教训（grep 扫掉 4
个假缺口；host 自审源优先；positive-evidence 胜出记录不撤改）。该实例专供佐证方法，
**刻意不进** fixture 池——测试永不依赖方法唯一绑定的那个例子。

---

## 6. 当前状态与开放边界

**已落地**（2026-10-15，8 commits，HEAD `bea0c8b`）：八步工作流 + 自检门定稿；
F1/F2/F3 三条 pilot 缺陷全部落码；四组 fixture 与 gold 同步；E1–E4 均有首轮结果；
论文核心稿与三张 archify 正稿已交付。

**诚实边界**：
- E1 κ 是同模型三 judge 下限信号，人类/第二模型 judge 未到位 → 真 IRR 未达成；
- EΔ（phonopy methods ⋈ phonopy 仓库）未跑 → C1/C3 仍是假说；
- E2 真实层数值 gold 待 phonopy 可执行安装；按 paper vs repo 规格拆臂尚未做；
- 需求侧 `coverage(H,W)` 分布未立；E4 mini fixture 太干净不可证伪；
- 断言 E（stale recall）需要纵向 git 历史，尚未开跑。

**复现命令**：漂移测量见 §5.4；fixture 验收按 `tests/README.md` 指令式运行：
`inventory → align → 比对 gold/*.json`，零捆绑，无测试框架。

---

*配图为 image-gen 概念渲染；论文用 archify 正稿（`docs/figures/*.html`/`*.svg`）*
*以 `self_check:` 头块全绿为准；引用以 references/ 各契约文件为准。*