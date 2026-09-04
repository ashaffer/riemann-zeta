from fractions import Fraction
from math import comb

from qp_high_completion_tail_gate import (
    bilinear_parabola_matching,
    critical_scattered_ledger,
    factorial_tail_ledger,
    residual_cross_ledger,
    tangent_triple_height_ledger,
    tail_exponent_ledger,
    two_sided_critical_ledger,
    two_sided_residual_ledger,
    two_point_residual_line_bound,
)


def test_factorial_anchor_identities_and_high_tail_majorants() -> None:
    # Columns 0 and 1 have codegree four; column 2 meets them in two rows.
    incidence = [
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 1],
    ]
    ledger = factorial_tail_ledger(incidence, threshold=3)
    assert ledger.codegrees[0][1] == 4
    assert ledger.codegrees[0][2] == 2
    assert ledger.second_factorial_row_sums == ledger.second_anchor_identity_sums
    assert ledger.third_factorial_row_sums == ledger.third_anchor_identity_sums
    assert ledger.high_ordered_pairs == 2
    assert ledger.second_high_row_sums == (6, 6, 0, 0)
    assert ledger.third_high_row_sums == (4, 4, 0, 0)
    assert ledger.second_majorant_numerator >= 2 * comb(3, 2)
    assert ledger.third_majorant_numerator >= 2 * comb(3, 3)


def test_k23_reciprocal_height_gate_is_exactly_r_le_two_k() -> None:
    ledger = tail_exponent_ledger(
        multiplicity=Fraction(5, 16),
        reciprocal_height=Fraction(5, 8),
        occupied_line_count=Fraction(3, 16),
    )
    assert ledger.reciprocal_height_required == Fraction(5, 8)
    assert ledger.third_factorial_tail == ledger.desired_tail == Fraction(11, 16)
    assert ledger.curvature_tail == Fraction(25, 32)
    assert ledger.curvature_loss == Fraction(3, 32)


def test_subpower_occupied_lines_give_the_sharp_parabolic_tail() -> None:
    ledger = tail_exponent_ledger(
        multiplicity=Fraction(7, 32),
        reciprocal_height=Fraction(0),
        occupied_line_count=Fraction(0),
    )
    assert ledger.curvature_tail == ledger.desired_tail == Fraction(25, 32)


def test_critical_scattered_endpoint_has_exact_quarter_power_gap() -> None:
    ledger = critical_scattered_ledger()
    assert ledger.multiplicity == Fraction(5, 16)
    assert ledger.current_color_mass == Fraction(15, 16)
    assert ledger.required_color_mass == Fraction(11, 16)
    assert ledger.missing_saving == Fraction(1, 4)
    assert ledger.current_completed_mass == Fraction(5, 4)
    assert ledger.target_completed_mass == 1
    assert ledger.closed_determinant_range == Fraction(11, 16)
    assert ledger.remaining_determinant_width == Fraction(5, 16)
    assert ledger.remaining_residual_product == Fraction(21, 16)
    assert ledger.formal_high_region_fraction == Fraction(17, 64)
    assert ledger.formal_two_sided_region_fraction == Fraction(223, 3072)


def test_residual_cross_is_color_determinant_times_row_cross() -> None:
    ledger = residual_cross_ledger(
        a=(101, 107, 113),
        A=(103, 109, 127),
        first_column=(131, 137),
        second_column=(139, 149),
    )
    assert ledger.column_determinant == 131 * 149 - 139 * 137
    assert ledger.defect == (0, 0, 0)


def test_two_point_residual_lines_force_area_over_covolume() -> None:
    ledger = two_point_residual_line_bound(
        lattice_determinant=101,
        first_width=40,
        second_width=60,
    )
    # ceil(sqrt(ceil(2400/101)))=5.
    assert ledger.parallel_coset_bound == 21
    assert ledger.point_bound == 2 * ledger.parallel_coset_bound


def test_two_sided_residual_bilinear_level_identity() -> None:
    ledger = two_sided_residual_ledger(
        colors=(101, 103, 107, 109),
        completion=(113, 127, 131, 137),
    )
    assert ledger.color_determinant == 101 * 109 - 103 * 107
    assert ledger.bilinear_defect == 0


def test_critical_two_sided_balanced_box_is_forced_to_determinant_scale() -> None:
    ledger = two_sided_critical_ledger(Fraction(11, 16), Fraction(5, 16))
    assert ledger.row_product_required == Fraction(21, 16)
    assert ledger.carrier_product_required == Fraction(21, 16)
    assert ledger.cross_product_required == Fraction(11, 8)
    assert ledger.fully_balanced_side_required == Fraction(11, 16)


def test_bilinear_level_has_arbitrarily_large_line_sparse_matchings() -> None:
    rows = []
    carriers = []
    for parameter in range(1, 9):
        row, carrier = bilinear_parabola_matching(parameter)
        rows.append(row)
        carriers.append(carrier)
        assert row[0] * carrier[0] + row[1] * carrier[1] == 1

    def determinant(first, second, third):
        return (
            (second[0] - first[0]) * (third[1] - first[1])
            - (second[1] - first[1]) * (third[0] - first[0])
        )

    from itertools import combinations

    assert all(determinant(*triple) != 0 for triple in combinations(rows, 3))
    assert all(
        determinant(*triple) != 0 for triple in combinations(carriers, 3)
    )


def test_affine_tangent_packet_reciprocal_height_is_quadratic_polylog() -> None:
    import math

    order = 9
    ledger = tangent_triple_height_ledger(order)
    brute = Fraction(0)
    for first in range(order):
        for second in range(first + 1, order):
            for third in range(second + 1, order):
                left_gap = second - first
                right_gap = third - second
                height = (third - first) // math.gcd(left_gap, right_gap)
                brute += Fraction(1, height)
    assert ledger.triples == 84
    assert ledger.reciprocal_height_sum == brute
    assert ledger.reciprocal_height_sum <= ledger.divisor_majorant
