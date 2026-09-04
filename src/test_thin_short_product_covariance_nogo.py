from fractions import Fraction
import unittest

from thin_short_product_covariance_nogo import (
    H_MIN,
    KAPPA,
    adversarial_eta,
    aligned_block_energy,
    closing_eta_frontier,
    diagonal_delta_frontier,
    prime_product_blocks,
    voronoi_difference_diagonal,
)


class ThinShortProductCovarianceNoGoTests(unittest.TestCase):
    def test_unique_fibres_and_exact_alignment(self) -> None:
        blocks, unique = prime_product_blocks(20_000, 23, 59, 100)
        self.assertTrue(unique)
        result = aligned_block_energy(blocks, 20_000, 100)
        self.assertGreater(result.total_pairs, 0)
        self.assertTrue(result.unique_large_factor)
        self.assertAlmostEqual(result.direct_energy, result.count_energy)
        self.assertLess(result.maximum_beta_modulus_error, 1e-12)
        self.assertGreaterEqual(result.count_energy, result.cauchy_floor)

    def test_exact_exponent_miss(self) -> None:
        self.assertEqual(
            adversarial_eta(H_MIN) - closing_eta_frontier(H_MIN),
            4 * KAPPA,
        )
        self.assertGreater(4 * KAPPA, Fraction(78, 1000))
        self.assertGreater(diagonal_delta_frontier(), Fraction(1, 1000))
        self.assertLess(diagonal_delta_frontier(), Fraction(11, 10_000))

    def test_voronoi_diagonal_bound(self) -> None:
        energy, bound = voronoi_difference_diagonal(
            [0, 7, 12], [0, 2, 5, 7, 9, 12]
        )
        self.assertGreater(energy, 0)
        self.assertLessEqual(energy, bound)


if __name__ == "__main__":
    unittest.main()
