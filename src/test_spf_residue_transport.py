#!/usr/bin/env python3
"""Tests for the exact SPF residue-transport representation."""

from __future__ import annotations

import math
import unittest

from prime_gap_sieve_deletion import decompose, rational_mode
from spf_residue_transport import _fourier, analyze, decompose_residues


class SpfResidueTransportTests(unittest.TestCase):
    def test_vector_identity_is_exact(self) -> None:
        result = decompose_residues(1_000, 1_500, 19)
        self.assertEqual(result.identity_error_vector(), [0] * 19)
        self.assertEqual(sum(result.initial_twice_mass), 2 * result.length)
        self.assertEqual(sum(result.final_twice_mass), 2 * result.length)

    def test_fourier_matches_complex_decomposition(self) -> None:
        lo, hi, q, a = 1_000, 1_500, 19, 5
        vectors = decompose_residues(lo, hi, q)
        complex_result = decompose(lo, hi, rational_mode(a, q))
        self.assertAlmostEqual(
            abs(_fourier(list(vectors.initial_twice_mass), a) - complex_result.initial),
            0.0,
            places=9,
        )
        self.assertAlmostEqual(
            abs(_fourier(list(vectors.final_twice_mass), a) - complex_result.final),
            0.0,
            places=9,
        )
        for prime, vector in vectors.stages_twice_mass.items():
            self.assertAlmostEqual(
                abs(_fourier(list(vector), a) - complex_result.stages[prime]),
                0.0,
                places=9,
            )

    def test_parseval_ledgers(self) -> None:
        payload = analyze(1_000, 1_500, 19)
        self.assertLess(payload["post_q"]["parseval_second_error"], 1e-7)
        self.assertLess(payload["post_q"]["parseval_fourth_error"], 1e-4)
        self.assertLess(
            payload["post_q"]["nonzero_parseval_second_error"], 1e-7
        )
        self.assertLess(
            payload["post_q"]["nonzero_parseval_fourth_error"], 1e-4
        )
        self.assertEqual(payload["post_q"]["twice_mass_sum"], 0)

    def test_reduced_frequencies_are_distinguished_for_composite_q(self) -> None:
        payload = analyze(1_000, 1_500, 21)["post_q"]
        self.assertEqual(payload["reduced_frequency_count"], 12)
        self.assertEqual(math.gcd(payload["reduced_maximum"]["a"], 21), 1)
        self.assertLessEqual(
            payload["reduced_l2_envelope_normalized"],
            payload["nonzero_l2_envelope_normalized"],
        )


if __name__ == "__main__":
    unittest.main()
