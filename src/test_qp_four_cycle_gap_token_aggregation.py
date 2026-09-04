from fractions import Fraction

from qp_four_cycle_gap_token_aggregation import (
    divisor_lift_bound_is_valid,
    fixed_direction_merger_applies,
    normalized_gcd_line_ledger,
    occupied_line_square_root_bound_is_valid,
    occupied_parabolic_line_ledger,
    primitive_lifts_of_gap,
    refined_parabolic_exponent_ledger,
    thin_strip_certificate,
)


def test_qp_exponents_satisfy_thin_strip_certificate() -> None:
    # Finite integer replay of q=D^(33/16)>D^2.  Taking D=N^16 and
    # q=N^33, every H<=D has H*D<q for N>1.
    for base in range(2, 8):
        determinant_width = base**16
        shell_scale = base**33
        assert thin_strip_certificate(
            determinant_width,
            determinant_width,
            shell_scale,
        )


def test_divisor_lifting_bound_exhaustively() -> None:
    for gap in range(-60, 61):
        if gap == 0:
            continue
        for radius in range(1, 25):
            assert divisor_lift_bound_is_valid(gap, radius)


def test_gap_lifts_are_primitive_and_exact() -> None:
    lifts = primitive_lifts_of_gap(30, 7)
    assert lifts
    for r1, r2, eta in lifts:
        assert r2 * eta == 30
        assert r1 and r2


def test_canonical_occupied_line_multiplier_and_divisibility() -> None:
    # K'=[[0,10],[6,7]], a=(2,5), b=(4,9).  The primitive
    # longitudinal direction is (A,B)=(1,-3).
    ledger = occupied_parabolic_line_ledger(
        eta=6,
        theta=10,
        gamma=7,
        u=2,
        alpha=5,
        v=4,
        beta=9,
    )
    assert ledger.determinant == -60
    assert ledger.common_level == 615
    assert ledger.transverse_gcd == 30
    assert (ledger.row_multiplier, ledger.column_multiplier) == (1, -3)
    assert ledger.quadratic_multiplier == -3
    assert ledger.primitive_direction
    assert ledger.transverse_scale_divides_level_discriminant


def test_normalized_gcd_reduction_cancels_transverse_contents() -> None:
    # (eta,beta)=3*(2,3), (theta,alpha)=5*(2,1).  Thus
    # g0=gcd(2*1,2*3)=2 and (|A|,|B|)=(1,3).
    ledger = normalized_gcd_line_ledger(
        eta=6,
        theta=10,
        alpha=5,
        beta=9,
    )
    assert ledger.eta_beta_content == 3
    assert ledger.theta_alpha_content == 5
    assert (ledger.eta_reduced, ledger.beta_reduced) == (2, 3)
    assert (ledger.theta_reduced, ledger.alpha_reduced) == (2, 1)
    assert ledger.reduced_cross_gcd == 2
    assert (ledger.row_multiplier, ledger.column_multiplier) == (1, 3)
    assert ledger.inverse_quadratic_multiplier == Fraction(1, 3)


def test_rich_merger_threshold_leaves_two_point_chords_residual() -> None:
    assert not fixed_direction_merger_applies(0)
    assert not fixed_direction_merger_applies(1)
    assert not fixed_direction_merger_applies(2)
    assert fixed_direction_merger_applies(3)
    assert fixed_direction_merger_applies(20)


def test_occupied_line_ordering_has_square_root_cost() -> None:
    for line_count in range(0, 500):
        assert occupied_line_square_root_bound_is_valid(line_count)


def test_refined_parabolic_lp_has_the_claimed_sharp_endpoint() -> None:
    ledger = refined_parabolic_exponent_ledger(
        row_height=Fraction(11, 16),
        column_height=Fraction(3, 16),
        eta_height=Fraction(0),
        theta_height=Fraction(1),
        gcd_height=Fraction(0),
    )
    assert ledger.plane_covolume == Fraction(11, 8)
    assert ledger.slice_multiplicity == Fraction(5, 16)
    assert ledger.relation_mass == Fraction(15, 16)
    assert ledger.singleton_contribution == Fraction(5, 4)
    assert ledger.curvature_contribution == Fraction(37, 32)
    assert ledger.scoped_bounds_hold


def test_polynomial_gcd_gain_offsets_the_covolume_content() -> None:
    ledger = refined_parabolic_exponent_ledger(
        row_height=Fraction(5, 16),
        column_height=Fraction(11, 16),
        eta_height=Fraction(7, 8),
        theta_height=Fraction(1, 8),
        gcd_height=Fraction(1, 8),
    )
    assert ledger.plane_covolume == Fraction(11, 8)
    assert ledger.relation_mass == Fraction(7, 8)
    assert ledger.singleton_contribution == Fraction(19, 16)
    assert ledger.curvature_contribution == Fraction(33, 32)
    assert ledger.scoped_bounds_hold
