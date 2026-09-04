import math
import unittest

import numpy as np

from conditional_pick_actual_scan import (
    build_geometry,
    endpoint_boundary_anchor,
    evaluate_actual_conditional_pick,
    rationalized_boundary_coordinates,
)
from high_height_carrier_slice import endpoint_null_basis
from scipy.linalg import null_space
from subfull_direct_q_failfast import (
    build_floating_base,
    selected_rows_with_phase,
)


class ConditionalPickActualScanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = build_floating_base(
            32.0,
            gamma_fraction=1.5,
            aperture_fraction=0.32,
            grid_phase=0.0,
        )

    def test_endpoint_anchor_spans_coordinate_leakage(self) -> None:
        endpoint = endpoint_null_basis(self.base.indices, 3)
        anchor = endpoint_boundary_anchor(
            self.base.indices, self.base.tau, endpoint, 3
        )
        projection = endpoint @ endpoint.T
        leakage = endpoint.T @ (
            self.base.tau[:, None] * (np.eye(self.base.indices.size) - projection)
        )
        residual = leakage - np.outer(anchor, anchor.conj() @ leakage)
        self.assertLess(np.linalg.norm(residual), 1.0e-10 * np.linalg.norm(leakage))

    def test_geometry_and_completed_balance(self) -> None:
        geometry = build_geometry(self.base, alpha=0.4, jet_order=3)
        self.assertGreater(geometry.theta_star, 0.0)
        row = evaluate_actual_conditional_pick(
            self.base,
            alpha=0.4,
            jet_order=3,
            theta=0.5 * geometry.theta_star,
        )
        self.assertLess(row["anchor_residual"], 1.0e-10)
        self.assertAlmostEqual(
            row["budget_plus_centered_residual"], 0.0, places=9
        )
        self.assertAlmostEqual(row["plus_one_shift"], 2.0 * math.pi / self.base.length)

    def test_anchor_null_is_exactly_one_more_endpoint_moment(self) -> None:
        order = 3
        alpha = 0.4
        geometry = build_geometry(self.base, alpha=alpha, jet_order=order)
        anchor_null = null_space(geometry.anchor.conj()[None, :])
        inherited = geometry.inclusion @ anchor_null

        endpoint_next = endpoint_null_basis(self.base.indices, order + 1)
        selected_x, selected_y = selected_rows_with_phase(
            self.base.tau,
            self.base.length,
            self.base.gamma,
            alpha,
            self.base.grid_phase,
        )
        selected_next = null_space(
            (endpoint_next.T @ selected_x)[None, :], rcond=1.0e-12
        )
        direct = endpoint_next @ selected_next
        inherited_projector = inherited @ inherited.conj().T
        direct_projector = direct @ direct.conj().T
        self.assertLess(
            np.linalg.norm(inherited_projector - direct_projector), 1.0e-10
        )

        old_energy = np.linalg.norm(geometry.inclusion.conj().T @ selected_y) ** 2
        new_energy = np.linalg.norm(direct.conj().T @ selected_y) ** 2
        self.assertAlmostEqual(geometry.theta_star, new_energy / old_energy, places=11)

    def test_boundary_state_rationalizes_in_rigorous_basis(self) -> None:
        geometry = build_geometry(self.base, alpha=0.4, jet_order=1)
        replay = rationalized_boundary_coordinates(
            self.base,
            alpha=0.4,
            jet_order=1,
            theta=0.5 * geometry.theta_star,
            max_denominator=10**7,
        )
        self.assertEqual(len(replay["coefficients"]), geometry.inclusion.shape[1])
        self.assertLess(replay["floating_basis_residual"], 1.0e-10)
        self.assertLess(replay["rationalized_physical_residual"], 1.0e-9)

    def test_centered_even_jet_has_exact_parity_geometry(self) -> None:
        base = build_floating_base(
            64.0,
            gamma_fraction=1.5,
            aperture_fraction=0.2,
            grid_phase=0.0,
        )
        geometry = build_geometry(base, alpha=0.4, jet_order=4)
        physical_carrier = geometry.inclusion @ geometry.carrier
        physical_anchor = geometry.inclusion @ geometry.anchor
        self.assertLess(
            np.linalg.norm(physical_carrier + physical_carrier[::-1]), 1.0e-11
        )
        self.assertLess(
            np.linalg.norm(physical_anchor - physical_anchor[::-1]), 1.0e-11
        )
        self.assertAlmostEqual(geometry.theta_star, 1.0, places=12)


if __name__ == "__main__":
    unittest.main()
