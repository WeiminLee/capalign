# Portfolio admission and evidence-gated lifecycle

> Research note, 2026-10-23. Feeds `docs/acl-paper-design.md` and the skill's
> step 7. Companion to `typed-introduction.md` (row-level \(\lambda\to I\)).
> Nothing here is an experimental result of ours; every number is cited from the
> paper named next to it. Our own claims are marked **design** or **hypothesis**.

## 0. Why this note exists

`typed-introduction.md` answers one question: given a unit \(u=(p,s,e,v_p,v_r,\kappa)\),
what does the host edit, and what test must fail first. That is a **row-level**
decision. It assumes the host is \(H=(P_H,K_H)\): a set of products and a set of
validity checks.

A deployed scientific agent is not a set. It is a **portfolio**: named skills,
tools and routers, each with a description, competing for the agent's choice on
every turn. Adding a row-correct capability can still make the host worse,
because the new entry changes *selection*, not only coverage. The 2026 evidence
is consistent and strong:

| Result | Number | Source |
|---|---|---|
| Pass rate drop when a known-helpful skill set is expanded to a 202-skill library | **up to 21%** | Skill Shadowing, arXiv:2605.24050 |
| Share of that drop attributed to **skill shadowing** (wrong selection), not context | **up to 68%**; context overhead indistinguishable from zero | ibid. |
| Tool-selection accuracy, <30 candidates → 11,100 candidates | **>90% → 13.6%** | RAG-MCP, arXiv:2505.03275 |
| Selection accuracy vs library size (5–200 skills) | **non-linear phase transition** at a capacity threshold; semantic confusability, not raw size, drives it | Single-Agent with Skills, arXiv:2601.04748 |
| Performance drop from large tool spaces, some models | **up to 85%**; long tool outputs up to **91%** | Tool-Space Interference, Microsoft Research 2026 (survey of 1,470 MCP servers) |
| Name collisions across MCP servers | **775 tools**; "search" appears in 32 servers; largest server exposes 256 tools | ibid. |
| Tool definitions for 2,500 endpoints vs a search+execute surface | **1.17M → ~1k tokens (−99.9%)** | Tool-Surface Compression, Infralovers 2026-06-12 |
| Skill-library gain: human-curated vs LLM-authored | **+16.2pp vs +0.0pp** | SkillsBench, arXiv:2602.12670 (as cited by Library Drift) |
| Premature retirement in a self-evolving library | **−1.9pp** (active harm) | Library Drift, arXiv:2605.19576 |

Two caveats before using these numbers. First, "context overhead" in Skill
Shadowing is the *fixed* cost of carrying more skill descriptions, not the
*variable* cost of tool outputs; the latter can be enormous (the heaviest MCP
tool in the Microsoft survey averaged 557,766 tokens). Our budget \(\beta_H\)
therefore separates fixed description tax, active tool count, and output size.
Second, the 21% figure is a 202-skill library on SkillsBench; a 37-skill
materials host may sit below the knee. Report the host's size and do not
transfer the number.

The design consequence is not "add fewer skills". It is that **admission is a
property of a set, not of a row**, and that **removal is as dangerous as
addition**. This note turns that into a second predicate, a lifecycle action
table, and a retention invariant, then lists what the repo and the paper must
change.

## 1. The 2026 map: four clusters and the empty slot

### A. Library growth degrades selection

- **Skill Shadowing** (arXiv:2605.24050) formalises the drop and decomposes it
  by conditioning on the invoked skill set. Two mechanisms: *shadowing*
  (distractors displace the oracle during selection) and *context overhead*
  (larger context degrades execution after correct selection). Shadowing grows
  with library size and dominates; context overhead stays near zero. Their
  library is built by unioning authored bundles; distractor similarity, not
  bundle structure, causes the failure.
- **Single-Agent with Skills** (arXiv:2601.04748) fits a scaling law
  \(\mathrm{Acc}(|\Sigma|)\approx \alpha/(1+(|\Sigma|/\kappa)^\gamma)\cdot
  \exp(-\epsilon\,\mathcal{I}(\Sigma))\): a capacity threshold plus a semantic
  interference term. Hierarchical routing restores accuracy. This is the closest
  thing to a formal model of the portfolio effect, and it is somebody else's.
- **RAG-MCP** (arXiv:2505.03275), **How Many Tools** (arXiv:2605.24660),
  **Tool-Space Interference** (Microsoft, 2026), **Tool-Surface Compression**
  (2026) measure the same bottleneck on the tool/MCP side: shortlist depth,
  description quality, naming collisions, output size, and the cardinality /
  timing / structure axes. **Progressive Disclosure** (arXiv:2607.17598) gives
  the controlled evidence for on-demand loading.
- **Tool Description Rewrite** (arXiv:2602.20426) shows the interface text
  itself is a lever: descriptions written for humans carry ambiguity agents
  cannot resolve.

Occupied: measurement, decomposition, scaling law, compression. **Not
occupied:** deciding *which* incoming capability may enter a given host, using
evidence external to the library.

### B. Lifecycle governance of skill libraries

- **SkillOps** (arXiv:2605.13716): typed edges (dependency / compatibility /
  redundancy / alternative / lineage) and maintenance operators `merge`,
  `repair`, `retire`, `add_validator`, `add_adapter`. Merge keeps the skill with
  the most validators and unions failure modes. 79.5% on ALFWorld (+8.8pp over
  the strongest baseline) with no extra task-time LLM calls. Library-internal
  health; the trigger is debt, not an incoming work.
- **Dynamic Agent Skills** (arXiv:2607.10113): eight-stage lifecycle
  (admit / repair / prune / …). Library-internal.
- **Library Drift** (arXiv:2605.19576): unbounded accumulation causes retrieval
  degradation and false-positive injection. A governance recipe (outcome-driven
  retirement + bounded active cap + authoring prior) lifts pass@1 from 0.258 to
  0.584 over 100 rounds; **premature retirement costs −1.9pp**. This is the
  strongest evidence that retirement must be evidence-gated, not scheduled.
- **SkillsVote** (arXiv:2605.18401): governance across collection,
  recommendation, attribution, evolution; million-scale corpus profiled for
  environment, quality, verifiability.
- **MUSE-Autoskill** (arXiv:2605.27366): creation / memory / management /
  evaluation / refinement, +15.2pp on SkillsBench.
- **Skill Misevolution** (arXiv:2608.12851): unsafe procedures persist inside
  otherwise useful skills; 525 tasks, 25 episodes. Evolution can entrench harm.
- **WikiSkill** (arXiv:2608.27454): separates raw experience, consolidated
  knowledge, and executable skills; co-evolves skills with a wiki.
- **MCCL** (arXiv:2610.29357): memory lifecycle with a **four-gate retention
  cascade** — preservation, access, utilization, effect. A stored item counts
  only if it survives interference, is retrieved, is used, and changes behaviour.
  This is the right evaluation shape for capability retention, transplanted from
  memory to skills.
- **SkillLearnBench** (arXiv:2604.20087): the first continual skill-learning
  benchmark — 20 tasks across 15 sub-domains, scored at skill quality, execution
  trajectory, and task outcome. The protocol shape for E6.
- **SkillRAE** (arXiv:2605.10114): retrieval-augmented execution; retrieves skill
  evidence and compiles it into context. The "retrieve, do not install" baseline
  in E5.

Occupied: maintenance from experience/outcomes, library health, drift,
retention of memory. **Not occupied:** lifecycle actions selected by an
*incoming scientific work's* typed evidence, with paper-defined validity as the
admission signal.

### C. Distillation and generation from sources

- **SkillFoundry** (arXiv:2604.03964): heterogeneous scientific resources →
  verified skills.
- **Repo-To-Skill / DisCo** (arXiv:2609.02749): 5,353 verified skills from 1,000
  repositories, 20 areas, 178 capability families; skill graphs with routing /
  dependency / composition edges; "no skill enters without verification"; a
  construction record \(R\) keeps evidence, checks, and unresolved gaps. Gains
  under a fixed backbone/harness: MLE-bench +134.3%, PaperBench +34.4%,
  FrontierCS +9.2%, PassNet +14.0%.
- **Paper2Agent** (Nature, s41586-026-11044-y): paper + code → MCP server → chat
  agent; generated tests refine robustness. Creates a *new* agent around the
  paper; it does not align an existing host.

Occupied: source → skill, verification that the skill runs. **Not occupied:**
whether *this* host should own the capability, whether the delivered number is
the paper's quantity under the paper's invalidation conditions, and what the
addition does to the host's existing selection surface.

### D. Host-relative alignment (our existing neighbours)

AutoMat, SciCoQA, BIV / SkillConsist / DCI, Skill Coverage, ClaimReceipt — see
`related-work.md`. Their objects are claims, own-code consistency, intra-package
drift, or trajectory coverage. None admits a set into a host.

### The slot

> **External dual-encoded scientific work supplies the typed evidence that
> selects admission, refusal, and lifecycle action for a *specific* host
> portfolio, with retained tests and a no-live-obligation-lost invariant.**

That sentence is the differentiator against A (measures degradation, no external
evidence), B (evolves from experience, no incoming work), and C (distils from
sources, no host-relative obligation/validity, no portfolio).

## 2. Design: the host as a portfolio

### 2.1 Object

Extend the host:

\[
H=(P_H,\;K_H,\;\Sigma_H,\;\rho_H,\;\beta_H)
\]

- \(P_H,K_H\): products and executed validity checks (unchanged).
- \(\Sigma_H\): installed entries \(\sigma_i=(name_i,d_i,P_i,K_i,prov_i)\),
  including skills, host tools, and MCP-exposed tools (an MCP tool is an entry
  with a description and a schema, not a separate layer). \(d_i\) is the
  **selection description** the router sees, \(P_i\subseteq P_H\) the products it
  delivers, \(K_i\) its checks, \(prov_i\) provenance (source work, commit, date,
  admission record).
- \(\rho_H\): the selection policy. Not assumed observable. We probe it.
- \(\beta_H\): budget — default-context tokens, active tool count, latency.

A work \(W\) induces cards \(C(W)=\{c_1,\dots,c_n\}\), each with a label
\(\lambda\). A card that installs proposes an entry \(\sigma(c)\). Row-level
admissibility is the existing \(\lambda\) table. **Portfolio admissibility** is a
predicate on the set of proposed entries plus the lifecycle plan.

### 2.2 Probes

A probe is a declared tuple

\[
q=(qid,\; text,\; owner,\; expected,\; kind)
\]

where `owner` is the entry that should serve the query, `expected` the product
or observable, and `kind ∈ {route, deliver, validity}`. Probes are **declared,
not generated at verdict time**, and they are retained across runs. The host's
existing entries contribute at least one route probe each; every install card
contributes one deliver probe and, where \(t_v\) applies, one validity probe.

The skill does not execute probes. It writes them into the admission package;
the host (or the experiment harness) executes them. This preserves the
zero-bundle / advice-only contract.

### 2.3 Two conditions, not one

A candidate set \(A\) is **admissible** for \(H\) iff:

1. **Delivery (row).** Every \(c\in A\) is installable under \(\lambda\), and its
   contract is fail-before → green → destroy-red.
2. **Portfolio (set).** After applying \(A\) and the lifecycle plan \(L\):
   - every retained probe still routes to its owner and passes;
   - every new probe routes to the new entry;
   - no co-admitted pair has a host-level procedure conflict
     \(\kappa_H(a,b)=1\);
   - \(\beta_H\) is not exceeded in the default surface (demotion may be used);
   - no live obligation loses its last deliverer (§2.5).

Condition 1 is `typed-introduction.md`. Condition 2 is new. The paper's claim
becomes two-level: *the number is the paper's result* **and** *the host still
works after admission*.

### 2.4 Non-composition (design proposition)

**Proposition (non-composition).** Under any selection model in which accuracy
is non-increasing in a pairwise semantic-interference term \(\mathcal{I}(\Sigma)\)
and \(\mathcal{I}\) is superadditive on overlapping pairs, row-wise admissibility
is not closed under union: there exist \(a,b\) such that \(\{a\}\) and \(\{b\}\)
are each admissible and \(\{a,b\}\) is not.

*Witness.* Let the retained probe \(q\) have owner \(o\) with margin
\(m(q,\Sigma)>0\). Adding \(a\) costs \(\delta_a<m\), adding \(b\) costs
\(\delta_b<m\), but the cross term \(\gamma(a,b)>0\) (shared description facets,
or a procedural conflict) gives
\(m(q,\Sigma\cup\{a,b\})=m-\delta_a-\delta_b-\gamma<0\). The same construction
crosses the capacity threshold in the scaling law even when neither addition
does.

The algebra is trivial; the design consequence is not. It says a **set test** is
required, and it predicts exactly the regime Skill Shadowing measures. We do not
claim the scaling law or the interference term as ours; we use them as the
declared selection model and cite 2601.04748 / 2605.24050 for the empirical
claim that the regime holds.

A second, non-selection form: two cards can each be consistent with the host
doctrine and jointly prescribe incompatible procedures (e.g. one fixes the
equilibrium volume at 0 K, the other at finite \(T\)). That is
\(\kappa_H(a,b)=1\), a *composition* conflict, not a shadowing effect. Both are
caught by the set test; neither is caught row-wise.

### 2.5 Lifecycle actions and the retention invariant

Lifecycle is not a second method; it is how the portfolio stays admissible as
works accumulate. Each action is selected by typed evidence plus portfolio
evidence.

| Action | Trigger | Evidence required | Test |
|---|---|---|---|
| `bind` | \(\lambda=\) both-aligned, product new to host | paper product + repo entry | fail-before → green → destroy |
| `author` | obligation-sans-entry | paper steps | same; no fabricated entry id |
| `extend` | both-aligned, same question as an existing entry | routing probes both ways | old question still routes; neighbour does not absorb the new one |
| `add_validator` | validity-gap | the one-sided invalidation sentence | violating input fails |
| `merge` | two entries have the same product, same procedure, and same regime (a true duplicate); union of checks covers both live obligations; description overlap alone is not a trigger | both entries' probes + no unique product lost | both old probes pass; entry count decreases; interference does not rise |
| `demote` | entry still useful but shadowing risk high | overlap with oracle entries + probe margin | default context shrinks; explicit invocation still works |
| `upgrade` | new work supersedes an entry with a strictly stronger contract | old + new contracts | new probe passes; old probe passes or is explicitly retired |
| `downgrade` | new evidence narrows an existing entry's validity regime (the entry is still useful, but not where it claimed) | the new invalidation sentence + the old probe | old probe passes inside the narrowed regime; outside it fails or routes to a fallback |
| `retire` | entry has no live obligation and no retained probe depends on it | provenance + last-obligation record | removal changes no retained probe |
| `quarantine` | \(\lambda=\) procedure-conflict, or validity unassessed | conflict record | not selectable by default; no silent side chosen |
| `refuse` | entry-sans-obligation | paper silent | host unchanged |

**Retention as reachability.** Let \(O\) be the union of obligations of all
*active* works, and draw an edge \(o\to\sigma\) when entry \(\sigma\) delivers
\(o\). Then:

- **Safety:** no live obligation loses its last deliverer.
- **Liveness:** every live obligation has at least one deliverer.
- **Retire** is allowed only for an entry with no incoming edge from \(O\) and no
  retained probe.
- **Merge** is allowed only if the union of products and checks covers both
  entries' live obligations and the merged description lowers interference.
- **Upgrade** is allowed only if the new entry delivers a superset of the old
  products and passes the old probes.

This is reachability-aware garbage collection over obligations. It explains
Library Drift's −1.9pp: premature retirement violates liveness (it removes a
deliverer while the obligation is still live). It also gives the lifecycle a
proof obligation instead of a schedule: *retirement is safe iff nothing live
points at the entry*.

### 2.5.1 Fusion relations

Before choosing a lifecycle action, classify the candidate against each existing
entry. The classification is a decision over declared fields, not over prose
similarity:

\[
\sigma=(Q,P,\mathrm{Pre},\mathrm{Post},R,\mathrm{Proc},K,\mathrm{Prov}),
\]

where \(Q\) is the triggering question, \(P\) the delivered products,
\(\mathrm{Pre}/\mathrm{Post}\) the conditions, \(R\) a named validity regime,
\(\mathrm{Proc}\) the procedure, \(K\) the checks/invalidation conditions, and
\(\mathrm{Prov}\) the evidence. Every field is declared; no field is inferred from
a description.

| Relation | Predicate | Allowed action |
|---|---|---|
| `covered` | `same_product ∧ same_procedure ∧ regime_subset ∧ ¬checks_missing` | `no-op` |
| `partial` | `same_product ∧ same_procedure ∧ (¬same_regime ∨ checks_missing)` | `add_validator` / `upgrade` / `downgrade` / `split` |
| `duplicate` | `same_product ∧ same_procedure ∧ same_regime ∧ ¬checks_missing` | `merge` |
| `variant` | `same_product ∧ ¬same_procedure ∧ ¬regime_overlap` | `split` / `demote` |
| `hard-conflict` | `same_product ∧ ¬same_procedure ∧ regime_overlap` | `quarantine` / `refuse` |
| `subsumes` | `products_superset ∧ checks_superset ∧ regime_superset` | `upgrade` |
| `subsumed` | `products_subset ∧ checks_subset ∧ regime_subset` | `no-op` |
| `adjacent` | `¬same_product ∧ question_overlap` | `extend` / `new-entry` |
| `unrelated` | `¬same_product ∧ ¬question_overlap` | `new-entry` / `no-op` |

`same_procedure` includes the pre/post contract: an incompatible precondition is a
different procedure. Fusion `covered` is not the gap table's `equivalent`; the gap
table keeps its own six classes.

The nine relations collapse to four typed graph edges, so the vocabulary can be
read alongside ecosystem-governance work: `dependency` (adjacent with a stated
prerequisite), `compatibility` (covered/partial/subsumed), `redundancy`
(duplicate), and `alternative` (variant/subsumes). SkillOps derives merge
candidates from redundancy edges; cap-align keeps that restriction and adds the
fail-closed evidence ladder below, because a redundancy edge is a structural
classification, not a license to delete.

**Decision tree.** Compute the witnesses first; the tree is their reading order.

1. One side strictly stronger (all supersets, at least one proper)? Candidate
   `subsumes` (`upgrade`); old entry `subsumed` (`no-op`).
2. Same product? No → question overlap? Yes `adjacent` (`extend` / `new-entry`);
   no `unrelated` (`new-entry` / `no-op`).
3. Same procedure (including pre/post)? No → regime overlap? Yes `hard-conflict`
   (`quarantine` / `refuse`); no `variant` (`split` / `demote`).
4. Same regime and no missing check? `duplicate` (`merge`).
5. Regime subset and no missing check? `covered` (`no-op`).
6. Otherwise `partial` (`add_validator` / `upgrade` / `downgrade` / `split`), or
   `hard-conflict` when pre/post cannot both hold.

**Merge safety (only for `duplicate`).** Union products and checks; do not lose a
unique product or a live obligation. Intersect the regimes; the merged entry claims
only what both claim. Union provenance. Keep both test contracts. Rewrite the
description as one question, not a concatenation, and rerun both route probes. The
entry count falls while portfolio coverage does not; interference must not rise.
Record rollback (restore both entries, descriptions, and probes). If the union
cannot cover both live obligations, use `split` or `demote`, not `merge`.

**Prefer validator insertion to merge.** When the only gap is a missing check,
`add_validator` precedes `merge` or `split`. SkillOps found validator insertion to
be the most valuable single maintenance action; merge and repair alone had
limited effect and paid off mainly in combination. This gives a cheap repair path
before any structural compression.

**Merge evidence ladder (from the structure-compression literature).** Field
union is necessary but not sufficient. SkillZip Pro reports that an
evidence-free 71–76% compression lost 18–26 accuracy points, one-sidedly, by
deleting exemption rules ("when not to act"); structural coverage does not by
itself preserve behavior. cap-align therefore treats each merge as a set of
auditable deletions:

- *One witness per deletion.* `W1` literal inclusion is preferred, then `W2`
  deterministic coverage, then `W3` restricted entailment by a frozen checker.
  No witness vetoes the merge; a second witness on the same unit is an error.
  The removed source entry (`entry:<card_id>`) is itself a deletion.
- *W3 is barred from obligations and outputs.* Obligations, output fields, and
  units carrying a prohibition/exemption/output marker admit only W1/W2.
- *Locked residual.* Units that cannot be parsed or witnessed are preserved
  verbatim (`unit`, `reason`, `verbatim`), never deleted. The intended failure
  mode is under-compression, not silent loss.
- *Hard surface coverage.* The union of both sides' triggers, workflow edges,
  tool requirements, obligations, and output fields must equal
  `coverage ∪ removed_units ∪ locked_residual`; coverage may not invent units.
- *Recall commit gate.* Both sides' retained probes are declared in
  `recall_probes` and replayed; an observed failure vetoes the commit. This is
  the statically checkable core of SkillGLoW's commit gate (which reserves a
  held-out recall estimate and commits a whole round only above an anchor).
- *Interaction check.* A declared pairwise \(\hat\beta_{ij} < -0.15\) requires an
  extended regression check with evidence, following SkillSmith's interaction
  matrix. A zero beta means "not estimated", not "independent".
- *Never inflate.* If the merged surface costs more than the two entries cost
  separately, keep both (or `split`/`demote`); an audit that passes without an
  improvement is not a reason to compress.
- *No borrowed causal claim.* `evidence_level` is `constructive`, `model`, or
  `statistical`; the last requires a randomized design with \(n_{\text{trials}}>0\).
  Similarity clustering, soft scores, and pre/post means are not causal evidence.

Two mechanisms are deliberately not imported. SkillGLoW's all-or-nothing round
commit is an execution policy, while cap-align only records rollback advice.
SkillSmith has no rollback on a failed merge; here rollback is a precondition for
admission. The structural checks establish the absence of *known* silent loss,
not behavioral equivalence; the latter needs host probes and remains E5/E6 work.

**Conflict policy.** Do not adjudicate a `hard-conflict`: record both procedures,
regimes, and evidence, quarantine the pair, and remove it from the default router.
Apparent conflicts split by regime: same product and different procedure but
disjoint regimes become two `variant` entries with explicit routing.
`env_conflict` (dependency, version, installation) is a host-environment issue, not
a scientific conflict.

**Worked example (phonopy × MatDiscovery).**

- `qha` vs `eos`: thermal expansion from minimizing \(F(V,T)\) vs an \(E(V)\)
  Birch–Murnaghan fit. Different products, overlapping question → `adjacent` →
  `new-entry`; the shared "equation of state" wording is not duplication.
- `lattice-kappa` (BTE) vs `heat-flow` (BTE): same product and procedure, different
  regime → `partial` → `split`, not `variant`.
- A Slack-model kappa at overlapping temperature vs `heat-flow`: same product,
  different procedure, overlapping regime → `hard-conflict` → `quarantine`. At a
  disjoint low-temperature regime it is `variant` → `split` / `demote`.
- `band-structure`: no host entry for phonon dispersion → `unrelated` →
  `new-entry`.
- `force-constants` and `phonon-dos`: paper-silent, repo-present → `refuse` at the
  row layer; `unrelated` → `no-op` at the portfolio layer.
- Joint shadow: `qha` and `kappa-bte-lowT` each cost 0.2 on `q-heat-flow-route`
  with margin 0.3. Either alone is safe; add-all is \(0.3-0.2-0.2=-0.1\) and
  fails. Demoting `qha` restores 0.1. Row-wise safety is not closed under union;
  this is why the set test exists.

### 2.6 Admission algorithm (advice only)

1. **Row filter.** Drop `refuse`, `procedure-conflict`, `insufficient-evidence`.
   Keep install candidates in priority order (fix-wrongness > honor-promise >
   extend-surface).
2. **Build the portfolio record.** Freeze \(\Sigma_H\), its descriptions, its
   route probes, and \(\beta_H\).
3. **Pairwise checks.** For each candidate and each existing entry, compute
   description overlap and \(\kappa_H\); flag pairs above threshold. Report the
   interference graph, not a single score.
4. **Greedy set test.** Add one candidate at a time. After each addition, run
   the retained probes (declared). If a retained probe breaks, try in order:
   `merge` with the nearest entry → `demote` out of the default router →
   `defer`. Never silently accept the break.
5. **Lifecycle plan.** Merge duplicates; upgrade superseded entries; retire only
   unreachable entries; quarantine conflicts. Every action carries the probe
   that justifies it.
6. **Package.** Emit cards + probes + lifecycle plan + budget delta + rollback
   (the exact entries and checks to restore). Do not execute.

The output is richer than a card, but it is still advice. The host owns the
placement and the merge.

### 2.7 Packaging: plugin, manifest, or plain card set

The same admission package can be shipped three ways without changing the
method:

1. **Card set (default).** Markdown report + JSON; the host reads it and edits
   itself. This is the current zero-bundle contract.
2. **Admission manifest.** The `portfolio` block is a machine-readable manifest:
   proposed entries, descriptions, probes, lifecycle plan, budget delta,
   rollback. A host plugin manager may consume it; cap-align still does not
   install.
3. **Plugin bundle.** Only if the host's plugin format can carry (a) the new
   skill/tool, (b) the lifecycle policy, and (c) the retained probes. The bundle
   is a *delivery* format, not a new method; it must not smuggle the reference
   agent or MCP server in as the runtime (rule 6 still applies).

Do not make the plugin the unit of analysis. The unit is the host portfolio and
the evidence that licenses an entry.

### 2.8 Concrete mechanisms to borrow from AREX-Skill

The cloned library (`/tmp/capalign-external/AREX-Skill`, Apache-2.0) already
implements several mechanisms our design needs; borrow the mechanism, not the
method:

- **Entry provenance record** (`references/repo-provenance.md`, schema
  `disco.repo-provenance.v1`): source remote, branch, commit, package versions,
  evidence roots (docs/examples/tests/requirements), `reference_only` paths, and
  **refresh signals** ("commit differs", "public signature changes"). Our
  `prov_i` should be this shape, plus the paper arm (DOI/arXiv id, method
  section, validity sentence).
- **Routing metadata** (`repo-routing-metadata.json`): `taxonomy_sha256`,
  `routing_status`, assignments with area/family and confidence. Our
  `portfolio` block should carry a taxonomy/description hash so a merge or
  re-description invalidates the old probe rather than silently reusing it.
- **Atomic import contract**: skill, metadata, indexes, and router are updated
  together under a shared lock. Admission should be one atomic package with a
  rollback record, not a sequence of independent edits.
- **`disable-model-invocation: true`** is a real `demote`: the entry remains
  installed and explicitly invocable, but is out of the model's default
  selection surface. Prefer this to deletion when an entry is still live.
- **"Do not force a route"** when no family fits is the router-side analogue of
  our refusal: an unmatched request stays general rather than being forced onto
  a nearby entry.

## 3. Metrics

| Metric | Definition | Why |
|---|---|---|
| **Retention** \(R\) | pass rate on retained probes after minus before | the portfolio condition, directly |
| **Shadowing risk** \(SR(a)\) | max over probes of relevance of \(a\) relative to the owner, or the measured margin drop | static proxy for the dominant effect; do not call it a measurement of shadowing |
| **Interference** \(\mathcal{I}(\Sigma)\) | count and max of pairwise description overlaps above threshold | the scaling-law term; report as a graph |
| **Context tax** | tokens added to the default surface (router line only under progressive disclosure) | separate from interference; do not conflate |
| **Portfolio coverage** | live obligations with a deliverer / live obligations | liveness |
| **Orphan rate** | entries with no live obligation and no probe | retirement candidates |
| **Churn** | lifecycle actions per admitted work | self-evolution cost |
| **Admission precision** | admitted entries later retired / admitted, over a replay | longitudinal quality |

`t_v`, FI, Miss, and the fail-before/destroy-red contract are unchanged.

## 4. Experiments

**E5 — portfolio admission (cross-sectional).** Host library of 20–40 entries;
add one work's cards. Arms: add-all, oracle (only the new entry), portfolio-gated
(merge/demote as needed), refuse-new, retrieve-only (RAG shortlist). Measure
retention, new-capability pass, probe flips, interference, context tax. Prediction
from A: add-all loses retention; portfolio-gated ≈ oracle. This is the C4
experiment.

**E6 — lifecycle replay (longitudinal).** Replay 5–8 works or successive
versions of one work into the host. Arms: no lifecycle, retire-only,
merge-only, full evidence-gated. Measure pass@1, portfolio coverage, size,
orphans. Prediction from Library Drift: no-lifecycle drifts; scheduled
retirement harms; reachability-gated retirement preserves. This is the C5
experiment and the expensive one.

**E7 — mechanism replication (cheap).** Replicate the Skill Shadowing
decomposition on the materials host: is the drop (if any) selection or context?
This is a sanity check, not a contribution.

**Minimum for ACL.** E5 plus a worked lifecycle example (one merge, one retire,
one upgrade) is enough for a fourth contribution; E6 can be a follow-up. The
paper must not claim E6 results it has not run.

## 5. Paper framing

### 5.1 Claim

Keep the current headline and add the second half:

> A delivered number counts only if the paper defines the quantity and the run
> executes that definition inside the paper's invalidation conditions — **and
> the host still selects and delivers its retained capabilities after the new
> one is admitted.**

Short form: **green is not the paper's result; correct is not yet admissible.**

### 5.2 Contributions

- **C1–C3** unchanged (coverage fork; typed introduction \(I\), refusal, \(K_H\);
  contract acceptance).
- **C4 — Portfolio admission (new, provisional).** Row-correct introduction is
  not host-safe. Admission is a predicate on capability sets because selection
  degrades through semantic interference, not context length; two individually
  safe cards can jointly shadow a retained entry. The paper gives the predicate,
  the probe format, and the E5 protocol. Related work: Skill Shadowing,
  Single-Agent Skills, RAG-MCP, Library Drift.
- **C5 — Evidence-gated lifecycle (new, provisional).** Merge / retire / upgrade
  / downgrade / demote / quarantine are selected by typed evidence plus
  reachability; no live obligation loses its last deliverer. Retention makes
  retirement auditable and explains why scheduled retirement harms. E6 or a
  worked example.

If the paper must stay at three contributions, fold C5 into C4 as "the set
predicate and its maintenance" and keep E6 out of the claims.

### 5.3 Related-work rows to add

| Work | Their question | Ours |
|---|---|---|
| Skill Shadowing (2605.24050) | How much does a larger library hurt, and is it selection or context? | Which incoming capability may enter, and what set test licenses it |
| Single-Agent Skills (2601.04748) | Scaling law of selection vs library size | Use interference as an admission cost, not only a diagnosis |
| Library Drift (2605.19576) | Why self-evolving libraries stagnate; governance recipe | External work supplies the evidence for each retire/merge, not outcome logs alone |
| SkillOps (2605.13716) | Library-internal merge/repair/retire | Lifecycle triggered by a paper's obligations and validity |
| Dynamic Agent Skills (2607.10113) | Eight-stage library lifecycle | Same stages, but admission evidence is dual-encoded \(W\), not experience |
| Repo-To-Skill (2609.02749) | Distil 1,000 repos into 5k verified skills | Host-relative: refuse, validity, portfolio admission; verification is "the paper's number", not "it runs" |
| Paper2Agent (Nature 2026) | Turn a paper into an MCP agent | Align an existing host; do not create a new agent around the paper |
| MCCL (2610.29357) | Four-gate retention for memory | Four-gate analogue for capabilities; reachability invariant |

### 5.4 Limitations to write now

- The materials host is ~37 skills, below the 202-skill regime where shadowing
  is measured. E5 must scale the library with declared distractors, and the
  paper must say so.
- The selection model is declared, not learned. We report probe flips and
  interference; we do not claim to predict the scaling law's parameters.
- C4/C5 are implemented in the skill and its checker, but unmeasured until
  E5/E6 run; no retention, shadowing, or library-health number is claimed.
- Lifecycle actions are advice; the host executes them. The paper does not
  measure host compliance.

## 6. Repo changes

### P0 — design docs (no behaviour change)

- `docs/portfolio-and-lifecycle.md` (Chinese design authority; **created
  2026-10-23**): object, non-composition, action table + reachability, metrics,
  experiments, change list.
- `docs/typed-introduction.md` §7: add a "portfolio" column or a forward pointer;
  §9 add the admission predicate; §15 note that the next measurement is a set,
  not a row.
- `docs/acl-paper-design.md`: §1.5 C4/C5; §2 rows; §3 E5/E6; §4 limitations.
- `docs/progress.md`: new dated section; priorities.
- `research/related-work.md`: L2 additions (Skill Shadowing, Single-Agent
  Skills, Library Drift, SkillsVote, MUSE, Skill Misevolution, MCCL,
  Repo-To-Skill, Paper2Agent); L3 RAG-MCP / tool-space.
- `README.md`: one line on portfolio admission.

### P1 — skill behaviour (implemented)

- `SKILL.md`: **step 7 "Portfolio admission"** before the report; report is 8,
  self-check is 9. Trigger only when the host has a skill/tool library (≥2
  entries with descriptions). Output: `portfolio` block, admission verdict per
  card, lifecycle plan.
- `references/portfolio-admission.md` (new): definitions, probe schema,
  non-composition, action table, reachability, and what the skill must not
  execute. This is the single source for the lifecycle rules; the card and
  placement references point here rather than restating them.
- `references/report-contract.md`: required **Portfolio admission** section
  (entries, probes, set test, verdict, lifecycle plan, budget, metrics);
  card-level `portfolio` block.
- `references/report-schema.json`: top-level `portfolio` object and conditional
  card-level `portfolio`; `$defs` for entries, probes, set test, and lifecycle.
- `references/evaluation.md`: Layer-1 checks **19–21** — (19) portfolio
  coverage, (20) fusion consistency, (21) lifecycle safety.
- `references/quick-decisions.md`: "which portfolio action?" decision.
- `references/alignment-rules.md`: no separate section; the merge/retire rules
  and the advice-only boundary live in `portfolio-admission.md` §6 and §12.

### P2 — acceptance tests (implemented)

- `tests/fixtures/mini-library/`: two-entry host; ten cards covering all nine
  relations; `qha` and `kappa-bte-lowT` are individually safe but jointly shadow
  `heat-flow`; the add-all arm fails and the gated arm demotes `qha`.
- `tests/fixtures/mini-retire/`: `upgrade` + valid `retire` + a rejected retire
  of the live last deliverer of `lattice-kappa`.
- `tests/README.md`: pass condition is 21 checks plus the named portfolio
  violations.

### P3 — tool (implemented)

- `research/tools/portfolio-model.py` (pure stdlib): validates relation
  witnesses, action pairs, merge safety and the fail-closed merge evidence block
  (witness ladder, surface coverage, locked residual, recall and interaction
  gates, never-inflate, evidence level), lifecycle reachability, probes, set-test
  arithmetic, and budget; emits plan and metrics. It is static: no probe
  execution, no host edit, no LLM call.
- `research/tools/test_portfolio_model.py`: 33 unit cases (33 passing), 12 of
  them for the merge evidence block.

### P4 — paper (design-only)

- `docs/acl-draft/paper.md`: new subsection "From rows to portfolios" + C4;
  C5 only if E6/worked example lands. Update abstract's last sentence. Not yet
  written.

### Implementation status

| Artifact | Path | Status |
|---|---|---|
| Workflow step | `SKILL.md` step 7 | implemented |
| Admission rules | `references/portfolio-admission.md` | implemented |
| Report contract | `references/report-contract.md` §6 | implemented |
| Schema | `references/report-schema.json` | implemented |
| Self-checks 19–21 | `references/evaluation.md` | implemented |
| Static checker | `research/tools/portfolio-model.py` | implemented |
| Unit tests | `research/tools/test_portfolio_model.py` | implemented (33 pass) |
| Portfolio fixtures | `tests/fixtures/mini-library/`, `mini-retire/` | implemented |
| C4/E5 | portfolio admission protocol | implemented, **unrun** |
| C5/E6 | lifecycle plan | implemented, **unrun** |
| Paper subsection | `docs/acl-draft/paper.md` | design-only |

## 7. What not to claim

- Do not claim context overhead is the problem. The evidence says selection is;
  context is small at 202 skills.
- Do not claim shadowing is measured in materials. It is measured on SkillsBench;
  our host is smaller. Say "risk", "probe flip", "interference".
- Do not claim a new scaling law. 2601.04748 owns it; we use it.
- Do not turn cap-align into a runtime router or executor. It emits a plan.
- Do not let `merge` / `retire` be scheduled. Library Drift's −1.9pp is the
  counterexample; reachability is the gate.
- Do not put generic agent plumbing (plugin marketplace, MCP install, env) into
  the portfolio. The scope rules still hold.
- Do not count a demoted entry as admitted to the default surface. Report both.
- Do not report an admission verdict without the probe that could fail.

## 8. Open questions

1. **Probe source.** Can route probes be derived from the host's own skill
   descriptions without circularity? (Declared by the host owner is safer.)
2. **Interference measure.** Lexical overlap is cheap but crude; embedding
   similarity is better but adds a dependency. Start with declared facet overlap
   (product names, input regimes, invariants), not text similarity.
3. **Merge semantics.** SkillOps keeps the entry with the most validators and
   unions failure modes. Is that safe when the two entries have different
   validity regimes? Probably not; merge should require regime compatibility,
   not just validator count.
4. **Rollback.** The package must name the exact commit and entries to restore.
   The host may have moved; the report already records the host commit.
5. **Size of the effect on a 37-skill host.** The knee may be above it. E5's
   distractor scaling is the honest test.
6. **Does a demoted entry still count as host capability?** For coverage, yes;
   for selection, no. Report both, never one.
