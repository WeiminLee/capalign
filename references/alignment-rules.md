# Alignment & placement rules

Generic, framework- and domain-agnostic rules. One doctrine — MatDiscovery's
capability surface — was the first **instance** that validated them and is cited
here only as a worked example (§Host doctrine adaptation). A host's own convention
overrides wherever it has one. Methodology (phases, false-gap lessons) is in
`methodology.md`.

## Validate before classify
Classification happens **after** candidate gaps are validated against the host
(search code/docs for the capability terms, read artifact/output specs, check for an
existing partial path). The comparison table alone is not evidence. A candidate that
cannot be validated is `unknown`, not `missing`.

## Gap source kinds (informs priority, tags every gap)
| kind | definition | priority |
|---|---|---|
| `host self-audit` | the host's own docs/roadmap/audit already admits the gap | highest — the host already owes it |
| `reference-contrast` | the reference has it, the host lacks it, neither documents it | medium — reference is the source of truth |
| `domain inference` | a domain expert reasons it is wrong/missing; both sides silent | lowest — must be argued, not cited |

## Gap classification
| class | definition | evidence required |
|---|---|---|
| `equivalent` | host capability covers the reference semantics | host id is named in the report line |
| `partial` | host covers a **strict subset** of the reference semantics; adjacent-but-different is NOT partial — an adjacent host capability that does not subsume the reference belongs in the gap's note as a near-miss, and the gap is `missing` (strict subsume semantics, cf. `formal-foundations.md` §2) | host id + what is / is not covered, stated |
| `missing` | reference capability with no host counterpart | **validated** reference evidence entries, ≥1 high/medium |
| `host-only` | host capability with no reference counterpart | host evidence (informational) |
| `unknown` | cannot be characterized from the inputs | never classified as `missing` |

## Reference-side inventory heuristics
- **repo**: CLI entry points (`cli`/`console_scripts`/`bin`/`[project.scripts]`), package modules
  (top-level modules = capability boundaries), dependency fingerprints → implied
  capability families (**domain lexicon — replace per domain**; materials example: a
  phonon engine implies force-constants/dynamical-matrix/DOS/thermal/QHA families, a
  DFT engine implies SCF/relax/bands/response; derived families start at
  `medium` confidence until confirmed), docs feature pages.
- **paper**: Methods→Steps decomposition; explicit software/dataset dependencies
  (must-run tools and data products are hard `tool`/`data` capabilities); contribution
  claims that imply a procedure (→ `workflow`), a computation (→ `compute`), or a
  theory (→ `concept`).
- **blog**: claims and recipes only; every extracted capability needs a quote as evidence;
  opinion without procedure → `concept` at `confidence: low`.

## Placement decision (per missing gap)
Order recommendations with an explicit priority judgment, not a count
(`methodology.md` Phase 5: fix-wrongness > honor-promise > extend-surface);
source kind informs priority (host self-audit first). Then ask, in order:

1. **Axis** — does the host need "a way to do something" (skill), "a deterministic
   computation" (tool/script), or "a settings/UI/service surface" (plugin/server)?
   A bare `compute` capability usually wants a tool or script, never a plugin.
2. **Tool vs script** — change-count test: a capability that one place computes and
   several consume is a shared tool; something only one skill consumes belongs in that
   skill's own companion scripts. Gate/render/audit/parallelism needs push it to a tool.
3. **New skill vs extend** — same input contract + adjacent problem class → extend the
   existing skill (minimal body addition + a dedicated reference page); an independent
   routing trigger or a different input contract → new skill. Naming/prefixes are the
   host's convention.
4. **Constraint ownership** — state which layer owns each validity constraint:
   static-checkable → linter/gate; runtime-known → hook/runner self-report;
   never-mechanical → agent judgment in the skill body. The recommendation names the
   layer; it does not design the constraint.
5. **Never** — recommend a capability whose reference-side evidence is all
   `confidence: low`; mark it `unknown` instead.

## Host doctrine adaptation
If the host documents its own capability surface (axis definitions, skill shape,
tool-vs-script rules, naming, enforcement gates), that doctrine **is the law for that
host** and overrides these generic rules on conflict. The report must state which
doctrine it used. MatDiscovery's `CAPABILITY-SURFACE.md` (§0.1 decision quick-ask,
ARCHITECTURE §5 axis table) is a complete worked example of such a doctrine — usable
verbatim only for a host with the same architecture (plugin package + skill bundle +
local MCP tools + remote families), and only then by explicit choice, never by default.

## What this skill does NOT decide
- Scientific soundness of the reference capability (that belongs to the host's domain skills).
- Whether to actually build the gap (a product decision for the human).
- Host-specific schema/format details (the report uses the IR + report contract;
  the host adapts).