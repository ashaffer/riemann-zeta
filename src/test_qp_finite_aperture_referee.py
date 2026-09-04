#!/usr/bin/env python3

import math
import unittest

from qp_finite_aperture_referee import (
    KAPPA_PROMOTE,
    TENT_NEGATIVE_THRESHOLD_FACTOR,
    antipode_from_spectral_null,
    rational_margin_ledger,
    spectral_null_from_antipode,
    tent_failure_log_bound,
    tent_population,
    tent_population_by_antiderivative,
)


class QPFiniteApertureRefereeTests(unittest.TestCase):
    def test_tent_transform_two_closed_forms_agree_and_are_nonnegative(self) -> None:
        for width in (0.2, 0.7, 2.0):
            for t in (0.0, 1e-7, 0.3, 2.0, 17.0, 100.0):
                direct = tent_population_by_antiderivative(t, width)
                sinc_square = tent_population(t, width)
                self.assertTrue(math.isclose(direct, sinc_square, rel_tol=2e-9, abs_tol=2e-12))
                self.assertGreaterEqual(sinc_square, 0.0)

    def test_exact_continuum_probability_constant(self) -> None:
        epsilon = 0.1
        expected = (
            math.log(2.0)
            + math.log(2.0 + 4.0 * 0.2 * 100.0 / epsilon)
            - 50_000 * epsilon * epsilon / 8.0
        )
        self.assertAlmostEqual(
            tent_failure_log_bound(50_000, 0.2, 100.0, epsilon), expected, places=14
        )
        self.assertEqual(str(TENT_NEGATIVE_THRESHOLD_FACTOR), "8/3")

    def test_metric_exponent_is_the_claimed_power(self) -> None:
        self.assertAlmostEqual(1.0 - 2.0 * KAPPA_PROMOTE, 0.9639393531512824, places=14)

    def test_spectral_null_conversion_is_exact(self) -> None:
        for depth in (0.0, 1e-4, 0.037, 0.5):
            alpha, transformed = spectral_null_from_antipode(depth, [-depth] * 7)
            self.assertLess(max(abs(value) for value in transformed), 1e-15)
            self.assertAlmostEqual(antipode_from_spectral_null(alpha), depth, places=14)
            self.assertAlmostEqual(alpha, depth / (1.0 + depth), places=14)

    def test_exact_rational_margins(self) -> None:
        ledger = rational_margin_ledger()
        self.assertEqual(ledger.long_gap_saving, "249/13000")
        self.assertEqual(ledger.collar_saving, "131/6600")
        self.assertEqual(ledger.inverse_image_saving, "373/4125")
        self.assertEqual(ledger.long_gap_margin, "1/6500")
        self.assertEqual(ledger.collar_margin, "7/8250")
        self.assertEqual(ledger.inverse_image_margin, "2357/33000")
        self.assertTrue(ledger.target_clears_uniform_kappa)


if __name__ == "__main__":
    unittest.main()
