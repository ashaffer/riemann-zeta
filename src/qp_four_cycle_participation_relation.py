"""Finite ledgers for participation-sensitive short-relation bounds.

The analytic statements live in the accompanying report.  This module
replays the capped-hyperbola dyadic inequality, counts primitive rank-one
relation directions at small heights, and constructs the exact direct-sum
barrier for an invertible product-band argument.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


Matrix2 = tuple[int, int, int, int]


def capped_dyadic_l1(length: int, participation: int) -> Fraction:
    """Return ``min(sqrt(length),length/sqrt(M))`` squared.

    The returned rational is the square of the dyadic ``ell^1`` envelope,
    namely ``min(length, length**2/M)``.  Squaring avoids floating-point
    roundoff in exact tests.
    """

    if length < 1 or participation < 1:
        raise ValueError("length and participation must be positive")
    return min(Fraction(length), Fraction(length * length, participation))


def capped_hyperbola_block_is_valid(
    first_length: int,
    second_length: int,
    product_limit: int,
    participation: int,
) -> bool:
    """Check the exact squared dyadic bound from Lemma 2.1.

    For ``HL<=D``, the product of the two capped ``ell^1`` envelopes is at
    most ``min(sqrt(D),D/M)``.  This function verifies the squared form.
    """

    if min(first_length, second_length, product_limit, participation) < 1:
        raise ValueError("all inputs must be positive")
    if first_length * second_length > product_limit:
        raise ValueError("the dyadic rectangle exceeds the product limit")
    left_squared = (
        capped_dyadic_l1(first_length, participation)
        * capped_dyadic_l1(second_length, participation)
    )
    target_squared = min(
        Fraction(product_limit),
        Fraction(product_limit * product_limit, participation * participation),
    )
    return left_squared <= target_squared


def _canonical_sign(matrix: Matrix2) -> Matrix2:
    for value in matrix:
        if value:
            if value < 0:
                return tuple(-entry for entry in matrix)  # type: ignore[return-value]
            return matrix
    raise ValueError("the zero matrix has no projective direction")


def primitive_rank_one_directions(height: int) -> set[Matrix2]:
    """Enumerate primitive rank-one two-by-two directions of small height."""

    if height < 1:
        raise ValueError("height must be positive")
    directions: set[Matrix2] = set()
    for a in range(-height, height + 1):
        for b in range(-height, height + 1):
            for c in range(-height, height + 1):
                for d in range(-height, height + 1):
                    matrix = (a, b, c, d)
                    if matrix == (0, 0, 0, 0) or a * d != b * c:
                        continue
                    common = gcd(gcd(abs(a), abs(b)), gcd(abs(c), abs(d)))
                    if common != 1:
                        continue
                    directions.add(_canonical_sign(matrix))
    return directions


@dataclass(frozen=True)
class DirectSumBarrierLedger:
    """Exact norms and bilinear value for the product-band barrier."""

    block_side: int
    block_count: int
    coordinate_count: int
    product_limit: int
    input_norm_squared: Fraction
    input_fourth_power_sum: Fraction
    bilinear_value: Fraction
    square_root_product_limit: int


def direct_sum_product_band_barrier(
    block_side: int,
    block_count: int,
) -> DirectSumBarrierLedger:
    """Return the constant-vector ledger for ``T`` complete ``K x K`` blocks."""

    if block_side < 1 or block_count < 1:
        raise ValueError("block dimensions must be positive")
    k = block_side
    t = block_count
    coordinate_count = t * k
    coefficient_squared = Fraction(1, coordinate_count)
    input_norm_squared = coordinate_count * coefficient_squared
    input_fourth_power_sum = coordinate_count * coefficient_squared**2
    bilinear_value = t * k * k * coefficient_squared
    product_limit = k * k
    return DirectSumBarrierLedger(
        block_side=k,
        block_count=t,
        coordinate_count=coordinate_count,
        product_limit=product_limit,
        input_norm_squared=input_norm_squared,
        input_fourth_power_sum=input_fourth_power_sum,
        bilinear_value=bilinear_value,
        square_root_product_limit=isqrt(product_limit),
    )
