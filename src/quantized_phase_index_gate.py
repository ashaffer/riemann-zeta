"""Exact and lightweight checks for the quantized phase/index branch.

The module separates three logically different facts.

* A symmetric off-critical quartet is invisible on the real critical-line
  phase, and becomes compact-open small when it is moved to large height.
* The shifted divisor phase detects that quartet by an integer winding jump.
* Natural finite-prime Euler realizations do not carry that integer through
  the RH-relevant limit topology.

The analytic convergence and divergence proofs are recorded in
``results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md``.  The finite sums here are
regression fixtures, not numerical evidence for RH.
"""
from __future__ import annotations

from fractions import Fraction
from math import atan
from typing import Iterable, List


def quartet_factor(x: complex | float | Fraction,
                   gamma: float | Fraction,
                   delta: float | Fraction):
    """The even quartet polynomial with roots ``+-gamma +- i delta``."""
    return (((x - gamma) ** 2 + delta ** 2)
            * ((x + gamma) ** 2 + delta ** 2))


def quartet_expansion(x: complex | float | Fraction,
                      gamma: float | Fraction,
                      delta: float | Fraction):
    """Expanded form used by the remote-quartet continuity estimate."""
    scale = gamma ** 2 + delta ** 2
    return (scale ** 2 + 2 * (delta ** 2 - gamma ** 2) * x ** 2
            + x ** 4)


def normalized_quartet_deviation_bound(radius: float,
                                        gamma: float,
                                        delta: float) -> float:
    """Uniform bound for ``|Q(z)/Q(0)-1|`` on ``|z| <= radius``."""
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    scale = gamma * gamma + delta * delta
    if scale == 0:
        raise ValueError("the quartet must be nontrivial")
    return 2 * radius * radius / scale + radius ** 4 / scale ** 2


def shifted_strip_winding(a: float | Fraction,
                           root_imaginary_parts: Iterable[float | Fraction]) -> int:
    """Winding of ``P(x-ia)/P(x+ia)`` in the standard orientation.

    Each root strictly inside ``|Im(lambda)| < a`` contributes one.  A root
    on a boundary line makes the quotient singular, so the winding is not
    defined there.
    """
    if a <= 0:
        raise ValueError("a must be positive")
    count = 0
    for ordinate in root_imaginary_parts:
        magnitude = abs(ordinate)
        if magnitude == a:
            raise ValueError("a root lies on the shifted boundary")
        if magnitude < a:
            count += 1
    return count


def quartet_shifted_winding(a: float | Fraction,
                             delta: float | Fraction) -> int:
    """The shifted-phase winding is zero before, and four after, a quartet."""
    if delta <= 0:
        raise ValueError("delta must be positive")
    return shifted_strip_winding(a, (delta, delta, -delta, -delta))


def literal_local_k1_degree(a: float | Fraction) -> int:
    """Degree of the literal local shifted Euler quotient on one prime circle.

    The circle coordinate has its standard counterclockwise orientation.  In
    the relevant range ``0 < a < 1/2``, both affine factors have their zeros
    outside the unit disk and the degree is zero.  The transition at ``1/2``
    is the Euler-product pole boundary, not the critical-line-zero defect.
    """
    if a <= 0:
        raise ValueError("a must be positive")
    half = Fraction(1, 2)
    if a == half:
        raise ValueError("the local loop passes through zero at a=1/2")
    return 0 if a < half else 1


def right_shift_local_phase(p: int, a: float, z: complex,
                            homotopy_time: float = 1.0) -> complex:
    """A unit local Euler phase and its contraction to the constant loop.

    Here ``|z|=1``, ``sigma=1/2+a``, and the radius is
    ``homotopy_time * p**(-sigma)``.  For ``0 <= homotopy_time <= 1`` the
    denominator cannot vanish and time zero is the constant phase one.
    """
    if p < 2 or a <= 0:
        raise ValueError("expected p >= 2 and a > 0")
    if not 0 <= homotopy_time <= 1:
        raise ValueError("homotopy_time must lie in [0,1]")
    if abs(abs(z) - 1.0) > 1e-12:
        raise ValueError("z must lie on the unit circle")
    radius = homotopy_time * p ** (-(0.5 + a))
    return (1 - radius * z.conjugate()) / (1 - radius * z)


def primes_up_to(limit: int) -> List[int]:
    """Small sieve used only by bounded regression checks."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, int(limit ** 0.5) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            sieve[start:limit + 1:candidate] = b"\x00" * (
                (limit - start) // candidate + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def literal_log_b2_partial_variance(a: float, prime_limit: int,
                                    max_prime_power: int = 8) -> float:
    """Partial Bohr-B2 norm square of the literal shifted Euler logarithm."""
    if not 0 < a < 0.5:
        raise ValueError("the literal gate is stated for 0 < a < 1/2")
    if max_prime_power < 1:
        raise ValueError("max_prime_power must be positive")
    total = 0.0
    for p in primes_up_to(prime_limit):
        outer = p ** (-0.5 + a)
        inner = p ** (-0.5 - a)
        for power in range(1, max_prime_power + 1):
            coefficient = (outer ** power - inner ** power) / power
            total += coefficient * coefficient
    return total


def literal_quotient_b2_norm_squared(a: float, prime_limit: int) -> float:
    """Exact finite-torus B2 norm square of the literal Euler quotient.

    The convention is

    ``prod_p (1-p**(-1/2+a) z_p)/(1-p**(-1/2-a) z_p)``.

    Haar orthogonality gives the displayed local factor exactly, and prime
    independence multiplies the factors.  The product diverges as the cutoff
    grows for every ``0<a<1/2``; this is stronger than failure of its chosen
    logarithm to converge.
    """
    if not 0 < a < 0.5:
        raise ValueError("the literal gate is stated for 0 < a < 1/2")
    total = 1.0
    for p in primes_up_to(prime_limit):
        outer = p ** (-0.5 + a)
        inner = p ** (-0.5 - a)
        total *= 1 + (outer - inner) ** 2 / (1 - inner * inner)
    return total


def right_phase_log_b2_partial_variance(a: float, prime_limit: int,
                                        max_prime_power: int = 8) -> float:
    """Partial Bohr-B2 norm square of the normalized unit-phase logarithm."""
    if a <= 0:
        raise ValueError("a must be positive")
    if max_prime_power < 1:
        raise ValueError("max_prime_power must be positive")
    sigma = 0.5 + a
    total = 0.0
    for p in primes_up_to(prime_limit):
        radius = p ** (-sigma)
        for power in range(1, max_prime_power + 1):
            # Equal positive- and negative-frequency Fourier coefficients.
            total += 2 * radius ** (2 * power) / (power * power)
    return total


def right_phase_tail_b2_distance_squared(a: float, lower_prime: int,
                                         upper_prime: int) -> float:
    """Exact B2 distance square contributed by a finite independent tail."""
    if a <= 0:
        raise ValueError("a must be positive")
    if lower_prime < 0 or upper_prime < lower_prime:
        raise ValueError("expected 0 <= lower_prime <= upper_prime")
    sigma = 0.5 + a
    tail_mean = 1.0
    for p in primes_up_to(upper_prime):
        if p > lower_prime:
            tail_mean *= 1 - p ** (-2 * sigma)
    return 2 - 2 * tail_mean


def aligned_phase_angle_capacity(a: float, prime_limit: int) -> float:
    """A lower bound on the aligned finite-prime phase-log excursion.

    Setting every independent prime coordinate to ``i`` gives local angle
    ``2 atan(p**(-1/2-a))``.  Kronecker density approximates this simultaneous
    alignment along the real translation orbit.  The sum diverges exactly
    through the non-uniform range ``a <= 1/2``.
    """
    if a <= 0:
        raise ValueError("a must be positive")
    sigma = 0.5 + a
    return sum(2 * atan(p ** (-sigma)) for p in primes_up_to(prime_limit))


def main() -> None:
    gamma = Fraction(7, 3)
    delta = Fraction(2, 5)
    x = Fraction(11, 7)
    print("quartet_expansion_exact", quartet_factor(x, gamma, delta)
          == quartet_expansion(x, gamma, delta))
    print("quartet_real_value_positive", quartet_factor(x, gamma, delta) > 0)
    print("winding_before_after", quartet_shifted_winding(delta / 2, delta),
          quartet_shifted_winding(2 * delta, delta))
    print("finite_prime_k1_relevant_range",
          literal_local_k1_degree(Fraction(1, 4)))
    phase = right_shift_local_phase(3, 0.25, 1j)
    print("right_shift_local_phase_norm", abs(phase))


if __name__ == "__main__":
    main()
