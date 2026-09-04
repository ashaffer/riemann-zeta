"""A multilevel full-integer tangent grid with polynomial color reuse.

The construction is a geometry-only obstruction to decomposing tangent
patches under a bounded color-reuse hypothesis.  It is not an actual
prime-power counterexample.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MultilevelTranslationLedger:
    m: int
    length: int
    q: int
    degree_scale: int
    patches: int
    completions_per_patch: int
    maximum_color_patch_reuse: int
    color_support_size: int
    raw_offdiagonal_pairs: int
    flat_weighted_offdiagonal_mass: float
    spiked_weighted_offdiagonal_mass: float
    maximum_absolute_residual: int
    normalized_residual_cap: float


RESIDUAL_SCALE = 2048


def multilevel_entry(
    m: int,
    row_step: int,
    column_step: int,
    translation: int,
    row_index: int,
    column_index: int,
) -> tuple[int, int, int]:
    """Return one triple in the multilevel translation grid."""

    if row_index not in (0, 1) or column_index not in (0, 1):
        raise ValueError("indices must be zero or one")
    row_offset = row_index * row_step
    column_offset = column_index * column_step
    return (
        m + row_offset + translation,
        m + column_offset - translation,
        m - row_offset - column_offset,
    )


def multilevel_product_increment(
    m: int,
    row_offset: int,
    column_offset: int,
    translation: int,
) -> int:
    """Return ``abc-m^3`` by the exact first-order-cancelled formula."""

    total = row_offset + column_offset
    remainder = (
        row_offset * column_offset
        + translation * (column_offset - row_offset)
        - translation * translation
    )
    return m * (remainder - total * total) - total * remainder


def audit_multilevel_translation_grid(
    m: int,
    length: int,
) -> MultilevelTranslationLedger:
    """Audit the ``h,l,t`` family used in the bounded-reuse obstruction.

    ``h,l`` range from ``L`` through ``2L`` with ``h!=l`` and ``t`` ranges
    from ``20L`` through ``21L``.  Every fixed ``(h,l)`` is one tangent
    patch; the top-left color ``m`` occurs in every patch.
    """

    if length < 2:
        raise ValueError("length must be at least two")
    # Ample room for the shell separation and for asymptotic pair uniqueness.
    if m <= 100_000 * length * length:
        raise ValueError("m must dominate the residual constant times D")
    q = 2 * m
    # The elementary estimate in the proof is
    #
    #   |8(abc-m^3)|/(2m)
    #       <= 2012 L^2 + 7792 L^3/m < 2048 L^2.
    #
    # Thus this choice gives the literal window |8abc-q^3| < qD,
    # rather than only a window with an unspecified absolute constant.
    degree_scale = RESIDUAL_SCALE * length * length
    translations = range(20 * length, 21 * length + 1)
    steps = range(length, 2 * length + 1)
    colors: set[int] = set()
    patch_count = 0
    maximum_residual = 0
    for row_step in steps:
        for column_step in steps:
            if row_step == column_step:
                continue
            patch_count += 1
            patch_colors = (
                m,
                m - column_step,
                m - row_step,
                m - row_step - column_step,
            )
            if len(set(patch_colors)) != 4:
                raise AssertionError("a patch has repeated colors")
            colors.update(patch_colors)
            for translation in translations:
                labels: list[int] = []
                for row_index in (0, 1):
                    for column_index in (0, 1):
                        a, b, c = multilevel_entry(
                            m,
                            row_step,
                            column_step,
                            translation,
                            row_index,
                            column_index,
                        )
                        row_offset = row_index * row_step
                        column_offset = column_index * column_step
                        predicted = multilevel_product_increment(
                            m,
                            row_offset,
                            column_offset,
                            translation,
                        )
                        if a * b * c - m**3 != predicted:
                            raise AssertionError("the residual formula failed")
                        maximum_residual = max(
                            maximum_residual,
                            abs(8 * predicted),
                        )
                        labels.append(c)
                # The four carrier labels are independent of the corner
                # repetition used above.
                carriers = (
                    m + translation,
                    m + row_step + translation,
                    m - translation,
                    m + column_step - translation,
                )
                displayed = (*carriers, *patch_colors)
                if len(set(displayed)) != 8:
                    raise AssertionError("a displayed rectangle repeats a label")
    completions = len(translations)
    raw_pairs = patch_count * completions * (completions - 1)
    support_size = len(colors)
    ledger = MultilevelTranslationLedger(
        m=m,
        length=length,
        q=q,
        degree_scale=degree_scale,
        patches=patch_count,
        completions_per_patch=completions,
        maximum_color_patch_reuse=patch_count,
        color_support_size=support_size,
        raw_offdiagonal_pairs=raw_pairs,
        flat_weighted_offdiagonal_mass=raw_pairs / support_size**2,
        # Put z_m=1/2 and z_c=1/(2*sqrt(L)) on each of the 3L
        # non-anchor colors.  This has l2 norm one, and each color matrix
        # has weight 1/(16 L^(3/2)).
        spiked_weighted_offdiagonal_mass=(
            raw_pairs / (16 * length ** 1.5)
        ),
        maximum_absolute_residual=maximum_residual,
        normalized_residual_cap=maximum_residual / (q * degree_scale),
    )
    if ledger.normalized_residual_cap >= 1:
        raise AssertionError("the literal qD product window failed")
    return ledger
