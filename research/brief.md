# Research brief — Material Capability Engineering

**Working title:** *From Scientific Software Assets to Agent Capabilities: Representing, Aligning, and Verifying Capability Surfaces for Materials Agents*

**Status:** research brief v0.1 (2026-10-15). Anchor for the paper; capalign (this repo) is the first complete instantiation of the proposed paradigm.

---

## 1. Problem

Materials (computational) software — phonopy, ASE, pymatgen, VASP, QE — is a
half-century pool of *community-verified scientific capability assets*. A materials
agent's capability surface is essentially the interface layer over those assets.
Three observed phenomena, one research question:

1. **Fragmented re-wiring.** Every materials agent (MatDiscovery, El Agente Sólido,
   PolyJarvis, Catalyst-Agent, …) manually rewires the same asset pool. MCP solves the
   transport layer, not the capability-semantics layer.
2. **Claim drift is a real, measured problem.** BIV audited 49,943 skills and found
   **80.0% of declarations diverge from implementation**; Lejaeghere et al. (Science
   2016) showed codes can be cross-validated against each other; AutoMat (2026) showed
   agents reproduce paper claims only ~53% of the time. **These two threads — "codes
   are mutually verifiable" and "agents cannot reproduce claims" — have never been
   joined.**
3. **Three knowledge modalities cannot be unified.** The same capability ("compute
   heat capacity") exists as code (phonopy), method (paper), and recipe (blog). Existing
   work treats each separately: BIV audits skills only, ChatExtract extracts data only,
   MatPROV builds process graphs without software nodes, blog-side is empty.

**Research question.** Can an agent's capability surface be managed as a
first-class, computable object — representable, alignable, verifiable — instead of a
one-off, hand-assembled artifact?

## 2. Methodology — a three-layer closed loop

```
      Represent                          Align                          Verify
repo ──┐                           ┌─ equivalent/partial/            ┌─ evidence-first protocol
paper ─┼─→ Capability IR ──→  host surface ──→ missing/host-only ───→ recommendations
blog ──┘    (typed+evidence)      ref surface      /unknown ×3 sources   (5 questions)
                                                                    └─ fixture gold + determinism
                                       ↑                                      │
                                       └────────── loop: re-inventory ←────────┘
```

- **Represent.** Capability IR: typed capabilities (`compute/tool/workflow/data/interface/concept`)
  + evidence (path:line / quote) + confidence + source kind. Semantic anchors: CORA /
  IEEE 1872 capability ontology (capability-as-conditional-enablement), OWL-S / WSMO
  contracts (IOPE / PAPE).
- **Align.** Five-gap classification (`equivalent/partial/missing/host-only/unknown`)
  × three source kinds (`host-self-audit / reference-contrast / domain-inference`) +
  five-question placement. The matching dimension has mature ancestors — Paolucci's
  four-way service matching (ISWC 2002) and requirements-traceability states (Gotel &
  Finkelstein 1994) — so the claims are *not* "first matching": they are **self-referential,
  cross-source, evidence-gated alignment** on an agent auditing itself.
- **Verify.** Validate-before-classify (every suspected gap is grep-verified against
  host code/artifacts), per-run 8-point self-check, synthetic-fixture gold acceptance,
  same-input determinism re-run. Anchors: BetterBench meta-evaluation × ClaimReceipt
  evidence receipts × reproducibility obligations. Position: registries/credentials
  manage *who signed*, behavioral verification manages *is the code right*; the middle
  layer — "does the claim have mandatory, machine-checkable evidence" — is
  **unsystematized**.

## 3. Contributions

| # | Contribution | Empty where | Theory anchor |
|---|---|---|---|
| 1 | Cross-modal unified capability lattice (repo/paper/blog → one IR) | BIV single-modal; ChatExtract data-only; MatPROV no software nodes; blog side empty | CORA types + DL concept lattice |
| 2 | **Epistemic graded subsumption**: gap classification = semantic matching ∧ evidence thresholds (two-predicate decision) | Paolucci four-way is purely semantic; RE states are purely semantic | Paolucci (ISWC'02) × test-adequacy theory (Zhu 1997) |
| 3 | **Evidence-obligation layer for capability claims** (claim-as-contract + lifecycle: assert → verify → expire → re-audit) | KYA/TessIndex/LEGIT manage custody; drift papers only measure; nobody defines validity/re-verify/revoke semantics | BetterBench × ClaimReceipt × reproducibility obligation |
| 4 | **coverage@reference / promise-drift rate**: library-level metrics | existing metrics are all task-side success rates; nothing demand-side | Test sufficiency (coverage≠adequacy) × FCA/Galois connection |

**Defensive thesis** (against "matching is old"): not "first capability matching" —
that loses to Paolucci/RE — but **"first capability engineering that closes the
represent–align–verify loop onto a self-referential agent"**. Each layer reuses a
named community's formalism; the closure is the novelty.

## 4. Positioning vs. neighbors (system layer)

| Neighbor | System-layer position | Our difference |
|---|---|---|
| Externalization (2604.08224) — capabilities externalized into memory/skills/protocols/harness | most mature "capability engineering" account | no scientific software, no reference anchoring — we instantiate it in materials |
| SkillOps (2605.13716) / SkillFoundry (2604.03964) | skill libs as software ecosystems; heterogeneous resources → skill generation | we produce alignment/gaps/placement, not generation/ops |
| AutoMat (2605.00803) | paper → workflow → verify; 53% reproduction | evaluation only, no representation/alignment; we join it with Lejaeghere's code cross-validation |
| CDD (Capability Driven Development, BISE 2015) | the one complete represent-align-verify framework | organizational processes, not self-referential agents |
| TessIndex / LEGIT / Market-for-Lemons | capability verification into identity/credentials/trust | mechanism layer; we do content-level evidence verification |

Materials anchoring: the field has the most centralized, standardized, community
cross-verified software asset pool (Lejaeghere: 40 codes cross-validated) — the best
testbed for capability engineering.

## 5. Evidence plan (see `experiments.md`)

E1 inter-rater reliability of gap/source classification (κ); E2 before/after task gain
from report-driven capability assembly; E3 coverage@reference / promise-drift evolution
on real libraries incl. stale-skill recall; E4 self-referential alignment reliability
(calibration of self-reported vs verified surface — a theoretical gap).

Case study assets already in hand: phonopy↔MatDiscovery full record (19 gaps, A–E
tiers, three false-gap catches), the real 37-skill MatDiscovery library, and
SKILLS-AUDIT as real claimed-vs-actual drift corpus.

## 6. Risks & defense

- Crowded 2026 field → differentiate on three words: **materials-anchored · evidence-graded ·
  bilateral reference alignment** (not trust layers, not capability-representation
  theory, not skill generation).
- "Matching is not new" → theory pillar = reuse-not-invent (ontology/DL lattice for
  representation; contract/behavioral subtyping for verification; Galois connection for
  metrics); every layer has a named community.
- "Skill-scope too narrow" → frame at the system layer: scientific software assets →
  agent capabilities, with the closed loop as the methodology system.