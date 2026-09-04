from fractions import Fraction

import pytest

from qp_near_zero_dual_cloud import (
    canonical_near_zero_dual_mode,
    densest_scaled_quadratic_bin,
    enumerate_one_mode_per_tangent,
    high_precision_stationary_packet,
    mode_is_supported,
    near_zero_dual_exponent_ledger,
    packet_correlation,
)


def test_canonical_mode_has_exact_integer_affine_alias_and_regular_jet():
    mode = canonical_near_zero_dual_mode(10**6, 25, 8, 1)
    assert (mode.h, mode.k, mode.m) == (1089, 578, 625)
    assert mode.action == 2 * 10**6 * 25 * (25 - 8)
    assert mode.first == -1250
    assert mode.action.denominator == mode.first.denominator == 1
    assert mode.second == Fraction(
        2 * 25**3 * 2, 10**6 * (2 * 25 + 25 + 8)
    )
    assert mode.second > 0 and mode.maximum_frequency == 1089
    assert mode_is_supported(mode, 1300)


def test_tangent_fingerprint_is_distinct_off_reflection():
    modes = [canonical_near_zero_dual_mode(10**6, 25, d, 1) for d in (2, 4, 6, 8)]
    assert len({mode.tangent_fingerprint for mode in modes}) == len(modes)
    assert all(mode.d > 0 and mode.m > 0 for mode in modes)


def test_finite_high_precision_packets_form_a_real_coherent_fixture():
    modes = [canonical_near_zero_dual_mode(10**6, 26, d, 1) for d in (1, 3, 5, 7)]
    packets = [high_precision_stationary_packet(mode, 100, decimal_digits=50) for mode in modes]
    correlations = [
        abs(packet_correlation(packets[0], packet)) for packet in packets[1:]
    ]
    # The application-scale full threshold is about 0.327 in this fixture.
    eta = (10**6) ** (-Fraction(16, 33) / 6)
    # The least value is 0.8403778668... (the d=1 versus d=7 pair).
    assert min(correlations) > 0.84 > eta


def test_exact_cloud_enumerator_and_densest_bin():
    modes = enumerate_one_mode_per_tangent(
        Q=10**7,
        cutoff=10**6,
        p_min=20,
        p_max=120,
    )
    assert len(modes) > 300
    assert len({(mode.p, mode.d) for mode in modes}) == len(modes)
    assert len({mode.tangent_fingerprint for mode in modes}) == len(modes)
    assert all(mode_is_supported(mode, 10**6) for mode in modes)
    dense = densest_scaled_quadratic_bin(modes, 10_000)
    assert dense
    spread = max(mode.scaled_quadratic_jet for mode in dense) - min(
        mode.scaled_quadratic_jet for mode in dense
    )
    assert spread < 10_000


def test_exact_exponent_no_go_and_nonuniform_repair():
    ledger = near_zero_dual_exponent_ledger(Fraction(1, 96))
    assert ledger["p_floor"] == Fraction(77, 160)
    assert ledger["p_ceiling"] == Fraction(17, 32)
    assert ledger["full_second_small_edge"] == Fraction(25, 24)
    assert ledger["full_unresolved_R_window"] == Fraction(49, 48)
    assert ledger["chosen_cloud_bin"] == Fraction(97, 96)
    assert ledger["full_degree_excess"] == Fraction(1, 96)
    assert ledger["full_window_slack"] == Fraction(1, 96)
    assert ledger["closing_second_small_edge"] == Fraction(13, 12)
    assert ledger["closing_unresolved_R_window"] == Fraction(47, 48)
    assert ledger["closing_cluster_ceiling"] == Fraction(49, 48)
    assert ledger["closing_unresolved_margin"] == Fraction(1, 24)
    assert ledger["nonuniform_schur_inverse_term"] == Fraction(7, 8)
    assert ledger["nonuniform_schur_direct_term"] == Fraction(9, 16)
    assert ledger["nonuniform_schur_total"] == Fraction(7, 8)
    assert ledger["nonuniform_schur_margin_to_D"] == Fraction(1, 8)


def test_invalid_parity_is_rejected():
    with pytest.raises(ValueError):
        canonical_near_zero_dual_mode(1000, 25, 3, 1)
