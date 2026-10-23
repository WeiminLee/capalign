# Report contract

`capability-alignment-report.md` (+ companion `capability-alignment.json` with the IR).

Write these in the **caller's current working directory**, or under
`research/runs/<ref-label>-vs-<host-label>/` when the run is an experiment in
this repo. If a report already exists whose `surfaces.reference` (or host) is a
different pair, namespace the filename
(`capability-alignment-<ref>-vs-<host>.md`) — never overwrite another \((H,W)\).

## Mandatory header: `self_check:`

Every report opens with its own validity gate (Layer-1, `evaluation.md`). The block
lists each of the **21** checks (sections, validated evidence, no-low-driven-missing,
rule citations, source kinds, host-only tracked, closing statement, determinism,
neighborhood stratified, host-owned placement, card routing, test contract, slot
evidence & fork, verification honesty, agent competence, bridge not guardrail,
unknown handling, host-need discipline, portfolio coverage, fusion consistency,
lifecycle safety) with `pass` / `fail` / `not-checkable` and a one-line reason. Any `fail` is reported verbatim — the report is then **not valid**
and the run must be reworked, not delivered. `not-checkable` is allowed only where
the input makes the check impossible (live-network determinism); it is never a pass.

Also record `independent_check`: `isolated-context` (a second pass by a separately
invoked context/agent), or `not-available` with the reason. A self-check alone is a
claim, not a verification.

## Required sections

1. **Surfaces** — reference label/kind/license, host label, generated_at; for a
   repo run, also the recovered companion paper (or "not recovered") and whether
   search ran. The host entry carries `host_sync`: the synced commit hash,
   `not-a-git-repo`, `paused-user-decision` (the run stopped for the caller to
   resolve a conflict — such a run is incomplete and produces no gap table), or
   `proceed-dirty@<sha>` with the caller's explicit instruction quoted. It also
   carries `arms` (`method`: `isolated-context|file-freeze|none`, `blind`, and
   `contaminated`) and `independent_check`.
2. **Reference inventory** — capability table (id, name, type, confidence;
   low-confidence rows visibly marked) with evidence pointers. Repo runs split
   **repo projection** from **paper projection** when a companion paper was
   inventoried; do not merge. Every projection row states which arm its evidence
   came from.
3. **Host inventory** — capability table with provenance (where each was found).
4. **Gap table** — every **core** reference capability with class
   (`equivalent|partial|missing|agent-competence|unknown`), **source kind**
   (`host-self-audit|reference-contrast|domain inference`), **host need**
   (`none|data|contract|runner|verification`), `host_need_note`, `local_check`
   (when `host_need: none`), matched host id (when any), and evidence. `partial`
   rows state what is / is not covered. `agent-competence` rows name the local
   check's form and status and carry **no card**; `named` checks are tallied
   separately as unrun. `unknown` rows say which slot was unknown and why — they
   are not `missing`. Paper-arm gaps, when present, are a second table, not extra
   rows in the repo-arm table. After the two tables, a **fork summary**:
   `paper_gaps`, `repo_gaps`, their `intersection`, and `jaccard` — one line,
   computed from the tables, never hand-edited. An empty intersection on a
   non-empty union is the coverage fork; report it verbatim, and mark it
   `contaminated` when `surfaces.arms.blind` is false.
5. **Introduction cards** — one card per joined product (`introduction-card.md`).
   The two projection gap tables stay separate. An `install` card carries the five
   placement fields, `validity_owner`, `rule`, `boundary`, `priority`, and the
   three-beat test contract. A `refuse` card cites rule 7, sets `placement` to
   null, and states that the host stays unchanged. `ignore` rows do not appear. A
   product whose `s` or `e` is `unknown` gets **no card** (`insufficient-evidence`);
   it stays in the gap table as `unknown` and in Unresolved. A
   `validity-unassessed` card installs with `prescribed: ["bind"]`, states
   `validity: unknown (not assessed)`, and prescribes no `check`. A
   `confidence: low` span is called out and never drives `install`.
6. **Portfolio admission** — required whenever at least one card is `install`; a run with
   only refusals emits an empty block. It contains:
   - **Host entries** table: id, question, products, pre/postconditions, regime
     (claim + tags), procedure, checks, provenance, optional `surface` (triggers,
     workflow edges, tool requirements, obligations, output fields), and whether
     a test contract exists. Fields are declared, not inferred from descriptions.
   - **Relations and actions** table: card id, `target_entry`, relation, the
     witness booleans that establish it, action, products added/preserved, regime
     change, conflict, and merge block. `merge` is only for `duplicate`;
     description overlap alone never justifies it.
   - **Probes** table: `qid`, owner, kind (`route|deliver|validity`), declared
     expected result, and `retained`. Probes are declared before results.
   - **Set test**: retained probes with margin, per-card contributions, score,
     pass/fail; new probes; \(\kappa_H\) conflicts; budget before/after/limit and
     demoted ids; overall verdict and reason. The joint arithmetic is
     `margin + Σ probe_effects`; a negative score fails. Demoted candidates do not
     contribute.
   - **Lifecycle plan**: action, target, sources, reason, probes, rollback.
     `retire` only for an entry with no live obligation and no retained probe;
     `upgrade` only for a product/check/regime superset; `merge` preserves both
     test contracts, all live obligations, and provenance, and carries the
     fail-closed merge evidence block (§Merge evidence below).
   - **Budget delta and metrics**: entry count, duplicate count, hard-conflict
     count, orphan count, portfolio coverage. Retention, interference, context
     tax, and churn are reported separately when measured; do not collapse them
     into one score.

   One paragraph must state that the plan is **advice only**: it was not executed,
   no host file was edited, no probe was run, and a `demote`d entry is not part of
   the default surface.

7. **Verification ledger** — every card's `verification.status` in one table,
   with counts: how many `e2e-verified`, how many `contract-only`, how many
   `failed`. A `contract-only` card is a written test that has never been
   executed; the report must say so in plain words and must not claim its
   product as delivered. A `failed` card names the beat that failed (including
   "destroy stayed green" = the test itself is void). This section exists even
   when every card is `contract-only`. When a later build record exists, the
   ledger points at it and derives the status from it; the card block is not
   rewritten.
8. **Host-only section** (informational) — capabilities the host has beyond the reference.
9. **Neighborhood** — required on every run (empty for paper/blog). Lists kept items
   (`relation`, lightweight inventory, gap class), rejected candidates (reason),
   search budget used, and `unresolved` neighborhood seeds. Neighborhood rows must
   not be copied into the core gap table. Companion paper is core, not listed here.
10. **Unresolved** — `unknown` gaps and why (unreachable / unparsable / offline /
   source not consulted — including "host failure statistics not read" when
   applicable; `search-required-offline` when a named seed needed web-search and
   none was available). Every `state: "unknown"` slot is listed here with its
   `why_unknown`.

## Build records

The alignment run writes cards that are `contract-only` by construction. A later
implementation may append a **build record**; it may not edit the alignment
report in place.

```json
{"card_id": "...", "date": "ISO-8601", "host_commit": "<sha>",
 "commands": {"fail_before": "...", "pass_after": "...", "destroy": "..."},
 "beats": {"fail_before": "pass|fail", "pass_after": "pass|fail", "destroy": "pass|fail"},
 "evidence": "observed outcome per beat"}
```

A card is `e2e-verified` only when a build record names the host commit and all
applicable beats passed. A record missing a commit, a command, or an outcome does
not promote the card.

## Validity rules

- Every non-`equivalent` row in the gap table must name the reference capability id;
  no orphan rows.
- Slot states are tri-state (`1` / `0` / `"unknown"`) and carry provenance. A slot
  filled from the wrong arm is invalid: `s`/`v_p` are `paper`, `e`/`v_r` are
  `repo`, `none` only when that arm does not exist.
- `unknown` is never read as `0`. An `unknown` `s` or `e` produces
  `insufficient-evidence`: no install card, no refuse card, and the gap row is
  `unknown`.
- A `state: 0` slot states what was inspected in `span` and why it is empty in
  `why_empty` (`absent`, `no-paper-arm`, `no-repo-arm`).
- `missing` requires ≥1 high/medium-confidence reference evidence entry **and** a
  `host_need` that is not `none` **and** a `host_need_note` with the evidence
  described in `alignment-rules.md` §Host-need evidence. A row whose host need is
  `none` is `agent-competence` or `unknown`, never `missing`.
- `agent-competence` requires a `local_check` with a form and a status. Without
  one, the row is `missing` or `unknown`, not competence. `named` checks are
  reported as unrun and never support a "no gaps" claim.
- Every card slot is an object with `state`, `provenance`, `span`, and `quote`; a
  `state: 1` slot has a non-empty verbatim quote, and a slot that cannot be
  inspected is `state: "unknown"` with `why_unknown`. `kappa: 1` only appears with
  `s` and `e` both `1`.
- Every card carries `prescribed` and `forbidden_primitives` from the table in
  `introduction-card.md`. An `install` card's `test.destroy` names one element of
  `prescribed`; removing it must turn the test red again. A refuse card has
  `destroy: n/a` and no host patch to remove.
- Every card carries a `verification` block (`introduction-card.md`
  §Verification status). A product is claimed as delivered only when a build
  record makes its card `e2e-verified`; `contract-only` and `failed` cards are
  visibly marked in the Verification ledger. A beat marked `pass` carries
  non-empty `evidence`.
- `extend:` cards carry two routing cases: the existing skill still routes its
  original question, and the neighbouring skill does not absorb the new one.
  Skill cards carry a positive and a negative routing case.
- The `fork` block is computed from the two projection gap tables
  (`paper_gaps` ∩ `repo_gaps` = `intersection`; Jaccard over their union);
  it never contradicts them. When `surfaces.arms.blind` is false, the fork is
  marked `contaminated` and is not a measurement.
- Every `install` card carries a `portfolio` block with `relation`,
  `relation_evidence`, `action`, `target_entry`, and `retention_probes`. The
  relation→action pair must be in the allowed table. `duplicate` requires
  `same_product && same_procedure && same_regime`; `variant` requires
  `regime_overlap: false`; `hard-conflict` requires `regime_overlap: true`.
  Description overlap alone never justifies `merge`.
- The top-level `portfolio` block exists even when there is no install card; in
  that case `host_entries` and `probes` may be empty, but `set_test`, `lifecycle`,
  and `metrics` are still present.
- `retire` names an entry with no live obligation and no retained probe;
  `upgrade` names a product/check/regime superset; `merge` preserves both test
  contracts, all live obligations, and provenance. A `merge`/`upgrade` candidate
  carries the target's retained probes in `retention_probes`; the upgrade
  superset is checked against the entry records, not only the witness booleans.
  A `demote`d entry is not counted as part of the default surface for the set
  test, but remains callable for coverage.
- A card whose action is `merge` carries a non-null `merge` block:
  `witnesses` (`unit`, `kind ∈ {W1,W2,W3}`, `evidence`), `removed_units`
  (including `entry:<card_id>`), `locked_residual` (`unit`, `reason`,
  `verbatim`), `coverage` (the five surface classes), `recall_probes`,
  `interaction` (`beta`, `checked`, optional `evidence`), `evidence_level`
  (`constructive|model|statistical`), and `surface_tokens_before/after`.
  Every removed unit has exactly one witness; W3 never deletes an obligation or
  an output/prohibition/exemption unit; the union of both sides' surface units
  equals coverage ∪ removed ∪ locked; both sides' retained probes and the
  candidate's own `deliver`/`validity` probes are in the recall gate and none
  observed failing; `beta < -0.15` requires an extended
  regression check with evidence; `surface_tokens_after` is not greater than
  before; `statistical` requires randomized causal evidence. A missing or
  malformed block is a violation, not a reason to fall back to similarity.
- Each `deliver` (and `validity`) probe names the candidate it belongs to in
  `card_id`; a probe owned by the target entry cannot stand in for several
  candidates.
- The portfolio section is advice only. No host edit, merge, install, or probe
  execution may be reported as done.
- Install cards cite a placement-rule number; refuse cards cite rule 7. A card
  without a rule is a stub.
- Install cards are **host-owned** (`alignment-rules.md` §Placement 6): `target`
  names a host skill/tool/script/extend/runner. A host tool that **calls a
  scientific engine** named by the reference is allowed, and the engine's license
  is reported (`placement.engine_license`); it is not decided. A card that clones,
  wraps, or MCP-mounts the reference **agent/hub/plugin** as the host runtime
  is invalid. Refuse cards name no target.
- Neighborhood rows are absent from the core gap table; the companion paper is
  core (`relation: companion-paper`), never a neighborhood kept-item.
- Neighborhood `missing` requires neighbor-owned high/medium evidence (abstract /
  README / docs), never a search snippet alone.
- Report ends with the exact statement: "Recommendations are placement suggestions;
  building them is a decision for the host agent and its human. Unverified capabilities
  were never treated as missing. Cards marked contract-only carry written tests that
  were never executed; their products are not delivered."

## File shape (JSON companion)

Validated by `references/report-schema.json`. Use any JSON Schema validator the
host already has; the skill ships no runner.

```json
{
  "surfaces": {
    "reference": "...",
    "reference_kind": "repo|paper|blog",
    "reference_license": "...",
    "host": "...",
    "host_sync": "synced@<sha>|not-a-git-repo|paused-user-decision|proceed-dirty@<sha>",
    "generated_at": "...",
    "companion_paper": "...|null",
    "search_used": false,
    "arms": {"method": "isolated-context|file-freeze|none", "blind": true, "contaminated": false},
    "independent_check": "isolated-context|not-available"
  },
  "gaps": [{
    "ref_id": "...",
    "class": "equivalent|partial|missing|agent-competence|host-only|unknown",
    "host_need": "none|data|contract|runner|verification",
    "host_need_note": "...",
    "local_check": {"form": "analytic|conservation|limit", "status": "named|demonstrated", "command": "..."},
    "host_id": "...|null",
    "source_kind": "host-self-audit|reference-contrast|domain inference",
    "layer": "core"
  }],
  "paper_projection_gaps": [],
  "neighborhood": {
    "kept": [{"id": "...", "relation": "sibling|cited-method|declared-related|official-docs", "class": "..."}],
    "rejected": [{"id": "...", "reason": "..."}],
    "unresolved": []
  },
  "cards": [
    {
      "id": "...",
      "slots": {
        "s": {"state": 1, "provenance": "paper", "span": "path:start-end", "quote": "verbatim"},
        "e": {"state": 0, "provenance": "repo", "span": "path:start-end", "quote": "", "why_empty": "absent"},
        "v_p": {"state": "unknown", "provenance": "paper", "span": null, "quote": "", "why_unknown": "unreachable"},
        "v_r": {"state": 1, "provenance": "repo", "span": "path:start-end", "quote": "verbatim"},
        "kappa": 0
      },
      "lambda": "obligation-sans-entry|entry-sans-obligation|procedure-conflict|validity-gap|both-aligned|validity-unassessed",
      "action": "install|refuse",
      "boundary": "in-question|new-question",
      "priority": "fix-wrongness|honor-promise|extend-surface|null",
      "rule": [1, 3, 6],
      "prescribed": ["bind", "impl", "check", "record"],
      "forbidden_primitives": ["impl", "check", "record"],
      "placement": {"target": "...", "question": "...", "input": "...", "validity": "...", "validity_owner": "gate|runner|skill-body|null", "forbidden": "...", "engine": "...|null", "engine_license": "...|null"},
      "test": {"fail_before": "...|null", "pass_after": "...", "destroy": "...|n/a"},
      "verification": {
        "status": "e2e-verified|contract-only|failed",
        "beats": {"fail_before": "pass|fail|not-run", "pass_after": "pass|fail|not-run", "destroy": "pass|fail|not-run|n/a"},
        "evidence": "command + observed outcome per executed beat; empty when not-run"
      },
      "portfolio": {
        "relation": "covered|partial|duplicate|variant|hard-conflict|subsumes|subsumed|adjacent|unrelated",
        "relation_evidence": {"same_product": false, "same_procedure": false, "same_regime": false, "regime_overlap": false, "regime_subset": false, "checks_missing": false, "question_overlap": true, "products_superset": false, "checks_superset": false, "regime_superset": false, "products_subset": false, "checks_subset": false},
        "action": "no-op|bind|author|extend|add_validator|merge|demote|upgrade|downgrade|retire|quarantine|refuse|split|new-entry",
        "target_entry": "...|null",
        "retention_probes": ["..."],
        "conflict": null,
        "merge": {
          "witnesses": [{"unit": "entry:...", "kind": "W1|W2|W3", "evidence": "..."}],
          "removed_units": ["entry:..."],
          "locked_residual": [{"unit": "...", "reason": "...", "verbatim": "..."}],
          "coverage": {"triggers": [], "workflow_edges": [], "tool_requirements": [], "obligations": [], "output_fields": []},
          "recall_probes": ["..."],
          "interaction": {"beta": 0.0, "checked": false, "evidence": "..."},
          "evidence_level": "constructive|model|statistical",
          "surface_tokens_before": 0,
          "surface_tokens_after": 0
        },
        "rollback": "..."
      }
    }
  ],
  "portfolio": {
    "host_entries": [{
      "id": "...", "question": "...", "products": ["..."],
      "preconditions": ["..."], "postconditions": ["..."],
      "regime": {"claim": "...", "tags": ["..."]},
      "procedure": "...", "checks": ["..."], "provenance": ["..."],
      "test_contract": {"fail_before": "...|null", "pass_after": "...", "destroy": "..."}
    }],
    "probes": [{"qid": "...", "text": "...", "owner": "...", "card_id": "...|null", "expected": "...", "kind": "route|deliver|validity", "retained": true}],
    "set_test": {
      "retained_probes": [{
        "qid": "...", "owner": "...", "margin": 0.3,
        "contributions": [{"card_id": "...", "delta": -0.2}],
        "score": 0.1, "passed": true
      }],
      "new_probes": [{"qid": "...", "owner": "...", "passed": true}],
      "conflicts": [{"a": "...", "b": "...", "kind": "procedure|regime|precondition|env", "evidence": "..."}],
      "budget": {"context_tokens_before": 0, "context_tokens_after": 0, "limit": 0, "demoted": []},
      "passed": true,
      "reason": "..."
    },
    "lifecycle": [{"action": "...", "target": "...|null", "sources": ["..."], "reason": "...", "probes": ["..."], "rollback": "..."}],
    "metrics": {"entry_count": 0, "duplicate_count": 0, "hard_conflict_count": 0, "orphan_count": 0, "portfolio_coverage": 1.0}
  },
  "fork": {
    "paper_gaps": ["product ids that are gaps on the paper projection"],
    "repo_gaps": ["product ids that are gaps on the repo projection"],
    "intersection": ["ids in both"],
    "jaccard": 0.0,
    "contaminated": false
  },
  "unresolved": [],
  "build_records": []
}
```
