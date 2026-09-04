import math
import unittest

import numpy as np

from carrier_slice_support import (
    carrier_slice_support,
    collateral_demo,
    collateral_support_closed_form,
    mirror_demo,
)


class CarrierSliceSupportTest(unittest.TestCase):
    def test_exact_mirror_slice_is_one_dimensional(self) -> None:
        result = mirror_demo()
        self.assertAlmostEqual(result["h_eta_diagonal_remainder"], 1.0)
        self.assertAlmostEqual(
            result["h_over_cross_bill"],
            1.0 / result["C_cosh_alpha_D"],
        )

    def test_collateral_dual_matches_closed_form(self) -> None:
        k0, k1 = 1.3, 0.8
        remainder = k1 * np.array(
            [[-1.0, -1.0 / math.sqrt(2.0)],
             [-1.0 / math.sqrt(2.0), 0.0]]
        )
        carrier = np.diag([2.0 * k0, 0.0])
        for fraction in (0.0, 0.1, 0.3, 0.5, 0.75, 0.95, 1.0):
            eta = 2.0 * k0 * fraction
            numerical = carrier_slice_support(remainder, carrier, eta).value
            analytic = collateral_support_closed_form(k0, k1, eta)
            self.assertAlmostEqual(numerical, analytic, places=9)

    def test_equal_scale_collateral_state_reproduces_two_over_eleven(self) -> None:
        result = collateral_demo(1.0, 1.0)
        self.assertAlmostEqual(result["x_cancel_q_mass"], 2.0 / 11.0)
        self.assertAlmostEqual(result["eta_cancel"], 4.0 / 11.0)
        self.assertAlmostEqual(result["aggregate_expectation"], 0.0, places=12)
        self.assertAlmostEqual(
            result["complete_selected_pair_expectation"], -4.0 / 11.0
        )
        self.assertAlmostEqual(
            result["complete_collateral_pair_expectation"], -4.0 / 11.0
        )
        self.assertGreater(result["h_eta_cancel_dual"], result["eta_cancel"])

    def test_carrier_slice_can_make_positive_part_useless(self) -> None:
        result = collateral_demo(1.0, 1.0)
        self.assertGreater(result["positive_part_norm_R"], 0.0)
        self.assertLess(result["h_at_three_quarter_carrier"], 0.0)

    def test_empty_slice_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            carrier_slice_support(np.eye(2), np.diag([1.0, 0.0]), 1.01)


if __name__ == "__main__":
    unittest.main()
