from fractions import Fraction
from math import gcd

from qp_parabolic_double_gcd_and_fixed_determinant import (
    DeterminantVertex,
    content_block_degree_bounds,
    determinant_incidence,
    duplicated_refinement_ledger,
    fixed_determinant_star,
    gcd_cross_majorant,
    invert_gap_coordinates,
    normalized_line_weight_squared,
    paired_residual_ledgers,
    rectangular_gcd_divisor_bound,
    rectangular_gcd_sum,
    survivor_exponent_ledger,
    tangent_congruence_chain,
)


def test_cross_gcd_majorant_prime_by_prime_identity_range() -> None:
    for m in range(1, 15):
        for n in range(1, 15):
            if gcd(m, n) != 1:
                continue
            for alpha in range(1, 12):
                for beta in range(1, 12):
                    left, right = gcd_cross_majorant(m, n, alpha, beta)
                    assert left <= right


def test_rectangular_divisor_expansion_bounds_exact_sum() -> None:
    for m, n, x, y in ((5, 7, 8, 9), (8, 9, 11, 7), (1, 13, 6, 10)):
        exact = rectangular_gcd_sum(m, n, x, y)
        bound = rectangular_gcd_divisor_bound(m, n, x, y)
        assert Fraction(exact) <= bound


def test_normalized_line_weight() -> None:
    # g=gcd(24,30)=6, hence (A,B)=(4,5) and the squared weight is 1/20.
    assert normalized_line_weight_squared(eta=8, theta=5, alpha=3, beta=6) == Fraction(1, 20)


def test_exact_gap_coordinate_inversion() -> None:
    b1, b2 = invert_gap_coordinates(
        x=101,
        y=97,
        s1=3,
        s2=2,
        residual=65,
        wedge=98,
    )
    assert (b1, b2) == (89, 92)


def test_four_token_residual_couplings() -> None:
    ledger = paired_residual_ledgers(
        x=101,
        y=97,
        zeta=204,
        w=197,
        r1=2,
        r2=1,
        s1=3,
        s2=2,
        eta=109,
        theta=1,
        a1=83,
        a2=86,
        b1=89,
        b2=92,
    )
    assert ledger["horizontal_coupling_error"] == 0
    assert ledger["vertical_coupling_error"] == 0
    assert ledger["e_top"] == 65
    assert ledger["e_bottom"] == 32
    assert ledger["beta"] == 98


def test_one_token_congruence_can_contain_a_long_affine_chain() -> None:
    # 3*(2+j)+5*(1+6j)=11*(1+3j), so all points lie on one congruence.
    points = tangent_congruence_chain(
        length=23,
        s1=3,
        y=5,
        residual_start=2,
        residual_step=1,
        wedge_start=1,
        wedge_step=6,
        determinant=11,
    )
    assert len(points) == 23


def test_content_block_schur_bounds_are_symmetric() -> None:
    row, column = content_block_degree_bounds(12, 3)
    assert row == 5
    assert column == Fraction(5, 4)
    swapped = content_block_degree_bounds(3, 12)
    assert swapped == (column, row)


def test_fixed_determinant_star_is_exact_and_sharp_shape() -> None:
    level, right, rows = fixed_determinant_star(31)
    assert right.content == 31
    assert len(rows) >= 8
    for left in rows:
        assert left.content == 1
        assert determinant_incidence(left, right, level)


def test_survivor_exponents() -> None:
    ledger = survivor_exponent_ledger()
    assert ledger["old_total"] == Fraction(37, 32)
    assert ledger["conditional_content_total"] == Fraction(69, 64)
    assert ledger["conditional_primitive_total"] == 1
    assert ledger["endpoint_double_gcd_total"] == Fraction(35, 32)


def test_matching_norm_does_not_pay_for_refinement_duplicates() -> None:
    ledger = duplicated_refinement_ledger(37)
    assert ledger["matching_operator_norm"] == 1
    assert ledger["base_squared_mass"] == 1
    assert ledger["refined_squared_mass"] == 37
    assert ledger["positive_bilinear_value"] == 37
