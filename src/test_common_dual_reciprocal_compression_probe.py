#!/usr/bin/env python3
"""Tests for the exact reciprocal compression diagnostic."""

from __future__ import annotations

import unittest

import numpy as np

from common_dual_reciprocal_compression_probe import (
    analyze_reciprocal_compression,
    complete_shift_period,
    native_prime_point_ceiling,
    native_shifted_type2_vector,
    ordered_column_metadata,
    reciprocal_rotation,
    shifted_ramanujan_kernel,
)
from farey_beat_frame_probe import crt_beat


class ReciprocalCompressionTests(unittest.TestCase):
    def test_shifted_kernel_compression_and_decomposition_are_exact(self) -> None:
        result = analyze_reciprocal_compression(
            8, (5, 7, 11), start=9, shift=2
        )
        self.assertLess(result.isometry_error, 2.0e-12)
        self.assertLess(result.shifted_kernel_error, 2.0e-11)
        self.assertLess(result.native_shifted_formula_error, 2.0e-11)
        self.assertLess(result.compression_formula_error, 2.0e-12)
        self.assertLess(result.reciprocal_orientation_error, 2.0e-12)
        self.assertLess(result.reconstruction_error, 2.0e-12)
        self.assertLess(result.coefficient_phase_identity_error, 2.0e-12)
        self.assertLess(result.compression_dissipation_identity_error, 2.0e-11)
        self.assertLess(result.schur_leakage_identity_error, 2.0e-11)
        self.assertLess(result.full_decomposition_error, 2.0e-12)
        self.assertLessEqual(result.compression_operator_norm, 1.0 + 2.0e-12)
        self.assertGreaterEqual(
            result.adversarial_largest_whitened_ratio,
            result.adversarial_smallest_whitened_ratio,
        )

    def test_zero_shift_is_the_identity_on_the_canonical_slice(self) -> None:
        result = analyze_reciprocal_compression(
            8, (5, 7, 11), start=9, shift=0
        )
        self.assertAlmostEqual(result.compression_operator_norm, 1.0, places=11)
        self.assertAlmostEqual(
            result.compression_smallest_singular_value, 1.0, places=11
        )
        self.assertLess(result.compression_defect_operator_norm, 2.0e-12)
        self.assertLess(result.canonical_euclidean_defect_ratio, 2.0e-12)
        self.assertLess(result.canonical_whitened_defect_ratio, 2.0e-12)
        self.assertLess(result.coefficient_phase_defect, 2.0e-12)
        self.assertAlmostEqual(
            result.native_whitened_residual_ratio,
            result.mismatch_whitened_ratio,
            places=11,
        )

    def test_rotation_orientation_is_native_crt_phase(self) -> None:
        primes = (5, 7, 11)
        shift = 3
        rotation = reciprocal_rotation(primes, shift)
        for phase, (p, r, theta) in zip(
            rotation, ordered_column_metadata(primes)
        ):
            _, numerator_r = crt_beat(theta, p, r)
            expected = np.exp(2j * np.pi * shift * numerator_r / r)
            self.assertAlmostEqual(abs(phase - expected), 0.0, places=11)

    def test_shifted_kernel_is_start_independent(self) -> None:
        first = shifted_ramanujan_kernel(8, (5, 7, 11), 2, start=1)
        translated = shifted_ramanujan_kernel(8, (5, 7, 11), 2, start=101)
        np.testing.assert_array_equal(first, translated)

    def test_native_shift_formula_is_real_and_has_the_requested_length(self) -> None:
        values = native_shifted_type2_vector(
            8, (5, 7, 11), 2, start=9
        )
        self.assertEqual(values.shape, (8,))
        self.assertTrue(np.isrealobj(values))

    def test_complete_shift_average_exposes_minus_target(self) -> None:
        length = 8
        primes = (5, 7, 11)
        start = 9
        period = complete_shift_period(primes)
        native_average = sum(
            native_shifted_type2_vector(
                length, primes, shift, start=start
            )
            for shift in range(period)
        ) / period
        self.assertLess(float(np.max(np.abs(native_average))), 2.0e-12)

        rotation_average = sum(
            reciprocal_rotation(primes, shift)
            for shift in range(period)
        ) / period
        self.assertLess(float(np.max(np.abs(rotation_average))), 2.0e-12)

    def test_native_prime_points_are_uniformly_below_the_ceiling(self) -> None:
        primes = (5, 7, 11)
        start = 101
        length = 12
        ceiling = native_prime_point_ceiling(primes)
        for shift in (-9, 0, 3, 117):
            values = native_shifted_type2_vector(
                length, primes, shift, start=start
            )
            for offset, value in enumerate(values):
                point = start + offset
                is_prime = all(
                    point % divisor
                    for divisor in range(2, int(point**0.5) + 1)
                )
                if is_prime:
                    self.assertLessEqual(value, ceiling + 2.0e-14)

    def test_target_shape_is_checked(self) -> None:
        with self.assertRaisesRegex(ValueError, "shape"):
            analyze_reciprocal_compression(
                8,
                (5, 7, 11),
                target=np.ones(7),
            )


if __name__ == "__main__":
    unittest.main()
