from fractions import Fraction
import unittest

from ca4_mask_transference_falsifier import (
    FULL_SUP_DEFICIT,
    MASS_O1_THRESHOLD,
    MASS_TARGET_THRESHOLD,
    O1_TRUNCATION_DEFICIT,
    SUP_BUDGET_THRESHOLD,
    TARGET_TRUNCATION_DEFICIT,
    energy_inflation,
    l2_tail_mass_exponent,
    l2_truncation_can_fit_sup_budget,
    natural_diagonal_budget,
)


class CA4MaskTransferenceFalsifierTests(unittest.TestCase):
    def test_exact_budget_values(self) -> None:
        self.assertEqual(energy_inflation(), Fraction(463, 3250))
        self.assertEqual(natural_diagonal_budget(), Fraction(1251, 3250))
        self.assertEqual(SUP_BUDGET_THRESHOLD, Fraction(1251, 13000))

    def test_mass_retention_thresholds(self) -> None:
        self.assertEqual(MASS_O1_THRESHOLD, Fraction(463, 3250))
        self.assertEqual(MASS_TARGET_THRESHOLD, Fraction(2099, 13000))
        self.assertEqual(l2_tail_mass_exponent(MASS_TARGET_THRESHOLD), Fraction(19, 1000))

    def test_no_overlap(self) -> None:
        self.assertFalse(l2_truncation_can_fit_sup_budget())
        self.assertEqual(O1_TRUNCATION_DEFICIT, Fraction(601, 13000))
        self.assertEqual(TARGET_TRUNCATION_DEFICIT, Fraction(212, 3250))
        self.assertEqual(FULL_SUP_DEFICIT, Fraction(434, 1625))


if __name__ == "__main__":
    unittest.main()
