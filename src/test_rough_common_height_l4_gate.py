#!/usr/bin/env python3

import unittest
from fractions import Fraction

from rough_common_height_l4_gate import (
    IntegerCountermodelLedger,
    Ledger,
    band_recombination_ratio,
    fourth_moment_ledger,
    weighted_block_holder_ratio,
)


class RoughCommonHeightL4GateTests(unittest.TestCase):
    def test_moment_identities(self) -> None:
        moments = fourth_moment_ledger([1 + 2j, -3, 2j, 4 - 1j, -2])
        self.assertAlmostEqual(moments["full_direct"], moments["full_correlation"])
        self.assertAlmostEqual(
            moments["primitive_direct"], moments["primitive_correlation"]
        )

    def test_holder_exponents(self) -> None:
        ledger = Ledger()
        delta = Fraction(1, 1000)
        self.assertEqual(ledger.holder_output_exponent(delta), 1 - ledger.kappa - delta)
        self.assertGreater(ledger.injective_diagonal_margin(Fraction(33, 133)), 0)

    def test_band_recombination(self) -> None:
        self.assertLessEqual(band_recombination_ratio([1, 2j, -3, 4 + 2j]), 1)

    def test_weighted_block_holder(self) -> None:
        self.assertLessEqual(
            weighted_block_holder_ratio([2 + 1j, -4j, 3], [5, 7, 13]), 1
        )

    def test_current_kappa_integer_witness(self) -> None:
        witness = IntegerCountermodelLedger()
        self.assertTrue(witness.all_conditions_hold())
        self.assertFalse(witness.as_dict()["scope_is_actual_rough_set"])


if __name__ == "__main__":
    unittest.main()
