#!/usr/bin/env python3
"""Exact formulas and finite diagnostics for the shifted-Psi/ramp bridge.

For ``1/2 < alpha < 1`` put ``kappa = 1-alpha``.  This module evaluates

    B_alpha(x) = sum_{n<=x} Lambda(n)n^(-alpha)
                   [2(n/x)^kappa-1]
                 -(1-x^(-kappa))/kappa

and the pole-centred triangular ramp occurring in Suzuki's shifted
``Psi_omega``, where ``omega=alpha-1/2``.  The formulas are unconditional;
finite scans are diagnostics, not evidence for an asymptotic sign theorem.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from typing import Iterable

import mpmath as mp


def von_mangoldt_table(limit: int, *, prime_only: bool = False) -> list[float]:
    """Return ``Lambda(n)`` for ``0 <= n <= limit`` using a byte sieve."""
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    values = [0.0] * (limit + 1)
    if limit < 2:
        return values
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for candidate in range(2, math.isqrt(limit) + 1):
        if is_prime[candidate]:
            start = candidate * candidate
            is_prime[start : limit + 1 : candidate] = b"\x00" * (
                (limit - start) // candidate + 1
            )
    for prime in range(2, limit + 1):
        if not is_prime[prime]:
            continue
        logarithm = math.log(prime)
        values[prime] = logarithm
        if prime_only:
            continue
        power = prime * prime
        while power <= limit:
            values[power] = logarithm
            if power > limit // prime:
                break
            power *= prime
    return values


def _check_alpha(alpha: float | mp.mpf) -> None:
    if not mp.mpf("0.5") < alpha < 1:
        raise ValueError("alpha must lie strictly between 1/2 and 1")


def shifted_bounded_ramp(
    alpha: float,
    x: float,
    mangoldt: list[float],
) -> float:
    """Evaluate the symmetric shifted bounded ramp at ``x``.

    ``mangoldt`` must contain all desired atoms through ``floor(x)``.  It may
    be either the full von Mangoldt table or its prime-only version.
    """
    _check_alpha(alpha)
    if x < 1:
        raise ValueError("x must be at least one")
    maximum = math.floor(x)
    if maximum >= len(mangoldt):
        raise ValueError("mangoldt table is too short")
    kappa = 1.0 - alpha
    total = 0.0
    for integer in range(2, maximum + 1):
        weight = mangoldt[integer]
        if weight:
            ratio = integer / x
            total += weight * integer ** (-alpha) * (2.0 * ratio**kappa - 1.0)
    return total - (1.0 - x ** (-kappa)) / kappa


def two_scale_pole_killing_ramp(
    alpha: float,
    decay: float,
    x: float,
    mangoldt: list[float],
) -> float:
    r"""Evaluate the general normalized two-scale pole-killing ramp.

    Put ``kappa=1-alpha`` and ``r=decay``.  The unique kernel of the form
    ``a*y**r+b`` which is one at ``y=1`` and whose Laplace multiplier
    vanishes at the pole frequency ``q=kappa`` is

        w(y) = (r+kappa)/r * y**r - kappa/r.

    The subtracted continuum is its integral against the PNT density.  The
    symmetric ramp :func:`shifted_bounded_ramp` is the case ``r=kappa``.
    """
    _check_alpha(alpha)
    if decay <= 0:
        raise ValueError("decay must be positive")
    if x < 1:
        raise ValueError("x must be at least one")
    maximum = math.floor(x)
    if maximum >= len(mangoldt):
        raise ValueError("mangoldt table is too short")
    kappa = 1.0 - alpha
    total = 0.0
    for integer in range(2, maximum + 1):
        atom = mangoldt[integer]
        if atom:
            ratio = integer / x
            kernel = (decay + kappa) / decay * ratio**decay - kappa / decay
            total += atom * integer ** (-alpha) * kernel
    return total - (1.0 - x ** (-decay)) / decay


def shifted_bounded_ramp_from_moments(
    alpha: float,
    x: float,
    lower_moment: float,
    upper_moment: float,
) -> float:
    """Evaluate the ramp from its two cumulative weighted moments.

    Here ``lower_moment=sum Lambda(n)n^(-alpha)`` and
    ``upper_moment=sum Lambda(n)n^(1-2alpha)`` through ``n<=x``.
    """
    _check_alpha(alpha)
    kappa = 1.0 - alpha
    return (
        2.0 * x ** (-kappa) * upper_moment
        - lower_moment
        - (1.0 - x ** (-kappa)) / kappa
    )


def weighted_mertens_error(x: float, mangoldt: list[float]) -> float:
    """Return ``sum_{n<=x} Lambda(n)/n-log(x)``."""
    if x < 1:
        raise ValueError("x must be at least one")
    maximum = math.floor(x)
    if maximum >= len(mangoldt):
        raise ValueError("mangoldt table is too short")
    return sum(mangoldt[n] / n for n in range(2, maximum + 1)) - math.log(x)


def centered_triangular_ramp(
    alpha: mp.mpf,
    t: mp.mpf,
    atoms: Iterable[tuple[int, mp.mpf]],
) -> mp.mpf:
    """Return Suzuki's weighted triangular prime ramp minus its pole ramp."""
    _check_alpha(alpha)
    kappa = 1 - alpha
    cutoff = mp.e**t
    prime_ramp = mp.fsum(
        weight * mp.power(integer, -alpha) * (t - mp.log(integer))
        for integer, weight in atoms
        if integer <= cutoff
    )
    pole_ramp = (mp.e ** (kappa * t) - 1 - kappa * t) / kappa**2
    return prime_ramp - pole_ramp


def completed_archimedean_ramp(alpha: mp.mpf, t: mp.mpf) -> mp.mpf:
    """Return the explicit non-zeta-pole completion ``H_alpha(t)``."""
    _check_alpha(alpha)
    c_infinity = (
        1 / alpha - mp.log(mp.pi) / 2 + mp.digamma(alpha / 2) / 2
    )
    c_infinity_prime = -1 / alpha**2 + mp.polygamma(1, alpha / 2) / 4
    tail = mp.e ** (-alpha * t) * (
        1 / alpha**2
        - mp.lerchphi(mp.e ** (-2 * t), 2, alpha / 2) / 4
    )
    return c_infinity * t + c_infinity_prime + tail


def shifted_suzuki_psi(
    alpha: mp.mpf,
    t: mp.mpf,
    atoms: Iterable[tuple[int, mp.mpf]],
) -> mp.mpf:
    """Evaluate ``Psi_(alpha-1/2)(t)=H_alpha(t)-J_alpha(t)``."""
    return completed_archimedean_ramp(alpha, t) - centered_triangular_ramp(
        alpha, t, atoms
    )


def inverse_bridge_kernel(kappa: mp.mpf, lag: mp.mpf) -> mp.mpf:
    """Green kernel taking the shifted bounded ramp to the triangular ramp."""
    if not 0 < kappa < mp.mpf("0.5"):
        raise ValueError("kappa must lie strictly between 0 and 1/2")
    if lag < 0:
        return mp.mpf(0)
    return 2 * mp.e ** (kappa * lag) - 1


def exact_bridge_multiplier_product(q: Fraction, kappa: Fraction) -> Fraction:
    """Return the exact product of the ramp and inverse-bridge multipliers."""
    ramp = (q - kappa) / (q * (q + kappa))
    inverse = (q + kappa) / (q * (q - kappa))
    return ramp * inverse


def exact_general_bridge_multiplier_product(
    q: Fraction, kappa: Fraction, decay: Fraction
) -> Fraction:
    """Return the general ramp/Green multiplier product exactly."""
    ramp = (q - kappa) / (q * (q + decay))
    inverse = (q + decay) / (q * (q - kappa))
    return ramp * inverse


def exact_mertens_deformation_multiplier_product(
    q: Fraction, kappa: Fraction
) -> Fraction:
    """Check the exact multiplier connecting ``B_kappa`` to ``B_0``.

    If ``f(t)=exp(kappa*t)B_0(t)``, then

        B_kappa = [I + kappa I_0 - 4 kappa (exp(-kappa .) *)] f.
    """
    direct = (q - kappa) ** 2 / (q * (q + kappa))
    decomposed = 1 + kappa / q - 4 * kappa / (q + kappa)
    return direct - decomposed


def exact_general_mertens_deformation_partial_fractions(
    q: Fraction, kappa: Fraction, decay: Fraction
) -> Fraction:
    """Return zero iff the general Mertens deformation identity is exact.

    For ``f(t)=exp(kappa*t)B_0(t)``, the general ramp has multiplier

        (q-kappa)^2/[q(q+decay)]
          = 1 + kappa^2/(decay*q)
              - (decay+kappa)^2/[decay*(q+decay)].
    """
    direct = (q - kappa) ** 2 / (q * (q + decay))
    decomposed = (
        1
        + kappa**2 / (decay * q)
        - (decay + kappa) ** 2 / (decay * (q + decay))
    )
    return direct - decomposed


def euler_boundary_profile(c: float | mp.mpf, ratio: float | mp.mpf = 1) -> mp.mpf:
    r"""Leading ``kappa*log(x)=c`` profile for ``decay=ratio*kappa``.

    If ``ratio=a>0``, the profile is

        gamma/a * [1-(a+1)exp(-a*c)].
    """
    c_value = mp.mpf(c)
    a_value = mp.mpf(ratio)
    if c_value <= 0 or a_value <= 0:
        raise ValueError("c and ratio must be positive")
    return mp.euler / a_value * (
        1 - (a_value + 1) * mp.e ** (-a_value * c_value)
    )


def weighted_mertens_integral_constant() -> mp.mpf:
    r"""Return ``integral_0^infinity (B_0(t)+gamma) dt``.

    With the standard Stieltjes convention this is
    ``gamma**2 + 2*gamma_1 = F'(1)``.
    """
    return mp.euler**2 + 2 * mp.stieltjes(1)


def euler_boundary_profile_two_term(
    kappa: float | mp.mpf,
    c: float | mp.mpf,
    ratio: float | mp.mpf = 1,
) -> mp.mpf:
    r"""Return the first two terms of the Euler boundary-layer expansion."""
    kappa_value = mp.mpf(kappa)
    c_value = mp.mpf(c)
    a_value = mp.mpf(ratio)
    if kappa_value <= 0:
        raise ValueError("kappa must be positive")
    leading = euler_boundary_profile(c_value, a_value)
    coefficient = (
        (a_value + 1) ** 2 * mp.e ** (-a_value * c_value) - 1
    ) / a_value
    return leading - kappa_value * coefficient * weighted_mertens_integral_constant()


def euler_boundary_crossing(
    kappa: float | mp.mpf, ratio: float | mp.mpf = 1
) -> mp.mpf:
    r"""Two-term prediction for the zero in ``c=kappa*log(x)``."""
    kappa_value = mp.mpf(kappa)
    a_value = mp.mpf(ratio)
    if kappa_value <= 0 or a_value <= 0:
        raise ValueError("kappa and ratio must be positive")
    return (
        mp.log(a_value + 1) / a_value
        + kappa_value * weighted_mertens_integral_constant() / mp.euler
    )


def scan_checkpoints(
    limit: int,
    deltas: list[float],
    checkpoints: list[int],
    *,
    prime_only: bool = False,
) -> dict[str, object]:
    """Evaluate shifted ramps incrementally at selected integer cutoffs."""
    if not checkpoints or min(checkpoints) < 2 or max(checkpoints) > limit:
        raise ValueError("checkpoints must lie between 2 and limit")
    table = von_mangoldt_table(limit, prime_only=prime_only)
    requested = set(checkpoints)
    moments = {
        delta: {"lower": 0.0, "upper": 0.0, "values": {}}
        for delta in deltas
    }
    mertens = 0.0
    mertens_values: dict[str, float] = {}
    for integer in range(2, limit + 1):
        weight = table[integer]
        if weight:
            mertens += weight / integer
            for delta, state in moments.items():
                alpha = 1.0 - delta
                state["lower"] += weight * integer ** (-alpha)
                state["upper"] += weight * integer ** (1.0 - 2.0 * alpha)
        if integer in requested:
            mertens_values[str(integer)] = mertens - math.log(integer)
            for delta, state in moments.items():
                state["values"][str(integer)] = shifted_bounded_ramp_from_moments(
                    1.0 - delta,
                    float(integer),
                    state["lower"],
                    state["upper"],
                )
    return {
        "evidence": "FLOATING_POINT_DIAGNOSTIC",
        "prime_only": prime_only,
        "limit": limit,
        "checkpoints": checkpoints,
        "weighted_mertens": mertens_values,
        "shifted_ramps": {
            str(delta): state["values"] for delta, state in moments.items()
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument(
        "--deltas", type=float, nargs="+", default=[0.25, 0.1, 0.01, 0.001]
    )
    parser.add_argument(
        "--checkpoints",
        type=int,
        nargs="+",
        default=[10, 100, 1_000, 10_000, 100_000, 1_000_000],
    )
    parser.add_argument("--prime-only", action="store_true")
    args = parser.parse_args()
    payload = scan_checkpoints(
        args.limit,
        args.deltas,
        args.checkpoints,
        prime_only=args.prime_only,
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
