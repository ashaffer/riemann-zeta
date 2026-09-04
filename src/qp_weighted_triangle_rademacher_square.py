"""Weighted residual-triangle Rademacher square functions.

For an edge ``e={i,j,k}`` and color coefficients ``z`` the QP carry block is

    M_e[i,j]=z[k],  M_e[i,k]=z[j],  M_e[j,k]=z[i]

and is symmetric.  If the edges are partitioned into classes which are
vertex matchings, the class matrices ``A_v`` satisfy a sharp randomized
fourth-trace estimate.  The proof uses only linearity of the triple system
(two edges meet in at most one vertex) and the maximum vertex degree.

The all-plus, arithmetically ordered unconditionality estimate remains open;
this module records the exact finite identities used in that reduction.
"""

from __future__ import annotations

from itertools import product
from typing import Iterable, Sequence

import numpy as np


Edge = tuple[int, int, int]


def weighted_edge_matrix(n: int, edge: Sequence[int], z: Sequence[complex]) -> np.ndarray:
    """Build the symmetric weighted ``3 x 3`` edge block in ``n`` vertices."""

    raw = tuple(int(v) for v in edge)
    if len(raw) != 3 or len(set(raw)) != 3:
        raise ValueError("edge must have three distinct vertices")
    if min(raw) < 0 or max(raw) >= n:
        raise ValueError("edge vertex outside matrix range")
    weights = np.asarray(z, dtype=complex)
    if weights.size != n:
        raise ValueError("z must have one coefficient per vertex")
    matrix = np.zeros((n, n), dtype=complex)
    i, j, k = raw
    matrix[i, j] = matrix[j, i] = weights[k]
    matrix[i, k] = matrix[k, i] = weights[j]
    matrix[j, k] = matrix[k, j] = weights[i]
    return matrix


def validate_linear_matching_partition(
    n: int, classes: Sequence[Sequence[Sequence[int]]]
) -> tuple[list[Edge], int]:
    """Validate matching classes and global linearity; return edges and degree."""

    edges: list[Edge] = []
    used_pairs: set[tuple[int, int]] = set()
    degrees = np.zeros(n, dtype=int)
    for matching in classes:
        used_vertices: set[int] = set()
        for raw in matching:
            edge = tuple(int(v) for v in raw)
            if len(edge) != 3 or len(set(edge)) != 3:
                raise ValueError("all edges must have three distinct vertices")
            if min(edge) < 0 or max(edge) >= n:
                raise ValueError("edge vertex outside range")
            if used_vertices.intersection(edge):
                raise ValueError("each class must be a vertex matching")
            used_vertices.update(edge)
            for i in range(3):
                for j in range(i + 1, 3):
                    pair = tuple(sorted((edge[i], edge[j])))
                    if pair in used_pairs:
                        raise ValueError("the global triple system must be linear")
                    used_pairs.add(pair)
            for vertex in edge:
                degrees[vertex] += 1
            edges.append(edge)
    return edges, int(degrees.max(initial=0))


def weighted_class_matrices(
    n: int,
    classes: Sequence[Sequence[Sequence[int]]],
    z: Sequence[complex],
) -> list[np.ndarray]:
    """Return one weighted carry matrix for every matching class."""

    validate_linear_matching_partition(n, classes)
    answers: list[np.ndarray] = []
    for matching in classes:
        matrix = np.zeros((n, n), dtype=complex)
        for edge in matching:
            matrix += weighted_edge_matrix(n, edge, z)
        answers.append(matrix)
    return answers


def schatten_fourth_power(matrix: np.ndarray) -> float:
    """Return ``tr((A* A)^2)``."""

    array = np.asarray(matrix)
    gram = array.conj().T @ array
    return float(np.trace(gram @ gram).real)


def exact_rademacher_fourth_average(matrices: Sequence[np.ndarray]) -> float:
    """Average the fourth trace over every sign choice (small finite replay)."""

    if not matrices:
        return 0.0
    if len(matrices) > 16:
        raise ValueError("exact sign enumeration is limited to 16 matrices")
    total = 0.0
    for signs in product((-1.0, 1.0), repeat=len(matrices)):
        combined = sum(sign * matrix for sign, matrix in zip(signs, matrices))
        total += schatten_fourth_power(combined)
    return total / (2 ** len(matrices))


def rademacher_upper_bound(max_degree: int, z_l2: float) -> float:
    """Return the proved universal upper bound ``42*Delta*||z||_2^4``."""

    if max_degree < 0 or z_l2 < 0:
        raise ValueError("degree and norm must be nonnegative")
    return 42.0 * max_degree * z_l2**4


def coefficient_sensitive_square_function_bound(
    max_degree: int, z_l2: float, z_linf: float
) -> float:
    """Bound either square-function Gram using coefficient dispersion.

    Put ``theta=||z||_infinity^2/||z||_2^2``.  The proved bound is

    ``16*Delta*min(1,Delta*theta)*||z||_2^4``.

    The constant is deliberately safe.  The self-edge terms cost at most
    ``12*Delta*theta*||z||_2^4`` and the cross-edge diagonal costs at most
    ``4*Delta*min(1,Delta*theta)*||z||_2^4``.
    """

    if max_degree < 0 or z_l2 < 0 or z_linf < 0:
        raise ValueError("degree and norms must be nonnegative")
    if z_l2 == 0.0 or max_degree == 0:
        return 0.0
    if z_linf > z_l2 * (1.0 + 1.0e-12):
        raise ValueError("the infinity norm cannot exceed the l2 norm")
    theta = min(1.0, (z_linf / z_l2) ** 2)
    return 16.0 * max_degree * min(1.0, max_degree * theta) * z_l2**4


def coefficient_sensitive_rademacher_bound(
    max_degree: int, z_l2: float, z_linf: float
) -> float:
    """Return the coefficient-sensitive randomized fourth-trace bound.

    The elementary noncommutative Rademacher expansion uses one right and
    two left square functions, so the safe constant is ``3*16=48``.
    """

    return 3.0 * coefficient_sensitive_square_function_bound(
        max_degree, z_l2, z_linf
    )


def comparable_support_rademacher_bound(
    max_degree: int,
    support_size: int,
    z_l2: float,
    *,
    squared_comparability: float = 4.0,
) -> float:
    """Specialize the randomized bound to one coefficient-height bin.

    The hypothesis encoded by ``squared_comparability`` is

    ``||z||_infinity^2 <= squared_comparability*||z||_2^2/support_size``.

    A factor-two bin in coefficient magnitude has
    ``squared_comparability<=4``.
    """

    if support_size <= 0:
        raise ValueError("support_size must be positive")
    if squared_comparability < 1.0:
        raise ValueError("squared_comparability must be at least one")
    if max_degree < 0 or z_l2 < 0:
        raise ValueError("degree and norm must be nonnegative")
    return (
        48.0
        * max_degree
        * min(1.0, squared_comparability * max_degree / support_size)
        * z_l2**4
    )


def square_function_gram_bounds(matrices: Sequence[np.ndarray]) -> tuple[float, float]:
    """Return ``(||sum A* A||_HS^2, ||sum A A*||_HS^2)``."""

    if not matrices:
        return 0.0, 0.0
    right = sum(matrix.conj().T @ matrix for matrix in matrices)
    left = sum(matrix @ matrix.conj().T for matrix in matrices)
    return float(np.linalg.norm(right, "fro") ** 2), float(
        np.linalg.norm(left, "fro") ** 2
    )
