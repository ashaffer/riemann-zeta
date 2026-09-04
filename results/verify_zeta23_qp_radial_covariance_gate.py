#!/usr/bin/env python3
"""Replay the project exponents and a finite exact collision count."""

import math

import numpy as np

from qp_radial_covariance_gate import (
    all_integer_factor_pair_bound,
    exponent_ledger,
    fejer_transverse_dual,
    near_reflection_pairs,
    sampled_pair_block_gram,
)


def main() -> None:
    aperture = 50.0 / 33.0
    depth = 0.019
    ledger = exponent_ledger(aperture, depth)
    print(f"A={aperture:.12f}")
    print(f"d={depth:.12f}")
    print(f"collision exponent 2-A={ledger.collision_pair_exponent:.12f}")
    print(f"long exponent 1-d={ledger.long_carrier_exponent:.12f}")
    print(f"survival gap A-1-d={ledger.survival_gap:.12f}")

    Y = 100.5
    B = Y**aperture
    values = range(82, 124)
    pairs = near_reflection_pairs(values, Y, B)
    universal_bound = all_integer_factor_pair_bound(Y, B)
    print(f"finite pairs={len(pairs)}")
    print(f"all-integer factor-pair bound={universal_bound}")
    assert len(pairs) <= universal_bound
    assert ledger.survives

    gram_minimum = min(
        float(np.linalg.eigvalsh(sampled_pair_block_gram(float(z)))[0])
        for z in np.linspace(0.0, 1.0, 101)
    )
    print(f"sampled normalized pair-Gram minimum={gram_minimum:.12f}")
    assert gram_minimum > 0.001

    order = 37
    angles = np.linspace(0.0, 2.0 * math.pi, 5001)
    dual = fejer_transverse_dual(order, angles)
    ceiling = 1.0 / (2.0 * (order - 1))
    print(f"Fejer F(0)={float(dual[0]):.12f}")
    print(f"Fejer sampled maximum={float(np.max(dual)):.12f}")
    print(f"Fejer exact ceiling={ceiling:.12f}")
    assert math.isclose(float(dual[0]), -0.5, abs_tol=1e-12)
    assert float(np.max(dual)) <= ceiling + 1e-12


if __name__ == "__main__":
    main()
