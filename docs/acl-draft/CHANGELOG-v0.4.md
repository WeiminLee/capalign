# CHANGELOG — paper.md v0.4 / v0.4.1 / v0.4.2 / v0.4.3 / v0.4.4 (2026-10-18)

## Summary

Bulk rewrite of `paper.md` around locked **C1–C3** (coverage fork + principled refusal + \(K_H\)/\(t_v\); contract FI/Miss/\(t_v\)+destroy). Principle figure regenerated to match. No fabricated experimental numbers.

## Word count

| Version | Whitespace words (approx.) |
|---|---|
| v0.3 (pre-rewrite) | ~3209 |
| v0.4.1 | ~5400 |
| v0.4.2 | ~6276 |
| v0.4.3 | ~7770 |
| v0.4.4 (this) | ~7868 |

Target band for thick draft: 5–7k English words.

## Content changes vs v0.3

- **Title / Abstract / Intro** retargeted: lead with coverage fork (C1), not “six λ.”
- **Contributions** = locked C1–C3 from `acl-paper-design.md` / `innovation-proposals.md` DECIDED.
- **Related Work**: detect / reproduce / audit / SE cousins; positioning sentence wall vs SciCoQA / ReproAgent / MCP.
- **Method depth:** product slots; λ as partition-not-headline; coverage fork + `qha`/`band` table + single-face corollary; validity-gap worked sketch; algorithm sketch; \(I\) table with REFUSE; Props. 2–5 with proof intuitions; contract metrics.
- **Experiments:** EΔ / E1′ / E2′ / Testable / Fast protocol + TODO tables + Findings packet §4.7.
- **Discussion:** three instruments; residual→wrong edits; MCP as named \(W_{\mathrm{rap}}\); refusal-as-success; destroy-tests; expanded failure modes.
- **Limitations / Ethics / Conclusion** updated to C1–C3 honesty rules.
- **Appendix A caption** retargeted to C1–C3.

## Figure X (Phase 2)

Regenerated `docs/figures/typed-introduction/`:

- (a) Dual encode → product Id → λ [C1]
- (b) Coverage fork `qha`/`band` + empty intersection callout [C1]
- (c) \(I\) with REFUSE rows + \(K_H\)/\(t_v\) [C2]
- (d) Contract vs \(W_{\mathrm{rap}}\)/MCP / \(P_{\mathrm{aper}}\) + Effective/Testable/Fast [C3]

Files: `.pdf` / `.svg` / `.png` + `render_typed_introduction_figure.py` + figure-notes.

## Not done (still TODO)

- EΔ / E1′ human IRR / E2′ arm tables / destroy batch / Fast call counts
- ACL LaTeX packaging
- Fake empirics: none invented

## Backup

- `paper-v0.3-backup.md` — snapshot before v0.4 rewrite

## v0.4.2 (2026-10-18) — deep-research levers woven

Surgical weave only; **C1–C3 substance unchanged**; **no invented empirics / filled tables**.

### Weaves
- **§1.3:** orphan obligation / phantom entry framing; single-face impossibility when both nonempty.
- **§2.1:** Dude granularity asymmetry / over-reporting; Code Check reverse sweep + adversarial reject; Detect ≠ Introduce.
- **§2.3b (new):** Skill-V / SkillOps, PDD Evidence Chain, ReqToCode Traceables, install-manifest + MCP ABAC, deterministic gates + Ambient Persuasion, UTBoost / STING, ChopChop / CodeStruct — as *design constraints*, not our method.
- **§2.4:** +2 contrast rows (admission neighbors; weak suites / discovery≠authorize).
- **§2.5:** positioning refreshed (criterion provenance; typed install-or-refuse; fail-before/green/destroy-red).
- **§3.5:** closed typed edit API; criterion provenance (CLAIMCHECK-style); structured no-op refuse; register≠authorize.
- **§3.7:** TestPrism JSF; λ-indexed destroy mutants; test-invalid / survivor rate (UTBoost/STING); Harbor Faithful harness; Evidence Gate / Evidence Chain wording.
- **§5.3–5.4:** Ambient Persuasion (prompt refuse ≠ install gate); green alone insufficient.
- **§6:** +G1 crypto non-claim; +MCP UIR non-claim; +LLM-judge not sole FI/t_v oracle.
- **Appendix B/C:** version bump + v0.4.2 checklist items.

### Sources (read-only; not invented)
- `innovation-web-research-2026-10-18.md` (round 1)
- `innovation-web-research-round2-2026-10-18.md` (round 2)

### Still TODO
- EΔ / E1′ human IRR / E2′ arm tables / destroy batch / Fast call counts (unchanged)

## v0.4.3 (2026-10-18) — method/protocol details fleshed

Surgical expansion of Method + Experiments protocol + appendices. **C1–C3 substance unchanged**; **no invented empirics / filled tables**.

### Additions
- **§3.5.1:** Full deterministic pipeline (8 steps: independent inventory → Id merge → loci → κ only if s=e=1 → λ → project → I → accept); freeze of H/tests; no look-ahead label rewrite; Faithful vs measured green-rate / destroy-still-green.
- **§3.4:** Worked refusal sketches (*illustrative*): entry-sans-obligation `band`; procedure-conflict (SciCoQA-style L1 vs L2).
- **§3.7.1 (new):** Per-λ fail-before / post-edit / destroy table including refusal rows (success = H unchanged).
- **§4.3:** Annotation rules (what opens a row; Id undecidable → no merge; κ undecidable → 0; function wins over hand label; line-bounded loci; contamination control) + destroy-harness (witnesses outside patch surface; per-λ mutants).
- **§4.4 / §4.5:** Qualitative Faithful outcomes per arm; scoring columns contract-expected vs realized; per-λ breakdown mandatory for E2′.
- **Appendix D:** Obl/Ent; project(λ, host_has); t_v; coverage_paper + Faithful upper bound; pointer to introduction-operator.md.
- **Appendix E:** Introduce / test / must-not cheat-sheet (typed-introduction §7).
- **Abstract / Keywords:** paper-grounded checks; refusal as success; +criterion provenance; +structured refusal.
- **Ethics / Conclusion:** destroy harness isolation; LLM-judge not sole oracle; λ-indexed destroy-red wording.

### Sources (read-only; not invented)
- `docs/typed-introduction.md` §§5, 7, 9.1–9.4, 11
- `research/introduction-operator.md` §§1–5
- Prior web-research notes on box (design constraints only)

### Still TODO
- EΔ / E1′ human IRR / E2′ arm tables / destroy batch / Fast call counts (unchanged)

## v0.4.4 (2026-10-18) — status / gaps inventory (no empirics)

Discoverability bump only. **C1–C3 substance unchanged**; **no invented empirics / filled tables**.

### Additions
- Header **Status / gaps** block: story core written; ACL-blocking gaps = empty EΔ / human IRR / four-arm+\(π\) / destroy batch / ≥2 real pairs; links [`gaps-and-todos-v043.md`](gaps-and-todos-v043.md) + [`experiment-checklist-v043.md`](experiment-checklist-v043.md).
- §6 Limitations: one **Draft status** sentence pointing at the gaps doc (honesty bounds, not filled rates).
- Appendix B: rows for gaps doc + experiment checklist; version line → v0.4.4.
- Appendix C: v0.4.4 checklist item.
- New file: `docs/acl-draft/gaps-and-todos-v043.md` (Chinese: 阻断/削弱/可选；paper TODO 轴；工程 Phase + 拍板；已齐清单). Box copy: `/workspace/cap-align-figure/gaps-and-todos-v043.md`.

### Still TODO (unchanged substance)
- EΔ / E1′ human IRR / E2′ arm tables / destroy batch / Fast call counts
- Pair-2 selection, second annotator, and other Owen decisions (see gaps §C2 / checklist)
- ACL LaTeX packaging

