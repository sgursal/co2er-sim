from src.kinetics.butler_volmer import ButlerVolmer as bv


def test_bv_zero_overpotential():
    i = bv.multi_electron(1.0, 0.5, 0.5, 0.5, 0, 298, 1)
    assert abs(i) < 1e-12
    pass


def test_bv_large_overpotential():
    bv.tafel_approximation()
    pass
