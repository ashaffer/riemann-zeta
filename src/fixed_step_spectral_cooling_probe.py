#!/usr/bin/env python3
"""Exploratory fixed-step B-spline spectral-cooling probe.

For a fixed step ``h`` and order ``k``, put

    q_h(s) = sinh(h s / 2) / (h s / 2)

and let ``H_(h,k)`` be the Perron multiplier of the causal B-spline
primitive.  The exact multiplier of its width-``k*h`` coboundary is

    G_(h,k)(s)
      = (exp(k h s) - 1) H_(h,k)(s)
      = 2 sinh(k h s / 2) q_h(s)^k / s.

On the critical line, ``|q_h(i gamma)|^k`` is the universal low-pass factor
``|sinc(h gamma / 2)|^k``.  Off the line, the core exponential size at a
basepoint ``R`` is

    delta * R + k * log(|q_h(delta + i gamma)|).

It therefore still grows like ``delta*R`` when ``delta > 0`` and ``k=o(R)``.
This module verifies those identities and a small direct von Mangoldt
coboundary calculation.  It does not prove the required prime-side bound.
In particular, the proposed locally constant block-schedule converse remains
unproved; an arbitrary adaptive schedule is not justified by this probe.
"""

from __future__ import annotations

import argparse
import cmath
import math
from dataclasses import dataclass


FIRST_ZERO_ORDINATE = 14.134725141734693790457251983562


def _validate_h_k(h: float, k: int) -> None:
    if not math.isfinite(h) or h <= 0.0:
        raise ValueError("h must be finite and positive")
    if not isinstance(k, int) or isinstance(k, bool) or k <= 0:
        raise ValueError("k must be a positive integer")


def q_h(s: complex, h: float) -> complex:
    """Return the centered one-step multiplier ``sinh(hs/2)/(hs/2)``."""
    if not math.isfinite(h) or h <= 0.0:
        raise ValueError("h must be finite and positive")
    z = h * complex(s) / 2.0
    if z == 0.0:
        return 1.0 + 0.0j
    if abs(z) < 1.0e-4:
        z_squared = z * z
        return 1.0 + z_squared / 6.0 + z_squared * z_squared / 120.0
    return cmath.sinh(z) / z


def primitive_multiplier(s: complex, h: float, k: int) -> complex:
    """Return ``H_(h,k)(s)`` in its stable centered factorization."""
    _validate_h_k(h, k)
    value = complex(s)
    if value == 0.0:
        raise ZeroDivisionError("the primitive multiplier has a pole at s=0")
    return cmath.exp(-k * h * value / 2.0) * q_h(value, h) ** k / value


def coboundary_multiplier(s: complex, h: float, k: int) -> complex:
    """Return the exact compact-coboundary multiplier ``G_(h,k)(s)``."""
    _validate_h_k(h, k)
    value = complex(s)
    if value == 0.0:
        return complex(k * h)
    return (
        2.0
        * cmath.sinh(k * h * value / 2.0)
        * q_h(value, h) ** k
        / value
    )


def critical_line_contraction(h: float, k: int, gamma: float) -> float:
    """Return the universal factor ``|sinc(h*gamma/2)|^k``."""
    _validate_h_k(h, k)
    if not math.isfinite(gamma):
        raise ValueError("gamma must be finite")
    argument = h * gamma / 2.0
    sinc = 1.0 if argument == 0.0 else math.sin(argument) / argument
    return abs(sinc) ** k


def critical_coboundary_bound(h: float, k: int, gamma: float) -> float:
    """Return the bound ``2/|gamma| * |sinc(h*gamma/2)|^k``."""
    if gamma == 0.0:
        raise ValueError("the critical-line bound requires gamma != 0")
    return 2.0 * critical_line_contraction(h, k, gamma) / abs(gamma)


def off_line_net_log_amplitude(
    delta: float,
    gamma: float,
    h: float,
    k: int,
    basepoint: float,
) -> float:
    """Return ``delta*R + k*log|q_h(delta+i*gamma)|``.

    This is the core exponential balance after centering the repeated
    averaging step.  Fixed factors and the outer coboundary factor contribute
    only ``O_(h,s)(k)`` and do not change survival when ``k=o(R)``.
    """
    _validate_h_k(h, k)
    if not all(math.isfinite(value) for value in (delta, gamma, basepoint)):
        raise ValueError("delta, gamma, and basepoint must be finite")
    modulus = abs(q_h(complex(delta, gamma), h))
    if modulus == 0.0:
        return -math.inf
    return delta * basepoint + k * math.log(modulus)


def exact_mode_log_amplitude(
    delta: float,
    gamma: float,
    h: float,
    k: int,
    basepoint: float,
) -> float:
    """Return ``log|exp(sR) G_(h,k)(s)|`` for ``s=delta+i*gamma``."""
    if not all(math.isfinite(value) for value in (delta, gamma, basepoint)):
        raise ValueError("delta, gamma, and basepoint must be finite")
    multiplier = abs(coboundary_multiplier(complex(delta, gamma), h, k))
    if multiplier == 0.0:
        return -math.inf
    return delta * basepoint + math.log(multiplier)


def support_log_width(h: float, k: int) -> float:
    """Return the total logarithmic support width ``k*h``."""
    _validate_h_k(h, k)
    return k * h


def support_ratio(h: float, k: int) -> float:
    """Return the multiplicative support ratio ``exp(k*h)``."""
    width = support_log_width(h, k)
    try:
        return math.exp(width)
    except OverflowError:
        return math.inf


def bspline_cdf(t: float, h: float, k: int) -> float:
    """Return ``P(U_1+...+U_k < t)`` for ``U_j`` uniform on ``[0,h]``.

    This inclusion-exclusion evaluator is intended only for modest ``k``.
    The symmetry reduction avoids the worst right-tail cancellation, but it
    is not a high-order interval implementation.
    """
    _validate_h_k(h, k)
    if not math.isfinite(t):
        raise ValueError("t must be finite")
    width = k * h
    if t <= 0.0:
        return 0.0
    if t >= width:
        return 1.0
    if t > width / 2.0:
        return 1.0 - bspline_cdf(width - t, h, k)

    normalized = t / h
    last = min(k, math.floor(normalized))
    factorial = math.factorial(k)
    terms = (
        (-1.0 if index % 2 else 1.0)
        * math.comb(k, index)
        * (normalized - index) ** k
        / factorial
        for index in range(last + 1)
    )
    value = math.fsum(terms)
    return min(1.0, max(0.0, value))


def compact_window(t: float, h: float, k: int) -> float:
    """Return ``Phi_(h,k)(t+k*h)-Phi_(h,k)(t)``."""
    width = support_log_width(h, k)
    return bspline_cdf(t + width, h, k) - bspline_cdf(t, h, k)


def _von_mangoldt_up_to(limit: int) -> list[float]:
    if limit < 2:
        return [0.0] * (limit + 1)
    prime = bytearray(b"\x01") * (limit + 1)
    prime[0:2] = b"\x00\x00"
    for value in range(2, math.isqrt(limit) + 1):
        if not prime[value]:
            continue
        start = value * value
        count = (limit - start) // value + 1
        prime[start : limit + 1 : value] = b"\x00" * count

    mangoldt = [0.0] * (limit + 1)
    for value in range(2, limit + 1):
        if not prime[value]:
            continue
        log_prime = math.log(value)
        power = value
        while power <= limit:
            mangoldt[power] = log_prime
            if power > limit // value:
                break
            power *= value
    return mangoldt


def pole_coefficient(h: float, k: int) -> float:
    """Return ``H_(h,k)(1/2)`` for the primitive pole subtraction."""
    _validate_h_k(h, k)
    one_step = -math.expm1(-h / 2.0) / (h / 2.0)
    return 2.0 * one_step**k


@dataclass(frozen=True)
class CoboundaryCheck:
    basepoint: float
    h: float
    k: int
    width: float
    limit: int
    lower_primitive: float
    upper_primitive: float
    difference: float
    compact_prime_sum: float
    pole_difference: float
    compact_evaluation: float
    closure_error: float


def direct_von_mangoldt_coboundary(
    basepoint: float = 5.0,
    h: float = 0.2,
    k: int = 4,
) -> CoboundaryCheck:
    """Directly verify ``C(R+k*h)-C(R)`` on a modest prime-power range."""
    _validate_h_k(h, k)
    if not math.isfinite(basepoint) or basepoint <= 0.0:
        raise ValueError("basepoint must be finite and positive")
    width = k * h
    upper_point = basepoint + width
    if upper_point > 14.0:
        raise ValueError("the lightweight direct check requires R+k*h <= 14")
    limit = math.ceil(math.exp(upper_point))
    mangoldt = _von_mangoldt_up_to(limit)

    lower_terms: list[float] = []
    upper_terms: list[float] = []
    compact_terms: list[float] = []
    for n in range(2, limit + 1):
        lambda_n = mangoldt[n]
        if lambda_n == 0.0:
            continue
        normalized = lambda_n / math.sqrt(n)
        lower_weight = bspline_cdf(basepoint - math.log(n), h, k)
        upper_weight = bspline_cdf(upper_point - math.log(n), h, k)
        lower_terms.append(normalized * lower_weight)
        upper_terms.append(normalized * upper_weight)
        compact_terms.append(normalized * (upper_weight - lower_weight))

    coefficient = pole_coefficient(h, k)
    lower_primitive = math.fsum(lower_terms) - coefficient * math.exp(
        basepoint / 2.0
    )
    upper_primitive = math.fsum(upper_terms) - coefficient * math.exp(
        upper_point / 2.0
    )
    difference = upper_primitive - lower_primitive
    compact_prime_sum = math.fsum(compact_terms)
    pole_difference = coefficient * (
        math.exp(upper_point / 2.0) - math.exp(basepoint / 2.0)
    )
    compact_evaluation = compact_prime_sum - pole_difference
    closure_error = difference - compact_evaluation
    tolerance = 5.0e-13 * max(
        1.0, abs(compact_prime_sum), abs(pole_difference)
    )
    if abs(closure_error) > tolerance:
        raise RuntimeError(
            "direct coboundary identity failed: "
            f"error={closure_error!r}, tolerance={tolerance!r}"
        )

    return CoboundaryCheck(
        basepoint=basepoint,
        h=h,
        k=k,
        width=width,
        limit=limit,
        lower_primitive=lower_primitive,
        upper_primitive=upper_primitive,
        difference=difference,
        compact_prime_sum=compact_prime_sum,
        pole_difference=pole_difference,
        compact_evaluation=compact_evaluation,
        closure_error=closure_error,
    )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h", type=float, default=0.1)
    parser.add_argument("--k", type=int, default=32)
    parser.add_argument("--gamma", type=float, default=FIRST_ZERO_ORDINATE)
    parser.add_argument("--delta", type=float, default=0.1)
    parser.add_argument("--basepoint", type=float, default=1000.0)
    parser.add_argument("--direct-basepoint", type=float, default=5.0)
    parser.add_argument("--skip-direct", action="store_true")
    args = parser.parse_args(argv)

    node = complex(args.delta, args.gamma)
    print(f"q_h(s)={q_h(node, args.h)!r}")
    print(f"G_hk(s)={coboundary_multiplier(node, args.h, args.k)!r}")
    print(
        "critical_contraction="
        f"{critical_line_contraction(args.h, args.k, args.gamma):.16g}"
    )
    print(
        "off_line_core_log_amplitude="
        f"{off_line_net_log_amplitude(args.delta, args.gamma, args.h, args.k, args.basepoint):.16g}"
    )
    print(
        "off_line_exact_log_amplitude="
        f"{exact_mode_log_amplitude(args.delta, args.gamma, args.h, args.k, args.basepoint):.16g}"
    )
    print(f"support_log_width={support_log_width(args.h, args.k):.16g}")
    print(f"support_ratio={support_ratio(args.h, args.k):.16g}")

    if not args.skip_direct:
        direct_h = min(args.h, 0.5)
        direct_k = min(args.k, 8)
        check = direct_von_mangoldt_coboundary(
            basepoint=args.direct_basepoint,
            h=direct_h,
            k=direct_k,
        )
        print(
            f"direct_h={direct_h:.16g} direct_k={direct_k} "
            f"direct_coboundary={check.difference:.16g} "
            f"closure_error={check.closure_error:.3e} limit={check.limit}"
        )

    print("interpretation=universal low-pass cooling; no prime-side bound proved")
    print("block_schedule_converse=UNPROVED")


if __name__ == "__main__":
    main()
