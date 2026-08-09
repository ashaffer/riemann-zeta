#!/usr/bin/env python3

import cmath
import math
import unittest

from fixed_step_spectral_cooling_probe import coboundary_multiplier
from proportional_order_detector_bank import (
    SpectralNode,
    alpha_h,
    beta_h,
    dyadic_orders,
    factorized_coboundary_multiplier,
    raw_bank_rate,
    retreated_cutoff_theta,
    retreated_support_margin,
    retreated_uv_error_exponent,
    tilted_bases,
    tilted_rate,
    vk_shell_scale,
    vk_tilted_saving,
)


class ProportionalOrderDetectorBankTests(unittest.TestCase):
    def test_alpha_beta_relation_and_existing_multiplier(self) -> None:
        h = 0.17
        node = complex(0.13, 8.75)
        for order in (1, 2, 7, 19):
            self.assertAlmostEqual(
                abs(beta_h(node, h) - cmath.exp(-h * node) * alpha_h(node, h)),
                0.0,
                places=13,
            )
            self.assertAlmostEqual(
                abs(
                    factorized_coboundary_multiplier(node, h, order)
                    - coboundary_multiplier(node, h, order)
                ),
                0.0,
                places=12,
            )

    def test_proportional_power_factorization(self) -> None:
        h = 0.08
        slope = 0.03
        order = 11
        node = complex(0.07, 3.5)
        z_value, w_value = tilted_bases(node, h, slope)
        left = (
            cmath.exp(node * order / slope)
            * factorized_coboundary_multiplier(node, h, order)
        )
        right = (z_value**order - w_value**order) / node
        scale = max(1.0, abs(left), abs(right))
        self.assertLess(abs(left - right) / scale, 2.0e-12)

    def test_critical_nodes_contract_and_off_line_node_is_detected(self) -> None:
        h = 0.1
        gamma = 14.134725141734695
        critical = complex(0.0, gamma)
        z_value, w_value = tilted_bases(critical, h, 0.02)
        self.assertLess(abs(z_value), 1.0)
        self.assertLess(abs(w_value), 1.0)

        off_line = complex(0.04, gamma)
        self.assertGreater(tilted_rate(off_line, h, 0.001), 0.0)

    def test_vertical_bases_compactify(self) -> None:
        h = 0.1
        slope = 0.02
        low = max(abs(value) for value in tilted_bases(complex(0.1, 100.0), h, slope))
        high = max(abs(value) for value in tilted_bases(complex(0.1, 1.0e6), h, slope))
        self.assertLess(high, low / 100.0)

    def test_zero_temperature_rate_approaches_rightmost_displacement(self) -> None:
        nodes = (
            SpectralNode(0.0, 14.0),
            SpectralNode(0.08, 30.0),
            SpectralNode(0.17, 1000.0),
        )
        h = 0.05
        coarse = raw_bank_rate(nodes, h, 0.01)
        fine = raw_bank_rate(nodes, h, 1.0e-5)
        self.assertGreater(fine, coarse)
        self.assertAlmostEqual(fine, 0.17, delta=2.0e-4)

    def test_dyadic_bank_has_only_logarithmically_many_orders(self) -> None:
        orders = dyadic_orders(1.0e6, 0.2, 1.0)
        self.assertEqual(orders, tuple(sorted(set(orders), reverse=True)))
        self.assertGreaterEqual(orders[-1], 1)
        self.assertLessEqual(len(orders), math.ceil(math.log2(2.0e5)) + 1)

    def test_vk_scaling_identity(self) -> None:
        for slope in (1.0e-2, 1.0e-4, 1.0e-8):
            shell = vk_shell_scale(slope)
            saving = vk_tilted_saving(slope)
            self.assertAlmostEqual(saving, slope * shell)
            self.assertGreater(shell, 1.0)
            self.assertGreater(saving, 0.0)
        self.assertGreater(vk_tilted_saving(1.0e-4), vk_tilted_saving(1.0e-8))

    def test_retreated_cutoff_support_and_euler_exponent(self) -> None:
        log_scale = 10000.0
        h = 0.1
        a_zero = 0.75
        euler_constant = 2.0
        retreat = 3.0
        for order in (1, 10, 100, 1000):
            theta = retreated_cutoff_theta(
                log_scale, order, a_zero, retreat
            )
            self.assertGreater(theta, 0.0)
            self.assertLess(theta, 1.0)
            self.assertGreaterEqual(
                retreated_support_margin(
                    log_scale, order, h, a_zero, retreat
                ),
                0.0,
            )
            self.assertLess(
                retreated_uv_error_exponent(
                    log_scale,
                    order,
                    a_zero,
                    retreat,
                    euler_constant,
                ),
                -0.2 * log_scale,
            )


if __name__ == "__main__":
    unittest.main()
