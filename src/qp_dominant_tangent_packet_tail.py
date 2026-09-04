"""Exact arithmetic checks for the dominant tangent-packet tail theorem."""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def quadratic_second_difference(base: int, step: int, t: int) -> int:
    """Second difference of (a+t*A*r)(b+t*B*s) in symmetric form.

    ``base`` is irrelevant algebraically; it is retained to make the helper
    mirror a translated product-window packet.  ``step`` is the product of
    the two projected primitive steps.
    """

    f_minus = base - step * t + step * t * t
    f_zero = base
    f_plus = base + step * t + step * t * t
    return f_minus - 2 * f_zero + f_plus


def dominant_height_cap(D: Fraction, K: Fraction, J: Fraction) -> Fraction:
    """The cap h <= D J^2/K^2 after dropping harmless constants."""

    if D <= 0 or K <= 0 or J <= 0:
        raise ValueError("D, K, and J must be positive")
    return D * J * J / (K * K)


def gap_mass_at_cap(D: Fraction, height_cap: Fraction) -> Fraction:
    """sqrt(D*h_cap), returned exactly when the product is a square."""

    product = D * height_cap
    num_root = int(product.numerator**0.5)
    den_root = int(product.denominator**0.5)
    if num_root * num_root != product.numerator:
        raise ValueError("numerator is not a square")
    if den_root * den_root != product.denominator:
        raise ValueError("denominator is not a square")
    return Fraction(num_root, den_root)


def dominant_tail_bound(D: Fraction, K: Fraction, J: Fraction) -> Fraction:
    """The exact scale J*D/K in the dominant-packet theorem."""

    return J * D / K


def direct_dyadic_bound(
    K: Fraction, color_mass_bound: Fraction
) -> Fraction:
    """Use m(C)<2K on one multiplicity bin."""

    return 2 * K * color_mass_bound


def defects(colors: tuple[int, int, int, int], b: tuple[int, int]) -> tuple[int, int]:
    """Return the two row-sharing cross-product defects."""

    x, y, u, v = colors
    b1, b2 = b
    return x * b1 - y * b2, u * b1 - v * b2


def column_wedge(s: tuple[int, int], b: tuple[int, int]) -> int:
    """det(s,b) in the sign convention of the report."""

    s1, s2 = s
    b1, b2 = b
    return s1 * b2 - s2 * b1


def defect_intercept(
    r: tuple[int, int], defect_pair: tuple[int, int]
) -> int:
    """The left side r1*delta1-r2*delta2 of (5.5)."""

    r1, r2 = r
    delta1, delta2 = defect_pair
    return r1 * delta1 - r2 * delta2


def reconstruct_carriers(
    x: int,
    y: int,
    s: tuple[int, int],
    beta: int,
    delta: int,
) -> tuple[Fraction, Fraction]:
    """Invert the exact (beta, delta) transform in (5.9)."""

    s1, s2 = s
    d = s1 * x - s2 * y
    if d == 0:
        raise ValueError("the top gap d must be nonzero")
    return Fraction(y * beta + s1 * delta, d), Fraction(
        x * beta + s2 * delta, d
    )


def secant_solution_step(x: int, y: int) -> tuple[int, int]:
    """Primitive difference of two solutions to x*b1-y*b2=delta."""

    common = gcd(abs(x), abs(y))
    return y // common, x // common
