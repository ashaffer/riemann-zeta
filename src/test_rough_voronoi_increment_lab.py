#!/usr/bin/env python3
"""Tests for the finite rough-Voronoi increment lab."""

from __future__ import annotations

import unittest

from prime_gap_sieve_deletion import smallest_prime_factors
from rough_voronoi_increment_lab import (
    analyze,
    analyze_row,
    dyadic_increment_vector,
    prime_barriers,
    rough_points,
    twice_trapezoid_residues,
)


class RoughVoronoiIncrementTests(unittest.TestCase):
    def setUp(self) -> None:
        self.spf = smallest_prime_factors(5000)

    def test_prime_barriers(self) -> None:
        self.assertEqual(prime_barriers(100, 200, self.spf), (101, 199))

    def test_rough_points_nested(self) -> None:
        fine = rough_points(101, 199, 7, self.spf)
        coarse = rough_points(101, 199, 14, self.spf)
        self.assertTrue(set(coarse).issubset(fine))
        self.assertEqual(fine[0], 101)
        self.assertEqual(fine[-1], 199)

        # nu_z is the measure *after* every prime stage p<=z.  In
        # particular the prime cutoff itself is excluded, not retained.
        self.assertNotIn(7 * 17, fine)
        self.assertIn(11 * 17, fine)
        self.assertNotIn(11 * 17, coarse)

    def test_trapezoid_total_mass(self) -> None:
        points = [101, 107, 109, 127]
        vector = twice_trapezoid_residues(points, 11)
        self.assertEqual(sum(vector), 2 * (127 - 101))

    def test_increment_mass_zero(self) -> None:
        delta, fine, coarse = dyadic_increment_vector(
            101, 499, 7, 11, self.spf
        )
        self.assertEqual(sum(delta), 0)
        self.assertGreater(fine, coarse)

    def test_moments_certified(self) -> None:
        row = analyze_row(1000, 5, 7, self.spf).as_json()
        self.assertTrue(all(row["certificates"].values()))

    def test_small_analysis(self) -> None:
        result = analyze([1000], exhaustive_q=True)
        self.assertTrue(result["rows"])
        self.assertTrue(
            all(row["certificates"]["zero_total_mass"] for row in result["rows"])
        )


if __name__ == "__main__":
    unittest.main()
