import unittest

import numpy as np

from shift_phase_covariance_falsifier import (
    ShiftedCharacteristic,
    scalar_coercive_metric,
)
from suzuki_weighted_clark_measure_diagnostic import (
    analytic_boundary_phase_derivative,
    analyze_weighted_clark_candidates,
    defect_overlap_data,
    normalized_clark_candidate_weights,
    weighted_cauchy_transform,
)
from suzuki_weighted_clark_target_diagnostic import (
    cauchy_transform_from_characteristic,
    first_symmetric_zero_pair_mass,
)
from suzuki_livsic_calibration import XiLivsicTarget, xi_log_derivative


class SuzukiWeightedClarkMeasureDiagnosticTest(unittest.TestCase):
    def test_cayley_atom_normalization(self) -> None:
        # Check the pointwise formula at three hypothetical Cayley crossings.
        locations = np.array([-3.0, 0.0, 4.0])
        derivatives = 2.0 / (1.0 + locations**2)
        np.testing.assert_allclose(
            normalized_clark_candidate_weights(locations, derivatives),
            np.ones(3),
            rtol=0.0,
            atol=1e-14,
        )

    def test_analytic_phase_derivative_matches_centered_difference(self) -> None:
        characteristic = ShiftedCharacteristic(
            scalar_coercive_metric(6), radius=0.6, shift=-0.25
        )
        points = np.array([-4.0, -1.0, 0.0, 2.0, 5.0])
        step = 1e-5
        left = characteristic.boundary_phasor(points - step)
        right = characteristic.boundary_phasor(points + step)
        finite_difference = np.angle(right / left) / (2.0 * step)
        np.testing.assert_allclose(
            analytic_boundary_phase_derivative(characteristic, points),
            finite_difference,
            rtol=2e-7,
            atol=2e-8,
        )

    def test_defect_overlap_weights_are_exact_but_not_a_root_measure(self) -> None:
        characteristic = ShiftedCharacteristic(
            scalar_coercive_metric(4), radius=0.75, shift=-0.25
        )
        roots = characteristic.real_zeros(
            0.0, -80.0, 80.0, samples=16001
        )
        weights, normalized_gram = defect_overlap_data(
            characteristic, roots
        )
        self.assertGreater(roots.size, characteristic.dimension)
        self.assertGreater(float(np.sum(weights)), 1.5)
        off_diagonal = np.abs(
            normalized_gram - np.eye(roots.size, dtype=complex)
        )
        self.assertGreater(float(np.max(off_diagonal)), 0.9)

    def test_full_audit_keeps_phase_and_defect_weights_distinct(self) -> None:
        characteristic = ShiftedCharacteristic(
            scalar_coercive_metric(6), radius=0.5, shift=-0.25
        )
        row = analyze_weighted_clark_candidates(
            characteristic,
            model="scalar-control",
            support=2.0,
            phase=0.0,
            height=30.0,
            samples=8001,
        )
        self.assertEqual(row.nonpositive_phase_derivative_count, 0)
        self.assertGreater(row.phase_candidate_mass, 0.9)
        self.assertIn("pending", row.measure_status)
        self.assertGreaterEqual(row.maximum_distinct_root_coherence, 0.0)

    def test_cauchy_transform_rejects_invalid_measure_data(self) -> None:
        value = weighted_cauchy_transform(
            np.array([-1.0, 2.0]), np.array([0.25, 0.75]), 1j
        )
        self.assertGreater(value.imag, 0.0)
        with self.assertRaises(ValueError):
            weighted_cauchy_transform(
                np.array([0.0]), np.array([-1.0]), 1j
            )
        with self.assertRaises(ValueError):
            weighted_cauchy_transform(
                np.array([0.0]), np.array([1.0]), -1j
            )

    def test_root_free_transform_recovers_target_log_derivative(self) -> None:
        import mpmath as mp

        with mp.workdps(60):
            target = XiLivsicTarget.compute(dps=50)
            z = 2 * mp.j
            transformed = cauchy_transform_from_characteristic(
                target.characteristic(z), z
            )
            logarithmic_derivative = xi_log_derivative(
                mp.mpf("0.5") - mp.j * z
            )
            expected = (
                mp.j * logarithmic_derivative / target.ell - z
            ) / (1 + z**2)
            self.assertLess(abs(transformed - expected), mp.mpf("1e-40"))

    def test_first_zero_pair_has_substantial_target_mass(self) -> None:
        target = XiLivsicTarget.compute(dps=50)
        mass = first_symmetric_zero_pair_mass(
            14.134725141734693790457251983562, target.ell
        )
        self.assertAlmostEqual(float(mass), 0.2158975286051251, places=14)


if __name__ == "__main__":
    unittest.main()
