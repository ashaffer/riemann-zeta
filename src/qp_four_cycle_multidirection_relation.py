"""Exact ledgers for aggregate primitive rank-one color relations.

The accompanying report proves a restricted-strong-type estimate for the
union of all primitive rank-one relations of bounded height.  This module
keeps the two elementary numerical inequalities used in the proof exact:

* the unequal-cap dyadic hyperbola estimate; and
* the interpolation between triple uniqueness and the union of the
  fixed-relation estimates.

No floating point arithmetic is used.
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt


def capped_l1_squared(length: int, cap_denominator: int) -> Fraction:
    """Square of ``min(sqrt(length), length/sqrt(cap_denominator))``."""

    if length < 1 or cap_denominator < 1:
        raise ValueError("length and cap_denominator must be positive")
    return min(
        Fraction(length),
        Fraction(length * length, cap_denominator),
    )


def unequal_capped_hyperbola_block_is_valid(
    first_length: int,
    second_length: int,
    product_limit: int,
    first_cap_denominator: int,
    second_cap_denominator: int,
) -> bool:
    """Verify the exact dyadic unequal-cap hyperbola bound.

    If ``HL <= D``, ``||a||_2,||b||_2 <= 1``, and

    ``||a||_infinity <= A^{-1/2}``,
    ``||b||_infinity <= B^{-1/2}``,

    then the product of the two dyadic ``ell^1`` envelopes is at most
    ``min(sqrt(D), D/sqrt(A B))``.  We check its squared form.
    """

    values = (
        first_length,
        second_length,
        product_limit,
        first_cap_denominator,
        second_cap_denominator,
    )
    if min(values) < 1:
        raise ValueError("all inputs must be positive")
    if first_length * second_length > product_limit:
        raise ValueError("the dyadic rectangle exceeds the product limit")

    left_squared = (
        capped_l1_squared(first_length, first_cap_denominator)
        * capped_l1_squared(second_length, second_cap_denominator)
    )
    target_squared = min(
        Fraction(product_limit),
        Fraction(
            product_limit * product_limit,
            first_cap_denominator * second_cap_denominator,
        ),
    )
    return left_squared <= target_squared


def restricted_type_bounds(
    support_sizes: tuple[int, int, int, int],
    direction_height: int,
    determinant_width: int,
) -> tuple[Fraction, Fraction]:
    """Return squared triple-uniqueness and fixed-relation-union bounds.

    The support sizes are sorted internally.  For normalized indicators of
    four sets of sizes ``N1 <= ... <= N4``, the two bounds are

    ``X = sqrt(N1 N2 N3 / N4)`` and

    ``Y = H^2 D / ((N2 N3)^(1/4) N4^(1/2))``.

    The second value is represented after squaring, so both outputs are
    exact rationals.
    """

    if direction_height < 1 or determinant_width < 1:
        raise ValueError("height and width must be positive")
    if len(support_sizes) != 4 or min(support_sizes) < 1:
        raise ValueError("four positive support sizes are required")
    n1, n2, n3, n4 = sorted(support_sizes)
    x_squared = Fraction(n1 * n2 * n3, n4)
    # Y^2 = H^4 D^2 / (sqrt(N2 N3) N4).  Keep the radical out
    # by returning a conservative rational upper certificate using
    # floor(sqrt(N2 N3)); tests of the interpolation use integer squares
    # directly in ``restricted_type_interpolation_is_valid`` below.
    root = isqrt(n2 * n3)
    y_squared_upper = Fraction(
        direction_height**4 * determinant_width**2,
        max(1, root) * n4,
    )
    return x_squared, y_squared_upper


def restricted_type_interpolation_is_valid(
    support_sizes: tuple[int, int, int, int],
    direction_height: int,
    determinant_width: int,
) -> bool:
    """Check ``min(X,Y) <= H sqrt(D)`` without radicals.

    Here ``X`` and ``Y`` are the two bounds documented in
    :func:`restricted_type_bounds`.  The verification splits according to
    whether ``X <= H sqrt(D)``.  In the complementary case it checks the
    two consequences used in the proof:

    ``N2 N3 > H^2 D`` and ``N4 > H sqrt(D)``.

    Those imply the denominator of ``Y`` is larger than ``H sqrt(D)``.
    """

    if direction_height < 1 or determinant_width < 1:
        raise ValueError("height and width must be positive")
    if len(support_sizes) != 4 or min(support_sizes) < 1:
        raise ValueError("four positive support sizes are required")
    n1, n2, n3, n4 = sorted(support_sizes)
    h2d = direction_height * direction_height * determinant_width

    # X^2 <= H^2 D.
    if n1 * n2 * n3 <= h2d * n4:
        return True

    # X > H sqrt(D).  Since N1 <= N4 and X <= N4, these are the
    # exact squared consequences used to make Y < H sqrt(D).
    if n2 * n3 <= h2d:
        return False
    if n4 * n4 <= h2d:
        return False

    # We need ((N2 N3)^(1/4) N4^(1/2))^2
    #       = sqrt(N2 N3) N4 > H^2 D.
    # Squaring this last inequality gives the exact integer check below.
    return n2 * n3 * n4 * n4 > h2d * h2d

