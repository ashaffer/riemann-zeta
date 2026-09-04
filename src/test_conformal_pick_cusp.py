import cmath
import math
import unittest

from conformal_pick_cusp import (
    contour_h,
    cusp_coordinate,
    exponential_taylor_tail,
    half_delay_normalized_margin,
    odd_root_fan_max_depth,
    taylor_degree_for_error,
)


class ConformalPickCuspTests(unittest.TestCase):
    def test_contour_maps_exactly_to_unit_circle_phase(self) -> None:
        d = 0.66
        lambda0 = 1.25
        for x in (-3.0, -1.1, 0.0, 0.8, 2.7):
            w = cusp_coordinate(contour_h(x, d, lambda0), d, lambda0)
            self.assertAlmostEqual(abs(w - cmath.exp(-1j * x)), 0.0, places=12)

    def test_half_delay_is_nonnegative_on_closed_cell(self) -> None:
        values = [
            half_delay_normalized_margin(x, 3.0, 0.66)
            for x in (-math.pi, -1.0, 0.0, 2.0, math.pi)
        ]
        self.assertTrue(all(value >= -1e-14 for value in values))
        self.assertGreater(values[2], 0.0)

    def test_odd_root_fan_depth_formula(self) -> None:
        d = 0.66
        lambda0 = 1.0
        for count in (3, 5, 101):
            x_max = math.pi * (1.0 - 1.0 / count)
            expected = -contour_h(x_max, d, lambda0).real
            self.assertAlmostEqual(
                odd_root_fan_max_depth(count, d, lambda0), expected, places=12
            )

    def test_taylor_degree_meets_requested_bound(self) -> None:
        radius = 12.0
        degree = taylor_degree_for_error(radius, 0.125)
        self.assertLessEqual(exponential_taylor_tail(radius, degree), 0.125)
        self.assertGreater(exponential_taylor_tail(radius, degree - 1), 0.125)


if __name__ == "__main__":
    unittest.main()
