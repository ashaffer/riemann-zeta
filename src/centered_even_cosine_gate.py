"""Exact diagnostics for the centered-even cosine one-square gate.

The centered parity carrier has coefficients proportional to
``k / (k**2 + q**2)`` before endpoint projection.  On the two-sided sharp
lattice its synthesis is the Fourier transform of the odd truncated-sinh
packet.  This module records the resulting autocorrelation identity, its
two-abscissa prime-polynomial collapse, and an Arb evaluator for the
evenized completed multiplier.

None of the routines asserts the missing uniform one-square sign.
"""

from __future__ import annotations

from fractions import Fraction
import math
from typing import Any, Sequence

import numpy as np

from signed_garding_failfast import prime_powers

try:  # The rigorous certificate is optional on installations without FLINT.
    from flint import acb, arb, ctx
except ImportError:  # pragma: no cover
    acb = arb = ctx = None


def centered_carrier_coefficients(
    half_count: int,
    length: float,
    alpha: float,
) -> np.ndarray:
    """Return the unnormalized centered full-carrier Cauchy coefficients.

    These are the selected odd row after removing its harmless common
    scalar.  Endpoint projection, when desired, is a separate linear step.
    """

    if half_count < 1:
        raise ValueError("half_count must be positive")
    if length <= 0 or alpha <= 0:
        raise ValueError("length and alpha must be positive")
    spacing = 2.0 * math.pi / length
    q = alpha / spacing
    indices = np.arange(-half_count, half_count + 1, dtype=float)
    return indices / (indices * indices + q * q)


def infinite_centered_synthesis(
    scaled_frequency: np.ndarray | float,
    q: float,
    spacing: float = 1.0,
) -> np.ndarray:
    """Closed synthesis of ``k/(k^2+q^2)`` on the two-sided lattice.

    If ``x=(t-gamma)/spacing``, the sharp synthesis is

    ``(2*pi/spacing) * (x*cos(pi*x)-q*coth(pi*q)*sin(pi*x))/(x^2+q^2)``.

    Removable values at ``x=+/- i*q`` are irrelevant on the real line.
    """

    if q <= 0 or spacing <= 0:
        raise ValueError("q and spacing must be positive")
    x = np.asarray(scaled_frequency, dtype=float)
    coth = 1.0 / math.tanh(math.pi * q)
    numerator = x * np.cos(math.pi * x) - q * coth * np.sin(math.pi * x)
    return (2.0 * math.pi / spacing) * numerator / (x * x + q * q)


def sinh_tent_autocorrelation(
    length: float,
    alpha: float,
    shift: np.ndarray | float,
    *,
    normalize_packet: bool = False,
) -> np.ndarray:
    """Autocorrelation of ``sinh(alpha*x) 1_[|x|<=length/2]``.

    For ``0 <= u <= length`` the exact value is

    ``sinh(alpha*(length-u))/(2*alpha)
       -(length-u)*cosh(alpha*u)/2``.

    The answer is even and vanishes outside ``[-length,length]``.  With
    ``normalize_packet=True`` it is divided by ``sinh(alpha*length/2)^2``.
    """

    if length <= 0 or alpha <= 0:
        raise ValueError("length and alpha must be positive")
    u = np.abs(np.asarray(shift, dtype=float))
    inside = np.maximum(length - u, 0.0)
    answer = (
        np.sinh(alpha * inside) / (2.0 * alpha)
        - inside * np.cosh(alpha * u) / 2.0
    )
    answer = np.where(u <= length, answer, 0.0)
    if normalize_packet:
        answer = answer / math.sinh(alpha * length / 2.0) ** 2
    return answer


def sinh_tent_prime_correlation(
    cutoff: int,
    gamma: float,
    alpha: float,
) -> tuple[float, float]:
    """Evaluate the same prime correlation in two exactly equal ways.

    The direct value is

    ``sum Lambda(n)/sqrt(n) C(log n) cos(gamma log n)``.

    Expanding the sinh-tent ``C`` collapses this to the real part of one
    linear combination of the truncated logarithmic-derivative polynomial
    and its ``sigma`` derivative at ``1/2 +/- alpha + i*gamma``.  The second
    returned value uses that two-abscissa formula.
    """

    if cutoff < 2 or alpha <= 0:
        raise ValueError("cutoff must be at least two and alpha positive")
    length = math.log(cutoff)
    logs, weights = prime_powers(cutoff)
    phases = np.cos(gamma * logs)
    direct = float(np.dot(
        weights * phases,
        sinh_tent_autocorrelation(length, alpha, logs),
    ))

    plus = weights * np.exp(-alpha * logs) * phases
    minus = weights * np.exp(alpha * logs) * phases
    p_plus = float(np.sum(plus))
    p_minus = float(np.sum(minus))
    d_plus = float(np.dot(length - logs, plus))
    d_minus = float(np.dot(length - logs, minus))
    collapsed = 0.25 * (
        math.exp(alpha * length) * p_plus / alpha
        - math.exp(-alpha * length) * p_minus / alpha
        - d_plus
        - d_minus
    )
    return direct, collapsed


def _primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


def rigorous_evenized_shifted_multiplier(
    cutoff: int,
    first_height: Fraction | int,
    second_height: Fraction | int,
    *,
    decimal_digits: int = 80,
) -> Any:
    """Return an Arb enclosure of ``1+(nu(t1)+nu(t2))/2``.

    Here ``nu`` is the exact completed multiplier used by the conditional
    Pick report,

    ``nu(t)=(Re psi(1/4+it/2)-log pi)/(2*pi)
            +1/(2*pi*(1/4+t^2))-(1/pi) Re E_X(t)``,

    with all prime powers through the integer cutoff and the matching
    continuum integral retained.  A strictly negative returned ball is a
    rigorous counterexample to pointwise evenized Herglotz positivity, not
    to positivity of the compressed one-square.
    """

    if arb is None:
        raise RuntimeError("python-flint is required for the interval replay")
    if cutoff < 2:
        raise ValueError("cutoff must be at least two")
    if decimal_digits < 30:
        raise ValueError("at least 30 decimal digits are required")

    def as_arb(value: Fraction | int) -> Any:
        fraction = value if isinstance(value, Fraction) else Fraction(value)
        return arb(fraction.numerator) / fraction.denominator

    old_digits = ctx.dps
    ctx.dps = decimal_digits
    try:
        pi = arb.pi()
        log_cutoff = arb(cutoff).log()
        primes = _primes_up_to(cutoff)

        def multiplier(height: Fraction | int) -> Any:
            t = as_arb(height)
            complex_s = acb(arb(1) / 2, t)
            prime_sum = acb(0)
            for prime in primes:
                log_prime = arb(prime).log()
                power = prime
                while power <= cutoff:
                    log_power = arb(power).log()
                    phase = acb(0, t * log_power).exp()
                    prime_sum += phase * log_prime / arb(power).sqrt()
                    if power > cutoff // prime:
                        break
                    power *= prime
            continuum = ((complex_s * log_cutoff).exp() - 1) / complex_s
            discrepancy = prime_sum - continuum
            gamma_part = (
                acb(arb(1) / 4, t / 2).digamma().real - pi.log()
            ) / (2 * pi)
            rational_part = 1 / (2 * pi * (arb(1) / 4 + t * t))
            return gamma_part + rational_part - discrepancy.real / pi

        return 1 + (multiplier(first_height) + multiplier(second_height)) / 2
    finally:
        ctx.dps = old_digits


def certified_herglotz_counterexample(decimal_digits: int = 80) -> Any:
    """The fixed rational ``T=4096`` pointwise countercertificate."""

    return rigorous_evenized_shifted_multiplier(
        4096,
        Fraction(50388992, 10000),
        Fraction(72491008, 10000),
        decimal_digits=decimal_digits,
    )


def jensen_zero_count_bound(exponential_type: float, radius: float) -> float:
    """Uniform Jensen bound for a normalized characteristic function.

    If a probability measure is supported in ``[-H,H]``, its characteristic
    function has at most this many zeros (with multiplicity) in ``|z|<=R``.
    The proof applies Jensen on ``|z|=2R`` and uses
    ``|phi(z)|<=exp(H*abs(Im z))``.
    """

    if exponential_type < 0 or radius <= 0:
        raise ValueError("type must be nonnegative and radius positive")
    return 4.0 * exponential_type * radius / (math.pi * math.log(2.0))

