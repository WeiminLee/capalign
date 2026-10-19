# ACL 投稿缺口与 TODO（cap-align · paper.md v0.4.4）

**版本：** gaps-v0.4.3-2（对照稿 v0.4.4；实验合同仍按 v0.4.3 冻结；修正 TODO 计数）  
**日期：** 2026-10-18（Asia/Shanghai）  
**权威稿：** [`paper.md`](paper.md)（v0.4.4）  
**实验清单：** [`experiment-checklist-v043.md`](experiment-checklist-v043.md)  
**变更记录：** [`CHANGELOG-v0.4.md`](CHANGELOG-v0.4.md)  
**硬规则：** 不填假数；不改 C1–C3；illustrative / same-model pilot / 旧 e1–e4 **不是**投稿表。

> **一句话：** 故事核（C1–C3 + 受控编辑合同）已齐；**阻断投稿的是空实验表**（EΔ / 人工 IRR / 四臂 / destroy），不是再缺概念。

---

## A) 对 ACL 仍不足（按严重度）

### A1. 阻断投稿（没有这些，Findings/Main 都站不住）

| # | 缺口 | 为什么阻断 | 填法（清单） | 状态 |
|---|---|---|---|---|
| B1 | **Table EΔ 无多工作实测** | C1「覆盖分叉」缺真实残余混合 + paper/repo gap Jaccard；示意槽位 ≠ 结果 | Phase 3（≥2 真实 paper–repo；独立双盘点） | **open** |
| B2 | **Table E1′ 无人 IRR** | 标注可信度；same-model 三裁判只能附录 lower bound（Rating Roulette） | Phase 1 + Phase 4 E1′（≥2 人；κ + 分歧分析） | **open** |
| B3 | **Table E2′ 无四臂+\(π\) 实测** | C2 / Props. 2–5 缺「同批单位、按 λ」的 FI/Miss/\(t_v\)；打不掉「不就是 LLM 改代码」 | Phase 4–5（\(I\) / \(W_{\mathrm{rap}}\) / \(P_{\mathrm{aper}}\) / write-directly / \(I\circ\pi\)） | **open** |
| B4 | **Destroy 批量 still-green 未报** | C3 Testable 合同写了，但无 invalid-test / survivor 率 → 补丁可被说成不可证伪 | Phase 2 夹具 + Phase 6.1（同批单位） | **open** |
| B5 | **语料不足：<2 真实双面工作** | §4.7 Findings 门 = ≥2 独立 paper–repo；迷你夹具 / phonopy 示意不算 | Phase 1 选 Pair-2 + Phase 3 | **open**（Pair-2 待拍板） |

### A2. 削弱贡献（有稿可投但易被打「engineering / incomplete」）

| # | 缺口 | 风险 | 填法 | 状态 |
|---|---|---|---|---|
| W1 | Intro / Related 仍偏厚 | 审稿人抓不到「为什么现有 detect / repro / wrap 盖不住」 | 压 Intro 到 missing-question + C1 铅；§2.5 定位句前置 | **open（polish）** |
| W2 | Faithful 服从未测（LLM 补丁） | 定理假定 Faithful；只有手写补丁时 Prop→实证桥梁弱 | Phase 4 先手写打通合同，再报 LLM green + destroy（§6.3） | **open** |
| W3 | 主图 Figure X 与正文叙事同步 / 投稿包 | 图已有 PDF/SVG；LaTeX 打包与 caption 进 ARR 包未做 | CHANGELOG「Figure X」；ACL LaTeX packaging | **open（非数字）** |
| W4 | 第二 enumerable host / 第二域 | Main 加分；Findings 非硬门 | §4.6 Main bonus；清单 Phase 5 扩容 | **open（可选 Main）** |
| W5 | 脚本与标注材料未公开释放 | Ethics：runs 完成后释放；现无可引用 artifact | 随 v043-exp 跑完再 release | **open** |

### A3. 可选 polish（不挡 Findings 最小包）

| # | 项 | 说明 | 状态 |
|---|---|---|---|
| P1 | **Fast** call-count 表 | 论文标 optional；清单默认投稿不做 | **open / 可整表 TODO** |
| P2 | 扩到 ~8 对 | §4.3 扩容目标；门仍是 ≥2 | **open（扩容）** |
| P3 | 用户研究「更快 / 更可信」 | **Not claimed**；有 destroy + call 前禁止品牌句 | **不做（明确）** |
| P4 | 检测 / 复现 SOTA 数字 | 类别错误；Limitations 已拒 | **不做（明确）** |

---

## B) `paper.md` 内仍打开的 TODO（按实验轴归并）

统计（v0.4.4）：含 `TODO` 的行约 **21**（`rg` 命中）；其中 **实验轴未填格仍全开**（EΔ / E1′ / E2′ / Testable / Fast）。相对 v0.4.3 的 ~17 行，多出的是 Status / Limitations / App B/C 的「仍 TODO」指针句——**不是新填的假数**。**无一格已填实测率。**

### B1. 实验轴（投稿表）

| 符号 | 位置 | 缺什么 | 靠哪条清单填 | 状态 |
|---|---|---|---|---|
| **EΔ** | Abstract 末；§1.5 Not claimed；§3.6 示意后；§4.2 行；§4.5 Table EΔ；§4.6 | 多工作残余混合；两面 missing-id Jaccard；fork yes/no | Phase 3（P3.*） | **open** |
| **E1′** | §1.5；§4.2；§4.5 Table E1′；§4.6；Ethics annotator | ≥2 人 Id / λ / projection IRR；κ + raw + 分歧（partial / Id 边界） | Phase 1 + Phase 4 E1′ | **open** |
| **E2′** | §4.2；§4.5 Table E2′；§4.6 | 同批单位上五臂（含 \(π\)）按 λ 的 FI/Miss/\(t_v\)/green/destroy；contract-expected vs realized | Phase 4–5 | **open** |
| **Testable** | §4.2；§4.5；§4.6 | destroy still-green（survivor / invalid-test）按 λ | Phase 2 + Phase 6.1 | **open** |
| **Fast** | §4.2；§4.5；§4.6；§6.9 | 同 fail-before 套件上到绿的 call 数 vs write-directly | Phase 6.2（可选） | **open / 投稿可留 TODO** |

### B2. 文内明示「非结果」的示意（勿当 TODO 填假数）

| 位置 | 内容 | 纪律 |
|---|---|---|
| §3.4 / §3.6 / §4.5 | phonopy / mini-ref / `qha`–`band` 示意计数 | 永远标 *illustration*；**禁止**抄进 EΔ/E2′ 实测列 |
| §4.2 / Limitations | same-model three-judge pilot | 仅附录 lower bound；**不是** E1′ |
| Abstract / §1.5 / Ethics | `TODO` 字样保留直到真跑 | 有数再删 marker 并升 `experiments-filled` 类版本 |

### B3. §4.6 勾选（论文内）— 全部未勾

- [ ] EΔ ≥1（prefer ≥2）真实独立双盘点 + Jaccard  
- [ ] E1′ ≥2 humans + κ + 分歧  
- [ ] E2′ 四臂 + \(π\)；按 λ 的 FI/Miss/\(t_v\)  
- [ ] Testable destroy-invalid rate  
- [ ] Fast（optional）  
- [ ] Main bonus：第二 host / 第二域  

---

## C) 文档 / 工程侧 TODO

### C1. 实验清单 Phase（48 项；详见 checklist）

| Phase | 目标 | 门控勾选 | 状态 |
|---|---|---|---|
| 0 冻资产 | SNAP / Λ / 规则 / \(H_0\) / 表模板 / 目录 | SNAP.txt | **open** |
| 1 标注/Gold | Pair-1 单飞 → 双人 seed IRR | ≥ Pair-1 + IRR 计划 | **open** |
| 2 Destroy 夹具 | fail-before→green→destroy-red；拒绝=宿主不动；见证隔离 | 烟雾绿 + ISOLATION.md | **open** |
| 3 EΔ | ≥2 真实对表 | 表草稿存在且实测/TODO 分列 | **open** |
| 4 E1′/E2′ | 人 IRR + 五臂表结构 | 表结构落盘（可先全 TODO） | **open** |
| 5 对照叙事 | 打掉「LLM 改代码」；写回 §4.5 纪律 | Findings 门 3 勾 | **open** |
| 6 Testable/Fast | still-green；Fast 可选 | Testable 有数或显式 TODO | **open** |

### C2. Owen 拍板（未决则 Phase 1/3 卡住）

| # | 问题 | 清单默认 | 状态 |
|---|---|---|---|
| A | Pair-2（及更多）选谁 | phonopy=Pair-1；Pair-2 另选有 Methods 的包；oh-my-mlip 暂不适合双面 | **待拍板** |
| B | 第二标注人 | Owen + 同事 | **待拍板** |
| C | 宿主：沙箱 vs 写 MatDiscovery | **默认沙箱**；MatDiscovery 只读 | 提案已写；**待确认** |
| D | E2′ 先手写 Faithful vs 直接 LLM | **先手写再 LLM** | 提案已写；**待确认** |
| E | Findings 先 ≥2 还是冲 ~8 | 先门后扩 | **待确认** |
| F | Fast 是否进投稿 | **默认不做** | **待确认** |
| G | 旧 E1–E4 是否重跑 | **以本清单 / paper §4 为准** | 提案已写 |

### C3. 包装 / 非实验

| 项 | 状态 |
|---|---|
| ACL LaTeX 打包（ARR 格式） | **open** |
| Figure X 进投稿包 + caption 定稿 | 资产在 `docs/figures/typed-introduction/`；**打包 open** |
| Intro 压缩版（可选冲刺） | **open（A2-W1）** |
| Artifact release（schema / guides / scripts） | **open（随 runs）** |

---

## D) 已齐、不再当「不足」

下列项**已写入稿**；继续扩概念不会提高可投稿性。缺口在 **A/B/C**，不在这里。

| 块 | 已齐内容 | 位置 |
|---|---|---|
| **C1** | 覆盖分叉模型；orphan/phantom；单面不可能同时 FI=Miss=0；`qha`/`band` 示意 | §1.3–1.5；§3.4 |
| **C2** | 类型引入 \(I\)；结构化拒绝；\(K_H\)/\(t_v\)；闭类型编辑 API；criterion provenance | §1.5；§3.5 |
| **C3** | Effective / Testable / Fast 定义；fail-before→green→destroy-red | §1.5；§3.7 |
| **算法** | 8 步流水线；冻结宿主/测试；禁止 look-ahead 改标签 | §3.5.1 |
| **Destroy 合同** | 按 λ 的改前/改后/拆掉表（含拒绝行） | §3.7.1 |
| **拒绝示意** | entry-sans-obl. `band`；procedure-conflict L1 vs L2（标 illustrative） | §3.4 |
| **标注协议** | 开行 / Id / κ / 函数压手写 / 污染控制 / 见证隔离 | §4.3 |
| **臂与评分列** | \(I\)/\(W_{\mathrm{rap}}\)/\(P_{\mathrm{aper}}\)/write-directly/\(π\)；expected vs realized | §4.4–4.5 |
| **Findings 门定义** | §4.7 四条（EΔ≥2 + IRR + E2′ + 诚实 Limitations） | §4.7 |
| **附录** | D：Obl/Ent、project、\(t_v\)、覆盖上界；E：introduce/test/must-not | App D/E |
| **诚实边界** | Not claimed / Limitations 12 条 / 不做检测·复现 SOTA | §1.5；§6 |
| **实验清单** | 48 项六阶段 + 拍板表 + 防造假 | `experiment-checklist-v043.md` |

**不该再加的：** 新 λ 类、新贡献子弹、检测/复现 leaderboard、用户信任问卷（无 destroy/call 前）、用示意数填表。

---

## E) 最小可投稿路径（Findings）

与论文 §4.7 / 清单「Findings 门」对齐：

1. Phase 0 冻完 → Phase 2 迷你夹具烟雾绿  
2. ≥2 真实双面工作完成独立盘点 → **填 EΔ**  
3. ≥2 人 IRR → **填 E1′**  
4. 同批 gold 上 \(I\) vs wrap vs paper-only（+\(π\)）→ **填 E2′**（按 λ）  
5. 同批 destroy still-green → **填 Testable**  
6. Fast 可整表 TODO；Limitations 保持诚实  

完成后：只改 §4.5 单元格 + §4.6 勾选 + SNAP 脚注；**禁止**改 C1–C3 条文凑故事。

---

## F) 人话（给 Owen）

- **原理够当 ACL 故事核**；**不够直接送审**——缺的是真表，不是再写一节 Method。  
- **阻断：** EΔ、人工 IRR、四臂+\(π\)、destroy 批量、至少两对真实工作。  
- **已齐可停手：** C1–C3、8 步、destroy 合同表、拒绝语义、附录 D/E、Findings 门文字。  
- **拍板前别空转：** Pair-2、第二标注人、沙箱宿主、先手写 Faithful。  
- **数字纪律：** `paper.md` 内约 21 处含 `TODO`（实验轴全开；多出的是 Status/Limitations 指针句）；谁填示意/旧 pilot 进表谁犯规。

