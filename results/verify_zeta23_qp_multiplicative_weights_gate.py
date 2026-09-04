#!/usr/bin/env python3
"""Replay the finite multiplicative-weights/Bessel gate ledger."""

from qp_multiplicative_weights_gate import (
    exponent_gap,
    i0_normalized_halfspace_limit,
    orthant_witness_upper_bound,
    scalar_bessel_floor,
    sufficient_dichotomy_iterations,
)


def main() -> None:
    epsilon = 0.01
    minimum_mass = 1.0e-6
    iterations = sufficient_dichotomy_iterations(epsilon, minimum_mass)
    witness = orthant_witness_upper_bound(
        epsilon, epsilon / 2.0, iterations, minimum_mass
    )
    floor = scalar_bessel_floor(1.0e-12, 0.001, 10_000)
    halfspace = i0_normalized_halfspace_limit(1.0)
    assert witness <= -epsilon / 2.0
    assert floor.normalized_lower_bound > 0.0
    assert 0.0 < halfspace < 1.0
    assert exponent_gap() > 0.0
    print(
        "PASS "
        f"iterations={iterations} witness={witness:.9g} "
        f"bessel_floor={floor.normalized_lower_bound:.9g} "
        f"halfspace_partition={halfspace:.9g} "
        f"kappa_gap={exponent_gap():.9g}"
    )


if __name__ == "__main__":
    main()

