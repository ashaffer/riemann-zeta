"""Exact exponent LP for the QP Guth--Maynard L3 audit."""

from __future__ import annotations

from fractions import Fraction


A = Fraction(50, 33)
H = 2 - A


def exponent_branches(m: Fraction, v: Fraction) -> dict[str, Fraction]:
    """Return the normalized large-value exponent branches."""

    if m < 0 or v < 0 or v > m / 2:
        raise ValueError("require m>=0 and 0<=v<=m/2")
    l2 = -2 * v
    common = H - m - 2 * v
    classical = min(1 - m - 2 * v, 4 - 3 * m - 6 * v)
    gm = Fraction(12, 5) - 2 * m - 4 * v
    return {"l2": l2, "common": common, "classical": classical, "gm": gm}


def count_exponent(m: Fraction, v: Fraction) -> Fraction:
    """Best ``R/T`` exponent, retaining the sum in each theorem."""

    e = exponent_branches(m, v)
    return min(
        e["l2"],
        max(e["common"], e["classical"]),
        max(e["common"], e["gm"]),
    )


def third_layer_exponent(m: Fraction, v: Fraction) -> Fraction:
    """Exponent of the dyadic third-moment layer ``V^3 R/T``."""

    return 3 * v + count_exponent(m, v)


def target_exponent() -> Fraction:
    return H / 4
