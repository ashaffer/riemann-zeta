import math
import unittest

import numpy as np

from carrier_ritz_loewner_gate import _actual_fixture_operators, lanczos_moments
from lanczos_m3_branch_gate import (
    actual_matrix_at_center,
    deterministic_branch_scan,
    lanczos_branch_point,
    lower_edge_variance_admission_gate,
    shifted_calibration,
)


class LanczosM3BranchGateTests(unittest.TestCase):
    def test_projector_moments_match_existing_fixture(self) -> None:
        height = 64
        alpha = 0.4
        aperture = 0.2
        old = _actual_fixture_operators(
            height,
            alpha=alpha,
            aperture_fraction=aperture,
            jet_order=None,
        )
        length = math.log(height)
        spacing = 2.0 * math.pi / length
        half_count = int(math.floor(aperture * height / spacing))
        center = 1.5 * height
        matrix, indices, _ = actual_matrix_at_center(height, half_count, center)
        row = lanczos_branch_point(
            matrix,
            indices,
            height=height,
            center=center,
            grid_phase=0.0,
            alpha=alpha,
            jet_order=old["jet_order"],
        )
        expected = lanczos_moments(old["K"], old["a"])
        self.assertAlmostEqual(row.m1, expected["m1"], places=11)
        self.assertAlmostEqual(row.m2, expected["m2"], places=11)
        self.assertAlmostEqual(row.m3, expected["m3"], places=11)

    def test_shifted_calibration_enters_bad_branch(self) -> None:
        point = shifted_calibration()["point"]
        self.assertLess(point["m1"], 0.0)
        self.assertLess(point["m3"], 0.0)
        self.assertEqual(point["theta_star"], 0.0)

    def test_small_scan_reports_branch_separately(self) -> None:
        report = deterministic_branch_scan(
            heights=[16],
            half_counts=[2],
            center_count=2,
            phases=[-0.49, 0.0, 0.49],
            alphas=[0.05, 0.499],
            maximum_jet_order=2,
        )
        self.assertEqual(report["base_count"], 2)
        self.assertEqual(report["point_count"], 36)
        self.assertEqual(report["negative_m1_count"], 0)
        self.assertGreater(report["minimum_m1_point"]["m1"], 0.0)

    def test_exact_bad_two_by_two_threshold(self) -> None:
        # The theorem-card countermodel is a sanity check for the moment
        # convention used here.
        matrix = np.diag([-1.0, -2.0])
        a = np.array([1.0, 1.0]) / math.sqrt(2.0)
        ka = matrix @ a
        m1 = float(a @ ka)
        m2 = float(ka @ ka)
        m3 = float(ka @ matrix @ ka)
        self.assertAlmostEqual(m1, -1.5)
        self.assertAlmostEqual(m2, 2.5)
        self.assertAlmostEqual(m3, -4.5)
        self.assertLess(m2 * m2 - m1 * m3, 0.0)

    def test_lower_edge_variance_gate(self) -> None:
        result = lower_edge_variance_admission_gate(
            m1=-1.0,
            m2=9.0,
            lower_edge_scale=4.0,
            theta=8.0 / 9.0,
        )
        self.assertTrue(result["admission_guaranteed"])
        self.assertAlmostEqual(result["required_m2"], 9.0)
        failed = lower_edge_variance_admission_gate(
            m1=-1.0,
            m2=8.99,
            lower_edge_scale=4.0,
            theta=8.0 / 9.0,
        )
        self.assertFalse(failed["admission_guaranteed"])


if __name__ == "__main__":
    unittest.main()
