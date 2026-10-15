# 项目进展 — capalign（能力对齐 skill + 论文实证）

> 更新：2026-10-15。本文记录到当日为止的项目状态、已完成实证、开放边界与下一阶段计划。
> 仓库当前 8 个 commit，工作区干净（HEAD `466997f`）。

## 1. 项目是什么

- **一个可插拔、零捆绑**的能力对齐 skill：宿主材料 agent 的能力面对齐到参考物（repo / paper / blog），产出能力清单、差距分类（equivalent/partial/missing/unknown）、逐缺口落点建议（新 skill / 新 tool / 扩既有 / runner 契约 / 跳过）。
- **一篇论文**《From Scientific Software Assets to Agent Capabilities》：把"对齐"从工具叙事升级为**三个实证研究 + 形式化定义（断言 A–E）+ 治理范式**（承诺漂移测量、coverage@reference、自审校准）。实证在前，工具是实现载体。
- 方法论三层纪律（`references/methodology.md` §0）：通用层零宿主词汇；phonopy↔MatDiscovery 只是第一个验证实例，不绑定任何具体 repo。

## 2. 已交付的产品层

| 资产 | 位置 | 状态 |
|---|---|---|
| skill 本体（8 步工作流 + 自检门） | `SKILL.md` | 已定，装机即用 |
| 方法论 / 评估 / IR / 对齐规则 / 报告契约 | `references/` | F1/F2/F3 三条 pilot 缺陷已全部落码 |
| 验收 fixtures（mini-ref/host/paper/blog + gold） | `tests/fixtures/` | gold 与规则同步（F2 残留已修） |
| 研究工具（drift-meter / build-registry，纯 stdlib） | `research/tools/` | v1 已含 host TS 产物面 |
| 论文中文核心稿 + 三张 archify 正稿（图1–3） | `docs/paper-core.md`, `docs/figures/` | 已交付 |

## 3. 第一轮实证结果（1→2→4→3 全部落地，commit 466997f）

| 实验 | 问的问题 | 结果 | 断言 |
|---|---|---|---|
| **E1 IRR**（P1 phonopy↔MD 13 能力、P2 mini-paper↔mini-host 9 能力，各 3 judge） | 分类判定可复现吗 | P1 Fleiss κ(class)=**0.853**（pass bar 0.6）；P2 κ=**1.000**；source 原始一致 92.6% | 方法可靠性 |
| **E2 三臂 harness** | 按报告补能力 > 随机补 > 不补？ | 协议 + 32 任务套件（29 real 派生自 phonopy docs + 3 mini）+ 5 脚本 + 可行性运行已跑通（判定管线正/负对照、三臂机制、重跑字节级一致）；真实层 gold 标 pending | B（coverage→任务成功） |
| **E4 自参照校准** | agent 自审能力面可信吗 | 两遍运行协议就绪；mini 实测 bias=0.0（fixture 太干净不可证伪）、cal(high)=0.75、类一致 6/6；诚实标注退化 | D（自审偏差可校准） |
| **E3 跨库漂移** | 承诺漂移跨库普遍吗 | K-Dense 177 skills：drift **30.3%** vs MatDiscovery **11.2%**；fabricated **0** vs **2.2%**；漂移集中 body 层（断言 C 初检成立） | C（漂移可排序/可预测） |

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

- **E1 κ 是同模型三 judge 下限信号**：无人类 judge、无第二模型 → 真 IRR 未达成。这是 E1 唯一结构性缺口。
- **E2 真实层 gold pending**：需要 phonopy 可执行安装才能生成数值 gold（k8: pending 已标，未假装）。
- **E3 只有 2 个库**：断言 C 的"分布"与 AUROC 预测未达成；K-Dense 验证面是 crafted registry（f-string 盲区已量化 31 处）。
- **E4 迷你不可证伪**：bias≥0 需真实库（有 AUDIT 或自报面）才有信号。
- **断言 E（stale recall）未跑**：需要纵向 git 历史。
- MatDiscovery 侧有大量未提交工作（benchmark/fieldmat ≈70 文件 + scripts/bench）与 capalign 无关，本项目对其只读（纪律已保持）。

## 6. 下一阶段计划

| 优先级 | 事项 | 前置/依赖 | 目标 |
|---|---|---|---|
| 1 | **E1 扩展** P3 复跑轴 + P4/P5 中性域真实对 + P6 博客 | **人类或第二模型 judge**（结构性缺口） | 真 IRR + 跨域泛化证据 |
| 2 | **E2 完整三臂执行** | phonopy 可执行安装生成真实 gold | 断言 B 唯一实证 |
| 3 | **E3 补分布**：第 3 宿主 + 宿主无关 claim 语法 + AUROC | — | 断言 C 升级为成立 |
| 4 | **E4 真实库跑点**：MD 37 skills / K-Dense 自参照 vs 外部 | — | 断言 D 实证（n≥5/标签格） |
| 5 | **E5 纵向 stale recall**：git 历史 ≥5 snapshot | — | 断言 E + 治理范式招牌 demo |
| 6 | **论文闭环**：experiments.md 完成状态 + paper-core 实证表 | 以上各项 | 可提交的实证章节 |

## 7. 复现命令

```bash
# 漂移测量（能力面验证）
python3 research/tools/build-registry.py <repo-root> --out reg.json
python3 research/tools/drift-meter.py <skills_dir> --registry reg.json --table

# 验收 fixtures（指令式，零捆绑）
# 按 tests/README.md 运行：inventory → align → 比对 gold/*.json
```