import math

import numpy as np
import pytest
from scipy.sparse import coo_matrix, kron

from qp_four_cycle_h_graph_lab import (
    build_pair_incidence_graph,
    filtered_pair_incidence_graph,
)
from qp_four_cycle_hostile_lab import FourCycleCore, build_four_cycle_core
from qp_four_cycle_pair_state_spectral_probe import (
    CompletionTerm,
    build_color_partial_permutations,
    build_diagonal_tensor_transfer,
    completion_pair_classification,
    directed_completion_groups,
    largest_singular_triplets,
    pair_state_mode_profile,
    schatten_fourth_mass,
    schatten_identity_ledger,
    sign_gauge_ledger,
)


def latin_core(order: int = 3) -> FourCycleCore:
    rows = []
    columns = []
    colors = []
    for row in range(order):
        for column in range(order):
            rows.append(row)
            columns.append(column)
            colors.append((row + column) % order)
    return FourCycleCore(
        q=101,
        aperture=1.5,
        width=0.2,
        cutoff=1.0,
        values=np.asarray([11, 13, 17][:order], dtype=np.int64),
        rows=np.asarray(rows, dtype=np.int32),
        columns=np.asarray(columns, dtype=np.int32),
        colors=np.asarray(colors, dtype=np.int32),
        weights=np.ones(order * order, dtype=np.int64),
    )


def expand_compressed_transfer(transfer) -> np.ndarray:
    dimension_square = transfer.dimension**2
    coordinates = transfer.matrix.tocoo()
    return coo_matrix(
        (
            coordinates.data,
            (
                transfer.row_pair_codes[coordinates.row],
                transfer.column_pair_codes[coordinates.col],
            ),
        ),
        shape=(dimension_square, dimension_square),
    ).toarray()


def test_color_slices_are_partial_permutations_and_tensor_builder_is_literal() -> None:
    core = latin_core()
    color_weights = np.asarray([1.0, 2.0, 3.0])
    partials = build_color_partial_permutations(core, kernel_weights=False)
    assert len(partials) == 3
    assert all(item.entries == 3 for item in partials.values())
    assert all(item.maximum_row_support == 1 for item in partials.values())
    assert all(item.maximum_column_support == 1 for item in partials.values())

    expected = sum(
        color_weights[color] * kron(item.matrix, item.matrix).toarray()
        for color, item in partials.items()
    )
    transfer = build_diagonal_tensor_transfer(
        core,
        color_weights,
        kernel_weights=False,
        sector="raw",
    )
    np.testing.assert_array_equal(expand_compressed_transfer(transfer), expected)


def test_schatten_identity_and_swap_sector_decomposition_are_exact() -> None:
    core = latin_core()
    color_weights = np.asarray([1.0, 2.0, 3.0])
    ledger = schatten_identity_ledger(
        core, color_weights, kernel_weights=False
    )
    assert ledger.absolute_error == 0.0
    assert ledger.transfer_fourth_mass == ledger.completion_square_mass

    sector_masses = []
    sectors = {}
    for sector in (
        "diagonal",
        "symmetric_offdiagonal",
        "antisymmetric_offdiagonal",
    ):
        transfer = build_diagonal_tensor_transfer(
            core,
            color_weights,
            kernel_weights=False,
            sector=sector,
        )
        sectors[sector] = transfer
        sector_masses.append(float(schatten_fourth_mass(transfer.matrix)))
    assert sum(sector_masses) == ledger.transfer_fourth_mass
    gauge = sign_gauge_ledger(
        sectors["symmetric_offdiagonal"].matrix,
        sectors["antisymmetric_offdiagonal"].matrix,
    )
    assert gauge.equivalent
    assert gauge.conflicting_edges == 0
    assert gauge.maximum_ratio_error == 0.0


def test_additive_tangent_pairs_and_energy_smith_invariants_are_classified() -> None:
    center = 1_000
    step = 20
    first_parameter = 3
    second_parameter = 5

    def completion(parameter: int) -> tuple[int, int, int, int]:
        return (
            center + step + parameter,
            center + 2 * step + parameter,
            center - step - parameter,
            center + step - parameter,
        )

    value_completions = (
        completion(first_parameter),
        completion(second_parameter),
    )
    values = np.asarray(sorted({value for item in value_completions for value in item}))
    lookup = {int(value): index for index, value in enumerate(values)}
    indexed = tuple(
        tuple(lookup[value] for value in item) for item in value_completions
    )
    core = FourCycleCore(
        q=2_001,
        aperture=1.5,
        width=0.2,
        cutoff=1.0,
        values=values,
        rows=np.empty(0, dtype=np.int32),
        columns=np.empty(0, dtype=np.int32),
        colors=np.empty(0, dtype=np.int32),
        weights=np.empty(0),
    )
    groups = {
        (0, 0, 0, 0): tuple(
            CompletionTerm(item, 1.0) for item in indexed
        )
    }
    classification = completion_pair_classification(
        core, groups, None, tangent_radius=100
    )
    assert classification.total_mass == 4.0
    assert classification.pair_diagonal_mass == 2.0
    assert classification.genuine_offdiagonal_mass == 2.0
    assert classification.additive_tangent_mass == 2.0
    assert classification.near_square_tangent_mass == 2.0
    assert classification.rank_one_secant_mass == 0.0
    assert classification.additive_tangent_pairs == 2
    assert sum(item.ordered_pairs for item in classification.smith_masses) == 2
    assert all(item.first_invariant > 0 for item in classification.smith_masses)
    assert all(item.second_invariant > 0 for item in classification.smith_masses)


def test_q25013_schatten_mass_separates_the_genuine_pair_energy() -> None:
    core = build_four_cycle_core(
        25_013,
        width=0.2,
        cutoff=12.0,
        kind="prime_powers",
        quadrature_order=32,
    )
    live_colors = np.unique(core.colors)
    color_weights = np.zeros(core.dimension)
    color_weights[live_colors] = 1.0 / math.sqrt(len(live_colors))
    ledger = schatten_identity_ledger(core, color_weights)
    assert core.dimension == 535
    assert len(core.rows) == 4_002
    assert len(live_colors) == 518
    assert ledger.tensor_entries == 39_052
    assert ledger.directed_completions == 79_778
    assert ledger.color_matrices == 70_906
    assert ledger.absolute_error < 3.0e-14

    groups = directed_completion_groups(core)
    classification = completion_pair_classification(
        core,
        groups,
        color_weights,
        tangent_radius=5 * math.ceil(math.sqrt(core.geometric_degree_cap)),
    )
    assert classification.ordered_pairs == 126_276
    assert classification.genuine_offdiagonal_pairs == 96
    assert classification.rank_one_secant_pairs == 0
    assert classification.additive_tangent_pairs == 0
    assert classification.near_square_tangent_pairs == 0
    assert len(classification.smith_masses) == 6
    assert classification.total_mass == pytest.approx(
        ledger.transfer_fourth_mass, abs=3.0e-14
    )
    assert classification.genuine_offdiagonal_mass / classification.total_mass < 0.001


def test_q25013_large_modes_split_into_diagonal_and_small_shift_incidence_modes() -> None:
    core = build_four_cycle_core(
        25_013,
        width=0.2,
        cutoff=12.0,
        kind="prime_powers",
        quadrature_order=32,
    )
    live_colors = np.unique(core.colors)
    color_weights = np.zeros(core.dimension)
    color_weights[live_colors] = 1.0 / math.sqrt(len(live_colors))

    diagonal = build_diagonal_tensor_transfer(
        core, color_weights, sector="diagonal"
    )
    diagonal_modes = largest_singular_triplets(diagonal.matrix, rank=1)
    diagonal_profile = pair_state_mode_profile(
        core,
        diagonal.row_pair_codes,
        diagonal.column_pair_codes,
        diagonal.matrix,
        diagonal_modes.left_vectors[:, 0],
        diagonal_modes.right_vectors[:, 0],
        singular_value=diagonal_modes.singular_values[0],
        tangent_threshold=math.ceil(core.geometric_degree_cap),
    )
    assert diagonal_profile.left_diagonal_mass == pytest.approx(1.0)
    assert diagonal_profile.right_diagonal_mass == pytest.approx(1.0)
    assert diagonal_profile.principal_tangent_influence_fraction == pytest.approx(1.0)

    graph = filtered_pair_incidence_graph(
        core,
        build_pair_incidence_graph(core),
        keep="all_five_distinct",
    )
    incidence_modes = largest_singular_triplets(graph.weighted, rank=2)
    incidence_profile = pair_state_mode_profile(
        core,
        graph.left_pair_codes,
        graph.right_pair_codes,
        graph.weighted,
        incidence_modes.left_vectors[:, 0],
        incidence_modes.right_vectors[:, 0],
        singular_value=incidence_modes.singular_values[0],
        tangent_threshold=math.ceil(core.geometric_degree_cap),
    )
    assert 2.0 < incidence_profile.singular_value < 2.2
    assert incidence_profile.left_diagonal_mass == 0.0
    assert incidence_profile.right_diagonal_mass == 0.0
    assert incidence_profile.principal_tangent_influence_fraction == 0.0
    assert incidence_profile.threshold_tangent_influence_fraction == pytest.approx(1.0)
    assert incidence_profile.weighted_ninetieth_absolute_shift < core.geometric_degree_cap
    assert all(
        item.first_invariant == 1
        for item in incidence_profile.smith_influences
        if item.influence_fraction > 1.0e-12
    )
