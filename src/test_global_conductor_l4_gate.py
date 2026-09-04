from fractions import Fraction
import math
import unittest

from flint import arb, ctx
import numpy as np

from global_conductor_l4_gate import (
    CONDUCTOR_GAIN,
    L2_SAVING,
    MOMENT_DECAY,
    OUTPUT_SAVING,
    PERSISTENCE_DECAY,
    REQUIRED_GAIN,
    STRICT_MARGIN,
    TAIL_SAVING,
    THETA,
    certified_physical_gap_mask,
    four_distinct_integrand,
    four_distinct_sharp_moment,
    four_distinct_trapezoid,
    ledger_closes_conditionally,
    l4_trapezoid,
    retained_hat_vector_from_arb_nodes,
    required_conductor_gain,
    sign_morphology_trapezoid,
)
from prime_log_hat_tail import hat_vector_from_arb_nodes


class GlobalConductorL4GateTests(unittest.TestCase):
    def test_exact_ledger(self) -> None:
        self.assertEqual(THETA, Fraction(161, 1000))
        self.assertEqual(TAIL_SAVING, Fraction(249, 13000))
        self.assertEqual(L2_SAVING, Fraction(2789, 3250))
        self.assertEqual(MOMENT_DECAY, Fraction(1187, 13000))
        self.assertEqual(PERSISTENCE_DECAY, Fraction(171, 2000))
        self.assertEqual(STRICT_MARGIN, Fraction(151, 26000))
        self.assertEqual(REQUIRED_GAIN, Fraction(9599, 26000))
        self.assertEqual(CONDUCTOR_GAIN - REQUIRED_GAIN, STRICT_MARGIN)
        self.assertEqual(OUTPUT_SAVING, Fraction(1187, 58500))
        self.assertEqual(
            required_conductor_gain(THETA, Fraction(19, 1000)),
            REQUIRED_GAIN,
        )
        self.assertTrue(ledger_closes_conditionally())

    def test_all_edges_recover_original_hat_vector(self) -> None:
        ctx.prec = 160
        nodes = tuple(arb(value) / 100 for value in (-19, -7, 3, 18))
        original = hat_vector_from_arb_nodes(nodes)
        retained = retained_hat_vector_from_arb_nodes(nodes, (True, True, True))
        for left, right in zip(original.weights, retained.weights):
            self.assertAlmostEqual(float(left.mid()), float(right.mid()), places=14)
        self.assertAlmostEqual(
            float(original.truncated_mass.mid()),
            float(retained.retained_mass.mid()),
            places=14,
        )

    def test_rejected_edge_loses_both_endpoint_shares(self) -> None:
        ctx.prec = 160
        nodes = tuple(arb(value) / 100 for value in (-19, -7, 3, 18))
        retained = retained_hat_vector_from_arb_nodes(
            nodes,
            (False, True, False),
        )
        self.assertEqual(retained.active_count, 2)
        self.assertEqual(float(retained.weights[0].mid()), 0.0)
        self.assertGreater(float(retained.weights[1].mid()), 0.0)
        self.assertGreater(float(retained.weights[2].mid()), 0.0)
        self.assertEqual(float(retained.weights[3].mid()), 0.0)
        self.assertAlmostEqual(sum(retained.float_weights), 1.0, places=14)

    def test_frozen_first_scale_mask_keeps_only_twin_edges(self) -> None:
        primes = (421, 431, 433, 439, 443, 449, 457, 461, 463)
        mask, cutoff = certified_physical_gap_mask(Fraction(1025, 2), primes)
        retained_gaps = [
            right - left
            for left, right, keep in zip(primes, primes[1:], mask)
            if keep
        ]
        self.assertGreater(float(cutoff.mid()), 2.0)
        self.assertLess(float(cutoff.mid()), 4.0)
        self.assertEqual(retained_gaps, [2, 2])

    def test_trapezoid_integrates_constant_polynomial(self) -> None:
        value = l4_trapezoid(
            np.array([0.0]),
            np.array([1.0]),
            3.25,
            104.75,
            maximum_step=2.0,
        )
        self.assertAlmostEqual(value, 101.5, places=12)
        morphology = sign_morphology_trapezoid(
            np.array([0.0]),
            np.array([1.0]),
            3.25,
            104.75,
        )
        self.assertAlmostEqual(morphology["complex_l4"], 101.5, places=12)
        self.assertAlmostEqual(morphology["real_l4"], 101.5, places=12)
        self.assertEqual(morphology["negative_real_l4"], 0.0)

    def test_trapezoid_matches_two_frequency_closed_form(self) -> None:
        # F(t)=cos(a t), so cos^4(x)=(3+4cos(2x)+cos(4x))/8.
        a = 0.17
        left, right = 2.3, 901.7
        numeric = l4_trapezoid(
            np.array([-a, a]),
            np.array([0.5, 0.5]),
            left,
            right,
            maximum_step=0.25,
        )

        def antiderivative(t: float) -> float:
            return (
                3 * t / 8
                + math.sin(2 * a * t) / (4 * a)
                + math.sin(4 * a * t) / (32 * a)
            )

        exact = antiderivative(right) - antiderivative(left)
        self.assertLess(abs(numeric - exact) / exact, 2e-5)

    def test_four_distinct_matches_direct_ordered_expansion(self) -> None:
        nodes = np.array([-0.18, -0.04, 0.07, 0.16])
        weights = np.array([0.11, 0.23, 0.29, 0.37])
        left, right = 17.0, 93.0
        isolated = four_distinct_sharp_moment(
            nodes,
            weights,
            left,
            right,
            block_size=2,
        )
        direct = 0.0 + 0.0j
        for p in range(4):
            for r in range(4):
                for q in range(4):
                    for s in range(4):
                        if len({p, r, q, s}) != 4:
                            continue
                        omega = nodes[p] + nodes[r] - nodes[q] - nodes[s]
                        kernel = (
                            (right - left)
                            * np.sinc(omega * (right - left) / (2 * math.pi))
                            * np.exp(1j * omega * (right + left) / 2)
                        )
                        direct += weights[p] * weights[r] * weights[q] * weights[s] * kernel
        self.assertAlmostEqual(isolated, direct.real, places=12)
        self.assertAlmostEqual(direct.imag, 0.0, places=12)

    def test_fast_pointwise_four_distinct_identity(self) -> None:
        nodes = np.array([-0.18, -0.04, 0.07, 0.16, 0.19])
        weights = np.array([0.07, 0.13, 0.21, 0.25, 0.34])
        times = np.array([0.0, 2.75, 19.0, 113.5])
        fast = four_distinct_integrand(nodes, weights, times)
        direct = []
        for time in times:
            value = 0.0 + 0.0j
            for p in range(len(nodes)):
                for r in range(len(nodes)):
                    for q in range(len(nodes)):
                        for s in range(len(nodes)):
                            if len({p, r, q, s}) != 4:
                                continue
                            value += (
                                weights[p]
                                * weights[r]
                                * weights[q]
                                * weights[s]
                                * np.exp(
                                    1j
                                    * time
                                    * (nodes[p] + nodes[r] - nodes[q] - nodes[s])
                                )
                            )
            direct.append(value.real)
            self.assertAlmostEqual(value.imag, 0.0, places=12)
        np.testing.assert_allclose(fast, direct, rtol=1e-12, atol=1e-12)

    def test_fast_integral_matches_pair_kernel(self) -> None:
        nodes = np.array([-0.18, -0.04, 0.07, 0.16, 0.19])
        weights = np.array([0.07, 0.13, 0.21, 0.25, 0.34])
        left, right = 17.0, 593.0
        kernel_value = four_distinct_sharp_moment(
            nodes,
            weights,
            left,
            right,
        )
        trapezoid_value = four_distinct_trapezoid(
            nodes,
            weights,
            left,
            right,
            maximum_step=0.1,
        )
        self.assertLess(
            abs(kernel_value - trapezoid_value) / max(1.0, abs(kernel_value)),
            2e-5,
        )


if __name__ == "__main__":
    unittest.main()
