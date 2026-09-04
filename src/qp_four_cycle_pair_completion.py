"""Exact pair-completion invariants for the QP four-cycle problem.

For a fixed oriented color matrix ``C=(c11,c12,c21,c22)``, a carrier
completion is ``X=(a1,a2,b1,b2)`` and its product matrix is

``M(X)=(a1*b1,a1*b2,a2*b1,a2*b2)``.

This module groups ordered pairs of completions by the exact difference
``E=M(X)-M(X')``.  The routines are exact combinatorics; the finite ledgers
they produce make no asymptotic assertion.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence

from qp_four_cycle_h_graph_lab import RectangleRecord


ColorMatrix = tuple[int, int, int, int]
Completion = tuple[int, int, int, int]
ProductMatrix = tuple[int, int, int, int]
EnergyMatrix = tuple[int, int, int, int]


@dataclass(frozen=True)
class PairCompletionLedger:
    """Exact multiplicity and common-level statistics for fixed colors."""

    completions: int
    oriented_color_matrices: int
    d4_color_orbits: int
    repeated_oriented_color_matrices: int
    maximum_oriented_completion_multiplicity: int
    maximum_d4_completion_multiplicity: int
    oriented_colors_with_multiple_levels: int
    maximum_levels_per_oriented_color: int
    ordered_completion_pairs: int
    zero_energy_ordered_pairs: int
    nonzero_energy_ordered_pairs: int
    fixed_color_energy_keys: int
    maximum_fixed_color_energy_multiplicity: int
    maximum_nonzero_fixed_color_energy_multiplicity: int
    colliding_nonzero_fixed_color_energy_keys: int
    maximum_d4_nonzero_energy_multiplicity: int


@dataclass(frozen=True)
class FlatCompletionEnergy:
    """Value of ``sum_C m(C)^2 prod_ij z_cij`` for flat ``z``."""

    active_colors: int
    contributing_color_matrices: int
    completions: int
    raw_completion_square_sum: int
    weighted_completion_square_sum: float


def carrier_product_matrix(completion: Completion) -> ProductMatrix:
    """Return the rank-one carrier product matrix in row-major order."""

    a1, a2, b1, b2 = completion
    return (a1 * b1, a1 * b2, a2 * b1, a2 * b2)


def energy_difference(first: Completion, second: Completion) -> EnergyMatrix:
    """Return ``M(first)-M(second)`` entrywise."""

    left = carrier_product_matrix(first)
    right = carrier_product_matrix(second)
    return tuple(x - y for x, y in zip(left, right))  # type: ignore[return-value]


def completion_level(colors: ColorMatrix, completion: Completion) -> int:
    """Return ``c11*M11+c22*M22-c12*M12-c21*M21``."""

    c11, c12, c21, c22 = colors
    m11, m12, m21, m22 = carrier_product_matrix(completion)
    return c11 * m11 + c22 * m22 - c12 * m12 - c21 * m21


def energy_linear_form(colors: ColorMatrix, energy: EnergyMatrix) -> int:
    """Return the exact common-level linear form applied to ``E``."""

    c11, c12, c21, c22 = colors
    e11, e12, e21, e22 = energy
    return c11 * e11 + c22 * e22 - c12 * e12 - c21 * e21


def determinant(values: Sequence[int]) -> int:
    """Return the determinant of a row-major two-by-two matrix."""

    if len(values) != 4:
        raise ValueError("a two-by-two matrix needs four entries")
    return values[0] * values[3] - values[1] * values[2]


def energy_determinant_factorization(
    first: Completion, second: Completion
) -> tuple[int, int]:
    """Return both sides of the exact determinant factorization.

    If ``M=a*b^T`` and ``M'=A*B^T``, then

    ``det(M-M')=-(a1*A2-a2*A1)(b1*B2-b2*B1)``.
    """

    a1, a2, b1, b2 = first
    A1, A2, B1, B2 = second
    left = determinant(energy_difference(first, second))
    right = -(a1 * A2 - a2 * A1) * (b1 * B2 - b2 * B1)
    return left, right


def _d4_orbit(matrix: Sequence[int]) -> tuple[tuple[int, int, int, int], ...]:
    if len(matrix) != 4:
        raise ValueError("a two-by-two matrix needs four entries")
    a, b, c, d = matrix
    return (
        (a, b, c, d),
        (c, d, a, b),
        (b, a, d, c),
        (d, c, b, a),
        (a, c, b, d),
        (b, d, a, c),
        (c, a, d, b),
        (d, b, c, a),
    )


def canonical_color_matrix(colors: ColorMatrix) -> ColorMatrix:
    """Canonicalize a color matrix under row, column, and transpose moves."""

    return min(_d4_orbit(colors))


def canonical_color_energy_pair(
    colors: ColorMatrix, energy: EnergyMatrix
) -> tuple[ColorMatrix, EnergyMatrix]:
    """Canonicalize ``(C,E)`` under the same simultaneous D4 move."""

    return min(zip(_d4_orbit(colors), _d4_orbit(energy)))


def completion_groups_from_rectangles(
    rectangles: Iterable[RectangleRecord],
) -> dict[ColorMatrix, tuple[Completion, ...]]:
    """Group finite rectangle records by their exact oriented colors."""

    groups: dict[ColorMatrix, list[Completion]] = defaultdict(list)
    for rectangle in rectangles:
        groups[rectangle.colors].append(
            (
                rectangle.first_row,
                rectangle.second_row,
                rectangle.first_column,
                rectangle.second_column,
            )
        )
    return {
        colors: tuple(sorted(completions))
        for colors, completions in groups.items()
    }


def pair_completion_ledger(
    groups: Mapping[ColorMatrix, Sequence[Completion]],
) -> PairCompletionLedger:
    """Audit exact ``(C,E)`` multiplicities over ordered completion pairs."""

    normalized = {
        tuple(colors): tuple(tuple(completion) for completion in completions)
        for colors, completions in groups.items()
    }
    color_multiplicity = {colors: len(items) for colors, items in normalized.items()}
    d4_color_counts: Counter[ColorMatrix] = Counter()
    levels_by_color: dict[ColorMatrix, set[int]] = {}
    exact_energy_counts: Counter[tuple[ColorMatrix, EnergyMatrix]] = Counter()
    d4_energy_counts: Counter[tuple[ColorMatrix, EnergyMatrix]] = Counter()
    zero_pairs = 0
    nonzero_pairs = 0

    for colors, completions in normalized.items():
        d4_color_counts[canonical_color_matrix(colors)] += len(completions)
        levels_by_color[colors] = {
            completion_level(colors, completion) for completion in completions
        }
        for first in completions:
            for second in completions:
                energy = energy_difference(first, second)
                if energy_linear_form(colors, energy) != (
                    completion_level(colors, first)
                    - completion_level(colors, second)
                ):
                    raise AssertionError("the common-level identity failed")
                exact_energy_counts[colors, energy] += 1
                d4_energy_counts[canonical_color_energy_pair(colors, energy)] += 1
                if energy == (0, 0, 0, 0):
                    zero_pairs += 1
                else:
                    nonzero_pairs += 1

    nonzero_counts = [
        count
        for (_, energy), count in exact_energy_counts.items()
        if energy != (0, 0, 0, 0)
    ]
    d4_nonzero_counts = [
        count
        for (_, energy), count in d4_energy_counts.items()
        if energy != (0, 0, 0, 0)
    ]
    total_completions = sum(color_multiplicity.values())
    return PairCompletionLedger(
        completions=total_completions,
        oriented_color_matrices=len(normalized),
        d4_color_orbits=len(d4_color_counts),
        repeated_oriented_color_matrices=sum(
            multiplicity >= 2 for multiplicity in color_multiplicity.values()
        ),
        maximum_oriented_completion_multiplicity=max(
            color_multiplicity.values(), default=0
        ),
        maximum_d4_completion_multiplicity=max(d4_color_counts.values(), default=0),
        oriented_colors_with_multiple_levels=sum(
            len(levels) >= 2 for levels in levels_by_color.values()
        ),
        maximum_levels_per_oriented_color=max(
            (len(levels) for levels in levels_by_color.values()), default=0
        ),
        ordered_completion_pairs=sum(
            multiplicity * multiplicity
            for multiplicity in color_multiplicity.values()
        ),
        zero_energy_ordered_pairs=zero_pairs,
        nonzero_energy_ordered_pairs=nonzero_pairs,
        fixed_color_energy_keys=len(exact_energy_counts),
        maximum_fixed_color_energy_multiplicity=max(
            exact_energy_counts.values(), default=0
        ),
        maximum_nonzero_fixed_color_energy_multiplicity=max(
            nonzero_counts, default=0
        ),
        colliding_nonzero_fixed_color_energy_keys=sum(
            count >= 2 for count in nonzero_counts
        ),
        maximum_d4_nonzero_energy_multiplicity=max(
            d4_nonzero_counts, default=0
        ),
    )


def flat_completion_energy(
    groups: Mapping[ColorMatrix, Sequence[Completion]],
    *,
    active_colors: Iterable[int] | None = None,
    repeated_only: bool = False,
) -> FlatCompletionEnergy:
    """Evaluate the raw and flat-weighted fixed-color square energy.

    The flat vector is ``z_c=K**(-1/2)`` on the selected ``K`` colors.
    Therefore every contributing four-color matrix has weight ``K**(-2)``,
    including matrices with repeated entries.
    """

    normalized = {
        tuple(colors): tuple(completions)
        for colors, completions in groups.items()
        if (not repeated_only or len(completions) >= 2)
    }
    if active_colors is None:
        active = {color for colors in normalized for color in colors}
    else:
        active = set(active_colors)
    contributing = {
        colors: completions
        for colors, completions in normalized.items()
        if all(color in active for color in colors)
    }
    raw = sum(len(completions) ** 2 for completions in contributing.values())
    weighted = raw / (len(active) ** 2) if active else 0.0
    return FlatCompletionEnergy(
        active_colors=len(active),
        contributing_color_matrices=len(contributing),
        completions=sum(len(items) for items in contributing.values()),
        raw_completion_square_sum=raw,
        weighted_completion_square_sum=weighted,
    )


def translation_grid_completion(
    denominator: int,
    row_ratio: int,
    row_step: int,
    column_step: int,
    translation: int,
) -> Completion:
    """Return the ordered carriers of one translation-grid completion."""

    base = denominator * row_ratio
    return (
        base + translation,
        base + row_ratio * row_step + translation,
        base - translation,
        base + row_ratio * column_step - translation,
    )


def translation_pair_energy_parameters(
    *,
    row_ratio: int,
    row_step: int,
    column_step: int,
    first_translation: int,
    second_translation: int,
) -> tuple[int, int, int, int]:
    """Recover the translation difference/sum from two entries of ``E``.

    The return is ``(difference, sum, recovered_difference, recovered_sum)``.
    Unequal row/column steps use ``E22-E11``.  Equal steps use
    ``E12-E21``.  The formula applies to a non-diagonal ordered pair.
    """

    difference = first_translation - second_translation
    total = first_translation + second_translation
    if difference == 0:
        raise ValueError("the ordered translation pair must be non-diagonal")
    base_completion = translation_grid_completion(
        1,
        row_ratio,
        row_step,
        column_step,
        first_translation,
    )
    other_completion = translation_grid_completion(
        1,
        row_ratio,
        row_step,
        column_step,
        second_translation,
    )
    e11, e12, e21, e22 = energy_difference(base_completion, other_completion)
    if row_step != column_step:
        denominator = row_ratio * (column_step - row_step)
        recovered_difference = (e22 - e11) // denominator
    else:
        denominator = 2 * row_ratio * row_step
        recovered_difference = (e12 - e21) // denominator
    if recovered_difference == 0:
        raise AssertionError("the energy did not recover a nonzero difference")
    recovered_sum = -e11 // recovered_difference
    return difference, total, recovered_difference, recovered_sum

