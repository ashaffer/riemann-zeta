import unittest

import numpy as np

from approximate_polarization_gate import (
    block_diagonal,
    off_line_generator,
    pole_tate_generator,
    relative_lyapunov_defect,
    scaling_generator,
)


class ApproximatePolarizationGateTest(unittest.TestCase):
    def test_off_line_identity_attains_exact_spectral_lower_bound(self) -> None:
        alpha = 0.2
        defect = relative_lyapunov_defect(
            off_line_generator(alpha), np.eye(2)
        )
        self.assertAlmostEqual(defect, 2 * alpha, places=13)

    def test_nondiagonal_positive_metric_cannot_beat_lower_bound(self) -> None:
        alpha = 0.17
        metric = np.array([[2.0, 0.4], [0.4, 1.0]])
        defect = relative_lyapunov_defect(
            off_line_generator(alpha), metric
        )
        self.assertGreaterEqual(defect + 1e-13, 2 * alpha)

    def test_ungraded_pole_tate_sector_has_boundary_defect_one(self) -> None:
        defect = relative_lyapunov_defect(
            pole_tate_generator(), np.eye(2)
        )
        self.assertAlmostEqual(defect, 1.0, places=13)

    def test_direct_sum_cannot_hide_pole_tate_defect(self) -> None:
        middle = off_line_generator(0.1)
        generator = block_diagonal(middle, pole_tate_generator())
        metric = block_diagonal(np.diag([2.0, 3.0]), np.eye(2))
        defect = relative_lyapunov_defect(generator, metric)
        self.assertAlmostEqual(defect, 1.0, places=13)

    def test_cross_sector_metric_cannot_beat_pole_tate_floor(self) -> None:
        generator = block_diagonal(
            off_line_generator(0.1), pole_tate_generator()
        )
        factor = np.array(
            [
                [1.0, 0.2, 0.1, 0.0],
                [0.0, 1.1, 0.3, 0.1],
                [0.2, 0.0, 0.9, 0.2],
                [0.1, 0.1, 0.0, 1.2],
            ]
        )
        metric = factor.T @ factor + 0.25 * np.eye(4)
        defect = relative_lyapunov_defect(generator, metric)
        self.assertGreaterEqual(defect + 1e-13, 1.0)

    def test_native_semilocal_algebra_has_zero_defect(self) -> None:
        # A positive Hankel Gram matrix and the corresponding symmetric
        # shifted-moment pattern exercise M=G^{-1}H and M^T G=G M without
        # numerical quadrature.  Odd moments vanish, as for the even
        # semilocal density.
        metric = np.array(
            [[2.0, 0.0, 1.0],
             [0.0, 1.0, 0.0],
             [1.0, 0.0, 3.0]]
        )
        shifted = np.array(
            [[0.0, 1.0, 0.0],
             [1.0, 0.0, 3.0],
             [0.0, 3.0, 0.0]]
        )
        generator = scaling_generator(metric, shifted)
        multiplication = np.linalg.solve(metric, shifted)
        np.testing.assert_allclose(
            multiplication.T @ metric,
            metric @ multiplication,
            atol=2e-15,
        )
        self.assertLess(relative_lyapunov_defect(generator, metric), 2e-15)


if __name__ == "__main__":
    unittest.main()
