from fractions import Fraction

import pytest

from qp_four_cycle_topk_tail_profile import (
    ONE_TAIL_RECIPROCALS,
    TWO_TAIL_RECIPROCALS,
    flat_topk_tail_mass,
    normalized_topk_tail_mass,
    topk_tail_ledger,
    topk_tail_trace_exponent,
)


def test_mixed_interpolation_endpoints_have_total_reciprocal_three() -> None:
    assert sum(ONE_TAIL_RECIPROCALS) == 3
    assert sum(TWO_TAIL_RECIPROCALS) == 3
    assert ONE_TAIL_RECIPROCALS[-1] == Fraction(1, 2)
    assert TWO_TAIL_RECIPROCALS[-2:] == (Fraction(1, 2), Fraction(1, 2))


def test_exact_sufficient_fc_thresholds() -> None:
    ledger = topk_tail_ledger()
    assert ledger.top_cutoff == Fraction(1, 2)
    assert ledger.parabolic_tail_decay_required == Fraction(1, 6)
    assert ledger.broad_tail_decay_required == Fraction(5, 24)
    assert ledger.tail_decay_required == Fraction(5, 24)
    assert not ledger.flat_on_degree_support_is_closed
    assert not ledger.iteration_removes_flat_barrier

    assert topk_tail_trace_exponent(Fraction(1, 2), Fraction(5, 24)) == 1


def test_crossing_either_threshold_loses_a_power() -> None:
    assert topk_tail_trace_exponent(Fraction(1, 2) + Fraction(1, 100), Fraction(1)) > 1
    assert topk_tail_trace_exponent(Fraction(0), Fraction(5, 24) - Fraction(1, 100)) > 1


def test_tail_mass_uses_largest_coordinates() -> None:
    weights = [1, 2, 3, 4]
    assert normalized_topk_tail_mass(weights, 2) == pytest.approx(5 / 30)
    assert normalized_topk_tail_mass(weights, 10) == 0
    assert normalized_topk_tail_mass([], 0) == 0
    with pytest.raises(ValueError):
        normalized_topk_tail_mass(weights, -1)


def test_flat_on_degree_support_is_the_exact_iteration_barrier() -> None:
    degree = 10_000
    assert flat_topk_tail_mass(degree, 100) == Fraction(99, 100)
    assert flat_topk_tail_mass(degree, degree // 2) == Fraction(1, 2)
    assert flat_topk_tail_mass(degree, degree) == 0
