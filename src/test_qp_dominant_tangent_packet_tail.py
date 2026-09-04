from fractions import Fraction

import pytest

from qp_dominant_tangent_packet_tail import (
    column_wedge,
    defect_intercept,
    defects,
    direct_dyadic_bound,
    dominant_height_cap,
    dominant_tail_bound,
    gap_mass_at_cap,
    quadratic_second_difference,
    reconstruct_carriers,
    secant_solution_step,
)


def test_quadratic_curvature_identity():
    for base in (100, 1009):
        for step in (1, 6, 35):
            for t in (1, 3, 11):
                assert quadratic_second_difference(base, step, t) == 2 * step * t * t


def test_height_to_tail_cancellation_is_exact():
    D = Fraction(2**20)
    K = Fraction(2**7)
    J = Fraction(2**2)
    cap = dominant_height_cap(D, K, J)
    assert gap_mass_at_cap(D, cap) == dominant_tail_bound(D, K, J)


def test_dyadic_direct_contribution_loses_only_dominance_factor():
    D = Fraction(3**12)
    K = Fraction(3**4)
    J = Fraction(3**2)
    tail = dominant_tail_bound(D, K, J)
    assert direct_dyadic_bound(K, tail) == 2 * J * D


def test_invalid_scales_are_rejected():
    with pytest.raises(ValueError):
        dominant_height_cap(Fraction(1), Fraction(0), Fraction(1))


def test_wedge_is_exact_defect_line_intercept():
    # The colors satisfy the four parabolic gap identities for
    # r=(2,3), s=(4,5), eta=3, theta=1.
    colors = (101, 79, 69, 54)
    r = (2, 3)
    s = (4, 5)
    b = (50, 61)
    pair = defects(colors, b)
    assert pair == (231, 156)
    assert column_wedge(s, b) == -6
    assert defect_intercept(r, pair) == column_wedge(s, b)


def test_beta_delta_transform_reconstructs_actual_carriers():
    x, y = 101, 79
    s = (4, 5)
    b = (50, 61)
    delta = x * b[0] - y * b[1]
    beta = column_wedge(s, b)
    assert reconstruct_carriers(x, y, s, beta, delta) == b


def test_fixed_wedge_moves_defect_by_exact_gap():
    x, y = 101, 79
    s = (4, 5)
    b = (50, 61)
    d = s[0] * x - s[1] * y
    assert d == 9
    for t in (-7, -1, 2, 9):
        moved = (b[0] + t * s[0], b[1] + t * s[1])
        assert column_wedge(s, moved) == column_wedge(s, b)
        old_delta = x * b[0] - y * b[1]
        new_delta = x * moved[0] - y * moved[1]
        assert new_delta == old_delta + t * d


def test_fixed_defect_solution_step():
    x, y, delta = 101, 79, 17
    step = secant_solution_step(x, y)
    assert step == (79, 101)
    b = (3, (x * 3 - delta) // y)
    # Adding the primitive kernel step leaves the defect unchanged,
    # irrespective of whether this sample happens to be in the shell.
    assert x * (b[0] + step[0]) - y * (b[1] + step[1]) == x * b[0] - y * b[1]
