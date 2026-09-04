#!/usr/bin/env python3

from __future__ import annotations

import math
import unittest

import qp_tent_explicit_formula_gate as gate


class QPTentExplicitFormulaGateTests(unittest.TestCase):
    def test_tent_mass_and_fourier_are_nonnegative(self) -> None:
        self.assertAlmostEqual(gate.tent_fourier(0.0, 0.2), 0.2)
        for t in (0.1, 1.0, 17.0, 100.0, 1000.0):
            self.assertGreaterEqual(gate.tent_fourier(t, 0.2), 0.0)

    def test_laplace_axis_matches_sinc_square(self) -> None:
        for t in (0.0, 0.1, 3.0, 17.0, 101.0):
            closed = gate.tent_laplace(-1j * t, 0.2)
            self.assertAlmostEqual(closed.imag, 0.0, places=13)
            self.assertAlmostEqual(
                closed.real, gate.tent_fourier(t, 0.2), places=13
            )

    def test_normalized_population(self) -> None:
        self.assertEqual(gate.normalized_tent_population(0.0), 1.0)
        self.assertGreaterEqual(gate.normalized_tent_population(31.0), 0.0)

    def test_delsarte_conversion_is_exact(self) -> None:
        for error in (1.0, 0.2, 1e-4):
            value = gate.delsarte_value_from_antenna_error(error)
            self.assertAlmostEqual(value, 1.0 + 1.0 / error)
            self.assertAlmostEqual(gate.promoted_depth_upper_bound(error), error)

    def test_positive_antenna_lipschitz_bound(self) -> None:
        nodes = [-0.2, 0.05, 0.1]
        weights = [0.25, 0.25, 0.5]
        self.assertAlmostEqual(
            gate.positive_antenna_lipschitz_bound(nodes, weights), 0.1125
        )

    def test_grid_loss_bounds_observed_drop(self) -> None:
        nodes = [-0.2, -0.07, 0.11, 0.19]
        weights = [0.1, 0.2, 0.3, 0.4]
        mesh = 0.04
        lip = gate.positive_antenna_lipschitz_bound(nodes, weights)
        for k in range(200):
            left = k * mesh
            mid = left + mesh / 2.0
            observed = abs(
                gate.positive_cosine_antenna(mid, nodes, weights)
                - gate.positive_cosine_antenna(left, nodes, weights)
            )
            self.assertLessEqual(observed, lip * mesh / 2.0 + 1e-14)
            self.assertLessEqual(observed, gate.grid_to_continuum_loss(0.2, mesh))

    def test_grid_exponent(self) -> None:
        self.assertAlmostEqual(
            gate.required_positive_grid_exponent(0.019), 50.0 / 33.0 + 0.019
        )

    def test_strip_threshold_is_strict(self) -> None:
        self.assertFalse(gate.strip_supplies_power(0.019, 0.019))
        self.assertTrue(gate.strip_supplies_power(0.020, 0.019))
        self.assertFalse(gate.strip_kills_fixed_slice(gate.KAPPA_MAX))
        self.assertTrue(gate.strip_kills_fixed_slice(0.019))

    def test_vk_shape_is_sublinear_in_log_y(self) -> None:
        values = []
        for log_y in (100.0, 1e4, 1e8):
            shape = gate.vk_shape_from_log(log_y)
            values.append(shape / log_y)
        self.assertGreater(values[0], values[1])
        self.assertGreater(values[1], values[2])

    def test_ledger_polarity(self) -> None:
        value = gate.ledger()
        self.assertFalse(value.strip_0019_supplies_convenient_power)
        self.assertTrue(value.strip_0020_supplies_convenient_power)
        self.assertTrue(value.strip_0020_kills_fixed_slice)
        self.assertFalse(value.squaring_stays_in_finite_actual_frequency_pool)
        self.assertFalse(value.even_positive_kernel_can_damp_a_resonant_zero)

    def test_convex_mixing_averages_instead_of_multiplies(self) -> None:
        errors = [0.2, 0.05]
        weights = [0.25, 0.75]
        mixed = gate.convex_mixture_error(errors, weights)
        self.assertAlmostEqual(mixed, 0.0875)
        self.assertGreater(mixed, errors[0] * errors[1])
        self.assertGreaterEqual(mixed, min(errors))

    def test_cosine_square_escapes_frequency_pool(self) -> None:
        self.assertEqual(gate.cosine_product_frequencies(0.2, 0.2), (0.0, 0.4))
        self.assertTrue(gate.nonlinear_power_escapes_finite_support(0.2, 2))
        self.assertFalse(gate.nonlinear_power_escapes_finite_support(0.2, 1))

    def test_positive_kernel_resonant_bounds(self) -> None:
        lower, upper = gate.positive_kernel_laplace_ratio_bounds(0.4, 0.2)
        self.assertAlmostEqual(lower, math.exp(-0.08))
        self.assertAlmostEqual(upper, math.exp(0.08))
        self.assertEqual(gate.even_positive_kernel_ratio_lower_bound(0.4, 0.2), 1.0)

    def test_iterated_reweighting_is_one_simplex_weight(self) -> None:
        base = [0.2, 0.3, 0.5]
        stages = [[2.0, 1.0, 4.0], [3.0, 5.0, 2.0]]
        result = gate.iterated_positive_reweighting(base, stages)
        direct = [base[j] * stages[0][j] * stages[1][j] for j in range(3)]
        total = sum(direct)
        direct = tuple(value / total for value in direct)
        for left, right in zip(result, direct):
            self.assertAlmostEqual(left, right)


if __name__ == "__main__":
    unittest.main()
