import math
import unittest

import numpy as np

from qp_actual_multiplicative_gate import (
    carrier_leverage_upper,
    direct_square_reweighted_characteristic,
    effective_rank,
    expanded_square_reweighted_characteristic,
    kmt_rank_tax,
    limiting_turan_strip_width,
    negative_zero_pole_residue,
    selberg_square_weight_on_prime,
    square_reweight_termwise_bound,
    turan_band_ledger,
)


class ActualMultiplicativeGateTests(unittest.TestCase):
    def test_exact_fixed_slice_strip_width(self) -> None:
        expected = (0.019 * 33.0 / 50.0) ** 2
        self.assertAlmostEqual(limiting_turan_strip_width(), expected, places=15)
        self.assertAlmostEqual(expected, 0.0001572516, places=15)

    def test_turan_band_embedding_near_limit(self) -> None:
        ledger = turan_band_ledger(0.0125)
        self.assertTrue(ledger.admissible)
        self.assertGreater(ledger.upper_height_exponent_at_shortest_length, 1.0)
        self.assertLess(ledger.lower_height_exponent_at_longest_length, 0.95)
        self.assertGreater(ledger.saving_exponent_at_shortest_length, 0.0125)

    def test_beta_at_or_above_limit_fails_saving(self) -> None:
        self.assertFalse(turan_band_ledger(0.0126).admissible)

    def test_kmt_rank_tax_eventually_increases_by_a_power(self) -> None:
        small = kmt_rank_tax(10.0**20)
        large = kmt_rank_tax(10.0**200)
        self.assertGreater(large, small)

    def test_scalar_mean_gram_ledger(self) -> None:
        self.assertAlmostEqual(carrier_leverage_upper(100, 0.01, 0.5), 0.02)
        self.assertAlmostEqual(carrier_leverage_upper(100, 0.1, 1.0), 1.0)

    def test_effective_rank(self) -> None:
        self.assertAlmostEqual(effective_rank([1.0, 1.0, 1.0, 1.0]), 4.0)
        self.assertAlmostEqual(effective_rank([1.0, 0.0, 0.0]), 1.0)

    def test_termwise_square_bound(self) -> None:
        self.assertAlmostEqual(square_reweight_termwise_bound(0.01, [1, 1]), 0.02 / 0.99)
        with self.assertRaises(ValueError):
            square_reweight_termwise_bound(0.6, [1, 1, 1])

    def test_square_difference_expansion_is_exact(self) -> None:
        nodes = [-0.2, -0.07, 0.03, 0.18]
        probabilities = [0.1, 0.2, 0.3, 0.4]
        shifts = [0.0, 2.3, 7.1]
        coefficients = [1.0 + 0.2j, -0.3j, 0.4 - 0.1j]
        direct = direct_square_reweighted_characteristic(
            nodes, probabilities, shifts, coefficients, 4.7
        )
        expanded = expanded_square_reweighted_characteristic(
            nodes, probabilities, shifts, coefficients, 4.7
        )
        self.assertAlmostEqual(direct.real, expanded.real, places=13)
        self.assertAlmostEqual(direct.imag, expanded.imag, places=13)

    def test_small_divisor_selberg_square_is_constant_on_large_primes(self) -> None:
        coefficients = {1: 2.0, 2: -7.0, 3: 11.0, 5: 13.0}
        values = [
            selberg_square_weight_on_prime(p, 10, coefficients)
            for p in (101, 103, 107, 109)
        ]
        self.assertEqual(values, [4.0, 4.0, 4.0, 4.0])

    def test_matching_zero_residue_has_hostile_sign(self) -> None:
        self.assertAlmostEqual(negative_zero_pole_residue(0.75, 2), -8.0 / 3.0)


if __name__ == "__main__":
    unittest.main()
