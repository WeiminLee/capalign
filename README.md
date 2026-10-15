# capalign — 能力对齐 skill（可插拔）

一个**框架无关、可安装到任意 agent 框架**的能力对齐 skill：
给定一个**参考物**（代码仓库 / paper / 博客文稿），盘点参考物的能力面，
与**宿主 agent 自身的能力面**对齐，产出：能力清单、差距表、逐缺口的落点建议
（新 skill / 新 tool / 扩既有 / runner 契约 / 跳过）。

**插拔式**：装在任何支持 `SKILL.md` + `references/` 的 agent 框架里
（Claude Code / Anthropic Agent Skills / DeepSeek Harness / Cursor / .agents …），
不调用框架专有 API。**零捆绑**：不预装任何脚本/依赖，盘点命令由 agent 用宿主
环境现成的 bash / python3 即席执行。

## 结构

```
capalign/
├── SKILL.md                 # skill 本体：frontmatter + 工作流八步（含交叉验证与报告自检）
├── references/
│   ├── methodology.md           # 通用方法论（三层：通用/可插拔适配/实例）
│   ├── evaluation.md            # 有效性评估：Layer1 运行自检 + Layer2 fixture 验收
│   ├── inventory-heuristics.md  # 三种参考物清单 + 宿主能力面扫描命令（零捆绑）
│   ├── capability-ir.md         # 能力中间表示 schema + 归一化规则
│   ├── alignment-rules.md       # 差距分类 + 落点五问 + 宿主 doctrine 适配
│   └── report-contract.md       # 报告结构（含 self_check 头块）+ 有效性规则
├── tests/
│   ├── README.md                # 验收测试怎么跑（指令式，零捆绑）
│   └── fixtures/
│       ├── mini-ref/            # 迷你 phonon 引擎（含 doc-claim 诱饵）
│       ├── mini-host/           # 迷你宿主面（skill+registry+自审账本）
│       ├── mini-paper.md        # 迷你论文摘录
│       ├── mini-blog.md         # 迷你博客
│       └── gold/                # 三份金标准（gap 分类 / 论文清单 / 博客清单）
└── .gitignore
```

## 用法（宿主 agent 视角）

```
capability-align <repo 路径 | paper | blog 文本>
  → 六步：盘点参考物 → 扫描宿主面（缺则询问）→ 归一化 IR → 差距分类
    → 落点推荐（引用规则号）→ 写报告
  → 产物：capability-alignment-report.md + capability-alignment.json
```

## 规则来源与状态

落点规则（alignment-rules.md）与核心方法论（methodology.md）是**通用、可复用的**：
方法论分三层——通用方法（任何宿主/任何参考物可用）→ 可插拔适配层（宿主自己的
能力面 doctrine、领域词典——按宿主/按领域替换）→ 实例（phonopy↔MatDiscovery
只是第一次验证它的实例，不是方法本身）。三层分离纪律：通用层不出现任何宿主或
领域词汇。落点五问、差距三分源、验证先于分类、消错>兑现>扩宽 排序，均以中性
语言写成。

**已定**（2026-10-15 与用户对齐）：指令式零捆绑 · 宿主面自动扫描+询问兜底 ·
repo/paper/blog 三种全收 · 方法论可复用不绑 phonopy。实现顺序待定：repo 形态
（已被验证过）先行，paper/blog 随后。