# 项目进展 — cap-align（能力对齐 skill + 论文实证）

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
| skill 本体（8 步工作流 + 自检门） | `SKILL.md` | 已定；§E + 材料范围 + 宿主自有落点（规则 6）；Layer-1 现为 10 项 |
| 方法论 / 评估 / IR / 对齐规则 / 报告契约 | `references/` | F1/F2/F3 三条 pilot 缺陷已全部落码 |
| 验收 fixtures（mini-ref/host/paper/blog + 邻域 gold） | `tests/fixtures/` | gold 与规则同步；有效跑例 `runs/2026-10-16-e-neighborhood/` |
| 真实跑：oh-my-mlip × MatDiscovery | `research/runs/oh-my-mlip-vs-matdiscovery/` | 暴露 F4–F9 并回写规则。F10（wrap 参考 hub 不是对齐）在该跑之后钉进 skill；该报告的 wrap 建议视为历史，不回写 |
| 研究工具（drift-meter / build-registry，纯 stdlib） | `research/tools/` | v1 已含 host TS 产物面 |
| 论文中文核心稿 + 三张 archify 正稿（图1–3） | `docs/paper-core.md`, `docs/figures/` | 文案已按新身份改写；图面邻居集待重绘 |

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