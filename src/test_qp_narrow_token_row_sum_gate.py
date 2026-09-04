from __future__ import annotations

import random

import pytest

from qp_narrow_token_row_sum_gate import (
    anchored_codegrees,
    carleson_tail_constant,
    complete_biclique,
    cramer_token,
    determinant,
    determinant_layer_support_ceiling,
    dyadic_codegree_profile,
    four_completion_remainders,
    max_weight_sufficiency_ratio,
    neighbor_degree_sums,
    physical_two_anchor_floor,
    primitive_token_content,
    rich_codegree_population_bound,
    token_pair_determinant,
    two_anchor_integral_ceiling,
    verify_rich_codegree_population_bound,
    verify_row_sum_codegree_identity,
    weighted_ordered_pair_form,
)


def test_cramer_reconstruction_content_and_area_transference() -> None:
    p = (101, 102)
    q = (102, 103)
    assert determinant(p, q) == -1
    vectors = tuple((101 + index, 102 + index) for index in range(1, 18))
    for vector in vectors:
        token = cramer_token(p, q, vector)
        assert token == (-index_of(vector, vectors) - 1, index_of(vector, vectors))
        assert primitive_token_content(p, q, vector) == 1
    for first in vectors:
        for second in vectors:
            assert token_pair_determinant(p, q, first, second) == (
                -determinant(p, q) * determinant(first, second)
            )


def index_of(vector: tuple[int, int], vectors: tuple[tuple[int, int], ...]) -> int:
    return vectors.index(vector)


def test_token_identities_on_random_primitive_data() -> None:
    rng = random.Random(20260825)
    checked = 0
    while checked < 200:
        p = (rng.randint(-30, 30), rng.randint(-30, 30))
        q = (rng.randint(-30, 30), rng.randint(-30, 30))
        u = (rng.randint(-30, 30), rng.randint(-30, 30))
        v = (rng.randint(-30, 30), rng.randint(-30, 30))
        if determinant(p, q) == 0:
            continue
        if __import__("math").gcd(abs(u[0]), abs(u[1])) != 1:
            continue
        cramer_token(p, q, u)
        primitive_token_content(p, q, u)
        token_pair_determinant(p, q, u, v)
        checked += 1


def test_two_anchor_ceiling_has_an_unavoidable_D_floor() -> None:
    for delta in (1, 2, 6, 35):
        for D in (1, 3, 17, 101):
            for content in range(1, delta + 1):
                if delta % content:
                    continue
                for minor in (1, max(1, D // 2), D):
                    ceiling = physical_two_anchor_floor(
                        delta, D, minor, content
                    )
                    assert ceiling >= 3 * (2 * D + 1)

    first = (6, 4)
    second = (-3, 5)
    assert two_anchor_integral_ceiling(first, second, 11) >= 1


def test_neighbor_degree_sum_is_anchored_codegree_l1_mass() -> None:
    edges = {
        ("p0", "g0"),
        ("p0", "g1"),
        ("p0", "g2"),
        ("p1", "g0"),
        ("p1", "g1"),
        ("p2", "g0"),
        ("p2", "g3"),
    }
    assert anchored_codegrees(edges, "g0") == {
        "g0": 3,
        "g1": 2,
        "g2": 1,
        "g3": 1,
    }
    assert neighbor_degree_sums(edges)["g0"] == 7
    assert verify_row_sum_codegree_identity(edges, "g0") == 7


def test_WNDS_and_max_row_weight_are_equivalent_up_to_four() -> None:
    weights = {(0, 1): 40.0, (1, 0): 3.0, (1, 2): 7.0, (2, 2): 5.0}
    vector = {0: 0.2, 1: 0.5, 2: 0.3}
    ratio = max_weight_sufficiency_ratio(weights, vector)
    assert ratio <= 40.0

    # A single directed off-diagonal entry of weight M contributes M/4 at
    # the two-point probability vector.  Hence any universal WNDS constant
    # is at least max(W)/4.
    witness = {0: 0.5, 1: 0.5}
    assert weighted_ordered_pair_form({(0, 1): 40.0}, witness) == 10.0
    assert max_weight_sufficiency_ratio({(0, 1): 40.0}, witness) == 10.0

    # A diagonal entry is detected without the factor four.
    assert max_weight_sufficiency_ratio({(2, 2): 5.0}, {2: 1.0}) == 5.0


def test_determinant_labels_and_affine_biclique_tail_are_target_sharp() -> None:
    assert determinant_layer_support_ceiling(17) == 35
    length = 16
    D = length**2
    edges = complete_biclique(length, length)
    profile = anchored_codegrees(edges, 0)
    assert len(profile) == length
    assert set(profile.values()) == {length}
    assert verify_row_sum_codegree_identity(edges, 0) == D
    assert dyadic_codegree_profile(profile) == {length: length}
    assert carleson_tail_constant(profile, D) == pytest.approx(1.0)


def test_four_completion_remainder_identity() -> None:
    r, s, h = four_completion_remainders(
        a=4998,
        x=5004,
        anchor=(5002, 5001),
        partner=(4996, 4995),
    )
    assert 5004 * h == 5001 * r - 5002 * s


def test_rich_codegree_dependent_pair_bound() -> None:
    length = 12
    edges = complete_biclique(length, length)
    population, ceiling = verify_rich_codegree_population_bound(
        edges, anchor=0, richness=length
    )
    assert population == length - 1
    assert ceiling == length
    assert rich_codegree_population_bound(20, 7, 5) == 133


def test_invalid_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        cramer_token((1, 2), (2, 4), (1, 0))
    with pytest.raises(ValueError):
        primitive_token_content((1, 0), (0, 1), (2, 2))
    with pytest.raises(ValueError):
        physical_two_anchor_floor(2, 10, 0, 1)
    with pytest.raises(ValueError):
        max_weight_sufficiency_ratio({(0, 0): -1.0}, {0: 1.0})
    with pytest.raises(ValueError):
        rich_codegree_population_bound(10, 4, 1)
