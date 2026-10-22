# 槽位模型 — 落在 mini-ref 上的一份实例

本文把「单元、槽、标签、宿主投影」写成可以逐格核对的记录。
实例只用本仓库已有文件，不另造语料。

| 角色 | 文件 |
|---|---|
| 论文 | `tests/fixtures/mini-ref/papers/qha-mini-ref-2015.md` |
| 仓库 | `tests/fixtures/mini-ref/`（`src/mini_ref/cli.py`、`docs/`、`pyproject.toml`） |
| 宿主 | `tests/fixtures/mini-host/`（`skills/`、`tools/tool-registry.json`、`AUDIT.md`） |

填好的记录在 `slot-model.example.json`。skill 验收用的 gold 在 `tests/fixtures/gold/`，本模型不替换它们；两者共用同一套槽位（三态）与同一张标签表。

## 1. 三条记录

一篇工作的一行是一个 **Unit**。一篇论文先出一批，仓库另出一批，再按产物并成同一行。

```text
Unit
  id            稳定编号，来自产物，不来自文件名
  product       人可以单独要到的结果，一句话
  paper.step     {state, provenance, span, quote}       有序做法
  paper.validity {state, provenance, span, quote}       论文里何时结果作废
  repo.entry     {state, provenance, span, quote}       源码或正式命令里的可调用物
  repo.validity  {state, provenance, span, quote}       仓库文档里何时结果作废
  kappa          0 | 1，只在 s=e=1 时允许为 1
  label          由下面的函数算出，不手写
```

槽位是**三态**，与 skill 的 `references/report-schema.json` 同一套：

| `state` | 含义 | 还要给 |
|---|---|---|
| `1` | 该来源写明了，并抄到原文 | `span` + 非空 `quote` |
| `0` | 该来源**查过**，里面没有 | `why_empty`（`absent` / `no-paper-arm` / `no-repo-arm`，可加 `: 说明`） |
| `"unknown"` | 该来源**读不到** | `why_unknown`（`unreachable` / `not-consulted` / `unparsable`，可加 `: 说明`）；`quote` 必须为空 |

`0` 与 `"unknown"` 不是一回事：`0` 是「查过，没有」，`"unknown"` 是「没法查」。
把读不到的来源记成 `0`，等于把"没看到"当成"不存在"的证据。`provenance` 记这一格
来自哪一臂（`s`/`v_p` 用 `paper`，`e`/`v_r` 用 `repo`；该臂不存在时用 `none`）。

宿主对每一行另记一张 **HostFill**，不改 Unit。

```text
HostFill
  unit_id
  host_has      宿主是否已经交出同一个 product
  nearest       最近的宿主技能或工具；没有则为空
  why_not       host_has 为 false 时，为什么 nearest 不算
  paper_projection    gap | covered | absent | host-already | validity-gap
  repo_projection     同上
```

`span` 写 `路径:起行-止行`。`quote` 抄原文，不改写。查过而没有，记 `state: 0` 并写
`why_empty`；读不到，记 `state: "unknown"` 并写 `why_unknown`。两者不要混。

## 2. 什么算填上

按这个顺序裁，裁完就停。

1. **产物。** 人可以单独要一个结果，才开一行。软件包名不开行。有效性条件不开行，它是某一行的槽。某个产物顺带提到的输入，不开新行。
2. **step。** 一段有序做法：先做什么、再做什么，或明确写出用哪一步得到该产物。一个名词、一句「用某某得到」，不算 step。
3. **entry。** 源码里存在的函数，或 `pyproject.toml` 的脚本入口确实调用到的子命令。文档点了一个模块、源码里没有该文件，`entry.state = 0`（查过，没有）。
4. **validity。** 一句写明在什么情况下该结果作废。只写「需要某模块」不算。
5. **并行。** 两侧 `product` 指同一个结果，才是同一个 `id`。并不上就保持单侧，另一侧三个槽都是 `state: 0`。
6. **宿主。** 只问宿主交不交同一个 `product`。名字相近、产物不同，`host_has = false`，把最近的对象写进 `nearest`，理由写进 `why_not`。

**读不到的那一臂。** 论文没有本地副本、搜索也取不到时，该臂未填的格记
`state: "unknown"` 与 `why_unknown`，不记 `0`。这一行的标签是 `证据不足`，不建卡。

## 3. 标签函数

标签由槽算出来。不允许根据物理量名字改标签。

```text
label(unit):
  step  = unit.paper.step.state      # 1 | 0 | "unknown"
  entry = unit.repo.entry.state
  val_p = unit.paper.validity.state
  val_r = unit.repo.validity.state
  if step == "unknown" or entry == "unknown":
      return 证据不足                  # 先短路：读不到，无从比较
  if not step and not entry:
      return 不成行
  if step and not entry:
      return 义务缺入口
  if entry and not step:
      return 入口缺义务
  if val_p == "unknown" or val_r == "unknown":
      return 有效性未评                # 入口与义务都在，作废条件没评
  if val_p != val_r:
      return 缺有效性
  return 两侧齐
```

**顺序不能换。** `unknown` 必须最先短路：若先比 `step and not entry`，`step=1,
entry="unknown"` 会落进 `两侧齐`，把"读不到的入口"当成"有入口"。这与 §6 里
`证据不足` 的判定是同一条纪律——读不到不是没有。

`证据不足`：`s` 或 `e` 读不到。**不建卡**，差距行记 `unknown`，理由进未决表。
它既不算误引入，也不算漏义务（见 §8）。

`有效性未评`：入口与义务都在，但某一侧的作废条件没评出来。可引入，但**不写作废检查**，
补丁只有 `bind`；`validity` 记 `unknown (not assessed)`。

`缺有效性` 只在步骤和入口都在、作废条件恰好写在一侧时出现。两侧都写了，或两侧都没写，这一槽没有残差，标签是 `两侧齐`。

`不成行` 的行从结果表删除：论文和仓库都没有给出可用的槽。

投影也由函数算出。

```text
project(label, host_has):
  gap = "gap" if not host_has else "host-already"
  if label in (两侧齐, 有效性未评):
      return (covered_or_gap, covered_or_gap)
      # host_has → covered；否则 → gap。两列相同。
  if label == 义务缺入口:
      return (gap, "absent")
  if label == 入口缺义务:
      return ("absent", gap)
  if label == 缺有效性:
      return ("validity-gap" if not host_has else "host-already",
              "validity-gap" if not host_has else "host-already")
  if label == 证据不足:
      return ("unknown", "unknown")   # 差距行记 unknown，不建卡
```

`absent` 的意思是：这一列的规格里没有这个单元，所以这张缺口表里不会出现它。`host-already` 的意思是：规格之间有残差，但宿主已经交出该产物，残差不成为宿主的洞。`unknown` 的意思是：这一列读不到，既不能算作缺口，也不能算作覆盖。

## 4. 这一对实际填出来的表

论文 Methods（`qha-mini-ref-2015.md` 第 5–7 行）只给出一个产物：由体积网格上的 Helmholtz 自由能得到热膨胀。第 9–10 行是这个产物的作废条件。第 14 行的包名删掉。

仓库在不看论文的情况下读 `cli.py`、`docs/band.md`、`pyproject.toml`。五个函数或子命令各是一个产物。`docs/qha.md` 点了 `qha` 模块，源码没有 `qha.py`，命令行用法是 `band|dos|thermal`，没有 `qha`。

| id | product | step 原文 | entry 原文 | 标签 |
|---|---|---|---|---|
| `qha` | 体积网格上极小化 F(V,T)，得到热膨胀 | 论文 5–7 行，有 | 无。`docs/qha.md` 3–4 行点了模块，源码没有 | 义务缺入口 |
| `force-constants` | 二阶力常数张量 | 无。论文只把力常数当作取得谐声子的手段 | `cli.py` 11–13 行 `force_constants` | 入口缺义务 |
| `dynamical-matrix` | 动力学矩阵 D(q) 及其对角化 | 无 | `cli.py` 16–18 行 | 入口缺义务 |
| `phonon-dos` | Gaussian 展宽的声子态密度 | 无 | `cli.py` 21–23 行，用法含 `dos` | 入口缺义务 |
| `harmonic-thermal` | 由频率得到 F / S / 热容 | 无。论文的 F(V,T) 是准谐自由能，不是这个函数的产物 | `cli.py` 26–28 行，用法含 `thermal` | 入口缺义务 |
| `band-structure` | 高对称路径上的声子色散 `band.yaml` | 无 | `docs/band.md` 3–5 行，用法含 `band` | 入口缺义务 |

删掉的行：

| 候选 | 删掉的原因 |
|---|---|
| `mini-ref-package` | 第 14 行是软件包名，没有产物 |
| `thermal-expansion` | 热膨胀是 `qha` 的产物，不是第二套做法 |
| `harmonic-validity` | 第 9–10 行是 `qha` 的 validity 槽 |

宿主清单是冻结的：`eos` 交 V0 与 B0，`heat-flow` 交晶格热导率 kappa，`parse-structure` 读结构，`fit-eos` 拟合 E(V)。`AUDIT.md` 写明没有热容、声子态密度、色散、力常数路径。

| id | 标签 | nearest | host_has | 论文投影 | 仓库投影 |
|---|---|---|---|---|---|
| `qha` | 义务缺入口 | `eos` | false。`eos` 拟合的是 E(V)，不极小化 F(V,T)，不交热膨胀 | gap | absent |
| `force-constants` | 入口缺义务 | — | false。AUDIT 写明无力常数路径 | absent | gap |
| `dynamical-matrix` | 入口缺义务 | — | false | absent | gap |
| `phonon-dos` | 入口缺义务 | — | false。AUDIT 写明无声子态密度 | absent | gap |
| `harmonic-thermal` | 入口缺义务 | `heat-flow` | false。`heat-flow` 交 kappa，不交 F/S/热容 | absent | gap |
| `band-structure` | 入口缺义务 | — | false。AUDIT 写明无色散 | absent | gap |

同一宿主的两张缺口表：

- 只认论文：`qha`
- 只认仓库：`force-constants`、`dynamical-matrix`、`phonon-dos`、`harmonic-thermal`、`band-structure`

两张表没有共同的 id。这就是这一对上的覆盖分叉。`eos` 和 `heat-flow` 留在 `nearest`，不把标签改成覆盖。

## 5. 第四类标签在这套文件上的反事实

真实文件里没有「step 和 entry 都在」的行，所以没有 `两侧齐`，也没有 `缺有效性`。下面两行不进结果表，只用来固定函数的另外两支。改动写明在行内。

| 反事实 | 改动 | 函数结果 |
|---|---|---|
| `qha` 有入口，作废条件仍只在论文 | 增加 `qha.py` 并接入 `phon-vib`；论文第 9–10 行保留；仓库文档仍不写虚频作废 | step 与 entry 都在，validity 只在论文 → `缺有效性`。宿主没有热膨胀 → 两列都是 validity-gap |
| `qha` 有入口，两侧都不写作废条件 | 同上，并删去论文第 9–10 行 | step 与 entry 都在，两侧 validity 都空 → `两侧齐`。宿主没有热膨胀 → 两列都是 gap |

## 6. 真实一对：phonopy 论文 × phonopy 文档

玩具对里没有 step 与 entry 同时为真的行。下面这对用公开文本把四类都填上。论文是 Togo 与 Tanaka，*Scripta Materialia* 108 (2015) 1–5，arXiv:1506.08498，正文用 ar5iv HTML。仓库入口用 Phonopy v.4.8.2 的命令页与 QHA 页，不把 phono3py 算进这个仓库。宿主投影不填：这次没有一份冻结的宿主清单。

| id | 标签 | 论文槽 | 仓库槽 |
|---|---|---|---|
| `harmonic-thermal` | 两侧齐 | §2 式 (9)–(11)：由频率算 \(C_V\)、\(F\)、\(S\)。作废条件两侧都没单写 | `-t` / `TPROP = .TRUE.` |
| `phonon-dos` | 两侧齐 | §2 式 (6)：\(g(\omega)=\frac{1}{N}\sum_{\mathbf{q}j}\delta(\omega-\omega_{\mathbf{q}j})\) | `--dos` |
| `qha` | 缺有效性 | §4 式 (17)：\(G(T,p)=\min_V[F(T,V)+pV]\)。作废：熔点附近高阶项明显时 QHA 不再合适 | `phonopy-qha`，至少 5 个体积点。该句是拟合前提，不算作废条件；文档没写熔点附近失效 |
| `force-constants` | 缺有效性 | §2 式 (2)：力常数由力对位移的导数得到。作废：只在小位移、定体积下二阶项才是谐近似 | `-d` 生成位移，`-f` 收集力。命令页没写「位移一大，二阶力常数就失效」 |
| `band-structure` | 入口缺义务 | 只有 Fig. 1 的结果，没有沿路径取样的做法 | `--band` |
| `group-velocity` | 入口缺义务 | 全文没有这个产物 | `--gv` |
| `lattice-kappa` | 义务缺入口 | §6：把非谐项变成声子–声子相互作用，再解线性化玻尔兹曼方程得到晶格热导率 | 命令页没有热导率或 LBTE 入口 |

记录与原文在 `slot-model.phonopy.json`。`lattice-kappa` 这一行就是「残差会改变覆盖」的论文侧：只读仓库命令，这行不出现；只读论文，它是一个没有入口的义务。

## 8. 读不到的那一臂：未决一行

第 4、6 两对的每一格都查到了，所以三态与二值在这些行上给出同一张表。三态要有用，
得用一行的实例固定住。

`tests/fixtures/mini-ref-unreachable/` 是同一形状，但配套论文只在 `CITATION.cff` 里
被声称（DOI `10.9999/mini-unreachable.2026`），本地没有副本，冻结的搜索也返回空。
仓库侧的入口照填 `state: 1`；论文侧的两格记 `state: "unknown"` 与
`why_unknown: unreachable: ...`，**不记 0**。

| | 二值会记成 | 三态记成 |
|---|---|---|
| 论文 `s` | `0`（"论文没写"） | `"unknown"`（"没读到"） |
| 标签 | `入口缺义务` → 拒绝 | `证据不足` → **不建卡** |
| 差距行 | `missing` | `unknown` |

差别不是措辞。二值那一列会读出一个自信的结论：「论文没有这个义务，所以拒绝它」。
而当时根本没有论文可读。三态把这一行移到未决，理由进 `Unresolved`。

对应的 golden 是 `tests/fixtures/gold/mini-unreachable-vs-mini-host.json`，
可执行检查在 skill 的 `references/evaluation.md` 第 17 项（unknown 处理）。

## 9. 下一对怎么填

复制 `slot-model.example.json` 的 `units` 数组。对新的一对，只改 `spans`、`quotes`，
以及每格的 `why_empty` / `why_unknown`，然后重新跑第 3 节的两个函数。手写的 `label`
若和函数不一致，以函数为准，并改 quote。8 对都按这份记录填完、第二个人能标出相同的
`state` 和 `label` 之后，再扩大语料。

两个函数的可执行形式是 `tools/slot-model.py`：`python3 tools/slot-model.py <slot.json>`
校验槽位良构（三态 / `why_empty` / `why_unknown` / `provenance` / `quote`）、标签、投影、
分叉并模拟四个算子，`unres` 一列单列未决；`--audit patch.json` 审计补丁是否属于
Adm(λ)（`introduction-operator.md` §4.1）。旧记录里的 `filled` 仍可读，折成 `state` 1/0。
