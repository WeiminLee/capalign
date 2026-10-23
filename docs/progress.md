# 项目进展 — cap-align（能力对齐 skill + 论文实证）

> 更新：2026-10-23。组合准入与融合已落码（见文末
> 「2026-10-23 — 组合准入与融合落码」）：`SKILL.md` 第 7 步、
> `references/portfolio-admission.md`、schema `portfolio` 块、Layer-1 19–21、
> `research/tools/portfolio-model.py`、`mini-library` / `mini-retire` fixtures。
> 工作流 8→9 步，Layer-1 18→21 项。E5/E6 未跑，真实宿主上的组合效果未测量。
>
> 更新：2026-10-22。槽位改**三态**（`1 | 0 | "unknown"` + `provenance` + `why_empty` /
> `why_unknown`）：读不到的论文不再被当成"论文没写"，`s`/`e` 为 unknown 的产品落成
> `insufficient-evidence`（**不建卡**，差距行 `unknown`），`v` 未知则 install 但只判
> `bind`、`validity: unknown (not assessed)`。配套落码：`host_need_note` 举证（含
> verification 的 regime / 缺的检查 / owner）、`local_check`（form + named/demonstrated）、
> `extend:` 双路由用例、`surfaces.arms` / `independent_check` / `reference_license`、
> 报告 9 节与 build records（append-only，必须记 host commit）、卡片 `rule` 改为数组、
> 新增 `references/report-schema.json` 与 `references/quick-decisions.md`。
> Layer-1 由 14 项增至 **18 项**：两条并行支线合流 ——「桥，不是护栏」支线加第 16 项，
> 本支线加第 17/18 项（unknown 处理、host_need 举证）；另设「独立复核」一节，不计入编号。
> 此前两支线各自记为「14 → 16」与「14 → 18」，均系从 14 分叉后单侧计数，此处按合流后的
> 实际表序（1–15 旧、16 桥、17 unknown、18 host_need）更正。
> 新 fixture：`tests/fixtures/mini-ref-unreachable/` 与对应 gold。金标卡槽已迁移三态。
> **论文轨已同步（2026-10-22）**：`research/tools/slot-model.py` 与
> `research/slot-model.*.json` 已迁到三态（`state` / `provenance` / `why_empty` /
> `why_unknown`），新增标签 `证据不足` 与 `有效性未评`，`unres` 单列未决；
> `research/introduction-operator.md` 的 \(\lambda\)、算子表、命题 2/3 与 Adm 表，
> `research/slot-model.md` 的槽位、标签函数与投影，`docs/typed-introduction.md` 的
> §5/§6 均已同步。旧记录的 `filled` 仍可读（折成 state 1/0）。
>
> 更新：2026-10-19（五）。宿主同步前置：对齐前先对宿主 `git pull --ff-only`，
> 拉不动（未提交改动 / 分叉 / 冲突）就停跑并把 `git status` 交给用户裁决
> （stash / commit / discard / proceed-dirty），skill 永不自动解决；
> 同步结果（commit 哈希或暂停原因）进报告 `surfaces.host_sync`，冻结的宿主清单
> 取自同步后的状态。落点：`SKILL.md` step 2、heuristics §D.0a、report-contract
> surfaces/第 1 节、Layer-1 第 1 项。
>
> 更新：2026-10-19（四）。验证诚实性落码：卡片新增 `verification` 块
> （三拍 `fail_before` / `pass_after` / `destroy` 各自 `pass|fail|not-run` + 证据），
> 状态三态 `e2e-verified | contract-only | failed`；报告契约新增必含节
> **Verification ledger**（逐卡状态 + 计数），contract-only 的产物禁止被声称已交付；
> 结语改为明示"contract-only 卡片的测试从未执行"。Layer-1 加第 14 项（验证诚实性）。
> 金标 6 卡全部标 `contract-only` 并记 log。
>
> 更新：2026-10-19（三）。skill 硬化 P0–P2 落码：盲盘纪律进 `SKILL.md` step 1 与
> heuristics §B（两侧槽位冻结后才按产物合并）；κ 判断步骤进 step 6（仅 s=e=1 时问，
> 判不了为 0）；卡片槽位升级为 `{filled, span, quote}` 对象；卡片新增
> `prescribed` / `forbidden_primitives`（Adm(λ) 审计锚点，`introduction-card.md` 新小节）；
> 报告契约加 `fork` 摘要块（paper_gaps / repo_gaps / intersection / jaccard，由两张投影表算出）；
> Layer-1 加第 13 项（槽位证据 + λ 重算 + fork 一致）。金标 `mini-introduction-cards.json`
> 已同步新 schema 并记 log。
>
> 更新：2026-10-19（二）。讨论沉淀三处：λ 的「四次提问」简化呈现进
> [`typed-introduction.md`](typed-introduction.md) §6.1；动作细化（Act = bind/impl/check/record/nop、
> 许用补丁集 Adm(λ)、Faithful 变为可静态审计）进 `../research/introduction-operator.md` §4.1；
> 审稿质疑答辩进 [`acl-paper-design.md`](acl-paper-design.md) §1.4。新工具
> `../research/tools/slot-model.py`：λ 标签校验、宿主投影、覆盖分叉（Jaccard）、
> 四算子模拟、Adm(λ) 补丁审计。mini-ref 与 phonopy 两份记录全部跑通，输出与
> typed-introduction §11.1/§11.2 的手算理论值逐项一致（mini-ref：fork Jaccard=0；
> phonopy：I 的 FI=0/Miss=0、W_rap FI=2/Miss=1、VG 单元 t_v=1）。
>
> 更新：2026-10-19。技能落点改为引入卡片：`references/introduction-card.md`，
> 金标 `tests/fixtures/gold/mini-introduction-cards.json`。五态投影金标的 `class`
> 未改。论文稿未动。Layer-1 现为 12 项。
>
> 更新：2026-10-18。ACL 文稿设计补充见 [`acl-paper-design.md`](acl-paper-design.md)
> （贡献 vs SciCoQA、Related Work 表、最小实验协议、Limitations、Figure X）。
>
> 更新：2026-10-17。设计结论见 [`typed-introduction.md`](typed-introduction.md)
> （按差异类型引入宿主，并带改前失败、改后通过的测试）。下文仍是 2026-10-16 的状态记录。
>
> 更新：2026-10-16。本文记录到当日为止的项目状态、已完成实证、开放边界与下一阶段计划。
> 论文身份已修订（双编码规格 + 宿主相对判定 + 参考条件化覆盖）；实证数字仍以
> 2026-10-15 的 E1–E4 首轮为准。当日补上 repo 输入的配套论文/有界邻域回收（§E）。
> 同日把对齐范围钉死为材料能力（最多到材料 agent 方法），落点必须宿主自有、禁止
> wrap 参考 agent（F10；`alignment-rules.md` §Scope / §Placement 6）。

## 1. 项目是什么

- **一个可插拔、零捆绑**的能力对齐 skill：把一篇材料论文（及其配套仓库）的**材料能力**对齐到用户自己的材料 agent，产出能力清单、差距分类、**宿主自有**的落点建议。给 repo 时回收配套论文与有界邻域。repo 与 paper 走同一套判定；blog 产品支持、论文主文不钉。不盘 plugin/MCP/装环境；不把参考 agent 嵌进宿主。
- **一篇论文**：外来科学工作 \(W=(\mathrm{paper},\mathrm{repo})\) 是双编码能力规格；\(\mathrm{Gap}(H,W)\) 是静态、证据门控的宿主相对判定；覆盖随选取哪一份编码而分叉。skill 是仪器。详见 [`paper-core.md`](paper-core.md)。
- 方法论三层纪律（`references/methodology.md` §0）：通用层零宿主词汇；phonopy↔MatDiscovery 只是第一个验证实例，不绑定任何具体 repo。

## 2. 已交付的产品层

| 资产 | 位置 | 状态 |
|---|---|---|
| skill 本体（9 步工作流 + 自检门） | `SKILL.md` | 已定；§E + 材料范围 + 引入卡片（规则 7 拒绝）+ 宿主自有落点（规则 6）+ 盲盘纪律与 κ 步骤（2026-10-19 三）+ 验证账本（2026-10-19 四）+ 槽位三态与 `host_need_note`（2026-10-22）+ 组合准入（2026-10-23）；Layer-1 现为 **21 项** |
| 方法论 / 评估 / IR / 对齐规则 / 报告契约 | `references/` | F1/F2/F3 三条 pilot 缺陷已全部落码 |
| 验收 fixtures（mini-ref/host/paper/blog + 邻域 gold） | `tests/fixtures/` | gold 与规则同步；有效跑例 `runs/2026-10-16-e-neighborhood/` |
| 真实跑：oh-my-mlip × MatDiscovery | `research/runs/oh-my-mlip-vs-matdiscovery/` | 暴露 F4–F9 并回写规则。F10（wrap 参考 hub 不是对齐）在该跑之后钉进 skill；该报告的 wrap 建议视为历史，不回写 |
| 研究工具（drift-meter / build-registry / slot-model，纯 stdlib） | `research/tools/` | v1 已含 host TS 产物面；slot-model 把 λ/投影/四算子/Adm 审计落成可执行 |
| 论文中文核心稿 + 三张 archify 正稿（图1–3） | `docs/paper-core.md`, `docs/figures/` | 文案已按新身份改写；图面邻居集待重绘 |
| ACL 写作包 + typed Method 主图 | `docs/acl-paper-design.md`, `docs/figures/typed-introduction/` | 2026-10-18：贡献/对照表/实验协议/Limitation/Figure X；实验数字未发明 |
| ACL 英文全稿草稿 | `docs/acl-draft/paper.md` | 2026-10-18：typed introduction 主张 + 洞察段；实验表 TODO；与 brief/abstract v0.3 对齐 |

## 3. 第一轮实证结果（1→2→4→3 全部落地，commit bea0c8b）

| 实验 | 问的问题 | 结果 | 断言 |
|---|---|---|---|
| **E1 IRR**（P1 phonopy↔MD 13 能力、P2 mini-paper↔mini-host 9 能力，各 3 judge） | 分类判定可复现吗 | P1 Fleiss κ(class)=**0.853**（pass bar 0.6）；P2 κ=**1.000**；source 原始一致 92.6% | 方法可靠性 |
| **E2 三臂 harness** | 按报告补能力 > 随机补 > 不补？ | 协议 + 32 任务套件（29 real 派生自 phonopy docs + 3 mini）+ 5 脚本 + 可行性运行已跑通；真实层 gold 标 pending。下一步要拆成「按 paper 规格补 vs 按 repo 规格补」才服务 C3 | B / C3 |
| **E4 自参照校准** | 自报面相对外来 \(W\) 可信吗 | 两遍运行协议就绪；mini 实测 bias=0.0（fixture 太干净不可证伪）、cal(high)=0.75、类一致 6/6 | D |
| **E3 跨库漂移** | 包内声称 vs 已验证 | K-Dense 177 skills：drift **30.3%** vs MatDiscovery **11.2%**。按新身份，这是分解项，不是头条；需求侧 `coverage(H,W)` 分布未立 | （降级） |
| **EΔ 跨形态残差** | 同一工作的 paper 面 ⋈ repo 面？ | **未跑**。phonopy methods vs phonopy 仓库是现成一对，C1/C3 的命门 | C1 / C3 |

**附带前置**：F3 粒度边界落码（`capability-ir.md`）、v1 registry 并入 host TS/tools 产物面（drift 15→13）、E1 pilot 遗留的 gold 与 F2 规则打架修复。

## 4. E1 判卷暴露的真正价值（pilot→IRR 的关键收获）

6 个隔离 judge 复跑同一份试卷，抓到了单作者 gold 的盲点：

1. **fc-assembly 证据驱动修订 missing→partial**：3 个 judge 独立在宿主侧找到真实 FC 组装代码（bte_controller core.py:490-504、qha muxi:529-539），gold 原判"缺失"是漏扫。修订带 log 登记。
2. **qha source 证据不对称**：gold 判 host-self-audit 有 `SKILL-DESIGN.md:495` 直接文档支撑（宿主自认 α 欠交付），judge 的 reference-contrast 是搜索未命中——正证据胜出，记录不撤改。
3. **band-structure partial/equiv 邻接**、**electronic-thermal 单片分歧**：记录为 confusion report 素材，不强行统一。
4. **统计要点**：source κ 塌缩是边际失衡悖论（27 标签中 26 个同值，Pe≈Pbar），论文须同时报 raw agreement 与 κ。
5. **污染披露**：2 个 judge 报告方法论 §3 整文件读取进入上下文（自行弃用），已记录为 contamination risk，方法必须强制行界读取。
6. **P2 9/9 完全一致**：fixture 在落码规则下确定性满格，验证规则本身无歧义。

## 5. 开放边界（论文必须诚实面对的）

- **EΔ 未跑**：同一工作的 paper 面 ⋈ repo 面还是假说。C1/C3 的命门。
- **E1 κ 是同模型三 judge 下限信号**：无人类 judge、无第二模型 → 真 IRR 未达成。
- **E2 真实层 gold pending**：需要 phonopy 可执行安装；按 paper vs repo 规格拆臂尚未做。
- **E3**：已测的是 2 库包内 drift（分解项）；需求侧 `coverage(H,W)` 分布未立。K-Dense 验证面是 crafted registry。
- **E4 迷你不可证伪**：bias≥0 需真实库（有 AUDIT 或自报面）才有信号。
- **断言 E（stale recall）未跑**：需要纵向 git 历史。
- MatDiscovery 侧有大量未提交工作（benchmark/fieldmat ≈70 文件 + scripts/bench）与 cap-align 无关，本项目对其只读（纪律已保持）。

## 6. 下一阶段计划

| 优先级 | 事项 | 前置/依赖 | 目标 |
|---|---|---|---|
| 1 | **EΔ** 同一工作 paper 面 ⋈ repo 面（phonopy methods vs 仓库） | 把 phonopy 论文提成 \(W_{\mathrm{paper}}\) | C1/C3 从假说变成测量 |
| 2 | **E2 双规格装配** | phonopy 可执行安装生成真实 gold | 按 paper 补 vs 按 repo 补，增益形状（C3） |
| 3 | **E1 扩展** 人类或第二模型 judge + 更多 paper 臂 | 结构性缺口 | C2 真 IRR |
| 4 | **E4 真实库跑点**：MD 37 skills 自报面 vs 外来 \(W\) | — | 断言 D |
| 5 | **E3 需求侧 coverage(H,W)** 分布（≥3 宿主）；包内 drift 留附录 | — | C3 库级形状 |
| 6 | **图 2 重绘**：定位图补 SciCoQA / SkillConsist / Skill Coverage 等邻居 | 正文表已改 | 图文一致 |

## 7. 复现命令

```bash
# 漂移测量（能力面验证）
python3 research/tools/build-registry.py <repo-root> --out reg.json
python3 research/tools/drift-meter.py <skills_dir> --registry reg.json --table

# 验收 fixtures（指令式，零捆绑）
# 按 tests/README.md 运行：inventory → align → 比对 gold/*.json
```

## 2026-10-22 — 桥，不是护栏

Layer-1 新增第 **16** 项「bridge, not guardrail」：每张 install 卡必须说清**没有这个落点时 agent 会做错什么**；内容以禁令为主的落点是错的。（此项与同日另一支线的第 17/18 项在合流后同表共存，编号见文件头说明。）

理由：把 FiPy 的能力面写成 `mat-phase-field-kinetics` 时发现，我第一版把 skill 写成了护栏（「不许声称材料性质」「不是 catalog」「未验证的不要用」）。但 skill 的存在理由是**桥**——装 agent 缺的**领域判断**（识别问题 / 选模型 / 尺度纪律 / 实测陷阱 / 怎么读结果），不是方程、不是 API、更不是禁令。仓库此前**没有一处正面定义 skill 该装什么**，本轮补上（`alignment-rules.md` §What a skill is for）。

连带：`introduction-card.md` 加 §The contract must exercise the bridge（`fail_before` 是「agent 判错」而不是「入口不存在」；`pass_after` 的 prompt 不得点名 skill 与入口）；`methodology.md` 的 adaptation layer 加一条「宿主 agent 供不了什么」。

## 2026-10-23 — 组合准入与生命周期：研究沉淀（先于落码）

**动机。** 能力单元一直新增；宿主在完成时固定。行级 \(\lambda\) 决定「这一行改不改」，但宿主是一个有描述、有路由、互相竞争的**能力组合**。新增一条行级正确的卡，仍可能让宿主选错。

**研究结论（全部为他人测量，不是我们的结果）。**

- 伤害主要来自**选择**，不是上下文：Skill Shadowing（2605.24050）202-skill 库通过率最多降 21%，其中最多 68% 归因于 shadowing，context overhead 与零不可分。
- 选择准确率随库大小**非线性相变**，由语义混淆驱动：Single-Agent Skills（2601.04748）给出 capacity threshold + interference 的 scaling law；分层路由可恢复。
- 工具侧同构：RAG-MCP（2505.03275）<30 候选 >90% → 11,100 候选 13.6%；Tool-Space Interference（Microsoft 2026）1,470 个 MCP server、775 个重名、最大 256 tools、部分模型最多 −85%。
- 生命周期不能按日程：Library Drift（2605.19576）**过早退休 −1.9pp**；治理配方 0.258→0.584。SkillOps（2605.13716）已有 merge/repair/retire/add_validator，但触发是库内健康。
- 生成侧最近邻：Repo-To-Skill（2609.02749）1,000 repos → 5,353 verified skills，construction record 保留证据/检查/缺口；验证是「能跑」。我们多的是宿主相对义务、作废条件、拒绝与组合准入。
- 保留的评估形状可借 MCCL（2610.29357）的四门：preservation → access → utilization → effect。

**设计增量（见 [`../research/portfolio-lifecycle.md`](../research/portfolio-lifecycle.md)）。**

1. 宿主扩为 \(H=(P_H,K_H,\Sigma_H,\rho_H,\beta_H)\)：条目、选择策略、预算。
2. 准入门是**集合谓词**：行条件 + 保留探针 + 组合冲突 \(\kappa_H\) + 预算 + 无 live obligation 失去最后交付者。
3. **非组合命题**：在干扰项超加的声明模型下，逐条安全不封闭于并集。两条各自安全的卡可以联合遮蔽一个保留条目。
4. **生命周期即可达性 GC**：`bind/author/extend/add_validator/merge/demote/upgrade/downgrade/retire/quarantine/refuse`；retire 只对无 live obligation 的条目；merge 必须覆盖双方 live obligations 且降低干扰。这解释 −1.9pp。
5. **指标**：retention、shadowing risk（代理，不叫测量）、interference、context tax、portfolio coverage、orphan、churn。
6. **实验**：E5 组合准入（四臂）；E6 生命周期 replay；E7 机制复现（可选）。E5 是 C4 的证据，E6 是 C5 的证据。

**文稿落点。**

- 新研究笔记 `research/portfolio-lifecycle.md`（引用、设计、实验、改动清单）。
- 中文设计稿 `docs/portfolio-and-lifecycle.md`（对象、准入门、可达性、指标、实验、落码清单）。
- `research/related-work.md` 增 L2b（shadowing / scaling law / drift / SkillsVote / MUSE / misevolution / MCCL / Repo-To-Skill / Paper2Agent / tool-selection）。
- `docs/acl-paper-design.md` 增 §1.5（C4/C5 provisional + claim scope）、§2 六行邻居、§3 E5/E6、§4 限制 (8)。
- `README.md` 加「设计增量，未落码」提示。
- **`SKILL.md` / `references/` / `tests/` 未改**；落码清单见研究笔记 §6（P1–P3）。工作流将从 8 步变 9 步，Layer-1 从 18 项变 21 项。

**下一步优先级。**

| 优先级 | 事项 | 依赖 |
|---|---|---|
| 1 | EΔ（不变，仍是 C1/C3 命门） | phonopy methods → \(W_p\) |
| 2 | `references/portfolio-admission.md`（`docs/portfolio-and-lifecycle.md` 已建） | 本轮笔记审阅 |
| 3 | 落码 step 7 + schema + 3 项自检 | 设计定稿 |
| 4 | `mini-library` / `mini-retire` fixture + gold | 落码 |
| 5 | `research/tools/portfolio-model.py`（纯 stdlib，可达性校验） | fixture |
| 6 | E5；E6 视时间 | 宿主库 + harness |

## 2026-10-23 — 组合准入与融合落码

把上一节的设计落成契约、schema、工具与 fixture。行级 \(\lambda\)、\(\kappa\)、
六态差距和报告结语不变；不写经验数字。

**文件。**

- `SKILL.md`：新增第 7 步「Portfolio admission」；报告与自检拆成第 8/9 步；
  Layer-1 改为 21 项；References 增 `references/portfolio-admission.md`。
- `references/portfolio-admission.md`：作用域、宿主组合 \(H\)、条目签名
  \(\sigma\)、九种融合关系、决策树、关系→动作表、merge 语义、14 个动作、
  探针与集合测试、可达性、指标、禁止项。
- `references/report-schema.json`：顶层 `portfolio`（host_entries / probes /
  set_test / lifecycle / metrics）与卡片级 `portfolio`（relation /
  relation_evidence / action / target_entry / retention_probes / conflict /
  merge / rollback）。
- `references/report-contract.md`、`references/evaluation.md`、
  `references/quick-decisions.md`：Portfolio 节、检查 19–21、八项决策。
- `research/tools/portfolio-model.py` + `research/tools/test_portfolio_model.py`：
  纯 stdlib 的声明一致性检查器；不执行宿主、不跑探针。
- `tests/fixtures/mini-library/`、`tests/fixtures/mini-retire/`：融合关系、
  联合遮蔽、merge/retire/upgrade 的合成陷阱与 gold。
- `docs/portfolio-and-lifecycle.md` §5.1、`research/portfolio-lifecycle.md`
  §2.5.1：融合设计定稿；`merge` 判据改为「同产物、同做法、同有效域」的真重复。

**行为变化。** 工作流 8→9 步；Layer-1 18→21 项（19 组合覆盖、20 融合一致、
21 生命周期安全）。有 `install` 卡时必须过组合准入；只有 `refuse` 卡时仍写空
`portfolio` 块。

**验证。** `python3 -m unittest research/tools/test_portfolio_model.py -v`：
21 项全过。`mini-library/portfolio-input.json` 以联合遮蔽
（`0.3 - 0.2 - 0.2 = -0.1`）退出 1；`portfolio-input-gated.json`（demote `qha`）
退出 0；`mini-retire/portfolio-input.json` 以 `lattice-kappa` 失去最后交付者
退出 1，而它前面的 upgrade 与 `qha-old` retire 通过。

**复审修正。** 独立复审后补齐：卡片级 `upgrade` 用条目实值检查产物/检查/
有效域超集与目标保留探针；生命周期 `merge` 要求真重复、双方 test contract、
重映射保留探针并取有效域交集；`deliver`/`validity` 探针带 `card_id`，一条
探针不能再服务多个候选；`demote` 的 id 必须是真实候选；指标按
「冻结宿主条目数 / 无 live obligation 且无保留探针的宿主条目 / 含 demoted
的可交付条目」重新定义；决策树改为与谓词表同一读取顺序。图 JSON 已改九步，
PNG/HTML/drawio 仍为旧八步示意，已在 README 标注待重绘。

**未跑。** E5（组合准入四臂）、E6（生命周期 replay）、真实宿主上的 retention /
shadowing 均未跑；fixtures 是合成陷阱，不是测量。`portfolio-model.py` 只检查
声明之间的一致性，不能替代宿主上的探针执行。C4/C5 因此是
implemented, unmeasured。

## 2026-10-23 — 融合策略 v2：证据阶梯、硬覆盖与提交门

依据 [`skill-merge-retire-survey.md`](skill-merge-retire-survey.md) §1.1–1.3，
把 merge 从“字段并集”升级为**可审计的删除**。所有数字仍是他人的测量；
cap-align 不新增经验结论，E5/E6 仍未跑。

**设计增量。**

- **证据阶梯（SkillZip Pro）。** 每条删除恰好一条 witness：W1 字面包含 ≻
  W2 覆盖 witness ≻ W3 受限蕴含。挂不上就否决；同一条目两条 witness 也算错。
  源条目本身（`entry:<card_id>`）是必须交代的删除。W3 不允许删除
  obligation、output field 或带 prohibition/exemption/output 标记的单元。
- **锁定残差。** 解析/证不了的单元逐字保留（`unit`、`reason`、`verbatim`），
  不得删除；失败模式是压缩不足，不是静默丢失。
- **硬 surface 覆盖。** trigger / workflow edge / tool requirement /
  obligation / output field 的双方并集必须等于
  `coverage ∪ removed_units ∪ locked_residual`；coverage 不能声明两边都没有的
  单元。
- **提交门（SkillGLoW）。** 双方保留探针都进 `recall_probes`，逐条声明；
  任一 `passed: false` 否决。
- **交互门（SkillSmith）。** `interaction.beta < -0.15` 必须附扩展回归检查与
  证据；`beta: 0` 表示未估计，不是已证明独立。
- **never-inflate。** 合并后 surface token 不得高于合并前；否则退回 no-op /
  split / demote。
- **证据等级诚实。** `evidence_level ∈ {constructive, model, statistical}`；
  `statistical` 必须带 `causal_evidence = {design: randomized, n_trials > 0}`。
- **关系图边型（SkillOps）。** 九关系折叠为
  dependency / compatibility / redundancy / alternative；只有 redundancy
  （duplicate）可 merge。
- **不引入。** SkillGLoW 的整轮提交是执行语义，cap-align 只记 rollback；
  SkillSmith 的合并没有回滚，我们把 rollback 设为准入前置条件。

**落码。**

- `references/portfolio-admission.md` §5–6：边型映射、merge 结构条件、
  §6.2 证据阶梯、§6.3 硬覆盖、§6.4 提交门、§6.5 交互、§6.6 never-inflate、
  §6.7 rollback。
- `references/report-schema.json`：`portfolioSurface`、`portfolioMerge`；
  entry 与 card-level `merge` 复用同一 `$ref`。
- `references/report-contract.md`、`references/evaluation.md`（检查 20）、
  `references/quick-decisions.md`（决策 6）：同步 merge block 与失败条件。
- `research/tools/portfolio-model.py`：新增 `check_merge_evidence`，由 `run`
  聚合；校验 witness 一一对应、W3 禁用面、locked residual、surface 覆盖、
  recall 门、交互门、证据等级、never-inflate。
- `research/tools/test_portfolio_model.py`：新增 12 项测试（33 项全过）。
- `tests/fixtures/mini-library/`：`eos` 与 `eos-dup` 增 surface；`eos-dup`
  增完整 merge block；gold 增 `merge_evidence_asserted` 与 trap；两个 arm
  同步。
- `docs/portfolio-and-lifecycle.md` §5.1、`research/portfolio-lifecycle.md`
  §2.5.1：设计论证与综述引用。

**验证。** 33/33 单测通过；add-all 仍只以联合遮蔽
（`0.3 - 0.2 - 0.2 = -0.1`）退出 1；gated 退出 0；mini-retire 仍以三条
生命周期违规退出 1。merge block 缺失或畸形现在是 violation，不再回退到
相似度。

**边界。** 结构检查只证明没有**已知的**静默丢失，不证明模型读合并文本后的
行为不变；后者要在宿主上跑探针。E5/E6 未跑，C4/C5 仍是
implemented, unmeasured。
