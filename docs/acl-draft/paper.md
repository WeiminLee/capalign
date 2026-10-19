# Coverage Fork and Typed Introduction: Residual Labels Select Host Edits, Refusal, and Validity Checks

> **Version.** Draft **v0.4.4** (2026-10-18, Asia/Shanghai). Status/gaps pointer only; method/protocol still as v0.4.3. **C1–C3 substance unchanged.** No new empirics.  
> **Claim authority.** [`../acl-paper-design.md`](../acl-paper-design.md) §0–§1.2; [`innovation-proposals.md`](innovation-proposals.md) DECIDED.  
> **Rule.** No fabricated empirics; unrun cells marked `TODO`. Illustrative phonopy / mini-ref slot counts are *not* multi-work results.  
> **Status / gaps.** Story core (C1–C3 + typed edit + destroy contract) is written; **ACL-blocking gaps are empty experiment tables** (EΔ / human IRR / four-arm+\(π\) / destroy batch / ≥2 real pairs). Full inventory: [`gaps-and-todos-v043.md`](gaps-and-todos-v043.md). Run plan: [`experiment-checklist-v043.md`](experiment-checklist-v043.md).  
> **Figure X.** [`../figures/typed-introduction/cap-align-typed-introduction.pdf`](../figures/typed-introduction/cap-align-typed-introduction.pdf)  
> **Formal proofs.** [`../../research/introduction-operator.md`](../../research/introduction-operator.md) (Props. 1–5). Design: [`../typed-introduction.md`](../typed-introduction.md). Insights map: [`insights-research.md`](insights-research.md).

---

## Abstract

A practitioner who already runs a host agent \(H\) and faces a dual-encoded scientific work \(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\) needs more than a discrepancy detector and more than a code generator. The first question is host-relative: which products of \(W\) does \(H\) already deliver; which residual *types* justify an edit; which types justify *refusal*; and which test must fail *before* any edit. We show that dual encoding **forks host coverage**: after independent paper/repo inventories are merged by *product identity*, the paper-face and repo-face host-gap sets can be disjoint. Unique residual type \(\lambda\) then selects a typed introduction operator \(I\) on \(H=(P_H,K_H)\) that both installs products and *paper-grounded* validity checks \(K_H\) *and* treats refusal of entry-sans-obligation, procedure-conflict, and incongruent units as success (not a failed run). Counting identities prove \(\mathrm{FI}(I)=0\); wrap-repo’s FI and Miss equal the two omission-type counts; wrap-repo and paper-only leave \(t_v=0\) on validity-gap units. Acceptance is a fail-before → green → destroy-red contract (Effective = FI / Miss / \(t_v\); Testable = destroy still-green rate; Fast = call count only when measured). Materials agents are instance one; \(\lambda\) is frozen. We do not claim detection SOTA (SciCoQA) or paper→code SOTA. Multi-work EΔ, human IRR, and arm tables remain `TODO`.

**Keywords:** scientific agents; dual-encoded specs; coverage fork; typed introduction; principled refusal; structured refusal; criterion provenance; validity checks; fail-before tests; host-relative coverage.

---

## 1. Introduction

### 1.1 The missing question

Deployed scientific agents and published paper+repo works arrive on different schedules. Holding a frozen host surface \(H\) and a new dual-encoded work \(W\), the practitioner’s first question is not “does this paper match its own code?” (detection) nor “can an agent regenerate the code?” (reproduction), but:

> Which products of \(W\) does \(H\) already deliver; which residual types justify an edit of \(H\); which types require *principled refusal*; and which test must fail *before* that edit?

A gap table answers only coverage. A discrepancy detector answers a different paper. A reproduction loop optimizes a new artifact. None of them says *what to change on an existing host* when paper and repo disagree—or when they agree on products but disagree on *when those products are scientifically invalid*.

### 1.2 Three families, three endpoints

| Family | Input | Output | Success |
|---|---|---|---|
| Detect | Paper + own code | Discrepancy labels | Recall / F1 |
| Reproduce | Paper (± repo) | Code / run / claim match | Fidelity / exec. |
| **Introduce (ours)** | \(W\) + **deployed host** \(H\) | \(I(H,\lambda)\) with refuse + \(K_H\) + fail-before | FI, Miss, \(t_v\); Testable; Fast (optional) |

**SciCoQA** (ACL 2026 Main, SAC Highlight) detects conflicts between a paper and *its own* code, and reports that even strong models recover only a minority of *real* discrepancies (best reported recall \(\approx 46.7\%\); Paper Omissions hardest). Their taxonomy (Difference / Paper Omission / Code Omission) roughly aligns with our procedure-conflict / obligation-sans-entry / entry-sans-obligation. **Shared surface: residual labels. Differential: we require a deployed host \(H\), and \(\lambda\) selects introduction *and refusal* plus validity checks \(K_H\).** Remove \(H\) and the claim collapses to detection—we refuse that collapse.

**Reproduction / generation** (SA-Bench, LMR-BENCH, SciReplicate, ReproAgent, PaperBench, AutoMat, SkillFoundry-style wrap) ask whether agents can write or run code from papers. ReproAgent persists *split* specs (paper obligations + repo conventions) into a *generation* contract; we keep the two faces *separable for introduction*, because fusing them on an existing host recreates wrap-repo’s false introductions. Our endpoint is an edit contract on a frozen host surface, scored by FI / Miss / \(t_v\), not execution accuracy.

### 1.3 Lead insight: coverage fork (C1)

Dual encoding is not two adapters for one coverage number. Define \(\mathrm{Obl}=\{p:s=1\}\) and \(\mathrm{Ent}=\{p:e=1\}\). On one \(H\), paper-face and repo-face host-gap projections can be **disjoint**: obligation-sans-entry gaps appear only on the paper face; entry-sans-obligation gaps only on the repo face (Figure X(b); worked `qha` vs `band`). In classical SE bidirectional-traceability language, the paper-face host gap is an **orphan obligation** (requirement without an owned host realization); the repo-face gap is a **phantom entry** (callable without a paper obligation). Wrapping every repo entry therefore **installs products the paper never obligated** (FI / phantoms) and **misses products the paper obligated but the repo never exposed** (Miss / orphans). Collapsing to either face alone is contractually wrong whenever both omission types are nonempty: **no single-face policy can be both FI\(=0\) and Miss\(=0\)** when orphans and phantoms coexist.

This is the knowledge claim detection cannot state: without a host, there is no coverage of \(H\) to fork. It is also what industry MCP / skill wrap silently optimize against—connect maximizes \(\mathrm{coverage}_{\mathrm{repo}}\) by definition (OWASP: connect \(\neq\) least-privilege ownership).

### 1.4 Supporting insights (why type is causal)

Three community takeaways motivate C2–C3; none is a contribution bullet by itself.

1. **Detection recall \(\neq\) introduction safety.** Low SciCoQA recall yields *false assurance* (missed real conflicts). Untyped wrapping yields *false introduction* (FI). Dude shows naïve dual-detection can raise recall while destroying precision via *granularity asymmetry*—sentence↔function alignment invents gaps no product identity supports. Both failures are silent and orthogonal.
2. **Runnable / used \(\neq\) host-covered.** SA-Bench: semantic drift persists under executability scaffolds. Materials-side methodological notes converge: code execution \(\neq\) reliable scientific execution; skill *usage* \(\neq\) capability gain; stop conditions must bind obligations, not “it compiled.” Nearest host skills (`eos` \(\neq\) QHA) must not flip `host_has`.
3. **Green tests can be invalid.** TestPrism: Joint Success ≪ single-reference success. Our destroy-test is the introduction analogue—if deleting the prescribed bind/steps/check leaves the suite green, it was never a validity witness. Rating Roulette: LLM-judge scores can be self-inconsistent; human IRR is required before labeling claims.

### 1.5 Contributions (locked C1–C3)

1. **C1 — Coverage-fork residual (model + insight).** Independent paper/repo inventories are merged by *product identity* into units \(u=(p,s,e,v_{\mathrm{p}},v_{\mathrm{r}},\kappa)\); the induced paper-face and repo-face host-gap sets can be *disjoint*. Unique type \(\lambda\) partitions residual (including validity-gap and procedure-conflict). Dual encoding is not two adapters for one coverage number—a detection taxonomy without host \(H\) cannot state this fork. Lead with *fork*, not “six labels.”
2. **C2 — Typed introduction \(I\) with principled refusal and \(K_H\).** \(\lambda\) maps to edits of \(H=(P_H,K_H)\) *or* to non-introduction (entry-sans-obligation / procedure-conflict / incongruent). Counting: \(\mathrm{FI}(I)=0\); wrap-repo FI/Miss equal omission-type counts; only \(I\) installs \(t_v=1\) on validity-gap (Props. 2–4). Label permutation \(\pi\) is a non-vacuous ablation (Prop. 5). **Refusal is part of correctness, not a failed run.**
3. **C3 — Contract acceptance protocol.** Against wrap-repo (\(W_{\mathrm{rap}}\) / MCP-attach), paper-only (\(P_{\mathrm{aper}}\)), and write-directly, report Effective (FI, Miss, \(t_v\)) and Testable (fail-before → green → destroy-red); Fast (calls to green) only when measured. Materials (or any domain with public products + enumerable host) is instance one; \(\lambda\) frozen. Reproduction fidelity and detection recall are the wrong scalars for host introduction.

**Not claimed:** multi-work residual rates (`TODO` EΔ); human IRR (`TODO` E1′); user-study “faster/more accurate/more trustworthy”; SciCoQA detection SOTA; paper→code SOTA; “six λ taxonomy” as the contribution; eight-step instrument loops as contributions.

---

## 2. Related Work

Neighbors by *scientific question*. Bibliography map: [`insights-research.md`](insights-research.md); citation store: [`../../research/related-work.md`](../../research/related-work.md).

### 2.1 Detect

**SciCoQA** (ACL 2026; arXiv:2601.12910) frames paper↔own-code discrepancy detection and documents low recall of real conflicts → *false assurance*. **Dude** (EMNLP 2026; arXiv:2609.03416) raises detection F1 but diagnoses *granularity asymmetry* and over-reporting: dual-detection can raise recall while destroying precision when sentence\leftrightarrow function grains invent mismatches that no product identity supports. **Code Check** (CSPaper productization of SciCoQA-family audit) adds a reverse code\to paper sweep for paper omissions and an adversarial reject gate against duplicates, dead code, and speculative discrepancies. We adopt these as *design constraints*: merge by product Id **before** typing; refuse grain-invented host gaps; entry-sans-obligation must not become host products; do not invent \(K_H\) from weak evidence. We do **not** list “better detector” as a contribution—**Detect ≠ Introduce**. Taxonomy surface-collision is real (their three classes ≈ three of our labels); the wall is **host + introduce/refuse + \(K_H\)**.

### 2.2 Reproduce / generate

**SA-Bench** (arXiv:2608.24252) measures semantic drift under paper→code generation; executability scaffolds do not imply scientific fidelity. **LMR-BENCH**, **SciReplicate-Bench**, **PaperBench** expose incomplete understanding, brittle integration, and early stopping. **ReproAgent** (Findings EMNLP 2026; arXiv:2608.24291) persists split specs for *generation*—the sibling contract language. AutoMat-style claim reproduction can match scalars while leaving the scientific claim unverified. Untyped skill compilation (SkillFoundry / Trace→skill / Repo-To-Skill) is our write-directly / wrap neighbor. Endpoint differs: edit contract on **existing** \(H\), not a new artifact. Competing on their accuracy tables is a category error.

### 2.3 Intra-artifact audit and SE cousins

**BIV / SkillConsist / DCI / Skill Coverage** compare a package or trajectory to *itself*. Shared words (“drift,” “coverage”) must not collapse axes: ours is incoming \(W\) vs deployed \(H\).

**ViewPoints** (Nuseibeh et al., IEEE TSE 1994): multi-view specs may contradict; consistency is *managed*, not forced—motivates unilateral rows and \(\kappa=0\) when undecidable. **TestPrism** / mutation testing: reject invalid suites—motivates destroy-tests. **OWASP MCP** / Agentic Skills Top 10: connect \(\neq\) least-privilege ownership—MCP-wrap is \(W_{\mathrm{rap}}\), not \(I\).

### 2.3b Contracts, gates, and weak suites (design constraints, not our method)

Library / software *admission* neighbors share vocabulary (typed contract, evidence, refuse) but answer a different decision: **foreign dual-encoded \(W\) → already-deployed \(H\)**, with coverage fork and principled refusal.

- **Skill-V / SkillOps** (arXiv:2610.11781 / 2605.13716): versioned falsifiable skill contracts and library health (including validation-gap \(V=\emptyset \approx t_v=0\)). They evolve *in-library* debt; we introduce *incoming* \(W\) into frozen \(H\). Cite as neighbors; do not claim their SOTA.
- **PDD Evidence Chain** (arXiv:2605.12981): admit implementations only with signed structural/behavioral/operational evidence—admission-narrative cousin of our fail-before/green/destroy witnesses.
- **ReqToCode Traceables** (arXiv:2603.13999): requirements as compile-time Traceables (orphan/phantom drift fails the build)—hardens SE orphan/phantom language for paper obligations vs repo callables.
- **install-manifest** smoke / kill_switch and **MCP ABAC discovery filters** (arXiv:2605.18414): install-time contracts and *register ≠ authorize* (unauthorized tools never enter context). Precedent for refuse-by-architecture, not our empirics.
- **Deterministic pre-execution gates** (arXiv:2607.07405) and **Ambient Persuasion** (arXiv:2605.00055): policy-permissive writes can yield *silent wrong state*; soft prompt “stand down” ≠ machine-enforced install refuse. Structured reject is a successful no-op.
- **UTBoost** (ACL 2025) / **STING** (arXiv:2604.01518): weak suites admit wrong patches / surviving variants—green alone is insufficient; motivates destroy-still-green as test-invalid / survivor rate.
- **ChopChop / CodeStruct**: constrained / typed edit action spaces—precedent for closed \(I_\lambda\) operators, not free-form patch text.

### 2.4 Contrast table

| Work | Their Q | Diff vs us |
|---|---|---|
| SciCoQA | Detect paper–own-code | Host required; \(\lambda\to I\) with refuse + \(K_H\) + fail-before |
| Dude | Raise detection F1 | Product-Id merge; refuse grain-invented gaps |
| SA-Bench / LMR / SciReplicate / PaperBench / ReproAgent | Generate / reproduce | Not a generation bench; FI/Miss/\(t_v\) |
| SkillFoundry / Trace→skill | Compile → new skills | Untyped gen. = baseline; gaps relative to *this* \(H\) |
| BIV / Skill Coverage | Package / trajectory vs self | Incoming \(W\) vs deployed \(H\) |
| ViewPoints / TestPrism / OWASP MCP | Multi-view; suite validity; tool connect | Design constraints for Id, destroy-tests, wrap≠\(I\) |
| Skill-V / SkillOps / PDD | Library / software admission contracts | Foreign \(W\to H\); fork + refuse; not in-library evolution |
| UTBoost / STING; MCP ABAC / Ambient Persuasion | Weak suites; discovery ≠ authorize | Destroy survivors; prompt refuse ≠ install gate |

### 2.5 Positioning sentence (for Intro/RW reuse)

> SciCoQA / Dude / Code Check *detect* residual (grain asymmetry, reverse sweep, adversarial reject); ReproAgent *fuses* paper obligations and repo evidence into a generation contract; Skill-V / SkillOps / PDD *admit* in-library or software contracts; wrap-repo / MCP *connects* entries. Typed introduction *keeps faces forked*, grounds \(K_H\) in **criterion provenance** (paper-stated / dual-side invalidation—never invent checks for phantoms), maps each \(\lambda\) to a **typed install-or-refuse** edit on already-deployed \(H\), and admits \(I\) only under **fail-before → green → destroy-red**. Detection and reproduction remain orthogonal.

That sentence is the Related Work wall. Shared vocabulary (contract, residual, coverage, evidence) must not collapse axes.

---

## 3. Method

Figure X summarizes the pipeline: dual encoding → product-Id merge → coverage fork → \(I\) with refuse + \(K_H\) → contract metrics vs \(W_{\mathrm{rap}}\) / \(P_{\mathrm{aper}}\). Proofs: `research/introduction-operator.md`. Design authority: `docs/typed-introduction.md`.

### 3.1 Dual encoding and domain co-conditions

\(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\) when three conditions co-hold: **(i)** public product names the community can agree on; **(ii)** both encodings describe one procedure (not training scripts vs method prose); **(iii)** the host surface is enumerable (skills, tools, runners frozen as text). Materials is instance one because product names are clearest; \(\lambda\) does not name phonons. Domains that satisfy the trio are transfer checks **with \(\lambda\) frozen**—not a license for arbitrary chat agents. Open-ended chat \(P_H\) is out of scope until freezable.

### 3.2 Product slots (grain for introduction)

Unit = one solicit-able product \(p\) (not file, function, or sentence):
\[
u=(p,\; s,\; e,\; v_{\mathrm{p}},\; v_{\mathrm{r}},\; \kappa),
\]
with \(s\)/\(e\) = paper procedure / repo entry (citeable loci); \(v_{\mathrm{p}},v_{\mathrm{r}}\) = explicit invalidation; \(\kappa=1\) only if both sides have procedures that are *not* the same computation (requires \(s=e=1\)). Inventories are **independent**; merge by product identity (**Id**). Uncertain Id → no merge; uncertain \(\kappa\) → 0.

**Why product slots (insight).** Sentence–function detectors optimize textual-conflict recall. Introduction needs a grain a host can *own*: add \(p\) to \(P_H\), install \((p,v)\) in \(K_H\), or refuse. Dude’s grain mismatch and SciCoQA’s Paper Omission hardness share a root—code exposes many callables papers need not obligate—so treating every entry as obligation inflates FI under wrap-repo. Product slots refuse that inflation *before* \(\lambda\). ViewPoints: manage inconsistency; unilateral rows stay unilateral until Id is decided.

What does *not* open a row: package names; invalidation conditions alone (they are slots of a product); incidental inputs mentioned in a procedure; documentation pointing at a missing module (e.g., `docs/qha.md` without `qha.py` → \(e=0\)).

### 3.3 Type \(\lambda\) as partition (means, not headline)

\[
\lambda(u)=\begin{cases}
\text{incongruent} & s=e=0 \\
\text{obligation-sans-entry} & s=1,\; e=0 \\
\text{entry-sans-obligation} & s=0,\; e=1 \\
\text{procedure-conflict} & s=e=\kappa=1 \\
\text{validity-gap} & s=e=1,\;\kappa=0,\; v_{\mathrm{p}}\neq v_{\mathrm{r}} \\
\text{both-aligned} & s=e=1,\;\kappa=0,\; v_{\mathrm{p}}=v_{\mathrm{r}}.
\end{cases}
\]

**Prop. 1 (partition).** Exactly one label per well-formed unit (case on \((s,e)\), then \(\kappa\), then validity equality). Incongruent units are ignored. Without \(\kappa\), conflicts would mislabel as both-aligned and wrongly bind into \(H\). Hand labels that disagree with the boolean function lose; the function is authoritative.

**Taxonomy discipline.** We do not claim “first taxonomy of paper–code mismatch”—SciCoQA already owns detection taxonomy. \(\lambda\) is the *partition engine* for C1–C2; the contribution headline is coverage fork + typed refuse/install, not six named chips.

### 3.4 Coverage fork (C1 core)

\[\mathrm{Obl}(W)=\{p\mid s=1\},\qquad \mathrm{Ent}(W)=\{p\mid e=1\}.\]

Projection assigns paper-face / repo-face statuses *before* editing \(H\): `gap`, `absent`, `host-already`, `covered`, plus `validity-gap` when products align but invalidation is one-sided. Obligation-sans-entry is `gap` on paper and `absent` on repo; entry-sans-obligation reverses. Hence \(\mathrm{coverage}_{\mathrm{paper}}\) need not equal \(\mathrm{coverage}_{\mathrm{repo}}\).

**Corollary (single-face impossibility).** If both omission types are nonempty on an empty host, no single-face policy can achieve FI\(=0\) and Miss\(=0\) simultaneously: wrap-repo has FI\(=|\text{entry-sans-obl.}|\) and Miss\(=|\text{obl.-sans-entry}|\) (Prop. 3); paper-only avoids FI but cannot bind entries or install \(K_H\).

**Nearest \(\neq\) covered.** Host skills with similar names do not flip `host_has`. Example: `eos` fits \(E(V)\), not minimizing \(F(V,T)\); `heat-flow` delivers lattice thermal conductivity, not free energy / entropy / heat capacity. Log nearest; keep \(\mathrm{host\_has}=\bot\).

#### Worked example: `qha` and `band` (illustrative)

Consider four products relative to one empty host (materials mini-ref / phonopy-style slots; **not** a multi-paper residual rate):

| Product | Paper \(s\) | Repo \(e\) | \(\lambda\) | Paper-face | Repo-face |
|---|---|---|---|---|---|
| DOS | 1 | 1 | both-aligned | covered* | covered* |
| thermal | 1 | 1 | both-aligned | covered* | covered* |
| **`qha`** | 1 | 0 | obl.-sans-entry | **gap** | **absent** |
| **`band`** | 0 | 1 | entry-sans-obl. | **absent** | **gap** |

\*If the host already delivers DOS/thermal; otherwise `gap` on both faces for those rows—still not a fork. The fork that matters is the last two rows: **paper-face missing ids = {`qha`}; repo-face missing ids = {`band`}; intersection empty.** Wrapping every entry installs `band` (FI) and never installs `qha` (Miss). Paper-only installs `qha` without a repo bind and still leaves validity unchecked when a later row is validity-gap.


#### Validity-gap worked sketch (phonopy-style `qha`)

Suppose paper procedure for quasi-harmonic approximation exists (\(s=1\)), repo exposes `phonopy-qha` (\(e=1\)), \(\kappa=0\), paper states invalidation near melting, repo docs omit it (\(v_{\mathrm{p}}\neq v_{\mathrm{r}}\)). Then \(\lambda=\)validity-gap. Wrap-repo can make “delivers thermal expansion” green while \(t_v=0\). Paper-only may write steps without binding the entry and still omit \(K_H\). Only \(I\) requires bind **and** check; destroy deleting the check must return \(t_v=0\). This row is the empirical differentiator SciCoQA’s three-class taxonomy does not force.

A second host that already delivers QHA but not bands flips only the paper-face status of `qha` to `host-already`; residual inside \(W\) remains, but it no longer lands as a host hole on that face. **Host comparison is load-bearing information**, not staging decoration.

#### Worked refusal sketches (*illustrative*; not EΔ)

**Entry-sans-obligation (`band`).** Repo exposes a band-structure entry (\(e=1\)); paper never states an ordered procedure for that product (\(s=0\)). Wrap-repo installs `band` → counts as FI. Typed \(I\) **refuses**: success is `band` \(\notin\) the paper test set and `band` \(\notin P_H\) after the trial (structured no-op). Destroy is N/A—there is no prescribed install to delete. The same pattern covers phonopy-style `group-velocity`.

**Procedure-conflict (SciCoQA-style L1 vs L2).** Both sides state a procedure (\(s=e=1\)) but compute different objects (\(\kappa=1\); e.g., paper obligates an L1 path while repo implements L2). \(\lambda=\)procedure-conflict. \(I\) leaves \(H\) unchanged and keeps an **unresolved** record; success is “no silent side-pick.” If an implementation side-picks paper or repo anyway, the trial is **invalid** (destroy N/A; count as silent-resolution failure, not as Miss under Prop. 3). *Illustrative sketch only—not a multi-work conflict rate.*

### 3.5 Operator \(I\): install, refuse, and \(K_H\) (C2)

Host state is \(H=(P_H,K_H)\): delivered products and installed invalidation checks \((p,v)\). **Each \(\lambda\) maps to a closed typed edit operator** on this pair—not free-form patch text: (i) add product \(p\) to \(P_H\); (ii) add check \((p,v)\) to \(K_H\); (iii) **structured no-op refuse** (success = \(H\) unchanged + exclusion/unresolved record); or (iv) pending conflict (no silent side-pick). CodeStruct / ChopChop-style constrained action spaces are precedents for this closed API; Faithful means the patch realizes the prescribed operator, not an arbitrary diff.

**Criterion provenance.** Checks written into \(K_H\) must be grounded in paper-stated invalidation text, or in dual-side invalidation when \(s=e=1\) and faces agree on \(v\) (CLAIMCHECK-style grounding). Never invent properties to green-light **entry-sans-obligation phantoms**—repo callables without paper obligation are refused, not given synthetic \(K_H\). Registering a repo tool is not authorizing it on \(H\) (MCP discovery-filter analogy: register \(\neq\) authorize).

| \(\lambda\) | Edit on \(H\) | Fail-before / destroy | Success meaning |
|---|---|---|---|
| both-aligned | Bind repo entry; install shared validity if stated | \(p\notin P_H\to p\in P_H\); unbind → red | Product via real entry |
| obligation-sans-entry | Host-owned procedure from paper; **no** forged entry ids | \(p\in P_H\) without fake \(e\); remove steps → red | Paper obligation realized |
| **entry-sans-obligation** | **Refuse: no edit** | \(p\notin\) paper test set; \(P_H\) unchanged | Refusal = success |
| **validity-gap** | Bind **and** install invalidation into \(K_H\) | \(t_v:0\to1\); remove check → 0 | Product *and* check |
| **procedure-conflict** | **Refuse silent side-pick**; unresolved record | \(P_H\) unchanged | Refusal = success |
| incongruent | Ignore | — | No invented product |

**Principled refusal (insight).** Correct typed introduction includes *positive refusal* as a **successful structured no-op**, not a crash: for entry-sans-obligation and procedure-conflict, success is “\(H\) unchanged + unresolved/excluded record,” not “more products on \(H\).” Installing an FI product without paper obligation is a *silent wrong state* of \(H\) (deterministic-gate vocabulary). Generation loops and MCP wrap share a wrong stop condition—*more tools* ≠ *better host relative to paper contract*. Soft prompt stand-down is not an install gate (Ambient Persuasion). Refusal is part of Effective.

**Validity-gap → \(K_H\) (insight).** When procedure and entry align but invalidation is one-sided (\(v_{\mathrm{p}}\neq v_{\mathrm{r}}\)), product presence alone is incomplete success (\(t_v=0\)). SciCoQA’s taxonomy has no dedicated invalidation type; SA-Bench drift classes are generation-side; ReproAgent validation is requirement/runtime review—not “paper says melts near melting point → host must fail on that input.” Phonopy-style `qha`: paper states near-melting invalidation; repo entry exists; docs omit the check—wrap-repo can make “delivers thermal expansion” green while \(t_v\) stays 0.

Baselines: \(W_{\mathrm{rap}}\) (every \(e=1\), never \(K_H\)); \(P_{\mathrm{aper}}\) (every \(s=1\), no bind/check); write-directly (no \(\lambda\)); ablation \(\pi\) swaps the two omission types then applies \(I\).


### 3.5.1 Deterministic pipeline (no look-ahead rewrite)

**Freeze first.** Host inventory \(H_0=(P_H,K_H)\), label set \(\Lambda\), and the fail-before / destroy witnesses are frozen *before* any model sees results. Later steps must not rewrite earlier labels or thaw \(H_0\).

Input: paper text, repo text, frozen \(H_0\). Each step’s output is determined by the previous step’s record—**no looking ahead to rewrite labels**.

1. **Inventory independently.** List products on each face separately. Finish the paper inventory before reading the repo (and vice versa). Cross-reading in one pass lets models fill paper steps from repo commands and erase residual.
2. **Merge by Id.** Form units \(u\) by product identity. Unmatched sides stay unilateral with zeros on the other face. If Id is undecidable, **do not merge** (two units, not a residual). Never invent a row from unmatched sentence↔function pairs (Dude grain constraint).
3. **Copy loci.** Every filled slot cites a line-bounded locus. If no locus can be copied, that boolean stays 0. “At least \(N\) fit points” is a runtime prerequisite, not invalidation.
4. **Judge \(\kappa\) only when \(s=e=1\).** If undecidable, keep \(\kappa=0\) (do not invent conflict). If \(\kappa=1\) appears on a unilateral row, reset to 0.
5. **Compute \(\lambda\).** Apply the case partition (Prop. 1 / Appendix D). If a hand label disagrees with the boolean function, **the function wins** and the locus citation is corrected.
6. **Project (before edit).** Emit paper-face and repo-face statuses via \(\mathrm{project}(\lambda,\mathrm{host\_has})\) (Appendix D); compute gap-set Jaccard as a C1 diagnostic. This step does **not** edit \(H\).
7. **Introduce or refuse (\(I\)).** Apply Table 3.5 / Appendix E. For refusal types, record exclusion/unresolved with \(\Delta P_H=\emptyset\). Generate the per-\(\lambda\) test contract (§3.7.1) *before* applying the edit.
8. **Accept.** On frozen \(H_0\): fail-before → apply edit → green → destroy prescribed action → must re-red. Then re-run the same labeled batch under \(W_{\mathrm{rap}}\), \(P_{\mathrm{aper}}\), and \(I\circ\pi\); report FI, Miss, green-rate, and destroy-still-green **broken out by \(\lambda\)**.

Under Faithful realization and empty start, the first two aggregates are fixed by Props. 2–3 *before* any model run; disagreement diagnoses the implementation. The theoretical support is a **deterministic operator contract**, not a learning-theoretic claim that models are smarter. Given slots and three external judgments (Id, \(\kappa\), Faithful), edits and tests are computed; only counting identities follow from definitions.

**Faithful vs measured rates.** Theorems assume patches realize the table. We do not prove an LLM writes them—report **green-rate** (fail-before ∧ pass-after) **and** **destroy still-green** (invalid tests \(\neq\) alignment success). Metacognitive “check outputs against findings” failures in AutoResearch-style loops are the obedience risk Faithful names.

### 3.6 Why \(\lambda\) selects the edit: counting identities

Detection says residual *exists*. Typed introduction says *which wrong edit* an untyped policy commits:

- **Prop. 2.** \(I\) adds only \(s=1\) products \(\Rightarrow \mathrm{FI}(I)=0\) (empty start, Faithful).
- **Prop. 3.** \(\mathrm{FI}(W_{\mathrm{rap}})=|\{u:\text{entry-sans-obligation}\}|\), \(\mathrm{Miss}(W_{\mathrm{rap}})=|\{u:\text{obligation-sans-entry}\}|\) (empty start).
- **Prop. 4.** On validity-gap, \(t_v=1\) under \(I\); \(t_v=0\) under \(W_{\mathrm{rap}}\) and \(P_{\mathrm{aper}}\) if check was absent.
- **Prop. 5.** If \(\pi\) swaps omission types and \(\ge 1\) such unit exists, some \(H\) and tests separate \(I\) from \(I\circ\pi\) (non-vacuous ablation).

**Knowledge claim.** SciCoQA-style labels become *edit selectors* with falsifiable counting identities. FI, Miss, and missing validity are separable errors—orthogonal to detection recall and reproduction accuracy. Type is causal for which wrong edit untyped policies commit.


### 3.6.1 Proof intuitions (for Soundness readers)

**Prop. 2 intuition.** The only labels that add to \(P_H\) are both-aligned, obligation-sans-entry, and validity-gap; each requires \(s=1\) by definition. Refusal labels never touch \(P_H\). Hence FI\(=0\) under Faithful realization from an empty start.

**Prop. 3 intuition.** Wrap-repo adds every \(e=1\). Those with \(s=0\) are exactly entry-sans-obligation (FI count). Those with \(s=1,e=0\) are never added and are exactly obligation-sans-entry (Miss count). The fork in §3.4 is the *mechanism* that makes these two counts independently nonzero.

**Prop. 4 intuition.** \(t_v\) is a product of indicators. Baselines that never write \(K_H\) leave the second factor zero even when \(p\in P_H\). Only validity-gap under \(I\) writes both.

**Prop. 5 intuition.** Swap the two omission labels, then reopen \(I\). On an empty host with test \(t=\mathbf{1}[p\in P_H]\), obligation-sans-entry units pass under \(I\) and fail under \(I\circ\pi\) (and conversely for entry-sans-obligation). If empirical pass sets do not separate, either those types are absent or the implementation ignored \(\lambda\).

*Illustrative* empty-host counts on filled phonopy / mini-ref slots (**not** multi-paper EΔ): \(I\): FI\(=0\); \(W_{\mathrm{rap}}\): FI\(=2\) (`band`, `group-velocity`), Miss\(=1\) (`lattice-kappa`); validity-gap rows get \(t_v=1\) only under \(I\). Full EΔ `TODO`.

### 3.7 Contract metrics (C3)

| Name | Definition | Colloquial |
|---|---|---|
| FI | Added to \(P_H\) with \(s=0\) | False introduction |
| Miss | \(s=1\), initially absent, operator did not add (conflicts listed separately) | Missed obligation |
| \(t_v\) | \(\mathbf{1}[p\in P_H]\cdot\mathbf{1}[(p,v)\in K_H]\) | Validity check installed |
| **Fast** | Model calls (opt. human edits) until fail-before holds and post-edit passes | Faster (only when measured) |
| **Effective** | Per-\(\lambda\) FI, Miss, \(t_v\) (+ deltas vs baselines) | More accurate (contract sense) |
| **Testable** | Fail-before ∧ pass-after ∧ fail-on-delete; report still-green-after-delete | More trustworthy (contract sense) |

Trustworthiness is destroy-test rate, not “the model said it matches.” Speed is call count to the *same* green contract vs write-directly. Task win-rate without destroy-tests understates invalid suites; call count without FI/Miss understates wrong installs. **Do not use brand slogans without these definitions.**

**Acceptance protocol (JSF + \(\lambda\)-indexed destroy).** In TestPrism’s Joint Success Function spirit, an introducing unit is admitted only if: (i) **fail-before** on frozen \(H_0\); (ii) **pass** after Faithful \(I\); (iii) **fail** after destroy—where destroy is a **\(\lambda\)-indexed semantic mutant** of the prescribed artifact \(a\). Destroy-still-green is reported as **test-invalid / survivor rate** (UTBoost / STING motivation: green alone admits wrong patches). Witnesses must not be writable by the introduction agent (Harbor-style Faithful harness). Optionally, admit \(I\) only with a replayable **Evidence Gate / Evidence Chain** of those three outcomes—generator proposes; protocol decides.

#### 3.7.1 Per-\(\lambda\) test contract (fail-before / post-edit / destroy)

Tests are written **before** editing \(H\). The table is the contract, not a model-invented checklist (`typed-introduction.md` §9.4).

| \(\lambda\) | Fail-before | Post-edit | Destroy (delete prescribed action) |
|---|---|---|---|
| both-aligned | \(p\notin P_H\) | \(p\in P_H\) | Unbind repo entry → \(p\notin P_H\) |
| obligation-sans-entry | \(p\notin P_H\) | \(p\in P_H\) and **no forged repo entry id** | Remove paper steps → \(p\notin P_H\) |
| validity-gap | \(t_v=0\) | \(t_v=1\) | Delete invalidation check → \(t_v=0\) |
| **entry-sans-obligation** | \(p\notin\) paper test set | **\(P_H\) unchanged** (refusal success) | — |
| **procedure-conflict** | \(P_H\) unchanged; unresolved record present | Same | If implementation silently side-picked, **trial invalid** |
| incongruent | — | Ignore | — |

**Refusal rows.** For entry-sans-obligation and procedure-conflict, success is *not* “another product on \(H\)”: it is structured no-op (exclusion / unresolved still present). Installing FI without obligation is a silent wrong state.

**Faithful vs measured.** Under Faithful realization, the post-edit column holds by definition. Experiments report (i) fail-before ∧ pass-after rate and (ii) destroy-still-green rate. The second diagnoses **invalid witnesses**, not host alignment success. Contract counts (Props. 2–3) stay separable from obedience rates.

Separate **contract counts** (Props. 2–3; decidable from labels + Faithful \(I\)) from **implementation obedience** (green-rate, destroy still-green). Model runs that disagree with Prop. 2 diagnose implementation, not the definition.

---

## 4. Experiments (protocol; results mostly TODO)

### 4.1 Design principles

Freeze \(H\), \(\lambda\), and tests *before* seeing results. Independent dual inventories (no cross-reading). Report contract-expected vs realized columns when Faithful may fail. Held-out works for E2′—fixed-task benchmark pass need not transfer to unseen introduction settings.

### 4.2 Experiment overview

| ID | Question | Serves | Status | Submission floor |
|---|---|---|---|---|
| **EΔ** | Residual non-empty and \(\lambda\)-typed; paper/repo gap Jaccard | C1 | **TODO** (phonopy/mini = illustrations) | ≥1 real pair; independent dual inventories; report fork Jaccard |
| **E1′** | Human IRR on Id / \(\lambda\) / projection | Annotation trust | Same-model pilot only; **human TODO** | ≥2 annotators; Cohen/Fleiss \(\kappa\) + raw agreement; same-model as appendix lower bound |
| **E2′** | \(I\) vs \(W_{\mathrm{rap}}\) vs \(P_{\mathrm{aper}}\) vs write-directly (+ \(\pi\)) | C2 / Props. 2–5 | Typed arms **TODO** | Same labeled units; FI/Miss/\(t_v\) by \(\lambda\) |
| **Testable** | Destroy still-green rate | C3 | Contract written; **batch TODO** | Report invalid-test rate |
| **Fast** | Calls to green vs write-directly | Optional | **TODO** | Matched tasks only |

Legacy same-model IRR may appear in appendix as instrument pilot—not human IRR, not typed Effective.

### 4.3 Corpus and annotation protocol

1. **What opens a row.** A row is a product a practitioner can request alone—not a package name, not an invalidation sentence (that fills a slot), not a merely incidental input, and not a docs mention without a callable source locus (`typed-introduction.md` §5). Soft mentions must not drive “missing” or introduction.
2. **Independent inventories.** Finish paper listing before reading the repo (and vice versa). Merge by product Id only. Undecidable Id → **no merge** (two units). Unilateral sides keep zeros on the other face.
3. **Slot fill rules.** \(s\): ordered procedure with locus (a noun alone does not count). \(e\): source function or documented subcommand that actually executes (docs pointing at a missing module → \(e=0\)). \(v_{\mathrm{p}}/v_{\mathrm{r}}\): explicit invalidation (“fails near melting”), not runtime prerequisites (“need ≥\(N\) points”). \(\kappa\): only when \(s=e=1\); undecidable → 0 (do not invent conflict).
4. **Loci.** Every filled boolean cites a **line-bounded** locus; uncopyable → boolean 0.
5. **Hand label vs function.** Compute \(\lambda\) from the boolean case partition. If a hand label disagrees, **the function wins** and the locus citation is corrected.
6. **Contamination control.** Methodology prose / skill guides must stay **out of the judge context**. Annotators and model judges see line-bounded paper/repo excerpts only (Limitations §7). Same-model mutual agreement is **not** human calibration (Rating Roulette).
7. **Scale (Findings floor).** First ~8 paper–repo pairs until a second annotator can independently reproduce `filled` and \(\lambda\); then expand. Venue-credible minimum: one batch of human-labeled units + three arms + one ablation + negative false-alarm cases.
8. **Freeze.** Host inventory \(H\), label set \(\Lambda\), and witnesses frozen before results; mid-run thaw forbidden.
9. **Id / \(\kappa\) humans-first.** Humans label a seed set; models report agreement with humans afterward—not among themselves.

**Destroy-harness protocol.** Witnesses live **outside** the introduction agent’s writable patch surface (Harbor-style isolation). Per-\(\lambda\) mutant operators (must re-red):
- both-aligned → unbind the repo entry bind;
- obligation-sans-entry → delete the paper-derived steps (no forged entry id may remain);
- validity-gap → delete the \(K_H\) invalidation check;
- entry-sans-obligation / procedure-conflict → no install mutant; success = \(H\) unchanged (+ unresolved for conflict); silent side-pick ⇒ trial invalid.
Report destroy-still-green as test-invalid / survivor rate, separate from FI/Miss.

### 4.4 Baselines and ablation

| Symbol | Behavior | Hits which prop | Faithful *qualitative* contract outcome (empty start) |
|---|---|---|---|
| \(I\) | Edit per \(\lambda\) + write \(K_H\); refuse phantoms/conflicts | Props. 2, 4 | FI\(=0\); Miss\(=0\) except deliberate unresolved conflicts; \(t_v=1\) on validity-gap |
| \(W_{\mathrm{rap}}\) | Every \(e=1\); never \(K_H\) | Props. 3, 4 | FI\(=|\{\text{entry-sans-obl.}\}|\); Miss\(=|\{\text{obl.-sans-entry}\}|\); \(t_v=0\) on validity-gap |
| \(P_{\mathrm{aper}}\) | Every \(s=1\); no bind/check | Prop. 4; both-aligned destroy fails bind | FI\(=0\); no Miss on obligations (but no entry bind); \(t_v=0\); both-aligned destroy (unbind) not applicable / fails contract |
| write-directly | Paper+repo to model; no \(\lambda\) | Fast; Effective contrast | No Prop. guarantee; may FI phantoms, Miss orphans, omit \(K_H\) |
| \(\pi\) | Swap obl.-sans-entry ↔ entry-sans-obl., then \(I\) | Prop. 5 | Pass sets separate from \(I\) when ≥1 omission-type unit exists |

**Scoring columns (required for E2′).** For each arm and each \(\lambda\), report **contract-expected** (Props. 2–4 / Table 3.7.1 under Faithful) vs **realized** (measured FI, Miss, \(t_v\), green-rate, destroy-still-green). Per-\(\lambda\) breakdown is mandatory—aggregate-only tables hide which residual type caused which wrong edit. Refusal arms score success as \(H\) unchanged (+ unresolved for conflict), not as product presence.

### 4.5 Placeholder tables (do not invent numbers)

**Table EΔ (TODO).** Residual mix and paper/repo gap-set Jaccard across works. Columns: work id; #units by \(\lambda\); paper-face missing-id set; repo-face missing-id set; Jaccard; fork (yes/no). *Illustration only:* for the four-row sketch above, Jaccard of missing-id sets across faces is \(0\) (`qha` vs `band`).

**Table E1′ (TODO).** Human IRR on Id, \(\lambda\), projection. Report Cohen/Fleiss \(\kappa\) + raw agreement; disagreement analysis on partial/missing loci and Id boundaries. Same-model three-judge pilot may be appendix lower bound only—not human IRR.

**Table E2′ (TODO).** **Per-\(\lambda\)** FI / Miss / \(t_v\) / green-rate / destroy-still-green for \(I\), \(W_{\mathrm{rap}}\), \(P_{\mathrm{aper}}\), write-directly, \(I\circ\pi\), with **contract-expected** vs **realized** columns (§4.4). *Illustration only (empty host, filled phonopy/mini slots, Faithful assumed—not multi-work EΔ):* \(I\) FI/Miss \(=0/0\), \(t_v=1\) on validity-gap; \(W_{\mathrm{rap}}\) FI/Miss \(=2/1\), \(t_v=0\); \(P_{\mathrm{aper}}\) \(t_v=0\); \(I\circ\pi\) FI/Miss \(=2/1\).

**Table Testable / Fast (TODO).** Destroy still-green (survivor) rate by \(\lambda\); call counts to shared fail-before suite vs write-directly (Fast optional). No brand claim until these cells exist.

### 4.6 TODO checklist (no fake fills)

- [ ] EΔ: ≥1 (prefer ≥2) real paper–repo independent inventories; residual mix + Jaccard
- [ ] E1′: ≥2 human annotators; \(\kappa\) + disagreement analysis (partial/missing, Id boundaries)
- [ ] E2′: four arms + \(\pi\); FI/Miss/\(t_v\) by \(\lambda\)
- [ ] Testable: destroy-test invalid rate
- [ ] Fast: matched call-count vs write-directly (optional for Findings)
- [ ] (Main bonus) Second enumerable host or second computational domain, \(\lambda\) unchanged

### 4.7 What “enough for Findings” looks like

ARR Findings prioritizes soundness and reproducibility over flashy novelty theater. A Findings-ready packet for this paper is:

1. **EΔ on ≥2 real pairs** with independent dual inventories, nonempty residual, and at least one pair whose paper/repo missing-id Jaccard is near zero (fork evidence).
2. **E1′ human IRR** on Id and \(\lambda\) with disagreement analysis (partial products, Id boundaries, \(\kappa=0\) defaults).
3. **E2′ contract table** on the same labeled units: \(I\) vs \(W_{\mathrm{rap}}\) vs \(P_{\mathrm{aper}}\) (+ \(\pi\)), reporting FI/Miss/\(t_v\) by \(\lambda\), plus destroy still-green rate.
4. **Honest Limitations** as in §6—same-model pilots only as appendix lower bounds; no detection/reproduction leaderboard claims.

Main would additionally want a second enumerable host or domain with \(\lambda\) frozen, larger EΔ, and Faithful obedience rates under LLM patches—not a thicker taxonomy.


---

## 5. Discussion

### 5.1 Three instruments

Detect, reproduce, and introduce answer incompatible targets. Competing on SciCoQA recall or SA-Bench / PaperBench scores is a **category error**: a perfect detector still does not choose host edits; a perfect reproducer may wrap entry-sans-obligation products into \(H\); scalar match can leave the claim unverified. **Community takeaway:** peers need three instruments—(i) discrepancy detectors, (ii) reproduction / semantic-alignment benches, (iii) typed introduction contracts for *already-deployed* hosts. Collapsing (iii) into (i)/(ii) recreates wrap-repo’s FI/Miss identities.

### 5.2 Residual as cause of wrong edits

The fork \(\mathrm{coverage}_{\mathrm{paper}}\neq\mathrm{coverage}_{\mathrm{repo}}\) is the mechanism behind Prop. 3. Toolchains that “just MCP-wrap the companion repo” inherit wrap-repo FI/Miss whenever omission types exist—a systems insight independent of materials jargon. Dude + SciCoQA Paper Omission jointly explain why wrap looks attractive (concrete callables) and why it is unsafe (many callables are not obligations; many obligations lack entries). Dynamic capability expansion can still be right when the *typed* obligation is missing—but expansion must be selected by \(\lambda\), not by entry presence.

ReproAgent’s dual channels *fuse for generation*; ours *keep faces forked for introduction*. That sentence is the Related Work wall against contract-language collision.

### 5.2.1 MCP / skill wrap as named baseline

Industry default *is* wrap-repo: attach an MCP server or compile a skill surface from a companion repository and treat connect as success. OWASP MCP and Agentic Skills Top 10 document tool poisoning, rug pulls, and confused-deputy risks; our point is narrower and methodological: even a *benign* wrap realizes \(W_{\mathrm{rap}}\)’s FI/Miss identities whenever omission types exist. Naming MCP-attach as \(W_{\mathrm{rap}}\) makes the FI story concrete rather than abstract. Least-privilege introduction is \(I\), not connect.


### 5.3 Refusal as success

Agent “capability expansion” literature and industry wrap-all share a wrong stop condition. Entry-sans-obligation and procedure-conflict succeed when \(P_H\) is unchanged—**structured reject raises correctness**, not a failed run. Soft prompt stand-down and Ambient Persuasion-style “ask first / be resourceful” conflicts are **not** enforceable install gates; \(\lambda\)-refuse must be machine-enforced at the edit boundary (deterministic pre-exec / discovery-filter precedent). Ablation \(\pi\) must flip which units are refused vs written; if pass rates do not separate, either those types are absent or the implementation ignores \(\lambda\) (Prop. 5).

### 5.4 Destroy-tests and honest Fast

Fail-before + destroy-tests operationalize trust for LLM patches. **Green alone is insufficient** (UTBoost: weak suites admit wrong patches; STING: surviving variants diagnose under-constrained witnesses). Green-only metrics conflate lucky tests with correct installs (TestPrism JSF). Destroy-tests are a local form of the broader *external verifiability* gap in agent harnesses. Always report still-green-after-delete as test-invalid / survivor rate; treat LLM-judge-only green as non-claims until human IRR (Rating Roulette; ACL 2025–26 Findings on judge fragility). Fast is defined only vs write-directly on the **same** fail-before suite—otherwise “faster alignment” is process theater.

### 5.5 Failure modes

| Failure | Breaks | Honest handling |
|---|---|---|
| **Id fails** | Invented/split products | No merge; no cross-row residual |
| **\(\kappa\) undecidable** | Conflict vs aligned | \(\kappa=0\); never invent conflict |
| **nearest as covered** | False `host_has` | Log nearest; \(\mathrm{host\_has}=\bot\) |
| **Faithful breaks** | Theorem antecedents | Report obedience; do not cite Prop. 2 as empirical FI\(=0\) |
| **Cross-reading inventories** | Erased residual | Separate passes (write-directly cheats this) |
| **Open-ended chat \(P_H\)** | Non-enumerable surface | Out of scope until freezable |
| **MCP wrap as \(I\)** | FI; privilege confusion | Wrap \(=W_{\mathrm{rap}}\); pin manifests |
| **Usage / nearest as coverage** | False `host_has` | Require product Id; usage \(\neq\) gain |
| **LLM-judge-only Effective** | Self-inconsistent labels | Human IRR; report \(\alpha\) |
| **Judge contamination** | Inflated agreement | Line-bounded reads; disclose |
| **Silent side-pick on conflict** | Violates refusal | Keep unresolved; test \(P_H\) unchanged |
| **Validity as post-hoc lint** | \(t_v\) never installed | Validity-gap is a residual *type*, not a lint |

### 5.6 Domain scope

Require co-holding of public product names, dual encodings of one process, and enumerable host surface. Computational materials is instance one; other domains that satisfy the trio are transfer checks **with \(\lambda\) frozen**. Do not open the venue claim to arbitrary chat agents.

---

## 6. Limitations

**Draft status.** Empirics for EΔ / E1′ / E2′ / Testable / Fast remain `TODO` (see [`gaps-and-todos-v043.md`](gaps-and-todos-v043.md)); this section states honesty bounds, not filled rates.

(1) Multi-work EΔ quantifying \(\Delta(W_p,W_r)\) and fork Jaccard beyond illustrative phonopy / mini-ref slots is incomplete; dual-encoding residual remains partially hypothetical until that table exists. (2) Existing classification agreement is a same-model three-judge pilot, not human IRR; Id and \(\kappa\) require human protocols before claims of calibrated labeling. (3) Counting theorems assume Faithful patches—we do not prove that a given LLM writes such patches; report green-rate and destroy still-green. (4) Scope requires product names + dual encoding + enumerable \(H\). (5) No competition on SciCoQA recall or paper→code accuracy (SA-Bench / LMR / SciReplicate / PaperBench / ReproAgent); no claim of Dude / Code Check detection SOTA. (6) Intra-package drift numbers are decomposition context, not headline results. (7) Pilot contamination risk (methodology prose entering judge context) → line-bounded protocol. (8) Fixed-task benchmark signals need not transfer to unseen introduction works. (9) Fast / “more trustworthy” brand claims are undefined until call-count and destroy tables exist. (10) We do **not** claim cryptographic G1 capability binding or implement capability-context integrity; that vocabulary is threat framing only. (11) We do **not** report MCP-proxy Unauthorized Invocation Rate (or related gate deltas) as our numbers—infrastructure precedent only. (12) LLM-as-judge is **not** the sole FI / \(t_v\) oracle (ACL 2025–26 Findings on judge fragility / attribute verifiability); prefer executable witnesses + destroy + human IRR.

---

## 7. Ethics statement (draft)

Public scientific papers/repos; no personal data. Risks: over-trust without destroy-tests; silent side-pick on procedure-conflict; dual-use wrapping of untrusted repos—mitigated by host-owned capability (no nesting a reference agent as runtime), by treating MCP-wrap as \(W_{\mathrm{rap}}\) not \(I\), and by keeping destroy witnesses outside the introduction agent’s write surface. LLM-as-judge is never the sole FI/\(t_v\) oracle (executable witnesses + destroy + human IRR). Annotator studies (`TODO`) use public texts, line-bounded loci, and disclosed agreement protocols. Slot schemas, guides, and EΔ/E1′/E2′ scripts to be released when runs complete.

---

## 8. Conclusion

We reframed paper–repo residual from a detection target into a **coverage-fork + typed introduction contract**: product-Id merge induces possibly disjoint host-gap faces; \(\lambda\) selects edits *and principled refusal* on \(H=(P_H,K_H)\), including validity checks; wrap-repo and paper-only admit countable FI, Miss, and \(t_v\) failures that \(I\) avoids under Faithful realization. Acceptance is fail-before → green → \(\lambda\)-indexed destroy-red (paper-grounded checks; refusal as success), not detection recall or reproduction fidelity. Remaining work is measurement—human IRR, multi-work EΔ with fork Jaccard, obedience and destroy tables—not further taxonomy. Detection and reproduction remain valuable and orthogonal; introduction is the missing third instrument for already-deployed hosts.

---

## Appendix A. Figure X caption (C1–C3)

> **Figure X.** Coverage fork and typed introduction for dual-encoded scientific work. (a) Independent paper/repo encodings are merged by product identity into unit \(u\); unique \(\lambda\) partitions residual (partition engine, not contribution headline). (b) **Coverage fork:** the same \(\lambda\) projects to disjoint host-gap sets on paper vs repo faces—illustrated on mini-ref / phonopy-style slots `qha` (obl.-sans-entry → gap/absent) and `band` (entry-sans-obl. → absent/gap). (c) Operator \(I\) maps \(\lambda\) to edits on \(H=(P_H,K_H)\) *or* principled refusal; validity-gap installs \(K_H\) (\(t_v\)). (d) Against wrap-repo (\(W_{\mathrm{rap}}\)) and paper-only (\(P_{\mathrm{aper}}\)), contract metrics Effective (FI, Miss, \(t_v\)) and Testable (fail-before→destroy); Fast optional until measured.

## Appendix B. Document map

| Path | Role |
|---|---|
| This file | ACL English draft **v0.4.4** (status/gaps pointer; method still v0.4.3; C1–C3 unchanged; empirics TODO) |
| [`gaps-and-todos-v043.md`](gaps-and-todos-v043.md) | ACL-blocking gaps + open TODOs (Chinese) |
| [`experiment-checklist-v043.md`](experiment-checklist-v043.md) | Six-phase run checklist (48 items) |
| [`CHANGELOG-v0.4.md`](CHANGELOG-v0.4.md) | What changed vs v0.3 |
| [`paper-v0.3-backup.md`](paper-v0.3-backup.md) | Pre-v0.4 snapshot |
| [`innovation-proposals.md`](innovation-proposals.md) | DECIDED lock memo |
| [`insights-research.md`](insights-research.md) | Bibliography → insight map |
| [`../acl-paper-design.md`](../acl-paper-design.md) | Writing pack / claim scope |
| [`../typed-introduction.md`](../typed-introduction.md) | Design authority |
| [`../../research/introduction-operator.md`](../../research/introduction-operator.md) | Operator proofs |
| [`../figures/typed-introduction/`](../figures/typed-introduction/) | Figure X vectors + notes |

## Appendix C. Checklist

- [x] Contributions = C1 fork / C2 refuse+\(K_H\) / C3 contract (not “six λ”)
- [x] RW opens detect vs introduce (SciCoQA); no “better detector”
- [x] Worked `qha`/`band` table + single-face impossibility corollary
- [x] Prop. 1–5 intuition + Faithful honesty
- [x] Three instruments + refusal-as-success discussion
- [x] Experiment protocol with TODO tables; illustrative counts labeled non-claim
- [x] Limitations: EΔ, IRR, Faithful, scope, neighbors, Fast brand, transfer
- [x] No eight-step / lattice / intra-package drift as contributions
- [x] Figure caption retargeted to C1–C3
- [x] v0.4.2: orphan/phantom framing in §1.3; Dude grain + Code Check reverse/adversarial in §2.1
- [x] v0.4.2: §2.3b contracts/gates neighbors (Skill-V/SkillOps/PDD/ReqToCode/ABAC/Ambient/UTBoost/STING/ChopChop)
- [x] v0.4.2: §3.5 typed edit API + criterion provenance + structured refuse; register≠authorize
- [x] v0.4.2: §3.7 JSF + λ-indexed destroy + survivor rate + Harbor + Evidence Gate wording
- [x] v0.4.2: §5.3–5.4 Ambient Persuasion / UTBoost–STING; Limitations G1/UIR/LLM-judge honesty
- [x] v0.4.2: §2.5 positioning refreshed; C1–C3 substance unchanged; no invented empirics
- [x] v0.4.3: §3.5.1 full deterministic pipeline (inventory→Id→loci→κ→λ→project→I→accept; freeze; no look-ahead)
- [x] v0.4.3: §3.7.1 per-λ fail-before / post-edit / destroy table (incl. refusal rows)
- [x] v0.4.3: worked refusal sketches (entry-sans-obl. `band`; procedure-conflict L1 vs L2)
- [x] v0.4.3: §4.3 annotation + destroy-harness protocol expanded
- [x] v0.4.3: §4.4/§4.5 scoring columns (contract-expected vs realized; per-λ E2′)
- [x] v0.4.3: Appendix D formal defs; Appendix E introduce/test/must-not cheat-sheet
- [x] v0.4.3: Abstract/Keywords (criterion provenance; structured refusal); Ethics/Conclusion destroy + no sole LLM-judge
- [x] v0.4.3: C1–C3 substance unchanged; no invented empirics
- [x] v0.4.4: Status/gaps pointer + Limitations draft-status line; link [`gaps-and-todos-v043.md`](gaps-and-todos-v043.md); C1–C3 + empirics TODOs unchanged


## Appendix D. Formal definitions (compact)

Full proofs: [`../../research/introduction-operator.md`](../../research/introduction-operator.md) (Props. 1–5). Notation matches [`../typed-introduction.md`](../typed-introduction.md) §9.

**Obligation / entry sets.**
\[
\mathrm{Obl}(W)=\{p\mid s=1\},\qquad \mathrm{Ent}(W)=\{p\mid e=1\}.
\]

**Host.** \(H=(P_H,K_H)\); \(K_H\) holds pairs \((p,v)\) meaning invalidation \(v\) is installed as a failing check. One edit does exactly one of: add \(p\) to \(P_H\); add \((p,v)\) to \(K_H\); or no-op.

**Projection (before edit).** \(\mathrm{host\_has}\) true selects the second status in each branch; false selects the first.
\[
\mathrm{project}(\lambda,\mathrm{host\_has})=
\begin{cases}
(\mathrm{covered\ or\ gap},\;\mathrm{covered\ or\ gap}) & \lambda=\text{both-aligned} \\
(\mathrm{gap\ or\ host\text{-}already},\;\mathrm{absent}) & \lambda=\text{obligation-sans-entry} \\
(\mathrm{absent},\;\mathrm{gap\ or\ host\text{-}already}) & \lambda=\text{entry-sans-obligation} \\
(\mathrm{validity\text{-}gap\ or\ host\text{-}already},\;\text{same}) & \lambda=\text{validity-gap}
\end{cases}
\]
Procedure-conflict does not enter the two gap tables; it is logged unresolved. This is the algorithmic form of the coverage fork: obligation-sans-entry appears only on the paper projection; entry-sans-obligation only on the repo projection.

**Validity indicator.**
\[
t_v(H)=\mathbf{1}[p\in P_H]\cdot\mathbf{1}[(p,v)\in K_H].
\]

**Paper-face coverage after edit.**
\[
\mathrm{coverage}_{\mathrm{paper}}(H',W)
=\frac{|\mathrm{Obl}(W)\cap P_{H'}|}{|\mathrm{Obl}(W)|}.
\]
Under Faithful \(I\), all of \(\mathrm{Obl}(W)\setminus P_H\) except unresolved conflicts enter \(P_{H'}\). Upper bound is \(1\) minus the unresolved-conflict share of obligations—not unconditional \(1\). Report “alignment complete” separately from “conflicts still open.”

## Appendix E. Introduce / test / must-not cheat-sheet

Compact copy of `typed-introduction.md` §7 (English labels). \(\lambda\) selects the edit and the test; it is not the contribution headline.

| \(\lambda\) | Introduce | Test | Must-not |
|---|---|---|---|
| both-aligned | Bind repo entry under the paper product name; install shared invalidation if both sides state it | Paper product: fail-before → pass-after | Drop the entry and rewrite a parallel procedure |
| obligation-sans-entry | Host-owned procedure from paper text; mark that the repo has no entry | Paper product; no forged repo entry id | Pretend a repo command exists |
| entry-sans-obligation | **Do not introduce** | Product absent from paper test set; \(P_H\) unchanged | Record it as a missing host obligation |
| validity-gap | Bind entry **and** install the side’s stated invalidation into \(K_H\) | Normal inputs deliver \(p\); violating inputs must fail (\(t_v=1\)) | Test only the happy path |
| procedure-conflict | Do not edit \(H\); leave unresolved | No silent side-pick | Quietly choose paper or repo procedure |
| incongruent | Ignore | — | Invent a product |
