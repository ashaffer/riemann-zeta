from fractions import Fraction

import pytest

from qp_universal_content_blowup import (
    multiplier_chart_count_exponents,
    multiplier_chart_data,
    nondivisible_zero_offset_family,
    one_band_axis_certificate,
    primitive_point_from_content,
    universal_content_blowup,
)


def test_multiplier_chart_normal_crossing_and_transverse_identity() -> None:
    for p, d, J, c, u in (
        (7, 2, 3, 5, -1),
        (11, 3, 2, -7, 2),
        (13, 4, 5, 9, 3),
    ):
        data = multiplier_chart_data(p, d, J, c, u)
        point = data.point
        assert point.g == 2 * J * d * d
        assert point.Q == J * p * (p * p - d * d) + c
        assert point.y == J * d * (p * p - d * d) + u
        assert data.h == d * c - 2 * p * u
        assert point.e + u * u == J * d * (p - d) * data.left_residual
        assert point.f + u * u == J * d * (p + d) * data.right_residual


def test_all_multiplier_height_count_has_one_over_48_margin() -> None:
    ledger = multiplier_chart_count_exponents()
    assert ledger["height_count"] == Fraction(23, 48)
    assert ledger["balanced_height_count"] == Fraction(23, 144)
    assert ledger["saving"] == Fraction(1, 48)


def test_universal_blowup_is_exact_for_genuinely_nondivisible_content() -> None:
    point = primitive_point_from_content(211, 83, 6, 10, 3)
    assert point.g % (point.d * point.d) != 0
    normal = universal_content_blowup(point)
    assert normal.C == 2 * 3 * 3 * 211 - 6 * 10 * (100 - 9)
    assert normal.U == 2 * 3 * 83 - 6 * (100 - 9)
    assert 2 * point.d * point.n == -(normal.H + point.p * normal.U)


def test_left_one_band_axis_has_two_fixed_Q_divisors() -> None:
    # (p,d,g,Q,y)=(4,3,6,13,8) is off d^2|g and has H-dU=0.
    point = primitive_point_from_content(13, 8, 6, 4, 3)
    certificate = one_band_axis_certificate(point)
    assert certificate == {
        "xi": 1,
        "content_quotient": 2,
        "axis": "left",
        "p_target": 12,
        "second_target": 14,
        "second_divisor": 7,
    }
    assert (point.e, point.n) == (-1, -7)


def test_right_one_band_axis_and_asymmetric_second_root() -> None:
    point = primitive_point_from_content(11, 8, 6, 4, 3)
    certificate = one_band_axis_certificate(point)
    assert certificate["axis"] == "right"
    assert certificate["xi"] == 1
    assert (point.f, point.n) == (-1, -1)

    # Here xi=-g(p-d), so the narrow error vanishes although xi is large.
    bad = primitive_point_from_content(18, 9, 2, 4, 1)
    bad_certificate = one_band_axis_certificate(bad)
    assert (bad.e, bad.f) == (0, -36)
    assert bad_certificate["axis"] == "right"
    assert bad_certificate["xi"] == -6
    assert bad_certificate["eta"] == 0
    assert bad_certificate["eta_target"] == 36
    assert bad_certificate["third_target"] == 36
    assert bad_certificate["third_divisor"] == 2


def test_one_band_certificate_rejects_the_two_factor_locus() -> None:
    point = nondivisible_zero_offset_family(7, 3)
    with pytest.raises(ValueError, match="exactly one"):
        one_band_axis_certificate(point)


def test_nondivisible_zero_offset_family_is_remote_and_two_factor() -> None:
    for d in (3, 7, 12, 25):
        point = nondivisible_zero_offset_family(d, 3)
        p = 3 * d + 1
        normal = universal_content_blowup(point)
        assert point.g == 2 * d
        assert point.g % (d * d) != 0
        assert point.Q > point.y > point.Q ** Fraction(2, 3)
        assert (point.e, point.f) == (-(p - d), -(p + d))
        assert normal.U == 0
        assert normal.H == normal.left_residual == normal.right_residual == -2 * d


def test_invalid_multiplier_chart_is_rejected() -> None:
    with pytest.raises(ValueError):
        multiplier_chart_data(6, 2, 1, 0, 0)

