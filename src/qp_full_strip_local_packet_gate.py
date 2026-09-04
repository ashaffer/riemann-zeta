"""Exact identities for the local full-reciprocal-strip packet gate.

The companion report proves a local collinearity theorem for integer points
``(a, v)`` in one product strip ``|a*v-C| <= D``.  This module keeps the
rational determinant identities, packet cardinality bound, and critical
exponent ledger executable.  It does *not* claim the open global projected
energy estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


@dataclass(frozen=True)
class FullStripLocalLedger:
    q_in_degree: Fraction
    local_arc: Fraction
    local_rounding_error: Fraction
    packet_cardinality: Fraction
    three_ap_lower_edge: Fraction
    three_ap_upper_edge: Fraction
    four_ap_lower_edge: Fraction
    four_ap_upper_edge: Fraction
    macroscopic_ap_step: Fraction
    macroscopic_to_four_ap_lower_margin: Fraction
    four_ap_upper_to_macroscopic_margin: Fraction
    behrend_spacing_over_local_arc: Fraction
    macroscopic_ap_hs_smooth_term: Fraction
    macroscopic_ap_hs_tolerance_term: Fraction
    macroscopic_ap_hs_major_term: Fraction
    macroscopic_ap_to_energy_core_margin: Fraction


def full_strip_local_ledger() -> FullStripLocalLedger:
    """Return powers of ``D`` at ``q=D^(33/16)``."""

    q = Fraction(33, 16)
    local_arc = q / 3
    macroscopic_step = q - 1
    four_ap_lower = (1 + q) / 3
    four_ap_upper = 2 * q / 3
    return FullStripLocalLedger(
        q_in_degree=q,
        local_arc=local_arc,
        # The perturbation in a three-point determinant is L*D/q.
        local_rounding_error=local_arc + 1 - q,
        packet_cardinality=Fraction(1, 2),
        three_ap_lower_edge=Fraction(1, 2),
        three_ap_upper_edge=q / 2,
        four_ap_lower_edge=four_ap_lower,
        four_ap_upper_edge=four_ap_upper,
        macroscopic_ap_step=macroscopic_step,
        macroscopic_to_four_ap_lower_margin=macroscopic_step - four_ap_lower,
        four_ap_upper_to_macroscopic_margin=four_ap_upper - macroscopic_step,
        behrend_spacing_over_local_arc=macroscopic_step - local_arc,
        # Huxley--Sargos with k=4 on f(k)=C/(a_0+R*k), at
        # M=D and R=q/D.  See Section 5 of the companion report.
        macroscopic_ap_hs_smooth_term=Fraction(129, 160),
        macroscopic_ap_hs_tolerance_term=Fraction(79, 96),
        macroscopic_ap_hs_major_term=Fraction(7, 32),
        macroscopic_ap_to_energy_core_margin=Fraction(5, 6)
        - Fraction(79, 96),
    )


def reciprocal_three_point_determinant(
    carrier_constant: Fraction,
    completions: tuple[int, int, int],
) -> Fraction:
    """Return ``det((1,a,C/a))`` in direct and factored form.

    The completions must be strictly increasing and positive.  The exact
    factorization is the second divided-difference identity for ``C/a``.
    """

    a1, a2, a3 = completions
    if not 0 < a1 < a2 < a3:
        raise ValueError("completions must be positive and strictly increasing")
    direct = (
        a2 * carrier_constant / a3
        - a3 * carrier_constant / a2
        - a1 * carrier_constant / a3
        + a3 * carrier_constant / a1
        + a1 * carrier_constant / a2
        - a2 * carrier_constant / a1
    )
    # Expanding a 3 x 3 determinant directly is less transparent than its
    # Vandermonde/divided-difference factorization.
    factored = (
        carrier_constant
        * (a2 - a1)
        * (a3 - a1)
        * (a3 - a2)
        / (a1 * a2 * a3)
    )
    if direct != factored:
        raise AssertionError("reciprocal three-point determinant identity failed")
    return direct


def integer_three_point_determinant(
    points: tuple[tuple[int, int], tuple[int, int], tuple[int, int]],
) -> int:
    """Return ``det((1,a,v))`` for three integer points."""

    ordered = sorted(points)
    (a1, v1), (a2, v2), (a3, v3) = ordered
    if not 0 < a1 < a2 < a3:
        raise ValueError("completion coordinates must be positive and distinct")
    return a2 * v3 - a3 * v2 - a1 * v3 + a3 * v1 + a1 * v2 - a2 * v1


def local_determinant_upper_bound(
    carrier_constant: Fraction,
    product_radius: Fraction,
    completions: tuple[int, int, int],
) -> Fraction:
    """Bound the integer determinant for points in one product strip.

    If ``|a_i*v_i-C| <= D``, then ``v_i=C/a_i+theta_i`` with
    ``|theta_i| <= D/a_min``.  The curve determinant contributes the exact
    divided difference, and the perturbation contributes at most
    ``2*(a_max-a_min)*D/a_min``.
    """

    a1, a2, a3 = completions
    curve = abs(reciprocal_three_point_determinant(carrier_constant, completions))
    perturbation = 2 * (a3 - a1) * product_radius / a1
    return curve + perturbation


def local_strip_forces_collinearity(
    carrier_constant: Fraction,
    product_radius: Fraction,
    points: tuple[tuple[int, int], tuple[int, int], tuple[int, int]],
) -> bool:
    """Certify collinearity when the rigorous determinant bound is below one."""

    ordered = tuple(sorted(points))
    completions = tuple(a for a, _ in ordered)
    for a, v in ordered:
        if abs(Fraction(a * v) - carrier_constant) > product_radius:
            raise ValueError("a point lies outside the supplied product strip")
    bound = local_determinant_upper_bound(
        carrier_constant, product_radius, completions  # type: ignore[arg-type]
    )
    if bound >= 1:
        return False
    determinant = integer_three_point_determinant(ordered)  # type: ignore[arg-type]
    if determinant != 0:
        raise AssertionError("an integral determinant of absolute value < 1 survived")
    return True


def reciprocal_third_difference(
    carrier_constant: Fraction,
    first_completion: int,
    completion_step: int,
) -> Fraction:
    """Return the exact third forward difference of ``C/a``."""

    a = first_completion
    r = completion_step
    coordinates = (a, a + r, a + 2 * r, a + 3 * r)
    if min(coordinates) <= 0 or r == 0:
        raise ValueError("the four completions must be positive and distinct")
    direct = (
        carrier_constant / (a + 3 * r)
        - 3 * carrier_constant / (a + 2 * r)
        + 3 * carrier_constant / (a + r)
        - carrier_constant / a
    )
    factored = (
        -6
        * carrier_constant
        * r**3
        / (a * (a + r) * (a + 2 * r) * (a + 3 * r))
    )
    if direct != factored:
        raise AssertionError("reciprocal third-difference identity failed")
    return direct


def line_product_value(
    first_point: tuple[int, int],
    primitive_direction: tuple[int, int],
    parameter: int,
) -> int:
    """Evaluate the product along direction ``(Q,-P)``."""

    a0, v0 = first_point
    horizontal_step, downward_step = primitive_direction
    if horizontal_step <= 0 or downward_step < 0:
        raise ValueError("expected a direction (Q,-P) with Q>0 and P>=0")
    return (a0 + horizontal_step * parameter) * (
        v0 - downward_step * parameter
    )


def line_product_second_difference(
    primitive_direction: tuple[int, int],
) -> int:
    """Return the constant second difference of the product on a line."""

    horizontal_step, downward_step = primitive_direction
    if horizontal_step <= 0 or downward_step < 0:
        raise ValueError("expected a direction (Q,-P) with Q>0 and P>=0")
    return -2 * horizontal_step * downward_step


def _ceil_sqrt_fraction(value: Fraction) -> int:
    if value < 0:
        raise ValueError("cannot take a real square root of a negative number")
    quotient = value.numerator // value.denominator
    root = isqrt(quotient)
    while root * root * value.denominator < value.numerator:
        root += 1
    return root


def line_packet_cardinality_bound(
    product_radius: Fraction,
    horizontal_step: int,
    downward_step: int,
) -> int:
    """A safe integer bound for a nonhorizontal affine packet.

    Along a primitive line of direction ``(Q,-P)``, the product is a
    quadratic with leading coefficient ``-P*Q``.  The preimage of an interval
    of width ``2D`` is the union of at most two intervals of total length at
    most ``2*sqrt(2D/(PQ))``.  Adding one endpoint allowance per component
    gives the returned bound.
    """

    if product_radius < 0 or horizontal_step <= 0 or downward_step <= 0:
        raise ValueError("the radius, Q, and P must be positive")
    scale = Fraction(2) * product_radius / (horizontal_step * downward_step)
    return 2 + 2 * _ceil_sqrt_fraction(scale)


def interval_additive_energy(length: int) -> int:
    """Return the ordered additive energy of ``{1,...,length}``."""

    if length < 1:
        raise ValueError("length must be positive")
    return (2 * length**3 + length) // 3
