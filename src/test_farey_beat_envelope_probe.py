#!/usr/bin/env python3

import unittest

from farey_beat_envelope_probe import (
    farey_beats,
    l1_spectral_gap_lower_bound,
    minimum_l1_uniform_approximation,
)


class FareyBeatEnvelopeProbeTests(unittest.TestCase):
    def test_y256_beat_catalogue(self) -> None:
        beats = farey_beats(256, 16.0)
        self.assertEqual(len(beats), 140)
        self.assertAlmostEqual(beats[0].scaled_frequency, 16.0 / 15.0)
        for beat in beats:
            self.assertEqual(beat.left - beat.right, beat.difference)
            self.assertNotEqual(beat.left, beat.right)
            self.assertLessEqual(beat.left.denominator, 16)
            self.assertLessEqual(beat.right.denominator, 16)
            self.assertGreaterEqual(beat.multiplicity, 1)

    def test_y256_minimum_l1_regression(self) -> None:
        result = minimum_l1_uniform_approximation(256)
        self.assertLessEqual(result.holdout_max_error, 1.001 * 15.0 / 256.0)
        self.assertAlmostEqual(result.coefficient_l1, 14.0960564, places=4)
        self.assertLessEqual(result.support_size, 20)

    def test_square_root_scale_has_constant_spectral_gap_cost(self) -> None:
        lower_bound = l1_spectral_gap_lower_bound(256, 16, 15.0 / 256.0)
        self.assertGreater(lower_bound, 2.9)
        self.assertLess(lower_bound, 3.2)


if __name__ == "__main__":
    unittest.main()
