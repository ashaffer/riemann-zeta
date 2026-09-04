#!/usr/bin/env python3
"""Regression tests for the nonresonant SPF-tail information gate."""

from __future__ import annotations

import unittest
from fractions import Fraction

from spf_tail_large_sieve_gate import build_countermodel, exponent_ledger


class ExponentLedgerTests(unittest.TestCase):
    def test_square_function_stops_at_critical_aggregate(self) -> None:
        b = Fraction(799, 5000)
        kappa = Fraction(1974048259, 100000000000)
        ledger = exponent_ledger(b, kappa)
        self.assertEqual(ledger["proved_square_function_exponent"], str(2 - b))
        self.assertEqual(
            ledger["required_square_function_exponent"],
            str(2 - b - 2 * kappa),
        )
        self.assertEqual(ledger["fixed_power_energy_deficit"], str(2 * kappa))
        self.assertEqual(ledger["cauchy_aggregate_exponent"], "1")


class CoherentDeletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = build_countermodel(gap_count=30_000)

    def test_exact_certificates(self) -> None:
        self.assertTrue(all(self.payload["certificates"].values()))

    def test_gap_energy_is_near_linear(self) -> None:
        energy = self.payload["gap_energy"]
        self.assertEqual(energy["initial_G2_over_Y"], 10.0)
        self.assertLess(energy["final_G2_over_Y"], 11.0)

    def test_fixed_frequency_is_exceptional(self) -> None:
        spectrum = self.payload["finite_group_spectrum"]
        self.assertGreater(spectrum["selected_over_parseval_rms"], 5.0)
        self.assertGreater(spectrum["selected_over_fourth_mean_root"], 2.0)

    def test_stage_cauchy_can_be_nearly_sharp(self) -> None:
        stage = self.payload["stage_square_function"]
        self.assertGreater(stage["coherent_over_cauchy_bound"], 0.7)

    def test_power_saving_is_not_forced(self) -> None:
        deletion = self.payload["exact_deletion"]
        # The dimensionless value remains a visible constant in this finite
        # model, matching the asymptotic Y/log(P) obstruction.
        self.assertGreater(deletion["aggregate_times_logP_over_Y"], 0.08)


if __name__ == "__main__":
    unittest.main()
