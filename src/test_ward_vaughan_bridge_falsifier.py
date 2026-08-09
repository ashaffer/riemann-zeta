import unittest
from fractions import Fraction

from ward_vaughan_bridge_falsifier import (
    Quadratic,
    binary_macro_audit,
    global_covariance_sign_audit,
    higher_ward_cutoff_audit,
    prime_power_audit,
    scale_fiber_audit,
    semiprime_polynomial_audit,
)


class WardVaughanBridgeFalsifierTests(unittest.TestCase):
    def test_semiprime_assignment_cross_has_only_one_ward_copy(self) -> None:
        audit = semiprime_polynomial_audit()
        self.assertEqual(audit.assignment_cross, audit.lambda_convolution)
        self.assertEqual(
            audit.ward_connected,
            audit.lambda_convolution.scale(2),
        )
        self.assertNotEqual(audit.assignment_cross, audit.ward_connected)
        self.assertEqual(
            audit.tail_square - audit.ward_connected,
            audit.anisotropy,
        )
        # The missing second connected copy is obtained only by
        # reclassifying the assignment self-squares.
        self.assertEqual(
            audit.assignment_self,
            audit.lambda_convolution + audit.anisotropy,
        )

    def test_factor_swap_innovation_is_anisotropic(self) -> None:
        audit = semiprime_polynomial_audit()
        self.assertEqual(
            audit.swap_innovation,
            Quadratic(Fraction(1, 4), Fraction(-1, 2), Fraction(1, 4)),
        )
        self.assertEqual(
            audit.swap_retained,
            Quadratic(Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)),
        )

    def test_terminal_macro_does_not_leave_only_anisotropy(self) -> None:
        audit = binary_macro_audit()
        self.assertEqual(
            audit.raw_diagonal - audit.subtracted_innovation,
            audit.retained_diagonal,
        )
        self.assertEqual(
            audit.retained_diagonal,
            Quadratic(Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)),
        )
        self.assertEqual(
            audit.retained_connected,
            Quadratic(0, 1, 0),
        )
        self.assertNotEqual(audit.retained_connected, Quadratic(0, 0, 0))

    def test_global_remainder_has_no_sign_from_psd_and_ward(self) -> None:
        aligned = global_covariance_sign_audit(correlation=1)
        orthogonal = global_covariance_sign_audit(correlation=0)
        self.assertEqual(aligned.gram_determinant, 0)
        self.assertEqual(orthogonal.gram_determinant, 1)
        self.assertEqual(aligned.completed_energy, 0)
        self.assertLess(aligned.global_remainder, 0)
        self.assertGreater(orthogonal.global_remainder, 0)
        self.assertLess(aligned.ward_renormalized_remainder, 0)
        self.assertGreater(orthogonal.ward_renormalized_remainder, 0)

    def test_exact_type_i_head_cancels_whole_semiprime_fiber(self) -> None:
        audit = semiprime_polynomial_audit()
        self.assertEqual(audit.exact_full_square, Quadratic(0, 0, 0))
        self.assertEqual(
            audit.fixed_fiber_center_quadratic,
            Quadratic(0, 0, 0),
        )

    def test_scale_markov_operator_is_rank_one_on_product_fiber(self) -> None:
        audit = scale_fiber_audit()
        self.assertGreaterEqual(audit.minimum_kernel, -2.0e-16)
        self.assertLess(audit.grouped_rank_one_error, 2.0e-14)
        self.assertLess(audit.natural_cross_error, 2.0e-14)
        self.assertGreater(audit.missing_connected_copy, 0.01)
        self.assertLess(audit.exact_head_completion_error, 1.0e-30)

    def test_prime_square_companion_breaks_positive_anisotropy_remainder(self) -> None:
        audit = prime_power_audit(2)
        self.assertEqual(
            audit.ward_sum_coefficient,
            audit.mobius_log_square_coefficient,
        )
        self.assertEqual(audit.lambda_log_coefficient, 2)
        self.assertEqual(audit.lambda_convolution_coefficient, 1)
        self.assertEqual(audit.residual_after_twice_connected, -1)

    def test_triple_higher_ward_term_survives_exact_tail_cancellation(self) -> None:
        audit = higher_ward_cutoff_audit((2, 11, 13), 10)
        self.assertEqual(audit.tail_log_multiplicities, (0, 0, 0))
        self.assertEqual(audit.tail_coefficient, 0.0)
        self.assertEqual(audit.ward_product_multiplier, 6)
        self.assertGreater(audit.ward_coefficient, 0.0)
        self.assertGreater(audit.amgm_connected, 0.0)
        self.assertLess(audit.remainder, 0.0)

    def test_quad_higher_ward_term_survives_exact_tail_cancellation(self) -> None:
        audit = higher_ward_cutoff_audit((2, 3, 11, 13), 10)
        self.assertEqual(audit.tail_log_multiplicities, (0, 0, 0, 0))
        self.assertEqual(audit.tail_coefficient, 0.0)
        self.assertEqual(audit.ward_product_multiplier, 24)
        self.assertGreater(audit.ward_coefficient, 0.0)
        self.assertGreater(audit.amgm_connected, 0.0)
        self.assertLess(audit.remainder, 0.0)

    def test_nonzero_triple_remainder_changes_sign(self) -> None:
        negative = higher_ward_cutoff_audit((2, 7, 11), 10)
        positive = higher_ward_cutoff_audit((2, 7, 1009), 10)
        self.assertEqual(negative.tail_log_multiplicities, (0, 0, 1))
        self.assertEqual(positive.tail_log_multiplicities, (0, 0, 1))
        self.assertLess(negative.remainder, 0.0)
        self.assertGreater(positive.remainder, 0.0)


if __name__ == "__main__":
    unittest.main()
