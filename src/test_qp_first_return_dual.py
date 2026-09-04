#!/usr/bin/env python3

import math
import unittest

import numpy as np

from qp_first_return_dual import (
    UNIFORM_KILL_EXPONENT,
    carrier_loss_exponent,
    cosine_atoms,
    exponent_ledger,
    finite_bohr_average,
    projected_gram_correction,
    projection_leverage,
    remote_incommensurate_fixture,
)


class QPFirstReturnDualTests(unittest.TestCase):
    def test_min_max_polarity(self) -> None:
        ledger = exponent_ledger()
        self.assertAlmostEqual(ledger.kappa_min, 0.018030323424358778, places=14)
        self.assertAlmostEqual(ledger.kappa_max, 0.018746369714728765, places=14)
        self.assertLess(ledger.kappa_min, ledger.kappa_max)
        self.assertGreater(float(UNIFORM_KILL_EXPONENT), ledger.kappa_max)
        self.assertGreater(ledger.proposed_margin_over_kappa_max, 0.0)

    def test_recalibrated_auxiliary_margins(self) -> None:
        ledger = exponent_ledger()
        self.assertEqual(ledger.long_gap_margin, "1/6500")
        self.assertEqual(ledger.short_collar_margin, "7/8250")
        self.assertEqual(ledger.inverse_image_margin, "2357/33000")
        self.assertLess(ledger.ap_shadow_relative_exponent_at_kappa_min, -0.47)

    def test_point_019_is_fixed_d_only(self) -> None:
        self.assertLess(0.019, carrier_loss_exponent(0.5, 0.665))
        self.assertAlmostEqual(
            carrier_loss_exponent(0.5, 2.0 / 3.0),
            0.020075148161991937,
            places=14,
        )

    def test_carrier_loss_is_increasing_on_candidate_band(self) -> None:
        values = [carrier_loss_exponent(alpha) for alpha in np.linspace(0.49, 0.5, 21)]
        self.assertTrue(all(right > left for left, right in zip(values, values[1:])))

    def test_projected_gram_correction_is_exact_and_carrier_null(self) -> None:
        nodes = np.asarray([0.11, 0.17, 0.23, 0.31])
        centers = cosine_atoms(nodes, [17.0, 31.0])
        base = -np.ones(len(nodes)) / len(nodes)
        certificate = projected_gram_correction(base, centers, [0.03, -0.02])
        self.assertLess(certificate.maximum_center_residual, 1e-12)
        self.assertLess(abs(certificate.carrier_change), 1e-12)
        self.assertGreater(certificate.gram_smallest_eigenvalue, 0.0)
        query = cosine_atoms(nodes, [17.0, 23.0, 31.0])
        leverage = projection_leverage(centers, query)
        self.assertAlmostEqual(float(leverage[0]), 1.0, places=11)
        self.assertAlmostEqual(float(leverage[-1]), 1.0, places=11)
        self.assertGreaterEqual(float(leverage[1]), 0.0)

    def test_remote_incommensurate_chamber_survives(self) -> None:
        fixture = remote_incommensurate_fixture()
        self.assertGreater(fixture.minimum_weight, 0.0)
        self.assertGreater(fixture.perturbed_depth, 0.49)
        self.assertLess(fixture.interpolation_residual, 1e-12)
        self.assertGreater(fixture.first_frequency, 100.0)
        self.assertGreater(abs(fixture.augmented_determinant), 1e-8)

    def test_nonzero_frequency_dual_has_zero_cesaro_mean(self) -> None:
        coefficients = [0.4, -0.1, 0.7]
        nodes = [0.11, 0.19, 0.31]
        self.assertTrue(math.isclose(sum(coefficients), 1.0))
        self.assertLess(abs(finite_bohr_average(coefficients, nodes, 1e8)), 1e-7)


if __name__ == "__main__":
    unittest.main()
