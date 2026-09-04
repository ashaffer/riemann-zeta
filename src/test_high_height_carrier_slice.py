import math
import unittest

import numpy as np
from scipy.integrate import quad
from scipy.special import digamma

from high_height_carrier_slice import (
    archimedean_matrix_sign,
    build_fixture,
    prime_powers,
    rational_pole_matrix_sign,
)


class HighHeightCarrierSliceTest(unittest.TestCase):
    def test_archimedean_closed_form_matches_physical_kernel(self) -> None:
        length = 3.0
        tau = np.array([10.0, 10.0 + 2.0 * math.pi / length])
        matrix = archimedean_matrix_sign(tau, length)
        kernel = lambda u: math.exp(-u / 2.0) / (-math.expm1(-2.0 * u))
        tail = sum(
            math.exp(-(2.0 * n + 0.5) * length) / (2.0 * n + 0.5)
            for n in range(100)
        )
        constant = float(digamma(0.25).real - math.log(math.pi))
        diagonal = (
            constant * length
            + 2.0 * quad(
                lambda u: (
                    length - (length - u) * math.cos(tau[0] * u)
                ) * kernel(u),
                0.0,
                length,
                epsabs=1e-11,
                limit=1000,
            )[0]
            + 2.0 * length * tail
        )
        shifted = quad(
            lambda u: (
                (math.sin(tau[1] * u) - math.sin(tau[0] * u))
                / (tau[0] - tau[1])
            ) * kernel(u),
            0.0,
            length,
            epsabs=1e-11,
            limit=1000,
        )[0]
        self.assertAlmostEqual(matrix[0, 0], diagonal, places=10)
        self.assertAlmostEqual(matrix[0, 1], -2.0 * shifted, places=10)

    def test_actual_von_mangoldt_atoms_include_prime_powers(self) -> None:
        logs, weights = prime_powers(16)
        atoms = {
            round(math.exp(float(log_value))): float(weight)
            for log_value, weight in zip(logs, weights)
        }
        self.assertAlmostEqual(atoms[2], math.log(2) / math.sqrt(2))
        self.assertAlmostEqual(atoms[4], math.log(2) / 2)
        self.assertAlmostEqual(atoms[8], math.log(2) / math.sqrt(8))
        self.assertAlmostEqual(atoms[9], math.log(3) / 3)

    def test_rational_pole_matrix_is_positive(self) -> None:
        length = 3.0
        tau = 10.0 + 2.0 * math.pi / length * np.arange(-2, 3)
        matrix = rational_pole_matrix_sign(tau, length)
        self.assertGreater(np.linalg.eigvalsh(matrix)[0], 0.0)

    def test_small_fixture_normalizations_and_completion(self) -> None:
        result = build_fixture(32.0)
        checks = result["checks"]
        self.assertLess(checks["endpoint_moment_residual"], 1e-10)
        self.assertLess(checks["selected_positive_row_residual"], 1e-10)
        self.assertLess(checks["selected_pair_equals_minus_N_residual"], 1e-10)
        self.assertLess(checks["completed_centered_decomposition_residual"], 1e-10)
        self.assertLess(checks["carrier_lambda_max_residual"], 1e-10)
        self.assertLess(checks["full_carrier_q_identity_residual"], 1e-10)
        self.assertLess(
            checks["full_carrier_baseline_identity_residual"], 1e-10
        )
        self.assertGreaterEqual(
            checks["baseline_sandwich_min_lower_margin"], -1e-10
        )
        self.assertGreaterEqual(
            checks["baseline_sandwich_min_upper_margin"], -1e-10
        )
        self.assertGreaterEqual(result["rational_matrix_lambda_min"], -1e-10)
        self.assertFalse(result["candidate_is_asserted_zero"])

    def test_target_subtracted_support_obeys_baseline_sandwich(self) -> None:
        result = build_fixture(32.0)
        kappa = result["kappa_selected"]
        for row in result["q_and_baseline_diagnostics"]:
            q_value = row["q_eta_direct_arithmetic"]
            h_value = row["h_eta_target_subtracted"]
            eta = row["eta"]
            self.assertGreaterEqual(h_value + 1e-9, q_value + eta)
            self.assertLessEqual(h_value, q_value + kappa + 1e-9)


if __name__ == "__main__":
    unittest.main()
