# Evidence plan (E1–E4 + EΔ)

How the paper's claims are supported. Named in `brief.md` §5 and `docs/paper-core.md`
§7. All experiments run **through the skill's own workflow** (no custom harness).

Identity mapping (2026-10-16):

| Experiment | Serves |
|---|---|
| E1 (repo arm + paper arm) | C2 — same predicate, two encodings |
| **EΔ** (paper surface ⋈ repo surface of one work) | C1 / C3 lifeline |
| E2 split by projection | C3 — assembly along paper spec vs repo spec |
| E3 | library-level `coverage(H,W)`; intra-package drift demoted |
| E4 | C2 — self-report vs incoming \(W\) |

## E1 — Inter-rater reliability of gap/source classification

Question: is the classification (five gaps × three sources) reproducible across
human/agent judges, or does it depend on the operator?

- Corpus: ≥ 6 reference-host pairs spanning all three reference kinds
  (repo × 3, paper × 2, blog × 1) and ≥ 2 domains (materials, one neutral domain to
  prove cross-domain generality).
- Raters: ≥ 2 human judges + ≥ 2 agent judges (different models); each produces a gap
  table for the same pairs.
- Metric: Cohen/Fleiss κ per gap class; κ per source kind; disagreement analysis
  (which classes confuse — expected: `partial` vs `missing` adjacency, `unknown` vs
  missing-gating).
- Pass bar: κ ≥ 0.6 overall; the confusion report is a paper deliverable even if
  lower (it documents the method's honest boundaries).
- Assets: gold fixtures in `tests/fixtures/` are the seed; expand with 3 real
  reference-host pairs (phonopy→MatDiscovery among them).

## EΔ — Cross-modal residual of a paired scientific work

Question: for a paper and its companion repository, is \(W_{\mathrm{paper}}\) the
same capability surface as \(W_{\mathrm{repo}}\)?

- Corpus: at least one paired computational-science work. Seed: phonopy Methods
  (or the phonopy paper used as the methods source) vs the phonopy repository
  already inventoried in the MatDiscovery run. A second pair (different code
  family) is required before claiming generality.
- Protocol: inventory each encoding independently (no peeking), normalize to the
  same IR, apply the identity predicate, report \(\Delta(W)\) as two residual
  sets (paper-only method obligations vs repo-only interfaces).
- Metric: Jaccard of the two surfaces after identity; residual size; residual
  class mix. Pass bar: residual non-empty and not explainable as inventory
  undershoot (false-gap protocol from methodology §3 applies).
- Why first: if \(\Delta(W)=\emptyset\), dual-encoding is a product feature and
  C1/C3 collapse.

## E2 — Before/after: does report-driven assembly beat baselines?

Question: does acting on the alignment report's recommendations improve task-level
capability more than random or retrieval-based augmentation?

- Protocol: take a host library (start with MatDiscovery's 37 skills). Run alignment
  twice against the same work \(W\): once with \(W_{\mathrm{repo}}\) (phonopy
  repo), once with \(W_{\mathrm{paper}}\) (phonopy Methods). Partition
  `missing`/`partial` recommendations into arms: (a) assemble per the **repo**
  report, (a′) assemble per the **paper** report, (b) assemble randomly-selected
  equivalent effort, (c) no assembly (control). C3 predicts (a) and (a′) differ
  in *which* tasks move, not only in mean gain.
- Evaluation: a task suite derived from the reference's own documented capabilities
  (phonopy's docs feature surface); measure task success per arm.
- Anchor: SoK's curated +16.2pp over self-generated skills gives the comparison scale.
- Confounder control: assemble effort (tokens/steps) equalized across arms; report
  both raw gain and gain-per-effort.

## E3 — coverage@reference and promise-drift as library-level metrics

Question: do the proposed metrics behave like useful governance signals over evolving
libraries?

- Define (initial formalism in `brief.md` §3#4): `coverage@reference` = share of
  validated reference capabilities satisfied by the host (evidence-gated, adequacy
  not raw coverage); `promise-drift rate` = |claimed − validated| / |claimed|.
- Study 1 (static): across ≥ 3 host libraries → coverage distribution; correlate with
  task success on shared tasks (does higher coverage@ref predict better task outcome?).
- Study 2 (longitudinal): snapshot an evolving library (MatDiscovery's own git history
  or a public skill repo) at ≥ 5 commits; show (a) coverage@ref changing as skills are
  added/removed, (b) promise-drift appearing when a skill's runner/output contract
  changes (stale-skill recall: does re-alignment flag the drifted skills?).
- Pass bar (contribution #4): demonstrate ≥ 1 drifted capability caught by re-alignment
  that version-diff alone would miss.

## E4 — Self-referential alignment reliability

Question: when an agent audits its own capability surface, how trustworthy is the
self-report? (The theoretical gap from L2/`brief.md`: all prior mechanisms assume an
external auditor.)

- Protocol: run alignment twice on the host — once self-referential (skill reads its
  own surface), once with the surface supplied by an external corpus (gold). Measure
  gap-table agreement; record self-reported evidence entries that fail validation.
- Metric: calibration of `confidence` labels vs actual validation hit-rate; systematic
  self-audit biases (over-claiming on one's own skills vs the reference).
- Deliverable: first empirical calibration curve for self-referential capability
  auditing; feeds back into the evidence-gating rules (when is `unknown` safer than
  `missing`?).

## Shared requirements

- Determinism: every experiment run records the run ID, model, inputs; same-input
  re-run must reproduce the gap table (Layer-1 check #8).
- Fixture/gold logging: any adaptation of gold during experiments is logged in the
  gold `log:` array (`evaluation.md` Layer 2), never silently edited.
- The phonopy↔MatDiscovery run doubles as E1 seed, E2 arm-(a) source, and the paper's
  case study narrative (19 gaps, three false-gap catches documented in
  `references/methodology.md` §3).