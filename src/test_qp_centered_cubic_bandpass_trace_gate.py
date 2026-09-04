import numpy as np

from qp_centered_cubic_bandpass_trace_gate import (
    centered_third_tensor,
    cubic_value,
    hard_carry_slice,
    partial_trace,
    scalar_centering_identity,
    side_block_max_degrees,
    signed_cubic_tensors,
    spline_cosine_transform,
    sym_one_minus_partial_trace,
    trace_and_row_sum_barrier_tensor,
    zero_sum_partial_permutation_barrier,
)


def test_scalar_centering_identity() -> None:
    nodes = np.array([0.07, 0.11, 0.19, 0.31])
    coefficients = np.array([0.8, -0.3, 0.4, -0.6])
    transform = lambda omega: spline_cosine_transform(omega, 37.0, 6)
    central, right, _, variance = scalar_centering_identity(
        nodes, coefficients, transform
    )
    assert variance > 0.0
    assert np.isclose(central, right, atol=2.0e-13)


def test_three_one_minus_orientations_add_on_the_diagonal() -> None:
    nodes = np.array([0.08, 0.13, 0.22])
    coefficients = np.array([0.5, -0.7, 0.2])
    transform = lambda omega: np.exp(-omega * omega)
    all_plus, minus_k, sym_one_minus, raw = signed_cubic_tensors(
        nodes, transform
    )
    assert np.isclose(
        cubic_value(raw, coefficients),
        0.25 * cubic_value(all_plus, coefficients)
        + 0.75 * cubic_value(minus_k, coefficients),
    )
    assert np.isclose(
        cubic_value(sym_one_minus, coefficients),
        cubic_value(minus_k, coefficients),
    )


def test_symmetrized_trace_contains_doubling_correlation() -> None:
    nodes = np.array([0.09, 0.17, 0.28, 0.41])
    transform = lambda omega: np.cos(3.0 * omega) * np.exp(-omega * omega)
    sym_one_minus = signed_cubic_tensors(nodes, transform)[2]
    assert np.allclose(
        partial_trace(sym_one_minus),
        sym_one_minus_partial_trace(nodes, transform),
        atol=2.0e-13,
    )


def test_actual_half_integer_core_slices_are_trace_free_and_side_partial() -> None:
    # These actual prime powers have the exact absolute-log carry
    # u_8+u_16=u_23 about Y=23/2.
    center = 11.5
    actual_nodes = np.array([8.0, 16.0, 23.0])
    nodes = np.abs(np.log(actual_nodes / center))
    sides = actual_nodes > center
    bandwidth = 500.0
    core_radius = 0.2
    assert core_radius / bandwidth < np.min(nodes)
    nonzero_entries = 0
    for fixed in range(len(nodes)):
        matrix = hard_carry_slice(nodes, fixed, bandwidth, core_radius)
        nonzero_entries += int(np.sum(matrix != 0.0))
        assert np.trace(matrix) == 0.0
        max_row, max_column = side_block_max_degrees(matrix, sides, sides)
        assert max_row <= 1
        assert max_column <= 1
    assert nonzero_entries == 2


def test_an_actual_exact_carry_survives_centering() -> None:
    center = 11.5
    actual_nodes = np.array([8.0, 16.0, 23.0])
    nodes = np.abs(np.log(actual_nodes / center))
    assert np.isclose(nodes[0] + nodes[1], nodes[2], atol=1.0e-15)
    transform = lambda omega: spline_cosine_transform(omega, 10_000.0, 8)
    tensor = centered_third_tensor(nodes, transform)
    assert tensor[0, 1, 2] > 0.249


def test_centered_tensor_matches_direct_tensor_contraction() -> None:
    nodes = np.array([0.06, 0.14, 0.24])
    coefficients = np.array([-0.4, 0.9, 0.1])
    transform = lambda omega: spline_cosine_transform(omega, 29.0, 4)
    tensor = centered_third_tensor(nodes, transform)
    central, _, _, _ = scalar_centering_identity(nodes, coefficients, transform)
    assert np.isclose(cubic_value(tensor, coefficients), central)


def test_trace_and_all_ones_row_sums_do_not_bound_diagonal_norm() -> None:
    scale = 7.0
    tensor, e1, _ = trace_and_row_sum_barrier_tensor(8, scale)
    ones = np.ones(8)
    assert np.allclose(partial_trace(tensor), 0.0, atol=2.0e-13)
    assert np.allclose(
        np.einsum("ijk,i->jk", tensor, ones), 0.0, atol=2.0e-13
    )
    assert np.isclose(cubic_value(tensor, e1), scale)


def test_zero_sum_partial_permutation_barrier_keeps_sqrt_order_norm() -> None:
    order = 12
    matrix = zero_sum_partial_permutation_barrier(order)
    assert np.allclose(np.sum(matrix, axis=0), 0.0)
    assert np.allclose(np.sum(matrix, axis=1), 0.0)
    assert np.isclose(np.trace(matrix), 0.0)
    norm = np.linalg.svd(matrix, compute_uv=False)[0]
    assert norm >= np.sqrt(order)
