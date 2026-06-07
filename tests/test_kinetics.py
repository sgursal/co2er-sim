"""
Unit tests for Butler-Volmer electrode kinetics module.
"""

from src.kinetics.butler_volmer import compute_current_density


def test_bv_zero_overpotential():
    i = compute_current_density(0.0, 0.5, 0.5, 0.5, 298, 2)
    assert abs(i) < 1e-12
