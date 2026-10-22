# Report contract

`capability-alignment-report.md` (+ companion `capability-alignment.json` with the IR).

Write these in the **caller's current working directory**, or under
`research/runs/<ref-label>-vs-<host-label>/` when the run is an experiment in
this repo. If a report already exists whose `surfaces.reference` (or host) is a
different pair, namespace the filename
(`capability-alignment-<ref>-vs-<host>.md`) — never overwrite another \((H,W)\).

## Mandatory header: `self_check:`

Every report opens with its own validity gate (Layer-1, `evaluation.md`). The block
lists each of the **18** checks (sections, validated evidence, no-low-driven-missing,
rule citations, source kinds, host-only tracked, closing statement, determinism,
neighborhood stratified, host-owned placement, card routing, test contract, slot
evidence & fork, verification honesty, agent competence, bridge not guardrail,
unknown handling, host-need discipline) with `pass` / `fail` / `not-checkable` and a
one-line reason. Any `fail` is reported verbatim — the report is then **not valid**
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
6. **Verification ledger** — every card's `verification.status` in one table,
   with counts: how many `e2e-verified`, how many `contract-only`, how many
   `failed`. A `contract-only` card is a written test that has never been
   executed; the report must say so in plain words and must not claim its
   product as delivered. A `failed` card names the beat that failed (including
   "destroy stayed green" = the test itself is void). This section exists even
   when every card is `contract-only`. When a later build record exists, the
   ledger points at it and derives the status from it; the card block is not
   rewritten.
7. **Host-only section** (informational) — capabilities the host has beyond the reference.
8. **Neighborhood** — required on every run (empty for paper/blog). Lists kept items
   (`relation`, lightweight inventory, gap class), rejected candidates (reason),
   search budget used, and `unresolved` neighborhood seeds. Neighborhood rows must
   not be copied into the core gap table. Companion paper is core, not listed here.
9. **Unresolved** — `unknown` gaps and why (unreachable / unparsable / offline /
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
      }
    }
  ],
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
