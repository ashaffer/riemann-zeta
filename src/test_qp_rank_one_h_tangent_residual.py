from __future__ import annotations

from math import exp

import pytest

from qp_rank_one_h_tangent_residual import (
    affine_packet_vertices,
    apply_transition_rank_one,
    direct_schatten_fourth,
    edge_degree_spectral_ceiling,
    endpoint_gcd_lcm_divisor,
    hard_window_audit,
    inverse_step_transference,
    literal_hard_window_triples,
    maximum_edge_degree_product,
    near_determinant_cartesian_countermodel,
    opposite_token_population_ceiling,
    peel_affine_packets,
    rank_one_energy,
    shared_edge_cross_determinant_ceiling,
    shared_edge_palette,
    shared_edge_product_ledger,
    split_tangent_residual,
    tangent_coordinates,
    tangent_l1_certificate,
    tangent_ratio_blocks,
    transition_incidence,
    transition_witnesses,
)


def test_transition_is_exact_original_schatten_fourth() -> None:
    triples = (
        (2, 5, 11),
        (2, 7, 13),
        (3, 5, 17),
        (3, 7, 19),
        (4, 11, 13),
    )
    z = {11: 1 + 2j, 13: -2 + 0.5j, 17: 3 - 1j, 19: 0.25 + 4j}
    transition = transition_incidence(triples)
    assert rank_one_energy(transition, z) == pytest.approx(
        direct_schatten_fourth(triples, z)
    )


def test_exact_tangent_reduced_ratio_and_l1_certificate() -> None:
    # b=gu,b'=gv,c=vd,c'=ud for (u,v)=(2,3).
    tangent = {
        ((10, 15), (21, 14)): 1,
        ((14, 21), (33, 22)): 1,
        ((22, 33), (39, 26)): 1,
    }
    coordinates = tangent_coordinates((10, 15), (21, 14))
    assert (
        coordinates.gcd,
        coordinates.first_reduced_center,
        coordinates.second_reduced_center,
        coordinates.common_color_parameter,
    ) == (5, 2, 3, 7)
    assert tangent_ratio_blocks(tangent) == {
        (2, 3): {(5, 7), (7, 11), (11, 13)}
    }
    z = {14: 1 + 1j, 21: 2j, 22: -1j, 33: 2, 26: 3, 39: -2}
    assert rank_one_energy(tangent, z) <= tangent_l1_certificate(tangent, z) + 1e-12


def test_edge_degree_product_is_the_residual_spectral_certificate() -> None:
    # Biadjacency [[1,1],[1,0]] has edge degree products 4,2,2.
    graph = {
        ((1, 1), (4, 4)): 1,
        ((1, 1), (5, 5)): 1,
        ((2, 2), (4, 4)): 1,
    }
    maximum, edge = maximum_edge_degree_product(graph)
    assert maximum == 4
    assert edge in graph
    assert edge_degree_spectral_ceiling(graph) == 4


def test_affine_packet_peeling_is_exact_and_local() -> None:
    witnesses = {
        ((10, 11), (30, 31)): 100,
        ((10, 11), (29, 30)): 101,
        ((10, 11), (28, 29)): 102,
        ((20, 21), (40, 42)): 100,
        ((20, 21), (38, 39)): 103,
    }
    incidence = {edge: 1 for edge in witnesses}
    left, right = affine_packet_vertices(witnesses)
    assert (10, 11) in left
    assert (20, 21) not in left
    peeled = peel_affine_packets(incidence, witnesses)
    assert len(peeled) == 2


def test_literal_hard_window_preserves_pair_uniqueness_and_split() -> None:
    q, D = 400, 18
    lower = round((q / 2) * exp(-0.2))
    upper = round((q / 2) * exp(0.2))
    values = tuple(range(lower, upper + 1))
    triples = literal_hard_window_triples(q, D, values)
    incidence = transition_incidence(triples)
    tangent, residual = split_tangent_residual(incidence)
    assert len(tangent) + len(residual) == len(incidence)
    # This is a finite diagnostic, not an asymptotic assertion.
    audit = hard_window_audit(q, D, values)
    assert audit.triples == len(triples)
    assert audit.residual_edge_degree_product <= D
    assert audit.peeled_edge_degree_product <= audit.residual_edge_degree_product
    norm = len(values) ** -0.5
    z = {value: complex(norm) for value in values}
    assert apply_transition_rank_one(incidence, z)


def test_shared_edge_pluecker_palette_and_physical_ledger() -> None:
    q, D = 400, 18
    lower = round((q / 2) * exp(-0.2))
    upper = round((q / 2) * exp(0.2))
    values = tuple(range(lower, upper + 1))
    triples = literal_hard_window_triples(q, D, values)
    incidence = transition_incidence(triples)
    witnesses = transition_witnesses(triples)
    _, residual = split_tangent_residual(incidence)
    _, edge = maximum_edge_degree_product(residual)
    assert edge is not None
    palette = shared_edge_palette(residual, edge)
    assert palette.base_determinant != 0
    assert palette.base_determinant % endpoint_gcd_lcm_divisor(*edge) == 0
    assert sum(count for _, count in palette.cross_determinant_multiplicities) == (
        palette.left_degree * palette.right_degree
    )

    centers, colors = edge
    left_edge = next(candidate for candidate in residual if candidate[0] == centers)
    right_edge = next(candidate for candidate in residual if candidate[1] == colors)
    ledger = shared_edge_product_ledger(
        witnesses[edge],
        centers,
        colors,
        witnesses[left_edge],
        left_edge[1],
        witnesses[right_edge],
        right_edge[0],
    )
    assert ledger.scaled_cross_determinant == ledger.expanded_ledger
    ceiling = shared_edge_cross_determinant_ceiling(q, D, lower, upper)
    assert max(
        abs(cross) for cross, _ in palette.cross_determinant_multiplicities
    ) <= ceiling


def test_inverse_step_transport_and_determinant_only_no_go() -> None:
    # delta=5000*5002-5001^2=-1, and both signed gaps are invertible.
    transport = inverse_step_transference((5000, 5001), (5002, 5001))
    delta = 5000 * 5002 - 5001 * 5001
    assert delta * transport.center_inverse_step == (
        5001 + 5000 * transport.center_lift
    )
    assert delta * transport.color_inverse_step == (
        -5000 + 5001 * transport.color_lift
    )
    assert 5000 * transport.coupling_factor == delta * (
        transport.color_lift * transport.center_inverse_step
        - transport.color_inverse_step
    )
    assert 5001 * transport.coupling_factor == delta * (
        transport.center_inverse_step
        + transport.center_lift * transport.color_inverse_step
    )

    left, right = near_determinant_cartesian_countermodel(10_000, 31)
    determinants = {
        u[0] * v[1] - u[1] * v[0] for u in left for v in right
    }
    assert max(abs(value) for value in determinants) == 30
    assert len(left) * len(right) == 31**2


def test_two_independent_tokens_bound_the_opposite_integral_arm() -> None:
    first = (6, 4)
    second = (-3, 5)
    cap = 11
    retained = []
    for ell in range(-100, 101):
        for t in range(-100, 101):
            if (
                abs(first[1] * t - first[0] * ell) <= cap
                and abs(second[1] * t - second[0] * ell) <= cap
            ):
                retained.append((ell, t))
    assert len(retained) <= opposite_token_population_ceiling(first, second, cap)
