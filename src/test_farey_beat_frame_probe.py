#!/usr/bin/env python3

import math
import unittest

import numpy as np

from farey_beat_frame_probe import (
    analyze_frame,
    coefficient_matrix,
    crt_beat,
    exact_gram_formula,
    lower_frame_certificate,
    primitive_frame_matrix,
    primitive_residues,
    tensor_diagnostic,
    two_primes_near_twice_sqrt,
)


class FareyBeatFrameProbeTests(unittest.TestCase):
    def test_primitive_character_gram_formula(self) -> None:
        length = 18
        prime_p, prime_r = two_primes_near_twice_sqrt(length)
        frame = primitive_frame_matrix(length, prime_p, prime_r)
        exact = exact_gram_formula(length, prime_p, prime_r)
        np.testing.assert_allclose(frame @ frame.conj().T, exact, atol=2.0e-12)

    def test_crt_turns_every_unit_into_a_primitive_beat(self) -> None:
        prime_p, prime_r = 11, 13
        modulus = prime_p * prime_r
        for theta in primitive_residues(modulus):
            a, b = crt_beat(theta, prime_p, prime_r)
            self.assertNotEqual(a, 0)
            self.assertNotEqual(b, 0)
            self.assertEqual((a * prime_r - b * prime_p - theta) % modulus, 0)

    def test_elementary_frame_bounds(self) -> None:
        for length in (12, 24, 36):
            prime_p, prime_r = two_primes_near_twice_sqrt(length)
            gram = exact_gram_formula(length, prime_p, prime_r)
            eigenvalues = np.linalg.eigvalsh(gram)
            self.assertGreaterEqual(
                eigenvalues[0],
                lower_frame_certificate(length, prime_p, prime_r) - 2.0e-12,
            )
            self.assertLessEqual(
                eigenvalues[-1], prime_p * prime_r + length + 2.0e-12
            )

    def test_prime_vector_reconstructs_and_obeys_dual_norm_bounds(self) -> None:
        result = analyze_frame(32)
        self.assertLess(result.reconstruction_error, 2.0e-13)
        self.assertGreaterEqual(
            result.coefficient_norm_squared,
            result.target_norm_squared / (result.modulus + result.length) - 2.0e-13,
        )
        self.assertLessEqual(
            result.coefficient_norm_squared,
            result.target_norm_squared / result.lower_certificate + 2.0e-13,
        )

    def test_primes_are_at_the_square_root_scale(self) -> None:
        prime_p, prime_r = two_primes_near_twice_sqrt(100)
        self.assertGreaterEqual(prime_p, math.ceil(2 * math.sqrt(100)))
        self.assertGreater(prime_r, prime_p)

    def test_crt_matrix_preserves_the_coefficient_frobenius_norm(self) -> None:
        result = analyze_frame(32)
        matrix = coefficient_matrix(result)
        self.assertAlmostEqual(
            float(np.vdot(matrix, matrix).real),
            result.coefficient_norm_squared,
            places=13,
        )

    def test_actual_prime_tensor_is_full_row_rank_at_y32(self) -> None:
        diagnostic = tensor_diagnostic(32)
        self.assertEqual(diagnostic.matrix_rank, 12)
        self.assertGreater(diagnostic.nuclear_to_frobenius, 3.2)
        self.assertLess(diagnostic.nuclear_to_frobenius, 3.3)


if __name__ == "__main__":
    unittest.main()
