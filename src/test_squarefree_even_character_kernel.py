import unittest
from fractions import Fraction

from squarefree_even_character_kernel import (
    complete_local_euler_product,
    explicit_primitive_even_character_sum,
    local_product_even_kernel,
    mobius_weighted_even_kernel,
    normalized_primitive_even_character_sum,
    odd_squarefree_prime_factors,
    primitive_even_character_sum,
    radical_factorized_euler_product,
    squarefree_phi,
    squarefree_mobius,
    truncated_squarefree_kernel_sum,
)


class SquarefreeCharacterTests(unittest.TestCase):
    def test_basic_arithmetic(self) -> None:
        self.assertEqual(odd_squarefree_prime_factors(1), ())
        self.assertEqual(odd_squarefree_prime_factors(105), (3, 5, 7))
        self.assertEqual(squarefree_phi(105), 48)
        self.assertEqual(squarefree_mobius(105), -1)
        with self.assertRaises(ValueError):
            odd_squarefree_prime_factors(45)
        with self.assertRaises(ValueError):
            odd_squarefree_prime_factors(10)

    def test_even_sum_against_enumeration(self) -> None:
        for modulus in (1, 3, 5, 7, 15, 21, 33, 35, 55, 105):
            for value in range(-2 * max(1, modulus), 2 * max(1, modulus) + 1):
                direct = explicit_primitive_even_character_sum(modulus, value)
                exact = complex(primitive_even_character_sum(modulus, value))
                self.assertAlmostEqual(direct.real, exact.real, places=10)
                self.assertAlmostEqual(direct.imag, exact.imag, places=10)

    def test_local_product_formula(self) -> None:
        for modulus in (1, 3, 5, 7, 15, 21, 33, 35, 55, 105):
            for value in range(-25, 26):
                self.assertEqual(
                    mobius_weighted_even_kernel(modulus, value),
                    local_product_even_kernel(modulus, value),
                )
                self.assertEqual(
                    normalized_primitive_even_character_sum(modulus, value)
                    * squarefree_mobius(modulus),
                    local_product_even_kernel(modulus, value),
                )


class EulerProductTests(unittest.TestCase):
    def test_radical_suppression_identity(self) -> None:
        for limit in (3, 5, 11, 31, 97):
            for value in range(-20, 21):
                for sign in (-1, 1):
                    self.assertEqual(
                        complete_local_euler_product(limit, value, sign),
                        radical_factorized_euler_product(limit, value, sign),
                    )

    def test_truncated_kernel_is_exact_rational(self) -> None:
        values = [truncated_squarefree_kernel_sum(75, value) for value in range(1, 12)]
        self.assertTrue(all(isinstance(value, Fraction) for value in values))
        self.assertGreater(len(set(values)), 1)


class ValidationTests(unittest.TestCase):
    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            complete_local_euler_product(10, 3, 0)
        with self.assertRaises(ValueError):
            truncated_squarefree_kernel_sum(0, 1)


if __name__ == "__main__":
    unittest.main()
