"""Exact finite replays for post-peeling mask stability.

This module accompanies the hostile audit of masked carrier ANOVA.  It is
deliberately finite-dimensional: the identities are linear algebra, while
the affine F_3 example is a method obstruction rather than a QP
prime-power counterexample.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

import numpy as np


@dataclass(frozen=True)
class HermitianAnova:
    centered: np.ndarray
    broad: np.ndarray
    degree_vector: np.ndarray
    degree_fluctuation: np.ndarray
    covariance: np.ndarray


def hermitian_masked_anova(kernel: np.ndarray) -> HermitianAnova:
    """Return the exact constant/degree/broad decomposition of a kernel."""

    kernel = np.asarray(kernel, dtype=complex)
    if kernel.ndim != 2 or kernel.shape[0] != kernel.shape[1]:
        raise ValueError("kernel must be square")
    if not np.allclose(kernel, kernel.conj().T):
        raise ValueError("kernel must be Hermitian")
    n = kernel.shape[0]
    one = np.ones(n, dtype=complex)
    u = one / np.sqrt(n)
    projection = np.eye(n, dtype=complex) - np.outer(u, u.conj())
    degree = kernel @ one
    mean_degree = np.vdot(one, degree) / n
    fluctuation = degree - mean_degree * one
    w = fluctuation / np.sqrt(n)
    broad = projection @ kernel @ projection
    centered = kernel - (mean_degree / n) * np.ones((n, n), dtype=complex)
    covariance = projection @ (kernel @ kernel) @ projection - np.outer(w, w.conj())
    return HermitianAnova(
        centered=centered,
        broad=broad,
        degree_vector=degree,
        degree_fluctuation=fluctuation,
        covariance=covariance,
    )


@dataclass(frozen=True)
class RectangularAnova:
    centered: np.ndarray
    broad: np.ndarray
    output_degree_channel: np.ndarray
    input_degree_channel: np.ndarray
    input_covariance: np.ndarray
    output_covariance: np.ndarray


def rectangular_anova(matrix: np.ndarray) -> RectangularAnova:
    """Two-sided ANOVA for an arbitrary complex rectangular operator."""

    matrix = np.asarray(matrix, dtype=complex)
    m, n = matrix.shape
    u = np.ones(m, dtype=complex) / np.sqrt(m)
    v = np.ones(n, dtype=complex) / np.sqrt(n)
    p = np.eye(m, dtype=complex) - np.outer(u, u.conj())
    q = np.eye(n, dtype=complex) - np.outer(v, v.conj())
    alpha = np.vdot(u, matrix @ v)
    broad = p @ matrix @ q
    output_channel = p @ matrix @ v
    input_channel = q @ matrix.conj().T @ u
    centered = matrix - alpha * np.outer(u, v.conj())
    input_covariance = q @ matrix.conj().T @ p @ matrix @ q
    output_covariance = p @ matrix @ q @ matrix.conj().T @ p
    return RectangularAnova(
        centered=centered,
        broad=broad,
        output_degree_channel=output_channel,
        input_degree_channel=input_channel,
        input_covariance=input_covariance,
        output_covariance=output_covariance,
    )


def path_pair_mask() -> np.ndarray:
    """The smallest diagonal-one 0/1 pair mask with no Hilbert Gram lift."""

    return np.array([[1, 1, 0], [1, 1, 1], [0, 1, 1]], dtype=float)


def positive_gram_with_indefinite_threshold() -> np.ndarray:
    """A positive Gram matrix whose 1/2 entry threshold is the path mask."""

    return np.array(
        [[1.0, 3.0 / 5.0, 1.0 / 10.0],
         [3.0 / 5.0, 1.0, 3.0 / 5.0],
         [1.0 / 10.0, 3.0 / 5.0, 1.0]],
        dtype=float,
    )


def two_carrier_lift_gap(size: int) -> tuple[float, float]:
    """Norms of the scalar and a PSD-masked two-carrier operators.

    The scalar rows are identical, hence output centering kills them.  In
    the lift, the first carrier uses the all-ones correlation matrix and
    the second the identity correlation matrix.  On the flat unit vector
    the centered lifted energy is exactly ``(size-1)/2``.
    """

    if size < 2:
        raise ValueError("size must be at least two")
    scalar = np.ones((2, size), dtype=float)
    p_two = np.eye(2) - np.ones((2, 2)) / 2
    scalar_norm = float(np.linalg.norm(p_two @ scalar, ord=2))

    z = np.ones(size, dtype=float) / np.sqrt(size)
    first = np.zeros(size, dtype=float)
    first[0] = np.sum(z)
    second = z.copy()
    centered_energy = 0.5 * float(np.linalg.norm(first - second) ** 2)
    return scalar_norm, centered_energy


def _add_mod_three(x: tuple[int, ...], y: tuple[int, ...], scale: int = 1) -> tuple[int, ...]:
    return tuple((a + scale * b) % 3 for a, b in zip(x, y))


def affine_directions(dimension: int) -> list[tuple[int, ...]]:
    """Canonical projective directions in F_3^dimension."""

    directions: list[tuple[int, ...]] = []
    for vector in product(range(3), repeat=dimension):
        if not any(vector):
            continue
        first = next(value for value in vector if value)
        if first == 1:
            directions.append(vector)
    return directions


def affine_triangle_factor(dimension: int, direction: tuple[int, ...]) -> np.ndarray:
    """Adjacency matrix of the affine-line triangle factor in one direction."""

    points = list(product(range(3), repeat=dimension))
    index = {point: i for i, point in enumerate(points)}
    matrix = np.zeros((len(points), len(points)), dtype=float)
    for point in points:
        i = index[point]
        for scale in (1, 2):
            j = index[_add_mod_three(point, direction, scale)]
            matrix[i, j] = 1.0
    return matrix


@dataclass(frozen=True)
class AffineTriangleFamily:
    factors: tuple[np.ndarray, ...]
    full_sum: np.ndarray
    subspace_sum: np.ndarray
    selected_count: int
    subspace_dimension: int


def affine_triangle_family(dimension: int, subspace_dimension: int) -> AffineTriangleFamily:
    """Build the full and a coherent subspace family of triangle factors."""

    if not 1 <= subspace_dimension < dimension:
        raise ValueError("need 1 <= subspace_dimension < dimension")
    directions = affine_directions(dimension)
    factors = tuple(affine_triangle_factor(dimension, direction) for direction in directions)
    full = np.sum(factors, axis=0)
    selected = [
        factor
        for factor, direction in zip(factors, directions)
        if all(value == 0 for value in direction[subspace_dimension:])
    ]
    return AffineTriangleFamily(
        factors=factors,
        full_sum=full,
        subspace_sum=np.sum(selected, axis=0),
        selected_count=len(selected),
        subspace_dimension=subspace_dimension,
    )


def sylvester_hadamard(order: int) -> np.ndarray:
    """Return the Sylvester Hadamard matrix of power-of-two order."""

    if order < 1 or order & (order - 1):
        raise ValueError("order must be a power of two")
    matrix = np.ones((1, 1), dtype=float)
    while matrix.shape[0] < order:
        matrix = np.block([[matrix, matrix], [matrix, -matrix]])
    return matrix


def zero_one_gamma2_lower_bound(order: int) -> float:
    """Certified lower bound for a 0/1 mask derived from a Hadamard matrix."""

    # gamma_2(H)=sqrt(order), gamma_2(J)=1, and H=2M-J.
    return (np.sqrt(order) - 1.0) / 2.0
