import numpy as np

from qp_log_product_polar_gate import (
    centered_log_rayleigh_lower_bound,
    coarse_weighted_bounds,
    log_rayleigh_identity,
    product_mean_boundary_lower_bound,
    residual_log_error,
)


def test_exact_triangle_log_rayleigh_identity() -> None:
    values = np.array([-0.13, 0.04, 0.09, -0.08, -0.02, 0.101])
    replay = log_rayleigh_identity(values, [(0, 1, 2), (3, 4, 5)])
    assert np.isclose(replay.matrix_quadratic, replay.triangle_quadratic)
    assert replay.residual_square_mass < 2.0e-6
    assert replay.matrix_quadratic < 0


def test_log_error_is_at_the_D_over_q_squared_scale() -> None:
    error = residual_log_error(q=100_003, degree_parameter=265)
    assert error < 2.7e-8
    assert error > 2.6e-8


def test_product_mean_boundary_has_no_power_at_project_scale() -> None:
    q = 10**9
    degree = q ** (16 / 33)
    # Even using the full fine-window separation, q covered vertices give
    # total log signal only D/q=o(1).
    lower = product_mean_boundary_lower_bound(
        triangle_count=q // 3,
        log_center_separation=degree / q**2,
        log_block_radius=0.0,
        shell_log_diameter=0.4,
    )
    assert lower < 1


def test_weighted_coarse_principal_is_schatten_small() -> None:
    q = 1_000_003
    degree = 811
    support = 15_000
    bounds = coarse_weighted_bounds(
        q=q,
        degree_parameter=degree,
        layer_entry_cap=q,
        cell_overlap_cap=2,
        row_degree_cap=2,
        z_l1=np.sqrt(support),
        z_l2=1.0,
    )
    assert bounds.hilbert_schmidt_squared < 6
    assert bounds.operator_norm < 0.5
    assert bounds.schatten_four_fourth < 1


def test_centered_log_lower_bound_subtracts_only_tiny_residual_error() -> None:
    bound = centered_log_rayleigh_lower_bound(
        weighted_triangle_log_mass=12.0,
        triangle_count=100,
        log_error=1.0e-4,
        log_norm_squared=4.0,
    )
    assert np.isclose(bound, (12.0 - 1.0e-6) / 4.0)
