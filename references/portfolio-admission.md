# Portfolio admission, fusion, and lifecycle

Read this after the row-level card exists (`introduction-card.md`). A row-level
`install` can be locally correct and still make the host worse: it can compete with
an existing entry for the same routing decision, duplicate an entry, or push the
library past its selection budget. This reference adds the **set-level** check.
It is advice only.

## 1. Scope

Run this step only when at least one card is `install`. A run with only `refuse`
cards still emits an empty `portfolio` block (`host_entries: []`, `probes: []`,
`set_test` with empty arrays, `lifecycle: []`, zeroed metrics), but checks 19–21
are not applicable.

This reference classifies, declares probes, and writes a plan. It never edits the
host, merges files, installs anything, changes a router, or executes a probe. The
set test is reasoned in the report; it is not run against a live host. Whether to
build the plan is the host's and its human's decision.

## 2. Host portfolio

The host is a portfolio, not a bag of files:

\[
H=(P_H,K_H,\Sigma_H,\rho_H,\beta_H),
\]

where \(P_H\) is the set of entries, \(K_H\) the checks/obligations they carry,
\(\Sigma_H\) the selection policy (how the host chooses an entry), \(\rho_H\) the
routing surface (descriptions and route probes), and \(\beta_H\) the context
budget.

Each entry — existing or proposed — is a declared record:

\[
\sigma=(Q,P,\mathrm{Pre},\mathrm{Post},R,\mathrm{Proc},K,\mathrm{Prov}),
\]

- \(Q\): the question that selects this entry.
- \(P\): the products it delivers.
- \(\mathrm{Pre}\), \(\mathrm{Post}\): preconditions and postconditions.
- \(R\): a **named** validity regime (`{claim, tags}`), not free prose.
- \(\mathrm{Proc}\): the procedure; it includes the pre/post contract.
- \(K\): checks and invalidation conditions.
- \(\mathrm{Prov}\): provenance (where each field was evidenced).

Every field is declared. Do not infer products or regimes from a description; if
the host does not declare them, mark them `unknown` and do not manufacture a
relation. Freeze the host entries, descriptions, route probes, and budget before
classifying any candidate.

## 3. Relation taxonomy

The twelve declared witnesses are booleans:

`same_product`, `same_procedure`, `same_regime`, `regime_overlap`,
`regime_subset`, `checks_missing`, `question_overlap`, `products_superset`,
`checks_superset`, `regime_superset`, `products_subset`, `checks_subset`.

| Relation | Necessary and sufficient predicate | Meaning |
|---|---|---|
| `covered` | `same_product ∧ same_procedure ∧ regime_subset ∧ ¬checks_missing` | the existing entry already covers the candidate |
| `partial` | `same_product ∧ same_procedure ∧ (¬same_regime ∨ checks_missing)` | same procedure, different regime or missing checks |
| `duplicate` | `same_product ∧ same_procedure ∧ same_regime ∧ ¬checks_missing` | a true duplicate; mergeable |
| `variant` | `same_product ∧ ¬same_procedure ∧ ¬regime_overlap` | same product, different procedure, disjoint regimes |
| `hard-conflict` | `same_product ∧ ¬same_procedure ∧ regime_overlap` | same product, different procedure, overlapping regimes |
| `subsumes` | `products_superset ∧ checks_superset ∧ regime_superset` | the candidate is strictly stronger than the entry |
| `subsumed` | `products_subset ∧ checks_subset ∧ regime_subset` | the candidate is strictly contained by the entry |
| `adjacent` | `¬same_product ∧ question_overlap` | different product, overlapping question |
| `unrelated` | `¬same_product ∧ ¬question_overlap` | no product or question overlap |

`subsumed` is the inverse of `subsumes`; it is not inferred from description
length. `same_procedure` includes \(\mathrm{Pre}/\mathrm{Post}\): an incompatible
precondition makes the procedure different, so the pair falls to
`variant`/`hard-conflict`, not `partial`.

Fusion `covered` is **not** the gap table's `equivalent`. The gap table keeps its
six classes (`equivalent | partial | missing | agent-competence | host-only |
unknown`). `equivalent` is a host-relative judgment about the reference question;
`covered` is a relation between two entries and licenses `no-op` in the plan.

A relation is accepted when its declared predicate is true. The checker does not
require the relation to be unique: when two predicates both fit, record the
declared evidence and the more conservative action; never merge or retire on an
ambiguous pair.

## 4. Decision tree

Compute the §3 witnesses first; this tree is the reading order for those
witnesses, not a second rule. The first hit ends the classification:

1. **Is one side strictly stronger?** Products, checks, and regime are all
   supersets, and at least one is a proper superset.
   - Candidate stronger → `subsumes` (`upgrade`); existing entry stronger →
     `subsumed` (`no-op`).
2. **Same product?**
   - No → does the question overlap? Yes → `adjacent`; no → `unrelated`.
3. **Same procedure (including pre/post)?**
   - No → do the regimes overlap? Yes → `hard-conflict`; no → `variant`.
4. **Same regime and no missing check?**
   - Yes → `duplicate` (`merge`).
5. **Regime subset and no missing check?**
   - Yes → `covered` (`no-op`).
6. **Otherwise** → `partial` (`add_validator` / `upgrade` / `downgrade` /
   `split`), or `hard-conflict` when the pre/post conditions cannot both hold.

Description similarity is not a branch. It is recorded as a shadowing signal and
handled by probes and `demote`/`split`.

## 5. Action mapping

Only these pairs are allowed:

| Relation | Allowed actions |
|---|---|
| `covered` | `no-op` |
| `partial` | `add_validator`, `upgrade`, `downgrade`, `split` |
| `duplicate` | `merge` |
| `variant` | `split`, `demote` |
| `hard-conflict` | `quarantine`, `refuse` |
| `subsumes` | `upgrade` |
| `subsumed` | `no-op` |
| `adjacent` | `extend`, `new-entry` |
| `unrelated` | `new-entry`, `no-op` |

`merge` is only for `duplicate`. A description-overlap pair is `adjacent` or
`unrelated` (or `variant`/`hard-conflict`), never `duplicate` unless the declared
product, procedure, and regime witnesses are all true.

For reading the graph, the nine relations collapse to four edge types:
`dependency` (adjacent with a stated prerequisite), `compatibility`
(covered/partial/subsumed), `redundancy` (duplicate), and `alternative`
(variant/subsumes). Only `redundancy` authorizes `merge`; the edge is a
classification, not permission to delete.

When the only gap is a missing check, prefer `add_validator` over `merge` or
`split`. In the ecosystem-governance evidence, validator insertion was the most
valuable single maintenance action, while merge or repair alone had limited
effect and paid off mainly in combination. cap-align keeps the action order:
repair the check first, merge only true redundancy.

The full action enum is
`no-op | bind | author | extend | add_validator | merge | demote | upgrade | downgrade | retire | quarantine | refuse | split | new-entry`.
Deferral is not an action. "Defer admission" means no lifecycle action for this
card; record it in Unresolved.

## 6. Merge semantics

Merge is admissible only for `duplicate`. A duplicate pair is a redundant
representation, so merge is **structural compression**, not a measured causal
claim. The evidence below protects the compression; it does not establish that
the merged library is better.

### 6.1 Structural conditions

- **Products:** union of both entries' products. No unique product is lost.
- **Checks:** union of both checks. No unique check is lost.
- **Regime:** intersection. The merged entry claims only the regime both claim.
- **Provenance:** union. Both evidence trails survive.
- **Test contracts:** both entries' contracts are retained; the merged entry must
  be able to replay both fail-before/pass-after/destroy sequences.
- **Description:** rewrites to one question, not a concatenation. Re-run both
  route probes after the rewrite.
- **Coverage and interference:** entry count decreases; portfolio coverage does
  not decrease; interference does not increase. If either fails, do not merge.
- **Rollback:** record the exact source entries, descriptions, probes, and checks
  to restore.

If the union cannot cover both live obligations, use `split` or `demote` instead.
Merge never adjudicates a procedure conflict.

### 6.2 Evidence ladder: every deletion has one witness

A card-level merge carries a `portfolio.merge` block. The source entry is itself
a deletion: `removed_units` must contain `entry:<card_id>`. Every unit in
`removed_units` carries **exactly one** witness:

| Kind | Witness | Use |
|---|---|---|
| `W1` | literal inclusion: the unit appears verbatim in the merged entry or both sources | preferred; reversible |
| `W2` | coverage witness: a deterministic content-word/coverage gate shows the merged unit covers the source unit | allowed when W1 is impossible |
| `W3` | restricted entailment: a frozen checker (temperature 0) says the unit follows | last resort |

`W3` is forbidden for obligations, output fields, and any unit carrying a
`prohibition`, `exemption`, or `output` marker. Those are the units whose silent
loss changes behavior, and entailment is the weakest evidence about them. A
removed unit with no witness vetoes the merge regardless of token savings; a
second witness on the same unit is also an error (one deletion, one reason).

Anything that cannot be parsed or witnessed is preserved verbatim in
`locked_residual` (`unit`, `reason`, `verbatim`). A unit cannot be both removed
and locked. Missing `reason` or missing verbatim text is a violation. The
failure mode is "compressed too little", never "silently deleted".

### 6.3 Hard coverage: no surface unit disappears

Each entry may declare a `surface` object with five unit classes:

```
triggers | workflow_edges | tool_requirements | obligations | output_fields
```

For a merge, the union of both sides' surface units must equal
`coverage ∪ removed_units ∪ locked_residual`. Every unit not deleted with a
witness and not locked verbatim must be declared covered. `coverage` may not
invent units that neither side declares. This catches the failure that
description-level similarity misses: the union of products and checks can look
complete while a trigger, workflow edge, tool requirement, obligation, or output
field has silently vanished.

### 6.4 Commit gate: both sides' probes replay before the merge lands

`recall_probes` must contain every retained probe owned by the target, every
probe the candidate declares in `retention_probes`, and the candidate's own
`deliver`/`validity` probes. Each recall probe must be
declared in the portfolio probe list, and an observed `passed: false` vetoes the
merge. The gate is fail-closed: a missing probe is a failure, not a skip.

`evidence_level` is one of:

- `constructive` — the structural conditions above establish the merge; this is
  the default and the only honest label for a rule-based merge;
- `model` — a model judged the merge; record the judge and prompt in `evidence`;
- `statistical` — only with `causal_evidence = {design: randomized, n_trials: N>0}`.
  A merge supported only by similarity scores or pre/post averages is not
  statistical evidence and must not be labeled as such.

### 6.5 Interaction check

`interaction.beta` is the declared pairwise interaction estimate for the merged
pair. `beta < -0.15` requires `checked: true` plus non-empty `evidence` from an
extended regression suite; otherwise the merge is refused. A declared `beta: 0`
means "no estimate", not "independence proven"; sparse co-occurrence must not be
reported as a zero interaction.

### 6.6 Never inflate

`surface_tokens_after` must not exceed `surface_tokens_before`. If the union
costs more surface than the two entries cost separately, merge is not the right
operation: keep both entries, `split`, or `demote`. The fallback is a verbatim
no-op, not a larger merged entry. Both counts are declared, like probe results;
the static checker checks the relation between them, not the measurement.

### 6.7 Rollback

The card records `rollback` with the exact source entries, descriptions, probes,
and checks. Rollback is a precondition for admitting the merge, not a post-hoc
convenience. A lifecycle `merge` uses the same block shape; the static checker
enforces the block on card-level merges and checks lifecycle reachability,
remapping, duplicate records, and both test contracts separately.

## 7. Lifecycle actions

| Action | Trigger | Evidence | Test |
|---|---|---|---|
| `no-op` | covered/subsumed, or a refuse card | relation witnesses | retained probes unchanged |
| `bind` | both sides aligned, product new to host | paper product + repo entry | fail-before → pass-after → destroy |
| `author` | obligation without an entry | paper steps | same; no fabricated entry id |
| `extend` | both sides aligned, same question as an entry | routing probes both ways | old question still routes; neighbour does not absorb the new one |
| `add_validator` | validity gap / missing check | the one-sided invalidation sentence | violating input fails |
| `merge` | duplicate | merge block: witness per removed unit, hard coverage, locked residual, both entries' recall probes, contracts, provenance | both old probes pass; entry count down; no surface unit dropped; surface tokens not up |
| `demote` | entry still useful but shadowing risk high | overlap with the owner + probe margin | default surface shrinks; explicit invocation still works |
| `upgrade` | candidate strictly stronger (`subsumes`) | old + new contracts | new probe passes; old probe passes or is explicitly retired |
| `downgrade` | new evidence narrows the entry's regime | new invalidation sentence + old probe | old probe passes inside the narrowed regime; outside it fails or routes to fallback |
| `split` | same product, parallel regimes or procedures | regime witnesses + one probe per branch | each branch routes inside its regime; no default tie |
| `new-entry` | adjacent or unrelated, and the host needs the product | product + placement | route probe for the new entry; old entries unchanged |
| `retire` | no live obligation and no retained probe depends on the entry | provenance + last-obligation record | removal changes no retained probe |
| `quarantine` | hard conflict or validity unassessed | conflict record | not selectable by default; no silent side chosen |
| `refuse` | entry without obligation | the source's silence | host unchanged |

A lifecycle entry records `action`, `target`, `sources`, `reason`, `probes`, and
`rollback`. `upgrade` removes the target, adds the source, and remaps retained
probes owned by the target to the source; the source must be a product/check/regime
superset. `merge` replaces its sources with one merged entry and remaps their
retained probes. `retire` removes the target only when it delivers no live
obligation and owns no retained probe. The tool checks these statically; observed
probe results belong in the report.

## 8. Probes and the set test

A probe is `(qid, text, owner, expected, kind)` with
`kind ∈ {route, deliver, validity}`:

- `route`: the host still chooses the owner for this question.
- `deliver`: the owner still emits the expected product.
- `validity`: an invalid input is still rejected.

Declare every probe **before** looking at any outcome. A probe invented after a
failure is not evidence.

The set test has five inputs:

1. retained probes (with margin \(m\));
2. new probes for the admitted candidates;
3. \(\kappa_H\) conflicts between candidates and entries;
4. the context budget \(\beta_H\);
5. reachability over live obligations.

For each retained probe, the joint margin is

\[
m(q,\Sigma_{\text{accepted}})=m(q)+\sum_{c\in\Sigma_{\text{accepted}}}
\delta_c(q),
\]

where \(\delta_c(q)\) is the candidate's declared `probe_effects[qid]`. A negative
margin is a failure. Candidates in `plan.demoted` are out of the default router and
do not contribute their delta. The candidate record is the only source of deltas;
the report records the resulting contributions.

Two individually safe candidates can break a probe jointly:
\(0.3-0.2-0.2=-0.1\). Row-wise safety is not closed under union. Declare both
probes before seeing that result.

Budget: if `context_tokens_after > limit`, at least one entry must be in
`plan.demoted`, and the demoted entry must no longer count toward the default
surface. A demoted entry is not a removed entry; explicit invocation still works.

## 9. Reachability

Let \(O\) be the union of obligations of all live works. Draw an edge
\(o\to\sigma\) when entry \(\sigma\) delivers obligation \(o\).

- **Safety:** no live obligation loses its last deliverer.
- **Liveness:** every live obligation has at least one deliverer.
- **Retire:** only an entry with no incoming edge from \(O\) and no retained probe.
- **Merge:** only when the union of products and checks covers both entries' live
  obligations and the merged description does not increase interference.
- **Upgrade:** only when the source delivers a superset of the target's products
  and the target's retained probes pass on the source.

A retirement that removes the last deliverer is a violation even if the entry looks
old or unused. Do not schedule retirement by age or release cadence.

## 10. Admission procedure

1. **Freeze** the host portfolio: entries, descriptions, declared
   products/checks/regimes, route probes, live obligations, budget.
2. **Classify** each install card against every entry using §3–§4. Record the
   witness booleans, not a prose judgment.
3. **Choose** an action from §5; `merge` only for `duplicate`.
4. **Declare** retained and new probes before any outcome.
5. **Run** the set test in the report: retained probes, new probes, \(\kappa_H\),
   budget, reachability.
6. **On failure**, try in order: `merge` with the nearest true duplicate →
   `demote` out of the default router → defer admission (no action, recorded in
   Unresolved). Never silently accept the break.
7. **Emit** the lifecycle plan with rollback and the budget delta. Do not execute.

A hard conflict is recorded and quarantined; do not pick a side. An apparent
conflict may split by regime (two `variant` entries), but only with declared
regimes and explicit routing.

## 11. Metrics

| Metric | Definition | Use |
|---|---|---|
| Entry count | frozen host entries; lifecycle effects are reported separately, because a rejected lifecycle action must not change the metric | size |
| Retention | retained probes passing after the plan / before | the portfolio condition itself |
| Shadowing risk | maximum relative overlap with the owner, or the probe-margin drop | static proxy; **not** a measurement of shadowing |
| Interference | count and maximum of pairwise description overlaps above threshold | an interference graph, not one score |
| Context tax | tokens added to the default surface (route lines only under progressive disclosure) | report separately from interference |
| Portfolio coverage | live obligations with a deliverer among host + accepted candidates (a demoted entry still counts, because it remains callable) / all live obligations | liveness |
| Orphan rate | host entries with no live obligation and no retained probe | retirement candidates |
| Churn | lifecycle actions per admitted work | cost of self-evolution |

Do not collapse these into a single composite score. Report retention, coverage,
and context tax separately.

## 12. Do not

- Do not turn cap-align into a runtime router, executor, or installer.
- Do not merge because two descriptions look alike.
- Do not retire on a schedule or by age; use reachability.
- Do not silently resolve a procedure conflict.
- Do not execute a probe and call the result measured retention without saying so.
- Do not claim E5/E6 ran, or report measured retention, shadowing, or lifecycle
  effects on a real host. Those experiments are unrun.
- Do not treat `env_conflict` (dependency/version/installation) as a scientific
  conflict.
- Do not count a `demote`d entry as part of the default surface.
