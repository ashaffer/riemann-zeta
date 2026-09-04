"""Finite replay for the actual-log perturbative Fejer rigidity gate.

The analytic integer-gap argument is in the accompanying theorem card.
This module checks the finite coloring fact, the normalized Fejer weights,
and the exact aperture exponent ledger.  It does not compute or certify a
transverse upper bound.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


PROJECT_APERTURE = Fraction(50, 33)


def monochromatic_three_ap(colors: tuple[int, ...]) -> tuple[int, int, int] | None:
    """Return a nonconstant monochromatic three-term AP, if one exists."""

    length = len(colors)
    for left in range(length):
        for step in range(1, (length - left + 1) // 2):
            middle = left + step
            right = left + 2 * step
            if right < length and colors[left] == colors[middle] == colors[right]:
                return left, middle, right
    return None


def all_two_colorings_have_three_ap(length: int) -> bool:
    """Exhaust the ``2^length`` colorings (used only at length nine)."""

    if length < 0:
        raise ValueError("length must be nonnegative")
    return all(
        monochromatic_three_ap(tuple(colors)) is not None
        for colors in product((0, 1), repeat=length)
    )


def fejer_weights(length: int) -> tuple[Fraction, ...]:
    """Normalized nonzero triangular weights from ``F_(length+1)``."""

    if length < 1:
        raise ValueError("length must be positive")
    return tuple(
        Fraction(2 * (length + 1 - index), length * (length + 1))
        for index in range(1, length + 1)
    )


def perturbative_support_exponent(aperture: Fraction) -> Fraction:
    """Exponent in ``L <= Y^(2-A)`` for aperture exponent ``A``."""

    if aperture <= 0:
        raise ValueError("aperture must be positive")
    return Fraction(2) - aperture


def project_ledger() -> dict[str, str]:
    exponent = perturbative_support_exponent(PROJECT_APERTURE)
    return {
        "aperture_exponent": str(PROJECT_APERTURE),
        "maximum_perturbative_support_exponent": str(exponent),
        "minimum_fejer_floor_exponent": str(exponent),
        "scope": "Lipschitz-stable harmonic transfer only",
    }
