# Figure notes: Coverage fork + typed introduction (C1–C3)

**Files.** `cap-align-typed-introduction.pdf` (vector), `.svg` (vector), `.png` (300 dpi preview).  
**Source.** `render_typed_introduction_figure.py` (matplotlib; regenerated 2026-10-18 for C1–C3 lock).  
**Size.** Double-column Method figure, ~7.0 in × 5.25 in.

## Figure claim (caption-ready, C1–C3)

Dual encoding forks host coverage after product-Id merge; \(\lambda\) selects introduction *and principled refusal* on \(H=(P_H,K_H)\), including validity checks \(K_H\); vs wrap-repo / paper-only, contract metrics FI / Miss / \(t_v\) + destroy-tests. Lead insight is the **coverage fork**, not “six λ chips.”

## Panel contents

| Panel | Content | Claim |
|---|---|---|
| **(a)** Dual encode → product Id → \(\lambda\) | \(W_{\mathrm{paper}}\) (\(s\), \(v_{\mathrm{p}}\)) ∥ \(W_{\mathrm{repo}}\) (\(e\), \(v_{\mathrm{r}}\)) → product Id → unit \(u\); \(\lambda\) as *partition engine* | **C1** model |
| **(b)** Coverage fork | `qha` (obl.-sans-entry) → gap/absent; `band` (entry-sans-obl.) → absent/gap; missing-id intersection \(\emptyset\); single-face impossibility | **C1** insight |
| **(c)** Operator \(I\): install / refuse / \(K_H\) | Per-\(\lambda\) edit; purple rows = REFUSE; validity-gap installs \(K_H\) (\(t_v\)); fail-before / destroy | **C2** |
| **(d)** Contract vs \(W_{\mathrm{rap}}\) / \(P_{\mathrm{aper}}\) | \(I\) vs wrap-repo/MCP vs paper-only; ablation \(\pi\); Effective / Testable / Fast (optional) | **C3** |

## Symbol glossary

| Symbol | Meaning |
|---|---|
| \(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\) | Dual-encoded scientific work |
| \(s\), \(e\) | Paper procedure / repo entry |
| \(v_{\mathrm{p}}\), \(v_{\mathrm{r}}\) | Paper / repo validity (invalidation) |
| \(\kappa\) | Procedure conflict (only when \(s=e=1\)) |
| \(u=(p,s,e,v_{\mathrm{p}},v_{\mathrm{r}},\kappa)\) | Slot-filled unit for product \(p\) |
| \(\lambda(u)\) | Type partition (means, not headline contribution) |
| \(H=(P_H,K_H)\) | Host products + installed validity checks |
| \(I\) | Typed introduction (install **or** refuse) |
| \(W_{\mathrm{rap}}\) | Wrap-repo / MCP-attach baseline |
| \(P_{\mathrm{aper}}\) | Paper-only baseline |
| \(\pi\) | Ablation swapping omission types |
| FI, Miss, \(t_v\) | False introduction; missed obligation; validity-check indicator |

## Suggested caption (English)

> **Figure X.** Coverage fork and typed introduction for dual-encoded scientific work. (a) Independent paper/repo encodings are merged by product identity into unit \(u\); unique \(\lambda\) partitions residual (partition engine, not contribution headline). (b) **Coverage fork:** the same \(\lambda\) projects to disjoint host-gap sets on paper vs repo faces—illustrated on mini-ref / phonopy-style slots `qha` (obl.-sans-entry → gap/absent) and `band` (entry-sans-obl. → absent/gap). (c) Operator \(I\) maps \(\lambda\) to edits on \(H=(P_H,K_H)\) *or* principled refusal; validity-gap installs \(K_H\) (\(t_v\)). (d) Against wrap-repo (\(W_{\mathrm{rap}}\) / MCP) and paper-only (\(P_{\mathrm{aper}}\)), contract metrics Effective (FI, Miss, \(t_v\)) and Testable (fail-before→destroy); Fast optional until measured.

## Visual / production notes

- English labels; black/white-friendly palette; purple for REFUSE rows; amber for validity / fork callouts.
- Fonts: DejaVu Sans (+ mathtext dejavusans). PDF fonttype 42.
- No eight-step instrument pipeline; no “six λ as headline.”
- Do not invent empirical residual rates; `qha`/`band` are illustrative slot patterns.
- Re-run: set `OUT` in the script to this directory (or `/workspace/cap-align-figure` on the box), then `python render_typed_introduction_figure.py`.

## Cross-links

- Claim lock: [`../../acl-paper-design.md`](../../acl-paper-design.md) §0–§1.2; [`../../acl-draft/innovation-proposals.md`](../../acl-draft/innovation-proposals.md)
- Manuscript: [`../../acl-draft/paper.md`](../../acl-draft/paper.md) v0.4+
- Design / proofs: [`../../typed-introduction.md`](../../typed-introduction.md); [`../../../research/introduction-operator.md`](../../../research/introduction-operator.md)
