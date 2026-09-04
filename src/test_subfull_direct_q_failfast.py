import math
import unittest

import numpy as np
from scipy.linalg import eigh

from high_height_carrier_slice import selected_rows_sign
from subfull_direct_q_failfast import (
    _exact_endpoint_kernel,
    adversarial_scan,
    build_floating_base,
    build_rigorous_fixture_forms,
    certify_negative_dual,
    certify_full_carrier_sign,
    evaluate_floating_point,
    selected_rows_with_phase,
)


class SubfullDirectQFailfastTest(unittest.TestCase):
    def test_phase_zero_row_is_the_established_centered_row(self) -> None:
        length = math.log(32.0)
        gamma = 48.0
        indices = np.arange(-3, 4)
        tau = gamma + 2.0 * math.pi / length * indices
        expected_x, expected_y = selected_rows_sign(
            tau, gamma, length, 0.4
        )
        actual_x, actual_y = selected_rows_with_phase(
            tau, length, gamma, 0.4, 0.0
        )
        np.testing.assert_allclose(actual_x, expected_x, atol=1e-14)
        np.testing.assert_allclose(actual_y, expected_y, atol=1e-14)

    def test_exact_endpoint_kernel_annihilates_integer_moments(self) -> None:
        indices = list(range(-3, 4))
        basis = _exact_endpoint_kernel(indices, 3)
        for power in range(3):
            for column in range(basis.ncols()):
                value = sum(
                    (index ** power) * basis[row, column]
                    for row, index in enumerate(indices)
                )
                self.assertEqual(value, 0)

    def test_interval_replay_matches_floating_generalized_forms(self) -> None:
        floating_base = build_floating_base(
            16.0,
            gamma_fraction=1.31,
            aperture_fraction=0.32,
            grid_phase=0.49,
        )
        floating = evaluate_floating_point(
            floating_base, alpha=0.499, jet_order=1, theta=1.0
        )
        rigorous = build_rigorous_fixture_forms(
            16,
            gamma_fraction="131/100",
            aperture_fraction="8/25",
            grid_phase="49/100",
            alpha="499/1000",
            jet_order=1,
            bits=128,
        )

        def midpoint(matrix):
            return np.array([
                [
                    float(matrix[i, j].real.mid())
                    + 1j * float(matrix[i, j].imag.mid())
                    for j in range(matrix.ncols())
                ]
                for i in range(matrix.nrows())
            ])

        gram = midpoint(rigorous.gram)
        carrier = midpoint(rigorous.carrier_form)
        arithmetic = midpoint(rigorous.arithmetic_form)
        values, vectors = eigh(carrier, gram)
        direction = vectors[:, -1]
        q_full = float(np.vdot(direction, arithmetic @ direction).real)
        self.assertAlmostEqual(values[-1], floating["kappa"], places=12)
        self.assertAlmostEqual(q_full, floating["q_eta"], places=12)
        self.assertLess(
            float(rigorous.selected_null_residual_radius.upper()), 1e-30
        )
        full_sign = certify_full_carrier_sign(rigorous)
        self.assertEqual(full_sign["q_kappa_sign"], "strictly_positive")
        lower, upper = full_sign["q_kappa_interval"]
        self.assertAlmostEqual((lower + upper) / 2, floating["q_eta"], places=12)

    def test_interval_dual_rejects_false_claim_and_certifies_calibration(self) -> None:
        forms = build_rigorous_fixture_forms(
            16,
            gamma_fraction="131/100",
            aperture_fraction="8/25",
            grid_phase="49/100",
            alpha="499/1000",
            jet_order=1,
            bits=128,
        )
        actual = certify_negative_dual(
            forms, theta=1, mu=0, delta="1/1000"
        )
        shifted = certify_negative_dual(
            forms,
            theta=1,
            mu=0,
            delta="1/1000",
            arithmetic_shift=1,
        )
        self.assertFalse(actual["certified_negative_dual"])
        self.assertTrue(shifted["certified_negative_dual"])
        self.assertIn("calibration", shifted["scope"])

    def test_small_cartesian_scan_reports_every_axis(self) -> None:
        result = adversarial_scan(
            heights=[16.0],
            gamma_fractions=[1.31],
            grid_phases=[0.0, 0.49],
            aperture_fractions=[0.32],
            jet_orders=[1, 2],
            alphas=[0.4, 0.499],
            thetas=[0.9, 1.0],
            iterations=40,
        )
        self.assertEqual(result["base_count"], 2)
        self.assertEqual(result["point_count"], 16)
        self.assertEqual(len(result["minimum_by_theta"]), 2)
        self.assertEqual(result["negative_point_count_at_tolerance_1e-10"], 0)


if __name__ == "__main__":
    unittest.main()
