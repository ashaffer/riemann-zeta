import math
import unittest

import numpy as np

from hypocoercive_thomson_probe import (
    audit_common_laurent_residue,
    audit_cutoff_dirac,
    audit_hypocoercive_transport,
    audit_thomson_incidence,
    center_scale_generator,
    controlled_row_closure,
    coordinate_dilation_edges,
    enumerate_vaughan_assignments,
    fiber_projection,
    prime_pair_bottleneck,
    ratio_fiber_audit,
    skew_edge_generator,
)


class HypocoerciveThomsonProbeTests(unittest.TestCase):
    def test_exact_completed_cutoff_dirac_leaves_common_carrier(self) -> None:
        audit = audit_cutoff_dirac()
        self.assertEqual(audit.cutoffs, (2, 3))
        self.assertEqual(audit.bracket_nullity, audit.quadrature_points)
        self.assertEqual(audit.skew_error, 0.0)
        self.assertEqual(audit.exact_cutoff_difference_norm, 0.0)
        self.assertEqual(audit.common_carrier_residual, 0.0)
        self.assertGreater(audit.approximate_cutoff_difference_norm, 0.08)
        self.assertLess(audit.source_identity_error, 2.0e-14)
        self.assertAlmostEqual(
            audit.approximate_cutoff_difference_norm,
            audit.euler_difference_norm,
            places=14,
        )

    def test_assignment_dissipator_and_edges_are_exact(self) -> None:
        states = enumerate_vaughan_assignments(4, 64)
        dissipator = fiber_projection(states)
        edges = coordinate_dilation_edges(states, 64)
        self.assertEqual(len(states), 17)
        self.assertEqual(len(edges), 3)
        np.testing.assert_allclose(dissipator.T, dissipator, atol=0.0)
        np.testing.assert_allclose(
            dissipator @ dissipator, dissipator, atol=2.0e-16
        )
        for edge in edges:
            generator = skew_edge_generator(len(states), edge)
            np.testing.assert_allclose(
                generator.T, -generator, atol=0.0
            )
            lower = states[edge.lower]
            upper = states[edge.upper]
            lower_coordinates = (
                lower.divisor,
                lower.mangoldt_index,
                lower.cofactor,
            )
            upper_coordinates = (
                upper.divisor,
                upper.mangoldt_index,
                upper.cofactor,
            )
            ratios = [
                upper_value / lower_value
                for lower_value, upper_value in zip(
                    lower_coordinates, upper_coordinates
                )
            ]
            self.assertEqual(sum(value != 1.0 for value in ratios), 1)
            self.assertIn(float(edge.prime), ratios)
        _, ranks = controlled_row_closure(dissipator, edges)
        self.assertEqual(ranks, (3, 4, 5))

    def test_controlled_dilation_closure_misses_grouped_mode(self) -> None:
        audit = audit_hypocoercive_transport()
        self.assertEqual(audit.active_products, (55, 56, 60))
        self.assertEqual(audit.closure_rank, 5)
        self.assertEqual(audit.nullity, 12)
        self.assertEqual(audit.regrouping_error, 0.0)
        self.assertEqual(audit.dissipator_projection_error, 0.0)
        self.assertEqual(audit.maximum_skew_error, 0.0)
        self.assertGreater(audit.raw_uncontrolled_fraction, 0.972)
        self.assertAlmostEqual(
            audit.coherent_raw_uncontrolled_fraction, 1.0, places=14
        )

    def test_larger_dilation_closure_replication(self) -> None:
        audit = audit_hypocoercive_transport(
            scale=205.0, cutoff=7, step=0.03
        )
        self.assertEqual(audit.assignments, 45)
        self.assertEqual(audit.dilation_edges, 11)
        self.assertEqual(audit.closure_ranks, (9, 13, 17))
        self.assertEqual(audit.nullity, 28)
        self.assertGreater(audit.raw_uncontrolled_fraction, 0.932)
        self.assertGreater(
            audit.coherent_raw_uncontrolled_fraction, 0.992
        )

    def test_factor_ratio_bracket_and_prime_square_null(self) -> None:
        frequency = 0.2
        audit = ratio_fiber_audit(5, 7, frequency)
        twist = frequency * math.log(7.0 / 5.0)
        self.assertEqual(audit.assignments, 2)
        self.assertEqual(audit.bracket_rank, 2)
        self.assertAlmostEqual(
            audit.bracket_eigenvalues[0], twist * twist, places=14
        )
        self.assertAlmostEqual(audit.bracket_eigenvalues[1], 1.0, places=14)
        expected_gap = (1.0 - math.sqrt(1.0 - 4.0 * twist * twist)) / 2.0
        self.assertAlmostEqual(audit.generator_gap, expected_gap, places=14)

        square = ratio_fiber_audit(97, 97, frequency)
        self.assertEqual(square.assignments, 1)
        self.assertEqual(square.dissipator_rank, 0)
        self.assertEqual(square.bracket_rank, 0)
        self.assertEqual(square.generator_gap, 0.0)

    def test_near_prime_ratio_gap_collapses(self) -> None:
        low = prime_pair_bottleneck(1000, 14.134725141734693)
        high = prime_pair_bottleneck(10000, 14.134725141734693)
        self.assertLess(high.log_ratio, low.log_ratio)
        self.assertLess(high.generator_gap, low.generator_gap / 100.0)
        self.assertGreater(high.coherent_weight_fraction, 0.999999999)

    def test_positive_thomson_network_forgets_mobius_orientations(self) -> None:
        audit = audit_thomson_incidence()
        self.assertEqual(audit.assignments, 20)
        self.assertEqual(audit.mobius_inverse_error, 0.0)
        self.assertEqual(audit.tail_regrouping_error, 0.0)
        self.assertEqual(audit.divergence_error, 0.0)
        self.assertEqual(audit.orientation_laplacian_error, 0.0)
        self.assertLess(audit.vaughan_completion_error, 5.0e-15)
        self.assertLess(audit.mellin_identity_error, 1.0e-14)
        self.assertLess(audit.fiber_formula_error, 1.0e-14)
        self.assertLess(
            audit.minimum_flow_energy, audit.canonical_flow_energy
        )

    def test_every_finite_cutoff_has_same_zero_residue(self) -> None:
        audit = audit_common_laurent_residue()
        self.assertLess(audit.maximum_unit_residue_error, 5.0e-6)
        for residue in audit.residues:
            self.assertLess(abs(residue + 1.0), 5.0e-6)

    def test_rank_two_center_drift_cannot_be_positive_metric_skew(self) -> None:
        generator = center_scale_generator()
        self.assertAlmostEqual(float(np.trace(generator)), 1.0)
        critical = generator - 0.5 * np.eye(2)
        self.assertGreater(float(np.linalg.norm(critical)), 0.0)
        np.testing.assert_allclose(critical @ critical, 0.0, atol=0.0)
        # A positive-metric skew operator is similar to a skew-Hermitian
        # matrix and hence diagonalizable.  This nonzero nilpotent is not.
        self.assertEqual(np.linalg.matrix_rank(critical), 1)


if __name__ == "__main__":
    unittest.main()
