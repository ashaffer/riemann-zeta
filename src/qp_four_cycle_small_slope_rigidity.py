"""Exact ledgers for small-height primitive parabolic directions.

The mathematical input is elementary.  A primitive pair of slope vectors
annihilating one nonzero-determinant color matrix determines a divisor of
the color determinant.  For a fixed divisor the second slope vector lies
in a very thin symmetric convex body.  When that body's area is below two,
all of its integral points are collinear, so it contains at most two
primitive vectors.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


Pair = tuple[int, int]
Colors = tuple[int, int, int, int]


def _primitive(vector: Pair) -> bool:
    return gcd(abs(vector[0]), abs(vector[1])) == 1


@dataclass(frozen=True)
class PrimitiveSlopeRigidityLedger:
    color_determinant: int
    weighted_relation_defect: int
    determinant_divisor: int
    divisor_remainder: int
    direction_bound: int
    controlling_row_norm_square: int
    area_test_left: int
    area_test_right: int
    rank_one_lattice_certificate: bool


def primitive_slope_rigidity_ledger(
    colors: Colors,
    row_direction: Pair,
    column_direction: Pair,
) -> PrimitiveSlopeRigidityLedger:
    """Return the determinant-divisor and thin-strip certificates.

    Both direction vectors must be primitive.  If ``C=(c_ij)`` and
    ``r^T (c11,-c12;-c21,c22) s=0``, put

    ``T s=(c21*s1-c22*s2, c11*s1-c12*s2)=eta*r``.

    Then ``eta`` is nonzero and divides ``det(C)``.  For fixed ``eta``, all
    possible primitive ``s`` with infinity norm at most ``B`` lie in a
    symmetric convex body of area at most

    ``4*sqrt(2)*abs(eta)*B**2 / max_row_norm(T)``.

    The integer inequality recorded by ``rank_one_lattice_certificate`` is
    exactly the condition that this upper bound is below two.
    """

    if not _primitive(row_direction) or not _primitive(column_direction):
        raise ValueError("both direction vectors must be primitive")
    c11, c12, c21, c22 = colors
    r1, r2 = row_direction
    s1, s2 = column_direction
    determinant = c11 * c22 - c12 * c21
    if determinant == 0:
        raise ValueError("the color determinant must be nonzero")
    defect = (
        c11 * r1 * s1
        - c12 * r1 * s2
        - c21 * r2 * s1
        + c22 * r2 * s2
    )
    if defect:
        raise ValueError("the directions do not annihilate the color matrix")

    first = c21 * s1 - c22 * s2
    second = c11 * s1 - c12 * s2
    eta: int | None = None
    for image_coordinate, direction_coordinate in (
        (first, r1),
        (second, r2),
    ):
        if direction_coordinate:
            if image_coordinate % direction_coordinate:
                raise AssertionError("the image is not an integral slope multiple")
            candidate = image_coordinate // direction_coordinate
            if eta is None:
                eta = candidate
            elif eta != candidate:
                raise AssertionError("the two slope multiples disagree")
        elif image_coordinate:
            raise AssertionError("a zero slope coordinate has nonzero image")
    if eta in (None, 0):
        raise AssertionError("an invertible color matrix has zero slope image")
    if determinant % eta:
        raise AssertionError("the primitive slope gap does not divide det(C)")

    bound = max(abs(r1), abs(r2), abs(s1), abs(s2))
    row_norm_square = max(
        c21 * c21 + c22 * c22,
        c11 * c11 + c12 * c12,
    )
    # 4 sqrt(2) |eta| B^2 / row_norm < 2
    # is equivalent to 8 eta^2 B^4 < row_norm^2.
    area_left = 8 * eta * eta * bound**4
    area_right = row_norm_square
    return PrimitiveSlopeRigidityLedger(
        color_determinant=determinant,
        weighted_relation_defect=defect,
        determinant_divisor=eta,
        divisor_remainder=determinant % eta,
        direction_bound=bound,
        controlling_row_norm_square=row_norm_square,
        area_test_left=area_left,
        area_test_right=area_right,
        rank_one_lattice_certificate=(area_left < area_right),
    )
