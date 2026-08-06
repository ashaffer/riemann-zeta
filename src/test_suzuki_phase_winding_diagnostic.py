import unittest

import numpy as np

from shift_phase_covariance_falsifier import (
    ShiftedCharacteristic,
    scalar_coercive_metric,
)
from suzuki_phase_winding_diagnostic import (
    count_matching_support,
    geometric_weyl_turns,
    phase_winding,
    sampled_phase_root_count,
    smooth_zeta_zero_count,
)


class SuzukiPhaseWindingDiagnosticTest(unittest.TestCase):
    def test_density_helpers_use_repository_normalization(self) -> None:
        support = 3.0
        height = 100.0
        self.assertAlmostEqual(
            geometric_weyl_turns(support, height),
            support * height / (4.0 * np.pi),
            places=14,
        )
        scaled = height / (2.0 * np.pi)
        self.assertAlmostEqual(
            smooth_zeta_zero_count(height),
            scaled * (np.log(scaled) - 1.0) + 7.0 / 8.0,
            places=14,
        )
        self.assertAlmostEqual(
            count_matching_support(height),
            2.0 * (np.log(scaled) - 1.0),
            places=14,
        )

    def test_density_helpers_reject_nonpositive_inputs(self) -> None:
        with self.assertRaises(ValueError):
            geometric_weyl_turns(0.0, 10.0)
        with self.assertRaises(ValueError):
            smooth_zeta_zero_count(0.0)
        with self.assertRaises(ValueError):
            count_matching_support(-1.0)

    def test_phase_winding_on_synthetic_path(self) -> None:
        turns = 3.75
        angles = np.linspace(0.2, 0.2 + 2.0 * np.pi * turns, 2001)
        self.assertAlmostEqual(phase_winding(np.exp(1j * angles)), turns, places=12)

    def test_sampled_counts_match_bisection_roots_on_scalar_control(self) -> None:
        characteristic = ShiftedCharacteristic(
            scalar_coercive_metric(6), radius=0.75, shift=-0.25
        )
        height = 40.0
        samples = 6001
        grid = np.linspace(0.0, height, samples)
        phasors = characteristic.boundary_phasor(grid)

        winding = phase_winding(phasors)
        for phase in (0.0, np.pi, 0.37):
            sampled_count = sampled_phase_root_count(phasors, phase)
            roots = characteristic.real_zeros(
                phase, 0.0, height, samples=samples
            )
            self.assertEqual(sampled_count, roots.size)
            self.assertLessEqual(abs(float(roots.size) - winding), 1.0)

    def test_phase_helpers_reject_degenerate_phasors(self) -> None:
        with self.assertRaises(ValueError):
            phase_winding([1.0 + 0.0j])
        with self.assertRaises(ValueError):
            sampled_phase_root_count([1.0 + 0.0j, 0.0 + 0.0j], 0.0)


if __name__ == "__main__":
    unittest.main()
