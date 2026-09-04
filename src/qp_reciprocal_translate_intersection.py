"""Exact algebra for translated reciprocal-window intersections.

For an integer ``target`` and window ``width`` we study integers ``a`` for
which there is an integer ``n`` with ``|a*n-target| <= width``.  A translated
intersection consists of

    a*n = target + e,
    (a+h)*m = target + f,

with ``|e|, |f| <= width``.  The routines below expose the exact midpoint and
primitive-direction normal forms of such a pair.  They are deliberately
integer-only: no floating-point nearest-integer decision is used.

This module certifies reductions and finite experiments.  It does *not* claim
the unresolved uniform ``sqrt(width)`` translate-intersection theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True)
class ReciprocalPair:
    a: int
    n: int
    m: int
    shift: int
    target: int

    @property
    def e(self) -> int:
        return self.a * self.n - self.target

    @property
    def f(self) -> int:
        return (self.a + self.shift) * self.m - self.target

    @property
    def k(self) -> int:
        return self.n - self.m

    @property
    def X(self) -> int:
        return 2 * self.a + self.shift

    @property
    def Y(self) -> int:
        return self.n + self.m


@dataclass(frozen=True)
class PrimitiveNormalForm:
    g: int
    r: int
    s: int
    T: int
    Z: int


def admissible_quotient(a: int, target: int, width: int) -> int | None:
    """Return the unique quotient in the reciprocal window, when it exists.

    Uniqueness is automatic under ``2*width < a``.  This hypothesis is the
    one used in the reciprocal-strip application.
    """

    if a <= 0 or width < 0:
        raise ValueError("a must be positive and width nonnegative")
    if 2 * width >= a:
        raise ValueError("the window is not narrow enough for uniqueness")
    lower = (target - width + a - 1) // a
    upper = (target + width) // a
    if lower > upper:
        return None
    if lower != upper:
        raise AssertionError("narrow-window uniqueness failed")
    return lower


def translated_pairs(
    target: int,
    width: int,
    shift: int,
    a_min: int,
    a_max: int,
) -> list[ReciprocalPair]:
    """Enumerate starts ``a`` for which both ``a`` and ``a+shift`` qualify."""

    if shift <= 0:
        raise ValueError("this finite enumerator uses a positive shift")
    answer: list[ReciprocalPair] = []
    for a in range(a_min, a_max + 1):
        n = admissible_quotient(a, target, width)
        m = admissible_quotient(a + shift, target, width)
        if n is not None and m is not None:
            answer.append(ReciprocalPair(a, n, m, shift, target))
    return answer


def primitive_normal_form(pair: ReciprocalPair) -> PrimitiveNormalForm:
    """Return ``h=g*s``, ``k=g*r`` and the tangent coordinates ``T,Z``."""

    h = pair.shift
    k = pair.k
    if h <= 0 or k <= 0:
        raise ValueError("the intended dyadic reciprocal box has h,k > 0")
    g = gcd(h, k)
    r, s = k // g, h // g
    return PrimitiveNormalForm(
        g=g,
        r=r,
        s=s,
        T=r * pair.X + s * pair.Y,
        Z=r * pair.X - s * pair.Y,
    )


def verify_midpoint_identities(pair: ReciprocalPair) -> bool:
    """Check the two exact midpoint identities.

    They are

        X*k - Y*h = 2(e-f),
        X*Y - h*k - 4*target = 2(e+f).
    """

    return (
        pair.X * pair.k - pair.Y * pair.shift == 2 * (pair.e - pair.f)
        and pair.X * pair.Y - pair.shift * pair.k - 4 * pair.target
        == 2 * (pair.e + pair.f)
    )


def verify_primitive_identities(pair: ReciprocalPair) -> bool:
    """Check the primitive tangent/hyperbola identities and CRT masks."""

    form = primitive_normal_form(pair)
    h, k = pair.shift, pair.k
    g, r, s, T, Z = form.g, form.r, form.s, form.T, form.Z
    center = 4 * r * s * (4 * pair.target + g * g * r * s)
    return (
        gcd(r, s) == 1
        and h == g * s
        and k == g * r
        and g * Z == 2 * (pair.e - pair.f)
        and T * T - Z * Z - center == 8 * r * s * (pair.e + pair.f)
        and (T + Z) % (2 * r) == 0
        and (T - Z) % (2 * s) == 0
    )


def diamond_slack(pair: ReciprocalPair, width: int) -> int:
    """Return the slack in the exact L1 normal-form window.

    Admissibility ``|e|,|f| <= width`` is equivalent to nonnegative slack:

      16*r*s*width
        - |T^2-Z^2-4*r*s*(4*target+g^2*r*s)|
        - 4*g*r*s*|Z|.
    """

    form = primitive_normal_form(pair)
    g, r, s, T, Z = form.g, form.r, form.s, form.T, form.Z
    center = 4 * r * s * (4 * pair.target + g * g * r * s)
    return (
        16 * r * s * width
        - abs(T * T - Z * Z - center)
        - 4 * g * r * s * abs(Z)
    )


def reconstruct_from_midpoint(
    X: int,
    Y: int,
    shift: int,
    k: int,
    target: int,
) -> ReciprocalPair:
    """Invert the midpoint map, rejecting parity failures."""

    if (X - shift) % 2 or (Y + k) % 2 or (Y - k) % 2:
        raise ValueError("midpoint parity conditions fail")
    a = (X - shift) // 2
    n = (Y + k) // 2
    m = (Y - k) // 2
    return ReciprocalPair(a, n, m, shift, target)


def tangent_chain(target_root: int, width: int, shift: int) -> list[ReciprocalPair]:
    """The sharp ``sqrt(width)`` lower-bound family at ``target=root^2``.

    For ``a=root+t``, choose ``n=root-t`` and
    ``m=root-t-shift``.  The two errors are ``-t^2`` and
    ``-(t+shift)^2``.
    """

    if target_root <= 0 or width < 0 or shift <= 0:
        raise ValueError("positive root/shift and nonnegative width required")
    last = isqrt(width) - shift
    if last < 0:
        return []
    target = target_root * target_root
    return [
        ReciprocalPair(
            a=target_root + t,
            n=target_root - t,
            m=target_root - t - shift,
            shift=shift,
            target=target,
        )
        for t in range(last + 1)
    ]


def worst_shift_intersection(
    target: int,
    width: int,
    a_min: int,
    a_max: int,
    max_shift: int,
) -> tuple[int, int]:
    """Return ``(largest_count, attaining_shift)`` for a finite fixture."""

    best_count, best_shift = 0, 0
    for shift in range(1, max_shift + 1):
        count = len(
            translated_pairs(target, width, shift, a_min, a_max - shift)
        )
        if count > best_count:
            best_count, best_shift = count, shift
    return best_count, best_shift


def worst_target_on_interval(
    target_min: int,
    target_max: int,
    width: int,
    shift: int,
    a_min: int,
    a_max: int,
) -> tuple[int, int]:
    """Sweep *all* integer targets in an interval without sampling them.

    Each possible pair of products ``a*n`` and ``(a+shift)*m`` contributes an
    inclusive interval of targets on which both errors have size at most
    ``width``.  A line sweep returns the maximum overlap depth and an attaining
    target.  Under the usual narrow-window hypotheses, overlap depth is exactly
    translate-intersection cardinality.
    """

    if target_min > target_max:
        raise ValueError("empty target interval")
    if shift <= 0 or width < 0:
        raise ValueError("positive shift and nonnegative width required")
    events: dict[int, int] = {}
    for a in range(a_min, a_max + 1):
        b = a + shift
        n_min = (target_min - width + a - 1) // a
        n_max = (target_max + width) // a
        for n in range(n_min, n_max + 1):
            first_product = a * n
            m_floor = first_product // b
            for m in (m_floor, m_floor + 1):
                second_product = b * m
                left = max(
                    target_min,
                    first_product - width,
                    second_product - width,
                )
                right = min(
                    target_max,
                    first_product + width,
                    second_product + width,
                )
                if left <= right:
                    events[left] = events.get(left, 0) + 1
                    events[right + 1] = events.get(right + 1, 0) - 1
    active = best = 0
    attaining_target = target_min
    for target in sorted(events):
        active += events[target]
        if target <= target_max and active > best:
            best = active
            attaining_target = target
    return best, attaining_target
