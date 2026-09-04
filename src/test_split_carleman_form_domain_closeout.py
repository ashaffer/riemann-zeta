"""Regression tests for the exact R186 finite fixtures."""

from fractions import Fraction

import pytest

from split_carleman_form_domain_closeout import (
    arcsine_falsifier,
    finite_part_counterterm,
    reciprocal_synthetic_contact,
    root_partial_fractions,
)


Q = Fraction


@pytest.mark.parametrize(
    ("x", "y"), [(Q(2), Q(1)), (Q(5, 3), Q(2, 7)), (Q(3, 4), Q(7, 5))]
)
def test_both_fourth_root_partial_fractions_are_exact(x: Q, y: Q) -> None:
    ledger = root_partial_fractions(x, y)
    assert ledger.left_root_sum == ledger.left_collapsed
    assert ledger.right_root_sum == ledger.right_collapsed


def test_finite_part_counterterm_leaves_only_endpoint_terms() -> None:
    ledger = finite_part_counterterm(Q(97, 11), Q(5, 7), Q(-13, 17))
    assert ledger.defect == 0
    assert (
        ledger.left_constant_integral
        + ledger.right_constant_integral
        + ledger.subtraction
        == ledger.surviving_endpoint_term
    )


def test_default_synthetic_contact_is_exact_psd_and_charged() -> None:
    ledger = reciprocal_synthetic_contact()
    assert ledger.local_completion == Q(2039, 255)
    assert ledger.old_matrix == (
        (Q(4079, 255), Q(781, 105), Q(4079, 255)),
        (Q(781, 105), Q(4079, 255), Q(781, 105)),
        (Q(4079, 255), Q(781, 105), Q(4079, 255)),
    )
    assert ledger.old_residual == (0, 0, 0)
    assert all(value >= 0 for value in ledger.principal_minors_1)
    assert ledger.principal_minors_2 == (
        Q(42599672, 212415), Q(0), Q(42599672, 212415)
    )
    assert ledger.determinant == 0
    assert ledger.exterior_cauchy == Q(6688, 4095)
    assert ledger.exterior_total == Q(201161, 8190)
    assert ledger.left_exterior_total == -ledger.exterior_total


@pytest.mark.parametrize("ratio", [Q(3, 2), Q(2), Q(5, 2), Q(3)])
def test_reciprocal_family_has_exact_old_null_and_positive_exterior(ratio: Q) -> None:
    ledger = reciprocal_synthetic_contact(ratio, Q(0))
    assert ledger.old_residual == (0, 0, 0)
    assert ledger.exterior_cauchy > 0
    assert ledger.exterior_total > 0


def test_arcsine_local_data_has_zero_average_but_nonzero_exterior() -> None:
    ledger = arcsine_falsifier()
    assert ledger.plemelj_average == 0
    assert ledger.exterior_modulus_squared == Q(1, 12) > 0


@pytest.mark.parametrize(
    ("call", "message"),
    [
        (lambda: root_partial_fractions(1, 1), r"x\^4"),
        (lambda: root_partial_fractions(0, 2), "nonzero"),
        (lambda: reciprocal_synthetic_contact(1), "exceed"),
        (lambda: reciprocal_synthetic_contact(2, -1), "nonnegative"),
    ],
)
def test_invalid_inputs_fail_closed(call: object, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        call()  # type: ignore[operator]
