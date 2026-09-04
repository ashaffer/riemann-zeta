#!/usr/bin/env python3

from fractions import Fraction
import unittest

import numpy as np

from same_packet_minimax_sync_gate import (
    D,
    GP_CORRECTION_ROOM_AT_PROMOTE_FRONTIER,
    GP_SURCHARGE,
    KAPPA_PROMOTE,
    PHASE_AVAILABLE_SQUARED_RADIUS,
    PHASE_REQUIRED_SQUARED_RADIUS,
    PHASE_THRESHOLD,
    QP_PROMOTE_X_BILL,
    TwoWitnessSlacks,
    common_observable_minimax,
    coherent_null_break_vectors,
    joint_budget_closes,
    joint_budget_margin,
    lag_autocorrelation,
    lag_one_matrix,
    lag_two_imag_matrix,
    lag_two_real_matrix,
    live_same_packet_hypothesis_closes_strip,
    phase_counterfixture_vectors,
    phase_joint_feasible,
    quadratic_value,
    scalarized_common_observable_value,
    same_observable_cross_margin,
    separate_witnesses_do_not_imply_joint_state,
)


class SamePacketMinimaxSyncTests(unittest.TestCase):
    def test_exact_joint_budget(self) -> None:
        self.assertEqual(QP_PROMOTE_X_BILL, D * KAPPA_PROMOTE)
        self.assertEqual(
            QP_PROMOTE_X_BILL,
            Fraction(2_975_003_361, 250_000_000_000),
        )
        self.assertEqual(
            GP_CORRECTION_ROOM_AT_PROMOTE_FRONTIER,
            Fraction(3_372_810_389, 250_000_000_000),
        )
        self.assertEqual(
            GP_CORRECTION_ROOM_AT_PROMOTE_FRONTIER,
            GP_SURCHARGE - QP_PROMOTE_X_BILL,
        )
        self.assertTrue(
            joint_budget_closes(
                GP_CORRECTION_ROOM_AT_PROMOTE_FRONTIER / 2,
                KAPPA_PROMOTE,
            )
        )
        self.assertFalse(
            joint_budget_closes(
                GP_CORRECTION_ROOM_AT_PROMOTE_FRONTIER,
                KAPPA_PROMOTE,
            )
        )
        self.assertEqual(
            joint_budget_margin(
                GP_CORRECTION_ROOM_AT_PROMOTE_FRONTIER,
                KAPPA_PROMOTE,
            ),
            0,
        )

    def test_two_witness_cross_slack_determinant(self) -> None:
        good = TwoWitnessSlacks(
            gp_own=Fraction(3, 5),
            ga_deficit_at_gp=Fraction(1, 5),
            gp_deficit_at_ga=Fraction(1, 4),
            ga_own=Fraction(1, 2),
        )
        self.assertTrue(good.synchronizable)
        interval = good.feasible_lambda_interval()
        self.assertIsNotNone(interval)
        assert interval is not None
        self.assertLessEqual(interval[0], interval[1])

        bad = TwoWitnessSlacks(
            gp_own=Fraction(1, 4),
            ga_deficit_at_gp=Fraction(3, 4),
            gp_deficit_at_ga=Fraction(3, 4),
            ga_own=Fraction(1, 4),
        )
        self.assertEqual(bad.determinant_margin, Fraction(-1, 2))
        self.assertFalse(bad.synchronizable)
        self.assertIsNone(bad.feasible_lambda_interval())
        self.assertEqual(
            same_observable_cross_margin(
                Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)
            ),
            Fraction(-1, 2),
        )

    def test_common_observable_minimax_is_negative(self) -> None:
        value, observable = common_observable_minimax(
            Fraction(1, 4), Fraction(3, 4)
        )
        self.assertEqual(observable, Fraction(1, 2))
        self.assertEqual(value, Fraction(-1, 4))
        self.assertEqual(
            scalarized_common_observable_value(
                Fraction(1, 2), Fraction(1, 4), Fraction(3, 4)
            ),
            Fraction(-1, 4),
        )
        # The two endpoint scalarizations are individually positive.
        self.assertEqual(
            scalarized_common_observable_value(
                Fraction(0), Fraction(1, 4), Fraction(3, 4)
            ),
            Fraction(1, 4),
        )
        self.assertEqual(
            scalarized_common_observable_value(
                Fraction(1), Fraction(1, 4), Fraction(3, 4)
            ),
            Fraction(1, 4),
        )

    def test_exact_phase_radius_obstruction(self) -> None:
        self.assertEqual(PHASE_REQUIRED_SQUARED_RADIUS, Fraction(8, 25))
        self.assertEqual(PHASE_AVAILABLE_SQUARED_RADIUS, Fraction(1, 4))
        self.assertGreater(
            PHASE_REQUIRED_SQUARED_RADIUS, PHASE_AVAILABLE_SQUARED_RADIUS
        )
        self.assertFalse(phase_joint_feasible(PHASE_THRESHOLD, PHASE_THRESHOLD))
        self.assertTrue(
            phase_joint_feasible(Fraction(1, 4), Fraction(1, 4))
        )
        self.assertTrue(separate_witnesses_do_not_imply_joint_state())

    def test_coherent_enrichment_can_break_qp_null(self) -> None:
        e, v, q = coherent_null_break_vectors()
        self.assertAlmostEqual(abs(lag_autocorrelation(e, 1)), 0.0)
        self.assertAlmostEqual(abs(lag_autocorrelation(v, 1)), 0.0)
        self.assertAlmostEqual(lag_autocorrelation(q, 1).real, 0.5)
        self.assertAlmostEqual(lag_autocorrelation(q, 1).imag, 0.0)

    def test_small_matrix_separate_phase_witnesses(self) -> None:
        q_gp, q_ga = phase_counterfixture_vectors()
        h_null = lag_one_matrix()
        h_real = lag_two_real_matrix()
        h_imag = lag_two_imag_matrix()
        for vector in (q_gp, q_ga):
            self.assertAlmostEqual(float(np.vdot(vector, vector).real), 1.0)
            self.assertAlmostEqual(quadratic_value(vector, h_null), 0.0)
            self.assertAlmostEqual(abs(lag_autocorrelation(vector, 1)), 0.0)
        self.assertAlmostEqual(quadratic_value(q_gp, h_real), 0.5)
        self.assertAlmostEqual(quadratic_value(q_gp, h_imag), 0.0)
        self.assertAlmostEqual(quadratic_value(q_ga, h_real), 0.0)
        self.assertAlmostEqual(quadratic_value(q_ga, h_imag), 0.5)
        self.assertAlmostEqual(lag_autocorrelation(q_gp, 2).real, 0.5)
        self.assertAlmostEqual(lag_autocorrelation(q_ga, 2).imag, 0.5)

    def test_strip_card_requires_joint_scalarization(self) -> None:
        complete = dict(
            qp_promote=True,
            compact_autocorrelation_factorization=True,
            full_scalarization_nonnegative=True,
            strict_joint_budget=True,
            reserve_gap_positive=True,
            low_height_closed=True,
        )
        self.assertTrue(live_same_packet_hypothesis_closes_strip(**complete))
        complete["full_scalarization_nonnegative"] = False
        self.assertFalse(live_same_packet_hypothesis_closes_strip(**complete))


if __name__ == "__main__":
    unittest.main()
