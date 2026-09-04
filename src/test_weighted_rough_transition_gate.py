#!/usr/bin/env python3
"""Regression tests for the weighted rough-transition residue gate."""

from __future__ import annotations

import unittest
from fractions import Fraction

from weighted_rough_transition_gate import (
    B_MAX,
    B_MIN,
    KAPPA_MAX,
    THETA_GT,
    closure_exponent_ledger,
    finite_post_q_audit,
    linear_sieve_frontier,
    localized_sieve_parameter,
    simultaneous_stage_vectors,
)


class ComponentTransportTests(unittest.TestCase):
    def test_adjacent_deleted_run_is_exact(self) -> None:
        # The deleted points 3,5 form one run in the ordered active set.
        stage = simultaneous_stage_vectors([0, 2, 3, 5, 9, 12], [3, 5], 7)
        self.assertEqual(stage.deleted, 2)
        self.assertEqual(stage.components, 1)
        self.assertEqual(sum(stage.delta), 0)
        self.assertEqual(sum(stage.positive), sum(stage.negative))

    def test_q_first_does_not_change_later_spf_stages(self) -> None:
        payload = finite_post_q_audit()
        self.assertTrue(all(payload["certificates"].values()))
        self.assertGreater(payload["band"]["deleted_centres"], 0)
        self.assertEqual(payload["band"]["delta_mass"], 0)


class ExponentLedgerTests(unittest.TestCase):
    def test_bottom_and_top_sieve_parameters(self) -> None:
        bottom = linear_sieve_frontier(B_MIN)
        top = linear_sieve_frontier(B_MAX)
        self.assertEqual(bottom["s"], str(Fraction(6926, 1537)))
        self.assertEqual(top["s"], str(Fraction(67, 33)))
        self.assertTrue(bottom["lower_sieve_positive"])
        self.assertTrue(top["lower_sieve_positive"])
        self.assertFalse(bottom["fixed_s_gives_power_discrepancy"])
        self.assertFalse(top["fixed_s_gives_power_discrepancy"])

    def test_lower_sieve_thresholds(self) -> None:
        self.assertEqual(
            linear_sieve_frontier(B_MIN)["lower_u_threshold"],
            str(Fraction(2821, 10_000)),
        )

    def test_critical_block_has_no_per_prime_sieve_level(self) -> None:
        h = B_MAX
        self.assertEqual(
            localized_sieve_parameter(h, B_MIN, B_MIN),
            Fraction(-78842, 204421),
        )
        self.assertEqual(localized_sieve_parameter(h, B_MAX, B_MAX), -1)
        self.assertEqual(
            linear_sieve_frontier(B_MAX)["lower_u_threshold"],
            str(Fraction(100, 399)),
        )

    def test_l2_l4_close_at_same_target(self) -> None:
        delta = Fraction(1, 10_000)
        ledger = closure_exponent_ledger(KAPPA_MAX, delta)
        target = 1 - KAPPA_MAX - delta
        self.assertEqual(ledger["l2_output_exponent"], str(target))
        self.assertEqual(ledger["l4_output_exponent"], str(target))
        self.assertEqual(
            ledger["l2_current_deficit_at_delta_zero"],
            str(THETA_GT + 2 * KAPPA_MAX),
        )
        self.assertEqual(
            ledger["l4_current_deficit_at_delta_zero"],
            str(THETA_GT + 4 * KAPPA_MAX),
        )

    def test_injective_selector_l2_exponents(self) -> None:
        self.assertLess(1 - 2 * KAPPA_MAX, 1)
        self.assertLess(Fraction(63827, 65000), 1)
        self.assertEqual(
            1 - B_MAX + THETA_GT,
            Fraction(606001, 665000),
        )


if __name__ == "__main__":
    unittest.main()
