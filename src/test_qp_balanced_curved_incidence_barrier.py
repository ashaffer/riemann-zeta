from fractions import Fraction

import pytest

from qp_balanced_curved_incidence_barrier import (
    CurvedIncidenceLedger,
    active_ledger,
    exact_binned_product_energy,
    logarithmic_group_sum,
    pigeonhole_pair_energy_floor,
)


def test_active_curvature_ledger() -> None:
    ledger = active_ledger()
    assert ledger.residual_exponent == Fraction(16, 33)
    assert ledger.hard_width_exponent == Fraction(49, 33)
    assert ledger.raw_tensor_exponent == Fraction(8, 33)
    assert ledger.lettington_curvature_exponent == Fraction(3, 2)
    assert ledger.lettington_loss == Fraction(1, 66)


def test_exact_logarithmic_group_form() -> None:
    a, b, c = 11.0, 13.0, 17.0
    center = 2000.0
    residual = a * b * c - center
    assert logarithmic_group_sum(a, b, c, residual, center) == pytest.approx(0.0)


def test_pigeonhole_energy_floor() -> None:
    pair_count = 100
    ambient_length = 1000
    bin_width = 40
    assert pigeonhole_pair_energy_floor(pair_count, ambient_length, bin_width) == 400.0


def test_finite_product_bins_obey_cauchy_floor() -> None:
    nodes = (11, 13, 17, 19, 23)
    width = 20
    products = [a * b for a in nodes for b in nodes]
    ambient = max(products) - min(products) + 1
    floor = pigeonhole_pair_energy_floor(len(products), ambient, width)
    assert exact_binned_product_energy(nodes, width) >= floor


def test_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        CurvedIncidenceLedger(Fraction(3, 2))
    with pytest.raises(ValueError):
        logarithmic_group_sum(0.0, 1.0, 1.0, 0.0, 1.0)
    with pytest.raises(ValueError):
        pigeonhole_pair_energy_floor(1, 1, 0)
    with pytest.raises(ValueError):
        exact_binned_product_energy((), 1)
