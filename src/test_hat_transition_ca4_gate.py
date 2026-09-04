from fractions import Fraction
import unittest

from hat_transition_ca4_gate import (
    CA4_L2_SAVING,
    CA4_OUTPUT_SAVING,
    CA4_TAIL_SAVING,
    TARGET,
    TRANSITION_SAVING,
    TRANSITION_THETA,
    TRANSITION_TIME,
    ca4_pointwise_saving,
    gt_tail_saving,
    ledger_closes_target,
    peano_saving,
    retained_l2_saving,
)


class HatTransitionCA4GateTests(unittest.TestCase):
    def test_retuned_transition_exact_values(self) -> None:
        self.assertEqual(TRANSITION_THETA, Fraction(201, 1250))
        self.assertEqual(TRANSITION_TIME, Fraction(1049, 1250))
        self.assertEqual(TRANSITION_SAVING, Fraction(309, 16250))
        self.assertEqual(
            peano_saving(TRANSITION_THETA, TRANSITION_TIME),
            TRANSITION_SAVING,
        )
        self.assertEqual(TRANSITION_SAVING - TARGET, Fraction(1, 65000))

    def test_ca4_exact_values(self) -> None:
        theta = Fraction(163, 1000)
        self.assertEqual(gt_tail_saving(theta), Fraction(267, 13000))
        self.assertEqual(retained_l2_saving(theta), Fraction(2787, 3250))
        self.assertEqual(CA4_TAIL_SAVING, Fraction(267, 13000))
        self.assertEqual(CA4_L2_SAVING, Fraction(2787, 3250))
        self.assertEqual(CA4_OUTPUT_SAVING, Fraction(10717, 536250))
        self.assertEqual(
            ca4_pointwise_saving(theta, Fraction(1, 10)) - TARGET,
            Fraction(2113, 2145000),
        )

    def test_every_adapter_has_strict_slack(self) -> None:
        self.assertTrue(ledger_closes_target())

    def test_outside_gt_branch_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            gt_tail_saving(Fraction(1, 10))


if __name__ == "__main__":
    unittest.main()
