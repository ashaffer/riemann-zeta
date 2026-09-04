from __future__ import annotations

import math

import pytest

from qp_weighted_fejer_matching_gate import (
    exponent_ledger,
    golomb_pair_frequencies,
    matching_ledger,
    oriented_differences_are_unique,
    subcritical_ap_ledger,
)


def test_exact_bad_packet_root_and_stable_normalization() -> None:
    delta = 1.0e-3
    # kappa=(2m)delta^2 is asymptotic to 1/16.
    m = int((1.0 / 32.0) / delta**2)
    ledger = matching_ledger(delta, m)
    assert ledger.b / ledger.base_normalization == pytest.approx(delta)
    assert ledger.difference_moment == pytest.approx(4.0 * ledger.b * delta)
    assert 0.9 < ledger.candidate_normalization < 1.0


def test_absolute_covariance_has_constant_size() -> None:
    delta = 1.0e-4
    m = int((1.0 / 32.0) / delta**2)
    ledger = matching_ledger(delta, m)
    kappa = 2.0 * m * delta**2
    assert ledger.covariance_at_matching_shift >= kappa / 2.0
    assert ledger.covariance_at_matching_shift > 100.0 * delta * ledger.candidate_normalization


def test_explicit_golomb_geometry() -> None:
    values, d = golomb_pair_frequencies(31)
    assert oriented_differences_are_unique(values)
    span = values[-1] - values[0]
    assert d > 2 * span
    assert min(values) > 2 * d
    packet_values = values + [value + d for value in values]
    differences = {
        packet_values[i] - packet_values[j]
        for i in range(len(packet_values))
        for j in range(len(packet_values))
        if i != j
    }
    assert d in differences
    assert all(value not in differences for value in packet_values)


def test_project_exponent_and_prime_mesh_transfer() -> None:
    ledger = exponent_ledger()
    assert ledger["frequency_top"] < ledger["project_aperture_top"]
    assert ledger["frequency_top"] > 0.01
    assert ledger["character_transfer_error"] < ledger["delta_squared"]
    assert ledger["quadratic_transfer_error"] < ledger["delta_squared"]


def test_invalid_critical_constant_is_rejected() -> None:
    with pytest.raises(ValueError):
        matching_ledger(0.1, 7)


def test_subcritical_ap_breaks_even_one_sided_covariance() -> None:
    # R=delta^-2=10^8 and L=R^.6 is strictly between sqrt(R) and R^(2/3).
    delta = 1.0e-4
    critical_count = delta**-2
    length = int(critical_count**0.6)
    ledger = subcritical_ap_ledger(delta, length)
    assert ledger.b / ledger.base_normalization == pytest.approx(delta)
    assert ledger.maximum_difference_moment < 2.0 * length * delta**2
    assert ledger.additive_energy == (2 * length**3 + length) // 3
    assert ledger.endpoint_triple_count == length * (length + 1) // 2
    assert 0.99 < ledger.candidate_normalization < 1.03
    assert ledger.endpoint_covariance < 0.0
    assert -ledger.endpoint_covariance > 5.0 * delta * ledger.candidate_normalization
