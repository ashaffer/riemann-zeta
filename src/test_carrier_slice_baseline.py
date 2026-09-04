import unittest

import numpy as np

from carrier_slice_support import carrier_slice_support


class CarrierSliceAlignedBaselineTest(unittest.TestCase):
    def setUp(self) -> None:
        self.kappa = 3.0
        self.carrier = np.diag([self.kappa, 0.0, 0.0])
        self.arithmetic = np.array(
            [
                [-0.2, 0.3 + 0.1j, -0.1j],
                [0.3 - 0.1j, 0.4, -0.2],
                [0.1j, -0.2, -0.5],
            ],
            dtype=complex,
        )

    def test_baseline_sandwich(self) -> None:
        remainder = self.arithmetic + self.carrier
        for theta in (0.0, 0.2, 0.6, 0.9):
            eta = theta * self.kappa
            q_eta = carrier_slice_support(
                self.arithmetic, self.carrier, eta
            ).value
            h_eta = carrier_slice_support(
                remainder, self.carrier, eta
            ).value
            self.assertGreaterEqual(h_eta + 1e-9, q_eta + eta)
            self.assertLessEqual(h_eta - 1e-9, q_eta + self.kappa)

    def test_full_carrier_collapses_to_one_scalar(self) -> None:
        remainder = self.arithmetic + self.carrier
        h_top = carrier_slice_support(
            remainder, self.carrier, self.kappa
        ).value
        expected = self.kappa + self.arithmetic[0, 0].real
        self.assertAlmostEqual(h_top, expected, places=12)

    def test_small_arithmetic_operator_forces_subfull_gate_to_pass(self) -> None:
        epsilon = 0.05
        direction = self.arithmetic / np.linalg.norm(self.arithmetic, ord=2)
        arithmetic = epsilon * self.kappa * direction
        remainder = self.carrier + arithmetic
        theta = 0.8
        support = carrier_slice_support(
            remainder, self.carrier, theta * self.kappa
        ).value
        self.assertGreater(support, theta * self.kappa)
        self.assertGreaterEqual(
            support + 1e-9, (1.0 - epsilon) * self.kappa
        )


if __name__ == "__main__":
    unittest.main()
