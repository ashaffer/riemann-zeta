from fractions import Fraction

from qp_first_gap_uniform_nine_eighths import (
    carry_operator_exponent,
    curvature_dual_rhs,
    first_gap_curvature_endpoint,
    global_trace_exponent,
    replay_first_gap_identities,
    transferred_transverse_exponent,
)


def test_literal_first_gap_identities() -> None:
    replay = replay_first_gap_identities(
        x=101,
        y=97,
        zeta=89,
        a1=83,
        a2=79,
        b1=73,
        b2=71,
        r1=7,
        r2=5,
        s1=3,
        s2=2,
        row_multiplier=11,
        column_multiplier=13,
        separation=4,
    )
    assert replay.identities_hold


def test_curvature_endpoint_is_seventy_one_sixty_fourths() -> None:
    endpoint = first_gap_curvature_endpoint()
    assert endpoint.curvature_exponent == Fraction(71, 64)
    assert endpoint.column_multiplier_height - endpoint.row_multiplier_height == (
        endpoint.row_height - endpoint.column_height
    )


def test_exact_dual_and_global_ledgers() -> None:
    assert curvature_dual_rhs() == Fraction(71, 64)
    assert global_trace_exponent() == Fraction(9, 8)
    assert carry_operator_exponent() == Fraction(9, 32)
    assert transferred_transverse_exponent() == Fraction(7, 11)

