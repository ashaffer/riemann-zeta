import unittest

import numpy as np

from shift_phase_covariance_falsifier import (
    ShiftedCharacteristic,
    scalar_coercive_metric,
)
from suzuki_selected_divisor_alignment import (
    PhaseRootScanner,
    alternating_split,
    continuum_positivity_certificate,
    first_critical_line_ordinates,
    fit_circular_phase,
    measured_metric_floor,
    optimize_phase_by_training_roots,
    ordered_injective_match,
    selected_divisor_alignment,
)


def circular_distance(left: float, right: float) -> float:
    return abs(np.angle(np.exp(1j * (left - right))))


class SuzukiSelectedDivisorAlignmentTest(unittest.TestCase):
    def test_first_known_ordinates_and_order(self) -> None:
        ordinates = first_critical_line_ordinates(3, dps=40)
        np.testing.assert_allclose(
            ordinates,
            [14.134725141734695, 21.022039638771556, 25.01085758014569],
            rtol=0.0,
            atol=2e-13,
        )
        self.assertTrue(np.all(np.diff(ordinates) > 0))

    def test_immutable_zero_table_rejects_unbundled_count(self) -> None:
        with self.assertRaisesRegex(ValueError, "only the first 20"):
            first_critical_line_ordinates(21)

    def test_circular_mean_recovers_exact_synthetic_phase(self) -> None:
        phase = 1.234
        phasors = np.full(7, np.exp(1j * phase))
        fit = fit_circular_phase(phasors)
        self.assertLess(abs(np.exp(1j * fit.phase) - np.exp(1j * phase)), 1e-14)
        self.assertLess(fit.residual_max, 1e-14)
        self.assertAlmostEqual(fit.resultant_length, 1.0, places=14)

    def test_alternating_split_is_disjoint_and_exhaustive(self) -> None:
        train, holdout = alternating_split(9)
        np.testing.assert_array_equal(train, [0, 2, 4, 6, 8])
        np.testing.assert_array_equal(holdout, [1, 3, 5, 7])
        np.testing.assert_array_equal(
            np.sort(np.concatenate([train, holdout])), np.arange(9)
        )

    def test_ordered_matching_rejects_nearest_root_reuse(self) -> None:
        # Independent nearest-neighbor matching would reuse 0.05 twice.
        match = ordered_injective_match([0.0, 0.1], [0.05, 10.0])
        np.testing.assert_array_equal(match.root_indices, [0, 1])
        self.assertEqual(len(np.unique(match.root_indices)), 2)
        self.assertGreater(match.maximum, 9.0)

    def test_ordered_matching_finds_exact_injected_subsequence(self) -> None:
        match = ordered_injective_match([2.0, 5.0, 9.0], [0.0, 2.0, 4.0, 5.0, 9.0, 12.0])
        np.testing.assert_array_equal(match.root_indices, [1, 3, 4])
        self.assertEqual(match.rms, 0.0)

    def test_phase_optimizer_recovers_planted_scalar_phase(self) -> None:
        dimension = 7
        radius = 0.75
        characteristic = ShiftedCharacteristic(
            scalar_coercive_metric(dimension), radius, -0.25
        )
        planted_phase = _planted_phase = 2.0 * np.pi * 7.0 / 64.0
        roots = characteristic.real_zeros(
            planted_phase, 0.0, 45.0, samples=12001
        )
        self.assertGreaterEqual(roots.size, 7)
        scanner = PhaseRootScanner(characteristic, 0.0, 45.0, samples=12001)
        optimization = optimize_phase_by_training_roots(
            scanner,
            roots[:7:2],
            phase_grid_size=64,
            refinement_levels=1,
            refinement_grid_size=17,
        )
        self.assertLess(circular_distance(optimization.phase, _planted_phase), 2e-4)
        self.assertLess(optimization.training_match_rms, 2e-3)

    def test_scalar_self_spectrum_is_exact_global_control(self) -> None:
        dimension = 7
        radius = 0.75
        shift = -0.25
        metric = scalar_coercive_metric(dimension)
        floor = measured_metric_floor(metric, shift)
        characteristic = ShiftedCharacteristic(metric, radius, shift)
        phase = 0.37
        roots = characteristic.real_zeros(phase, 0.0, 50.0, samples=12001)
        self.assertGreaterEqual(roots.size, 7)
        result = selected_divisor_alignment(
            "scalar-control",
            characteristic,
            floor,
            "primary",
            roots[:7],
            "synthetic-self-spectrum",
            root_scan_min=0.0,
            root_scan_max=50.0,
            root_samples=12001,
            phase_grid_size=65,
            refinement_levels=2,
            refinement_grid_size=17,
        )
        self.assertLess(circular_distance(result.optimized_phase, phase), 2e-4)
        self.assertLess(result.train_only_injective_rms, 2e-3)
        self.assertLess(result.global_injective_rms, 2e-3)
        indices = [
            int(value)
            for value in (
                result.training_matched_root_indices
                + ";"
                + result.holdout_matched_root_indices
            ).split(";")
        ]
        self.assertEqual(len(indices), len(set(indices)))
        self.assertTrue(result.symmetry_theta_zero_has_root_at_zero)
        self.assertTrue(np.isfinite(result.symmetry_theta_zero_global_rms))
        self.assertTrue(np.isfinite(result.symmetry_theta_pi_global_rms))

    def test_continuum_certificate_scope_and_bounds(self) -> None:
        first = continuum_positivity_certificate(1.75)
        second = continuum_positivity_certificate(2.0)
        third = continuum_positivity_certificate(2.996)
        self.assertIsNotNone(first)
        self.assertIsNotNone(second)
        self.assertIsNotNone(third)
        assert first is not None and second is not None and third is not None
        self.assertEqual(first.lower_bound, 2.2699e-5)
        self.assertEqual(second.lower_bound, 9.99e-11)
        self.assertEqual(third.lower_bound, 9.9e-16)
        self.assertIsNone(continuum_positivity_certificate(3.0))

    def test_numerically_unsafe_shift_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "numerically measured"):
            measured_metric_floor(2.0 * np.eye(4), shift=2.0)

    def test_reflection_phasor_symmetry_and_zero_phase_root(self) -> None:
        characteristic = ShiftedCharacteristic(
            scalar_coercive_metric(6), radius=0.75, shift=-0.25
        )
        values = np.asarray([0.7, 3.0, 8.0])
        positive = characteristic.boundary_phasor(values)
        negative = characteristic.boundary_phasor(-values)
        np.testing.assert_allclose(positive * negative, 1.0, atol=2e-13)
        self.assertLess(
            float(characteristic.normalized_characteristic_residual(0.0, 0.0)),
            1e-13,
        )


if __name__ == "__main__":
    unittest.main()
