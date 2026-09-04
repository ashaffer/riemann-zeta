from fractions import Fraction
import math

from qp_a1_weighted_star_h_audit import (
    final_face_exponents,
    two_column_h_packet,
    weighted_a1_star,
)


def test_weighted_star_norm_is_bounded_but_endpoint_copy_costs_sqrt_k() -> None:
    ledger = weighted_a1_star(range(100, 200))
    assert ledger.branches == 100
    assert ledger.operator_norm < 1.0
    assert ledger.copied_endpoint_norm == 10.0
    assert ledger.compressed_coefficient > 7.0
    assert 0.98 < ledger.cauchy_ratio <= 1.0


def test_original_h_two_column_packet_keeps_every_common_neighbour() -> None:
    ledger = two_column_h_packet((3, 4, 5))
    assert ledger.common_neighbours == 12
    assert math.isclose(ledger.incidence_operator_norm, math.sqrt(24))
    assert ledger.gram_off_diagonal == 12
    assert ledger.diagonal_subtracted_operator_norm == 12
    assert ledger.equal_unit_pair_quadratic == 12
    assert ledger.four_distinct_equal_z_quadratic == Fraction(3, 2)


def test_final_face_reproduces_the_exact_missing_square_root_k() -> None:
    ledger = final_face_exponents()
    assert ledger.relation_mass == Fraction(45, 64)
    assert ledger.direction_height == Fraction(26, 64)
    assert ledger.line_count == Fraction(20, 64)
    assert ledger.inverse_sqrt_line_sum == Fraction(10, 64)
    assert ledger.bare_curvature_prefactor == Fraction(19, 64)
    assert ledger.one_line_length == Fraction(9, 64)
    assert ledger.common_neighbour_count == Fraction(29, 64)
    assert ledger.positive_trace == Fraction(74, 64)
    assert ledger.missing_saving == Fraction(10, 64)
