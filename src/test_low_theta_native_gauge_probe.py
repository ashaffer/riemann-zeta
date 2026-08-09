#!/usr/bin/env python3

import unittest

from low_theta_native_gauge_probe import (
    analyze_exact_gauge,
    analyze_profile_envelope,
)


class LowThetaNativeGaugeProbeTests(unittest.TestCase):
    def test_affine_theta_profile_escapes_equal_weight_ill_conditioning(self) -> None:
        native = analyze_profile_envelope(
            4096, theta_limit=4, profile_dimension=1
        )
        affine = analyze_profile_envelope(
            4096, theta_limit=4, profile_dimension=2
        )
        self.assertLessEqual(native.holdout_max_error, 0.1001)
        self.assertLessEqual(affine.holdout_max_error, 0.1001)
        self.assertGreater(native.parameter_l1, 1.0e6)
        self.assertLess(affine.parameter_l1, 20.0)

    def test_high_theta_contact_survives_in_minimum_norm_exact_gauge(self) -> None:
        result = analyze_exact_gauge(
            128,
            theta_limit=4,
            target_name="constant",
            strategy="joint",
        )
        self.assertLess(result.reconstruction_error, 1.0e-10)
        self.assertGreater(abs(result.high_contact), 0.5 * abs(result.full_contact))
        self.assertGreater(result.high_contact_majorant, abs(result.high_contact))

    def test_one_scalar_contact_can_be_killed_at_bounded_cost(self) -> None:
        canonical = analyze_exact_gauge(
            128,
            theta_limit=4,
            target_name="constant",
            strategy="joint",
            compute_majorant=False,
        )
        contact_zero = analyze_exact_gauge(
            128,
            theta_limit=4,
            target_name="constant",
            strategy="contact-zero",
            compute_majorant=False,
        )
        self.assertLess(contact_zero.reconstruction_error, 1.0e-10)
        self.assertLess(abs(contact_zero.high_contact), 1.0e-10)
        self.assertLess(contact_zero.total_l2, 2.0 * canonical.total_l2)

    def test_fitting_the_whole_target_exposes_coefficient_arbitrage(self) -> None:
        canonical = analyze_exact_gauge(
            128,
            theta_limit=4,
            target_name="constant",
            strategy="joint",
            compute_majorant=False,
        )
        low_fit = analyze_exact_gauge(
            128,
            theta_limit=4,
            target_name="constant",
            strategy="low-fit",
            compute_majorant=False,
        )
        self.assertLess(low_fit.reconstruction_error, 1.0e-10)
        self.assertGreater(low_fit.total_l2, 100.0 * canonical.total_l2)


if __name__ == "__main__":
    unittest.main()
