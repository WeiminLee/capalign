# Research brief — Host-relative alignment of dual-encoded scientific works

**Working title:** *From Scientific Works to Agent Capabilities: Host-Relative Alignment of Dual-Encoded Specifications*

**Status:** research brief v0.2 (2026-10-16). Identity revised: the object is an
incoming scientific work \(W=(\mathrm{paper},\mathrm{repo})\) aligned to an
existing host agent \(H\). cap-align is the measurement instrument, not the
contribution. Canonical Chinese statement: `docs/paper-core.md`.

---

## 1. Problem

Materials science now accumulates two piles at once: deployed materials agents
(MatDiscovery, El Agente Sólido, PolyJarvis, Catalyst-Agent, …) and published
works that arrive as a **paper plus a companion repository**. A user holding
their own agent and a new paper needs a decision, not a re-implementation:

> Which capabilities of this paper does my agent already have, which are missing,
> and where should each gap land on my architecture?

Three neighbouring questions are already occupied:

1. **Reproduction.** AutoMat (2026) asks whether an agent can run a paper claim
   to completion (best setting ~53%). That is task success, not host coverage.
2. **Generation.** SkillFoundry compiles heterogeneous scientific resources into
   new skills. The output is a skill package, not a gap table against *this* host.
3. **Intra-artifact audit.** BIV / SkillConsist / DCI compare a skill (or MCP
   tool) with *its own* implementation. SciCoQA / paper–code consistency compare
   a paper with *its own* code at sentence–function grain.

**Research question.** Can a published scientific work be treated as a capability
specification and aligned, evidence-gated, to an already-deployed scientific
agent — and do the paper encoding and the repo encoding specify the same surface?

“Quick” is the operational corollary of a **static decision procedure**: no
execution of the reference, no implementation of the gap. It sits *before*
generation and *before* reproduction.

## 2. Methodology — a decision procedure (instrument, not contribution)

```
W_paper ──┐
          ├──→ Capability IR ──→ Gap(H, W) ──→ placement (5 questions)
W_repo  ──┤     (typed+evidence)   five-way × 3 sources
H_host  ──┘                        evidence-gated
                 │
                 └── coverage(H, W_paper)  vs  coverage(H, W_repo)
```

- **Specification.** \(W=(W_{\mathrm{paper}}, W_{\mathrm{repo}})\) induces two
  surfaces. Identity across encodings uses one predicate: semantic match
  \(\in\{\mathrm{exact},\mathrm{plugin},\mathrm{subsume}\}\) and evidence
  strength \(\ge\theta\). Blog is a third encoding; the paper pins paper/repo.
- **Decision procedure.** \(\mathrm{Gap}(H,W)\): five-way class × three source
  kinds + placement. Validate-before-classify; low-confidence evidence cannot
  alone yield `missing`; adding evidence may turn `unknown→missing` and never
  the reverse without a host artifact. Output stops at recommendations.
- **Coverage.** \(\mathrm{coverage}(H,W)\) is reference-conditioned: the paper
  projection and the repo projection can (and, we claim, do) fork. Intra-artifact
  `promise-drift` is a decomposition term, not the headline metric.

Represent / align / verify is the *shape of the instrument*. Closed loops are
common in 2026 skill systems; they are not a contribution.

## 3. Contributions

| # | Contribution | Assertion | Experiment |
|---|---|---|---|
| **C1** | **A scientific work is a dual-encoded capability specification.** Paper methods and companion-repo interfaces share an identity predicate; taking only one encoding leaves the specification incomplete. Distinct from intra-package declaration–implementation audit and from sentence–function paper–code discrepancy. | Residual \(\Delta(W_{\mathrm{paper}},W_{\mathrm{repo}})\) is non-empty and classifiable | **EΔ** (unrun; phonopy paper vs phonopy repo) |
| **C2** | **Host-relative alignment is a decision problem.** \(\mathrm{Gap}(H,W)\) is static, evidence-gated, reproducible, and stops at placement. Distinct from reproducing a claim (AutoMat) and from compiling skills (SkillFoundry). | A (evidence monotonicity); IRR on both the repo arm and the paper arm | E1 (P1 κ=0.853, P2 κ=1.000; same-model judges) |
| **C3** | **Coverage is reference-conditioned.** \(\mathrm{coverage}(H,W_{\mathrm{paper}})\) and \(\mathrm{coverage}(H,W_{\mathrm{repo}})\) diverge; residual type tells wrap-the-interface from honour-the-method. Distinct from Skill Coverage (trajectory vs a skill’s own constraints) and from BIV’s 80% intra-package drift. | Assembly along the paper spec vs the repo spec yields different task-gain shapes | E2 (protocol ready; gold pending) |

Self-audit bias (E4) hangs off C2: whether the host can stand in for an external
alignment against incoming \(W\). Stale-skill recall (old assertion E) is
governance follow-on, not a headline contribution.

**Defensive thesis.** Matching is old (Paolucci / RE). The claim is host-relative
alignment of a dual-encoded scientific work, plus the finding that coverage forks
with the encoding. The skill is the instrument; the residual and the
reference-conditioned coverage are the paper.

## 4. Positioning vs. neighbours

| Neighbour | Their question | Ours |
|---|---|---|
| AutoMat (2605.00803) | Can the agent reproduce this claim? | Which capabilities of this work does the host already cover? |
| SkillFoundry (2604.03964) | Can resources be compiled into skills? | Where does each gap land on *this* host? Stop at advice. |
| SciCoQA (2601.12910) / Do Papers Match Code? (2603.22018) | Does this paper match *its own* code? | Does this paper+repo, as a spec, sit relative to *another* agent? |
| BIV (2605.11770) / SkillConsist (2608.07639) / DCI (2606.04769) | Does a skill/tool match its own implementation? | Does an incoming work get covered by the host? |
| Skill Coverage (2606.20659) | Did the trajectory exercise the skill’s own constraints? | Did the host cover the external scientific work? |
| SkillOps (2605.13716) | Library-internal merge / repair / retire | Demand-side: a new work against an existing surface |
| ClaimReceipt / TessIndex / Lemons | Credentials, identity, market mechanisms | Content-level, host-relative evidence gates |
| Externalization (2604.08224) / CDD | Capability-as-infrastructure / organisational processes | Scientific work → deployed scientific agent |

Materials is the instance: many agents, many paper–repo pairs, the deepest
community-verified software pool (Lejaeghere). The generic method names no host
file and no domain lexicon.

## 5. Evidence plan (see `experiments.md`)

- **E1** IRR of \(\mathrm{Gap}(H,W)\) on a repo arm and a paper arm (C2).
- **EΔ** residual \(W_{\mathrm{paper}}\bowtie W_{\mathrm{repo}}\) on a paired
  work (C1/C3 lifeline; unrun).
- **E2** assembly along paper spec vs repo spec vs random / none (C3).
- **E3** library-level distribution of \(\mathrm{coverage}(H,W)\); intra-package
  drift demoted to an appendix decomposition.
- **E4** self-report vs externally verified surface against incoming \(W\) (C2).

Seed corpus: phonopy↔MatDiscovery (19 gaps, A–E tiers, three false-gap catches)
and the 37-skill host library.

## 6. Risks & defense

- Crowded 2026 skill-audit field → differentiate on **host-relative · dual-encoded
  scientific work · reference-conditioned coverage**. Intra-package drift, skill
  generation, and claim reproduction are occupied.
- “Matching is not new” → grant Paolucci/RE; the object is \(W\) against \(H\),
  with a residual between encodings.
- “Two input adapters” → the paper must lead with the residual (C1/C3), or
  dual-modality collapses to a product feature. EΔ is therefore first priority.
- Empirics currently cannot carry a findings-first paper (EΔ unrun, E2 gold
  pending, E4 unfalsifiable on mini). Method+phenomenon identity (C1–C3 as
  definitions plus a residual measurement) is the honest present tense.
