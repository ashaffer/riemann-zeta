import unittest

import numpy as np

from shift_phase_covariance_falsifier import (
    ShiftedCharacteristic,
    diagnose_phase_alignment,
    dirichlet_energy_metric,
    scalar_coercive_metric,
)


class ShiftPhaseCovarianceTest(unittest.TestCase):
    def test_real_boundary_phasor_has_unit_modulus(self) -> None:
        metric = dirichlet_energy_metric(6, radius=0.75)
        characteristic = ShiftedCharacteristic(
            metric, radius=0.75, shift=0.0, basis_kind="dirichlet-sine"
        )
        phasors = characteristic.boundary_phasor(
            np.linspace(-12.0, 12.0, 31), normalize=False
        )
        np.testing.assert_allclose(np.abs(phasors), 1.0, atol=1e-12)

    def test_located_roots_annihilate_characteristic(self) -> None:
        phase = 0.37
        metric = dirichlet_energy_metric(6, radius=0.75)
        characteristic = ShiftedCharacteristic(
            metric, radius=0.75, shift=0.0, basis_kind="dirichlet-sine"
        )
        roots = characteristic.real_zeros(
            phase, -16.0, 16.0, samples=4001
        )
        self.assertGreaterEqual(len(roots), 4)
        residual = characteristic.normalized_characteristic_residual(
            roots, phase
        )
        self.assertLess(float(np.max(residual)), 1e-9)

    def test_scalar_metric_is_exact_positive_control(self) -> None:
        metric = scalar_coercive_metric(6)
        diagnostic = diagnose_phase_alignment(
            "scalar",
            ShiftedCharacteristic(metric, 0.75, 0.0),
            ShiftedCharacteristic(metric, 0.75, -1.0),
            phase=0.37,
            z_min=-16.0,
            z_max=16.0,
            samples=4001,
            root_limit=7,
        )
        self.assertLess(diagnostic.required_phase_chord_diameter, 1e-10)
        self.assertLess(diagnostic.phase_velocity_range, 1e-10)
        self.assertLess(diagnostic.max_normalized_residual, 1e-10)
        self.assertLess(diagnostic.nearest_root_max, 1e-9)

    def test_dirichlet_energy_rejects_one_constant_phase(self) -> None:
        metric = dirichlet_energy_metric(6, radius=0.75)
        diagnostic = diagnose_phase_alignment(
            "dirichlet",
            ShiftedCharacteristic(
                metric, 0.75, 0.0, basis_kind="dirichlet-sine"
            ),
            ShiftedCharacteristic(
                metric, 0.75, -1.0, basis_kind="dirichlet-sine"
            ),
            phase=0.37,
            z_min=-16.0,
            z_max=16.0,
            samples=4001,
            root_limit=7,
        )
        self.assertGreater(diagnostic.required_phase_chord_diameter, 1e-3)
        self.assertGreater(diagnostic.phase_velocity_range, 1e-3)
        self.assertGreater(diagnostic.max_normalized_residual, 1e-4)

    def test_shift_must_stay_below_metric_floor(self) -> None:
        metric = scalar_coercive_metric(4, value=2.0)
        with self.assertRaises(ValueError):
            ShiftedCharacteristic(metric, radius=0.5, shift=2.0)

    def test_root_scan_rejects_nonreflection_metric(self) -> None:
        metric = np.array([[3.0, 0.2], [0.2, 5.0]])
        characteristic = ShiftedCharacteristic(metric, radius=0.75, shift=0.0)
        with self.assertRaisesRegex(ValueError, "reflection-symmetric"):
            characteristic.boundary_phasor(np.linspace(-5.0, 5.0, 21))

    def test_phase_velocity_matches_centered_shift_difference(self) -> None:
        radius = 0.75
        metric = dirichlet_energy_metric(6, radius)
        z = np.array([-4.0, 1.5, 6.0])
        step = 1e-5
        center = ShiftedCharacteristic(
            metric, radius, 0.0, basis_kind="dirichlet-sine"
        )
        plus = ShiftedCharacteristic(
            metric, radius, step, basis_kind="dirichlet-sine"
        )
        minus = ShiftedCharacteristic(
            metric, radius, -step, basis_kind="dirichlet-sine"
        )
        finite_difference = np.angle(
            plus.boundary_phasor(z) * np.conj(minus.boundary_phasor(z))
        ) / (2.0 * step)
        np.testing.assert_allclose(
            center.phase_velocity(z), finite_difference, rtol=2e-7, atol=2e-8
        )


if __name__ == "__main__":
    unittest.main()
