from fractions import Fraction

from qp_critical_walsh_codegree_audit import (
    CommonNeighborWalk,
    constant_determinant_path_step,
    critical_walsh_exponent_ledger,
    transverse_common_neighbor_ledger,
)


def test_critical_flat_bin_moves_the_walsh_tail_to_seven_eighths() -> None:
    ledger = critical_walsh_exponent_ledger()
    assert ledger.support_exponent == Fraction(15, 8)
    assert ledger.refined_randomized_exponent == Fraction(1, 8)
    assert ledger.automatic_carleson_cutoff_exponent == Fraction(7, 8)
    assert ledger.close_row_gap_exponent == Fraction(3, 8)
    assert ledger.close_row_remainder_exponent == Fraction(13, 16)
    assert ledger.close_row_covers_cutoff


def test_tangent_common_neighbor_fan_replays_both_transverse_identities() -> None:
    # The triples are the two adjacent rows of the exact integer tangent grid:
    # x=m+1, y=m+2, v_j=m+2L+j,
    # a_j=m-2L-1-j, b_j=m-2L-2-j.
    length = 6
    center = 100 * length**3
    q = 2 * center
    x = center + 1
    y = center + 2
    walks = tuple(
        CommonNeighborWalk(
            carrier=center + 2 * length + j,
            first_completion=center - 2 * length - 1 - j,
            second_completion=center - 2 * length - 2 - j,
        )
        for j in range(1, length + 1)
    )
    ledger = transverse_common_neighbor_ledger(q, x, y, walks)
    assert ledger.walk_count == length
    assert ledger.maximum_residual_identity_error == 0
    assert ledger.maximum_product_identity_error == 0
    assert ledger.maximum_determinant_identity_error == 0
    assert ledger.completion_gaps == (1,) * length
    assert ledger.distinct_defects == length
    assert ledger.completion_determinant_energy >= (
        ledger.determinant_energy_cauchy_lower
    )
    assert ledger.nonzero_determinant_energy >= (
        ledger.nonzero_determinant_energy_cauchy_lower
    )
    assert ledger.most_popular_determinant_multiplicity == length - 1


def test_constant_determinant_path_in_a_narrow_collar_is_an_exact_ap() -> None:
    points = tuple((100 + index, 101 + index) for index in range(8))
    determinants = tuple(
        a * d - c * b for (a, b), (c, d) in zip(points, points[1:])
    )
    assert determinants == (-1,) * 7
    assert constant_determinant_path_step(points) == (1, 1)
