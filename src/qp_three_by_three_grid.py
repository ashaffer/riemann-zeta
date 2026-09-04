"""Exact determinant certificate for a completed carry 3-by-3 grid.

This is an algebraic rigidity check.  It does not claim that a large
four-cycle sum contains such a grid, nor does it classify rank-two matrices
of prime powers.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import prod
from typing import Sequence


Matrix3 = tuple[
    tuple[int, int, int],
    tuple[int, int, int],
    tuple[int, int, int],
]


def as_matrix3(matrix: Sequence[Sequence[int]]) -> Matrix3:
    """Validate and freeze a 3-by-3 integer matrix."""

    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("expected a 3-by-3 matrix")
    return tuple(tuple(int(value) for value in row) for row in matrix)  # type: ignore[return-value]


def determinant3(matrix: Sequence[Sequence[int]]) -> int:
    """Return the exact determinant of a 3-by-3 integer matrix."""

    a = as_matrix3(matrix)
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def two_by_two_minors(matrix: Sequence[Sequence[int]]) -> tuple[int, ...]:
    """Return the nine signed 2-by-2 minors in lexicographic order."""

    a = as_matrix3(matrix)
    answer: list[int] = []
    for i0, i1 in ((0, 1), (0, 2), (1, 2)):
        for j0, j1 in ((0, 1), (0, 2), (1, 2)):
            answer.append(
                a[i0][j0] * a[i1][j1] - a[i0][j1] * a[i1][j0]
            )
    return tuple(answer)


def qj_residual_determinant_bound(Q: int, H: int) -> int:
    """The multilinear bound ``|det(Q J + R)| <= 18 Q H^2+6 H^3``."""

    if Q < 0 or H < 0:
        raise ValueError("Q and H must be nonnegative")
    return 18 * Q * H**2 + 6 * H**3


@dataclass(frozen=True)
class GridDeterminantCertificate:
    rows: tuple[int, int, int]
    columns: tuple[int, int, int]
    colors: Matrix3
    products: Matrix3
    residuals: Matrix3
    color_determinant: int
    product_determinant: int
    factored_determinant: int
    residual_determinant: int
    residual_bound: int
    determinant_quantum: int
    within_window: bool
    quantum_separation: bool

    @property
    def hypotheses_force_singular(self) -> bool:
        """Whether the window and quantum inequality invoke the theorem."""

        return self.within_window and self.quantum_separation

    @property
    def conclusion_verified(self) -> bool:
        """Whether the exact data obey the singularity implication."""

        return not self.hypotheses_force_singular or self.color_determinant == 0


def grid_determinant_certificate(
    rows: Sequence[int],
    columns: Sequence[int],
    colors: Sequence[Sequence[int]],
    Q: int,
    H: int,
) -> GridDeterminantCertificate:
    """Build the exact determinant/quantization certificate.

    The product matrix is ``N_ij=8 rows_i columns_j colors_ij`` and the
    residual matrix is ``R=N-QJ``.  If every residual has modulus at most
    ``H`` and the residual determinant bound is below the determinant
    quantum, then the color determinant must vanish.
    """

    if len(rows) != 3 or len(columns) != 3:
        raise ValueError("expected three rows and three columns")
    frozen_rows = tuple(int(value) for value in rows)
    frozen_columns = tuple(int(value) for value in columns)
    if any(value <= 0 for value in frozen_rows + frozen_columns):
        raise ValueError("row and column labels must be positive")
    if Q < 0 or H < 0:
        raise ValueError("Q and H must be nonnegative")
    frozen_colors = as_matrix3(colors)
    products = as_matrix3(
        [
            [
                8 * frozen_rows[i] * frozen_columns[j] * frozen_colors[i][j]
                for j in range(3)
            ]
            for i in range(3)
        ]
    )
    residuals = as_matrix3(
        [[products[i][j] - Q for j in range(3)] for i in range(3)]
    )
    color_det = determinant3(frozen_colors)
    product_det = determinant3(products)
    factored_det = 8**3 * prod(frozen_rows) * prod(frozen_columns) * color_det
    residual_det = determinant3(
        [[Q + residuals[i][j] for j in range(3)] for i in range(3)]
    )
    bound = qj_residual_determinant_bound(Q, H)
    quantum = 8**3 * prod(frozen_rows) * prod(frozen_columns)
    certificate = GridDeterminantCertificate(
        rows=frozen_rows,  # type: ignore[arg-type]
        columns=frozen_columns,  # type: ignore[arg-type]
        colors=frozen_colors,
        products=products,
        residuals=residuals,
        color_determinant=color_det,
        product_determinant=product_det,
        factored_determinant=factored_det,
        residual_determinant=residual_det,
        residual_bound=bound,
        determinant_quantum=quantum,
        within_window=max(abs(value) for row in residuals for value in row) <= H,
        quantum_separation=bound < quantum,
    )
    if not (
        product_det == factored_det
        and product_det == residual_det
        and (not certificate.within_window or abs(residual_det) <= bound)
        and certificate.conclusion_verified
    ):
        raise AssertionError("invalid 3-by-3 determinant certificate")
    return certificate
