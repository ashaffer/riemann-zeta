from fractions import Fraction

import numpy as np
import pytest

from qp_finite_carrier_relative_trace import build_actual_carrier_matrix
from qp_q2_packet_cross_gram_discovery import (
    aligned_packet_coefficients,
    balanced_distinct_flow_dimension_lower_bound,
    block_log_polar_ledger,
    block_matrix,
    block_product_conservation,
    block_vertex_overlap_matrix,
    build_q2_residue_atom_model,
    centered_atom_gram_numerator,
    coarse_label_slices,
    coarse_packet_matrix,
    distinct_block_square_identity,
    empirical_log_polynomial_basis,
    matching_block_count_upper_bound,
    one_boundary_minimum_edge_count,
    packet_hilbert_schmidt_gram,
    physical_primitive_weights,
    log_polar_spectral_ledger,
    primitive_atomic_inverse_budget,
    primitive_reconstruction_values,
    q2_packet_discovery_ledger,
    short_residual_matching_blocks,
    weighted_atom_matrix,
    weighted_coarse_principal_matrix,
    weighted_principal_ledger,
)


def _projection(dimension: int) -> np.ndarray:
    return np.eye(dimension) - np.ones((dimension, dimension)) / dimension


def test_residue_atoms_are_complete_disjoint_permutation_orbits() -> None:
    model = build_q2_residue_atom_model(503)
    assert model.dimension == 20
    assert len(model.atoms) == 7
    assert model.coarse_edge_count == 36
    assert {atom.orbit_size for atom in model.atoms} <= {1, 3, 6}

    occupied: set[tuple[int, int]] = set()
    for atom in model.atoms:
        rows, columns = atom.support.nonzero()
        cells = set(zip(rows.tolist(), columns.tolist()))
        assert not occupied.intersection(cells)
        occupied.update(cells)

    fine = weighted_atom_matrix(
        model, {atom.residual: 1 for atom in model.selected_atoms}
    ).real
    literal = build_actual_carrier_matrix(503)
    assert fine == pytest.approx(literal.support.toarray())


def test_exact_q2_primitive_reconstruction_and_coarse_principal_part() -> None:
    model = build_q2_residue_atom_model(151)
    reconstructed = primitive_reconstruction_values(model)
    selected_residuals = {atom.residual for atom in model.selected_atoms}
    expected = np.asarray(
        [float(atom.residual in selected_residuals) for atom in model.atoms]
    )
    assert reconstructed == pytest.approx(expected, abs=6e-11)

    coefficients = aligned_packet_coefficients(model.q, model.degree_parameter)
    # The primitive packet coefficients are the non-q-divisible frequencies;
    # the omitted conditional expectation is exactly 2D/q on every unit atom.
    assert coefficients.shape == (model.q**2,)
    primitive = weighted_atom_matrix(model, physical_primitive_weights(model))
    fine = weighted_atom_matrix(
        model, {atom.residual: 1 for atom in model.selected_atoms}
    )
    coarse = coarse_packet_matrix(model, 0)
    assert fine == pytest.approx(
        primitive + float(Fraction(2 * model.degree_parameter, model.q)) * coarse
    )


def test_weighted_coarse_principal_is_a_disjoint_partial_permutation_sum() -> None:
    model = build_q2_residue_atom_model(503)
    slices = coarse_label_slices(model)
    assert len(slices) == model.dimension
    support_sum = sum(
        (matrix.astype(np.int64) for matrix in slices),
        start=np.zeros((model.dimension, model.dimension), dtype=np.int64),
    )
    # Summing over the third label recovers the unweighted coarse carrier.
    coarse = coarse_packet_matrix(model, 0).real
    assert support_sum == pytest.approx(coarse)
    assert max(matrix.nnz for matrix in slices) <= model.dimension

    rng = np.random.default_rng(240824)
    coefficients = rng.normal(size=model.dimension) + 1j * rng.normal(
        size=model.dimension
    )
    coefficients /= np.linalg.norm(coefficients)
    ledger = weighted_principal_ledger(model, coefficients)
    weighted = weighted_coarse_principal_matrix(model, coefficients)
    assert ledger.maximum_slice_row_degree == 1
    assert ledger.maximum_slice_column_degree == 1
    assert ledger.maximum_physical_support_overlap == 1
    assert ledger.hilbert_schmidt_squared <= ledger.hilbert_schmidt_squared_bound
    assert ledger.operator_norm <= ledger.operator_norm_bound
    assert ledger.schatten_fourth_power <= ledger.schatten_fourth_power_bound
    assert np.linalg.norm(weighted, ord=2) == pytest.approx(ledger.operator_norm)
    # The shell has fewer than q nodes, giving the advertised asymptotic
    # D/sqrt(q) and D^4/q^2 scales, with the exact principal factor 2.
    assert ledger.operator_norm_bound <= 2 * model.degree_parameter / np.sqrt(model.q)
    assert ledger.schatten_fourth_power_bound <= 16 * model.degree_parameter**4 / model.q**2


def test_centered_packet_gram_has_the_exact_degree_low_rank_correction() -> None:
    model = build_q2_residue_atom_model(503)
    dimension = model.dimension
    projection = _projection(dimension)
    exact_numerator = centered_atom_gram_numerator(model)
    direct = np.empty((len(model.atoms), len(model.atoms)))
    centered_atoms = [projection @ atom.support.toarray() @ projection for atom in model.atoms]
    for row, first in enumerate(centered_atoms):
        for column, second in enumerate(centered_atoms):
            direct[row, column] = np.vdot(first, second).real
    assert exact_numerator / dimension**2 == pytest.approx(direct)

    sizes = np.asarray([atom.orbit_size for atom in model.atoms])
    uncentered = np.diag(dimension**2 * sizes)
    assert np.linalg.matrix_rank((exact_numerator - uncentered).astype(float)) <= dimension

    frequencies = (0, 1, 7, model.q + 1)
    formula = packet_hilbert_schmidt_gram(model, frequencies)
    packets = [
        projection @ coarse_packet_matrix(model, frequency) @ projection
        for frequency in frequencies
    ]
    observed = np.asarray(
        [[np.vdot(first, second) for second in packets] for first in packets]
    )
    assert formula == pytest.approx(observed)

    # A larger finite shell has an extensive exact flat eigenspace of
    # balanced hyperedge-cycle flows, rather than degree modes.
    flow_model = build_q2_residue_atom_model(5_003)
    assert balanced_distinct_flow_dimension_lower_bound(flow_model) == 11


def test_short_residual_blocks_are_vertex_disjoint_triangle_matchings() -> None:
    model = build_q2_residue_atom_model(25_013)
    blocks = short_residual_matching_blocks(model)
    assert len(model.selected_atoms) == 13
    assert len(blocks) == 12
    assert max(len(block.atoms) for block in blocks) == 2
    for block in blocks:
        vertices: set[int] = set()
        for atom in block.atoms:
            assert not vertices.intersection(atom.vertex_set)
            vertices.update(atom.vertex_set)
        assert np.linalg.norm(block_matrix(block, model.dimension).toarray(), ord=2) <= 2 + 1e-12

    assert len(blocks) <= matching_block_count_upper_bound(
        model.q, model.degree_parameter, int(model.values[0])
    )
    left, right = distinct_block_square_identity(model, blocks)
    assert np.array_equal(left, right)

    # Ordered equal-size blocks cannot cover the same vertex multiset.  The
    # exact cancellation identity records the stronger boundary ordering.
    equal_size_pair = next(
        (first, second)
        for index, first in enumerate(blocks)
        for second in blocks[index + 1 :]
        if len(first.atoms) == len(second.atoms)
    )
    conservation = block_product_conservation(model, *equal_size_pair)
    assert conservation.individual_product_identities_hold
    assert conservation.cancelled_boundary_identity_holds
    assert conservation.residual_order_forces_boundary_order
    assert conservation.first_boundary_count > 0
    threshold = one_boundary_minimum_edge_count(
        model.q, model.degree_parameter, int(model.values[-1])
    )
    assert threshold > max(len(block.atoms) for block in blocks)


def test_actual_adjacent_blocks_have_a_nonzero_centered_tangent_cross_gram() -> None:
    # This is a literal prime-power shell, not an abstract matching model.
    # The two selected triangles share 83 and have complementary products
    # 71*73 and 64*81, differing by one.  Hence their residuals differ by
    # exactly 8*83 and occupy adjacent canonical blocks.
    model = build_q2_residue_atom_model(151)
    blocks = short_residual_matching_blocks(model)
    assert len(blocks) == 2
    assert blocks[1].index - blocks[0].index == 1
    first, second = blocks[0].atoms[0], blocks[1].atoms[0]
    shared = first.vertex_set.intersection(second.vertex_set)
    assert len(shared) == 1
    vertex_index = next(iter(shared))
    assert int(model.values[vertex_index]) == 83
    assert abs(first.residual - second.residual) == 8 * 83

    overlap = block_vertex_overlap_matrix(blocks, model.dimension)
    assert overlap[0, 1] == 1
    projection = _projection(model.dimension)
    first_matrix = block_matrix(blocks[0], model.dimension).toarray()
    second_matrix = block_matrix(blocks[1], model.dimension).toarray()
    assert np.linalg.norm(first_matrix @ second_matrix, ord=2) == pytest.approx(2.0)
    assert np.linalg.norm(
        projection @ first_matrix @ projection @ second_matrix @ projection,
        ord=2,
    ) > 1.1


def test_actual_prime_blocks_can_have_branching_cross_gram_above_two() -> None:
    # At q=4751 one earlier triangle shares two different vertices with two
    # vertex-disjoint triangles in a later short block.  This is a faithful
    # prime-power/product-window counterexample to treating cross-block
    # overlap as a matching or assigning it norm at most two.
    model = build_q2_residue_atom_model(4_751)
    blocks = {block.index: block for block in short_residual_matching_blocks(model)}
    first = blocks[2]
    second = blocks[23]
    assert len(first.atoms) == 1
    assert len(second.atoms) == 2
    first_vertices = set(first.atoms[0].vertex_set)
    assert sum(bool(first_vertices.intersection(atom.vertex_set)) for atom in second.atoms) == 2

    first_matrix = block_matrix(first, model.dimension).toarray()
    second_matrix = block_matrix(second, model.dimension).toarray()
    assert np.linalg.norm(first_matrix @ second_matrix, ord=2) == pytest.approx(
        np.sqrt(6.0)
    )
    projection = _projection(model.dimension)
    assert np.linalg.norm(
        projection @ first_matrix @ projection @ second_matrix @ projection,
        ord=2,
    ) > 2.29


def test_log_linear_polar_does_not_remove_the_actual_branching_mode() -> None:
    model = build_q2_residue_atom_model(4_751)
    basis = empirical_log_polynomial_basis(model.values, model.q, 4)
    assert basis.T @ basis == pytest.approx(np.eye(5))
    ledger = block_log_polar_ledger(model)
    assert ledger.constant_projected_ratio == pytest.approx(1.147838153)
    assert ledger.linear_projected_ratio == pytest.approx(1.147894752)
    assert ledger.maximum_constant_projected_cross_norm > 2.29
    assert ledger.maximum_linear_projected_cross_norm > 2.29

    literal = build_actual_carrier_matrix(4_751)
    fine = log_polar_spectral_ledger(literal.support, literal.values, literal.q)
    assert fine.linear_projected_norm / fine.centered_norm > 0.999
    assert fine.most_linear_correlation_squared < 0.03


def test_coarse_operator_has_a_real_log_linear_mode_but_weighted_hs_closes_it() -> None:
    model = build_q2_residue_atom_model(25_013)
    coarse = sum(
        (atom.support.astype(float) for atom in model.atoms),
        start=np.zeros((model.dimension, model.dimension)),
    )
    ledger = log_polar_spectral_ledger(coarse, model.values, model.q)
    assert ledger.most_linear_correlated_eigenvalue < -10.0
    assert ledger.most_linear_correlation_squared > 0.77
    assert ledger.corresponding_degree_eight_polynomial_mass > 0.81
    # It is only one coarse mode: deleting x does not remove the unrelated
    # positive extreme eigenvector.  The coefficient-sensitive HS theorem,
    # not a finite polynomial deletion, controls the full principal block.
    assert ledger.linear_projected_norm / ledger.centered_norm > 0.999


def test_atomic_inverse_dft_rules_out_a_coefficient_uniform_q_budget() -> None:
    energy, q_budget = primitive_atomic_inverse_budget(107)
    assert energy == Fraction(106, 107**3)
    assert q_budget == Fraction(106, 107**2)

    model = build_q2_residue_atom_model(107)
    atom = model.selected_atoms[0]
    weights = {
        other.residual: Fraction(
            int(other.residual == atom.residual), 1
        )
        - Fraction(
            int((other.residual - atom.residual) % model.q == 0), model.q
        )
        for other in model.atoms
    }
    synthesis = weighted_atom_matrix(model, weights).real
    centered = _projection(model.dimension) @ synthesis @ _projection(model.dimension)
    # Even after deleting the physical constant and degree cross channels,
    # the squared norm is order one while q*||alpha||_2^2 is order 1/q.
    assert np.linalg.norm(centered, ord=2) ** 2 > 50 * float(q_budget)


def test_discovery_ledger_tracks_all_three_candidate_subtractions() -> None:
    model = build_q2_residue_atom_model(25_013)
    ledger = q2_packet_discovery_ledger(model)
    assert ledger.maximum_block_norm <= 2 + 1e-12
    assert ledger.cross_block_vertex_overlaps == 1
    assert ledger.fine_doubly_centered_norm == pytest.approx(2.5428085030)
    assert ledger.primitive_doubly_centered_norm == pytest.approx(2.5185714991)
    assert ledger.centered_atom_gram_correction_rank <= model.dimension
