import math
import unittest

import numpy as np

from carrier_ritz_loewner_gate import (
    actual_fixture_ritz,
    canonical_companion,
    lanczos_moments,
    two_dimensional_carrier_ritz,
    two_dimensional_ritz_from_entries,
)


class CarrierRitzLoewnerGateTests(unittest.TestCase):
    def test_closed_formula_matches_dense_angle_scan(self) -> None:
        rng = np.random.default_rng(20260812)
        theta = 0.37
        for _ in range(20):
            r, d = rng.normal(size=2)
            c = abs(float(rng.normal()))
            result = two_dimensional_ritz_from_entries(r, d, c, theta)
            x = np.linspace(theta, 1.0, 300001)
            values = (
                x * r + (1.0 - x) * d
                + 2.0 * c * np.sqrt(x * (1.0 - x))
            )
            self.assertAlmostEqual(result.value, float(np.max(values)), places=9)

    def test_boundary_branch(self) -> None:
        result = two_dimensional_ritz_from_entries(-2.0, 3.0, 0.25, 0.9)
        self.assertTrue(result.boundary_active)
        expected = -1.8 + 0.3 + 2.0 * math.sqrt(0.09) * 0.25
        self.assertAlmostEqual(result.value, expected)

    def test_lanczos_moment_identities(self) -> None:
        matrix = np.array(
            [[2.0, 1.0 - 0.5j, -0.3],
             [1.0 + 0.5j, -1.0, 0.7j],
             [-0.3, -0.7j, 0.4]],
            dtype=complex,
        )
        a = np.array([1.0, 0.0, 0.0], dtype=complex)
        w = canonical_companion(matrix, a)
        moments = lanczos_moments(matrix, a)
        direct = two_dimensional_carrier_ritz(matrix, a, w, 0.5)
        self.assertAlmostEqual(
            direct.coupling_modulus ** 2,
            moments["coupling_squared"],
        )
        self.assertAlmostEqual(
            direct.complement_diagonal,
            moments["complement_diagonal"],
        )

    def test_negative_scalar_loewner_countermodel(self) -> None:
        magnitude = 7.25
        matrix = -magnitude * np.eye(3)
        a = np.array([1.0, 0.0, 0.0])
        w = np.array([0.0, 1.0, 0.0])
        for theta in (0.1, 0.5, 0.9, 1.0):
            result = two_dimensional_carrier_ritz(matrix, a, w, theta)
            self.assertAlmostEqual(result.value, -magnitude)

    def test_actual_fixture_restricted_values_are_lower_bounds(self) -> None:
        payload = actual_fixture_ritz(64.0, theta_values=(0.9,))
        row = payload["rows"][0]
        full = row["full_q"]
        self.assertLessEqual(row["geometric_ritz_q"], full + 1e-10)
        for result in row["two_dimensional"].values():
            self.assertLessEqual(result["value"], full + 1e-10)


if __name__ == "__main__":
    unittest.main()
