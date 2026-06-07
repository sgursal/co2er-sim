"""
Unit tests for Butler-Volmer electrode kinetics module.
"""

from src.kinetics.butler_volmer import compute_current_density


def test_bv_zero_overpotential():
    i = compute_current_density(1.0, 0.5, 0.5, 0.5, 0, 298, 1)
    assert abs(i) < 1e-12
    pass
