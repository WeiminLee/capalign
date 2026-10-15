# E1 IRR — first judged corpus (P1 phonopy↔MatDiscovery, P2 mini-paper↔mini-host)

Run: 2026-10-15. Corpus seed: `research/runs/e1/corpus-design.md` (6 pairs
planned; P1/P2 judged first). Judges: 3 isolated agent judges per pair
(alpha/beta/gamma) — same model, independent contexts, no gold access, no
prior-judgment access. Gold: `research/runs/e1/draft-gold-01` / `draft-gold-02`
(main-agent drafted, judge-validated in this run).

## Agreement numbers

| metric | P1 (13 ref caps) | P2 (9 ref caps) |
|---|---|---|
| judge pairwise class agreement | 35/39 = 0.897 | 27/27 = 1.000 |
| majority-vs-gold class | 11/13 = 0.846 | 9/9 = 1.000 |
| **Fleiss κ (class)** | **0.853** | **1.000** |
| judge pairwise source (gap rows) | 25/27 = 0.926 | — (see note) |
| **Fleiss κ (source, 9 gap rows)** | **≈ 0.0** (marginal-imbalance collapse) | 1.000 / trivial |

Pass bar (experiments.md §E1): κ ≥ 0.6 → **P1 class and P2 class pass**. Source
κ on P1 is uninterpretable as-is — see statistics note. P2 source is trivially
1.0 (all gap rows identical across judges).

### Statistics note — why P1 source "κ≈0" while raw agreement is 92.6%
27 gap-row labels: 26 `reference-contrast`, 1 `host-self-audit`. With such
skewed marginals, chance agreement Pe ≈ 0.928 ≈ observed Pbar → κ collapses
(Fleiss-style coefficient paradox, same family as Cohen's kappa).
Cite raw agreement per-class instead: **source raw agreement 92.6%**,
disagreement is 2 rows out of 27 (below). The paper must report both κ and raw
agreement, and pre-specify which; this corpus pre-specifies raw agreement for
the ≥2-source cells and κ for class.

## P1 per-capability verdicts (gold → per-judge)

| ref cap | gold | jα | jβ | jγ | resolution |
|---|---|---|---|---|---|
| fc-assembly | missing | partial | equivalent | equivalent | **revised** → partial/medium (evidence-driven, see log) |
| mode-gruneisen | partial | partial | partial | partial | holds |
| qha-thermodynamics | partial/host-self-audit | partial/rc | partial/rc | partial/rc | **class holds; source holds (gold), judged rc — evidence asymmetry, see note** |
| nac-lo-to | missing | missing | missing | missing | holds |
| electronic-thermal | missing/rc | missing/rc | missing/**hsa** | missing/rc | holds (rc); jβ's hsa recorded, rejected |
| irreps-symmetry | missing | missing | missing | missing | holds |
| mlp-sscha | missing | missing | missing | missing | holds |
| dynamic-structure-factor | missing | missing | missing | missing | holds |
| site-mixture-vca | unknown | unknown | unknown | unknown | holds |
| phonon-dos | equivalent | equivalent | equivalent | equivalent | holds |
| band-structure | equivalent | partial | equivalent | partial | **recorded disagreement** (partial/equiv adjacency) |
| group-velocity | equivalent | equivalent | equivalent | equivalent | holds |
| thermal-properties-harmonic | equivalent | equivalent | equivalent | equivalent | holds |

### Disagreement analysis (the E1 value)

1. **fc-assembly — gold revised missing → partial/medium.** Judges produced new
   *positive* evidence the gold drafter had not found: the host's BTE route
   executes real FC assembly — `bte_controller core.py:490-504`
   (displacement → forces → symprec symmetrization → fc2/fc3 persisted),
   and `simple_mattersim_qha_muxi.py:529-539` produces+such symmetrizes on the
   QHA route. Gold's `missing` rested on "no standalone FORCE_CONSTANTS
   deliverable in mat-phonon's output list" — true but insufficient: the
   capability is *performed*, only the standalone delivery form is absent →
   that is a **strict subset**, i.e. `partial`, not absent. (2/3 judges went
   as far as `equivalent`; the drafter takes `partial` because "user-reachable
   deliverable" is still missing — granularity rule #1. Logged.)

2. **qha-thermodynamics source — gold `host-self-audit` held over 3/3 `rc`.** The
   judges scanned host AUDIT/SKILL-DESIGN §9 and found "no open admitted gap"
   because α's tool landed 2026-10-15 (`mat_thermal_expansion`), which they read
   as closure. Direct evidence check: `docs/SKILL-DESIGN.md:495` explicitly
   documents the admission — "α(T,P) 曾声称了但没实现（审计 §1.4 …2026-10-15 已
   落地）… 不产 thermal_expansion 表" — i.e. the host *itself* recorded the
   deficiency, *and* records that the runner still has no table (α is derived
   local interior-points-only). Partial repair ≠ gap closed. Gold's source kind
   stands on positive documentary evidence; the judges' `rc` is a
   search-miss negative. Logged as a calibration case for E4 (self-audit
   mapping when the host partially repaired its own admission).

3. **band-structure — equivalent vs partial (2/3 partial).** Judges: host ships
   `band.yaml` by default (dispersion is a default property) but exposes no
   user-settable BAND path and no bandplot renderer → "路径选择" belongs to the
   capability semantics → strict subset → partial. Gold: default band delivery
   is the capability. This is the expected partial/equiv adjacency — **recorded,
   not resolved**; it is the kind of cell E1's confusion report is for.

4. **electronic-thermal — jβ: host-self-audit.** jβ read
   `thermal-router.md:31` "Ask whether an electronic contribution is
   required…" as a self-admission. Drafter: an *ask-the-user* routing question
   is not a declaration of a gap; the host never admits lacking the capability
   (no electronic-thermal mention in any audit). Rejected, logged.

## P2 — 9/9 unanimity (κ=1.0)

All six missing rows, both equivalent rows, and the unknown row agree exactly
across judges and gold. The fixture (AUDIT.md self-admitting the five product
gaps; heat-flow as BTE→κ solver; single-mention tetrahedron) resolves cleanly
under the codified rules. One convention drift worth fixing: non-gap rows got
`source_kind` values `reference-contrast` (jα/jγ) vs `not-a-gap` (jβ) — the
schema should define a nominal value for covered rows so source-agreement on
the *gap* rows is what's counted (it was: gap-row source agreement is 1.0).

## Corrupting-context audit

Judges were forbidden gold, `gold/`, `runs/`, `e4/`, draft-gold files, and
methodology §3. Disclosures: jα and jγ each reported that an initial whole-file
`Read` of methodology.md pulled §3 into context; both self-reported the section
was not used as evidence. jβ correctly line-bounded reads to §0–2/§4. The two
disclosures are recorded as contamination risk (small: every classification is
supported by claimed host-side verification), and the paper's method must make
line-bounded reads the rule, not the exception.

## Next

- P3 (mini-ref↔mini-host) judges: replication anchor — reuse the same judge
  protocol; it tests the *same* gold that the E1 pilot recorded (5/6 class,
  2/6 source → expect F1/F2-fixed agreement now).
- P4 (zvec-grep ↔ memmy-agent, neutral domain) + P5 (hindsight paper) + P6
  (blog): build gold per pair (entry-point pinning per corpus-design §6), then
  judge. Needs a second human/model judge for the real κ claim; the current
  three are same-model lower-bound signal.
- Promote P1/P2 (post-revision) into `tests/fixtures/gold/` per corpus-design §5
  once P3 replicates.