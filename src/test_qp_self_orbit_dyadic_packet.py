from fractions import Fraction

import pytest

from qp_self_orbit_dyadic_packet import (
    affine_area,
    certify_local_affine_packet,
    cleared_reciprocal_collision,
    close_direction_certificate,
    critical_dyadic_packet_ledger,
    cross_determinant_from_labels,
    drpls_block_l1_bound,
    label_area_identity,
    orbit_label,
    reciprocal_chart_difference,
    tower_coordinate_identities,
    tower_easy_sector_ledger,
)


def test_label_area_identity_and_local_affine_packet() -> None:
    anchor = (10_007, 10_009)
    # Label zero is the reflected anchor (C,c), not (c,C).
    points = tuple((anchor[1] + n, anchor[0] + n) for n in range(-4, 5))
    assert [orbit_label(anchor, point) for point in points] == [
        -2 * n for n in range(-4, 5)
    ]
    for first in range(len(points) - 2):
        left, right = label_area_identity(
            anchor, points[first], points[first + 1], points[first + 2]
        )
        assert left == right == 0
    certificate = certify_local_affine_packet(anchor, points, degree=8, radius=8)
    assert certificate.all_collinear
    assert certificate.area_numerator_bound == 256 < certificate.anchor_denominator
    assert affine_area(points[0], points[4], points[-1]) == 0


def test_local_affine_packet_checks_its_hypotheses() -> None:
    anchor = (10_007, 10_009)
    points = ((10_009, 10_007), (10_010, 10_008), (10_011, 10_009))
    with pytest.raises(ValueError, match="not strict"):
        certify_local_affine_packet(anchor, points, degree=1_000, radius=8)


def test_close_direction_is_a_legendre_direction() -> None:
    anchor = (10_007, 10_009)
    first = (anchor[1], anchor[0])
    second = (first[0] + 12, first[1] + 12)
    certificate = close_direction_certificate(anchor, first, second)
    assert certificate.primitive_direction == (1, 1)
    assert certificate.multiplicity == 12
    assert certificate.label_step == -2
    assert certificate.satisfies_legendre


def test_cross_determinant_and_reciprocal_chart_identities() -> None:
    anchor = (101, 103)
    first = (107, 109)
    second = (113, 127)
    assert cross_determinant_from_labels(anchor, first, second)[0] == (
        cross_determinant_from_labels(anchor, first, second)[1]
    )
    direct, formula = reciprocal_chart_difference(1_001, first, second)
    assert direct == formula
    for left, right in tower_coordinate_identities(anchor, (17, 16), first):
        assert left == right


def test_cleared_collision_identity() -> None:
    Q = Fraction(1_001**3, 8)
    direct, residual = cleared_reciprocal_collision(Q, 107 * 127, 113 * 109, 3)
    assert direct == residual


def test_critical_exponents_and_drpls_closure() -> None:
    ledger = critical_dyadic_packet_ledger()
    assert ledger.degree == Fraction(16, 33)
    assert ledger.low_frequency == Fraction(1, 33)
    assert ledger.top_frequency == Fraction(17, 33)
    assert ledger.largest_packet_radius == Fraction(16, 33)
    assert ledger.smallest_packet_radius == Fraction(8, 33)
    assert ledger.affine_integrality_margin == Fraction(1, 33)
    assert ledger.low_mode_l1 == 1
    assert ledger.one_block_l1 == 1
    assert ledger.selberg_output == Fraction(16, 33)
    assert drpls_block_l1_bound(10_000.0, 125.0) == pytest.approx(10_000.0)


def test_tower_easy_sector_thresholds() -> None:
    # q=10^12, D=10^4, K=10^6 gives R=10^3.  The easy thresholds are
    # |r|>=200 and ||U||>=10 (the factor two in the first is explicit).
    by_remainder = tower_easy_sector_ledger(10**12, 10**4, 10**6, 200, 1)
    assert by_remainder.closes_by_remainder
    assert by_remainder.crude_packet_square_bound <= by_remainder.drpls_target
    by_direction = tower_easy_sector_ledger(10**12, 10**4, 10**6, 1, 10)
    assert by_direction.closes_by_direction_size
    assert by_direction.crude_packet_square_bound <= by_direction.drpls_target
    hard = tower_easy_sector_ledger(10**12, 10**4, 10**6, 50, 2)
    assert not hard.closes_by_remainder
    assert not hard.closes_by_direction_size
    assert hard.crude_packet_square_bound > hard.drpls_target
