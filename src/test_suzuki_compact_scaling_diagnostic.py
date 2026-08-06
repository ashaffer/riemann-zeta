import unittest

import numpy as np

from shift_phase_covariance_falsifier import (
    ShiftedCharacteristic,
    dirichlet_energy_metric,
    scalar_coercive_metric,
)
from suzuki_compact_scaling_diagnostic import (
    analyze_characteristic_on_compacts,
    near_floor_shift,
)


class SuzukiCompactScalingDiagnosticTest(unittest.TestCase):
    def test_near_floor_shift_is_admissible_and_conditioned(self) -> None:
        metric = np.diag([2.0, 5.0, 11.0])
        shift = near_floor_shift(metric, target_condition=1.0e4)
        self.assertLess(shift, 2.0)
        condition = np.linalg.cond(metric - shift * np.eye(3))
        self.assertAlmostEqual(condition, 1.0e4, delta=2.0)

    def test_scalar_control_has_weyl_scale_and_positive_clark_weights(self) -> None:
        support = 3.0
        characteristic = ShiftedCharacteristic(
            scalar_coercive_metric(6), support / 4.0, -0.25
        )
        rows = analyze_characteristic_on_compacts(
            characteristic=characteristic,
            model="scalar-test",
            diagnostic_scope="test control",
            support=support,
            shift_role="fixed",
            heights=[20.0, 40.0],
            samples=6001,
            continuum_safe=False,
            continuum_safety_scope="test",
        )
        self.assertEqual(len(rows), 2)
        for row in rows:
            self.assertAlmostEqual(
                row.delta_phi_over_support_height, 0.5, delta=0.02
            )
            self.assertEqual(row.nonpositive_root_phase_derivative_count, 0)
            self.assertGreater(row.positive_clark_weight_minimum, 0.0)
            self.assertGreaterEqual(row.theta_zero_root_count, 1)

    def test_dirichlet_control_is_analyzed_on_nested_compacts(self) -> None:
        support = 2.0
        radius = support / 4.0
        metric = dirichlet_energy_metric(6, radius)
        characteristic = ShiftedCharacteristic(
            metric, radius, -0.25, basis_kind="dirichlet-sine"
        )
        rows = analyze_characteristic_on_compacts(
            characteristic=characteristic,
            model="dirichlet-test",
            diagnostic_scope="test control",
            support=support,
            shift_role="fixed",
            heights=[15.0, 30.0],
            samples=5001,
            continuum_safe=False,
            continuum_safety_scope="test",
        )
        self.assertLessEqual(
            rows[0].theta_zero_root_count, rows[1].theta_zero_root_count
        )
        self.assertEqual(rows[1].nonpositive_root_phase_derivative_count, 0)
        self.assertTrue(np.isfinite(rows[1].positive_clark_weight_median))

    def test_invalid_compact_ladder_is_rejected(self) -> None:
        characteristic = ShiftedCharacteristic(
            scalar_coercive_metric(4), radius=0.5, shift=-0.25
        )
        with self.assertRaises(ValueError):
            analyze_characteristic_on_compacts(
                characteristic=characteristic,
                model="test",
                diagnostic_scope="test",
                support=2.0,
                shift_role="fixed",
                heights=[20.0, 10.0],
                samples=2001,
                continuum_safe=False,
                continuum_safety_scope="test",
            )


if __name__ == "__main__":
    unittest.main()
