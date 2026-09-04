from fractions import Fraction

import pytest

from qp_self_restriction_assembly import (
    dyadic_fejer_sum,
    flat_mixed_energy_exponent,
    fourier_cauchy_ratio,
    infinite_dyadic_fejer_sum,
    self_to_mixed_constant_exponent,
    sharp_min_weighted_norm_exponent,
    sidon_nonfactorable_gap,
    symmetric_over_sharp_norm_gap,
    weighted_fejer_norm_exponent,
)


def test_exact_self_to_mixed_and_flat_ledgers() -> None:
    u = Fraction(1, 10)
    v = Fraction(1, 6)
    assert self_to_mixed_constant_exponent(u, v) == Fraction(17, 30)
    assert flat_mixed_energy_exponent(u, v) == Fraction(17, 6)
    assert weighted_fejer_norm_exponent(u, v) == Fraction(53, 60)


def test_symmetric_loss_over_sharp_min_is_one_eighth_of_imbalance() -> None:
    m = Fraction(1, 20)
    M = Fraction(3, 20)
    assert symmetric_over_sharp_norm_gap(m, M) == Fraction(1, 80)
    assert weighted_fejer_norm_exponent(m, M) == (
        sharp_min_weighted_norm_exponent(m, M) + Fraction(1, 80)
    )


def test_double_fejer_sum_is_uniformly_bounded() -> None:
    finite = dyadic_fejer_sum(100)
    infinite = infinite_dyadic_fejer_sum()
    assert finite <= infinite < 2.0
    assert finite**2 < 4.0


@pytest.mark.parametrize(
    "left,right",
    [
        ([1, 2, 3], [2, -1]),
        ([1 + 2j, -3j, 4], [2 - 1j, 0, 5j]),
        ([1], [1, 2, 4, 8]),
        ([0, 0], [1, 2]),
    ],
)
def test_finite_fourier_cauchy(left: list[complex], right: list[complex]) -> None:
    assert fourier_cauchy_ratio(left, right) <= 1.0 + 1.0e-12


def test_nonfactorable_pair_space_is_not_a_scalar_consequence() -> None:
    scalar_constant, pair_block_norm = sidon_nonfactorable_gap(12)
    assert scalar_constant < 2
    assert pair_block_norm == 12


def test_invalid_order_is_rejected() -> None:
    with pytest.raises(ValueError):
        sharp_min_weighted_norm_exponent(Fraction(1, 3), Fraction(1, 4))
