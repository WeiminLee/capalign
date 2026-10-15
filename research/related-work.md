# Related work (three layers)

All arXiv IDs verified. Grouped by the layer of the system they operate on; the
third group is our direct neighbors.

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
  update); drift detection "largely absent".
- **Externalization in LLM Agents** — arXiv:2604.08224. Capabilities externalized into
  memory / skills / protocols / harness; capability-as-infrastructure thesis.
- **SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software
  Ecosystems** — arXiv:2605.13716. Skill technical debt; library lifecycle.
- **SKILLFOUNDRY** — arXiv:2604.03964. Heterogeneous scientific resources → verified
  skills; generation-centric, no host alignment, no gap table.
- **SkillComposer** — Generative skill composition; composition bottleneck, gold-skill
  51.1% vs no-skill 22.2%.
- **Packaged, But Not Portable** — arXiv:2609.23809. Conforming to Agent Plugins v1.0.0
  is rare and insufficient; form ≠ content.
- **A Survey of Agent Skills / Procedural Infrastructure** — C. Yang, preprint 2026.

## L3 — Claim verification, audit, and trust (direct neighbors)

- **Behavioral Integrity Verification for AI Agent Skills (BIV)** — arXiv:2605.11770.
  49,943 skills; 80.0% declared-vs-actual drift; single-modal skill audit, no alignment.
- **Do Skill Descriptions Tell the Truth?** — arXiv:2605.12875. Description vs
  executable implementation consistency; security-disclosure goal, not capability
  truthfulness.
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
  (AutoMat)** — arXiv:2605.00803. 53% best reproduction — agent-side claim failure.
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