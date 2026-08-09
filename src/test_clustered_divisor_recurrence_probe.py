import cmath
import math
import unittest

import numpy as np

from clustered_divisor_recurrence_probe import (
    build_clustered_symmetric_divisor,
    build_completed_detector,
    carrier_recurrence_bound,
    finite_recurrence_diagnostic,
    quantile_clustered_divisor,
    triangular_transform,
)


class ClusteredDivisorConstructionTests(unittest.TestCase):
    def test_triangular_multiplier_has_the_completed_symmetries(self) -> None:
        self.assertAlmostEqual(triangular_transform(0.0, 1.3).real, 1.3)
        value = 7.0 + 0.2j
        self.assertAlmostEqual(
            abs(triangular_transform(-value) - triangular_transform(value)),
            0.0,
            places=14,
        )
        self.assertAlmostEqual(
            abs(
                triangular_transform(value.conjugate())
                - triangular_transform(value).conjugate()
            ),
            0.0,
            places=14,
        )
        self.assertGreater(abs(triangular_transform(value)), 0.0)

    def test_pair_replacement_is_simple_symmetric_and_count_preserving(self) -> None:
        divisor = build_clustered_symmetric_divisor(
            (10.0, 11.0, 20.0, 21.0, 30.0, 31.0, 40.0),
            displacement=0.2,
            moved_pair_starts=(0, 2, 4),
        )
        self.assertEqual(len(divisor.nodes), 14)
        self.assertEqual(divisor.fixed_carrier_midpoint, 10.5)
        self.assertTrue(divisor.is_simple)
        self.assertTrue(divisor.has_exact_symmetries)
        self.assertEqual(divisor.maximum_counting_discrepancy, 1)
        self.assertTrue(all(abs(node.imag) <= 0.2 for node in divisor.nodes))

    def test_quantile_model_keeps_riemann_von_mangoldt_count_to_constant_error(self) -> None:
        divisor = quantile_clustered_divisor(
            node_count=32,
            displacement=0.15,
            moved_pair_starts=(0, 10, 12, 24),
        )
        self.assertEqual(divisor.maximum_counting_discrepancy, 1)
        self.assertTrue(divisor.is_simple)
        self.assertTrue(divisor.has_exact_symmetries)

    def test_invalid_pairs_and_strip_width_are_rejected(self) -> None:
        ordinates = (10.0, 11.0, 20.0, 21.0)
        with self.assertRaises(ValueError):
            build_clustered_symmetric_divisor(ordinates, 0.5, (0,))
        with self.assertRaises(ValueError):
            build_clustered_symmetric_divisor(ordinates, 0.2, (0, 1))
        with self.assertRaises(ValueError):
            build_clustered_symmetric_divisor(ordinates, 0.2, ())


class CompletedDetectorRecurrenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.divisor = build_clustered_symmetric_divisor(
            (10.0, 11.0, 20.0, 21.0, 30.0, 31.0, 40.0, 41.0),
            displacement=0.2,
            moved_pair_starts=(0, 2, 4),
        )
        cls.detector = build_completed_detector(cls.divisor, length=1.0)

    def test_upper_critical_lower_decomposition_is_exact(self) -> None:
        points = np.array([0.0, 1.5, 7.0, 15.0])
        direct = np.array(
            [
                sum(
                    triangular_transform(node)
                    * cmath.exp(-1j * node * point)
                    for node in self.divisor.nodes
                )
                * math.exp(-self.divisor.displacement * point)
                for point in points
            ]
        )
        np.testing.assert_allclose(
            self.detector.normalized_detector(points),
            direct,
            rtol=2.0e-14,
            atol=2.0e-14,
        )
        remainder = np.abs(
            self.detector.normalized_detector(points)
            - self.detector.top_series(points)
        )
        for point, error in zip(points, remainder):
            self.assertLessEqual(
                error,
                self.detector.uniform_normalization_error_bound(float(point))
                + 1.0e-14,
            )

    def test_carrier_has_an_uncancellable_positive_bohr_diagonal(self) -> None:
        bound = carrier_recurrence_bound(self.detector, block_length=1.25)
        self.assertGreater(bound.carrier_mean_square, 0.0)
        self.assertGreaterEqual(
            bound.top_mean_square, bound.carrier_mean_square
        )
        self.assertAlmostEqual(
            bound.block_weight,
            math.expm1(2.0 * bound.displacement * bound.block_length)
            / (2.0 * bound.displacement),
        )
        expected_density = (
            bound.top_mean_square - bound.carrier_mean_square / 2.0
        ) / (bound.top_l1_norm**2 - bound.carrier_mean_square / 2.0)
        self.assertAlmostEqual(bound.lower_density_bound, expected_density)
        self.assertGreater(bound.lower_density_bound, 0.0)
        self.assertLessEqual(bound.lower_density_bound, 1.0)
        self.assertAlmostEqual(
            bound.eventual_completed_block_threshold,
            bound.limiting_block_threshold / 2.0,
        )
        remainder = self.detector.uniform_normalization_error_bound(
            bound.sufficient_start_for_completed_threshold
        )
        self.assertLessEqual(
            remainder,
            bound.normalization_remainder_target * (1.0 + 1.0e-12),
        )

    def test_finite_diagnostic_shows_positive_not_zero_density(self) -> None:
        bound = carrier_recurrence_bound(self.detector, block_length=1.0)
        diagnostic = finite_recurrence_diagnostic(
            self.detector,
            bound,
            grid_start=0.0,
            grid_end=80.0,
            grid_step=0.02,
        )
        self.assertGreater(diagnostic.sampled_top_superlevel_density, 0.0)
        self.assertGreater(diagnostic.sampled_limiting_block_density, 0.0)
        self.assertTrue(math.isfinite(diagnostic.sampled_completed_block_density))
        self.assertGreater(diagnostic.sampled_completed_block_density, 0.0)

    def test_recurrence_inputs_are_validated(self) -> None:
        with self.assertRaises(ValueError):
            carrier_recurrence_bound(self.detector, 0.0)
        bound = carrier_recurrence_bound(self.detector, 1.0)
        with self.assertRaises(ValueError):
            finite_recurrence_diagnostic(
                self.detector,
                bound,
                grid_end=20.0,
                grid_step=0.03,
            )


if __name__ == "__main__":
    unittest.main()
