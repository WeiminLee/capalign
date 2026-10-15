# Report contract

`capability-alignment-report.md` (+ companion `capability-alignment.json` with the IR).

## Mandatory header: `self_check:`
Every report opens with its own validity gate (Layer-1, `evaluation.md`). The block
lists each check (sections, validated evidence, no-low-driven-missing, rule
citations, source kinds, host-only tracked, closing statement, determinism) with
`pass`/`fail` and a one-line reason. Any `fail` is reported verbatim — the report is
then **not valid** and the run must be reworked, not delivered.

## Required sections
1. **Surfaces** — reference label/kind, host label, generated_at.
2. **Reference inventory** — capability table (id, name, type, confidence; low-confidence
   rows visibly marked) with evidence pointers.
3. **Host inventory** — capability table with provenance (where each was found).
4. **Gap table** — every reference capability with class (`equivalent|partial|missing|unknown`),
   **source kind** (`host self-audit|reference-contrast|domain inference`), matched host id
   (when any), and evidence. `partial` rows state what is / is not covered.
5. **Recommendations** — per `missing`/`partial` gap: placement (skill/tool/script/extend/
   runner contract/skip), the decision rule satisfied (numbered from alignment-rules.md),
   estimated surface (new skill? extend which? new tool? which module?), and a
   `confidence: low`-evidence call-out where applicable.
6. **Host-only section** (informational) — capabilities the host has beyond the reference.
7. **Unresolved** — `unknown` gaps and why (e.g., proprietary, unparsable, offline, source
   not consulted — including "host failure statistics not read" when applicable).

## Validity rules
- Every non-`equivalent` row in the gap table must name the reference capability id;
  no orphan rows.
- `missing` requires ≥1 high/medium-confidence reference evidence entry.
- Recommendations must cite the rule number; a recommendation without a rule is a stub.
- Report ends with the exact statement: "Recommendations are placement suggestions;
  building them is a decision for the host agent and its human. Unverified capabilities
  were never treated as missing."

## File shape (JSON companion)
```json
{
  "surfaces": {"reference": "...", "host": "...", "generated_at": "..."},
  "gaps": [{"ref_id": "...", "class": "...", "host_id": "...|null", "rule": "2|3|5|null"}],
  "recommendations": [...],
  "unresolved": [...]
}
```