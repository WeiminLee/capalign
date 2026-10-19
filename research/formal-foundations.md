# Formal foundations

Strict definitions for the objects the paper measures. Grounded in capability IR
(`../references/capability-ir.md`) and test-adequacy theory (Zhu, Hall & May, ACM
CSUR 1997 — coverage ≠ adequacy). Notation is chosen to be checkable, not clever;
each definition ends with the falsifiable assertion the experiments target.

Identity of the paper (2026-10-16): a published scientific work is a dual-encoded
specification; host-relative alignment is a decision procedure; coverage is
reference-conditioned. Matching vocabulary (Paolucci) and evidence gates are
parts of the procedure, not contributions. Galois / “capability lattice” views
stay in the open-formalism note at the end.

---

## 0. Scientific work as a dual-encoded specification

A **scientific work** is a pair \(W = (W_{\mathrm{paper}}, W_{\mathrm{repo}})\),
where each component is a capability surface (defined in §1):

- \(W_{\mathrm{paper}}\) is extracted from Methods / claimed products / hard
  software dependencies;
- \(W_{\mathrm{repo}}\) is extracted from CLI entry points, top-level modules,
  documented features, and dependency fingerprints.

A third encoding (blog/recipe) exists in the instrument; the paper pins paper
and repo. **Identity** of a capability across encodings is the same `covers`
predicate as §2 (semantic match ∧ evidence threshold). The **residual** is
```
Δ(W) := (W_paper \ W_repo,  W_repo \ W_paper)
```
taken after identity has been applied (exact/plugin count as the same cell).

**Assertion C1 (non-empty residual).** For a paired computational-science work,
\(\Delta(W)\) is non-empty and classifiable into method-obligation-only vs
interface-only cells. (Empirical check: EΔ, phonopy Methods vs phonopy repo.)

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
`θ` is a gate threshold. The semantic verdict and the evidence threshold are a
two-predicate conjunction (Paolucci-style match gated by Zhu-style evidence;
the name is a description, not a contribution). The same predicate is used
whether \(r\) was drawn from \(W_{\mathrm{paper}}\) or \(W_{\mathrm{repo}}\).

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

When the reference is a scientific work \(W\), coverage is **reference-conditioned**:
```
coverage_paper(H, W) := coverage@reference(W_paper, H)
coverage_repo(H, W)  := coverage@reference(W_repo,  H)
```
The two numbers are not assumed equal.

**Assertion B (anchor to task outcome).** coverage@reference predicts task success
on a suite derived from the chosen projection better than (i) coverage_raw,
(ii) host skill count, (iii) no signal. Predicted shape: a gain plateau
("enoughness threshold") — success rises with coverage@ref up to some
`coverage* < 1`, then flattens. (Empirical check: E2.)

**Assertion C3 (fork).** `coverage_paper(H,W)` and `coverage_repo(H,W)` diverge
on real paired works; assembling along the paper spec vs the repo spec yields
different task-gain shapes. (Empirical check: E2 split by projection; EΔ
supplies the residual that predicts the fork.)

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

**Assertion C-intra (predictive intra-package drift).** Demoted: BIV / DCI /
SKILLSCOPE already measure declaration–implementation drift at scale. We may
still decompose `drift` by source as an appendix signal; it is not a headline
contribution. Starting hypothesis if reported: `drift(paper-methods) > drift(blog-recipes) > drift(repo-docs)`.

## 5. Self-referential alignment (calibration, not assumption)

All prior mechanisms assume an **external** auditor. cap-align audits the host with
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
re-inventory → align(S(t), R) → drift(S(t)) → I(S(t)) → S(t+1)
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
lattice is an organizing view (coverage@ref = extent-inclusion ratio), not a
theorem and not a contribution. “Epistemic graded subsumption” is a description
of the two-predicate gate in §2, not an innovation name.

Headline assertions: **C1** (residual, §0), **A** (gates, §2), **C2** via E1 IRR,
**B / C3** (reference-conditioned coverage, §3), **D** (self-audit, §5).
Intra-package drift (old C) and stale recall (E) are follow-ons. If C1 fails
(\(\Delta(W)=\emptyset\) on paired works), dual-encoding collapses to a product
feature and the paper identity weakens to C2 alone.

The introduction step above is the operator \(I\) in `introduction-operator.md`:
label \(\lambda\) selects the edit and the pre/post test. Propositions there
fix false-introduction and missed-obligation counts for \(I\) versus wrapping
the repo. They do not prove that a generated patch implements the edit.