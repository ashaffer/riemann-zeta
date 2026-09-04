import math
from fractions import Fraction
from itertools import permutations

import pytest

from qp_four_cycle_spectral_gate import (
    active_exponent_ledger,
    apply_incidence,
    closed_walk_product_ledger,
    coefficient_matrix,
    common_column_diagonal_mass,
    completed_grid_determinant_identity,
    degree_ledger,
    determinant_three,
    degeneracy_operator_bound,
    flat_fc_threshold,
    factorization_resource_ledger,
    fourth_norm_fc_threshold,
    fourth_norm_gram_bound,
    kloosterman_active_range_ledger,
    nondegenerate_four_cycle,
    restricted_color_ledger,
    restricted_combinatorial_bounds,
    row_pair_gram,
    row_pair_incidence,
    split_five_distinct_incidence,
    support_graph_degeneracy,
    three_by_three_rigidity_ledger,
    two_step_transport_ledger,
    uniform_support_gram_bound,
    weighted_multiplicity_cauchy_bound,
    validate_pair_uniqueness,
    weighted_restricted_gram_bound,
)


def latin_triples(order: int) -> dict[tuple[int, int, int], complex]:
    """A finite pair-unique fixture with nontrivial complex edge weights."""

    answer = {}
    for a in range(order):
        for b in range(order):
            raw = complex(1.0, (a - b) / (10 * order))
            answer[a, b, (a + b) % order] = raw / abs(raw)
    return answer


def symmetric_hypergraph_triples() -> dict[tuple[int, int, int], complex]:
    """A linear unordered fixture with simple and repeated-node triples."""

    answer: dict[tuple[int, int, int], complex] = {}
    for edge in ((1, 2, 3), (2, 4, 5), (6, 6, 7)):
        for oriented in set(permutations(edge)):
            answer[oriented] = 1.0
    return answer


def test_exact_incidence_application_equals_the_row_pair_gram() -> None:
    triples = latin_triples(4)
    raw = {0: 1 + 2j, 1: -0.5j, 2: 2 - 0.25j, 3: -1.5}
    norm = math.sqrt(sum(abs(value) ** 2 for value in raw.values()))
    z = {color: value / norm for color, value in raw.items()}
    matrix = coefficient_matrix(triples, z)
    incidence = row_pair_incidence(triples)

    expected = row_pair_gram(matrix)
    actual = apply_incidence(incidence, z)
    assert expected.keys() == actual.keys()
    for pair in expected:
        assert actual[pair] == pytest.approx(expected[pair], abs=1.0e-12)


def test_five_distinct_split_is_exact_and_nontrivial() -> None:
    triples = symmetric_hypergraph_triples()
    split = split_five_distinct_incidence(triples)
    full = row_pair_incidence(triples)
    assert split.generic
    assert split.exceptional

    z = {node: complex(node, 1 - node) / 20 for node in range(1, 8)}
    full_image = apply_incidence(full, z)
    generic_image = apply_incidence(split.generic, z)
    exceptional_image = apply_incidence(split.exceptional, z)
    for left in set(full_image) | set(generic_image) | set(exceptional_image):
        assert full_image.get(left, 0.0) == pytest.approx(
            generic_image.get(left, 0.0) + exceptional_image.get(left, 0.0),
            abs=1.0e-12,
        )


def test_nondegenerate_cycle_is_gram_square_minus_column_diagonal() -> None:
    triples = latin_triples(3)
    z = {0: 1 / math.sqrt(2), 1: 0.5j, 2: 0.5}
    matrix = coefficient_matrix(triples, z)
    gram_square = sum(abs(value) ** 2 for value in row_pair_gram(matrix).values())
    diagonal = common_column_diagonal_mass(matrix)
    assert nondegenerate_four_cycle(matrix) == pytest.approx(
        gram_square - diagonal, abs=1.0e-12
    )
    assert diagonal >= 0


def test_pair_uniqueness_and_unique_incidence_carrier_are_enforced() -> None:
    validate_pair_uniqueness(((0, 0, 0), (0, 1, 1), (1, 0, 1)))
    with pytest.raises(ValueError):
        validate_pair_uniqueness(((0, 0, 0), (0, 0, 1)))


def test_degree_ledger_replays_both_schur_sides() -> None:
    incidence = row_pair_incidence(latin_triples(5))
    ledger = degree_ledger(incidence)
    assert ledger.maximum_left == pytest.approx(5.0, abs=1.0e-12)
    assert ledger.maximum_right == pytest.approx(5.0, abs=1.0e-12)
    assert ledger.total_weight > 0


def test_degeneracy_criterion_treats_stars_at_square_root_scale() -> None:
    star = {
        (0, 1): {(color, color + 1): 1.0 for color in range(17)}
    }
    ledger = degree_ledger(star)
    assert ledger.maximum_left == 17
    assert ledger.maximum_right == 1
    assert support_graph_degeneracy(star) == 1
    assert degeneracy_operator_bound(
        max(ledger.maximum_left, ledger.maximum_right), 1
    ) == pytest.approx(2 * math.sqrt(17), abs=1.0e-12)

    cycle = {
        (0, 1): {(0, 1): 1.0, (1, 2): 1.0},
        (1, 2): {(0, 1): 1.0, (1, 2): 1.0},
    }
    assert support_graph_degeneracy(cycle) == 2


def test_two_step_transport_identity_is_exact() -> None:
    ledger = two_step_transport_ledger(
        1_000_003,
        101,
        103,
        107,
        109,
        113,
    )
    assert ledger.identity_left == ledger.identity_right
    assert ledger.drift_left == ledger.drift_right


def test_closed_walk_identity_does_not_force_carrier_pairing() -> None:
    ledger = closed_walk_product_ledger(
        1_000_003,
        (11, 13, 17, 19, 11),
        (23, 29, 31, 37),
    )
    assert ledger.identity_left == ledger.identity_right
    assert ledger.odd_carrier_product != ledger.even_carrier_product


def test_actual_c4_carriers_have_unequal_alternating_products() -> None:
    # q=25013, U=12 actual-shell witness from the H-graph laboratory.
    odd = 15_031 * 11_393
    even = 13_723 * 12_479
    assert odd == 171_248_183
    assert even == 171_249_317
    assert odd - even == -1_134


def test_completed_three_by_three_grid_has_the_exact_determinant_factor() -> None:
    colors = ((2, 3, 5), (7, 11, 13), (17, 19, 23))
    left, right = completed_grid_determinant_identity(
        (29, 31, 37), (41, 43, 47), colors
    )
    assert determinant_three(colors) != 0
    assert left == right


def test_three_by_three_short_residual_test_forces_singular_colors() -> None:
    ledger = three_by_three_rigidity_ledger(
        center=10**6,
        residual_bound=1,
        shell_minimum=100,
    )
    assert ledger.determinant_upper_bound == 18_000_006
    assert ledger.nonzero_color_lower_bound == 512 * 100**6
    assert ledger.forces_zero_color_determinant


def test_full_one_factorization_family_violates_the_color_degree_cap() -> None:
    ledger = factorization_resource_ledger(5, 9, 5)
    assert ledger.colors == 10
    assert ledger.matching_components == 9
    assert ledger.left_vertices == 45
    assert ledger.right_vertices == 45
    assert ledger.incidence_edges == 225
    assert ledger.fresh_carriers == 225
    assert ledger.color_degree == 45
    assert not ledger.obeys_color_degree_cap
    assert ledger.rank_one_output_squared == Fraction(45, 4)
    assert ledger.ratio_to_fc_scale == Fraction(9, 4)


def test_color_degree_cap_reduces_factorization_output_to_fc_scale() -> None:
    ledger = factorization_resource_ledger(100, 25, 4)
    assert ledger.color_degree == 100
    assert ledger.obeys_color_degree_cap
    assert ledger.rank_one_output_squared == 25
    assert ledger.ratio_to_fc_scale == Fraction(1, 4)


def test_restricted_color_counts_obey_the_support_sensitive_bounds() -> None:
    order = 7
    triples = tuple(latin_triples(order))
    colors = (0, 2, 5)
    actual = restricted_color_ledger(triples, colors)
    bounds = restricted_combinatorial_bounds(len(colors), order)
    assert actual.triple_count <= bounds["triple_count"]
    assert actual.incidence_count <= bounds["incidence_count"]
    assert actual.maximum_carrier_degree <= bounds["maximum_carrier_degree"]
    assert actual.maximum_row_pair_degree <= bounds["maximum_row_pair_degree"]
    assert actual.row_degree_square_sum <= bounds["row_degree_square_sum"]


def test_weighted_and_uniform_support_bounds_have_the_claimed_threshold() -> None:
    degree = 11
    support = degree**2
    uniform = uniform_support_gram_bound(support, degree)
    assert uniform == pytest.approx(float(degree), abs=1.0e-12)
    assert flat_fc_threshold(degree) == support

    coefficient_maximum = (support * degree**2) ** -0.25
    assert weighted_restricted_gram_bound(
        support, degree, coefficient_maximum
    ) == pytest.approx(float(degree), abs=1.0e-12)


def test_nonuniform_finite_gram_obeys_the_restricted_max_norm_bound() -> None:
    degree = 7
    triples = latin_triples(degree)
    raw = {0: 1.0, 2: 0.4j, 5: -0.25}
    norm = math.sqrt(sum(abs(value) ** 2 for value in raw.values()))
    z = {color: value / norm for color, value in raw.items()}
    gram = apply_incidence(row_pair_incidence(triples), z)
    actual = sum(abs(value) ** 2 for value in gram.values())
    bound = weighted_restricted_gram_bound(
        len(z), degree, max(map(abs, z.values()))
    )
    assert actual <= bound + 1.0e-12
    fourth_bound = fourth_norm_gram_bound(
        degree, sum(abs(value) ** 4 for value in z.values())
    )
    assert actual <= fourth_bound + 1.0e-12


def test_fourth_norm_threshold_is_the_effective_support_D_squared() -> None:
    degree = 13
    support = degree**2
    fourth_power_sum = 1 / support
    assert fourth_norm_fc_threshold(degree) == pytest.approx(
        fourth_power_sum, abs=1.0e-15
    )
    assert fourth_norm_gram_bound(
        degree, fourth_power_sum
    ) == pytest.approx(float(degree), abs=1.0e-12)


def test_active_exponents_record_the_flat_power_saving_only() -> None:
    ledger = active_exponent_ledger()
    assert ledger["D"].numerator == 16 and ledger["D"].denominator == 33
    assert ledger["mean_degree"] == Fraction(-1, 33)
    assert ledger["flat_full_gram"] == Fraction(5, 11)
    assert ledger["flat_full_saving_from_D"] == Fraction(1, 33)
    assert ledger["uniform_support_threshold"] == Fraction(32, 33)


def test_weighted_multiplicity_second_moment_would_close_at_D() -> None:
    degree = 121
    assert weighted_multiplicity_cauchy_bound(degree, degree) == degree


def test_new_kloosterman_theorem_ranges_have_the_audited_margins() -> None:
    ledger = kloosterman_active_range_ledger()
    assert ledger["mohammadi_D_box_product_margin"] == Fraction(31, 66)
    assert ledger["mohammadi_sqrt_D_box_product_deficit"] == Fraction(1, 66)
    assert ledger["mqw_balanced_threshold_margin"] == Fraction(2, 231)
    assert ledger["mqw_first_term_saving"] == Fraction(5, 66)
    assert ledger["mqw_second_term_saving"] == Fraction(1, 275)
    assert ledger["mqw_third_term_saving"] == Fraction(7, 704)
    assert ledger["mqw_sqrt_D_first_term_growth"] == Fraction(1, 22)
    assert ledger["bp_balanced_threshold_margin"] == Fraction(19, 924)
    assert ledger["bp_first_term_saving"] == Fraction(19, 1056)
    assert ledger["bp_second_term_saving"] == Fraction(1, 48)
    assert ledger["bp_third_term_saving"] == Fraction(5, 99)
    assert ledger["bp_saving_over_sqrt_shortfall"] == Fraction(1, 352)


def test_invalid_scalar_ledgers_are_rejected() -> None:
    with pytest.raises(ValueError):
        restricted_combinatorial_bounds(-1, 2)
    with pytest.raises(ValueError):
        weighted_restricted_gram_bound(2, 3, -0.1)
    with pytest.raises(ValueError):
        uniform_support_gram_bound(0, 3)
    with pytest.raises(ValueError):
        fourth_norm_fc_threshold(0)
