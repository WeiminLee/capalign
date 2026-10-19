#!/usr/bin/env python3
"""ACL Method 主图 v6：贡献一眼可见
全宽主张条 + 中栏放大「覆盖分叉」焦点；左右为设定与合同后果。
"""
from __future__ import annotations
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyBboxPatch as _
from matplotlib.lines import Line2D

OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
SANS = "Noto Sans CJK SC"
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": [SANS, "DejaVu Sans"],
    "mathtext.fontset": "dejavusans",
    "axes.unicode_minus": False,
    "pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none",
    "figure.dpi": 150, "savefig.dpi": 300,
})

BLUE_BG, BLUE_BD, BLUE_TX = "#E8F1FA", "#6E9BC4", "#2A5680"
AMBER_BG, AMBER_BD, AMBER_TX = "#FBF3DF", "#C09A4E", "#6E4E12"
AMBER_HI = "#F3E2B0"
GREEN_BG, GREEN_BD, GREEN_TX = "#EAF5EE", "#6EAB82", "#2A6640"
PURPLE_BG, PURPLE_BD, PURPLE_TX = "#F1EBF6", "#9F7FB8", "#553870"
PIPE, INK, MUTED, WHITE, CHIP = "#8E97A3", "#1F1F1F", "#5A5A5A", "#FFFFFF", "#F2F4F6"
BAD = "#A04545"


def soft(ax, xy, w, h, *, fc, ec, lw=1.4, r=0.035, z=1):
    ax.add_patch(FancyBboxPatch(
        xy, w, h, boxstyle=f"round,pad=0.003,rounding_size={r}",
        facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z, clip_on=False))


def chip(ax, xy, w, h, *, fc=WHITE, ec="#CDD2D8", lw=0.9, r=0.028, z=3):
    soft(ax, xy, w, h, fc=fc, ec=ec, lw=lw, r=r, z=z)


def arrow(ax, x0, y0, x1, y1, *, c=PIPE, lw=1.35):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=c, lw=lw,
                                mutation_scale=10, shrinkA=1, shrinkB=1),
                zorder=15)


def tx(ax, x, y, s, *, size=7.0, w="normal", c=INK, ha="center", va="center", **kw):
    ax.text(x, y, s, fontsize=size, fontweight=w, color=c,
            ha=ha, va=va, zorder=30, clip_on=False, **kw)


def icon_doc(ax, x, y, *, s=0.018, color=BLUE_TX):
    ax.add_patch(FancyBboxPatch((x - s*0.55, y - s*0.7), s*1.1, s*1.4,
        boxstyle="round,pad=0.001,rounding_size=0.004",
        facecolor=WHITE, edgecolor=color, lw=1.05, zorder=28))
    for i in range(3):
        ax.add_line(Line2D([x - s*0.32, x + s*0.32],
                           [y + s*0.35 - i*s*0.28]*2, color=color, lw=0.75, zorder=29))


def icon_repo(ax, x, y, *, s=0.018, color=BLUE_TX):
    ax.add_patch(FancyBboxPatch((x - s*0.7, y - s*0.45), s*1.4, s*0.95,
        boxstyle="round,pad=0.001,rounding_size=0.006",
        facecolor=WHITE, edgecolor=color, lw=1.05, zorder=28))
    ax.add_patch(FancyBboxPatch((x - s*0.7, y + s*0.25), s*0.55, s*0.28,
        boxstyle="round,pad=0.001,rounding_size=0.004",
        facecolor=color, edgecolor=color, lw=0.4, zorder=29, alpha=0.35))


def icon_fork(ax, x, y, *, s=0.028, color=AMBER_TX):
    ax.plot([x, x], [y + s, y], color=color, lw=2.0, zorder=28)
    ax.plot([x, x - s], [y, y - s], color=color, lw=2.0, zorder=28)
    ax.plot([x, x + s], [y, y - s], color=color, lw=2.0, zorder=28)
    ax.plot(x, y + s, "o", color=color, markersize=4.5, zorder=29)


def icon_check(ax, x, y, *, s=0.014, color=GREEN_TX):
    ax.add_patch(Circle((x, y), s*1.15, facecolor=WHITE, edgecolor=color, lw=1.15, zorder=28))
    ax.plot([x - s*0.5, x - s*0.05, x + s*0.55],
            [y - s*0.05, y - s*0.45, y + s*0.45],
            color=color, lw=1.35, solid_capstyle="round", zorder=29)


def icon_x(ax, x, y, *, s=0.014, color=PURPLE_TX):
    ax.add_patch(Circle((x, y), s*1.15, facecolor=WHITE, edgecolor=color, lw=1.15, zorder=28))
    ax.plot([x - s*0.45, x + s*0.45], [y - s*0.45, y + s*0.45], color=color, lw=1.35, zorder=29)
    ax.plot([x - s*0.45, x + s*0.45], [y + s*0.45, y - s*0.45], color=color, lw=1.35, zorder=29)


def icon_badge(ax, x, y, n, color):
    ax.add_patch(Circle((x, y), 0.014, facecolor=color, edgecolor=color, lw=0.4, zorder=28))
    tx(ax, x, y, str(n), size=6.2, w="bold", c=WHITE)


def row(ax, x, y, w, h, left, right, *, left_c=INK, right_c=MUTED):
    soft(ax, (x, y), w, h, fc=CHIP, ec="#DEE2E7", lw=0.5, r=0.016, z=4)
    tx(ax, x + 0.01, y + h/2, left, size=5.4, w="bold", c=left_c, ha="left")
    tx(ax, x + w - 0.01, y + h/2, right, size=5.1, c=right_c, ha="right")


def main():
    fig = plt.figure(figsize=(7.3, 5.25), facecolor="white")
    ax = fig.add_axes([0.008, 0.018, 0.984, 0.955])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    # title
    tx(ax, 0.50, 0.985, "覆盖分叉与类型化引入", size=11.8, w="bold")

    # ===== CLAIM BANNER (contribution at a glance) =====
    soft(ax, (0.008, 0.900), 0.984, 0.065, fc=AMBER_HI, ec=AMBER_BD, lw=1.8, r=0.025, z=2)
    icon_fork(ax, 0.045, 0.932, s=0.022, color=AMBER_TX)
    tx(ax, 0.075, 0.945, "核心贡献 C1", size=7.5, w="bold", c=AMBER_TX, ha="left")
    tx(ax, 0.075, 0.918,
       "同一 λ 投到论文面 / 仓库面 → 宿主缺口集合可不相交 → 单面包仓库或仅论文在合同上错误",
       size=6.4, w="bold", c=INK, ha="left")

    # stage shells — middle WIDER and stronger
    soft(ax, (0.006, 0.015), 0.236, 0.865, fc=BLUE_BG, ec=BLUE_BD, lw=1.35, r=0.028, z=0)
    soft(ax, (0.262, 0.015), 0.476, 0.865, fc=AMBER_BG, ec=AMBER_BD, lw=2.2, r=0.028, z=0)  # FOCAL
    soft(ax, (0.760, 0.015), 0.234, 0.865, fc=GREEN_BG, ec=GREEN_BD, lw=1.35, r=0.028, z=0)
    arrow(ax, 0.242, 0.48, 0.262, 0.48, lw=1.8)
    arrow(ax, 0.738, 0.48, 0.760, 0.48, lw=1.8)

    # ===== LEFT (a) supporting =====
    icon_badge(ax, 0.025, 0.845, 1, BLUE_TX)
    tx(ax, 0.042, 0.845, "(a) 设定", size=7.6, w="bold", c=BLUE_TX, ha="left")
    tx(ax, 0.042, 0.820, "双编码 → λ（引擎）", size=5.3, c=MUTED, ha="left")

    chip(ax, (0.020, 0.700), 0.100, 0.090, fc=WHITE, ec=BLUE_BD)
    icon_doc(ax, 0.040, 0.760, color=BLUE_TX)
    tx(ax, 0.070, 0.760, r"$W_{\mathrm{paper}}$", size=5.8, w="bold", c=BLUE_TX, ha="left")
    tx(ax, 0.070, 0.735, r"$s,v_p$", size=5.2, c=MUTED, ha="left")
    tx(ax, 0.070, 0.715, "论文面", size=5.1, c=MUTED, ha="left")

    chip(ax, (0.128, 0.700), 0.100, 0.090, fc=WHITE, ec=BLUE_BD)
    icon_repo(ax, 0.148, 0.760, color=BLUE_TX)
    tx(ax, 0.178, 0.760, r"$W_{\mathrm{repo}}$", size=5.8, w="bold", c=BLUE_TX, ha="left")
    tx(ax, 0.178, 0.735, r"$e,v_r$", size=5.2, c=MUTED, ha="left")
    tx(ax, 0.178, 0.715, "仓库面", size=5.1, c=MUTED, ha="left")

    arrow(ax, 0.070, 0.700, 0.100, 0.665, lw=1.0)
    arrow(ax, 0.178, 0.700, 0.145, 0.665, lw=1.0)

    chip(ax, (0.030, 0.575), 0.185, 0.080, fc=WHITE, ec="#C5CCD4")
    tx(ax, 0.122, 0.630, "Id 合并 → 槽位 u", size=6.0, w="bold")
    tx(ax, 0.122, 0.600, r"$(p,s,e,v_p,v_r,\kappa)$", size=5.4, c=MUTED)
    tx(ax, 0.122, 0.580, r"$\kappa$：做法冲突", size=5.1, c=MUTED)

    arrow(ax, 0.122, 0.575, 0.122, 0.540, lw=1.0)

    chip(ax, (0.020, 0.040), 0.205, 0.490, fc=WHITE, ec=BLUE_BD, lw=1.0)
    tx(ax, 0.035, 0.500, r"$\lambda(u)$ 分区（非贡献）", size=6.2, w="bold", c=BLUE_TX, ha="left")
    for y, name, desc in [
        (0.450, "两侧齐", "对齐"),
        (0.405, "义务缺入口", "→ 论文缺口"),
        (0.360, "入口缺义务", "→ 仓库缺口"),
        (0.315, "缺有效性", "→ 写 K_H"),
        (0.270, "做法冲突", "→ 拒绝"),
        (0.225, "宿主已有", "→ 不动"),
    ]:
        row(ax, 0.030, y, 0.185, 0.036, name, desc, left_c=BLUE_TX)
    tx(ax, 0.122, 0.175, "λ 只做分区", size=5.5, w="bold", c=BLUE_TX)
    tx(ax, 0.122, 0.145, "贡献在中栏分叉", size=5.3, c=MUTED)
    tx(ax, 0.122, 0.115, "不报六个芯片墙", size=5.2, c=MUTED)
    tx(ax, 0.122, 0.080, "下一步只读 λ", size=5.1, c=MUTED)
    tx(ax, 0.122, 0.055, "不回头改标签", size=5.1, c=MUTED)

    # ===== MIDDLE (b) FOCAL CONTRIBUTION =====
    # core ribbon
    soft(ax, (0.275, 0.825), 0.450, 0.045, fc=AMBER_BD, ec=AMBER_BD, lw=0.5, r=0.02, z=5)
    tx(ax, 0.500, 0.847, "★  核心贡献 C1 · 覆盖分叉  ★", size=8.0, w="bold", c=WHITE)

    icon_badge(ax, 0.285, 0.795, 2, AMBER_TX)
    icon_fork(ax, 0.315, 0.795, s=0.020, color=AMBER_TX)
    tx(ax, 0.340, 0.795, "(b) 同一 λ，两面缺口可不相交", size=7.4, w="bold", c=AMBER_TX, ha="left")

    # Obl / Ent
    chip(ax, (0.280, 0.725), 0.195, 0.045, fc=WHITE, ec="#C5CCD4")
    tx(ax, 0.377, 0.747, r"$\mathrm{Obl}=\{p:s{=}1\}$", size=6.4, w="bold")
    chip(ax, (0.500, 0.725), 0.195, 0.045, fc=WHITE, ec="#C5CCD4")
    tx(ax, 0.597, 0.747, r"$\mathrm{Ent}=\{p:e{=}1\}$", size=6.4, w="bold")

    # big fork hub
    soft(ax, (0.380, 0.655), 0.215, 0.050, fc=WHITE, ec=AMBER_BD, lw=1.5, r=0.025, z=4)
    tx(ax, 0.487, 0.680, r"同一 $\lambda$ 投影", size=7.0, w="bold", c=AMBER_TX)

    arrow(ax, 0.430, 0.655, 0.360, 0.600, lw=1.8, c=AMBER_BD)
    arrow(ax, 0.545, 0.655, 0.615, 0.600, lw=1.8, c=AMBER_BD)

    # two gap cards — large
    soft(ax, (0.275, 0.430), 0.200, 0.160, fc=WHITE, ec=AMBER_BD, lw=1.5, r=0.03, z=3)
    icon_doc(ax, 0.295, 0.555, s=0.016, color=AMBER_TX)
    tx(ax, 0.320, 0.555, "论文面缺口", size=6.8, w="bold", c=AMBER_TX, ha="left")
    tx(ax, 0.375, 0.520, r"$\mathrm{Obl}\setminus\mathrm{Ent}$", size=7.5, w="bold")
    tx(ax, 0.375, 0.490, "义务有 · 入口无 → gap", size=5.5, c=MUTED)
    tx(ax, 0.375, 0.465, "反面类型 → absent", size=5.4, c=MUTED)
    tx(ax, 0.375, 0.440, "例：qha", size=6.0, w="bold")

    soft(ax, (0.525, 0.430), 0.200, 0.160, fc=WHITE, ec=AMBER_BD, lw=1.5, r=0.03, z=3)
    icon_repo(ax, 0.545, 0.555, s=0.016, color=AMBER_TX)
    tx(ax, 0.570, 0.555, "仓库面缺口", size=6.8, w="bold", c=AMBER_TX, ha="left")
    tx(ax, 0.625, 0.520, r"$\mathrm{Ent}\setminus\mathrm{Obl}$", size=7.5, w="bold")
    tx(ax, 0.625, 0.490, "入口有 · 义务无 → gap", size=5.5, c=MUTED)
    tx(ax, 0.625, 0.465, "反面类型 → absent", size=5.4, c=MUTED)
    tx(ax, 0.625, 0.440, "例：band", size=6.0, w="bold")

    # THE one-liner insight — biggest claim box
    soft(ax, (0.275, 0.300), 0.450, 0.105, fc=AMBER_HI, ec=AMBER_BD, lw=2.0, r=0.03, z=5)
    tx(ax, 0.500, 0.375, "一眼结论", size=6.0, w="bold", c=AMBER_TX)
    tx(ax, 0.500, 0.345, "缺口集合可不相交", size=9.5, w="bold", c=INK)
    tx(ax, 0.500, 0.315, "⇒  wrap-repo / 仅论文  在合同上错误（产生 FI 或 Miss）", size=6.2, w="bold", c=BAD)

    # mini evidence + vs
    chip(ax, (0.275, 0.040), 0.450, 0.240, fc=WHITE, ec="#C5CCD4")
    tx(ax, 0.290, 0.250, "示意证据（非经验数）· 对照基线失败模式", size=6.0, w="bold", ha="left")

    # tiny table
    for x, h in ((0.320, "槽"), (0.400, "λ"), (0.490, "论文"), (0.560, "仓库"), (0.655, "单面后果")):
        tx(ax, x, 0.220, h, size=5.2, w="bold", c=MUTED)
    for y, vals in [
        (0.175, ("qha", "义务缺入口", "gap", "absent", "仅论文漏? 包仓Miss")),
        (0.130, ("band", "入口缺义务", "absent", "gap", "包仓库 → FI")),
        (0.085, ("κ", "冲突", "未决", "未决", "必须拒绝")),
    ]:
        soft(ax, (0.285, y - 0.012), 0.430, 0.038, fc=CHIP, ec="#E2E5EA", lw=0.45, r=0.012, z=4)
        for x, v in zip((0.320, 0.400, 0.490, 0.560, 0.655), vals):
            tx(ax, x, y + 0.007, v, size=5.1, w="bold" if x == 0.320 else "normal",
               c=INK if x != 0.655 else BAD)

    tx(ax, 0.500, 0.055, "这不是「检测一致性」——是宿主相对对齐的合同对象变了", size=5.4, c=MUTED)

    # ===== RIGHT (c) consequence =====
    icon_badge(ax, 0.778, 0.845, 3, GREEN_TX)
    tx(ax, 0.795, 0.845, "(c) 后果", size=7.6, w="bold", c=GREEN_TX, ha="left")
    tx(ax, 0.795, 0.820, "I 安装/拒绝 · 合同", size=5.3, c=MUTED, ha="left")

    chip(ax, (0.772, 0.560), 0.210, 0.230, fc=WHITE, ec="#C5CCD4")
    tx(ax, 0.785, 0.760, r"$\lambda\to I$（C2）", size=6.3, w="bold", ha="left")
    for y, a, b, col in [
        (0.710, "义务缺入口", "装 p", AMBER_TX),
        (0.670, "入口缺义务", "拒装", AMBER_TX),
        (0.630, "缺有效性", "写 K_H", GREEN_TX),
        (0.590, "冲突", "拒绝", PURPLE_TX),
    ]:
        row(ax, 0.780, y, 0.195, 0.032, a, b, left_c=col)

    chip(ax, (0.772, 0.430), 0.098, 0.100, fc=WHITE, ec=GREEN_BD, lw=1.1)
    icon_check(ax, 0.795, 0.500, color=GREEN_TX)
    tx(ax, 0.821, 0.500, "安装", size=6.5, w="bold", c=GREEN_TX, ha="left")
    tx(ax, 0.821, 0.460, r"$P_H{+}K_H$", size=5.2, c=MUTED, ha="left")

    chip(ax, (0.884, 0.430), 0.098, 0.100, fc=PURPLE_BG, ec=PURPLE_BD, lw=1.1)
    icon_x(ax, 0.907, 0.500, color=PURPLE_TX)
    tx(ax, 0.933, 0.500, "拒绝", size=6.5, w="bold", c=PURPLE_TX, ha="left")
    tx(ax, 0.933, 0.460, "不引入", size=5.2, c=MUTED, ha="left")

    chip(ax, (0.772, 0.040), 0.210, 0.360, fc=WHITE, ec=GREEN_BD, lw=1.05)
    tx(ax, 0.785, 0.370, "合同 C3", size=6.5, w="bold", c=GREEN_TX, ha="left")
    tx(ax, 0.785, 0.345, r"对照 wrap / 仅论文", size=5.1, c=MUTED, ha="left")

    for y, sym, desc, col in [
        (0.290, "FI", "假引入", BLUE_TX),
        (0.240, "Miss", "漏义务", AMBER_TX),
        (0.190, r"$t_v$", "有效性检查", GREEN_TX),
    ]:
        soft(ax, (0.785, y - 0.012), 0.185, 0.040, fc=CHIP, ec="#DEE2E7", lw=0.5, r=0.014, z=4)
        tx(ax, 0.800, y + 0.008, sym, size=6.0, w="bold", c=col, ha="left")
        tx(ax, 0.955, y + 0.008, desc, size=5.2, c=MUTED, ha="right")

    tx(ax, 0.877, 0.140, "可测", size=5.6, w="bold")
    tx(ax, 0.877, 0.110, "fail-before", size=5.2, c=MUTED)
    tx(ax, 0.877, 0.085, "→ destroy", size=5.2, c=MUTED)
    tx(ax, 0.877, 0.055, "Fast 未测不报", size=5.0, c=MUTED)

    stem = "cap-align-acl-main-zh"
    fig.savefig(OUT / f"{stem}.pdf")
    fig.savefig(OUT / f"{stem}.svg")
    fig.savefig(OUT / f"{stem}.png", dpi=300)
    plt.close(fig)
    print("wrote", OUT / stem)


if __name__ == "__main__":
    main()
