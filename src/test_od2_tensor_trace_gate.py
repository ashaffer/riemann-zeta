#!/usr/bin/env python3

import unittest
from fractions import Fraction

from od2_tensor_trace_gate import (
    EDGE_EXPONENT,
    H_MAX,
    H_MIN,
    SELECTOR_BETA,
    SELECTOR_CAP,
    TRUNCATED_CUBE_SAVING,
    endpoint_trapezoid,
    low_slope_exponent,
    low_slope_monomial_identity,
    nested_affine_difference,
    paired_empty_jordan_certificate,
    paired_word_state,
    partition_mesh,
    rational_grouping_loss,
    selector_wedge,
    trapezoid_error_envelope,
)


class OD2TensorTraceGateTests(unittest.TestCase):
    def test_paired_empty_word_has_quadratic_trace(self) -> None:
        for length in (1, 2, 7, 31):
            certificate = paired_empty_jordan_certificate(length)
            self.assertEqual(certificate["state"], (1, length, length, length**2))
            self.assertEqual(certificate["state"], certificate["expected_state"])

    def test_paired_empty_transition_has_jordan_length_three(self) -> None:
        certificate = paired_empty_jordan_certificate(5)
        self.assertTrue(certificate["nilpotent_square_nonzero"])
        self.assertTrue(certificate["nilpotent_cube_zero"])

    def test_paired_first_returns_multiply(self) -> None:
        # First survivors occur at positions three and two.
        state = paired_word_state([0, 0, 1, 0], [0, 1, 0, 0])
        self.assertEqual(state[3], 6)

    def test_endpoint_trapezoid_is_affine_exact(self) -> None:
        points = [Fraction(1), Fraction(7, 2), Fraction(9), Fraction(14)]
        self.assertAlmostEqual(endpoint_trapezoid(points, lambda _x: 1).real, 13)
        self.assertAlmostEqual(
            endpoint_trapezoid(points, lambda x: complex(x)).real,
            (14**2 - 1) / 2,
        )

    def test_nested_difference_annihilates_affine_functions(self) -> None:
        constant, linear = nested_affine_difference(
            [0, 4, 9, 15], [0, 1, 4, 6, 9, 12, 15]
        )
        self.assertEqual(constant, 0)
        self.assertEqual(linear, 0)

    def test_quadratic_saturates_trapezoid_error_constant(self) -> None:
        points = [0, 3]
        trapezoid = endpoint_trapezoid(points, lambda x: complex(x * x)).real
        integral = Fraction(3**3, 3)
        error = trapezoid - float(integral)
        self.assertAlmostEqual(error, float(trapezoid_error_envelope(points, 2)))
        self.assertEqual(partition_mesh(points), 3)

    def test_low_slope_threshold_closes_at_YG(self) -> None:
        identity = low_slope_monomial_identity()
        self.assertEqual(identity["eta_fourth"], "Y^d H^-1 G^-3")
        self.assertEqual(identity["global_cube_ledger"], "Y G^2 Y^-d")
        self.assertEqual(identity["aggregate_with_Y"], "Y*G")

    def test_selector_wedge_exact_boundaries(self) -> None:
        wedge = selector_wedge()
        self.assertEqual(wedge["eta_at_h_min"], Fraction(150703, 858000))
        self.assertEqual(wedge["eta_at_h_max"], Fraction(135181, 520000))
        self.assertGreater(low_slope_exponent(H_MIN), SELECTOR_BETA)
        self.assertFalse(wedge["wedge_reaches_h_max"])
        self.assertEqual(
            wedge["largest_h_with_nonempty_capped_wedge"],
            4 * SELECTOR_CAP
            - 3 * EDGE_EXPONENT
            + TRUNCATED_CUBE_SAVING,
        )
        self.assertEqual(
            wedge["largest_h_with_nonempty_capped_wedge"],
            Fraction(460197, 864500),
        )
        self.assertLess(H_MIN, wedge["largest_h_with_nonempty_capped_wedge"])
        self.assertLess(wedge["largest_h_with_nonempty_capped_wedge"], H_MAX)

    def test_rational_grouping_q_loss_cancels_with_occupancy(self) -> None:
        result = rational_grouping_loss(101, 17, 23)
        self.assertEqual(result["q_factor"], 17)
        self.assertEqual(result["max_occupancy"], 6)
        self.assertEqual(result["envelope"], 17 * 6 * 23)
        self.assertLessEqual(result["envelope"], result["two_h_diagonal"])


if __name__ == "__main__":
    unittest.main()
