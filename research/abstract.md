# Abstract (draft v0.2)

Materials science now accumulates deployed agents and published works that arrive
as a paper plus a companion repository. A user who already has an agent, facing a
new paper, needs to know which of the paper’s capabilities the agent already
covers, which are missing, and where each gap should land — before anyone
reproduces a claim or compiles a new skill. We treat a published scientific work
\(W=(\mathrm{paper},\mathrm{repo})\) as a **dual-encoded capability
specification**: the paper encodes method steps, validity conditions, and claimed
products; the repository encodes interfaces, modules, and executable paths.
Identity across encodings is a single evidence-gated predicate (semantic match
and an evidence threshold). We then define **host-relative alignment** as a
static decision procedure \(\mathrm{Gap}(H,W)\): a five-way gap class, a source
kind, and a placement recommendation, produced without executing the reference
and without implementing the gap. Coverage is **reference-conditioned**:
\(\mathrm{coverage}(H,W_{\mathrm{paper}})\) and
\(\mathrm{coverage}(H,W_{\mathrm{repo}})\) can fork, so aligning to only one
encoding under-specifies either method obligations or software interfaces. We
instantiate the procedure on materials agents, including a 37-skill host aligned
to phonopy (19 gaps, three false-gap catches). Unlike claim reproduction
(AutoMat), skill compilation (SkillFoundry), intra-artifact declaration–
implementation audit (BIV, SkillConsist), and paper–code discrepancy detection
(SciCoQA), the object is an incoming scientific work against an already-deployed
host. The skill that runs the procedure is the instrument; the contributions are
the dual-encoded specification, the host-relative decision procedure, and
reference-conditioned coverage.

**Keywords:** agent capabilities; capability alignment; scientific software;
materials agents; paper–repository specifications; host-relative coverage.
