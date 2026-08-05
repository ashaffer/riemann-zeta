from fractions import Fraction
import unittest

from quantized_phase_index_gate import (
    aligned_phase_angle_capacity,
    literal_local_k1_degree,
    literal_log_b2_partial_variance,
    literal_quotient_b2_norm_squared,
    normalized_quartet_deviation_bound,
    quartet_expansion,
    quartet_factor,
    quartet_shifted_winding,
    right_phase_log_b2_partial_variance,
    right_phase_tail_b2_distance_squared,
    right_shift_local_phase,
    shifted_strip_winding,
)


class QuantizedPhaseIndexGateTest(unittest.TestCase):
    def test_quartet_expansion_and_real_axis_positivity_are_exact(self) -> None:
        gamma = Fraction(7, 3)
        delta = Fraction(2, 5)
        for x in (Fraction(-11, 7), Fraction(0), Fraction(13, 9)):
            self.assertEqual(
                quartet_factor(x, gamma, delta),
                quartet_expansion(x, gamma, delta),
            )
            self.assertGreater(quartet_factor(x, gamma, delta), 0)

    def test_remote_quartet_bound_controls_complex_disk(self) -> None:
        radius = 3.0
        gamma = 100.0
        delta = 0.4
        scale = gamma * gamma + delta * delta
        bound = normalized_quartet_deviation_bound(radius, gamma, delta)
        for z in (3.0, -3.0, 3j, 1.8 + 2.4j):
            deviation = abs(quartet_factor(z, gamma, delta) / scale ** 2 - 1)
            self.assertLessEqual(deviation, bound + 1e-15)

    def test_shifted_phase_counts_roots_in_the_open_strip(self) -> None:
        delta = Fraction(2, 5)
        self.assertEqual(quartet_shifted_winding(delta / 2, delta), 0)
        self.assertEqual(quartet_shifted_winding(2 * delta, delta), 4)
        self.assertEqual(
            shifted_strip_winding(Fraction(1),
                                  (Fraction(0), Fraction(3, 2), Fraction(-2))),
            1,
        )
        with self.assertRaises(ValueError):
            quartet_shifted_winding(delta, delta)

    def test_literal_finite_prime_loop_is_null_in_relevant_range(self) -> None:
        self.assertEqual(literal_local_k1_degree(Fraction(1, 100)), 0)
        self.assertEqual(literal_local_k1_degree(Fraction(49, 100)), 0)
        self.assertEqual(literal_local_k1_degree(Fraction(3, 4)), 1)
        with self.assertRaises(ValueError):
            literal_local_k1_degree(Fraction(1, 2))

    def test_right_shift_local_phase_contracts_through_unit_phases(self) -> None:
        for p in (2, 3, 5, 29):
            for z in (1 + 0j, -1 + 0j, 1j, -1j):
                self.assertEqual(right_shift_local_phase(p, 0.2, z, 0), 1)
                for time in (0.25, 0.5, 1.0):
                    self.assertAlmostEqual(
                        abs(right_shift_local_phase(p, 0.2, z, time)),
                        1.0,
                        places=13,
                    )

    def test_two_limit_topologies_separate_numerically(self) -> None:
        # These bounded fixtures only guard the coefficient formulas.  The
        # divergence/convergence statements themselves are analytic proofs.
        literal_small = literal_log_b2_partial_variance(0.25, 100)
        literal_large = literal_log_b2_partial_variance(0.25, 5000)
        right_small = right_phase_log_b2_partial_variance(0.25, 100)
        right_large = right_phase_log_b2_partial_variance(0.25, 5000)
        self.assertGreater(literal_large, literal_small)
        self.assertGreater(right_large, right_small)
        self.assertGreater(literal_large - literal_small,
                           right_large - right_small)
        self.assertGreater(
            literal_quotient_b2_norm_squared(0.25, 5000),
            literal_quotient_b2_norm_squared(0.25, 100),
        )
        self.assertLess(
            right_phase_tail_b2_distance_squared(0.25, 1000, 5000),
            right_phase_tail_b2_distance_squared(0.25, 100, 5000),
        )

    def test_aligned_phase_capacity_grows_in_nonuniform_range(self) -> None:
        self.assertGreater(
            aligned_phase_angle_capacity(0.25, 5000),
            aligned_phase_angle_capacity(0.25, 100),
        )


if __name__ == "__main__":
    unittest.main()
