from __future__ import annotations

import cmath
import math

import mpmath as mp
import pytest

from jordan_detector_calculus import (
    alternating_exp_transform,
    causal_box_multiplier,
    endpoint_flat_log_abs_multiplier,
    exp_sine_unit_masses,
    grid_mask_negative_proxy,
    piecewise_linear_lipschitz,
    piecewise_linear_negative_mass,
    pole_survival_order,
)


def test_causal_box_multiplier_matches_direct_integral_and_is_right_half_plane_faithful() -> None:
    length = 1.7
    for point in (0.4 + 2.3j, 1.2 - 7.0j, 3.0 + 0.0j):
        # Closed-form integration of exp(-point*t) on [0,length].
        direct = (1.0 - cmath.exp(-length * point)) / point
        assert causal_box_multiplier(point, length) == pytest.approx(direct)
        assert abs(causal_box_multiplier(point, length)) > 0.0
    assert causal_box_multiplier(0.0, length) == pytest.approx(length)
    assert causal_box_multiplier(2j * math.pi / length, length) == pytest.approx(0.0)


def test_adaptive_block_orientation_can_hide_every_large_fixed_sign_mass() -> None:
    theta = 0.73
    for block in range(8):
        positive, negative = exp_sine_unit_masses(theta, block)
        assert min(positive, negative) == 0.0
        assert max(positive, negative) > 0.0

    p0, _ = exp_sine_unit_masses(theta, 0)
    p2, _ = exp_sine_unit_masses(theta, 2)
    _, n1 = exp_sine_unit_masses(theta, 1)
    _, n3 = exp_sine_unit_masses(theta, 3)
    assert p2 / p0 == pytest.approx(math.exp(2 * theta))
    assert n3 / n1 == pytest.approx(math.exp(2 * theta))


def test_alternating_block_transform_formula_matches_geometric_sum() -> None:
    theta = 0.4
    point = 1.8 + 0.7j
    z = point - theta
    one_block = (1.0 - cmath.exp(-z)) / z
    geometric = one_block / (1.0 + cmath.exp(-z))
    assert alternating_exp_transform(point, theta) == pytest.approx(geometric)
    assert alternating_exp_transform(theta, theta) == pytest.approx(0.5)


def test_pole_survival_is_multiplicity_sensitive_not_just_radical_sensitive() -> None:
    # Every filter vanishes at rho, yet an order-two source pole survives.
    assert pole_survival_order(2, (1, 1, 3)) == 1
    # A simple source pole is killed precisely by a common filter zero.
    assert pole_survival_order(1, (1, 2)) == 0
    assert pole_survival_order(1, (0, 4)) == 1
    assert pole_survival_order(5, ()) == 0


def test_grid_masks_obey_the_lipschitz_mesh_bound() -> None:
    nodes = (0.0, 0.17, 0.41, 0.66, 1.0)
    values = (-0.8, 0.5, -0.25, 0.9, -0.4)
    jordan = piecewise_linear_negative_mass(nodes, values)
    proxy = grid_mask_negative_proxy(nodes, values)
    lipschitz = piecewise_linear_lipschitz(nodes, values)
    mesh = max(right - left for left, right in zip(nodes, nodes[1:]))
    assert 0.0 <= proxy <= jordan
    assert jordan - proxy <= (
        lipschitz * mesh * (nodes[-1] - nodes[0]) / 2.0
    )


def test_grid_mask_error_order_L_delta_is_sharp() -> None:
    # Alternate centered ramps of slopes +L and -L.  The result is globally
    # continuous and L-Lipschitz; every cell integral is zero, while its
    # negative mass is L*delta^2/8.
    cells = 20
    delta = 1.0 / cells
    lipschitz = 3.0
    nodes = tuple(index * delta for index in range(cells + 1))
    values = tuple(
        (-1.0 if index % 2 == 0 else 1.0) * lipschitz * delta / 2.0
        for index in range(cells + 1)
    )
    jordan = piecewise_linear_negative_mass(nodes, values)
    proxy = grid_mask_negative_proxy(nodes, values)
    gap = jordan - proxy
    assert piecewise_linear_lipschitz(nodes, values) == pytest.approx(lipschitz)
    assert proxy == pytest.approx(0.0)
    assert gap == pytest.approx(lipschitz * delta / 8.0)


def test_endpoint_order_inserts_factorial_attenuation() -> None:
    point = 0.8 + 14.0j
    logs = [endpoint_flat_log_abs_multiplier(order, point) for order in range(8)]
    assert all(later < earlier for earlier, later in zip(logs, logs[1:]))

    # Removing the explicit factorial still leaves polynomial order-dependent
    # attenuation: Gamma(r+2) H_r(s) has log magnitude -Re(s) log r + O(1).
    residuals = []
    for order in (200, 1000, 5000, 20000):
        normalized = endpoint_flat_log_abs_multiplier(
            order, point, factorial_normalized=True
        )
        residuals.append(normalized + point.real * math.log(order))
    limit = float(mp.log(abs((point - 1.0) * mp.gamma(point))))
    assert abs(residuals[-1] - limit) < 0.03
    assert abs(residuals[-1] - residuals[-2]) < abs(
        residuals[-2] - residuals[-3]
    )


def test_invalid_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        causal_box_multiplier(1.0, 0.0)
    with pytest.raises(ValueError):
        pole_survival_order(2, (1, -1))
    with pytest.raises(ValueError):
        piecewise_linear_negative_mass((0.0, 0.0), (1.0, -1.0))
