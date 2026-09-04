#!/usr/bin/env python3
"""Replay the singular-atomic packet and directional determinant ledger."""

from __future__ import annotations

import math
from collections import Counter

import numpy as np


KAPPA = 0.0180303234
BETA = 50.0 / 33.0
WIDTH = 0.2


def prime_powers(limit: int) -> list[int]:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    values: set[int] = set()
    for p in np.flatnonzero(sieve):
        value = int(p)
        while value <= limit:
            values.add(value)
            if value > limit // int(p):
                break
            value *= int(p)
    return sorted(values)


def actual_window(y: int) -> list[int]:
    lower = y * math.exp(-WIDTH)
    upper = y * math.exp(WIDTH)
    return [
        n
        for n in prime_powers(math.ceil(upper))
        if lower <= n <= upper
    ]


def multiplicative_energy(nodes: list[int]) -> tuple[int, int]:
    products = Counter(a * b for a in nodes for b in nodes)
    return sum(value * value for value in products.values()), max(products.values())


def directional_schur_check(y: int) -> tuple[int, float, float, float]:
    nodes = actual_window(y)
    u = np.log(np.asarray(nodes, dtype=float) / y)
    q0 = np.ones(len(nodes))
    lower = y**0.751
    centers = (1.1 * lower, 1.7 * lower)
    columns: list[np.ndarray] = []
    for center in centers:
        columns.append(np.cos(center * u))
        columns.append(-u * np.sin(center * u))
    matrix = np.column_stack(columns)
    gram = matrix.T @ matrix
    cross = matrix.T @ q0
    augmented = np.block(
        [[np.array([[q0 @ q0]]), cross[None, :]], [cross[:, None], gram]]
    )
    schur = float(q0 @ q0 - cross @ np.linalg.solve(gram, cross))
    basis, _ = np.linalg.qr(matrix, mode="reduced")
    direct = float(np.linalg.norm(q0 - basis @ (basis.T @ q0)) ** 2)
    sign_g, logdet_g = np.linalg.slogdet(gram)
    sign_a, logdet_a = np.linalg.slogdet(augmented)
    assert sign_g > 0 and sign_a > 0
    determinant_ratio = float(math.exp(logdet_a - logdet_g))
    return len(nodes), schur, direct, determinant_ratio


def main() -> None:
    second_moment_fraction_exponent = -1.0 + 2.0 * KAPPA
    fourth_moment_length_exponent = 4.0 * KAPPA
    fixed_packet_exponent = 2.0 * KAPPA
    shrinking_packet_exponent = 3.0 * KAPPA
    gm_middle_exponent = -2.0 / 5.0 + 4.0 * KAPPA
    gm_long_exponent = BETA - 8.0 / 5.0 + 4.0 * KAPPA
    hb_first_ratio_exponent = 2.0 * KAPPA - 1.0
    hb_third_ratio_exponent = KAPPA / 2.0 + BETA / 2.0 - 1.0
    harmonic_spacing_exponent = BETA - 1.0
    print(f"kappa={KAPPA:.10f}")
    print(
        "second_moment_exceptional_fraction_exponent="
        f"{second_moment_fraction_exponent:.12f}"
    )
    print(f"fourth_moment_length_exponent={fourth_moment_length_exponent:.12f}")
    print(f"fixed_packet_exponent={fixed_packet_exponent:.12f}")
    print(f"shrinking_packet_exponent={shrinking_packet_exponent:.12f}")
    print(f"guth_maynard_middle_term_exponent={gm_middle_exponent:.12f}")
    print(f"guth_maynard_long_term_exponent={gm_long_exponent:.12f}")
    print(f"heath_brown_first_ratio_exponent={hb_first_ratio_exponent:.12f}")
    print(f"heath_brown_third_ratio_exponent={hb_third_ratio_exponent:.12f}")
    print(f"harmonic_spacing_ceiling_exponent={harmonic_spacing_exponent:.12f}")
    assert fixed_packet_exponent < shrinking_packet_exponent < 1.0
    assert gm_middle_exponent < 0.0
    assert gm_long_exponent < 0.0
    assert hb_first_ratio_exponent < 0.0
    assert hb_third_ratio_exponent < 0.0
    print("actual_Y actual_M pair_energy energy_over_M2 max_r2")
    for y in (100, 300, 1000, 3000):
        actual = actual_window(y)
        energy, max_r2 = multiplicative_energy(actual)
        print(
            f"{y} {len(actual)} {energy} "
            f"{energy / len(actual) ** 2:.12g} {max_r2}"
        )
    print()
    print("schur_Y M schur direct determinant_ratio max_relative_error")
    for y in (300, 1000, 3000):
        size, schur, direct, determinant_ratio = directional_schur_check(y)
        scale = max(1.0, abs(schur), abs(direct), abs(determinant_ratio))
        error = max(abs(schur - direct), abs(schur - determinant_ratio)) / scale
        print(
            f"{y} {size} {schur:.12g} {direct:.12g} "
            f"{determinant_ratio:.12g} {error:.3e}"
        )
        assert error < 2e-9


if __name__ == "__main__":
    main()
