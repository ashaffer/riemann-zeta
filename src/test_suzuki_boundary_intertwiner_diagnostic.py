import unittest

import numpy as np

from shift_phase_covariance_falsifier import (
    diagonal_coercive_metric,
    scalar_coercive_metric,
)
from suzuki_boundary_intertwiner_diagnostic import (
    DeficiencyKernelFamily,
    compare_projective_kernels,
    evaluate_affine_pair,
    evaluate_shift_pair,
    tune_affine_reparameterization,
    tune_target_shift,
)


PROBES = [-6.0, -2.0, 0.0, 2.0, 6.0, 1j, -1j]


class SuzukiBoundaryIntertwinerDiagnosticTest(unittest.TestCase):
    def test_kernel_is_hermitian_positive(self) -> None:
        family = DeficiencyKernelFamily(
            diagonal_coercive_metric(7), 0.8, PROBES
        )
        kernel = family.kernel(-0.25)
        np.testing.assert_allclose(kernel, kernel.conj().T, atol=1e-13)
        self.assertGreater(float(np.linalg.eigvalsh(kernel)[0]), -1e-12)
        normalized = family.normalized_kernel(-0.25)
        np.testing.assert_allclose(np.diag(normalized), 1.0, atol=1e-13)
        np.testing.assert_allclose(
            normalized,
            family.normalized_kernel(-0.25, probes=PROBES),
            atol=2e-13,
        )

    def test_phase_gauge_is_invisible_to_all_residuals(self) -> None:
        family = DeficiencyKernelFamily(
            diagonal_coercive_metric(7), 0.8, PROBES
        )
        reference = family.normalized_kernel(-0.25)
        phases = np.exp(1j * np.linspace(0.1, 1.7, len(PROBES)))
        target = np.conj(phases[:, None]) * phases[None, :] * reference
        residual = compare_projective_kernels(reference, target)
        self.assertLess(residual.magnitude_max, 1e-13)
        self.assertLess(residual.bargmann_phase_max, 1e-13)
        self.assertLess(residual.gauge_residual_rms, 1e-13)

    def test_scalar_metric_shift_is_exact_positive_control(self) -> None:
        family = DeficiencyKernelFamily(
            scalar_coercive_metric(7), 0.8, PROBES
        )
        residual = compare_projective_kernels(
            family.normalized_kernel(0.0), family.normalized_kernel(-2.0)
        )
        self.assertLess(residual.gauge_residual_rms, 1e-12)
        self.assertLess(residual.magnitude_max, 1e-12)

    def test_affine_dilation_is_exact_scalar_control(self) -> None:
        reference_radius = 0.55
        target_radius = 0.9
        metric = scalar_coercive_metric(7)
        reference = DeficiencyKernelFamily(metric, reference_radius, PROBES)
        target = DeficiencyKernelFamily(metric, target_radius, PROBES)
        diagnostic = evaluate_affine_pair(
            reference,
            target,
            reference_shift=0.0,
            target_shift=0.0,
            alpha=reference_radius / target_radius,
            beta=0.0,
            train_indices=[0, 2, 4, 5],
            holdout_indices=[1, 3, 6],
        )
        self.assertLess(diagnostic.full.gauge_residual_rms, 2e-12)
        self.assertLess(diagnostic.full.magnitude_max, 2e-12)

    def test_affine_grid_recovers_scalar_dilation(self) -> None:
        reference_radius = 0.6
        target_radius = 0.8
        metric = scalar_coercive_metric(7)
        reference = DeficiencyKernelFamily(metric, reference_radius, PROBES)
        target = DeficiencyKernelFamily(metric, target_radius, PROBES)
        diagnostic = tune_affine_reparameterization(
            reference,
            target,
            reference_shift=0.0,
            target_shift=0.0,
            alpha_min=0.6,
            alpha_max=0.9,
            beta_min=-0.5,
            beta_max=0.5,
            train_indices=[0, 2, 4, 5],
            holdout_indices=[1, 3, 6],
            grid_size=17,
            refinement_levels=3,
        )
        self.assertAlmostEqual(
            diagnostic.alpha, reference_radius / target_radius, places=4
        )
        self.assertLess(diagnostic.full.gauge_residual_rms, 1e-6)

    def test_dirichlet_metric_is_a_fixed_shift_negative_control(self) -> None:
        from shift_phase_covariance_falsifier import dirichlet_energy_metric

        family = DeficiencyKernelFamily(
            dirichlet_energy_metric(7, 0.8),
            0.8,
            PROBES,
            basis_kind="dirichlet-sine",
        )
        diagnostic = evaluate_shift_pair(
            family,
            family,
            0.0,
            -1.0,
            train_indices=[0, 2, 4, 5],
            holdout_indices=[1, 3, 6],
        )
        self.assertGreater(diagnostic.full.gauge_residual_rms, 1e-3)
        self.assertGreater(diagnostic.full.magnitude_max, 1e-3)

    def test_tuning_reports_held_out_failure_for_different_radius(self) -> None:
        metric = diagonal_coercive_metric(7)
        reference = DeficiencyKernelFamily(metric, 0.55, PROBES)
        target = DeficiencyKernelFamily(metric, 0.9, PROBES)
        diagnostic = tune_target_shift(
            reference,
            target,
            reference_shift=-0.25,
            shift_min=-3.0,
            shift_max=-0.01,
            train_indices=[0, 2, 4, 5],
            holdout_indices=[1, 3, 6],
            grid_size=33,
        )
        self.assertTrue(-3.0 <= diagnostic.target_shift <= -0.01)
        self.assertGreater(diagnostic.holdout.gauge_residual_rms, 1e-3)
        self.assertGreater(diagnostic.holdout.magnitude_max, 1e-3)
        self.assertGreater(diagnostic.full.gauge_residual_rms, 1e-3)

    def test_invalid_shift_interval_is_rejected(self) -> None:
        family = DeficiencyKernelFamily(
            scalar_coercive_metric(7, value=2.0), 0.8, PROBES
        )
        with self.assertRaises(ValueError):
            tune_target_shift(
                family,
                family,
                reference_shift=0.0,
                shift_min=-1.0,
                shift_max=2.0,
                train_indices=[0, 2, 4, 5],
                holdout_indices=[1, 3, 6],
            )


if __name__ == "__main__":
    unittest.main()
