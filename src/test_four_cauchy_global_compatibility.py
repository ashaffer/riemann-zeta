"""Regression tests for the exact R185 compatibility fixtures."""

from __future__ import annotations

from fractions import Fraction

import pytest

from four_cauchy_global_compatibility import (
    charged_contact_countermodel,
    chebyshev_propagation,
    fourth_root_filter,
    four_cauchy_hankel_determinant,
    left_exterior_moment_filter,
    projection_cocycle,
    right_exterior_moment_filter,
    root_filtered_right_series,
    toeplitz_contact,
)


Q = Fraction


@pytest.mark.parametrize("exponent", range(20))
def test_fourth_root_filter_selects_multiples_of_four(exponent: int) -> None:
    ledger = fourth_root_filter(exponent)
    assert ledger.power_sum_imaginary == 0
    assert ledger.power_sum_real == ledger.expected_real


def test_right_completion_cancels_only_the_leading_lerch_mode() -> None:
    ledger = right_exterior_moment_filter(
        Q(3), {-1: Q(2), 1: Q(5), 5: Q(7), 9: Q(-4)}, Q(11)
    )
    assert ledger.cancellation_defect == 0
    assert ledger.surviving_pole == 6
    assert ledger.higher_lerch_modes == Q(-563, 19683)
    assert ledger.exterior_total == Q(-98978, 19683)


def test_left_completion_is_the_reflected_filter() -> None:
    ledger = left_exterior_moment_filter(
        Q(1, 3), {-9: Q(4), -5: Q(-7), -1: Q(2), 1: Q(5)}, Q(11)
    )
    assert ledger.cancellation_defect == 0
    assert ledger.surviving_pole == 15
    assert ledger.higher_lerch_modes == Q(563, 19683)
    assert ledger.exterior_total == Q(79295, 19683)


def test_root_filtered_series_keeps_every_fourth_moment() -> None:
    moments = {0: Q(3), 1: Q(100), 4: Q(-5), 7: Q(200), 8: Q(11)}
    x = Q(2)
    expected = -2 * (Q(3) / x + Q(-5) / x**5 + Q(11) / x**9)
    assert root_filtered_right_series(x, moments) == expected


def test_projection_leakage_and_product_cocycle_are_exact() -> None:
    projection = ((Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(0)))
    first = ((Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(1)), (Q(1), Q(0), Q(0)))
    second = ((Q(1), Q(2), Q(0)), (Q(0), Q(1), Q(3)), (Q(4), Q(0), Q(1)))
    ledger = projection_cocycle(projection, first, second)
    assert ledger.leakage_left == ledger.leakage_via_commutator
    assert not any(any(row) for row in ledger.leakage_defect)
    assert ledger.product_commutator_left == ledger.product_commutator_right
    assert not any(any(row) for row in ledger.product_commutator_defect)


@pytest.mark.parametrize(
    ("a", "c", "d"),
    [(Q(0), Q(0), Q(0)), (Q(1, 2), Q(-1, 2), Q(7)), (Q(-3, 4), Q(5, 6), Q(-2))],
)
def test_toeplitz_determinant_factorization(a: Q, c: Q, d: Q) -> None:
    ledger = toeplitz_contact(a, c, d)
    assert ledger.determinant == ledger.determinant_factorization


def test_even_contact_requires_the_chebyshev_next_lag() -> None:
    a = Q(2, 3)
    c = 2 * a * a - 1
    d = 2 * a * c - a
    ledger = toeplitz_contact(a, c, d)
    assert ledger.determinant == 0
    assert ledger.r2 == 0
    assert ledger.r3 == 0
    assert ledger.even_contact_residual == (0, 0)
    assert not any(any(row) for row in ledger.even_factor_defect)
    assert chebyshev_propagation(a, 3)[3] == d


def test_even_contact_can_retain_a_nonzero_global_charge() -> None:
    a = Q(2, 3)
    c = 2 * a * a - 1
    ledger = toeplitz_contact(a, c, Q(0))
    assert ledger.determinant == 0
    assert ledger.even_contact_residual == (ledger.r3, ledger.r3)
    assert ledger.r3 != 0


def test_odd_contact_requires_reflected_next_lag() -> None:
    a = Q(3, 5)
    ledger = toeplitz_contact(a, Q(1), a)
    assert ledger.determinant == 0
    assert ledger.odd_contact_residual == (0, 0)


def test_rational_charged_contact_is_exact_and_psd() -> None:
    ledger = charged_contact_countermodel()
    assert ledger.old_residual == (0, 0, 0)
    assert ledger.exterior_charge == (Q(-229319, 32760),) * 2
    assert not any(any(row) for row in ledger.idempotent_scaling_defect)
    assert ledger.completion_adjustments[:2] == (Q(37, 15), Q(3569, 1020))


def test_four_cauchy_geometric_sequence_has_nonzero_hankel_witnesses() -> None:
    for order in range(1, 5):
        assert four_cauchy_hankel_determinant(order) > 0


@pytest.mark.parametrize(
    ("call", "message"),
    [
        (lambda: fourth_root_filter(-1), "nonnegative"),
        (lambda: right_exterior_moment_filter(0, {}), "positive"),
        (lambda: left_exterior_moment_filter(-1, {}), "positive"),
        (lambda: right_exterior_moment_filter(1, {1.5: 2}), "integers"),
        (lambda: root_filtered_right_series(1, {True: 2}), "integers"),
        (lambda: chebyshev_propagation(1, -1), "nonnegative"),
        (lambda: four_cauchy_hankel_determinant(0), "positive"),
    ],
)
def test_invalid_inputs_fail_closed(call: object, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        call()  # type: ignore[operator]
