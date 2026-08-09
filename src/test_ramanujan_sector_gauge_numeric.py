#!/usr/bin/env python3

import unittest

import numpy as np

from ramanujan_sector_gauge_numeric import (
    build_sector_proxy,
    penalized_gauge,
    prime_cloud_null_vector,
)


class RamanujanSectorGaugeNumericTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.proxy = build_sector_proxy(24, shift_count=4)

    def test_primitive_synthesis_and_sector_ledger(self) -> None:
        proxy = self.proxy
        self.assertLess(proxy.mode_reconstruction_error, 1.0e-11)
        np.testing.assert_allclose(
            proxy.bad,
            proxy.theta_zero + proxy.axes + proxy.near_zero,
            rtol=0.0,
            atol=2.0e-12,
        )
        np.testing.assert_allclose(
            proxy.full,
            proxy.bad + proxy.off_axis,
            rtol=0.0,
            atol=2.0e-12,
        )

    def test_bad_proxy_is_positive_semidefinite(self) -> None:
        self.assertGreaterEqual(np.linalg.eigvalsh(self.proxy.bad)[0], -2.0e-12)

    def test_prime_cloud_is_null_and_cross_sector_cancels(self) -> None:
        proxy = self.proxy
        vector = prime_cloud_null_vector(proxy)
        self.assertLess(np.max(np.abs(proxy.synthesis @ vector)), 2.0e-14)
        self.assertAlmostEqual(proxy.energy(proxy.full, vector), 0.0, places=10)
        self.assertAlmostEqual(
            proxy.energy(proxy.bad, vector),
            -proxy.energy(proxy.off_axis, vector),
            places=10,
        )

    def test_baseline_and_penalized_gauge_remain_on_exact_orbit(self) -> None:
        proxy = self.proxy
        np.testing.assert_allclose(
            proxy.synthesis @ proxy.baseline,
            proxy.target,
            rtol=0.0,
            atol=3.0e-14,
        )
        self.assertEqual(proxy.baseline[0], 1.0)
        candidate = penalized_gauge(proxy, 0.01)
        self.assertLess(candidate.constraint_residual, 3.0e-13)
        self.assertAlmostEqual(
            candidate.full_energy,
            proxy.energy(proxy.full, proxy.baseline),
            places=10,
        )

    def test_y24_regression(self) -> None:
        proxy = self.proxy
        self.assertAlmostEqual(proxy.baseline_ledger, 5.389166648782759, places=11)
        self.assertAlmostEqual(
            proxy.energy(proxy.bad, proxy.baseline),
            12.595073505664141,
            places=10,
        )


if __name__ == "__main__":
    unittest.main()
