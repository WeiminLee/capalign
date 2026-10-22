# Methodology — a reusable capability-alignment method

This is the method, stated generically. The phonopy ↔ MatDiscovery alignment was the
**first instance that validated it** — it is referenced as such (an instance, a
worked example), never as the method's content. The method works for any host agent
and any reference (repo / paper / blog), in any domain, with any host doctrine.

## 0. Three layers — keep them separate

| layer | what lives here | reusable? |
|---|---|---|
| **Generic method** (this file) | the phases and rules below; neutral language, no host or domain vocabulary | always |
| **Adaptation layer** | the host's own capability doctrine (skill/tool axes, naming, report dialect), and the domain lexicon used to map dependencies → capability families | pluggable; replaced per host / per domain |
| **Instance** | a concrete run — phonopy ↔ MatDiscovery, or the next one | evidence that the method works, not the method |

Discipline: a rule written into the generic layer must not mention a host's file, a
host's artifact name, or one domain's lexicon. If it does, it belongs in the
adaptation layer.

## 1. Generic phases

### Phase 0 — Frame the target
Decide before any scan: what is the reference, what is the host surface, and what is
the deliverable (inventory / gap table / placement / all). The deliverable is
**domain-capability gaps**: simulation/analysis first, domain-agent methods at
most (`alignment-rules.md` §Scope). Generic agent packaging is out of scope.
The deliverable fixes how deep each inventory must go; it may legitimately evolve
as the work proceeds, and then the report says so. A homepage URL and a git clone
of the same project are **one** reference \(W\), not two runs. Scope the host to
its declared skill/tool root before scanning (worktrees and `node_modules` are
not the host surface).

### Phase 0.5 — Observe the reference fully (repo input)
A repo tree is \(W_{\mathrm{repo}}\). Before building inventories, recover the
companion encoding and a **bounded neighborhood** (`inventory-heuristics.md` §E):
local seeds, then homepage, then web-search only when a named seed or the
companion paper is still missing. Identity-gate membership. Split **core** \(W\)
(given work: repo + its paper/docs) from **neighborhood** \(N\) (siblings /
cited methods / declared-related). \(N\) is an instrument completeness layer;
C1/C3 stay defined on \(W\). Live network is never required for a valid run.

### Phase 1 — Dual independent inventories
Build the reference inventory and the host inventory **separately, without looking at
each other**. Two lists built while contaminated by each other produce a list of
differences, not of gaps. Inventories are of *capabilities* (semantic units: things a
user can get done), not of files or functions. Core paper-arm and repo-arm are
two projections of \(W\), inventoried independently of the host and of each
other. Neighborhood items are additional reference surfaces, also built without
looking at the host.

Freeze the paper arm before opening the repo arm: write its slot records with
`span` + verbatim `quote` first, or run the two inventories in separate
contexts. Record the method in `surfaces.arms`
(`isolated-context` / `file-freeze` / `none`). An unisolated run is allowed but
sets `blind: false`, caps paper-arm confidence at `medium`, and marks the fork
`contaminated`; the residual is then not a measurement.

### Phase 2 — Cross-validate suspected gaps
Never classify from the comparison table alone. Every candidate `missing` / `partial`
is validated against the host (and, where cheap, the reference): search the host's
code/docs for the capability terms, read its artifact/output specifications, check for
an existing partial path. The comparison table is a set of hypotheses; validation turns
them into evidence. (The first instance caught several false candidates this way — see
§3.)

### Phase 3 — Gap classification with source tagging
Assign each reference capability a class: `equivalent | partial | missing | agent-competence |
host-only | unknown`, and record `host_need` (`none|data|contract|runner|verification`) —
what the host must **own**. `host_need: none` with a named local check is
`agent-competence`, not debt. A source that could not be inspected yields
`unknown`, never a `0`-driven verdict: absence of evidence is not evidence of
absence. Additionally tag every gap with a **source kind**:

- `host-self-audit` — the host's own documents/roadmap already admit the gap.
- `reference-contrast` — the reference has it, the host lacks it, neither documents it.
- `domain inference` — a domain expert reasons it is wrong/missing; both sides silent.

Source kind drives priority, so it is recorded, not implied.

### Phase 4 — Cost-tier the placement
Cost-tier only cards whose `action` is `install` (`introduction-card.md`). A
`refuse` card is a finished outcome: the host stays unchanged. For each
install card, estimate what the **host** must change to close it. The tier question is
always about the host's own architecture, never about the size of the reference side.
Never cost-tier "add the reference agent as a nested runtime"; that is not a
host change (`alignment-rules.md` §Placement 6).
A sensible default ladder (names and examples are the adaptation layer's job):
A) pure local (data already on hand, a host-side computation closes it);
B) probe-gated local (locally closeable once one unknown is confirmed);
C) contract change (the host's remote runner / envelope / policy surface);
D) new physical input (needs something the host cannot synthesize);
E) not recommended (route conflict or outside the host's product boundary).

### Phase 5 — Prioritize with an explicit judgment
Order the install cards with a stated judgment, not a count. A refuse card is
already finished. The reference run used
**fix-wrongness > honor-promise > extend-surface** (first close results that are
systematically wrong or promised but absent, then whole-class physics errors, then new
question classes). The judgment must be stated in the report so it can be argued with.

### Phase 6 — Granularity against the host's authority
Placement uses the host's own decision boundaries where it has any (its capability
doctrine: what a skill is, what a tool is, naming, where scripts live). Where the host
has no doctrine, fall back to `alignment-rules.md` §Alignment boundary,
§Placement, and §Skill boundary and tool duty. Never invent host rules for the occasion; never apply another
host's doctrine as law.

### Phase 7 — Advice, stopping at advice
The output is the introduction card, written before any host edit. The test
contract on the card is not executed in this run. Building is a
product/engineering decision for the host and its human; the report says so
in a fixed closing statement.

## 2. Adaptation layer (pluggable — replaced per host / per domain)

- **Host doctrine**: if the host documents its capability-surface decisions (axis
  definitions, tool-vs-script rules, naming/prefix conventions, enforcement gates),
  capture them here and let them override the generic placement rules for that host.
  MatDiscovery's `CAPABILITY-SURFACE.md` is one such doctrine — a worked example, not
  the law for other hosts.
- **Domain lexicon**: mapping dependency fingerprints → implied capability families is
  domain knowledge, not method. For materials simulation, a phonon engine may imply
  force-constants / dynamical-matrix / DOS / thermal-properties, and a DFT
  engine may imply SCF / relax / bands / response. A named method is not a family
  for every engine in that area; it enters only when this work states it. The same lexicon also names which
  verbs are domain-agent methods (benchmark a potential, fine-tune, distill) versus
  generic packaging (plugin, extra MCP, lockfiles). Another domain swaps this table.
- **What the host agent cannot supply** (the skill's content): the domain judgement
  that surrounds a method — problem recognition, model selection, scale discipline,
  the measured traps, how a result is read. Not the equation and not the API, which
  a general agent already has. `alignment-rules.md` §What a skill is for states this
  as the bridge definition; it is what a placement must carry to be worth a card, and
  what a test contract must exercise.
  The method provides the *action* (derive implied families from dependencies, mark
  them medium confidence until confirmed; drop packaging), not the table.
- **Report dialect**: what the report is called, where it lands, and the JSON schema
  are host conventions. The generic contract (required sections, validity rules in
  `report-contract.md`) stays; names and locations adapt.

## 3. Instance: phonopy ↔ MatDiscovery (first validation, recorded)

What the generic phases looked like in practice, and what the instance taught the
method:

| generic phase | instance facts | lesson folded back into the generic method |
|---|---|---|
| 1 dual inventories | two parallel read-only passes, one per side | separation is the rule, not a convenience |
| 2 cross-validation | out of ~25 candidate gaps, grep killed 4 false ones: mode Grüneisen and group velocity existed in the host; thermal-expansion α was `partial` (default listed, no table) not `missing`; NAC/LO-TO confirmed truly absent | comparison table = hypotheses; validation = evidence |
| 3 source tagging | gaps traced to host-self-audit (its SKILL-DESIGN §9 roadmap listed α, FF sanity, collective conductivity, melting-point runner), reference-contrast (NAC, electronic thermal, irreps…), domain inference (metal κ_e) | source kind → priority; host-self-audit gaps were done first |
| 4 cost tiering | A–E ladder mapped onto MatDiscovery's local-tool / runner-contract / DFT-input surface | tiers are host-architectural by definition |
| 5 priority | fix-wrongness > honor-promise > extend-surface; the four host-self-audit gaps were the first batch | judgment stated, source-informed |
| 6 granularity | placement anchored to MatDiscovery's CAPABILITY-SURFACE §0.1 (its own doctrine) | host doctrine overrides generic; never borrow a doctrine |
| 7 advice | report ended at recommendations; the implementer (a human + the same agent) decided | fixed closing statement |

## 4. Standing discipline (generic — applies to every run)

1. Evidence per capability; no name without a pointer.
2. `low`-confidence entries never drive a `missing` verdict.
3. The three source kinds are **not exhaustive**: nobody asked "which questions do
   users actually ask most" — that needs the host's failure statistics, which this
   method does not read. The report must list which sources were NOT consulted.
4. `host-only` capabilities are reported too — the reverse gap is information, not noise.
5. Cross-validation is mandatory before classification on every run, not just in the
   first instance.
6. **A host agent already knows its domain's standard methods.** The unit of a gap
   is what the host must **own** — data, a contract, a runner, a verified regime —
   not what a library can compute. A method the agent can run against a standard
   library and check locally is `agent-competence`, not debt; counting a code
   library's modules as capabilities inflates the gap table and produces install
   cards for textbook work. The named local check is what keeps this from
   collapsing into "the agent knows it".
