#!/usr/bin/env python3

import cmath
import math
import unittest
from fractions import Fraction

from same_packet_conditional_covariance_gate import (
    TwoChannelLedger,
    clean_power_residues,
    contact_leading_coefficient,
    direct_two_channel_reserve,
    phase_optimized_two_channel_reserve,
    polarize_cross_entry,
    transverse_scale_floor,
)


class SamePacketConditionalCovarianceGateTests(unittest.TestCase):
    def test_all_finite_powers_locally_linearize(self) -> None:
        for degree in range(1, 11):
            nonlinear, linearized = clean_power_residues(
                degree,
                multiplicity=2,
                analytic_germ=[Fraction(3, 5), Fraction(-7, 11), Fraction(13, 17)],
                test_tail=[Fraction(19, 23), Fraction(-29, 31)],
            )
            self.assertEqual(nonlinear, linearized)

    def test_positive_polynomial_covariance_keeps_contact(self) -> None:
        degree, coefficient = contact_leading_coefficient(
            [[1, 1j, 2 - 3j], [4, -2], [9]], [2.0, 3.0, 5.0], multiplicity=3
        )
        self.assertEqual(degree, 2)
        self.assertGreater(coefficient, 0)

    def test_contact_free_positive_covariance_is_constant(self) -> None:
        degree, coefficient = contact_leading_coefficient(
            [[1], [2 + 3j], [-4]], [1.0, 2.0, 4.0]
        )
        self.assertEqual(degree, 0)
        self.assertGreater(coefficient, 0)

    def test_two_channel_phase_maximum(self) -> None:
        eta, r, c, z = 0.61, -3.0, 8.0, -5 + 12j
        maximum, phase = phase_optimized_two_channel_reserve(eta, r, c, z)
        self.assertAlmostEqual(
            maximum, direct_two_channel_reserve(eta, r, c, z, phase)
        )
        for offset in (0.2, 0.7, 1.4, 2.9):
            self.assertLessEqual(
                direct_two_channel_reserve(eta, r, c, z, phase + offset),
                maximum + 1e-12,
            )

    def test_polarization(self) -> None:
        q_e, q_v, z = 2.0, 7.0, 4 - 9j
        q_plus = q_e + q_v + 2 * z.real
        q_minus = q_e + q_v - 2 * z.real
        q_plus_i = q_e + q_v - 2 * z.imag
        q_minus_i = q_e + q_v + 2 * z.imag
        self.assertAlmostEqual(
            abs(polarize_cross_entry(q_plus, q_minus, q_plus_i, q_minus_i) - z),
            0.0,
        )

    def test_transverse_floor_is_necessary(self) -> None:
        eta, epsilon, carrier, r = 0.8, 0.1, 100.0, 0.0
        floor = transverse_scale_floor(eta, epsilon, carrier, r)
        denominator = (1 - eta) + 2 * math.sqrt(eta * (1 - eta))
        self.assertAlmostEqual(floor * denominator, epsilon * eta * carrier)

    def test_isolated_block_never_closes_strict_gate(self) -> None:
        ledger = TwoChannelLedger(
            eta=0.7, epsilon=0.01, carrier=10.0, r=0.0, c=0.0, z=0j
        )
        self.assertFalse(ledger.closes_algebraic_gate())


if __name__ == "__main__":
    unittest.main()
