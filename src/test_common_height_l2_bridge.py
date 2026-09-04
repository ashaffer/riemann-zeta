from fractions import Fraction
import unittest

from common_height_l2_bridge import (
    H_MIN_EXPONENT,
    KAPPA,
    LONG_EDGE_EXPONENT,
    block_covariance_identity,
    delta_frontier_from_l2,
    diagonal_l2_exponent,
    l2_bridge_upper,
    maximum_closing_l2_exponent,
    weighted_l4,
)


class CommonHeightL2BridgeTests(unittest.TestCase):
    def test_exact_frontier(self) -> None:
        self.assertEqual(delta_frontier_from_l2(), Fraction(2, 33) - KAPPA)
        self.assertGreater(delta_frontier_from_l2(), Fraction(4, 100))
        self.assertEqual(H_MIN_EXPONENT, Fraction(8, 33))
        self.assertEqual(maximum_closing_l2_exponent(), Fraction(1) + Fraction(8, 33) - 4 * KAPPA)
        self.assertGreater(maximum_closing_l2_exponent(), Fraction(116, 100))
        self.assertEqual(diagonal_l2_exponent(), 1 + LONG_EDGE_EXPONENT)
        self.assertGreater(
            delta_frontier_from_l2(diagonal_l2_exponent()),
            Fraction(1, 1000),
        )

    def test_deterministic_bridge(self) -> None:
        values = [2 + 1j, -3j, 1 - 2j]
        lengths = [5.0, 7.0, 11.0]
        self.assertLessEqual(weighted_l4(values, lengths), l2_bridge_upper(values, lengths, 1.0) + 1e-12)

    def test_covariance_identity(self) -> None:
        direct, expanded = block_covariance_identity([[1 + 2j, 3 - 1j], [-2j, 4, 1j]])
        self.assertAlmostEqual(abs(direct - expanded), 0.0)


if __name__ == "__main__":
    unittest.main()
