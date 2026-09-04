from itertools import combinations
import random

import pytest

from qp_cartesian_determinant_line_spread import (
    cartesian_line_spread_certificate,
    cross_form,
    determinant,
    lattice_line_spread_ceiling,
    maximum_affine_line_occupancy,
    maximum_pair_determinant,
    projected_line_lift_audit,
    transverse_line_pair_certificate,
    witness_interpolation_certificate,
)


def test_line_occupancy_and_determinant_invariants_are_exact() -> None:
    points = ((10, 11), (11, 12), (12, 13), (10, 13), (12, 17))
    assert maximum_affine_line_occupancy(points) == 3
    assert maximum_pair_determinant(points) == max(
        abs(determinant(first, second)) for first, second in combinations(points, 2)
    )


def test_two_line_sparse_arms_obey_the_cartesian_bound() -> None:
    left = tuple((100 + t, 103 + t * t) for t in range(9))
    right = tuple((97 + t * t, 101 - t) for t in range(7))
    certificate = cartesian_line_spread_certificate(left, right)
    assert certificate.left_maximum_line_occupancy == 2
    assert certificate.right_maximum_line_occupancy == 2
    assert certificate.plucker_product <= certificate.plucker_ceiling
    assert certificate.population_product <= certificate.universal_population_ceiling


def test_affine_biclique_shows_the_line_factors_are_necessary() -> None:
    length = 30
    left = tuple((10_000 + t, 10_001 + t) for t in range(length))
    right = tuple((10_020 + t, 10_019 + t) for t in range(length))
    certificate = cartesian_line_spread_certificate(left, right)
    assert certificate.left_maximum_line_occupancy == length
    assert certificate.right_maximum_line_occupancy == length
    assert certificate.population_product == length**2
    assert certificate.cross_determinant_cap >= length


def test_degenerate_same_arm_is_handled_by_cross_form_level_lines() -> None:
    left = ((3, 3), (5, 5), (7, 7))
    right = ((10, 9), (11, 10), (12, 11), (13, 12))
    certificate = cartesian_line_spread_certificate(left, right)
    assert certificate.left_maximum_determinant == 0
    assert certificate.left_maximum_line_occupancy == len(left)
    assert certificate.cross_determinant_cap == 7


def test_random_small_integer_sets_never_violate_the_certificate() -> None:
    generator = random.Random(20260829)
    pool = tuple(
        (first, second)
        for first in range(1, 12)
        for second in range(1, 12)
    )
    for _ in range(100):
        left = generator.sample(pool, generator.randint(1, 10))
        right = generator.sample(pool, generator.randint(1, 10))
        cartesian_line_spread_certificate(left, right)


def test_invalid_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        cartesian_line_spread_certificate((), ((1, 1),))
    with pytest.raises(ValueError):
        cartesian_line_spread_certificate(((0, 0),), ((1, 1),))
    with pytest.raises(ValueError):
        maximum_affine_line_occupancy(((1, 1), (1, 1)))
    with pytest.raises(ValueError):
        lattice_line_spread_ceiling(-1, 2)


def test_cross_form_matches_the_project_sign_convention() -> None:
    assert cross_form((3, 5), (7, 11)) == 21 - 55


def test_literal_residual_projected_line_does_not_lift_to_physical_plane() -> None:
    audit = projected_line_lift_audit(
        q=809,
        hard_window_radius=26,
        center=(391, 440),
        neighbors=(
            (349, 485, 431),
            (377, 449, 399),
            (419, 404, 359),
            (449, 377, 335),
        ),
    )
    assert audit.projected_line_equation == (8, -9, -1)
    assert audit.determinant_tokens == (-5, -1, 4, 7)
    assert audit.all_edges_are_residual
    assert audit.maximum_product_residual <= audit.q * audit.hard_window_radius
    assert audit.product_lift_is_planar
    assert not audit.witnesses_are_affine_on_projected_line
    assert not audit.original_triples_are_coplanar


def test_subunit_interpolation_defect_forces_affine_witnesses() -> None:
    certificate = witness_interpolation_certificate(
        q=2000,
        hard_window_radius=16,
        fixed_column=1000,
        samples=((0, 1000, 1000), (1, 999, 1001), (2, 998, 1002)),
    )
    assert certificate.maximum_product_residual == 32_000
    assert certificate.maximum_affine_defect == 0
    assert certificate.maximum_exact_defect_bound < 1
    assert certificate.every_exact_bound_is_subunit
    assert certificate.witness_graph_is_affine


def test_transverse_rich_line_pair_closes_by_one_mixed_difference() -> None:
    left = tuple((100 + t, 103 + t) for t in (0, 2, 5, 9, 14))
    right = tuple((111 + s, 109 - s) for s in (0, 1, 4, 8))
    certificate = transverse_line_pair_certificate(left, right)
    assert certificate.direction_cross_form == 2
    assert certificate.mixed_difference == 2 * 14 * 8
    assert certificate.population_product == 20
    assert certificate.population_product <= certificate.population_ceiling


def test_parallel_null_line_pair_is_the_exact_unclosed_branch() -> None:
    left = ((100, 101), (101, 102), (102, 103))
    right = ((110, 109), (111, 108), (112, 107))
    # Directions (1,1) and (1,-1) are transverse, so use the B-null dual
    # direction (1,1) on the second arm instead.
    right_null = ((110, 109), (111, 110), (112, 111))
    transverse_line_pair_certificate(left, right)
    with pytest.raises(ValueError, match="cross-form null"):
        transverse_line_pair_certificate(left, right_null)
