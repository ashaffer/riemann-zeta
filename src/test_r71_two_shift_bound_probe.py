import unittest

from r71_two_shift_bound_probe import direct_two_shift_audit


class R71TwoShiftBoundProbeTests(unittest.TestCase):
    def test_every_complete_two_shift_decomposition_closes(self) -> None:
        base = direct_two_shift_audit().base
        self.assertAlmostEqual(
            base.raw_energy,
            base.tail_diagonal_raw
            + base.raw_unequal_product
            + base.raw_center_completion,
            places=14,
        )
        self.assertAlmostEqual(
            base.full_innovation,
            base.tail_diagonal_covariance
            + base.global_covariance_remainder,
            places=14,
        )
        self.assertAlmostEqual(
            base.retained_energy,
            base.tail_diagonal_retained
            + base.retained_unequal_product
            + base.retained_center_completion,
            places=14,
        )
        for diagonal, remainder, energy in zip(
            base.spectral_diagonal,
            base.spectral_remainder,
            base.spectral_energy,
        ):
            self.assertAlmostEqual(
                energy,
                diagonal + remainder,
                places=14,
            )

    def test_small_full_center_model_fails_every_simple_bound(self) -> None:
        audit = direct_two_shift_audit()
        base = audit.base
        self.assertEqual(base.active_tail_product_values, (55, 56, 60))
        self.assertEqual(base.active_central_semiprime_values, (55,))
        for margin in (
            audit.raw_signed_margin,
            audit.raw_leading_one_margin,
            audit.covariance_signed_margin,
            audit.covariance_leading_one_margin,
            audit.zero_mode_signed_margin,
            audit.zero_mode_leading_one_margin,
            audit.low_band_signed_margin,
            audit.low_band_leading_one_margin,
            audit.raw_unequal_signed_margin,
            audit.raw_center_signed_margin,
        ):
            self.assertLess(margin, 0.0)

    def test_low_frequency_failure_persists_off_zero(self) -> None:
        audit = direct_two_shift_audit()
        ratios = [
            remainder / diagonal
            for remainder, diagonal in zip(
                audit.base.spectral_remainder,
                audit.base.spectral_diagonal,
            )
        ]
        self.assertGreater(min(ratios), 1.45)

    def test_quadrature_refinement_preserves_decisive_margins(self) -> None:
        coarse = direct_two_shift_audit(gaussian_order=8)
        fine = direct_two_shift_audit(gaussian_order=24)
        fields = (
            "raw_leading_one_margin",
            "covariance_leading_one_margin",
            "zero_mode_leading_one_margin",
            "low_band_leading_one_margin",
        )
        for field in fields:
            self.assertLess(
                abs(getattr(coarse, field) - getattr(fine, field)),
                2.0e-12,
            )

    def test_larger_replication(self) -> None:
        audit = direct_two_shift_audit(
            scale=205.0,
            cutoff=7,
            step=0.03,
            gaussian_order=16,
        )
        self.assertEqual(
            audit.base.active_tail_product_values,
            (195, 207, 208, 209),
        )
        self.assertEqual(audit.base.active_central_semiprime_values, (209,))
        self.assertLess(audit.raw_leading_one_margin, 0.0)
        self.assertLess(audit.covariance_leading_one_margin, 0.0)
        self.assertLess(audit.zero_mode_leading_one_margin, 0.0)
        self.assertLess(audit.low_band_leading_one_margin, 0.0)

    def test_higher_order_terminal_replication(self) -> None:
        audit = direct_two_shift_audit(
            scale=60.0,
            cutoff=4,
            step=0.02,
            input_order=3,
            macro_order=3,
            gaussian_order=16,
        )
        self.assertEqual(
            audit.base.active_tail_product_values,
            (54, 55, 56, 60, 63),
        )
        self.assertEqual(audit.base.active_central_semiprime_values, (55,))
        self.assertLess(audit.raw_leading_one_margin, 0.0)
        self.assertLess(audit.covariance_leading_one_margin, 0.0)
        self.assertLess(audit.zero_mode_leading_one_margin, 0.0)
        self.assertLess(audit.low_band_leading_one_margin, 0.0)


if __name__ == "__main__":
    unittest.main()
