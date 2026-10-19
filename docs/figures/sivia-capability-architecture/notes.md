# cap-align 核心能力架构图 · 出图记录

两条路线都走过。**交付物是 archify 正稿**（`docs/figures/cap-align-capability-architecture.*`）；
sivia 的栅格路线留在 `sivia-capability-architecture/` 作为已否决过程的存档。

---

## 一、交付：archify 正稿

| 文件 | 说明 |
|---|---|
| `cap-align-capability-architecture.html` | 交付件：自包含可交互 HTML（内联 SVG、明暗主题、缩放、搜索、导出 PNG/SVG） |
| `cap-align-capability-architecture.architecture.json` | 冻结的图规格（已通过校验，勿再改；改则须重新 validate + deliver） |
| `cap-align-capability-architecture.visual-check.*` | 浏览器取证截图与回执 |

**验收回执**

- `validate --quality showcase`：9/9 工件检查通过，composition `pass`，0 error / 0 warning
- `deliver`：exit 0，spec sha256 `29d2a1e9…`→ 最终 artifact sha256 `ab0db7fa…`，812,803 bytes
- 仓库证据：8 处 `sources` 引用经 `--repo-root` 校验通过，钉在 revision `b6a06b75…`
- `visual-check`：`pass`，containment `pass`；1440×900 / 1600×1000 / 1920×1080 / 2048×1320
  四个视口均无横向或纵向溢出，最小正文投影 7.03–9.00px（下限 6px）

**图面内容**（本图讲的是能力架构，不是八步流水线——八步流水线在 README 的 hero 图里）

- 主脊柱：`W_paper · 论文编码` ‖ `W_repo · 仓库编码`（虚线区域「外来科学工作 W · 双编码规格」）
  → `归一化 → 能力 IR` → `验证门 · 验证先于分类` → `五态覆盖比对 Gap(H, W)` → `落点建议 · 六问`
  → `对齐产物 + 自检门`
- 宿主带：`宿主能力面 H` 自下方两路虚线馈入（验证门取宿主代码与产物 spec；覆盖比对取被比对的宿主面），
  落点建议以强调绿线回到宿主面，并标「落点宿主自有」
- 三张结论卡：C1 双编码规格 / C2 五态差距 · 三来源 / C3 落点宿主自有

**我自己做的感知审阅，两处遗留取舍（如实记）**

1. **五个状态名不在图体里**，在 C2 卡片里。原因是 archify 的 `desktop-readability` 门槛
   （1440px 视口下投影字号 ≥ 6px）不允许把 `equivalent · partial · missing · host-only · unknown`
   塞进焦点节点的 sublabel。若要把五态画进图体，需要把此图拆成两张（总览 + 五态细节），
   或加大 viewBox 与节点尺寸——那是另一次结构调整，需要你点头。
2. 宿主带（琥珀）左右仍留白较多；`被比对的宿主面` 那条虚线为进入焦点节点走了一段右侧绕行，
   是画面最密的一处。机械检查（标签-路由间距 ≥13px、零交叉）都过，但观感上略挤。

**另一处过程记录**：`tag` 字段（`焦点` / `self_check 10 项`）写进 JSON 后**并未被 viewer 渲染**，
第一版因此实际没把自检门的主张画出来；后来改为写进 C2/C3 卡片才算落在图上。也记一句：
`meta.legend.mode:"all"` 会列出未使用的类型并产生重复条目，应用 `auto` + `entries` 改标签。

---

## 二、存档：sivia 栅格路线（已否决）

### 执行方式

sivia 插件市场已添加（`known_marketplaces.json`）但**插件未安装**（`installed_plugins.json` 里没有），
所以 `/sivia:design-scientific-figure` 不可调用；本次是直接读 marketplace 克隆里的 skill 本体与
references 后按协议执行。渲染器为 `image-gen` skill + `doubao-seedream-4-5-251128`，2560×1440。

### 源依据

`README.md`（八步工作流、五态差距、落点六问、三来源、自检门）、`SKILL.md`（各步判据、§Scope、
§Placement 6）、`docs/paper-core.md`（C1/C2/C3、Δ 残差）、`docs/images/cap-align-principle.png`（既有图面语言）。

### 冻结的设计（Designer 产出）

**Figure Claim**：外来科学工作 W =（paper ‖ repo）是双编码能力规格，可相对于已部署宿主 H
做成证据门控的五态差距判定，终点是宿主自有的落点——不执行 W、不实现缺口。

**阅读脊柱**：规格 W（两个编码面 + 同一性谓词 + Δ≠0）→ 归一化 IR（六个 typed chips）→ 验证门
→ 五态覆盖比对（焦点）→ 落点建议 → 输出两份产物 + self_check 门；宿主能力面 H 自下馈入。

**visual_grammar_receipt（要点）**：主脊柱左→右五段；焦点=五态覆盖比对；能力=格、类型=chip、
判定门=双颚夹合、覆盖=列∩带、落点=等宽文本条、产物=文档叶；主脊柱实线 > 宿主馈入虚线 > 谓词/残差点线；
navy 墨 + 蓝（W）/ 紫（H）/ 琥珀（门）/ 绿（covered）/ 单一红（uncovered）/ 灰（unestablished）；
禁：等宽卡片墙、色块条、字面梯子、图例色卡、生产说明文字、计数数字；本图无经验图像字段。

### 长度门回执（sivia 硬门，`check_prompt_length.py`，下限 15,356 非空白字符）

| 稿 | 非空白字符 | 结果 |
|---|---|---|
| v1 | 26,180 | pass |
| v2 | 21,892 | pass |
| v3 | 17,099 | pass |
| v4 | 16,020 | pass |
| v5 | 17,215 | pass |
| v6 | 18,223 | pass |
| v7（局部修订） | 21,105 | pass |

### 尝试记录（逐稿全图审视）

- **v1** `cap-align-architecture-v1-rejected.jpg` — 生产说明印进画面：色值 `(1B2559)`、`操作block`、
  `Typograph`、`SPACING`/`COLOR` 竖条；焦点区「五态覆盖比对」根本没画；门与落点梯塌掉。
- **v2** `-v2-rejected.jpg` — 结构成立，但区域标题印成我的内部描述词（`Specification` / `normalization`
  / `gate` / `Overy` / `Deliverables`）；落点画成**字面梯子**；计数器丢失；中文长句乱码；
  `capability-alignment.json` 被折行截断。
- **v3** `-v3-rejected.jpg` — 步骤标题印成 `Sta笑一 / Sta笑二 / Sta绝五`；两编码面被拉平成一整行；
  宿主行凭空生成 `8 2 4 5` 与红色块（凭空数据 + 红色滥用）。
- **v4** `-v4-rejected.jpg` — 最好的一稿：五格顺序与标题基本正确、图例干净、文件名完整、无凭空数字。
  但顶部凭空多一条深色横梁 + 五个实心方块；③验证门被嵌进②下方；④列中印出数字 `6`；
  ⑤变彩色柱状图且标签折行；`partial` 半格丢失。
- **v5** `-v5-rejected.jpg` — 横梁、计数数字、柱状图都消掉了，但五格身份与顺序崩了（两格都写成
  「宿主能力面 H」），且图例出现**错误科学标注**「④ 五态覆盖比对 / host-only」；出现彩虹渐变条。
- **v6** `-v6-rejected.jpg` — 五格标题与顺序全对、无横梁无计数数字，但**内容相对标题整体左移一格**
  （W_repo 跑进②、chips 跑进③、④⑤ 变空箱）；图例「缺失 missing」配了绿色对勾；
  底部漏出版式 junk（`Legend Lopat` / `Supernatary: 16:9 enns`）。
- **v7 局部修订** — 未生成。`--image` 编辑端点连续四次返回 `502 Bad Gateway`（同期 text-to-image 通），
  后台重试又遇到沙箱无网络。这条动作在本机当前不可用。

### 结论

七次长度门全过、六次全图重绘 + 一次局部修订动作失败，**没有一稿通过 sivia 验收**。缺陷在轮换而非收敛：
印出生产文字 → 标题被内部词替换 → 内容错位一格 → 凭空数字与装饰图表 → 图例自相矛盾。
根因是这类"标签密集 + 拓扑精确"的图超出栅格模型的稳定能力：约束越紧，模型越倾向自造结构填满版面。
这正是 image-gen skill 自己写明的边界。

### 存档说明（过程缺陷，如实记账）

- v1–v4 的完整提示词是**就地覆写**的，只剩图与上面的审视记录；v5 起留档
  （`sivia-capability-architecture/prompts/prompt-v5.txt`、`prompt-v6.txt`、`prompt-v7-edit.txt`）。
- `cap-align-architecture-draft.jpg`（= v4）虽是最好的栅格稿，但**带已知错误**（③错位、⑤柱状图、
  `partial` 半格缺失），**没有**按仓库惯例放进 `docs/images/` 当概念渲染，以免日后被误当正稿。
  要不要把它降级采用、或整目录删除，由你定。
