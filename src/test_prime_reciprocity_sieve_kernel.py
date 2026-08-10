import cmath
import unittest
from fractions import Fraction

from prime_reciprocity_sieve_kernel import (
    centered_progression_average,
    explicit_primitive_even_character_sum,
    normalized_primitive_even_character_sum,
    prime_dual_coefficient_direct,
    prime_dual_coefficient_factorized,
    primes_up_to,
    weighted_error_majorant_identity,
)


class CharacterOrthogonalityTests(unittest.TestCase):
    def test_normalized_formula_against_character_enumeration(self) -> None:
        for p in (3, 5, 7, 11, 13, 17, 19):
            for a in range(-2 * p, 2 * p + 1):
                direct = explicit_primitive_even_character_sum(p, a) / (p - 1)
                exact = complex(normalized_primitive_even_character_sum(p, a))
                self.assertAlmostEqual(direct.real, exact.real, places=12)
                self.assertAlmostEqual(direct.imag, exact.imag, places=12)

    def test_centered_progression_identity(self) -> None:
        coefficients = {
            1: Fraction(1, 2),
            2: Fraction(-3, 7),
            3: Fraction(5, 11),
            5: Fraction(-2, 9),
            8: Fraction(7, 13),
        }
        for p in (5, 7, 11, 13):
            for multiplier in (1, 2, 3, 5, 8):
                left = centered_progression_average(p, multiplier, coefficients)
                selected = Fraction(0)
                baseline = Fraction(0)
                for n, coefficient in coefficients.items():
                    residue = (multiplier * n) % p
                    if residue in (1, p - 1):
                        selected += coefficient / 2
                    if residue != 0:
                        baseline += coefficient / (p - 1)
                self.assertEqual(left, selected - baseline)


class DualCoefficientTests(unittest.TestCase):
    def test_prime_dual_factorization(self) -> None:
        for p, q in ((3, 5), (5, 11), (7, 13), (11, 17)):
            for t in (-2.0, -0.3, 0.0, 0.7, 3.0):
                chi = cmath.exp(1j * (p + q) / 7.0)
                direct = prime_dual_coefficient_direct(
                    p, q, 100.0, 37.0, t, chi
                )
                factorized = prime_dual_coefficient_factorized(
                    p, q, 100.0, 37.0, t, chi
                )
                tolerance = 2.0e-14 * max(1.0, abs(direct), abs(factorized))
                self.assertLessEqual(abs(direct - factorized), tolerance)

    def test_error_majorant_factorization(self) -> None:
        primes = tuple(p for p in primes_up_to(31) if p > 2)
        weights = {p: Fraction((p % 5) + 1, p + 3) for p in primes}
        direct, factorized = weighted_error_majorant_identity(primes, weights)
        self.assertEqual(direct, factorized)
        self.assertGreater(direct, 0)


class ValidationTests(unittest.TestCase):
    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            normalized_primitive_even_character_sum(9, 1)
        with self.assertRaises(ValueError):
            prime_dual_coefficient_direct(3, 3, 10.0, 5.0, 0.0, 1.0)
        with self.assertRaises(ValueError):
            primes_up_to(-1)
        with self.assertRaises(ValueError):
            weighted_error_majorant_identity((3, 5), {3: Fraction(1)})


if __name__ == "__main__":
    unittest.main()
