#!/usr/bin/env python3
"""Tests for the exact integer-base rational deletion reorder."""

from __future__ import annotations

import math
import unittest

from spf_residue_transport import _fourier
from universal_q_reorder_transport import analyze, decompose_universal, gap_sector_ledger


class UniversalQReorderTests(unittest.TestCase):
    def test_exact_telescope_and_resonant_vector(self) -> None:
        result = decompose_universal(1_009, 2_003, 19)
        self.assertEqual(result.identity_error_vector(), [0] * 19)
        expected = [0] * 19
        expected[0] = -2 * result.q_multiple_count
        expected[1] = result.q_multiple_count
        expected[-1] = result.q_multiple_count
        self.assertEqual(list(result.resonant_twice_mass), expected)

    def test_explicit_resonant_fourier_formula(self) -> None:
        result = decompose_universal(1_009, 2_003, 19)
        for a in range(1, 19):
            actual = _fourier(list(result.resonant_twice_mass), a)
            expected = result.q_multiple_count * (
                math.cos(2.0 * math.pi * a / 19) - 1.0
            )
            self.assertAlmostEqual(actual.real, expected, places=10)
            self.assertAlmostEqual(actual.imag, 0.0, places=10)

    def test_moment_ledger(self) -> None:
        payload = analyze(1_009, 2_003, 19)
        self.assertLess(payload["explicit_resonant_formula_max_error"], 1e-10)
        self.assertLess(
            payload["nonresonant_tail"]["parseval_second_error"], 1e-6
        )
        self.assertEqual(payload["nonresonant_tail"]["twice_mass_sum"], 0)

    def test_composite_modulus(self) -> None:
        result = decompose_universal(1_009, 2_003, 21)
        self.assertGreater(result.q_multiple_count, 0)
        self.assertEqual(result.identity_error_vector(), [0] * 21)

    def test_gap_sector_reconstruction(self) -> None:
        payload = gap_sector_ledger(1_009, 2_003, 19, 5)
        self.assertLess(payload["reconstruction_error"], 1e-9)
        self.assertTrue(any(row["gap"] == 4 for row in payload["sectors"]))


if __name__ == "__main__":
    unittest.main()
