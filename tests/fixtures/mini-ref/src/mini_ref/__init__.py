"""Mini-reference package for cap-align acceptance tests.

A deliberately small harmonic-phonon toolkit. It exists so the inventory
heuristics have something deterministic to read — the acceptance test checks
what the aligner reports, not what this code computes.
"""

from . import cli  # noqa: F401