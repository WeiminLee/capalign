# mini-host self-audit notes

Known gaps in this host's capability surface (admitted here, not yet built):

- No harmonic heat capacity / specific heat (`Cv`) or phonon thermal properties
  (free energy F, entropy S, zero-point energy) — a user asking for `Cv` today gets
  no result.
- No phonon DOS or dispersion.
- No force-constant / dynamical-matrix pathway for any structure.

Open (not gaps, boundaries): lattice thermal conductivity is covered by the
`heat-flow` skill (BTE); equations of state by the `eos` skill.