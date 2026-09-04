#!/usr/bin/env python3
"""Exact tests for :mod:`rough_gap_lower_sieve_frontier`."""

from fractions import Fraction
import unittest

from rough_gap_lower_sieve_frontier import (
    LowerSieveParameters,
    required_excess,
    rough_gap_moment_certificate,
    type_ii_exponent,
)


class RoughGapLowerSieveFrontierTests(unittest.TestCase):
    def test_main_term_is_strictly_inside_lower_sieve_range(self) -> None:
        p = LowerSieveParameters()
        self.assertEqual(p.linear_sieve_ratio, Fraction(5000, 2397))
        self.assertEqual(p.main_term_power_margin, Fraction(103, 7500))
        self.assertGreater(p.linear_sieve_ratio, 2)

    def test_one_to_two_factor_exponents(self) -> None:
        p = LowerSieveParameters()
        self.assertEqual(p.first_factor, Fraction(1003, 4500))
        self.assertEqual(p.second_factor, Fraction(1003, 9000))
        self.assertEqual(p.total_weight_level, Fraction(1003, 3000))
        self.assertEqual(p.jacobsthal_gap_cutoff, Fraction(799, 2500))
        self.assertEqual(p.type_ii_poisson_range, Fraction(797, 1800))
        self.assertLess(p.jacobsthal_gap_cutoff, p.type_ii_poisson_range)

    def test_endpoint_type_ii_max_plus_nodes(self) -> None:
        p = LowerSieveParameters()
        c = type_ii_exponent(
            p.jacobsthal_gap_cutoff,
            p.first_factor,
            p.second_factor,
            p.total_weight_level,
        )
        self.assertEqual(c.shifted_product, Fraction(-22, 1875))
        self.assertEqual(c.shifted_or_second, Fraction(1003, 9000))
        self.assertEqual(c.q_or_second_square, Fraction(1003, 3000))
        self.assertEqual(c.inner_first, Fraction(1003, 1000))
        self.assertEqual(c.inner_second, Fraction(4927, 7500))
        self.assertEqual(c.convolution_first, Fraction(84457, 90000))
        self.assertEqual(c.convolution_second, Fraction(84457, 90000))
        self.assertEqual(c.convolution, Fraction(84457, 90000))

    def test_final_gap_square_exponent(self) -> None:
        c = rough_gap_moment_certificate()
        self.assertEqual(c.diagonal_gap_square, 1)
        self.assertEqual(c.geometric_error_gap_square, Fraction(799, 1250))
        self.assertEqual(c.type_ii_gap_square, Fraction(84457, 90000))
        self.assertEqual(c.final_gap_square, 1)
        self.assertEqual(c.excess, 0)

    def test_type_ii_frontier_is_nondecreasing(self) -> None:
        p = LowerSieveParameters()
        previous = Fraction()
        for numerator in range(0, 321):
            h = Fraction(numerator, 1000)
            current = type_ii_exponent(
                h,
                p.first_factor,
                p.second_factor,
                p.total_weight_level,
            ).convolution
            self.assertGreaterEqual(current, previous)
            previous = current

    def test_hostile_required_frontier_clears(self) -> None:
        # Exact decimal used by the current carrier audit.
        kappa = Fraction(19740482582942, 10**15)
        needed = required_excess(Fraction(799, 5000), kappa)
        actual = rough_gap_moment_certificate().excess
        self.assertGreater(needed, actual)
        self.assertGreater(float(needed - actual), 0.12)


if __name__ == "__main__":
    unittest.main()
