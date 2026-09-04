"""Finite algebra for the centered-cubic band-pass/trace gate.

The routines in this file replay exact tensor identities and finite matrix
barriers.  They do not certify an asymptotic norm estimate for the actual
prime-power carry tensor.
"""

from __future__ import annotations

import numpy as np


def _sinc(value: np.ndarray | float) -> np.ndarray:
    values = np.asarray(value, dtype=float)
    return np.sinc(values / np.pi)


def spline_cosine_transform(
    frequency: np.ndarray | float, bandwidth: float, order: int = 8
) -> np.ndarray:
    """Cosine transform of the compact B-spline probability.

    The law is ``B/2 + sum(U_j)``, where the ``U_j`` are uniform on
    ``[-B/(6q), B/(6q)]``.
    """

    if bandwidth <= 0.0:
        raise ValueError("bandwidth must be positive")
    if order < 1:
        raise ValueError("order must be positive")
    omega = np.asarray(frequency, dtype=float)
    return (
        np.cos(0.5 * bandwidth * omega)
        * _sinc(bandwidth * omega / (6.0 * order)) ** order
    )


def raw_second_tensor(nodes: np.ndarray, transform) -> np.ndarray:
    """Return ``E[cos(t u_i) cos(t u_j)]`` from a cosine transform."""

    u = np.asarray(nodes, dtype=float)
    return 0.5 * (
        transform(u[:, None] - u[None, :])
        + transform(u[:, None] + u[None, :])
    )


def signed_cubic_tensors(nodes: np.ndarray, transform) -> tuple[np.ndarray, ...]:
    """Return all-plus, one-minus, symmetrized one-minus, and raw tensors."""

    u = np.asarray(nodes, dtype=float)
    ui = u[:, None, None]
    uj = u[None, :, None]
    uk = u[None, None, :]
    all_plus = transform(ui + uj + uk)
    minus_k = transform(ui + uj - uk)
    minus_j = transform(ui - uj + uk)
    minus_i = transform(-ui + uj + uk)
    sym_one_minus = (minus_k + minus_j + minus_i) / 3.0
    raw = 0.25 * all_plus + 0.75 * sym_one_minus
    return all_plus, minus_k, sym_one_minus, raw


def centered_third_tensor(nodes: np.ndarray, transform) -> np.ndarray:
    """Return the exact central third tensor of the cosine features."""

    u = np.asarray(nodes, dtype=float)
    mean = np.asarray(transform(u), dtype=float)
    second = raw_second_tensor(u, transform)
    raw = signed_cubic_tensors(u, transform)[-1]
    centered = raw.copy()
    centered -= np.einsum("i,jk->ijk", mean, second)
    centered -= np.einsum("j,ik->ijk", mean, second)
    centered -= np.einsum("k,ij->ijk", mean, second)
    centered += 2.0 * np.einsum("i,j,k->ijk", mean, mean, mean)
    return centered


def cubic_value(tensor: np.ndarray, coefficients: np.ndarray) -> float:
    y = np.asarray(coefficients, dtype=float)
    return float(np.einsum("ijk,i,j,k->", tensor, y, y, y, optimize=True))


def scalar_centering_identity(
    nodes: np.ndarray, coefficients: np.ndarray, transform
) -> tuple[float, float, float, float]:
    """Replay ``kappa3 = raw3 - 3*m*V - m**3``.

    Returns ``(central_third, right_hand_side, mean, variance)``.
    """

    u = np.asarray(nodes, dtype=float)
    y = np.asarray(coefficients, dtype=float)
    mean_vector = np.asarray(transform(u), dtype=float)
    second = raw_second_tensor(u, transform)
    raw = signed_cubic_tensors(u, transform)[-1]
    mean = float(mean_vector @ y)
    raw_second = float(y @ second @ y)
    variance = raw_second - mean * mean
    raw_third = cubic_value(raw, y)
    central = cubic_value(centered_third_tensor(u, transform), y)
    right = raw_third - 3.0 * mean * variance - mean**3
    return central, right, mean, variance


def partial_trace(tensor: np.ndarray) -> np.ndarray:
    """Contract the first two coefficient indices of a cubic tensor."""

    return np.einsum("iik->k", np.asarray(tensor, dtype=float))


def sym_one_minus_partial_trace(nodes: np.ndarray, transform) -> np.ndarray:
    """Exact trace formula for the symmetrized one-minus tensor.

    For ``S_ijk=(C(ui+uj-uk)+C(ui-uj+uk)+C(-ui+uj+uk))/3``, this returns

        (2 M C(u_i) + sum_j C(2 u_j-u_i))/3.
    """

    u = np.asarray(nodes, dtype=float)
    count = len(u)
    return (
        2.0 * count * transform(u)
        + np.sum(transform(2.0 * u[:, None] - u[None, :]), axis=0)
    ) / 3.0


def hard_carry_slice(
    nodes: np.ndarray, fixed_index: int, bandwidth: float, core_radius: float
) -> np.ndarray:
    """Return the hard one-minus slice ``|B(ui+uj-uk)| <= c``."""

    u = np.asarray(nodes, dtype=float)
    if bandwidth <= 0.0 or core_radius < 0.0:
        raise ValueError("invalid bandwidth or core radius")
    residual = u[fixed_index] + u[:, None] - u[None, :]
    return (np.abs(bandwidth * residual) <= core_radius).astype(float)


def side_block_max_degrees(
    matrix: np.ndarray, row_sides: np.ndarray, column_sides: np.ndarray
) -> tuple[int, int]:
    """Maximum row and column support sizes inside all side blocks."""

    support = np.asarray(matrix) != 0
    row_sides = np.asarray(row_sides)
    column_sides = np.asarray(column_sides)
    max_row = 0
    max_column = 0
    for row_side in np.unique(row_sides):
        rows = row_sides == row_side
        for column_side in np.unique(column_sides):
            columns = column_sides == column_side
            block = support[np.ix_(rows, columns)]
            if block.size:
                max_row = max(max_row, int(np.max(np.sum(block, axis=1))))
                max_column = max(
                    max_column, int(np.max(np.sum(block, axis=0)))
                )
    return max_row, max_column


def trace_and_row_sum_barrier_tensor(
    dimension: int, scale: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """A symmetric trace-free cubic of diagonal norm ``scale``.

    The tensor is supported on a two-dimensional subspace perpendicular to
    the all-ones vector.  Consequently contraction with the all-ones vector
    vanishes in every mode.  This is an identity-only barrier, not an actual
    carry tensor.
    """

    if dimension < 3:
        raise ValueError("dimension must be at least three")
    if scale < 0.0:
        raise ValueError("scale must be nonnegative")
    e1 = np.zeros(dimension)
    e1[:2] = (1.0, -1.0)
    e1 /= np.linalg.norm(e1)
    e2 = np.zeros(dimension)
    e2[:3] = (1.0, 1.0, -2.0)
    e2 /= np.linalg.norm(e2)
    tensor = np.einsum("i,j,k->ijk", e1, e1, e1)
    tensor -= np.einsum("i,j,k->ijk", e1, e2, e2)
    tensor -= np.einsum("i,j,k->ijk", e2, e1, e2)
    tensor -= np.einsum("i,j,k->ijk", e2, e2, e1)
    return scale * tensor, e1, e2


def zero_sum_partial_permutation_barrier(order: int) -> np.ndarray:
    """A zero-row/column-sum, trace-zero matrix of norm ``asymp sqrt(R)``.

    On the cyclic group of size ``4R``, take

        R^(-1/2) sum_(r=1)^R (S^r-S^(r+R)).

    Each summand is a difference of two partial/permutation maps.  This is a
    finite linear-algebra barrier, not an actual prime-log slice.
    """

    if order < 2:
        raise ValueError("order must be at least two")
    dimension = 4 * order
    identity = np.eye(dimension)
    matrix = np.zeros((dimension, dimension))
    for shift in range(1, order + 1):
        matrix += np.roll(identity, shift, axis=0)
        matrix -= np.roll(identity, shift + order, axis=0)
    return matrix / np.sqrt(order)
