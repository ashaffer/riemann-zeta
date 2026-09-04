from fractions import Fraction

import pytest

from qp_full_strip_local_packet_gate import (
    full_strip_local_ledger,
    integer_three_point_determinant,
    interval_additive_energy,
    line_packet_cardinality_bound,
    line_product_second_difference,
    line_product_value,
    local_determinant_upper_bound,
    local_strip_forces_collinearity,
    reciprocal_third_difference,
    reciprocal_three_point_determinant,
)


def test_critical_full_strip_local_exponents() -> None:
    ledger = full_strip_local_ledger()
    assert ledger.local_arc == Fraction(11, 16)
    assert ledger.local_rounding_error == Fraction(-3, 8)
    assert ledger.packet_cardinality == Fraction(1, 2)
    assert ledger.three_ap_lower_edge == Fraction(1, 2)
    assert ledger.three_ap_upper_edge == Fraction(33, 32)
    assert ledger.four_ap_lower_edge == Fraction(49, 48)
    assert ledger.four_ap_upper_edge == Fraction(11, 8)
    assert ledger.macroscopic_ap_step == Fraction(17, 16)
    assert ledger.macroscopic_to_four_ap_lower_margin == Fraction(1, 24)
    assert ledger.four_ap_upper_to_macroscopic_margin == Fraction(5, 16)
    assert ledger.behrend_spacing_over_local_arc == Fraction(3, 8)
    assert ledger.macroscopic_ap_hs_smooth_term == Fraction(129, 160)
    assert ledger.macroscopic_ap_hs_tolerance_term == Fraction(79, 96)
    assert ledger.macroscopic_ap_hs_major_term == Fraction(7, 32)
    assert ledger.macroscopic_ap_to_energy_core_margin == Fraction(1, 96)


def test_reciprocal_three_point_determinant_factorization() -> None:
    value = reciprocal_three_point_determinant(Fraction(10_000), (98, 100, 102))
    expected = Fraction(10_000 * 2 * 4 * 2, 98 * 100 * 102)
    assert value == expected


def test_local_tangent_points_are_certifiably_collinear() -> None:
    # These lie on v=200-a and have products 9996, 10000, 9996.
    points = ((98, 102), (100, 100), (102, 98))
    assert local_determinant_upper_bound(Fraction(10_000), Fraction(4), (98, 100, 102)) < 1
    assert local_strip_forces_collinearity(Fraction(10_000), Fraction(4), points)
    assert integer_three_point_determinant(points) == 0


def test_local_certificate_refuses_a_wide_arc() -> None:
    points = ((90, 111), (100, 100), (110, 91))
    assert not local_strip_forces_collinearity(
        Fraction(10_000), Fraction(10), points
    )


def test_reciprocal_third_difference_factorization() -> None:
    value = reciprocal_third_difference(Fraction(17_000), 100, 3)
    expected = Fraction(-6 * 17_000 * 27, 100 * 103 * 106 * 109)
    assert value == expected


def test_product_is_quadratic_along_an_affine_packet() -> None:
    values = [line_product_value((100, 100), (1, 1), k) for k in range(-5, 6)]
    assert all(
        values[index + 2] - 2 * values[index + 1] + values[index] == -2
        for index in range(len(values) - 2)
    )
    assert line_product_second_difference((7, 5)) == -70


def test_packet_cardinality_bound_on_enumerated_quadratics() -> None:
    for radius in range(1, 20):
        for horizontal_step in range(1, 8):
            for downward_step in range(1, 8):
                bound = line_packet_cardinality_bound(
                    Fraction(radius), horizontal_step, downward_step
                )
                for linear_term in range(-20, 21):
                    values = [
                        k
                        for k in range(-100, 101)
                        if abs(
                            -horizontal_step * downward_step * k * k
                            + linear_term * k
                        )
                        <= radius
                    ]
                    assert len(values) <= bound


def test_projection_can_restore_cubic_interval_energy() -> None:
    assert interval_additive_energy(1) == 1
    assert interval_additive_energy(4) == 44
    with pytest.raises(ValueError, match="positive"):
        interval_additive_energy(0)
