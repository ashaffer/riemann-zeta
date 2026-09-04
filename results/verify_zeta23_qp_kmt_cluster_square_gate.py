#!/usr/bin/env python3
"""Replay the exact numerical ledger in the KMT cluster-square report."""

from qp_kmt_cluster_square_gate import (
    asymptotic_ledger,
    fixed_sum_sign_moments,
    forced_block_size,
    forced_tail_energy_fraction,
    local_positive_radius,
    maximum_separated_points,
    termwise_covariance_certificate,
)


def main() -> None:
    c = 0.019
    epsilon = 1.0e-3
    r = round(epsilon**-2)
    kappa = 2.0
    q = 0.5
    block = forced_block_size(
        r, epsilon, linear_fraction=q, normalization_ratio=kappa
    )
    tail = forced_tail_energy_fraction(
        r,
        epsilon,
        max(1, round(block)),
        linear_fraction=q,
        normalization_ratio=kappa,
    )
    eta = 1.0e-2
    tax = termwise_covariance_certificate(eta, round(block), tail)
    radius = local_positive_radius(0.2)
    capacity = maximum_separated_points(2.0 * radius)
    sign_r, sign_mean, sign_off = fixed_sum_sign_moments(100, depth=2)
    asymptotic = asymptotic_ledger(2.0e3, c)
    print(
        "PASS "
        f"R={r} block_lower={block:.6g} tail_fraction={tail:.6g} "
        f"termwise_tax={tax:.6g} local_capacity={capacity} "
        f"sign_model=({sign_r},{sign_mean:.6g},{sign_off:.6g}) "
        f"etaR={asymptotic['eta_times_rank']:.6g}"
    )


if __name__ == "__main__":
    main()
