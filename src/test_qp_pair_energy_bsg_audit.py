from fractions import Fraction
import unittest

from qp_pair_energy_bsg_audit import (
    ap_islands_model,
    line_additive_energy,
    orientation_countermodel,
    orthogonal_antipode_model,
    pair_ledger,
    rank_two_gap_model,
    sum_matching_model,
)


class PairEnergyBSGAuditTests(unittest.TestCase):
    def test_exact_line_energy(self) -> None:
        for length in range(1, 20):
            direct = sum(
                (length - abs(delta)) ** 2
                for delta in range(-(length - 1), length)
            )
            self.assertEqual(line_additive_energy(length), direct)

    def test_pair_ledger_is_weaker_than_one_point(self) -> None:
        for cost in (2, 3, 10, 100):
            ledger = pair_ledger(cost)
            self.assertGreater(
                ledger.one_point_heavy_cell_lower,
                ledger.cell_l2_mass_lower,
            )
            self.assertGreaterEqual(
                ledger.normalized_good_pair_mass,
                Fraction(1, 2 * cost**2),
            )

    def test_bessel_saturated_positive_antipode(self) -> None:
        for cost in (2, 3, 10):
            model = orthogonal_antipode_model(cost)
            self.assertEqual(model.packet_types, cost**2)
            self.assertEqual(model.antipode_depth, Fraction(1, cost))
            self.assertEqual(model.good_pair_probability, Fraction(1, cost**2))
            self.assertEqual(model.unnormalized_good_pair_mass, 1)
            self.assertEqual(model.normalized_off_diagonal_kernel, 0)
            self.assertEqual(model.one_point_exceptional_probability, 1)

    def test_ap_islands_saturate_all_scales(self) -> None:
        for cost in (2, 3, 10):
            model = ap_islands_model(cost)
            self.assertEqual(model.islands, cost**2)
            self.assertEqual(model.good_pair_probability, Fraction(1, cost**2))
            self.assertEqual(model.mass_per_island, Fraction(1, cost**2))
            self.assertLessEqual(model.allowed_within_difference_count, cost**4)
            self.assertEqual(model.difference_span_rank, cost**2)
            self.assertFalse(model.contained_in_rank_one_progression)

            # The normalized energy is on the claimed C^-8 scale, up to
            # harmless absolute constants for every tested C.
            scaled = model.weighted_additive_energy * cost**8
            self.assertGreater(scaled, Fraction(1, 10))
            self.assertLess(scaled, 10)

    def test_rank_two_gap_is_not_rank_one(self) -> None:
        model = rank_two_gap_model(8)
        self.assertEqual(model.support_size, 64)
        self.assertEqual(model.sumset_size, 225)
        self.assertEqual(model.difference_span_rank, 2)
        self.assertFalse(model.contained_in_rank_one_progression)
        self.assertGreater(model.energy_density, Fraction(1, 4))

    def test_sum_branch_can_be_only_a_matching(self) -> None:
        model = sum_matching_model(49)
        self.assertEqual(model.edge_count, 49)
        self.assertEqual(model.edge_density, Fraction(1, 49))
        self.assertEqual(model.restricted_sumset_size, 1)
        self.assertEqual(model.connected_component_size, 2)

    def test_pair_geometry_does_not_orient_antipode(self) -> None:
        model = orientation_countermodel()
        self.assertEqual(model.represented_carrier, 1)
        self.assertEqual(model.total_variation, 2)
        self.assertGreater(model.kernel_value, model.kernel_threshold)
        self.assertFalse(model.convex_hull_hits_negative_carrier_ray)


if __name__ == "__main__":
    unittest.main()
