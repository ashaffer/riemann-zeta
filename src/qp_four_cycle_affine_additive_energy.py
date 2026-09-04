"""Exact Aff x Add embedding and the Fourier-fibre obstruction.

For affine carriers ``A_i(t)=a_i+r_i*t`` and
``B_j(t)=b_j+s_j*t``, put ``g_ij=A_i o B_j^{-1}``.  The four cell maps
satisfy an affine-group energy identity.  If
``d_ij=r_i*s_j*c_ij`` and the weighted colors form an additive rectangle,
the tagged maps satisfy the same identity in ``Aff(Q) x Add(Z)``.

Fourier transformation in the additive tag is exact, but it does not turn
arbitrary tag fibres into l2 objects: a single affine-map fibre carrying an
interval of L tags has additive energy (2L^3+L)/3.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


AffineMap = tuple[Fraction, Fraction]  # slope, intercept
Carrier = tuple[int, int]  # intercept, slope


def compose(first: AffineMap, second: AffineMap) -> AffineMap:
    """Return ``first o second``."""

    a, b = first
    c, d = second
    return a * c, a * d + b


def inverse(mapping: AffineMap) -> AffineMap:
    slope, intercept = mapping
    if slope == 0:
        raise ValueError("an affine-group element must have nonzero slope")
    return 1 / slope, -intercept / slope


def cell_map(row: Carrier, column: Carrier) -> AffineMap:
    """Return ``A o B^{-1}`` for two affine carrier functions."""

    row_intercept, row_slope = row
    column_intercept, column_slope = column
    if row_slope == 0 or column_slope == 0:
        raise ValueError("carrier slopes must be nonzero")
    return compose(
        (Fraction(row_slope), Fraction(row_intercept)),
        inverse((Fraction(column_slope), Fraction(column_intercept))),
    )


@dataclass(frozen=True)
class AffineAdditiveEnergyLedger:
    cell_maps: tuple[AffineMap, AffineMap, AffineMap, AffineMap]
    tags: tuple[int, int, int, int]
    first_affine_quotient: AffineMap
    second_affine_quotient: AffineMap
    first_tag_difference: int
    second_tag_difference: int

    @property
    def affine_identity(self) -> bool:
        return self.first_affine_quotient == self.second_affine_quotient

    @property
    def additive_identity(self) -> bool:
        return self.first_tag_difference == self.second_tag_difference


def affine_additive_energy_ledger(
    rows: tuple[Carrier, Carrier],
    columns: tuple[Carrier, Carrier],
    colors: tuple[int, int, int, int],
) -> AffineAdditiveEnergyLedger:
    """Build the four tagged cell maps and audit their energy identity."""

    maps = tuple(
        cell_map(rows[i], columns[j])
        for i, j in ((0, 0), (0, 1), (1, 0), (1, 1))
    )
    r1, r2 = rows[0][1], rows[1][1]
    s1, s2 = columns[0][1], columns[1][1]
    c11, c12, c21, c22 = colors
    tags = (
        r1 * s1 * c11,
        r1 * s2 * c12,
        r2 * s1 * c21,
        r2 * s2 * c22,
    )
    g11, g12, g21, g22 = maps
    first_quotient = compose(inverse(g11), g12)
    second_quotient = compose(inverse(g21), g22)
    ledger = AffineAdditiveEnergyLedger(
        cell_maps=maps,  # type: ignore[arg-type]
        tags=tags,
        first_affine_quotient=first_quotient,
        second_affine_quotient=second_quotient,
        first_tag_difference=tags[1] - tags[0],
        second_tag_difference=tags[3] - tags[2],
    )
    if not ledger.affine_identity:
        raise AssertionError("the carrier cell maps failed their energy identity")
    return ledger


def interval_additive_energy(length: int) -> int:
    """Return ``E^+({1,...,length})=(2L^3+L)/3``."""

    if length < 1:
        raise ValueError("length must be positive")
    return (2 * length**3 + length) // 3
