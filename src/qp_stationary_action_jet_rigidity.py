"""Exact rigidity of the completion-sum stationary-action three-jet.

For fixed ``C`` consider

    F(a,S) = -m*a + C*h/a + C*k/(S-a).

At a regular stationary point in ``a``, the critical value ``psi(S)`` is a
function of the physical completion sum.  This module computes its first
three derivatives exactly and inverts that three-jet.  It deliberately does
not assert the still-open quantitative Bessel estimate for near-coincident
jets.
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt
from typing import Mapping


def _q(value: int | Fraction) -> Fraction:
    return Fraction(value)


def stationary_action_three_jet(
    C: int | Fraction,
    S: int | Fraction,
    a: int | Fraction,
    h: int | Fraction,
    k: int | Fraction,
    m: int | Fraction,
) -> dict[str, Fraction]:
    """Return the exact critical action and its first three ``S`` jets.

    The inputs must obey the stationary equation

    ``m=C*(k/(S-a)^2-h/a^2)``.

    Regularity means ``X*b+Y*a != 0`` for
    ``X=h/a^2`` and ``Y=k/b^2``.  This is exactly nonvanishing of the
    second derivative of the original phase in the saddle variable.
    """

    Cq, Sq, aq = _q(C), _q(S), _q(a)
    hq, kq, mq = _q(h), _q(k), _q(m)
    bq = Sq - aq
    if Cq <= 0 or aq <= 0 or bq <= 0:
        raise ValueError("require C>0 and an interior saddle 0<a<S")
    X = hq / aq**2
    Y = kq / bq**2
    if mq != Cq * (Y - X):
        raise ValueError("the supplied point does not satisfy stationarity")
    D = X * bq + Y * aq
    if D == 0:
        raise ValueError("the stationary point is a fold, not a regular saddle")

    action = -mq * aq + Cq * hq / aq + Cq * kq / bq
    first = -Cq * Y
    second = 2 * Cq * X * Y / D
    third = -6 * Cq * X * Y * (X**2 * bq + Y**2 * aq) / D**3
    return {
        "C": Cq,
        "S": Sq,
        "a": aq,
        "b": bq,
        "h": hq,
        "k": kq,
        "m": mq,
        "X": X,
        "Y": Y,
        "D": D,
        "action": action,
        "first": first,
        "second": second,
        "third": third,
    }


def stationary_action_four_jet(
    C: int | Fraction,
    S: int | Fraction,
    a: int | Fraction,
    h: int | Fraction,
    k: int | Fraction,
    m: int | Fraction,
) -> dict[str, Fraction]:
    """Return the exact critical action and its first four ``S`` jets."""

    record = stationary_action_three_jet(C, S, a, h, k, m)
    Cq = record["C"]
    aq, bq = record["a"], record["b"]
    X, Y, D = record["X"], record["Y"], record["D"]
    numerator = (
        4 * X**4 * bq**2
        - 5 * X**3 * Y * aq * bq
        + 18 * X**2 * Y**2 * aq * bq
        - 5 * X * Y**3 * aq * bq
        + 4 * Y**4 * aq**2
    )
    record["fourth"] = 6 * Cq * X * Y * numerator / D**5
    return record


def _rational_square_root(value: Fraction) -> Fraction:
    """Return the nonnegative rational square root, or reject a non-square."""

    if value < 0:
        raise ValueError("a real stationary jet cannot have a negative square")
    numerator = isqrt(value.numerator)
    denominator = isqrt(value.denominator)
    if numerator**2 != value.numerator or denominator**2 != value.denominator:
        raise ValueError("the supplied exact jet does not reconstruct a rational saddle")
    return Fraction(numerator, denominator)


def recover_reflection_orbit_from_higher_three_jet(
    C: int | Fraction,
    S: int | Fraction,
    second: int | Fraction,
    third: int | Fraction,
    fourth: int | Fraction,
) -> tuple[dict[str, Fraction], dict[str, Fraction]]:
    """Invert ``(psi'',psi''',psi'''')`` modulo physical reflection.

    No value of ``psi'`` is used, so the inverse survives the integral affine
    Poisson alias.  On an interior regular branch with ``h*k*m != 0``, the
    only two reconstructions are

    ``(a,h,k,m)`` and ``(S-a,k,h,-m)``.

    The implementation is exact for rational jets arising from rational
    saddle data.  It is also a replayable form of the algebraic proof.
    """

    Cq, Sq = _q(C), _q(S)
    q2, q3, q4 = _q(second), _q(third), _q(fourth)
    if Cq <= 0 or Sq <= 0 or q2 == 0:
        raise ValueError("require C,S>0 and a nonzero second jet")

    # Put t=a/S and u=da/dS.  The two scale-free higher-jet invariants are
    #
    # A=1+(u-t)^2/[t(1-t)],
    # B=4*A^2-5*R*(A-1),  R=u(1-u)/[t(1-t)].
    A = -Sq * q3 / (3 * q2)
    w = A - 1
    if w <= 0:
        raise ValueError("the higher jet lies on or outside the zero-dual branch")
    B = Sq**2 * q4 / (3 * q2)
    R = (4 * A**2 - B) / (5 * w)
    ell = 1 - R - w

    # With x=2t-1 and y=2u-1, reflection is (x,y)->(-x,-y).
    # The invariants give
    #   (y-x)^2=w(1-x^2),  2x(y-x)=ell(1-x^2).
    x_squared = ell**2 / (ell**2 + 4 * w)
    x = _rational_square_root(x_squared)
    if ell == 0:
        if x != 0:
            raise AssertionError("the central-saddle reconstruction is inconsistent")
        y = _rational_square_root(w)
    else:
        y = x * (ell + 2 * w) / ell

    answers: list[dict[str, Fraction]] = []
    for oriented_x, oriented_y in ((x, y), (-x, -y)):
        t = (1 + oriented_x) / 2
        u = (1 + oriented_y) / 2
        if not 0 < t < 1 or u in (0, 1):
            raise ValueError("the jet does not reconstruct a regular interior mode")
        aq, bq = Sq * t, Sq * (1 - t)
        X = Sq * t * q2 / (2 * Cq * u)
        Y = Sq * (1 - t) * q2 / (2 * Cq * (1 - u))
        h, k = X * aq**2, Y * bq**2
        m = Cq * (Y - X)
        if h == 0 or k == 0 or m == 0:
            raise ValueError("the inverse excludes zero frequencies and zero dual mode")
        replay = stationary_action_four_jet(Cq, Sq, aq, h, k, m)
        assert (replay["second"], replay["third"], replay["fourth"]) == (
            q2,
            q3,
            q4,
        )
        answers.append(replay)

    first, reflected = answers
    assert reflected["a"] == first["b"]
    assert (reflected["h"], reflected["k"], reflected["m"]) == (
        first["k"],
        first["h"],
        -first["m"],
    )
    return first, reflected


def recover_saddle_from_three_jet(
    C: int | Fraction,
    S: int | Fraction,
    first: int | Fraction,
    second: int | Fraction,
    third: int | Fraction,
) -> dict[str, Fraction]:
    """Invert a regular nonzero-dual stationary-action three-jet.

    The inverse is valid when ``h*k*m != 0`` and the saddle is regular.
    The exceptional denominator vanishes exactly on the zero-dual branch
    ``m=0`` (apart from excluded zero frequencies/endpoints).
    """

    Cq, Sq = _q(C), _q(S)
    q1, q2, q3 = _q(first), _q(second), _q(third)
    if Cq <= 0 or Sq <= 0 or q1 == 0 or q2 == 0:
        raise ValueError("require C,S>0 and nonzero first and second jets")

    Y = -q1 / Cq
    inverse_denominator = 1 + 2 * Cq * Y * q3 / (3 * q2**2)
    if inverse_denominator == 0:
        raise ValueError("the three-jet lies on the zero-dual exceptional branch")
    X = (Sq * q2 / (2 * Cq) - Y) / inverse_denominator
    if X == 0 or X == Y:
        raise ValueError("the inverse requires nonzero frequencies and m!=0")

    D = 2 * Cq * X * Y / q2
    a = (D - X * Sq) / (Y - X)
    b = Sq - a
    if a <= 0 or b <= 0 or D == 0:
        raise ValueError("the jet does not reconstruct an interior regular saddle")
    h = X * a**2
    k = Y * b**2
    m = Cq * (Y - X)

    replay = stationary_action_three_jet(Cq, Sq, a, h, k, m)
    assert (replay["first"], replay["second"], replay["third"]) == (q1, q2, q3)
    return replay


def three_jet_collision_is_identical(
    left: Mapping[str, Fraction], right: Mapping[str, Fraction]
) -> bool:
    """Verify exact three-jet rigidity for two precomputed saddle records."""

    if left["C"] != right["C"] or left["S"] != right["S"]:
        raise ValueError("collision comparison requires the same C and S")
    same_jet = all(left[name] == right[name] for name in ("first", "second", "third"))
    if not same_jet:
        return False
    recovered = recover_saddle_from_three_jet(
        left["C"], left["S"], left["first"], left["second"], left["third"]
    )
    for name in ("a", "b", "h", "k", "m", "X", "Y"):
        assert left[name] == recovered[name] == right[name]
    return True
