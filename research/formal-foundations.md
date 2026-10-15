# Formal foundations

Strict definitions for the objects the paper measures. Grounded in capability IR
(`../references/capability-ir.md`) and test-adequacy theory (Zhu, Hall & May, ACM
CSUR 1997 — coverage ≠ adequacy). Notation is chosen to be checkable, not clever;
each definition ends with the falsifiable assertion the experiments target.

---

## 1. Capability IR as a typed corpus

Let `C` be a **capability** = `(id, τ, l, E, conf, src)` where

- `τ ∈ T` = `{compute, tool, workflow, data, interface, concept}` is the type,
- `l` is the natural-language description,
- `E = {e₁, …, eₖ}` is the **evidence set** — pointers into code/docs/artifacts
  (`path:line` or quote) that *justify* the capability,
- `conf ∈ {high, medium, low}` is the confidence of the extractor,
- `src ∈ {host-self-audit, reference-contrast, domain-inference}` is the
  **source kind** (who first claimed the gap).

A **capability surface** is a set `S = {C₁, …, Cₙ}` (one IR instance per inventoried
object). Two surfaces matter: the reference surface `R` (from repo/paper/blog) and
the host surface `H` (the agent's own).

**Evidence strength.** `w : E → [0,1]` grades each evidence pointer by kind
(module/CLI/doc-direct vs quote/inference); `confl(C) := maxₑ w(e)` is the
capability-level evidence strength. Discipline: `confl(C) = low` ⇒ a gap may never
be classified `missing` from `C` alone (it can only support `unknown`).

## 2. Alignment and the gap predicate

Define a relation `⪰` ("host covers reference") per capability pair
`(h ∈ H, r ∈ R)` by semantic match (description-logic notion of concept inclusion,
Paolucci-style: `exact / plugin / subsume / fail`), then **gate it with evidence**:

```
covers(h, r) := match(h, r) ∈ {exact, plugin}          ∧  confl-align(h, r) ≥ θ
```
where `confl-align` is the strength of the *comparison* evidence (there is a
grep-verified trace between the host artifact and the reference capability), and
`θ` is a gate threshold. This is **epistemic graded subsumption**: the semantic
verdict and the evidence threshold are a two-predicate conjunction.

Gap classes follow:
- `r` is **covered** iff `∃ h : covers(h, r)`,
- **partial** iff semantic match is `subsume` (host covers a strict subset) with
  evidence ≥ θ,
- **missing** iff no `h` matches *and* `confl(r) ≥ medium` (validated evidence),
- **unknown** iff no match and evidence is only `low`,
- **host-only** = `H ∖ R` (informational; reported, never scored against R).

**Assertion A (validity of gates).** For fixed θ, the classification is monotone in
evidence: adding validated evidence can turn `unknown → missing` but never
`missing → covered` without a host artifact; removing evidence acts inversely.
(Empirical check: IRR stability under evidence perturbation.)

## 3. coverage@reference

Let `R_med = {r ∈ R : confl(r) ≥ medium}` be the **reference capabilities this
survey may legitimately call gaps** (low-confidence entries excluded — they have no
standing in the count).

**Raw coverage** (what a table shows):
```
coverage_raw(R, H) = |{r ∈ R_med : r is covered}| / |R_med|
```

**Adequacy-gated coverage** (what a *demonstration* claims — Zhu 1997's
coverage ≠ adequacy): for each host capability `h` that covers some `r`, require a
**witness test** — a reproducible execution (fixture gold, `--describe` output,
determinism re-run) proving `h` actually performs `r`. Let `Prov(h)` be the set of
reference capabilities `h` demonstrably performs:
```
coverage@reference(R, H) := |{r ∈ R_med : ∃ h, r ∈ Prov(h)}| / |R_med|
```
`coverage_raw − coverage@reference ≥ 0`; the gap is exactly the **unproven claim
mass** of the host.

**Assertion B (anchor to task outcome).** coverage@reference predicts task success
on a suite derived from `R` better than (i) coverage_raw, (ii) host skill count,
(iii) no signal. Predicted shape: a gain plateau ("enoughness threshold") —
success rises with coverage@ref up to some `coverage* < 1`, then flattens.
(Empirical check: E2 before/after across a hull of host libraries.)

## 4. promise-drift rate

Per host surface, let `Claim(H)` = capabilities the host or its documents **declare**,
and `Verified(H)` = capabilities with `confl ≥ medium` **and** a witness test.
```
drift(H) := |Claim(H) − Verified(H)| / |Claim(H)|      (declared but unproven)
fabricated(H) := |{c ∈ Claim(H) : E(c) = ∅}| / |Claim(H)|  (no evidence at all)
```
`fabricated` is the strictest tier — the claim has no pointer to any artifact
(BIV's 80% is a superset; we decompose it). Decompose `drift` **by source**:
`drift(H) = Σ_{s ∈ src} share(s) · drift_s(H)` where `share(s)` is the fraction of
claims born from source `s`.

**Assertion C (predictive drift).** `drift_s` is systematically ordered by source —
starting hypothesis: `drift(paper-methods) > drift(blog-recipes) > drift(repo-docs)` —
and `drift(H)` is predictable from cheap surface features (skill count, description
length, evidence density, update recency) with AUROC ≥ threshold on held-out
libraries. (Empirical check: E1/E3 on public skill libraries + materials assets.)

## 5. Self-referential alignment (calibration, not assumption)

All prior mechanisms assume an **external** auditor. capalign audits the host with
the host. Define the self-audit bias
```
bias := drift(H_self-reported) − drift(H_externally-verified)
```
and the confidence calibration
```
cal := P(conf-label = verified | label assigned)
```
**Assertion D (systematic, calibratable bias).** `bias ≥ 0` (self-reports
over-claim) but is stable across surface types and can be corrected per-source;
`cal` is monotone in `confl`. If self-audit is systematically *uncalibratable*
(bias varies without recoverable structure), the closed-loop governance claim
weakens to external-audit-only — a falsifiable boundary we state up front.
(Empirical check: E4, two runs on identical input, one self-referential one gold-fed.)

## 6. Metrics and the governance loop

The closed loop is a measurement sequence on a *single evolving surface* `S(t)`:
```
re-inventory → align(S(t), R) → drift(S(t)) → assemble per gap → S(t+1)
```
Two governance signals:
- **coverage@reference(S(t))** — should rise after assembly (Assertion B shape);
- **drift(S(t))** — should fall after verified assembly and rise again when the
  environment (reference or library) moves — **stale-skill recall**: re-alignment
  flags capabilities whose witness test broke after dependency/API drift.

**Assertion E (stale recall).** Re-alignment detects mechanical drift (runner/output
contract changes) with recall > version-diff-only baselines, i.e. the *validation*
step adds detection power beyond diffing. (Empirical check: E3 longitudinal on git
history + tool-version history.)

---

## Open formalism (stated, not over-claimed)

Alignment as a **Galois connection** between the reference lattice and the host
lattice is an organizing view (coverage@ref = extent-inclusion ratio), not a theorem
we need — flagged here so the paper does not overstate. The three falsifiable
assertions above (B, C, D) carry the empirical weight; A and E carry method
soundness. If any fails, the framework's boundary shifts, which is the point of
writing them down.