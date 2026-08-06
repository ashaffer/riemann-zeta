import math
import unittest

import numpy as np

from fixed_box_width_spectrometer import (
    arithmetic_cross,
    main_coefficient,
    prime_triangle_sum,
    ramp,
    triangle,
)
from signed_garding_failfast import prime_powers


class FixedBoxWidthSpectrometerTest(unittest.TestCase):
    def test_triangle(self):
        values = triangle(np.asarray([-2.0, -0.5, 0.0, 0.5, 2.0]), 1.0)
        np.testing.assert_allclose(values, [0.0, 0.5, 1.0, 0.5, 0.0])

    def test_triangle_is_ramp_coboundary(self):
        values = np.linspace(-3.0, 3.0, 25)
        length = 0.7
        np.testing.assert_allclose(
            triangle(values, length),
            ramp(values + length, length) - ramp(values, length),
        )

    def test_normalized_triangle_refinement(self):
        values = np.linspace(-4.0, 4.0, 41)
        half_length = 0.8
        coarse = triangle(values, 2 * half_length) / (2 * half_length)
        fine = (
            0.25 * triangle(values - half_length, half_length)
            + 0.5 * triangle(values, half_length)
            + 0.25 * triangle(values + half_length, half_length)
        ) / half_length
        np.testing.assert_allclose(coarse, fine, atol=2e-15)

    def test_pole_coefficient_forms_agree(self):
        for length in (0.25, 1.0, 2.5):
            expected = 8 * (math.cosh(length / 2) - 1) / length
            self.assertAlmostEqual(main_coefficient(length), expected, places=14)

    def test_prime_sum_uses_one_polarized_copy(self):
        logs, weights = prime_powers(100)
        length = 0.1
        separation = math.log(2)
        value = prime_triangle_sum(length, separation, logs, weights)
        self.assertAlmostEqual(value, math.log(2) / math.sqrt(2), places=14)

    def test_arithmetic_normalization_anchor(self):
        values = arithmetic_cross(1.0, 4.0)
        self.assertAlmostEqual(values["coefficient"], 1.021007721651046, places=14)
        self.assertAlmostEqual(values["cross"], 0.01479877736638, places=12)


if __name__ == "__main__":
    unittest.main()
