import numpy as np

from qp_q2_principal_weighted_fc import (
    CoarseLayerBounds,
    coarse_principal_upper_bounds,
    exact_schatten_fourth_power,
    project_scale_exponents,
    weighted_coarse_matrix,
)


def test_project_scale_principal_channel_is_power_small():
    exponents = project_scale_exponents()
    assert exponents["operator"] == -1 / 32
    assert exponents["hilbert_schmidt_squared"] == -1 / 16
    assert exponents["schatten_fourth"] == -1 / 8


def test_finite_weighted_layer_inequality():
    # Three partial-permutation layers with at most one nonzero per row and
    # column and cell-overlap one.
    layers = np.zeros((3, 4, 4), dtype=float)
    layers[0, 0, 1] = layers[0, 1, 0] = 1
    layers[1, 1, 2] = layers[1, 2, 1] = 1
    layers[2, 2, 3] = layers[2, 3, 2] = 1
    z = np.array([1.0, -2.0, 0.5])
    scale = 0.07
    matrix = weighted_coarse_matrix(layers, z, scale)
    bounds = CoarseLayerBounds(
        shell_size=3,
        max_layer_degree=1,
        max_layer_entries=2,
        max_cell_overlap=1,
    )
    op, hs2, s4 = coarse_principal_upper_bounds(
        q=100.0,
        D=7.0,
        z_l2=float(np.linalg.norm(z)),
        bounds=bounds,
    )
    assert np.linalg.norm(matrix, 2) <= op + 1e-12
    assert np.linalg.norm(matrix, "fro") ** 2 <= hs2 + 1e-12
    assert exact_schatten_fourth_power(matrix) <= s4 + 1e-12


def test_complex_weights_are_supported():
    layers = np.zeros((2, 2, 2), dtype=float)
    layers[0, 0, 1] = 1
    layers[1, 1, 0] = 1
    matrix = weighted_coarse_matrix(layers, np.array([1j, 2.0]), 0.5)
    assert matrix[0, 1] == 0.5j
    assert matrix[1, 0] == 1.0

