"""Exact arithmetic for error-labelled pair cells in one QP shell.

The module deliberately separates two assertions which are easy to conflate:

* after fixing the completion sum, error sum, *and carrier sum*, a pair cell
  has divisor-scale multiplicity;
* after forgetting the carrier sum, the number of surviving carrier sums is
  not bounded here.

The second assertion is the open projection step in the sharp four-cycle
argument.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from math import isqrt


@dataclass(frozen=True)
class ProductBandPoint:
    completion: int
    carrier: int
    error: int


@dataclass(frozen=True)
class PairInvariants:
    completion_sum: int
    carrier_sum: int
    error_sum: int
    product_sum: int
    completion_difference: int
    carrier_difference: int
    product_difference: int
    cross_determinant: int


def divisor_count(value: int) -> int:
    """Return the number of positive divisors of a nonzero integer."""

    value = abs(value)
    if value == 0:
        raise ValueError("zero has no finite divisor count")
    total = 1
    prime = 2
    while prime * prime <= value:
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        if exponent:
            total *= exponent + 1
        prime = 3 if prime == 2 else prime + 2
    if value > 1:
        total *= 2
    return total


def invariants(
    first: ProductBandPoint,
    second: ProductBandPoint,
    center: int,
) -> PairInvariants:
    """Compute the centered variables used by the discriminant audit."""

    a, v = first.completion, first.carrier
    b, w = second.completion, second.carrier
    if a * v - center != first.error or b * w - center != second.error:
        raise ValueError("point does not have the declared product error")
    return PairInvariants(
        completion_sum=a + b,
        carrier_sum=v + w,
        error_sum=first.error + second.error,
        product_sum=a * v + b * w,
        completion_difference=a - b,
        carrier_difference=v - w,
        product_difference=a * v - b * w,
        cross_determinant=a * w - b * v,
    )


def verify_discriminant_identities(
    first: ProductBandPoint,
    second: ProductBandPoint,
    center: int,
) -> PairInvariants:
    """Replay all exact pair-cell identities from the audit."""

    data = invariants(first, second, center)
    a, v = first.completion, first.carrier
    b, w = second.completion, second.carrier
    S, U, P = data.completion_sum, data.carrier_sum, data.product_sum
    x, y, X = (
        data.completion_difference,
        data.carrier_difference,
        data.product_difference,
    )
    delta = data.cross_determinant

    assert P == 2 * center + data.error_sum
    assert S * U + x * y == 2 * P
    assert S * y + x * U == 2 * X
    assert S * X + P * (b - a) == 2 * a * b * (v - w)
    assert 2 * a * b * U - P * S == (b - a) * X
    assert U * X + P * (w - v) == 2 * v * w * (a - b)
    assert (S * U - P - delta) * (S * U - P + delta) == P * P - X * X
    return data


def refined_pair_cells(
    points: list[ProductBandPoint],
) -> Counter[tuple[int, int, int]]:
    """Count ordered pairs by ``(completion sum, error sum, carrier sum)``."""

    return Counter(
        (
            first.completion + second.completion,
            first.error + second.error,
            first.carrier + second.carrier,
        )
        for first in points
        for second in points
    )


def projected_pair_cells(
    points: list[ProductBandPoint],
) -> Counter[tuple[int, int]]:
    """Count ordered pairs after forgetting the carrier sum."""

    return Counter(
        (
            first.completion + second.completion,
            first.error + second.error,
        )
        for first in points
        for second in points
    )


def refined_divisor_majorant(
    completion_sum: int,
    error_sum: int,
    carrier_sum: int,
    center: int,
) -> int | None:
    """Return ``2*tau(|2P-SU|)``; ``None`` denotes its zero exceptional case.

    Here ``P=2*center+error_sum``.  If the returned value is not ``None``,
    it bounds the number of ordered integral pairs in this refined cell,
    before imposing parity or shell restrictions.
    """

    product_sum = 2 * center + error_sum
    residual = 2 * product_sum - completion_sum * carrier_sum
    if residual == 0:
        return None
    return 2 * divisor_count(residual)


def assert_refined_divisor_bounds(
    points: list[ProductBandPoint],
    center: int,
) -> None:
    """Check the divisor bound, including the graph-like zero residual case."""

    completion_fibres = Counter(point.completion for point in points)
    carrier_fibres = Counter(point.carrier for point in points)
    graph_like = max(completion_fibres.values(), default=0) <= 1
    inverse_graph_like = max(carrier_fibres.values(), default=0) <= 1
    for (completion_sum, error_sum, carrier_sum), multiplicity in refined_pair_cells(
        points
    ).items():
        majorant = refined_divisor_majorant(
            completion_sum, error_sum, carrier_sum, center
        )
        if majorant is None:
            if not (graph_like and inverse_graph_like):
                raise ValueError("zero residual needs one-point coordinate fibres")
            assert multiplicity <= 1
        else:
            assert multiplicity <= majorant


def shell_points(q: int, band: int, center: int) -> list[ProductBandPoint]:
    """Enumerate the integer graph in ``[q,2q]^2`` and one product band."""

    if q <= 2 * band:
        raise ValueError("the shell must be thinner than a coordinate fibre")
    points: list[ProductBandPoint] = []
    for completion in range(q, 2 * q + 1):
        nearest = center // completion
        for carrier in range(nearest - 1, nearest + 3):
            error = completion * carrier - center
            if q <= carrier <= 2 * q and abs(error) <= band:
                points.append(ProductBandPoint(completion, carrier, error))
    return sorted(set(points), key=lambda point: (point.completion, point.carrier))


def scan_pair_cells(q: int, band: int, center: int) -> dict[str, int]:
    """Return a small deterministic exact/refined multiplicity ledger."""

    points = shell_points(q, band, center)
    projected = projected_pair_cells(points)
    refined = refined_pair_cells(points)
    carrier_sums_by_cell: dict[tuple[int, int], set[int]] = defaultdict(set)
    for completion_sum, error_sum, carrier_sum in refined:
        carrier_sums_by_cell[completion_sum, error_sum].add(carrier_sum)
    return {
        "points": len(points),
        "maximum_projected_cell": max(projected.values(), default=0),
        "maximum_refined_cell": max(refined.values(), default=0),
        "maximum_carrier_sums_per_cell": max(
            (len(values) for values in carrier_sums_by_cell.values()), default=0
        ),
    }


def tangent_block_ledger(root: int, band: int) -> dict[str, int]:
    """Calibrate exact and ``sqrt(band)``-blocked cells on a tangent packet."""

    if root <= 4 * band:
        raise ValueError("root must dominate the product band")
    radius = isqrt(band)
    points = [
        ProductBandPoint(root + offset, root - offset, -(offset * offset))
        for offset in range(-radius, radius + 1)
    ]
    exact = projected_pair_cells(points)
    block_width = max(1, isqrt(band))
    central_sum = 2 * root
    central_pairs = []
    for first in points:
        for second in points:
            if first.completion + second.completion != central_sum:
                continue
            error_sum = first.error + second.error
            if -block_width <= error_sum <= 0:
                central_pairs.append((first, second, error_sum))

    maximum_direction_product = 0
    for first, _, _ in central_pairs:
        for other, other_second, _ in central_pairs:
            direction_product = abs(
                (other.completion - first.completion)
                * (other_second.completion - first.completion)
            )
            maximum_direction_product = max(maximum_direction_product, direction_product)

    return {
        "points": len(points),
        "block_width": block_width,
        "maximum_exact_cell": max(exact.values(), default=0),
        "central_block_cell": len(central_pairs),
        "maximum_direction_product_in_central_block": maximum_direction_product,
    }


if __name__ == "__main__":
    print(scan_pair_cells(q=200, band=12, center=76_156))
    print(tangent_block_ledger(root=100_000, band=10_000))
