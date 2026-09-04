from fractions import Fraction
import math
import unittest

import numpy as np

from centered_even_cosine_gate import (
    certified_herglotz_counterexample,
    jensen_zero_count_bound,
    sinh_tent_autocorrelation,
    sinh_tent_prime_correlation,
)


class CenteredEvenCosineGateTests(unittest.TestCase):
    def test_sinh_tent_autocorrelation_matches_quadrature(self) -> None:
        length = 5.0
        alpha = 0.37
        for shift in (0.0, 0.2, 1.7, 4.8):
            grid = np.linspace(-length / 2, length / 2 - shift, 200001)
            values = np.sinh(alpha * grid) * np.sinh(alpha * (grid + shift))
            numerical = float(np.trapz(values, grid))
            exact = float(sinh_tent_autocorrelation(length, alpha, shift))
            self.assertAlmostEqual(numerical, exact, places=9)

    def test_two_abscissa_collapse(self) -> None:
        direct, collapsed = sinh_tent_prime_correlation(257, 311.125, 0.37)
        self.assertAlmostEqual(direct, collapsed, places=11)

    def test_jensen_bound_is_linear_in_type_and_radius(self) -> None:
        first = jensen_zero_count_bound(2.0, 7.0)
        second = jensen_zero_count_bound(4.0, 7.0)
        self.assertAlmostEqual(second, 2.0 * first)

    def test_rigorous_evenized_herglotz_counterexample(self) -> None:
        try:
            enclosure = certified_herglotz_counterexample(60)
        except RuntimeError:
            self.skipTest("python-flint is unavailable")
        self.assertLess(enclosure.upper(), 0)
        self.assertLess(float(enclosure.upper()), -0.52)


if __name__ == "__main__":
    unittest.main()
