#!/usr/bin/env python3

import math
import unittest

from qp_exceptional_translated_ap_audit import (
    FIRST_HARMONIC_SIGN_MARGIN,
    all_remote_uniform_template,
    first_harmonic_template,
    generic_r0_exponential_term_lower,
    negative_packet_mass_lower,
    positive_harmonic_template,
    singular_r0_certificate,
    two_frequency_kronecker_return,
)


class QPExceptionalTranslatedAPAuditTests(unittest.TestCase):
    def test_explicit_positive_first_harmonic_templates(self) -> None:
        for degree in (2, 3, 5, 8, 12):
            item = first_harmonic_template(degree)
            self.assertEqual(item.root_count, degree)
            self.assertGreater(item.minimum_root, -1.0)
            self.assertLess(item.maximum_root, 1.0)
            self.assertGreater(item.minimum_chebyshev_coefficient, 0.0)
            self.assertGreater(item.normalized_depth, 0.45)
            self.assertGreater(item.minimum_probability_weight, 0.0)
            self.assertLess(item.interpolation_residual, 1e-10)
            self.assertLess(item.nodal_ratio_error, 1e-10)
            self.assertGreater(abs(item.augmented_determinant), 1e-8)
            self.assertLess(item.perturbation_l1, FIRST_HARMONIC_SIGN_MARGIN / 4.0)

    def test_any_harmonic_block_has_an_interior_positive_template(self) -> None:
        for indices in ([1, 2, 3], [3, 4, 5], [5, 6, 7, 8], [1, 3, 7]):
            item = positive_harmonic_template(indices)
            self.assertEqual(item.harmonic_indices, sorted(indices))
            self.assertGreater(item.minimum_weight, 0.0)
            self.assertGreater(item.solved_depth, 0.49)
            self.assertLess(item.interpolation_residual, 1e-10)
            self.assertGreater(abs(item.augmented_determinant), 1e-8)

    def test_all_remote_block_has_uniform_inverse_degree_perturbation(self) -> None:
        for degree in (2, 3, 5, 8, 12):
            item = all_remote_uniform_template(degree, constant=0.05)
            self.assertEqual(item.harmonic_indices, list(range(degree, 2 * degree)))
            self.assertAlmostEqual(item.epsilon * degree, 0.05)
            self.assertGreater(item.minimum_weight, 0.0)
            self.assertGreater(item.solved_depth, 0.47)
            self.assertLess(item.interpolation_residual, 1e-10)
            self.assertGreater(abs(item.augmented_determinant), 1e-8)

    def test_singular_r0_is_inconsistent_and_nearby_cost_blows_up(self) -> None:
        coarse = singular_r0_certificate(1e-2)
        fine = singular_r0_certificate(1e-6)
        self.assertEqual(coarse.singular_matrix_rank, 1)
        self.assertEqual(coarse.singular_augmented_rank, 2)
        self.assertGreater(coarse.singular_least_squares_residual, 1.0)
        self.assertGreater(fine.directional_cost, 1000.0 * coarse.directional_cost)
        self.assertLess(fine.positive_depth, coarse.positive_depth / 1000.0)
        self.assertGreater(fine.r0, 0.0)
        self.assertGreater(fine.r1, 0.0)
        self.assertAlmostEqual(fine.r2, 0.5, places=12)

    def test_negative_packet_mass_ledger(self) -> None:
        self.assertAlmostEqual(negative_packet_mass_lower(0.5), 1.0 / 3.0)
        self.assertAlmostEqual(negative_packet_mass_lower(0.1), 0.1 / 1.9)

    def test_turan_order_is_exponential_in_node_count(self) -> None:
        self.assertEqual(generic_r0_exponential_term_lower(1), 2)
        self.assertEqual(generic_r0_exponential_term_lower(10), 1024)

    def test_toy_kronecker_return_enters_positive_chamber(self) -> None:
        item = two_frequency_kronecker_return(20000)
        self.assertGreater(item.tau, 1000.0)
        self.assertLess(item.circular_phase_error, 1e-4)
        self.assertGreater(item.minimum_weight, 0.0)
        self.assertGreater(item.solved_depth, 0.45)
        self.assertLess(item.interpolation_residual, 1e-12)


if __name__ == "__main__":
    unittest.main()
