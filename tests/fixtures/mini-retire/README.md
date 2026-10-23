# mini-retire

A four-entry host with a good upgrade, a good retire, and one bad retire in the
same lifecycle plan.

- `eos-old` → `eos-new` is a valid upgrade: the source delivers a superset of
  products, checks, and regime, and the retained probe `q-eos-old` is remapped.
- `qha-old` is a valid retire: `thermal-expansion` is not live and its only probe
  is not retained.
- `heat-flow` is a rejected retire: `lattice-kappa` is live and `q-heat-flow` is a
  retained probe. The tool names the liveness violation and the retained-probe
  dependency; the good actions before it still pass.

The plan is checked statically. Nothing is executed and no host file is edited.
