import math

import numpy as np

from qp_signed_discrepancy_gate import (
    conditional_sign_mean,
    continuum_grid_audit,
    half_grid_nodes,
    half_grid_normalized_value,
    perturbed_half_grid_error_bound,
    required_sign_carrier,
    verify_finite_polar_identity,
)


def test_grid_audit_and_carrier_scale() -> None:
    audit = continuum_grid_audit(
        lower=10.0,
        upper=1000.0,
        shell_width=0.2,
        coefficient_l1=100.0,
        carrier=20.0,
        epsilon=0.01,
    )
    assert math.isclose(audit.derivative_bound, 20.0)
    assert math.isclose(audit.mesh, 0.005)
    assert audit.grid_points == 198001
    assert required_sign_carrier(7.5, 0.01) == 750.0


def test_conditional_sign_mean() -> None:
    atom = np.array([-0.7, 0.2, 0.8, 0.3])
    assert math.isclose(conditional_sign_mean(atom, 2), 2.0 * np.mean(atom))
    assert conditional_sign_mean(atom, 0) == 0.0


def test_half_grid_defeats_arbitrary_signed_coefficients() -> None:
    aperture = 137.0
    nodes = half_grid_nodes(np.array([2, 7, 11, 19]), aperture)
    coefficients = np.array([4.0, -1.5, 0.25, 2.0])
    assert math.isclose(
        half_grid_normalized_value(coefficients, nodes, aperture),
        -1.0,
        abs_tol=1e-12,
    )
    assert math.isclose(
        perturbed_half_grid_error_bound(
            phase_perturbation=1e-3, normalized_total_variation=100.0
        ),
        5e-5,
    )


def test_finite_signed_tv_polarity() -> None:
    matrix = np.array(
        [
            [1.0, 0.2, -0.4, 0.7],
            [0.1, 1.0, 0.5, -0.2],
            [-0.3, 0.4, 1.0, 0.1],
        ]
    )
    assert verify_finite_polar_identity(matrix)
