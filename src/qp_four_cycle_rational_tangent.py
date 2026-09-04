"""Finite replay helpers for rational-slope tangent patches.

The companion theorem observes that a product restricted to a primitive
line of direction ``(r,-s)`` is a concave quadratic with curvature ``rs``.
These routines expose the exact integer envelope used in that proof.
"""

from __future__ import annotations

from fractions import Fraction
import math


def _ceil_sqrt_fraction(value: Fraction) -> int:
    if value < 0:
        raise ValueError("the square-root argument must be nonnegative")
    quotient = value.numerator // value.denominator
    root = math.isqrt(quotient)
    if root * root * value.denominator == value.numerator:
        return root
    return root + 1


def tangent_component_point_bound(
    product_half_width: int,
    row_step: int,
    column_step: int,
) -> int:
    """Integer points in one connected product-band component.

    A real component has length at most
    ``2*sqrt(2*product_half_width/(row_step*column_step))``.  An interval of
    length ``L`` contains at most ``ceil(L)+1`` integers.
    """

    if product_half_width < 0 or row_step <= 0 or column_step <= 0:
        raise ValueError("invalid product band or direction")
    length_square = Fraction(
        2 * product_half_width,
        row_step * column_step,
    )
    return 2 * _ceil_sqrt_fraction(length_square) + 1


def tangent_patch_fourth_trace_coefficient(
    product_half_width: int,
    row_step: int,
    column_step: int,
    color_diagonal_multiplicity: int = 1,
) -> int:
    """Coefficient in the Frobenius fourth-trace majorant.

    If each color labels at most ``mu`` anti-diagonals, then

    ``tr((H H*)^2) <= (mu*L)^2 ||z||_2^4``.
    """

    if color_diagonal_multiplicity <= 0:
        raise ValueError("the color multiplicity must be positive")
    points = tangent_component_point_bound(
        product_half_width,
        row_step,
        column_step,
    )
    return (color_diagonal_multiplicity * points) ** 2


def product_on_tangent_line(
    a0: int,
    b0: int,
    row_step: int,
    column_step: int,
    parameter: int,
) -> int:
    """Return ``(a0+r*t)(b0-s*t)`` exactly."""

    return (a0 + row_step * parameter) * (
        b0 - column_step * parameter
    )


def integer_band_components(
    *,
    a0: int,
    b0: int,
    row_step: int,
    column_step: int,
    product_center: int,
    product_half_width: int,
    first_parameter: int,
    last_parameter: int,
) -> tuple[tuple[int, ...], ...]:
    """Brute-force integer components for finite theorem diagnostics."""

    if first_parameter > last_parameter:
        raise ValueError("empty parameter range")
    accepted = [
        parameter
        for parameter in range(first_parameter, last_parameter + 1)
        if abs(
            product_on_tangent_line(
                a0,
                b0,
                row_step,
                column_step,
                parameter,
            )
            - product_center
        )
        <= product_half_width
    ]
    components: list[list[int]] = []
    for parameter in accepted:
        if not components or parameter != components[-1][-1] + 1:
            components.append([parameter])
        else:
            components[-1].append(parameter)
    return tuple(tuple(component) for component in components)
