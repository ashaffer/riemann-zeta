"""Exact finite fixtures for the R186 split-Carleman closeout.

This module replays only rational/Gaussian-rational algebra: the fourth-root
partial fractions, cancellation of the finite-part counterterm, and a
synthetic PSD split-Cauchy/dilation contact with nonzero exterior charge.
It does not formalize the analytic form-core extension, Carleman's inequality,
the completed-zeta operator, KNC, a zero-free strip, or RH.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


Q = Fraction
GQ = tuple[Q, Q]
Matrix = tuple[tuple[Q, ...], ...]
Vector = tuple[Q, ...]


def _gadd(a: GQ, b: GQ) -> GQ:
    return a[0] + b[0], a[1] + b[1]


def _gmul(a: GQ, b: GQ) -> GQ:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def _ginv(a: GQ) -> GQ:
    norm = a[0] * a[0] + a[1] * a[1]
    if norm == 0:
        raise ZeroDivisionError("Gaussian-rational division by zero")
    return a[0] / norm, -a[1] / norm


def _gdiv(a: GQ, b: GQ) -> GQ:
    return _gmul(a, _ginv(b))


ROOTS: tuple[GQ, ...] = (
    (Q(1), Q(0)),
    (Q(-1), Q(0)),
    (Q(0), Q(1)),
    (Q(0), Q(-1)),
)


@dataclass(frozen=True)
class RootIdentityLedger:
    left_root_sum: GQ
    left_collapsed: GQ
    right_root_sum: GQ
    right_collapsed: GQ


def root_partial_fractions(x_raw: Q | int, y_raw: Q | int) -> RootIdentityLedger:
    """Evaluate both identities in (R186.1.4) exactly."""

    x, y = Q(x_raw), Q(y_raw)
    if x == y or x == -y or x == 0 or y == 0:
        raise ValueError("x and y must be nonzero and x^4 != y^4")
    xg, yg = (x, Q(0)), (y, Q(0))
    left: GQ = (Q(0), Q(0))
    right: GQ = (Q(0), Q(0))
    for root in ROOTS:
        left_den = _gadd(xg, _gmul((-root[0], -root[1]), yg))
        left = _gadd(left, _gdiv((Q(1, 2), Q(0)), left_den))
        root_inv = _ginv(root)
        right_den = _gadd(yg, _gmul((-root[0], -root[1]), xg))
        right = _gadd(right, _gdiv(_gmul((Q(1, 2), Q(0)), root_inv), right_den))
    left_closed = (2 * x**3 / (x**4 - y**4), Q(0))
    right_closed = (2 * x * y**2 / (y**4 - x**4), Q(0))
    return RootIdentityLedger(left, left_closed, right, right_closed)


@dataclass(frozen=True)
class CountertermLedger:
    left_constant_integral: Q
    right_constant_integral: Q
    subtraction: Q
    surviving_endpoint_term: Q
    defect: Q


def finite_part_counterterm(
    ell_epsilon: Q | int, ell_left: Q | int, ell_right: Q | int
) -> CountertermLedger:
    """Replay the exact constant-piece cancellation in additive variables.

    By ``ell'=-2K``, either truncated constant integral equals one half of
    ``ell(epsilon)-ell(endpoint distance)``.
    """

    ee, el, er = Q(ell_epsilon), Q(ell_left), Q(ell_right)
    left = (ee - el) / 2
    right = (ee - er) / 2
    subtraction = -ee
    endpoint = -(el + er) / 2
    return CountertermLedger(
        left, right, subtraction, endpoint, left + right + subtraction - endpoint
    )


def _matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((entry * value for entry, value in zip(row, vector, strict=True)), Q(0))
        for row in matrix
    )


def _det2(matrix: Matrix, i: int, j: int) -> Q:
    return matrix[i][i] * matrix[j][j] - matrix[i][j] * matrix[j][i]


@dataclass(frozen=True)
class SyntheticContactLedger:
    ratio: Q
    dilation_weight: Q
    local_completion: Q
    split_matrix: Matrix
    pole_matrix: Matrix
    dilation_matrix: Matrix
    old_matrix: Matrix
    null_vector: Vector
    old_residual: Vector
    principal_minors_1: tuple[Q, ...]
    principal_minors_2: tuple[Q, ...]
    determinant: Q
    exterior_pole: Q
    exterior_cauchy: Q
    exterior_prime: Q
    exterior_total: Q
    left_exterior_total: Q


def reciprocal_synthetic_contact(
    ratio_raw: Q | int = 2, dilation_weight_raw: Q | int = Q(3, 7)
) -> SyntheticContactLedger:
    """Exact reciprocal three-node hostile model.

    Nodes are ``(r^-1,1,r)`` inside ``J=(1/3,3)`` for the default ``r=2``.
    The model is a collocation grammar witness, not a continuum discretization
    theorem and not an actual-zeta counterexample.
    """

    r, q = Q(ratio_raw), Q(dilation_weight_raw)
    if r <= 1 or q < 0:
        raise ValueError("ratio must exceed one and dilation weight be nonnegative")
    adjacent = 2 * r**4 / (r**4 - 1)
    corner = 2 * r**7 / (r**8 - 1)
    split: Matrix = (
        (Q(0), adjacent, corner),
        (adjacent, Q(0), adjacent),
        (corner, adjacent, Q(0)),
    )
    pole: Matrix = (
        (4 * r, 2 * (1 + r**2), 2 * (r**-1 + r**3)),
        (2 * (1 + r**2), 4 * r, 2 * (1 + r**2)),
        (2 * (r**-1 + r**3), 2 * (1 + r**2), 4 * r),
    )
    dilation: Matrix = (
        (Q(0), Q(1), Q(0)),
        (Q(1), Q(0), Q(1)),
        (Q(0), Q(1), Q(0)),
    )
    completion = 2 * (r**2 - 1) ** 2 / r - corner
    old: Matrix = tuple(
        tuple(
            pole[i][j]
            + (completion if i == j else Q(0))
            - q * dilation[i][j]
            - split[i][j]
            for j in range(3)
        )
        for i in range(3)
    )
    null = (Q(1), Q(0), Q(-1))
    residual = _matvec(old, null)
    minors1 = tuple(old[i][i] for i in range(3))
    minors2 = (_det2(old, 0, 1), _det2(old, 0, 2), _det2(old, 1, 2))
    # First and third rows coincide, so the determinant is identically zero.
    determinant = Q(0)
    moment = 2 * (r**2 - 1)
    exterior_pole = moment * (r**2 - r**-2)
    exterior_cauchy = 2 * r**4 / (r**4 - 1) - 2 * r**10 / (r**12 - 1)
    exterior_prime = q
    exterior_total = exterior_pole + exterior_cauchy + exterior_prime
    return SyntheticContactLedger(
        r,
        q,
        completion,
        split,
        pole,
        dilation,
        old,
        null,
        residual,
        minors1,
        minors2,
        determinant,
        exterior_pole,
        exterior_cauchy,
        exterior_prime,
        exterior_total,
        -exterior_total,
    )


@dataclass(frozen=True)
class ArcsineLedger:
    plemelj_average: Q
    exterior_imaginary_coefficient: Q
    exterior_modulus_squared: Q


def arcsine_falsifier() -> ArcsineLedger:
    """Exact algebraic data for ``C(2)=i/(2 sqrt(3))``."""

    return ArcsineLedger(Q(0), Q(1, 2), Q(1, 12))
