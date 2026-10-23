# Related work (four layers)

All arXiv IDs verified. Grouped by the layer of the system they operate on.
Direct neighbours of **this** paper are: AutoMat (reproduce a claim),
SkillFoundry (compile skills from resources), SciCoQA / paper–code consistency
(paper vs *its own* code), BIV / SkillConsist / DCI (package vs *its own*
implementation), Skill Coverage (trajectory vs a skill’s own constraints). Our
object is an incoming work \(W=(\mathrm{paper},\mathrm{repo})\) against an
already-deployed host \(H\). **Manuscript claim (2026-10-18):** typed residual
\(\lambda\to I\) — see `docs/acl-draft/paper.md` and `docs/acl-paper-design.md` §2;
do not position this paper as detection-only.

Updated 2026-10-16: added 2026-06..10 neighbours that occupy intra-package
audit, skill coverage, and paper–code discrepancy. The 2026-02 SoK remark that
“proactive drift detection is largely absent” is **expired** after BIV (May).

## L1 — Formalism for capabilities (theory anchors, reused not invented)

- **IEEE 1872-2015 / CORA** — IEEE Standard Ontologies for Robotics and Automation
  (10.1109/IEEESTD.2015.7084073). Capability = `mechanism → capability → action`
  ontology chain; capability as *conditional enablement* — the static skeleton for
  our `type` lattice.
- **Semantic Matching of Web Services Capabilities** — Paolucci et al., ISWC 2002.
  Four-way DL concept matching `exact / plugin / subsume / fail` — the direct ancestor
  of our `equivalent / partial / missing`.
- **OWL-S** (W3C 2004) / **WSMO** (Applied Ontology 2005) — capability as IOPE / PAPE
  contract; WSMO adds "what the caller must know" — our `unknown` class.
- **An analysis of the requirements traceability problem** — Gotel & Finkelstein,
  ICRE 1994. `satisfied / partial / unsatisfied / undetermined` states — the five-gap
  ancestor; traceability matrix = our gap table.
- **Capability Driven Development & Capability Management in Digital Enterprises** —
  Bēržiša et al., BISE 2015 / Springer 2018. The one complete represent–align–verify
  framework, but for organizational processes, not self-referential agents.
- **A behavioral notion of subtyping** — Liskov & Wing, 1994; **Signature matching**
  for software libraries, Zaremski & Wing, 1995 — verification-layer anchors.
- **Software Unit Test Coverage and Adequacy** — Zhu, Hall & May, ACM CSUR 1997.
  coverage ≠ adequacy; the axiomatics behind coverage@reference.
- **Formal Concept Analysis** — Ganter & Wille, 1999. Concept lattices / Galois
  connections — alignment as a lattice adjunction decomposed by evidence kind.
- **MCQS / Autonomous Assessment of Generalizability of AI Agent Capabilities** —
  Bramblett et al., arXiv:2512.16733. Capability as conditional output distribution;
  the *runtime verification* semantics — deliberately not our static representation.
- **The Agent Capability Problem** — Lutati, arXiv:2512.07631. Information-theoretic
  solvability bound; a budget semantics for coverage@reference.

## L2 — Agent skill ecosystems & capability engineering (system layer)

- **SoK: Agentic Skills — Beyond Tool Use in LLM Agents** — arXiv:2602.20867. Skill
  lifecycle (discovery / practice / distillation / storage / composition / evaluation /
  update). The 2026-02 remark that proactive drift detection is "largely absent"
  is expired after BIV (May 2026); do not cite it as a novelty gap.
- **Externalization in LLM Agents** — arXiv:2604.08224. Capabilities externalized into
  memory / skills / protocols / harness; capability-as-infrastructure thesis.
- **SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software
  Ecosystems** — arXiv:2605.13716. Skill technical debt; library lifecycle;
  typed HSEG relation graph, redundancy-edge merge candidates, field-level patch,
  validator insertion as the highest-value single maintenance action.
- **SkillZip / SkillZip Pro / Tan et al. (structural compression)** —
  arXiv:2608.11079 / arXiv:2608.30785 / arXiv:2608.05604. Typed skill contracts,
  MDL minimization, hard coverage, locked residual, and the W1/W2/W3 deletion
  witness ladder. Evidence-free compression loses exemption rules; cap-align
  imports the witness ladder and coverage constraints, not the compression claim.
- **SkillGLoW** — arXiv:2609.02217. Procedure-clustered global priors with a
  held-out recall commit gate (anchor −0.02). cap-align keeps the gate idea but
  checks declared recall probes statically; it does not cluster or rewrite skills.
- **SkillSmith** — arXiv:2606.01314. Lineage crossover and an interaction matrix
  \(\hat\beta_{ij}<-0.15\) feeding merge/retirement. cap-align imports the
  negative-interaction gate and adds the rollback precondition SkillSmith lacks.
- **SKILLFOUNDRY** — arXiv:2604.03964. Heterogeneous scientific resources → verified
  skills; generation-centric, no host alignment, no gap table. Closest generation
  neighbour: they melt modalities into skills; we keep paper/repo as two encodings
  of a specification and align them to an existing host.
- **Formal Skill** — arXiv:2605.19604. Runtime-native executable skill objects
  (JSON schema, executors, hooks). Representation of a skill, not host-relative
  alignment to a scientific work.
- **Dynamic Agent Skills** — arXiv:2607.10113 (TMLR). Eight-stage lifecycle of
  evolving skill libraries (admit / repair / prune). Library-internal; no incoming
  paper+repo spec.
- **SkillComposer** — Generative skill composition; composition bottleneck, gold-skill
  51.1% vs no-skill 22.2%.
- **A Framework for Evaluating Agentic Skills at Scale** — arXiv:2606.17819. 500
  skills, 1,000 tasks derived from skill content. Evaluates a skill, not a host
  against a scientific work.
- **An Empirical Study of Agent Skills' Downstream Utility** — arXiv:2610.08875.
  The same skills help some configurations and hurt others on 36.8% of tasks.
  Constraint on E2: coverage ≠ utility unless configurations are held fixed.
- **Skill Coverage** — arXiv:2606.20659. Trajectory-based test adequacy of a
  skill’s own constraints (~39–45% covered on SkillsBench). Name collision with
  our `coverage@reference`; their axis is the skill artifact, ours is an external
  scientific work \(W\).
- **Packaged, But Not Portable** — arXiv:2609.23809. Conforming to Agent Plugins v1.0.0
  is rare and insufficient; form ≠ content.
- **A Survey of Agent Skills / Procedural Infrastructure** — C. Yang, preprint 2026.

### L2b — Library growth, selection interference, and lifecycle (2026-10)

- **More Skills, Worse Agents? Skill Shadowing** — arXiv:2605.24050. A 202-skill
  library cuts pass rate by up to 21%; decomposition attributes up to 68% of the
  drop to **skill shadowing** (wrong selection), with context overhead
  indistinguishable from zero. Their object is a library growing by unioning
  bundles; ours is admission of an external work. We borrow the decomposition and
  the probe idea, not the headline.
- **When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail**
  — arXiv:2601.04748. Selection accuracy follows a non-linear scaling law with a
  capacity threshold and a **semantic interference** term; hierarchical routing
  restores accuracy. The formal support for non-compositional admission
  (`research/portfolio-lifecycle.md` §2.4). We use their law; we do not claim it.
- **Library Drift** — arXiv:2605.19576. Unbounded accumulation causes retrieval
  degradation and false-positive injection; governance recipe lifts pass@1
  0.258→0.584 over 100 rounds; **premature retirement −1.9pp**. The empirical
  case for reachability-gated retirement.
- **SkillsVote** — arXiv:2605.18401. Lifecycle governance over collection,
  recommendation, attribution, evolution; million-scale corpus profiled for
  environment, quality, verifiability. Experience-side; no incoming \(W\).
- **MUSE-Autoskill** — arXiv:2605.27366. Creation / memory / management /
  evaluation / refinement; +15.2pp on SkillsBench. Self-evolution from tasks.
- **Practice Makes Unsafe: Skill Misevolution** — arXiv:2608.12851. Unsafe
  procedures persist inside otherwise useful skills (525 tasks, 25 episodes).
  Why admission needs evidence *before* practice, not only outcome logs.
- **Memory-Centric Continual Learning** — arXiv:2610.29357. Three-axis taxonomy
  (substrates / assets / policies), inner state loop + outer policy loop, and a
  **four-gate retention cascade** (preservation, access, utilization, effect).
  The evaluation shape we transplant to capability retention.
- **Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills** —
  arXiv:2609.02749. 5,353 verified skills from 1,000 repositories; skill graphs
  with routing / dependency / composition edges; construction record keeps
  evidence, checks, unresolved gaps; no skill without verification. Gains under a
  fixed backbone: MLE-bench +134.3%, PaperBench +34.4%, FrontierCS +9.2%,
  PassNet +14.0%. Closest generation neighbour: they distil sources into a global
  library; we decide what *this* host should admit, with refusal and validity.
- **Paper2Agent** — Nature, s41586-026-11044-y (2026). Paper + code → MCP server →
  chat agent; generated tests refine robustness. Creates a new agent around the
  paper; does not align an existing host.
- **Tool-selection scale**: **RAG-MCP** (arXiv:2505.03275; >90% at <30 candidates
  → 13.6% at 11,100), **How Many Tools** (arXiv:2605.24660; shortlist depth as the
  object, chance-corrected), **Tool-Space Interference** (Microsoft Research
  2026; 1,470 servers, 775 name collisions, largest server 256 tools, large tool
  spaces up to −85% for some models), **Tool-Surface Compression** (2026;
  2,500 endpoints = 1.17M tokens vs search+execute ≈1k). Together: the bottleneck
  is interface/selection, not only context length.
- **Progressive Disclosure** — arXiv:2607.17598. Controlled study of on-demand
  skill loading; the timing axis behind `demote`.
- **Learning to Rewrite Tool Descriptions** — arXiv:2602.20426. Description
  quality as a reliability lever; supports treating \(d_i\) as an admission
  object, not prose.

## L3 — Claim verification, audit, and trust (direct neighbors)

- **Behavioral Integrity Verification for AI Agent Skills (BIV)** — arXiv:2605.11770.
  49,943 skills; 80.0% declared-vs-actual drift; typed set comparison of a skill
  against *itself*. Occupies intra-package drift; our headline is host-relative
  coverage of an incoming work, not a second 80%-style number.
- **SkillConsist** — arXiv:2608.07639. Bidirectional graph alignment of declaration
  vs implementation inside one skill package (F1 87.93% on 633 skills).
- **Description-Code Inconsistency in MCP servers (DCI)** — arXiv:2606.04769.
  19,200 description–code pairs, 9.93% inconsistent. MCP tools vs their code.
- **PL-HCL** — arXiv:2607.10534. Cross-layer misalignment (metadata / instructions /
  resources) inside a skill package.
- **Do Skill Descriptions Tell the Truth?** — arXiv:2605.12875. Description vs
  executable implementation; security-disclosure goal (SKILLSCOPE, 9.4% confirmed
  inconsistency on 4,556 skills).
- **Why Static Skill Inconsistencies Do Not Equate to Runtime Risks** —
  arXiv:2610.18927. Static contract defects ≠ runtime harm. Constraint on any
  static gap table, including ours: E2 must show task consequences.
- **SciCoQA** — arXiv:2601.12910. Paper–code discrepancy detection; best models
  recall 46.7% of real discrepancies. Sentence/claim grain, paper vs *its own*
  repo.
- **Do Papers Match Code?** — arXiv:2603.22018. Bioinformatics sentence–function
  consistency (BioCon, 48 projects). Same grain family as SciCoQA.
- **Capability Advertisement as a Market for Lemons** — arXiv:2606.03034. Trust-layer
  theory; mechanism level, no content-level verification.
- **TessIndex** (arXiv:2608.21942), **LEGIT** (arXiv:2609.21325), **KYA**
  (arXiv:2605.25376), **ANS** (arXiv:2604.26997) — custody/credential layers; who
  signed, not whether true.
- **BetterBench** — arXiv:2411.12990. Meta-audit of benchmarks; our per-run
  self-check's ancestor.
- **ClaimReceipt** — arXiv:2609.01992. Evidence sufficiency + coverage receipts for
  evaluation claims — the closest "claim as evidence-bearing contract".
- **Auditing Discovery Claims** (arXiv:2608.00981) — two-sided criterion, negative side
  decidable; agentic-science claim audit.
- **Registry Descriptions Go Stale Unevenly** (arXiv:2608.00997) and **Same Name,
  Different Server** (arXiv:2609.14119) — MCP drift measurement; drift measured, no
  validity/re-verify/revoke mechanism.
- **SkillTrace** (arXiv:2608.05204), **AgentRFC** (arXiv:2603.23801) — provenance and
  conformance auditing pipelines.

## L4 — Materials & AI-for-science systems

- **Trends in atomistic simulation software usage** — Talirz, Ghiringhelli & Smit,
  arXiv:2108.12350. The one census of the simulation software ecosystem.
- **Reproducibility in DFT calculations of solids** — Lejaeghere et al., Science 2016.
  40+ codes cross-validated — "code as mutually verifiable scientific claims".
- **Can Coding Agents Reproduce Findings in Computational Materials Science?
  (AutoMat)** — arXiv:2605.00803. 53% best reproduction; worst when workflows must
  be reconstructed from paper text alone. Our C3 reads this as coverage against
  \(W_{\mathrm{paper}}\) without \(W_{\mathrm{repo}}\).
- **From AI for Science to Agentic Science** — arXiv:2508.14111. Agentic-science
  survey; capability-governance question unanswered.
- **A Survey of AI for Materials Science** — arXiv:2506.20743. Materials task/tool/data
  landscape.
- **Extracting accurate materials data from research papers** — Polak & Morgan,
  Nat. Commun. 2024. Data extraction; not method/tool requirements.
- **MatPROV** — arXiv:2509.01042. Process provenance graphs; no software nodes.
- **CompMat-Bench** (arXiv:2610.00636) / **MatToolBench** (arXiv:2609.37053) —
  task benchmarks with failure attribution (science-vs-software; cross-tool handoff).
- **SciAgentGym** (arXiv:2602.12984) — 1,780 domain tools; long-chain tool
  orchestration as bottleneck.