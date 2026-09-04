import math

import numpy as np
import pytest

from qp_spectral_null_grouping_gate import (
    FULL_APERTURE_EXPONENT,
    QP_KAPPA,
    bernoulli_null_certificate,
    bernoulli_support_upper_bound,
    central_atom_from_depth,
    depth_from_central_atom,
    finite_pool_delsarte_value,
    finite_pool_positive_depth,
    grouped_product_depth_upper,
    haar_adaptive_support_log_bound,
    max_groups_for_target_depth,
    odd_alias_at_or_above,
    reciprocal_node_sum_bound,
    required_group_size,
    target_metric_power,
)


def test_depth_atom_bijection() -> None:
    for depth in (1e-6, 0.1, 0.7):
        assert depth_from_central_atom(central_atom_from_depth(depth)) == pytest.approx(depth)


def test_odd_alias_and_zero_node() -> None:
    node = -0.137
    alias = odd_alias_at_or_above(node, 17.0)
    assert alias >= 17.0
    assert alias < 17.0 + 2.0 * math.pi / abs(node) + 1e-12
    assert np.exp(1j * alias * node) == pytest.approx(-1.0 + 0.0j, abs=2e-14)
    with pytest.raises(ValueError):
        odd_alias_at_or_above(0.0, 17.0)


def test_exact_bernoulli_spectral_null() -> None:
    nodes = np.asarray([-0.19, -0.071, 0.043, 0.163])
    row = bernoulli_null_certificate(nodes, lower=11.0)
    assert np.all(row.aliases >= 11.0)
    assert row.upper == pytest.approx(float(np.sum(row.aliases)))
    assert row.central_atom == pytest.approx(1.0 / 16.0)
    assert row.depth == pytest.approx(1.0 / 15.0)
    assert row.max_fourier_residual < 2e-14


def test_half_integer_support_bound_is_polynomially_legal() -> None:
    y = 100_000_000.5
    bound = bernoulli_support_upper_bound(
        y=y,
        width=0.2,
        node_count=20_000_000,
        lower=y**0.01,
    )
    assert reciprocal_node_sum_bound(y, 0.2) > 0.0
    assert bound < y**FULL_APERTURE_EXPONENT


def test_grouping_ledger() -> None:
    assert grouped_product_depth_upper(1) == pytest.approx(1.0)
    assert grouped_product_depth_upper(4) == pytest.approx(1.0 / 15.0)
    depth = 2.0**-10
    assert max_groups_for_target_depth(depth) == 10
    assert required_group_size(101, depth) == 11


def test_metric_exponent_and_log_bound() -> None:
    assert target_metric_power() == pytest.approx(1.0 - 2.0 * QP_KAPPA)
    log_bound = haar_adaptive_support_log_bound(
        node_count=100_000,
        max_harmonic=1_000_000,
        depth=0.1,
    )
    assert log_bound < -400.0


def test_finite_delsarte_reciprocity() -> None:
    atoms = np.asarray([[-1.0, 0.0], [0.0, -1.0]])
    depth = finite_pool_positive_depth(atoms)
    delsarte = finite_pool_delsarte_value(atoms)
    assert depth == pytest.approx(0.5)
    assert delsarte == pytest.approx(3.0)
    assert depth == pytest.approx(1.0 / (delsarte - 1.0))
