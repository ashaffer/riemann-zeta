#!/usr/bin/env python3

import unittest
from fractions import Fraction

from finite_ramanujan_completion_probe import (
    expected_von_mangoldt,
    finite_coefficients,
    mobius_sieve,
    ramanujan_sum,
    reconstruct,
)


class FiniteRamanujanCompletionProbeTests(unittest.TestCase):
    def test_ramanujan_sum_divisor_formula(self) -> None:
        mobius = mobius_sieve(12)
        self.assertEqual(ramanujan_sum(5, 1, mobius), -1)
        self.assertEqual(ramanujan_sum(5, 5, mobius), 4)
        self.assertEqual(ramanujan_sum(6, 1, mobius), 1)

    def test_expansion_is_exact_on_the_active_range(self) -> None:
        limit = 24
        for n in range(1, limit + 1):
            self.assertEqual(reconstruct(limit, n), expected_von_mangoldt(n))

    def test_nonsquarefree_modulus_has_zero_coefficient(self) -> None:
        coefficients = finite_coefficients(30)
        self.assertEqual(coefficients[4], {})
        self.assertEqual(coefficients[12], {})

    def test_prime_and_composite_targets(self) -> None:
        self.assertEqual(expected_von_mangoldt(8), {2: Fraction(1)})
        self.assertEqual(expected_von_mangoldt(12), {})
        self.assertEqual(expected_von_mangoldt(1), {})


if __name__ == "__main__":
    unittest.main()
