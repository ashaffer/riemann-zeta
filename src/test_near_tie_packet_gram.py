import unittest

import numpy as np

from near_tie_packet_gram import (
    branch_gram,
    collision_quadratic,
    gauss_packet,
    gram_determinant,
    hermite_row,
    interval_moment,
    mirror_cross_identity,
    normalized_correlation,
    packet_block_ratios,
    sampled_normalized_row,
)


class NearTiePacketGramTests(unittest.TestCase):
    def test_closed_moment_and_correlation_match_quadrature(self) -> None:
        width = 1.3
        nodes, weights = gauss_packet(width, 180)
        s = 0.37 + 0.81j
        numerical_moment = np.sum(weights * np.exp(s * nodes))
        self.assertAlmostEqual(abs(numerical_moment - interval_moment(s, width)), 0.0, places=13)

        parameters = (0.21, -0.7, 0.34, 0.4)
        row0 = sampled_normalized_row(parameters[0], parameters[1], width, 180)
        row1 = sampled_normalized_row(parameters[2], parameters[3], width, 180)
        numerical = np.sum(row0 * np.conj(row1))
        exact = normalized_correlation(*parameters, width)
        self.assertLess(abs(numerical - exact), 2.0e-14)

    def test_mean_depth_is_real_data_not_only_parameter_difference(self) -> None:
        width = 1.0
        # Same delta alpha and delta gamma, different mean depth.
        first = gram_determinant(0.10, -0.015, 0.14, 0.015, width)
        second = gram_determinant(0.36, -0.015, 0.40, 0.015, width)
        self.assertGreater(abs(first - second), 1.0e-7)

    def test_collision_determinant_has_variance_coefficient(self) -> None:
        mean_alpha = 0.28
        width = 1.4
        for epsilon in (2.0e-2, 1.0e-2, 5.0e-3):
            da = epsilon
            dg = -0.6 * epsilon
            determinant = gram_determinant(
                mean_alpha - da / 2,
                -dg / 2,
                mean_alpha + da / 2,
                dg / 2,
                width,
            )
            prediction = collision_quadratic(mean_alpha, da, dg, width)
            self.assertLess(abs(determinant / prediction - 1.0), 5.0e-5)

    def test_projective_divided_difference_tends_to_hermite_row(self) -> None:
        alpha = 0.25
        gamma = 0.8
        width = 1.2
        da, dg = 1.0, -0.4
        target = hermite_row(alpha, gamma, da, dg, width, 200)
        overlaps = []
        for epsilon in (2.0e-2, 1.0e-2, 5.0e-3):
            minus = sampled_normalized_row(
                alpha - epsilon * da / 2,
                gamma - epsilon * dg / 2,
                width,
                200,
            )
            plus = sampled_normalized_row(
                alpha + epsilon * da / 2,
                gamma + epsilon * dg / 2,
                width,
                200,
            )
            coefficient = np.vdot(minus, plus)
            orthogonal = plus - coefficient * minus
            orthogonal /= np.linalg.norm(orthogonal)
            overlaps.append(abs(np.vdot(target, orthogonal)))
        self.assertGreater(overlaps[-1], 0.999999)
        self.assertGreater(overlaps[-1], overlaps[0])

    def test_four_branch_confluent_small_eigenvalues_are_quadratic(self) -> None:
        alpha = 0.31
        width = 1.1
        scaled = []
        for epsilon in (2.0e-2, 1.0e-2, 5.0e-3):
            gram = branch_gram(alpha, 0.2, epsilon, -0.7 * epsilon, width, 180)
            eigenvalues = np.linalg.eigvalsh(gram)
            self.assertGreater(eigenvalues[0], 0.0)
            self.assertGreater(eigenvalues[1], 0.0)
            scaled.append(eigenvalues[:2] / (epsilon * epsilon))
        np.testing.assert_allclose(scaled[-1], scaled[-2], rtol=1.2e-2, atol=0.0)

    def test_pure_cross_mirror_identity_ignores_transverse_angles(self) -> None:
        rng = np.random.default_rng(812)
        free_rows = rng.normal(size=(3, 6)) + 1j * rng.normal(size=(3, 6))
        seed_rows = rng.normal(size=(3, 4)) + 1j * rng.normal(size=(3, 4))
        seed = rng.normal(size=4) + 1j * rng.normal(size=4)
        identity = mirror_cross_identity(free_rows, seed_rows, seed)
        self.assertLess(identity.residual, 2.0e-13)
        self.assertLess(
            abs(identity.cross_real + identity.negative_seed_mass), 2.0e-12
        )

    def test_same_lobe_block_is_exponentially_below_cross_carrier(self) -> None:
        alpha = 0.30
        width = 1.0
        ratios12 = packet_block_ratios(alpha, 12.0, width, 90)
        ratios20 = packet_block_ratios(alpha, 20.0, width, 90)
        self.assertLess(ratios20.same_to_cross, ratios12.same_to_cross)
        observed = ratios20.same_to_cross / ratios12.same_to_cross
        expected = np.exp(-alpha * 8.0)
        self.assertLess(abs(observed / expected - 1.0), 3.0e-2)
        self.assertLess(ratios20.reverse_to_cross, np.exp(-2.0 * alpha * 20.0) * 1.01)


if __name__ == "__main__":
    unittest.main()
