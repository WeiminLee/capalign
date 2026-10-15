# I benchmarked phonon heat transport the fast way (excerpt)

Instead of a full DFT workflow, I ran `vibcalc kappa` on my relaxed POSCAR and
got a thermal conductivity in minutes. The recipe: relax the cell, run
`vibcalc kappa` with the default q-mesh, then check the convergence line in the
log — if the kappa value moves less than 5% between two q-meshes you are done.

In my experience MACE-based interatomic potentials are noticeably more faithful
than NEP for this kind of transport calculation.