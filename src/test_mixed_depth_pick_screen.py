#!/usr/bin/env python3

import math
import unittest

from mixed_depth_pick_screen import (
    DENSITY,
    PICK_SURCHARGE,
    affine_screen_attenuation,
    affine_screen_max_poisson_load,
    affine_screen_poisson_load_at,
    complex_lagrange_rate_at,
    cyclotomic_three_interpolation_log_cost,
    fixed_color_separation_upper_bound,
    microscopic_cluster_poisson_ceiling,
    optimize_affine_screen,
    segment_geometry,
)


class MixedDepthPickScreenTests(unittest.TestCase):
    def test_complex_lagrange_primitive(self) -> None:
        y = 0.47
        expected = 0.5 * math.log(0.25 + y * y) + 2 * y * math.atan(
            1 / (2 * y)
        )
        self.assertAlmostEqual(
            complex_lagrange_rate_at(0.5 + 1j * y), expected, places=12
        )

    def test_centered_geometry(self) -> None:
        b, H = 0.47, 0.04
        radius, target, left, right = segment_geometry(b, H, 0.0)
        self.assertAlmostEqual(left, b)
        self.assertAlmostEqual(right, b)
        self.assertAlmostEqual(radius, math.hypot(0.49 - b, H / 2))
        self.assertAlmostEqual(target.real, 0.5)
        self.assertAlmostEqual(target.imag, (0.49 - b) / H)

    def test_reflection_symmetry(self) -> None:
        args = (0.43, 0.08)
        left = affine_screen_attenuation(
            *args, 0.35, ordinate_center=0.025
        )
        right = affine_screen_attenuation(
            *args, -0.35, ordinate_center=-0.025
        )
        self.assertAlmostEqual(left, right, places=12)

    def test_equal_depth_poisson_formula(self) -> None:
        b, H = 0.46, 0.031
        expected = (4 * DENSITY / math.pi) * (
            math.atan(H / (2 * (0.5 - b)))
            + math.atan(H / (2 * (0.5 + b)))
        )
        self.assertAlmostEqual(
            affine_screen_poisson_load_at(0.0, b, H, 0.0),
            expected,
            places=10,
        )
        load, peak = affine_screen_max_poisson_load(b, H, 0.0)
        self.assertAlmostEqual(load, expected, places=9)
        self.assertAlmostEqual(peak, 0.0, places=7)

    def test_mixed_depth_search_does_not_cross_budget(self) -> None:
        optimum = optimize_affine_screen(seed=17)
        self.assertAlmostEqual(optimum.attenuation, 0.0139849238, places=8)
        self.assertAlmostEqual(optimum.poisson_load, 0.5, places=7)
        self.assertLess(optimum.attenuation, PICK_SURCHARGE)
        self.assertGreater(optimum.surcharge_gap, 0.0114)

    def test_cubic_root_screen_has_finite_lp_cost(self) -> None:
        cost = cyclotomic_three_interpolation_log_cost(
            6, 0.5 + 0.5j, target_angle_samples=8
        )
        self.assertGreater(cost / 6, 1.8)
        self.assertLess(cost / 6, 1.85)

    def test_poisson_cap_does_not_imply_fixed_N_carleson(self) -> None:
        ceiling = microscopic_cluster_poisson_ceiling(0.01, 0.47)
        self.assertLess(ceiling, 0.5)
        small = fixed_color_separation_upper_bound(100, 0.47, 7)
        large = fixed_color_separation_upper_bound(1000, 0.47, 7)
        self.assertLess(large, small / 900)


if __name__ == "__main__":
    unittest.main()
