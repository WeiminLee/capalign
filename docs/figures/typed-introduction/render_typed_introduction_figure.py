#!/usr/bin/env python3
"""
ACL Method figure v2 (C1–C3 lock): coverage fork + typed introduction.
(a) dual encode → product Id → λ partition
(b) qha/band coverage fork
(c) I with refuse + K_H
(d) contract FI/Miss/t_v + destroy vs wrap-repo/paper-only
Double-column ~7.0 in x 5.25 in; PDF + SVG + PNG@300dpi.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent  # also /workspace/cap-align-figure on box
OUT.mkdir(parents=True, exist_ok=True)

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Liberation Sans", "Nimbus Sans", "sans-serif"],
        "mathtext.fontset": "dejavusans",
        "axes.unicode_minus": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
    }
)

INK = "#111111"
MUTED = "#4a4a4a"
FAINT = "#8a8a8a"
LIGHT = "#f2f2f2"
WHITE = "#ffffff"
PANEL = "#fcfcfc"
LINE = "#222222"
EDGE = "#bdbdbd"
ACCENT = "#1f4e79"
ACCENT_LT = "#e8f0f7"
WARN = "#6b5320"
WARN_LT = "#f5efdf"
OK = "#1f5a32"
OK_LT = "#e6f0e9"
BAD = "#6b2c2c"
BAD_LT = "#f5e8e8"
REFUSE = "#5a3d7a"
REFUSE_LT = "#f0eaf5"


def rounded(ax, xy, w, h, *, fc=LIGHT, ec=LINE, lw=0.75, r=0.035, z=2, ls="-"):
    p = FancyBboxPatch(
        xy, w, h,
        boxstyle=f"round,pad=0.006,rounding_size={r}",
        facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls,
        zorder=z, clip_on=False,
    )
    ax.add_patch(p)
    return p


def arrow(ax, p0, p1, *, color=INK, lw=0.85, ms=7.5, rad=0.0, z=5, shrinkA=0.5, shrinkB=0.5):
    a = FancyArrowPatch(
        p0, p1,
        arrowstyle="-|>,head_length=3.0,head_width=1.8",
        mutation_scale=ms, linewidth=lw, color=color,
        connectionstyle=f"arc3,rad={rad}",
        zorder=z, shrinkA=shrinkA, shrinkB=shrinkB, clip_on=False,
    )
    ax.add_patch(a)
    return a


def txt(ax, x, y, s, *, size=7.0, weight="normal", color=INK, ha="center", va="center", **kw):
    return ax.text(
        x, y, s, fontsize=size, fontweight=weight, color=color,
        ha=ha, va=va, zorder=10, clip_on=False, **kw,
    )


def panel_frame(ax, title):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("auto")
    ax.axis("off")
    rounded(ax, (0.008, 0.008), 0.984, 0.984, fc=PANEL, ec=EDGE, lw=0.55, r=0.018, z=0)
    txt(ax, 0.028, 0.955, title, size=7.8, weight="bold", ha="left", va="top", color=INK)


def draw_panel_a(ax):
    panel_frame(ax, r"(a)  Dual encode $\rightarrow$ product Id $\rightarrow$ $\lambda$  [C1]")

    # W_paper / W_repo
    rounded(ax, (0.04, 0.62), 0.26, 0.26, fc=WHITE, ec=LINE, lw=0.8, r=0.03)
    rounded(ax, (0.33, 0.62), 0.26, 0.26, fc=WHITE, ec=LINE, lw=0.8, r=0.03)
    txt(ax, 0.17, 0.845, r"$W_{\mathrm{paper}}$", size=7.6, weight="bold")
    txt(ax, 0.46, 0.845, r"$W_{\mathrm{repo}}$", size=7.6, weight="bold")

    for x0, labs in (
        (0.055, [(r"$s$", "procedure"), (r"$v_{\mathrm{p}}$", "validity")]),
        (0.345, [(r"$e$", "entry"), (r"$v_{\mathrm{r}}$", "validity")]),
    ):
        y = 0.76
        for sym, name in labs:
            rounded(ax, (x0, y - 0.05), 0.22, 0.055, fc=ACCENT_LT, ec=ACCENT, lw=0.5, r=0.016)
            txt(ax, x0 + 0.03, y - 0.022, sym, size=6.2, color=ACCENT, ha="left", weight="bold")
            txt(ax, x0 + 0.10, y - 0.022, name, size=5.5, color=ACCENT, ha="left")
            y -= 0.075

    # Id
    rounded(ax, (0.64, 0.68), 0.31, 0.15, fc=WARN_LT, ec=WARN, lw=0.85, r=0.028)
    txt(ax, 0.795, 0.79, "product Id merge", size=6.8, weight="bold", color=WARN)
    txt(ax, 0.795, 0.73, r"independent inventories", size=5.6, color=WARN)
    arrow(ax, (0.30, 0.75), (0.64, 0.76), color=FAINT, lw=0.7, ms=6)
    arrow(ax, (0.59, 0.75), (0.64, 0.76), color=FAINT, lw=0.7, ms=6)

    # unit
    rounded(ax, (0.06, 0.40), 0.88, 0.14, fc=WHITE, ec=LINE, lw=0.85, r=0.026)
    txt(ax, 0.50, 0.495, r"unit  $u=(p,\,s,\,e,\,v_{\mathrm{p}},\,v_{\mathrm{r}},\,\kappa)$",
        size=7.4, weight="bold")
    txt(ax, 0.50, 0.435, r"$\lambda(u)$ partitions residual  ·  not a detection headline",
        size=5.6, color=MUTED)
    arrow(ax, (0.795, 0.68), (0.70, 0.54), color=FAINT, lw=0.7, ms=6)

    # chips — emphasize partition role
    chips = [
        ("both-\naligned", OK_LT, OK),
        ("obl.-sans-\nentry", ACCENT_LT, ACCENT),
        ("entry-sans-\nobl.", ACCENT_LT, ACCENT),
        ("validity-\ngap", WARN_LT, WARN),
        ("proc.-\nconflict", BAD_LT, BAD),
        ("incon-\ngruent", LIGHT, MUTED),
    ]
    x = 0.04
    w = 0.15
    gap = 0.008
    for name, fc, ec in chips:
        rounded(ax, (x, 0.13), w, 0.16, fc=fc, ec=ec, lw=0.55, r=0.02)
        txt(ax, x + w / 2, 0.21, name, size=5.3, color=ec, weight="bold", linespacing=1.15)
        x += w + gap
    arrow(ax, (0.50, 0.40), (0.50, 0.30), color=FAINT, lw=0.7, ms=6)
    txt(ax, 0.50, 0.055, r"C1: product Id before typing  ·  forbids sentence$\leftrightarrow$function host gaps",
        size=5.6, color=MUTED)


def draw_panel_b(ax):
    panel_frame(ax, r"(b)  Coverage fork on $H$  [C1]  ·  $\mathtt{qha}$ / $\mathtt{band}$")

    rounded(ax, (0.04, 0.82), 0.92, 0.08, fc=ACCENT_LT, ec=ACCENT, lw=0.6, r=0.02)
    txt(ax, 0.50, 0.86,
        r"paper-face gaps  $\neq$  repo-face gaps   (can be disjoint)",
        size=6.6, color=ACCENT, weight="bold")

    rounded(ax, (0.04, 0.32), 0.44, 0.46, fc=WHITE, ec=LINE, lw=0.8, r=0.026)
    rounded(ax, (0.52, 0.32), 0.44, 0.46, fc=WHITE, ec=LINE, lw=0.8, r=0.026)
    txt(ax, 0.26, 0.735, "paper projection", size=7.0, weight="bold")
    txt(ax, 0.74, 0.735, "repo projection", size=7.0, weight="bold")
    txt(ax, 0.26, 0.69, r"Obl $=\{p:s{=}1\}$", size=5.4, color=FAINT)
    txt(ax, 0.74, 0.69, r"Ent $=\{p:e{=}1\}$", size=5.4, color=FAINT)

    # qha
    rounded(ax, (0.07, 0.52), 0.38, 0.13, fc=ACCENT_LT, ec=ACCENT, lw=0.65, r=0.02)
    txt(ax, 0.26, 0.605, r"$\mathtt{qha}$  obl.-sans-entry", size=6.0, color=ACCENT, weight="bold")
    txt(ax, 0.26, 0.555, r"$\Rightarrow$  gap", size=7.0, color=ACCENT, weight="bold")

    rounded(ax, (0.55, 0.52), 0.38, 0.13, fc=LIGHT, ec=MUTED, lw=0.6, r=0.02, ls="--")
    txt(ax, 0.74, 0.605, r"$\mathtt{qha}$  obl.-sans-entry", size=6.0, color=MUTED, weight="bold")
    txt(ax, 0.74, 0.555, r"$\Rightarrow$  absent", size=7.0, color=MUTED, weight="bold")

    # band
    rounded(ax, (0.07, 0.36), 0.38, 0.13, fc=LIGHT, ec=MUTED, lw=0.6, r=0.02, ls="--")
    txt(ax, 0.26, 0.445, r"$\mathtt{band}$  entry-sans-obl.", size=6.0, color=MUTED, weight="bold")
    txt(ax, 0.26, 0.395, r"$\Rightarrow$  absent", size=7.0, color=MUTED, weight="bold")

    rounded(ax, (0.55, 0.36), 0.38, 0.13, fc=ACCENT_LT, ec=ACCENT, lw=0.65, r=0.02)
    txt(ax, 0.74, 0.445, r"$\mathtt{band}$  entry-sans-obl.", size=6.0, color=ACCENT, weight="bold")
    txt(ax, 0.74, 0.395, r"$\Rightarrow$  gap", size=7.0, color=ACCENT, weight="bold")

    arrow(ax, (0.48, 0.585), (0.52, 0.585), color=ACCENT, lw=0.8, ms=5.5)
    arrow(ax, (0.52, 0.425), (0.48, 0.425), color=ACCENT, lw=0.8, ms=5.5)

    rounded(ax, (0.04, 0.12), 0.92, 0.16, fc=WARN_LT, ec=WARN, lw=0.55, r=0.02)
    txt(ax, 0.50, 0.23,
        r"missing ids: paper $\{{\tt qha}\}$  $\cap$  repo $\{{\tt band}\}$  $=$  $\emptyset$",
        size=6.4, color=WARN, weight="bold")
    txt(ax, 0.50, 0.155,
        r"single-face policy cannot be FI$=$0 and Miss$=$0 when both omission types nonempty",
        size=5.4, color=MUTED)


def draw_panel_c(ax):
    panel_frame(ax, r"(c)  Operator $I$: install / refuse / $K_H$  [C2]")

    txt(ax, 0.055, 0.88, r"$\lambda$", size=6.2, weight="bold", ha="left", color=MUTED)
    txt(ax, 0.26, 0.88, "action on $H=(P_H,K_H)$", size=6.2, weight="bold", ha="left", color=MUTED)
    txt(ax, 0.68, 0.88, "accept / destroy", size=6.2, weight="bold", ha="left", color=MUTED)
    ax.plot([0.04, 0.96], [0.855, 0.855], color=EDGE, lw=0.5, transform=ax.transAxes, clip_on=False)

    rows = [
        ("both-aligned",
         r"bind entry; $+K_H$ if shared $v$",
         r"fail$\to$pass; unbind$\to$fail",
         OK_LT, OK),
        ("obl.-sans-entry",
         r"write paper steps (no forged $e$)",
         r"fail$\to$pass; drop steps$\to$fail",
         ACCENT_LT, ACCENT),
        ("entry-sans-obl.",
         r"REFUSE  —  $\Delta P_H=\emptyset$",
         r"$p\notin$ paper tests",
         REFUSE_LT, REFUSE),
        ("validity-gap",
         r"bind + install check $\to K_H$",
         r"$t_v$: $0\to1$; drop check$\to0$",
         WARN_LT, WARN),
        ("proc.-conflict",
         r"REFUSE silent pick; keep record",
         r"$H$ unchanged",
         REFUSE_LT, REFUSE),
        ("incongruent",
         r"ignore",
         r"—",
         LIGHT, MUTED),
    ]
    y = 0.78
    rh = 0.105
    for name, edit, test, fc, ec in rows:
        rounded(ax, (0.04, y - rh + 0.012), 0.92, rh - 0.01, fc=fc, ec=ec, lw=0.45, r=0.014)
        txt(ax, 0.055, y - rh / 2 + 0.008, name, size=5.5, weight="bold", ha="left", color=ec)
        txt(ax, 0.26, y - rh / 2 + 0.008, edit, size=5.4, ha="left", color=INK)
        txt(ax, 0.68, y - rh / 2 + 0.008, test, size=5.4, ha="left", color=MUTED)
        y -= rh

    txt(ax, 0.50, 0.05,
        r"refusal is success  ·  validity-gap requires $t_v{=}1$  ·  Props. 2–4",
        size=5.6, color=MUTED, weight="bold")


def draw_panel_d(ax):
    panel_frame(ax, r"(d)  Contract vs $W_{\mathrm{rap}}$ / $P_{\mathrm{aper}}$  [C3]")

    cols = [
        (0.04, r"$I$  (typed)", OK_LT, OK,
         [r"FI $=0$  (Prop. 2)",
          r"refuse non-obligations",
          r"$t_v{=}1$ on val.-gap"]),
        (0.355, r"$W_{\mathrm{rap}}$ / MCP", BAD_LT, BAD,
         [r"FI $=$ # entry-sans-obl.",
          r"Miss $=$ # obl.-sans-entry",
          r"$t_v{=}0$  (no $K_H$)"]),
        (0.67, r"$P_{\mathrm{aper}}$", WARN_LT, WARN,
         [r"FI $=0$ but no entry bind",
          r"writes Obl without $e$",
          r"$t_v{=}0$  (Prop. 4)"]),
    ]
    for x, title, fc, ec, bullets in cols:
        rounded(ax, (x, 0.46), 0.29, 0.38, fc=WHITE, ec=ec, lw=0.85, r=0.026)
        rounded(ax, (x + 0.012, 0.745), 0.266, 0.07, fc=fc, ec=ec, lw=0.55, r=0.016)
        txt(ax, x + 0.145, 0.78, title, size=6.4, weight="bold", color=ec)
        yy = 0.69
        for b in bullets:
            txt(ax, x + 0.025, yy, "·  " + b, size=5.3, ha="left", color=INK)
            yy -= 0.065

    rounded(ax, (0.04, 0.335), 0.92, 0.09, fc=LIGHT, ec=MUTED, lw=0.5, r=0.018)
    txt(ax, 0.50, 0.38,
        r"ablation $\pi$: swap omission types $\rightarrow$ $I$  (Prop. 5: pass sets differ)",
        size=5.5, color=MUTED)

    metrics = [
        (0.04, "Effective", r"FI · Miss · $t_v$", OK_LT, OK),
        (0.355, "Testable", "red→green→\nred-on-delete", WARN_LT, WARN),
        (0.67, "Fast", "calls to green\n(optional)", ACCENT_LT, ACCENT),
    ]
    for x, title, body, fc, ec in metrics:
        rounded(ax, (x, 0.055), 0.29, 0.24, fc=fc, ec=ec, lw=0.65, r=0.02)
        txt(ax, x + 0.145, 0.23, title, size=7.0, weight="bold", color=ec)
        txt(ax, x + 0.145, 0.13, body, size=5.5, color=INK, linespacing=1.25)


def main():
    fig_w, fig_h = 7.0, 5.25
    fig = plt.figure(figsize=(fig_w, fig_h), facecolor="white")
    gs = fig.add_gridspec(
        2, 2,
        left=0.012, right=0.988,
        top=0.988, bottom=0.018,
        wspace=0.05, hspace=0.07,
    )
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[1, 0])
    ax_c = fig.add_subplot(gs[0, 1])
    ax_d = fig.add_subplot(gs[1, 1])

    draw_panel_a(ax_a)
    draw_panel_b(ax_b)
    draw_panel_c(ax_c)
    draw_panel_d(ax_d)

    pdf = OUT / "cap-align-typed-introduction.pdf"
    svg = OUT / "cap-align-typed-introduction.svg"
    png = OUT / "cap-align-typed-introduction.png"
    for path, fmt, dpi in (
        (pdf, "pdf", 300),
        (svg, "svg", None),
        (png, "png", 300),
    ):
        kw = dict(format=fmt, facecolor="white", edgecolor="none")
        if dpi:
            kw["dpi"] = dpi
        fig.savefig(path, **kw)
    plt.close(fig)
    for path in (pdf, svg, png):
        print("wrote", path, path.stat().st_size)


if __name__ == "__main__":
    main()
