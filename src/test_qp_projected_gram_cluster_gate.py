#!/usr/bin/env python3

import math
import unittest

import numpy as np

from qp_projected_gram_cluster_gate import (
    SHELL_WIDTH,
    alternating_binomial,
    asymptotic_cluster_rate,
    carrier_residual_dual,
    central_binomial,
    cluster_rayleigh_upper_bound,
    cosine_atoms,
    critical_packet_slice,
    critical_regular_hadamard,
    gate_ledger,
    guth_maynard_count_exponents,
    log_relative_cluster_bound,
    next_packet_distance_bound,
    projected_dictionary,
    zero_center_source_condition,
)


class QPProjectedGramClusterGateTests(unittest.TestCase):
    def setUp(self) -> None:
        # A deterministic irregular shell fixture; primality is irrelevant to
        # the universal cluster inequality.
        self.nodes = np.asarray([0.013, 0.037, 0.071, 0.109, 0.143, 0.181, 0.197])

    def test_central_binomial_identity(self) -> None:
        for order in range(1, 12):
            coefficients = alternating_binomial(order)
            self.assertEqual(round(float(coefficients @ coefficients)), central_binomial(order))

    def test_binomial_difference_identity_and_rayleigh_bound(self) -> None:
        order = 5
        t0 = 43.25
        times = t0 + np.arange(order + 1)
        matrix, projected = projected_dictionary(self.nodes, times)
        coefficients = alternating_binomial(order)
        direct = matrix @ coefficients
        complex_difference = np.real(
            np.exp(1j * t0 * self.nodes) * (np.exp(1j * self.nodes) - 1.0) ** order
        )
        self.assertLess(float(np.max(np.abs(direct - complex_difference))), 2e-12)

        gram = projected.T @ projected
        rayleigh = float(coefficients @ gram @ coefficients / (coefficients @ coefficients))
        theorem_bound = cluster_rayleigh_upper_bound(len(self.nodes), order)
        self.assertLessEqual(rayleigh, theorem_bound * (1.0 + 1e-9))
        self.assertLessEqual(float(np.linalg.eigvalsh(gram)[0]), rayleigh + 1e-12)

    def test_log_bound_matches_direct_formula(self) -> None:
        for order in (1, 4, 12, 32):
            direct = cluster_rayleigh_upper_bound(1, order)
            self.assertAlmostEqual(math.log(direct), log_relative_cluster_bound(order), places=12)

    def test_fixed_width_rate(self) -> None:
        self.assertAlmostEqual(asymptotic_cluster_rate(), 4.608504631138533, places=14)
        ledger = gate_ledger()
        self.assertAlmostEqual(ledger.allowed_packet_exponent, 0.038, places=15)
        self.assertLess(ledger.relative_log_bound_order_32, ledger.relative_log_bound_order_8)

    def test_guth_maynard_substitution_is_count_only(self) -> None:
        first, second, third = guth_maynard_count_exponents()
        self.assertAlmostEqual(first, 0.038, places=15)
        self.assertAlmostEqual(second, -0.324, places=15)
        self.assertAlmostEqual(third, -0.00884848484848485, places=15)
        self.assertLess(second, 0.0)
        self.assertLess(third, 0.0)

    def test_critical_count_and_orthogonality_do_not_bound_leverage(self) -> None:
        matrix = critical_packet_slice(2)
        dimension, packet_count = matrix.shape
        epsilon = packet_count ** -0.5
        q = np.ones(dimension)
        self.assertTrue(np.array_equal(matrix.T @ matrix, dimension * np.eye(packet_count)))
        self.assertTrue(np.allclose(matrix.T @ q / dimension, -epsilon))
        coefficients = -np.ones(packet_count) / math.sqrt(packet_count)
        self.assertTrue(np.array_equal(matrix @ coefficients, q))
        self.assertTrue(np.array_equal(matrix @ (np.ones(packet_count) / packet_count), -epsilon * q))
        self.assertAlmostEqual(packet_count * epsilon**2, 1.0, places=15)
        projected = matrix - np.outer(q, matrix.T @ q) / dimension
        self.assertLess(float(np.linalg.eigvalsh(projected.T @ projected)[0]), 1e-12)

    def test_regular_hadamard_countermodel_has_linear_row_count(self) -> None:
        matrix = critical_regular_hadamard(power=2, repeats=3)
        dimension, packet_count = matrix.shape
        epsilon = packet_count ** -0.5
        q = np.ones(dimension)
        self.assertEqual(packet_count, 16)
        self.assertEqual(dimension, 48)
        self.assertTrue(np.array_equal(matrix.T @ matrix, dimension * np.eye(packet_count)))
        self.assertTrue(np.allclose(matrix.T @ q / dimension, -epsilon))
        self.assertTrue(np.allclose(matrix @ (np.ones(packet_count) / packet_count), -epsilon * q))

    def test_source_schur_and_variational_identities(self) -> None:
        matrix = cosine_atoms(self.nodes, [31.0, 47.0, 79.0])
        source = zero_center_source_condition(matrix)
        residual = carrier_residual_dual(matrix)
        self.assertLess(source.maximum_center_residual, 2e-12)
        self.assertLess(source.carrier_normalization_residual, 2e-12)
        self.assertAlmostEqual(source.source_energy, source.source_from_leverage, places=11)
        self.assertAlmostEqual(source.source_energy, source.variational_probe, places=11)
        self.assertAlmostEqual(
            source.zeroing_norm_square,
            1.0 / len(self.nodes) + source.source_energy,
            places=12,
        )
        self.assertGreaterEqual(source.carrier_leverage, 0.0)
        self.assertLess(source.carrier_leverage, 1.0)
        self.assertAlmostEqual(source.carrier_leverage, residual.carrier_leverage, places=11)
        self.assertAlmostEqual(source.zeroing_norm_square, residual.dual_norm_square, places=11)
        self.assertLess(residual.maximum_center_residual, 2e-12)
        self.assertLess(residual.carrier_normalization_residual, 2e-12)

        # The full-band dual inequality is exactly the residual antenna.
        query = cosine_atoms(self.nodes, [113.0])[:, 0]
        dual_value = float(np.asarray(residual.dual) @ query)
        residual_ratio = -float(np.asarray(residual.residual) @ query) / residual.residual_norm_square
        self.assertAlmostEqual(dual_value, residual_ratio, places=13)

    def test_next_packet_distance_bound(self) -> None:
        packet_count = 4
        t0 = 83.0
        centers = t0 + np.arange(packet_count)
        query = t0 + packet_count
        _, projected_centers = projected_dictionary(self.nodes, centers)
        _, projected_query_matrix = projected_dictionary(self.nodes, [query])
        projected_query = projected_query_matrix[:, 0]
        coefficients = np.linalg.lstsq(projected_centers, projected_query, rcond=None)[0]
        distance = float(np.linalg.norm(projected_query - projected_centers @ coefficients))
        self.assertLessEqual(
            distance,
            next_packet_distance_bound(len(self.nodes), packet_count) * (1.0 + 1e-10),
        )

    def test_shell_constant_is_small_arc(self) -> None:
        self.assertLess(SHELL_WIDTH, math.pi)


if __name__ == "__main__":
    unittest.main()
