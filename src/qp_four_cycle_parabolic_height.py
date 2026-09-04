"""Exact ledgers for parabolic height and scaled-additivity arguments."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd


Matrix2 = tuple[int, int, int, int]
Pair = tuple[int, int]


def determinant(matrix: Matrix2) -> int:
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def determinant_polarization(first: Matrix2, second: Matrix2) -> int:
    """Return the mixed coefficient in ``det(x*first+y*second)``."""

    a, b, c, d = first
    e, f, g, h = second
    return a * h + e * d - b * g - f * c


@dataclass(frozen=True)
class DegeneratePlaneDirectionLedger:
    first_determinant: int
    mixed_coefficient: int
    second_determinant: int
    discriminant: int
    root_coordinates: Pair
    direction: Matrix2
    direction_determinant: int


@dataclass(frozen=True)
class NondegenerateSliceChoice:
    shear: int
    sheared_second: Matrix2
    binary_discriminant: int


def degenerate_plane_direction(
    first: Matrix2,
    second: Matrix2,
) -> DegeneratePlaneDirectionLedger:
    """Return the repeated rank-one direction of a degenerate binary section."""

    a = determinant(first)
    b = determinant_polarization(first, second)
    c = determinant(second)
    discriminant = b * b - 4 * a * c
    if discriminant:
        raise ValueError("the binary determinant restriction is nondegenerate")
    if a == b == c == 0:
        raise ValueError("the determinant restriction vanishes identically")
    if a:
        root_x, root_y = b, -2 * a
    else:
        # Then b=0 and c!=0, so the repeated root is y=0.
        root_x, root_y = 1, 0
    common = gcd(abs(root_x), abs(root_y))
    root_x //= common
    root_y //= common
    if root_x < 0 or (root_x == 0 and root_y < 0):
        root_x = -root_x
        root_y = -root_y
    raw_direction = tuple(
        root_x * left + root_y * right
        for left, right in zip(first, second)
    )
    entry_gcd = 0
    for entry in raw_direction:
        entry_gcd = gcd(entry_gcd, abs(entry))
    if not entry_gcd:
        raise ValueError("the repeated root produced the zero matrix")
    direction = tuple(
        entry // entry_gcd for entry in raw_direction
    )  # type: ignore[assignment]
    if determinant(direction):
        raise AssertionError("the repeated direction is not rank one")
    return DegeneratePlaneDirectionLedger(
        first_determinant=a,
        mixed_coefficient=b,
        second_determinant=c,
        discriminant=discriminant,
        root_coordinates=(root_x, root_y),
        direction=direction,
        direction_determinant=determinant(direction),
    )


def binary_determinant_discriminant(
    first: Matrix2,
    second: Matrix2,
) -> int:
    """Return the infinity discriminant on ``span(first,second)``."""

    mixed = determinant_polarization(first, second)
    return mixed * mixed - 4 * determinant(first) * determinant(second)


def choose_nondegenerate_slice_plane(
    first: Matrix2,
    second: Matrix2,
    third: Matrix2,
) -> NondegenerateSliceChoice:
    """Choose ``t in {0,1,2}`` with nondegenerate ``span(first,second+t*third)``.

    Existence is guaranteed when the determinant form restricted to the
    span of the three inputs is nondegenerate.  The finite function raises
    if the supplied triple violates that hypothesis.
    """

    for shear in (0, 1, 2):
        sheared = tuple(
            left + shear * right for left, right in zip(second, third)
        )
        discriminant = binary_determinant_discriminant(first, sheared)
        if discriminant:
            return NondegenerateSliceChoice(
                shear=shear,
                sheared_second=sheared,  # type: ignore[arg-type]
                binary_discriminant=discriminant,
            )
    raise ValueError("the ternary determinant restriction is degenerate")


@dataclass(frozen=True)
class ScaledAdditivityLedger:
    raw_additive_defect: int
    scaled_colors: Matrix2
    scaled_additive_defect: int
    first_step: int
    second_step: int
    color_determinant: int
    slope_product: int
    scaled_determinant: int
    factored_scaled_determinant: int


def scaled_additivity_ledger(
    colors: Matrix2,
    row_slopes: Pair,
    column_slopes: Pair,
) -> ScaledAdditivityLedger:
    """Audit ``r^T K s=0`` and the resulting determinant factorization."""

    c11, c12, c21, c22 = colors
    r1, r2 = row_slopes
    s1, s2 = column_slopes
    if not all((r1, r2, s1, s2)):
        raise ValueError("all slope components must be nonzero")
    scaled = (
        r1 * s1 * c11,
        r1 * s2 * c12,
        r2 * s1 * c21,
        r2 * s2 * c22,
    )
    d11, d12, d21, d22 = scaled
    scaled_defect = d11 + d22 - d12 - d21
    if scaled_defect:
        raise ValueError("the colors do not obey the rank-one direction relation")
    first_step = d11 - d12
    second_step = d11 - d21
    slope_product = r1 * r2 * s1 * s2
    scaled_determinant = determinant(scaled)
    factored = -first_step * second_step
    if scaled_determinant != slope_product * determinant(colors):
        raise AssertionError("diagonal scaling did not preserve the determinant")
    if scaled_determinant != factored:
        raise AssertionError("the additive determinant did not factor")
    return ScaledAdditivityLedger(
        raw_additive_defect=c11 + c22 - c12 - c21,
        scaled_colors=scaled,
        scaled_additive_defect=scaled_defect,
        first_step=first_step,
        second_step=second_step,
        color_determinant=determinant(colors),
        slope_product=slope_product,
        scaled_determinant=scaled_determinant,
        factored_scaled_determinant=factored,
    )


@dataclass(frozen=True)
class GeneralizedTangentEntry:
    row: int
    column: int
    color: int
    product: int
    target: int
    product_defect: int


def generalized_tangent_entry(
    scale: int,
    parameter: int,
    row_index: int,
    column_index: int,
) -> GeneralizedTangentEntry:
    """Return one cell of the unequal-slope active integer chart."""

    if scale < 1 or scale % 6 != 1:
        raise ValueError("scale must be positive and congruent to one modulo six")
    if row_index not in (0, 1) or column_index not in (0, 1):
        raise ValueError("row and column indices must be zero or one")
    row_slopes = (6, 5)
    column_slopes = (5, 5)
    row_offsets = (0, 2)
    column_offsets = (1, 7)
    row_slope = row_slopes[row_index]
    column_slope = column_slopes[column_index]
    first_offset = row_offsets[row_index]
    second_offset = column_offsets[column_index]
    row = row_slope * (scale + first_offset + parameter)
    column = column_slope * (scale + second_offset - parameter)
    color = (
        125
        * (scale - first_offset - second_offset)
        // (row_slope * column_slope)
    )
    if (
        125 * (scale - first_offset - second_offset)
        % (row_slope * column_slope)
    ):
        raise AssertionError("the chart color is not integral")
    product = row * column * color
    target = 125 * scale**3
    return GeneralizedTangentEntry(
        row=row,
        column=column,
        color=color,
        product=product,
        target=target,
        product_defect=product - target,
    )


def height_split_exponents() -> tuple[Fraction, Fraction, Fraction]:
    """Return the balanced chart threshold, trace, and fourth-root exponents."""

    threshold = Fraction(3, 8)
    trace = 1 + threshold
    operator = trace / 4
    return threshold, trace, operator


def middle_slice_exponents() -> tuple[Fraction, Fraction, Fraction]:
    """Return the critical-cutoff gap and the two middle trace exponents."""

    cutoff_gap = Fraction(1, 11) - Fraction(1, 16)
    nondegenerate = 1 + cutoff_gap
    degenerate = Fraction(11, 8) + cutoff_gap
    return cutoff_gap, nondegenerate, degenerate


def four_elevenths_exponents() -> tuple[Fraction, Fraction, Fraction]:
    """Return the optimized relation cutoff, trace, and operator exponents."""

    cutoff = Fraction(1, 11)
    trace = 1 + 5 * cutoff
    broad = Fraction(3, 2) - cutoff / 2
    if trace != broad:
        raise AssertionError("the relation-cutoff balance is inconsistent")
    return cutoff, trace, trace / 4


def twenty_three_sixty_fourths_exponents(
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return the minima-product cutoff, slice loss, trace, and operator exponents."""

    product_cutoff = Fraction(9, 8)
    project_q = Fraction(33, 16)
    slice_loss = 1 + product_cutoff - project_q
    high_product = 2 - product_cutoff / 2
    low_product = Fraction(11, 8) + slice_loss
    if high_product != low_product:
        raise AssertionError("the minima-product split is not balanced")
    return product_cutoff, slice_loss, high_product, high_product / 4


def eleven_thirty_seconds_exponents(
) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    """Return the sharp two-stage minima split and its consequences.

    The first cutoff is ``lambda1*lambda2=q/D``.  Above it, balancing the
    universal ``D/lambda2`` cap with the parabolic
    ``D^(3/2)*lambda2^(3/2)/q`` cap chooses ``lambda2=D^(5/8)``.
    """

    project_q = Fraction(33, 16)
    product_cutoff = project_q - 1
    second_minimum_cutoff = Fraction(5, 8)
    universal_completion = 1 - second_minimum_cutoff
    parabolic_completion = (
        Fraction(3, 2)
        + Fraction(3, 2) * second_minimum_cutoff
        - project_q
    )
    nondegenerate_completion = (
        1 + 2 * second_minimum_cutoff - project_q
    )
    if universal_completion != parabolic_completion:
        raise AssertionError("the second-minimum split is not balanced")
    if nondegenerate_completion >= universal_completion:
        raise AssertionError("the nondegenerate slice term should be lower")
    trace = 1 + universal_completion
    return (
        product_cutoff,
        second_minimum_cutoff,
        universal_completion,
        trace,
        trace / 4,
    )
