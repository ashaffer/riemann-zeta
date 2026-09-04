"""Exact spectral identities for the QP band-pass partial-permutation gate.

The routines here are deliberately finite and arithmetic-free.  They replay
the Frobenius, rank-one-defect, and four-cycle identities used in the report
``ZETA23-QP-BANDPASS-PARTIAL-PERMUTATION-SPECTRAL-INVERSE-2026-08-15.md``.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Iterable, Mapping, Sequence


ComplexMatrix = Sequence[Sequence[complex]]


@dataclass(frozen=True)
class DefectLedger:
    """Nonnegative pieces of the Schur/Frobenius spectral defect."""

    degree: float
    stable_rank: float
    endpoint: float

    @property
    def total(self) -> float:
        return self.degree + self.stable_rank + self.endpoint


def coherence_length(center: float, bandwidth: float) -> float:
    if center <= 0 or bandwidth <= 0:
        raise ValueError("center and bandwidth must be positive")
    return center / sqrt(bandwidth)


def block_taylor_scales(center: float, bandwidth: float) -> tuple[float, float]:
    """Quadratic and cubic scales on a block of length center/sqrt(bandwidth)."""

    length = coherence_length(center, bandwidth)
    quadratic = bandwidth * length**2 / center**2
    cubic = bandwidth * length**3 / center**3
    return quadratic, cubic


def schur_defect(epsilon: float) -> float:
    """Return ``1-(1-epsilon)^2``."""

    if not 0 <= epsilon <= 1:
        raise ValueError("epsilon must lie in [0,1]")
    return 2 * epsilon - epsilon * epsilon


def spectral_defect_ledger(
    degree_cap: float, frobenius_sq: float, operator_sq: float, value_sq: float
) -> DefectLedger:
    """Split ``degree_cap-value_sq`` into three exact nonnegative defects."""

    tolerance = 1e-12 * max(1.0, degree_cap)
    if not (
        degree_cap + tolerance >= frobenius_sq
        and frobenius_sq + tolerance >= operator_sq
        and operator_sq + tolerance >= value_sq
        and value_sq >= -tolerance
    ):
        raise ValueError("require D >= ||A||_F^2 >= ||A||_op^2 >= |x*Ay|^2")
    return DefectLedger(
        max(0.0, degree_cap - frobenius_sq),
        max(0.0, frobenius_sq - operator_sq),
        max(0.0, operator_sq - value_sq),
    )


def frobenius_sq(matrix: ComplexMatrix) -> float:
    return float(sum(abs(value) ** 2 for row in matrix for value in row))


def matvec_value(
    matrix: ComplexMatrix, left: Sequence[complex], right: Sequence[complex]
) -> complex:
    if len(matrix) != len(left):
        raise ValueError("left vector has wrong length")
    if matrix and any(len(row) != len(right) for row in matrix):
        raise ValueError("right vector has wrong length")
    return sum(
        left[i].conjugate() * matrix[i][j] * right[j]
        for i in range(len(matrix))
        for j in range(len(right))
    )


def rank_one_error_sq(
    matrix: ComplexMatrix,
    left: Sequence[complex],
    right: Sequence[complex],
) -> float:
    """Squared Frobenius error after the phase-normalized endpoint projection.

    The vectors must be unit vectors.  If ``t=|left* matrix right|``, this
    computes the distance to the correctly phased matrix
    ``t left right*``.
    """

    value = matvec_value(matrix, left, right)
    phase = value / abs(value) if value else 1.0 + 0.0j
    target_scale = phase * abs(value)
    return float(
        sum(
            abs(
                matrix[i][j]
                - target_scale * left[i] * right[j].conjugate()
            )
            ** 2
            for i in range(len(matrix))
            for j in range(len(right))
        )
    )


def partial_color_frobenius_sq(
    entries: Mapping[tuple[int, int], tuple[int, complex]],
    colors: Mapping[int, complex],
) -> float:
    """Frobenius mass of a disjoint-support color combination.

    ``entries[(a,b)] = (c, omega)`` encodes pair uniqueness and the matrix
    entry ``colors[c] * omega``.
    """

    return float(
        sum(abs(colors[color] * weight) ** 2 for color, weight in entries.values())
    )


def color_fibre_identity(
    entries: Mapping[tuple[int, int], tuple[int, complex]],
    colors: Mapping[int, complex],
) -> tuple[float, float]:
    """Return both sides of the Hilbert--Schmidt color identity."""

    direct = partial_color_frobenius_sq(entries, colors)
    fibres: dict[int, float] = {}
    for color, weight in entries.values():
        fibres[color] = fibres.get(color, 0.0) + abs(weight) ** 2
    separated = sum(abs(colors.get(color, 0.0)) ** 2 * mass for color, mass in fibres.items())
    return direct, float(separated)


def trace_fourth(matrix: ComplexMatrix) -> float:
    """Compute ``tr((A* A)^2)`` as a Gram-matrix square."""

    if not matrix:
        return 0.0
    columns = len(matrix[0])
    if any(len(row) != columns for row in matrix):
        raise ValueError("matrix must be rectangular")
    total = 0.0
    for first in range(columns):
        for second in range(columns):
            gram = sum(
                row[first].conjugate() * row[second] for row in matrix
            )
            total += abs(gram) ** 2
    return float(total)


def rectangle_expansion(matrix: ComplexMatrix) -> complex:
    """Compute the signed ordered four-cycle expansion of ``tr((A*A)^2)``."""

    if not matrix:
        return 0.0 + 0.0j
    rows = len(matrix)
    columns = len(matrix[0])
    return sum(
        matrix[a1][b1].conjugate()
        * matrix[a1][b2]
        * matrix[a2][b2].conjugate()
        * matrix[a2][b1]
        for a1 in range(rows)
        for a2 in range(rows)
        for b1 in range(columns)
        for b2 in range(columns)
    )


def degenerate_rectangle_mass(matrix: ComplexMatrix) -> float:
    """Upper bound from rectangles with an equal row or an equal column."""

    if not matrix:
        return 0.0
    columns = len(matrix[0])
    row_term = sum(sum(abs(value) ** 2 for value in row) ** 2 for row in matrix)
    column_term = sum(
        sum(abs(matrix[row][column]) ** 2 for row in range(len(matrix))) ** 2
        for column in range(columns)
    )
    return float(row_term + column_term)


def latin_uniform_invariants(order: int) -> tuple[float, float, float]:
    """Frobenius square, fourth trace, and tensor value for a Latin saturator."""

    if order <= 0:
        raise ValueError("order must be positive")
    # Uniform colors on c=-a-b make every matrix entry 1/sqrt(order).
    frobenius = float(order)
    fourth_trace = float(order * order)
    tensor_value = sqrt(order)
    return frobenius, fourth_trace, tensor_value


def cross_ratio_log(residual_logs: Iterable[float]) -> float:
    """Alternating four-residual sum controlling a color cross ratio."""

    values = tuple(residual_logs)
    if len(values) != 4:
        raise ValueError("four residual logs are required")
    return values[0] + values[3] - values[1] - values[2]
