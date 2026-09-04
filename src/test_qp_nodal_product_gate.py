#!/usr/bin/env python3

import math
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from qp_nodal_product_gate import (
    actual_nodes,
    carrier_mass,
    cluster_collapse_carrier_error,
    cluster_collapse_feature_error,
    continuum_potential_max,
    cutoff_frontier,
    log_relaxed_carrier_bound,
    max_log_nodal_product,
)


class QPNodalProductGateTests(unittest.TestCase):
    def test_prime_power_nodes_are_distinct_and_in_shell(self) -> None:
        nodes = actual_nodes(1000.0, 0.2)
        self.assertGreater(len(nodes), 40)
        self.assertEqual(len(nodes), len(np.unique(nodes)))
        self.assertTrue(np.all(nodes >= -0.2))
        self.assertTrue(np.all(nodes <= 0.2))

    def test_nodal_product_maximum_enumeration(self) -> None:
        nodes = np.array([-0.12, 0.03, 0.16])
        log_max, location = max_log_nodal_product(nodes, 0.2)
        grid = np.linspace(-0.2, 0.2, 20001)
        direct = np.max(
            np.sum(np.log(np.maximum(np.abs(grid[:, None] - nodes), 1e-300)), axis=1)
        )
        self.assertGreaterEqual(log_max + 1e-8, direct)
        self.assertGreaterEqual(location, -0.2)
        self.assertLessEqual(location, 0.2)

    def test_frontier_inverts_bound(self) -> None:
        y = 1000.0
        nodes = actual_nodes(y, 0.2)
        log_product, _ = max_log_nodal_product(nodes, 0.2)
        mass = carrier_mass(0.2, 0.49)
        frontier = cutoff_frontier(
            y=y,
            kappa=0.0180303234,
            max_log_product=log_product,
            node_count=len(nodes),
            weight_mass=mass,
        )
        log_bound = log_relaxed_carrier_bound(
            max_log_product=log_product,
            node_count=len(nodes),
            cutoff=frontier,
            weight_mass=mass,
        )
        self.assertAlmostEqual(log_bound, -0.0180303234 * math.log(y), places=10)

    def test_canonical_continuum_constant(self) -> None:
        potential, location, ratio = continuum_potential_max(0.2)
        self.assertAlmostEqual(potential, -1.81872667647, places=8)
        self.assertAlmostEqual(location, -0.2, places=7)
        self.assertAlmostEqual(ratio, 2.26761059653, places=8)

    def test_cluster_collapse_ledgers(self) -> None:
        self.assertAlmostEqual(
            cluster_collapse_feature_error(
                total_variation=3.0, width=0.2, node_count=100, diameter=0.01
            ),
            0.06,
        )
        self.assertLess(
            cluster_collapse_carrier_error(
                total_variation=3.0, width=0.2, alpha=0.49, diameter=0.01
            ),
            0.002,
        )


if __name__ == "__main__":
    unittest.main()
