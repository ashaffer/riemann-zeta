"""Exact arithmetic checks for the central-packet cubic parity theorem.

The mathematical input is elementary but easy to obscure numerically.  If
``Y=N+1/2`` and ``n`` is an integer, then ``2*abs(n-Y)`` is odd.  A signed
sum of three such distances therefore has an odd, nonzero doubled numerator.
This module records that parity and the exponent ledger with ``Fraction``
arithmetic; it is not a numerical proof of any full-shell statement.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import math
from typing import Iterable


@dataclass(frozen=True)
class CentralPacketParityCertificate:
    N: int
    center: Fraction
    node_count: int
    maximum_distance: Fraction
    maximum_reflection_cluster_size: int
    odd_triple_numerator_lower: int
    interpolation_corner_leading_terms_consistent: bool
    taylor_error_per_frequency_upper: Fraction
    signed_cubic_log_frequency_lower: Fraction
    aperture_exponent: Fraction
    packet_dimension_exponent: Fraction
    spline_order: int
    cubic_dimension_loss_exponent: Fraction
    fourier_decay_gain_exponent: Fraction
    net_cubic_decay_exponent: Fraction


def doubled_half_integer_distances(N: int, nodes: Iterable[int]) -> tuple[int, ...]:
    """Return the exact odd integers ``2*abs(n-(N+1/2))``."""

    if N < 1:
        raise ValueError("N must be positive")
    center_twice = 2 * N + 1
    distances = tuple(abs(2 * int(node) - center_twice) for node in nodes)
    if not distances:
        raise ValueError("the node list must be nonempty")
    if any(value == 0 or value % 2 == 0 for value in distances):
        raise AssertionError("an integer-to-half-integer distance must be odd")
    return distances


def brute_force_minimum_signed_triple_numerator(
    doubled_distances: Iterable[int],
) -> int:
    """Enumerate the doubled numerator in every signed triple.

    This is intended for small audit sets.  Repetitions are included, exactly
    as they are in a cubic tensor entry.
    """

    values = tuple(int(value) for value in doubled_distances)
    if not values or any(value <= 0 or value % 2 == 0 for value in values):
        raise ValueError("doubled distances must be positive odd integers")
    minimum = math.inf
    for first, second, third in product(values, repeat=3):
        for signs in product((-1, 1), repeat=3):
            numerator = abs(
                signs[0] * first + signs[1] * second + signs[2] * third
            )
            if numerator == 0:
                raise AssertionError("three odd integers cannot have zero signed sum")
            minimum = min(minimum, numerator)
    return int(minimum)


def verify_reflection_box_leading_terms(N: int, nodes: Iterable[int]) -> int:
    """Verify every divided-difference corner has one common leading term.

    Nodes at the two endpoints of a reflected block have the same exact
    doubled distance from ``Y``.  This routine enumerates triples of blocks,
    including repetitions, every cosine sign pattern, and every endpoint
    corner.  It returns the smallest absolute doubled leading numerator.
    """

    node_tuple = tuple(int(node) for node in nodes)
    distances = doubled_half_integer_distances(N, node_tuple)
    blocks: dict[int, list[int]] = {}
    for node, distance in zip(node_tuple, distances, strict=True):
        blocks.setdefault(distance, []).append(node)
    if any(len(block) > 2 for block in blocks.values()):
        raise AssertionError("a reflection block cannot have three endpoints")
    center_twice = 2 * N + 1
    minimum = math.inf
    block_items = tuple(blocks.items())
    for first, second, third in product(block_items, repeat=3):
        selected = (first, second, third)
        block_distances = tuple(item[0] for item in selected)
        for signs in product((-1, 1), repeat=3):
            expected = sum(
                sign * distance
                for sign, distance in zip(signs, block_distances, strict=True)
            )
            if expected == 0:
                raise AssertionError("three odd block distances cannot sum to zero")
            corner_values: set[int] = set()
            for endpoints in product(*(item[1] for item in selected)):
                corner_values.add(
                    sum(
                        sign * abs(2 * endpoint - center_twice)
                        for sign, endpoint in zip(signs, endpoints, strict=True)
                    )
                )
            if corner_values != {expected}:
                raise AssertionError("a reflection box changed its leading term")
            minimum = min(minimum, abs(expected))
    return int(minimum)


def exact_exponent_ledger(
    *,
    aperture_exponent: Fraction = Fraction(50, 33),
    packet_epsilon: Fraction = Fraction(0),
    spline_order: int = 8,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return exact exponents in ``M^(3/2)(Y/B)^q``.

    The packet dimension is at most ``Y^(1/2-epsilon)``.  The returned tuple
    is ``(dimension, loss, Fourier gain, net gain)``; a positive net gain is
    precisely the power by which the standardized cubic bound decays.
    """

    aperture = Fraction(aperture_exponent)
    epsilon = Fraction(packet_epsilon)
    if aperture <= 1:
        raise ValueError("the aperture exponent must exceed one")
    if epsilon < 0 or epsilon >= Fraction(1, 2):
        raise ValueError("packet epsilon must lie in [0,1/2)")
    if spline_order < 1:
        raise ValueError("spline order must be positive")
    dimension = Fraction(1, 2) - epsilon
    cubic_loss = Fraction(3, 2) * dimension
    fourier_gain = spline_order * (aperture - 1)
    return dimension, cubic_loss, fourier_gain, fourier_gain - cubic_loss


def central_packet_parity_certificate(
    N: int,
    nodes: Iterable[int],
    *,
    aperture_exponent: Fraction = Fraction(50, 33),
    packet_epsilon: Fraction = Fraction(0),
    spline_order: int = 8,
) -> CentralPacketParityCertificate:
    """Build an exact parity, Taylor, cluster, and exponent certificate."""

    node_tuple = tuple(int(node) for node in nodes)
    distances = doubled_half_integer_distances(N, node_tuple)
    center = Fraction(2 * N + 1, 2)
    maximum_distance = Fraction(max(distances), 2)
    if maximum_distance >= center:
        raise ValueError("all nodes must be positive")

    # For x=h/Y, both |log(1+x)-x| and |-log(1-x)-x| are at most
    # x^2/[2(1-x)].  Three logarithms therefore lose at most three times
    # this exact rational majorant from the parity gap 1/(2Y).
    ratio = maximum_distance / center
    taylor_error = ratio * ratio / (2 * (1 - ratio))
    cubic_lower = Fraction(1, 2) / center - 3 * taylor_error

    counts = Counter(distances)
    maximum_cluster = max(counts.values())
    if maximum_cluster > 2:
        raise AssertionError("a half-integer center has at most two reflections")

    dimension, loss, gain, net = exact_exponent_ledger(
        aperture_exponent=aperture_exponent,
        packet_epsilon=packet_epsilon,
        spline_order=spline_order,
    )
    return CentralPacketParityCertificate(
        N=N,
        center=center,
        node_count=len(node_tuple),
        maximum_distance=maximum_distance,
        maximum_reflection_cluster_size=maximum_cluster,
        odd_triple_numerator_lower=1,
        interpolation_corner_leading_terms_consistent=True,
        taylor_error_per_frequency_upper=taylor_error,
        signed_cubic_log_frequency_lower=cubic_lower,
        aperture_exponent=Fraction(aperture_exponent),
        packet_dimension_exponent=dimension,
        spline_order=spline_order,
        cubic_dimension_loss_exponent=loss,
        fourier_decay_gain_exponent=gain,
        net_cubic_decay_exponent=net,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--N", type=int, default=1_000_000)
    parser.add_argument("--H", type=int, default=200)
    parser.add_argument("--spline-order", type=int, default=8)
    parser.add_argument("--epsilon-numerator", type=int, default=1)
    parser.add_argument("--epsilon-denominator", type=int, default=10)
    args = parser.parse_args()
    center = args.N + 0.5
    nodes = range(math.ceil(center - args.H), math.floor(center + args.H) + 1)
    certificate = central_packet_parity_certificate(
        args.N,
        nodes,
        packet_epsilon=Fraction(
            args.epsilon_numerator, args.epsilon_denominator
        ),
        spline_order=args.spline_order,
    )
    for name, value in certificate.__dict__.items():
        print(f"{name}={value}")


if __name__ == "__main__":
    main()
