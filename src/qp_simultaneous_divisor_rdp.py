"""Exact ledgers for the simultaneous-divisor residual degree-product gate.

Nothing in this module asserts the open residual degree-product theorem.  It
records two elementary divisibility facts and the exact mixed-error identity
which explains why the inequality ``D**2 < q`` does not, by itself, turn the
two-arm problem into an exact rank-one problem.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


Pair = tuple[int, int]
Triple = tuple[int, int, int]


@dataclass(frozen=True)
class EndpointGcdLedger:
    base_determinant: int
    left_gcd: int
    right_gcd: int
    gcd_lcm: int


def endpoint_gcd_ledger(centers: Pair, colors: Pair) -> EndpointGcdLedger:
    """Verify that both endpoint gcds, hence their lcm, divide ``delta``."""

    b, other_b = centers
    c, other_c = colors
    delta = b * c - other_b * other_c
    left = gcd(b, other_b)
    right = gcd(c, other_c)
    lcm = left // gcd(left, right) * right
    if delta % left or delta % right or delta % lcm:
        raise AssertionError("endpoint gcd divisibility failed")
    return EndpointGcdLedger(delta, left, right, lcm)


@dataclass(frozen=True)
class MixedErrorLedger:
    left_errors: Pair
    right_errors: Pair
    base_determinant: int
    cross_determinant: int
    scaled_cross_determinant: int
    expanded_cross_determinant: int


def mixed_error_ledger(
    base_row: int,
    centers: Pair,
    colors: Pair,
    left_row: int,
    left_colors: Pair,
    right_row: int,
    right_centers: Pair,
) -> MixedErrorLedger:
    """Return the exact one-cell error-coordinate expansion.

    Put

    ``alpha=x*d-a*c, beta=x*D-a*C,``
    ``gamma=y*e-a*b, eta=y*E-a*B``.

    Then the verified identity is

    ``x*y*(d*e-D*E)``
    ``=a^2*(b*c-B*C) + a*b*alpha-a*B*beta``
    `` +a*c*gamma-a*C*eta + alpha*gamma-beta*eta``.
    """

    a, x, y = base_row, left_row, right_row
    b, other_b = centers
    c, other_c = colors
    d, other_d = left_colors
    e, other_e = right_centers
    alpha = x * d - a * c
    beta = x * other_d - a * other_c
    gamma = y * e - a * b
    eta = y * other_e - a * other_b
    delta = b * c - other_b * other_c
    cross = d * e - other_d * other_e
    scaled = x * y * cross
    expanded = (
        a * a * delta
        + a * b * alpha
        - a * other_b * beta
        + a * c * gamma
        - a * other_c * eta
        + alpha * gamma
        - beta * eta
    )
    if scaled != expanded:
        raise AssertionError("mixed error ledger failed")
    return MixedErrorLedger(
        left_errors=(alpha, beta),
        right_errors=(gamma, eta),
        base_determinant=delta,
        cross_determinant=cross,
        scaled_cross_determinant=scaled,
        expanded_cross_determinant=expanded,
    )


def rectangular_mixed_remainder(
    left_first: Pair,
    left_second: Pair,
    right_first: Pair,
    right_second: Pair,
) -> int:
    """The exact rectangular remainder after additive terms cancel."""

    alpha_1, beta_1 = left_first
    alpha_2, beta_2 = left_second
    gamma_1, eta_1 = right_first
    gamma_2, eta_2 = right_second
    return (alpha_1 - alpha_2) * (gamma_1 - gamma_2) - (
        beta_1 - beta_2
    ) * (eta_1 - eta_2)


@dataclass(frozen=True)
class PrimeScaleMixedNoGo:
    q: int
    D: int
    triples: tuple[Triple, ...]
    residuals: tuple[int, ...]
    cross_determinants: tuple[tuple[int, int], tuple[int, int]]
    mixed_remainder: int


def prime_scale_mixed_no_go() -> PrimeScaleMixedNoGo:
    """A literal prime-``q`` hard-window fixture with ``D^2<q`` and mix 56.

    The coordinates are ordinary integers, not the actual prime-power shell.
    Thus the fixture refutes only an integrality argument based on the six
    hard windows and ``D^2<q``; it is not an RDP counterexample.
    """

    q, D = 809, 26
    a, b, other_b, c, other_c = 377, 391, 440, 449, 399
    x, d, other_d = 349, 485, 431
    y, e, other_e = 440, 335, 377
    triples = (
        (a, b, c),
        (a, other_b, other_c),
        (x, b, d),
        (x, other_b, other_d),
        (y, e, c),
        (y, other_e, other_c),
    )
    residuals = tuple(8 * u * v * w - q**3 for u, v, w in triples)
    if not D * D < q:
        raise AssertionError("fixture is not below the square-root aperture")
    if any(abs(residual) > q * D for residual in residuals):
        raise AssertionError("fixture left the literal hard window")

    base = mixed_error_ledger(
        a, (b, other_b), (c, other_c), a, (c, other_c), a, (b, other_b)
    )
    cross = mixed_error_ledger(
        a, (b, other_b), (c, other_c), x, (d, other_d), y, (e, other_e)
    )
    mixed = rectangular_mixed_remainder(
        base.left_errors,
        cross.left_errors,
        base.right_errors,
        cross.right_errors,
    )
    first_row = (
        c * b - other_c * other_b,
        c * e - other_c * other_e,
    )
    second_row = (
        d * b - other_d * other_b,
        d * e - other_d * other_e,
    )
    if mixed != 56:
        raise AssertionError("unexpected mixed no-go value")
    return PrimeScaleMixedNoGo(
        q=q,
        D=D,
        triples=triples,
        residuals=residuals,
        cross_determinants=(first_row, second_row),
        mixed_remainder=mixed,
    )
