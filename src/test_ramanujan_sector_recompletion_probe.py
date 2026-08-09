#!/usr/bin/env python3

import math
import unittest
from fractions import Fraction

from finite_ramanujan_completion_probe import mobius_sieve, ramanujan_sum
from ramanujan_sector_recompletion_probe import (
    determinant_certificate,
    divisor_factor_matrices,
    divisor_sum,
    interval_ramanujan_sum,
    matrix_product,
    mean_ramanujan_correlation,
    ramanujan_matrix,
    singular_series_interval_majorant,
    singular_series_interval_sum,
)


class RamanujanSectorRecompletionProbeTests(unittest.TestCase):
    def test_triangular_factorization_is_exact(self) -> None:
        for limit in range(1, 13):
            incidence, transform = divisor_factor_matrices(limit)
            self.assertEqual(matrix_product(incidence, transform), ramanujan_matrix(limit))

    def test_determinant_certificate_is_factorial(self) -> None:
        for limit in range(1, 15):
            self.assertEqual(determinant_certificate(limit), math.factorial(limit))

    def test_uniform_interval_bound_for_ramanujan_sums(self) -> None:
        for q in range(2, 20):
            for start in range(20):
                for length in range(20):
                    self.assertLessEqual(
                        abs(interval_ramanujan_sum(q, start, length)),
                        divisor_sum(q),
                    )

    def test_singular_series_ledger_controls_every_tested_interval(self) -> None:
        coefficients = [Fraction(), Fraction(1)] + [
            Fraction((-1) ** q, q + 1) for q in range(2, 14)
        ]
        majorant = singular_series_interval_majorant(coefficients)
        for start in range(20):
            for length in range(20):
                self.assertLessEqual(
                    abs(singular_series_interval_sum(coefficients, start, length)),
                    majorant,
                )

    def test_ramanujan_correlations_are_diagonal_in_the_modulus(self) -> None:
        mobius = mobius_sieve(10)
        for q in range(1, 11):
            for r in range(1, 11):
                for shift in range(6):
                    expected = (
                        Fraction(ramanujan_sum(q, shift, mobius))
                        if q == r
                        else Fraction()
                    )
                    self.assertEqual(mean_ramanujan_correlation(q, r, shift), expected)


if __name__ == "__main__":
    unittest.main()
