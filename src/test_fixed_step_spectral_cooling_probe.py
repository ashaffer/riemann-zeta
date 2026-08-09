import cmath
import math
import unittest

from fixed_step_spectral_cooling_probe import (
    FIRST_ZERO_ORDINATE,
    bspline_cdf,
    coboundary_multiplier,
    compact_window,
    critical_coboundary_bound,
    critical_line_contraction,
    direct_von_mangoldt_coboundary,
    off_line_net_log_amplitude,
    primitive_multiplier,
    q_h,
    support_ratio,
)


class FixedStepSpectralCoolingProbeTest(unittest.TestCase):
    def test_exact_multiplier_factorization(self):
        h = 0.1
        k = 7
        s = complex(0.2, FIRST_ZERO_ORDINATE)
        expected = (cmath.exp(k * h * s) - 1.0) * primitive_multiplier(s, h, k)
        self.assertAlmostEqual(
            abs(coboundary_multiplier(s, h, k) - expected), 0.0, places=13
        )
        self.assertAlmostEqual(coboundary_multiplier(0.0, h, k).real, k * h)

    def test_critical_line_multiplier_is_sinc_contraction(self):
        h = 0.1
        k = 32
        gamma = FIRST_ZERO_ORDINATE
        expected = abs(math.sin(h * gamma / 2.0) / (h * gamma / 2.0)) ** k
        self.assertAlmostEqual(critical_line_contraction(h, k, gamma), expected)
        self.assertAlmostEqual(abs(q_h(1j * gamma, h)) ** k, expected)
        self.assertLessEqual(
            abs(coboundary_multiplier(1j * gamma, h, k)),
            critical_coboundary_bound(h, k, gamma) * (1.0 + 1.0e-14),
        )

    def test_sublinear_order_leaves_off_line_exponential_visible(self):
        delta = 0.1
        gamma = FIRST_ZERO_ORDINATE
        h = 0.1
        small_r = 10_000.0
        large_r = 1_000_000.0
        small = off_line_net_log_amplitude(
            delta, gamma, h, math.floor(math.sqrt(small_r)), small_r
        )
        large = off_line_net_log_amplitude(
            delta, gamma, h, math.floor(math.sqrt(large_r)), large_r
        )
        self.assertGreater(small, 0.0)
        self.assertGreater(large, 0.0)
        self.assertLess(abs(large / large_r - delta), abs(small / small_r - delta))

    def test_support_and_compact_window(self):
        self.assertAlmostEqual(support_ratio(0.2, 4), math.exp(0.8))
        h = 0.2
        k = 4
        width = h * k
        self.assertEqual(bspline_cdf(0.0, h, k), 0.0)
        self.assertEqual(bspline_cdf(width, h, k), 1.0)
        self.assertAlmostEqual(bspline_cdf(width / 2.0, h, k), 0.5)
        for value in (-0.7, -0.2, 0.0, 0.2, 0.7):
            self.assertAlmostEqual(
                compact_window(value, h, k), compact_window(-value, h, k)
            )

    def test_direct_von_mangoldt_coboundary(self):
        check = direct_von_mangoldt_coboundary()
        self.assertLess(abs(check.closure_error), 1.0e-13)
        self.assertAlmostEqual(check.difference, check.compact_evaluation, places=13)
        self.assertAlmostEqual(check.difference, 0.001042240238, places=10)


if __name__ == "__main__":
    unittest.main()
