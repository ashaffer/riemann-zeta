import unittest

import numpy as np

from r71_fixed_strip_moment_probe import (
    bohr_phase_moment_density,
    multiplicative_energy_moment_density,
)
from r71_pair_cell_probe import (
    atomic_pair_audit,
    audit_pair_sectors,
    build_pair_channel_system,
    exact_product_cell_audit,
    near_product_cell_audit,
    scan_pair_cells,
)


class CompletedPairCellTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.system = build_pair_channel_system(
            scale=127.0,
            cutoff=8,
            height=80.0,
            frequency_step=0.5,
            gaussian_order=12,
        )

    def test_unordered_pair_channels_reconstruct_the_completed_square(self) -> None:
        system = self.system
        self.assertEqual(system.channel_count, 10)
        self.assertEqual(system.pair_count, 55)
        self.assertLess(system.direct_square_completion_error, 1.0e-14)
        np.testing.assert_allclose(
            np.sum(system.pair_values, axis=1),
            system.completed_square,
            rtol=0.0,
            atol=1.0e-14,
        )

    def test_signed_tail_center_sector_ledger_is_exact(self) -> None:
        audit = audit_pair_sectors(self.system)
        ledger_sum = (
            audit.tail_tail_energy
            + audit.tail_center_energy
            + audit.center_center_energy
            + audit.tail_tail_tail_center_cross
            + audit.tail_tail_center_center_cross
            + audit.tail_center_center_center_cross
        )
        self.assertAlmostEqual(audit.completed_fourth_moment, ledger_sum)
        self.assertLess(audit.ledger_error, 1.0e-14)
        self.assertLess(audit.center_net_contribution, 0.0)
        self.assertGreater(
            audit.tail_tail_energy, audit.completed_fourth_moment
        )

    def test_atomic_and_exact_product_diagonals_match_both_comparators(self) -> None:
        system = self.system
        atomic = atomic_pair_audit(system)
        exact = exact_product_cell_audit(system)
        phase_density = bohr_phase_moment_density(system.channel_values, 4)
        multiplicative_density = multiplicative_energy_moment_density(
            system.channel_values,
            (*system.active_product_values, 1),
            4,
        )
        phase_integral = float(
            np.dot(system.integration_weights, phase_density)
        )
        multiplicative_integral = float(
            np.dot(system.integration_weights, multiplicative_density)
        )
        self.assertAlmostEqual(atomic.cell_diagonal, phase_integral)
        self.assertAlmostEqual(exact.cell_diagonal, multiplicative_integral)
        self.assertAlmostEqual(
            atomic.completed_to_cell_diagonal_ratio,
            1.6334823915,
            places=6,
        )
        self.assertAlmostEqual(
            exact.completed_to_cell_diagonal_ratio,
            1.5947043586,
            places=6,
        )

    def test_every_partition_obeys_the_exact_interference_identity(self) -> None:
        for audit in (
            atomic_pair_audit(self.system),
            exact_product_cell_audit(self.system),
            near_product_cell_audit(self.system, 0.01, 0.25),
        ):
            self.assertAlmostEqual(
                audit.completed_fourth_moment,
                audit.atomic_pair_diagonal
                + audit.within_cell_interference
                + audit.cross_cell_interference,
            )
            self.assertLess(audit.cell_completion_error, 1.0e-14)
            self.assertAlmostEqual(
                audit.cross_cell_interference,
                audit.positive_cross_cell_interference
                + audit.negative_cross_cell_interference,
            )

    def test_short_resolution_cells_and_positive_merge_are_falsified(self) -> None:
        scan = scan_pair_cells(
            scale=127.0,
            cutoff=8,
            height=80.0,
            frequency_step=0.5,
            cell_widths=(0.005, 0.01, 0.02, 0.04),
            offset_count=8,
            gaussian_order=12,
        )
        envelopes = {item.cell_width: item for item in scan.scale_envelopes}
        self.assertTrue(
            envelopes[0.01].domination_fails_at_every_sampled_offset
        )
        self.assertGreater(
            envelopes[0.01].minimum_completed_to_diagonal_ratio, 1.3
        )
        zero_offset = {
            audit.cell_width: audit
            for audit in scan.near_audits
            if audit.offset_fraction == 0.0
        }
        self.assertLess(
            zero_offset[0.01].cell_diagonal,
            zero_offset[0.005].cell_diagonal,
        )
        self.assertIn(
            "atomic pair-diagonal domination",
            scan.sampled_falsifications,
        )
        self.assertTrue(
            any(
                item.startswith("monotone nonnegative dyadic cell merging")
                for item in scan.sampled_falsifications
            )
        )

    def test_cell_parameters_are_validated(self) -> None:
        with self.assertRaises(ValueError):
            near_product_cell_audit(self.system, 0.0)
        with self.assertRaises(ValueError):
            near_product_cell_audit(self.system, 0.01, 1.0)
        with self.assertRaises(ValueError):
            scan_pair_cells(cell_widths=(0.02, 0.01))


if __name__ == "__main__":
    unittest.main()
