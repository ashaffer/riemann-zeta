#!/usr/bin/env python3
"""Tests for the selected-numerator SPF stage-energy laboratory."""

from __future__ import annotations

import math
import unittest

from spf_stage_energy_lab import StageEnergy, analyze_modulus, analyze_numerator


class SpfStageEnergyLabTests(unittest.TestCase):
    def test_stage_energy_norm_order(self) -> None:
        class Result:
            stages = {2: 3 + 4j, 3: -1j}
            deleted_by_stage = {2: 7, 3: 11}

        ledger = StageEnergy.from_primes(Result(), [2, 3])
        self.assertEqual(ledger.stage_count, 2)
        self.assertEqual(ledger.deleted, 18)
        self.assertEqual(ledger.coherent, 3 + 3j)
        self.assertAlmostEqual(ledger.energy, math.sqrt(26.0))
        self.assertAlmostEqual(ledger.variation, 6.0)
        self.assertLessEqual(abs(ledger.coherent), ledger.variation + 1e-12)

    def test_exact_telescope_partition(self) -> None:
        row = analyze_numerator(1_000, 1_400, 19, 5)
        self.assertLess(row["identity_error"], 1e-8)
        total_stages = (
            row["pre_q"]["stage_count"]
            + row["at_q"]["stage_count"]
            + row["post_q"]["stage_count"]
        )
        total_bins = sum(item["stage_count"] for item in row["post_q_bins"])
        self.assertGreater(total_stages, 0)
        self.assertEqual(total_bins, row["post_q"]["stage_count"])

    def test_scan_selects_existing_numerator(self) -> None:
        payload = analyze_modulus(1_000, 1_300, 11, (1, 3, 5))
        self.assertEqual(payload["numerator_count"], 3)
        self.assertIn(payload["worst_post_q"]["a"], {1, 3, 5})
        self.assertIn(payload["worst_final"]["a"], {1, 3, 5})
        self.assertEqual(len(payload["rows"]), 3)
        moments = payload["selected_numerator_moments"]["post_q"]
        self.assertGreaterEqual(moments["maximum_over_rms"], 1.0)
        self.assertLessEqual(
            moments["root_mean_powers"]["2"],
            moments["root_mean_powers"]["8"],
        )

    def test_invalid_numerator_rejected(self) -> None:
        with self.assertRaises(ValueError):
            analyze_modulus(1_000, 1_300, 11, (0,))


if __name__ == "__main__":
    unittest.main()
