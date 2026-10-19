# 实验落地清单（cap-align ACL draft · paper.md v0.4.4）

**版本：** checklist-v0.4.3-2  
**日期：** 2026-10-18（Asia/Shanghai）  
**论文：** `docs/acl-draft/paper.md`（v0.4.4；方法合同仍按 v0.4.3）  
**本文件：** `docs/acl-draft/experiment-checklist-v043.md`（Mac）＋ `/workspace/cap-align-figure/experiment-checklist-v043.md`（box）  
**投稿缺口总表：** [`gaps-and-todos-v043.md`](gaps-and-todos-v043.md)（阻断 / 削弱 / 可选；paper 内 TODO 轴；拍板项；已齐清单）  
**硬规则：** 不填假数；不改 C1–C3；数字格一律 `TODO` 直到真跑完；LLM-as-judge 不是 FI / \(t_v\) 唯一神谕。

---

## 投稿缺口（指针）

- **阻断 ACL：** EΔ 多工作表、人工 IRR、四臂+\(π\)、destroy 批量、≥2 真实双面工作 —— 细节见 gaps 文档 §A1。  
- **已齐不再当不足：** C1–C3、8 步流水线、按 λ destroy 合同、附录 D/E —— 见 gaps §D。  
- **本清单职责：** 只排 Phase 0–6 怎么跑；不重写论文主张。

---

## 一页摘要（给聊天转述）

1. **主张已齐，该填真实验**：C1 覆盖分叉 / C2 类型引入含拒绝+\(K_H\) / C3 fail-before→green→destroy；表格仍全 TODO。
2. **六阶段落地**：冻资产 → 人工 gold / IRR → destroy 夹具接线 → EΔ → E1′/E2′ → Testable/Fast。
3. **最小 Findings 包（论文 §4.7）**：≥2 真实 paper–repo 对 + 人工 IRR + 同批单位上四臂+\(π\) 的 FI/Miss/\(t_v\)（按 λ 拆）+ destroy still-green。
4. **已有可挂路径**：`tests/fixtures/mini-*`、`research/slot-model*.json`、`research/runs/e1|e2|e4`、`e2-scripts/`；旧 E1–E4 是早期 gap 叙事，**不能**直接当 v0.4.3 表填数。
5. **需 Owen 拍板**：第二对真实工作选谁；第二标注人；宿主用沙箱仿真还是写 MatDiscovery；E2′ 先手写 Faithful 补丁还是直接 LLM。
6. **禁止**：把 illustrative phonopy/mini 计数、same-model pilot、e2 feasibility 空目录写成论文结果。

---

## 术语速查（与论文一致）

| 符号 | 含义 |
|---|---|
| \(\lambda\) | residual type（分区引擎，不是贡献标题） |
| FI / Miss / \(t_v\) | Effective：假引入 / 漏义务 / 有效性检查是否装上 |
| \(W_{\mathrm{rap}}\) / \(P_{\mathrm{aper}}\) / write-directly / \(\pi\) | 四臂 + 标签置换消融 |
| fail-before → green → destroy-red | C3 验收合同 |
| destroy still-green | Testable：见证无效 / survivor 率（≠ 对齐成功） |
| Fast | 同 fail-before 套件上到绿的 call 数（可选） |
| Obl / Ent | \(s=1\) / \(e=1\) 集合 |
| \(H=(P_H,K_H)\) | 宿主产品集 + 有效性检查集 |

**六类 \(\lambda\)（冻结，禁止中途加类）：**  
`both-aligned` · `obligation-sans-entry` · `entry-sans-obligation` · `validity-gap` · `procedure-conflict` · `incongruent`

---

## Phase 0 — 冻资产（开跑前一次做完）

**目标：** 任何模型/标注员看到结果之前，宿主、标签、见证、语料针都冻结。对应论文 §3.5.1「Freeze first」+ §4.1。

| ID | 事项 | 前置 | 命令 / 路径 | 成功标准 | 填哪张表 | 造假风险 |
|---|---|---|---|---|---|---|
| P0.1 | 冻结论文与仓库快照 | — | `git -C /Users/lwm/code/cap-align rev-parse HEAD` → 写入 `research/runs/v043-exp/SNAP.txt`；论文头写明 v0.4.3 | SNAP 含 commit + 日期（Asia/Shanghai） | 复现脚注 | 禁止事后改论文合同再跑 |
| P0.2 | 导出 \(\Lambda\) 清单（六类，中英对照） | P0.1 | 手抄论文 Table 3.5 / §3.7.1 → `research/runs/v043-exp/lambda-inventory.md` | 恰好 6 类；与 boolean 分区一致 | E2′ 列头 | 禁止新增第 7 类当贡献 |
| P0.3 | 冻结 Id 合并规则 + 开行规则 | P0.2 | 摘抄 §4.3 规则 1–5 → `annotation-rules-freeze.md` | 含：Id 不定不合并；κ 仅 s=e=1；函数压过手写 | E1′ / EΔ | 禁止用 sentence↔function 发明行 |
| P0.4 | 冻结空宿主 \(H_0\)（或声明仿真边界） | P0.1 | **提案 A（默认）：** 用 `tests/fixtures/mini-host/` 作可写沙箱 \(H_0\)；MatDiscovery **只读**（沿用 `research/runs/e2/e2-protocol.md`） | \(P_H,K_H\) JSON 落盘且 hash 固定 | E2′ / Testable | 禁止边跑边改宿主金标 |
| P0.5 | 建标注表模板（空表，无标签答案） | P0.3 | `research/runs/v043-exp/sheets/annotation-sheet.template.csv` 列见下方 | 模板可开新对；无预填 \(\lambda\) | E1′ / EΔ | 禁止把 gold 答案塞进发给标注员的表 |
| P0.6 | 盘点可复用资产（只读引用，不当结果） | — | 见「资产地图」 | 清单写明 *pilot / illustrative / not paper table* | Limitations | 禁止把 e1 judgments 当 human IRR |
| P0.7 | 建运行目录骨架 | P0.1 | `mkdir -p research/runs/v043-exp/{sheets,inventories,harness,eda,e1p,e2p,testable,fast,logs}` | 目录存在 | 全部 | — |

**标注表模板列（提案，Owen 可改）：**

```text
work_id, unit_id, product_one_liner,
paper_step_filled, paper_step_locus, paper_step_quote,
paper_validity_filled, paper_validity_locus, paper_validity_quote,
repo_entry_filled, repo_entry_locus, repo_entry_quote,
repo_validity_filled, repo_validity_locus, repo_validity_quote,
kappa, kappa_locus_or_NA,
lambda_hand, lambda_from_function, lambda_final,
host_has, paper_projection, repo_projection,
annotator_id, notes_disagreement
```

`lambda_from_function` 由布尔分区脚本算；与 `lambda_hand` 冲突时 **函数胜**（§4.3.5），记入 notes。

**资产地图（已有 → 用途）：**

| 路径 | 状态 | 本清单怎么用 |
|---|---|---|
| `tests/fixtures/mini-ref/` + `mini-host/` + `mini-paper.md` | 合成夹具 | Phase 2 夹具接线；**不是** EΔ 多工作率 |
| `research/slot-model.example.json` / `slot-model.phonopy.json` | illustrative 槽位 | Phase 0 λ 自检；EΔ 排版样例；**禁止**抄进 Table EΔ 数字 |
| `research/runs/e1/`（same-model 三裁判） | pilot | 附录 lower bound **仅**；E1′ 正文要 human |
| `research/runs/e2/e2-scripts/`（`run_feasibility.py` 等） | 旧任务臂骨架 | 可参考目录布局；**须重写**成 typed I / destroy API |
| `research/runs/e2/e2-runs/feasibility-*` | 多数空目录 | **不可**当臂结果 |
| `research/runs/e3/` kdense drift | 库内漂移 | Limitations：非 headline |
| `research/runs/e4/` calib | 旧校准 | 可选参考；非 E2′ |
| `research/runs/oh-my-mlip-vs-matdiscovery/` | repo↔host 对齐 | **候选**第二对需补 paper 面；当前 companion_paper 空 |
| `research/experiments.md` | 旧 E1–E4 叙事 | **以 paper §4 为准**；本清单覆盖它 |

- [ ] Phase 0 全部完成并写入 `SNAP.txt`

---

## Phase 1 — 标注 / Gold（人为主）

**目标：** 独立双面盘点 → Id 合并 → 填槽 → \(\lambda\)；至少 2 人 IRR。对应 §4.3、Table E1′、EΔ 输入。

| ID | 事项 | 人前/可单飞 | 前置 | 命令 / 路径 | 成功标准 | 填哪张表 | 造假风险 |
|---|---|---|---|---|---|---|---|
| P1.1 | 选定工作对清单 | 人（Owen） | P0.7 | 写入 `research/runs/v043-exp/corpus.md` | ≥2 真实对（Findings）；合成 mini 另列 *dev only* | EΔ 行 | 禁止把 mini 算进「真实对」计数 |
| P1.2 | **提案默认语料**（待批） | 人批 | P1.1 | 见下方「语料提案」 | Owen 在 corpus.md 批「采用/替换」 | EΔ | 未批之前不写进 paper |
| P1.3 | 单人 pilot：对 Pair-1 做完整独立双盘点 | **可单飞** | P0.5, P1.2 | 纸面先、repo 后（或反过来另开 session）；输出 `inventories/<work>/paper.json` + `repo.json` | 两侧无交叉引用痕迹；每 filled 有行级 locus | EΔ 草稿 | 禁止一边读一边补另一边 |
| P1.4 | Id 合并 → units | 可单飞 | P1.3 | `TBD: implement` `scripts/merge_by_id.py` 或手合并 + 审计 | 不定 Id → 两行不合并；无 Dude 式发明行 | EΔ | 禁止为「好看」强行合并 |
| P1.5 | 算 \(\lambda\)（函数）+ 手标对照 | 可单飞 | P1.4 | `TBD: implement` `scripts/lambda_from_bools.py`（对照 `research/slot-model.md`） | 冲突以函数为准并改 locus | E1′ 准备 | 禁止事后改布尔凑标签 |
| P1.6 | 招募第 2 标注人 + 培训（规则冻结稿） | **必须真人** | P0.3 | 发 `annotation-rules-freeze.md` + 1 个已标 demo（不含答案关键） | 培训记录入 `e1p/training-log.md` | E1′ | 禁止把方法论长文塞进评委上下文 |
| P1.7 | 双人独立标注同一 seed batch | **必须真人** | P1.6 | 每人一份 sheet；勿共享 | 每人完成同一 `unit_id` 集合 | E1′ | 禁止对答案 |
| P1.8 | IRR 计算 + 分歧分析 | 可脚本 | P1.7 | `TBD: implement` `scripts/irr_cohen_fleiss.py`；分歧类：partial/missing、Id 边界、κ=0 默认 | 报告 Cohen/Fleiss \(\kappa\) + raw agreement + 分歧表；数字格 `TODO` 直到跑完 | **Table E1′** | 禁止用 same-model κ 冒充 human |
| P1.9 | 冻结 gold batch（仲裁后） | 人 | P1.8 | `inventories/gold-batch-v1.json` + hash | 仲裁规则书面化；此后 E2′ 只用此 gold | E2′ 输入 | 禁止 E2′ 中途改 gold |
| P1.10 | 扩展到 ~8 对（Findings 扩容，非最小门槛） | 人 | P1.9 | 论文 §4.3.7 | 第二人能独立复现 filled+\(\lambda\) 后再扩 | EΔ 扩 | 未达 IRR 前扩集会污染 |

**语料提案（标 *proposal*，非论文事实）：**

| work_id | paper 面 | repo 面 | 备注 |
|---|---|---|---|
| `phonopy-2015` | arXiv:1506.08498 Methods（或固定 PDF 页） | `/Users/lwm/code/phonopy` @ pin | slot-model.phonopy 已 illustrative；EΔ 须**重做独立盘点** |
| `mini-ref-dev` | `tests/fixtures/mini-ref/papers/…` | `tests/fixtures/mini-ref/` | **仅 harness / 培训**；不进多工作率 |
| `pair-2` **待选** | 须有可引用 Methods | 公开 companion repo | **候选：** 另找有 paper+repo 的材料/科学包；`oh-my-mlip` 当前无 companion paper → **不宜**直接作 EΔ 双面，除非补到可引用论文 |
| （扩容）至 ~8 | … | … | Findings 扩容用 |

**分歧规则（提案，与 §4.3 对齐）：**

1. Id 不定 → 不合并（两 unit）；不计「残差一致」。  
2. κ 不定 → κ=0；不发明 conflict。  
3. 手标 ≠ 函数 → 函数胜，改 locus。  
4. 仲裁第三人仅在 P1.8 后启用；仲裁记录进 gold log。

- [ ] Phase 1：至少 Pair-1 pilot + 双人 seed IRR 计划就绪（真人未到也可先做完 P1.1–P1.5）

---

## Phase 2 — Destroy-harness + 类型编辑 API 接线

**目标：** 实现 §3.7.1 合同：fail-before → 编辑 → green → destroy → 必须再红；拒绝类成功 = \(H\) 不变。见证在补丁写不到的面。

| ID | 事项 | 前置 | 命令 / 路径 | 成功标准 | 填哪张表 | 造假风险 |
|---|---|---|---|---|---|---|
| P2.1 | 定义宿主编辑 API（按 λ） | P0.2, P0.4 | `TBD: implement` `research/runs/v043-exp/harness/typed_edit_api.py`：`bind_entry` / `install_paper_steps` / `install_Kh_check` / `refuse_noop` / `record_unresolved` | 每个 λ 只调表内动作；拒绝路径 \(\Delta P_H=\emptyset\) | E2′ | 禁止 wrap 全部 e=1 却标成 \(I\) |
| P2.2 | 见证套件隔离目录 | P2.1 | `harness/witnesses/`（agent 工作区只读挂载或路径拒绝写） | 引入 agent 无法改 witness 文件（Harbor 式） | Testable | 禁止见证与补丁同目录可写 |
| P2.3 | 按 λ 写 fail-before 测试 | P2.2 | `harness/contracts/<lambda>/*.py` | 在冻结 \(H_0\) 上**必须失败** | E2′ / Testable | 禁止先改宿主再写「fail-before」 |
| P2.4 | 按 λ 写 destroy 突变算子 | P2.3 | 与 §4.3 destroy-harness 一致：unbind / 删 steps / 删 \(K_H\) check；拒绝类无 install mutant | destroy 后规定断言再红 | **Table Testable** | 禁止 destroy 只删无关文件 |
| P2.5 | 端到端烟雾：mini-ref 上手写 Faithful 补丁 | P2.4 | 对 slot-model 中已知行跑通一遍（**不写进论文表**） | 每类至少 1 条：fail-before→green→destroy-red；拒绝类：宿主 hash 不变 | 开发日志 | 烟雾数字 ≠ E2′ |
| P2.6 | 拒绝类合同断言 | P2.5 | entry-sans-obligation：不进 paper test set 且 \(P_H\) 不变；procedure-conflict：未决记录仍在；静默选边 → trial invalid | 断言自动化 | E2′ refusal 列 | 禁止把「没装上」算 Miss |
| P2.7 | 臂实现骨架 | P2.1 | `harness/arms/{I,wrap_repo,paper_only,write_directly,pi}.py` | 行为符合 §4.4 定性合同（代码层，尚未跑批） | E2′ | 禁止四臂共用同一补丁目录却改标签名 |

**每 λ 合同（执行核对表，数字勿填）：**

| \(\lambda\) | 改前 | 改后 | Destroy | 成功 |
|---|---|---|---|---|
| both-aligned | \(p\notin P_H\) | \(p\in P_H\) | unbind → 再红 | 真入口交付 |
| obligation-sans-entry | \(p\notin P_H\) | \(p\in P_H\) 且无伪造 entry id | 删 paper steps → 再红 | 义务实现 |
| validity-gap | \(t_v=0\) | \(t_v=1\) | 删 check → \(t_v=0\) | 产品+检查 |
| entry-sans-obligation | — | **\(P_H\) 不变** | — | 拒绝=成功 |
| procedure-conflict | 未决记录 | **\(P_H\) 不变** | 静默选边→trial invalid | 拒绝=成功 |
| incongruent | — | Ignore | — | 不发明产品 |

- [ ] Phase 2：烟雾绿 + 见证隔离证明（路径/权限记录进 `harness/ISOLATION.md`）

---

## Phase 3 — EΔ（覆盖分叉 / 残差混合）

**目标：** 证明残差非空、可 \(\lambda\) 分型、paper/repo gap-set Jaccard 可报；服务 **C1**。对应 Table EΔ、§4.5、§4.6。

| ID | 事项 | 前置 | 命令 / 路径 | 成功标准 | 填哪张表 | 造假风险 |
|---|---|---|---|---|---|---|
| P3.1 | 对每对工作跑独立双盘点（用 Phase 1 gold 流程） | P1.9 或至少 P1.5 | `inventories/<work>/` | ≥1（更好 ≥2）真实对完成 | EΔ | 禁止只报合成 |
| P3.2 | 投影 gap 集 + Jaccard | P3.1 | `TBD: implement` `scripts/fork_jaccard.py`：paper-face missing-id vs repo-face missing-id | 输出两集合与 Jaccard；**至少一对 Jaccard 近 0** 作 fork 证据（§4.7） | **Table EΔ** | 禁止用 illustrative `qha`/`band` 顶替真实对 |
| P3.3 | 残差混合表（按 λ 计数） | P3.2 | 聚合 `lambda_final` | 列：work id；#units by \(\lambda\)；两 missing 集；Jaccard；fork yes/no | **Table EΔ** | 单元格未跑前保持 `TODO` |
| P3.4 | 引入 vs 拒绝率（描述性） | P3.3 | 统计 introduce 类 vs refuse 类单位占比 | 只作描述；**不**宣称最优检测率 | EΔ 附列 / Discussion | 禁止写成 SciCoQA SOTA |
| P3.5 | 论文占位表替换纪律 | P3.3 | 仅当真实跑完才改 `paper.md` §4.5 Table EΔ | PR 说明「真实跑」+ SNAP hash | paper.md | **禁止**把 slot-model 的 FI=2/Miss=1 写进 EΔ |

**Table EΔ 列（论文已定，数字 TODO）：**  
`work_id | #units by λ | paper-face missing-id set | repo-face missing-id set | Jaccard | fork (yes/no)`

**指标清单（只列名，不填数）：**

- 残差非空：\(|\{u:\lambda \neq \text{both-aligned}\}| > 0\)（或按论文「residual mix」）  
- fork Jaccard（missing-id 跨面）  
- 每 λ 计数  
- （可选）introduce-eligible vs refuse 单位数  

- [ ] Phase 3：≥2 真实对表草稿存在且标 `TODO`/实测分列清楚

---

## Phase 4 — E1′ / E2′（IRR + 四臂合同）

**目标：** E1′ 标注可信；E2′ 同批 gold 上 \(I\) vs \(W_{\mathrm{rap}}\) vs \(P_{\mathrm{aper}}\) vs write-directly（+\(\pi\)），**按 λ** 报 FI/Miss/\(t_v\)/green-rate/destroy-still-green，且 **contract-expected vs realized** 两列。服务 **C2 / Props. 2–5**。

### 4a · E1′

| ID | 事项 | 前置 | 命令 / 路径 | 成功标准 | 填哪张表 | 造假风险 |
|---|---|---|---|---|---|---|
| P4.1 | 锁定 IRR 指标 | P1.8 | Id、\(\lambda\)、projection 分报；Cohen 或 Fleiss + raw agreement | 与 §4.5 Table E1′ 列一致 | **Table E1′** | same-model 仅附录 |
| P4.2 | 写入分歧分析段 | P4.1 | partial/missing、Id 边界、κ=0 | 即使 κ 低也诚实写（论文允许） | E1′ / Limitations | 禁止藏分歧 |
| P4.3 | （附录）归档 e1 same-model pilot | — | `research/runs/e1/` → 引用为 lower bound | 正文不声称 human | Appendix | 禁止正文混用 |

### 4b · E2′

| ID | 事项 | 前置 | 命令 / 路径 | 成功标准 | 填哪张表 | 造假风险 |
|---|---|---|---|---|---|---|
| P4.4 | 固定评测单位 = gold-batch | P1.9, P2.7 | 同一 `unit_id` 集合喂所有臂 | 臂间单位集合恒等 | E2′ | 禁止各臂不同子集 |
| P4.5 | **提案：** 先 Faithful 手写补丁跑通合同计数 | Owen 批 | 对 gold 子集手写 \(I\) 补丁，验证 Props. 2–3 **实现层**与定义一致 | contract-expected 列可填「定性」；realized 仍实测 | E2′ | 手写成功 ≠ LLM 服从率 |
| P4.6 | 跑臂 \(I\) | P4.4–P4.5, P2.* | `TBD: implement` `harness/run_arm.py --arm I` | 产出 per-λ FI/Miss/\(t_v\)/green/destroy-still-green | **Table E2′** | 未跑单元格 `TODO` |
| P4.7 | 跑臂 \(W_{\mathrm{rap}}\)（含 MCP-attach 叙事等价：全 e=1、不写 \(K_H\)） | P4.6 | `--arm wrap_repo` | FI/Miss 应对齐 omission 计数（Faithful 下）；realized 另报 | E2′ | 禁止把 MCP 安全扫描率当 FI |
| P4.8 | 跑臂 \(P_{\mathrm{aper}}\) | P4.6 | `--arm paper_only` | \(t_v=0\) 预期（无 check）；both-aligned destroy(unbind) 不适用/失败合同 | E2′ | — |
| P4.9 | 跑臂 write-directly | P4.6 | `--arm write_directly`（无 λ 提示） | 无 Prop 保证；记录 FI/Miss/\(t_v\) | E2′ / Fast 对照 | 禁止只报 win-rate |
| P4.10 | 消融 \(\pi\)（交换两 omission 类再 \(I\)） | P4.6 | `--arm pi` | 当存在 ≥1 omission 单位时，pass set 应与 \(I\) 分离（Prop. 5） | E2′ | 无 omission 单位则消融无信息量——须在 EΔ 保证 |
| P4.11 | 填 contract-expected vs realized | P4.6–P4.10 | 表模板见下 | 每臂每 λ 两列齐全 | **Table E2′** | 禁止只报聚合 |
| P4.12 | （可选后续）LLM 补丁服从率 | P4.11 | 同 fail-before 套件；报 green-rate 与 destroy-still-green | 与「定义 FI=0」分列；Faithful 破 → 不引用 Prop. 2 当实测 | E2′ / Limitations | 禁止把服从失败改成改定义 |

**Table E2′ 行×列模板（数字 TODO）：**

```text
arm × λ → contract-expected(FI, Miss, t_v) | realized(FI, Miss, t_v, green-rate, destroy-still-green)
arms: I | W_rap | P_aper | write-directly | I∘π
λ: 六类（拒绝类：成功=H unchanged，不计产品在场）
```

**四臂最小集（论文已命名，非新发明）：**  
支持 C1–C3 不需外加检测 SOTA 臂；**不要**加 SciCoQA/SA-Bench 分数竞赛列。

- [ ] Phase 4：E1′ 人表就绪或已跑；E2′ 表结构落盘（可先全 TODO）

---

## Phase 5 — 四臂 / 基线对照（汇总与叙事）

**说明：** 论文 §4.4 已点名臂；本阶段是「跑完后的对照叙事 + 负例」，不是新理论。

| ID | 事项 | 前置 | 命令 / 路径 | 成功标准 | 填哪张表 | 造假风险 |
|---|---|---|---|---|---|---|
| P5.1 | 汇总 Expected vs Realized 总表 | P4.11 | `e2p/summary.md` | 指出哪类 λ 驱动 FI/Miss | E2′ / §5 | 禁止夸大未测臂 |
| P5.2 | 负例：false-alarm / grain-invented 行 | P1.4 | 收录「曾被错误合并、后拆回」的单位 | ≥1 负例说明 Id 门控 | Discussion / EΔ | 禁止编造负例 |
| P5.3 | MCP-wrap 叙事对齐 | P4.7 | Discussion §5.2.1：良性 wrap 仍实现 \(W_{\mathrm{rap}}\) FI/Miss | 文案不引用未跑 UIR | §5 | 禁止填 MCP 代理安全数字 |
| P5.4 | Findings 够用性核对 | P3.*, P4.*, P5.1 | 对照 §4.7 三条 | 清单打勾见下「Findings 门」 | §4.7 | 未齐宣称 Findings |

**Findings 门（§4.7，抄录为执行勾选）：**

- [ ] EΔ ≥2 真实对 + 独立双盘点 + 非空残差 + 至少一对 Jaccard 近 0  
- [ ] E1′ human IRR + 分歧分析  
- [ ] E2′ 同批：\(I\) vs \(W_{\mathrm{rap}}\) vs \(P_{\mathrm{aper}}\)（+\(\pi\)）+ 按 λ 的 FI/Miss/\(t_v\) + destroy still-green  

**Main 额外（非本清单阻塞）：** 第二可枚举宿主/域（λ 冻结）、更大 EΔ、LLM Faithful 服从率。

---

## Phase 6 — Testable / Fast（仅论文已定义部分）

| ID | 事项 | 前置 | 命令 / 路径 | 成功标准 | 填哪张表 | 造假风险 |
|---|---|---|---|---|---|---|
| P6.1 | Testable：按 λ 汇总 destroy still-green | P4.6+ | `testable/survivor-by-lambda.csv` | 报告 invalid-test / survivor rate；与 FI/Miss **分列** | **Table Testable** | 禁止把 still-green 算「对齐成功」 |
| P6.2 | Fast（可选）：同 fail-before 套件上 \(I\) vs write-directly 的 call 数 | P4.9 | `fast/call-counts.csv`；仅 matched tasks | 有数才准说 faster；否则 paper 保持 TODO、禁用品牌口号 | **Table Fast** | 禁止不同套件比速度 |
| P6.3 | 品牌口号门禁 | P6.1–P6.2 | 检查 Abstract/Intro 无「faster/more trustworthy」除非表已填 | 未测则不出现口号 | paper 全文 | 见 Limitations (9) |

- [ ] Phase 6：Testable 列有实测或显式 TODO；Fast 未测则整表 TODO

---

## 建议执行顺序（可勾）

```text
Week A  P0 全做完 → P2 夹具烟雾（mini）→ P1.1–P1.5 Pair-1 单飞
Week B  P1.6–P1.9 双人 IRR → P3 第二对 EΔ
Week C  P4.5 手写 Faithful → P4.6–P4.11 五臂表 → P6.1 Testable
Week D  （可选）P4.12 LLM 服从；P6.2 Fast；扩到 ~8 对
```

（周次为 **提案**，非论文承诺。）

---

## 需 Owen 拍板的含糊点

| # | 问题 | 论文现状 | 清单默认提案 |
|---|---|---|---|
| A | 第二（及更多）真实 paper–repo 对选谁？ | ≥2，未点名 | phonopy 为 Pair-1；Pair-2 **另选有 Methods 的包**；oh-my-mlip 暂不适合双面 EΔ |
| B | 第二标注人是谁？ | ≥2 humans | Owen + 一位同事；培训用冻结规则 |
| C | 宿主 \(H\)：写 MatDiscovery 还是沙箱？ | enumerable H | **默认沙箱 mini-host / e2 仿真边界**；MatDiscovery 只读 |
| D | E2′ 先手写 Faithful 还是直接 LLM？ | 报 green + destroy；定理假定 Faithful | **先手写打通合同，再 LLM** |
| E | Findings 最小对数量：2 还是冲 8？ | 门=2；扩容~8 | 先门后扩 |
| F | Fast 是否进投稿？ | 可选 | 默认 **投稿不做 Fast**，表留 TODO |
| G | 旧 `research/experiments.md` E1–E4 是否还跑？ | 与 v0.4.x §4 轴不同 | **以本清单 / paper §4 为准**；旧 runs 仅资产 |

---

## 明确不做（防范围膨胀）

- 不刷 SciCoQA / Dude 检测 SOTA  
- 不刷 SA-Bench / PaperBench / ReproAgent 复现 SOTA  
- 不把六类 λ 写成「新贡献标题」  
- 不填 MCP Unauthorized Invocation Rate 等基础设施数字  
- 不把 illustrative 槽位计数写入 EΔ/E2′  
- 不改 paper.md C1–C3 条文（本清单不碰论文正文）

---

## 完成后如何写回 paper.md（纪律）

1. 仅替换 §4.5 中标 `TODO` 的单元格与 §4.6 勾选。  
2. 每次填数附 `research/runs/v043-exp/SNAP.txt` hash + 日期（Asia/Shanghai）。  
3. contract-expected（定性）与 realized（实测）分列；Faithful 破则 Limitations 点名，不改 Prop 陈述。  
4. changelog：v0.4.4 已用于 gaps 指针；**填数后**再记 `experiments-filled` / v0.4.5+——禁止用示意数催版本。

---

## 条目统计

| Phase | 条目数（P*.*） |
|---|---|
| 0 冻资产 | 7 |
| 1 标注/Gold | 10 |
| 2 Destroy-harness | 7 |
| 3 EΔ | 5 |
| 4 E1′/E2′ | 12（3+9） |
| 5 对照叙事 | 4 |
| 6 Testable/Fast | 3 |
| **合计** | **48** |

另：Findings 门 3 勾；Owen 拍板 7 项。

---

## 人话（5–8 行）

主张和验收合同已经写死了，现在缺的是真跑。先冻宿主/标签/见证，再用迷你夹具把「改前必败 → 改后绿 → 拆掉再红」和「拒绝成功=宿主不动」接到可执行脚本。标注上先单人把第一对 paper–repo 独立盘点跑通，再找第二人算 IRR；EΔ 至少两对真实工作，并盯住跨面 Jaccard 是否接近 0。同一批 gold 上跑四臂加 π，按 λ 报 FI/Miss/\(t_v\)，合同预期和实测分两列。destroy 还绿单独报成见证无效率；Fast 可先不做。整份清单 48 项，数字全留 TODO——谁也不许拿 illustrative 或旧 pilot 顶表。
