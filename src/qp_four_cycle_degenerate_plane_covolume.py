"""Exact covolume ledger for a degenerate determinant plane.

If a rank-two common-level plane has a repeated determinant-null direction
``e=r*s^T``, its two primitive normals are the signed color matrix ``K``
and ``adj(e)^T``.  This module records the exact Pluecker content and
covolume formula used to control the height of ``e``.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


Matrix2 = tuple[int, int, int, int]
Pair = tuple[int, int]


def _det(matrix: Matrix2) -> int:
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def _primitive(vector: Pair) -> bool:
    return gcd(abs(vector[0]), abs(vector[1])) == 1


def _multiple(image: Pair, direction: Pair) -> int:
    scalar: int | None = None
    for value, base in zip(image, direction):
        if base:
            if value % base:
                raise ValueError("the image is not an integral multiple")
            candidate = value // base
            if scalar is None:
                scalar = candidate
            elif scalar != candidate:
                raise ValueError("the image coordinates give different multiples")
        elif value:
            raise ValueError("a zero direction coordinate has nonzero image")
    if scalar in (None, 0):
        raise ValueError("the multiple must be nonzero")
    return scalar


@dataclass(frozen=True)
class DegeneratePlaneCovolumeLedger:
    color_determinant: int
    row_gap: int
    column_gap: int
    determinant_gap_defect: int
    pluecker_content: int
    expected_content: int
    wedge_norm_square: int
    expected_wedge_norm_square: int
    saturated_covolume_square_numerator: int
    row_norm_square: int
    column_norm_square: int
    null_matrix_frobenius_norm_square: int
    null_height_below_covolume: bool


def degenerate_plane_covolume_ledger(
    signed_color: Matrix2,
    row_direction: Pair,
    column_direction: Pair,
) -> DegeneratePlaneCovolumeLedger:
    """Audit the exact null-plane covolume identities.

    The direction factors must be primitive and satisfy
    ``r^T K s=0``.  With ``r_perp=(r2,-r1)`` and similarly for ``s``, the
    two gap integers are defined by

    ``K s=eta*r_perp`` and ``K^T r=theta*s_perp``.

    Then ``eta*theta=-det(K)``.  If ``n=adj(r*s^T)^T``, the content of the
    Pluecker vector ``K wedge n`` is ``gcd(eta,theta)`` and

    ``||K wedge n||^2=eta^2||r||^4+theta^2||s||^4``.
    """

    if not _primitive(row_direction) or not _primitive(column_direction):
        raise ValueError("the two direction factors must be primitive")
    k11, k12, k21, k22 = signed_color
    r1, r2 = row_direction
    s1, s2 = column_direction
    determinant = _det(signed_color)
    if determinant == 0:
        raise ValueError("the signed color matrix must be invertible")
    relation = (
        k11 * r1 * s1
        + k12 * r1 * s2
        + k21 * r2 * s1
        + k22 * r2 * s2
    )
    if relation:
        raise ValueError("the rank-one direction does not kill the color")

    row_perp = (r2, -r1)
    column_perp = (s2, -s1)
    ks = (k11 * s1 + k12 * s2, k21 * s1 + k22 * s2)
    ktr = (k11 * r1 + k21 * r2, k12 * r1 + k22 * r2)
    eta = _multiple(ks, row_perp)
    theta = _multiple(ktr, column_perp)

    e = (r1 * s1, r1 * s2, r2 * s1, r2 * s2)
    normal = (e[3], -e[2], -e[1], e[0])
    minors = tuple(
        signed_color[i] * normal[j] - signed_color[j] * normal[i]
        for i in range(4)
        for j in range(i + 1, 4)
    )
    content = 0
    for minor in minors:
        content = gcd(content, abs(minor))
    expected_content = gcd(abs(eta), abs(theta))
    if content != expected_content:
        raise AssertionError("the Pluecker content identity failed")

    rr = r1 * r1 + r2 * r2
    ss = s1 * s1 + s2 * s2
    wedge_square = sum(minor * minor for minor in minors)
    expected_wedge_square = eta * eta * rr * rr + theta * theta * ss * ss
    if wedge_square != expected_wedge_square:
        raise AssertionError("the wedge norm identity failed")
    if eta * theta != -determinant:
        raise AssertionError("the determinant-gap identity failed")

    covolume_square_numerator = wedge_square // (content * content)
    null_norm_square = rr * ss
    return DegeneratePlaneCovolumeLedger(
        color_determinant=determinant,
        row_gap=eta,
        column_gap=theta,
        determinant_gap_defect=eta * theta + determinant,
        pluecker_content=content,
        expected_content=expected_content,
        wedge_norm_square=wedge_square,
        expected_wedge_norm_square=expected_wedge_square,
        saturated_covolume_square_numerator=covolume_square_numerator,
        row_norm_square=rr,
        column_norm_square=ss,
        null_matrix_frobenius_norm_square=null_norm_square,
        null_height_below_covolume=(
            null_norm_square <= covolume_square_numerator
        ),
    )
