"""Capability-bearing modules of mini-ref (fixture).

Module boundaries are the capability boundaries the inventory should find:
one module per capability. `qha.py` deliberately does NOT exist — docs/qha.md
claims it, which is the low-confidence trap.
"""

import numpy as np


def force_constants(displacements, forces):
    """Build the 2nd-order force-constant tensor from displacement/force data."""
    return np.einsum("iab,icd->abcd", displacements, forces)


def dynamical_matrix(force_constants, masses, qpoint):
    """Assemble the dynamical matrix D(q) and diagonalize it."""
    return np.diag(np.ones(3))


def dos(frequencies, weights, sigma=0.01):
    """Gaussian-broadened phonon density of states."""
    return np.zeros_like(frequencies)


def thermal_properties(frequencies, temperatures):
    """Free energy / entropy / heat capacity from the phonon frequencies."""
    return np.zeros((len(temperatures), 3))


def main():
    """CLI entry: `phon-vib band|dos|thermal [POSCAR]`."""
    import sys

    print("usage: phon-vib band|dos|thermal [POSCAR]")
    return 0 if len(sys.argv) == 1 else 0