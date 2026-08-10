import math
import unittest

from high_order_mollifier_shift import (
    carrier_rate,
    fixed_divisor_convergence,
    logarithmic_cutoff_weight,
    minimum_carrier_rate_on_interval,
    proportional_order,
    proportional_weight,
    scaled_entropy_rate,
    shifted_reciprocal_weight,
    terminal_power_exponent,
    verify_weight_domination,
)


class ProportionalOrderTests(unittest.TestCase):
    def test_order_ledger(self) -> None:
        scale = math.exp(20.0)
        ledger = proportional_order(scale, 0.2)
        self.assertEqual(ledger.order, 4)
        self.assertAlmostEqual(ledger.order_over_log_scale, 0.2)
        self.assertAlmostEqual(ledger.shifted_real_part, 0.7)

    def test_weight_domination_grid(self) -> None:
        excess = verify_weight_domination(
            scales=(10.0, 1.0e3, 1.0e6, 1.0e12),
            alphas=(0.02, 0.1, 0.25, 0.49),
            divisor_cap=500,
        )
        self.assertLessEqual(excess, 2.0e-14)

    def test_fixed_divisor_limit(self) -> None:
        scales = tuple(math.exp(value) for value in (20.0, 50.0, 100.0, 200.0))
        errors = fixed_divisor_convergence(2, 0.2, scales)
        self.assertLess(errors[-1], errors[0])
        self.assertLess(errors[-1], 5.0e-4)
        target = shifted_reciprocal_weight(2, 0.2)
        self.assertAlmostEqual(
            proportional_weight(scales[-1], 2, 0.2), target, delta=5.0e-4
        )

    def test_cutoff_endpoint_and_sharp_order_zero(self) -> None:
        self.assertEqual(logarithmic_cutoff_weight(10.0, 11, 3), 0.0)
        self.assertEqual(logarithmic_cutoff_weight(10.0, 10, 3), 0.0)
        self.assertEqual(logarithmic_cutoff_weight(10.0, 10, 0), 1.0)
        self.assertEqual(logarithmic_cutoff_weight(10.0, 1, 8), 1.0)


class CarrierRateTests(unittest.TestCase):
    def test_entropy_identity_and_nonnegativity(self) -> None:
        for alpha in (0.02, 0.1, 0.25, 0.49):
            for displacement in (0.005, 0.02, 0.07, 0.1, 0.25, 0.49):
                direct = carrier_rate(alpha, displacement)
                stable = scaled_entropy_rate(alpha, displacement)
                self.assertAlmostEqual(direct, stable, places=14)
                self.assertGreaterEqual(direct, -2.0e-15)

    def test_unique_zero(self) -> None:
        for alpha in (0.02, 0.1, 0.25, 0.49):
            self.assertAlmostEqual(carrier_rate(alpha, alpha), 0.0, places=15)
            self.assertGreater(carrier_rate(alpha, alpha / 2.0), 0.0)
            self.assertGreater(carrier_rate(alpha, min(0.5, 2.0 * alpha)), -1.0e-15)

    def test_interval_minimum(self) -> None:
        rate, minimizer = minimum_carrier_rate_on_interval(0.1, 0.02, 0.5)
        self.assertAlmostEqual(minimizer, 0.1)
        self.assertAlmostEqual(rate, 0.0, places=15)

        rate, minimizer = minimum_carrier_rate_on_interval(0.01, 0.05, 0.5)
        self.assertAlmostEqual(minimizer, 0.05)
        self.assertGreater(rate, 0.0)

        rate, minimizer = minimum_carrier_rate_on_interval(0.8, 0.05, 0.5)
        self.assertAlmostEqual(minimizer, 0.5)
        self.assertGreater(rate, 0.0)

    def test_terminal_power_exponent(self) -> None:
        self.assertEqual(terminal_power_exponent(0.2, 0.0), 0.0)
        self.assertAlmostEqual(
            terminal_power_exponent(0.2, 0.5), 0.2 * math.log(0.5)
        )
        self.assertLess(terminal_power_exponent(0.2, 0.9), 0.0)


class ValidationTests(unittest.TestCase):
    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            proportional_order(1.0, 0.1)
        with self.assertRaises(ValueError):
            proportional_order(10.0, 0.0)
        with self.assertRaises(ValueError):
            logarithmic_cutoff_weight(10.0, 0, 1)
        with self.assertRaises(ValueError):
            logarithmic_cutoff_weight(10.0, 2, -1)
        with self.assertRaises(ValueError):
            carrier_rate(0.0, 0.1)
        with self.assertRaises(ValueError):
            carrier_rate(0.1, 0.0)
        with self.assertRaises(ValueError):
            minimum_carrier_rate_on_interval(0.1, 0.2, 0.1)
        with self.assertRaises(ValueError):
            terminal_power_exponent(0.1, 1.0)
        with self.assertRaises(ValueError):
            fixed_divisor_convergence(2, 0.1, (1.5,))


if __name__ == "__main__":
    unittest.main()
