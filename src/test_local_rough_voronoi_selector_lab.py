#!/usr/bin/env python3
"""Tests for the local rough-Voronoi selector lab."""

from __future__ import annotations

import math
import unittest

from local_rough_voronoi_selector_lab import (
    BETA,
    BETA_MAX,
    RationalSelector,
    _thresholds,
    analyze,
    localized_coefficients,
    localized_residue_vector,
    prime_barriers,
    rational_power_floor,
    residue_moment_ledger,
    rough_points,
    select_rational,
    twice_increment,
    twice_increment_between,
    twice_voronoi_measure,
)
from prime_gap_sieve_deletion import smallest_prime_factors


class LocalRoughVoronoiSelectorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.spf = smallest_prime_factors(5000)

    def test_prime_barriers(self) -> None:
        self.assertEqual(prime_barriers(100, 200, self.spf), (101, 199))

    def test_exact_rational_power_floor(self) -> None:
        from fractions import Fraction

        self.assertEqual(rational_power_floor(16, Fraction(1, 2)), 4)
        self.assertEqual(rational_power_floor(15, Fraction(1, 2)), 3)
        value = rational_power_floor(3000, BETA)
        self.assertLessEqual(pow(value, BETA.denominator), pow(3000, BETA.numerator))
        self.assertGreater(
            pow(value + 1, BETA.denominator), pow(3000, BETA.numerator)
        )

    def test_mass_and_nesting(self) -> None:
        fine = rough_points(1009, 1999, 7, self.spf)
        coarse = rough_points(1009, 1999, 14, self.spf)
        self.assertTrue(set(coarse).issubset(fine))
        mass = twice_voronoi_measure(fine)
        self.assertEqual(sum(mass.values()), 2 * (1999 - 1009))
        self.assertNotIn(7 * 211, fine)
        self.assertIn(11 * 137, fine)
        self.assertNotIn(11 * 137, coarse)

    def test_increment_zero_mass(self) -> None:
        delta = twice_increment(1000, 2000, 11, self.spf)
        self.assertEqual(sum(delta.values()), 0)
        self.assertTrue(delta)

    def test_complete_post_q_band_and_crossing_band(self) -> None:
        left, right = 1009, 1999
        q = 11

        def qfirst_mass(cutoff: int) -> dict[int, int]:
            points = [
                n
                for n in range(left, right + 1)
                if n in (left, right)
                or (n % q != 0 and self.spf[n] > cutoff)
            ]
            return twice_voronoi_measure(points)

        def difference(
            coarse: dict[int, int], fine: dict[int, int]
        ) -> dict[int, int]:
            keys = coarse.keys() | fine.keys()
            return {
                n: coarse.get(n, 0) - fine.get(n, 0)
                for n in keys
                if coarse.get(n, 0) != fine.get(n, 0)
            }

        complete_p = 13
        complete = difference(
            qfirst_mass(2 * complete_p), qfirst_mass(complete_p)
        )
        self.assertEqual(
            complete,
            twice_increment(left, right, complete_p, self.spf),
        )

        crossing_p = 7
        exact_crossing = difference(
            qfirst_mass(2 * crossing_p), qfirst_mass(q)
        )
        precomputed = twice_increment(left, right, crossing_p, self.spf)
        self.assertNotEqual(exact_crossing, precomputed)
        self.assertEqual(
            exact_crossing,
            twice_increment_between(
                left, right, q, 2 * crossing_p, self.spf
            ),
        )

    def test_selector_certificate(self) -> None:
        # Search a deterministic minor-arc example instead of baking in a
        # fragile continued-fraction choice.
        found = None
        for numerator in range(1, 1000):
            alpha = math.sqrt(2.0) + numerator / 997.0
            found = select_rational(alpha, 200, 11)
            if found is not None:
                break
        self.assertIsNotNone(found)
        assert found is not None
        self.assertGreater(found.denominator, 11)
        self.assertLessEqual(found.denominator, 200)
        self.assertLessEqual(
            found.error, 1.0000001 / (found.denominator * 200)
        )
        self.assertEqual(
            found.lifted_numerator % found.denominator, found.numerator
        )
        self.assertEqual(math.gcd(found.numerator, found.denominator), 1)

    def test_selector_upper_cap(self) -> None:
        found = None
        for numerator in range(1, 1000):
            alpha = math.sqrt(2.0) + numerator / 997.0
            found = select_rational(alpha, 200, 11, 47)
            if found is not None:
                break
        self.assertIsNotNone(found)
        assert found is not None
        self.assertLessEqual(found.denominator, 47)

    def test_localized_zero(self) -> None:
        selector = select_rational(math.sqrt(2.0), 200, 11)
        self.assertIsNotNone(selector)
        assert selector is not None
        rational, logarithmic, variation = localized_coefficients(
            {}, 1500.0, 100, 1000.0, selector
        )
        self.assertEqual(rational, 0j)
        self.assertEqual(logarithmic, 0j)
        self.assertEqual(variation, 0.0)

    def test_localized_normalization_and_phase(self) -> None:
        selector = RationalSelector(1, 5, 6, 0.0, 0.2)
        delta = {100: 2, 101: -2}
        rational, logarithmic, variation = localized_coefficients(
            delta, 100.0, 10, 7.0, selector
        )
        expected_rational = 1.0 - 0.9 * complex(
            math.cos(2.0 * math.pi / 5.0),
            math.sin(2.0 * math.pi / 5.0),
        )
        expected_logarithmic = 1.0 - 0.9 * complex(
            math.cos(7.0 * math.log(1.01)),
            math.sin(7.0 * math.log(1.01)),
        )
        self.assertAlmostEqual(rational.real, expected_rational.real)
        self.assertAlmostEqual(rational.imag, expected_rational.imag)
        self.assertAlmostEqual(logarithmic.real, expected_logarithmic.real)
        self.assertAlmostEqual(logarithmic.imag, expected_logarithmic.imag)
        self.assertAlmostEqual(variation, 1.9)
        vector, residue_variation = localized_residue_vector(
            delta, 100.0, 10, 5
        )
        self.assertAlmostEqual(residue_variation, variation)
        residue_rational = sum(
            value
            * complex(
                math.cos(2.0 * math.pi * residue / 5.0),
                math.sin(2.0 * math.pi * residue / 5.0),
            )
            for residue, value in enumerate(vector)
        )
        self.assertAlmostEqual(residue_rational.real, rational.real)
        self.assertAlmostEqual(residue_rational.imag, rational.imag)

    def test_residue_moment_normalization(self) -> None:
        vector = [1.0, -2.0, 0.5, 0.5]
        ledger = residue_moment_ledger(vector)
        transforms = [
            sum(
                value
                * complex(
                    math.cos(2.0 * math.pi * a * r / len(vector)),
                    math.sin(2.0 * math.pi * a * r / len(vector)),
                )
                for r, value in enumerate(vector)
            )
            for a in range(len(vector))
        ]
        self.assertAlmostEqual(
            sum(abs(value) ** 2 for value in transforms),
            len(vector) * ledger["residue_l2_squared"],
        )
        self.assertAlmostEqual(
            sum(abs(value) ** 4 for value in transforms),
            len(vector) * ledger["cyclic_correlation_l2_squared"],
        )
        self.assertAlmostEqual(
            ledger["zero_shift_correlation"],
            ledger["residue_l2_squared"],
        )

    def test_thresholds_reach_terminal_band(self) -> None:
        values = _thresholds(10_000, 3)
        self.assertLess(values[-2] * 2, math.isqrt(20_000))
        self.assertGreaterEqual(values[-1] * 2, math.isqrt(20_000))

    def test_small_analysis(self) -> None:
        payload = analyze([3000], [0.9, 1.2], block_samples=2)
        self.assertEqual(
            payload["schema"], "zeta23.local-rough-voronoi-selector-lab.v4"
        )
        self.assertTrue(payload["blocks"])
        for block in payload["blocks"]:
            self.assertTrue(all(block["certificates"].values()))
            self.assertEqual(
                block["q_floor"],
                max(2, rational_power_floor(block["Y"], BETA)),
            )
            self.assertEqual(
                block["q_cap"],
                max(
                    block["q_floor"],
                    rational_power_floor(block["Y"], BETA_MAX),
                ),
            )
            self.assertLessEqual(block["q"], block["q_cap"])
            self.assertEqual(
                block["lifted_a"] % block["q"], block["a"]
            )
        for row in payload["rows"]:
            self.assertLessEqual(row["dirichlet_error"], row["dirichlet_bound"])
            self.assertGreater(row["low_major_distance"], 1.0 / row["H"])
            self.assertGreater(row["q"], row["q_floor"])
            self.assertGreaterEqual(row["cutoff_P"], row["q"])
            self.assertAlmostEqual(
                row["rational_normalized_abs"],
                math.hypot(
                    row["rational_normalized_real"],
                    row["rational_normalized_imag"],
                ),
            )
            self.assertAlmostEqual(
                row["zero_shift_correlation_actual_mass"],
                row["residue_l2_squared_actual_mass"],
            )
            self.assertLessEqual(
                row["selected_fourier_from_residue_error"], 1e-9
            )


if __name__ == "__main__":
    unittest.main()
