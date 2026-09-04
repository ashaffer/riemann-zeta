#!/usr/bin/env python3

import math
import unittest

from growing_jet_tchakaloff_barrier import (
    ALPHA,
    PICK_SURCHARGE,
    asymptotic_depth_ratio,
    inverse_phase_depth_barrier,
    log_monic_chebyshev_sup_bound,
    log_positive_spanning_inradius_upper_bound,
    log_vandermonde_condition_lower_bound,
    optimize_same_b_condition_charged_envelope,
    same_b_condition_charged_envelope,
    self_check,
    taylor_remainder_upper_bound,
    thin_rectangle_bernstein_tau,
)


class GrowingJetTchakaloffBarrierTests(unittest.TestCase):
    def test_inverse_phase_depth_is_linear(self) -> None:
        ratios = [
            inverse_phase_depth_barrier(r) / r
            for r in (1000, 10_000, 100_000)
        ]
        self.assertLess(ratios[0], ratios[1])
        self.assertLess(ratios[1], ratios[2])
        self.assertLess(ratios[2], asymptotic_depth_ratio())
        self.assertGreater(ratios[2], 1.11)

    def test_exact_ellipse_rectangle_identity(self) -> None:
        L, b, d = 200_000.0, 0.41, 0.66
        eta = 2 * math.pi / (b * d * L)
        tau = thin_rectangle_bernstein_tau(L, b, d)
        # The corner (1+i*eta) lies on the chosen ellipse.
        lhs = 1 / math.cosh(tau) ** 2 + eta**2 / math.sinh(tau) ** 2
        self.assertAlmostEqual(lhs, 1.0, places=11)

    def test_capacity_four_condition_rate(self) -> None:
        L, b = 2_000_000.0, 0.43
        for r in (10_000, 30_000):
            log_kappa = log_vandermonde_condition_lower_bound(r, L, b)
            self.assertGreater(log_kappa / r, 1.37)
            self.assertLess(log_kappa / r, math.log(4))
            self.assertAlmostEqual(
                log_kappa,
                -log_monic_chebyshev_sup_bound(r, L, b)
                - 0.5 * math.log(2),
                places=10,
            )
            self.assertLess(
                log_positive_spanning_inradius_upper_bound(r, L, b) / r,
                -1.37,
            )

    def test_condition_rate_tends_to_log_four(self) -> None:
        r = 20_000
        small = log_vandermonde_condition_lower_bound(r, 100_000, 0.43) / r
        large = log_vandermonde_condition_lower_bound(r, 10_000_000, 0.43) / r
        self.assertGreater(large, small)
        self.assertLess(large, math.log(4))

    def test_taylor_tail(self) -> None:
        self.assertAlmostEqual(taylor_remainder_upper_bound(4, 0.2), 0.0004)
        with self.assertRaises(ValueError):
            taylor_remainder_upper_bound(2, 1.0)

    def test_condition_charged_old_envelope_falls_below_budget(self) -> None:
        old_optimizer = 0.3268277905
        self.assertGreater(
            same_b_condition_charged_envelope(old_optimizer), 0.0039
        )
        optimum = optimize_same_b_condition_charged_envelope()
        self.assertAlmostEqual(optimum.horizontal, 0.43000979, places=6)
        self.assertAlmostEqual(optimum.exponent, 0.010934642, places=8)
        self.assertGreater(optimum.gap_below_surcharge, 0.014)
        self.assertLess(optimum.exponent, PICK_SURCHARGE)
        self.assertLess(optimum.horizontal, ALPHA)

    def test_self_check(self) -> None:
        out = self_check()
        self.assertFalse(out["uniform_subexponential_conditioning_possible"])
        self.assertFalse(out["gp_closed"])


if __name__ == "__main__":
    unittest.main()
