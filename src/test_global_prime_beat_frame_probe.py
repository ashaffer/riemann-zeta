#!/usr/bin/env python3

import unittest
from fractions import Fraction

from global_prime_beat_frame_probe import (
    analyze_global_frame,
    analyze_sparse_global_frame,
    global_prime_beats,
)


class GlobalPrimeBeatFrameProbeTests(unittest.TestCase):
    def test_crt_representatives_have_the_exact_low_beat(self) -> None:
        _, beats = global_prime_beats(4096, 4)
        for beat in beats:
            self.assertEqual(
                beat.numerator_p * beat.prime_r
                - beat.numerator_r * beat.prime_p,
                beat.theta,
            )
            self.assertEqual(
                Fraction(beat.numerator_p, beat.prime_p)
                - Fraction(beat.numerator_r, beat.prime_r),
                Fraction(beat.theta, beat.prime_p * beat.prime_r),
            )

    def test_canonical_global_frame_reconstructs_but_fixed_pair_does_not(self) -> None:
        result = analyze_global_frame(4096, theta_limit=4)
        self.assertLess(result.holdout_rms_error, 1.01 * 15.0 / 4096.0)
        self.assertGreater(result.best_fixed_pair_rms_error, 0.9)
        self.assertEqual(result.prime_unfold_rank, len(result.primes))
        self.assertEqual(result.output_rank_at_tenfold_error, len(result.primes))

    def test_sparse_global_frame_has_bounded_tested_support(self) -> None:
        result = analyze_sparse_global_frame(10000, theta_limit=4)
        self.assertLessEqual(
            result.holdout_max_error,
            1.001 * 250.0 / 10000.0,
        )
        self.assertLess(result.coefficient_l1, 22.0)
        self.assertLessEqual(result.support_size, 18)
        self.assertLessEqual(result.cp_rank_edge_bound, 36)


if __name__ == "__main__":
    unittest.main()
