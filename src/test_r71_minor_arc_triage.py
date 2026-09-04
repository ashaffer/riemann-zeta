import math
import unittest
from fractions import Fraction

import numpy as np

from r71_minor_arc_triage import (
    additive_principal_band_passport,
    affine_center_moments,
    completed_difference_band_audit,
    finite_dft_band_audit,
    gevrey_frequency_constant,
    minor_arc_exponent_passport,
)


class R71MinorArcTriageTests(unittest.TestCase):
    def test_finite_dft_closes_with_every_completed_sector(self) -> None:
        points = np.arange(12, dtype=float)
        tail = (
            0.8 * np.cos(2.0 * math.pi * points / 12.0)
            + 0.2 * np.sin(8.0 * math.pi * points / 12.0)
            + 0.03 * points
        )
        center = 0.17 + 0.01 * points
        weight = (1.0 - ((points - 5.5) / 6.5) ** 2) ** 2
        audit = finite_dft_band_audit(tail, center, weight, near_radius=2)

        self.assertLess(audit.physical_spectral_error, 2.0e-14)
        self.assertLess(audit.near_far_error, 2.0e-14)
        self.assertLess(audit.total_component_error, 2.0e-14)
        self.assertLess(audit.near_component_error, 2.0e-14)
        self.assertLess(audit.far_component_error, 2.0e-14)
        self.assertLess(audit.maximum_imaginary_residual, 2.0e-14)
        self.assertLessEqual(
            abs(audit.far_energy), audit.far_young_bound + 2.0e-14
        )

        for total, near, far in zip(
            (
                audit.total_components.tail_tail,
                audit.total_components.tail_center,
                audit.total_components.center_center,
            ),
            (
                audit.near_components.tail_tail,
                audit.near_components.tail_center,
                audit.near_components.center_center,
            ),
            (
                audit.far_components.tail_tail,
                audit.far_components.tail_center,
                audit.far_components.center_center,
            ),
        ):
            self.assertAlmostEqual(total, near + far, places=13)

    def test_actual_completed_microblock_has_negative_far_piece(self) -> None:
        audit = completed_difference_band_audit(gaussian_order=16)
        self.assertTrue(audit.far_is_negative)
        self.assertAlmostEqual(audit.total_energy, 0.12774990145250775)
        self.assertAlmostEqual(audit.near_energy, 0.15751993851259488)
        self.assertAlmostEqual(audit.far_energy, -0.02977003706008713)
        self.assertAlmostEqual(
            audit.far_components.tail_tail, -0.02588424310991555
        )
        self.assertAlmostEqual(
            audit.far_components.tail_center, -0.00385966246150052
        )
        self.assertAlmostEqual(
            audit.far_components.center_center, -0.00002613148867099
        )
        self.assertLess(audit.near_far_error, 2.0e-15)
        self.assertLess(audit.total_component_error, 2.0e-15)
        self.assertLess(audit.near_component_error, 2.0e-15)
        self.assertLess(audit.far_component_error, 2.0e-15)

    def test_negative_far_margin_survives_quadrature_refinement(self) -> None:
        coarse = completed_difference_band_audit(gaussian_order=8)
        fine = completed_difference_band_audit(gaussian_order=24)
        self.assertLess(coarse.far_energy, -0.02)
        self.assertLess(fine.far_energy, -0.02)
        for field in ("total_energy", "near_energy", "far_energy"):
            self.assertLess(
                abs(getattr(coarse, field) - getattr(fine, field)), 8.0e-15
            )

    def test_eta_one_hundredth_passport(self) -> None:
        passport = minor_arc_exponent_passport(eta=0.01)
        self.assertAlmostEqual(passport.target_exponent, 0.98)
        self.assertAlmostEqual(passport.far_exponent, 0.97)
        self.assertAlmostEqual(passport.far_margin_below_target, 0.01)
        self.assertTrue(passport.far_is_negligible_at_target_scale)

    def test_gevrey_frequency_budget_solves_the_displayed_exponent(self) -> None:
        passport = minor_arc_exponent_passport(eta=0.01)
        order = 2.0
        decay = 0.4
        constant = gevrey_frequency_constant(
            gevrey_order=order,
            fourier_decay_rate=decay,
            natural_energy_exponent=passport.natural_energy_exponent,
            desired_far_exponent=passport.far_exponent,
        )
        resulting_exponent = (
            passport.natural_energy_exponent
            - decay * constant ** (1.0 / order)
        )
        self.assertAlmostEqual(resulting_exponent, 0.97)

    def test_order_four_additive_principal_band_has_power_margin(self) -> None:
        passport = additive_principal_band_passport(
            eta=0.01, aperture_exponent=0.01, spline_order=4
        )
        self.assertAlmostEqual(passport.target_energy_exponent, 0.98)
        self.assertAlmostEqual(passport.tail_amplitude_exponent, 0.46)
        self.assertAlmostEqual(passport.tail_energy_exponent, 0.92)
        self.assertAlmostEqual(passport.cross_term_exponent, 0.96)
        self.assertAlmostEqual(passport.localization_error_exponent, 0.96)
        self.assertTrue(passport.localization_is_negligible_at_target_scale)

    def test_affine_center_density_matches_both_moments_exactly(self) -> None:
        ledger = affine_center_moments(
            Fraction(3, 5),
            Fraction(-7, 11),
            Fraction(13, 17),
            Fraction(19, 23),
            Fraction(-29, 31),
        )
        self.assertEqual(ledger.recovered_alpha, ledger.alpha)
        self.assertEqual(ledger.recovered_beta, ledger.beta)


if __name__ == "__main__":
    unittest.main()
