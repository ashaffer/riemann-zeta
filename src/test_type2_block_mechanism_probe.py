import math
import unittest

from type2_block_mechanism_probe import (
    analyze_scale,
    geometric_scales,
    ramp_profile,
    ramp_weight,
)


class Type2BlockMechanismProbeTest(unittest.TestCase):
    def test_ramp_endpoint_conventions(self):
        self.assertEqual(ramp_profile(-1.0), 0.0)
        self.assertEqual(ramp_profile(0.0), 0.0)
        self.assertEqual(ramp_profile(0.25), 0.25)
        self.assertEqual(ramp_profile(1.0), 1.0)
        self.assertEqual(ramp_profile(2.0), 1.0)
        self.assertEqual(ramp_weight(100, 100), 0.0)

    def test_balanced_decompositions_and_centering_close(self):
        result = analyze_scale(10_000)

        self.assertEqual(result.cutoff, 31)
        self.assertAlmostEqual(result.balanced, 9.413938995, places=8)
        self.assertAlmostEqual(result.centering, 12.086057833, places=8)
        self.assertAlmostEqual(result.centered_residual, -2.672118838, places=8)
        self.assertAlmostEqual(result.full_discrepancy, -2.672860626, places=8)
        self.assertAlmostEqual(result.euler_defect, 0.000741788, places=8)

        tolerance = 2.0e-12 * result.raw_l1
        self.assertLessEqual(abs(result.triple_fiber_error), tolerance)
        self.assertLessEqual(abs(result.block_closure_error), tolerance)
        self.assertLessEqual(abs(result.centered_identity_error), tolerance)
        self.assertAlmostEqual(
            result.positive_l1 - result.negative_l1,
            result.balanced,
            places=10,
        )
        self.assertAlmostEqual(
            math.fsum(result.cofactor_sums.values()),
            result.balanced,
            places=10,
        )
        self.assertAlmostEqual(
            math.fsum(result.dyadic_cells.values()),
            result.balanced,
            places=10,
        )
        self.assertAlmostEqual(
            math.fsum(result.omega_sums.values()),
            result.balanced,
            places=10,
        )

    def test_geometric_scales_include_endpoints(self):
        self.assertEqual(geometric_scales(100, 10_000, 3), [100, 1000, 10_000])


if __name__ == "__main__":
    unittest.main()
