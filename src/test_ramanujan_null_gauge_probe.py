#!/usr/bin/env python3

import unittest
from fractions import Fraction

from finite_ramanujan_completion_probe import expected_von_mangoldt
from ramanujan_null_gauge_probe import (
    CONSTANT_KEY,
    gauged_coefficients,
    inverse_totient_weights,
    null_relation,
    optimal_adjustment_ledger,
    reconstruct_gauged,
)


class RamanujanNullGaugeProbeTests(unittest.TestCase):
    def test_weights_are_normalized(self) -> None:
        weights = inverse_totient_weights(24)
        self.assertEqual(sum(weights.values(), Fraction()), 1)

    def test_prime_cloud_is_an_exact_null_relation(self) -> None:
        for n in range(1, 25):
            self.assertEqual(null_relation(24, n), 0)

    def test_gauged_expansion_reconstructs_von_mangoldt(self) -> None:
        for n in range(1, 25):
            self.assertEqual(reconstruct_gauged(24, n), expected_von_mangoldt(n))

    def test_integer_lattice_coefficient_is_exactly_one(self) -> None:
        self.assertEqual(gauged_coefficients(24)[1], {CONSTANT_KEY: Fraction(1)})

    def test_inverse_totient_choice_has_exact_minimum_ledger(self) -> None:
        weights = inverse_totient_weights(24)
        reciprocal_sum = sum((Fraction(1, p - 1) for p in weights), Fraction())
        self.assertEqual(optimal_adjustment_ledger(24), 1 / reciprocal_sum)


if __name__ == "__main__":
    unittest.main()
