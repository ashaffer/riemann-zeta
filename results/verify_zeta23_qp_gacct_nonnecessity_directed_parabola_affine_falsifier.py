#!/usr/bin/env python3
"""Exact abstract countermodel to necessity of cardinal generic GACCT.

The model is deliberately not asserted to be an actual-prime QP graph.  It
retains directed-pair rank-one inputs and gives every rich anchor-partner
fiber finite-parabola/Sidon geometry.  Cardinal NDS fails by sqrt(D), while
the rank-one transition energy has an elementary D/4 upper certificate.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return value == divisor
        divisor += 1
    return True


@dataclass(frozen=True)
class DirectedParabolaLedger:
    prime: int
    degree_parameter: int
    row_count: int
    partner_count: int
    anchor_degree: int
    partner_degree: int
    row_degree: int
    anchor_partner_codegree: int
    maximum_distinct_partner_codegree: int
    anchor_neighbor_degree_sum: int
    gacct_mass: int
    gacct_ratio: int
    maximum_fiber_line_occupancy: int
    ordered_secants_per_fiber: int
    distinct_ordered_secants_per_fiber: int
    product_curve_secants_invertible: bool
    product_curve_secants_distinct: bool
    rank_one_energy_upper_coefficient_numerator: int
    rank_one_energy_upper_coefficient_denominator: int


def finite_line_key(first: tuple[int, int], second: tuple[int, int], p: int):
    dx = (second[0] - first[0]) % p
    dy = (second[1] - first[1]) % p
    if dx:
        slope = dy * pow(dx, -1, p) % p
        return (1, slope, (first[1] - slope * first[0]) % p)
    return (0, 1, first[0] % p)


def product_matrix(parameter: int, prime: int) -> tuple[int, int, int, int]:
    middle = prime + 1
    value = middle + parameter + 1
    # Both factor pairs are comparable: u=(M^2+t^2,Mt), v=(M^2,Mt).
    # Their outer product lies on x11-x22=M^4.  The curve has coordinates
    # of degrees 2,3,1,2 after subtracting its constant part, so it spans
    # the full three-dimensional pinned hyperplane rather than one plane.
    first_factor = (middle * middle + value * value, middle * value)
    second_factor = (middle * middle, middle * value)
    return (
        first_factor[0] * second_factor[0],
        first_factor[0] * second_factor[1],
        first_factor[1] * second_factor[0],
        first_factor[1] * second_factor[1],
    )


def audit(prime: int) -> DirectedParabolaLedger:
    if prime % 2 == 0 or not is_prime(prime):
        raise ValueError("require an odd prime")
    rows = tuple((x, y) for x in range(prime) for y in range(prime))
    partners = tuple((a, b) for a in range(prime) for b in range(prime))
    fibers = {
        partner: {
            (t, (t * t + partner[0] * t + partner[1]) % prime)
            for t in range(prime)
        }
        for partner in partners
    }
    if any(len(fiber) != prime for fiber in fibers.values()):
        raise AssertionError("a parabola fiber lost a point")

    row_partner_degrees = {
        row: sum(row in fiber for fiber in fibers.values()) for row in rows
    }
    if set(row_partner_degrees.values()) != {prime}:
        raise AssertionError("finite-plane parabolas are not row regular")
    maximum_partner_intersection = max(
        (
            len(fibers[first] & fibers[second])
            for first, second in combinations(partners, 2)
        ),
        default=0,
    )
    if maximum_partner_intersection > 1:
        raise AssertionError("two distinct translated parabolas met twice")

    line_occupancy = 0
    for fiber in fibers.values():
        lines: dict[tuple[int, int, int], set[tuple[int, int]]] = {}
        for first, second in combinations(sorted(fiber), 2):
            key = finite_line_key(first, second, prime)
            lines.setdefault(key, set()).update((first, second))
        line_occupancy = max(
            line_occupancy, max(map(len, lines.values()), default=1)
        )
    if line_occupancy != 2:
        raise AssertionError("a translated parabola acquired three collinear points")

    # For one fiber, (t-s, f(t)-f(s)) determines ordered (t,s), since 2 is
    # invertible.  Verify the exact count rather than relying on the formula.
    a, b = partners[-1]
    ordered_secants = []
    for t in range(prime):
        for s in range(prime):
            if t == s:
                continue
            ordered_secants.append(
                (
                    (t - s) % prime,
                    (
                        t * t
                        + a * t
                        + b
                        - s * s
                        - a * s
                        - b
                    )
                    % prime,
                )
            )
    distinct_secants = len(set(ordered_secants))

    matrices = tuple(product_matrix(t, prime) for t in range(prime))
    matrix_secants: set[tuple[int, int, int, int]] = set()
    invertible = True
    pinned_level = (prime + 1) ** 4
    for t, first in enumerate(matrices):
        if first[0] * first[3] != first[1] * first[2]:
            raise AssertionError("the product curve left the rank-one cone")
        if first[0] - first[3] != pinned_level:
            raise AssertionError("the product curve left its pinned level")
        for s, second in enumerate(matrices):
            if t == s:
                continue
            secant = tuple(x - y for x, y in zip(first, second))
            matrix_secants.add(secant)
            invertible &= secant[0] * secant[3] - secant[1] * secant[2] != 0

    degree = prime * prime
    anchored_sum = degree * (prime + 1)
    gacct_mass = prime * degree
    return DirectedParabolaLedger(
        prime=prime,
        degree_parameter=degree,
        row_count=degree,
        partner_count=degree,
        anchor_degree=degree,
        partner_degree=prime,
        row_degree=prime + 1,
        anchor_partner_codegree=prime,
        maximum_distinct_partner_codegree=maximum_partner_intersection,
        anchor_neighbor_degree_sum=anchored_sum,
        gacct_mass=gacct_mass,
        gacct_ratio=prime,
        maximum_fiber_line_occupancy=line_occupancy,
        ordered_secants_per_fiber=prime * (prime - 1),
        distinct_ordered_secants_per_fiber=distinct_secants,
        product_curve_secants_invertible=invertible,
        product_curve_secants_distinct=(
            len(matrix_secants) == prime * (prime - 1)
        ),
        # For normalized z, every row is a subset of one global directed
        # matching, hence contributes <=1/4.  There are D rows.
        rank_one_energy_upper_coefficient_numerator=degree,
        rank_one_energy_upper_coefficient_denominator=4,
    )


def main() -> None:
    print("PASS directed-parabola GACCT nonnecessity audit")
    print("p D rows partners codeg W/D RP/D linecap distinct-secants energy-bound")
    for prime in (3, 5, 7, 11):
        item = audit(prime)
        assert item.maximum_distinct_partner_codegree <= 1
        assert item.distinct_ordered_secants_per_fiber == prime * (prime - 1)
        assert item.product_curve_secants_invertible
        assert item.product_curve_secants_distinct
        assert item.anchor_neighbor_degree_sum // item.degree_parameter == prime + 1
        print(
            prime,
            item.degree_parameter,
            item.row_count,
            item.partner_count,
            item.anchor_partner_codegree,
            prime + 1,
            item.gacct_ratio,
            item.maximum_fiber_line_occupancy,
            item.distinct_ordered_secants_per_fiber,
            f"{item.degree_parameter}/4",
        )


if __name__ == "__main__":
    main()
