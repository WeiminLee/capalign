# Abstract (draft v0.1)

Materials (computational) software — phonopy, ASE, pymatgen, VASP, QE — represents a
half-century pool of community-verified scientific capability assets. Yet the agents
now being built on top of them re-wire the same asset pool by hand, claim
capabilities they do not verifiably possess, and manage their capability surfaces as
one-off artifacts rather than as engineered objects. We propose **capability
engineering for scientific agents**: a three-layer method — *represent, align,
verify* — closed into a self-referential loop. (1) **Represent**: a cross-modal
capability intermediate representation (IR) that normalizes the same capability as it
appears in three knowledge modalities — software repositories (CLI entry points,
modules, dependency fingerprints), papers (method steps, software dependencies,
products), and experience write-ups (commands, recipes, claims) — into one typed
lattice with evidence, confidence, and provenance. (2) **Align**: bilateral alignment
of a host agent's capability surface against any reference, producing a five-way gap
classification (equivalent / partial / missing / host-only / unknown) tagged with
three source kinds (host self-audit / reference-contrast / domain inference), and
placement recommendations. Gap classification is *evidence-gated*: a candidate gap is
classified only after code-level validation against the host, and never from
low-confidence evidence. (3) **Verify**: per-run self-checks, synthetic-fixture gold
acceptance, and same-input determinism make the alignment itself auditable, and
define library-level metrics — coverage@reference and promise-drift rate — for
capability-surface governance. We instantiate the method with the first complete
reproduction of the paradigm: aligning a materials agent with 37 skills against
phonopy, demonstrating the discovery of 19 capability gaps, three false-gap catches,
and a prioritized assembly plan. Unlike skill-generation (SkillFoundry) and
skill-auditing (BIV) work, our contribution is the closed represent–align–verify loop
on a self-referential agent, anchored in the community-verified software assets of
materials science.

**Keywords:** agent capabilities; capability alignment; scientific software assets;
materials agents; claim verification; skill engineering.