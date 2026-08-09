#!/usr/bin/env python3

import unittest

import numpy as np

from common_dual_prime_beat_probe import (
    analyze_common_dual,
    explicit_global_frame,
    global_frame_bounds,
    global_gram_formula,
)


class CommonDualPrimeBeatProbeTests(unittest.TestCase):
    def test_global_gram_formula_matches_explicit_frame(self) -> None:
        length = 12
        primes = (11, 13, 17)
        frame = explicit_global_frame(length, primes)
        exact = global_gram_formula(length, primes)
        self.assertLess(np.max(np.abs(frame @ frame.conj().T - exact)), 1.0e-10)

    def test_frame_certificates_and_common_dual_reconstruction(self) -> None:
        result = analyze_common_dual(16, (11, 13, 17))
        lower, upper = global_frame_bounds(result.length, result.primes)
        self.assertGreater(lower, 0)
        self.assertGreaterEqual(result.smallest_eigenvalue, lower - 1.0e-9)
        self.assertLessEqual(result.largest_eigenvalue, upper + 1.0e-9)
        self.assertLess(result.reconstruction_error, 1.0e-10)
        self.assertLess(result.ratio_formula_error, 1.0e-12)
        self.assertAlmostEqual(
            result.coefficient_norm_squared,
            result.dual_energy,
            places=10,
        )


if __name__ == "__main__":
    unittest.main()
