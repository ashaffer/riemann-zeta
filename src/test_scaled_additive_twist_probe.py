#!/usr/bin/env python3

import unittest

from fixed_step_spectral_cooling_probe import coboundary_multiplier
from scaled_additive_twist_probe import (
    finite_scaled_additive_multiplier,
    scaled_additive_limit,
)


class ScaledAdditiveTwistProbeTests(unittest.TestCase):
    def test_zero_frequency_recovers_coboundary_multiplier(self) -> None:
        s = complex(0.2, 0.7)
        finite = finite_scaled_additive_multiplier(s, 0.2, 4, 0.0)
        exact = coboundary_multiplier(s, 0.2, 4)
        self.assertLess(abs(finite - exact), 2.0e-9)

    def test_limit_has_the_expected_conjugation_symmetry(self) -> None:
        s = complex(0.2, 0.7)
        positive = scaled_additive_limit(s, 0.3)
        reflected = scaled_additive_limit(s.conjugate(), -0.3)
        self.assertAlmostEqual(abs(reflected - positive.conjugate()), 0.0, places=12)
        self.assertGreater(abs(positive), 0.0)

    def test_finite_multiplier_moves_toward_gamma_limit(self) -> None:
        s = complex(0.2, 0.7)
        xi = 0.3
        limiting = scaled_additive_limit(s, xi)
        low = finite_scaled_additive_multiplier(s, 0.2, 4, xi)
        high = finite_scaled_additive_multiplier(s, 0.2, 40, xi)
        self.assertLess(abs(high - limiting), abs(low - limiting))


if __name__ == "__main__":
    unittest.main()
