import numpy as np

from qp_residual_block_triangle_matching import affine_plane_sts9_parallel_classes
from qp_weighted_triangle_rademacher_square import (
    coefficient_sensitive_rademacher_bound,
    coefficient_sensitive_square_function_bound,
    comparable_support_rademacher_bound,
    exact_rademacher_fourth_average,
    rademacher_upper_bound,
    schatten_fourth_power,
    square_function_gram_bounds,
    validate_linear_matching_partition,
    weighted_class_matrices,
)


def test_randomized_weighted_triangle_trace_has_sharp_degree_budget():
    classes = affine_plane_sts9_parallel_classes()
    z = np.array([1, 2j, -1, 3, -2j, 1, 0.5, -0.25, 2], dtype=complex)
    z /= np.linalg.norm(z)
    _, degree = validate_linear_matching_partition(9, classes)
    matrices = weighted_class_matrices(9, classes, z)
    average = exact_rademacher_fourth_average(matrices)
    assert degree == 4
    assert average <= rademacher_upper_bound(degree, np.linalg.norm(z)) + 1e-10


def test_square_function_gram_has_linear_degree_scale():
    classes = affine_plane_sts9_parallel_classes()
    z = np.ones(9) / 3
    matrices = weighted_class_matrices(9, classes, z)
    right, left = square_function_gram_bounds(matrices)
    assert right <= 14 * 4 + 1e-10
    assert left <= 14 * 4 + 1e-10


def test_all_plus_can_be_much_larger_than_random_sign_budget():
    classes = affine_plane_sts9_parallel_classes()
    z = np.ones(9) / 3
    matrices = weighted_class_matrices(9, classes, z)
    all_plus = schatten_fourth_power(sum(matrices))
    randomized = exact_rademacher_fourth_average(matrices)
    assert all_plus > randomized


def test_nonlinear_partition_is_rejected():
    bad = [[(0, 1, 2)], [(0, 1, 3)]]
    try:
        validate_linear_matching_partition(4, bad)
    except ValueError:
        pass
    else:
        raise AssertionError("a repeated vertex pair must be rejected")


def test_coefficient_sensitive_square_and_randomized_bounds():
    classes = affine_plane_sts9_parallel_classes()
    z = np.array([1, -1j, 2, 0, 0, 0, 0, 0, 0], dtype=complex)
    z /= np.linalg.norm(z)
    _, degree = validate_linear_matching_partition(9, classes)
    matrices = weighted_class_matrices(9, classes, z)
    right, left = square_function_gram_bounds(matrices)
    square_bound = coefficient_sensitive_square_function_bound(
        degree, np.linalg.norm(z), np.max(np.abs(z))
    )
    assert right <= square_bound + 1.0e-10
    assert left <= square_bound + 1.0e-10
    average = exact_rademacher_fourth_average(matrices)
    assert average <= coefficient_sensitive_rademacher_bound(
        degree, np.linalg.norm(z), np.max(np.abs(z))
    ) + 1.0e-10


def test_factor_two_bin_has_D_squared_over_M_randomized_scale():
    degree = 100
    support = 1_000
    bound = comparable_support_rademacher_bound(
        degree, support, 1.0, squared_comparability=4.0
    )
    assert bound == 48 * degree * (4 * degree / support)
    assert comparable_support_rademacher_bound(
        degree, 10, 1.0, squared_comparability=4.0
    ) == 48 * degree
