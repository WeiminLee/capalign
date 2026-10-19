# Research brief — Typed introduction of dual-encoded scientific work

**Working title:** *Typed Introduction: Residual Labels Decide Host Edits and
Fail-Before Tests for Dual-Encoded Scientific Work*

**Status:** research brief v0.4 (2026-10-18). **Paper claim (DECIDED):**
coverage fork + principled refusal + \(K_H\)/\(t_v\) — refined C1–C3 in
`docs/acl-paper-design.md` §1.2 / `docs/acl-draft/innovation-proposals.md`.
Prior shorthand \(\lambda\to I\) remains the operator; lead insight is the
*fork*, not “six labels.” Skill gap-table endpoint is **not** the manuscript
contribution. Canonical design: `docs/typed-introduction.md`. ACL draft:
`docs/acl-draft/paper.md` (claim lock only; body not bulk-rewritten).

---

## 1. Problem

Materials and other computational sciences accumulate deployed agents and
published works \(W=(\mathrm{paper},\mathrm{repo})\). Holding \(H\) and a new
\(W\), the user needs:

> Which products does my host already deliver, which residual **types** justify
> an edit, and which test must fail **before** that edit?

Three neighbouring questions are occupied:

1. **Detect** (SciCoQA): paper vs *its own* code.
2. **Reproduce / generate** (SA-Bench, LMR-BENCH, SciReplicate, ReproAgent,
   AutoMat, SkillFoundry): code or claim success from papers / resources.
3. **Intra-artifact audit** (BIV, SkillConsist, DCI): package vs itself.

**Research question.** Does dual encoding *fork* host coverage such that
product-typed \(\lambda\) selects introduction *and refusal* (incl. \(K_H\))
with countable advantages over wrap-repo / paper-only / write-directly on FI,
Miss, and \(t_v\)?

---

## 2. Method (contribution, not only instrument)

```
W_paper ─┐
         ├→ slots → u=(p,s,e,v_p,v_r,κ) → λ → project(·) → I(H,λ) + tests
W_repo  ─┤                                      │
H_host  ─┘                                      ├ vs W_rap / P_aper / write-directly / π
                                                └ Fast / Effective / Testable
```

- **Typed residual.** Unique \(\lambda\) per unit (Prop. 1).
- **Typed introduction \(I\).** Edits \(P_H\) / \(K_H\) by \(\lambda\); conflict
  unresolved; incongruent ignored.
- **Counting insights (Props. 2–5).** FI\((I)=0\); wrap-repo FI/Miss identities;
  \(t_v\) on validity-gap; \(\pi\) non-vacuous.
- **Assumptions outside theorems:** Id, \(\kappa\), Faithful.

Instrument workflow (inventory → IR → five-way gap → placement) may still run
for measurement; manuscript contributions are \(\lambda\), \(I\), and the
contract protocol.

---

## 3. Contributions (ACL) — **DECIDED** C1–C3

| # | Contribution | Assertion | Experiment |
|---|---|---|---|
| **C1** | **Coverage-fork residual:** product-Id merge; paper-face vs repo-face gaps can be disjoint; \(\lambda\) partitions residual | Fork is the insight; \(\lambda\) is the partition engine—not “six labels” as headline | **EΔ** TODO (Jaccard of faces); slots illustrated on mini-ref / phonopy (`qha`/`band`) |
| **C2** | **Typed \(I\) + principled refusal + \(K_H\):** refuse entry-sans-obl / conflict / incongruent; install \(t_v\) on validity-gap | Props. 2–5 (contract); Faithful separate; refusal = success | **E2′** TODO; obedience ≠ definition |
| **C3** | **Contract acceptance:** Effective (FI, Miss, \(t_v\)) + Testable (fail-before→destroy); Fast optional | Wrong scalars: detection recall / reproduction fidelity | **Testable** TODO; **Fast** TODO until measured; human **E1′** TODO |

**ZH one-liners.** C1: 双编码分叉宿主覆盖。C2: \(\lambda\) 决定编辑与原则性拒绝，有效性装 \(K_H\)。C3: FI/Miss/\(t_v\)+破坏测试验收。

**Defensive thesis.** Matching and detection are occupied. The claim is
host-relative **typed introduction with refusal**, with *coverage fork* as cause
of wrong edits under single-face wrap/paper policies—not a better SciCoQA detector.

---

## 4. Positioning

| Neighbour | Their question | Ours |
|---|---|---|
| SciCoQA | Detect paper–own-code discrepancies | \(\lambda\to I\) on deployed \(H\) |
| SA-Bench / LMR / SciReplicate / ReproAgent | Generate / reproduce | Edit contract; FI/Miss/\(t_v\) |
| SkillFoundry | Compile new skills | Type must choose the edit; untyped gen = baseline |
| BIV / SkillConsist / DCI | Package vs own implementation | Incoming \(W\) vs \(H\) |
| Skill Coverage | Trajectory vs skill’s own constraints | External \(W\); two projections |

Full table: `docs/acl-paper-design.md` §2; draft prose: `docs/acl-draft/paper.md` §2.

---

## 5. Evidence plan

Minimum submission pack (`acl-paper-design.md` §3): **EΔ**, **E1′** (human),
**E2′** (four arms + \(\pi\)), **Fast**, **Testable**. Legacy E1 same-model
\(\kappa\) and E3 intra-package drift are appendix / decomposition only.

Illustrative empty-host phonopy / mini-ref **definitional** counts exist in
`docs/typed-introduction.md` §11 — not multi-work results.

---

## 6. Risks & defense

- SciCoQA Main collision → nail detect vs introduce in Intro sentence 1 of RW.
- “Matching is not new” → grant; object is \(\lambda\to I\) on \(H\).
- Thin empirics → honest TODO tables; do not invent residual rates or human \(\kappa\).
- ARR M1 (LLM-only eval) → same-model pilot disclosed; human IRR required.
- Faithful → report obedience and destroy failures separately from Props. 2–4.
