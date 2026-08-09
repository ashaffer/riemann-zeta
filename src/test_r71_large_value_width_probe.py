import math
import unittest

import numpy as np

from r71_large_value_width_probe import (
    build_completed_microblock,
    centered_transform,
    compact_global_width,
    energy_exceptional_gate,
    guth_maynard_exponent_gate,
    moment_gate,
    quadrature_refinement_error,
    raw_moment_gate,
    raw_point_width,
    raw_transform,
    sobolev_exponent_gate,
    synthetic_mode_audit,
    turan_remez_gate,
    width_gate,
)


class AnalyticLargeValueGateTests(unittest.TestCase):
    def test_raw_width_keeps_the_value_to_global_supremum_ratio(self) -> None:
        self.assertAlmostEqual(raw_point_width(2.0, 10.0, 4.0), 0.1)
        self.assertAlmostEqual(
            raw_point_width(2.0, 10.0, 4.0, fraction=0.25),
            0.15,
        )
        with self.assertRaises(ValueError):
            raw_point_width(10.1, 10.0, 4.0)

    def test_compact_global_width_has_the_correct_half_level_constant(self) -> None:
        half_width = 4.0
        self.assertAlmostEqual(compact_global_width(half_width), 0.25)
        # A support interval [-B,B] has frequency diameter 2B.  At a
        # global maximum the raw and compact Bernstein formulas agree.
        self.assertAlmostEqual(
            compact_global_width(half_width),
            raw_point_width(7.0, 7.0, 2.0 * half_width),
        )

    def test_completed_energy_forces_the_stated_threshold_and_measure(self) -> None:
        gate = energy_exceptional_gate(
            energy=8.0,
            support_length=4.0,
            height=10.0,
            eta=0.25,
        )
        self.assertAlmostEqual(gate.spectral_energy_floor, 4.0 * math.pi)
        self.assertAlmostEqual(gate.threshold, math.sqrt(math.pi / 10.0))
        self.assertAlmostEqual(
            gate.exceptional_measure_lower_bound,
            math.pi / 16.0,
        )

    def test_fixed_sobolev_order_has_the_one_over_4q_plus_2_gate(self) -> None:
        critical = sobolev_exponent_gate(0.1, 2)
        self.assertAlmostEqual(critical.minimum_height_exponent, 0.2)
        self.assertAlmostEqual(critical.limiting_threshold_exponent, 0.0)
        self.assertAlmostEqual(critical.critical_displacement, 0.1)
        self.assertFalse(critical.positive_threshold)

        above = sobolev_exponent_gate(0.11, 2)
        self.assertGreater(above.limiting_threshold_exponent, 0.0)
        self.assertTrue(above.positive_threshold)

    def test_guth_maynard_length_term_never_excludes_one_value(self) -> None:
        gate = guth_maynard_exponent_gate(0.1, 0.05)
        expected = (0.8, 1.2, 0.05)
        for observed, target in zip(gate.normalized_exponents, expected):
            self.assertAlmostEqual(observed, target)
        self.assertAlmostEqual(gate.one_value_barrier_exponent, 1.2)
        self.assertFalse(gate.excludes_one_value)

        near_edge = guth_maynard_exponent_gate(0.49, 0.0)
        self.assertAlmostEqual(near_edge.length_term_exponent, 0.02)
        self.assertGreater(near_edge.one_value_barrier_exponent, 0.0)
        self.assertFalse(near_edge.excludes_one_value)

    def test_raw_moment_threshold_matches_the_sobolev_critical_value(self) -> None:
        below = raw_moment_gate(0.09, 2, upper_exponent=0.0)
        above = raw_moment_gate(0.11, 2, upper_exponent=0.0)
        self.assertAlmostEqual(below.forced_exponent, -0.05)
        self.assertAlmostEqual(above.forced_exponent, 0.05)
        self.assertAlmostEqual(
            above.critical_displacement_for_zero_upper,
            0.1,
        )
        self.assertFalse(below.excludes_displacement)
        self.assertTrue(above.excludes_displacement)

    def test_optimized_finite_moment_gate_constants(self) -> None:
        gate = moment_gate(
            moment_upper_bound=3.0,
            peak_lower_bound=5.0,
            power=4,
            centered_type=0.2,
            raw_type=4.0,
        )
        self.assertAlmostEqual(gate.optimized_theta, 0.8)
        self.assertAlmostEqual(gate.markov_measure_upper_bound, 3.0 / 256.0)
        self.assertAlmostEqual(gate.centered_bernstein_measure_lower_bound, 2.0)
        self.assertAlmostEqual(gate.raw_bernstein_measure_lower_bound, 0.1)

    def test_term_count_remez_gate_records_its_own_failure_regime(self) -> None:
        constant = turan_remez_gate(1, interval_length=3.0)
        self.assertEqual(constant.critical_theta, 1.0)
        self.assertEqual(constant.superlevel_measure_lower_bound, 3.0)

        many_terms = turan_remez_gate(8, theta=0.5)
        self.assertLess(many_terms.critical_theta, 0.5)
        self.assertEqual(many_terms.superlevel_measure_lower_bound, 0.0)


class CompletedMicroblockNumericalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = build_completed_microblock(gaussian_order=16)

    def test_builder_keeps_boundary_products_and_the_full_center(self) -> None:
        model = self.model
        self.assertEqual(
            model.active_product_values,
            (49, 54, 55, 56, 60, 63, 65, 66),
        )
        # Product 49 lies outside the block itself and is present only
        # because its compact profile intersects the lower boundary strip.
        self.assertLess(math.log(49.0), model.lower)
        self.assertGreater(
            math.log(49.0) + model.coboundary_width,
            model.lower,
        )
        np.testing.assert_allclose(
            model.completed_values,
            model.tail_values - model.center_values,
            rtol=0.0,
            atol=1.0e-15,
        )
        self.assertGreater(float(np.max(np.abs(model.center_values))), 0.0)

    def test_centered_and_raw_transforms_differ_only_by_the_known_phase(self) -> None:
        model = self.model
        frequencies = np.array([-40.0, 0.0, 17.0, 53.0])
        centered = centered_transform(model, frequencies)
        raw = raw_transform(model, frequencies)
        phase = np.exp(-1j * frequencies * model.logarithmic_center)
        np.testing.assert_allclose(raw, phase * centered, atol=2.0e-15)
        np.testing.assert_allclose(np.abs(raw), np.abs(centered), atol=2.0e-15)

        centered_derivative = centered_transform(
            model,
            frequencies,
            derivative_order=1,
        )
        raw_derivative = raw_transform(
            model,
            frequencies,
            derivative_order=1,
        )
        np.testing.assert_allclose(
            raw_derivative,
            phase
            * (
                centered_derivative
                - 1j * model.logarithmic_center * centered
            ),
            atol=3.0e-15,
        )

    def test_completed_transform_retains_center_cancellation(self) -> None:
        model = self.model
        frequencies = np.array([0.0, 25.0, 50.0])
        completed = centered_transform(model, frequencies, component="completed")
        tail = centered_transform(model, frequencies, component="tail")
        center = centered_transform(model, frequencies, component="center")
        np.testing.assert_allclose(completed, tail - center, atol=3.0e-15)
        self.assertLess(abs(completed[0]), 0.2 * abs(tail[0]))

    def test_modest_scan_respects_centered_width_and_derivative_bounds(self) -> None:
        model = self.model
        gate = width_gate(
            model,
            frequency_bound=100.0,
            frequency_points=4_001,
        )
        self.assertTrue(gate.peak_is_interior)
        self.assertAlmostEqual(gate.peak_frequency, -42.285, places=2)
        self.assertAlmostEqual(
            gate.conditional_global_bernstein_width,
            compact_global_width(model.half_width),
        )
        self.assertGreaterEqual(
            gate.observed_superlevel_component_width,
            gate.conditional_global_bernstein_width,
        )
        self.assertLessEqual(
            gate.observed_centered_derivative_maximum,
            gate.centered_type * model.tapered_l1_norm + 1.0e-14,
        )
        self.assertLessEqual(
            gate.observed_raw_derivative_maximum,
            gate.raw_type * model.tapered_l1_norm + 1.0e-14,
        )
        self.assertGreater(
            gate.l1_centered_width_at_observed_peak,
            gate.l1_raw_width_at_observed_peak,
        )

    def test_quadrature_refinement_is_negligible(self) -> None:
        error = quadrature_refinement_error(
            self.model,
            frequencies=(0.0, 1.0, 25.0, 50.0),
            refined_order=24,
        )
        self.assertLess(error, 1.0e-12)

    def test_synthetic_mode_separates_raw_phase_from_compact_width(self) -> None:
        audit = synthetic_mode_audit(gaussian_order=128)
        self.assertAlmostEqual(audit.peak_frequency, audit.ordinate)
        self.assertAlmostEqual(audit.pure_frequency_raw_derivative_ratio, 1_000.0)
        self.assertEqual(audit.pure_frequency_centered_derivative_ratio, 0.0)
        self.assertGreaterEqual(
            audit.observed_half_height_width,
            audit.bernstein_half_height_width,
        )


if __name__ == "__main__":
    unittest.main()
