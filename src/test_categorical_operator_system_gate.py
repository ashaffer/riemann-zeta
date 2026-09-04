import math
import unittest

import numpy as np
import sympy as sp

from categorical_operator_system_gate import (
    I2,
    J2,
    Z2,
    asymmetric_observation_matrix,
    block_dephasing_covariance,
    cross_aware_unitary,
    exact_normalized_prime2_form,
    exact_prime2_coefficient,
    exact_prime2_form,
    exact_support_contrast_scale,
    exact_two_hat_gram,
    finite_scalar_counterexample,
    four_scalar_counterexample,
    mirror_observation_matrix,
    numerical_place_fixture,
    normalized_block_covariance,
    parity_vectors,
    symmetry_recovery_block_choi,
    symmetry_recovery_effects,
    unitary_recovery_choi,
    vector_expectation,
)


class CategoricalOperatorSystemGateTest(unittest.TestCase):
    def test_exact_two_hat_arithmetic_fixture_generates_mirror_system(self) -> None:
        gram = exact_two_hat_gram()
        self.assertEqual(gram, sp.Rational(7, 144) * (4 * I2 + J2))
        prime = exact_prime2_form()
        self.assertEqual(prime[0, 0], 0)
        self.assertEqual(prime[1, 1], 0)
        self.assertGreater(float(sp.N(prime[0, 1])), 0.0)
        self.assertEqual(prime[0, 1], exact_prime2_coefficient())
        normalized = exact_normalized_prime2_form()
        self.assertNotEqual(sp.simplify(normalized[0, 1]), 0)
        self.assertEqual(sp.simplify(normalized[0, 0] - normalized[1, 1]), 0)

    def test_support_contrast_is_nonzero_and_zero_independent(self) -> None:
        self.assertEqual(exact_support_contrast_scale(), sp.sqrt(15) / 4)
        self.assertNotEqual(exact_support_contrast_scale(), 0)

        # Derive the claimed scale from the exact Gram metric rather than
        # merely checking the closed-form helper against its own constant.
        gram = exact_two_hat_gram()
        plus, minus = parity_vectors()
        p_plus = plus * plus.T
        p_minus = minus * minus.T
        sqrt_gram = sp.sqrt(sp.Rational(35, 144)) * p_plus + sp.sqrt(
            sp.Rational(21, 144)
        ) * p_minus
        e1 = sp.Matrix([1, 0])
        e2 = sp.Matrix([0, 1])
        left = sp.simplify(sqrt_gram * e1 / sp.sqrt(gram[0, 0]))
        right = sp.simplify(sqrt_gram * e2 / sp.sqrt(gram[1, 1]))
        contrast = sp.simplify(left * left.T - right * right.T)
        self.assertEqual(
            sp.simplify(contrast - exact_support_contrast_scale() * Z2),
            sp.zeros(2),
        )

    def test_coordinate_probes_fail_on_the_mirror_system(self) -> None:
        e1 = sp.Matrix([1, 0])
        e2 = sp.Matrix([0, 1])
        observation = mirror_observation_matrix((e1, e2))
        self.assertEqual(observation.rank(), 1)
        self.assertEqual(observation * sp.Matrix([0, 1]), sp.zeros(2, 1))
        self.assertEqual(J2.det(), -1)

    def test_parity_probes_have_an_exact_cp_recovery(self) -> None:
        plus, minus = parity_vectors()
        observation = mirror_observation_matrix((plus, minus))
        self.assertEqual(observation, sp.Matrix([[1, 1], [1, -1]]))
        effects = symmetry_recovery_effects()
        self.assertEqual(effects[0] + effects[1], I2)
        for effect in effects:
            self.assertEqual(effect * effect, effect)
            self.assertEqual(effect.T, effect)
        self.assertEqual(effects[0] - effects[1], J2)
        choi = symmetry_recovery_block_choi()
        self.assertEqual(sorted(choi.eigenvals().keys()), [0, 1])

    def test_four_natural_scalar_probes_are_injective_but_not_order_reflecting(self) -> None:
        e1 = sp.Matrix([1, 0])
        e2 = sp.Matrix([0, 1])
        plus, minus = parity_vectors()
        probes = (e1, e2, plus, minus)
        observation = asymmetric_observation_matrix(probes)
        self.assertEqual(observation.rank(), 3)
        witness = four_scalar_counterexample()
        eigenvalues = witness.eigenvals()
        self.assertIn(sp.Rational(-1, 8), eigenvalues)
        self.assertIn(sp.Rational(1), eigenvalues)
        exact_minimum = (sp.Integer(14) - 9 * sp.sqrt(2)) / 32
        self.assertGreater(float(exact_minimum), 0.0)
        for probe in probes:
            self.assertGreaterEqual(
                float(sp.N(vector_expectation(witness, probe))),
                float(sp.N(exact_minimum)) - 1e-14,
            )

    def test_constructive_finite_scalar_no_go(self) -> None:
        angles = [0.0, math.pi / 7.0, math.pi / 3.0, 0.9 * math.pi]
        witness = finite_scalar_counterexample(angles)
        self.assertLess(np.linalg.eigvalsh(witness)[0], 0.0)
        for angle in angles:
            vector = np.array([math.cos(angle), math.sin(angle)])
            self.assertGreater(float(vector @ witness @ vector), -1e-13)

    def test_full_pair_matrix_probe_has_unitary_cp_recovery(self) -> None:
        unitary = cross_aware_unitary()
        self.assertEqual(sp.simplify(unitary.T * unitary), I2)
        for basis in (I2, J2, Z2):
            observed = sp.simplify(unitary.T * basis * unitary)
            recovered = sp.simplify(unitary * observed * unitary.T)
            self.assertEqual(recovered, basis)
        choi = unitary_recovery_choi()
        eigenvalues = choi.eigenvals()
        self.assertEqual(eigenvalues.get(sp.Integer(0)), 3)
        self.assertEqual(eigenvalues.get(sp.Integer(2)), 1)

    def test_low_cost_numeric_place_assembly_has_mirror_symmetry(self) -> None:
        fixture = numerical_place_fixture(cutoff=40.0, intervals=2000)
        for matrix in (fixture.normalized_gamma,
                       fixture.normalized_pole,
                       fixture.normalized_prime2):
            self.assertLess(abs(matrix[0, 0] - matrix[1, 1]), 1e-11)
            self.assertLess(abs(matrix[0, 1] - matrix[1, 0]), 1e-11)
        self.assertGreater(abs(fixture.normalized_prime2[0, 1]), 1e-8)

    def test_block_dephasing_covariance_is_exactly_cross_coupling(self) -> None:
        left = np.array([[2.0, 0.25], [0.25, 1.5]])
        right = np.array([[1.25]])
        cross = np.array([[0.3], [-0.2]])
        matrix = np.block([[left, cross], [cross.T, right]])
        covariance = block_dephasing_covariance(matrix, 2)
        expected = np.block([
            [cross @ cross.T, np.zeros((2, 1))],
            [np.zeros((1, 2)), cross.T @ cross],
        ])
        np.testing.assert_allclose(covariance, expected, atol=2e-15)

        normalized = normalized_block_covariance(left, cross, right)
        self.assertLess(float(normalized["norm_identity_error"]), 2e-15)
        self.assertAlmostEqual(
            float(normalized["covariance_norm"]),
            float(normalized["coupling"]) ** 2,
            places=14,
        )


if __name__ == "__main__":
    unittest.main()
