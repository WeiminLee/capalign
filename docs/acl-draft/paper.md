# Green but Not the Paper's Result: Admissible Revision of a Deployed Scientific Host

> **Version.** Draft **v0.4.7** (2026-10-20, Asia/Shanghai). v0.4.6 withdrew. “Same name, different equation, usually an old host skill” mis-states the cases: near melting the equation is unchanged and the paper’s condition fails; a band file can be a correct computation the paper never owned. The object is a delivered number that does not have both responsibilities at once: the paper’s definition and conditions, and a run that executes that definition inside those conditions. **No new empirics.**  
> **Rule.** No fabricated empirics; unrun cells marked `TODO`.  
> **Status / gaps.** Story core rewritten in §1. **ACL-blocking gaps remain empty experiment tables.** Full inventory: [`gaps-and-todos-v043.md`](gaps-and-todos-v043.md). Run plan: [`experiment-checklist-v043.md`](experiment-checklist-v043.md). Prior lock (fork as C1) is superseded here: [`innovation-proposals.md`](innovation-proposals.md).  
> **Figure X.** [`../figures/typed-introduction/cap-align-typed-introduction.pdf`](../figures/typed-introduction/cap-align-typed-introduction.pdf)  
> **Formal proofs.** [`../../research/introduction-operator.md`](../../research/introduction-operator.md) (Props. 1–5). Design: [`../typed-introduction.md`](../typed-introduction.md). Insights map: [`insights-research.md`](insights-research.md).

---

## Abstract

A paper and its repository do not carry the same responsibility. The paper defines a quantity and states when that quantity does not count. The repository exposes commands that actually run. An agent that already runs is updated from one side or from a blend, and the update is kept when a number comes back. On the phonopy paper of Togo and Tanaka (2015), that number need not have both responsibilities. Very near melting, `phonopy-qha` still returns a quasi-harmonic expansion; the equation is the paper’s equation, and the paper says it does not count there. `--band` returns a real file; the paper never stated the sampling method as its own. A conductivity number can appear with no phonopy command for the anharmonic Boltzmann path the paper wrote. An \(E(V)\) fit on a frozen mini-host can be labeled thermal expansion; the paper’s definition is the minimization of \(F(V,T)\). These are forms read off the sources, not a rate.

The problem we take on is not whether the paper matches its own code, and not whether a new repository can be generated. It is how to revise an agent that is already running so that these three results are not accepted. We read the paper and the repository separately, open a row only for a product a user can request alone, and cite the procedure, the real entry, and any invalidation condition in the source. Before any edit, each row is written as one of the three failures. The edit may only bind a real entry, write the paper’s procedure without inventing an entry, bind the entry together with the stated invalidation check, or leave the host unchanged. Tests are fixed first. They must catch the failure before the edit, pass after the allowed edit, and fail again when that edit is removed. A suite that stays green after removal does not count. Whether this revision actually blocks the three results is `TODO`.

**Keywords:** scientific agents; deployed host; false success; invalidation conditions; admissible revision; paper–repo products; fail-before tests.

---

## 1. Introduction

### 1.1 What is going wrong

Materials work now arrives as two piles at once. One pile is agents that are already running and can already return some scientific quantities. The other is papers that keep appearing with a companion repository. The usual update is to attach that repository to the agent, or to let a model read the paper and write a new capability. The update is kept when it runs, writes a file, or returns a number.

That standard accepts results the paper does not stand behind. The rest of this section names three such results on one public pair. It then states the revision problem and the procedure we will test. Detecting whether a paper matches its own code, and generating a repository from a paper, answer different questions. They do not decide whether a number just returned by an existing agent is a result of this paper.

### 1.2 Three results that look successful and are not the paper's

The pair is Togo and Tanaka, *Scripta Materialia* 108 (2015) 1–5 (arXiv:1506.08498), read against the Phonopy v.4.8.2 command and QHA pages. Slots and quotations are recorded in `research/slot-model.phonopy.json`. A second, smaller pair (`research/slot-model.md`) supplies the equation-of-state confusion on a frozen mini-host. Nothing here is a count of how often agents do this.

**A number is returned in a regime the paper says does not count.** Section 4 writes the quasi-harmonic Gibbs energy as \(G(T,p)=\min_V[F(T,V)+pV]\) and states that the approximation is reasonable below the melting point except very near melting, where higher-order terms become evident. `phonopy-qha` fits the curve and asks for at least five volume points. That sentence is a precondition for the fit, not the melting invalidation, and the page does not state the melting failure. An agent that binds the command returns a thermal expansion on a room-temperature example, and the obvious test goes green. Asked for the same quantity near melting, it still returns a number. The fit ran. Under the paper’s own condition the number is not a quasi-harmonic result. Force constants have the same shape. Section 2 defines them as the derivative of forces with respect to displacement and treats the second-order term as the harmonic approximation only at small displacement and fixed volume. The repository can generate displacements and collect forces. Its command page does not say that a large displacement voids the harmonic constants. An agent that uses a large displacement still writes a force-constant matrix. The file exists. The harmonic approximation does not.

**A file exists, and it is not a result this paper is responsible for.** The phonon band structure appears as a figure for aluminum. The paper does not state how samples are taken along a high-symmetry path. The repository’s `--band` writes `band.yaml`. After the command is attached, the host produces the plot and looks as if it now implements the paper’s band method. The paper never wrote that procedure down as its method. Group velocity is cleaner: the paper has no such product, and `--gv` returns numbers. The numbers belong to the repository. They are not results of this paper.

**The requested quantity appears, and the path that produced it is the wrong path.** Section 6 obtains lattice thermal conductivity by turning anharmonic terms into phonon–phonon interactions and solving the linearized Boltzmann equation. The phonopy command page has no such entry; that calculation lives in another program, which we do not treat as this repository. If the agent still returns a conductivity, it used a conductivity skill the host already had, or a command that was invented. A test that only checks whether a conductivity number exists goes green. The number was not computed by the paper’s procedure, and it was not computed by this repository. A second wrong path shows up on the mini-host. The paper’s thermal expansion minimizes \(F(V,T)\). The host’s equation-of-state skill fits \(E(V)\) and returns an equilibrium volume and a bulk modulus. Returning that fit as thermal expansion looks like a materials answer. The thermodynamic potential is the wrong one. A similar name does not make the host already able to deliver the product.

| Looks successful | What the host returns | Why it is not this paper’s result | Source |
|---|---|---|---|
| Room-temperature QHA test is green; near-melting request still returns a number | Thermal expansion / \(G(T,p)\) from `phonopy-qha` | Paper: QHA fails very near melting, where higher-order terms matter. The docs require five volumes and do not state that failure | arXiv:1506.08498 §4; phonopy QHA page |
| Force-constant file is written | Second-order constants from a large displacement | Paper: harmonic form holds at small displacement and fixed volume. Command page does not state the failure | arXiv:1506.08498 §2; `-d` / `-f` |
| Band plot or group-velocity numbers appear | `band.yaml`, `--gv` | Paper shows a band figure and does not specify path sampling. Group velocity is absent from the paper | Fig. 1; `--band`, `--gv` |
| A conductivity number appears | \(\kappa\) from another skill or an invented command | Paper’s path is anharmonic phonon interactions and the linearized Boltzmann equation. The phonopy command page has no such entry | arXiv:1506.08498 §6 |
| An equation-of-state fit is labeled thermal expansion | \(V_0\), \(B_0\) from \(E(V)\) | The requested product minimizes \(F(V,T)\) | Frozen mini-host `eos` vs QHA |

### 1.3 What has to be true of a delivered number

A number returned under this work’s name is that work’s result only when both of the following hold.

The paper contains a passage that defines the quantity and states when it does not count. The run that produced the number executes that definition inside those conditions.

Near melting, the first passage exists and the run steps outside it. The equation has not been replaced. The paper’s condition has. For the band file, the run is real and the passage does not exist: the paper never owned that method. For lattice thermal conductivity, the passage exists in §6 and the phonopy command page has no run of it; a number from some other code fails the second sentence. For the equation-of-state fit, neither the paper nor this repository owns that run, and the definition in the paper is a different minimization.

The rows in §1.2 are these two sentences failing in different places. They are not three mechanisms, and they are not one mechanism of “a similar name, a different formula.” An edit table is not required to apply the two sentences. The table in §1.4 is a way to keep a later revision from creating such numbers. It does not decide, by itself, that a number is scientifically void.

### 1.4 A candidate control, not the claim

If false delivery is common, one control is to revise the host before it answers. That control is specified here so it can be ablated later. It is not what the paper claims to have found.

Read the paper and the repository separately. Open a row only for a result a person can ask for on its own. Copy the location of the procedure, of the entry that actually runs, and of any sentence that says when the result is void. A package name does not open a row. “At least five volume points” does not count as an invalidation. A name that merely resembles a host skill does not count as the host already having the product: fitting \(E(V)\) is not minimizing \(F(V,T)\).

Write the failure before changing the agent. Near melting, quasi-harmonic output must be rejected, and a room-temperature request must still succeed. A band file and a group velocity must not be reported as this paper’s method. Lattice thermal conductivity must come from the procedure the paper wrote, and the revision must not pretend this repository has that command. If the repository has no entry, write the paper’s procedure as the host’s own capability and record that no entry exists.

Each row then receives one action and no other: bind a real entry; write the paper’s steps and do not invent an entry id; bind the entry and install the stated invalidation check together; or leave the host unchanged. Leaving it unchanged is a successful revision when the row is a repository product the paper never owned, or when the two sides state conflicting procedures. Tests are written before the edit. The host must fail them before the edit and pass the ones it should pass after the edit. Delete the one prescribed action. If the test stays green, the test was wrong, and the revision does not count.

Section 3 records the same rule as slots, a label, and an operator. Those are the bookkeeping. They are not a separate claim. The coverage fork — paper-face gaps and repository-face gaps with nothing in common — is what this bookkeeping shows when the host can deliver neither product. On this phonopy reading the two faces are disjoint. That is an illustration. How often it happens is not the result this paper needs.

### 1.5 What would make the revision count

The revision counts if, on the same frozen host and the same requests, it blocks the three results while the usual updates still produce them, and it still returns the results the paper does stand behind (room-temperature quasi-harmonic output; a product whose procedure and entry both exist, bound to that entry). It does not count if every policy blocks every result, or if deleting the prescribed action leaves the test green. Section 4 states the arms and the ablations. No arm has been run. Counting identities under an operator that is assumed to follow the rule are not this evidence.

### 1.6 Neighbors, briefly

SciCoQA (ACL 2026) asks whether a paper and its own code disagree. On its real items the best reported recall is about 46.7%, and 55% of those items are differences of method rather than omissions. A detected omission is a fact about that pair. It does not say whether this host may return the corresponding file as the paper’s result. ReproAgent fuses paper obligations and repository evidence into a contract for building a new repository. That fusion is the right shape when the repository does not yet exist. Applied to an agent that already runs, it is one of the updates that can return the three results above. We do not compete on detection recall or on paper-to-code accuracy.

### 1.7 Contributions

1. **A delivered number needs both responsibilities.** The paper must define it and state when it does not count. The run must execute that definition inside those conditions. Attaching a repository, or accepting any number the host can compute, checks only the run. We show how each sentence fails on the phonopy pair and on one frozen mini-host. We do not show a rate.
2. **What is not yet shown.** In answers an agent actually marks successful, how often one of the two sentences fails, and whether the revision in §1.4 reduces those answers without discarding runs that satisfy both. Both are `TODO`.

**Not claimed:** that name collision with an old skill is the general cause; an edit taxonomy; a measured coverage-fork rate; detection or paper-to-code SOTA.

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

The procedure in §1.4 is recorded here as slots, a label \(\lambda\), and an operator \(I\). That record is how a revision stays checkable. It is not a second claim beside the three false results. The coverage fork in §3.4 is the special case in which the host delivers neither product and the two faces therefore list different gaps. Proofs that assume the operator is followed exactly are in `research/introduction-operator.md`. They are lemmas about the record, not the experiment. Design notes: `docs/typed-introduction.md`.

### 3.1 Dual encoding and domain co-conditions

\(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\) when three conditions co-hold: **(i)** public product names the community can agree on; **(ii)** both encodings describe one procedure (not training scripts vs method prose); **(iii)** the host surface is enumerable (skills, tools, runners frozen as text). Materials is instance one because product names are clearest; \(\lambda\) does not name phonons. Domains that satisfy the trio are transfer checks **with \(\lambda\) frozen**—not a license for arbitrary chat agents. Open-ended chat \(P_H\) is out of scope until freezable.

### 3.2 Product slots (grain for introduction)

Unit = one solicit-able product \(p\) (not file, function, or sentence):
\[
u=(p,\; s,\; e,\; v_{\mathrm{p}},\; v_{\mathrm{r}},\; \kappa),\qquad s,e,v_{\mathrm{p}},v_{\mathrm{r}}\in\{0,1,\mathrm{u}\},
\]
with \(s\)/\(e\) = paper procedure / repo entry (citeable loci); \(v_{\mathrm{p}},v_{\mathrm{r}}\) = explicit invalidation; \(\kappa=1\) only if both sides have procedures that are *not* the same computation (requires \(s=e=1\)). **Slots are tri-state:** \(1\) = stated with a locus; \(0\) = the source was inspected and is silent; \(\mathrm{u}\) = the source could not be inspected. Inventories are **independent**; merge by product identity (**Id**). Uncertain Id → no merge; uncertain \(\kappa\) → 0.

**Why tri-state (not two-valued).** Recording "not stated" and "not inspectable" as the same value reads absence of evidence as evidence of absence. When a companion paper is claimed but unreachable—a frozen search returns nothing—two-valued slots record \(s=0\) for every paper obligation, and the run then reports a confident *refusal* ("the paper never obligated this") on a work it never read. Tri-state moves that row to **insufficient evidence**: no card, `unknown` in both gap tables, the reason in Unresolved, and excluded from FI and Miss (an uninspectable row is neither a confirmed obligation nor a confirmed false introduction). A slot whose invalidation is unassessed installs with `bind` only and states validity as unknown—never a `check`, which would disguise an open question as a discharged one.

**Why product slots (insight).** Sentence–function detectors optimize textual-conflict recall. Introduction needs a grain a host can *own*: add \(p\) to \(P_H\), install \((p,v)\) in \(K_H\), or refuse. Dude’s grain mismatch and SciCoQA’s Paper Omission hardness share a root—code exposes many callables papers need not obligate—so treating every entry as obligation inflates FI under wrap-repo. Product slots refuse that inflation *before* \(\lambda\). ViewPoints: manage inconsistency; unilateral rows stay unilateral until Id is decided.

What does *not* open a row: package names; invalidation conditions alone (they are slots of a product); incidental inputs mentioned in a procedure; documentation pointing at a missing module (e.g., `docs/qha.md` without `qha.py` → \(e=0\), inspected-and-silent, not \(\mathrm{u}\)).

### 3.3 Type \(\lambda\) as partition (means, not headline)

\[
\lambda(u)=\begin{cases}
\text{insufficient-evidence} & s=\mathrm{u}\ \text{or}\ e=\mathrm{u} \\
\text{incongruent} & s=e=0 \\
\text{obligation-sans-entry} & s=1,\; e=0 \\
\text{entry-sans-obligation} & s=0,\; e=1 \\
\text{procedure-conflict} & s=e=\kappa=1 \\
\text{validity-unassessed} & s=e=1,\;\kappa=0,\; v_{\mathrm{p}}=\mathrm{u}\ \text{or}\ v_{\mathrm{r}}=\mathrm{u} \\
\text{validity-gap} & s=e=1,\;\kappa=0,\; v_{\mathrm{p}},v_{\mathrm{r}}\in\{0,1\},\; v_{\mathrm{p}}\neq v_{\mathrm{r}} \\
\text{both-aligned} & s=e=1,\;\kappa=0,\; v_{\mathrm{p}}=v_{\mathrm{r}}\in\{0,1\}.
\end{cases}
\]

**Prop. 1 (partition).** Exactly one label per well-formed unit. The case order is part of the definition: \(\mathrm{u}\) on \(s\) or \(e\) is decided **first** (otherwise \(s=1,e=\mathrm{u}\) falls into both-aligned and binds an unread entry), then \(\mathrm{u}\) on the validity slots (validity-unassessed), then \((s,e)\), then \(\kappa\), then validity equality. Incongruent units are ignored. Without \(\kappa\), conflicts would mislabel as both-aligned and wrongly bind into \(H\). Hand labels that disagree with the function lose; the function is authoritative.

**Taxonomy discipline.** We do not claim “first taxonomy of paper–code mismatch”—SciCoQA already owns detection taxonomy. \(\lambda\) is the *partition engine* for C1–C2; the contribution headline is coverage fork + typed refuse/install, not the named chips. Two of the eight labels produce no card (incongruent, insufficient-evidence) and are reported as such, not silently dropped.

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
3. **Copy loci.** Every slot at \(1\) cites a line-bounded locus and a verbatim quote. A source that was inspected and is silent is \(0\) with a recorded reason; a source that could not be inspected is \(\mathrm{u}\) with its own reason. The two are never collapsed. “At least \(N\) fit points” is a runtime prerequisite, not invalidation.
4. **Judge \(\kappa\) only when \(s=e=1\).** If undecidable, keep \(\kappa=0\) (do not invent conflict). If \(\kappa=1\) appears on a unilateral row, reset to 0.
5. **Compute \(\lambda\).** Apply the case partition (Prop. 1 / Appendix D). If a hand label disagrees with the function, **the function wins** and the locus citation is corrected.
6. **Project (before edit).** Emit paper-face and repo-face statuses via \(\mathrm{project}(\lambda,\mathrm{host\_has})\) (Appendix D); compute gap-set Jaccard as a C1 diagnostic. This step does **not** edit \(H\).
7. **Introduce or refuse (\(I\)).** Apply Table 3.5 / Appendix E. For refusal types, record exclusion/unresolved with \(\Delta P_H=\emptyset\). Generate the per-\(\lambda\) test contract (§3.7.1) *before* applying the edit.
8. **Accept.** On frozen \(H_0\): fail-before → apply edit → green → destroy prescribed action → must re-red. Then re-run the same labeled batch under \(W_{\mathrm{rap}}\), \(P_{\mathrm{aper}}\), and \(I\circ\pi\); report FI, Miss, green-rate, and destroy-still-green **broken out by \(\lambda\)**.

Under Faithful realization and empty start, the first two aggregates are fixed by Props. 2–3 *before* any model run; disagreement diagnoses the implementation. The theoretical support is a **deterministic operator contract**, not a learning-theoretic claim that models are smarter. Given slots and three external judgments (Id, \(\kappa\), Faithful), edits and tests are computed; only counting identities follow from definitions.

**Faithful vs measured rates.** Theorems assume patches realize the table. We do not prove an LLM writes them—report **green-rate** (fail-before ∧ pass-after) **and** **destroy still-green** (invalid tests \(\neq\) alignment success). Metacognitive “check outputs against findings” failures in AutoResearch-style loops are the obedience risk Faithful names.

### 3.6 Why \(\lambda\) selects the edit: counting identities

Detection says residual *exists*. Typed introduction says *which wrong edit* an untyped policy commits:

- **Prop. 2.** \(I\) adds only \(s=1\) products \(\Rightarrow \mathrm{FI}(I)=0\) (empty start, Faithful).
- **Prop. 3.** \(\mathrm{FI}(W_{\mathrm{rap}})=|\{u:\text{entry-sans-obligation}\}|\), \(\mathrm{Miss}(W_{\mathrm{rap}})=|\{u:\text{obligation-sans-entry}\}|\) (empty start; holds because \(\lambda\) removes \(\mathrm{u}\)-rows from both labels).
- **Prop. 4.** On validity-gap, \(t_v=1\) under \(I\); \(t_v=0\) under \(W_{\mathrm{rap}}\) and \(P_{\mathrm{aper}}\) if check was absent.
- **Prop. 5.** If \(\pi\) swaps omission types and \(\ge 1\) such unit exists, some \(H\) and tests separate \(I\) from \(I\circ\pi\) (non-vacuous ablation).

**Prop. 3 under tri-state.** An uninspectable row is neither a confirmed obligation nor a confirmed false introduction: \(W_{\mathrm{rap}}\) cannot bind an entry it could not read, and \(P_{\mathrm{aper}}\) cannot copy a procedure it could not read. Such rows are reported in a third aggregate, **unresolved**, and excluded from FI and Miss. The identity still holds because \(\lambda\) assigns them to insufficient-evidence, not to either omission type — but an implementation that counts "\(e\neq1\)" as "not bound" will silently inflate Miss. We report the unresolved count beside FI/Miss so that inflation is visible.

**Knowledge claim.** SciCoQA-style labels become *edit selectors* with falsifiable counting identities. FI, Miss, and missing validity are separable errors—orthogonal to detection recall and reproduction accuracy. Type is causal for which wrong edit untyped policies commit.


### 3.6.1 Proof intuitions (for Soundness readers)

**Prop. 2 intuition.** The only labels that add to \(P_H\) are both-aligned, obligation-sans-entry, validity-gap, and validity-unassessed; each requires \(s=1\) by definition. Refusal and no-card labels never touch \(P_H\). Hence FI\(=0\) under Faithful realization from an empty start.

**Prop. 3 intuition.** Wrap-repo adds every \(e=1\). Those with \(s=0\) are exactly entry-sans-obligation (FI count). Those with \(s=1,e=0\) are never added and are exactly obligation-sans-entry (Miss count). Rows with \(s=\mathrm{u}\) or \(e=\mathrm{u}\) are insufficient-evidence and sit outside both counts. The fork in §3.4 is the *mechanism* that makes these two counts independently nonzero.

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

The outcome that matters is, among answers the host marks successful, how often one of the two sentences in §1.3 fails. Fork rate and label counts are not substitutes. No cell below has been filled.

### 4.0 Requests that define a false success

Freeze the host, the paper, and the repository before any edit. Each request is something a user can ask the host after the update. Score the returned object, not a label.

| Request | False success | Legitimate success |
|---|---|---|
| Thermal expansion very near melting | A QHA number is returned and not rejected | The host refuses, citing the paper’s melting condition |
| Thermal expansion at a temperature the paper still allows | No expansion, or an \(E(V)\) fit labeled as \(F(V,T)\) | Expansion from the paper’s minimization, not from `eos` |
| Force constants from a large displacement | A second-order matrix is returned as harmonic | The host refuses: the harmonic regime is small displacement, fixed volume |
| “The paper’s band method” / group velocity | `band.yaml` or `--gv` numbers, described as this paper’s method | No such claim. The repository command may exist; it is not introduced as the paper’s obligation |
| Lattice thermal conductivity via this phonopy workflow | A \(\kappa\) from `heat-flow` or from an invented phonopy command | \(\kappa\) only from the paper’s Boltzmann path, with the missing phonopy entry recorded. A number from another skill does not count |

Write these checks before editing. Room-temperature QHA and a both-aligned product (phonon DOS, whose formula and `--dos` entry both exist) are the positive controls: a revision that refuses every request has not solved the problem.

### 4.1 Design principles

Freeze \(H\), the allowed action, and the tests *before* seeing results. Read the paper and the repository separately. A second paper–repo pair uses the same requests in form and no retuned rule text. An operator that is assumed to obey the rule cannot prove the revision works.

### 4.2 Experiment overview

| ID | Question | Serves | Status | Submission floor |
|---|---|---|---|---|
| **E-false** | On the requests in §4.0, which arms return a false success, and which still return the legitimate product | §1.5 | **TODO** | Phonopy pair + frozen mini-host; same requests for every arm |
| **E1′** | Human agreement on product identity, cited procedure / entry / invalidation | The rows are not private | Same-model pilot only; **human TODO** | ≥2 annotators; \(\kappa\) + disagreements on what counts as an invalidation |
| **E2′** | Admissible revision vs wrap-repo vs paper-only vs write-directly | §1.5 | **TODO** | Same units; false-success rate and legitimate-success rate, not only FI/Miss |
| **Ablations** | §4.4: drop the check; swap install with refuse; labels without forbidden actions; hide `host_has`; delete the prescribed action | The block is due to that action | **TODO** | Each ablation restores the failure it names, or the claim is unsupported |
| **EΔ** | How often the two faces list different products | Descriptive corollary | **TODO** (phonopy/mini = illustrations) | Report the mix. Do not lead with it |
| **Fast** | Calls until the §4.0 suite behaves | Optional | **TODO** | Only against write-directly on the same requests |

Legacy same-model IRR may appear in appendix as instrument pilot—not human IRR, not typed Effective.

### 4.3 Corpus and annotation protocol

1. **What opens a row.** A row is a product a practitioner can request alone—not a package name, not an invalidation sentence (that fills a slot), not a merely incidental input, and not a docs mention without a callable source locus (`typed-introduction.md` §5). Soft mentions must not drive “missing” or introduction.
2. **Independent inventories.** Finish paper listing before reading the repo (and vice versa). Merge by product Id only. Undecidable Id → **no merge** (two units). Unilateral sides keep zeros on the other face.
3. **Slot fill rules.** \(s\): ordered procedure with locus (a noun alone does not count). \(e\): source function or documented subcommand that actually executes (docs pointing at a missing module → \(e=0\)). \(v_{\mathrm{p}}/v_{\mathrm{r}}\): explicit invalidation (“fails near melting”), not runtime prerequisites (“need ≥\(N\) points”). \(\kappa\): only when \(s=e=1\); undecidable → 0 (do not invent conflict).
4. **Loci.** Every slot at `1` cites a **line-bounded** locus and a verbatim quote. Inspected-and-silent is `0` with a recorded reason; not-inspectable is `unknown` with its own reason. The two are never collapsed.
5. **Hand label vs function.** Compute \(\lambda\) from the case partition, in its defined order (unknown before any `s`/`e` comparison). If a hand label disagrees, **the function wins** and the locus citation is corrected.
6. **Contamination control.** Methodology prose / skill guides must stay **out of the judge context**. Annotators and model judges see line-bounded paper/repo excerpts only (Limitations §7). Same-model mutual agreement is **not** human calibration (Rating Roulette).
7. **Scale (Findings floor).** First ~8 paper–repo pairs until a second annotator can independently reproduce each slot's `state` and \(\lambda\); then expand. Venue-credible minimum: one batch of human-labeled units + three arms + one ablation + negative false-alarm cases.
8. **Freeze.** Host inventory \(H\), label set \(\Lambda\), and witnesses frozen before results; mid-run thaw forbidden.
9. **Id / \(\kappa\) humans-first.** Humans label a seed set; models report agreement with humans afterward—not among themselves.

**Destroy-harness protocol.** Witnesses live **outside** the introduction agent’s writable patch surface (Harbor-style isolation). Per-\(\lambda\) mutant operators (must re-red):
- both-aligned → unbind the repo entry bind;
- obligation-sans-entry → delete the paper-derived steps (no forged entry id may remain);
- validity-gap → delete the \(K_H\) invalidation check;
- entry-sans-obligation / procedure-conflict → no install mutant; success = \(H\) unchanged (+ unresolved for conflict); silent side-pick ⇒ trial invalid.
Report destroy-still-green as test-invalid / survivor rate, separate from FI/Miss.

### 4.4 Baselines and ablation

Arms see the same frozen host, paper, repository, and §4.0 requests.

| Arm | What it does | False success it is expected to emit | What would falsify that expectation |
|---|---|---|---|
| Admissible revision | One allowed action per row, including “do nothing” and the invalidation check | None of the three. Legitimate rows still return a product | It still returns a voided number, a repository-only product as the paper’s method, or a quantity from the wrong path. Or it refuses the room-temperature QHA and the DOS as well |
| Wrap repository | Attach every real entry. No invalidation check. No paper-only procedure | Near-melting QHA number; band and group velocity as if they were the paper’s method; no paper-path \(\kappa\) | It refuses near melting without being told to, and it does not present `--band` / `--gv` as the paper’s method |
| Paper only | Write every paper procedure. No real entry. No check | \(\kappa\) or QHA from a rewritten procedure that cites a phonopy command which does not exist; no melting refusal | The rewritten procedure names no fake entry and rejects the melting regime on its own |
| Write directly | Paper, repository, and host in one prompt. No allowed-action list | Whichever of the three the model happens to produce | Across requests it neither voids the melting result, nor substitutes `eos` / `heat-flow`, nor calls repository-only outputs the paper’s method |
| Drop the check | Same as admissible revision, but do not install the melting or large-displacement refusal | Near-melting QHA and large-displacement constants look successful again. Other requests unchanged | Those two stay blocked. Then the check was not what blocked them |
| Swap install and refuse | Treat “paper only” as “do nothing”, and “repository only” as “write it as an obligation” | Band and group velocity get installed as obligations; \(\kappa\) is dropped | The false successes do not move with the swap |
| Label without a forbidden action | Tell the editor the row’s name only | A green result whose patch still contains a forbidden action: fake entry id, missing check, or a silent choice of one procedure | Green patches contain none of those actions |
| Hide whether the host already can | Run the thermal-expansion request once with `eos` visible and once with it hidden, under write-directly | With `eos` visible, an \(E(V)\) fit is returned as thermal expansion | The substitution appears even when `eos` is hidden, or never appears. The host’s existing skill is then not part of the failure |
| Delete the prescribed action | After a passing admissible revision, remove only the bind, the paper steps, or the check | The request fails again | It still passes. The test does not witness that action |

Contract counts (false introductions, missed obligations) may be reported beside these outcomes. They do not replace them. A run in which the editor is assumed to obey the table is not a row in this experiment.

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

### 4.7 What would count as shown

1. **E-false / E2′ on the phonopy pair and the frozen mini-host.** Same §4.0 requests for every arm. Admissible revision blocks the three false successes and still returns room-temperature QHA and DOS. Wrap, paper-only, and write-directly do not.
2. **The ablations in §4.4 put those failures back in the place each ablation names.** A revision that stays perfect under every ablation has not been shown to work by this procedure.
3. **A second paper–repo pair**, same request forms, no retuned rule, plus human agreement on the cited procedure, entry, and invalidation.
4. **Delete-the-action** on the passing revisions: the witness goes red again.

A fork rate can sit in an appendix. It is not a substitute for (1)–(4). No item above has been run.


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

(1) Multi-work EΔ quantifying \(\Delta(W_p,W_r)\) and fork Jaccard beyond illustrative phonopy / mini-ref slots is incomplete; dual-encoding residual remains partially hypothetical until that table exists. (2) Existing classification agreement is a same-model three-judge pilot, not human IRR; Id and \(\kappa\) require human protocols before claims of calibrated labeling. (3) Counting theorems assume Faithful patches—we do not prove that a given LLM writes such patches; report green-rate and destroy still-green. (4) Scope requires product names + dual encoding + enumerable \(H\). (5) No competition on SciCoQA recall or paper→code accuracy (SA-Bench / LMR / SciReplicate / PaperBench / ReproAgent); no claim of Dude / Code Check detection SOTA. (6) Intra-package drift numbers are decomposition context, not headline results. (7) Pilot contamination risk (methodology prose entering judge context) → line-bounded protocol. (8) Fixed-task benchmark signals need not transfer to unseen introduction works. (9) Fast / “more trustworthy” brand claims are undefined until call-count and destroy tables exist. (10) We do **not** claim cryptographic G1 capability binding or implement capability-context integrity; that vocabulary is threat framing only. (11) We do **not** report MCP-proxy Unauthorized Invocation Rate (or related gate deltas) as our numbers—infrastructure precedent only. (12) LLM-as-judge is **not** the sole FI / \(t_v\) oracle (ACL 2025–26 Findings on judge fragility / attribute verifiability); prefer executable witnesses + destroy + human IRR. (13) The tri-state split between \(0\) (inspected, silent) and \(\mathrm{u}\) (not inspectable) is an annotation judgment, not a theorem—we assume **Availability**: annotators agree on which sources count as inspected. Disagreement there changes both the label and the denominators, so it needs its own agreement statistic alongside Id and \(\kappa\).

---

## 7. Ethics statement (draft)

Public scientific papers/repos; no personal data. Risks: over-trust without destroy-tests; silent side-pick on procedure-conflict; dual-use wrapping of untrusted repos—mitigated by host-owned capability (no nesting a reference agent as runtime), by treating MCP-wrap as \(W_{\mathrm{rap}}\) not \(I\), and by keeping destroy witnesses outside the introduction agent’s write surface. LLM-as-judge is never the sole FI/\(t_v\) oracle (executable witnesses + destroy + human IRR). Annotator studies (`TODO`) use public texts, line-bounded loci, and disclosed agreement protocols. Slot schemas, guides, and EΔ/E1′/E2′ scripts to be released when runs complete.

---

## 8. Conclusion

A paper defines a quantity and states when it does not count. Its repository exposes commands that run. An agent updated from either side keeps the update when a number comes back, which checks the run and not the paper’s definition and conditions. On phonopy, a quasi-harmonic number very near melting, a band file the paper never specified, and a conductivity with no command for the paper’s anharmonic path each fail one of those two requirements. The rate at which agents mark such numbers successful is unmeasured. Detection asks whether the two texts owe each other a correction. This draft asks whether the number a user received has both the paper’s responsibility and the run’s.

---

## Appendix A. Figure X caption (C1–C3)

> **Figure X.** Coverage fork and typed introduction for dual-encoded scientific work. (a) Independent paper/repo encodings are merged by product identity into unit \(u\); unique \(\lambda\) partitions residual (partition engine, not contribution headline). (b) **Coverage fork:** the same \(\lambda\) projects to disjoint host-gap sets on paper vs repo faces—illustrated on mini-ref / phonopy-style slots `qha` (obl.-sans-entry → gap/absent) and `band` (entry-sans-obl. → absent/gap). (c) Operator \(I\) maps \(\lambda\) to edits on \(H=(P_H,K_H)\) *or* principled refusal; validity-gap installs \(K_H\) (\(t_v\)). (d) Against wrap-repo (\(W_{\mathrm{rap}}\)) and paper-only (\(P_{\mathrm{aper}}\)), contract metrics Effective (FI, Miss, \(t_v\)) and Testable (fail-before→destroy); Fast optional until measured.

## Appendix B. Document map

| Path | Role |
|---|---|
| This file | ACL English draft **v0.4.5** (narrative retarget: three false successes; fork demoted; empirics TODO) |
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

- [x] v0.4.5: claim = three false successes + revision tested against them (fork demoted; not “six λ”)
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
(\mathrm{covered\ or\ gap},\;\mathrm{covered\ or\ gap}) & \lambda\in\{\text{both-aligned},\text{validity-unassessed}\} \\
(\mathrm{gap\ or\ host\text{-}already},\;\mathrm{absent}) & \lambda=\text{obligation-sans-entry} \\
(\mathrm{absent},\;\mathrm{gap\ or\ host\text{-}already}) & \lambda=\text{entry-sans-obligation} \\
(\mathrm{validity\text{-}gap\ or\ host\text{-}already},\;\text{same}) & \lambda=\text{validity-gap} \\
(\mathrm{unknown},\;\mathrm{unknown}) & \lambda=\text{insufficient-evidence}
\end{cases}
\]
Procedure-conflict and incongruent do not enter the two gap tables; conflict is logged unresolved. Insufficient-evidence enters both tables as `unknown` and produces no card. This is the algorithmic form of the coverage fork: obligation-sans-entry appears only on the paper projection; entry-sans-obligation only on the repo projection.

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
| validity-unassessed | Bind entry only; state validity as unknown | Product delivered; no invalidation check claimed | Write a `check` whose condition was never read |
| insufficient-evidence | **Do not introduce**; record the unread arm and why | — (no card) | Treat the unread side as \(0\) and refuse |
| procedure-conflict | Do not edit \(H\); leave unresolved | No silent side-pick | Quietly choose paper or repo procedure |
| incongruent | Ignore | — | Invent a product |
