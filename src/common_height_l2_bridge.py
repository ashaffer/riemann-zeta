#!/usr/bin/env python3
"""Exact exponent and finite identities for the common-height L2-to-CH4 bridge."""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Sequence


KAPPA = Fraction(1_974_048_259, 100_000_000_000)
H_MIN_EXPONENT = Fraction(8, 33)
LONG_EDGE_EXPONENT = Fraction(797, 5000)


def ch4_exponent_from_l2(
    l2_exponent: Fraction, h_min_exponent: Fraction = H_MIN_EXPONENT
) -> Fraction:
    """Exponent obtained from |B_I| <= C H_I and a global L2 exponent."""

    return l2_exponent - h_min_exponent


def delta_frontier_from_l2(
    l2_exponent: Fraction = Fraction(1),
    h_min_exponent: Fraction = H_MIN_EXPONENT,
    kappa: Fraction = KAPPA,
) -> Fraction:
    """Largest CH4 delta delivered by the deterministic interpolation step."""

    return (Fraction(1) - l2_exponent + h_min_exponent) / 4 - kappa


def maximum_closing_l2_exponent(
    h_min_exponent: Fraction = H_MIN_EXPONENT, kappa: Fraction = KAPPA
) -> Fraction:
    """Strict upper frontier for an L2 exponent that still yields some CH4 delta."""

    return Fraction(1) + h_min_exponent - 4 * kappa


def diagonal_l2_exponent(
    long_edge_exponent: Fraction = LONG_EDGE_EXPONENT,
) -> Fraction:
    """Exponent from max atom Y^theta times total mass O(Y)."""

    return Fraction(1) + long_edge_exponent


def weighted_l4(
    block_values: Sequence[complex], block_lengths: Sequence[float]
) -> float:
    if len(block_values) != len(block_lengths):
        raise ValueError("length mismatch")
    return sum(abs(value) ** 4 / length**3 for value, length in zip(block_values, block_lengths))


def l2_bridge_upper(
    block_values: Sequence[complex], block_lengths: Sequence[float], tv_constant: float
) -> float:
    """C^2/H_min times the selected physical block L2 energy."""

    if len(block_values) != len(block_lengths):
        raise ValueError("length mismatch")
    if not block_lengths:
        return 0.0
    if min(block_lengths) <= 0 or tv_constant < 0:
        raise ValueError("invalid bridge parameters")
    for value, length in zip(block_values, block_lengths):
        if abs(value) > tv_constant * length + 1e-12:
            raise ValueError("block value exceeds the asserted TV bound")
    return tv_constant**2 * sum(abs(value) ** 2 for value in block_values) / min(block_lengths)


def block_covariance_identity(blocks: Iterable[Sequence[complex]]) -> tuple[complex, complex]:
    """Return sum_I |sum_n c_In|^2 and its exact within-block pair expansion."""

    direct = 0j
    expanded = 0j
    for block in blocks:
        total = sum(block, 0j)
        direct += total * total.conjugate()
        expanded += sum(x * y.conjugate() for x in block for y in block)
    return direct, expanded


def audit() -> dict[str, str | bool]:
    delta = delta_frontier_from_l2()
    diagonal_delta = delta_frontier_from_l2(diagonal_l2_exponent())
    obtained = ch4_exponent_from_l2(Fraction(1))
    required_at_zero = Fraction(1) - 4 * KAPPA
    return {
        "kappa": str(KAPPA),
        "minimum_block_exponent": str(H_MIN_EXPONENT),
        "obtained_ch4_exponent": str(obtained),
        "required_delta_zero_exponent": str(required_at_zero),
        "exponent_margin": str(required_at_zero - obtained),
        "delta_frontier": str(delta),
        "maximum_closing_l2_exponent": str(maximum_closing_l2_exponent()),
        "diagonal_l2_exponent": str(diagonal_l2_exponent()),
        "diagonal_exponent_margin": str(
            maximum_closing_l2_exponent() - diagonal_l2_exponent()
        ),
        "diagonal_delta_frontier": str(diagonal_delta),
        "strictly_positive": delta > 0,
        "diagonal_closes": diagonal_delta > 0,
    }


if __name__ == "__main__":
    print(audit())
