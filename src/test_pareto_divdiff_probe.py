#!/usr/bin/env python3

import math
import unittest

from pareto_divdiff_probe import (
    closed_laplace,
    knot_jump,
    pareto_divided_carrier,
    truncated_piecewise_laplace,
    weighted_jump_mass,
)


class ParetoDividedDifferenceProbeTests(unittest.TestCase):
    def test_sampled_divided_carriers_are_positive(self) -> None:
        node_sets = ([1.2], [1.2, 2.0], [1.2, 1.5, 2.0], [1.1, 1.3, 1.6, 2.0])
        for nodes in node_sets:
            for integer in range(1, 35):
                for numerator in (1, 3, 7, 9):
                    x = integer + numerator / 10.0
                    self.assertGreater(pareto_divided_carrier(nodes, x), 0.0)

    def test_first_uncancelled_u_derivative_has_unit_jump(self) -> None:
        for nodes in ([1.2, 2.0], [1.2, 1.5, 2.0], [1.1, 1.3, 1.6, 2.0]):
            order = len(nodes) - 1
            for derivative in range(order):
                self.assertAlmostEqual(knot_jump(nodes, 17, derivative), 0.0, places=9)
            self.assertAlmostEqual(knot_jump(nodes, 17, order), 1.0, places=9)

    def test_boundary_vanishing_order(self) -> None:
        nodes = [1.2, 1.5, 2.0]
        order = len(nodes) - 1
        u = 1.0e-3
        observed = pareto_divided_carrier(nodes, math.exp(u))
        predicted = u**order / math.factorial(order)
        self.assertAlmostEqual(observed / predicted, 1.0, delta=2.0e-3)

    def test_piecewise_integral_matches_closed_transform(self) -> None:
        nodes = [1.2, 1.5, 2.0]
        s = 2.7 + 0.4j
        observed = truncated_piecewise_laplace(nodes, s, intervals=3000)
        predicted = closed_laplace(nodes, s)
        self.assertLess(abs(observed - predicted), 2.0e-8)

    def test_weighted_jump_mass_does_not_stabilize_below_one(self) -> None:
        self.assertGreater(weighted_jump_mass(0.9, 10000), weighted_jump_mass(0.9, 1000) + 1.0)
        self.assertGreater(weighted_jump_mass(1.0, 10000), weighted_jump_mass(1.0, 1000) + 1.0)


if __name__ == "__main__":
    unittest.main()
