"""Exact finite diagnostics for weighted QP completion secants.

The routines in this module do not assert an asymptotic four-cycle bound.
They isolate two positive quartic forms on an actual finite carry core:

``off_diagonal_form``
    ``sum_C m(C)(m(C)-1) prod_ij z[c_ij]``;

``broad_slice_proxy_form``
    ``sum_C (1+D/lambda_3(C)) prod_ij z[c_ij]`` over completed
    colors whose determinant restriction on the first two reduced kernel
    vectors is nondegenerate or identically zero.

The first form is exact.  The second uses the third LLL-basis length (within
a fixed-dimensional factor of the Euclidean third successive minimum) and
that basis to classify the binary restriction, so it is explicitly a finite
proxy for the proposed broad theorem.  In particular, no output of this
module is asymptotic evidence by itself.

The residual-factorization ledger is also exact: on an all-five-distinct
actual slope-block edge it recovers the common carrier by a gcd and records
the six-per-residual projection theorem.  Its ``q=25013`` fixture is a finite
structural obstruction, not an asymptotic counterexample to the slope-block
bound.

``fixed_row_pair_secant_norm_ledger`` replays the exact transposition of the
fixed-secant binary-norm identities to two fixed slope-block row vertices.
The companion exponent ledger records the proved pointwise ``sqrt(D)``
codegree dichotomy, while explicitly leaving cross-row aggregation and the
slope-block theorem open.

``minor_product_kernel_gate_ledger`` records the exact balanced exponents
in the stationary minor ``L2`` reduction.  It is bookkeeping only: the
weighted shifted multiplication-table estimate recorded there remains an
input, not a theorem of this module.

``hsm_spacing_fallback_ledger`` records the proved spacing fallback
``N(delta) << delta*P^4 + P^3``.  Its finite sharpness fixture checks both
the nonzero aligned-center family and the homogeneous gcd family with exact
rational arithmetic.  The fallback retains a full factor ``P=sqrt(D)`` and
therefore does not prove the sharp HSM or slope-block theorem.

``fejer_diagonal_cubic_fallback_ledger`` records the sharper fallback for
the positive diagonal Fejer peak.  Rational-point counting improves its
trivial ``L*P`` incidence bound to ``L*P^(3/7+o(1))``.  Exact rational cube
rays contribute only ``O(L)``, but the remaining ``P^(3/7)`` gap means that
this still does not prove the HSM estimate.

``cubic_reciprocal_endpoint_ledger`` records the sharp one-dimensional
endpoint left after the spacing reduction.  It includes the best audited
unconditional rational-approximation exponent and the elementary
``abc``-quality certificate.  The latter is a hard-limit diagnostic, not an
invocation or proof of the ``abc`` conjecture.

``conditional_abc_closure_audit_ledger`` records the exact boundary of that
diagnostic.  Conditional ``abc`` strengthens the hostile cubic certificate
and, together with the audited Huxley decomposition, improves the positive
diagonal loss, but generic transition, spacing, and fixed-row product
strata remain quality one.  In particular, the ledger does not assert HSM,
the slope-block theorem, or the four-cycle bound under ``abc``.

``fixed_a_transition_energy_audit_ledger`` records the sharper cubic audit
of the quality-one transition.  A target-sized fixed-denominator factorial
energy would close that transition by Cauchy--Schwarz.  Exact pair identities
and three- and six-point determinants give substantial local spacing, but an
explicit abstract incidence array satisfies every one of those constraints
at the full ``P^(5/8)`` Huxley floor.  The required energy estimate therefore
remains an input, not a theorem of this module.

``hsm_stationary_packet_audit_ledger`` separates the exact stationary center
from the signed completed HSM.  A physical zero quotient has primitive
multiplicity at most one, the stationary fan tube locks onto the principal
relation, and its exact center is proportional (hence diagonal on primitive
support).  Rectangular completion nevertheless creates a ``q^(3/11)``
packet-level absolute-value loss and an exact nonprincipal modular alias.
The former is explicitly **not** a lower bound for the signed HSM kernel.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
import math
from typing import Iterable, Mapping, Sequence

import numpy as np

from qp_four_cycle_h_graph_lab import RectangleRecord
from qp_four_cycle_pair_completion import (
    Completion,
    ColorMatrix,
    carrier_product_matrix,
)
from qp_four_cycle_pair_energy_audit import fixed_energy_norm_ledger
from qp_four_cycle_residual_gate import (
    is_pairwise_coprime_prime_power_shell,
)


IntegerVector = tuple[int, int, int, int]


def signed_color_relation(
    colors: Sequence[int], relation: Sequence[int]
) -> int:
    """Return the common-level color relation ``<K_C, relation>``.

    Both inputs use row-major order.  Thus the signs are ``(+,-,-,+)``.
    """

    if len(colors) != 4 or len(relation) != 4:
        raise ValueError("colors and relation must be four-vectors")
    return (
        int(colors[0]) * int(relation[0])
        - int(colors[1]) * int(relation[1])
        - int(colors[2]) * int(relation[2])
        + int(colors[3]) * int(relation[3])
    )


def fixed_energy_pairing_coefficients(
    colors: Sequence[int], energy: Sequence[int]
) -> tuple[int, int]:
    """Return the two determinants in the fixed-``(E,k)`` pairing.

    Fixing ``(c11,c12)`` leaves a two-by-two linear system for
    ``(c21,c22)`` whose determinant is the first returned integer.  Fixing
    the bottom pair gives the second determinant.  If the four colors are
    pairwise coprime, ``det(E) != 0``, and ``max(abs(E)) < min(colors)``,
    neither determinant can vanish on a common-level solution.
    """

    if len(colors) != 4 or len(energy) != 4:
        raise ValueError("colors and energy must be four-vectors")
    c11, c12, c21, c22 = (int(value) for value in colors)
    e11, e12, e21, e22 = (int(value) for value in energy)
    return (
        e22 * c12 - e21 * c11,
        e12 * c22 - e11 * c21,
    )


def _determinant_4(matrix: Sequence[Sequence[int]]) -> int:
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        raise ValueError("expected a four-by-four matrix")
    answer = 0
    for permutation in permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        term = 1
        for row, column in enumerate(permutation):
            term *= int(matrix[row][column])
        answer += -term if inversions % 2 else term
    return answer


def complementary_kernel_projection_pair(
    first_relation: Sequence[int], second_relation: Sequence[int]
) -> tuple[tuple[int, int], tuple[int, int]] | None:
    """Find complementary injective coordinate projections of a kernel.

    The two independent input rows cut out a rational two-plane ``V`` in
    four-space.  A coordinate-pair projection is injective on ``V`` exactly
    when adjoining its two coordinate rows gives a nonsingular four-by-four
    matrix.  The return value is one partition for which both complementary
    projections are injective, or ``None`` when the coordinate matroid has
    a parallel class of size three.
    """

    if len(first_relation) != 4 or len(second_relation) != 4:
        raise ValueError("relations must be four-vectors")
    first = tuple(int(value) for value in first_relation)
    second = tuple(int(value) for value in second_relation)
    coordinate_rows = tuple(
        tuple(int(index == coordinate) for index in range(4))
        for coordinate in range(4)
    )
    if not any(
        _determinant_4((first, second, coordinate_rows[i], coordinate_rows[j]))
        for i in range(4)
        for j in range(i + 1, 4)
    ):
        raise ValueError("relations must be independent")
    for left, right in (
        ((0, 1), (2, 3)),
        ((0, 2), (1, 3)),
        ((0, 3), (1, 2)),
    ):
        left_determinant = _determinant_4(
            (first, second, coordinate_rows[left[0]], coordinate_rows[left[1]])
        )
        right_determinant = _determinant_4(
            (first, second, coordinate_rows[right[0]], coordinate_rows[right[1]])
        )
        if left_determinant and right_determinant:
            return left, right
    return None


def _extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return nonnegative ``g`` and integers ``x,y`` with ``ax+by=g``."""

    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    if a < 0:
        old_s = -old_s
    if b < 0:
        old_t = -old_t
    return old_r, old_s, old_t


def saturated_kernel_basis(normal: Sequence[int]) -> tuple[IntegerVector, ...]:
    """Return a saturated integral basis of ``normal dot x=0``.

    A sequence of two-coordinate Bezout column operations produces a
    unimodular matrix ``U`` with ``normal*U=(gcd(normal),0,0,0)``.  Its last
    three columns are therefore a saturated kernel basis.
    """

    if len(normal) != 4 or not any(normal):
        raise ValueError("normal must be a nonzero four-vector")
    row = [int(value) for value in normal]
    transform = [[int(i == j) for j in range(4)] for i in range(4)]
    for column in range(1, 4):
        first = row[0]
        second = row[column]
        divisor, x_coefficient, y_coefficient = _extended_gcd(first, second)
        if divisor == 0:
            continue
        block = (
            (x_coefficient, -second // divisor),
            (y_coefficient, first // divisor),
        )
        old_row = row.copy()
        row[0] = old_row[0] * block[0][0] + old_row[column] * block[1][0]
        row[column] = (
            old_row[0] * block[0][1] + old_row[column] * block[1][1]
        )
        old_transform = [values.copy() for values in transform]
        for index in range(4):
            transform[index][0] = (
                old_transform[index][0] * block[0][0]
                + old_transform[index][column] * block[1][0]
            )
            transform[index][column] = (
                old_transform[index][0] * block[0][1]
                + old_transform[index][column] * block[1][1]
            )
    if any(row[index] for index in range(1, 4)):
        raise AssertionError("Bezout reduction did not clear the normal")
    basis = tuple(
        tuple(transform[row_index][column] for row_index in range(4))
        for column in range(1, 4)
    )
    if any(sum(int(normal[i]) * vector[i] for i in range(4)) for vector in basis):
        raise AssertionError("a returned vector is not in the kernel")
    return basis  # type: ignore[return-value]


def _nearest_integer(value: Fraction) -> int:
    """Round a rational to a nearest integer (ties away from zero)."""

    if value >= 0:
        return (2 * value.numerator + value.denominator) // (
            2 * value.denominator
        )
    return -_nearest_integer(-value)


def _gram_schmidt(
    basis: Sequence[Sequence[int]],
) -> tuple[list[list[Fraction]], list[Fraction]]:
    dimension = len(basis)
    stars: list[list[Fraction]] = []
    coefficients = [
        [Fraction(0) for _ in range(dimension)] for _ in range(dimension)
    ]
    norms: list[Fraction] = []
    for index, vector in enumerate(basis):
        star = [Fraction(value) for value in vector]
        for previous in range(index):
            numerator = sum(
                Fraction(vector[position]) * stars[previous][position]
                for position in range(len(vector))
            )
            coefficient = numerator / norms[previous]
            coefficients[index][previous] = coefficient
            for position in range(len(vector)):
                star[position] -= coefficient * stars[previous][position]
        norm = sum(value * value for value in star)
        if norm == 0:
            raise ValueError("basis vectors must be independent")
        stars.append(star)
        norms.append(norm)
    return coefficients, norms


def lll_reduce(
    basis: Sequence[Sequence[int]], *, delta: Fraction = Fraction(3, 4)
) -> tuple[IntegerVector, ...]:
    """LLL-reduce three integral row vectors using exact rational arithmetic."""

    reduced = [[int(value) for value in vector] for vector in basis]
    if len(reduced) != 3 or any(len(vector) != 4 for vector in reduced):
        raise ValueError("expected three four-dimensional vectors")
    index = 1
    while index < len(reduced):
        coefficients, _ = _gram_schmidt(reduced)
        for previous in range(index - 1, -1, -1):
            multiple = _nearest_integer(coefficients[index][previous])
            if multiple:
                reduced[index] = [
                    value - multiple * old
                    for value, old in zip(reduced[index], reduced[previous])
                ]
                coefficients, _ = _gram_schmidt(reduced)
        coefficients, norms = _gram_schmidt(reduced)
        mu = coefficients[index][index - 1]
        if norms[index] >= (delta - mu * mu) * norms[index - 1]:
            index += 1
        else:
            reduced[index], reduced[index - 1] = (
                reduced[index - 1],
                reduced[index],
            )
            index = max(1, index - 1)
    reduced.sort(key=lambda vector: sum(value * value for value in vector))
    return tuple(tuple(vector) for vector in reduced)  # type: ignore[return-value]


def _determinant_3(matrix: Sequence[Sequence[int]]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def _rank_increases(
    independent: Sequence[tuple[int, int, int]], candidate: tuple[int, int, int]
) -> bool:
    if not independent:
        return candidate != (0, 0, 0)
    if len(independent) == 1:
        first = independent[0]
        return (
            first[1] * candidate[2] - first[2] * candidate[1],
            first[2] * candidate[0] - first[0] * candidate[2],
            first[0] * candidate[1] - first[1] * candidate[0],
        ) != (0, 0, 0)
    return _determinant_3((independent[0], independent[1], candidate)) != 0


def exact_successive_minima_squares(
    reduced_basis: Sequence[Sequence[int]],
) -> tuple[int, int, int]:
    """Return the exact squared Euclidean successive minima in rank three.

    The maximum reduced-basis length is an a priori third-minimum upper
    bound.  If ``G`` is the basis Gram matrix, then

    ``lambda_min(G) >= det(G)/trace(G)^2``.

    This gives a rigorous finite coefficient box containing every lattice
    vector up to that upper bound.  Greedy independence in increasing norm
    then gives the three exact minima.
    """

    basis = [tuple(int(value) for value in vector) for vector in reduced_basis]
    gram = [
        [sum(left[k] * right[k] for k in range(4)) for right in basis]
        for left in basis
    ]
    determinant = _determinant_3(gram)
    if determinant <= 0:
        raise ValueError("basis Gram matrix must be positive definite")
    trace = sum(gram[index][index] for index in range(3))
    radius_square = max(gram[index][index] for index in range(3))
    coefficient_square = radius_square * trace * trace // determinant + 1
    bound = math.isqrt(coefficient_square) + 2
    candidates: list[tuple[int, tuple[int, int, int]]] = []
    for x in range(-bound, bound + 1):
        for y in range(-bound, bound + 1):
            for z in range(-bound, bound + 1):
                coefficient = (x, y, z)
                if coefficient == (0, 0, 0):
                    continue
                norm_square = sum(
                    coefficient[i] * gram[i][j] * coefficient[j]
                    for i in range(3)
                    for j in range(3)
                )
                if norm_square <= radius_square:
                    candidates.append((norm_square, coefficient))
    candidates.sort(key=lambda item: item[0])
    independent: list[tuple[int, int, int]] = []
    minima: list[int] = []
    for norm_square, coefficient in candidates:
        if _rank_increases(independent, coefficient):
            independent.append(coefficient)
            minima.append(norm_square)
            if len(minima) == 3:
                break
    if len(minima) != 3:
        raise AssertionError("enumeration missed a full independent set")
    return tuple(minima)  # type: ignore[return-value]


def _matrix_determinant(vector: Sequence[int]) -> int:
    return vector[0] * vector[3] - vector[1] * vector[2]


def _determinant_polar(left: Sequence[int], right: Sequence[int]) -> int:
    return (
        left[0] * right[3]
        + right[0] * left[3]
        - left[1] * right[2]
        - right[1] * left[2]
    )


@dataclass(frozen=True)
class TernaryQuadricDiscriminantLedger:
    """Exact polar discriminants of the common-level determinant quadric."""

    color_determinant: int
    common_level: int
    restricted_polar_discriminant: int
    projective_polar_discriminant: int


@dataclass(frozen=True)
class SecantTriangleLedger:
    """Exact Pluecker and dual-conic invariants of three completions."""

    common_level: int
    energies: tuple[IntegerVector, IntegerVector, IntegerVector]
    energy_cocycle: IntegerVector
    row_pluecker: tuple[int, int, int]
    column_pluecker: tuple[int, int, int]
    energy_determinants: tuple[int, int, int]
    homogeneous_normal: IntegerVector
    normal_content: int
    normal_determinant: int
    factorized_normal_determinant: int
    pencil_discriminant: int
    carrier_line_quadratics: tuple[int, int, int]
    carrier_collinear: bool


@dataclass(frozen=True)
class FourCompletionVolumeLedger:
    """Exact Khatri--Rao and common-level volume invariants."""

    common_level: int
    row_pluecker: tuple[int, int, int, int, int, int]
    column_pluecker: tuple[int, int, int, int, int, int]
    product_volume: int
    khatri_rao_volume: int
    secant_cofactor: IntegerVector
    cofactor_content: int
    affine_volume_index: int
    common_level_volume: int
    affine_rank_three: bool


@dataclass(frozen=True)
class FareyVolumePlaneBarrierLedger:
    """A split-quadric matching spread over many exact volume planes."""

    colors: ColorMatrix
    anchors: tuple[Completion, Completion, Completion]
    completions: tuple[Completion, ...]
    volume_indices: tuple[int, ...]


def secant_triangle_ledger(
    colors: Sequence[int], completions: Sequence[Completion]
) -> SecantTriangleLedger:
    """Return exact invariants of one coherent common-level triangle.

    The three product matrices must be distinct and have invertible pairwise
    secants.  Their cofactor normal ``N`` obeys the scale-sensitive identity
    ``det(N)=-prod det(M_i-M_j)`` over the three cyclic sides.  This routine
    is finite algebra and makes no aggregation claim.
    """

    if len(colors) != 4 or len(completions) != 3:
        raise ValueError("four colors and three completions are required")
    color_tuple = tuple(int(value) for value in colors)
    completion_tuple = tuple(
        tuple(int(value) for value in completion) for completion in completions
    )
    if len(set(completion_tuple)) != 3:
        raise ValueError("the completions must be distinct")
    products = tuple(
        carrier_product_matrix(completion) for completion in completion_tuple
    )
    levels = tuple(
        signed_color_relation(color_tuple, product) for product in products
    )
    if len(set(levels)) != 1:
        raise ValueError("the completions must have one common level")

    cyclic_pairs = ((0, 1), (1, 2), (2, 0))
    energies = tuple(
        tuple(
            products[i][position] - products[j][position]
            for position in range(4)
        )
        for i, j in cyclic_pairs
    )
    energy_determinants = tuple(
        _matrix_determinant(energy) for energy in energies
    )
    if any(value == 0 for value in energy_determinants):
        raise ValueError("the pairwise secants must be invertible")
    row_pluecker = tuple(
        completion_tuple[i][0] * completion_tuple[j][1]
        - completion_tuple[i][1] * completion_tuple[j][0]
        for i, j in cyclic_pairs
    )
    column_pluecker = tuple(
        completion_tuple[i][2] * completion_tuple[j][3]
        - completion_tuple[i][3] * completion_tuple[j][2]
        for i, j in cyclic_pairs
    )
    if any(
        energy_determinants[index]
        != -row_pluecker[index] * column_pluecker[index]
        for index in range(3)
    ):
        raise AssertionError("secant determinant factorization failed")

    normal_values = []
    for omitted in range(4):
        minor = tuple(
            tuple(
                product[index] for index in range(4) if index != omitted
            )
            for product in products
        )
        normal_values.append(((-1) ** omitted) * _determinant_3(minor))
    homogeneous_normal = tuple(normal_values)
    if not any(homogeneous_normal):
        raise AssertionError("invertible secants produced a dependent triangle")
    if any(
        sum(
            normal * value
            for normal, value in zip(homogeneous_normal, product)
        )
        for product in products
    ):
        raise AssertionError("triangle cofactor normal failed")
    normal_determinant = _matrix_determinant(homogeneous_normal)
    factorized_normal_determinant = -math.prod(energy_determinants)
    if normal_determinant != factorized_normal_determinant:
        raise AssertionError("triangle normal determinant identity failed")

    signed_color = (
        color_tuple[0],
        -color_tuple[1],
        -color_tuple[2],
        color_tuple[3],
    )
    mixed_polar = _determinant_polar(homogeneous_normal, signed_color)
    pencil_discriminant = (
        mixed_polar * mixed_polar
        - 4
        * normal_determinant
        * _matrix_determinant(signed_color)
    )
    line_quadratics = []
    for i, j in cyclic_pairs:
        difference = tuple(
            completion_tuple[j][position] - completion_tuple[i][position]
            for position in range(4)
        )
        da1, da2, db1, db2 = difference
        line_quadratics.append(
            signed_color_relation(
                color_tuple,
                (da1 * db1, da1 * db2, da2 * db1, da2 * db2),
            )
        )
    first_difference = tuple(
        completion_tuple[1][position] - completion_tuple[0][position]
        for position in range(4)
    )
    second_difference = tuple(
        completion_tuple[2][position] - completion_tuple[0][position]
        for position in range(4)
    )
    carrier_collinear = all(
        first_difference[i] * second_difference[j]
        == first_difference[j] * second_difference[i]
        for i in range(4)
        for j in range(4)
    )
    energy_cocycle = tuple(
        sum(energy[position] for energy in energies)
        for position in range(4)
    )
    return SecantTriangleLedger(
        common_level=levels[0],
        energies=energies,  # type: ignore[arg-type]
        energy_cocycle=energy_cocycle,  # type: ignore[arg-type]
        row_pluecker=row_pluecker,  # type: ignore[arg-type]
        column_pluecker=column_pluecker,  # type: ignore[arg-type]
        energy_determinants=energy_determinants,  # type: ignore[arg-type]
        homogeneous_normal=homogeneous_normal,  # type: ignore[arg-type]
        normal_content=math.gcd(
            *(abs(value) for value in homogeneous_normal)
        ),
        normal_determinant=normal_determinant,
        factorized_normal_determinant=factorized_normal_determinant,
        pencil_discriminant=pencil_discriminant,
        carrier_line_quadratics=tuple(line_quadratics),  # type: ignore[arg-type]
        carrier_collinear=carrier_collinear,
    )


def four_completion_volume_ledger(
    colors: Sequence[int], completions: Sequence[Completion]
) -> FourCompletionVolumeLedger:
    """Return the exact affine-volume ledger for four common-level points.

    If ``E_i=M_i-M_0`` for ``i=1,2,3``, their integral cofactor normal is
    ``t*K_C`` because the signed color normal is primitive.  Consequently
    the four-product determinant is exactly ``t*L``.  The same determinant
    is the difference of two Khatri--Rao Pluecker monomials.
    """

    if len(colors) != 4 or len(completions) != 4:
        raise ValueError("four colors and four completions are required")
    color_tuple = tuple(int(value) for value in colors)
    completion_tuple = tuple(
        tuple(int(value) for value in completion) for completion in completions
    )
    if len(set(completion_tuple)) != 4:
        raise ValueError("the completions must be distinct")
    signed_color = (
        color_tuple[0],
        -color_tuple[1],
        -color_tuple[2],
        color_tuple[3],
    )
    if math.gcd(*(abs(value) for value in signed_color)) != 1:
        raise ValueError("the signed color normal must be primitive")
    products = tuple(
        carrier_product_matrix(completion) for completion in completion_tuple
    )
    levels = tuple(
        signed_color_relation(color_tuple, product) for product in products
    )
    if len(set(levels)) != 1:
        raise ValueError("the completions must have one common level")

    pair_order = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
    row_by_pair = {
        pair: completion_tuple[pair[0]][0] * completion_tuple[pair[1]][1]
        - completion_tuple[pair[0]][1] * completion_tuple[pair[1]][0]
        for pair in pair_order
    }
    column_by_pair = {
        pair: completion_tuple[pair[0]][2] * completion_tuple[pair[1]][3]
        - completion_tuple[pair[0]][3] * completion_tuple[pair[1]][2]
        for pair in pair_order
    }
    product_volume = _determinant_4(products)
    khatri_rao_volume = (
        row_by_pair[0, 2]
        * row_by_pair[1, 3]
        * column_by_pair[0, 1]
        * column_by_pair[2, 3]
        - row_by_pair[0, 1]
        * row_by_pair[2, 3]
        * column_by_pair[0, 2]
        * column_by_pair[1, 3]
    )
    if product_volume != khatri_rao_volume:
        raise AssertionError("Khatri--Rao determinant identity failed")

    differences = tuple(
        tuple(products[i][position] - products[0][position] for position in range(4))
        for i in range(1, 4)
    )
    cofactor_values = []
    for omitted in range(4):
        minor = tuple(
            tuple(
                difference[index]
                for index in range(4)
                if index != omitted
            )
            for difference in differences
        )
        cofactor_values.append(((-1) ** omitted) * _determinant_3(minor))
    secant_cofactor = tuple(cofactor_values)
    affine_rank_three = any(secant_cofactor)
    if affine_rank_three:
        if secant_cofactor[0] % signed_color[0]:
            raise AssertionError("common-level cofactor is not an integral color multiple")
        affine_volume_index = secant_cofactor[0] // signed_color[0]
        if any(
            secant_cofactor[index]
            != affine_volume_index * signed_color[index]
            for index in range(4)
        ):
            raise AssertionError("common-level cofactor is not parallel to the color normal")
    else:
        affine_volume_index = 0
    cofactor_content = math.gcd(*(abs(value) for value in secant_cofactor))
    if cofactor_content != abs(affine_volume_index):
        raise AssertionError("primitive color did not recover the affine volume index")
    common_level_volume = affine_volume_index * levels[0]
    if product_volume != common_level_volume:
        raise AssertionError("common-level volume quantization failed")
    return FourCompletionVolumeLedger(
        common_level=levels[0],
        row_pluecker=tuple(row_by_pair[pair] for pair in pair_order),  # type: ignore[arg-type]
        column_pluecker=tuple(column_by_pair[pair] for pair in pair_order),  # type: ignore[arg-type]
        product_volume=product_volume,
        khatri_rao_volume=khatri_rao_volume,
        secant_cofactor=secant_cofactor,  # type: ignore[arg-type]
        cofactor_content=cofactor_content,
        affine_volume_index=affine_volume_index,
        common_level_volume=common_level_volume,
        affine_rank_three=affine_rank_three,
    )


def ternary_quadric_discriminant_ledger(
    colors: Sequence[int], product_matrix: Sequence[int]
) -> TernaryQuadricDiscriminantLedger:
    """Replay ``disc(det|Lambda_C)=2 det(C)`` and the affine ``L^2`` identity.

    ``product_matrix`` is a row-major rank-one matrix on the common level.
    The color normal must be primitive, as it is in the all-distinct actual
    prime-power sector.  Discriminants use the integral polar form of the
    determinant, avoiding convention-dependent powers of two.
    """

    if len(colors) != 4 or len(product_matrix) != 4:
        raise ValueError("colors and product_matrix must be four-vectors")
    color_tuple = tuple(int(value) for value in colors)
    product = tuple(int(value) for value in product_matrix)
    normal = (
        color_tuple[0],
        -color_tuple[1],
        -color_tuple[2],
        color_tuple[3],
    )
    if math.gcd(*normal) != 1:
        raise ValueError("the color normal must be primitive")
    if _matrix_determinant(product) != 0:
        raise ValueError("product_matrix must have rank one")
    basis = saturated_kernel_basis(normal)
    restricted_gram = tuple(
        tuple(_determinant_polar(left, right) for right in basis)
        for left in basis
    )
    augmented = (*basis, product)
    projective_gram = tuple(
        tuple(_determinant_polar(left, right) for right in augmented)
        for left in augmented
    )
    color_determinant = (
        color_tuple[0] * color_tuple[3]
        - color_tuple[1] * color_tuple[2]
    )
    common_level = signed_color_relation(color_tuple, product)
    return TernaryQuadricDiscriminantLedger(
        color_determinant=color_determinant,
        common_level=common_level,
        restricted_polar_discriminant=_determinant_3(restricted_gram),
        projective_polar_discriminant=_determinant_4(projective_gram),
    )


def _alternate_farey_neighbors(
    order: int,
) -> tuple[tuple[int, int, int, int], ...]:
    """Return disjoint consecutive pairs ``a/c < b/d`` of Farey fractions."""

    if order < 2:
        raise ValueError("order must be at least two")
    fractions = sorted(
        {
            Fraction(numerator, denominator)
            for denominator in range(1, order + 1)
            for numerator in range(1, denominator)
            if math.gcd(numerator, denominator) == 1
        }
    )
    neighbors = []
    for index in range(0, len(fractions) - 1, 2):
        left = fractions[index]
        right = fractions[index + 1]
        a, c = left.numerator, left.denominator
        b, d = right.numerator, right.denominator
        if b * c - a * d != 1:
            raise AssertionError("the selected fractions are not Farey neighbors")
        neighbors.append((a, c, b, d))
    return tuple(neighbors)


def farey_split_quadric_matching(order: int) -> tuple[IntegerVector, ...]:
    """Return a large ruling-free matching on one split integral quadric.

    Alternate consecutive positive fractions in the Farey sequence.  If
    ``a/c < b/d`` are consecutive, ``ad-cb=-1``.  Thus
    ``P=(a,c)^T(b,d)`` is rank one and has fixed symplectic level
    ``P12-P21=-1``.  Disjoint endpoints make every returned difference
    invertible.  This is a geometry-only barrier, not an actual
    prime-power/product-window construction.
    """

    products: list[IntegerVector] = []
    for a, c, b, d in _alternate_farey_neighbors(order):
        products.append((a * b, a * d, c * b, c * d))
    return tuple(products)


def farey_volume_plane_barrier(order: int) -> FareyVolumePlaneBarrierLedger:
    """Return the exact many-volume-plane obstruction from one Farey matching.

    The base matrices ``(a,c)^T(-d,b)`` have determinant zero and trace one.
    Right multiplication by ``K^{-T}``, where

    ``K=((64,-71),(-73,81))``,

    changes the common signed color normal to ``K`` while preserving integral
    rank, four-dimensional volume, and invertibility of secants.  The color
    tuple ``(64,71,73,81)`` consists of four distinct pairwise-coprime prime
    powers.  The carriers are not shell prime powers, so this remains an
    integer/algebraic barrier rather than an actual-node construction.
    """

    colors: ColorMatrix = (64, 71, 73, 81)
    inverse_normal = ((81, 71), (73, 64))

    def transform_column(left: int, right: int) -> tuple[int, int]:
        return (
            inverse_normal[0][0] * left + inverse_normal[0][1] * right,
            inverse_normal[1][0] * left + inverse_normal[1][1] * right,
        )

    anchors_list = []
    for parameter in (1, 2, -1):
        transformed = transform_column(2 // parameter, 1)
        anchors_list.append((parameter, -1, *transformed))
    anchors = tuple(anchors_list)

    completions = []
    volume_indices = []
    anchor_products = tuple(carrier_product_matrix(anchor) for anchor in anchors)
    for a, c, b, d in _alternate_farey_neighbors(order):
        transformed = transform_column(-d, b)
        completion = (a, c, *transformed)
        product = carrier_product_matrix(completion)
        if any(
            _matrix_determinant(
                tuple(x - y for x, y in zip(product, anchor_product))
            )
            == 0
            for anchor_product in anchor_products
        ):
            # Only finitely many Farey endpoints meet an anchor ruling.
            continue
        completions.append(completion)
        volume_indices.append(6 * (1 + b * c))
    return FareyVolumePlaneBarrierLedger(
        colors=colors,
        anchors=anchors,  # type: ignore[arg-type]
        completions=tuple(completions),
        volume_indices=tuple(volume_indices),
    )


def symmetric_tangent_cell_residual(
    modulus: int, center: int, translation: int
) -> int:
    """Return the literal residual of the symmetric tangent cell.

    The top-left multilevel cell is
    ``(center+translation, center-translation, center)``.  For an odd
    project modulus the baseline ``2*center`` cannot equal ``modulus``;
    at ``D=o(modulus)`` this exact residual is therefore outside the active
    window for all ``translation^2=O(D)``.
    """

    q = int(modulus)
    m = int(center)
    t = int(translation)
    return 8 * (m + t) * (m - t) * m - q**3


def critical_covolume_anchor_factors(parameter: int) -> tuple[int, int, int]:
    """Return the two factors and gcd of the critical integer anchor.

    In the critical covolume model ``c11=(N^2+1)X``.  The returned gcd is
    exactly ``gcd(N+1,2)``, which prevents this anchor from being a prime
    power for every ``N>=2``.
    """

    parameter = int(parameter)
    if parameter < 2:
        raise ValueError("parameter must be at least two")
    first = parameter * parameter + 1
    second = first * (2 * parameter**29) - 1 - parameter**13
    return first, second, math.gcd(first, second)


@dataclass(frozen=True)
class KernelMinimaLedger:
    reduced_basis: tuple[IntegerVector, IntegerVector, IntegerVector]
    minima_squares: tuple[int, int, int]
    minima_exact: bool
    binary_discriminant: int
    binary_identically_zero: bool

    @property
    def broad(self) -> bool:
        return self.binary_discriminant != 0 or self.binary_identically_zero

    @property
    def third_minimum(self) -> float:
        return math.sqrt(self.minima_squares[2])


def kernel_minima_ledger(
    colors: ColorMatrix, *, exact_minima: bool = True
) -> KernelMinimaLedger:
    """Compute kernel lengths and the reduced first-plane determinant type.

    If ``exact_minima`` is false, ``minima_squares`` are the ordered squared
    lengths of the LLL basis.  They are fixed-dimensional proxies for the
    successive minima and make large finite scans substantially faster.
    """

    normal = (colors[0], -colors[1], -colors[2], colors[3])
    reduced = lll_reduce(saturated_kernel_basis(normal))
    if exact_minima:
        minima = exact_successive_minima_squares(reduced)
    else:
        minima = tuple(
            sum(value * value for value in vector) for vector in reduced
        )
    first, second, _ = reduced
    first_det = _matrix_determinant(first)
    second_det = _matrix_determinant(second)
    polar = _determinant_polar(first, second)
    discriminant = polar * polar - 4 * first_det * second_det
    identically_zero = first_det == second_det == polar == 0
    return KernelMinimaLedger(
        reduced_basis=reduced,  # type: ignore[arg-type]
        minima_squares=minima,
        minima_exact=exact_minima,
        binary_discriminant=discriminant,
        binary_identically_zero=identically_zero,
    )


@dataclass(frozen=True)
class PositiveQuarticForm:
    """A sparse positive form ``sum coefficient*prod z[index]``."""

    dimension: int
    indices: np.ndarray
    coefficients: np.ndarray

    def value_and_gradient(
        self, vector: Sequence[float] | np.ndarray
    ) -> tuple[float, np.ndarray]:
        values = np.asarray(vector, dtype=float)
        if values.shape != (self.dimension,):
            raise ValueError("vector has the wrong dimension")
        if self.indices.size == 0:
            return 0.0, np.zeros(self.dimension, dtype=float)
        selected = values[self.indices]
        products = np.prod(selected, axis=1)
        value = float(np.dot(self.coefficients, products))
        gradient = np.zeros(self.dimension, dtype=float)
        for position in range(4):
            other = np.prod(np.delete(selected, position, axis=1), axis=1)
            np.add.at(
                gradient,
                self.indices[:, position],
                self.coefficients * other,
            )
        return value, gradient

    def flattening_schur_bound(self, pairing: tuple[tuple[int, int], tuple[int, int]]) -> float:
        """Return an exact-data Schur upper bound for one pair flattening."""

        left_positions, right_positions = pairing
        row_sums: dict[tuple[int, int], float] = {}
        column_sums: dict[tuple[int, int], float] = {}
        cells: dict[tuple[tuple[int, int], tuple[int, int]], float] = {}
        for indices, coefficient in zip(self.indices, self.coefficients):
            left = (int(indices[left_positions[0]]), int(indices[left_positions[1]]))
            right = (
                int(indices[right_positions[0]]),
                int(indices[right_positions[1]]),
            )
            cells[left, right] = cells.get((left, right), 0.0) + float(coefficient)
        for (left, right), coefficient in cells.items():
            row_sums[left] = row_sums.get(left, 0.0) + coefficient
            column_sums[right] = column_sums.get(right, 0.0) + coefficient
        return math.sqrt(
            max(row_sums.values(), default=0.0)
            * max(column_sums.values(), default=0.0)
        )

    def best_flattening_schur_bound(self) -> float:
        return min(
            self.flattening_schur_bound(pairing)
            for pairing in (
                ((0, 1), (2, 3)),
                ((0, 2), (1, 3)),
                ((0, 3), (1, 2)),
            )
        )


def _form_from_terms(
    values: Sequence[int], terms: Iterable[tuple[ColorMatrix, float]]
) -> PositiveQuarticForm:
    lookup = {int(value): index for index, value in enumerate(values)}
    index_rows: list[tuple[int, int, int, int]] = []
    coefficients: list[float] = []
    for colors, coefficient in terms:
        if coefficient <= 0:
            continue
        index_rows.append(tuple(lookup[int(color)] for color in colors))
        coefficients.append(float(coefficient))
    indices = np.asarray(index_rows, dtype=np.int64)
    if not index_rows:
        indices = np.empty((0, 4), dtype=np.int64)
    return PositiveQuarticForm(
        dimension=len(values),
        indices=indices,
        coefficients=np.asarray(coefficients, dtype=float),
    )


def completion_groups_from_generic_rectangles(
    rectangles: Iterable[RectangleRecord],
) -> dict[ColorMatrix, tuple[Completion, ...]]:
    """Group only rectangles with eight distinct displayed nodes."""

    groups: dict[ColorMatrix, list[Completion]] = {}
    for rectangle in rectangles:
        if rectangle.distinct_node_count != 8:
            continue
        groups.setdefault(rectangle.colors, []).append(
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


def off_diagonal_form(
    values: Sequence[int], groups: Mapping[ColorMatrix, Sequence[Completion]]
) -> PositiveQuarticForm:
    """Build the exact ordered off-diagonal completion-pair form."""

    return _form_from_terms(
        values,
        (
            (colors, float(len(completions) * (len(completions) - 1)))
            for colors, completions in groups.items()
        ),
    )


def anchor_completion_loads(
    groups: Mapping[ColorMatrix, Sequence[Completion]],
) -> dict[int, int]:
    """Return the direct-completion load of every color occurrence.

    A group with ``m`` completions contributes ``m`` to each of its four
    color positions.  Thus repeated colors are counted with their occurrence
    multiplicity.  In the all-distinct sector the maximum returned load is
    the deliberately overstrong AM--GM sufficient condition discussed in
    Section 2E of the companion report.
    """

    loads: dict[int, int] = {}
    for colors, completions in groups.items():
        multiplicity = len(completions)
        for color in colors:
            value = int(color)
            loads[value] = loads.get(value, 0) + multiplicity
    return loads


@dataclass(frozen=True)
class CommonCarrierIncidenceLedger:
    """Finite row-pair/color-pair incidence underlying direct completion.

    A left vertex is an ordered row pair ``(a1,a2)``.  A right vertex is an
    ordered vertical color pair ``(c1,c2)``.  Pair uniqueness makes the
    common carrier on one incidence edge unique.  The Gram entry between the
    two vertical color pairs of a matrix is therefore its completion count
    when the supplied groups are an exhaustive core.
    """

    left_vertices: tuple[tuple[int, int], ...]
    right_vertices: tuple[tuple[int, int], ...]
    carriers: tuple[tuple[int, int, int], ...]
    matrix: np.ndarray
    edge_count: int
    maximum_left_degree: int
    maximum_right_degree: int
    operator_norm: float


@dataclass(frozen=True)
class ProjectiveCommonNeighborLedger:
    """Exact determinant identities for two incidences sharing one side.

    The two left vertices are ``(a1,a2)`` and ``(a1',a2')`` and the shared
    right vertex is ``(c1,c2)``.  Put ``v=a2*c2-a1*c1``.  Then

    ``c2*det(left,left') = a1*v' - a1'*v`` and
    ``c1*det(left,left') = a2*v' - a2'*v``.

    These identities are the projective localization behind the slope-bin
    restricted-type reduction.  No asymptotic estimate is asserted here.
    """

    first_shift: int
    second_shift: int
    left_determinant: int
    first_identity_left: int
    first_identity_right: int
    second_identity_left: int
    second_identity_right: int


@dataclass(frozen=True)
class PrimitiveSlopeModularLift:
    """One primitive vector reconstructed from its reference determinant."""

    reference: tuple[int, int]
    determinant_offset: int
    first_coordinate_residue: int
    vector: tuple[int, int] | None


def primitive_slope_modular_lift(
    reference: tuple[int, int],
    determinant_offset: int,
    shell_lower: int,
    shell_upper: int,
) -> PrimitiveSlopeModularLift:
    """Replay the exact one-lift parametrization of a primitive slope bin.

    For ``reference=(p,r)`` and ``x=(x1,x2)``, the convention is
    ``h=det(reference,x)=p*x2-r*x1``.  Hence
    ``x1=-r^{-1}h (mod p)``.  When the shell interval has length below
    ``p``, it contains at most one representative of this residue class.
    The routine returns that vector when its second coordinate is also in
    the shell, and otherwise returns ``None``.
    """

    p, r = (int(value) for value in reference)
    h = int(determinant_offset)
    lower = int(shell_lower)
    upper = int(shell_upper)
    if min(p, r, lower) <= 0 or upper < lower:
        raise ValueError("reference and shell must be positive")
    if math.gcd(p, r) != 1:
        raise ValueError("reference must be primitive")
    if upper - lower >= p:
        raise ValueError("shell interval must be shorter than the modulus")
    residue = (-pow(r, -1, p) * h) % p
    first = residue + ((lower - residue + p - 1) // p) * p
    vector: tuple[int, int] | None = None
    if first <= upper:
        numerator = r * first + h
        if numerator % p:
            raise AssertionError("modular lift failed its divisibility test")
        second = numerator // p
        if lower <= second <= upper:
            vector = (first, second)
            if p * second - r * first != h:
                raise AssertionError("modular lift failed its determinant test")
    return PrimitiveSlopeModularLift(
        reference=(p, r),
        determinant_offset=h,
        first_coordinate_residue=residue,
        vector=vector,
    )


@dataclass(frozen=True)
class SlopeBlockRandomScaleLedger:
    """Exact exponent bookkeeping for the random slope-block heuristic."""

    degree_exponent_in_q: Fraction
    raw_pair_exponent_in_q: Fraction
    carrier_density_exponent_in_q: Fraction
    expected_edge_exponent_in_q: Fraction
    expected_edge_exponent_in_degree: Fraction
    margin_to_degree_exponent: Fraction


def slope_block_random_scale_ledger() -> SlopeBlockRandomScaleLedger:
    """Return ``D^2*(D/q)=D^(15/16)`` at ``D=q^(16/33)`` exactly."""

    degree = Fraction(16, 33)
    raw_pairs = 2 * degree
    carrier_density = degree - 1
    expected = raw_pairs + carrier_density
    expected_in_degree = expected / degree
    return SlopeBlockRandomScaleLedger(
        degree_exponent_in_q=degree,
        raw_pair_exponent_in_q=raw_pairs,
        carrier_density_exponent_in_q=carrier_density,
        expected_edge_exponent_in_q=expected,
        expected_edge_exponent_in_degree=expected_in_degree,
        margin_to_degree_exponent=1 - expected_in_degree,
    )


@dataclass(frozen=True)
class SlopeBlockFourierGateLedger:
    """Exact exponent ledger for the Selberg reciprocal-sum gate.

    If ``Delta=D/q`` and ``H=Delta^{-1}``, a degree-``H`` Selberg
    majorant reduces one slope-block edge count to

    ``Delta*D**2 + Delta*sum_(1<=ell<=H) |S_ell|``.

    Hence the sharp missing Fourier statement is an ``L1`` sum of size
    ``q`` (average size ``D``).  A Cauchy--Schwarz proof would need a
    weighted second moment of size ``H*D**2``; its diagonal already has
    precisely that scale when both block projections have size ``D``.
    The coherent tangent modes recorded below can in fact make the full
    second moment larger by a factor ``D`` while retaining sharp ``L1``
    mass.
    """

    degree_exponent_in_q: Fraction
    carrier_window_exponent_in_q: Fraction
    selberg_degree_exponent_in_q: Fraction
    zero_mode_exponent_in_q: Fraction
    target_l1_exponent_in_q: Fraction
    target_average_exponent_in_q: Fraction
    target_second_moment_exponent_in_q: Fraction
    target_second_moment_exponent_in_degree: Fraction


def slope_block_fourier_gate_ledger() -> SlopeBlockFourierGateLedger:
    """Return the exact active powers in the Selberg/Fourier reduction."""

    degree = Fraction(16, 33)
    carrier_window = degree - 1
    selberg_degree = 1 - degree
    zero_mode = 3 * degree - 1
    target_l1 = Fraction(1)
    target_average = target_l1 - selberg_degree
    target_second_moment = selberg_degree + 2 * degree
    return SlopeBlockFourierGateLedger(
        degree_exponent_in_q=degree,
        carrier_window_exponent_in_q=carrier_window,
        selberg_degree_exponent_in_q=selberg_degree,
        zero_mode_exponent_in_q=zero_mode,
        target_l1_exponent_in_q=target_l1,
        target_average_exponent_in_q=target_average,
        target_second_moment_exponent_in_q=target_second_moment,
        target_second_moment_exponent_in_degree=(
            target_second_moment / degree
        ),
    )


@dataclass(frozen=True)
class MinorProductKernelGateLedger:
    """Exact powers in the balanced stationary-minor product kernel.

    After the common ``SL_2`` B-process, smooth Mellin separation makes an
    interior stationary term a superposition of separable weights
    ``u(j)v(k)``.  Grouping ``x=jk`` makes the product diagonal contribute
    exactly ``qD``.  The missing off-diagonal statement is a weighted
    shifted multiplication-table estimate.

    The ``classical_*`` fields record an optimistic comparison only: assume
    all zero-frequency main terms vanish and assign the level-one
    shifted-divisor benchmark ``X^(2/3)`` the natural coefficient-density
    factor ``D``.  Even then, summing the ``B0`` coherent short shifts loses
    ``q^(2/11)``.  No level-uniform spectral theorem for the actual growing
    Dirichlet-kernel moduli is asserted.
    """

    degree_exponent_in_q: Fraction
    ell_block_exponent_in_q: Fraction
    fan_modulus_exponent_in_q: Fraction
    dual_side_exponent_in_q: Fraction
    product_scale_exponent_in_q: Fraction
    phase_coherence_width_exponent_in_q: Fraction
    stationary_shift_spacing_exponent_in_q: Fraction
    stationary_amplitude_exponent_in_q: Fraction
    pair_weight_l2_exponent_in_q: Fraction
    unscaled_diagonal_moment_exponent_in_q: Fraction
    scaled_diagonal_moment_exponent_in_q: Fraction
    target_minor_moment_exponent_in_q: Fraction
    required_average_short_shift_exponent_in_q: Fraction
    classical_per_shift_benchmark_exponent_in_q: Fraction
    classical_short_shift_total_exponent_in_q: Fraction
    classical_aggregate_excess_exponent_in_q: Fraction
    arbitrary_path_length_exponent_in_q: Fraction
    arbitrary_path_l2_loss_exponent_in_q: Fraction
    actual_stationary_weight_is_mellin_separable: bool
    arbitrary_diagonal_path_is_separable: bool
    shifted_multiplication_table_theorem_proved: bool


def minor_product_kernel_gate_ledger() -> MinorProductKernelGateLedger:
    """Return the exact ``D=q^(16/33)`` minor-product exponent ledger."""

    degree = Fraction(16, 33)
    ell_block = 1 - degree
    fan_modulus = 1 - degree / 2
    dual_side = ell_block + fan_modulus
    product_scale = 2 * dual_side
    coherence_width = ell_block + 2 * fan_modulus - 1
    stationary_shift_spacing = ell_block + coherence_width
    stationary_amplitude = 1 - ell_block - 2 * fan_modulus
    pair_weight_l2 = degree + product_scale
    unscaled_diagonal = ell_block + pair_weight_l2
    scaled_diagonal = 2 * stationary_amplitude + unscaled_diagonal
    required_average = degree + product_scale - coherence_width
    classical_per_shift = degree + Fraction(2, 3) * product_scale
    classical_short_total = coherence_width + classical_per_shift
    classical_excess = classical_short_total - pair_weight_l2
    return MinorProductKernelGateLedger(
        degree_exponent_in_q=degree,
        ell_block_exponent_in_q=ell_block,
        fan_modulus_exponent_in_q=fan_modulus,
        dual_side_exponent_in_q=dual_side,
        product_scale_exponent_in_q=product_scale,
        phase_coherence_width_exponent_in_q=coherence_width,
        stationary_shift_spacing_exponent_in_q=stationary_shift_spacing,
        stationary_amplitude_exponent_in_q=stationary_amplitude,
        pair_weight_l2_exponent_in_q=pair_weight_l2,
        unscaled_diagonal_moment_exponent_in_q=unscaled_diagonal,
        scaled_diagonal_moment_exponent_in_q=scaled_diagonal,
        target_minor_moment_exponent_in_q=1 + degree,
        required_average_short_shift_exponent_in_q=required_average,
        classical_per_shift_benchmark_exponent_in_q=classical_per_shift,
        classical_short_shift_total_exponent_in_q=classical_short_total,
        classical_aggregate_excess_exponent_in_q=classical_excess,
        arbitrary_path_length_exponent_in_q=ell_block,
        arbitrary_path_l2_loss_exponent_in_q=ell_block,
        actual_stationary_weight_is_mellin_separable=True,
        arbitrary_diagonal_path_is_separable=False,
        shifted_multiplication_table_theorem_proved=False,
    )


@dataclass(frozen=True)
class HSMSpacingFallbackLedger:
    """Exponent ledger for the proved, non-sharp HSM spacing fallback.

    With ``P=q^(8/33)`` and ``L=q^(17/33)``, the proved estimate is
    ``N(delta) << delta*P^4 + P^3``.  Dyadic integration gives
    ``K << P^4*log(L) + L*P^3``.  The Dirichlet normalization ``P^(-2)``
    therefore leaves ``L*P`` rather than the sharp ``L``.
    """

    aperture_exponent_in_q: Fraction
    hsm_length_exponent_in_q: Fraction
    sharp_endpoint_exponent_in_q: Fraction
    fallback_endpoint_exponent_in_q: Fraction
    endpoint_gap_exponent_in_q: Fraction
    kernel_fallback_exponent_in_q: Fraction
    normalized_target_exponent_in_q: Fraction
    normalized_fallback_exponent_in_q: Fraction
    normalized_loss_exponent_in_q: Fraction
    local_target_exponent_in_q: Fraction
    local_fallback_exponent_in_q: Fraction
    local_fallback_exponent_in_degree: Fraction
    fallback_spacing_theorem_proved: bool
    sharp_spacing_theorem_proved: bool
    fallback_reproduces_existing_high_step_loss: bool
    slope_block_bound_proved: bool


def hsm_spacing_fallback_ledger() -> HSMSpacingFallbackLedger:
    """Return exact powers for ``N(delta) << delta P^4 + P^3``."""

    aperture = Fraction(8, 33)
    hsm_length = Fraction(17, 33)
    degree = 2 * aperture
    sharp_endpoint = 2 * aperture
    fallback_endpoint = 3 * aperture
    kernel_fallback = hsm_length + fallback_endpoint
    normalized_fallback = kernel_fallback - 2 * aperture
    return HSMSpacingFallbackLedger(
        aperture_exponent_in_q=aperture,
        hsm_length_exponent_in_q=hsm_length,
        sharp_endpoint_exponent_in_q=sharp_endpoint,
        fallback_endpoint_exponent_in_q=fallback_endpoint,
        endpoint_gap_exponent_in_q=fallback_endpoint - sharp_endpoint,
        kernel_fallback_exponent_in_q=kernel_fallback,
        normalized_target_exponent_in_q=hsm_length,
        normalized_fallback_exponent_in_q=normalized_fallback,
        normalized_loss_exponent_in_q=normalized_fallback - hsm_length,
        local_target_exponent_in_q=degree,
        local_fallback_exponent_in_q=degree + aperture,
        local_fallback_exponent_in_degree=Fraction(3, 2),
        fallback_spacing_theorem_proved=True,
        sharp_spacing_theorem_proved=False,
        fallback_reproduces_existing_high_step_loss=True,
        slope_block_bound_proved=False,
    )


@dataclass(frozen=True)
class FejerDiagonalCubicFallbackLedger:
    """Exact powers in the proved positive diagonal-peak fallback.

    The diagonal incidence target is ``E_diag << L*q^o(1)``.  Combining a
    degree-``P`` Selberg majorant, Dirichlet approximation, the standard
    reciprocal-sum lemma, and Huxley's rational-points-near-a-curve theorem
    proves ``E_diag << L*P^(3/7+o(1))``.  This is a necessary positive piece
    of the weighted HSM, not a proof of the full two-dimensional estimate.
    """

    aperture_exponent_in_q: Fraction
    hsm_length_exponent_in_q: Fraction
    trivial_gap_exponent_in_p: Fraction
    trivial_rational_incidence_exponent_in_denominator: int
    huxley_first_p_exponent: Fraction
    huxley_first_denominator_exponent: Fraction
    huxley_second_p_exponent: Fraction
    huxley_second_denominator_exponent: int
    crossover_denominator_exponent_in_p: Fraction
    fallback_gap_exponent_in_p: Fraction
    fallback_gap_exponent_in_q: Fraction
    target_exponent_in_q: Fraction
    fallback_exponent_in_q: Fraction
    exact_rational_ray_exponent_in_length: int
    exact_rational_rays_close_at_target: bool
    diagonal_peak_fallback_proved: bool
    sharp_diagonal_peak_bound_proved: bool
    full_weighted_hsm_proved: bool


def fejer_diagonal_cubic_fallback_ledger() -> FejerDiagonalCubicFallbackLedger:
    """Return the exact ``E_diag << L*P^(3/7+o(1))`` exponent ledger."""

    aperture = Fraction(8, 33)
    hsm_length = Fraction(17, 33)
    gap_in_p = Fraction(3, 7)
    gap_in_q = aperture * gap_in_p
    return FejerDiagonalCubicFallbackLedger(
        aperture_exponent_in_q=aperture,
        hsm_length_exponent_in_q=hsm_length,
        trivial_gap_exponent_in_p=1,
        trivial_rational_incidence_exponent_in_denominator=2,
        huxley_first_p_exponent=Fraction(3, 4),
        huxley_first_denominator_exponent=Fraction(1, 4),
        huxley_second_p_exponent=Fraction(1, 3),
        huxley_second_denominator_exponent=1,
        crossover_denominator_exponent_in_p=gap_in_p,
        fallback_gap_exponent_in_p=gap_in_p,
        fallback_gap_exponent_in_q=gap_in_q,
        target_exponent_in_q=hsm_length,
        fallback_exponent_in_q=hsm_length + gap_in_q,
        exact_rational_ray_exponent_in_length=1,
        exact_rational_rays_close_at_target=True,
        diagonal_peak_fallback_proved=True,
        sharp_diagonal_peak_bound_proved=False,
        full_weighted_hsm_proved=False,
    )


def exact_cubic_ray_persistent_count(
    base: int, length: int, lower_index: int, upper_index: int
) -> int:
    """Count exact resonances ``ell*(base/m)^3 in Z`` for ``1<=ell<=L``.

    If ``base/m=s/t`` in lowest terms, the exact period is ``t^3``.  The
    report proves that summing ``L//t^3`` over a dyadic interval ``m~base``
    is ``O(L)``.  This finite helper makes the period calculation exact.
    """

    if min(base, length, lower_index) <= 0 or upper_index < lower_index:
        raise ValueError("the base, length, and index interval must be positive")
    return sum(
        length // (index // math.gcd(base, index)) ** 3
        for index in range(lower_index, upper_index + 1)
    )


@dataclass(frozen=True)
class CubicReciprocalEndpointLedger:
    """Exact powers in the remaining shifted-cube endpoint.

    All exponents in this ledger are powers of ``P``.  At the hostile
    dyadic endpoint one has ``Q=P^(11/32)``, residual width
    ``H=P^(7/32)``, and restored gcd multiplicity ``G=P^(21/32)``.
    Konyagin's rational-approximation theorem gives the best audited raw
    bound ``P^(43/80+o(1))``; the desired raw count is ``Q*P^o(1)``.

    A nonzero solution ``r*a^3-p*c^3=e`` yields, after division by the
    common gcd ``g``, a primitive ``abc`` triple.  If ``g=P^gamma`` on the
    exponent ledger, its height and radical exponents are bounded by
    ``107/32-gamma`` and ``93/32-gamma``.  Their quotient is minimized at
    ``gamma=0``, giving quality ``107/93`` and the sharp audited epsilon
    barrier ``14/93``.  This proves the displayed quality lower bound
    unconditionally.  It does *not* invoke ``abc`` or prove that no such
    nonzero solution exists.
    """

    denominator_exponent_in_p: Fraction
    residual_exponent_in_p: Fraction
    gcd_multiplicity_exponent_in_p: Fraction
    desired_raw_count_exponent_in_p: Fraction
    huxley_raw_count_exponent_in_p: Fraction
    konyagin_raw_count_exponent_in_p: Fraction
    konyagin_raw_gap_exponent_in_p: Fraction
    restored_target_exponent_in_p: Fraction
    restored_konyagin_exponent_in_p: Fraction
    restored_gap_exponent_in_p: Fraction
    common_gcd_upper_exponent_in_p: Fraction
    height_before_common_gcd_exponent_in_p: Fraction
    radical_before_common_gcd_exponent_in_p: Fraction
    primitive_height_lower_exponent_in_p: Fraction
    primitive_radical_upper_exponent_in_p: Fraction
    primitive_abc_quality_lower_bound: Fraction
    abc_epsilon_barrier: Fraction
    common_gcd_cancels_from_height_and_radical: bool
    zero_residual_raw_count_exponent_in_p: Fraction
    zero_residual_exact_rays_target_controlled: bool
    polynomial_term_degree_before_common_gcd: int
    polynomial_radical_degree_before_common_gcd: int
    polynomial_common_gcd_degree_upper_bound: int
    polynomial_term_degree_after_common_gcd: int
    polynomial_radical_degree_upper_bound: int
    pointwise_exclusion_is_abc_level: bool
    polynomial_counterfamily_excluded: bool
    averaged_cubic_theorem_proved: bool
    sharp_hsm_proved: bool


def cubic_reciprocal_endpoint_ledger() -> CubicReciprocalEndpointLedger:
    """Return the exact hostile shifted-cube exponent ledger."""

    denominator = Fraction(11, 32)
    residual = Fraction(7, 32)
    multiplicity = Fraction(21, 32)
    huxley = Fraction(9, 16)
    konyagin = Fraction(43, 80)
    common_gcd = residual
    height_before_gcd = Fraction(107, 32)
    radical_before_gcd = Fraction(93, 32)
    coarse_height_after_gcd = height_before_gcd - common_gcd
    coarse_radical = radical_before_gcd
    return CubicReciprocalEndpointLedger(
        denominator_exponent_in_p=denominator,
        residual_exponent_in_p=residual,
        gcd_multiplicity_exponent_in_p=multiplicity,
        desired_raw_count_exponent_in_p=denominator,
        huxley_raw_count_exponent_in_p=huxley,
        konyagin_raw_count_exponent_in_p=konyagin,
        konyagin_raw_gap_exponent_in_p=konyagin - denominator,
        restored_target_exponent_in_p=1,
        restored_konyagin_exponent_in_p=multiplicity + konyagin,
        restored_gap_exponent_in_p=multiplicity + konyagin - 1,
        common_gcd_upper_exponent_in_p=common_gcd,
        height_before_common_gcd_exponent_in_p=height_before_gcd,
        radical_before_common_gcd_exponent_in_p=radical_before_gcd,
        primitive_height_lower_exponent_in_p=coarse_height_after_gcd,
        primitive_radical_upper_exponent_in_p=coarse_radical,
        primitive_abc_quality_lower_bound=height_before_gcd / radical_before_gcd,
        abc_epsilon_barrier=Fraction(14, 93),
        common_gcd_cancels_from_height_and_radical=True,
        zero_residual_raw_count_exponent_in_p=denominator / 3,
        zero_residual_exact_rays_target_controlled=True,
        polynomial_term_degree_before_common_gcd=107,
        polynomial_radical_degree_before_common_gcd=93,
        polynomial_common_gcd_degree_upper_bound=7,
        polynomial_term_degree_after_common_gcd=100,
        polynomial_radical_degree_upper_bound=93,
        pointwise_exclusion_is_abc_level=True,
        polynomial_counterfamily_excluded=True,
        averaged_cubic_theorem_proved=False,
        sharp_hsm_proved=False,
    )


@dataclass(frozen=True)
class ConditionalABCClosureAuditLedger:
    """Exact exponent boundary of the conditional-``abc`` audit.

    The diagonal statement is conditional on standard ``abc`` together
    with the already audited Huxley/Farey decomposition.  Huxley's fourth
    rational-points-near-a-curve theorem is applicable with determinant
    parameter ``d=2``.  Its four primitive exponents are ``5/8, 5/8,
    3/5, 25/72``; the pure minor term therefore leaves a ``P^(5/8)``
    floor, even after ``abc``.  Against the ``P^(9/16)`` transition target,
    this is the remaining ``P^(1/16)`` diagonal loss.

    The transition equation is

    ``A*u^3-B*P^3=D``, ``A,B~P^(9/16)``, ``|D|<=P^(7/16)``.

    Its term height and the permitted generic radical both have exponent
    ``57/16``.  Hensel lifting gives only ``R<<T*H=P``.  Standard ``abc``
    forces ``|D|>=P^(7/16-o(1))`` but supplies no saving in the number of
    top-shell residuals.

    For generic nonzero spacing levels, ``q^3*w-2*t*z^2=e`` has height and
    permitted radical exponent four when ``t=1`` and the other factors are
    squarefree.  For a fixed row pair, the identity

    ``J^2+Delta*det(E)=(u^T*K*v')*(u'^T*K*v)``

    likewise has a generically squarefree product term of full height.
    Both are quality-one obstructions rather than conditional closures.
    """

    diagonal_unconditional_gap_exponent_in_p: Fraction
    diagonal_huxley_d_parameter: int
    diagonal_huxley_primitive_term_exponents_in_p: tuple[Fraction, ...]
    diagonal_huxley_pure_minor_floor_exponent_in_p: Fraction
    diagonal_transition_target_exponent_in_p: Fraction
    diagonal_huxley_primitive_count_bound_exponent_in_p: Fraction
    diagonal_abc_huxley_gap_exponent_in_p: Fraction
    diagonal_abc_huxley_gap_exponent_in_q: Fraction
    diagonal_abc_huxley_total_exponent_in_q: Fraction
    transition_coefficient_exponent_in_p: Fraction
    transition_residual_exponent_in_p: Fraction
    transition_term_height_exponent_in_p: Fraction
    transition_generic_radical_exponent_in_p: Fraction
    transition_abc_quality: Fraction
    transition_hensel_bound_exponent_in_p: Fraction
    transition_target_exponent_in_p: Fraction
    transition_hensel_gap_exponent_in_p: Fraction
    transition_abc_residual_lower_exponent_in_p: Fraction
    spacing_generic_height_exponent_in_q: Fraction
    spacing_generic_radical_exponent_in_q: Fraction
    spacing_generic_abc_quality: Fraction
    fixed_row_degree_exponent_in_q: Fraction
    fixed_row_main_minimum_exponent_in_q: Fraction
    fixed_row_correction_upper_exponent_in_q: Fraction
    fixed_row_main_correction_gap_exponent_in_q: Fraction
    fixed_row_generic_abc_quality: Fraction
    abc_huxley_diagonal_bound_is_conditional: bool
    abc_huxley_diagonal_target_proved: bool
    transition_hensel_bound_proved: bool
    transition_target_proved_under_abc: bool
    transition_abc_only_forces_top_residual_shell: bool
    spacing_t_zero_target_bound_proved: bool
    spacing_exact_zero_residual_nonzero_level_impossible: bool
    sharp_spacing_endpoint_proved_under_abc: bool
    fixed_row_cross_product_identity_exact: bool
    fixed_row_abc_forces_tangent_chart_reuse: bool
    weighted_hsm_proved_under_abc: bool
    slope_block_bound_proved_under_abc: bool
    full_four_cycle_bound_proved_under_abc: bool


def conditional_abc_closure_audit_ledger() -> ConditionalABCClosureAuditLedger:
    """Return exact powers and nonimplication flags for conditional ``abc``."""

    aperture = Fraction(8, 33)
    hsm_length = Fraction(17, 33)
    huxley_terms = (
        Fraction(5, 8),
        Fraction(5, 8),
        Fraction(3, 5),
        Fraction(25, 72),
    )
    huxley_floor = max(huxley_terms)
    diagonal_transition_target = Fraction(9, 16)
    diagonal_gap_in_p = huxley_floor - diagonal_transition_target
    diagonal_gap_in_q = aperture * diagonal_gap_in_p
    transition_coefficient = Fraction(9, 16)
    transition_residual = Fraction(7, 16)
    transition_height = transition_coefficient + 3
    fixed_row_degree = Fraction(16, 33)
    fixed_row_main = Fraction(2)
    fixed_row_correction = 3 * fixed_row_degree
    return ConditionalABCClosureAuditLedger(
        diagonal_unconditional_gap_exponent_in_p=Fraction(3, 7),
        diagonal_huxley_d_parameter=2,
        diagonal_huxley_primitive_term_exponents_in_p=huxley_terms,
        diagonal_huxley_pure_minor_floor_exponent_in_p=huxley_floor,
        diagonal_transition_target_exponent_in_p=diagonal_transition_target,
        diagonal_huxley_primitive_count_bound_exponent_in_p=huxley_floor,
        diagonal_abc_huxley_gap_exponent_in_p=diagonal_gap_in_p,
        diagonal_abc_huxley_gap_exponent_in_q=diagonal_gap_in_q,
        diagonal_abc_huxley_total_exponent_in_q=(
            hsm_length + diagonal_gap_in_q
        ),
        transition_coefficient_exponent_in_p=transition_coefficient,
        transition_residual_exponent_in_p=transition_residual,
        transition_term_height_exponent_in_p=transition_height,
        transition_generic_radical_exponent_in_p=transition_height,
        transition_abc_quality=Fraction(1),
        transition_hensel_bound_exponent_in_p=(
            transition_coefficient + transition_residual
        ),
        transition_target_exponent_in_p=transition_coefficient,
        transition_hensel_gap_exponent_in_p=transition_residual,
        transition_abc_residual_lower_exponent_in_p=transition_residual,
        spacing_generic_height_exponent_in_q=Fraction(4),
        spacing_generic_radical_exponent_in_q=Fraction(4),
        spacing_generic_abc_quality=Fraction(1),
        fixed_row_degree_exponent_in_q=fixed_row_degree,
        fixed_row_main_minimum_exponent_in_q=fixed_row_main,
        fixed_row_correction_upper_exponent_in_q=fixed_row_correction,
        fixed_row_main_correction_gap_exponent_in_q=(
            fixed_row_main - fixed_row_correction
        ),
        fixed_row_generic_abc_quality=Fraction(1),
        abc_huxley_diagonal_bound_is_conditional=True,
        abc_huxley_diagonal_target_proved=False,
        transition_hensel_bound_proved=True,
        transition_target_proved_under_abc=False,
        transition_abc_only_forces_top_residual_shell=True,
        spacing_t_zero_target_bound_proved=True,
        spacing_exact_zero_residual_nonzero_level_impossible=True,
        sharp_spacing_endpoint_proved_under_abc=False,
        fixed_row_cross_product_identity_exact=True,
        fixed_row_abc_forces_tangent_chart_reuse=False,
        weighted_hsm_proved_under_abc=False,
        slope_block_bound_proved_under_abc=False,
        full_four_cycle_bound_proved_under_abc=False,
    )


@dataclass(frozen=True)
class FixedATransitionEnergyAuditLedger:
    """Exact exponent ledger for the fixed-``A`` cubic transition audit.

    The transition variables satisfy

    ``A*u^3-B*P^3=D``, ``A,B~T=P^(9/16)``, ``|D|<=H=P^(7/16)``.

    If ``r_A`` counts solutions with a fixed value of ``A``, put
    ``E_2=sum_A r_A(r_A-1)``.  The estimate ``E_2<<T*P^o(1)`` is sufficient:

    ``R^2 <= T*sum_A r_A^2 = T*(R+E_2)``.

    The ledger records proved identities and local determinant spacings, not
    the missing estimate.  The three-point spacing is unconditional; the
    six-point statement is the nonzero-alternant (minor) branch, with the
    zero alternant defining the rational-quadratic packet branch.  Its final
    fields describe an abstract incidence array which obeys all recorded
    constraints while retaining the complete ``P^(5/8)`` Huxley count.
    """

    coefficient_exponent_in_p: Fraction
    residual_exponent_in_p: Fraction
    fixed_a_values_exponent_in_p: Fraction
    target_count_exponent_in_p: Fraction
    sufficient_factorial_energy_exponent_in_p: Fraction
    huxley_count_exponent_in_p: Fraction
    huxley_critical_cell_exponent_in_p: Fraction
    huxley_cells_exponent_in_p: Fraction
    missing_saving_exponent_in_p: Fraction
    same_a_pair_gap_exponent_in_p: Fraction
    same_a_three_point_span_exponent_in_p: Fraction
    same_a_six_point_span_exponent_in_p: Fraction
    zero_residual_factorial_energy_exponent_in_p: Fraction
    saturator_denominator_labels_exponent_in_p: Fraction
    saturator_points_per_label_exponent_in_p: Fraction
    saturator_same_label_spacing_exponent_in_p: Fraction
    saturator_total_points_exponent_in_p: Fraction
    factorial_energy_bound_is_sufficient: bool
    same_a_pair_identities_are_exact: bool
    zero_residual_rays_are_target_controlled: bool
    local_determinant_spacing_is_proved: bool
    three_point_spacing_is_unconditional: bool
    six_point_spacing_requires_nonzero_alternant: bool
    current_constraints_force_target: bool
    fixed_a_factorial_energy_proved: bool
    transition_target_proved: bool


def fixed_a_transition_energy_audit_ledger() -> FixedATransitionEnergyAuditLedger:
    """Return exact powers and status flags for the fixed-``A`` audit."""

    coefficient = Fraction(9, 16)
    residual = Fraction(7, 16)
    huxley_count = Fraction(5, 8)
    critical_cell = Fraction(3, 8)
    points_per_label = huxley_count - coefficient
    same_label_spacing = coefficient + critical_cell
    return FixedATransitionEnergyAuditLedger(
        coefficient_exponent_in_p=coefficient,
        residual_exponent_in_p=residual,
        fixed_a_values_exponent_in_p=coefficient,
        target_count_exponent_in_p=coefficient,
        sufficient_factorial_energy_exponent_in_p=coefficient,
        huxley_count_exponent_in_p=huxley_count,
        huxley_critical_cell_exponent_in_p=critical_cell,
        huxley_cells_exponent_in_p=1 - critical_cell,
        missing_saving_exponent_in_p=huxley_count - coefficient,
        same_a_pair_gap_exponent_in_p=residual,
        same_a_three_point_span_exponent_in_p=Fraction(23, 48),
        same_a_six_point_span_exponent_in_p=Fraction(39, 80),
        zero_residual_factorial_energy_exponent_in_p=coefficient,
        saturator_denominator_labels_exponent_in_p=coefficient,
        saturator_points_per_label_exponent_in_p=points_per_label,
        saturator_same_label_spacing_exponent_in_p=same_label_spacing,
        saturator_total_points_exponent_in_p=huxley_count,
        factorial_energy_bound_is_sufficient=True,
        same_a_pair_identities_are_exact=True,
        zero_residual_rays_are_target_controlled=True,
        local_determinant_spacing_is_proved=True,
        three_point_spacing_is_unconditional=True,
        six_point_spacing_requires_nonzero_alternant=True,
        current_constraints_force_target=False,
        fixed_a_factorial_energy_proved=False,
        transition_target_proved=False,
    )


@dataclass(frozen=True)
class FixedATransitionPairIdentity:
    """Exact identities attached to two transition solutions with one ``A``."""

    gap: int
    quotient_gap: int
    residual_gap: int
    cubic_secant_factor: int
    differenced_identity: int
    cross_cubic_residual: int
    cross_cubic_identity: int


def fixed_a_transition_pair_identity(
    modulus: int,
    coefficient: int,
    first_u: int,
    first_b: int,
    first_residual: int,
    second_u: int,
    second_b: int,
    second_residual: int,
) -> FixedATransitionPairIdentity:
    """Verify and return the two exact same-``A`` cubic pair identities.

    Both supplied endpoints must satisfy ``A*u^3-B*P^3=D``.  For
    ``k=u_2-u_1``, ``c=B_2-B_1`` and ``e=D_2-D_1``, subtraction gives

    ``A*k*(3*u_1^2+3*u_1*k+k^2)-c*P^3=e``.

    Eliminating ``A`` instead gives

    ``P^3*(B_1*u_2^3-B_2*u_1^3)=D_2*u_1^3-D_1*u_2^3``.
    """

    if min(modulus, coefficient, first_u, first_b, second_u, second_b) <= 0:
        raise ValueError(
            "the transition modulus and positive variables are required"
        )
    if coefficient * first_u**3 - first_b * modulus**3 != first_residual:
        raise ValueError("the first endpoint does not satisfy the transition equation")
    if coefficient * second_u**3 - second_b * modulus**3 != second_residual:
        raise ValueError("the second endpoint does not satisfy the transition equation")
    gap = second_u - first_u
    quotient_gap = second_b - first_b
    residual_gap = second_residual - first_residual
    secant = 3 * first_u**2 + 3 * first_u * gap + gap**2
    differenced = coefficient * gap * secant - quotient_gap * modulus**3
    cross_residual = first_b * second_u**3 - second_b * first_u**3
    cross_identity = (
        second_residual * first_u**3 - first_residual * second_u**3
    )
    return FixedATransitionPairIdentity(
        gap=gap,
        quotient_gap=quotient_gap,
        residual_gap=residual_gap,
        cubic_secant_factor=secant,
        differenced_identity=differenced,
        cross_cubic_residual=cross_residual,
        cross_cubic_identity=cross_identity,
    )


def exact_zero_transition_quotient(
    modulus: int, coefficient: int, input_value: int
) -> int | None:
    """Return ``B`` when ``A*u^3=B*P^3``, using the reduced cube ray.

    Write ``u/P=x/y`` in lowest terms.  Exact resonance is equivalent to
    ``y^3|A``, in which case ``B=(A/y^3)*x^3``.  This is the parameterization
    used in the target-sized zero-residual energy bound.
    """

    if min(modulus, coefficient, input_value) <= 0:
        raise ValueError("the exact-ray variables must be positive")
    common = math.gcd(input_value, modulus)
    numerator = input_value // common
    denominator = modulus // common
    denominator_cube = denominator**3
    if coefficient % denominator_cube:
        return None
    return coefficient // denominator_cube * numerator**3


@dataclass(frozen=True)
class FixedAFactorialEnergyCertificate:
    """Finite Cauchy certificate for fixed-``A`` multiplicities."""

    number_of_labels: int
    total_count: int
    factorial_energy: int
    square_energy: int
    cauchy_left: int
    cauchy_right: int


def fixed_a_factorial_energy_certificate(
    multiplicities: Sequence[int],
) -> FixedAFactorialEnergyCertificate:
    """Return the exact identity behind the sufficient energy lemma."""

    if any(value < 0 for value in multiplicities):
        raise ValueError("multiplicities must be nonnegative")
    count = sum(multiplicities)
    factorial_energy = sum(value * (value - 1) for value in multiplicities)
    square_energy = sum(value * value for value in multiplicities)
    labels = len(multiplicities)
    return FixedAFactorialEnergyCertificate(
        number_of_labels=labels,
        total_count=count,
        factorial_energy=factorial_energy,
        square_energy=square_energy,
        cauchy_left=count * count,
        cauchy_right=labels * square_energy,
    )


def fixed_a_huxley_saturator(
    denominator_labels: int, points_per_label: int
) -> tuple[tuple[int, int], ...]:
    """Build the abstract incidence array saturating all current spacings.

    The critical cells are numbered ``0,...,T*r-1``.  Label ``a`` occupies
    cells ``a+k*T``.  Hence each cell has one point, each label has ``r``
    points, and equal labels are separated by exactly ``T`` critical cells.
    This is combinatorial only; it is not asserted to solve the cubic
    transition equation.
    """

    if denominator_labels <= 0 or points_per_label <= 0:
        raise ValueError("the saturator dimensions must be positive")
    return tuple(
        (label, label + layer * denominator_labels)
        for layer in range(points_per_label)
        for label in range(denominator_labels)
    )


def hsm_spacing_phase(
    q: int,
    row_modulus: int,
    color_modulus: int,
    row_index: int,
    color_index: int,
    row_shift: int,
    color_shift: int,
) -> Fraction:
    """Return ``h*A_mn+k*B_mn`` with no floating-point rounding."""

    positive = (q, row_modulus, color_modulus, row_index, color_index)
    if any(value <= 0 for value in positive):
        raise ValueError("the modulus and index parameters must be positive")
    return Fraction(
        row_shift * q**3,
        8 * row_modulus**2 * color_modulus * row_index**2 * color_index,
    ) + Fraction(
        color_shift * q**3,
        8 * row_modulus * color_modulus**2 * row_index * color_index**2,
    )


def _fractional_distance(value: Fraction) -> Fraction:
    residue = value.numerator % value.denominator
    return Fraction(min(residue, value.denominator - residue), value.denominator)


@dataclass(frozen=True)
class HSMSpacingSharpnessFixture:
    """Exact finite aligned-center and homogeneous-gcd resonance counts."""

    q: int
    aperture: int
    row_modulus: int
    color_modulus: int
    threshold: Fraction
    center: tuple[int, int]
    center_shift_cutoff: int
    center_relations_tested: int
    center_relations_passing: int
    center_maximum_distance: Fraction
    center_nearest_integer_is_shift_sum: bool
    gcd_shell: tuple[int, int]
    gcd_relations_tested: int
    gcd_relations_passing: int
    gcd_maximum_distance: Fraction
    minimum_triangular_autocorrelation: int

    @property
    def center_all_tested_relations_pass(self) -> bool:
        return self.center_relations_passing == self.center_relations_tested

    @property
    def gcd_all_tested_relations_pass(self) -> bool:
        return self.gcd_relations_passing == self.gcd_relations_tested


def hsm_spacing_sharpness_fixture(
    q: int, aperture: int
) -> HSMSpacingSharpnessFixture:
    """Check two endpoint-sharp spacing families in an exact finite model.

    Set ``R`` to the nearest integer to ``q/P`` and ``S=R+1``.  At
    ``m=n=P/2``, short positive shifts align with the nonzero integer
    ``h+k``.  On ``P/2 <= m,n <= 3P/4``, the shifts
    ``(h,k)=(z*m/g,-z*n/g)`` give the homogeneous gcd family.  The exact
    threshold ``P^2/q`` is the finite analogue of ``1/L``.
    """

    if q <= 0:
        raise ValueError("q must be positive")
    if aperture < 20 or aperture % 2:
        raise ValueError("the aperture must be an even integer at least 20")
    row_modulus = (q + aperture // 2) // aperture
    if row_modulus <= 1:
        raise ValueError("q/aperture must exceed one")
    color_modulus = row_modulus + 1
    threshold = Fraction(aperture**2, q)
    center = (aperture // 2, aperture // 2)
    center_cutoff = max(1, aperture // 20)

    center_distances: list[Fraction] = []
    center_nearest_integer_is_shift_sum = True
    for row_shift in range(1, center_cutoff + 1):
        for color_shift in range(1, center_cutoff + 1):
            phase = hsm_spacing_phase(
                q,
                row_modulus,
                color_modulus,
                center[0],
                center[1],
                row_shift,
                color_shift,
            )
            center_distances.append(_fractional_distance(phase))
            center_nearest_integer_is_shift_sum &= (
                abs(phase - (row_shift + color_shift)) <= threshold
            )

    shell_lower = aperture // 2
    shell_upper = 3 * aperture // 4
    gcd_distances: list[Fraction] = []
    maximum_shift = 0
    for row_index in range(shell_lower, shell_upper + 1):
        for color_index in range(shell_lower, shell_upper + 1):
            common = math.gcd(row_index, color_index)
            for multiplier in range(1, common + 1):
                row_shift = multiplier * row_index // common
                color_shift = -multiplier * color_index // common
                maximum_shift = max(
                    maximum_shift, abs(row_shift), abs(color_shift)
                )
                phase = hsm_spacing_phase(
                    q,
                    row_modulus,
                    color_modulus,
                    row_index,
                    color_index,
                    row_shift,
                    color_shift,
                )
                gcd_distances.append(_fractional_distance(phase))

    return HSMSpacingSharpnessFixture(
        q=q,
        aperture=aperture,
        row_modulus=row_modulus,
        color_modulus=color_modulus,
        threshold=threshold,
        center=center,
        center_shift_cutoff=center_cutoff,
        center_relations_tested=len(center_distances),
        center_relations_passing=sum(
            distance <= threshold for distance in center_distances
        ),
        center_maximum_distance=max(center_distances, default=Fraction(0)),
        center_nearest_integer_is_shift_sum=center_nearest_integer_is_shift_sum,
        gcd_shell=(shell_lower, shell_upper),
        gcd_relations_tested=len(gcd_distances),
        gcd_relations_passing=sum(
            distance <= threshold for distance in gcd_distances
        ),
        gcd_maximum_distance=max(gcd_distances, default=Fraction(0)),
        minimum_triangular_autocorrelation=aperture - maximum_shift,
    )


@dataclass(frozen=True)
class RelevantStripIntegerLiftLedger:
    """All-integer lift count in a nonempty high-denominator slope strip.

    Fix a primitive reference ``(p,r)`` in a shell shorter than ``p``.
    Every integer vector ``x`` with ``det((p,r),x)=h`` is congruent to one
    residue class in its first coordinate, and two such vectors with the
    same ``h`` differ by an integer multiple of ``(p,r)``.  The shell
    therefore contains at most one lift for every determinant offset,
    without any primitivity assumption on ``x``.
    """

    reference: tuple[int, int]
    shell: tuple[int, int]
    determinant_bound: int
    determinant_values_checked: int
    admissible_vector_count: int
    maximum_lifts_per_determinant: int
    cardinality_cap: int


def relevant_strip_integer_lift_ledger(
    reference: tuple[int, int],
    shell_lower: int,
    shell_upper: int,
    determinant_bound: int,
) -> RelevantStripIntegerLiftLedger:
    """Count all integer shell lifts with ``|det(reference,x)| <= B``.

    This is the legal all-integer enlargement of a *relevant* slope block:
    its primitive reference has coordinates on the shell scale.  It should
    not be confused with a strip centered on a fixed small-denominator
    rational ray.
    """

    p, r = (int(value) for value in reference)
    lower = int(shell_lower)
    upper = int(shell_upper)
    bound = int(determinant_bound)
    if bound < 0:
        raise ValueError("determinant bound must be nonnegative")
    if min(p, r, lower) <= 0 or upper < lower:
        raise ValueError("reference and shell must be positive")
    if math.gcd(p, r) != 1:
        raise ValueError("reference must be primitive")
    if upper - lower >= p:
        raise ValueError("shell interval must be shorter than the modulus")

    admissible = 0
    for h in range(-bound, bound + 1):
        lift = primitive_slope_modular_lift(
            (p, r), h, lower, upper
        )
        admissible += int(lift.vector is not None)
    cap = 2 * bound + 1
    return RelevantStripIntegerLiftLedger(
        reference=(p, r),
        shell=(lower, upper),
        determinant_bound=bound,
        determinant_values_checked=cap,
        admissible_vector_count=admissible,
        maximum_lifts_per_determinant=1,
        cardinality_cap=cap,
    )


@dataclass(frozen=True)
class ReducedDeterminantFanLedger:
    """An invariant shortest-vector decomposition of one modular strip.

    In determinant/first-coordinate variables the difference lattice is

    ``Lambda={(h,a): a == -inverse(r)*h (mod p)}``, ``det Lambda=p``.

    Scaling the two coordinates by ``D`` and ``p`` gives covolume ``1/D``.
    A shortest vector therefore has scaled sup norm at most ``D^(-1/2)``.
    Its lattice cosets cut a ``2D``-by-``<p`` lift rectangle into at most
    ``O(sqrt(D))`` parallel arithmetic fans.  This is the reduced version
    of a residue-class fan split; it is independent of a chosen congruence
    presentation.
    """

    reference: tuple[int, int]
    determinant_bound: int
    multiplier: int
    shortest_vector: tuple[int, int]
    shortest_scaled_norm: Fraction
    minkowski_scaled_norm_cap: float
    primitive_basis_coordinates: tuple[int, int]
    fan_count_envelope: int
    fan_length_envelope: int


def reduced_determinant_fan_ledger(
    reference: tuple[int, int], determinant_bound: int
) -> ReducedDeterminantFanLedger:
    """Find the exact anisotropic shortest direction of a lift lattice.

    The returned fan envelopes apply to any first-coordinate interval of
    length strictly less than ``p`` and determinant interval ``[-D,D]``.
    Enumeration only uses ``1<=|h|<=D``: Minkowski gives a nonzero vector
    with scaled norm at most ``D^(-1/2)<1``, so a shortest vector cannot
    have ``|h|>D`` or be the vertical vector ``(0,p)`` when ``D>1``.
    """

    p, r = (int(value) for value in reference)
    degree = int(determinant_bound)
    if min(p, r, degree) <= 0:
        raise ValueError("reference and determinant bound must be positive")
    if math.gcd(p, r) != 1:
        raise ValueError("reference must be primitive")
    multiplier = (-pow(r, -1, p)) % p

    best_vector: tuple[int, int] | None = None
    best_norm: Fraction | None = None
    for first in range(1, degree + 1):
        second = (multiplier * first) % p
        if 2 * second > p:
            second -= p
        norm = max(Fraction(first, degree), Fraction(abs(second), p))
        if best_norm is None or norm < best_norm:
            best_norm = norm
            best_vector = (first, second)
    if best_vector is None or best_norm is None:
        raise AssertionError("shortest-vector enumeration was empty")

    first, second = best_vector
    quotient_coordinate = (second - multiplier * first) // p
    if second - multiplier * first != p * quotient_coordinate:
        raise AssertionError("shortest vector is not in the lift lattice")
    if math.gcd(first, quotient_coordinate) != 1:
        raise AssertionError("a shortest nonzero lattice vector is not primitive")

    # The quotient functional det(v,x)/p changes by at most this amount on
    # a rectangle of h-width 2D and a-width <p.
    quotient_range = Fraction(abs(first), 1) + Fraction(
        2 * degree * abs(second), p
    )
    fan_count = quotient_range.numerator // quotient_range.denominator + 2
    h_length = 2 * degree // abs(first) + 1
    a_length = (
        (p - 1) // abs(second) + 1 if second else h_length
    )
    fan_length = min(h_length, a_length)

    if best_norm > Fraction(1, math.isqrt(degree)):
        # ``1/isqrt(D)`` is a slightly weaker exact form of ``D^(-1/2)``.
        # Keep the assertion useful without introducing floating rounding.
        raise AssertionError("shortest vector missed the Minkowski scale")
    return ReducedDeterminantFanLedger(
        reference=(p, r),
        determinant_bound=degree,
        multiplier=multiplier,
        shortest_vector=best_vector,
        shortest_scaled_norm=best_norm,
        minkowski_scaled_norm_cap=degree ** -0.5,
        primitive_basis_coordinates=(first, quotient_coordinate),
        fan_count_envelope=fan_count,
        fan_length_envelope=fan_length,
    )


@dataclass(frozen=True)
class QuarticHighStepFanBarrierLedger:
    """Exact anti-diagonal obstruction to a geometry-only fan estimate.

    Put ``R=n^33``, ``m=R^2``, ``q=2m``, ``T=n^8`` and
    ``D=4T^4``.  On two arithmetic fans with common absolute step ``R``,
    pair the points

    ``a_i=m+R*i, c_i=m-R*i, b_i=m+i^2`` (``1<=i<=T``).

    The quadratic carrier correction is integral and the product error is
    exactly quartic.  This disproves the tempting geometry-only estimate

    ``E_fan << q^o(1 + D/R^2 + (D/q)T^2)``.

    The centre ``q=2R^2`` is even and composite, and the fan projections
    are not asserted to arise from actual prime-power slope vertices.  The
    ledger is therefore a method barrier, not a counterexample to ``(SB)``.
    """

    scale: int
    step: int
    center: int
    modulus: int
    aperture: int
    fan_length: int
    edge_count: int
    support_four_cycle_count: int
    first_fan_endpoints: tuple[int, int]
    second_fan_endpoints: tuple[int, int]
    maximum_product_residual: int
    product_window: int
    proposed_curvature_term: Fraction
    proposed_volume_term: Fraction
    proposed_bound_without_q_o: Fraction


def quartic_high_step_fan_barrier_ledger(
    scale: int,
) -> QuarticHighStepFanBarrierLedger:
    """Return the exact quartic high-step matching at active exponents."""

    base = int(scale)
    if base < 2:
        raise ValueError("scale must be at least two")
    step = base**33
    center = step * step
    modulus = 2 * center
    fan_length = base**8
    aperture = 4 * fan_length**4

    # At i=T the exact identity is
    # (m+Ri)(m-Ri)(m+i^2)=m^3-m*i^4.
    maximum_residual = 8 * center * fan_length**4
    window = modulus * aperture
    if maximum_residual != window:
        raise AssertionError("quartic endpoint must exactly saturate the window")

    curvature = Fraction(aperture, step * step)
    volume = Fraction(aperture * fan_length * fan_length, modulus)
    proposed = Fraction(1, 1) + curvature + volume
    return QuarticHighStepFanBarrierLedger(
        scale=base,
        step=step,
        center=center,
        modulus=modulus,
        aperture=aperture,
        fan_length=fan_length,
        edge_count=fan_length,
        support_four_cycle_count=0,
        first_fan_endpoints=(
            center + step,
            center + step * fan_length,
        ),
        second_fan_endpoints=(
            center - step * fan_length,
            center - step,
        ),
        maximum_product_residual=maximum_residual,
        product_window=window,
        proposed_curvature_term=curvature,
        proposed_volume_term=volume,
        proposed_bound_without_q_o=proposed,
    )


@dataclass(frozen=True)
class OppositeFanPolynomialArcLedger:
    """Exact coefficients and sublevel scale of one opposite-fan arc.

    The arc is

    ``a(t)=A+R*t, c(t)=C-S*t, b(t)=B+L*t+K*t^2``.

    If ``K != 0``, the residual polynomial
    ``8*a(t)*b(t)*c(t)-q^3`` has leading coefficient ``-8*R*S*K``.
    The fixed-degree divided-difference sublevel lemma therefore gives

    ``# {integer t: |residual(t)| <= qD}``
    ``<< 1+(qD/(8*R*S*|K|))^(1/4)``.

    If ``K=0`` and the three factors stay positive and comparable to ``q``,
    the logarithm of their product has second derivative at most
    ``-c*(R^2+S^2+L^2)/q^2``.  Strong concavity instead gives

    ``#t << 1+sqrt(D/(R^2+S^2+L^2))``.

    The displayed scales omit only absolute fixed-degree constants.
    """

    q: int
    aperture: int
    centers: tuple[int, int, int]
    coefficients: tuple[int, int, int, int]
    product_coefficients: tuple[int, int, int, int, int]
    residual_coefficients: tuple[int, int, int, int, int]
    polynomial_degree: int
    leading_coefficient: int
    fourth_difference_coefficient: int
    quartic_sublevel_scale_fourth_power: Fraction | None
    log_concavity_scale_squared: Fraction | None


def opposite_fan_polynomial_arc_ledger(
    q: int,
    aperture: int,
    *,
    first_center: int,
    second_center: int,
    carrier_center: int,
    first_step: int,
    second_step: int,
    carrier_linear_step: int,
    carrier_quadratic_step: int,
) -> OppositeFanPolynomialArcLedger:
    """Return exact polynomial data for an opposite-fan carrier arc."""

    modulus = int(q)
    degree = int(aperture)
    A = int(first_center)
    C = int(second_center)
    B = int(carrier_center)
    R = int(first_step)
    S = int(second_step)
    L = int(carrier_linear_step)
    K = int(carrier_quadratic_step)
    if min(modulus, degree, A, B, C, R, S) <= 0:
        raise ValueError("q, aperture, centers, and fan steps must be positive")

    cross = R * C - A * S
    product_coefficients = (
        A * B * C,
        A * C * L + B * cross,
        A * C * K + L * cross - B * R * S,
        K * cross - L * R * S,
        -K * R * S,
    )
    residual_coefficients = (
        8 * product_coefficients[0] - modulus**3,
        *(8 * coefficient for coefficient in product_coefficients[1:]),
    )
    if K:
        polynomial_degree = 4
        quartic_scale = Fraction(
            modulus * degree,
            abs(residual_coefficients[4]),
        )
        log_scale = None
    else:
        polynomial_degree = 3 if L else 2
        quartic_scale = None
        log_scale = Fraction(degree, R * R + S * S + L * L)
    return OppositeFanPolynomialArcLedger(
        q=modulus,
        aperture=degree,
        centers=(A, C, B),
        coefficients=(R, S, L, K),
        product_coefficients=product_coefficients,
        residual_coefficients=residual_coefficients,
        polynomial_degree=polynomial_degree,
        leading_coefficient=residual_coefficients[polynomial_degree],
        fourth_difference_coefficient=24 * residual_coefficients[4],
        quartic_sublevel_scale_fourth_power=quartic_scale,
        log_concavity_scale_squared=log_scale,
    )


@dataclass(frozen=True)
class ExactQuarticPrimeExclusionLedger:
    """Coprimality obstruction to an exact quartic carrier resonance.

    Vanishing of the linear, quadratic, and cubic product coefficients
    forces

    ``R*C=A*S, L=0, K*A*C=B*R*S``.

    If each of the two affine fans contains two distinct prime powers in a
    shell of endpoint ratio below two, then ``gcd(A,R)=gcd(C,S)=1``.
    The first identity then forces ``A=C`` and ``R=S``; the last one forces
    ``A^2 | B``.  If the resonance centers ``A,B`` lie in the same narrow
    shell, this is impossible for ``A>=2``.
    """

    product_coefficients: tuple[int, int, int, int, int]
    lower_coefficients_vanish: bool
    first_fan_content: int
    second_fan_content: int
    primitive_fan_intercepts: bool
    forced_equal_centers: bool
    forced_equal_steps: bool
    forced_center_square_divides_carrier: bool
    carrier_to_center_ratio: Fraction
    narrow_shell_contradiction: bool


def exact_quartic_prime_exclusion_ledger(
    *,
    first_center: int,
    second_center: int,
    carrier_center: int,
    first_step: int,
    second_step: int,
    carrier_linear_step: int,
    carrier_quadratic_step: int,
) -> ExactQuarticPrimeExclusionLedger:
    """Certify the exact-resonance prime-power non-embedding algebra."""

    A = int(first_center)
    C = int(second_center)
    B = int(carrier_center)
    R = int(first_step)
    S = int(second_step)
    L = int(carrier_linear_step)
    K = int(carrier_quadratic_step)
    if min(A, B, C, R, S, K) <= 0:
        raise ValueError("centers, steps, and quadratic coefficient must be positive")
    cross = R * C - A * S
    coefficients = (
        A * B * C,
        A * C * L + B * cross,
        A * C * K + L * cross - B * R * S,
        K * cross - L * R * S,
        -K * R * S,
    )
    lower_vanish = coefficients[1:4] == (0, 0, 0)
    first_content = math.gcd(A, R)
    second_content = math.gcd(C, S)
    primitive = first_content == second_content == 1
    equal_centers = lower_vanish and primitive and A == C
    equal_steps = lower_vanish and primitive and R == S
    square_divides = (
        lower_vanish
        and primitive
        and B % (A * A) == 0
    )
    if lower_vanish and primitive:
        if not equal_centers or not equal_steps or not square_divides:
            raise AssertionError("exact resonance did not force the divisibility obstruction")
    shell_contradiction = square_divides and A >= 2 and B >= 2 * A
    return ExactQuarticPrimeExclusionLedger(
        product_coefficients=coefficients,
        lower_coefficients_vanish=lower_vanish,
        first_fan_content=first_content,
        second_fan_content=second_content,
        primitive_fan_intercepts=primitive,
        forced_equal_centers=equal_centers,
        forced_equal_steps=equal_steps,
        forced_center_square_divides_carrier=square_divides,
        carrier_to_center_ratio=Fraction(B, A),
        narrow_shell_contradiction=shell_contradiction,
    )


@dataclass(frozen=True)
class ConditionalPolynomialArcCoveringLedger:
    """Active exponents for a conditional polynomial-arc proof of ``(SB)``.

    The unproved input is a uniform covering by ``q^o(1)`` polynomial arcs
    per reduced fan pair.  The proved sublevel estimates above would then
    sum: the random volume is ``D^(15/16)``, nonlinear quadratic-carrier
    arcs contribute ``D^(63/64)``, and the one-per-arc and tangent terms
    contribute ``D``.  Thus that covering input would imply ``(SB)``.
    """

    aperture_exponent_in_q: Fraction
    residual_height_exponent_in_q: Fraction
    random_volume_exponent_in_degree: Fraction
    worst_single_quadratic_arc_exponent_in_q: Fraction
    high_step_quartic_arc_exponent_in_q: Fraction
    linear_carrier_tangent_exponent_in_q: Fraction
    cubic_coefficient_exactness_threshold_in_q: Fraction
    cubic_threshold_gap_over_aperture_in_q: Fraction
    summed_quadratic_arc_exponent_in_degree: Fraction
    summed_quadratic_arc_exponent_in_q: Fraction
    conditional_total_exponent_in_degree: Fraction
    arc_covering_theorem_proved: bool


def conditional_polynomial_arc_covering_ledger(
) -> ConditionalPolynomialArcCoveringLedger:
    """Return the exact exponent ledger for the missing arc covering."""

    degree = Fraction(16, 33)
    residual = 1 + degree
    random_volume = Fraction(15, 16)
    worst_arc = residual / 4
    high_step_arc = (residual - 1) / 4
    tangent = degree / 2
    cubic_threshold = residual / 3
    summed_arc_degree = Fraction(63, 64)
    summed_arc_q = degree * summed_arc_degree
    return ConditionalPolynomialArcCoveringLedger(
        aperture_exponent_in_q=degree,
        residual_height_exponent_in_q=residual,
        random_volume_exponent_in_degree=random_volume,
        worst_single_quadratic_arc_exponent_in_q=worst_arc,
        high_step_quartic_arc_exponent_in_q=high_step_arc,
        linear_carrier_tangent_exponent_in_q=tangent,
        cubic_coefficient_exactness_threshold_in_q=cubic_threshold,
        cubic_threshold_gap_over_aperture_in_q=cubic_threshold - degree,
        summed_quadratic_arc_exponent_in_degree=summed_arc_degree,
        summed_quadratic_arc_exponent_in_q=summed_arc_q,
        conditional_total_exponent_in_degree=Fraction(1),
        arc_covering_theorem_proved=False,
    )


@dataclass(frozen=True)
class DeterminantCellCoveringBarrierLedger:
    """Exponent ledger for four-point coplanarity cells in one fan pair.

    For index side lengths ``H,K`` and physical fan steps ``R,S``, Taylor
    expansion of ``q^3/(8ac)`` and the integral determinant with columns
    ``(1,m,n,b)`` give the sufficient coplanarity scale

    ``H*K*(D+R^2*H^2+R*S*H*K+S^2*K^2) << q``.

    The continuous cell-area optimum is bounded by
    ``H*K ~ sqrt(q/(R*S))`` because ``q*R*S>D^2`` at the active aperture;
    it is attained up to constants in the balanced worst case ``R=S=1``.
    There, cells with at most three points cost ``q^(1/66)`` more than the
    random volume.  This is a barrier to a local-cell proof, not to ``(SB)``.
    """

    aperture_exponent_in_q: Fraction
    random_cell_area_exponent_in_q: Fraction
    largest_coplanar_cell_area_exponent_in_q: Fraction
    isolated_cell_gap_exponent_in_q: Fraction
    maximal_block_sparse_count_exponent_in_q: Fraction
    random_volume_exponent_in_q: Fraction
    maximal_block_sparse_count_exponent_in_degree: Fraction
    random_volume_exponent_in_degree: Fraction
    rich_cell_threshold: int


def determinant_cell_covering_barrier_ledger(
) -> DeterminantCellCoveringBarrierLedger:
    """Return the exact active powers in the coplanarity-cell barrier."""

    degree = Fraction(16, 33)
    random_cell_area = 1 - degree
    coplanar_cell_area = Fraction(1, 2)
    sparse_count = 2 * degree - coplanar_cell_area
    random_volume_q = 3 * degree - 1
    return DeterminantCellCoveringBarrierLedger(
        aperture_exponent_in_q=degree,
        random_cell_area_exponent_in_q=random_cell_area,
        largest_coplanar_cell_area_exponent_in_q=coplanar_cell_area,
        isolated_cell_gap_exponent_in_q=(
            random_cell_area - coplanar_cell_area
        ),
        maximal_block_sparse_count_exponent_in_q=sparse_count,
        random_volume_exponent_in_q=random_volume_q,
        maximal_block_sparse_count_exponent_in_degree=sparse_count / degree,
        random_volume_exponent_in_degree=random_volume_q / degree,
        rich_cell_threshold=4,
    )


@dataclass(frozen=True)
class DeterminantCellStepCutoffLedger:
    """Exact low/high-step powers for the isolated-cell decomposition.

    If a dyadic row/color fan class has ``F_a*M,F_c*N <= D``, its main
    isolated-cell charge is

    ``D^2*sqrt(R*S/q)``.

    It is at most ``D`` exactly in the low-step range
    ``R*S <= q/D^2 = q^(1/33) = D^(1/16)``.  At ``R*S=q^o(1)`` it is
    ``D^(31/32+o(1))``.  Above the cutoff the determinant cells provide
    local three-point nonconcentration, but not an ``O(D)`` count.
    """

    aperture_exponent_in_q: Fraction
    low_step_product_cutoff_exponent_in_q: Fraction
    low_step_product_cutoff_exponent_in_degree: Fraction
    bounded_step_isolated_exponent_in_q: Fraction
    bounded_step_isolated_exponent_in_degree: Fraction
    cutoff_isolated_exponent_in_q: Fraction
    cutoff_isolated_exponent_in_degree: Fraction
    worst_low_step_boundary_exponent_in_q: Fraction
    inherited_cell_occupancy: int


def determinant_cell_step_cutoff_ledger(
) -> DeterminantCellStepCutoffLedger:
    """Return the exact fan-class cutoff for the cell remainder."""

    degree = Fraction(16, 33)
    cutoff = 1 - 2 * degree
    bounded_step = 2 * degree - Fraction(1, 2)
    # At the most anisotropic endpoint R=q^(1/33), S=1, the shorter
    # balanced determinant-cell side has exponent 5/22.  Thus a D-long
    # boundary strip costs q^(16/33-5/22)=q^(17/66), below D.
    worst_boundary = degree - Fraction(5, 22)
    return DeterminantCellStepCutoffLedger(
        aperture_exponent_in_q=degree,
        low_step_product_cutoff_exponent_in_q=cutoff,
        low_step_product_cutoff_exponent_in_degree=cutoff / degree,
        bounded_step_isolated_exponent_in_q=bounded_step,
        bounded_step_isolated_exponent_in_degree=bounded_step / degree,
        cutoff_isolated_exponent_in_q=degree,
        cutoff_isolated_exponent_in_degree=Fraction(1),
        worst_low_step_boundary_exponent_in_q=worst_boundary,
        inherited_cell_occupancy=3,
    )


@dataclass(frozen=True)
class DeterminantLevelStratificationLedger:
    """No-go powers for plane-index stratification in the balanced class.

    The balanced stationary class has ``R=S=q/sqrt(D)`` and
    ``F=M=sqrt(D)`` on both sides.  Taking the largest square index cell
    ``h=M`` leaves ``D`` cells globally.  The determinant range per cell is
    ``q*D``, while at most ``D`` levels can be nonempty because the carrier
    is unique for each of the ``h^2=D`` index pairs.

    Absolute square-root summation over nonempty levels costs ``D^(3/2)``.
    Even granting global orthogonality across all cell-level bins gives
    ``sqrt(D^2)*D=D^2`` for normalized unit separable weights: the first
    factor is the square root of the bin count and the second is the
    coefficient ``L2`` norm.  Thus determinant-level partitioning alone
    does not meet the ``D`` target.
    """

    aperture_exponent_in_q: Fraction
    balanced_step_exponent_in_q: Fraction
    balanced_fan_length_exponent_in_q: Fraction
    balanced_fan_count_exponent_in_q: Fraction
    global_cell_count_exponent_in_degree: Fraction
    determinant_range_exponent_in_q: Fraction
    nonempty_levels_per_cell_exponent_in_degree: Fraction
    absolute_sqrt_nonempty_level_cost_exponent_in_degree: Fraction
    absolute_sqrt_range_cost_exponent_in_q: Fraction
    global_cell_level_bin_sqrt_exponent_in_degree: Fraction
    separable_coefficient_l2_exponent_in_degree: Fraction
    optimistic_global_l2_cost_exponent_in_degree: Fraction
    target_exponent_in_degree: Fraction
    plane_index_preserves_separability: bool
    closes_balanced_high_step: bool


def determinant_level_stratification_ledger(
) -> DeterminantLevelStratificationLedger:
    """Return exact active exponents for the determinant-level no-go."""

    degree = Fraction(16, 33)
    half_degree = degree / 2
    step = 1 - half_degree
    determinant_range = 1 + degree
    absolute_range_cost = degree + determinant_range / 2
    return DeterminantLevelStratificationLedger(
        aperture_exponent_in_q=degree,
        balanced_step_exponent_in_q=step,
        balanced_fan_length_exponent_in_q=half_degree,
        balanced_fan_count_exponent_in_q=half_degree,
        global_cell_count_exponent_in_degree=Fraction(1),
        determinant_range_exponent_in_q=determinant_range,
        nonempty_levels_per_cell_exponent_in_degree=Fraction(1),
        absolute_sqrt_nonempty_level_cost_exponent_in_degree=Fraction(3, 2),
        absolute_sqrt_range_cost_exponent_in_q=absolute_range_cost,
        global_cell_level_bin_sqrt_exponent_in_degree=Fraction(1),
        separable_coefficient_l2_exponent_in_degree=Fraction(1),
        optimistic_global_l2_cost_exponent_in_degree=Fraction(2),
        target_exponent_in_degree=Fraction(1),
        plane_index_preserves_separability=False,
        closes_balanced_high_step=False,
    )


@dataclass(frozen=True)
class CrossCuspKuznetsovAuditLedger:
    """Balanced powers and functional status of the cross-cusp proposal.

    The exact-divisor cusps of level ``N=R*S`` have widths ``S,R``; canonical
    Atkin--Lehner scaling introduces no power loss for one fixed scalar
    large sieve.  What is not formal is the proposed data coefficient
    ``A_pi``.  Hilbert tensorization only applies when every fan twist stays
    as an external orthogonal coordinate of one common scalar transform.

    In the raw Poisson congruence

    ``n == U*r*c-a*k*R (mod c*R)``,

    CRT makes ``(r mod R,k mod c)`` injective when all relevant gcds are
    one, but a length-``K`` dual interval folds ``K/c`` times onto ``k mod
    c``.  In the balanced class this is ``q^(17/33)`` on each side and
    ``B0=q^(34/33)`` jointly.  Recovering the joint factor is a theorem,
    not finite Fourier orthogonality for free.
    """

    aperture_exponent_in_q: Fraction
    fan_count_exponent_in_q: Fraction
    fan_length_exponent_in_q: Fraction
    physical_step_exponent_in_q: Fraction
    level_exponent_in_q: Fraction
    dual_side_exponent_in_q: Fraction
    product_length_exponent_in_q: Fraction
    shift_length_exponent_in_q: Fraction
    delta_modulus_exponent_in_q: Fraction
    one_side_alias_exponent_in_q: Fraction
    joint_alias_exponent_in_q: Fraction
    strong_data_power_exponent_in_q: Fraction
    weakest_data_power_exponent_in_q: Fraction
    translation_norm_fourth_power_exponent_in_q: Fraction
    weakest_total_data_rhs_exponent_in_q: Fraction
    weakest_data_square_root_exponent_in_q: Fraction
    shift_large_sieve_square_root_exponent_in_q: Fraction
    resulting_bound_exponent_in_q: Fraction
    target_exponent_in_q: Fraction
    strong_candidate_bound_exponent_in_q: Fraction
    strong_candidate_margin_exponent_in_q: Fraction
    naive_joint_alias_bound_exponent_in_q: Fraction
    naive_harmonic_diagonal_bound_exponent_in_q: Fraction
    fixed_cusp_width_power_loss: bool
    crt_separates_fan_and_residue_modulo_periods: bool
    long_dual_interval_is_alias_free: bool
    hilbert_tensorization_proves_data_lift: bool
    cross_cusp_closure_proved: bool


def cross_cusp_kuznetsov_audit_ledger(
) -> CrossCuspKuznetsovAuditLedger:
    """Return the exact balanced cross-cusp exponent audit."""

    degree = Fraction(16, 33)
    fan = degree / 2
    step = 1 - fan
    level = 2 * step
    dual = Fraction(42, 33)
    product = 2 * dual
    shift = Fraction(34, 33)
    delta_modulus = level / 2
    alias = dual - delta_modulus
    strong_data = Fraction(4, 3) * product
    weakest_data = 2 * product - shift
    norm_fourth = 4 * fan
    total_data = norm_fourth + weakest_data
    data_root = total_data / 2
    shift_root = shift / 2
    resulting = data_root + shift_root
    strong_bound = norm_fourth / 2 + strong_data / 2 + shift_root
    return CrossCuspKuznetsovAuditLedger(
        aperture_exponent_in_q=degree,
        fan_count_exponent_in_q=fan,
        fan_length_exponent_in_q=fan,
        physical_step_exponent_in_q=step,
        level_exponent_in_q=level,
        dual_side_exponent_in_q=dual,
        product_length_exponent_in_q=product,
        shift_length_exponent_in_q=shift,
        delta_modulus_exponent_in_q=delta_modulus,
        one_side_alias_exponent_in_q=alias,
        joint_alias_exponent_in_q=2 * alias,
        strong_data_power_exponent_in_q=strong_data,
        weakest_data_power_exponent_in_q=weakest_data,
        translation_norm_fourth_power_exponent_in_q=norm_fourth,
        weakest_total_data_rhs_exponent_in_q=total_data,
        weakest_data_square_root_exponent_in_q=data_root,
        shift_large_sieve_square_root_exponent_in_q=shift_root,
        resulting_bound_exponent_in_q=resulting,
        target_exponent_in_q=norm_fourth / 2 + product,
        strong_candidate_bound_exponent_in_q=strong_bound,
        strong_candidate_margin_exponent_in_q=resulting - strong_bound,
        naive_joint_alias_bound_exponent_in_q=resulting + shift_root,
        naive_harmonic_diagonal_bound_exponent_in_q=resulting + level / 2,
        fixed_cusp_width_power_loss=False,
        crt_separates_fan_and_residue_modulo_periods=True,
        long_dual_interval_is_alias_free=False,
        hilbert_tensorization_proves_data_lift=False,
        cross_cusp_closure_proved=False,
    )


@dataclass(frozen=True)
class IntermodulusCRTAuditLedger:
    """Exact powers for the inter-modulus CRT large-sieve obstruction.

    At delta modulus ``c`` the normalized Poisson frequency is

    ``U*r/R-a*k/c (mod 1)``.

    The rays ``k=t*c`` are independent of ``c`` modulo one.  Equivalently,
    the raw residue ``n=U*r*c-a*k*R`` conductor-lowers to
    ``n/c=U*r-a*t*R`` on every modulus.  Hence the cross-Gram
    ``U_c^*U_c'`` contains an identity block after identifying
    ``(r,t*c)`` with ``(r,t*c')``.  A family of ``C`` coprime moduli has a
    Gram eigenvalue ``C`` and cannot yield a uniform power saving over
    ``C`` without first projecting or cancelling this coherent subspace.
    """

    delta_modulus_exponent_in_q: Fraction
    long_dual_quotient_exponent_in_q: Fraction
    target_squared_saving_exponent_in_q: Fraction
    desired_gram_constant_exponent_in_q: Fraction
    coherent_gram_eigenvalue_exponent_in_q: Fraction
    gram_exponent_miss_in_q: Fraction
    conditional_hecke_fold_length_exponent_in_q: Fraction
    spectral_level_exponent_in_q: Fraction
    weakest_data_power_exponent_in_q: Fraction
    coherent_ray_survives_conductor_lowering: bool
    uniform_intermodulus_saving_holds: bool
    hecke_fold_valid_if_product_formula_holds: bool
    conductor_lowered_product_formula_proved: bool
    oldform_and_eisenstein_fold_automatic: bool


def intermodulus_crt_audit_ledger() -> IntermodulusCRTAuditLedger:
    """Return the exact coherent-ray and Hecke-fold status ledger."""

    delta_modulus = Fraction(25, 33)
    quotient = Fraction(17, 33)
    saving = Fraction(1, 11)
    level = 2 * delta_modulus
    product_length = Fraction(84, 33)
    shift = Fraction(34, 33)
    return IntermodulusCRTAuditLedger(
        delta_modulus_exponent_in_q=delta_modulus,
        long_dual_quotient_exponent_in_q=quotient,
        target_squared_saving_exponent_in_q=saving,
        desired_gram_constant_exponent_in_q=delta_modulus - saving,
        coherent_gram_eigenvalue_exponent_in_q=delta_modulus,
        gram_exponent_miss_in_q=saving,
        conditional_hecke_fold_length_exponent_in_q=Fraction(16, 33),
        spectral_level_exponent_in_q=level,
        weakest_data_power_exponent_in_q=2 * product_length - shift,
        coherent_ray_survives_conductor_lowering=True,
        uniform_intermodulus_saving_holds=False,
        hecke_fold_valid_if_product_formula_holds=True,
        conductor_lowered_product_formula_proved=False,
        oldform_and_eisenstein_fold_automatic=False,
    )


@dataclass(frozen=True)
class DeltaNormalizationAuditLedger:
    """Exact balanced powers omitted by a schematic delta/CRT ledger.

    In the standard DFI normalization the delta symbol has prefactor
    ``C^(-2)``.  On a top block ``c asymp C`` this is equivalently an outer
    ``C^(-1)`` average times a reciprocal-modulus ``c^(-1)`` weight.  The
    row Poisson lattice has period ``cR`` and prefactor ``J/(cR)`` before
    its complete residue sum; relative to normalized finite Fourier
    coordinates the resulting multiplier is ``J/sqrt(cR)``.

    A second Poisson transform cancels the raw first-step quotient and gives
    the exact prefactor ``J*K/c``.  This repairs that particular objection
    for a fully separable, smooth top-modulus term.  It does not prove an
    estimate: the transformed congruence classes, archimedean weights,
    lower delta-modulus blocks, and zero axes still require uniform bounds.
    The status fields record those proof gaps rather than treating their
    exponent ledger as a theorem.
    """

    aperture_exponent_in_q: Fraction
    kernel_block_length_exponent_in_q: Fraction
    fan_count_exponent_in_q: Fraction
    physical_step_exponent_in_q: Fraction
    spectral_level_exponent_in_q: Fraction
    dual_side_length_exponent_in_q: Fraction
    shift_length_exponent_in_q: Fraction
    delta_modulus_exponent_in_q: Fraction
    dfi_top_block_weight_exponent_in_q: Fraction
    dfi_outer_average_exponent_in_q: Fraction
    dfi_reciprocal_modulus_exponent_in_q: Fraction
    dfi_mismatch_argument_exponent_in_q: Fraction
    row_poisson_period_exponent_in_q: Fraction
    row_poisson_lattice_prefactor_exponent_in_q: Fraction
    normalized_row_fourier_multiplier_exponent_in_q: Fraction
    long_quotient_exponent_in_q: Fraction
    two_row_multiplier_exponent_in_q: Fraction
    two_dimensional_lattice_prefactor_exponent_in_q: Fraction
    complete_bilinear_sum_exponent_in_q: Fraction
    full_two_dimensional_poisson_prefactor_exponent_in_q: Fraction
    top_block_two_copy_outer_prefactor_exponent_in_q: Fraction
    normalized_nondegenerate_weil_exponent_in_q: Fraction
    cauchy_joint_support_exponent_in_q: Fraction
    random_joint_support_required_exponent_in_q: Fraction
    top_block_parseval_bound_exponent_in_q: Fraction
    hsm_correlation_target_exponent_in_q: Fraction
    top_block_parseval_gap_exponent_in_q: Fraction
    aligned_single_modulus_support_exponent_in_q: Fraction
    aligned_support_excess_over_random_target_exponent_in_q: Fraction
    desired_intermodulus_gram_exponent_in_q: Fraction
    flat_single_fan_energy_saving_exponent_in_q: Fraction
    exact_dfi_uses_only_top_moduli: bool
    zero_phase_forces_one_fan_when_coprime: bool
    flat_coefficients_gain_single_fan_density: bool
    uniform_l2_coefficients_gain_single_fan_density: bool
    full_two_dimensional_poisson_removes_first_step_quotient: bool
    one_sided_zero_becomes_kloosterman_after_full_transform: bool
    ramanujan_zero_axes_extracted: bool
    support_cauchy_and_fixed_c_parseval_close_top_block: bool
    support_only_random_joint_bound_holds_uniformly: bool
    farey_burgess_composition_proved: bool
    jutila_error_resolved: bool
    stationary_boundary_terms_resolved: bool
    eisenstein_terms_resolved: bool
    high_step_hsm_proved: bool


def delta_normalization_audit_ledger() -> DeltaNormalizationAuditLedger:
    """Return the exact DFI and row-Poisson exponent audit."""

    degree = Fraction(16, 33)
    kernel_length = 1 - degree
    fan_count = degree / 2
    step = 1 - fan_count
    level = 2 * step
    dual = Fraction(42, 33)
    shift = Fraction(34, 33)
    delta_modulus = level / 2
    row_period = delta_modulus + step
    normalized_row_multiplier = dual - row_period / 2
    two_dimensional_lattice = 2 * dual - 2 * row_period
    complete_bilinear_sum = delta_modulus + level
    full_poisson = two_dimensional_lattice + complete_bilinear_sum
    product_length = 2 * dual
    joint_support = 2 * fan_count
    required_joint_support = joint_support + 3 * delta_modulus - product_length
    parseval_bound = joint_support + 2 * product_length - 3 * delta_modulus
    correlation_target = joint_support + product_length
    return DeltaNormalizationAuditLedger(
        aperture_exponent_in_q=degree,
        kernel_block_length_exponent_in_q=kernel_length,
        fan_count_exponent_in_q=fan_count,
        physical_step_exponent_in_q=step,
        spectral_level_exponent_in_q=level,
        dual_side_length_exponent_in_q=dual,
        shift_length_exponent_in_q=shift,
        delta_modulus_exponent_in_q=delta_modulus,
        dfi_top_block_weight_exponent_in_q=-2 * delta_modulus,
        dfi_outer_average_exponent_in_q=-delta_modulus,
        dfi_reciprocal_modulus_exponent_in_q=-delta_modulus,
        dfi_mismatch_argument_exponent_in_q=shift - 2 * delta_modulus,
        row_poisson_period_exponent_in_q=row_period,
        row_poisson_lattice_prefactor_exponent_in_q=dual - row_period,
        normalized_row_fourier_multiplier_exponent_in_q=(
            normalized_row_multiplier
        ),
        long_quotient_exponent_in_q=dual - delta_modulus,
        two_row_multiplier_exponent_in_q=2 * normalized_row_multiplier,
        two_dimensional_lattice_prefactor_exponent_in_q=(
            two_dimensional_lattice
        ),
        complete_bilinear_sum_exponent_in_q=complete_bilinear_sum,
        full_two_dimensional_poisson_prefactor_exponent_in_q=(
            full_poisson
        ),
        top_block_two_copy_outer_prefactor_exponent_in_q=(
            -delta_modulus + 2 * full_poisson
        ),
        normalized_nondegenerate_weil_exponent_in_q=-delta_modulus / 2,
        cauchy_joint_support_exponent_in_q=joint_support,
        random_joint_support_required_exponent_in_q=required_joint_support,
        top_block_parseval_bound_exponent_in_q=parseval_bound,
        hsm_correlation_target_exponent_in_q=correlation_target,
        top_block_parseval_gap_exponent_in_q=parseval_bound - correlation_target,
        aligned_single_modulus_support_exponent_in_q=joint_support,
        aligned_support_excess_over_random_target_exponent_in_q=(
            joint_support - required_joint_support
        ),
        desired_intermodulus_gram_exponent_in_q=(
            delta_modulus - Fraction(1, 11)
        ),
        flat_single_fan_energy_saving_exponent_in_q=fan_count,
        exact_dfi_uses_only_top_moduli=False,
        zero_phase_forces_one_fan_when_coprime=True,
        flat_coefficients_gain_single_fan_density=True,
        uniform_l2_coefficients_gain_single_fan_density=False,
        full_two_dimensional_poisson_removes_first_step_quotient=True,
        one_sided_zero_becomes_kloosterman_after_full_transform=True,
        ramanujan_zero_axes_extracted=False,
        support_cauchy_and_fixed_c_parseval_close_top_block=False,
        support_only_random_joint_bound_holds_uniformly=False,
        farey_burgess_composition_proved=False,
        jutila_error_resolved=False,
        stationary_boundary_terms_resolved=False,
        eisenstein_terms_resolved=False,
        high_step_hsm_proved=False,
    )


def aligned_modulus_support_counts(
    row_step: int,
    row_fan_count: int,
    color_fan_count: int,
) -> tuple[int, int, int]:
    """Return the exact support counts in the aligned ``S=R+1`` fixture.

    Take odd ``R``, ``S=R+1``, ``c=S+1``, and the Bezout pair
    ``U=R-1,V=R``.  Then ``R*V-S*U=1``, while the transformed congruences
    are ``nu=-2r (mod R)`` and ``mu=-s (mod S)``.  The frequency windows
    are taken to be ``|nu|<=P`` and ``|mu|<=Q``.  One admissible modulus
    therefore carries a positive proportion of the whole ``P*Q`` support.
    """

    R = int(row_step)
    P = int(row_fan_count)
    Q = int(color_fan_count)
    if R <= 1 or R % 2 == 0:
        raise ValueError("row step must be an odd integer greater than one")
    if min(P, Q) <= 0 or 2 * P >= R or Q >= R + 1:
        raise ValueError("fan windows must lie inside the centered residues")
    S = R + 1
    c = S + 1
    U = R - 1
    V = R

    def centered(value: int, modulus: int) -> int:
        residue = value % modulus
        if 2 * residue > modulus:
            residue -= modulus
        return residue

    row_support = sum(
        abs(centered(U * r * c, R)) <= P for r in range(P)
    )
    color_support = sum(
        abs(centered(V * s * c, S)) <= Q for s in range(Q)
    )
    return row_support, color_support, row_support * color_support


def bilinear_complete_sum_prediction(
    delta_modulus: int,
    row_step: int,
    color_step: int,
    delta_numerator: int,
    row_bezout: int,
    color_bezout: int,
    row_fan: int,
    color_fan: int,
    row_frequency: int,
    color_frequency: int,
) -> tuple[int, int]:
    """Predict the exact complete sum in the two-dimensional Poisson step.

    With ``c=delta_modulus``, the complete sum over
    ``x mod cR, y mod cS`` has phase

    ``e_c(a*x*y-U0*r*x*c/R-V0*s*y*c/S)``

    together with Fourier phases ``e_(cR)(nu*x)e_(cS)(mu*y)``.  It vanishes
    unless ``nu=U0*r*c (mod R)`` and ``mu=V0*s*c (mod S)``.  On that support
    its amplitude is ``c*R*S`` and its phase numerator modulo ``c`` is

    ``-inverse(a)*inverse(R*S)*nu*mu``.

    Returning the amplitude and phase numerator avoids floating-point
    arithmetic in the audited identity itself.
    """

    c = int(delta_modulus)
    R = int(row_step)
    S = int(color_step)
    a = int(delta_numerator)
    U0 = int(row_bezout)
    V0 = int(color_bezout)
    r = int(row_fan)
    s = int(color_fan)
    nu = int(row_frequency)
    mu = int(color_frequency)
    if min(c, R, S) <= 0:
        raise ValueError("moduli must be positive")
    if math.gcd(c, R * S) != 1 or math.gcd(a, c) != 1:
        raise ValueError("the complete-sum formula requires coprime data")
    if (nu - U0 * r * c) % R or (mu - V0 * s * c) % S:
        return 0, 0
    phase = (-pow(a, -1, c) * pow(R * S, -1, c) * nu * mu) % c
    return c * R * S, phase


@dataclass(frozen=True)
class BProcessBoundaryAuditLedger:
    """Exact active powers in the unresolved fan-endpoint B-process term.

    Low modes ``ell<=q/D^2`` cost ``q`` before the Selberg factor by the
    trivial ``D^2`` bound.  The coherent interior ledger also costs ``q``.
    A sequential one-dimensional B-process, however, leaves an endpoint and
    transition error for every value of the untransformed fan coordinate.
    In a class with ``P*L_a,Q*L_c<=D`` its best ordering costs

    ``min(P*Q*L_a,P*Q*L_c) <= D*min(P,Q) <= D^(3/2)``

    per mode, using ``P*Q<=D``.  The balanced class attains the exponent.
    Summing ``q/D`` modes and multiplying by the Selberg coefficient ``D/q``
    leaves ``D^(3/2)``, a ``sqrt(D)`` loss.  This is a proof-method gap, not
    a lower bound for the actual boundary contribution.
    """

    aperture_exponent_in_q: Fraction
    low_mode_cutoff_exponent_in_q: Fraction
    low_mode_raw_sum_exponent_in_q: Fraction
    coherent_interior_raw_sum_exponent_in_q: Fraction
    balanced_boundary_per_mode_exponent_in_q: Fraction
    selberg_mode_count_exponent_in_q: Fraction
    boundary_raw_sum_exponent_in_q: Fraction
    selberg_coefficient_exponent_in_q: Fraction
    boundary_weighted_exponent_in_q: Fraction
    target_weighted_exponent_in_q: Fraction
    boundary_loss_exponent_in_q: Fraction
    boundary_loss_exponent_in_degree: Fraction
    low_modes_close: bool
    coherent_interior_closes: bool
    endpoint_terms_close: bool
    high_step_b_process_closes: bool


def b_process_boundary_audit_ledger() -> BProcessBoundaryAuditLedger:
    """Return the exact balanced endpoint-loss ledger."""

    degree = Fraction(16, 33)
    low_cutoff = 1 - 2 * degree
    per_mode = Fraction(3, 2) * degree
    mode_count = 1 - degree
    raw = per_mode + mode_count
    selberg = degree - 1
    weighted = raw + selberg
    return BProcessBoundaryAuditLedger(
        aperture_exponent_in_q=degree,
        low_mode_cutoff_exponent_in_q=low_cutoff,
        low_mode_raw_sum_exponent_in_q=Fraction(1),
        coherent_interior_raw_sum_exponent_in_q=Fraction(1),
        balanced_boundary_per_mode_exponent_in_q=per_mode,
        selberg_mode_count_exponent_in_q=mode_count,
        boundary_raw_sum_exponent_in_q=raw,
        selberg_coefficient_exponent_in_q=selberg,
        boundary_weighted_exponent_in_q=weighted,
        target_weighted_exponent_in_q=degree,
        boundary_loss_exponent_in_q=weighted - degree,
        boundary_loss_exponent_in_degree=(weighted - degree) / degree,
        low_modes_close=True,
        coherent_interior_closes=True,
        endpoint_terms_close=False,
        high_step_b_process_closes=False,
    )


@dataclass(frozen=True)
class PositiveRectangularCompletionLedger:
    """Power ledger for the positive rectangular fan completion.

    The sharp sequential B-process still has the endpoint loss recorded by
    :func:`b_process_boundary_audit_ledger`.  For the *positive* Selberg
    count one may instead fill the quotient fan interval and put a fixed
    smooth majorant on the physical shell coordinate.  If the fan step is
    ``R>=q/D`` and its quotient count is ``P<<1+R*D/q``, the completed row
    support has

    ``P*(1+q/R) << (1+R*D/q)*(1+q/R) << D``.

    Poisson summation is then performed only in the long fan coordinate;
    the quotient index remains an external Dirichlet weight.  Thus no
    fanwise endpoint chart is created.  This removes the boundary gate
    conditional on the same diagonal-strength HSM estimate required for
    the smooth interior; it does not prove that HSM estimate.
    """

    aperture_exponent_in_q: Fraction
    minimum_relevant_step_exponent_in_q: Fraction
    balanced_step_exponent_in_q: Fraction
    balanced_fan_count_exponent_in_q: Fraction
    balanced_completed_fan_length_exponent_in_q: Fraction
    completed_strip_size_exponent_in_q: Fraction
    zero_mode_exponent_in_q: Fraction
    conditional_raw_hsm_exponent_in_q: Fraction
    conditional_weighted_exponent_in_q: Fraction
    positive_completion_is_size_safe: bool
    physical_cutoff_can_be_slow_and_smooth: bool
    quotient_weights_remain_external_and_separable: bool
    fanwise_fresnel_charts_are_absent: bool
    boundary_gate_closes_conditionally_on_hsm: bool
    high_step_hsm_proved: bool


def positive_rectangular_completion_ledger() -> PositiveRectangularCompletionLedger:
    """Return exact powers for the boundary-free positive completion.

    In the balanced class ``R=S=q/sqrt(D)`` and both the fan count and the
    completed fan length are ``sqrt(D)``.  Their product is still ``D``.
    The Selberg zero mode remains ``D^3/q``.  A raw ``O(q)`` smooth-HSM
    estimate would therefore give the target ``O(D)`` after multiplication
    by ``D/q``, with no additional endpoint term.
    """

    degree = Fraction(16, 33)
    minimum_step = 1 - degree
    balanced_step = 1 - degree / 2
    square_root_degree = degree / 2
    zero_mode = 3 * degree - 1
    return PositiveRectangularCompletionLedger(
        aperture_exponent_in_q=degree,
        minimum_relevant_step_exponent_in_q=minimum_step,
        balanced_step_exponent_in_q=balanced_step,
        balanced_fan_count_exponent_in_q=square_root_degree,
        balanced_completed_fan_length_exponent_in_q=square_root_degree,
        completed_strip_size_exponent_in_q=degree,
        zero_mode_exponent_in_q=zero_mode,
        conditional_raw_hsm_exponent_in_q=Fraction(1),
        conditional_weighted_exponent_in_q=degree,
        positive_completion_is_size_safe=True,
        physical_cutoff_can_be_slow_and_smooth=True,
        quotient_weights_remain_external_and_separable=True,
        fanwise_fresnel_charts_are_absent=True,
        boundary_gate_closes_conditionally_on_hsm=True,
        high_step_hsm_proved=False,
    )


@dataclass(frozen=True)
class HSMArcInverseObstructionLedger:
    """Exact gates blocking an HSM-excess-to-actual-arc inverse proof.

    Positivity-first rectangular completion is a valid upper-bound device,
    but its Poisson data contain the filled quotient intervals rather than
    the original prime-power masks.  It is therefore not an invertible
    transference step: a resonance of the completed HSM need not carry any
    original edge mass.

    The terminal quartic exclusion also needs exact vanishing of the lower
    coefficients.  Interpolation at the full aperture ``N=D=q^(48/99)``
    only bounds the cubic coefficient by ``q/D^2=q^(1/33)``; integrality
    would require ``N>(qD)^(1/3)=q^(49/99)``.

    Finally, the Fouvry--Radziwill ``17/33`` theorem is an averaged-modulus
    level-of-distribution result for an unbalanced convolution with a
    Siegel--Walfisz factor.  It is not a fixed-level estimate for the
    balanced shifted multiplication-table HSM.  On the natural product
    scale ``X=q^(84/33)``, the cross-cusp level is
    ``N=q^(50/33)=X^(25/42)``, strictly above ``X^(17/33)``.
    """

    aperture_exponent_in_q: Fraction
    selberg_frequency_exponent_in_q: Fraction
    hsm_product_scale_exponent_in_q: Fraction
    cross_cusp_level_exponent_in_q: Fraction
    cross_cusp_level_exponent_in_product_scale: Fraction
    fouvry_radziwill_level_exponent: Fraction
    cross_cusp_excess_over_fr_level: Fraction
    exact_quartic_threshold_exponent_in_q: Fraction
    quartic_integrality_gap_exponent_in_q: Fraction
    classical_hsm_gap_exponent_in_q: Fraction
    positive_completion_retains_actual_node_mask: bool
    completed_hsm_excess_forces_original_arc_mass: bool
    fixed_direction_merger_controls_all_directions: bool
    exact_quartic_exclusion_controls_approximate_arcs: bool
    fouvry_radziwill_supplies_hsm: bool
    full_fc_inverse_route_closes: bool


def hsm_arc_inverse_obstruction_ledger() -> HSMArcInverseObstructionLedger:
    """Return exact powers for the failed HSM-to-primal inverse route."""

    degree = Fraction(16, 33)
    product_scale = Fraction(84, 33)
    cross_cusp_level = Fraction(50, 33)
    cross_cusp_relative = cross_cusp_level / product_scale
    fr_level = Fraction(17, 33)
    quartic_threshold = (1 + degree) / 3
    return HSMArcInverseObstructionLedger(
        aperture_exponent_in_q=degree,
        selberg_frequency_exponent_in_q=1 - degree,
        hsm_product_scale_exponent_in_q=product_scale,
        cross_cusp_level_exponent_in_q=cross_cusp_level,
        cross_cusp_level_exponent_in_product_scale=cross_cusp_relative,
        fouvry_radziwill_level_exponent=fr_level,
        cross_cusp_excess_over_fr_level=cross_cusp_relative - fr_level,
        exact_quartic_threshold_exponent_in_q=quartic_threshold,
        quartic_integrality_gap_exponent_in_q=quartic_threshold - degree,
        classical_hsm_gap_exponent_in_q=Fraction(2, 11),
        positive_completion_retains_actual_node_mask=False,
        completed_hsm_excess_forces_original_arc_mass=False,
        fixed_direction_merger_controls_all_directions=False,
        exact_quartic_exclusion_controls_approximate_arcs=False,
        fouvry_radziwill_supplies_hsm=False,
        full_fc_inverse_route_closes=False,
    )


@dataclass(frozen=True)
class HSMStationaryPacketAuditLedger:
    """Certified exponent and status ledger for completed HSM tangencies.

    Put ``D=q^(16/33)`` and use the balanced stationary block

    ``P=Q=sqrt(D), R=S=q/sqrt(D), L=q/D, J=K=q^2/D^(3/2)``.

    The exact stationary center is principal and proportional.  The
    ``completed_tangent_absolute_*`` fields instead describe what remains
    after taking absolute values *before* the signed ``K_L`` sum.  There are
    ``B0/S=L/P=q^(3/11)`` aligned shift packets, so this method permits that
    loss over the HSM target.  It is not a lower bound for the HSM quadratic
    form: ``K_L/L`` is a signed Fourier kernel on the scale ``h/B0``.
    """

    degree_exponent_in_q: Fraction
    fan_length_exponent_in_q: Fraction
    physical_step_exponent_in_q: Fraction
    ell_block_exponent_in_q: Fraction
    dual_side_exponent_in_q: Fraction
    product_scale_exponent_in_q: Fraction
    short_shift_exponent_in_q: Fraction
    primitive_zero_quotient_multiplier_exponent_in_q: Fraction
    stationary_tube_cross_bound_exponent_in_q: Fraction
    pair_weight_l2_exponent_in_q: Fraction
    hsm_target_exponent_in_q: Fraction
    completed_tangent_packet_loss_exponent_in_q: Fraction
    completed_tangent_absolute_exponent_in_q: Fraction
    parabolic_chart_exponent_in_degree: Fraction
    parabolic_chart_exponent_in_q: Fraction
    zero_quotient_primitive_multiplicity_cap: int
    physical_zero_quotient_is_excisable: bool
    stationary_tube_locks_principal_fan_relation: bool
    primitive_stationary_center_is_diagonal: bool
    completed_tangent_absolute_barrier_certified: bool
    completed_tangent_is_hsm_lower_bound: bool
    full_short_shift_kernel_is_nonnegative: bool
    exact_nonprincipal_alias_exists: bool
    parabolic_chart_bound_proved: bool
    mask_sensitive_packet_covering_proved: bool
    positive_completion_retains_actual_mask: bool
    full_weighted_hsm_proved: bool
    slope_block_bound_proved: bool
    four_cycle_bound_proved: bool


def hsm_stationary_packet_audit_ledger() -> HSMStationaryPacketAuditLedger:
    """Return the exact balanced stationary-packet powers and proof status."""

    degree = Fraction(16, 33)
    fan = degree / 2
    physical_step = 1 - fan
    ell_block = 1 - degree
    dual_side = ell_block + physical_step
    product_scale = 2 * dual_side
    short_shift = ell_block + 2 * physical_step - 1
    pair_weight_l2 = degree + product_scale
    hsm_target = ell_block + pair_weight_l2
    packet_loss = short_shift - physical_step
    return HSMStationaryPacketAuditLedger(
        degree_exponent_in_q=degree,
        fan_length_exponent_in_q=fan,
        physical_step_exponent_in_q=physical_step,
        ell_block_exponent_in_q=ell_block,
        dual_side_exponent_in_q=dual_side,
        product_scale_exponent_in_q=product_scale,
        short_shift_exponent_in_q=short_shift,
        primitive_zero_quotient_multiplier_exponent_in_q=fan,
        stationary_tube_cross_bound_exponent_in_q=fan - ell_block,
        pair_weight_l2_exponent_in_q=pair_weight_l2,
        hsm_target_exponent_in_q=hsm_target,
        completed_tangent_packet_loss_exponent_in_q=packet_loss,
        completed_tangent_absolute_exponent_in_q=hsm_target + packet_loss,
        parabolic_chart_exponent_in_degree=Fraction(5, 4),
        parabolic_chart_exponent_in_q=Fraction(5, 4) * degree,
        zero_quotient_primitive_multiplicity_cap=1,
        physical_zero_quotient_is_excisable=True,
        stationary_tube_locks_principal_fan_relation=True,
        primitive_stationary_center_is_diagonal=True,
        completed_tangent_absolute_barrier_certified=True,
        completed_tangent_is_hsm_lower_bound=False,
        full_short_shift_kernel_is_nonnegative=False,
        exact_nonprincipal_alias_exists=True,
        parabolic_chart_bound_proved=True,
        mask_sensitive_packet_covering_proved=False,
        positive_completion_retains_actual_mask=False,
        full_weighted_hsm_proved=False,
        slope_block_bound_proved=False,
        four_cycle_bound_proved=False,
    )


@dataclass(frozen=True)
class HSMUniformClosureRouteAuditLedger:
    """Exact powers for three failed uniform HSM promotion shortcuts.

    The scalar BBLR error is smaller than the fixed-short-shift target, but
    has only ``q^(1/11)`` headroom and is not stable under the four fan
    weights.  Positive ``SL_2`` orbit summation has a populated ``d=1``
    zero-residue floor.  Finally, ordinary decoupling loses more than the
    degree budget, while the finer approximate-energy refinement suggested
    by Farey occupancy is false without multiscale tangent control.
    """

    degree_exponent_in_q: Fraction
    fan_exponent_in_q: Fraction
    physical_step_exponent_in_q: Fraction
    dual_side_exponent_in_q: Fraction
    short_shift_exponent_in_q: Fraction
    fixed_short_shift_target_exponent_in_q: Fraction
    scalar_bblr_error_exponent_in_q: Fraction
    scalar_bblr_headroom_exponent_in_q: Fraction
    sqrt_degree_lift_exponent_in_q: Fraction
    sqrt_degree_lift_excess_exponent_in_q: Fraction
    full_degree_lift_exponent_in_q: Fraction
    full_degree_lift_excess_exponent_in_q: Fraction
    restricted_positive_target_exponent_in_q: Fraction
    restricted_zero_residue_floor_exponent_in_q: Fraction
    restricted_zero_residue_excess_exponent_in_q: Fraction
    flat_coefficient_alias_exponent_in_q: Fraction
    flat_coefficient_alias_excess_exponent_in_q: Fraction
    standard_decoupling_squared_loss_exponent_in_q: Fraction
    standard_decoupling_budget_excess_exponent_in_q: Fraction
    farey_fine_tube_occupancy_exponent_in_q: Fraction
    required_fine_tube_occupancy_exponent_in_q: Fraction
    conditional_incidence_squared_loss_exponent_in_q: Fraction
    conditional_incidence_margin_exponent_in_q: Fraction
    positive_restricted_l1_target_is_true: bool
    scalar_bblr_accepts_four_fan_weights: bool
    ordinary_decoupling_closes_hsm: bool
    exact_ruling_sparsity_implies_approximate_energy: bool
    mask_preserving_energy_reduction_proved: bool
    signed_uniform_hsm_proved: bool
    uniform_four_cycle_proved: bool


def hsm_uniform_closure_route_audit_ledger(
) -> HSMUniformClosureRouteAuditLedger:
    """Return the exact exponent ledger for the final uniform-route audit."""

    degree = Fraction(16, 33)
    fan = degree / 2
    physical_step = 1 - fan
    dual_side = Fraction(42, 33)
    short_shift = Fraction(34, 33)
    fixed_target = degree + 2 * dual_side
    bblr_error = Fraction(3, 2) * dual_side + short_shift
    sqrt_lift = bblr_error + fan
    full_lift = bblr_error + degree
    restricted_target = degree + 2 * dual_side - short_shift
    restricted_floor = degree + 2 * dual_side - physical_step
    flat_alias = restricted_floor + fan
    standard_decoupling_squared = dual_side / 2
    fine_occupancy = 2 - dual_side
    required_occupancy = 2 * degree
    conditional_incidence_squared = fine_occupancy / 2
    return HSMUniformClosureRouteAuditLedger(
        degree_exponent_in_q=degree,
        fan_exponent_in_q=fan,
        physical_step_exponent_in_q=physical_step,
        dual_side_exponent_in_q=dual_side,
        short_shift_exponent_in_q=short_shift,
        fixed_short_shift_target_exponent_in_q=fixed_target,
        scalar_bblr_error_exponent_in_q=bblr_error,
        scalar_bblr_headroom_exponent_in_q=fixed_target - bblr_error,
        sqrt_degree_lift_exponent_in_q=sqrt_lift,
        sqrt_degree_lift_excess_exponent_in_q=sqrt_lift - fixed_target,
        full_degree_lift_exponent_in_q=full_lift,
        full_degree_lift_excess_exponent_in_q=full_lift - fixed_target,
        restricted_positive_target_exponent_in_q=restricted_target,
        restricted_zero_residue_floor_exponent_in_q=restricted_floor,
        restricted_zero_residue_excess_exponent_in_q=(
            restricted_floor - restricted_target
        ),
        flat_coefficient_alias_exponent_in_q=flat_alias,
        flat_coefficient_alias_excess_exponent_in_q=(
            flat_alias - restricted_target
        ),
        standard_decoupling_squared_loss_exponent_in_q=(
            standard_decoupling_squared
        ),
        standard_decoupling_budget_excess_exponent_in_q=(
            standard_decoupling_squared - degree
        ),
        farey_fine_tube_occupancy_exponent_in_q=fine_occupancy,
        required_fine_tube_occupancy_exponent_in_q=required_occupancy,
        conditional_incidence_squared_loss_exponent_in_q=(
            conditional_incidence_squared
        ),
        conditional_incidence_margin_exponent_in_q=(
            degree - conditional_incidence_squared
        ),
        positive_restricted_l1_target_is_true=False,
        scalar_bblr_accepts_four_fan_weights=False,
        ordinary_decoupling_closes_hsm=False,
        exact_ruling_sparsity_implies_approximate_energy=False,
        mask_preserving_energy_reduction_proved=False,
        signed_uniform_hsm_proved=False,
        uniform_four_cycle_proved=False,
    )


def zero_quotient_content(
    multiplier: int, row_step: int, color_step: int
) -> int:
    """Return the gcd of ``multiplier*(row_step, color_step)``.

    The quotient chart uses a Bezout pair of steps, so they must be
    coprime.  Consequently the returned content is exactly ``|multiplier|``.
    A positive primitive zero-quotient point can therefore occur only for
    ``multiplier=1`` and can be removed before rectangular completion.
    """

    m = int(multiplier)
    R = int(row_step)
    S = int(color_step)
    if R <= 0 or S <= 0 or math.gcd(R, S) != 1:
        raise ValueError("row and color steps must be positive and coprime")
    content = math.gcd(abs(m * R), abs(m * S))
    if content != abs(m):
        raise AssertionError("the zero-quotient content identity failed")
    return content


def stationary_fan_cross_identity(
    row_fan: int,
    other_row_fan: int,
    color_fan: int,
    other_color_fan: int,
    product_ratio: Fraction,
) -> Fraction:
    """Replay the exact fan determinant identity in the stationary tube.

    If ``u`` is the product-fibre ratio, then

    ``r*s-r'*s' = r*(s-s'*u)+s'*(r*u-r')``.

    Thus the two stationary errors, each ``O(1/L)``, bound the integral
    left side by ``O(P/L)=o(1)`` and force ``r*s=r'*s'``.
    """

    r = int(row_fan)
    rp = int(other_row_fan)
    s = int(color_fan)
    sp = int(other_color_fan)
    u = Fraction(product_ratio)
    decomposed = r * (s - sp * u) + sp * (r * u - rp)
    exact = Fraction(r * s - rp * sp)
    if decomposed != exact:
        raise AssertionError("the stationary fan cross identity failed")
    return decomposed


def quotient_proportionality_identity(
    step: int,
    bezout_coordinate: int,
    multiplier: int,
    fan: int,
    other_multiplier: int,
    other_fan: int,
) -> tuple[int, int]:
    """Return both equal sides of the quotient proportionality identity.

    For ``a=R*m+U*r`` and ``a'=R*m'+U*r'``, the stationary ratio
    ``a'/a=r'/r`` is equivalent to

    ``r*a'-r'*a = R*(r*m'-r'*m)``.

    On positive primitive quotient pairs, simultaneous row and color
    proportionality therefore forces the two pairs to coincide.
    """

    R = int(step)
    U = int(bezout_coordinate)
    m = int(multiplier)
    r = int(fan)
    mp = int(other_multiplier)
    rp = int(other_fan)
    if R <= 0:
        raise ValueError("the quotient step must be positive")
    a = R * m + U * r
    ap = R * mp + U * rp
    expanded = r * ap - rp * a
    reduced = R * (r * mp - rp * m)
    if expanded != reduced:
        raise AssertionError("the quotient proportionality identity failed")
    return expanded, reduced


def nonprincipal_stabilizer_increment(
    gcd_content: int,
    weighted_gcd: int,
    line_step: int,
    row_fan: int,
    other_row_fan: int,
    color_fan: int,
    other_color_fan: int,
    color_modulus: int,
) -> Fraction:
    """Return the exact ``SL_2``-orbit phase increment.

    With ``Delta=s*r-s'*r'`` it is

    ``-d*A*Delta/(g^2*S)``.

    The balanced choice ``d=L, A=Q, S=LQ, g=1``, together with
    ``r=r'=1`` and ``s'=s-1``, gives the integer ``-1`` although
    ``Delta=1``.  Hence principal-resonance extraction alone does not
    control the fully nonconstant completion.
    """

    d = int(weighted_gcd)
    g = int(gcd_content)
    A = int(line_step)
    r = int(row_fan)
    rp = int(other_row_fan)
    s = int(color_fan)
    sp = int(other_color_fan)
    S = int(color_modulus)
    if g <= 0 or S <= 0:
        raise ValueError("gcd content and color modulus must be positive")
    delta = s * r - sp * rp
    return Fraction(-d * A * delta, g * g * S)


def conductor_lowered_crt_index(
    row_step: int,
    bezout_coordinate: int,
    delta_numerator: int,
    delta_modulus: int,
    fan_translation: int,
    dual_index: int,
) -> int:
    """Return ``n/c`` on an exact coherent CRT ray.

    The raw residue representative is
    ``n=U*r*c-a*k*R``.  Conductor lowering is integral precisely on the
    audited ray ``c|k``.  For ``k=t*c`` the result ``U*r-a*t*R`` is
    independent of ``c``.
    """

    R = int(row_step)
    U = int(bezout_coordinate)
    a = int(delta_numerator)
    c = int(delta_modulus)
    r = int(fan_translation)
    k = int(dual_index)
    if R <= 0 or c <= 0:
        raise ValueError("row step and delta modulus must be positive")
    if k % c:
        raise ValueError("dual index is not on a conductor-lowered CRT ray")
    return (U * r * c - a * k * R) // c


@dataclass(frozen=True)
class WeightedIsolatedCellAudit:
    """Exact audit for a half-open grid with separable complex weights.

    The occupied pairs are assigned to the unique cells

    ``[m0+iH,m0+(i+1)H) x [n0+jK,n0+(j+1)K)``.

    The routine requires at most ``maximum_occupancy`` pairs in every
    occupied cell.  For weights ``u_m v_n z_mn``, with ``|z_mn|<=1``, it
    records both the literal weighted ``L1`` mass and the cellwise square
    sum.  The certified inequalities are

    ``sum_E |u_m v_n z_mn| <= s*#cells*||u||inf*||v||inf``

    and

    ``sum_Q |sum_(E intersect Q) u_m v_n z_mn|^2
       <= s*sum_E |u_m|^2|v_n|^2``.

    These allow arbitrary phases and are the weighted nonconcentration
    data inherited by an analytic treatment of the high-step class.
    """

    occupied_pair_count: int
    occupied_cell_count: int
    maximum_cell_occupancy: int
    grid_overlap: int
    weighted_l1_mass: float
    weighted_l1_supremum_bound: float
    cellwise_square_sum: float
    cellwise_square_bound: float
    product_l2_square_bound: float


def weighted_isolated_cell_audit(
    occupied_pairs: Iterable[tuple[int, int]],
    row_weights: Mapping[int, complex],
    color_weights: Mapping[int, complex],
    *,
    row_cell_length: int,
    color_cell_length: int,
    row_origin: int = 0,
    color_origin: int = 0,
    phases: Mapping[tuple[int, int], complex] | None = None,
    maximum_occupancy: int = 3,
) -> WeightedIsolatedCellAudit:
    """Audit the exact separable-weight inequalities on isolated cells."""

    H = int(row_cell_length)
    K = int(color_cell_length)
    s = int(maximum_occupancy)
    if H <= 0 or K <= 0 or s <= 0:
        raise ValueError("cell lengths and maximum occupancy must be positive")
    pairs = tuple((int(m), int(n)) for m, n in occupied_pairs)
    if len(set(pairs)) != len(pairs):
        raise ValueError("occupied pairs must be distinct")

    cell_terms: dict[tuple[int, int], list[complex]] = {}
    weighted_l1 = 0.0
    weighted_l2_square = 0.0
    row_support = {m for m, _ in pairs}
    color_support = {n for _, n in pairs}
    row_supremum = max((abs(row_weights[m]) for m in row_support), default=0.0)
    color_supremum = max(
        (abs(color_weights[n]) for n in color_support), default=0.0
    )
    for pair in pairs:
        m, n = pair
        phase = 1.0 + 0.0j if phases is None else complex(phases[pair])
        if abs(phase) > 1.0 + 1e-12:
            raise ValueError("phase/cutoff factors must have modulus at most one")
        term = complex(row_weights[m]) * complex(color_weights[n]) * phase
        cell = ((m - row_origin) // H, (n - color_origin) // K)
        cell_terms.setdefault(cell, []).append(term)
        weighted_l1 += abs(term)
        weighted_l2_square += abs(term) ** 2

    maximum_cell = max((len(terms) for terms in cell_terms.values()), default=0)
    if maximum_cell > s:
        raise ValueError("an occupied cell exceeds the isolated-cell threshold")
    square_sum = sum(abs(sum(terms)) ** 2 for terms in cell_terms.values())
    product_l2_square = sum(abs(row_weights[m]) ** 2 for m in row_support) * sum(
        abs(color_weights[n]) ** 2 for n in color_support
    )
    return WeightedIsolatedCellAudit(
        occupied_pair_count=len(pairs),
        occupied_cell_count=len(cell_terms),
        maximum_cell_occupancy=maximum_cell,
        grid_overlap=1,
        weighted_l1_mass=weighted_l1,
        weighted_l1_supremum_bound=(
            s * len(cell_terms) * row_supremum * color_supremum
        ),
        cellwise_square_sum=square_sum,
        cellwise_square_bound=s * weighted_l2_square,
        product_l2_square_bound=s * product_l2_square,
    )


@dataclass(frozen=True)
class ParallelQuarticUniquenessLedger:
    """No-parallel-copy theorem inside the high-step quartic fan pair.

    Put ``m=R^2``, ``q=2m`` and use the parallel line ``y=x+k`` with the
    natural integral carrier

    ``b=m+R*k+x^2+x*k+k^2``.

    The product error divided by ``-R^2`` is

    ``R*k^3+2R*k^2*x+2R*k*x^2+k^3*x+2k^2*x^2+2k*x^3+x^4``.

    On the active high-step family, every ``k,x>=1`` already lies outside
    the product window, whereas ``k=0, 1<=x<=T`` is the original quartic
    arc.  Throughout the audited box ``1<=x,k<=T``, the displayed carrier
    is the unique nearest integer to ``m^3/(a*c)``.
    """

    scale: int
    step: int
    center: int
    q: int
    aperture: int
    quartic_length: int
    minimum_offset_error_quotient: int
    legal_error_quotient_cap: int
    maximum_offset_error_quotient: int
    minimum_offset_product: int
    natural_carrier_is_unique_nearest_integer: bool
    every_positive_parallel_offset_is_illegal: bool
    central_arc_endpoint_is_legal: bool


def parallel_quartic_uniqueness_ledger(
    scale: int,
) -> ParallelQuarticUniquenessLedger:
    """Return the exact no-parallel-copy ledger for (2E.F7r)."""

    barrier = quartic_high_step_fan_barrier_ledger(scale)
    R = barrier.step
    m = barrier.center
    T = barrier.fan_length
    degree = barrier.aperture

    def error_quotient(x: int, k: int) -> int:
        return (
            R * k**3
            + 2 * R * k * k * x
            + 2 * R * k * x * x
            + k**3 * x
            + 2 * k * k * x * x
            + 2 * k * x**3
            + x**4
        )

    minimum_error = error_quotient(1, 1)
    maximum_error = error_quotient(T, T)
    legal_cap = degree // 4
    first_factor = m + R * T
    second_factor = m - R * (T + T)
    if second_factor <= 0:
        raise AssertionError("the quartic audit left the positive shell")
    minimum_product = first_factor * second_factor
    # The error in the carrier is R^2*Q/(a*c).  Monotonicity of Q and the
    # displayed lower bound for a*c certify the entire positive box.
    unique_nearest = 2 * m * maximum_error < minimum_product
    if not unique_nearest:
        raise AssertionError("the natural carrier was not uniquely nearest")
    return ParallelQuarticUniquenessLedger(
        scale=int(scale),
        step=R,
        center=m,
        q=barrier.modulus,
        aperture=degree,
        quartic_length=T,
        minimum_offset_error_quotient=minimum_error,
        legal_error_quotient_cap=legal_cap,
        maximum_offset_error_quotient=maximum_error,
        minimum_offset_product=minimum_product,
        natural_carrier_is_unique_nearest_integer=unique_nearest,
        every_positive_parallel_offset_is_illegal=minimum_error > legal_cap,
        central_arc_endpoint_is_legal=T**4 == legal_cap,
    )


@dataclass(frozen=True)
class TangentLowModeL2BarrierLedger:
    """Exponent ledger for the coherent low modes of a tangent strip.

    In the full-integer consecutive chart with ``q=2m`` and
    ``A=C={m+i: 0<=i<cD}``, Taylor expansion modulo integers gives

    ``q^3/(8ac) = constant + (i^2+i*j+j^2)/m + O(D^3/m^2)``.

    Hence ``|S_ell|`` has order ``D^2`` for ``ell <= c*q/D^2``.  Those
    modes have the sharp target ``L1`` mass ``q`` but second-moment mass
    ``q*D^2``, whereas a Cauchy--Schwarz closure of the Selberg gate would
    require ``q*D``.  Thus a generic second-moment route loses ``sqrt(D)``.
    """

    degree_exponent_in_q: Fraction
    coherent_mode_cutoff_exponent_in_q: Fraction
    coherent_sum_size_exponent_in_q: Fraction
    low_mode_l1_exponent_in_q: Fraction
    low_mode_l2_exponent_in_q: Fraction
    required_second_moment_exponent_in_q: Fraction
    second_moment_excess_exponent_in_q: Fraction
    cauchy_loss_exponent_in_q: Fraction


def tangent_low_mode_l2_barrier_ledger() -> TangentLowModeL2BarrierLedger:
    """Return the exact active-scale powers in the low-mode obstruction."""

    degree = Fraction(16, 33)
    cutoff = 1 - 2 * degree
    sum_size = 2 * degree
    low_l1 = cutoff + sum_size
    low_l2 = cutoff + 2 * sum_size
    required_l2 = 1 + degree
    excess = low_l2 - required_l2
    return TangentLowModeL2BarrierLedger(
        degree_exponent_in_q=degree,
        coherent_mode_cutoff_exponent_in_q=cutoff,
        coherent_sum_size_exponent_in_q=sum_size,
        low_mode_l1_exponent_in_q=low_l1,
        low_mode_l2_exponent_in_q=low_l2,
        required_second_moment_exponent_in_q=required_l2,
        second_moment_excess_exponent_in_q=excess,
        cauchy_loss_exponent_in_q=excess / 2,
    )


@dataclass(frozen=True)
class RationalRayVisibilityLedger:
    """Multiplicity of a generic small-denominator rational ray.

    The vectors ``k*(p,r)`` all have exactly the same slope.  Their gcd is
    ``k`` because ``(p,r)`` is primitive, so visibility deletes every
    multiple except possibly ``k=1``.  This fixture is **not** an obstruction
    for a relevant nonempty slope block: a primitive shell-scale reference
    in that block forces any competing reduced denominator to be at least a
    constant times ``q/D``, and the determinant-lift lemma above caps all
    integer points by ``O(D)``.
    """

    direction: tuple[int, int]
    shell: tuple[int, int]
    first_multiplier: int
    last_multiplier: int
    lattice_points: int
    primitive_points: int


def rational_ray_visibility_ledger(
    direction: tuple[int, int], shell_lower: int, shell_upper: int
) -> RationalRayVisibilityLedger:
    """Count all and primitive multiples of one rational direction."""

    p, r = (int(value) for value in direction)
    lower = int(shell_lower)
    upper = int(shell_upper)
    if min(p, r, lower) <= 0 or upper < lower:
        raise ValueError("direction and shell must be positive")
    if math.gcd(p, r) != 1:
        raise ValueError("direction must be primitive")

    first = max((lower + p - 1) // p, (lower + r - 1) // r)
    last = min(upper // p, upper // r)
    lattice_points = max(0, last - first + 1)
    primitive_points = int(first <= 1 <= last)
    return RationalRayVisibilityLedger(
        direction=(p, r),
        shell=(lower, upper),
        first_multiplier=first,
        last_multiplier=last,
        lattice_points=lattice_points,
        primitive_points=primitive_points,
    )


@dataclass(frozen=True)
class SymmetricTangentPackingLedger:
    """Exhaustive curvature cap for the symmetric tangent normal form.

    The candidate indexed by ``(x,z)`` has

    ``alpha=(m+x,m+x+1)``, ``gamma=(m+z,m+z-1)``, and
    ``b=m-x-z``.

    It includes every translate of the primitive tangent rectangles built
    from this normal form.  Thus counting all admissible ``(x,z)`` also
    counts any attempted packing of disjoint rectangles inside the chart.
    This is a full-integer diagnostic; ``q=2m`` is not an actual odd-prime
    centre.
    """

    center: int
    q: int
    degree_scale: int
    search_radius: int
    candidate_edge_count: int
    admissible_edge_count: int
    curvature_upper_bound: int
    maximum_admissible_radius_squared: int
    ratio_interval_width: Fraction
    canonical_bin_width: Fraction


def symmetric_tangent_packing_ledger(
    center: int, degree_scale: int, *, search_radius: int | None = None
) -> SymmetricTangentPackingLedger:
    """Count the whole shifted symmetric tangent chart exactly.

    Put ``q=2m``.  The first product residual divided by eight is

    ``F(x,z)=-m*(x^2+x*z+z^2)-x*z*(x+z)``.

    If ``|x|,|z|<=R`` and ``m>4R``, then

    ``|F(x,z)| >= (m/2)*(x^2+x*z+z^2)``.

    Consequently the legal window ``|8F|<=qD`` forces
    ``x^2+z^2<D``.  There are at most
    ``(2*floor(sqrt(D))+1)^2=O(D)`` such pairs.  The routine exhausts the
    requested chart and checks this implication for every accepted edge.
    """

    m = int(center)
    degree = int(degree_scale)
    radius = degree if search_radius is None else int(search_radius)
    if min(m, degree) <= 0 or radius < 0:
        raise ValueError("center and degree must be positive and radius nonnegative")
    if m <= 4 * radius:
        raise ValueError("the curvature audit requires center > 4*search_radius")

    q = 2 * m
    target = q**3
    admissible: list[tuple[int, int]] = []
    ratios: list[Fraction] = []
    maximum_radius_squared = 0
    for x in range(-radius, radius + 1):
        first_row = m + x
        second_row = first_row + 1
        for z in range(-radius, radius + 1):
            first_color = m + z
            second_color = first_color - 1
            carrier = m - x - z
            first_residual = 8 * first_row * carrier * first_color - target
            second_residual = (
                8 * second_row * carrier * second_color - target
            )
            if max(abs(first_residual), abs(second_residual)) > q * degree:
                continue
            quadratic = x * x + x * z + z * z
            cubic = x * z * (x + z)
            exact_divided_residual = first_residual // 8
            if first_residual % 8 or exact_divided_residual != -m * quadratic - cubic:
                raise AssertionError("the tangent residual identity failed")
            radius_squared = x * x + z * z
            if radius_squared >= degree:
                raise AssertionError("an admissible edge escaped the curvature disk")
            maximum_radius_squared = max(maximum_radius_squared, radius_squared)
            admissible.append((x, z))
            ratios.extend(
                (
                    Fraction(first_row, second_row),
                    Fraction(second_color, first_color),
                )
            )

    curvature_upper_bound = (2 * math.isqrt(degree) + 1) ** 2
    if len(admissible) > curvature_upper_bound:
        raise AssertionError("the exhaustive chart exceeded its curvature cap")
    ratio_width = max(ratios) - min(ratios) if ratios else Fraction(0)
    return SymmetricTangentPackingLedger(
        center=m,
        q=q,
        degree_scale=degree,
        search_radius=radius,
        candidate_edge_count=(2 * radius + 1) ** 2,
        admissible_edge_count=len(admissible),
        curvature_upper_bound=curvature_upper_bound,
        maximum_admissible_radius_squared=maximum_radius_squared,
        ratio_interval_width=ratio_width,
        canonical_bin_width=Fraction(degree, q * q),
    )


def projective_common_neighbor_ledger(
    first_left: tuple[int, int],
    second_left: tuple[int, int],
    shared_right: tuple[int, int],
) -> ProjectiveCommonNeighborLedger:
    """Return the two exact shared-neighbor determinant identities."""

    a1, a2 = (int(value) for value in first_left)
    other_a1, other_a2 = (int(value) for value in second_left)
    c1, c2 = (int(value) for value in shared_right)
    first_shift = a2 * c2 - a1 * c1
    second_shift = other_a2 * c2 - other_a1 * c1
    determinant = a1 * other_a2 - a2 * other_a1
    return ProjectiveCommonNeighborLedger(
        first_shift=first_shift,
        second_shift=second_shift,
        left_determinant=determinant,
        first_identity_left=c2 * determinant,
        first_identity_right=a1 * second_shift - other_a1 * first_shift,
        second_identity_left=c1 * determinant,
        second_identity_right=a2 * second_shift - other_a2 * first_shift,
    )


SlopeBlockEdge = tuple[int, int, int, int, int]


@dataclass(frozen=True)
class ResidualFactorizationLedger:
    """Exact residual projections of actual slope-block edges.

    An edge is ordered as ``(a1,a2,b,c1,c2)`` and has residuals

    ``rho_i=8*b*a_i*c_i-q^3``.

    For five distinct prime powers in the narrow shell, unique
    factorization gives at most six edges above either fixed residual.
    Pairwise coprimality also recovers the carrier and cross shift from the
    ordered residual pair.  This ledger checks those identities on a finite
    edge set and records the resulting residual-projection bound.
    """

    q: int
    edges: tuple[SlopeBlockEdge, ...]
    residual_pairs: tuple[tuple[int, int], ...]
    recovered_carriers: tuple[int, ...]
    recovered_shifts: tuple[int, ...]
    first_residual_levels: tuple[int, ...]
    second_residual_levels: tuple[int, ...]
    maximum_first_level_multiplicity: int
    maximum_second_level_multiplicity: int
    maximum_pair_multiplicity: int
    projection_edge_bound: int

    @property
    def edge_count(self) -> int:
        return len(self.edges)


def residual_factorization_ledger(
    q: int, edges: Sequence[SlopeBlockEdge]
) -> ResidualFactorizationLedger:
    """Certify carrier recovery and the six-per-residual projection cap.

    Every supplied edge must have five distinct, pairwise-coprime prime
    powers.  The theorem applies to a complete slope-block edge set; the
    routine itself is a finite identity checker and multiplicity ledger.
    """

    modulus = int(q)
    if modulus <= 0:
        raise ValueError("q must be positive")
    normalized_edges: list[SlopeBlockEdge] = []
    residual_pairs: list[tuple[int, int]] = []
    carriers: list[int] = []
    shifts: list[int] = []
    first_counts: dict[int, int] = {}
    second_counts: dict[int, int] = {}
    pair_counts: dict[tuple[int, int], int] = {}
    first_row_projection: dict[int, int] = {}
    second_row_projection: dict[int, int] = {}
    first_color_projection: dict[int, int] = {}
    second_color_projection: dict[int, int] = {}

    for raw_edge in edges:
        if len(raw_edge) != 5:
            raise ValueError("a slope-block edge must have five entries")
        edge = tuple(int(value) for value in raw_edge)
        a1, a2, carrier, c1, c2 = edge
        if not is_pairwise_coprime_prime_power_shell(edge):
            raise ValueError(
                "each edge must contain five distinct prime-power bases"
            )
        for projection, key, value in (
            (first_row_projection, a1, a2),
            (second_row_projection, a2, a1),
            (first_color_projection, c1, c2),
            (second_color_projection, c2, c1),
        ):
            if key in projection and projection[key] != value:
                raise ValueError(
                    "each coordinate projection must be injective in one slope block"
                )
            projection[key] = value
        first_residual = 8 * carrier * a1 * c1 - modulus**3
        second_residual = 8 * carrier * a2 * c2 - modulus**3
        first_product = (modulus**3 + first_residual) // 8
        second_product = (modulus**3 + second_residual) // 8
        recovered_carrier = math.gcd(first_product, second_product)
        residual_difference = second_residual - first_residual
        if recovered_carrier != carrier:
            raise AssertionError("the residual gcd did not recover the carrier")
        if residual_difference % (8 * recovered_carrier):
            raise AssertionError("the residual difference did not recover a shift")
        recovered_shift = residual_difference // (8 * recovered_carrier)
        if recovered_shift != a2 * c2 - a1 * c1:
            raise AssertionError("the recovered cross shift is incorrect")

        pair = (first_residual, second_residual)
        normalized_edges.append(edge)
        residual_pairs.append(pair)
        carriers.append(recovered_carrier)
        shifts.append(recovered_shift)
        first_counts[first_residual] = first_counts.get(first_residual, 0) + 1
        second_counts[second_residual] = second_counts.get(second_residual, 0) + 1
        pair_counts[pair] = pair_counts.get(pair, 0) + 1

    maximum_first = max(first_counts.values(), default=0)
    maximum_second = max(second_counts.values(), default=0)
    maximum_pair = max(pair_counts.values(), default=0)
    if maximum_first > 6 or maximum_second > 6:
        raise AssertionError("unique factorization permits at most six assignments")
    if maximum_pair > 2:
        raise AssertionError("a residual pair permits at most two assignments")
    projection_bound = 6 * min(len(first_counts), len(second_counts))
    return ResidualFactorizationLedger(
        q=modulus,
        edges=tuple(normalized_edges),
        residual_pairs=tuple(residual_pairs),
        recovered_carriers=tuple(carriers),
        recovered_shifts=tuple(shifts),
        first_residual_levels=tuple(sorted(first_counts)),
        second_residual_levels=tuple(sorted(second_counts)),
        maximum_first_level_multiplicity=maximum_first,
        maximum_second_level_multiplicity=maximum_second,
        maximum_pair_multiplicity=maximum_pair,
        projection_edge_bound=projection_bound,
    )


@dataclass(frozen=True)
class SlopeBlockAnchorResultantLedger:
    """The exact determinant-coordinate resultant relative to one edge."""

    anchor_shift: int
    row_coordinates: tuple[int, int]
    color_coordinates: tuple[int, int]
    edge_shift: int
    resultant_left: int
    resultant_right: int
    anchor_shift_is_unit: bool


def slope_block_anchor_resultant_ledger(
    anchor_left: tuple[int, int],
    anchor_reciprocal_color: tuple[int, int],
    left: tuple[int, int],
    reciprocal_color: tuple[int, int],
) -> SlopeBlockAnchorResultantLedger:
    """Return ``kappa*v=h*g-alpha*beta`` in anchor coordinates."""

    p, r = (int(value) for value in anchor_left)
    u, v = (int(value) for value in anchor_reciprocal_color)
    x, y = (int(value) for value in left)
    z, w = (int(value) for value in reciprocal_color)
    kappa = r * u - p * v
    if kappa == 0:
        raise ValueError("the anchor row and reciprocal color must be transverse")
    h = p * y - r * x
    alpha = u * y - v * x
    g = u * w - v * z
    beta = p * w - r * z
    edge_shift = y * z - x * w
    resultant_left = kappa * edge_shift
    resultant_right = h * g - alpha * beta
    if resultant_left != resultant_right:
        raise AssertionError("the anchor resultant identity failed")
    return SlopeBlockAnchorResultantLedger(
        anchor_shift=kappa,
        row_coordinates=(h, alpha),
        color_coordinates=(g, beta),
        edge_shift=edge_shift,
        resultant_left=resultant_left,
        resultant_right=resultant_right,
        anchor_shift_is_unit=all(
            math.gcd(abs(kappa), coordinate) == 1
            for coordinate in (p, r, u, v)
        ),
    )


@dataclass(frozen=True)
class ActualResidualSlopeBlockFixtureLedger:
    """The legal ``q=25013`` ten-edge residual/resultant obstruction."""

    q: int
    cutoff: int
    bandwidth: float
    degree_scale: float
    left_vertices: tuple[tuple[int, int], ...]
    right_vertices: tuple[tuple[int, int], ...]
    edges: tuple[SlopeBlockEdge, ...]
    residuals: ResidualFactorizationLedger
    ratio_span_in_degree_bins: float
    maximum_normalized_frequency: float
    maximum_carrier_interval_length: float
    carrier_diameter: int
    anchor_left: tuple[int, int]
    anchor_reciprocal_color: tuple[int, int]
    anchor_shift: int
    row_determinant_coordinates: tuple[tuple[int, int], ...]
    color_determinant_coordinates: tuple[tuple[int, int], ...]
    maximum_resultant_error: int


def actual_residual_slope_block_fixture_ledger(
) -> ActualResidualSlopeBlockFixtureLedger:
    """Build the all-prime ten-edge block at ``q=25013,U=24``."""

    q = 25_013
    cutoff = 24
    bandwidth = (q / 2.0) ** (50.0 / 33.0)
    degree = q * q / bandwidth
    left = (
        (10_559, 11_443),
        (11_443, 12_401),
        (11_897, 12_893),
        (13_259, 14_369),
    )
    right = (
        (11_443, 10_559),
        (12_401, 11_443),
        (12_893, 11_897),
        (14_369, 13_259),
    )
    carrier_by_pair = {
        (0, 1): 14_939,
        (0, 2): 14_369,
        (0, 3): 12_893,
        (1, 0): 14_939,
        (1, 2): 13_259,
        (1, 3): 11_897,
        (2, 0): 14_369,
        (2, 1): 13_259,
        (2, 3): 11_443,
        (3, 0): 12_893,
        (3, 1): 11_897,
        (3, 2): 11_443,
    }
    edges: list[SlopeBlockEdge] = []
    normalized_frequencies: list[float] = []
    carrier_interval_lengths: list[float] = []
    for (left_index, right_index), carrier in carrier_by_pair.items():
        a1, a2 = left[left_index]
        c1, c2 = right[right_index]
        edge = (a1, a2, carrier, c1, c2)
        if len(set(edge)) < 5:
            continue
        edges.append(edge)
        for row, color in ((a1, c1), (a2, c2)):
            normalized_frequencies.append(
                bandwidth * math.log(8 * row * carrier * color / q**3)
            )
            center = q**3 / (8 * row * color)
            carrier_interval_lengths.append(
                center
                * (
                    math.exp(cutoff / bandwidth)
                    - math.exp(-cutoff / bandwidth)
                )
            )

    ratios = [a1 / a2 for a1, a2 in left]
    ratios.extend(c2 / c1 for c1, c2 in right)
    canonical_width = degree / q**2
    residuals = residual_factorization_ledger(q, edges)
    anchor_left = left[0]
    anchor_reciprocal = (right[2][1], right[2][0])
    row_coordinates = []
    color_coordinates = []
    for vertex in left:
        ledger = slope_block_anchor_resultant_ledger(
            anchor_left, anchor_reciprocal, vertex, anchor_reciprocal
        )
        row_coordinates.append(ledger.row_coordinates)
    for c1, c2 in right:
        reciprocal = (c2, c1)
        ledger = slope_block_anchor_resultant_ledger(
            anchor_left, anchor_reciprocal, anchor_left, reciprocal
        )
        color_coordinates.append(ledger.color_coordinates)

    resultant_errors = []
    for a1, a2, _carrier, c1, c2 in edges:
        ledger = slope_block_anchor_resultant_ledger(
            anchor_left,
            anchor_reciprocal,
            (a1, a2),
            (c2, c1),
        )
        resultant_errors.append(ledger.resultant_left - ledger.resultant_right)

    carriers = [edge[2] for edge in edges]
    anchor_shift = (
        anchor_left[1] * anchor_reciprocal[0]
        - anchor_left[0] * anchor_reciprocal[1]
    )
    return ActualResidualSlopeBlockFixtureLedger(
        q=q,
        cutoff=cutoff,
        bandwidth=bandwidth,
        degree_scale=degree,
        left_vertices=left,
        right_vertices=right,
        edges=tuple(edges),
        residuals=residuals,
        ratio_span_in_degree_bins=(max(ratios) - min(ratios)) / canonical_width,
        maximum_normalized_frequency=max(map(abs, normalized_frequencies)),
        maximum_carrier_interval_length=max(carrier_interval_lengths),
        carrier_diameter=max(carriers) - min(carriers),
        anchor_left=anchor_left,
        anchor_reciprocal_color=anchor_reciprocal,
        anchor_shift=anchor_shift,
        row_determinant_coordinates=tuple(row_coordinates),
        color_determinant_coordinates=tuple(color_coordinates),
        maximum_resultant_error=max(map(abs, resultant_errors), default=0),
    )


RowPair = tuple[int, int]
RowPairCommonNeighbor = tuple[int, int, int, int]


@dataclass(frozen=True)
class FixedRowPairSecantNormLedger:
    """Exact fixed-secant norm identities for two shared neighbors.

    A neighbor is ``(b,B,c,d)`` and represents the rank-one product matrix
    ``(b,B)^T(c,d)`` for the fixed row vertices ``(a,m)`` and ``(A,M)``.
    The signed relation matrix is

    ``K=((-a,m),(A,-M))``.

    Thus ``det(K)=a*M-m*A`` and the common pinned level is
    ``<K,X>=-a*bc+m*bd+A*Bc-M*Bd``.  The returned defects replay the
    fixed-secant binary-norm reduction without making an asymptotic claim.
    """

    first_row: RowPair
    second_row: RowPair
    first_neighbor: RowPairCommonNeighbor
    second_neighbor: RowPairCommonNeighbor
    row_determinant: int
    first_level: int
    second_level: int
    first_product_matrix: IntegerVector
    second_product_matrix: IntegerVector
    secant: IntegerVector
    secant_determinant: int
    kernel_defect: int
    norm_rhs: int
    norm_discriminant: int
    relation_secant_trace: int
    secant_involution_trace: int
    mixed_trace: int
    relation_secant_square_defect: IntegerVector
    secant_involution_square_defect: IntegerVector
    anticommutator_defect: IntegerVector
    norm_square_defect: IntegerVector

    @property
    def norm_reduction_is_nondegenerate(self) -> bool:
        return bool(
            self.row_determinant
            and self.secant_determinant
            and self.norm_rhs
            and self.norm_discriminant
        )


def _row_pair_neighbor_product_matrix(
    neighbor: RowPairCommonNeighbor,
) -> IntegerVector:
    b, other_b, c, d = neighbor
    return (b * c, b * d, other_b * c, other_b * d)


def _fixed_row_pair_level(
    first_row: RowPair,
    second_row: RowPair,
    product_matrix: IntegerVector,
) -> int:
    a, m = first_row
    other_a, other_m = second_row
    x11, x12, x21, x22 = product_matrix
    return -a * x11 + m * x12 + other_a * x21 - other_m * x22


def fixed_row_pair_secant_norm_ledger(
    first_row: Sequence[int],
    second_row: Sequence[int],
    first_neighbor: Sequence[int],
    second_neighbor: Sequence[int],
) -> FixedRowPairSecantNormLedger:
    """Replay the transposed fixed-secant identities exactly.

    Both row vectors and both left/right neighbor factors must be primitive.
    In the actual all-five-distinct shell this follows from pairwise
    coprimality; equality of the two carriers would force the fixed rows to
    coincide by the sub-unit third-node interval.  Distinct neighbors must
    have the same pinned level and an invertible secant.
    """

    if len(first_row) != 2 or len(second_row) != 2:
        raise ValueError("row vertices must be two-vectors")
    if len(first_neighbor) != 4 or len(second_neighbor) != 4:
        raise ValueError("common neighbors must be four-vectors")
    row = tuple(int(value) for value in first_row)
    other_row = tuple(int(value) for value in second_row)
    neighbor = tuple(int(value) for value in first_neighbor)
    other_neighbor = tuple(int(value) for value in second_neighbor)
    if any(value <= 0 for value in (*row, *other_row, *neighbor, *other_neighbor)):
        raise ValueError("row and neighbor entries must be positive")
    if math.gcd(*row) != 1 or math.gcd(*other_row) != 1:
        raise ValueError("actual row vertices must be primitive")
    for values in (neighbor, other_neighbor):
        if math.gcd(values[0], values[1]) != 1:
            raise ValueError("the two carrier factors must be primitive")
        if math.gcd(values[2], values[3]) != 1:
            raise ValueError("the two color factors must be primitive")

    a, m = row
    other_a, other_m = other_row
    row_determinant = a * other_m - m * other_a
    if row_determinant == 0:
        raise ValueError("distinct primitive row vertices must be transverse")
    first_product = _row_pair_neighbor_product_matrix(neighbor)  # type: ignore[arg-type]
    second_product = _row_pair_neighbor_product_matrix(other_neighbor)  # type: ignore[arg-type]
    first_level = _fixed_row_pair_level(row, other_row, first_product)  # type: ignore[arg-type]
    second_level = _fixed_row_pair_level(row, other_row, second_product)  # type: ignore[arg-type]
    if first_level != second_level:
        raise ValueError("the two neighbors are not on one pinned level")
    secant = tuple(
        left - right for left, right in zip(first_product, second_product)
    )
    secant_determinant = _matrix_determinant(secant)
    if secant_determinant == 0:
        raise ValueError("distinct actual neighbors must have invertible secant")
    kernel_defect = _fixed_row_pair_level(row, other_row, secant)  # type: ignore[arg-type]

    # ``fixed_energy_norm_ledger`` forms the signed matrix
    # ``((c11,-c12),(-c21,c22))``.  The pseudo-colors below therefore give
    # exactly ``K=((-a,m),(A,-M))``; no sign is implicit here.
    pseudo_colors = (-a, -m, -other_a, -other_m)
    norm = fixed_energy_norm_ledger(
        pseudo_colors,
        neighbor,  # type: ignore[arg-type]
        other_neighbor,  # type: ignore[arg-type]
    )
    if norm.color_determinant != row_determinant:
        raise AssertionError("the transposed relation determinant has the wrong sign")
    if norm.energy_determinant != secant_determinant:
        raise AssertionError("the transposed secant determinant is inconsistent")
    if norm.level != first_level:
        raise AssertionError("the transposed pinned level is inconsistent")
    return FixedRowPairSecantNormLedger(
        first_row=row,  # type: ignore[arg-type]
        second_row=other_row,  # type: ignore[arg-type]
        first_neighbor=neighbor,  # type: ignore[arg-type]
        second_neighbor=other_neighbor,  # type: ignore[arg-type]
        row_determinant=row_determinant,
        first_level=first_level,
        second_level=second_level,
        first_product_matrix=first_product,
        second_product_matrix=second_product,
        secant=secant,  # type: ignore[arg-type]
        secant_determinant=secant_determinant,
        kernel_defect=kernel_defect,
        norm_rhs=norm.norm_rhs,
        norm_discriminant=-4 * row_determinant * secant_determinant,
        relation_secant_trace=norm.color_energy_trace,
        secant_involution_trace=norm.energy_involution_trace,
        mixed_trace=norm.mixed_trace,
        relation_secant_square_defect=norm.color_energy_square_defect,
        secant_involution_square_defect=norm.energy_involution_square_defect,
        anticommutator_defect=norm.anticommutator_defect,
        norm_square_defect=norm.norm_square_defect,
    )


@dataclass(frozen=True)
class FixedRowPairCodegreeDichotomyLedger:
    """Exact exponent and logical ledger for the fixed-row-pair theorem."""

    degree_exponent_in_q: Fraction
    generic_cubic_lattice_term_exponent_in_q: Fraction
    generic_factorial_energy_exponent_in_degree: Fraction
    codegree_exponent_in_q: Fraction
    codegree_exponent_in_degree: Fraction
    exceptional_third_minimum_exponent_in_q: Fraction
    exceptional_plane_separation_margin_exponent_in_q: Fraction
    norm_main_exponent_in_q: Fraction
    norm_perturbation_exponent_in_q: Fraction
    norm_nonvanishing_margin_exponent_in_q: Fraction
    fixed_secant_multiplicity_is_subpower: bool
    generic_factorial_energy_closes_at_degree: bool
    exceptional_nonparabolic_count_is_subpower: bool
    exceptional_power_count_forces_parabolic_chart: bool
    parabolic_chart_cover_is_subpower: bool
    near_sharp_generic_count_forces_chart: bool
    slope_block_bound_proved: bool
    full_four_cycle_bound_proved: bool


def fixed_row_pair_codegree_dichotomy_ledger(
) -> FixedRowPairCodegreeDichotomyLedger:
    """Return the sharp ``sqrt(D)`` row-codegree exponent ledger.

    This records the proved pointwise dichotomy only.  In particular, a
    generic Sidon transversal can use ``D`` different secants once each, so
    near-sharp generic codegree does not by itself force one tangent chart.
    No aggregation over row pairs, slope-block edge cap, or FC theorem is
    asserted.
    """

    degree = Fraction(16, 33)
    cubic = 3 * degree - 1
    codegree = degree / 2
    exceptional_third = 1 - degree
    separation_margin = 1 - 2 * degree
    norm_main = Fraction(2)
    norm_perturbation = 3 * degree
    return FixedRowPairCodegreeDichotomyLedger(
        degree_exponent_in_q=degree,
        generic_cubic_lattice_term_exponent_in_q=cubic,
        generic_factorial_energy_exponent_in_degree=Fraction(1),
        codegree_exponent_in_q=codegree,
        codegree_exponent_in_degree=Fraction(1, 2),
        exceptional_third_minimum_exponent_in_q=exceptional_third,
        exceptional_plane_separation_margin_exponent_in_q=separation_margin,
        norm_main_exponent_in_q=norm_main,
        norm_perturbation_exponent_in_q=norm_perturbation,
        norm_nonvanishing_margin_exponent_in_q=norm_main - norm_perturbation,
        fixed_secant_multiplicity_is_subpower=True,
        generic_factorial_energy_closes_at_degree=True,
        exceptional_nonparabolic_count_is_subpower=True,
        exceptional_power_count_forces_parabolic_chart=True,
        parabolic_chart_cover_is_subpower=True,
        near_sharp_generic_count_forces_chart=False,
        slope_block_bound_proved=False,
        full_four_cycle_bound_proved=False,
    )


@dataclass(frozen=True)
class PrimitiveTangentSlopeBlockLedger:
    """A sharp full-integer slope-block incidence packet.

    This is a finite algebraic fixture, not an actual-prime-power model.
    It has ``L^2`` all-five-distinct common-carrier incidences in one ratio
    interval at product-window scale ``D=100 L^2``.  Thus a conjectural
    ``O(D)`` edge cap for one slope block would have the right order.
    """

    order: int
    center: int
    q: int
    degree_scale: int
    edge_count: int
    distinct_hyperedges: int
    maximum_cubic_residual: int
    maximum_cross_shift: int
    ratio_interval_width: Fraction
    canonical_bin_width: Fraction
    pair_unique: bool
    all_five_distinct: bool
    q_exceeds_degree_squared: bool


def primitive_tangent_slope_block_ledger(
    order: int, center: int
) -> PrimitiveTangentSlopeBlockLedger:
    """Build the exact primitive tangent packet used in the RT audit.

    For ``0<=i<L`` and ``2L<=j<3L`` put

    ``alpha_i=(m+i,m+i+1)``, ``gamma_j=(m+j+1,m+j)``, and
    ``b_ij=m-i-j-1``.

    Both products lie in ``|8abc-q^3|<=qD`` for ``q=2m`` and
    ``D=100L^2``.  The role intervals are disjoint, so the displayed five
    nodes are distinct.  Duplicate descriptions of the same unordered
    triple are merged before pair uniqueness is checked.
    """

    if order < 2:
        raise ValueError("the tangent packet requires order at least two")
    if center <= 4 * order:
        raise ValueError("the center must exceed four times the order")

    q = 2 * center
    degree_scale = 100 * order * order
    target = q**3
    edges: list[tuple[tuple[int, int], tuple[int, int], int]] = []
    hyperedges: set[tuple[int, int, int]] = set()
    ratios: list[Fraction] = []
    maximum_residual = 0
    maximum_shift = 0
    all_five_distinct = True

    for row_index in range(order):
        first_row = center + row_index
        second_row = first_row + 1
        ratios.append(Fraction(first_row, second_row))
        for color_index in range(2 * order, 3 * order):
            first_color = center + color_index + 1
            second_color = center + color_index
            carrier = center - row_index - color_index - 1
            ratios.append(Fraction(second_color, first_color))
            edges.append(
                (
                    (first_row, second_row),
                    (first_color, second_color),
                    carrier,
                )
            )
            first_triple = tuple(sorted((first_row, carrier, first_color)))
            second_triple = tuple(
                sorted((second_row, carrier, second_color))
            )
            hyperedges.add(first_triple)
            hyperedges.add(second_triple)
            maximum_residual = max(
                maximum_residual,
                abs(8 * first_row * carrier * first_color - target),
                abs(8 * second_row * carrier * second_color - target),
            )
            maximum_shift = max(
                maximum_shift,
                abs(second_row * second_color - first_row * first_color),
            )
            all_five_distinct &= (
                len(
                    {
                        first_row,
                        second_row,
                        carrier,
                        first_color,
                        second_color,
                    }
                )
                == 5
            )

    pair_to_third: dict[tuple[int, int], int] = {}
    pair_unique = True
    for triple in hyperedges:
        if len(set(triple)) != 3:
            pair_unique = False
            continue
        for omitted in range(3):
            pair = tuple(
                triple[index] for index in range(3) if index != omitted
            )
            third = triple[omitted]
            previous = pair_to_third.get(pair)
            if previous is not None and previous != third:
                pair_unique = False
            pair_to_third[pair] = third

    return PrimitiveTangentSlopeBlockLedger(
        order=order,
        center=center,
        q=q,
        degree_scale=degree_scale,
        edge_count=len(edges),
        distinct_hyperedges=len(hyperedges),
        maximum_cubic_residual=maximum_residual,
        maximum_cross_shift=maximum_shift,
        ratio_interval_width=max(ratios) - min(ratios),
        canonical_bin_width=Fraction(degree_scale, q * q),
        pair_unique=pair_unique,
        all_five_distinct=all_five_distinct,
        q_exceeds_degree_squared=q > degree_scale * degree_scale,
    )


def common_carrier_incidence_ledger(
    groups: Mapping[ColorMatrix, Sequence[Completion]],
) -> CommonCarrierIncidenceLedger:
    """Build the exact binary common-carrier incidence matrix.

    Duplicate appearances of one incidence in different completed
    rectangles are merged.  Conflicting carriers for the same row-pair and
    color-pair edge violate pair uniqueness and are rejected.
    """

    edge_carrier: dict[tuple[tuple[int, int], tuple[int, int]], int] = {}
    for colors, completions in groups.items():
        c11, c12, c21, c22 = (int(value) for value in colors)
        for completion in completions:
            a1, a2, b1, b2 = (int(value) for value in completion)
            for left, right, carrier in (
                ((a1, a2), (c11, c21), b1),
                ((a1, a2), (c12, c22), b2),
            ):
                key = (left, right)
                previous = edge_carrier.get(key)
                if previous is not None and previous != carrier:
                    raise ValueError(
                        "one row-pair/color-pair edge has conflicting carriers"
                    )
                edge_carrier[key] = carrier

    left_vertices = tuple(sorted({key[0] for key in edge_carrier}))
    right_vertices = tuple(sorted({key[1] for key in edge_carrier}))
    left_lookup = {vertex: index for index, vertex in enumerate(left_vertices)}
    right_lookup = {
        vertex: index for index, vertex in enumerate(right_vertices)
    }
    matrix = np.zeros((len(left_vertices), len(right_vertices)), dtype=float)
    carriers = []
    for (left, right), carrier in sorted(edge_carrier.items()):
        left_index = left_lookup[left]
        right_index = right_lookup[right]
        matrix[left_index, right_index] = 1.0
        carriers.append((left_index, right_index, carrier))
    left_degrees = np.sum(matrix, axis=1) if matrix.size else np.zeros(0)
    right_degrees = np.sum(matrix, axis=0) if matrix.size else np.zeros(0)
    singular_values = (
        np.linalg.svd(matrix, compute_uv=False) if matrix.size else np.zeros(0)
    )
    return CommonCarrierIncidenceLedger(
        left_vertices=left_vertices,
        right_vertices=right_vertices,
        carriers=tuple(carriers),
        matrix=matrix,
        edge_count=len(edge_carrier),
        maximum_left_degree=int(max(left_degrees, default=0)),
        maximum_right_degree=int(max(right_degrees, default=0)),
        operator_norm=float(max(singular_values, default=0.0)),
    )


def completion_secant_determinants(
    first: Completion, second: Completion
) -> tuple[int, int]:
    """Return the signed row and column determinants ``(A,B)``."""

    a1, a2, b1, b2 = (int(value) for value in first)
    other_a1, other_a2, other_b1, other_b2 = (
        int(value) for value in second
    )
    return (
        a1 * other_a2 - a2 * other_a1,
        b1 * other_b2 - b2 * other_b1,
    )


@dataclass(frozen=True)
class FixedSecantLayerLedger:
    """Finite row/column fibres in one signed ``(A,B)`` layer."""

    row_determinant: int
    column_determinant: int
    ordered_pairs: int
    maximum_top_color_pair_fibre: int
    maximum_bottom_color_pair_fibre: int

    @property
    def schur_bound(self) -> float:
        return math.sqrt(
            self.maximum_top_color_pair_fibre
            * self.maximum_bottom_color_pair_fibre
        )


ColorPair = tuple[int, int]
MatchingEdge = tuple[ColorPair, ColorPair]


@dataclass(frozen=True)
class FixedDeterminantCotlarLedger:
    """Exact overlap data for restrictions of one determinant matching.

    On the actual prime-power shell, fixing ``det(C)=k`` makes the allowed
    top--bottom color pairs a partial matching.  Every fixed-energy kernel
    is a restriction of that same matching.  This finite ledger checks the
    common-matching hypothesis and records the two quantities relevant to a
    binary Cotlar argument.  In particular, the norm of the positive sum is
    the maximum number of layers containing one master edge.
    """

    layers: int
    distinct_master_edges: int
    maximum_layers_per_edge: int
    maximum_cotlar_overlap_sum: int


def fixed_determinant_cotlar_ledger(
    layers: Iterable[Iterable[MatchingEdge]],
) -> FixedDeterminantCotlarLedger:
    """Audit binary fixed-``(E,k)`` layers inside one master matching.

    A layer may repeat a supplied edge; repetitions are discarded because
    this routine models support kernels.  It rejects either a nonmatching
    individual layer or two layers assigning different partners to the same
    top or bottom color pair.
    """

    normalized: list[frozenset[MatchingEdge]] = []
    master_top: dict[ColorPair, ColorPair] = {}
    master_bottom: dict[ColorPair, ColorPair] = {}
    edge_layers: dict[MatchingEdge, set[int]] = {}
    for layer_index, raw_layer in enumerate(layers):
        layer = frozenset(raw_layer)
        local_top: dict[ColorPair, ColorPair] = {}
        local_bottom: dict[ColorPair, ColorPair] = {}
        for top, bottom in layer:
            if top in local_top and local_top[top] != bottom:
                raise ValueError("one energy layer is not a partial matching")
            if bottom in local_bottom and local_bottom[bottom] != top:
                raise ValueError("one energy layer is not a partial matching")
            local_top[top] = bottom
            local_bottom[bottom] = top
            if top in master_top and master_top[top] != bottom:
                raise ValueError("the layers do not share one master matching")
            if bottom in master_bottom and master_bottom[bottom] != top:
                raise ValueError("the layers do not share one master matching")
            master_top[top] = bottom
            master_bottom[bottom] = top
            edge_layers.setdefault((top, bottom), set()).add(layer_index)
        normalized.append(layer)

    overlap_neighbours = [set() for _ in normalized]
    for indices in edge_layers.values():
        for index in indices:
            overlap_neighbours[index].update(indices)
    return FixedDeterminantCotlarLedger(
        layers=len(normalized),
        distinct_master_edges=len(edge_layers),
        maximum_layers_per_edge=max(
            (len(indices) for indices in edge_layers.values()), default=0
        ),
        maximum_cotlar_overlap_sum=max(
            (len(indices) for indices in overlap_neighbours), default=0
        ),
    )


def fixed_secant_layer_ledger(
    groups: Mapping[ColorMatrix, Sequence[Completion]],
    *,
    row_determinant: int,
    column_determinant: int,
) -> FixedSecantLayerLedger:
    """Count exact ordered completion pairs in one secant layer.

    This is a finite replay of the coefficient matrix in (2B.5).  The
    asymptotic ``O(D)`` row/column bounds use the actual-shell lift theorem;
    this routine only reports the exact fibres of supplied data.
    """

    if row_determinant == 0 or column_determinant == 0:
        raise ValueError("the generic secant determinants must be nonzero")
    top_fibres: dict[tuple[int, int], int] = {}
    bottom_fibres: dict[tuple[int, int], int] = {}
    ordered_pairs = 0
    for colors, completions in groups.items():
        top = (int(colors[0]), int(colors[1]))
        bottom = (int(colors[2]), int(colors[3]))
        for first in completions:
            for second in completions:
                if first == second:
                    continue
                if completion_secant_determinants(first, second) != (
                    row_determinant,
                    column_determinant,
                ):
                    continue
                ordered_pairs += 1
                top_fibres[top] = top_fibres.get(top, 0) + 1
                bottom_fibres[bottom] = bottom_fibres.get(bottom, 0) + 1
    return FixedSecantLayerLedger(
        row_determinant=row_determinant,
        column_determinant=column_determinant,
        ordered_pairs=ordered_pairs,
        maximum_top_color_pair_fibre=max(top_fibres.values(), default=0),
        maximum_bottom_color_pair_fibre=max(bottom_fibres.values(), default=0),
    )


@dataclass(frozen=True)
class BroadSliceProxy:
    form: PositiveQuarticForm
    completed_colors: int
    broad_colors: int
    singleton_broad_colors: int
    maximum_slice_weight: float


def broad_slice_proxy_form(
    values: Sequence[int],
    groups: Mapping[ColorMatrix, Sequence[Completion]],
    *,
    degree_scale: float,
    singleton_safe: bool = False,
) -> BroadSliceProxy:
    """Build the finite broad ``K_C`` proxy form.

    With ``singleton_safe=True`` the coefficient is
    ``K_C*(m(C)-1)``.  Otherwise it is the proposed pure ``K_C`` weight.
    """

    terms: list[tuple[ColorMatrix, float]] = []
    broad = 0
    singleton = 0
    maximum = 0.0
    for colors, completions in groups.items():
        # The LLL third length is within a fixed-dimensional constant of the
        # actual third minimum, which is all this explicitly labelled proxy
        # scan needs.  Exact enumeration remains available to small tests.
        ledger = kernel_minima_ledger(colors, exact_minima=False)
        if not ledger.broad:
            continue
        broad += 1
        if len(completions) == 1:
            singleton += 1
        slice_weight = 1.0 + degree_scale / ledger.third_minimum
        maximum = max(maximum, slice_weight)
        coefficient = slice_weight
        if singleton_safe:
            coefficient *= max(0, len(completions) - 1)
        terms.append((colors, coefficient))
    return BroadSliceProxy(
        form=_form_from_terms(values, terms),
        completed_colors=len(groups),
        broad_colors=broad,
        singleton_broad_colors=singleton,
        maximum_slice_weight=maximum,
    )


def projected_positive_quartic_search(
    form: PositiveQuarticForm, *, iterations: int = 80
) -> tuple[float, np.ndarray]:
    """Return a deterministic finite lower bound for the unit-sphere maximum."""

    if iterations < 0:
        raise ValueError("iterations must be nonnegative")
    if form.indices.size == 0:
        return 0.0, np.zeros(form.dimension, dtype=float)
    marginal = np.zeros(form.dimension, dtype=float)
    for position in range(4):
        np.add.at(marginal, form.indices[:, position], form.coefficients)
    active = np.flatnonzero(marginal > 0)
    starts: list[np.ndarray] = []
    uniform = np.zeros(form.dimension, dtype=float)
    uniform[active] = 1.0 / math.sqrt(len(active))
    starts.append(uniform)
    for term_index in np.argsort(-form.coefficients)[: min(24, len(form.coefficients))]:
        vector = np.zeros(form.dimension, dtype=float)
        support = np.unique(form.indices[int(term_index)])
        vector[support] = 1.0 / math.sqrt(len(support))
        # A tiny positive background lets ascent discover overlapping terms.
        vector[active] += 1.0e-8 / math.sqrt(len(active))
        vector /= np.linalg.norm(vector)
        starts.append(vector)

    best_value = -math.inf
    best_vector = starts[0]
    for initial in starts:
        vector = initial.copy()
        value, gradient = form.value_and_gradient(vector)
        for _ in range(iterations):
            tangent = gradient - vector * float(np.dot(vector, gradient))
            tangent_norm = float(np.linalg.norm(tangent))
            if tangent_norm < 1.0e-12:
                break
            step = 0.5 / max(1.0, tangent_norm)
            slope = float(np.dot(tangent, tangent))
            accepted = False
            for _ in range(24):
                candidate = np.maximum(vector + step * tangent, 0.0)
                candidate_norm = float(np.linalg.norm(candidate))
                if candidate_norm == 0.0:
                    step *= 0.5
                    continue
                candidate /= candidate_norm
                candidate_value, candidate_gradient = form.value_and_gradient(candidate)
                if candidate_value >= value + 1.0e-8 * step * slope:
                    vector = candidate
                    value = candidate_value
                    gradient = candidate_gradient
                    accepted = True
                    break
                step *= 0.5
            if not accepted:
                break
        if value > best_value:
            best_value = value
            best_vector = vector
    return float(best_value), best_vector
