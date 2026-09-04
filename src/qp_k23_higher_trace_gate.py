"""Higher-trace consequences of the slope-block K_(3,2) elimination.

The module is deliberately graph theoretic after the two elementary
arithmetic identities have been isolated.  It records exactly what a bound
for common neighbours of three left vertices can and cannot say about the
operator norm of a binary incidence matrix.

Nothing in this file asserts the missing reciprocal-height aggregation
estimate for an actual prime-power slope block.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
import math
from typing import Mapping, Sequence

import numpy as np


Triple = tuple[int, int, int]


def cross3(x: Sequence[int], y: Sequence[int]) -> Triple:
    """Return the integral cross product of two three-vectors."""

    if len(x) != 3 or len(y) != 3:
        raise ValueError("cross3 requires two three-vectors")
    return (
        int(x[1]) * int(y[2]) - int(x[2]) * int(y[1]),
        int(x[2]) * int(y[0]) - int(x[0]) * int(y[2]),
        int(x[0]) * int(y[1]) - int(x[1]) * int(y[0]),
    )


def dot3(x: Sequence[int], y: Sequence[int]) -> int:
    if len(x) != 3 or len(y) != 3:
        raise ValueError("dot3 requires two three-vectors")
    return sum(int(a) * int(b) for a, b in zip(x, y, strict=True))


def primitive_part(vector: Sequence[int]) -> tuple[Triple, int]:
    """Return ``(primitive vector, content)`` with a fixed first-sign rule."""

    if len(vector) != 3:
        raise ValueError("primitive_part requires a three-vector")
    values = tuple(int(value) for value in vector)
    content = math.gcd(math.gcd(abs(values[0]), abs(values[1])), abs(values[2]))
    if content == 0:
        raise ValueError("the zero vector has no primitive part")
    primitive = tuple(value // content for value in values)
    first_nonzero = next(value for value in primitive if value)
    if first_nonzero < 0:
        primitive = tuple(-value for value in primitive)
    return primitive, content  # type: ignore[return-value]


def primitive_height(vector: Sequence[int]) -> int:
    primitive, _ = primitive_part(vector)
    return max(abs(value) for value in primitive)


@dataclass(frozen=True)
class K23EliminationLedger:
    """Exact algebra behind two columns with three common row pairs.

    The left vertices are ``(a_i,A_i)`` for ``i=1,2,3``.  The two right
    vertices are ``(c_1,d_1)`` and ``(c_2,d_2)``.  Thus ``p=(c_1,c_2)``
    and ``q=(d_1,d_2)`` are the coordinate projections of those columns.
    """

    a: Triple
    A: Triple
    p: tuple[int, int]
    q: tuple[int, int]
    e: tuple[tuple[int, int], ...]
    column_determinant: int
    first_recovery: Triple
    second_recovery: Triple
    h: Triple
    primitive_h: Triple
    content: int
    height: int
    orthogonal_to_a: bool
    orthogonal_to_A: bool


def k23_elimination_ledger(
    a: Sequence[int],
    A: Sequence[int],
    p: Sequence[int],
    q: Sequence[int],
) -> K23EliminationLedger:
    """Replay the determinant recovery identities in the K_(3,2) lemma."""

    if len(a) != 3 or len(A) != 3:
        raise ValueError("a and A must be three-vectors")
    if len(p) != 2 or len(q) != 2:
        raise ValueError("p and q must be pairs")
    aa = tuple(int(value) for value in a)
    AA = tuple(int(value) for value in A)
    c1, c2 = (int(value) for value in p)
    d1, d2 = (int(value) for value in q)
    e = tuple((aa[i] * c1 - AA[i] * d1, aa[i] * c2 - AA[i] * d2) for i in range(3))
    determinant = c1 * d2 - c2 * d1
    first = tuple(d2 * e1 - d1 * e2 for e1, e2 in e)
    second = tuple(c2 * e1 - c1 * e2 for e1, e2 in e)
    h = cross3(aa, AA)
    primitive, content = primitive_part(h)
    return K23EliminationLedger(
        a=aa,  # type: ignore[arg-type]
        A=AA,  # type: ignore[arg-type]
        p=(c1, c2),
        q=(d1, d2),
        e=e,
        column_determinant=determinant,
        first_recovery=first,  # type: ignore[arg-type]
        second_recovery=second,  # type: ignore[arg-type]
        h=h,
        primitive_h=primitive,
        content=content,
        height=max(abs(value) for value in primitive),
        orthogonal_to_a=dot3(h, aa) == 0,
        orthogonal_to_A=dot3(h, AA) == 0,
    )


def short_orthogonals_are_collinear(
    a: Sequence[int], h: Sequence[int], other_h: Sequence[int]
) -> bool:
    """Check the exact ``D^2<min(a)`` collinearity argument.

    Both short vectors must be orthogonal to the primitive positive vector
    ``a``.  If their cross product has sup norm below ``min(a)``, it cannot
    be a nonzero integral multiple of ``a``.
    """

    aa = tuple(int(value) for value in a)
    hh = tuple(int(value) for value in h)
    kk = tuple(int(value) for value in other_h)
    if math.gcd(math.gcd(abs(aa[0]), abs(aa[1])), abs(aa[2])) != 1:
        raise ValueError("a must be primitive")
    if min(aa) <= 0:
        raise ValueError("a must be positive")
    if dot3(aa, hh) or dot3(aa, kk):
        raise ValueError("both short vectors must be orthogonal to a")
    cross = cross3(hh, kk)
    if max(abs(value) for value in cross) >= min(aa):
        raise ValueError("the supplied vectors are not in the short range")
    return cross == (0, 0, 0)


@dataclass(frozen=True)
class K23MomentLedger:
    left_vertices: int
    right_vertices: int
    edge_count: int
    maximum_right_degree: int
    operator_norm_squared: float
    sixth_trace: float
    left_triple_excess: int
    right_pair_excess: int
    global_excess_operator_bound: float
    local_excess_operator_bound: float
    maximum_local_excess: int


def _binary_matrix(matrix: Sequence[Sequence[int]]) -> np.ndarray:
    array = np.asarray(matrix, dtype=int)
    if array.ndim != 2:
        raise ValueError("matrix must be two-dimensional")
    if np.any((array != 0) & (array != 1)):
        raise ValueError("matrix must be binary")
    return array


def triple_codegrees(matrix: Sequence[Sequence[int]]) -> dict[Triple, int]:
    array = _binary_matrix(matrix)
    answer: dict[Triple, int] = {}
    for triple in combinations(range(array.shape[0]), 3):
        answer[triple] = int(np.sum(np.prod(array[list(triple), :], axis=0)))
    return answer


def k23_moment_ledger(matrix: Sequence[Sequence[int]]) -> K23MomentLedger:
    """Compute the exact K_(3,2) excess and two rigorous norm bounds.

    If ``m(y,y')`` is the right-pair codegree, then

    ``sum_X binom(t_3(X),2) = sum_{y<y'} binom(m(y,y'),3)``.

    Splitting ``m=min(m,2)+(m-2)_+`` and using Frobenius/Hölder gives

    ``||B||^2 <= Delta_R+2(n_R-1)+(12*n_R*K)^(1/3)``.

    Rowwise Schur gives the second bound with
    ``n_R^(2/3)*(6*max_y K_y)^(1/3)``.
    """

    array = _binary_matrix(matrix)
    n_left, n_right = array.shape
    gram = array.T @ array
    degrees = np.diag(gram)
    maximum_degree = int(max(degrees, default=0))
    singular_values = np.linalg.svd(array.astype(float), compute_uv=False)
    operator_squared = float(max(singular_values, default=0.0) ** 2)
    sixth_trace = float(np.trace(np.linalg.matrix_power(gram.astype(float), 3)))

    triples = triple_codegrees(array)
    left_excess = sum(math.comb(value, 2) for value in triples.values())
    right_excess = 0
    local = [0 for _ in range(n_right)]
    for first, second in combinations(range(n_right), 2):
        codegree = int(gram[first, second])
        contribution = math.comb(codegree, 3)
        right_excess += contribution
        local[first] += contribution
        local[second] += contribution
    if left_excess != right_excess:
        raise AssertionError("the K_(3,2) double count failed")

    global_bound = (
        maximum_degree
        + 2 * max(0, n_right - 1)
        + (12 * n_right * right_excess) ** (1 / 3)
    )
    maximum_local = max(local, default=0)
    local_bound = (
        maximum_degree
        + 2 * max(0, n_right - 1)
        + n_right ** (2 / 3) * (6 * maximum_local) ** (1 / 3)
    )
    return K23MomentLedger(
        left_vertices=n_left,
        right_vertices=n_right,
        edge_count=int(np.sum(array)),
        maximum_right_degree=maximum_degree,
        operator_norm_squared=operator_squared,
        sixth_trace=sixth_trace,
        left_triple_excess=left_excess,
        right_pair_excess=right_excess,
        global_excess_operator_bound=float(global_bound),
        local_excess_operator_bound=float(local_bound),
        maximum_local_excess=maximum_local,
    )


@dataclass(frozen=True)
class HeightExcessLedger:
    k23_excess: int
    anchored_reciprocal_height_mass: float
    maximum_local_reciprocal_height_mass: float
    global_height_upper_bound: float
    local_height_upper_bound: float


def height_excess_ledger(
    matrix: Sequence[Sequence[int]],
    heights: Mapping[Triple, int],
    degree_scale: int,
) -> HeightExcessLedger:
    """Check the exact reciprocal-height consequence of a codegree cap.

    The input hypothesis is checked triple by triple:

    ``t_3(X) <= 1 + D/H(X)``.

    It implies

    ``K <= (D/2) sum_X t_3(X)/H(X)`` and, for every right anchor ``y``,
    ``K_y <= D sum_{X subset N(y)} 1/H(X)``.
    """

    array = _binary_matrix(matrix)
    n_left, n_right = array.shape
    triples = triple_codegrees(array)
    reciprocal_mass = 0.0
    local_mass = [0.0 for _ in range(n_right)]
    k23_excess = 0
    for triple, codegree in triples.items():
        if triple not in heights:
            raise ValueError(f"missing height for triple {triple}")
        height = int(heights[triple])
        if height <= 0:
            raise ValueError("heights must be positive")
        if codegree > 1 + degree_scale / height + 1.0e-12:
            raise ValueError("the K_(3,2) height cap fails")
        k23_excess += math.comb(codegree, 2)
        reciprocal_mass += codegree / height
        if codegree:
            common = np.prod(array[list(triple), :], axis=0)
            for right in np.flatnonzero(common):
                local_mass[int(right)] += 1.0 / height

    global_upper = degree_scale * reciprocal_mass / 2
    maximum_local_mass = max(local_mass, default=0.0)
    local_upper = degree_scale * maximum_local_mass
    if k23_excess > global_upper + 1.0e-9:
        raise AssertionError("the global reciprocal-height bound failed")

    gram = array.T @ array
    for right in range(n_right):
        local_excess = sum(
            math.comb(int(gram[right, other]), 3)
            for other in range(n_right)
            if other != right
        )
        if local_excess > degree_scale * local_mass[right] + 1.0e-9:
            raise AssertionError("a local reciprocal-height bound failed")
    return HeightExcessLedger(
        k23_excess=k23_excess,
        anchored_reciprocal_height_mass=reciprocal_mass,
        maximum_local_reciprocal_height_mass=maximum_local_mass,
        global_height_upper_bound=global_upper,
        local_height_upper_bound=local_upper,
    )


def disjoint_complete_blocks(blocks: int, order: int) -> np.ndarray:
    """Return the incidence matrix of ``blocks`` disjoint copies of K_(L,L)."""

    if blocks < 1 or order < 1:
        raise ValueError("blocks and order must be positive")
    matrix = np.zeros((blocks * order, blocks * order), dtype=int)
    for block in range(blocks):
        start = block * order
        matrix[start : start + order, start : start + order] = 1
    return matrix


def affine_tangent_triple_height(parameters: Sequence[int]) -> int:
    """Primitive height for three points ``(m+t,m+h+t)``.

    The common ``m`` and nonzero ``h`` cancel from the primitive part, so
    the answer is the diameter of the three parameters divided by the gcd
    of their two consecutive gaps.
    """

    if len(parameters) != 3:
        raise ValueError("three parameters are required")
    first, middle, last = sorted(int(value) for value in parameters)
    if first == middle or middle == last:
        raise ValueError("parameters must be distinct")
    left_gap = middle - first
    right_gap = last - middle
    return (last - first) // math.gcd(left_gap, right_gap)

