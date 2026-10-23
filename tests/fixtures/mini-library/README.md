# mini-library

A frozen two-entry host (`eos`, `heat-flow`) and ten candidate cards covering all
nine fusion relations. This fixture is for the portfolio admission step; it does
not run the capability inventory.

Traps asserted:

- all nine relations appear: `covered`, `partial` (twice: missing check and
  missing regime), `duplicate`, `variant`, `hard-conflict`, `subsumes`,
  `subsumed`, `adjacent`, `unrelated`;
- `duplicate` requires the same product, procedure, and regime; description
  overlap alone is not duplication;
- same procedure with a different regime is `partial`, not `variant`;
- `variant` requires disjoint regimes; overlapping regimes with different
  procedures is `hard-conflict`;
- `merge` preserves both test contracts, all live obligations, checks, and
  provenance;
- `eos-dup` carries the fail-closed merge block: every removed unit has one
  witness, the five surface classes are covered once (`coverage ∪ removed ∪
  locked_residual`), both sides' retained probes and the candidate's own
  deliver probe are in the recall gate, and the merged surface does not inflate;
- `qha` and `kappa-bte-lowT` are individually safe but jointly shadow
  `q-heat-flow-route`; the add-all arm fails and the gated arm (demote `qha`)
  passes.

The two JSON inputs are the two arms. The tool is static: it checks the declared
plan and never executes a probe or edits a host.
