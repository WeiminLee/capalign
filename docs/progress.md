# 项目进展 — cap-align（能力对齐 skill + 论文实证）

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
| skill 本体（8 步工作流 + 自检门） | `SKILL.md` | 已定；§E + 材料范围 + 引入卡片（规则 7 拒绝）+ 宿主自有落点（规则 6）+ 盲盘纪律与 κ 步骤（2026-10-19 三）+ 验证账本（2026-10-19 四）+ 槽位三态与 `host_need_note`（2026-10-22）；Layer-1 现为 **18 项** |
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
