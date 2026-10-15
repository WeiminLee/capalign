# capalign — 能力对齐（Capability Alignment）

> **给 agent 装上"能力审计"**：把宿主 agent 的能力面，对齐到一份参考物
> （代码仓库 / 论文 / 博客），产出 **能力清单 · 差距表 · 逐缺口落点建议**。

**框架无关 · 可插拔 · 零捆绑** 的 agent skill。

![capalign 一览：repo / paper / blog 三种参考物 → 统一能力记录 → 与宿主 agent 能力面对齐 → 清单 + 差距 + 落点](docs/images/capalign-overview.jpg)

---

## 这是什么

capalign 解决一个具体问题：

> 你面前有一个参考物——一份想接入的代码仓库、一篇方法论文、或一篇实操博客。
> **你和它差在哪里？该补什么？** capalign 把这两个问题变成一次可复现的审计，
> 输出三样东西：

1. **能力清单**（inventory）— 参考物"能做什么"、宿主 agent"能做什么"，各一张表
2. **差距表**（gap table）— 五态分类：`equivalent / partial / missing / host-only / unknown`
3. **落点建议**（placement）— 每条差距建议用 `新 skill / 新 tool / 扩既有 / runner 契约 / 跳过` 哪种方式补齐

**设计约束：**

| 约束 | 含义 |
|---|---|
| 框架无关 | 装在任何支持 `SKILL.md` + `references/` 的框架：Claude Code / Anthropic Agent Skills / DeepSeek Harness / Cursor / .agents… |
| 零捆绑 | 不预装脚本与依赖；盘点命令由 agent 用宿主环境现成的 bash / python3 即席执行 |
| 只建议，不实现 | 对齐的终点是推荐；"建不建"是宿主及其人类的产品决策（报告以固定结语声明） |

**它不做什么**：不运行参考工具本身、不替你实现缺口、不做脱离"能力面"框架的通用摘要。

---

## 能做什么

| 输入 | 输出 |
|---|---|
| **repo** — 代码仓库路径（仿真 / DFT / ML 工具） | `capability-alignment-report.md`（差距表 + 落点建议 + 自检块） |
| **paper** — 论文文本 | `capability-alignment.json`（IR 机器可读伴侣，与报告同源） |
| **blog** — 博客 / 文稿 | 同上一套；每条能力带原文引文为证 |

**八步工作流**（详见 `SKILL.md`）：

| # | 步骤 | 一句话 |
|---|---|---|
| 1 | 盘点参考物 | repo：CLI 入口 + 顶层模块 + 文档页 + 依赖指纹；paper：Methods 拆步骤；blog：声称 + recipe |
| 2 | 盘点宿主面 | 自动扫 skill 目录 / 注册表 + **强制宿主自审扫描** + 扫描不全则询问兜底 |
| 3 | 归一化 | 双侧落进同一能力 IR（typed + evidence 指针 + confidence + source） |
| 4 | 交叉验证 | **验证先于分类**：比对表只是假设，grep 宿主代码、读产物 spec 才是证据 |
| 5 | 分类 + 来源 | 五态差距 × 三来源（宿主自审 / 参考对比 / 领域推断） |
| 6 | 落点 | "落点五问"逐缺口给建议，每条引用其满足的规则号 |
| 7 | 报告 | 按报告契约的必需章节组织 |
| 8 | 自检门 | `self_check:` 8 项检查，任一 fail = 整轮无效、回炉 |

---

## 快速开始

**1. 安装 —— 一行命令**

```bash
npx skills add WeiminLee/capalign -g     # 全局安装；或 -p 装到当前项目
```

装好后 skill 出现在宿主框架 skills 目录（如 `.agents/skills/capability-align`），
适用于 Claude Code / Cursor / Codex / GitHub Copilot 等。想先试用、不落盘：

```bash
npx skills use WeiminLee/capalign@capability-align
```

**手动安装**：也可直接把 `SKILL.md` 与 `references/` 拷入宿主框架的 skills 目录，
或对话中指给 agent。没有依赖要装，没有脚本要跑。

**2. 使用 —— 给 agent 一句话**

```
capability-align <repo 路径 | paper 文本 | blog 文本>
```

例：`capability-align /path/to/phonopy` —— agent 盘点该仓库的能力面，
扫描你自身的能力面，对齐后产出差距表与落点建议。

**3. 看结果 —— 落在工作区根目录**

```
capability-alignment-report.md   # 人读：清单 / 差距表 / 建议 / 自检块
capability-alignment.json        # 机读：IR 伴侣
```

**4. 验收 —— 装机或改规则后跑一遍 fixture（零捆绑、无测试框架）**

```
1. 盘点：reference = tests/fixtures/mini-ref（mini-paper / mini-blog 同理）
2. 对齐：mini-ref vs mini-host
3. 比对：输出 vs tests/fixtures/gold/*.json，逐条 differ
```

通过标准：与 gold **零未登记差异** + 该次跑 Layer-1 自检全绿。详见 `tests/README.md`。

**研究工具**（承诺漂移测量，纯 stdlib）：

```bash
python3 research/tools/build-registry.py <repo-root> --out reg.json
python3 research/tools/drift-meter.py <skills_dir> --registry reg.json --table
```

---

## 工作原理

![运行逻辑：双盘点 → 归一化 → 验证门 → 五态分类 → 双自检门](docs/images/capalign-workflow.jpg)

| 阶段 | 发生什么 |
|---|---|
| 双盘点 | 参考侧与宿主侧**互不参照**地各建一张能力表——分离是规则，不是方便 |
| 归一化 | 三种知识形态 → 统一 IR：`type（compute/tool/workflow/data/interface/concept）+ evidence + confidence + source` |
| 验证门 | 每个疑缺口先 grep 宿主代码、读产物 spec、查既有部分路径；首跑 ~25 个候选中 grep 干掉 4 个假缺口 |
| 双谓词判定 | 覆盖 = 语义匹配 ∧ 证据强度 ≥ 阈值；`partial` 是严格子集语义；`low` 置信证据永远推不出 `missing` |
| 落点五问 | axis（skill / tool / plugin）→ tool vs script → 新 skill vs 扩既有 → 约束归属 → never |
| 报告 + 自检 | 报告头块 8 项自检；同输入重跑必须产出相同差距表 |

三个设计纪律（`references/methodology.md`）：

- **三层分离**：通用方法层（零宿主词汇、任何领域可用）→ 可插拔适配层（宿主的
  doctrine、领域词典，按宿主替换）→ 实例层（phonopy↔MatDiscovery 只是验证它的
  第一个证据，不是方法本身）
- **验证先于分类**：比对表是假设，交叉验证才是证据——把假缺口挡在表外
- **消错 > 兑现 > 扩宽**：优先级先修"系统性错的、承诺了却没有的"，再补整类问题，
  最后才上新问题类；优先级判断写进报告，允许被反驳

---

## 为什么可信

**三层防御 + 首轮实证**（都跑在 skill 自己的工作流上，不自造 harness）：

| 防线 | 机制 |
|---|---|
| 交叉验证门 | 分类前强制验证；实例记录：4 个疑似缺口经 grep 证实宿主已具备 → 未进表 |
| Layer-1 自检门 | 每跑强制；任一 fail 即"无效"，不是"基本完成" |
| Layer-2 金标 | 四组 fixture + 手算 gold；gold 修订必须带 `log:` 登记 |

**第一轮实证结果**：

| 实验 | 问的问题 | 结果 |
|---|---|---|
| E1 判卷一致性（IRR） | 五态 × 三来源的判定可复现吗 | P1 κ=**0.853**、P2 κ=**1.000**（pass bar 0.6） |
| E2 三臂装配 | 按报告补 > 随机补 > 不补？ | 协议 + 32 任务套件就绪；真实层数值 gold 待 phonopy 安装（已标注 pending） |
| E3 承诺漂移 | "声称"与"已验证"的差跨库普遍吗 | K-Dense 177 skills **30.3%** vs MatDiscovery **11.2%** |
| E4 自参照校准 | agent 自审自己的能力面可信吗 | mini 实测 bias=0.0、cal(high)=0.75 |

![三层能力工程范式：表示 → 对齐 → 验证 闭环](docs/images/capalign-paradigm.jpg)

capalign 是一篇研究论文的**首个完整实现**：**能力工程（Capability Engineering）**
——把表示（Represent）、对齐（Align）、验证（Verify）做成自指闭环，让 agent 的
能力面第一次成为可表示、可对齐、可验证、可治理的一阶计算对象；并给出两个库级
度量：`coverage@reference`（对参考物的可靠覆盖）与 `promise-drift rate`（|声称 − 已验证| / |声称|）。

- 论文核心稿（主张 / 创新点 / 差异化定位）：[`docs/paper-core.md`](docs/paper-core.md)
- 形式化定义与可证伪断言 A–E：[`research/formal-foundations.md`](research/formal-foundations.md)
- 实证协议 E1–E4：[`research/experiments.md`](research/experiments.md)
- 项目进展与复现命令：[`docs/progress.md`](docs/progress.md)

---

## 目录结构

```
capalign/
├── SKILL.md            # skill 本体：八步工作流 + 自检门
├── references/         # 规则与契约：methodology / IR / alignment / inventory / evaluation / report
├── tests/              # 验收 fixtures：mini-ref / mini-host / mini-paper / mini-blog + gold 金标
├── research/           # 论文与实证：formal-foundations / experiments / runs / tools
├── docs/               # 论文核心稿 + 项目介绍 + 图（figures/ 正稿 · images/ 概念渲染）
└── README.md
```

## 诚实边界（不做假装）

- E1 κ 仍为**同模型三 judge** 的下限信号——人类 / 第二模型 judge 未到位，真 IRR 未达成；
- E2 真实层数值 gold 依赖 phonopy 可执行安装，当前为 pending；
- E3 仅 2 个库——断言 C 的"分布 / AUROC 预测"尚未成立；
- 断言 E（stale-skill 召回）需要纵向 git 历史，尚未开跑。