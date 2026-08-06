#!/usr/bin/env python3
"""Certified fail-fast test for actual-prime reflection positivity.

For the critically centered actual-prime measure

    E_p = sum_p log(p)/sqrt(p) delta_(log p)
          - exp(t/2) dt + (1/2) dt,

this script evaluates

    H_(1,10)(E_p) = integral integral
        (1-abs(u+v-10))_+ dE_p(u)dE_p(v).

Only primes below ``exp(11)`` occur.  Arb interval arithmetic certifies that
the result is negative, so a direct reflection-positivity inequality is false
for the actual primes.  The analytic interpretation and exact expansion are
recorded in ``results/ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md``.
"""

from __future__ import annotations

from bisect import bisect_right

from flint import arb, ctx

CENTER = 10
# exp(11) lies strictly between 59874 and 59875.
PRIME_LIMIT = 59875


def _primes_up_to(limit: int) -> list[int]:
    """Return the primes below ``limit`` using a self-contained byte sieve."""
    if limit <= 2:
        return []
    sieve = bytearray(b"\x01") * limit
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, int((limit - 1) ** 0.5) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start:limit:prime] = b"\x00" * (
                ((limit - 1 - start) // prime) + 1
            )
    return [value for value in range(2, limit) if sieve[value]]


def _linear_baseline_antiderivative(v: arb, constant: arb, slope: arb) -> arb:
    """Integrate ``(constant+slope*v)(exp(v/2)-1/2)``."""
    return (
        (v / 2).exp() * (2 * constant + 2 * slope * (v - 2))
        - constant * v / 2
        - slope * v * v / 4
    )


def _baseline_triangle(center: arb) -> arb:
    """Pair the unit triangle centered at ``center`` with the baseline."""
    upper = center + 1
    if upper < 0:
        return arb(0)
    if not upper > 0:
        raise RuntimeError("an interval straddles the baseline endpoint")

    lower = arb(0) if center < 1 else center - 1
    answer = arb(0)
    if center > lower:
        constant = 1 - center
        answer += _linear_baseline_antiderivative(center, constant, arb(1))
        answer -= _linear_baseline_antiderivative(lower, constant, arb(1))
        middle = center
    else:
        if not center < lower:
            raise RuntimeError("an interval straddles a triangle breakpoint")
        middle = lower

    constant = 1 + center
    answer += _linear_baseline_antiderivative(upper, constant, arb(-1))
    answer -= _linear_baseline_antiderivative(middle, constant, arb(-1))
    return answer


def _baseline_convolution_antiderivative(
    v: arb, constant: arb, slope: arb
) -> arb:
    """Integrate one linear piece of the baseline--baseline convolution."""
    exponential = (v / 2).exp() * (
        2 * slope * v * v
        + (2 * constant - 12 * slope) * v
        - 8 * constant
        + 24 * slope
    )
    polynomial = (
        2 * constant * v
        + (constant / 8 + slope) * v * v
        + slope * v * v * v / 12
    )
    return exponential + polynomial


def certified_actual_prime_reflection(dps: int = 40) -> dict[str, arb]:
    """Return an Arb-certified decomposition of ``H_(1,10)(E_p)``."""
    if dps < 20:
        raise ValueError("use at least 20 decimal digits")
    ctx.dps = dps

    center = arb(CENTER)
    one = arb(1)
    if not arb(11).exp() < PRIME_LIMIT:
        raise RuntimeError("PRIME_LIMIT must lie above exp(11)")
    if not arb(11).exp() > PRIME_LIMIT - 1:
        raise RuntimeError("PRIME_LIMIT-1 must lie below exp(11)")

    primes = _primes_up_to(PRIME_LIMIT)
    weights = {
        int(prime): arb(int(prime)).log() / arb(int(prime)).sqrt()
        for prime in primes
    }

    prime_prime = arb(0)
    prime_diagonal = arb(0)
    for raw_prime in primes:
        prime = int(raw_prime)
        stop = bisect_right(primes, PRIME_LIMIT // prime)
        for raw_other in primes[:stop]:
            other = int(raw_other)
            offset = abs(arb(prime * other).log() - center)
            if offset < one:
                contribution = weights[prime] * weights[other] * (one - offset)
                prime_prime += contribution
                if prime == other:
                    prime_diagonal += contribution
            elif not offset > one:
                raise RuntimeError("an interval straddles a triangle endpoint")

    prime_baseline = arb(0)
    for raw_prime in primes:
        prime = int(raw_prime)
        prime_baseline += weights[prime] * _baseline_triangle(
            center - arb(prime).log()
        )

    left_constant = arb(1 - CENTER)
    right_constant = arb(1 + CENTER)
    baseline_baseline = (
        _baseline_convolution_antiderivative(center, left_constant, arb(1))
        - _baseline_convolution_antiderivative(
            center - 1, left_constant, arb(1)
        )
        + _baseline_convolution_antiderivative(
            center + 1, right_constant, arb(-1)
        )
        - _baseline_convolution_antiderivative(center, right_constant, arb(-1))
    )

    prime_background = -2 * prime_baseline
    reflection = prime_prime + prime_background + baseline_baseline
    return {
        "prime_prime": prime_prime,
        "prime_diagonal": prime_diagonal,
        "prime_background": prime_background,
        "baseline_baseline": baseline_baseline,
        "reflection": reflection,
        "reflection_without_prime_diagonal": reflection - prime_diagonal,
    }


def main() -> None:
    values = certified_actual_prime_reflection()
    for name, value in values.items():
        print(f"{name}={value}")
    if not values["reflection"] < 0:
        raise RuntimeError("the certified reflection interval is not negative")


if __name__ == "__main__":
    main()
