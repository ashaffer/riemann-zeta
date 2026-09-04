#!/usr/bin/env python3
"""Independent replay for the QP spectral-null/grouping gate."""

from __future__ import annotations

import math

import numpy as np

from qp_spectral_null_grouping_gate import (
    FULL_APERTURE_EXPONENT,
    QP_KAPPA,
    bernoulli_null_certificate,
    bernoulli_support_upper_bound,
    finite_pool_delsarte_value,
    finite_pool_positive_depth,
    grouped_product_depth_upper,
    haar_adaptive_support_log_bound,
    required_group_size,
    target_metric_power,
)


def main() -> None:
    nodes = np.asarray([-0.2, -0.083, 0.047, 0.119, 0.197])
    certificate = bernoulli_null_certificate(nodes, lower=13.0)
    assert certificate.max_fourier_residual < 1e-12
    assert abs(certificate.central_atom - 2.0**-5) < 1e-15
    assert abs(certificate.depth - 1.0 / 31.0) < 1e-15
    assert certificate.upper == np.sum(certificate.aliases)

    y = 100_000_000.5
    support_bound = bernoulli_support_upper_bound(
        y=y,
        width=0.2,
        node_count=20_000_000,
        lower=y**0.01,
    )
    assert support_bound < y**FULL_APERTURE_EXPONENT

    assert grouped_product_depth_upper(5) == 1.0 / 31.0
    assert required_group_size(10_000, 2.0**-20) == 500
    assert abs(target_metric_power() - (1.0 - 2.0 * QP_KAPPA)) < 1e-15
    assert haar_adaptive_support_log_bound(
        node_count=10**6,
        max_harmonic=10**9,
        depth=0.05,
    ) < -1000.0

    atoms = np.asarray([[-1.0, 0.0], [0.0, -1.0]])
    depth = finite_pool_positive_depth(atoms)
    delsarte = finite_pool_delsarte_value(atoms)
    assert abs(depth - 1.0 / (delsarte - 1.0)) < 1e-12

    print("QP spectral-null/grouping verifier: PASS")
    print(f"central_atom={certificate.central_atom:.12g}")
    print(f"depth={certificate.depth:.12g}")
    print(f"support_upper={certificate.upper:.12g}")
    print(f"half_integer_budget={support_bound:.12g}")
    print(f"metric_power={target_metric_power():.10f}")
    print(f"toy_delsarte={delsarte:.12g}")


if __name__ == "__main__":
    main()
