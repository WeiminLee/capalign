# P1 phonopy → MatDiscovery — judge-gamma 判卷

- run_id: `e1-p1-phonopy-vs-matdiscovery-judge-gamma-2026-10-15`
- judge: `judge-gamma`
- reference: `/Users/lwm/code/phonopy`（13 条 reference_inventory）
- host: `MatDiscovery plugins/matdiscovery`（`/Users/lwm/code/MatDiscovery`，37 skills / 13 local tools / 3 remote submit per `docs/CAPABILITY-SURFACE.md`）
- 日期: 2026-10-15
- 隔离纪律：仅读了 `judge-inputs/p1-phonopy-vs-matdiscovery.json` + 5 份 reference 判定文档；**未读**任何 `draft-gold-*`、`tests/fixtures/gold|runs`、`research/runs/e4`、其它 judge 输出。方法论 §3 在整文件读取时不可避免进入上下文，但本判卷的每条分类只由对宿主面的独立扫描证据驱动，未参考其实例记录。

## 分类总表（13 条）

| ref_id | class | source_kind | confidence | note |
|---|---|---|---|---|
| fc-assembly | equivalent | reference-contrast | medium | mat-phonon 路由跑 finite-displacement FC（mattersim PhononWorkflow，remote_mattersim_runner.py:2702-2711），下游 phonopy 对象 API 全链在；repo venv 实装 phonopy 4.8.1 + spglib 2.7.0；qha muxi 直接 `from phonopy import PhonopyQHA`。mattersim 内部源码本地不可读 → medium。 |
| phonon-dos | equivalent | reference-contrast | high | 契约产出 `phonon/total_dos.dat`（dos 请求时）+ `phonon/projected_dos.csv`（projected_dos 请求时），remote_mattersim_runner.py:494-511；envelope 自检强制 total_dos.dat（test_stdout_result_envelope.py）；宿主自审确认 projected DOS 由 runner 产出。 |
| band-structure | partial | reference-contrast | medium | 宿主只交付 `phonon/band.yaml`（色散数据，workflow 内部默认路径），无任何用户可设 band-path 参数、无 bandplot 类渲染；reference 语义含用户指定路径的 BAND + phonopy-bandplot → 严格子集。 |
| group-velocity | equivalent | reference-contrast | high | `phonon/group_velocity.csv` 逐 q/带 v_x/y/z/norm（THz·Å），phonon.run_mesh(with_group_velocities=True)，remote_mattersim_runner.py:2636-2686。 |
| thermal-properties-harmonic | equivalent | reference-contrast | high | `phonon/thermal_properties.csv/.yaml` F/S/Cv vs T + ZPE（run_thermal_properties + cutoff），remote_mattersim_runner.py:2544-2608；stability-only 请求自动补 zpe 保证产出。 |
| mode-gruneisen | partial | reference-contrast | high | 宿主**确实**算逐模 γ(q,band)=−Δlnω/ΔlnV（write_mode_gruneisen，simple_mattersim_qha_muxi.py:583-678），但仅在 QHA 显式请求路径、q-mesh、仅 2 个相邻体积；reference phonopy-gruneisen 是独立 CLI（mesh+band 双路径）→ QHA-gated 子集，严格子集，不是 equivalent。 |
| qha-thermodynamics | partial | reference-contrast | medium | PhonopyQHA 逐压力 Cp/Gibbs/S/H/veq；α(T) 由本地工具 mat_thermal_expansion 对 volume_temperature.csv 求**内部温度点**（端点无 α）；宿主全库无 anisotropic QHA → reference 的 aniso-thermal-expansion 无对应 → 严格子集。注：宿主自审 §1.4（2026-09-24 报 α 全缺）已被 2026-10-15 的 mat_thermal_expansion 部分闭合。 |
| nac-lo-to | missing | reference-contrast | high | 全宿主（代码/skills/docs/2026-10-09 BTE spec）零命中 born 有效电荷 / nac / lo-to；mat-elasticity 的 "Born" 是机械 Born 稳定判据（刚度张量特征值全正），相邻概念不构成覆盖。reference 证据 high。 |
| electronic-thermal | missing | reference-contrast | high | 全宿主零命中 electronic thermal / Fermi / tetrahedron；reference phonopy/electron + doc 是独立交付类，宿主无对应。 |
| irreps-symmetry | missing | reference-contrast | high | 无 irrep / character table / 模对称性能力；最近邻是 mat_analyze_structure 的空间群标签（structure.py:86-103），为结构标签而非模不可约表示，不构成覆盖。 |
| mlp-sscha | missing | reference-contrast | medium | 全宿主零命中 sscha；MatterSim ML-FF 仅用于 singlepoint/MD/BTE 力批次——输入契约不同（FF 力评估 vs MLP 插值声子采样/重整化），phono3py BTE 是微扰 3-phonon 而非 SSCHA → 相邻而不同，missing。 |
| dynamic-structure-factor | missing | reference-contrast | medium | 宿主只有静态 S(q)（mat_compute_structure_factor 吃 RDF rows）；无动态结构因子 S(q,ω)/spectrum；宿主文档自诫勿从通用 MD 诊断推结构因子、并披露静态 S(q) 边界 → 静态不包含动态，missing。 |
| site-mixture-vca | unknown | reference-contrast | low | reference 证据 low（[Experimental] CLI 开关）；宿主零命中 VCA/无序；low 证据绝不驱动 missing（capability-ir #3 / placement rule 5）→ unknown。 |

**计数**：equivalent 4 · partial 3 · missing 5 · unknown 1（合计 13）

## 陷阱应对（traps_asserted 逐条）

1. **依赖指纹≠能力** — 确认：repo `.venv/lib/python3.12/site-packages` 实装 phonopy-4.8.1 / phono3py-4.8.2 / spglib-2.7.0 / ase-3.29.0，且 bte-controller pyproject 声明 phonopy/phono3py 依赖。此指纹**从未**单独驱动任何 equivalent/missing；全部 equivalent 均由可执行代码路径 + 产物契约 + 自审佐证驱动（remote_mattersim_runner.py phonon 段、envelope 自检、SKILLS-AUDIT §6）。指纹只用于解释 phonopy 栈可执行，不作为能力证据。
2. **Born 稳定≠Born 有效电荷** — 宿主唯一 "Born" 命中在 mat-elasticity（SKILL.md:29：Born check = 刚度张量特征值全正；workflow_elastic_wrapper.md:50），是机械 Born 稳定判据，与 NAC/LO-TO（Z\* → 长程库仑→LO-TO 劈裂）无关；全宿主零 nac 命中 → nac-lo-to = missing 维持。
3. **mode-gruneisen 实例杀不可过度应用** — 逐行读了 write_mode_gruneisen（simple_mattersim_qha_muxi.py:583-678）：γ(q,band) 同式有限差分、真实逐模，但**仅**在 QHA 显式请求 gruneisen 时、q-mesh、2 相邻体积；skill 自声明 gruneisen.csv "only when Gruneisen data were explicitly requested"（mat-qha SKILL.md:33），派生属性 refs 亦限 "reported only when the run's output already provides it"。→ partial（严格子集），不是 equivalent，也不是 missing。
4. **qha α 内点推导→严格子集** — mat_thermal_expansion 工具实体确认（tools/mat-local-compute/server.py:202，docstring：interior temperature，endpoints carry no alpha）+ 宿主动手修了 α（2026-10-15 批次），但 α 仅内点、无端点、无各向异性 α 张量 → qha-thermodynamics = partial（isotropic-only），非 equivalent。
5. **sscha/MLP 路由** — MatterSim FF 单点/MD/力批次是"给定结构→FF 力评估"契约；SSCHA 是"ML 指力 + 声子采样/重整化"契约，不同输入契约且宿主零 sscha 实现 → missing，不做 partial。
6. **静态 S(q) 不包含动态 S(q,ω)** — 宿主 mat_compute_structure_factor 仅静态（且宿主文档自认其质量边界）；reference dynamic-structure-factor 是 1-phonon 动态结构因子（spectrum/ 模块）→ 相邻而不同 → missing。
7. **site-mixture VCA** — reference 侧仅有 [Experimental] CLI 文本证据（low）；宿主零命中 → class=unknown、confidence=low，绝不 missing。
8. **irreps** — 宿主空间群标签（mat_analyze_structure）是结构晶群信息，不是声子模式不可约表示/特征表 → 相邻 → missing；near-miss 已记入 evidence_note。

## 最难判的 2-3 条（与原因）

1. **band-structure（partial vs equivalent）** — 宿主真实产出色散数据 band.yaml（"实例杀"倾向 equivalent），但无路径选择参数、无 bandplot。判据不得不落在"reference 语义边界是否含渲染与路径控制"上——granularity 判断，非事实判断。
2. **mode-gruneisen（partial vs equivalent）** — 宿主逐模 γ 的公式与 reference 完全同式、逐 q/band 导出；若只看"算得出 γ"会判 equivalent。读实现后确认 γ 只存在于 QHA 显式请求子路径（无独立 CLI、无 band 路径、仅 2 个体积点）——"存在于宿主"≠"覆盖 reference 语义"，严格子集成立。
3. **fc-assembly（equivalent，medium）** — mattersim 的 PhononWorkflow 内部源码不在本地（远程 runner 依赖），无法直接读证 FC 组装与对称性约化；只能靠 phonopy 对象下游 API 链、.venv 实装栈与产物契约推断。归类 equivalent 但诚实降为 medium。

## 未咨询的来源（methodology §4.3 要求披露）

- 未读宿主失败统计/telemetry（方法规定不读）；未读其它 judge 或 gold 判卷；未咨询宿主维护者。