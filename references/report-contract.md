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
statement, determinism, host-owned placement) with
`pass`/`fail` and a one-line reason. Any `fail` is reported verbatim — the report is
then **not valid** and the run must be reworked, not delivered.

## Required sections
1. **Surfaces** — reference label/kind, host label, generated_at; for a repo run,
   also the recovered companion paper (or "not recovered") and whether search ran.
2. **Reference inventory** — capability table (id, name, type, confidence; low-confidence
   rows visibly marked) with evidence pointers. Repo runs split **repo projection**
   from **paper projection** when a companion paper was inventoried; do not merge.
3. **Host inventory** — capability table with provenance (where each was found).
4. **Gap table** — every **core** reference capability with class (`equivalent|partial|missing|unknown`),
   **source kind** (`host self-audit|reference-contrast|domain inference`), matched host id
   (when any), and evidence. `partial` rows state what is / is not covered. Paper-arm
   gaps, when present, are a second table, not extra rows in the repo-arm table.
5. **Recommendations** — per `missing`/`partial` gap: placement (skill/tool/script/extend/
   runner contract/skip), the decision rule satisfied (numbered from alignment-rules.md),
   estimated surface (new skill? extend which? new tool? which module?), and a
   `confidence: low`-evidence call-out where applicable.
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
- Recommendations must cite the rule number; a recommendation without a rule is a stub.
- Recommendations are **host-owned** (`alignment-rules.md` §Placement 6): they
  name a host skill/tool/script/extend/skip. A host tool that **calls a
  scientific engine** named by the reference is allowed. A recommendation that
  clones, wraps, or MCP-mounts the reference **agent/hub/plugin** as the host
  runtime is invalid.
- Neighborhood rows are absent from the core gap table; the companion paper is
  core (`relation: companion-paper`), never a neighborhood kept-item.
- Neighborhood `missing` requires neighbor-owned high/medium evidence (abstract /
  README / docs), never a search snippet alone.
- Report ends with the exact statement: "Recommendations are placement suggestions;
  building them is a decision for the host agent and its human. Unverified capabilities
  were never treated as missing."

## File shape (JSON companion)
```json
{
  "surfaces": {
    "reference": "...",
    "host": "...",
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
  "recommendations": [...],
  "unresolved": [...]
}
```