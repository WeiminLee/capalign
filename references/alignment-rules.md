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
| `equivalent` | host capability covers the reference semantics, **including the same domain observable produced by a different calculator or Hamiltonian** (energy on FieldMat covers energy on MACE as `compute`; see §Scope) | host id is named in the report line |
| `partial` | host covers a **strict subset** of the reference semantics; adjacent-but-different is NOT partial — an adjacent host capability that does not subsume the reference belongs in the gap's note as a near-miss, and the gap is `missing` (strict subsume semantics, cf. `formal-foundations.md` §2). A different Hamiltonian is **not** adjacent-but-different at the `compute` layer; it is `equivalent`. A domain-agent method (benchmark protocol, fine-tune, distill) on top of an existing observable is a separate capability and may still be `missing`. | host id + what is / is not covered, stated |
| `missing` | reference capability with no host counterpart | **validated** reference evidence entries, ≥1 high/medium |
| `host-only` | host capability with no reference counterpart | host evidence (informational) |
| `unknown` | cannot be characterized from the inputs | never classified as `missing` |

## Reference-side inventory heuristics
- **repo**: CLI entry points (`cli`/`console_scripts`/`bin`/`[project.scripts]`), package modules
  (top-level modules = capability boundaries), dependency fingerprints → implied
  capability families (**domain lexicon — replace per domain**; materials example: a
  phonon engine implies force-constants/dynamical-matrix/DOS/thermal/QHA families, a
  DFT engine implies SCF/relax/bands/response; derived families start at
  `medium` confidence until confirmed), docs feature pages. After the local
  inventory, run `inventory-heuristics.md` §E: recover companion paper (core)
  and a budgeted neighborhood; identity gate; search only when necessary.
- **paper**: Methods→Steps decomposition; explicit software/dataset dependencies
  (must-run tools and data products are hard `tool`/`data` capabilities); contribution
  claims that imply a procedure (→ `workflow`), a computation (→ `compute`), or a
  theory (→ `concept`).
- **blog**: claims and recipes only; every extracted capability needs a quote as evidence;
  opinion without procedure → `concept` at `confidence: low`.

## Scope of alignment (what counts)

Inventory **domain capabilities** a practitioner can get done, not the packaging
that ships them. Ask two in-scope layers in order. Materials is the default
lexicon for this skill; another domain replaces the examples, not the cut.

1. **Domain simulation / analysis (core).** Physical (or domain) observables and
   procedures. Same observable on a different backend or calculator is **one**
   `compute` capability — class `equivalent` if the host already produces that
   quantity. Do not mint a new energy/relax/MD gap per Hamiltonian.
2. **Domain-agent methods (outer bound).** Procedures a domain agent should
   expose for working with models, datasets, or benchmark protocols in that
   domain. Materials examples: run an adsorption-energy benchmark; fine-tune a
   foundation potential on the user's chemistry; distill a large potential into
   a production student. These may be `missing` even when the underlying
   observable already exists on the host.

**Out of scope** (do not inventory; never `missing`): generic agent packaging —
plugin marketplaces, extra MCP servers, lockfile replay, per-environment
bootstrap, token login, calculator codegen, framework wrappers. How an agent
ships is not what this skill aligns.

A registry/roster of N models is at most one domain-agent `interface` (model
selection), never N capabilities, and never a neighborhood.

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
6. **Host-owned** — the recommendation is a capability the **host would own** on
   its own skill/tool/runner surface after the reference *agent* is gone.
   - If the reference is a **scientific engine** (library/CLI whose deliverable
     is a domain quantity or method): a new host tool/skill may **call that
     engine**. That is owning the agent-facing capability.
   - If the reference is an **agent or hub** (skill pack, plugin, registry that
     drives other engines): place the driven domain verbs as host-native
     skills/tools. The host may call the **same upstream engines** the hub
     drives. It must not clone, wrap, or MCP-mount the hub (`install.sh` of the
     reference, `$REF_HOME`, plugin marketplace, nested skill pack).
   Invalid: "new skill wrapping a clone of the reference." Valid: "new host
   skill that runs this protocol on host compute / an upstream scientific
   library." License of a sibling engine is reported, not decided.

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
- Whether the host should take a GPL (or otherwise copyleft) sibling engine as
  a dependency — report the license, do not decide.
- Host-specific schema/format details (the report uses the IR + report contract;
  the host adapts).