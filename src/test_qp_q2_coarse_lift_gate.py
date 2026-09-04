from fractions import Fraction

from qp_q2_coarse_lift_gate import (
    aligned_unit_residual_size,
    principal_density,
    project_q2_coarse_exponent_ledger,
    q2_conductor_counts,
    unit_fibre_count,
)


def test_q2_conductor_counts() -> None:
    counts = q2_conductor_counts(11)
    assert counts.principal == 1
    assert counts.nonprincipal_conductor_q == 9
    assert counts.primitive_conductor_q_squared == 100
    assert counts.total == 110


def test_aligned_residual_and_principal_density() -> None:
    assert aligned_unit_residual_size(11, 3) == 60
    assert principal_density(11, 3) == Fraction(6, 11)
    for residue in range(1, 11):
        assert unit_fibre_count(11, 3, residue) == 6


def test_project_bandwidth_and_square_budget() -> None:
    row = project_q2_coarse_exponent_ledger()
    assert row.degree_in_q == Fraction(16, 33)
    assert row.additive_packet_count_in_q == Fraction(17, 33)
    assert row.packet_centre_maximum_in_q == Fraction(50, 33)
    assert row.fine_mellin_bandwidth_in_q == Fraction(50, 33)
    assert row.residual_rms_in_q == Fraction(49, 66)
    assert row.burgess_r2_in_q == Fraction(295, 264)
    assert row.flat_packet_l2_mass_in_q == Fraction(-17, 33)
    assert row.square_function_budget_in_q == Fraction(16, 33)
    assert row.square_function_budget_in_q == row.desired_squared_norm_in_q
    assert row.polya_vinogradov_in_q < row.burgess_r2_in_q
