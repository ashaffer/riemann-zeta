"""Exact ledgers for the dyadic high-completion tail gate.

The routines in this file are finite combinatorics and rational-exponent
bookkeeping.  They do not assert the open high-completion tail theorem.

For a binary incidence matrix ``B`` between row-pairs and color-pairs, put

    m(y,z) = |N(y) intersect N(z)|.

The second and third factorial codegree kernels give exact singleton-safe
majorants for the dyadic set ``K <= m(y,z) < 2K``.  Their row sums can be
rewritten using common neighborhoods of two or three row-pairs.  The latter
is the point at which the proved K_(3,2) reciprocal-height lemma enters.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import comb, gcd, isqrt
from typing import Sequence


BinaryMatrix = Sequence[Sequence[int]]


@dataclass(frozen=True)
class FactorialTailLedger:
    """Finite high-codegree and anchored factorial-moment data."""

    threshold: int
    codegrees: tuple[tuple[int, ...], ...]
    second_factorial_row_sums: tuple[int, ...]
    third_factorial_row_sums: tuple[int, ...]
    second_high_row_sums: tuple[int, ...]
    third_high_row_sums: tuple[int, ...]
    second_anchor_identity_sums: tuple[int, ...]
    third_anchor_identity_sums: tuple[int, ...]
    high_ordered_pairs: int
    second_majorant_numerator: int
    third_majorant_numerator: int


def _validate_binary(matrix: BinaryMatrix) -> tuple[tuple[int, ...], ...]:
    normalized = tuple(tuple(int(value) for value in row) for row in matrix)
    if not normalized:
        return normalized
    width = len(normalized[0])
    if any(len(row) != width for row in normalized):
        raise ValueError("the incidence matrix must be rectangular")
    if any(value not in (0, 1) for row in normalized for value in row):
        raise ValueError("the incidence matrix must be binary")
    return normalized


def factorial_tail_ledger(
    incidence: BinaryMatrix, threshold: int
) -> FactorialTailLedger:
    """Return exact factorial-codegree identities for one finite graph.

    Color-pairs index columns.  Diagonal color-pairs are omitted everywhere.
    ``second_majorant_numerator`` is

        sum_(y!=z, m(y,z)>=K) binom(m(y,z),2),

    and similarly at level three.  Hence the number of ordered high pairs is
    at most these numerators divided by ``binom(K,2)`` or ``binom(K,3)``.
    """

    if threshold < 2:
        raise ValueError("the factorial threshold must be at least two")
    matrix = _validate_binary(incidence)
    row_count = len(matrix)
    column_count = len(matrix[0]) if row_count else 0
    neighborhoods = [
        {row for row in range(row_count) if matrix[row][column]}
        for column in range(column_count)
    ]
    codegrees = tuple(
        tuple(len(neighborhoods[y] & neighborhoods[z]) for z in range(column_count))
        for y in range(column_count)
    )

    second_rows = tuple(
        sum(comb(codegrees[y][z], 2) for z in range(column_count) if z != y)
        for y in range(column_count)
    )
    third_rows = tuple(
        sum(comb(codegrees[y][z], 3) for z in range(column_count) if z != y)
        for y in range(column_count)
    )
    second_high_rows = tuple(
        sum(
            comb(codegrees[y][z], 2)
            for z in range(column_count)
            if z != y and codegrees[y][z] >= threshold
        )
        for y in range(column_count)
    )
    third_high_rows = tuple(
        sum(
            comb(codegrees[y][z], 3)
            for z in range(column_count)
            if z != y and codegrees[y][z] >= threshold
        )
        for y in range(column_count)
    )

    second_identity: list[int] = []
    third_identity: list[int] = []
    for y in range(column_count):
        rows = sorted(neighborhoods[y])
        second_total = 0
        for pair in combinations(rows, 2):
            common = sum(
                all(matrix[row][column] for row in pair)
                for column in range(column_count)
            )
            second_total += common - 1
        second_identity.append(second_total)

        third_total = 0
        for triple in combinations(rows, 3):
            common = sum(
                all(matrix[row][column] for row in triple)
                for column in range(column_count)
            )
            third_total += common - 1
        third_identity.append(third_total)

    high_pairs = sum(
        y != z and codegrees[y][z] >= threshold
        for y in range(column_count)
        for z in range(column_count)
    )
    second_numerator = sum(
        comb(codegrees[y][z], 2)
        for y in range(column_count)
        for z in range(column_count)
        if y != z and codegrees[y][z] >= threshold
    )
    third_numerator = sum(
        comb(codegrees[y][z], 3)
        for y in range(column_count)
        for z in range(column_count)
        if y != z and codegrees[y][z] >= threshold
    )
    return FactorialTailLedger(
        threshold=threshold,
        codegrees=codegrees,
        second_factorial_row_sums=second_rows,
        third_factorial_row_sums=third_rows,
        second_high_row_sums=second_high_rows,
        third_high_row_sums=third_high_rows,
        second_anchor_identity_sums=tuple(second_identity),
        third_anchor_identity_sums=tuple(third_identity),
        high_ordered_pairs=high_pairs,
        second_majorant_numerator=second_numerator,
        third_majorant_numerator=third_numerator,
    )


@dataclass(frozen=True)
class TailExponentLedger:
    """Power-of-``D`` exponents in the factorial and parabolic gates."""

    multiplicity: Fraction
    reciprocal_height: Fraction
    third_factorial_tail: Fraction
    desired_tail: Fraction
    reciprocal_height_required: Fraction
    occupied_line_count: Fraction
    curvature_tail: Fraction
    curvature_loss: Fraction


def tail_exponent_ledger(
    multiplicity: Fraction,
    reciprocal_height: Fraction,
    occupied_line_count: Fraction,
) -> TailExponentLedger:
    """Return the exact exponent ledger.

    If ``K=D^k`` and the largest anchored reciprocal-height sum is ``D^r``,
    the K_(3,2) reduction gives tail exponent ``1+r-3k``.  The desired one is
    ``1-k``, so precisely ``r<=2k`` is required.

    In a parabolic block with at most ``J=D^j`` occupied lines, the proved
    gap-token and occupied-line estimates give the curvature tail
    ``D^(1+j/2-k)``.  Its excess over ``D/K`` is ``D^(j/2)``; it is sharp
    when ``J=D^o(1)``.
    """

    k = multiplicity
    r = reciprocal_height
    j = occupied_line_count
    return TailExponentLedger(
        multiplicity=k,
        reciprocal_height=r,
        third_factorial_tail=Fraction(1) + r - 3 * k,
        desired_tail=Fraction(1) - k,
        reciprocal_height_required=2 * k,
        occupied_line_count=j,
        curvature_tail=Fraction(1) + j / 2 - k,
        curvature_loss=j / 2,
    )


@dataclass(frozen=True)
class CriticalScatteredLedger:
    """The anisotropic singleton-line endpoint of the current estimates."""

    multiplicity: Fraction
    current_color_mass: Fraction
    required_color_mass: Fraction
    missing_saving: Fraction
    current_completed_mass: Fraction
    target_completed_mass: Fraction
    closed_determinant_range: Fraction
    remaining_determinant_width: Fraction
    remaining_residual_product: Fraction
    formal_high_region_fraction: Fraction
    formal_two_sided_region_fraction: Fraction


def critical_scattered_ledger() -> CriticalScatteredLedger:
    """Return the exact ``D^(1/4)`` gap in the scattered endpoint.

    At the determinant-content endpoint, ``m~D^(5/16)`` while the proved
    uncompleted color mass is ``D^(15/16)``.  The high-tail theorem needs
    ``D/m=D^(11/16)``.  Multiplication by ``m`` changes the same gap from
    completed exponent ``5/4`` to the target exponent one.
    """

    multiplicity = Fraction(5, 16)
    current_mass = Fraction(15, 16)
    required_mass = Fraction(11, 16)
    return CriticalScatteredLedger(
        multiplicity=multiplicity,
        current_color_mass=current_mass,
        required_color_mass=required_mass,
        missing_saving=current_mass - required_mass,
        current_completed_mass=current_mass + multiplicity,
        target_completed_mass=Fraction(1),
        closed_determinant_range=Fraction(1) - multiplicity,
        remaining_determinant_width=multiplicity,
        remaining_residual_product=Fraction(21, 16),
        formal_high_region_fraction=Fraction(17, 64),
        formal_two_sided_region_fraction=Fraction(223, 3072),
    )


@dataclass(frozen=True)
class ResidualCrossLedger:
    """The exact ``e cross f = -det(p,q)*(a cross A)`` identity."""

    column_determinant: int
    first_residual: tuple[int, int, int]
    second_residual: tuple[int, int, int]
    row_cross: tuple[int, int, int]
    residual_cross: tuple[int, int, int]
    defect: tuple[int, int, int]


def _cross(left: Sequence[int], right: Sequence[int]) -> tuple[int, int, int]:
    if len(left) != 3 or len(right) != 3:
        raise ValueError("the cross product requires two triples")
    return (
        int(left[1]) * int(right[2]) - int(left[2]) * int(right[1]),
        int(left[2]) * int(right[0]) - int(left[0]) * int(right[2]),
        int(left[0]) * int(right[1]) - int(left[1]) * int(right[0]),
    )


def residual_cross_ledger(
    a: Sequence[int],
    A: Sequence[int],
    first_column: Sequence[int],
    second_column: Sequence[int],
) -> ResidualCrossLedger:
    """Replay the residual-lattice cross-product identity exactly.

    For color columns ``p=(c_1,d_1)``, ``q=(c_2,d_2)``, put

        e_i=c_1*a_i-d_1*A_i,  f_i=c_2*a_i-d_2*A_i.

    Then ``e cross f = -det(p,q)*(a cross A)``.  Equivalently, the
    residual points ``(e_i,f_i)`` lie in the image lattice of determinant
    ``|det(p,q)|``.
    """

    if len(a) != 3 or len(A) != 3:
        raise ValueError("a and A must be triples")
    if len(first_column) != 2 or len(second_column) != 2:
        raise ValueError("the color columns must be pairs")
    aa = tuple(int(value) for value in a)
    AA = tuple(int(value) for value in A)
    c1, d1 = (int(value) for value in first_column)
    c2, d2 = (int(value) for value in second_column)
    determinant = c1 * d2 - c2 * d1
    first = tuple(c1 * aa[index] - d1 * AA[index] for index in range(3))
    second = tuple(c2 * aa[index] - d2 * AA[index] for index in range(3))
    row_cross = _cross(aa, AA)
    residual_cross = _cross(first, second)
    expected = tuple(-determinant * value for value in row_cross)
    defect = tuple(
        residual_cross[index] - expected[index] for index in range(3)
    )
    return ResidualCrossLedger(
        column_determinant=determinant,
        first_residual=first,  # type: ignore[arg-type]
        second_residual=second,  # type: ignore[arg-type]
        row_cross=row_cross,
        residual_cross=residual_cross,
        defect=defect,  # type: ignore[arg-type]
    )


@dataclass(frozen=True)
class TwoPointResidualLineBound:
    """Lattice-point bound after deleting residual lines with three points."""

    lattice_determinant: int
    first_width: int
    second_width: int
    maximum_line_occupancy: int
    parallel_coset_bound: int
    point_bound: int


def two_point_residual_line_bound(
    lattice_determinant: int,
    first_width: int,
    second_width: int,
    maximum_line_occupancy: int = 2,
) -> TwoPointResidualLineBound:
    """Bound a residual-lattice set in a rectangle.

    Let ``Lambda`` have covolume ``k`` and let a finite subset lie in a
    rectangle of coordinate widths ``E,F``.  After scaling the rectangle to
    a unit square, the lattice covolume is ``delta=k/(E*F)``.  Minkowski
    supplies a primitive vector of scaled sup norm ``O(sqrt(delta))``.
    Its parallel lattice cosets are separated by ``k`` under the determinant
    functional, while that functional has range ``O(sqrt(k*E*F))`` on the
    rectangle.  Hence at most

        O(1+sqrt(E*F/k))

    cosets meet it.  If every affine lattice line contains at most ``T``
    selected points, the displayed point bound follows.  The integer
    constant four in the implementation safely absorbs the strict form of
    Minkowski's theorem and rectangle boundary effects.
    """

    k = abs(int(lattice_determinant))
    if k == 0:
        raise ValueError("the residual lattice must have nonzero determinant")
    if first_width < 0 or second_width < 0:
        raise ValueError("rectangle widths must be nonnegative")
    if maximum_line_occupancy < 1:
        raise ValueError("line occupancy must be positive")
    area = first_width * second_width
    ceiling_ratio = (area + k - 1) // k
    root = isqrt(ceiling_ratio)
    if root * root < ceiling_ratio:
        root += 1
    cosets = 1 + 4 * root
    return TwoPointResidualLineBound(
        lattice_determinant=k,
        first_width=first_width,
        second_width=second_width,
        maximum_line_occupancy=maximum_line_occupancy,
        parallel_coset_bound=cosets,
        point_bound=maximum_line_occupancy * cosets,
    )


@dataclass(frozen=True)
class TwoSidedResidualLedger:
    """Exact row/carrier residual lattices and their bilinear level."""

    color_determinant: int
    level: int
    row_residual: tuple[int, int]
    carrier_residual: tuple[int, int]
    bilinear_level: int
    bilinear_defect: int


def two_sided_residual_ledger(
    colors: Sequence[int], completion: Sequence[int]
) -> TwoSidedResidualLedger:
    """Return ``r=K^T a``, ``s=K b`` and ``r^T adj(K)s=kL``.

    The signed color matrix is

        K=(c11,-c12;-c21,c22).

    Both maps have determinant ``k=det(K)=det(C)``.  In the active carry
    problem their two outputs lie in ``O(D)`` boxes.
    """

    if len(colors) != 4 or len(completion) != 4:
        raise ValueError("colors and completion must have four entries")
    c11, c12, c21, c22 = (int(value) for value in colors)
    a1, a2, b1, b2 = (int(value) for value in completion)
    determinant = c11 * c22 - c12 * c21
    level = (
        c11 * a1 * b1
        + c22 * a2 * b2
        - c12 * a1 * b2
        - c21 * a2 * b1
    )
    row = (c11 * a1 - c21 * a2, -c12 * a1 + c22 * a2)
    carrier = (c11 * b1 - c12 * b2, -c21 * b1 + c22 * b2)
    # adj(K)=(c22,c12;c21,c11) for the signed K above.
    first = c22 * carrier[0] + c12 * carrier[1]
    second = c21 * carrier[0] + c11 * carrier[1]
    bilinear = row[0] * first + row[1] * second
    return TwoSidedResidualLedger(
        color_determinant=determinant,
        level=level,
        row_residual=row,
        carrier_residual=carrier,
        bilinear_level=bilinear,
        bilinear_defect=bilinear - determinant * level,
    )


@dataclass(frozen=True)
class TwoSidedCriticalLedger:
    """Exponent constraints after both residual-line estimates."""

    determinant: Fraction
    multiplicity: Fraction
    row_product_required: Fraction
    carrier_product_required: Fraction
    cross_product_required: Fraction
    fully_balanced_side_required: Fraction


def two_sided_critical_ledger(
    determinant: Fraction, multiplicity: Fraction
) -> TwoSidedCriticalLedger:
    """Return the two-sided residual exponent polytope.

    If ``|k|=D^ell`` and ``K=D^kappa``, two-point residual-line sparsity on
    both sides requires

        e+f, g+h >= ell+2*kappa.

    The active estimate ``|L|~|k|q`` and the bilinear identity force some
    cross product to have exponent at least ``2*ell``.  In a fully balanced
    box of side exponent ``rho``, this gives

        rho >= max(ell, ell/2+kappa).
    """

    ell = determinant
    kappa = multiplicity
    projection = ell + 2 * kappa
    return TwoSidedCriticalLedger(
        determinant=ell,
        multiplicity=kappa,
        row_product_required=projection,
        carrier_product_required=projection,
        cross_product_required=2 * ell,
        fully_balanced_side_required=max(ell, ell / 2 + kappa),
    )


def bilinear_parabola_matching(parameter: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """An integer line-sparse matching on ``r dot s=1``.

    ``r_t=(t,t^2+1)`` and ``s_t=(t^2-t+1,1-t)`` both lie on nondegenerate
    parabolas, while their dot product is one.  This is a finite algebraic
    obstruction to deriving a rich affine line from a bilinear level and
    injective matching alone; it is not an actual-prime carry model.
    """

    t = int(parameter)
    return (t, t * t + 1), (t * t - t + 1, 1 - t)


@dataclass(frozen=True)
class TangentTripleHeightLedger:
    """Reciprocal primitive-height mass of one affine tangent packet."""

    order: int
    triples: int
    reciprocal_height_sum: Fraction
    divisor_majorant: int


def _divisor_count(value: int) -> int:
    return sum(value % divisor == 0 for divisor in range(1, value + 1))


def tangent_triple_height_ledger(order: int) -> TangentTripleHeightLedger:
    """Return the exact reciprocal-height sum for consecutive tangent rows.

    Take row vertices ``x_i=(M+i,M+i+1)``, ``0<=i<L``.  The primitive
    cross-product height of ``i<j<k`` is

        (k-i)/gcd(j-i,k-j).

    Therefore the sum is

        sum_(r,s>=1,r+s<L) (L-r-s)*gcd(r,s)/(r+s),

    which is at most ``L*sum_(n<L) tau(n)=O(L^2 log L)``.  The center ``M``
    cancels exactly.  Thus the coherent ``K=L`` packet lies at the sharp
    ``R_K<=K^2 q^o(1)`` scale of the factorial-triangle gate.
    """

    if order < 3:
        raise ValueError("at least three tangent rows are required")
    total = Fraction(0)
    for first_gap in range(1, order):
        for second_gap in range(1, order - first_gap):
            span = first_gap + second_gap
            translations = order - span
            total += Fraction(
                translations * gcd(first_gap, second_gap), span
            )
    majorant = order * sum(_divisor_count(value) for value in range(1, order))
    return TangentTripleHeightLedger(
        order=order,
        triples=comb(order, 3),
        reciprocal_height_sum=total,
        divisor_majorant=majorant,
    )
