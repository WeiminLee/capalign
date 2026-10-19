# Report contract

`capability-alignment-report.md` (+ companion `capability-alignment.json` with the IR).

Write these in the **caller's current working directory**, or under
`research/runs/<ref-label>-vs-<host-label>/` when the run is an experiment in
this repo. If a report already exists whose `surfaces.reference` (or host) is a
different pair, namespace the filename
(`capability-alignment-<ref>-vs-<host>.md`) — never overwrite another \((H,W)\).

## Mandatory header: `self_check:`
Every report opens with its own validity gate (Layer-1, `evaluation.md`). The block
lists each check (sections, validated evidence, no-low-driven-missing, rule
citations, source kinds, host-only tracked, neighborhood stratified, closing
statement, determinism, host-owned placement, card routing, test contract) with
`pass`/`fail` and a one-line reason. Any `fail` is reported verbatim — the report is
then **not valid** and the run must be reworked, not delivered.

## Required sections
1. **Surfaces** — reference label/kind, host label, generated_at; for a repo run,
   also the recovered companion paper (or "not recovered") and whether search ran.
   The host entry carries `host_sync`: the synced commit hash, `not-a-git-repo`,
   `paused-user-decision` (the run stopped for the caller to resolve a conflict —
   such a run is incomplete and produces no gap table), or `proceed-dirty@<sha>`
   with the caller's explicit instruction quoted.
2. **Reference inventory** — capability table (id, name, type, confidence; low-confidence
   rows visibly marked) with evidence pointers. Repo runs split **repo projection**
   from **paper projection** when a companion paper was inventoried; do not merge.
3. **Host inventory** — capability table with provenance (where each was found).
4. **Gap table** — every **core** reference capability with class (`equivalent|partial|missing|unknown`),
   **source kind** (`host self-audit|reference-contrast|domain inference`), matched host id
   (when any), and evidence. `partial` rows state what is / is not covered. Paper-arm
   gaps, when present, are a second table, not extra rows in the repo-arm table.
   After the two tables, a **fork summary**: `paper_gaps`, `repo_gaps`, their
   `intersection`, and `jaccard` — one line, computed from the tables, never
   hand-edited. An empty intersection on a non-empty union is the coverage fork;
   report it verbatim.
5. **Introduction cards** — one card per joined product (`introduction-card.md`).
   The two projection gap tables stay separate. An `install` card carries the five
   placement fields, `validity_owner`, `rule`, `boundary`, `priority`, and the
   three-beat test contract. A `refuse` card cites rule 7, sets `placement` to
   null, and states that the host stays unchanged. `ignore` rows do not appear.
   A `confidence: low` span is called out and never drives `install`.
6. **Verification ledger** — every card's `verification.status` in one table,
   with counts: how many `e2e-verified`, how many `contract-only`, how many
   `failed`. A `contract-only` card is a written test that has never been
   executed; the report must say so in plain words and must not claim its
   product as delivered. A `failed` card names the beat that failed (including
   "destroy stayed green" = the test itself is void). This section exists even
   when every card is `contract-only`.
6. **Host-only section** (informational) — capabilities the host has beyond the reference.
7. **Neighborhood** — required on every run (empty for paper/blog). Lists kept items
   (`relation`, lightweight inventory, gap class), rejected candidates (reason),
   search budget used, and `unresolved` neighborhood seeds. Neighborhood rows must
   not be copied into the core gap table. Companion paper is core, not listed here.
8. **Unresolved** — `unknown` gaps and why (e.g., proprietary, unparsable, offline, source
   not consulted — including "host failure statistics not read" when applicable;
   `search-required-offline` when a named seed needed web-search and none was available).

## Validity rules
- Every non-`equivalent` row in the gap table must name the reference capability id;
  no orphan rows.
- `missing` requires ≥1 high/medium-confidence reference evidence entry.
- Every card slot is an object `{filled, span, quote}`; a `filled: 1` slot has a
  non-empty verbatim quote, and a slot that cannot be cited is `filled: 0`.
  `kappa: 1` only appears with `s` and `e` both filled.
- Every card carries `prescribed` and `forbidden_primitives` from the table in
  `introduction-card.md`; `test.destroy` names the removal of exactly the
  `prescribed` primitive.
- Every card carries a `verification` block (`introduction-card.md`
  §Verification status). A product is claimed as delivered only when its card
  is `e2e-verified`; `contract-only` and `failed` cards are visibly marked in
  the Verification ledger. A beat marked `pass` carries non-empty `evidence`.
- The `fork` block is computed from the two projection gap tables
  (`paper_gaps` ∩ `repo_gaps` = `intersection`; Jaccard over their union);
  it never contradicts them.
- Install cards cite a placement-rule number; refuse cards cite rule 7. A card
  without a rule is a stub.
- Install cards are **host-owned** (`alignment-rules.md` §Placement 6): `target`
  names a host skill/tool/script/extend/runner. A host tool that **calls a
  scientific engine** named by the reference is allowed. A card that clones,
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
```json
{
  "surfaces": {
    "reference": "...",
    "host": "...",
    "host_sync": "synced@<sha>|not-a-git-repo|paused-user-decision|proceed-dirty@<sha>",
    "generated_at": "...",
    "companion_paper": "...|null",
    "search_used": false
  },
  "gaps": [{"ref_id": "...", "class": "...", "host_id": "...|null", "rule": "2|3|5|null", "layer": "core"}],
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
        "s": {"filled": 0, "span": "path:start-end|null", "quote": "verbatim"},
        "e": {"filled": 0, "span": "...", "quote": "..."},
        "v_p": {"filled": 0, "span": "...", "quote": "..."},
        "v_r": {"filled": 0, "span": "...", "quote": "..."},
        "kappa": 0
      },
      "lambda": "obligation-sans-entry|entry-sans-obligation|procedure-conflict|validity-gap|both-aligned",
      "action": "install|refuse",
      "boundary": "in-question|new-question",
      "priority": "fix-wrongness|honor-promise|extend-surface|null",
      "rule": "3,6|7",
      "prescribed": "bind|impl|check|record|none",
      "forbidden_primitives": ["bind", "impl"],
      "placement": {"target": "...", "question": "...", "input": "...", "validity": "...", "validity_owner": "gate|runner|skill-body|null", "forbidden": "..."},
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
    "jaccard": 0.0
  },
  "unresolved": [...]
}
```