#!/usr/bin/env python3

import math
import unittest

from global_pick_deep_fan_gate import (
    PICK_SURCHARGE,
    centered_binomial_attenuation,
    centered_screen_poisson_load,
    complex_lagrange_rate,
    optimize_centered_screen,
    optimize_four_row_jet_danger,
    pointwise_screen_c_cap,
)


class GlobalPickDeepFanGateTests(unittest.TestCase):
    def test_complex_lagrange_rate_at_zero(self) -> None:
        self.assertAlmostEqual(complex_lagrange_rate(0), -math.log(2))

    def test_pointwise_cap(self) -> None:
        b = 0.47
        c = pointwise_screen_c_cap(b)
        H = math.pi * c / 0.66
        self.assertAlmostEqual(centered_screen_poisson_load(H, b), 0.5)

    def test_screen_formula_is_below_surcharge(self) -> None:
        optimum = optimize_centered_screen()
        self.assertLess(optimum.attenuation, PICK_SURCHARGE)
        self.assertAlmostEqual(
            optimum.attenuation,
            centered_binomial_attenuation(optimum.b, optimum.c),
        )

    def test_conditional_jet_danger_crosses_surcharge(self) -> None:
        danger = optimize_four_row_jet_danger()
        self.assertGreater(danger.exponent, PICK_SURCHARGE)
        self.assertGreater(danger.excess_over_surcharge, 0)


if __name__ == "__main__":
    unittest.main()
