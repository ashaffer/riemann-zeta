#!/usr/bin/env python3
"""Finite identities for the QP projected-Gram cluster gate.

The functions here replay two exact facts from the companion report.

* Unit-spaced packet columns on a shell ``|u| <= w`` have an explicit
  binomial near-null vector.  This is independent of the arithmetic nature
  of the nodes.
* Zeroing finitely many packet centres from the normalized uniform dual is
  governed by one *directional* source quantity ``m.T @ G^-1 @ m``.  A
  condition number for the whole Gramian is stronger than necessary.

Floating point output is only a finite-dimensional replay.  The inequalities
and asymptotic statements are proved algebraically in the report.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import itertools
import json
import math
from typing import Iterable

import numpy as np


SHELL_WIDTH = 1.0 / 5.0
FIXED_SLICE_KILL_EXPONENT = 19.0 / 1000.0
FULL_APERTURE_EXPONENT = 50.0 / 33.0


def cosine_atoms(nodes: Iterable[float], times: Iterable[float]) -> np.ndarray:
    """Return the node-by-time cosine matrix."""

    u = np.asarray(tuple(nodes), dtype=float)
    t = np.asarray(tuple(times), dtype=float)
    if u.ndim != 1 or t.ndim != 1 or len(u) == 0 or len(t) == 0:
        raise ValueError("nodes and times must be nonempty vectors")
    return np.cos(np.outer(u, t))


def carrier_projection(dimension: int) -> np.ndarray:
    """Orthogonal projection onto the complement of the all-ones carrier."""

    if dimension < 2:
        raise ValueError("dimension must be at least two")
    q = np.ones(dimension)
    return np.eye(dimension) - np.outer(q, q) / dimension


def projected_dictionary(
    nodes: Iterable[float], times: Iterable[float]
) -> tuple[np.ndarray, np.ndarray]:
    """Return ``A`` and its carrier-projected dictionary ``V=P A``."""

    matrix = cosine_atoms(nodes, times)
    return matrix, carrier_projection(matrix.shape[0]) @ matrix


def alternating_binomial(order: int) -> np.ndarray:
    """Coefficients of the forward difference of the requested order."""

    if order < 1:
        raise ValueError("order must be positive")
    return np.asarray(
        [(-1.0) ** (order - k) * math.comb(order, k) for k in range(order + 1)]
    )


def central_binomial(order: int) -> int:
    """Return ``sum_k binom(order,k)^2 = binom(2 order,order)``."""

    if order < 0:
        raise ValueError("order must be nonnegative")
    return math.comb(2 * order, order)


def cluster_rayleigh_upper_bound(
    node_count: int,
    order: int,
    width: float = SHELL_WIDTH,
    spacing: float = 1.0,
) -> float:
    """Universal upper bound for the projected packet Gram minimum eigenvalue.

    For centres ``t0, t0+h, ..., t0+order*h`` and nodes ``|u_j|<=width``,
    the alternating binomial vector gives

    ``lambda_min(G) <= M (2 sin(h width/2))^(2 order)/C(2 order,order)``.

    The principal small-arc bound is used, so ``spacing*width <= pi``.
    """

    if node_count < 1 or order < 1 or width <= 0.0 or spacing <= 0.0:
        raise ValueError("parameters must be positive")
    if spacing * width > math.pi:
        raise ValueError("the monotone small-arc bound requires spacing*width <= pi")
    rho = 2.0 * math.sin(spacing * width / 2.0)
    return node_count * rho ** (2 * order) / central_binomial(order)


def log_relative_cluster_bound(
    order: int, width: float = SHELL_WIDTH, spacing: float = 1.0
) -> float:
    """Return ``log(lambda_upper/M)`` without overflowing binomials."""

    if order < 1 or width <= 0.0 or spacing <= 0.0:
        raise ValueError("parameters must be positive")
    if spacing * width > math.pi:
        raise ValueError("the monotone small-arc bound requires spacing*width <= pi")
    rho = 2.0 * math.sin(spacing * width / 2.0)
    return (
        2.0 * order * math.log(rho)
        - math.lgamma(2 * order + 1)
        + 2.0 * math.lgamma(order + 1)
    )


def asymptotic_cluster_rate(
    width: float = SHELL_WIDTH, spacing: float = 1.0
) -> float:
    """Positive rate ``-2 log(sin(h width/2))`` in the relative bound."""

    if not 0.0 < spacing * width < math.pi:
        raise ValueError("require 0 < spacing*width < pi")
    return -2.0 * math.log(math.sin(spacing * width / 2.0))


def guth_maynard_count_exponents(
    saving: float = FIXED_SLICE_KILL_EXPONENT,
    aperture_exponent: float = FULL_APERTURE_EXPONENT,
) -> tuple[float, float, float]:
    """Exponents of the three GM-v2 count terms at ``V=Y^(1-saving)``."""

    if saving < 0.0 or aperture_exponent <= 0.0:
        raise ValueError("saving and aperture exponent must be nonnegative")
    return (
        2.0 * saving,
        -2.0 / 5.0 + 4.0 * saving,
        aperture_exponent - 8.0 / 5.0 + 4.0 * saving,
    )


def critical_packet_slice(side: int = 2) -> np.ndarray:
    """Return a bounded critical count/leverage countermodel.

    Put ``R=side^2`` with even ``side``.  Rows run over all sign vectors in
    ``{-1,1}^R`` whose coordinate sum is ``-side``.  The columns are exactly
    orthogonal, every column has mean ``-1/side=-1/sqrt(R)``, and the carrier
    lies in their span.  Thus the sharp count ``R=epsilon^-2`` and even ideal
    unprojected orthogonality do not force a carrier-leverage gap.
    """

    if side < 2 or side % 2:
        raise ValueError("side must be an even integer at least two")
    packet_count = side * side
    plus_count = (packet_count - side) // 2
    rows: list[np.ndarray] = []
    for positive_positions in itertools.combinations(range(packet_count), plus_count):
        row = -np.ones(packet_count)
        row[list(positive_positions)] = 1.0
        rows.append(row)
    return np.vstack(rows)


def critical_regular_hadamard(power: int = 1, repeats: int = 1) -> np.ndarray:
    """Polynomial-size version of the critical leverage countermodel.

    The base regular Hadamard matrix is ``2 I_4-J_4``.  A signed tensor power
    of order ``R=4^power`` has column Gram ``R I``, all row sums ``-sqrt(R)``,
    and all column means ``-1/sqrt(R)``.  Repeating every row permits any row
    dimension ``M=repeats*R`` while preserving ``A.T A=M I``.
    """

    if power < 1 or repeats < 1:
        raise ValueError("power and repeats must be positive")
    base = 2.0 * np.eye(4) - np.ones((4, 4))
    matrix = base.copy()
    for _ in range(power - 1):
        matrix = np.kron(matrix, base)
    if float(np.sum(matrix[0])) > 0.0:
        matrix = -matrix
    return np.repeat(matrix, repeats, axis=0)


@dataclass(frozen=True)
class SourceCondition:
    packet_count: int
    source_energy: float
    carrier_leverage: float
    source_from_leverage: float
    zeroing_norm_square: float
    maximum_center_residual: float
    carrier_normalization_residual: float
    variational_probe: float


@dataclass(frozen=True)
class ResidualDual:
    carrier_leverage: float
    residual_norm_square: float
    dual_norm_square: float
    carrier_normalization_residual: float
    maximum_center_residual: float
    residual: tuple[float, ...]
    dual: tuple[float, ...]


def carrier_residual_dual(matrix: np.ndarray) -> ResidualDual:
    """Return the normalized carrier residual outside a packet span.

    With ``Pi=A(A.T A)^-1 A.T`` and ``R=(I-Pi)q``, the minimum-norm vector
    satisfying ``A.T y=0`` and ``q.T y=-1`` is exactly

    ``y=-R/(R.T R)``.

    This form removes all irrelevant Gram conditioning.  A full-band kill at
    level ``epsilon`` is precisely the one-sided residual inequality
    ``R.T a(t) >= -epsilon R.T R``.
    """

    atoms = np.asarray(matrix, dtype=float)
    if atoms.ndim != 2 or atoms.shape[0] < 2 or atoms.shape[1] == 0:
        raise ValueError("matrix must have at least two rows and one column")
    dimension, packet_count = atoms.shape
    if np.linalg.matrix_rank(atoms, tol=1e-11) < packet_count:
        raise ValueError("packet matrix must have full column rank")
    q = np.ones(dimension)
    coefficients = np.linalg.solve(atoms.T @ atoms, atoms.T @ q)
    residual = q - atoms @ coefficients
    residual_norm_square = float(residual @ residual)
    if residual_norm_square <= 1e-13:
        raise ValueError("the carrier lies in the packet span")
    dual = -residual / residual_norm_square
    leverage = 1.0 - residual_norm_square / dimension
    return ResidualDual(
        carrier_leverage=float(leverage),
        residual_norm_square=residual_norm_square,
        dual_norm_square=float(dual @ dual),
        carrier_normalization_residual=float(abs(q @ dual + 1.0)),
        maximum_center_residual=float(np.max(np.abs(atoms.T @ dual))),
        residual=tuple(float(value) for value in residual),
        dual=tuple(float(value) for value in dual),
    )


def zero_center_source_condition(matrix: np.ndarray) -> SourceCondition:
    """Replay the exact source/Schur identity for a full-rank packet list.

    If ``A`` has packet atoms as columns, ``m=A.T q/M``, ``V=P A`` and
    ``G=V.T V``, then the minimum-norm normalized dual zeroing the centres is

    ``y=-q/M + V G^-1 m``

    and its squared norm is ``1/M + m.T G^-1 m``.  The latter source energy
    equals ``h/[M(1-h)]``, where ``h`` is the normalized leverage of ``q`` in
    the unprojected packet span.
    """

    atoms = np.asarray(matrix, dtype=float)
    if atoms.ndim != 2 or atoms.shape[0] < 2 or atoms.shape[1] == 0:
        raise ValueError("matrix must have at least two rows and one column")
    dimension, packet_count = atoms.shape
    q = np.ones(dimension)
    projection = carrier_projection(dimension)
    projected = projection @ atoms
    gram = projected.T @ projected
    if np.linalg.matrix_rank(gram, tol=1e-11) < packet_count:
        raise ValueError("projected packet Gramian must be nonsingular")
    mean = atoms.T @ q / dimension
    solved = np.linalg.solve(gram, mean)
    source = float(mean @ solved)
    dual = -q / dimension + projected @ solved

    full_gram = atoms.T @ atoms
    full_solved = np.linalg.solve(full_gram, atoms.T @ q)
    leverage = float(q @ atoms @ full_solved / dimension)
    source_from_leverage = leverage / (dimension * (1.0 - leverage))

    # The optimizing coefficient for the variational formula is G^{-1}m.
    probe = atoms @ solved
    probe_mean = float(np.mean(probe))
    probe_variance_sum = float(np.sum((probe - probe_mean) ** 2))
    variational = probe_mean**2 / probe_variance_sum
    return SourceCondition(
        packet_count=packet_count,
        source_energy=source,
        carrier_leverage=leverage,
        source_from_leverage=source_from_leverage,
        zeroing_norm_square=float(dual @ dual),
        maximum_center_residual=float(np.max(np.abs(atoms.T @ dual))),
        carrier_normalization_residual=float(abs(q @ dual + 1.0)),
        variational_probe=variational,
    )


def next_packet_distance_bound(
    node_count: int,
    packet_count: int,
    width: float = SHELL_WIDTH,
    spacing: float = 1.0,
) -> float:
    """Bound distance of the next projected atom from a consecutive span."""

    if packet_count < 1:
        raise ValueError("packet_count must be positive")
    if spacing * width > math.pi:
        raise ValueError("the monotone small-arc bound requires spacing*width <= pi")
    rho = 2.0 * math.sin(spacing * width / 2.0)
    return math.sqrt(node_count) * rho**packet_count


@dataclass(frozen=True)
class GateLedger:
    shell_width: float
    kill_exponent: float
    allowed_packet_exponent: float
    asymptotic_cluster_rate: float
    relative_log_bound_order_8: float
    relative_log_bound_order_32: float
    guth_maynard_term_exponents: tuple[float, float, float]


def gate_ledger() -> GateLedger:
    """Return the exact fixed-slice constants used in the report."""

    return GateLedger(
        shell_width=SHELL_WIDTH,
        kill_exponent=FIXED_SLICE_KILL_EXPONENT,
        allowed_packet_exponent=2.0 * FIXED_SLICE_KILL_EXPONENT,
        asymptotic_cluster_rate=asymptotic_cluster_rate(),
        relative_log_bound_order_8=log_relative_cluster_bound(8),
        relative_log_bound_order_32=log_relative_cluster_bound(32),
        guth_maynard_term_exponents=guth_maynard_count_exponents(),
    )


def main() -> None:
    print(json.dumps(asdict(gate_ledger()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
