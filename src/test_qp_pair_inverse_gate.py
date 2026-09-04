import math

import numpy as np

from qp_pair_inverse_gate import (
    KAPPA_PROMOTE,
    audit_multi_island,
    audit_sign_simplex,
    carrier_concentration,
    cosine_kernel,
    cosine_kernel_via_sum,
    pair_concentration,
    pair_exponent_ledger,
    packet_mass_l2_lower,
    restricted_relation_energy_lower,
    restricted_relation_l2_lower,
    rooted_neighbor_concentration,
    sign_simplex_rows,
    upper_tail_lower_bound,
)


def test_exact_tail_bounds() -> None:
    threshold, mass = pair_concentration(2.0)
    assert threshold == 1.0 / 8.0
    assert mass == 1.0 / 7.0
    assert upper_tail_lower_bound(1.0 / 4.0, threshold) == mass

    threshold, mass = carrier_concentration(2.0)
    assert threshold == 1.0 / 4.0
    assert mass == 1.0 / 3.0

    threshold, mass = rooted_neighbor_concentration(2.0)
    assert threshold == 1.0 / 16.0
    assert mass == 1.0 / 15.0


def test_cosine_pair_kernel_identity() -> None:
    nodes = np.asarray([-0.31, -0.07, 0.11, 0.29])
    for left, right in [(2.3, 7.1), (-4.0, 1.25), (0.0, 9.0)]:
        assert math.isclose(
            cosine_kernel(nodes, left, right),
            cosine_kernel_via_sum(nodes, left, right),
            rel_tol=1e-13,
            abs_tol=1e-13,
        )


def test_sign_simplex_is_exact_bounded_antipode() -> None:
    for cost in (2, 3, 4):
        rows = sign_simplex_rows(cost)
        assert set(np.unique(rows)) == {-1, 1}
        audit = audit_sign_simplex(cost)
        assert audit.atom_count == cost * cost
        assert math.isclose(audit.antipode_depth, 1.0 / cost)
        assert math.isclose(audit.representation_tv, float(cost))
        assert audit.representation_residual < 1e-12
        assert audit.row_mean_error < 1e-12
        assert audit.gram_error < 1e-12
        assert math.isclose(audit.high_pair_mass, 1.0 / (cost * cost))


def test_many_island_model_saturates_pair_scale_without_global_lattice() -> None:
    audit = audit_multi_island(3, island_size=40)
    assert audit.island_count == 9
    assert audit.atom_count == 360
    assert math.isclose(audit.good_pair_mass, 1.0 / 9.0)
    assert audit.allowed_difference_bins == 79
    assert 1.9 < audit.l2_ratio_to_bound < 2.1
    assert 1.2 < audit.energy_ratio_to_bound < 1.4
    assert audit.minimum_cross_distance_to_allowed_lag > 1.0
    expected_ratio = 2.0 + math.sqrt(2.0) / 40.0
    assert math.isclose(audit.first_three_lattice_ratio, expected_ratio)


def test_discrete_l2_and_energy_ledger() -> None:
    cost = 7.0
    delta = cost**-2
    bins = int(cost**4)
    assert math.isclose(restricted_relation_l2_lower(delta, bins), cost**-6)
    assert math.isclose(restricted_relation_energy_lower(delta, bins), cost**-8)
    assert math.isclose(packet_mass_l2_lower(cost**-1, int(cost**2)), cost**-4)

    ledger = pair_exponent_ledger(KAPPA_PROMOTE)
    assert math.isclose(ledger.one_point_l2_lower, -4.0 * KAPPA_PROMOTE)
    assert math.isclose(ledger.pair_l2_lower, -6.0 * KAPPA_PROMOTE)
    assert math.isclose(ledger.pair_energy_lower, -8.0 * KAPPA_PROMOTE)
    assert ledger.gm_pair_third_margin_below_main < 0.0
