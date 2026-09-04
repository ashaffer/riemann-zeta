import unittest
from fractions import Fraction

from r188_principal_band_serialization_falsifier import (
    affine_zero_mode_audit,
    completed_channel_ledger,
    in_principal_core,
    in_principal_support,
    principal_band_geometry,
    principal_determinant_examples,
    primitive_mask_fourier_audit,
    target_matched_collar_passport,
    top_box_exponent_passport,
)


class R71PrincipalBandSerializationFalsifierTests(unittest.TestCase):
    def test_integer_power_family_gives_exact_principal_geometry(self) -> None:
        base = 2
        denominator_scale = base**99
        geometry = principal_band_geometry(base, shell_multiplier=2)

        self.assertEqual(geometry.scale, base**100)
        self.assertEqual(
            geometry.core_minimum_nonzero_denominator, denominator_scale
        )
        self.assertEqual(
            geometry.support_minimum_nonzero_denominator,
            (denominator_scale + 1) // 2,
        )
        self.assertFalse(in_principal_core(1, denominator_scale - 1, base))
        self.assertTrue(in_principal_core(1, denominator_scale, base))
        self.assertFalse(
            in_principal_support(1, (denominator_scale - 1) // 2, base)
        )
        self.assertTrue(
            in_principal_support(1, (denominator_scale + 1) // 2, base)
        )
        self.assertEqual(geometry.maximum_core_numerator, 4)
        self.assertEqual(geometry.maximum_core_physical_quotient, 4)
        self.assertLessEqual(geometry.maximum_support_physical_quotient, 8)

    def test_same_core_contains_low_high_and_reducible_determinants(self) -> None:
        base = 2
        scale = base**100
        examples = principal_determinant_examples(base)

        self.assertTrue(examples.low.both_modes_in_core)
        self.assertEqual(examples.low.common_divisor, 1)
        self.assertEqual(examples.low.determinant, 1)

        self.assertTrue(examples.high.both_modes_in_core)
        self.assertEqual(examples.high.common_divisor, 1)
        self.assertEqual(examples.high.determinant, scale - 1)

        self.assertTrue(examples.reducible.both_modes_in_core)
        self.assertEqual(examples.reducible.first_reduced_denominator, 1)
        self.assertEqual(examples.reducible.second_reduced_denominator, 2)

    def test_common_g_primitive_mask_has_subpower_local_product_bound(self) -> None:
        audits = (
            primitive_mask_fourier_audit(2, {2: (0,)}),
            primitive_mask_fourier_audit(3 * 5, {3: (0, 1), 5: (1, 3)}),
            primitive_mask_fourier_audit(
                2 * 3 * 5 * 7,
                {2: (0,), 3: (0, 1), 5: (1, 3), 7: ()},
            ),
        )
        for audit in audits:
            self.assertLessEqual(
                audit.fourier_l1, audit.local_product_bound + 1.0e-12
            )
            self.assertLessEqual(audit.bound_error, 1.0e-12)

    def test_affine_center_cannot_be_one_scalar_zero_mode(self) -> None:
        audit = affine_zero_mode_audit(
            Fraction(3, 5),
            Fraction(7, 11),
            Fraction(13, 17),
            Fraction(19, 23),
            Fraction(-2, 3),
            Fraction(5, 7),
        )
        expected = (
            audit.beta
            * (audit.second_sample - audit.first_sample)
            / audit.normalization
        )
        self.assertEqual(audit.normalized_residual_at_second_sample, expected)
        self.assertFalse(audit.scalar_axis_matches_both_samples)

        constant = affine_zero_mode_audit(3, 0, 5, 7, -2, 11)
        self.assertEqual(constant.normalized_residual_at_second_sample, 0)
        self.assertTrue(constant.scalar_axis_matches_both_samples)

    def test_complete_square_needs_packet_and_affine_cross_terms(self) -> None:
        packet_count = 23
        ledger = completed_channel_ledger(
            [Fraction(1, packet_count)] * packet_count,
            1,
            Fraction(3, 2),
            Fraction(1, 2) - Fraction(1, packet_count),
        )
        self.assertEqual(ledger.completed_amplitude, Fraction(1, packet_count))
        self.assertEqual(ledger.completed_square, Fraction(1, packet_count**2))
        self.assertEqual(ledger.closure_error, 0)
        self.assertEqual(ledger.packet_diagonal, Fraction(1, packet_count))
        self.assertEqual(
            ledger.packet_cross, Fraction(packet_count - 1, packet_count)
        )
        self.assertGreater(ledger.absolute_sector_sum, 1)

    def test_pointwise_packets_can_have_natural_coherent_cross_energy(self) -> None:
        for packet_count in (2, 11, 101):
            ledger = completed_channel_ledger(
                [Fraction(1, packet_count)] * packet_count, 0, 0, 0
            )
            self.assertEqual(ledger.packet_diagonal, Fraction(1, packet_count))
            self.assertEqual(
                ledger.packet_cross,
                Fraction(packet_count - 1, packet_count),
            )
            self.assertEqual(ledger.completed_square, 1)

    def test_frozen_top_box_passport_records_failure_of_scalar_import(self) -> None:
        passport = top_box_exponent_passport()
        self.assertEqual(passport.eta, Fraction(1, 100))
        self.assertEqual(passport.target_energy_exponent, Fraction(49, 50))
        self.assertEqual(passport.direct_energy_exponent, 1)
        self.assertEqual(passport.scalar_wright_exponent, Fraction(15, 8))
        self.assertEqual(passport.wright_excess_over_direct, Fraction(7, 8))
        self.assertTrue(passport.principal_high_k_witness_survives)

        collar = target_matched_collar_passport()
        self.assertEqual(collar.fourier_decay_order, 5)
        self.assertEqual(collar.target_field_exponent, Fraction(49, 100))
        self.assertEqual(collar.cofactor_exponent, Fraction(499, 500))
        self.assertEqual(
            collar.physical_quotient_exponent, Fraction(1, 500)
        )
        self.assertEqual(collar.numerator_exponent, Fraction(1, 400))
        self.assertEqual(
            collar.low_cofactor_error_exponent,
            collar.target_field_exponent,
        )
        self.assertEqual(
            collar.large_numerator_error_exponent,
            collar.target_field_exponent,
        )


if __name__ == "__main__":
    unittest.main()
