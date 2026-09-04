"""Independent finite replay for the signed-discrepancy affine gate."""

from __future__ import annotations

import math

import numpy as np

from qp_signed_discrepancy_gate import (
    conditional_sign_mean,
    continuum_grid_audit,
    half_grid_nodes,
    half_grid_normalized_value,
    verify_finite_polar_identity,
)


def main() -> None:
    matrix = np.array(
        [
            [1.0, -0.2, 0.4, 0.8],
            [0.3, 1.0, -0.6, 0.1],
            [-0.5, 0.7, 1.0, -0.3],
        ]
    )
    assert verify_finite_polar_identity(matrix)

    atom = np.array([-0.9, -0.1, 0.4, 0.8, 0.2, 0.6])
    assert math.isclose(conditional_sign_mean(atom, 2), 2.0 * atom.mean())

    aperture = 211.0
    nodes = half_grid_nodes(np.array([0, 5, 13, 21, 34]), aperture)
    coefficients = np.array([8.0, -2.0, 0.5, 1.25, -0.75])
    assert math.isclose(
        half_grid_normalized_value(coefficients, nodes, aperture),
        -1.0,
        abs_tol=1e-12,
    )

    audit = continuum_grid_audit(
        lower=3.0,
        upper=503.0,
        shell_width=0.2,
        coefficient_l1=50.0,
        carrier=10.0,
        epsilon=0.02,
    )
    assert math.isclose(audit.mesh, 0.01)
    assert audit.grid_points == 50001
    print("verified ZETA23 signed-discrepancy affine-carrier gate")


if __name__ == "__main__":
    main()
