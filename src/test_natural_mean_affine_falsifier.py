#!/usr/bin/env python3

import unittest

from natural_mean_affine_falsifier import (
    analyze_affine_ibp,
    analyze_affine_profiles,
    analyze_carrier_split,
    analyze_natural_centering,
    analyze_reciprocal_derivative_transfer,
)


class NaturalMeanAffineFalsifierTests(unittest.TestCase):
    def test_natural_prime_unit_mean_and_norm_formulas(self) -> None:
        result = analyze_natural_centering(11, 3)
        self.assertEqual(result.ramanujan_sum, -1)
        self.assertAlmostEqual(result.predicted_mean.real, -0.1)
        self.assertLess(result.mean_error, 1.0e-14)
        self.assertLess(result.centered_sum_error, 1.0e-13)
        self.assertAlmostEqual(result.raw_shift_norm_squared, 22.0, places=12)
        self.assertAlmostEqual(result.centered_norm_squared, 9.9, places=12)
        self.assertAlmostEqual(
            result.raw_shift_norm_squared,
            result.raw_shift_norm_squared_formula,
            places=12,
        )
        self.assertAlmostEqual(
            result.centered_norm_squared,
            result.centered_norm_squared_formula,
            places=12,
        )

    def test_divisible_frequency_is_the_constant_axis(self) -> None:
        result = analyze_natural_centering(11, 22)
        self.assertEqual(result.ramanujan_sum, 10)
        self.assertAlmostEqual(result.predicted_mean.real, 1.0)
        self.assertLess(result.raw_shift_norm_squared, 1.0e-25)
        self.assertLess(result.centered_norm_squared, 1.0e-25)

    def test_random_complex_carrier_split_is_exact(self) -> None:
        result = analyze_carrier_split(13, 5)
        self.assertLess(result.maximum_split_error, 2.0e-15)
        self.assertLess(result.centered_phase_sum_error, 2.0e-13)
        self.assertGreater(result.residual_carrier_norm, 0.0)

    def test_affine_factor_is_exactly_a_cutoff_derivative(self) -> None:
        result = analyze_affine_ibp()
        self.assertLess(result.relative_identity_error, 2.0e-13)
        self.assertLess(result.refinement_error, 2.0e-13)

    def test_reciprocal_derivative_transfer_preserves_natural_projection(self) -> None:
        result = analyze_reciprocal_derivative_transfer()
        self.assertLess(result.transfer_error, 2.0e-15)
        self.assertLess(result.centered_interpolation_error, 2.0e-15)
        self.assertLess(result.invariant_projection_error, 2.0e-15)
        self.assertAlmostEqual(result.coefficient_amplification, 10.0, places=12)

    def test_fixed_affine_profile_fails_two_finite_stress_tests(self) -> None:
        canonical, adversarial = analyze_affine_profiles()
        self.assertGreater(canonical.relative_l2_residual, 0.9)
        self.assertGreater(adversarial.relative_l2_residual, 0.98)
        self.assertGreater(canonical.relative_linf_residual, 0.9)
        self.assertGreater(adversarial.relative_linf_residual, 0.9)


if __name__ == "__main__":
    unittest.main()
