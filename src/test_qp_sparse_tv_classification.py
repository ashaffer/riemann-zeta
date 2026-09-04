#!/usr/bin/env python3
"""Tests for the cosine sparse/TV classification theorem ledger."""

from __future__ import annotations

import math
import unittest

import numpy as np
from scipy.optimize import linprog

from qp_sparse_tv_classification import (
    all_remote_extremal_chamber,
    basis_perturbation_ledger,
    classify_matrix,
    cosine_vandermonde_leading_constant,
    near_optimal_stability_bound,
    normalized_cosine_determinant,
    positive_depth_minimax,
)


class QPSparseTVClassificationTests(unittest.TestCase):
    def test_generalized_vandermonde_asymptotic(self) -> None:
        nodes = (0.4, 0.9, 1.6)
        frequencies = (0, 2, 5)
        predicted = cosine_vandermonde_leading_constant(nodes, frequencies)
        coarse = normalized_cosine_determinant(nodes, frequencies, 0.01)
        fine = normalized_cosine_determinant(nodes, frequencies, 0.005)
        self.assertLess(abs(fine - predicted), abs(coarse - predicted))
        self.assertLess(abs(fine / predicted - 1.0), 2.0e-3)

    def test_affine_independence_asymptotic_uses_zero_node(self) -> None:
        # Appending the row of ones is the same as appending the node u=0.
        nodes = (0.0, 0.3, 0.8, 1.4)
        frequencies = (1, 2, 4, 7)
        predicted = cosine_vandermonde_leading_constant(nodes, frequencies)
        replay = normalized_cosine_determinant(nodes, frequencies, 0.003)
        self.assertNotEqual(predicted, 0.0)
        self.assertLess(abs(replay / predicted - 1.0), 2.0e-3)

    def test_cramer_classification_matches_both_linear_programs(self) -> None:
        phases = np.asarray([0.88, 1.95])
        harmonics = tuple(range(1, 7))
        matrix = np.cos(np.outer(phases, harmonics))
        classification = classify_matrix(matrix, harmonics)
        self.assertTrue(classification.full_spark)
        self.assertTrue(classification.signed_unique)
        self.assertEqual(classification.signed_minimizing_supports, ((4, 6),))
        self.assertTrue(classification.positive_unique)
        self.assertEqual(classification.positive_minimizing_supports, ((4, 5),))

        rows, columns = matrix.shape
        signed_lp = linprog(
            np.ones(2 * columns),
            A_eq=np.column_stack([matrix, -matrix]),
            b_eq=np.ones(rows),
            bounds=[(0.0, None)] * (2 * columns),
            method="highs",
        )
        self.assertTrue(signed_lp.success)
        self.assertAlmostEqual(
            signed_lp.fun, classification.minimum_signed_cost, places=9
        )

        positive_lp = linprog(
            np.ones(columns),
            A_eq=-matrix,
            b_eq=np.ones(rows),
            bounds=[(0.0, None)] * columns,
            method="highs",
        )
        self.assertTrue(positive_lp.success)
        assert classification.minimum_positive_cost is not None
        self.assertAlmostEqual(
            positive_lp.fun, classification.minimum_positive_cost, places=9
        )

    def test_positive_depth_minimax_has_the_required_sign(self) -> None:
        phases = np.asarray([0.88, 1.95])
        harmonics = tuple(range(1, 7))
        matrix = np.cos(np.outer(phases, harmonics))
        classification = classify_matrix(matrix, harmonics)
        assert classification.maximum_positive_depth is not None
        self.assertAlmostEqual(
            positive_depth_minimax(matrix),
            classification.maximum_positive_depth,
            places=9,
        )

    def test_all_remote_chamber_is_unique_full_support(self) -> None:
        certificate = all_remote_extremal_chamber(5, constant=0.05)
        matrix = np.cos(np.outer(certificate.phases, certificate.harmonics))
        classification = classify_matrix(matrix, certificate.harmonics)
        self.assertTrue(classification.full_spark)
        self.assertTrue(classification.signed_unique)
        self.assertTrue(classification.positive_unique)
        self.assertEqual(
            classification.positive_minimizing_supports,
            (certificate.harmonics,),
        )
        self.assertAlmostEqual(
            classification.maximum_positive_depth, certificate.depth, places=9
        )
        self.assertGreater(certificate.depth, 1.0 / 2.1)
        self.assertLess(certificate.minimum_weight, 0.02)
        self.assertLess(certificate.residual, 1.0e-12)

    def test_dual_slack_stability_ledger(self) -> None:
        bound = near_optimal_stability_bound(
            objective_excess=0.003,
            dual_slack=0.2,
            inverse_infinity_norm=3.0,
            support_size=2,
        )
        self.assertAlmostEqual(bound.off_support_l1_upper, 0.015)
        self.assertAlmostEqual(bound.total_l1_distance_upper, 0.105)
        square_bound = near_optimal_stability_bound(0.003, math.inf, 3.0, 2)
        self.assertEqual(square_bound.off_support_l1_upper, 0.0)
        self.assertEqual(square_bound.total_l1_distance_upper, 0.0)
        with self.assertRaises(ValueError):
            near_optimal_stability_bound(0.1, 0.0, 1.0, 2)

        perturbation = basis_perturbation_ledger(
            phase_radius=1.0e-5,
            top_harmonic=10,
            support_size=4,
            maximum_inverse_infinity_norm=2.0,
            maximum_coefficient_infinity_norm=3.0,
        )
        self.assertAlmostEqual(perturbation.neumann_product, 0.0008)
        self.assertAlmostEqual(
            perturbation.coefficient_infinity_shift_upper, 0.0048
        )


if __name__ == "__main__":
    unittest.main()
