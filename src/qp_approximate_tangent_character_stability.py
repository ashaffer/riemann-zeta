"""Exact high-denominator character identities for the symmetric QP cusp.

The routines here audit the transfer from a physical slope to the cyclic
stationary character when ``lambda=1/4``.  They deliberately do not assert
the still-open outer square-function estimate.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def normalized_fejer_coefficient(order: int, frequency: int) -> Fraction:
    """Return the triangular Fourier coefficient of normalized Fejer mass."""

    if order <= 0:
        raise ValueError("order must be positive")
    if abs(frequency) >= order:
        return Fraction()
    return Fraction(order - abs(frequency), order * order)


def symmetric_character_geometry(
    p: int, d: int, h: int, k: int, m: int
) -> dict[str, Fraction | int]:
    """Evaluate stationarity and curvature at ``t0=(p+d)/(2p)``.

    The normalized phase is

    ``Phi(t)=(h/(4t))+(k/(4(1-t)))-m*t``.

    Thus stationarity asks that

    ``M=p^2*(k/(p-d)^2-h/(p+d)^2)``

    equal the integer ``m``.
    """

    if p <= 0 or abs(d) >= p or gcd(p, d) != 1:
        raise ValueError("require p>0, |d|<p, and gcd(p,d)=1")
    r, s = p + d, p - d
    stationary_value = Fraction(p * p * k, s * s) - Fraction(p * p * h, r * r)
    t0 = Fraction(r, 2 * p)
    second = Fraction(h, 2 * t0**3) + Fraction(k, 2 * (1 - t0) ** 3)
    third = -Fraction(3 * h, 2 * t0**4) + Fraction(
        3 * k, 2 * (1 - t0) ** 4
    )
    return {
        "r": r,
        "s": s,
        "R": r * r * s * s,
        "t0": t0,
        "stationary_value": stationary_value,
        "stationary_error": stationary_value - m,
        "second_derivative": second,
        "third_derivative": third,
    }


def regular_plateau_near_character(p: int, d: int) -> dict[str, Fraction | int]:
    """Return an exact same-sign singleton defeating a high-P ``P^-4`` layer.

    If ``4|p`` and ``3|d``, put

    ``h=p/4+d/3, k=p/4-d/3, m=d/3``.

    Then exactly

    ``M-m=-d^5/(3*(p^2-d^2)^2)``.

    Both frequencies are positive when ``3p>4d``; hence this is a regular
    quadratic mode, not a fold/translated-tangent caustic.
    """

    if p % 4 or d % 3 or gcd(p, d) != 1 or d <= 0 or 3 * p <= 4 * d:
        raise ValueError("require 4|p, 3|d, gcd(p,d)=1, and 3p>4d>0")
    h, k, m = p // 4 + d // 3, p // 4 - d // 3, d // 3
    data = symmetric_character_geometry(p, d, h, k, m)
    expected = -Fraction(d**5, 3 * (p * p - d * d) ** 2)
    assert data["stationary_error"] == expected
    assert data["second_derivative"] > 0
    return {**data, "h": h, "k": k, "m": m}


def opposite_sign_joint_identity(
    p: int, d: int, h: int, v: int
) -> dict[str, Fraction | int]:
    """Return the exact residue--fold identity for ``h>0, k=-v<0``.

    Write ``u=(h+v)/2`` and

    ``F=h*(p-d)^3-v*(p+d)^3``.

    For ``A=p^2*(h/(p+d)^2+v/(p-d)^2)`` one has

    ``A=(h+v)-X-c*F``,

    where ``X=6*d^2*u/(p^2+3*d^2)`` and
    ``c=2*p^2*d/((p^2-d^2)^2*(p^2+3*d^2))``.  Moreover the actual second
    derivative is ``4*p^3*F/(p^2-d^2)^3``.
    """

    if min(p, d, h, v) <= 0 or d >= p or gcd(p, d) != 1:
        raise ValueError("require coprime p>d>0 and h,v>0")
    r, s = p + d, p - d
    R = (p * p - d * d) ** 2
    u = Fraction(h + v, 2)
    fold_integer = h * s**3 - v * r**3
    A = Fraction(p * p * h, r * r) + Fraction(p * p * v, s * s)
    X = Fraction(6 * d * d, p * p + 3 * d * d) * u
    c = Fraction(2 * p * p * d, R * (p * p + 3 * d * d))
    second = Fraction(4 * p**3 * fold_integer, (p * p - d * d) ** 3)
    assert A == h + v - X - c * fold_integer
    return {
        "r": r,
        "s": s,
        "R": R,
        "u": u,
        "A": A,
        "X": X,
        "c": c,
        "F": fold_integer,
        "second_derivative": second,
    }


def no_wrap_curvature_lower_bound(
    p: int, d: int, h: int, v: int, tolerance: Fraction
) -> Fraction:
    """Prove the conditional no-wrap curvature lower bound.

    This applies when ``dist(A,Z)<=tolerance``, ``tolerance<=X/2``, and
    ``X+c*abs(F)<1/2``.  Under those hypotheses the nearest integer cannot
    wrap, and

    ``abs(Phi''(t0)) >= 6*p*d*u/(p^2-d^2)``.
    """

    if tolerance < 0:
        raise ValueError("tolerance must be nonnegative")
    data = opposite_sign_joint_identity(p, d, h, v)
    A = data["A"]
    X = data["X"]
    c = data["c"]
    F = data["F"]
    nearest_distance = min(A - (A.numerator // A.denominator),
                           (A.numerator // A.denominator) + 1 - A)
    if nearest_distance > tolerance:
        raise ValueError("the character is not within the stated tolerance")
    if tolerance > X / 2:
        raise ValueError("the tolerance is too large for transversality")
    if X + c * abs(F) >= Fraction(1, 2):
        raise ValueError("the character is in the wrap sector")
    lower = Fraction(6 * p * d, p * p - d * d) * data["u"]
    assert abs(data["second_derivative"]) >= lower
    return lower


def wrap_resonance_form(
    p: int, d: int, h: int, v: int, wrap: int
) -> dict[str, int]:
    """Clear denominators in the fixed-wrap resonance equation.

    If the positive stationarity integer is ``m=h+v-wrap``, then

    ``R*(A-m)=wrap*R+b*v-a*h``,

    with ``a=d*(2p+d)*(p-d)^2`` and
    ``b=d*(2p-d)*(p+d)^2``.  The exact fixed-wrap equation is linear, and
    ``gcd(a,b)/d`` is one of ``1,2,4`` (the last two are only parity
    effects).  Its primitive solution step is already of order ``p^3``.
    """

    if min(p, d, h, v) <= 0 or d >= p or gcd(p, d) != 1:
        raise ValueError("require coprime p>d>0 and h,v>0")
    r, s = p + d, p - d
    R = r * r * s * s
    a = d * (2 * p + d) * s * s
    b = d * (2 * p - d) * r * r
    cleared = wrap * R + b * v - a * h
    A = Fraction(p * p * h, r * r) + Fraction(p * p * v, s * s)
    m = h + v - wrap
    assert Fraction(cleared, R) == A - m
    common = gcd(a, b)
    assert common in (d, 2 * d, 4 * d)
    return {
        "R": R,
        "a": a,
        "b": b,
        "gcd": common,
        "cleared_error": cleared,
        "positive_stationary_integer": m,
    }


def high_p_stability_exponent_ledger() -> dict[str, Fraction]:
    """Return the exact worst-cell powers for the high-P stability audit."""

    Q = Fraction(33, 16)
    H = Fraction(17, 16)
    B = Fraction(7, 6)
    P = Q - B
    d = (3 * P - Q) / 2
    W = H + 2 * P
    coefficient = -2 * H
    proposed = W / 2 - 4 * P
    X = 2 * d + H - 2 * P
    mu = H + B - Q - P
    curvature = H + d - P
    curved_amplitude = (Q - curvature) / 2
    return {
        "Q": Q,
        "H": H,
        "B": B,
        "P_f": P,
        "H_to_five_sixths": Fraction(5, 6) * H,
        "counter_window": P - Fraction(5, 6) * H,
        "physical_d": d,
        "W_at_f": W,
        "singleton_coefficient": coefficient,
        "false_P_minus_four_bound": proposed,
        "counterexample_factor": coefficient - proposed,
        "fold_offset_X": X,
        "slope_tolerance_mu": mu,
        "X_over_mu": X - mu,
        "forced_curvature": curvature,
        "curved_amplitude": curved_amplitude,
        "no_wrap_total": Fraction(55, 96),
        "no_wrap_gap_above_target": Fraction(7, 96),
        "anisotropic_gain_needed": Fraction(7, 96),
        "endpoint_sqrt_A_over_B_gain": Fraction(1, 12),
    }


def finite_wrapped_fold_fixture() -> dict[str, Fraction | int]:
    """Return a checked simultaneous near-character/fold finite fixture."""

    p, d, H = 100, 3, 235
    h, v, m = 200, 167, -366
    phase = symmetric_character_geometry(p, d, h, -v, m)
    joint = opposite_sign_joint_identity(p, d, h, v)
    tolerance = Fraction(H, p * p)
    assert abs(phase["stationary_error"]) == Fraction(880354, 99820081)
    assert abs(phase["stationary_error"]) < tolerance
    assert joint["second_derivative"] == Fraction(
        196764000000, 997302429271
    )
    assert abs(phase["third_derivative"]) > H
    return {
        "p": p,
        "d": d,
        "H": H,
        "h": h,
        "k": -v,
        "m": m,
        "tolerance": tolerance,
        "stationary_error": phase["stationary_error"],
        "second_derivative": phase["second_derivative"],
        "third_derivative": phase["third_derivative"],
        "X": joint["X"],
    }


def integer_poisson_alias_gram(
    carrier_points: tuple[int, ...], wrap_labels: tuple[int, ...]
) -> tuple[tuple[int, ...], ...]:
    """Return the exact Gram matrix of the restored affine alias characters.

    The physical affine character attached to a wrap difference ``j-j'`` is
    ``e(-(j-j')*a)``.  At every integer carrier point it is one.  Therefore
    all Poisson-wrap columns are identical before some additional nonlinear
    phase or arithmetic support is used.
    """

    if not carrier_points or not wrap_labels:
        raise ValueError("both carrier points and labels must be nonempty")
    if not all(isinstance(value, int) for value in carrier_points + wrap_labels):
        raise ValueError("carrier points and wrap labels must be integers")
    mass = len(carrier_points)
    return tuple(tuple(mass for _ in wrap_labels) for _ in wrap_labels)


def dyadic_wrap_coherence_loss(number_of_labels: int) -> Fraction:
    """Return the squared loss of coherent versus diagonal dyadic wraps.

    On one dyadic block the curvature weights ``|j|^-1/2`` are comparable.
    Factoring out that common size, ``L`` aligned aliases have coherent
    square ``L^2`` and diagonal square ``L``.  Their ratio is exactly ``L``.
    """

    if number_of_labels <= 0:
        raise ValueError("number_of_labels must be positive")
    coherent_square = number_of_labels**2
    diagonal_square = number_of_labels
    return Fraction(coherent_square, diagonal_square)
