from math import sqrt

import pytest

from qp_bandpass_partial_permutation_inverse import (
    block_taylor_scales,
    color_fibre_identity,
    cross_ratio_log,
    degenerate_rectangle_mass,
    frobenius_sq,
    latin_uniform_invariants,
    matvec_value,
    rank_one_error_sq,
    rectangle_expansion,
    schur_defect,
    spectral_defect_ledger,
    trace_fourth,
)


def test_coherence_block_has_unit_quadratic_and_small_cubic_scale() -> None:
    quadratic, cubic = block_taylor_scales(10_000.0, 1_000_000.0)
    assert quadratic == pytest.approx(1.0)
    assert cubic == pytest.approx(0.001)


def test_exact_disjoint_color_frobenius_identity() -> None:
    entries = {
        (0, 0): (0, 1.0),
        (0, 1): (1, 0.5j),
        (1, 0): (1, -1.0),
    }
    colors = {0: 0.6 + 0.8j, 1: -0.5j}
    direct, separated = color_fibre_identity(entries, colors)
    assert direct == pytest.approx(separated)


def test_rank_one_endpoint_defect_identity() -> None:
    matrix = ((1.0 + 0.0j, 0.0j), (0.0j, 1.0 + 0.0j))
    left = (1.0 + 0.0j, 0.0j)
    right = (1.0 + 0.0j, 0.0j)
    value_sq = abs(matvec_value(matrix, left, right)) ** 2
    error = rank_one_error_sq(matrix, left, right)
    assert error == pytest.approx(frobenius_sq(matrix) - value_sq)

    ledger = spectral_defect_ledger(2.0, 2.0, 1.0, value_sq)
    assert ledger.total == pytest.approx(2.0 - value_sq)
    assert schur_defect(0.1) == pytest.approx(0.19)


def test_fourth_trace_is_exact_signed_rectangle_expansion() -> None:
    matrix = (
        (1.0 + 1.0j, -0.5j, 0.0j),
        (0.25 + 0.0j, 1.0 - 0.5j, 2.0j),
    )
    assert rectangle_expansion(matrix).imag == pytest.approx(0.0, abs=1e-12)
    assert rectangle_expansion(matrix).real == pytest.approx(trace_fourth(matrix))


def test_degenerate_rectangles_obey_two_frobenius_bound_under_row_column_cap() -> None:
    scale = 1 / sqrt(2)
    matrix = ((scale, scale), (scale, -scale))
    assert degenerate_rectangle_mass(matrix) <= 2 * frobenius_sq(matrix) + 1e-12


def test_latin_square_shows_nontriviality_of_four_cycle_target() -> None:
    for order in (1, 4, 25):
        frobenius, fourth_trace, tensor_value = latin_uniform_invariants(order)
        assert frobenius == pytest.approx(order)
        assert fourth_trace == pytest.approx(order**2)
        assert tensor_value == pytest.approx(sqrt(order))


def test_rectangle_forces_small_color_cross_ratio() -> None:
    residuals = (0.01, -0.02, 0.015, -0.005)
    assert cross_ratio_log(residuals) == pytest.approx(0.01)
    assert abs(cross_ratio_log(residuals)) <= sum(abs(value) for value in residuals)


def test_invalid_ledger_order_is_rejected() -> None:
    with pytest.raises(ValueError):
        spectral_defect_ledger(1.0, 2.0, 1.0, 0.0)
