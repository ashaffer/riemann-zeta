#!/usr/bin/env python3

import math
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from qp_remote_ap_gate import (
    KAPPA_PROMOTE,
    ap_shadow_exponents,
    ap_weights,
    dilation_shadow_measure_bound,
    effective_cosine_nodes,
    harmonic_number,
    interpolation_residual,
    nodal_polynomial_residual,
    positive_antipode_depth,
    required_peak,
)


class QPRemoteAPGateTests(unittest.TestCase):
    def test_exact_ap_interpolation(self) -> None:
        nodes = np.asarray([0.031, 0.083, 0.147, 0.191])
        tau = 17.25
        self.assertLess(interpolation_residual(nodes, tau), 2e-12)
        self.assertLess(nodal_polynomial_residual(nodes, tau), 2e-13)

    def test_one_node_positive_antipode_conversion(self) -> None:
        nodes = np.asarray([2.0 * math.pi / 3.0])
        weights = ap_weights(nodes, 1.0)
        self.assertAlmostEqual(weights[0], -2.0, places=12)
        self.assertAlmostEqual(positive_antipode_depth(weights), 0.5, places=12)
        probability = -0.5 * weights
        self.assertAlmostEqual(float(np.sum(probability)), 1.0, places=12)
        self.assertAlmostEqual(
            float(probability @ np.cos(nodes[:, None]).ravel()), -0.5, places=12
        )

    def test_mixed_sign_weights_do_not_make_positive_antipode(self) -> None:
        self.assertEqual(positive_antipode_depth(np.asarray([-2.0, 0.1])), 0.0)

    def test_effective_absolute_node_quotient(self) -> None:
        nodes = effective_cosine_nodes(np.asarray([-0.2, 0.2, 0.1, -0.1, 0.0]))
        np.testing.assert_allclose(nodes, np.asarray([0.0, 0.1, 0.2]))

    def test_dilation_shadow_jacobian_ledger(self) -> None:
        indices = [1, 2, 4]
        self.assertAlmostEqual(harmonic_number(indices), 1.75)
        self.assertAlmostEqual(
            dilation_shadow_measure_bound(
                packet_count=3.0, packet_radius=0.5, indices=indices
            ),
            5.25,
        )

    def test_promotion_shadow_has_power_zero_density(self) -> None:
        exponents = ap_shadow_exponents()
        self.assertAlmostEqual(exponents["packet_shadow"], 2.0 * KAPPA_PROMOTE)
        self.assertAlmostEqual(exponents["legal_step_interval"], 17.0 / 33.0)
        self.assertAlmostEqual(
            exponents["relative_density"],
            2.0 * KAPPA_PROMOTE - 17.0 / 33.0,
        )
        self.assertLess(exponents["relative_density"], -0.47)

    def test_scalar_peak_polarity(self) -> None:
        self.assertEqual(required_peak(100, 4.0), 25.0)
        with self.assertRaises(ValueError):
            required_peak(100, 0.0)


if __name__ == "__main__":
    unittest.main()
