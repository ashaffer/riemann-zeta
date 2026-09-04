"""Exact finite fixtures for the constructive completed-source search.

The routines in this module replay three algebraic facts used by the human
audit:

* a finite Neumann/source word has an exact remainder, and that remainder is
  the full charge at the contact spectral value ``K=-1``;
* postcomposition by an annihilator does not imply that an exterior charge
  vanishes; and
* the Cauchy kernel, which is the leading derivative of a logarithmic Hankel
  edge, has arbitrarily large finite rank; and
* Suzuki's Lerch derivative is the sum of four root-of-unity Cauchy channels.

All arithmetic is rational.  These fixtures do not model the analytic zeta
operator and make no assertion about a zero-free strip or RH.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import json
from typing import Iterable


Q = Fraction
Matrix = tuple[tuple[Q, ...], ...]
Vector = tuple[Q, ...]


def _polynomial_value(coefficients: Iterable[Q | int], value: Q | int) -> Q:
    """Evaluate coefficients in increasing order by Horner's rule."""

    x = Q(value)
    answer = Q(0)
    for coefficient in reversed(tuple(Q(c) for c in coefficients)):
        answer = answer * x + coefficient
    return answer


@dataclass(frozen=True)
class FiniteSourceWordLedger:
    depth: int
    old_residual_k: Q
    old_operator_a: Q
    charge_gamma: Q
    neumann_sum: Q
    factor_term: Q
    remainder_term: Q
    reconstruction_defect: Q


def finite_source_word(
    depth: int, old_residual_k: Q | int, charge_gamma: Q | int = 1
) -> FiniteSourceWordLedger:
    """Replay ``Gamma = T_m A + Gamma (-K)^m`` in one scalar mode.

    Here ``A=1+K`` and

    ``T_m=Gamma * sum_{j=0}^{m-1} (-K)^j``.

    The scalar replay is sufficient to expose the contact obstruction: at
    ``K=-1``, every positive depth has remainder ``Gamma``.
    """

    if depth < 1:
        raise ValueError("depth must be positive")
    k = Q(old_residual_k)
    gamma = Q(charge_gamma)
    neumann_sum = sum(((-k) ** j for j in range(depth)), Q(0))
    a = Q(1) + k
    factor_term = gamma * neumann_sum * a
    remainder_term = gamma * (-k) ** depth
    return FiniteSourceWordLedger(
        depth=depth,
        old_residual_k=k,
        old_operator_a=a,
        charge_gamma=gamma,
        neumann_sum=neumann_sum,
        factor_term=factor_term,
        remainder_term=remainder_term,
        reconstruction_defect=gamma - factor_term - remainder_term,
    )


@dataclass(frozen=True)
class PolynomialContactLedger:
    coefficients: tuple[Q, ...]
    polynomial_at_contact: Q
    residual_multiplier_at_contact: Q
    charge_gamma: Q
    residual_charge: Q


def polynomial_contact_residual(
    coefficients: Iterable[Q | int], charge_gamma: Q | int = 1
) -> PolynomialContactLedger:
    """Audit a regular polynomial candidate ``T=Gamma p(K)`` at ``K=-1``."""

    coeffs = tuple(Q(c) for c in coefficients)
    p_at_contact = _polynomial_value(coeffs, Q(-1))
    residual_multiplier = Q(1) - (Q(1) + Q(-1)) * p_at_contact
    gamma = Q(charge_gamma)
    return PolynomialContactLedger(
        coefficients=coeffs,
        polynomial_at_contact=p_at_contact,
        residual_multiplier_at_contact=residual_multiplier,
        charge_gamma=gamma,
        residual_charge=gamma * residual_multiplier,
    )


def _matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    columns = tuple(zip(*right, strict=True))
    return tuple(
        tuple(sum((a * b for a, b in zip(row, column, strict=True)), Q(0)) for column in columns)
        for row in left
    )


def _matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((a * b for a, b in zip(row, vector, strict=True)), Q(0))
        for row in matrix
    )


@dataclass(frozen=True)
class AnnihilatorCountermodelLedger:
    annihilator_times_source: Matrix
    old_compression: Matrix
    charged_old_vector: Vector
    exterior_charge: Vector
    exterior_charge_norm_squared: Q


def annihilator_countermodel() -> AnnihilatorCountermodelLedger:
    """Return a typed 3-by-3 countermodel to annihilator propagation.

    On ``Q^3`` let

    ``S(x,y,z)=(y,x+z,y)``, let ``P`` project onto the first coordinate, and
    let ``M`` project onto ``span((1,0,-1))``.  Then ``M S=0`` and
    ``P S P=0``, but the old vector ``e1`` has exterior charge ``e2``.
    """

    source: Matrix = (
        (Q(0), Q(1), Q(0)),
        (Q(1), Q(0), Q(1)),
        (Q(0), Q(1), Q(0)),
    )
    old_projection: Matrix = (
        (Q(1), Q(0), Q(0)),
        (Q(0), Q(0), Q(0)),
        (Q(0), Q(0), Q(0)),
    )
    exterior_projection: Matrix = (
        (Q(0), Q(0), Q(0)),
        (Q(0), Q(1), Q(0)),
        (Q(0), Q(0), Q(1)),
    )
    annihilator: Matrix = (
        (Q(1, 2), Q(0), Q(-1, 2)),
        (Q(0), Q(0), Q(0)),
        (Q(-1, 2), Q(0), Q(1, 2)),
    )
    old_vector: Vector = (Q(1), Q(0), Q(0))
    charge = _matvec(_matmul(_matmul(exterior_projection, source), old_projection), old_vector)
    return AnnihilatorCountermodelLedger(
        annihilator_times_source=_matmul(annihilator, source),
        old_compression=_matmul(_matmul(old_projection, source), old_projection),
        charged_old_vector=old_vector,
        exterior_charge=charge,
        exterior_charge_norm_squared=sum((entry * entry for entry in charge), Q(0)),
    )


def determinant(matrix: Matrix) -> Q:
    """Exact determinant by fraction-preserving Gaussian elimination."""

    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    work = [list(row) for row in matrix]
    answer = Q(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return Q(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        pivot_value = work[column][column]
        answer *= pivot_value
        for entry in range(column, size):
            work[column][entry] /= pivot_value
        for row in range(column + 1, size):
            scale = work[row][column]
            if scale:
                for entry in range(column, size):
                    work[row][entry] -= scale * work[column][entry]
    return answer


@dataclass(frozen=True)
class CauchyHankelLedger:
    order: int
    determinant_by_elimination: Q
    determinant_by_product: Q
    agreement_defect: Q


def cauchy_hankel_rank_witness(order: int) -> CauchyHankelLedger:
    """Give an exact full-rank Cauchy/Hankel matrix of prescribed order.

    The entries are ``1/(x_i+y_j)`` with ``x_i=i+1`` and
    ``y_j=j+order+1``.  Such matrices occur as the scaled leading derivative
    of a logarithmic edge kernel.  The fixture verifies the Cauchy
    determinant formula exactly for any requested finite order.
    """

    if order < 1:
        raise ValueError("order must be positive")
    xs = tuple(Q(index + 1) for index in range(order))
    ys = tuple(Q(index + order + 1) for index in range(order))
    matrix: Matrix = tuple(tuple(Q(1) / (x + y) for y in ys) for x in xs)
    numerator = Q(1)
    for i in range(order):
        for j in range(i + 1, order):
            numerator *= (xs[j] - xs[i]) * (ys[j] - ys[i])
    denominator = Q(1)
    for x in xs:
        for y in ys:
            denominator *= x + y
    product = numerator / denominator
    eliminated = determinant(matrix)
    return CauchyHankelLedger(
        order=order,
        determinant_by_elimination=eliminated,
        determinant_by_product=product,
        agreement_defect=eliminated - product,
    )


@dataclass(frozen=True)
class FourCauchyLedger:
    q: Q
    real_root_channels: Q
    imaginary_root_channels: Q
    four_channel_sum: Q
    rational_closed_form: Q
    agreement_defect: Q
    lerch_derivative: Q


def four_cauchy_lerch_derivative(q: Q | int) -> FourCauchyLedger:
    """Replay the four-Cauchy derivative identity at a rational ``q``.

    If ``q=exp(t/2)>1`` and

    ``L(t)=exp(-t/2) Phi(exp(-2t),1,1/4)``, then

    ``L'(t)=-1/2 sum_(zeta^4=1) 1/(q-zeta)``.

    The two imaginary-root channels are paired before evaluation, so every
    quantity remains rational:

    ``1/(q-i)+1/(q+i)=2q/(q^2+1)``.

    This routine checks only the resulting rational identity.  It does not
    formalize the Lerch series or analytic differentiation.
    """

    value = Q(q)
    if value in (Q(-1), Q(1)):
        raise ValueError("q must avoid the real fourth roots of unity")
    real_channels = Q(1) / (value - 1) + Q(1) / (value + 1)
    imaginary_channels = 2 * value / (value * value + 1)
    channel_sum = real_channels + imaginary_channels
    closed_form = 4 * value**3 / (value**4 - 1)
    return FourCauchyLedger(
        q=value,
        real_root_channels=real_channels,
        imaginary_root_channels=imaginary_channels,
        four_channel_sum=channel_sum,
        rational_closed_form=closed_form,
        agreement_defect=channel_sum - closed_form,
        lerch_derivative=-channel_sum / 2,
    )


def regular_parametrix_residual(parametrix_value: Q | int, symbol_value: Q | int) -> Q:
    """Return ``1-LM`` in one spectral mode."""

    return Q(1) - Q(parametrix_value) * Q(symbol_value)


def causal_ramp_boundary_correction(
    profile_multiplier: Q | int, core_multiplier: Q | int
) -> tuple[Q, Q, Q]:
    """Return ramp, completed-source, and collar multipliers.

    In the standard causal distribution convention the differentiated ramp
    has multiplier ``V*core``, whereas the completed compact source has
    multiplier ``V*(1+core)``.  Therefore ``ramp=source-V``.  This exact
    scalar replay prevents the fixed initial collar from being dropped.
    """

    profile = Q(profile_multiplier)
    core = Q(core_multiplier)
    ramp = profile * core
    source = profile * (Q(1) + core)
    return ramp, source, source - ramp


def _jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    return value


def audit_ledger() -> dict[str, object]:
    """Return a compact exact replay ledger."""

    return {
        "finite_source_contact": [
            asdict(finite_source_word(depth, -1, 3)) for depth in range(1, 7)
        ],
        "polynomial_contact": asdict(polynomial_contact_residual((2, -3, 5), 3)),
        "annihilator_countermodel": asdict(annihilator_countermodel()),
        "cauchy_hankel": [
            asdict(cauchy_hankel_rank_witness(order)) for order in range(1, 7)
        ],
        "four_cauchy_lerch": [
            asdict(four_cauchy_lerch_derivative(q)) for q in (2, 3, 5, 8)
        ],
        "causal_ramp_boundary": tuple(
            str(value) for value in causal_ramp_boundary_correction(3, 7)
        ),
        "regular_parametrix_at_divisor_zero": str(regular_parametrix_residual(17, 0)),
    }


def main() -> None:
    print(json.dumps(_jsonable(audit_ledger()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
