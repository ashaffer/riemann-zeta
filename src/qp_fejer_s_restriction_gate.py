"""Exact ledgers for the Fejer-weighted completion-sum restriction gate.

The module contains only finite identities and exponent arithmetic.  It does
not assert the open reciprocal-strip restriction theorem recorded in the
companion report.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import pi, sin
from typing import Iterable, Mapping, Sequence


ComplexSequence = Mapping[int, complex]


def normalized_fejer_value(order: int, theta: float, scale: float = 1.0) -> float:
    """Return ``scale/order**2 * |sum_{0<=r<order} e(r theta)|**2``.

    The value at an integer is evaluated by continuity.
    """

    if order <= 0:
        raise ValueError("order must be positive")
    distance = theta - round(theta)
    if abs(distance) < 1.0e-15:
        return float(scale)
    quotient = sin(pi * order * distance) / sin(pi * distance)
    return float(scale) * (quotient / order) ** 2


def fejer_riesz_coefficients(order: int, scale: float = 1.0) -> tuple[complex, ...]:
    """Return constant coefficients whose squared polynomial is Fejer."""

    if order <= 0:
        raise ValueError("order must be positive")
    coefficient = float(scale) ** 0.5 / order
    return tuple(complex(coefficient) for _ in range(order))


def rank_one_overlap(
    order: int, theta_one: float, theta_two: float, scale: float = 1.0
) -> complex:
    """Return the inner product of the Fejer tensor with a sampling vector."""

    alpha = fejer_riesz_coefficients(order, scale)
    first = sum(alpha[r] * complex_exp(r * theta_one) for r in range(order))
    second = sum(alpha[s] * complex_exp(s * theta_two) for s in range(order))
    return first * second


def complex_exp(theta: float) -> complex:
    """Return ``exp(2*pi*i*theta)`` without importing a numerical package."""

    from cmath import exp

    return exp(2j * pi * theta)


def convolution(left: ComplexSequence, right: ComplexSequence) -> dict[int, complex]:
    """Return the ordinary, noncyclic additive convolution."""

    answer: defaultdict[int, complex] = defaultdict(complex)
    for first, first_value in left.items():
        for second, second_value in right.items():
            answer[first + second] += first_value * second_value
    return dict(answer)


def norm_squared(values: Mapping[int, complex] | Iterable[complex]) -> float:
    """Return the squared ell-two norm."""

    iterable = values.values() if isinstance(values, Mapping) else values
    return float(sum(abs(value) ** 2 for value in iterable))


def convolution_energy(left: ComplexSequence, right: ComplexSequence) -> float:
    """Return ``||left * right||_2^2``."""

    return norm_squared(convolution(left, right))


def interval_self_energy(length: int, normalized: bool = False) -> Fraction:
    """Exact additive energy of an interval, optionally ell-two normalized."""

    if length <= 0:
        raise ValueError("length must be positive")
    raw = Fraction(2 * length**3 + length, 3)
    if normalized:
        return raw / length**2
    return raw


def packet_pair_overlap(
    left_packets: Sequence[Sequence[int]], right_packets: Sequence[Sequence[int]]
) -> int:
    """Maximum number of packet-pair sumsets covering one integer."""

    multiplicity: defaultdict[int, int] = defaultdict(int)
    for left in left_packets:
        left_set = set(left)
        for right in right_packets:
            sums = {first + second for first in left_set for second in set(right)}
            for total in sums:
                multiplicity[total] += 1
    return max(multiplicity.values(), default=0)


def packet_square_function_upper_bound(
    left_packets: Sequence[ComplexSequence], right_packets: Sequence[ComplexSequence]
) -> float:
    """Return the rigorous bounded-overlap packet-pair upper bound.

    If ``K`` is the maximum number of packet-pair sumsets through one output
    and ``L`` the largest smaller packet cardinality, pointwise Cauchy and
    Young give

        ||sum_{i,j} z_i * y_j||_2^2
        <= K L (sum_i ||z_i||_2^2)(sum_j ||y_j||_2^2).
    """

    left_supports = [tuple(packet) for packet in left_packets]
    right_supports = [tuple(packet) for packet in right_packets]
    overlap = packet_pair_overlap(left_supports, right_supports)
    smaller_capacity = max(
        (
            min(len(left), len(right))
            for left in left_supports
            for right in right_supports
        ),
        default=0,
    )
    left_mass = sum(norm_squared(packet) for packet in left_packets)
    right_mass = sum(norm_squared(packet) for packet in right_packets)
    return float(overlap * smaller_capacity) * left_mass * right_mass


@dataclass(frozen=True)
class RestrictionExponentLedger:
    q: Fraction
    reciprocal_bandwidth: Fraction
    pointwise_balanced_core: Fraction
    energy_balanced_core: Fraction
    energy_unbalanced_core: Fraction
    fejer_convolution_norm: Fraction
    fejer_energy: Fraction
    exceptional_sum_count: Fraction


def critical_restriction_exponents() -> RestrictionExponentLedger:
    """Return the exact powers of ``D`` in the restriction reduction."""

    return RestrictionExponentLedger(
        q=Fraction(33, 16),
        reciprocal_bandwidth=Fraction(17, 16),
        pointwise_balanced_core=Fraction(1, 6),
        energy_balanced_core=Fraction(1, 10),
        energy_unbalanced_core=Fraction(1, 6),
        fejer_convolution_norm=Fraction(5, 4),
        fejer_energy=Fraction(5, 2),
        exceptional_sum_count=Fraction(7, 4),
    )


def young_mask_energy_exponent(u: Fraction, v: Fraction) -> Fraction:
    """Power in ``D^3 m^2 M`` for ``m=D^u, M=D^v`` and ``u<=v``."""

    if u < 0 or v < u:
        raise ValueError("require 0 <= u <= v")
    return Fraction(3) + 2 * u + v


def weighted_young_mask_exponent(u: Fraction, v: Fraction) -> Fraction:
    """Power after the squared Fejer weight ``m^-4 M^-4``."""

    return young_mask_energy_exponent(u, v) - 4 * u - 4 * v


def restriction_fejer_term_exponents(
    u: Fraction, v: Fraction
) -> tuple[Fraction, Fraction, Fraction]:
    """Powers in one dyadic term under the conjectural mixed restriction.

    Returns the powers of the convolution norm before the Fejer weight, the
    Fejer weight, and their sum.  Here ``m=D^u``, ``M=D^v``, ``u<=v``.
    """

    if u < 0 or v < u:
        raise ValueError("require 0 <= u <= v")
    convolution_norm = Fraction(5, 4) + Fraction(3, 4) * u + Fraction(1, 2) * v
    fejer_weight = -2 * u - 2 * v
    return convolution_norm, fejer_weight, convolution_norm + fejer_weight
