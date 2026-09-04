import unittest

import numpy as np

from pick_halfdisk_probe import (
    affine_jet_obstruction_data,
    affine_jet_normals,
    affine_pick_lmi,
    alternating_lattice_configuration,
    alternating_lattice_inner,
    cauchy_kernel,
    odd_half_cell_configuration,
    phase_margins,
    pick_matrix,
    probe_halfdisk_extremal_barrier,
    pseudohyperbolic_distance,
    symmetric_opposite_pair_extremal,
    zero_blashke_target,
)


class PickHalfdiskProbeTests(unittest.TestCase):
    def test_affine_lmi_matches_pick_schur_complement(self) -> None:
        nodes = np.array([1.2, 0.9 + 0.4j, 1.1 - 0.7j])
        values = np.array([0.2, -0.1 + 0.15j, 0.05 - 0.2j])
        kernel = cauchy_kernel(nodes)
        lmi = affine_pick_lmi(nodes, values)
        count = len(nodes)
        schur = lmi[:count, :count] - lmi[:count, count:] @ np.linalg.solve(
            lmi[count:, count:], lmi[count:, :count]
        )
        np.testing.assert_allclose(schur, pick_matrix(nodes, values), atol=2e-15)
        np.testing.assert_allclose(lmi, lmi.conj().T, atol=2e-15)
        self.assertTrue(np.all(np.linalg.eigvalsh(kernel) > 0))

    def test_exact_hostile_conjugate_pair(self) -> None:
        depth = 2.0
        ordinate = np.pi
        exact, t_star = symmetric_opposite_pair_extremal(depth, ordinate)
        exact_nodes = np.array(
            [depth, depth + 1j * ordinate, depth - 1j * ordinate]
        )
        exact_values = np.array([exact, -1j * t_star, 1j * t_star])
        exact_pick = pick_matrix(exact_nodes, exact_values)
        self.assertGreaterEqual(float(np.min(np.linalg.eigvalsh(exact_pick))), -2e-15)
        self.assertAlmostEqual(float(np.linalg.det(exact_pick).real), 0.0, places=13)
        collateral, phases = odd_half_cell_configuration(depth, [0])
        result = probe_halfdisk_extremal_barrier(
            depth, collateral, phases, final_barrier=1e-6
        )
        self.assertLess(abs(result.target_amplitude - exact), 5e-5)
        self.assertGreaterEqual(result.dual_upper_bound + 1e-12, exact)
        self.assertLess(result.dual_upper_bound - exact, 2e-4)
        self.assertGreater(t_star, 0)
        self.assertGreater(exact, zero_blashke_target(depth, collateral))

    def test_five_point_affine_jet_positive_dependence(self) -> None:
        normals, weights = affine_jet_normals()
        np.testing.assert_allclose(weights @ normals, np.zeros(4), atol=2e-14)
        self.assertTrue(np.all(weights > 0))
        self.assertAlmostEqual(np.linalg.det(normals[:4]), 9 * np.pi**2 / 4, places=12)
        self.assertEqual(np.linalg.matrix_rank(normals), 4)

    def test_five_point_fixture_has_the_claimed_phases_and_center_cost(self) -> None:
        alpha = 0.45
        length = 80.0
        cell_index = 3
        d = 2.0 / 3.0
        target, nodes, phases, center = affine_jet_obstruction_data(
            alpha, length, cell_index, separation_ratio=d
        )
        physical_phases = d * length * (-nodes.imag)
        np.testing.assert_allclose(
            np.exp(-1j * physical_phases), np.exp(-1j * phases), atol=2e-14
        )
        self.assertEqual(target, complex(alpha))
        self.assertAlmostEqual(center.real, alpha)
        rho = pseudohyperbolic_distance(target, center)
        expected = abs(center.imag) / np.sqrt(4 * alpha**2 + center.imag**2)
        self.assertAlmostEqual(rho, expected, places=15)

    def test_exact_alternating_half_density_inner_function(self) -> None:
        depth = 4.0
        nodes, phases = alternating_lattice_configuration(depth, range(-6, 7))
        values = np.array([alternating_lattice_inner(z, depth) for z in nodes])
        margins = phase_margins(values, phases)
        self.assertGreaterEqual(float(np.min(margins)), -2e-14)
        even_cells = np.arange(-6, 7) % 2 == 0
        np.testing.assert_allclose(values[even_cells], 0.0, atol=2e-14)
        boundary = np.array(
            [alternating_lattice_inner(1j * y, depth) for y in np.linspace(-7, 7, 9)]
        )
        np.testing.assert_allclose(np.abs(boundary), 1.0, atol=2e-14)
        target = alternating_lattice_inner(depth, depth)
        self.assertAlmostEqual(target.imag, 0.0, places=14)
        self.assertAlmostEqual(target.real, 1 / np.sqrt(np.cosh(depth)), places=14)


if __name__ == "__main__":
    unittest.main()
