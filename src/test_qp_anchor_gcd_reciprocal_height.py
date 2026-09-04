from fractions import Fraction

from qp_anchor_gcd_reciprocal_height import (
    anchored_normalized_gcd_majorant,
    content,
    core_tail_exponent,
    defect_cross_identity,
    low_determinant_factorial_bound,
    primitive_height,
    quotient_coordinates,
    quotient_defect_identity,
    reciprocal_height_sum,
)


def test_defect_cross_identity_and_content():
    rows = ((101, 97), (103, 101), (107, 109))
    gamma = (113, 127)
    partner = (131, 137)
    left, right = defect_cross_identity(rows, gamma, partner)
    assert left == right
    k = abs(gamma[0] * partner[1] - gamma[1] * partner[0])
    raw_content = content(
        (
            rows[1][0] * rows[2][1] - rows[2][0] * rows[1][1],
            rows[2][0] * rows[0][1] - rows[0][0] * rows[2][1],
            rows[0][0] * rows[1][1] - rows[1][0] * rows[0][1],
        )
    )
    assert content(left) == k * raw_content


def test_normalized_gcd_expression_majorizes_reciprocal_height():
    rows = tuple((1009 + i, 1013 + 2 * i + i * i) for i in range(9))
    assert reciprocal_height_sum(rows) <= anchored_normalized_gcd_majorant(rows)


def test_tangent_packet_is_within_quadratic_scale():
    for order in (4, 8, 16):
        rows = tuple((10_000 + i, 10_001 + i) for i in range(order))
        total = reciprocal_height_sum(rows)
        assert total <= anchored_normalized_gcd_majorant(rows)
        assert total <= order * order


def test_primitive_height_is_scale_invariant():
    rows = ((11, 13), (17, 19), (23, 29))
    doubled = tuple((2 * a, 2 * b) for a, b in rows)
    assert primitive_height(rows) == primitive_height(doubled)


def test_core_excess_threshold_reproduces_five_fourths():
    k = Fraction(5, 16)
    assert core_tail_exponent(k, Fraction(0)) == 1
    assert core_tail_exponent(k, Fraction(1, 8)) == Fraction(5, 4)


def test_low_determinant_second_factorial_is_target_sized():
    D, K = 2**20, 2**7
    partners, factorial = low_determinant_factorial_bound(D, K)
    assert partners == 2 * D // K
    assert factorial == 4 * D * K


def test_unimodular_quotient_defect_identity():
    anchor = (13, 8)
    complement = (8, 5)  # 13*5-8*8=1
    row = (101, 61)
    partner = (89, 55)
    m, e = quotient_coordinates(row, anchor, complement)
    assert row == (
        m * anchor[0] - e * complement[0],
        m * anchor[1] - e * complement[1],
    )
    assert quotient_defect_identity(row, anchor, partner, complement)[0] == quotient_defect_identity(
        row, anchor, partner, complement
    )[1]
