"""Finite ledgers for the parabolic double-GCD and determinant gates.

The accompanying report proves two analytic statements.

* If ``(m, n) = 1``, the average of ``gcd(m*a, n*b)`` on a rectangle is
  only a divisor loss larger than the area of the rectangle.  This is the
  arithmetic input behind the uniform ``G*sqrt(R*S)`` line-weight sum.
* The incidence graph ``B*w + A*v = C`` on ``A, B`` in one dyadic interval
  has norm at most ``sqrt(U) C^o(1)`` after content decomposition.  A star
  shows that the square root cannot be removed without two-sided
  primitivity.

This module replays the exact finite identities and exponent arithmetic; it
does not pretend to certify an asymptotic ``q^o(1)`` divisor bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


def divisors(value: int) -> tuple[int, ...]:
    """Return the positive divisors of ``value`` in increasing order."""

    if value < 1:
        raise ValueError("value must be positive")
    low: list[int] = []
    high: list[int] = []
    for candidate in range(1, isqrt(value) + 1):
        if value % candidate:
            continue
        low.append(candidate)
        partner = value // candidate
        if partner != candidate:
            high.append(partner)
    return tuple(low + high[::-1])


def euler_phi(value: int) -> int:
    """Euler's totient, by trial division (sufficient for finite ledgers)."""

    if value < 1:
        raise ValueError("value must be positive")
    result = value
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            result -= result // prime
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        result -= result // remaining
    return result


def divisor_count(value: int) -> int:
    """The ordinary divisor function ``tau(value)``."""

    return len(divisors(value))


def gcd_cross_majorant(m: int, n: int, alpha: int, beta: int) -> tuple[int, int]:
    """Return the two sides of the coprime cross-GCD inequality.

    For ``gcd(m,n)=1`` the proved prime-by-prime inequality is

    ``gcd(m*alpha,n*beta) <= gcd(m,beta) gcd(n,alpha) gcd(alpha,beta)``.
    """

    if min(m, n, alpha, beta) < 1:
        raise ValueError("all inputs must be positive")
    if gcd(m, n) != 1:
        raise ValueError("m and n must be coprime")
    left = gcd(m * alpha, n * beta)
    right = gcd(m, beta) * gcd(n, alpha) * gcd(alpha, beta)
    return left, right


def rectangular_gcd_sum(m: int, n: int, x: int, y: int) -> int:
    """Compute ``sum_{a<=x,b<=y} gcd(m*a,n*b)`` exactly."""

    if min(m, n, x, y) < 1:
        raise ValueError("all inputs must be positive")
    if gcd(m, n) != 1:
        raise ValueError("m and n must be coprime")
    return sum(gcd(m * alpha, n * beta) for alpha in range(1, x + 1) for beta in range(1, y + 1))


def rectangular_gcd_divisor_bound(m: int, n: int, x: int, y: int) -> Fraction:
    """Return the explicit divisor-expansion upper bound for the GCD sum.

    The proof uses

    ``sum_{j<=L} gcd(v,j) <= L*tau(v)``

    after expanding ``gcd(alpha,beta)`` with Euler totients.  The returned
    rational number is

    ``x*y*tau(m)*tau(n) * sum_{d<=min(x,y)} phi(d) gcd(m*n,d)/d^2``.
    """

    if min(m, n, x, y) < 1:
        raise ValueError("all inputs must be positive")
    if gcd(m, n) != 1:
        raise ValueError("m and n must be coprime")
    local = sum(
        (Fraction(euler_phi(d) * gcd(m * n, d), d * d) for d in range(1, min(x, y) + 1)),
        Fraction(0),
    )
    return x * y * divisor_count(m) * divisor_count(n) * local


def normalized_line_weight_squared(eta: int, theta: int, alpha: int, beta: int) -> Fraction:
    """Return the square of ``1/sqrt(|A*B|)`` for one carrier line.

    If ``g=gcd(eta*alpha,theta*beta)``, then

    ``A=eta*alpha/g``, ``B=theta*beta/g`` (up to sign), so the square is
    ``g^2/|eta*theta*alpha*beta|``.
    """

    if eta == 0 or theta == 0 or alpha == 0 or beta == 0:
        raise ValueError("the active line coordinates are nonzero")
    transverse = gcd(abs(eta * alpha), abs(theta * beta))
    return Fraction(transverse * transverse, abs(eta * theta * alpha * beta))


def invert_gap_coordinates(
    *,
    x: int,
    y: int,
    s1: int,
    s2: int,
    residual: int,
    wedge: int,
) -> tuple[Fraction, Fraction]:
    """Invert one color-pair residual and carrier wedge exactly.

    With

    ``residual=x*b1-y*b2`` and ``wedge=s1*b2-s2*b1``, put
    ``d=s1*x-s2*y``.  Then

    ``b1=(s1*residual+y*wedge)/d`` and
    ``b2=(s2*residual+x*wedge)/d``.

    Fractions are returned so that failed integrality is visible.
    """

    determinant = s1 * x - s2 * y
    if determinant == 0:
        raise ValueError("the active gap determinant must be nonzero")
    b1 = Fraction(s1 * residual + y * wedge, determinant)
    b2 = Fraction(s2 * residual + x * wedge, determinant)
    return b1, b2


def paired_residual_ledgers(
    *,
    x: int,
    y: int,
    zeta: int,
    w: int,
    r1: int,
    r2: int,
    s1: int,
    s2: int,
    eta: int,
    theta: int,
    a1: int,
    a2: int,
    b1: int,
    b2: int,
) -> dict[str, int]:
    """Replay the exact two-row and two-column residual couplings.

    Under the four token equations, the returned differences vanish:

    ``r1*e_top-r2*e_bottom-theta*beta`` and
    ``s1*f_left-s2*f_right+eta*alpha``.
    """

    if s1 * x - s2 * y != r2 * eta:
        raise ValueError("the top token equation fails")
    if s1 * zeta - s2 * w != r1 * eta:
        raise ValueError("the bottom token equation fails")
    if r1 * x - r2 * zeta != -s2 * theta:
        raise ValueError("the left token equation fails")
    if r1 * y - r2 * w != -s1 * theta:
        raise ValueError("the right token equation fails")

    e_top = x * b1 - y * b2
    e_bottom = zeta * b1 - w * b2
    beta = s1 * b2 - s2 * b1
    f_left = x * a1 - zeta * a2
    f_right = y * a1 - w * a2
    alpha = r1 * a2 - r2 * a1
    return {
        "e_top": e_top,
        "e_bottom": e_bottom,
        "beta": beta,
        "horizontal_coupling_error": r1 * e_top - r2 * e_bottom - theta * beta,
        "f_left": f_left,
        "f_right": f_right,
        "alpha": alpha,
        "vertical_coupling_error": s1 * f_left - s2 * f_right + eta * alpha,
    }


def tangent_congruence_chain(
    *,
    length: int,
    s1: int,
    y: int,
    residual_start: int,
    residual_step: int,
    wedge_start: int,
    wedge_step: int,
    determinant: int,
) -> tuple[tuple[int, int], ...]:
    """Return a finite affine chain in the one-token congruence.

    Every returned ``(e,beta)`` is checked against
    ``s1*e+y*beta == 0 (mod determinant)``.  This is the exact lattice in
    which a short tangent vector can support all ``length`` points even
    when its ambient box has area below one.
    """

    if length < 1 or determinant == 0:
        raise ValueError("length must be positive and determinant nonzero")
    points = tuple(
        (residual_start + index * residual_step, wedge_start + index * wedge_step)
        for index in range(length)
    )
    if any((s1 * residual + y * wedge) % determinant for residual, wedge in points):
        raise ValueError("the requested affine chain misses the congruence lattice")
    return points


@dataclass(frozen=True)
class DeterminantVertex:
    """One vertex ``(coefficient, longitudinal coordinate)``."""

    coefficient: int
    longitudinal: int

    @property
    def content(self) -> int:
        return gcd(abs(self.coefficient), abs(self.longitudinal))


def determinant_incidence(
    left: DeterminantVertex,
    right: DeterminantVertex,
    level: int,
    *,
    primitive_direction: bool = True,
) -> bool:
    """Test ``B*w + A*v = level`` for a pair of determinant vertices."""

    a, w = left.coefficient, left.longitudinal
    b, v = right.coefficient, right.longitudinal
    if min(abs(a), abs(b)) < 1:
        raise ValueError("coefficients must be nonzero")
    if primitive_direction and gcd(abs(a), abs(b)) != 1:
        return False
    return b * w + a * v == level


def content_block_degree_bounds(left_content: int, right_content: int) -> tuple[Fraction, Fraction]:
    """Schur degree bounds for one exact content block.

    With ``A,B`` in intervals of comparable length ``U`` and size ``U``,
    division by the contents reduces the two congruence moduli to sizes
    ``U/g`` and ``U/h``.  The row and column degrees are therefore bounded,
    up to an absolute endpoint constant, by ``1+g/h`` and ``1+h/g``.
    """

    if min(left_content, right_content) < 1:
        raise ValueError("contents must be positive")
    g = left_content
    h = right_content
    return Fraction(g + h, h), Fraction(g + h, g)


def fixed_determinant_star(scale: int) -> tuple[int, DeterminantVertex, tuple[DeterminantVertex, ...]]:
    """Return the sharp nonprimitive star at level ``3*scale^2``.

    The right vertex is ``(scale,scale)``.  For every
    ``scale <= A < 2*scale`` coprime to ``3*scale``, the left vertex
    ``(A,3*scale-A)`` is primitive and is incident to that right vertex.
    """

    if scale < 2:
        raise ValueError("scale must be at least two")
    level = 3 * scale * scale
    right = DeterminantVertex(scale, scale)
    rows = tuple(
        DeterminantVertex(a, 3 * scale - a)
        for a in range(scale, 2 * scale)
        if gcd(a, 3 * scale) == 1
    )
    return level, right, rows


def survivor_exponent_ledger() -> dict[str, Fraction]:
    """Return the exact exponents at the surviving balanced grid.

    Here ``E=D``, ``T=1``, ``R=S=D^(3/16)``, and
    ``U=D^(5/32)``.  The determinant-content color mass is ``D^(11/16)``
    and ``sqrt(D/(R*S))=U^2``.
    """

    u = Fraction(5, 32)
    color_mass = Fraction(11, 16)
    curvature_prefactor = Fraction(5, 16)
    return {
        "u": u,
        "color_mass": color_mass,
        "curvature_prefactor": curvature_prefactor,
        "old_line_factor": u,
        "old_total": color_mass + curvature_prefactor + u,
        "conditional_content_line_factor": u / 2,
        "conditional_content_total": color_mass + curvature_prefactor + u / 2,
        "conditional_primitive_line_factor": Fraction(0),
        "conditional_primitive_total": color_mass + curvature_prefactor,
        "endpoint_double_gcd_total": Fraction(35, 32),
    }


def duplicated_refinement_ledger(number_of_lifts: int) -> dict[str, int]:
    """Replay why an incidence norm does not control token duplication.

    A base token of squared mass one can be copied to ``N`` vertices of a
    perfect matching.  The matching has operator norm one, but the refined
    squared mass and the positive bilinear form are both ``N``.
    """

    if number_of_lifts < 1:
        raise ValueError("number_of_lifts must be positive")
    return {
        "base_squared_mass": 1,
        "refined_squared_mass": number_of_lifts,
        "matching_operator_norm": 1,
        "positive_bilinear_value": number_of_lifts,
    }
