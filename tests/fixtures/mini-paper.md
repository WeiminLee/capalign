# Ab initio thermal conductivity of a model perovskite (excerpt)

## Methods

We compute the harmonic phonons of the cubic phase via the finite-displacement
method: (1) generate symmetry-inequivalent displacements of the 5-atom cell,
(2) evaluate forces on the displaced cells with the ASE calculator interface to
VASP, (3) assemble the force-constant matrix, (4) build and diagonalize the
dynamical matrix on a q-mesh, (5) integrate the phonon DOS with a Gaussian
broadening, and (6) evaluate the constant-volume heat capacity from the
frequencies. Convergence of the q-mesh was checked at 6x6x6.

Lattice thermal conductivity follows from solving the Boltzmann transport
equation under the relaxation-time approximation; we used phono3py with the
default settings.

## Results

Table 1 lists the computed heat capacity Cv(T) between 100 K and 500 K, and the
room-temperature lattice thermal conductivity kappa = 2.31 W/mK. The tetrahedron
integration gives a slightly larger DOS than Gaussian broadening.

Raw data (frequencies, Cv(T), kappa(T)) are published alongside the article.