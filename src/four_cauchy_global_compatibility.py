"""Exact fixtures for the four-Cauchy exterior-source calculation.

The module checks only finite algebra used by the R185 audit:

* the fourth-root filter and the one pole--Lerch cancellation on each side;
* the projection--dilation leakage and commutator cocycle;
* the first Toeplitz contact/extension compatibility polynomial; and
* a rational charged-contact countermodel to propagation from positive
  semidefinite Toeplitz old-contact algebra alone.

It does not discretize Suzuki's split finite-part old operator, impose its
homogeneous equation, construct a form-domain state adapter, prove kernel-null
charge, complete the global compatibility calculation, construct ``T_src``,
prove a zero-free strip, or prove RH.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import json
from typing import Iterable, Mapping


Q = Fraction
GaussianQ = tuple[Q, Q]
Matrix = tuple[tuple[Q, ...], ...]
Vector = tuple[Q, ...]


def _gadd(left: GaussianQ, right: GaussianQ) -> GaussianQ:
    return left[0] + right[0], left[1] + right[1]


def _gmul(left: GaussianQ, right: GaussianQ) -> GaussianQ:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def _gpow(value: GaussianQ, exponent: int) -> GaussianQ:
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    answer: GaussianQ = (Q(1), Q(0))
    base = value
    power = exponent
    while power:
        if power & 1:
            answer = _gmul(answer, base)
        base = _gmul(base, base)
        power //= 2
    return answer


@dataclass(frozen=True)
class FourthRootFilterLedger:
    exponent: int
    power_sum_real: Q
    power_sum_imaginary: Q
    expected_real: Q


def fourth_root_filter(exponent: int) -> FourthRootFilterLedger:
    """Return ``sum_(zeta^4=1) zeta^exponent`` over Gaussian rationals."""

    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    roots: tuple[GaussianQ, ...] = (
        (Q(1), Q(0)),
        (Q(0), Q(1)),
        (Q(-1), Q(0)),
        (Q(0), Q(-1)),
    )
    total: GaussianQ = (Q(0), Q(0))
    for root in roots:
        total = _gadd(total, _gpow(root, exponent))
    return FourthRootFilterLedger(
        exponent=exponent,
        power_sum_real=total[0],
        power_sum_imaginary=total[1],
        expected_real=Q(4) if exponent % 4 == 0 else Q(0),
    )


@dataclass(frozen=True)
class ExteriorMomentLedger:
    side: str
    multiplicative_coordinate: Q
    surviving_pole: Q
    canceled_pole: Q
    canceled_lerch_mode: Q
    cancellation_defect: Q
    higher_lerch_modes: Q
    prime_trace: Q
    exterior_total: Q


def right_exterior_moment_filter(
    coordinate: Q | int,
    moments: Mapping[int, Q | int],
    prime_trace: Q | int = 0,
) -> ExteriorMomentLedger:
    """Audit the right pole--Lerch filter in additive-moment notation.

    ``moments[s]`` denotes ``M_s = integral exp(s*y/2) n(y) dy`` and
    ``coordinate`` denotes ``X=exp(x/2)``.  The exact right exterior source is

    ``X*M_-1 - sum_(j>=1) M_(4j+1)/X^(4j+1) - prime_trace``.

    Only the finitely supplied higher moments are evaluated here.
    The caller is responsible for checking the analytic side condition
    ``X > beta``; this routine replays only the resulting algebra.
    """

    x = Q(coordinate)
    if x <= 0:
        raise ValueError("coordinate must be positive")
    if any(not isinstance(key, int) or isinstance(key, bool) for key in moments):
        raise ValueError("moment exponents must be integers")
    normalized = {key: Q(value) for key, value in moments.items()}
    m_minus = normalized.get(-1, Q(0))
    m_plus = normalized.get(1, Q(0))
    higher = -sum(
        (
            value / x**exponent
            for exponent, value in normalized.items()
            if exponent >= 5 and (exponent - 1) % 4 == 0
        ),
        Q(0),
    )
    canceled_pole = m_plus / x
    canceled_lerch = -m_plus / x
    trace = Q(prime_trace)
    surviving = x * m_minus
    return ExteriorMomentLedger(
        side="right",
        multiplicative_coordinate=x,
        surviving_pole=surviving,
        canceled_pole=canceled_pole,
        canceled_lerch_mode=canceled_lerch,
        cancellation_defect=canceled_pole + canceled_lerch,
        higher_lerch_modes=higher,
        prime_trace=trace,
        exterior_total=surviving + higher - trace,
    )


def left_exterior_moment_filter(
    coordinate: Q | int,
    moments: Mapping[int, Q | int],
    prime_trace: Q | int = 0,
) -> ExteriorMomentLedger:
    """Audit the reflected left pole--Lerch filter.

    The caller is responsible for checking ``0 < X < alpha``; this routine
    replays only the resulting algebra.
    """

    x = Q(coordinate)
    if x <= 0:
        raise ValueError("coordinate must be positive")
    if any(not isinstance(key, int) or isinstance(key, bool) for key in moments):
        raise ValueError("moment exponents must be integers")
    normalized = {key: Q(value) for key, value in moments.items()}
    m_minus = normalized.get(-1, Q(0))
    m_plus = normalized.get(1, Q(0))
    higher = -sum(
        (
            x ** (-exponent) * value
            for exponent, value in normalized.items()
            if exponent <= -5 and ((-exponent) - 1) % 4 == 0
        ),
        Q(0),
    )
    canceled_pole = x * m_minus
    canceled_lerch = -x * m_minus
    trace = Q(prime_trace)
    surviving = m_plus / x
    return ExteriorMomentLedger(
        side="left",
        multiplicative_coordinate=x,
        surviving_pole=surviving,
        canceled_pole=canceled_pole,
        canceled_lerch_mode=canceled_lerch,
        cancellation_defect=canceled_pole + canceled_lerch,
        higher_lerch_modes=higher,
        prime_trace=trace,
        exterior_total=surviving + higher - trace,
    )


def root_filtered_right_series(
    coordinate: Q | int, multiplicative_moments: Mapping[int, Q | int]
) -> Q:
    """Finite exact replay of the right four-root Cauchy moment filter.

    If ``mu[k]=integral f(Y)Y^k dY``, the filtered Cauchy contribution is
    ``-1/2 sum_k mu[k] X^(-k-1) sum_(zeta^4=1) zeta^k``.
    Analytic use additionally requires ``X`` to lie beyond the support so the
    geometric expansion converges.
    """

    x = Q(coordinate)
    if x <= 0:
        raise ValueError("coordinate must be positive")
    if any(
        not isinstance(exponent, int) or isinstance(exponent, bool)
        for exponent in multiplicative_moments
    ):
        raise ValueError("moment exponents must be integers")
    answer = Q(0)
    for exponent, raw_moment in multiplicative_moments.items():
        ledger = fourth_root_filter(exponent)
        if ledger.power_sum_imaginary:
            raise AssertionError("fourth-root power sum must be real")
        answer -= Q(1, 2) * Q(raw_moment) * ledger.power_sum_real / x ** (exponent + 1)
    return answer


def _shape(matrix: Matrix) -> tuple[int, int]:
    if not matrix:
        return 0, 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged matrix")
    return len(matrix), width


def _matmul(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_columns = _shape(left)
    right_rows, right_columns = _shape(right)
    if left_columns != right_rows:
        raise ValueError("incompatible matrix dimensions")
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(left_columns)), Q(0))
            for j in range(right_columns)
        )
        for i in range(left_rows)
    )


def _matadd(left: Matrix, right: Matrix) -> Matrix:
    if _shape(left) != _shape(right):
        raise ValueError("incompatible matrix dimensions")
    return tuple(
        tuple(a + b for a, b in zip(lrow, rrow, strict=True))
        for lrow, rrow in zip(left, right, strict=True)
    )


def _matsub(left: Matrix, right: Matrix) -> Matrix:
    if _shape(left) != _shape(right):
        raise ValueError("incompatible matrix dimensions")
    return tuple(
        tuple(a - b for a, b in zip(lrow, rrow, strict=True))
        for lrow, rrow in zip(left, right, strict=True)
    )


def _matscale(scalar: Q, matrix: Matrix) -> Matrix:
    return tuple(tuple(scalar * value for value in row) for row in matrix)


def _identity(size: int) -> Matrix:
    return tuple(
        tuple(Q(1) if i == j else Q(0) for j in range(size))
        for i in range(size)
    )


def _matvec(matrix: Matrix, vector: Vector) -> Vector:
    if _shape(matrix)[1] != len(vector):
        raise ValueError("incompatible matrix/vector dimensions")
    return tuple(
        sum((entry * value for entry, value in zip(row, vector, strict=True)), Q(0))
        for row in matrix
    )


def determinant(matrix: Matrix) -> Q:
    """Exact determinant by fraction-preserving elimination."""

    rows, columns = _shape(matrix)
    if rows != columns:
        raise ValueError("determinant requires a square matrix")
    work = [list(row) for row in matrix]
    answer = Q(1)
    for column in range(rows):
        pivot = next((row for row in range(column, rows) if work[row][column]), None)
        if pivot is None:
            return Q(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        pivot_value = work[column][column]
        answer *= pivot_value
        for entry in range(column, rows):
            work[column][entry] /= pivot_value
        for row in range(column + 1, rows):
            multiplier = work[row][column]
            for entry in range(column, rows):
                work[row][entry] -= multiplier * work[column][entry]
    return answer


@dataclass(frozen=True)
class ProjectionCocycleLedger:
    leakage_left: Matrix
    leakage_via_commutator: Matrix
    leakage_defect: Matrix
    product_commutator_left: Matrix
    product_commutator_right: Matrix
    product_commutator_defect: Matrix


def projection_cocycle(projection: Matrix, first: Matrix, second: Matrix) -> ProjectionCocycleLedger:
    """Replay leakage and ``[DE,P]=D[E,P]+[D,P]E`` exactly."""

    size, width = _shape(projection)
    if size != width or _shape(first) != (size, size) or _shape(second) != (size, size):
        raise ValueError("all matrices must be square with the same size")
    if _matmul(projection, projection) != projection:
        raise ValueError("projection must be idempotent")
    identity = _identity(size)
    complement = _matsub(identity, projection)
    first_projection = _matmul(first, projection)
    projected_first_projection = _matmul(projection, first_projection)
    leakage_left = _matmul(complement, first_projection)
    leakage_via_commutator = _matmul(
        complement, _matsub(first_projection, projected_first_projection)
    )
    product = _matmul(first, second)
    product_commutator_left = _matsub(
        _matmul(product, projection), _matmul(projection, product)
    )
    second_commutator = _matsub(
        _matmul(second, projection), _matmul(projection, second)
    )
    first_commutator = _matsub(
        _matmul(first, projection), _matmul(projection, first)
    )
    product_commutator_right = _matadd(
        _matmul(first, second_commutator), _matmul(first_commutator, second)
    )
    return ProjectionCocycleLedger(
        leakage_left=leakage_left,
        leakage_via_commutator=leakage_via_commutator,
        leakage_defect=_matsub(leakage_left, leakage_via_commutator),
        product_commutator_left=product_commutator_left,
        product_commutator_right=product_commutator_right,
        product_commutator_defect=_matsub(
            product_commutator_left, product_commutator_right
        ),
    )


@dataclass(frozen=True)
class ToeplitzContactLedger:
    a: Q
    c: Q
    d: Q
    determinant: Q
    determinant_factorization: Q
    even_contact_residual: Vector
    odd_contact_residual: Vector
    even_factor_defect: Matrix
    r2: Q
    r3: Q


def toeplitz_contact(a: Q | int, c: Q | int, d: Q | int) -> ToeplitzContactLedger:
    """Audit the first global Toeplitz contact/extension compatibility."""

    qa, qc, qd = Q(a), Q(c), Q(d)
    old: Matrix = (
        (Q(1), qa, qc),
        (qa, Q(1), qa),
        (qc, qa, Q(1)),
    )
    exterior: Matrix = ((qa, qc, qd), (qd, qc, qa))
    even_null: Vector = (Q(1), -2 * qa, Q(1))
    odd_null: Vector = (Q(1), Q(0), Q(-1))
    even_factor: Matrix = ((2 * qa, Q(-1), Q(0)), (Q(0), Q(-1), 2 * qa))
    r2 = qc + Q(1) - 2 * qa * qa
    r3 = qd + qa - 2 * qa * qc
    return ToeplitzContactLedger(
        a=qa,
        c=qc,
        d=qd,
        determinant=determinant(old),
        determinant_factorization=(qc - Q(1)) * (2 * qa * qa - qc - Q(1)),
        even_contact_residual=_matvec(exterior, even_null),
        odd_contact_residual=_matvec(exterior, odd_null),
        even_factor_defect=_matsub(exterior, _matmul(even_factor, old)),
        r2=r2,
        r3=r3,
    )


@dataclass(frozen=True)
class ChargedContactCountermodel:
    old_matrix: Matrix
    exterior_matrix: Matrix
    null_vector: Vector
    old_residual: Vector
    exterior_charge: Vector
    idempotent_scaling_defect: Matrix
    continuous_source_samples: tuple[Q, Q, Q]
    completion_adjustments: tuple[Q, Q, Q]


def charged_contact_countermodel() -> ChargedContactCountermodel:
    """A rational Toeplitz-algebra contact with nonzero exterior charge.

    The baseline values are the signed continuous source samples
    ``-(q + q^-1 - q^3/(q^4-1))`` at ``q=2,4,8``.  The completion adjustments
    are independently chosen symbolic numbers.  This model shows only that
    positive-semidefinite Toeplitz old-contact algebra does not force exterior
    null charge; it is not the actual zeta operator or the full source grammar.
    """

    a, c = Q(1, 2), Q(-1, 2)
    h2, h4, h8 = Q(-59, 30), Q(-4079, 1020), Q(-262079, 32760)
    adjustments = Q(37, 15), Q(3569, 1020), Q(0)
    d = h8 + adjustments[2]
    old: Matrix = (
        (Q(1), a, c),
        (a, Q(1), a),
        (c, a, Q(1)),
    )
    exterior: Matrix = ((a, c, d), (d, c, a))
    null: Vector = (Q(1), Q(-1), Q(1))
    return ChargedContactCountermodel(
        old_matrix=old,
        exterior_matrix=exterior,
        null_vector=null,
        old_residual=_matvec(old, null),
        exterior_charge=_matvec(exterior, null),
        idempotent_scaling_defect=_matsub(_matmul(old, old), _matscale(Q(3, 2), old)),
        continuous_source_samples=(h2, h4, h8),
        completion_adjustments=adjustments,
    )


def chebyshev_propagation(first_lag: Q | int, order: int) -> tuple[Q, ...]:
    """Return the recurrence ``b_(j+1)=2*b1*b_j-b_(j-1)``."""

    if order < 0:
        raise ValueError("order must be nonnegative")
    a = Q(first_lag)
    if order == 0:
        return (Q(1),)
    values = [Q(1), a]
    while len(values) <= order:
        values.append(2 * a * values[-1] - values[-2])
    return tuple(values)


def four_cauchy_geometric_sample(index: int) -> Q:
    """Return ``q^3/(q^4-1)`` at ``q=2^index`` exactly."""

    if index < 1:
        raise ValueError("index must be positive")
    q = Q(2) ** index
    return q**3 / (q**4 - 1)


def four_cauchy_hankel_determinant(order: int) -> Q:
    """Finite recurrence falsifier for the geometric four-Cauchy sequence."""

    if order < 1:
        raise ValueError("order must be positive")
    matrix: Matrix = tuple(
        tuple(four_cauchy_geometric_sample(i + j + 1) for j in range(order))
        for i in range(order)
    )
    return determinant(matrix)


def _json_ready(value: object) -> object:
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, tuple):
        return [_json_ready(item) for item in value]
    if isinstance(value, list):
        return [_json_ready(item) for item in value]
    if isinstance(value, dict):
        return {key: _json_ready(item) for key, item in value.items()}
    return value


def main() -> None:
    report = {
        "schema": "zeta23-four-cauchy-global-compatibility-exact-v1",
        "root_filters": [asdict(fourth_root_filter(index)) for index in range(8)],
        "right_filter": asdict(
            right_exterior_moment_filter(
                Q(3), {-1: Q(2), 1: Q(5), 5: Q(7), 9: Q(-4)}, Q(11)
            )
        ),
        "left_filter": asdict(
            left_exterior_moment_filter(
                Q(1, 3), {-9: Q(4), -5: Q(-7), -1: Q(2), 1: Q(5)}, Q(11)
            )
        ),
        "toeplitz_even_contact": asdict(toeplitz_contact(Q(2, 3), Q(-1, 9), Q(-22, 27))),
        "charged_countermodel": asdict(charged_contact_countermodel()),
        "four_cauchy_hankel_determinants": {
            str(order): four_cauchy_hankel_determinant(order) for order in range(1, 5)
        },
        "nonclaim": "FINITE_EXACT_ALGEBRA_ONLY_NOT_ANALYTIC_ZETA_KNC_TSRC_STRIP_OR_RH",
    }
    print(json.dumps(_json_ready(report), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
