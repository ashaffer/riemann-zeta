"""Exact translation-grid obstructions for fixed-color completion bounds.

The construction in this module lives in the *full integer* shell.  It does
not assert that its nodes are prime powers.  Its role is to replay exactly a
family in which one fixed 2-by-2 color rectangle has order ``sqrt(D)``
different row/carrier completions while its determinant has order ``D``.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np

from qp_four_cycle_hostile_lab import (
    FourCycleCore,
    centered_fourier_amplitude,
    rectangle_value_and_gradient,
)


FULL_APERTURE = 50.0 / 33.0
PROJECT_WIDTH = 0.2


@dataclass(frozen=True)
class TranslationGridAudit:
    """Exact labels and finite cutoff diagnostics for one translation grid."""

    q: int
    denominator: int
    row_ratio: int
    color_ratio: int
    row_step: int
    column_step: int
    first_translation: int
    last_translation: int
    cutoff: float
    geometric_degree_cap: float
    completions: int
    colors: tuple[int, int, int, int]
    color_determinant: int
    maximum_absolute_frequency: float
    maximum_absolute_eightfold_residual: int
    completion_determinant_ratio: float
    completion_sqrt_degree_ratio: float


@dataclass(frozen=True)
class TranslationGridFourCycleAudit:
    """Fourth-trace replay of a symmetrized finite translation grid."""

    nodes: int
    entries: int
    active_colors: int
    geometric_degree_cap: float
    smooth_non_degenerate_four_cycle: float
    smooth_fourth_trace: float
    unweighted_non_degenerate_four_cycle: float
    unweighted_fourth_trace: float


def translation_grid_entry(
    denominator: int,
    row_ratio: int,
    color_ratio: int,
    step: int,
    translation: int,
    row_index: int,
    column_index: int,
    *,
    column_step: int | None = None,
) -> tuple[int, int, int]:
    """Return ``(a_i(t), b_j(t), c_ij)`` for the exact grid."""

    if row_index not in (0, 1) or column_index not in (0, 1):
        raise ValueError("row_index and column_index must be zero or one")
    if column_step is None:
        column_step = step
    base_row = row_ratio * denominator
    base_color = color_ratio * denominator
    row = base_row + row_ratio * row_index * step + translation
    column = (
        base_row + row_ratio * column_index * column_step - translation
    )
    color = base_color - color_ratio * (
        row_index * step + column_index * column_step
    )
    return row, column, color


def translation_grid_product_increment(
    denominator: int,
    row_ratio: int,
    color_ratio: int,
    step: int,
    translation: int,
    row_index: int,
    column_index: int,
    *,
    column_step: int | None = None,
) -> int:
    """Return ``a_i(t)b_j(t)c_ij-A^2 C`` by its exact identity.

    Here ``A=row_ratio*denominator`` and
    ``C=color_ratio*denominator``.  The cancellation

    ``row_ratio*C = color_ratio*A``

    removes every term linear in ``step``.
    """

    if row_index not in (0, 1) or column_index not in (0, 1):
        raise ValueError("row_index and column_index must be zero or one")
    r = row_ratio
    s = color_ratio
    n = denominator
    if column_step is None:
        column_step = step
    row_offset = row_index * step
    column_offset = column_index * column_step
    base_increment = (
        -r
        * r
        * s
        * n
        * (
            row_offset * row_offset
            + row_offset * column_offset
            + column_offset * column_offset
        )
        - r
        * r
        * s
        * row_offset
        * column_offset
        * (row_offset + column_offset)
    )
    color = s * n - s * (row_offset + column_offset)
    translation_increment = (
        r * (column_offset - row_offset) * translation
        - translation * translation
    ) * color
    return base_increment + translation_increment


def audit_translation_grid(
    *,
    q: int,
    denominator: int,
    row_ratio: int,
    color_ratio: int,
    step: int,
    column_step: int | None = None,
    first_translation: int,
    last_translation: int,
    cutoff: float,
    aperture: float = FULL_APERTURE,
    width: float = PROJECT_WIDTH,
) -> TranslationGridAudit:
    """Verify every triple of a finite full-integer translation grid.

    The audit checks shell membership, the exact nearest-color condition used
    by the finite carry-core builder, and the logarithmic cutoff.  It raises
    ``ValueError`` at the first failed condition.
    """

    if q <= 2 or q % 2 == 0:
        raise ValueError("q must be an odd integer greater than two")
    if denominator <= 0 or row_ratio <= 0 or color_ratio <= 0:
        raise ValueError("ratios and denominator must be positive")
    if column_step is None:
        column_step = step
    if step <= 0 or column_step <= 0 or first_translation > last_translation:
        raise ValueError("invalid step or translation interval")
    if cutoff <= 0.0 or width <= 0.0 or not 1.0 < aperture < 2.0:
        raise ValueError("invalid analytic parameters")

    center = q / 2.0
    bandwidth = center**aperture
    degree_cap = cutoff * q * q / bandwidth
    lower = math.ceil(center * math.exp(-width))
    upper = math.floor(center * math.exp(width))
    maximum_frequency = 0.0
    maximum_residual = 0
    base_row = row_ratio * denominator
    base_color = color_ratio * denominator

    for translation in range(first_translation, last_translation + 1):
        for row_index in (0, 1):
            for column_index in (0, 1):
                row, column, color = translation_grid_entry(
                    denominator,
                    row_ratio,
                    color_ratio,
                    step,
                    translation,
                    row_index,
                    column_index,
                    column_step=column_step,
                )
                if not all(lower <= value <= upper for value in (row, column, color)):
                    raise ValueError("a translation-grid node leaves the shell")
                residual = 8 * row * column * color - q**3
                predicted = (
                    8
                    * (
                        base_row * base_row * base_color
                        + translation_grid_product_increment(
                            denominator,
                            row_ratio,
                            color_ratio,
                            step,
                            translation,
                            row_index,
                            column_index,
                            column_step=column_step,
                        )
                    )
                    - q**3
                )
                if residual != predicted:
                    raise AssertionError("translation-grid residual identity failed")
                # This is the exact nearest-integer condition
                # |c-q^3/(8ab)| < 1/2.
                if abs(residual) >= 4 * row * column:
                    raise ValueError("the selected color is not the unique nearest integer")
                frequency = bandwidth * math.log1p(residual / q**3)
                if abs(frequency) > cutoff:
                    raise ValueError("a translation-grid entry misses the cutoff")
                maximum_frequency = max(maximum_frequency, abs(frequency))
                maximum_residual = max(maximum_residual, abs(residual))

    colors = (
        base_color,
        base_color - color_ratio * column_step,
        base_color - color_ratio * step,
        base_color - color_ratio * (step + column_step),
    )
    determinant = colors[0] * colors[3] - colors[1] * colors[2]
    completions = last_translation - first_translation + 1
    return TranslationGridAudit(
        q=q,
        denominator=denominator,
        row_ratio=row_ratio,
        color_ratio=color_ratio,
        row_step=step,
        column_step=column_step,
        first_translation=first_translation,
        last_translation=last_translation,
        cutoff=cutoff,
        geometric_degree_cap=degree_cap,
        completions=completions,
        colors=colors,
        color_determinant=determinant,
        maximum_absolute_frequency=maximum_frequency,
        maximum_absolute_eightfold_residual=maximum_residual,
        completion_determinant_ratio=(
            completions * abs(determinant) / degree_cap
        ),
        completion_sqrt_degree_ratio=completions / math.sqrt(degree_cap),
    )


def explicit_prime_modulus_integer_witness() -> TranslationGridAudit:
    """Replay the exact ``q=87541837`` full-integer witness."""

    return audit_translation_grid(
        q=87_541_837,
        denominator=5_720_399,
        row_ratio=8,
        color_ratio=7,
        step=15,
        first_translation=-152,
        last_translation=152,
        cutoff=12.0,
    )


def explicit_distinct_color_integer_witness() -> TranslationGridAudit:
    """Replay an all-four-colors-distinct version of the prime-q witness."""

    return audit_translation_grid(
        q=87_541_837,
        denominator=5_720_399,
        row_ratio=8,
        color_ratio=7,
        step=15,
        column_step=14,
        first_translation=-165,
        last_translation=157,
        cutoff=12.0,
    )


def explicit_distinct_color_four_cycle_audit() -> TranslationGridFourCycleAudit:
    """Evaluate ``Q_nd`` on the symmetrized four-color explicit witness.

    Both ``(a,b,c)`` and ``(b,a,c)`` are inserted.  Duplicate ordered pairs
    are rejected unless they carry the same color, replaying pair uniqueness.
    The color vector is ``1/2`` on the four distinct colors.
    """

    q = 87_541_837
    n = 5_720_399
    r = 8
    s = 7
    row_step = 15
    column_step = 14
    first_translation = -165
    last_translation = 157
    cutoff = 12.0
    aperture = FULL_APERTURE
    bandwidth = (q / 2.0) ** aperture
    triples: dict[tuple[int, int, int], float] = {}
    pair_colors: dict[tuple[int, int], int] = {}
    for translation in range(first_translation, last_translation + 1):
        for row_index in (0, 1):
            for column_index in (0, 1):
                a, b, c = translation_grid_entry(
                    n,
                    r,
                    s,
                    row_step,
                    translation,
                    row_index,
                    column_index,
                    column_step=column_step,
                )
                frequency = bandwidth * math.log(8 * a * b * c / q**3)
                for row, column in ((a, b), (b, a)):
                    old_color = pair_colors.setdefault((row, column), c)
                    if old_color != c:
                        raise AssertionError("translation grid violates pair uniqueness")
                    triples[row, column, c] = frequency

    values = np.asarray(
        sorted({node for triple in triples for node in triple}), dtype=np.int64
    )
    index = {int(value): position for position, value in enumerate(values)}
    items = tuple(triples.items())
    frequencies = np.asarray([frequency for _, frequency in items], dtype=float)
    weights = centered_fourier_amplitude(frequencies, quadrature_order=128)
    rows = np.asarray([index[triple[0]] for triple, _ in items], dtype=np.int32)
    columns = np.asarray([index[triple[1]] for triple, _ in items], dtype=np.int32)
    color_indices = np.asarray(
        [index[triple[2]] for triple, _ in items], dtype=np.int32
    )
    core = FourCycleCore(
        q=q,
        aperture=aperture,
        width=PROJECT_WIDTH,
        cutoff=cutoff,
        values=values,
        rows=rows,
        columns=columns,
        colors=color_indices,
        weights=weights,
    )
    color_vector = np.zeros(values.size, dtype=float)
    active_colors = (
        s * n,
        s * n - s * column_step,
        s * n - s * row_step,
        s * n - s * (row_step + column_step),
    )
    for color in active_colors:
        color_vector[index[color]] = 0.5
    smooth_q, smooth_trace, _ = rectangle_value_and_gradient(
        core, color_vector, with_gradient=False
    )
    unweighted_core = FourCycleCore(
        q=q,
        aperture=aperture,
        width=PROJECT_WIDTH,
        cutoff=cutoff,
        values=values,
        rows=rows,
        columns=columns,
        colors=color_indices,
        weights=np.ones(rows.size, dtype=float),
    )
    unweighted_q, unweighted_trace, _ = rectangle_value_and_gradient(
        unweighted_core, color_vector, with_gradient=False
    )
    return TranslationGridFourCycleAudit(
        nodes=int(values.size),
        entries=int(rows.size),
        active_colors=len(active_colors),
        geometric_degree_cap=core.geometric_degree_cap,
        smooth_non_degenerate_four_cycle=smooth_q,
        smooth_fourth_trace=smooth_trace,
        unweighted_non_degenerate_four_cycle=unweighted_q,
        unweighted_fourth_trace=unweighted_trace,
    )
