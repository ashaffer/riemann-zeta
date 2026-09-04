#!/usr/bin/env python3

from fractions import Fraction
import unittest

from candidate_strip_assembly_gate import (
    ALPHA_0,
    AssemblyHypotheses,
    D,
    GP_SURCHARGE,
    KAPPA_HOSTILE,
    KAPPA_PROMOTE,
    MAX_COUNTERFACTUAL_OD2_X_BILL,
    MAX_COUNTERFACTUAL_OD2_Y_BILL,
    OD2_EPSILON_FRONTIER,
    RESIDUAL_GP_BUDGET_AFTER_COUNTERFACTUAL_OD2,
    ZF_DELTA,
    asymptotic_cost_bounds_compatible,
    budgeted_gp_is_compatible,
    corrected_package_proves_strip,
    od2_closes_ch4,
    od2_dual_antenna_exponent,
    qp_promote_upper_exponent,
    same_packet_sign_contradiction,
    stated_gp_od2_ga2_package_proves_strip,
    zf_delta,
)


class CandidateStripAssemblyGateTests(unittest.TestCase):
    def test_zero_free_width_is_not_od2_slack(self) -> None:
        self.assertEqual(zf_delta(ALPHA_0), Fraction(1, 100))
        self.assertEqual(ZF_DELTA, Fraction(1, 100))
        self.assertNotEqual(ZF_DELTA, OD2_EPSILON_FRONTIER)

    def test_exact_od2_frontier(self) -> None:
        self.assertEqual(
            OD2_EPSILON_FRONTIER,
            Fraction(3_351_407_453, 3_300_000_000_000),
        )
        self.assertTrue(od2_closes_ch4(OD2_EPSILON_FRONTIER / 2))
        self.assertFalse(od2_closes_ch4(OD2_EPSILON_FRONTIER))
        self.assertFalse(od2_closes_ch4(Fraction(0)))

    def test_frontier_bill_has_simple_exact_form(self) -> None:
        self.assertEqual(MAX_COUNTERFACTUAL_OD2_Y_BILL, Fraction(13_699, 660_000))
        self.assertEqual(MAX_COUNTERFACTUAL_OD2_X_BILL, Fraction(13_699, 1_000_000))
        self.assertEqual(
            RESIDUAL_GP_BUDGET_AFTER_COUNTERFACTUAL_OD2,
            Fraction(2_338_451, 200_000_000),
        )
        self.assertGreater(RESIDUAL_GP_BUDGET_AFTER_COUNTERFACTUAL_OD2, 0)
        self.assertGreater(GP_SURCHARGE, MAX_COUNTERFACTUAL_OD2_X_BILL)

    def test_od2_and_promotion_have_opposite_polarity(self) -> None:
        eta = Fraction(1, 100_000)
        epsilon = OD2_EPSILON_FRONTIER / 2
        promotion_upper = qp_promote_upper_exponent(eta)
        dual_lower = od2_dual_antenna_exponent(epsilon)
        self.assertLess(promotion_upper, KAPPA_PROMOTE)
        self.assertGreater(dual_lower, KAPPA_HOSTILE)
        self.assertGreater(dual_lower, promotion_upper)
        self.assertFalse(
            asymptotic_cost_bounds_compatible(promotion_upper, dual_lower)
        )

    def test_bare_gp_positive_margin_does_not_pay_qp(self) -> None:
        tiny_gp_margin = Fraction(1, 1_000_000)
        self.assertFalse(budgeted_gp_is_compatible(tiny_gp_margin, KAPPA_PROMOTE))
        self.assertTrue(
            budgeted_gp_is_compatible(D * KAPPA_PROMOTE + Fraction(1, 10_000), KAPPA_PROMOTE)
        )

    def test_same_packet_is_logically_mandatory(self) -> None:
        upper = Fraction(1, 1000)
        lower = Fraction(1, 100)
        self.assertTrue(
            same_packet_sign_contradiction(upper, lower, same_packet=True)
        )
        self.assertFalse(
            same_packet_sign_contradiction(upper, lower, same_packet=False)
        )

    def test_stated_three_gates_do_not_close(self) -> None:
        self.assertFalse(stated_gp_od2_ga2_package_proves_strip())

    def test_corrected_conditional_package(self) -> None:
        complete = AssemblyHypotheses(
            low_height_base_case=True,
            budgeted_gp=True,
            qp_promote=True,
            ga2_scalar_reserve=True,
            same_packet_compatibility=True,
            gp_other_upper_fraction=Fraction(1, 1000),
            ga_reserve_lower_fraction=Fraction(1, 100),
        )
        self.assertTrue(corrected_package_proves_strip(complete))
        self.assertFalse(
            corrected_package_proves_strip(
                AssemblyHypotheses(
                    low_height_base_case=True,
                    budgeted_gp=True,
                    qp_promote=False,
                    ga2_scalar_reserve=True,
                    same_packet_compatibility=True,
                )
            )
        )


if __name__ == "__main__":
    unittest.main()
