from fractions import Fraction
import unittest

from two_prime_global_trace_gate import (
    adjoint_law,
    alternating_pairing,
    connected_coefficient,
    connected_euler_jet,
    bridge_projections_commute,
    fake_global_supertrace,
    first_two_gamma_mode_sum,
    identity_metric,
    invariant_gram_pattern,
    minimal_all_place_labels,
    off_line_generator,
    on_line_generator,
    semilocal_3_5_fixture,
)


class TwoPrimeGlobalTraceGateTest(unittest.TestCase):
    def test_connected_jet_has_pure_terms_and_no_mixed_term(self) -> None:
        self.assertEqual(
            connected_euler_jet(),
            {(1, 0): Fraction(1), (2, 0): Fraction(1, 2),
             (0, 1): Fraction(1), (0, 2): Fraction(1, 2)},
        )
        self.assertEqual(connected_coefficient(1, 1), 0)
        self.assertEqual(connected_coefficient(7, 0), Fraction(1, 7))

    def test_mixed_15_is_inside_fixture_but_cancels(self) -> None:
        fixture = semilocal_3_5_fixture()
        self.assertEqual(fixture[3], (3, 1))
        self.assertEqual(fixture[9], (3, 2))
        self.assertEqual(fixture[5], (5, 1))
        self.assertEqual(fixture[25], (5, 2))
        self.assertIsNone(fixture[15])

    def test_functional_equation_duality_allows_off_line_pair(self) -> None:
        generator = off_line_generator(Fraction(2, 7))
        omega = alternating_pairing()
        self.assertEqual(adjoint_law(generator, omega), omega)

    def test_identity_metric_is_on_line_positive_control(self) -> None:
        generator = on_line_generator(Fraction(11, 13))
        identity = identity_metric()
        self.assertEqual(adjoint_law(generator, identity), identity)

    def test_noncommutative_bridge_is_supertrace_invisible(self) -> None:
        self.assertFalse(bridge_projections_commute())
        for length in range(1, 7):
            self.assertEqual(fake_global_supertrace("P" * length), 1)
            self.assertEqual(fake_global_supertrace("Q" * length), 1)
        for word in ("PQ", "QP", "PQP", "QPQ", "PPQQ", "PQQP"):
            self.assertEqual(fake_global_supertrace(word), 0)

    def test_equivariant_minimal_metric_has_no_cross_place_entries(self) -> None:
        pattern = invariant_gram_pattern(minimal_all_place_labels())
        self.assertEqual(
            pattern,
            [[i == j for j in range(6)] for i in range(6)],
        )

    def test_first_two_gamma_modes_are_fixed_exactly(self) -> None:
        # At tau=1: (1 - (1/4)/(1/16+1/4))
        #         +(1/2 - (5/4)/(25/16+1/4)) = 3/290.
        self.assertEqual(first_two_gamma_mode_sum(Fraction(1)), Fraction(3, 290))


if __name__ == "__main__":
    unittest.main()
