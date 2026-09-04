from fractions import Fraction
from math import isqrt

from qp_pair_sum_selberg_ledger import (
    centered_pair_data,
    centered_window_data,
    common_product_parametrization,
    cross_factorization,
    rational_tangent_point,
    residue_factorization,
    selberg_pair_sum_exponent_ledger,
    symmetric_cubic_caustic_phase,
    two_level_gap_ledger,
    ordered_matching_residuals,
)


def test_selberg_exponents_are_exact() -> None:
    ledger = selberg_pair_sum_exponent_ledger()
    assert ledger["q"] == Fraction(33, 16)
    assert ledger["delta"] == Fraction(-17, 16)
    assert ledger["H"] == Fraction(17, 16)
    assert ledger["zero_zero"] == Fraction(-1, 16)
    assert ledger["one_frequency"] == Fraction(1, 2)
    assert ledger["zero_dual_tangent"] == Fraction(1, 2)
    assert ledger["nonzero_nondegenerate_termwise"] == Fraction(25, 16)
    assert ledger["caustic_pairwise_absolute"] == Fraction(49, 48)
    assert ledger["symmetric_exact_caustic"] == Fraction(-1, 24)
    assert ledger["missing_cancellation_power"] == Fraction(17, 16)


def test_centered_and_cross_factorizations() -> None:
    for a, b, v, w in ((17, 23, 29, 31), (101, 89, 83, 107)):
        data = centered_pair_data(a, b, v, w)
        assert data.S == a + b
        assert data.n == a * v
        assert data.m == b * w
        left, right = cross_factorization(a, b, v, w)
        assert left * right == data.n * data.m


def test_rational_tangent_packet_saturates_square_root_scale() -> None:
    D = 500
    r, s, Q = 2, 3, 10_000
    radius = isqrt(2 * D // (r * s))
    C = r * s * Q * Q - D
    count = 0
    for h in range(-radius, radius + 1):
        a, b, v, w, _ = rational_tangent_point(Q, h, r, s)
        assert abs(a * v - C) <= D
        assert abs(b * w - C) <= D
        count += 1
    assert count == 2 * radius + 1


def test_common_product_parametrization() -> None:
    a, b, v, w, n = common_product_parametrization(12, 7, 11, 13)
    assert (a, b, v, w) == (84, 132, 143, 91)
    assert a * v == b * w == n


def test_symmetric_opposite_sign_saddle_is_exactly_cubic() -> None:
    Q, t = 101, 7
    assert symmetric_cubic_caustic_phase(Q, t, 0) == 2 * t * Q
    for y in (-13, -1, 1, 17):
        phase = symmetric_cubic_caustic_phase(Q, t, y)
        assert phase - 2 * t * Q == Fraction(
            -2 * t * y**3, Q * Q - y * y
        )


def test_scattered_physical_fixture_and_two_level_gap_laws() -> None:
    # Eight genuinely different quotient sums in one full-integer window.
    # Reflecting each row by (a,b,v,w)->(b,a,w,v) gives sixteen points.
    S, C, D = 2176, 1_228_776, 26
    rows = (
        (800, 1376, 1536, 893),
        (917, 1259, 1340, 976),
        (926, 1250, 1327, 983),
        (957, 1219, 1284, 1008),
        (963, 1213, 1276, 1013),
        (976, 1200, 1259, 1024),
        (983, 1193, 1250, 1030),
        (999, 1177, 1230, 1044),
    )
    data = []
    quotient_sums = set()
    for a, b, v, w in rows:
        assert a + b == S
        assert abs(a * v - C) <= D
        assert abs(b * w - C) <= D
        quotient_sums.add(v + w)
        data.append(centered_window_data(a, b, v, w, C))
        residue_factorization(a, b, v, w, C)
    assert len(quotient_sums) == 8

    for left, right in zip(data, data[1:]):
        two_level_gap_ledger(left, right)
    # The rows are listed with increasing a.  Both reciprocal legs are
    # strictly monotone in opposite directions, and the residuals are the
    # corresponding product-label changes.
    for left, right in zip(rows, rows[1:]):
        assert right[2] < left[2]
        assert right[3] > left[3]
        d1, d2 = ordered_matching_residuals(left, right)
        assert abs(d1) <= 2 * D
        assert abs(d2) <= 2 * D
