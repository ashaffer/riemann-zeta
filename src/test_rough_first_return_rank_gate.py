#!/usr/bin/env python3

import unittest
from fractions import Fraction

from rough_first_return_rank_gate import (
    Ledger,
    automaton_closed_form,
    automaton_product,
    automaton_truncated_return,
    duhamel_difference,
    first_return,
    inclusion_exclusion_prefix,
    matrix_subtract,
    periodic_parity_ledger,
    prefix_kernel,
    rational_rank,
    tail_square_certificate,
    truncated_empty_prefix,
)


class RoughFirstReturnRankGateTests(unittest.TestCase):
    def test_empty_prefix_and_inclusion_exclusion(self) -> None:
        bits = [1, 0, 0, 0, 1, 0, 0]
        self.assertEqual(first_return(bits), 4)
        for cutoff in range(1, 7):
            expected = min(4, cutoff)
            self.assertEqual(truncated_empty_prefix(bits, cutoff), expected)
            self.assertEqual(automaton_truncated_return(bits, cutoff), expected)
            self.assertEqual(inclusion_exclusion_prefix(bits, cutoff), expected)

    def test_tail_square(self) -> None:
        tail, bound = tail_square_certificate([2, 5, 9], 4)
        self.assertEqual(tail, 6)
        self.assertEqual(bound, Fraction(110, 4))

    def test_prefix_rank(self) -> None:
        for size in range(1, 16):
            self.assertEqual(rational_rank(prefix_kernel(size)), size)

    def test_exponent_ledger(self) -> None:
        ledger = Ledger()
        self.assertLess(ledger.bazin_shallow_localization_margin, 0)
        self.assertGreater(ledger.bazin_companion_bottom_margin, 0)
        self.assertLess(ledger.bazin_bottom_carrier_margin, 0)
        self.assertLess(ledger.bazin_local_block_target_margin, 0)
        self.assertGreater(ledger.bazin_modulus_range_margin, 0)
        self.assertEqual(ledger.moment_overlap_width, Fraction(63, 10_000))

    def test_product_closed_form_and_duhamel(self) -> None:
        old = [1, 0, 0, 1, 0, 1]
        new = [1, 0, 0, 0, 0, 0]
        self.assertEqual(automaton_product(old, 5), automaton_closed_form(old, 5))
        self.assertEqual(automaton_product(new, 5), automaton_closed_form(new, 5))
        self.assertEqual(
            duhamel_difference(new, old, 5),
            matrix_subtract(automaton_product(new, 5), automaton_product(old, 5)),
        )

    def test_parity_countermodel(self) -> None:
        self.assertEqual(
            periodic_parity_ledger([0, 1, 3, 4], 8),
            {
                "unweighted_parity": 0,
                "twice_sym_parity": 4,
                "gap_square": 22,
                "period": 8,
            },
        )


if __name__ == "__main__":
    unittest.main()
