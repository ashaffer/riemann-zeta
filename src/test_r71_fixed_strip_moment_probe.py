import math
import unittest

import numpy as np

from r71_fixed_strip_moment_probe import (
    audit_scale_moments,
    bohr_phase_moment_density,
    completed_channel_transforms,
    fourth_moment_strip_gate,
    full_moment_strip_gate,
    multiplicative_energy_moment_density,
    scan_fixed_strip_moments,
    stress_cutoff_grid,
)
from r71_large_value_width_probe import (
    build_completed_microblock,
    centered_transform,
)


class BohrPhaseMomentFormulaTests(unittest.TestCase):
    def test_one_channel_reduces_to_the_ordinary_even_moments(self) -> None:
        values = np.array([[3.0 + 4.0j], [-2.0j]])
        np.testing.assert_allclose(
            bohr_phase_moment_density(values, 4),
            np.abs(values[:, 0]) ** 4,
        )
        np.testing.assert_allclose(
            bohr_phase_moment_density(values, 6),
            np.abs(values[:, 0]) ** 6,
        )

    def test_two_unit_channels_have_the_exact_phase_averages(self) -> None:
        values = np.array([[1.0, 1.0], [1.0j, -1.0]])
        np.testing.assert_allclose(
            bohr_phase_moment_density(values, 4),
            np.array([6.0, 6.0]),
        )
        np.testing.assert_allclose(
            bohr_phase_moment_density(values, 6),
            np.array([20.0, 20.0]),
        )

    def test_formula_rejects_unsupported_powers_and_malformed_arrays(self) -> None:
        with self.assertRaises(ValueError):
            bohr_phase_moment_density(np.ones((2, 1)), 8)
        with self.assertRaises(ValueError):
            bohr_phase_moment_density(np.ones(2), 4)
        with self.assertRaises(ValueError):
            bohr_phase_moment_density(np.array([[math.nan]]), 4)

    def test_multiplicative_comparator_adds_exact_product_collisions(self) -> None:
        values = np.ones((1, 4), dtype=complex)
        # The only nontrivial unordered pair collision is
        # 6*35 = 10*21.  Its two ordered amplitudes are both two, adding
        # the cross contribution 2*2*2=8 to the independent value 28.
        phase = bohr_phase_moment_density(values, 4)
        multiplicative = multiplicative_energy_moment_density(
            values, (6, 35, 10, 21), 4
        )
        np.testing.assert_allclose(phase, np.array([28.0]))
        np.testing.assert_allclose(multiplicative, np.array([36.0]))

        # With multiplicatively independent labels the two comparators agree.
        independent = np.ones((2, 2), dtype=complex)
        for power, expected in ((4, 6.0), (6, 20.0)):
            np.testing.assert_allclose(
                multiplicative_energy_moment_density(
                    independent, (2, 3), power
                ),
                np.array([expected, expected]),
            )

    def test_multiplicative_comparator_validates_formal_labels(self) -> None:
        with self.assertRaises(ValueError):
            multiplicative_energy_moment_density(
                np.ones((2, 2)), (2,), 4
            )
        with self.assertRaises(ValueError):
            multiplicative_energy_moment_density(
                np.ones((2, 2)), (1, 0), 4
            )


class FourthMomentStripGateTests(unittest.TestCase):
    def test_full_line_gate_has_the_sharp_moment_width(self) -> None:
        fourth = full_moment_strip_gate(0.5)
        self.assertEqual(fourth.moment_power, 4)
        self.assertAlmostEqual(fourth.baseline_moment_exponent, 2.0)
        self.assertAlmostEqual(fourth.maximum_displacement, 3.0 / 8.0)
        self.assertAlmostEqual(fourth.strip_width, 1.0 / 8.0)
        self.assertAlmostEqual(fourth.right_boundary, 7.0 / 8.0)

        sixth = full_moment_strip_gate(0.6, 6)
        self.assertAlmostEqual(sixth.baseline_moment_exponent, 3.0)
        self.assertAlmostEqual(sixth.strip_width, 0.1)
        self.assertAlmostEqual(sixth.right_boundary, 0.9)

    def test_full_line_gate_validates_power_and_saving(self) -> None:
        for moment_power in (1, 1.5, True):
            with self.assertRaises(ValueError):
                full_moment_strip_gate(0.1, moment_power)
        for kappa in (0.0, 2.0, math.inf):
            with self.assertRaises(ValueError):
                full_moment_strip_gate(kappa, 4)

    def test_exact_conditional_exponent_identities(self) -> None:
        gate = fourth_moment_strip_gate(0.5, 2)
        self.assertAlmostEqual(gate.height_exponent_tau, 1.0 / 18.0)
        self.assertAlmostEqual(gate.energy_saving_eta, 1.0 / 9.0)
        self.assertAlmostEqual(gate.energy_upper_exponent, 7.0 / 9.0)
        self.assertAlmostEqual(gate.right_boundary, 8.0 / 9.0)
        self.assertAlmostEqual(
            gate.energy_saving_eta,
            gate.derivative_order * gate.height_exponent_tau,
        )
        self.assertAlmostEqual(
            gate.energy_upper_exponent,
            1.0 - 2.0 * gate.energy_saving_eta,
        )

    def test_strip_gate_validates_kappa_and_derivative_order(self) -> None:
        for kappa in (0.0, 2.0, math.inf):
            with self.assertRaises(ValueError):
                fourth_moment_strip_gate(kappa, 1)
        for derivative_order in (0, -1, True):
            with self.assertRaises(ValueError):
                fourth_moment_strip_gate(0.5, derivative_order)


class CompletedChannelMomentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = build_completed_microblock(gaussian_order=16)

    def test_boundary_products_and_signed_center_reconstruct_completion(self) -> None:
        frequencies = np.array([-43.0, -7.0, 0.0, 19.0, 71.0])
        channels = completed_channel_transforms(self.model, frequencies)
        direct = centered_transform(self.model, frequencies)

        self.assertEqual(
            channels.shape,
            (len(frequencies), len(self.model.active_product_values) + 1),
        )
        np.testing.assert_allclose(
            np.sum(channels, axis=1), direct, rtol=0.0, atol=8.0e-15
        )
        np.testing.assert_allclose(
            channels[:, -1],
            -centered_transform(self.model, frequencies, component="center"),
            rtol=0.0,
            atol=1.0e-15,
        )
        self.assertGreater(float(np.max(np.abs(channels[:, 0]))), 0.0)

    def test_single_scale_audit_normalizes_the_long_window_exactly(self) -> None:
        audit = audit_scale_moments(
            59.0,
            heights=(10.0,),
            long_height=20.0,
            frequency_step=0.5,
            gaussian_order=12,
        )
        self.assertLess(audit.channel_completion_error, 1.0e-12)
        self.assertEqual(audit.channel_count, audit.active_product_count + 1)
        for power in (4, 6):
            local = audit.comparison(power, 10.0)
            long = audit.comparison(power, 20.0)
            self.assertGreater(local.completed_moment, 0.0)
            self.assertGreater(local.bohr_phase_moment, 0.0)
            self.assertGreater(local.multiplicative_energy_moment, 0.0)
            self.assertLessEqual(local.completed_moment, long.completed_moment)
            self.assertGreater(local.completed_to_bohr_ratio, 0.0)
            self.assertGreater(
                local.completed_to_multiplicative_energy_ratio, 0.0
            )
            self.assertAlmostEqual(long.fraction_of_long_window_moment, 1.0)
            self.assertAlmostEqual(long.local_mean_to_long_mean_ratio, 1.0)

    def test_two_scale_scan_reports_only_finite_range_candidate_fits(self) -> None:
        scan = scan_fixed_strip_moments(
            scales=(59.0, 127.0),
            heights=(10.0,),
            long_height=20.0,
            frequency_step=0.5,
            gaussian_order=12,
        )
        self.assertEqual(len(scan.audits), 2)
        self.assertEqual(len(scan.fits), 4)
        self.assertGreater(scan.largest_fourth_moment_concentration, 0.0)
        self.assertGreater(scan.largest_sixth_moment_concentration, 0.0)
        self.assertGreater(
            scan.largest_fourth_multiplicative_concentration, 0.0
        )
        self.assertGreater(
            scan.largest_sixth_multiplicative_concentration, 0.0
        )
        for fit in scan.fits:
            self.assertEqual(fit.scale_count, 2)
            self.assertTrue(math.isfinite(fit.completed_moment_slope))
            self.assertTrue(math.isfinite(fit.coherence_ratio_slope))
            self.assertTrue(
                math.isfinite(fit.multiplicative_coherence_ratio_slope)
            )
            self.assertAlmostEqual(fit.completed_moment_r_squared, 1.0)
            self.assertAlmostEqual(fit.coherence_ratio_r_squared, 1.0)
            self.assertAlmostEqual(
                fit.multiplicative_coherence_ratio_r_squared, 1.0
            )

    def test_scan_and_window_validation_fail_before_numerics(self) -> None:
        with self.assertRaises(ValueError):
            audit_scale_moments(
                59.0,
                heights=(20.0, 10.0),
                long_height=40.0,
            )
        with self.assertRaises(ValueError):
            audit_scale_moments(
                59.0,
                heights=(10.0,),
                long_height=10.0,
            )
        with self.assertRaises(ValueError):
            scan_fixed_strip_moments(
                scales=(59.0, 127.0),
                cutoffs=(4,),
            )

    def test_x127_y8_kills_both_finite_domination_guesses(self) -> None:
        stress = stress_cutoff_grid(
            scales=(127.0,),
            cutoffs=(6, 8),
            heights=(40.0,),
            long_height=80.0,
            frequency_step=0.5,
            gaussian_order=12,
        )
        self.assertEqual(len(stress.audits), 2)
        self.assertGreater(stress.phase_baseline_exceedance_count, 0)
        self.assertGreater(stress.multiplicative_baseline_exceedance_count, 0)
        expected = {
            ("phase", 4): 1.6334823915,
            ("phase", 6): 1.7162258774,
            ("multiplicative", 4): 1.5947043586,
            ("multiplicative", 6): 1.6235788308,
        }
        for (baseline, power), expected_ratio in expected.items():
            peak = stress.peak(power, baseline)
            self.assertEqual(peak.scale, 127.0)
            self.assertEqual(peak.cutoff, 8)
            self.assertEqual(peak.height, 80.0)
            self.assertAlmostEqual(peak.ratio, expected_ratio, places=6)

        with self.assertRaises(ValueError):
            stress_cutoff_grid(scales=(127.0,), cutoffs=(8, 6))


if __name__ == "__main__":
    unittest.main()
