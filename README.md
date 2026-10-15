# capalign — 能力对齐（Capability Alignment）

> **把一个 agent 的能力面，对齐到一份参考物**（代码仓库 / 论文 / 博客），
> 产出 **能力清单**、**差距表** 和每条差距的 **落点建议**
> （新 skill / 新 tool / 扩展既有 / runner 契约 / 跳过）。

**可插拔 · 框架无关 · 零捆绑** —— 装进任何支持 `SKILL.md` + `references/` 的 agent
框架（Claude Code / Anthropic Agent Skills / DeepSeek Harness / Cursor / .agents…）。
不调用任何框架专有 API，不预装任何脚本与依赖：盘点命令由 agent 用宿主环境现成的
bash / python3 即席执行。

---

## 一览

![capalign 整体流程：repo / paper / blog 三种参考物 → 统一能力 IR → 与宿主 agent 能力面对齐 → 差距表 + 落点建议](docs/images/capalign-overview.jpg)

---

## 它能做什么

| 输入 | 输出 |
|---|---|
| **repo** — 一个代码仓库路径（仿真 / DFT / ML 工具） | `capability-alignment-report.md`：差距表（五态分类 × 三来源）+ 逐缺口落点建议 |
| **paper** — 一篇论文文本 | `capability-alignment.json`：机器可读的 IR 伴侣 |
| **blog** — 一篇博客 / 文稿 | 每一条能力带 evidence 指针，每一条推荐引用规则号 |

**八步工作流**（详见 `SKILL.md`）：

盘点参考物 → 盘点宿主面（含宿主自审扫描）→ 归一化到能力 IR → 交叉验证疑缺口 →
差距分类 + 来源标注 → 落点推荐 → 撰写报告 → **自检门**（`self_check:` 全绿才算有效）。

> 对齐的终点是**建议**，不是实现：逐缺口的落点是"该用什么方式补"，建不建由宿主
> 及其人类决定（报告以固定结语声明这一点）。

---

## 它是怎么运转的

![运行逻辑：双盘点 → 归一化 → 验证门 → 五态差距 × 三来源 → 双自检门](docs/images/capalign-workflow.jpg)

**核心机制：**

- **统一能力 IR** — 三种知识形态（代码 / 论文 / 经验）经同一套抽取算子，归一成同一
  种 shape：`typed（compute / tool / workflow / data / interface / concept）+
  evidence（可 grep 的指向）+ confidence + source kind`。一个仓库约归一化为 10–30 条
  能力——能力是"用户可达的语义单元"，不是文件/函数计数。
- **验证先于分类** — 比对表只是假设，交叉验证才是证据：每个疑缺口先 grep 宿主代码、
  读产物 spec，再定性。首跑 ~25 个疑缺口里 grep 杀掉 4 个假缺口。
- **Epistemic graded subsumption** — 差距判定 = 语义匹配 ∧ 证据强度阈值（双谓词
  合取）；`partial` 是严格子集语义；`low` 置信证据永远推不出 `missing`。
- **落点五问** — axis（skill vs tool vs plugin）→ tool vs script → 新 skill vs 扩既有
  → 约束归属 → never（低证据绝不推荐）。
- **三层方法论纪律** — 通用方法层（零宿主词汇）/ 可插拔适配层（宿主 doctrine、领域
  词典，按宿主替换）/ 实例层（phonopy↔MatDiscovery 只是证据，不是方法本身）。

---

## 为什么可信：三层防线 + 实证

| 防线 | 机制 |
|---|---|
| **交叉验证门** | 分类前必须验证；假缺口不进表 |
| **Layer-1 自检门（每跑强制）** | 报告头块 `self_check:` 8 项检查，任一 fail = 整轮无效 |
| **Layer-2 金标验收（装机/改规则时）** | mini-ref / mini-host / mini-paper / mini-blog 四组 fixture + 手算 gold，零捆绑跑通 skill 自己的工作流 |

**第一轮实证结果**（E1–E4，全部跑在 skill 自己的工作流上）：

- **E1 判卷一致性（IRR）**：P1 κ=**0.853**、P2 κ=**1.000**（pass bar 0.6）
- **E3 承诺漂移测量**：K-Dense 177 skills 漂移 **30.3%**、MatDiscovery **11.2%**
- **E4 自参照校准**：mini 实测 bias=0.0、cal(high)=0.75

![三层能力工程范式：表示 → 对齐 → 验证 闭环，可治理、可再盘点](docs/images/capalign-paradigm.jpg)

配套论文《From Scientific Software Assets to Agent Capabilities》把对齐升级为
**能力工程（Capability Engineering）范式**：表示（Represent）→ 对齐（Align）→
验证（Verify）三层闭环，带形式化定义（断言 A–E）与两个库级度量
`coverage@reference` 与 `promise-drift rate`；capalign 是该范式的**首个完整实例化**。
论文核心稿见 `docs/paper-core.md`，形式化见 `research/formal-foundations.md`。

---

## 快速开始

```bash
# 1. 把 skill（SKILL.md + references/）装进你的 agent 框架
# 2. 指向参考物运行（宿主 agent 视角）
capability-align <repo 路径 | paper 文本 | blog 文本>
#    → capability-alignment-report.md + capability-alignment.json
```

**验收测试**（零捆绑，无测试框架，径直跑 skill 自己的工作流）：

```
1. 盘点：reference = tests/fixtures/mini-ref（paper / blog 同理）
2. 对齐：mini-ref vs mini-host
3. 比对：输出 vs tests/fixtures/gold/*.json，逐条 differ
```
要求：与 gold **零未登记差异** + 该次跑 Layer-1 自检全绿。详见 `tests/README.md`。

**研究工具**（纯 stdlib）：

```bash
python3 research/tools/build-registry.py <repo-root> --out reg.json
python3 research/tools/drift-meter.py <skills_dir> --registry reg.json --table
```

---

## 目录结构

```
capalign/
├── SKILL.md              # skill 本体：八步工作流 + 自检门
├── references/           # 规则与契约（methodology / IR / alignment / inventory / evaluation / report）
├── tests/                # 验收 fixtures（mini-ref / mini-host / mini-paper / mini-blog + gold）
├── research/             # 论文与实证（formal-foundations / experiments / runs / tools）
├── docs/                 # 论文核心稿 + 项目介绍 + 图（figures/ 正稿 · images/ 概念渲染）
└── README.md
```

---

## 当前状态（2026-10-15）

- 8 个 commit，工作区干净（HEAD `bea0c8b`）；F1/F2/F3 三条 pilot 缺陷全部落码。
- **诚实边界**：E1 κ 仍为同模型三 judge 下限信号（人类/第二模型 judge 未到位）；
  E2 真实层数值 gold 待 phonopy 可执行安装；E3 仅 2 个库；断言 E（stale recall）
  尚未开跑。详见 `docs/progress.md`。
- 复现命令与逐项状态均记录在案，不假装未完成的部分。