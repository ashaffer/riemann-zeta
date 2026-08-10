import unittest
from fractions import Fraction

from squarefree_kernel_dirichlet_series import (
    base_local_factor,
    branch_correction_factor,
    branch_local_factor,
    branch_pole_residue,
    even_kernel_pole_residue,
    finite_factorized_euler_product,
    finite_raw_euler_product,
    normalized_log_taper_leading_coefficient,
    zeta_removed_local_factor,
)


class FiniteEulerProductTests(unittest.TestCase):
    def test_local_factorization(self) -> None:
        for p in (3, 5, 7, 11, 17):
            for value in range(-12, 13):
                for sign in (-1, 1):
                    for z in (0.0, 0.2 + 0.3j, 0.75 - 1.1j):
                        direct = branch_local_factor(p, value, sign, z)
                        factorized = base_local_factor(p, z) * branch_correction_factor(
                            p, value, sign, z
                        )
                        self.assertLessEqual(
                            abs(direct - factorized),
                            2.0e-13 * max(1.0, abs(direct), abs(factorized)),
                        )

    def test_global_finite_factorization(self) -> None:
        for limit in (3, 7, 19, 43):
            for value in (-17, -5, -1, 0, 1, 2, 6, 15, 37):
                for sign in (-1, 1):
                    for z in (0.1, 0.3 + 0.2j, 0.8 - 0.7j):
                        direct = finite_raw_euler_product(limit, value, sign, z)
                        factorized = finite_factorized_euler_product(
                            limit, value, sign, z
                        )
                        self.assertLessEqual(
                            abs(direct - factorized),
                            2.0e-12 * max(1.0, abs(direct), abs(factorized)),
                        )

    def test_removed_factor_is_one_at_zero(self) -> None:
        for p in (3, 5, 7, 11, 101):
            self.assertAlmostEqual(zeta_removed_local_factor(p, 0.0).real, 1.0)
            self.assertAlmostEqual(zeta_removed_local_factor(p, 0.0).imag, 0.0)


class ResidueTests(unittest.TestCase):
    def test_special_values_remove_pole(self) -> None:
        self.assertEqual(branch_pole_residue(0, 1), 0)
        self.assertEqual(branch_pole_residue(1, 1), 0)
        self.assertEqual(branch_pole_residue(-1, -1), 0)

    def test_even_residue_and_taper_coefficient(self) -> None:
        for value in range(-20, 21):
            residue = even_kernel_pole_residue(value)
            self.assertGreaterEqual(residue, 0)
            self.assertEqual(
                normalized_log_taper_leading_coefficient(value), residue / 2
            )

    def test_known_residue(self) -> None:
        # a=2: plus branch has a-1=1 and odd part of a empty, so residue 1/2.
        self.assertEqual(branch_pole_residue(2, 1), Fraction(1, 2))
        # minus branch has a+1=3, giving the additional factor 1/3.
        self.assertEqual(branch_pole_residue(2, -1), Fraction(1, 6))
        self.assertEqual(even_kernel_pole_residue(2), Fraction(1, 3))


if __name__ == "__main__":
    unittest.main()
