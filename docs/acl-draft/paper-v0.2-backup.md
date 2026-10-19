# Typed Introduction of Dual-Encoded Scientific Work into Deployed Agents

**Working title (ACL long / Findings).**  
*Typed Introduction: Residual Labels Decide Host Edits and Fail-Before Tests for Dual-Encoded Scientific Work*

**Status.** Draft v0.2 (2026-10-18, Asia/Shanghai). Venue framing: scientific NLP / agent methodology. Insights strengthened via web + AgentRepo deep-read (see `insights-research.md`).  
**Claim scope.** Follows [`../acl-paper-design.md`](../acl-paper-design.md) §1.3 — no fabricated empirical wins; unrun experiments marked `TODO`.  
**Figure X.** [`../figures/typed-introduction/cap-align-typed-introduction.pdf`](../figures/typed-introduction/cap-align-typed-introduction.pdf)

---

## Abstract

Scientific agents and scientific papers arrive on different schedules. A user who already runs a host agent \(H\) and faces a new dual-encoded work \(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\) needs more than a discrepancy detector: they need to know *which host edits are justified* and *which tests must fail before those edits*. We cast paper–repo residual as a typed unit \(u=(p,s,e,v_{\mathrm{p}},v_{\mathrm{r}},\kappa)\) with a unique label \(\lambda\), then define a typed introduction operator \(I\) that maps \(\lambda\) to edits on \(H=(P_H,K_H)\) and a fail-before / destroy-test contract. Relative to wrap-repo, paper-only, and write-directly baselines, counting statements show \(I\) introduces no false products (\(\mathrm{FI}=0\)), that wrap-repo’s false introductions and missed obligations equal the counts of entry-sans-obligation and obligation-sans-entry units, and that wrap-repo and paper-only leave validity checks uninstalled (\(t_v=0\)) on validity-gap units. We treat Fast / Effective / Testable as call count, those counters, and destroy-tests—not slogans. Materials agents are the first instance domain; the type set is frozen and reusable. We do not claim detection SOTA against SciCoQA, nor paper→code execution SOTA; those are orthogonal scientific questions. Multi-work residual measurement, human IRR, and arm-wise implementation tables remain `TODO`.

**Keywords:** scientific agents; dual-encoded specifications; paper–repository residual; typed introduction; fail-before tests; host-relative coverage.

---

## 1. Introduction

### 1.1 Problem

Two piles accumulate at once in scientific computing: **already-deployed agents** whose capabilities live in skills, tools, and runners, and **published works** that arrive as a paper plus a companion repository. A practitioner holding \(H\) and a new \(W\) is not asking “can an agent reproduce this claim?” or “does this paper match its own code?” First they need a decision about *coverage and justified change*:

> Which products of this work does my host already deliver, which residual types justify an edit, and which test must fail *before* that edit?

Stopping at a gap table answers only the first clause. Stopping at discrepancy detection answers a different paper’s question. Neither tells the host *what to change* when paper and repo disagree.

### 1.2 Gap vs SciCoQA and vs reproduction

**Detection** (SciCoQA, ACL 2026 Main) asks whether a paper conflicts with *its own* code, at sentence/claim grain, and reports recall of real discrepancies. **Reproduction / generation** (SA-Bench, LMR-BENCH, SciReplicate, ReproAgent, AutoMat, SkillFoundry) ask whether an agent can regenerate or run code from a paper. Our question is third:

| Question family | Input | Output | Success |
|---|---|---|---|
| Detect | Paper + own code | Discrepancy labels | Recall / F1 of real conflicts |
| Reproduce / generate | Paper (± repo) | Code, run, claim match | Execution / fidelity accuracy |
| **Introduce (ours)** | Incoming \(W\) + **deployed host** \(H\) | Edits \(I(H,\lambda)\) + fail-before tests | FI, Miss, \(t_v\); Fast; Testable |

SciCoQA’s Difference / Paper Omission / Code Omission roughly align with our procedure-conflict / obligation-sans-entry / entry-sans-obligation. **The shared surface is residual taxonomy; the differential is typed introduction on a required host.** Remove \(H\) and the claim collapses to detection.

### 1.3 Insight preview (why residual is not a catalog feature)

Dual encoding is not “two input adapters.” On the same \(H\), \(\mathrm{coverage}(H,W_{\mathrm{paper}})\) and \(\mathrm{coverage}(H,W_{\mathrm{repo}})\) can fork: obligation-sans-entry units appear only on the paper projection; entry-sans-obligation units appear only on the repo projection (Figure X(b); `qha` vs `band`). An untyped edit policy that wraps every entry therefore **installs products the paper never obligated** and **misses products the paper obligated but the repo never exposed**. Residual type is *causal for wrong host edits*, not a bookkeeping field.

Three community takeaways preview the formal sections:

1. **Detection recall is not introduction safety.** SciCoQA shows even the best LLMs recover only \(\approx 46.7\%\) of *real* paper–own-code discrepancies, with Paper Omissions hardest (Baumgärtner and Gurevych, ACL 2026). Dude further shows that naïvely adding a code-oriented detector raises recall but tanks precision via *granularity asymmetry*—paper prose over-interpreted, code trivia over-reported (Liu et al., arXiv:2609.03416). Low detection recall yields *false assurance*; untyped wrapping yields *false introduction*. Both are silent failures of different kinds.
2. **Executability and usage are wrong proxies for host coverage.** SA-Bench finds semantic drift under scaffolds optimized for running code (mean SAU \(\approx 0.221\); Hu et al., 2026). Materials-side evidence in our notes converges: *runnable \(\neq\) scientifically justified* and *skill usage rate \(\neq\) capability gain* (AgentRepo claims: `代码执行不等于可靠科学执行`, `使用率不是技能收益的代理指标`; cf. OmniMatBench / SkillFlow). Nearest-neighbor host skills (`eos` \(\neq\) QHA) must not flip `host_has`.
3. **Green tests can be invalid tests.** TestPrism’s Joint Success Function (fail-on-initial \(\wedge\) accept-all-valid \(\wedge\) reject-all-invalid) is \(\approx 28\%\) where single-reference success is \(\approx 60\%\) (Li et al., arXiv:2610.12289). Our destroy-test is the introduction analogue: if deleting the prescribed bind/steps/check leaves the suite green, the suite was never a validity witness.

Sections 3–4 formalize these; Section 5 keeps empirical cells `TODO`; Section 6 returns to failure modes when identity or faithfulness break.

### 1.4 Contributions

1. **Typed residual for dual-encoded scientific work.** We merge paper and companion-repo slots by product identity into a unit \(u\) and assign a unique type \(\lambda\) (both-aligned, obligation-sans-entry, entry-sans-obligation, validity-gap, procedure-conflict, incongruent). This is a host-facing specification, not a sentence–function discrepancy detector.
2. **Typed introduction operator \(I\).** \(\lambda\) selects edits on an already-deployed host \(H=(P_H,K_H)\) and a fail-before / destroy-test contract. We prove counting statements: \(I\) introduces no false products (\(\mathrm{FI}=0\)); wrap-repo incurs FI and Miss equal to the counts of entry-sans-obligation and obligation-sans-entry; wrap-repo and paper-only leave \(t_v=0\) on validity-gap units; label permutation is a non-vacuous ablation when those types are present.
3. **Contract evaluation protocol.** Against wrap-repo (\(W_{\mathrm{rap}}\)), paper-only (\(P_{\mathrm{aper}}\)), and write-directly, we report Fast (model call count / edit effort to green), Effective (FI, Miss, \(t_v\)), and Testable (red→green→red-on-delete). Materials agents are the first instance domain; the type set is frozen and reusable.

**What we do *not* claim** (see also Limitations): empirical residual rates on \(N\) papers (`TODO` EΔ); human IRR \(\kappa\) (`TODO` E1′; existing same-model pilot is a lower bound only); user-study “faster/more accurate”; detection SOTA vs SciCoQA; paper→code execution SOTA; eight-step instrument loops as contributions.

---

## 2. Related Work

We group neighbors by *scientific question*, not by venue year. Citation detail remains in [`../../research/related-work.md`](../../research/related-work.md); Table 1 is the ACL-facing contrast.

### 2.1 Detect vs introduce vs reproduce

**SciCoQA** (ACL 2026 Main; arXiv:2601.12910) detects paper–own-code discrepancies; best reported real recall is about 46.7%, with Paper Omissions hardest and long contexts / post-cutoff papers worsening recall. Their community takeaway—*missed discrepancies silently provide false assurance*—is orthogonal to ours: we care about *false introductions* when an agent wraps a companion repo into a host. **Dude** (arXiv:2609.03416; EMNLP 2026 Main) diagnoses *granularity asymmetry* (over-interpretation on the paper face; over-reporting on the code face) and shows naïve dual-detection multi-agents raise recall while destroying precision. We adopt both warnings as *design constraints*: units merge by product identity **before** typing; sentence-level residual that invents host gaps is refused; entry-sans-obligation units must not become host products.

**Paper→code fidelity and reproduction**—SA-Bench (arXiv:2608.24252) names *semantic drift* and finds executability scaffolds give limited leverage for scientific fidelity; LMR-BENCH (EMNLP 2025) and SciReplicate-Bench (COLM 2025) show incomplete paper understanding and brittle cross-file reasoning; ReproAgent (EMNLP 2026 Findings; arXiv:2608.24291) argues specifications are *split* (explicit paper obligations vs. implicit repo conventions) and persists both in a generation contract; PaperBench (ICML 2025) finds agents write substantial code yet fail integration, execution, and result match. Untyped skill compilation (SkillFoundry / Repo-To-Skill-style wrap) and claim reproduction (AutoMat) treat the paper or repo as a source of *new* artifacts. Our endpoint is an edit contract on an **existing** host surface, measured by FI / Miss / \(t_v\), not execution accuracy—ReproAgent’s “persistent contract” is a sibling idea for *generation*, not for host-relative introduction.

**Intra-artifact audit**—BIV, SkillConsist, DCI—compare a package to *itself*. Skill Coverage measures trajectory adequacy against a skill’s *own* constraints. Shared vocabulary (“drift,” “coverage”) must not collapse axes: ours is incoming \(W\) vs deployed \(H\).

### Table 1. Positioning (compact)

| Work | Their question | Ours | Shared surface | Diff |
|---|---|---|---|---|
| SciCoQA | Detect paper–own-code discrepancies | Type residual then **introduce** on \(H\) | Taxonomy ≈ conflict / omissions | Host required; \(\lambda\to I\) + fail-before tests |
| Dude (on SciCoQA) | Raise detection F1; grain mismatch | Merge by **product Id** before typing | Cross-modal QA | Refuse sentence-level host gaps |
| SA-Bench / LMR / SciReplicate / ReproAgent | Generate or reproduce from papers | Edit contract on **existing** \(H\) | Spec faithfulness | Not a generation benchmark |
| SkillFoundry | Compile resources → new skills | Gaps relative to **this** \(H\); type chooses edit | Resources → skills | Untyped generation = baseline |
| BIV / SkillConsist / DCI | Package vs own implementation | Incoming \(W\) vs deployed \(H\) | Drift language | Intra-artifact ≠ host-relative intro |
| Skill Coverage | Trajectory vs skill’s own constraints | Coverage of external \(W\) (two projections) | Word “coverage” | Different axis |
| ReproAgent | Persist paper obligations + repo evidence for *generation* | Persist \(\lambda\to I\) for *host edits* | Contract language | Existing \(H\) required; no new repo |
| TestPrism / mutation testing | Joint Success over valid+invalid implementations | Destroy-tests on prescribed host actions | Fail-before spirit | Introduction witness, not suite gen |
| ViewPoints (requirements SE) | Multi-view specs may overlap / contradict; consistency managed, not forced | Paper/repo as dual views; \(\kappa\) undecidable stays 0 | Multi-view inconsistency | Product Id merge replaces inter-view rules |

**Writing discipline.** We do not borrow SciCoQA’s six ML-pipeline category lexicon. We do not list “better detector” as a contribution. The first Related Work paragraph must close detect vs introduce before listing generation neighbors.

---

## 3. Method

Figure X summarizes the pipeline: dual encoding → typed unit → host projection → operator \(I\) with fail-before tests, evaluated against wrap-repo and paper-only on FI, Miss, and \(t_v\). Formal contracts and proofs live in [`../../research/introduction-operator.md`](../../research/introduction-operator.md) and [`../typed-introduction.md`](../typed-introduction.md); this section states definitions, **why** they are shaped this way, and the counting insights.

### 3.1 Dual encoding and product slots

A scientific work \(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\) induces two surfaces of the *same* process when public product names exist, both encodings describe one procedure, and the host surface is enumerable (skills, tools, runners). Materials computing is our first instance because those three conditions co-hold; the type set does not name phonons.

A **unit** is one solicit-able product \(p\), not a file, function, or sentence:

\[
u=(p,\; s,\; e,\; v_{\mathrm{p}},\; v_{\mathrm{r}},\; \kappa).
\]

| Slot | Filled by | Meaning of 1 |
|---|---|---|
| \(s\) | Paper | Ordered procedure to obtain \(p\), with citeable locus |
| \(e\) | Repo | Callable entry that delivers \(p\), with citeable locus |
| \(v_{\mathrm{p}}\), \(v_{\mathrm{r}}\) | Paper / repo docs | Explicit invalidation condition for \(p\) |
| \(\kappa\) | Separate judgment | Both sides have procedures that are *not* the same computation; allowed only if \(s=e=1\) |

Inventories of paper and repo are **independent** (no cross-reading while listing). Merge uses product identity (assumption **Id**), not paraphrase similarity. Unmergeable rows stay unilateral; uncertain Id does not merge. Uncertain \(\kappa\) stays 0 (no invented conflicts).

**Why product slots (insight).** Sentence–function detectors optimize recall of textual conflicts. Introduction needs a grain at which a host can *own* a product: add \(p\) to \(P_H\), install \((p,v)\) in \(K_H\), or refuse. Dude’s grain-mismatch warning becomes operational here: aligning “a sentence” to “a function” can manufacture host gaps that no product identity supports. SciCoQA’s Paper Omission hardness has the same root—*code contains many details the paper need not document*—so treating every callable as an obligation would over-report (Dude’s over-reporting) and inflate FI under wrap-repo. Product slots refuse that inflation before \(\lambda\) is assigned. Classical requirements engineering makes the same multi-view move: ViewPoints treat overlapping specifications as first-class and *manage* inconsistency rather than forcing a premature global merge (Nuseibeh et al., 1994); our analogue is: unilateral rows stay unilateral until Id is decided, and undecidable \(\kappa\) stays 0.

### 3.2 Type label \(\lambda\)

\[
\lambda(u)=
\begin{cases}
\text{incongruent} & s=e=0 \\
\text{obligation-sans-entry} & s=1,\; e=0 \\
\text{entry-sans-obligation} & s=0,\; e=1 \\
\text{procedure-conflict} & s=e=\kappa=1 \\
\text{validity-gap} & s=e=1,\;\kappa=0,\; v_{\mathrm{p}}\neq v_{\mathrm{r}} \\
\text{both-aligned} & s=e=1,\;\kappa=0,\; v_{\mathrm{p}}=v_{\mathrm{r}}.
\end{cases}
\]

**Proposition 1 (partition).** Every well-formed unit receives exactly one label (proof: case on \((s,e)\), then \(\kappa\), then validity asymmetry).

Incongruent units are ignored (no invented products). Procedure-conflict is *not* recoverable from the first four bits: without \(\kappa\), contradictory procedures would be mislabeled both-aligned and wrongly bound into \(H\).

### 3.3 Why dual encoding forks coverage (insight)

Define paper obligations and repo entries \(\mathrm{Obl}(W)=\{p\mid s=1\}\), \(\mathrm{Ent}(W)=\{p\mid e=1\}\). Host \(H=(P_H,K_H)\). Projection \(\mathrm{project}(\lambda,\mathrm{host\_has})\) assigns paper-face and repo-face statuses (`gap`, `absent`, `host-already`, `covered`, `validity-gap`) **without** editing \(H\).

**Causal claim.** Obligation-sans-entry appears as `gap` on the paper face and `absent` on the repo face; entry-sans-obligation reverses the fork. Therefore:

\[
\mathrm{coverage}_{\mathrm{paper}}(H,W)
=\frac{|\mathrm{Obl}(W)\cap P_H|}{|\mathrm{Obl}(W)|}
\quad\text{need not equal}\quad
\mathrm{coverage}_{\mathrm{repo}}(H,W)
=\frac{|\mathrm{Ent}(W)\cap P_H|}{|\mathrm{Ent}(W)|}.
\]

Wrapping every entry improves repo coverage while **hurting** Effective on the paper contract (FI from entry-sans-obligation; Miss from obligation-sans-entry). Mini-ref / phonopy-style slots illustrate: `qha` (obligation-sans-entry) and `band` (entry-sans-obligation) share **no** common missing ids across faces (Figure X(b)). Nearest host skills (e.g., `eos` ≠ QHA free-energy path) are recorded as nearest but \(\mathrm{host\_has}\) stays false—**nearest ≠ covered**.

**Mechanism insight (community takeaway).** Dual encoding is a *coverage fork*, not a retrieval inconvenience. ReproAgent’s split-specification diagnosis (explicit paper obligations vs. implicit repo conventions) explains why a single “faithfulness” scalar collapses two projections; SA-Bench’s finding that executability-oriented scaffolds do not close semantic drift is the generation-side twin of the same fork. For deployed hosts the operational slogan is: **MCP-wrapping the companion repo optimizes \(\mathrm{coverage}_{\mathrm{repo}}\) and can strictly worsen FI/Miss on the paper contract** whenever omission types are present. OWASP’s MCP guidance sharpens the systems reading: connecting a tool surface is not the same as owning a capability under least privilege—tool poisoning / rug-pull / confused-deputy risks argue against treating wrap as introduction (OWASP MCP Security Cheat Sheet).

### 3.4 Operator \(I\) and baselines

| \(\lambda\) | Edit on \(H\) | Fail-before / destroy contract |
|---|---|---|
| both-aligned | Bind repo entry for \(p\); install shared validity if both sides state it | \(p\notin P_H\) → \(p\in P_H\); remove binding → red |
| obligation-sans-entry | Write host-owned procedure from paper; **no** forged entry id | \(p\notin P_H\) → \(p\in P_H\) without fake entry; remove steps → red |
| entry-sans-obligation | **No** edit | Paper test set must **not** require \(p\); \(P_H\) unchanged |
| validity-gap | Bind entry **and** install stated invalidation check | \(t_v=0\) → \(t_v=1\); remove check → \(t_v=0\) |
| procedure-conflict | No silent side choice; leave unresolved record | \(P_H\) unchanged; private side-pick voids the item |
| incongruent | Ignore | — |

Baselines: \(W_{\mathrm{rap}}\) (add every \(e=1\), never write \(K_H\)); \(P_{\mathrm{aper}}\) (add every \(s=1\), no entry bind, no \(K_H\)); write-directly (model writes host capability from paper+repo without reading \(\lambda\)); ablation \(\pi\) swaps obligation-sans-entry ↔ entry-sans-obligation then applies \(I\).

**Assumption Faithful.** Counting theorems assume patches realize the table. We do **not** prove that a given LLM writes such patches; experiments must report green-rate **and** destroy-test failures (tests that stay green after deleting the prescribed action are invalid tests, not alignment success).

### 3.5 Why \(\lambda\) must select the edit (community insight beyond SciCoQA)

Detection tells the community *that* residual exists. Typed introduction tells *which wrong edit* an untyped policy will commit:

- **Proposition 2.** \(I\) adds only products with \(s=1\); hence \(\mathrm{FI}(I)=0\) under Faithful realization on a host that starts without those products.
- **Proposition 3.** If \(P_H\) initially omits the products, \(\mathrm{FI}(W_{\mathrm{rap}})=|\{u:\lambda=\text{entry-sans-obligation}\}|\) and \(\mathrm{Miss}(W_{\mathrm{rap}})=|\{u:\lambda=\text{obligation-sans-entry}\}|\).
- **Proposition 4.** On validity-gap units, \(t_v(H)=\mathbf{1}[p\in P_H]\cdot\mathbf{1}[(p,v)\in K_H]\) equals 1 under \(I\), and equals 0 under \(W_{\mathrm{rap}}\) and \(P_{\mathrm{aper}}\) when the check was initially absent.
- **Proposition 5.** If \(\pi\) swaps the two omission types and at least one such unit exists, there exist \(H\) and tests separating \(I\) from \(I\circ\pi\)—so label shuffle is a **non-vacuous** ablation of whether the implementation *uses* \(\lambda\).

**Knowledge claim.** SciCoQA-style labels become *edit selectors* with falsifiable counting identities. The community gains a contract language for agent maintenance: false introduction, missed obligation, and missing validity check are first-class, separable errors—orthogonal to detection recall and to reproduction accuracy.

Illustrative empty-host counts on filled phonopy / mini-ref slot records (definitions, **not** multi-paper measurement): under \(I\), FI\(=0\); under \(W_{\mathrm{rap}}\) on phonopy slots, FI\(=2\) (`band`, `group-velocity`) and Miss\(=1\) (`lattice-kappa`); validity-gap `qha` / force-constants get \(t_v=1\) only under \(I\). Full multi-work EΔ remains `TODO`.

### 3.6 Fast, Effective, Testable (design implications)

| Name | Definition | Colloquial |
|---|---|---|
| FI | Products added to \(P_H\) with \(s=0\) | False introduction |
| Miss | \(s=1\), \(p\notin P_H\) initially, operator did not add (procedure-conflict non-adds listed separately) | Missed obligation |
| \(t_v\) | Product present **and** invalidation check installed | Validity installed? |
| **Fast** | Model calls (optional: human edits, input size) until fail-before holds and post-edit passes | Speed |
| **Effective** | Per-\(\lambda\) FI, Miss, \(t_v\) (and deltas vs baselines) | Accuracy of introduction |
| **Testable** | Fail-before ∧ pass-after ∧ fail-again after deleting prescribed action; report still-green-after-delete rate | Trustworthiness |

**Insight for scientific agents.** Trustworthiness is not “the model said it matches.” It is a destroy-test: if removing the prescribed bind/steps/check leaves the test green, the check itself was wrong. TestPrism shows single-reference fail→pass overstates suite quality (\(\approx 60\%\) vs Joint Success \(\approx 28\%\)); mutation testing and Joint Success share the spirit of *rejecting invalid implementations*, while our destroy-test asks whether the *prescribed host action* was the reason for green. Rating Roulette (Findings EMNLP 2025) further warns that LLM-as-judge scores can be self-inconsistent (Krippendorff’s \(\alpha\) often \(< 0.8\)); therefore E1′ must report human IRR, and any LLM judge pilot is labeled lower-bound only. Speed is not “we wrote a workflow”; it is call count to the same green contract against write-directly. Papers that only report task win-rate without destroy-tests understate test invalidity; papers that only report call count without FI/Miss understate wrong installs. AgentRepo’s materials-facing claims compress the same lesson: *executable \(\neq\) obligation-satisfying* (`可执行性不是物理建模Agent的停止条件`; Pufibara harness) and *code execution \(\neq\) reliable scientific execution* (`代码执行不等于可靠科学执行`).

---

## 4. Experiments (protocol; results mostly TODO)

We separate **contract counts** (Propositions 2–3, decidable from labeled units + Faithful \(I\)) from **implementation obedience** (whether a model patch realizes \(I\)). Filling the latter without the former confuses definition with engineering.

### 4.1 Protocol overview

| ID | Question | Serves | Status | Submission floor |
|---|---|---|---|---|
| **EΔ** | Same \(W\): residual non-empty and \(\lambda\)-typed | C1 | **TODO** (phonopy/mini slots are illustrations) | ≥1 real pair, independent dual inventories |
| **E1′** | Human IRR on Id / \(\lambda\) / projection | Label trust | Same-model pilot only; **human IRR TODO** | ≥2 annotators; Cohen/Fleiss \(\kappa\) + raw agreement |
| **E2′** | \(I\) vs \(W_{\mathrm{rap}}\) vs \(P_{\mathrm{aper}}\) vs write-directly (+ \(\pi\)) | C2–C3; Props 2–5 | Typed arms **TODO** | Same human-labeled units; FI/Miss/\(t_v\) by \(\lambda\) |
| **Fast** | Calls to green vs write-directly | Speed def. | **TODO** | Matched tasks |
| **Testable** | Destroy-test still-green rate | Trust def. | Contract written; **batch TODO** | Report invalid-test rate |

Legacy instrument IRR (five-way gap classes; same-model judges) may appear in an appendix as an instrument reliability pilot—not as calibrated human IRR, and not as typed-introduction Effective.

### 4.2 Result tables (placeholders — do not invent numbers)

**Table 2. Residual mix (EΔ) — TODO**

| Work pair | #units | \(\lambda\) histogram | Paper∩Repo missing ids | Notes |
|---|---|---|---|---|
| mini-ref (illustration) | 6 | obl.-sans-entry:1; entry-sans-obl.:5 | empty intersection | Fixture; not a measurement claim |
| phonopy paper × docs (illustration) | 7 | both-aligned:2; validity-gap:2; entry-sans-obl.:2; obl.-sans-entry:1 | — | Slot fill; host projection not frozen in that pass |
| Real pair #1… | TODO | TODO | TODO | Independent inventories |

**Table 3. Human IRR (E1′) — TODO**

| Layer | Annotators | \(\kappa\) / agreement | Disagreement themes |
|---|---|---|---|
| Product Id | TODO | TODO | Boundary products |
| \(\lambda\) | TODO | TODO | \(\kappa\) undecidable → 0 |
| Projection | TODO | TODO | nearest vs covered |
| Same-model pilot (appendix only) | 3 judges, 1 model | See `research/runs/e1/` | Not human IRR |

**Table 4. Introduction arms (E2′) — TODO**

| Arm | FI | Miss | \(t_v\) on validity-gap | Destroy still-green | Calls to green |
|---|---|---|---|---|---|
| \(I\) | TODO (contract: 0 if Faithful) | TODO | TODO (contract: 1) | TODO | TODO |
| \(W_{\mathrm{rap}}\) | TODO (= #entry-sans-obl. if empty \(P_H\)) | TODO (= #obl.-sans-entry) | TODO (0) | TODO | TODO |
| \(P_{\mathrm{aper}}\) | TODO | TODO | TODO (0) | N/A bind destroy | TODO |
| write-directly | TODO | TODO | TODO | TODO | TODO |
| \(I\circ\pi\) | TODO | TODO | TODO | TODO | TODO |

Report **contract expected counts** and **realized counts** in separate columns when implementation may violate Faithful.

### 4.3 Illustrative (non-claim) empty-host phonopy counts

From filled slot records only—**not** a substitute for Table 4:

| Operator | FI | Miss | \(t_v\) on validity-gap rows |
|---|---|---|---|
| \(I\) | 0 | 0 (excl. conflicts; none in this fill) | 1 on `qha`, force-constants |
| \(W_{\mathrm{rap}}\) | 2 | 1 (`lattice-kappa`) | 0 |
| \(P_{\mathrm{aper}}\) | 0 | 0 | 0 |
| \(I\circ\pi\) | 2 | 1 | 1 (validity-gap untouched by \(\pi\)) |

---

## 5. Discussion

### 5.1 Three scientific questions

Detect, reproduce, and introduce answer incompatible evaluation targets. Competing on SciCoQA recall or on SA-Bench / PaperBench scores would be a **category error**: a perfect detector still does not choose host edits; a perfect reproducer may wrap a repo that installs entry-sans-obligation products into \(H\); AutoMat’s materials claim-reproduction further shows agents can match scalars while leaving the scientific claim unverified (`数字对、主张没验证` in AgentRepo AutoMat notes). Typed introduction makes residual *actionable* under an explicit error decomposition (FI / Miss / \(t_v\)).

**Community takeaway.** Peer review and agent ops need *three* instruments, not one: (i) discrepancy detectors for paper↔own-code faithfulness; (ii) reproduction / semantic-alignment benches for paper→code generation; (iii) typed introduction contracts for *already-deployed* hosts facing new dual-encoded works. Collapsing (iii) into (i) or (ii) recreates wrap-repo’s FI/Miss identities.

### 5.2 Residual as cause of wrong edits

The fork \(\mathrm{coverage}_{\mathrm{paper}}\neq\mathrm{coverage}_{\mathrm{repo}}\) is the mechanism behind Proposition 3. Any agent toolchain that “just MCP-wraps the companion repo” inherits wrap-repo’s FI and Miss identities whenever omission types are present. That is a **systems insight** for scientific agent maintenance, independent of materials jargon. Dude’s dual-detection result and SciCoQA’s Paper Omission hardness jointly explain *why* wrap looks attractive (repos expose concrete callables) and *why* it is unsafe (many callables are not paper obligations; many obligations lack entries). Dynamic capability expansion can still be the right lever when the *typed* obligation is missing (`动态能力扩张是突破静态工具集天花板的关键杠杆` in AgentRepo)—but expansion must be selected by \(\lambda\), not by entry presence.

### 5.3 Fail-before tests as trust infrastructure

Fail-before + destroy-tests operationalize trustworthiness for LLM-written patches. Green-only metrics conflate lucky tests with correct installs—TestPrism’s gap between single-reference and Joint Success is the clearest recent quantification; mutation testing is the classical SE ancestor. Agent harness literature in our notes flags the complementary gap: *external verifiability* (tamper-evident checks a third party can audit without trusting the runtime) is still largely absent from production harnesses (`Harness外部可验证性空白`). Destroy-tests are a minimal, local form of that demand for introduction patches. We recommend always reporting still-green-after-delete, and treating LLM-judge-only green rates as non-claims until human IRR exists (Rating Roulette).

### 5.4 Call count as the honest “Fast”

“Faster alignment” without a matched green contract invites process theater. Fast is defined only relative to write-directly (or another untyped writer) on the **same** fail-before suite.

### 5.5 Failure modes (negative insights)

| Failure | What breaks | Honest handling |
|---|---|---|
| **Id fails** | Merge invents or splits products | Do not merge; no residual claimed across unilateral rows |
| **\(\kappa\) undecidable** | Conflict vs both-aligned | Keep \(\kappa=0\); never invent conflict |
| **nearest treated as covered** | False host_has | nearest logged; \(\mathrm{host\_has}=\bot\) |
| **Faithful breaks** | Theorems’ antecedents false | Report obedience rate; do not cite Prop. 2 as empirical FI=0 |
| **Cross-reading while inventorying** | Residual erased | Enforce separate passes (write-directly is the baseline that cheats this) |
| **Open-ended chat agents** | Non-enumerable \(P_H\) | Out of scope until surface is freezable |
| **Methodology prose in judge context** | Inflated agreement | Line-bounded reads; disclose contamination |
| **MCP wrap as introduction** | FI from entry-sans-obligation; privilege confusion | Treat wrap as \(W_{\mathrm{rap}}\) baseline, not \(I\); pin tool manifests |
| **Usage / nearest as coverage** | False `host_has` | Log nearest; require product Id match; usage ≠ gain |
| **LLM-judge-only Effective** | Self-inconsistent labels | Human IRR required; report \(\alpha\), not accuracy alone |

### 5.6 Domain scope

We require co-holding of public product names, dual encodings of one process, and an enumerable host surface. Computational materials is instance one; computational biology-style domains that satisfy the same trio are transfer checks **with \(\lambda\) frozen**—not a reason to open the claim to arbitrary chat agents.

---

## 6. Limitations

(1) *Unrun residual measurement.* Multi-work EΔ beyond illustrative phonopy / mini-ref slots is incomplete; dual-encoding remains partially hypothetical until that table exists. (2) *Annotation reliability.* Existing classification agreement is a same-model three-judge pilot, not human IRR; Id and \(\kappa\) need human protocols before calibrated-labeling claims. (3) *Faithful patches.* Counting theorems assume edits realize the operator table; we do not prove that a given LLM writes such patches—experiments must report green-rate and destroy-test failures. (4) *Domain scope.* Public product names, dual encodings of one process, and an enumerable host surface must co-hold; we do not claim arbitrary chat agents. (5) *Neighbor metrics.* We do not compete on SciCoQA detection recall or on paper→code execution accuracy. (6) *Intra-package drift* numbers are decomposition context, not headline results. (7) *Contamination risk* in pilot judging (methodology prose entering context) requires line-bounded reads in the released protocol.

---

## 7. Ethics statement (draft notes)

This work studies alignment of public scientific papers and repositories to agent capability surfaces. It does not collect personal data. Risks: (i) over-trust in automated introduction if Faithful is assumed without destroy-tests; (ii) silent side choice on procedure-conflict if implementations ignore the unresolved-record rule; (iii) dual-use of scientific software wrapping—mitigated by host-owned capability requirement (no nesting of a reference agent as runtime). Annotator studies (`TODO`) should use public texts and disclose agreement protocols. We will release slot schemas, labeling guides, and scripts used for EΔ/E1′/E2′ when those runs complete.

---

## 8. Conclusion

We reframed paper–repo residual from a detection target into a **typed introduction contract** for deployed scientific agents: \(\lambda\) selects edits on \(H\) and fail-before tests; wrap-repo and paper-only baselines admit countable FI, Miss, and \(t_v\) failures that \(I\) avoids under Faithful realization. Remaining work is measurement—human IRR, multi-work EΔ, and obedience tables—not further taxonomy. Detection and reproduction remain valuable, orthogonal problems; introduction is the missing third.

---

## Appendix A. Figure X caption

> **Figure X.** Typed introduction for dual-encoded scientific work. (a) Paper and repo slots are merged by product identity into a unit \(u\) and labeled by a unique type \(\lambda\). (b) The same \(\lambda\) projects to different host gaps on the paper vs repo face—illustrated on mini-ref / phonopy-style slots `qha` and `band`, which share no common missing ids. (c–d) Operator \(I\) maps \(\lambda\) to edits on \(H=(P_H,K_H)\) and fail-before tests; against wrap-repo (\(W_{\mathrm{rap}}\)) and paper-only (\(P_{\mathrm{aper}}\)), typed introduction is contractually better on false introduction (FI), missed obligations (Miss), and validity checks (\(t_v\)), with Fast / Effective / Testable reported as call count, those counters, and destroy-tests.

## Appendix B. Document map

| Path | Role |
|---|---|
| This file | ACL English draft (v0.2 insights) |
| [`insights-research.md`](insights-research.md) | Deep-research notes + bibliography → insight map |
| [`../acl-paper-design.md`](../acl-paper-design.md) | Writing pack / claim scope |
| [`../typed-introduction.md`](../typed-introduction.md) | Design authority (ZH + formal) |
| [`../../research/introduction-operator.md`](../../research/introduction-operator.md) | Operator proofs |
| [`../paper-core.md`](../paper-core.md) | Instrument identity (gap-table endpoint) |
| [`../progress.md`](../progress.md) | Empirical status |

## Appendix C. Checklist (from acl-paper-design §7)

- [x] Intro contributions = typed residual / \(I\) / contract protocol
- [x] Related Work opens detect vs introduce (SciCoQA)
- [x] Method figure = Figure X; caption has no fake rates
- [x] Experiments mark TODO; illustrative counts labeled non-claim
- [x] Limitations include EΔ, human IRR, Faithful, scope, neighbor metrics
- [x] No eight-step / capability-lattice / intra-package drift as contributions
- [x] Insight paragraphs cite SciCoQA / Dude / SA-Bench / ReproAgent / TestPrism / Rating Roulette / ViewPoints / MCP; AgentRepo claims paraphrased with paths
- [ ] `research/brief.md` / `abstract.md` aligned (updated in same revision pass)
