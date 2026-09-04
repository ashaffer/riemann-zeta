from itertools import product

import numpy as np
import pytest

from qp_residual_block_triangle_matching import affine_plane_sts9_parallel_classes
from qp_residual_walsh_defect_inverse import (
    absolute_weight_fourth_domination,
    carleson_layers,
    defect_fan_translation_ledger,
    extract_high_effective_multiplicity,
    fixed_endpoint_defect_is_injective,
    full_integer_tangent_walsh_fixture,
    physical_wedge_defect,
    schatten_bin_recombination_bound,
    support_sensitive_carleson_ledger,
    translation_plane_weight_mass,
    walsh_fourth_ledger,
)
from qp_weighted_triangle_rademacher_square import (
    schatten_fourth_power,
    weighted_class_matrices,
)


def test_walsh_formula_matches_exact_sign_enumeration_for_complex_weights() -> None:
    classes = affine_plane_sts9_parallel_classes()
    weights = np.array(
        [1 + 2j, -2j, 3 - 1j, 1, -2, 1j, 2 + 1j, -1 + 3j, 2],
        dtype=complex,
    )
    weights /= np.linalg.norm(weights)
    matrices = weighted_class_matrices(9, classes, weights)
    exact_average = 0.0
    for signs in product((-1.0, 1.0), repeat=len(matrices)):
        exact_average += schatten_fourth_power(
            sum(sign * matrix for sign, matrix in zip(signs, matrices))
        )
    exact_average /= 2 ** len(matrices)

    replay = walsh_fourth_ledger(9, classes, weights)
    assert replay.all_plus_fourth == pytest.approx(
        schatten_fourth_power(sum(matrices))
    )
    assert replay.rademacher_fourth == pytest.approx(exact_average)


def test_absolute_weights_dominate_the_complex_physical_fourth_trace() -> None:
    classes = affine_plane_sts9_parallel_classes()
    weights = np.exp(2j * np.pi * np.arange(9) / 9) / 3.0
    complex_fourth, positive_fourth = absolute_weight_fourth_domination(
        9, classes, weights
    )
    assert complex_fourth <= positive_fourth + 1.0e-10
    assert complex_fourth < positive_fourth


def test_high_effective_multiplicity_carries_half_the_unsigned_mass() -> None:
    classes = affine_plane_sts9_parallel_classes()
    weights = np.ones(9) / 3.0
    replay = walsh_fourth_ledger(9, classes, weights)
    extraction = extract_high_effective_multiplicity(replay)
    assert extraction.global_effective_multiplicity >= 1.0
    assert extraction.high_all_plus_mass >= extraction.total_all_plus_mass / 2.0
    assert extraction.minimum_signature_support >= int(
        np.ceil(extraction.threshold - 1.0e-10)
    )
    assert sum(layer.all_plus_mass for layer in carleson_layers(replay)) == pytest.approx(
        replay.all_plus_fourth
    )


def test_actual_q151_adjacent_wedge_has_unit_defect() -> None:
    # {71,73,83} and {64,81,83} are literal adjacent residual-block atoms.
    h, residual_difference, factored_difference = physical_wedge_defect(
        151,
        middle=83,
        first_endpoint=71,
        second_endpoint=64,
        first_completion=73,
        second_completion=81,
    )
    assert h == -1
    assert residual_difference == -664
    assert residual_difference == factored_difference == 8 * 83 * h


def test_fixed_endpoint_and_defect_determine_the_completion_pair() -> None:
    assert fixed_endpoint_defect_is_injective(
        71,
        64,
        (73, 81),
        (73, 81),
        shell_diameter=19,
        shell_minimum=64,
    )
    # The next solution to 71*a-64*b=-1 is shifted by (64,71), which is
    # longer than the entire shell and is therefore illegal.
    with pytest.raises(ValueError):
        fixed_endpoint_defect_is_injective(
            71,
            64,
            (73, 81),
            (137, 152),
            shell_diameter=19,
            shell_minimum=64,
        )


def test_full_integer_tangent_packet_has_polynomial_walsh_gap_but_sharp_size() -> None:
    small = full_integer_tangent_walsh_fixture(4, 10**9)
    large = full_integer_tangent_walsh_fixture(8, 10**9)
    for replay in (small, large):
        length = replay.order
        assert replay.maximum_hyperedge_degree == length
        assert replay.all_plus_fourth == pytest.approx(
            2 * length**4 / (2 * length - 1) ** 2
        )
        assert replay.all_plus_fourth < replay.degree_scale
        assert replay.q_exceeds_degree_squared
        assert replay.all_plus_fourth / replay.rademacher_fourth > length / 3.0
    assert (
        large.all_plus_fourth / large.rademacher_fourth
        > 1.8 * small.all_plus_fourth / small.rademacher_fourth
    )


def test_critical_flat_bin_moves_the_open_tail_to_D_seven_eighths() -> None:
    degree = 2**8
    support = 2**15  # D^(15/8) when D=2^8.
    replay = support_sensitive_carleson_ledger(
        degree, support, squared_comparability=1.0
    )
    assert replay.randomized_scale_factor == 2**-7
    assert replay.automatic_multiplicity_threshold == 2**7
    assert replay.maximum_defect_multiplicity_scale == 2**8
    assert replay.high_tail_is_nonempty
    closed = support_sensitive_carleson_ledger(
        degree, degree**2, squared_comparability=1.0
    )
    assert not closed.high_tail_is_nonempty


def test_schatten_bin_recombination_is_the_exact_J_cubed_ledger() -> None:
    assert schatten_bin_recombination_bound([1.0, 2.0, 3.0]) == 27 * 6
    assert schatten_bin_recombination_bound([]) == 0.0


def test_dense_defect_fan_lifts_repeated_differences_to_one_color_plane() -> None:
    center = 10_000
    length = 32
    # x*a-y*b=1-s for (x,y)=(m,m+1), (a,b)=(m+s,m+s-1).
    points = tuple(
        (1 - step, center + step, center + step - 1)
        for step in range(1, length + 1)
    )
    replay = defect_fan_translation_ledger(
        center,
        center + 1,
        points,
        shell_minimum=center,
        shell_maximum=center + length,
    )
    assert replay.freiman_two_isomorphism_certified
    assert replay.fan_size == length
    assert replay.popular_translation_multiplicity == length - 2
    assert replay.popular_translation_multiplicity >= (
        replay.pigeonhole_multiplicity_lower_bound
    )
    assert replay.popular_translation_vector in ((2, 2), (-2, -2))
    assert replay.affine_color_plane_dimension == 2
    assert replay.all_four_colors_distinct
    assert not replay.all_eight_nodes_distinct


def test_popular_translation_survives_the_all_eight_distinct_filter() -> None:
    center = 10_000
    length = 32
    first_step = 10
    points = tuple(
        (
            1 - step,
            center - step,
            center + step,
            center + step - 1,
        )
        for step in range(first_step, first_step + length)
    )
    radius = first_step + length
    replay = defect_fan_translation_ledger(
        center,
        center + 1,
        points,
        shell_minimum=center - radius,
        shell_maximum=center + radius,
    )
    assert replay.all_eight_nodes_distinct
    assert replay.popular_translation_multiplicity == length - 2
    assert replay.popular_translation_multiplicity >= replay.pigeonhole_multiplicity_lower_bound


def test_one_affine_translation_plane_has_unit_weighted_mass() -> None:
    weights = {10: 1 + 1j, 11: -2j, 12: 3, 14: -1}
    mass, bound = translation_plane_weight_mass(weights, 1, 2)
    assert mass <= bound + 1.0e-12
    normalized = {index: value / np.sqrt(sum(abs(v) ** 2 for v in weights.values()))
                  for index, value in weights.items()}
    normalized_mass, normalized_bound = translation_plane_weight_mass(
        normalized, 1, 2
    )
    assert normalized_mass <= 1.0 + 1.0e-12
    assert normalized_bound == pytest.approx(1.0)
