"""Exact divisor reconstruction for the scaled-cusp fold-height branch.

The branch ``H-p*U=0`` has parameters

``Q=p*L,  g=d*a,  a*(p^2-d^2)+3*w=2*d*L``

and errors

``4*e=w*(a*(p-d)^2-w)``,
``4*f=w*(a*(p+d)^2-w)``.

This module records the two exact divisor identities which give an
``O(sqrt(A) Q^o(1))`` count under ``|e|<=A``.  It is a finite replay of the
arithmetic argument, not an implementation of the surrounding phase-jet
large sieve.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


@dataclass(frozen=True)
class FoldHeightDivisorData:
    """All exact factors attached to one fold-height parameter tuple."""

    Q: int
    p: int
    d: int
    a: int
    w: int
    L: int
    x: int
    z: int
    g: int
    y: int
    e: int
    f: int
    eta_left: int
    eta_right: int
    small_left_target: int
    small_left_factor: int
    large_left_target: int
    large_left_factor: int
    small_right_target: int
    small_right_factor: int
    large_right_target: int
    large_right_factor: int


def fold_height_divisor_data(
    Q: int, p: int, d: int, a: int, w: int
) -> FoldHeightDivisorData:
    """Return and verify the four fold-height divisor factorizations.

    Signed ``d`` is allowed.  Physical positivity says ``g=d*a>0``;
    consequently ``a`` and ``d`` have the same sign.  Both
    ``x=p-d`` and ``z=p+d`` remain positive because ``|d|<p``.
    """

    if Q <= 0 or p <= 0 or Q % p:
        raise ValueError("require Q>0, p>0, and p|Q")
    if d == 0 or abs(d) >= p or gcd(p, abs(d)) != 1:
        raise ValueError("require 0<|d|<p and gcd(p,d)=1")
    if a * d <= 0:
        raise ValueError("require positive content g=a*d")
    L = Q // p
    x, z = p - d, p + d
    if a * x * z + 3 * w != 2 * d * L:
        raise ValueError("parameters do not lie on the fold-height branch")

    g = a * d
    if (g * x) % 2 or (g * z) % 2:
        raise ValueError("the two physical shifts must be integral")
    y = d * L - w
    e4 = w * (a * x * x - w)
    f4 = w * (a * z * z - w)
    if e4 % 4 or f4 % 4:
        raise AssertionError("physical errors should be integral")
    e, f = e4 // 4, f4 // 4

    eta_left = a * x * x - w
    eta_right = a * z * z - w

    small_left_target = 2 * Q - 3 * w
    small_left_factor = x * (2 * L + a * z)
    large_left_target = 2 * Q + 3 * eta_left
    large_left_factor = 2 * x * (a * (p + x) + L)

    small_right_target = 2 * Q + 3 * w
    small_right_factor = z * (2 * L - a * x)
    large_right_target = 3 * eta_right - 2 * Q
    large_right_factor = 2 * z * (a * (p + z) - L)

    assert small_left_factor == small_left_target
    assert large_left_factor == large_left_target
    assert small_right_factor == small_right_target
    assert large_right_factor == large_right_target
    assert 4 * e == w * eta_left
    assert 4 * f == w * eta_right
    return FoldHeightDivisorData(
        Q=Q,
        p=p,
        d=d,
        a=a,
        w=w,
        L=L,
        x=x,
        z=z,
        g=g,
        y=y,
        e=e,
        f=f,
        eta_left=eta_left,
        eta_right=eta_right,
        small_left_target=small_left_target,
        small_left_factor=small_left_factor,
        large_left_target=large_left_target,
        large_left_factor=large_left_factor,
        small_right_target=small_right_target,
        small_right_factor=small_right_factor,
        large_right_target=large_right_target,
        large_right_factor=large_right_factor,
    )


def positive_divisors(value: int) -> tuple[int, ...]:
    """Return the positive divisors of a nonzero integer."""

    value = abs(value)
    if value == 0:
        raise ValueError("zero has no finite divisor list")
    low: list[int] = []
    high: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor == 0:
            low.append(divisor)
            if divisor * divisor != value:
                high.append(value // divisor)
    return tuple(low + high[::-1])


def fold_height_divisor_majorant(Q: int, A: int) -> int:
    """Return the literal divisor-sum upper bound from the proof.

    We split at ``w^2<=A``.  In the complementary range,
    ``eta=a*(p-d)^2-w`` obeys ``|eta|<4*sqrt(A)`` because
    ``4e=w*eta``.  The returned majorant also sums over ``p|Q``.

    The mild size condition makes every divisor target nonzero.  It holds
    with a large power margin in the four-cycle energy core.
    """

    if Q <= 0 or A < 1:
        raise ValueError("require Q>0 and A>=1")
    root = isqrt(A)
    eta_radius = isqrt(16 * A)
    if 2 * Q <= 3 * eta_radius:
        raise ValueError("require 2Q>12sqrt(A) to exclude a zero target")
    small_sum = sum(
        len(positive_divisors(2 * Q - 3 * w))
        for w in range(-root, root + 1)
    )
    large_sum = sum(
        len(positive_divisors(2 * Q + 3 * eta))
        for eta in range(-eta_radius, eta_radius + 1)
    )
    return len(positive_divisors(Q)) * (small_sum + large_sum)


def reconstruct_fold_height_points(
    Q: int, A: int, B: int
) -> tuple[FoldHeightDivisorData, ...]:
    """Reconstruct every physical fold point in ``|e|<=A, |f|<=B``.

    The search follows the proof rather than imposing an artificial bound
    on ``a`` or ``w``.  It is intended for finite verification fixtures.
    """

    if A < 1 or B < A:
        raise ValueError("require 1<=A<=B")
    root = isqrt(A)
    eta_radius = isqrt(16 * A)
    if 2 * Q <= 3 * eta_radius:
        raise ValueError("require 2Q>12sqrt(A) to exclude a zero target")
    points: dict[tuple[int, int, int, int], FoldHeightDivisorData] = {}

    def retain(p: int, d: int, a: int, w: int) -> None:
        if d == 0 or abs(d) >= p or gcd(p, abs(d)) != 1 or a * d <= 0:
            return
        try:
            data = fold_height_divisor_data(Q, p, d, a, w)
        except (ValueError, AssertionError):
            return
        if abs(data.e) <= A and abs(data.f) <= B:
            points[(p, d, a, w)] = data

    for p in positive_divisors(Q):
        L = Q // p
        # Small-w chart: x divides 2Q-3w.
        for w in range(-root, root + 1):
            target = 2 * Q - 3 * w
            for x in positive_divisors(target):
                if not 0 < x < 2 * p or x == p:
                    continue
                z = 2 * p - x
                quotient = target // x - 2 * L
                if quotient % z:
                    continue
                retain(p, p - x, quotient // z, w)

        # Large-w chart: x divides 2Q+3eta.
        for eta in range(-eta_radius, eta_radius + 1):
            target = 2 * Q + 3 * eta
            for x in positive_divisors(target):
                if not 0 < x < 2 * p or x == p or target % (2 * x):
                    continue
                denominator = p + x
                numerator = target // (2 * x) - L
                if numerator % denominator:
                    continue
                a = numerator // denominator
                w = a * x * x - eta
                if w * w <= A:
                    continue
                retain(p, p - x, a, w)

    return tuple(points[key] for key in sorted(points))


def fold_height_energy_exponents() -> dict[str, Fraction]:
    """Return the power margins used to make all targets comparable to Q."""

    q = Fraction(33, 16)
    a_max = Fraction(11, 10)
    sqrt_a_max = a_max / 2
    target_margin = q - sqrt_a_max
    assert sqrt_a_max == Fraction(11, 20)
    assert target_margin == Fraction(121, 80)
    return {
        "Q": q,
        "A_max": a_max,
        "sqrt_A_max": sqrt_a_max,
        "target_nonzero_margin": target_margin,
    }
