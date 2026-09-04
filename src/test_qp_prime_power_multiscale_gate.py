from fractions import Fraction

import pytest

from qp_prime_power_multiscale_gate import (
    layer_amplification_exponent,
    layer_mesh_exponent,
    prime_power_base,
    rational_shift_overlap,
    scaled_zero_is_separated,
    second_order_quadrature_top,
    shift_overlap_factor_bound,
    target_ledger,
)


def test_layer_bandwidth_is_strictly_nested() -> None:
    c = 0.019
    tops = [second_order_quadrature_top(k, c) for k in range(1, 6)]
    assert tops == sorted(tops, reverse=True)
    assert tops[0] == pytest.approx(0.4655)
    assert tops[1] == pytest.approx(0.228)


def test_proper_power_materiality_tax() -> None:
    assert layer_amplification_exponent(2, 0.019) == pytest.approx(0.481)
    assert layer_amplification_exponent(3, 0.019) > 0.64


def test_near_one_zero_cannot_cancel_across_higher_layers() -> None:
    beta = 0.99
    for k0 in range(1, 8):
        for k in range(k0 + 1, 12):
            assert scaled_zero_is_separated(beta, k0, k)


def test_rational_shift_overlap_uses_only_ratio_primes() -> None:
    # The shell ratio 23/16<2 permits at most one power of every base.
    nodes = [16, 17, 19, 23]
    assert all(prime_power_base(n) is not None for n in nodes)
    ratio = Fraction(17, 16)
    pairs = rational_shift_overlap(nodes, ratio)
    assert pairs == [(16, 17)]
    assert len(pairs) <= shift_overlap_factor_bound(ratio)


def test_target_ledger() -> None:
    ledger = target_ledger()
    assert ledger["prime_quadrature_top"] > 0.46
    assert ledger["square_quadrature_top"] < ledger["prime_quadrature_top"]
    assert ledger["square_amplification_tax"] == pytest.approx(0.481)
    assert ledger["prime_quadrature_top"] < ledger["aperture_top"]
