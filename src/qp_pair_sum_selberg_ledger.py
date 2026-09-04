"""Exact ledgers for the fixed pair-sum reciprocal-strip problem.

For ``a+b=S`` put ``n=a*v`` and ``m=b*w``.  The companion report uses
these identities to isolate the tangent (zero Poisson mode) contribution
from the still-open nonzero two-inverse frequency aggregate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


Q_POWER_IN_D = Fraction(33, 16)
WINDOW_POWER_IN_D = Fraction(1)
DELTA_POWER_IN_D = WINDOW_POWER_IN_D - Q_POWER_IN_D
SELBERG_DEGREE_POWER_IN_D = -DELTA_POWER_IN_D


def selberg_pair_sum_exponent_ledger() -> dict[str, Fraction]:
    """Return the exact powers arising after one-dimensional Poisson.

    The Selberg coefficients have size ``delta=D/q`` and degree
    ``H=q/D``.  A one-frequency Poisson sum has absolute scale
    ``sqrt(q)*H^(3/2)`` after summing its frequency.  The double-frequency
    zero dual mode has the same total scale.  Absolute summation of all
    nonzero double-frequency saddles replaces ``H^(3/2)`` by ``H^(5/2)``.
    """

    delta = DELTA_POWER_IN_D
    degree = SELBERG_DEGREE_POWER_IN_D
    q = Q_POWER_IN_D
    target = Fraction(1, 2)
    zero_zero = q + 2 * delta
    one_frequency = 2 * delta + q / 2 + 3 * degree / 2
    zero_dual = one_frequency
    nonzero_nondegenerate_termwise = (
        2 * delta + q / 2 + 5 * degree / 2
    )
    # A cubic (Airy) saddle has size (q^2/K)^(1/3).  Allowing one such
    # mode for every opposite-sign frequency pair gives this deliberately
    # crude absolute ledger.  It is smaller than the nondegenerate bulk
    # power, but it must not be silently treated as a quadratic saddle.
    caustic_pairwise_absolute = (
        2 * delta + 2 * q / 3 + 5 * degree / 3
    )
    # At C=Q^2, S=2Q, the coherent exact family (h,k,m)=(t,-t,-2t)
    # has only H members, not H^2.
    symmetric_exact_caustic = (
        2 * delta + 2 * q / 3 + 2 * degree / 3
    )
    return {
        "q": q,
        "delta": delta,
        "H": degree,
        "zero_zero": zero_zero,
        "one_frequency": one_frequency,
        "zero_dual_tangent": zero_dual,
        "nonzero_nondegenerate_termwise": nonzero_nondegenerate_termwise,
        "caustic_pairwise_absolute": caustic_pairwise_absolute,
        "symmetric_exact_caustic": symmetric_exact_caustic,
        "target": target,
        "missing_cancellation_power": (
            nonzero_nondegenerate_termwise - target
        ),
    }


@dataclass(frozen=True)
class CenteredPairData:
    """Centered coordinates and product labels for one fixed-sum pair."""

    S: int
    x: int
    U: int
    y: int
    n: int
    m: int


@dataclass(frozen=True)
class CenteredWindowData:
    """Centered data together with its two product-window labels."""

    S: int
    x: int
    U: int
    z: int
    n: int
    m: int
    sigma: Fraction
    tau: int


def centered_pair_data(a: int, b: int, v: int, w: int) -> CenteredPairData:
    """Return ``x=a-b``, ``U=v+w``, and ``y=w-v``.

    They obey

    ``S*U-x*y = 2*(n+m)`` and ``x*U-S*y = 2*(n-m)``.
    """

    if min(a, b, v, w) <= 0:
        raise ValueError("all four entries must be positive")
    S = a + b
    x = a - b
    U = v + w
    y = w - v
    n = a * v
    m = b * w
    data = CenteredPairData(S, x, U, y, n, m)
    assert S * U - x * y == 2 * (n + m)
    assert x * U - S * y == 2 * (n - m)
    assert (S * S - x * x) * (U * U - y * y) == 16 * n * m
    return data


def centered_window_data(
    a: int, b: int, v: int, w: int, center: int | Fraction
) -> CenteredWindowData:
    """Return the exact fixed-sum window equations.

    Here ``x=a-b``, ``z=v-w``, ``U=v+w``,
    ``sigma=(a*v-C)+(b*w-C)``, and ``tau=a*v-b*w``.  Thus

    ``U*x+S*z=2*tau`` and ``S*U+x*z=4*C+2*sigma``.
    """

    C = Fraction(center)
    base = centered_pair_data(a, b, v, w)
    z = v - w
    sigma = Fraction(base.n + base.m) - 2 * C
    tau = base.n - base.m
    assert base.U * base.x + base.S * z == 2 * tau
    assert base.S * base.U + base.x * z == 4 * C + 2 * sigma
    assert (
        base.U * (base.S * base.S - base.x * base.x)
        + 2 * tau * base.x
        == 4 * C * base.S + 2 * base.S * sigma
    )
    return CenteredWindowData(
        base.S, base.x, base.U, z, base.n, base.m, sigma, tau
    )


def two_level_gap_ledger(
    first: CenteredWindowData, second: CenteredWindowData
) -> tuple[Fraction, int]:
    """Verify the quadratic gap law and its exact congruence.

    If ``r=x_2-x_1`` and ``Delta=U_2-U_1``, the returned first value is
    the common value of the two sides of

    ``Delta*(S^2-x_1^2)-U_2*r*(x_1+x_2)``
    ``=2*S*(sigma_2-sigma_1)-2*(tau_2*x_2-tau_1*x_1)``.

    The second return value is the integer quotient after dividing

    ``U_1*U_2*r-2*(U_1*tau_2-U_2*tau_1)`` by ``S``.
    """

    if first.S != second.S:
        raise ValueError("the two points must have the same denominator sum")
    S = first.S
    r = second.x - first.x
    delta = second.U - first.U
    lhs = (
        delta * (S * S - first.x * first.x)
        - second.U * r * (first.x + second.x)
    )
    rhs = (
        2 * S * (second.sigma - first.sigma)
        - 2 * (second.tau * second.x - first.tau * first.x)
    )
    assert Fraction(lhs) == rhs
    congruence = (
        first.U * second.U * r
        - 2 * (first.U * second.tau - second.U * first.tau)
    )
    assert congruence % S == 0
    return rhs, congruence // S


def ordered_matching_residuals(
    first: tuple[int, int, int, int],
    second: tuple[int, int, int, int],
) -> tuple[int, int]:
    """Return the two exact small determinants between ordered points.

    Inputs are ``(a,b,v,w)`` with a common ``a+b`` and ``a_2>a_1``.
    If their two products lie in an interval shorter than every shell
    variable, monotonicity forces ``p=v_1-v_2>0`` and ``s=w_2-w_1>0``.
    The residuals are exactly the changes in ``a*v`` and ``b*w``:

    ``v_1*r-a_2*p`` and ``b_2*s-w_1*r``.
    """

    a1, b1, v1, w1 = first
    a2, b2, v2, w2 = second
    if a1 + b1 != a2 + b2 or not a2 > a1:
        raise ValueError("require a common sum and a_2>a_1")
    r = a2 - a1
    p = v1 - v2
    s = w2 - w1
    first_residual = v1 * r - a2 * p
    second_residual = b2 * s - w1 * r
    assert first_residual == a2 * v2 - a1 * v1
    assert second_residual == b2 * w2 - b1 * w1
    return first_residual, second_residual


def residue_factorization(
    a: int, b: int, v: int, w: int, integer_center: int
) -> tuple[int, int, int]:
    """Return the fixed-residue hyperbola factorization.

    For ``C0`` integral, ``X=S*v-C0`` and ``Y=S*w-C0`` are both congruent
    to ``-C0 (mod S)`` and

    ``X*Y-C0^2=S*((a*v-C0)*w+(b*w-C0)*v)``.
    """

    S = a + b
    C0 = integer_center
    n, m = a * v, b * w
    X, Y = S * v - C0, S * w - C0
    residual = X * Y - C0 * C0
    assert X % S == (-C0) % S
    assert Y % S == (-C0) % S
    assert residual == S * ((n - C0) * w + (m - C0) * v)
    return X, Y, residual


def cross_factorization(a: int, b: int, v: int, w: int) -> tuple[int, int]:
    """Return the exact cross factors whose product is ``(a*v)*(b*w)``.

    If ``S=a+b``, then ``S*v-a*v=b*v`` and ``S*w-b*w=a*w``.
    """

    S = a + b
    n = a * v
    m = b * w
    left = S * v - n
    right = S * w - m
    assert left == b * v
    assert right == a * w
    assert left * right == n * m
    return left, right


def rational_tangent_point(
    center: int, half_step: int, numerator: int = 1, denominator: int = 1
) -> tuple[int, int, int, int, int]:
    """Construct one point of an exact rational tangent packet.

    With coprime positive ``numerator=r`` and ``denominator=s``, the packet
    is

    ``a=s(Q+h), b=s(Q-h), v=r(Q-h), w=r(Q+h)``.

    Both products equal ``r*s*(Q^2-h^2)``.  The returned final entry is the
    tangent centre ``r*s*Q^2``.
    """

    Q = center
    h = half_step
    r = numerator
    s = denominator
    if min(Q - abs(h), r, s) <= 0:
        raise ValueError("the tangent point must stay positive")
    a = s * (Q + h)
    b = s * (Q - h)
    v = r * (Q - h)
    w = r * (Q + h)
    tangent_center = r * s * Q * Q
    assert a * v == b * w == tangent_center - r * s * h * h
    return a, b, v, w, tangent_center


def common_product_parametrization(
    gcd_ab: int, primitive_a: int, primitive_b: int, slope_scale: int
) -> tuple[int, int, int, int, int]:
    """Parametrize the exact slice ``a*v=b*w``.

    If ``(A,B)=1``, every positive solution with ``gcd(a,b)=g`` is
    ``a=g*A, b=g*B, v=B*l, w=A*l``.
    """

    from math import gcd

    g = gcd_ab
    A = primitive_a
    B = primitive_b
    ell = slope_scale
    if min(g, A, B, ell) <= 0 or gcd(A, B) != 1:
        raise ValueError("positive data with gcd(A,B)=1 are required")
    a, b, v, w = g * A, g * B, B * ell, A * ell
    n = g * ell * A * B
    assert a * v == b * w == n
    return a, b, v, w, n


def symmetric_cubic_caustic_phase(
    center: int, frequency: int, offset: int
) -> Fraction:
    """Evaluate the exact opposite-sign cubic caustic phase.

    This is ``C*(t/x-t/(S-x))-m*x`` at
    ``C=Q^2, S=2Q, m=-2t, x=Q+y``.  The returned identity exposes the
    cubic term after the constant integer phase ``2*t*Q``.
    """

    Q = center
    t = frequency
    y = offset
    if Q <= 0 or abs(y) >= Q:
        raise ValueError("require Q>0 and |y|<Q")
    x = Q + y
    direct = Fraction(Q * Q * t, x) - Fraction(
        Q * Q * t, 2 * Q - x
    ) + 2 * t * x
    cubic = Fraction(2 * t * Q) - Fraction(
        2 * t * y**3, Q * Q - y * y
    )
    assert direct == cubic
    return direct
