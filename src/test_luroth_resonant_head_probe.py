#!/usr/bin/env python3

import math
import unittest

from luroth_resonant_head_probe import (
    alias_response,
    closed_head,
    direct_head,
    exact_tail,
    linear_tail_symbol,
    scaled_alias_sample,
    stationary_block,
    stationary_prediction,
)


class LurothResonantHeadProbeTests(unittest.TestCase):
    def test_finite_head_collapses_exactly(self) -> None:
        for cutoff in (1, 7, 53):
            for s in (0.8 + 3.0j, 1.2 + 11.0j, 2.3 + 0.4j):
                self.assertLess(abs(direct_head(cutoff, s) - closed_head(cutoff, s)), 2e-14)

    def test_head_plus_hurwitz_tail_is_closed_carrier(self) -> None:
        import mpmath as mp

        s = 0.83 + 17.0j
        carrier = complex((s - 1) * mp.zeta(s) / (s * (s + 1)))
        self.assertLess(abs(closed_head(80, s) + exact_tail(80, s) - carrier), 2e-13)

    def test_linear_cutoff_symbol(self) -> None:
        sigma = 0.9
        height = 1000.0
        s = complex(sigma, height)
        a = round(2 * height)
        observed = a ** (s + 1) * exact_tail(a - 1, s)
        predicted = linear_tail_symbol(1j * height / a)
        self.assertLess(abs(observed - predicted), 1.1e-3)

    def test_single_alias_response(self) -> None:
        observed = scaled_alias_sample(k=2, sigma=0.9, height=100_000.0)
        self.assertLess(abs(observed - alias_response(2)), 2.0e-5)

    def test_stationary_window_prediction(self) -> None:
        s = 0.9 + 100_000.0j
        observed = stationary_block(k=2, s=s, c=0.12)
        predicted = stationary_prediction(k=2, s=s, c=0.12)
        self.assertLess(abs(observed - predicted) / abs(predicted), 5.0e-3)

    def test_symbol_has_no_imaginary_zero_before_first_alias(self) -> None:
        for numerator in range(1, 100):
            v = 2 * math.pi * numerator / 100
            self.assertGreater(abs(linear_tail_symbol(1j * v)), 1e-3)


if __name__ == "__main__":
    unittest.main()
