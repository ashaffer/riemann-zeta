import math
import unittest

import numpy as np

from shift_phase_covariance_falsifier import (
    ShiftedCharacteristic,
    scalar_coercive_metric,
)
from suzuki_defect_escape_diagnostic import (
    nested_projection_statistics,
    translated_riesz_lower_bound,
)


class SuzukiDefectEscapeDiagnosticTest(unittest.TestCase):
    def test_projection_statistics_have_exact_scalar_values(self) -> None:
        statistics = nested_projection_statistics(2.0, 8.0)
        self.assertEqual(statistics.squared_projection_mass, 0.25)
        self.assertEqual(statistics.normalized_coherence, 0.5)
        self.assertEqual(statistics.projection_tail_fraction, 0.75)
        self.assertEqual(statistics.normalized_squared_distance, 1.0)

    def test_projection_statistics_reject_decreasing_norm(self) -> None:
        with self.assertRaises(ValueError):
            nested_projection_statistics(2.0, 1.0)
        with self.assertRaises(ValueError):
            nested_projection_statistics(0.0, 1.0)

    def test_synthetic_nested_metric_has_the_projection_identity(self) -> None:
        small_metric = np.array([[2.0]])
        large_metric = np.array([[2.0, 0.2], [0.2, 3.0]])
        small_forcing = np.array([1.0])
        large_forcing = np.array([1.0, 4.0])
        small_vector = np.linalg.solve(small_metric, small_forcing)
        large_vector = np.linalg.solve(large_metric, large_forcing)
        embedded_small = np.array([small_vector[0], 0.0])
        residual = large_vector - embedded_small

        # Orthogonality to the embedded old space characterizes the projection.
        old_test = np.array([1.0, 0.0])
        self.assertAlmostEqual(
            float(old_test @ large_metric @ residual), 0.0, places=14
        )
        small_norm_sq = float(small_forcing @ small_vector)
        large_norm_sq = float(large_forcing @ large_vector)
        cross = float(embedded_small @ large_metric @ large_vector)
        self.assertAlmostEqual(cross, small_norm_sq, places=14)
        statistics = nested_projection_statistics(
            small_norm_sq, large_norm_sq
        )
        self.assertAlmostEqual(
            cross / math.sqrt(small_norm_sq * large_norm_sq),
            statistics.normalized_coherence,
            places=14,
        )

    def test_translated_riesz_bound_has_exponential_escape(self) -> None:
        base = translated_riesz_lower_bound(2.0, 5.0, 0.0)
        translated = translated_riesz_lower_bound(2.0, 5.0, 3.0)
        self.assertAlmostEqual(translated / base, math.exp(6.0), places=12)
        with self.assertRaises(ValueError):
            translated_riesz_lower_bound(1.0, 1.0, -1.0)

    def test_reflection_symmetric_control_has_equal_defect_norms(self) -> None:
        characteristic = ShiftedCharacteristic(
            scalar_coercive_metric(6), radius=0.6, shift=-0.25
        )
        shifted_metric = characteristic.metric + 0.25 * np.eye(6)
        minus_norm_sq = float(
            np.real(
                np.vdot(
                    characteristic.v_minus_coefficients,
                    shifted_metric @ characteristic.v_minus_coefficients,
                )
            )
        )
        plus_norm_sq = float(
            np.real(
                np.vdot(
                    characteristic.v_plus_coefficients,
                    shifted_metric @ characteristic.v_plus_coefficients,
                )
            )
        )
        self.assertAlmostEqual(minus_norm_sq, plus_norm_sq, places=13)


if __name__ == "__main__":
    unittest.main()
