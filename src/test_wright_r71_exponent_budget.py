#!/usr/bin/env python3

import unittest

from wright_r71_exponent_budget import (
    damped_cofactor_tradeoff,
    wright_budget,
)


class WrightR71ExponentBudgetTests(unittest.TestCase):
    def test_zero_slope_limit_is_one_fortieth(self) -> None:
        budget = wright_budget(1.0e-10, 3.0)
        self.assertAlmostEqual(budget.net_saving, 1.0 / 40.0, delta=1.0e-8)

    def test_fixed_denominator_is_a_power_at_fixed_slope(self) -> None:
        budget = wright_budget(0.01, 3.0)
        self.assertAlmostEqual(budget.fixed_denominator_exponent, 0.03)
        self.assertGreater(budget.fixed_denominator_exponent, 0.0)

    def test_small_slope_formula_in_minimal_numerator_regime(self) -> None:
        slope = 0.001
        retreat = 3.0
        budget = wright_budget(slope, retreat)
        expected = 1.0 / 40.0 - 11.0 * retreat * slope / 40.0
        self.assertAlmostEqual(budget.net_saving, expected, places=13)

    def test_upper_window_shell_pays_the_width_exponent(self) -> None:
        slope = 0.001
        retreat = 3.0
        window_step = 0.1
        budget = wright_budget(
            slope,
            retreat,
            product_shell_excess=window_step * slope,
        )
        expected = (
            1.0 / 40.0
            - (11.0 * retreat + 10.0 * window_step) * slope / 40.0
        )
        self.assertAlmostEqual(budget.net_saving, expected, places=13)

    def test_phase_and_mode_losses_consume_the_gain(self) -> None:
        clean = wright_budget(0.001, 3.0)
        long_numerator = wright_budget(
            0.001,
            3.0,
            numerator_length_exponent=0.8,
        )
        phase = wright_budget(
            0.001,
            3.0,
            numerator_length_exponent=0.8,
            phase_integer_exponent=0.3,
        )
        modes = wright_budget(0.001, 3.0, mode_loss=0.02)
        self.assertLess(phase.net_saving, long_numerator.net_saving)
        self.assertAlmostEqual(modes.net_saving, clean.net_saving - 0.02)

    def test_invalid_cutoff_scale_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            wright_budget(0.5, 2.0)

    def test_damped_cofactor_optimum_cannot_repay_shift(self) -> None:
        for epsilon in (0.001, 0.01, 0.1):
            tradeoff = damped_cofactor_tradeoff(epsilon)
            self.assertAlmostEqual(
                tradeoff.tail_saving,
                tradeoff.wright_saving,
                places=14,
            )
            self.assertLess(tradeoff.gross_saving, epsilon)
            self.assertLess(tradeoff.original_zero_strip, 0.0)

    def test_invalid_damping_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            damped_cofactor_tradeoff(0.0)


if __name__ == "__main__":
    unittest.main()
