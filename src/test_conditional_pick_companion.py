import unittest

import numpy as np

from conditional_pick_companion import (
    anchored_companion,
    phase_optimized_boundary,
    theta_star,
)


class ConditionalPickCompanionTests(unittest.TestCase):
    def test_anchor_is_nulled_at_prescribed_carrier_fraction(self) -> None:
        carrier = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
        anchor = np.array([0.3j, 0.4, 0.5j, 0.7], dtype=complex)
        threshold = theta_star(carrier, anchor)
        result = anchored_companion(carrier, anchor, 0.8 * threshold)
        self.assertAlmostEqual(np.linalg.norm(result.companion), 1.0, places=12)
        self.assertAlmostEqual(
            abs(np.vdot(carrier, result.companion)), 0.0, places=12
        )
        self.assertLess(result.anchor_residual, 1.0e-11)
        self.assertAlmostEqual(
            abs(np.vdot(carrier, result.boundary_state)) ** 2,
            0.8 * threshold,
            places=12,
        )

    def test_conditional_positive_form_implies_joint_boundary(self) -> None:
        carrier = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
        anchor = np.array([0.2, 0.7j, 0.5, 0.4j], dtype=complex)
        theta = 0.75 * theta_star(carrier, anchor)
        result = anchored_companion(carrier, anchor, theta)

        g = anchor / np.linalg.norm(anchor)
        projection = np.eye(4) - np.outer(g, g.conj())
        positive = np.diag([0.5, 1.0, 2.0, 3.0])
        operator = projection @ positive @ projection - 20.0 * np.outer(g, g.conj())
        state_value = float(
            np.vdot(result.boundary_state, operator @ result.boundary_state).real
        )
        boundary = phase_optimized_boundary(
            operator, carrier, result.companion, theta
        )
        self.assertGreaterEqual(state_value, -1.0e-11)
        self.assertGreaterEqual(boundary + 1.0e-11, state_value)

    def test_threshold_is_sharp_for_anchor_cancellation(self) -> None:
        carrier = np.array([1.0, 0.0, 0.0], dtype=complex)
        anchor = np.array([1.0, 2.0, 0.0], dtype=complex)
        threshold = theta_star(carrier, anchor)
        self.assertAlmostEqual(threshold, 0.8, places=12)
        with self.assertRaises(ValueError):
            anchored_companion(carrier, anchor, threshold + 0.01)

    def test_full_carrier_when_carrier_nulls_anchor(self) -> None:
        carrier = np.array([1.0, 0.0, 0.0], dtype=complex)
        anchor = np.array([0.0, 1.0, 0.0], dtype=complex)
        result = anchored_companion(carrier, anchor, 1.0)
        np.testing.assert_allclose(result.boundary_state, carrier)
        self.assertLess(result.anchor_residual, 1.0e-12)

    def test_geometry_tie_breaker_fixes_the_free_direction(self) -> None:
        carrier = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
        anchor = np.array([0.25, 0.5, 0.0, 0.0], dtype=complex)
        confluent = np.array([0.0, 0.0, 1.0j, 2.0], dtype=complex)
        theta = 0.5 * theta_star(carrier, anchor)
        result = anchored_companion(
            carrier, anchor, theta, tie_breaker=confluent
        )
        self.assertLess(result.anchor_residual, 1.0e-12)
        # The component transverse to carrier and anchor follows the supplied
        # confluent direction, rather than an ambient coordinate convention.
        transverse = result.companion.copy()
        u = anchor - carrier * np.vdot(carrier, anchor)
        u /= np.linalg.norm(u)
        transverse -= u * np.vdot(u, transverse)
        expected = confluent / np.linalg.norm(confluent)
        correlation = abs(np.vdot(expected, transverse / np.linalg.norm(transverse)))
        self.assertAlmostEqual(correlation, 1.0, places=12)


if __name__ == "__main__":
    unittest.main()
