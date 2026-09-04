#!/usr/bin/env python3
"""Exact Eratosthenes-deletion decomposition of a prime-gap trapezoid mode.

For an ordered active set S and arbitrary complex data f(x), put

    T(S; f) = 1/2 * sum_{x<y consecutive in S} (y-x)(f(x)+f(y)).

Deleting an interior point x with active neighbours l<x<r changes T by

    1/2 * ((r-x)f(l) + (x-l)f(r) - (r-l)f(x)).

Starting from every integer in [lo, hi] and deleting interior composites by
least prime factor therefore gives an exact, stage-by-stage decomposition of
the endpoint-augmented prime-gap trapezoid.  It is the literal prime-gap
trapezoid when both retained endpoints are prime.  The decomposition is an
exploratory instrument; finite computations do not imply an asymptotic prime
theorem.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


ComplexFunction = Callable[[int], complex]


def smallest_prime_factors(limit: int) -> list[int]:
    """Return the smallest-prime-factor table on [0, limit]."""
    if limit < 2:
        return list(range(limit + 1))
    spf = list(range(limit + 1))
    spf[0] = 0
    spf[1] = 1
    for prime in range(2, math.isqrt(limit) + 1):
        if spf[prime] != prime:
            continue
        start = prime * prime
        for value in range(start, limit + 1, prime):
            if spf[value] == value:
                spf[value] = prime
    return spf


def trapezoid(active: list[bool], values: list[complex], lo: int) -> complex:
    """Evaluate T on a Boolean active mask indexed relative to lo."""
    points = [lo + index for index, flag in enumerate(active) if flag]
    return sum(
        0.5
        * (right - left)
        * (values[left - lo] + values[right - lo])
        for left, right in zip(points, points[1:])
    )


@dataclass(frozen=True)
class DeletionResult:
    lo: int
    hi: int
    initial: complex
    final: complex
    stages: dict[int, complex]
    deleted_by_stage: dict[int, int]
    prime_count: int
    identity_error: float

    @property
    def length(self) -> int:
        return self.hi - self.lo

    def as_json(self, top: int | None = None) -> dict[str, object]:
        stage_l1 = sum(map(abs, self.stages.values()))
        stage_l2 = math.sqrt(sum(abs(value) ** 2 for value in self.stages.values()))
        total_deletion = self.final - self.initial
        dyadic: dict[int, complex] = {}
        dyadic_counts: dict[int, int] = {}
        for prime, value in self.stages.items():
            exponent = prime.bit_length() - 1
            dyadic[exponent] = dyadic.get(exponent, 0j) + value
            dyadic_counts[exponent] = dyadic_counts.get(exponent, 0) + self.deleted_by_stage[prime]
        rows = [
            {
                "least_prime_factor": prime,
                "deleted": self.deleted_by_stage[prime],
                "real": value.real,
                "imag": value.imag,
                "abs": abs(value),
                "normalized_abs": abs(value) / self.length,
            }
            for prime, value in self.stages.items()
        ]
        rows.sort(key=lambda row: float(row["abs"]), reverse=True)
        if top is not None:
            rows = rows[:top]
        return {
            "lo": self.lo,
            "hi": self.hi,
            "length": self.length,
            "prime_count": self.prime_count,
            "initial": [self.initial.real, self.initial.imag],
            "final": [self.final.real, self.final.imag],
            "total_deletion": [
                total_deletion.real,
                total_deletion.imag,
            ],
            "normalized_final_abs": abs(self.final) / self.length,
            "normalized_stage_l1": stage_l1 / self.length,
            "normalized_stage_l2": stage_l2 / self.length,
            "stage_cancellation_ratio": abs(total_deletion) / max(stage_l1, 1e-300),
            "identity_error": self.identity_error,
            "dyadic_stages": [
                {
                    "least_prime_factor_min": 1 << exponent,
                    "least_prime_factor_max": (1 << (exponent + 1)) - 1,
                    "deleted": dyadic_counts[exponent],
                    "real": dyadic[exponent].real,
                    "imag": dyadic[exponent].imag,
                    "abs": abs(dyadic[exponent]),
                    "normalized_abs": abs(dyadic[exponent]) / self.length,
                }
                for exponent in sorted(dyadic)
            ],
            "stages": rows,
        }

    def rational_stage_diagnostic(
        self, q: int, a: int, neighbor_stages: int = 3
    ) -> dict[str, object]:
        """Localize a rational q-mode across the least-factor stage q.

        The returned before/at/after decomposition is an exact telescoping of
        the finite deletion identity.  It is especially useful when
        ``f(n)=exp(2*pi*i*a*n/q)``: every point deleted at stage q has phase
        one, so the load-bearing stage is isolated without an inequality.

        ``1/q`` is reported only as a comparison scale.  The exact circular
        one-hole q-wheel coefficient is given separately by
        :func:`one_hole_q_wheel_coefficient`.
        """

        if q <= 1 or math.gcd(a, q) != 1:
            raise ValueError("require q>1 and gcd(a,q)=1")
        if neighbor_stages < 0:
            raise ValueError("neighbor_stages must be nonnegative")

        ordered = sorted(self.stages)
        before_stages = [prime for prime in ordered if prime < q]
        after_stages = [prime for prime in ordered if prime > q]
        before_contribution = sum((self.stages[p] for p in before_stages), 0j)
        at_contribution = self.stages.get(q, 0j)
        after_contribution = sum((self.stages[p] for p in after_stages), 0j)
        cumulative_before = self.initial + before_contribution
        cumulative_at = cumulative_before + at_contribution
        reconstructed_final = cumulative_at + after_contribution
        length = self.length

        position = sum(prime < q for prime in ordered)
        local_primes = ordered[
            max(0, position - neighbor_stages) : position + neighbor_stages + 1
        ]
        cumulative = self.initial
        cumulative_after_stage: dict[int, complex] = {}
        for prime in ordered:
            cumulative += self.stages[prime]
            if prime in local_primes:
                cumulative_after_stage[prime] = cumulative

        exact_wheel = one_hole_q_wheel_coefficient(a, q)
        period = pre_q_primorial(q)
        complete_pre_q_wheel_stage = (
            circular_pre_q_wheel_stage(a, q)
            if q > 2 and period <= 2_000_000
            else {
                "available": False,
                "pre_q_primorial": period,
                "reason": "period exceeds the deterministic enumeration cap",
            }
        )

        def encoded(value: complex) -> dict[str, float | int]:
            tolerance = 1e-14 * max(1.0, abs(value))

            def sign(part: float) -> int:
                if abs(part) <= tolerance:
                    return 0
                return 1 if part > 0 else -1

            return {
                "real": value.real,
                "imag": value.imag,
                "abs": abs(value),
                "phase_radians": cmath.phase(value) if value else 0.0,
                "real_sign": sign(value.real),
                "imag_sign": sign(value.imag),
                "normalized_abs": abs(value) / length,
            }

        local_rows = []
        for prime in local_primes:
            relation = "at" if prime == q else ("before" if prime < q else "after")
            local_rows.append(
                {
                    "least_prime_factor": prime,
                    "relation_to_q": relation,
                    "deleted": self.deleted_by_stage[prime],
                    "contribution": encoded(self.stages[prime]),
                    "cumulative_after_stage": encoded(cumulative_after_stage[prime]),
                }
            )

        final_normalized = abs(self.final) / length
        off_q_values = [self.stages[p] for p in ordered if p != q]
        off_q_max = max(map(abs, off_q_values), default=0.0)
        return {
            "q": q,
            "a": a,
            "stage_q_present": q in self.stages,
            "stage_q_deleted": self.deleted_by_stage.get(q, 0),
            "initial": encoded(self.initial),
            "before_q_contribution": encoded(before_contribution),
            "cumulative_before_q": encoded(cumulative_before),
            "stage_q_contribution": encoded(at_contribution),
            "cumulative_at_q": encoded(cumulative_at),
            "after_q_contribution": encoded(after_contribution),
            "final": encoded(self.final),
            "stage_norms": {
                "before_l1_normalized": sum(abs(self.stages[p]) for p in before_stages)
                / length,
                "before_l2_normalized": math.sqrt(
                    sum(abs(self.stages[p]) ** 2 for p in before_stages)
                )
                / length,
                "after_l1_normalized": sum(abs(self.stages[p]) for p in after_stages)
                / length,
                "after_l2_normalized": math.sqrt(
                    sum(abs(self.stages[p]) ** 2 for p in after_stages)
                )
                / length,
                "largest_off_q_stage_normalized": off_q_max / length,
                "q_stage_to_largest_off_q_ratio": abs(at_contribution)
                / max(off_q_max, 1e-300),
            },
            "benchmarks": {
                "q_inverse": 1.0 / q,
                "final_abs_over_q_inverse": q * final_normalized,
                "one_hole_q_wheel_exact": [exact_wheel.real, exact_wheel.imag],
                "one_hole_q_wheel_normalized_abs": abs(exact_wheel),
                "final_abs_over_one_hole_q_wheel": final_normalized
                / max(abs(exact_wheel), 1e-300),
                "complete_pre_q_wheel_stage": complete_pre_q_wheel_stage,
            },
            "telescoping_checks": {
                "before_at_after_error": abs(reconstructed_final - self.final),
                "stage_sum_identity_error": self.identity_error,
                "tail_from_cumulative_at_error": abs(
                    self.final - cumulative_at - after_contribution
                ),
            },
            "neighbor_stages": local_rows,
        }


def one_hole_q_wheel_coefficient(a: int, q: int) -> complex:
    """Exact normalized trapezoid coefficient for Z/qZ with zero removed.

    On the circular ordered set ``1,2,...,q-1``, all gaps are one except the
    wrap-around gap of length two.  Thus the Voronoi/trapezoid weights are one
    except for an extra half at residues ``+1`` and ``-1``.  For a nonzero
    additive mode the normalized coefficient is exactly

        (-1 + cos(2*pi*a/q)) / q.

    For ``q=3 (mod 4), a=(q+1)/4`` its magnitude is
    ``(1+sin(pi/(2q)))/q``, explaining why ``1/q`` is the natural full-wheel
    comparison while preserving the finite-q correction.
    """

    if q <= 1 or math.gcd(a, q) != 1:
        raise ValueError("require q>1 and gcd(a,q)=1")
    return complex((-1.0 + math.cos(2.0 * math.pi * a / q)) / q, 0.0)


def pre_q_primorial(q: int) -> int:
    """Return the product of all primes strictly below q."""

    if q < 2:
        raise ValueError("q must be at least two")
    spf = smallest_prime_factors(q - 1)
    return math.prod(value for value in range(2, q) if spf[value] == value)


def circular_pre_q_wheel_stage(
    a: int, q: int, *, maximum_period: int = 2_000_000
) -> dict[str, object]:
    """Exact finite formula for deletion stage q on the pre-q wheel.

    Put ``P=prod_(p<q) p`` and take the circular ordered set of residues
    coprime to P.  Across one interval of length qP, the surviving multiples
    of q visit every wheel residue exactly once.  If L and R are the adjacent
    wheel gaps there, the normalized q-stage is

        (1/(2qP)) sum [R e_q(-aL) + L e_q(aR) - (L+R)].

    Reflection of the wheel swaps L and R and conjugates the summand, so the
    complete-wheel value is real.  The function enumerates the wheel only
    when its period is below ``maximum_period``; the formula itself is not
    restricted to small q.
    """

    if q <= 2 or math.gcd(a, q) != 1:
        raise ValueError("require q>2 and gcd(a,q)=1")
    period = pre_q_primorial(q)
    if period > maximum_period:
        raise ValueError(
            f"pre-q primorial {period} exceeds maximum_period={maximum_period}"
        )
    residues = [value for value in range(1, period + 1) if math.gcd(value, period) == 1]
    gaps = [
        (residues[(index + 1) % len(residues)] - residue) % period
        for index, residue in enumerate(residues)
    ]
    raw = 0j
    reflected_real = 0.0
    for index in range(len(residues)):
        left_gap = gaps[index - 1]
        right_gap = gaps[index]
        raw += 0.5 * (
            right_gap * cmath.exp(-2j * math.pi * a * left_gap / q)
            + left_gap * cmath.exp(2j * math.pi * a * right_gap / q)
            - (left_gap + right_gap)
        )
        reflected_real += 0.5 * (
            right_gap * math.cos(2 * math.pi * a * left_gap / q)
            + left_gap * math.cos(2 * math.pi * a * right_gap / q)
            - (left_gap + right_gap)
        )
    normalized = raw / (q * period)
    normalized_reflected = reflected_real / (q * period)
    return {
        "q": q,
        "a": a,
        "pre_q_primorial": period,
        "wheel_residue_count": len(residues),
        "normalized_stage": [normalized.real, normalized.imag],
        "normalized_stage_abs": abs(normalized),
        "q_times_normalized_stage_abs": q * abs(normalized),
        "reflection_real_formula": normalized_reflected,
        "reflection_imaginary_error": abs(normalized.imag),
        "real_formula_error": abs(normalized.real - normalized_reflected),
        "pre_q_complete_wheel_mode": [0.0, 0.0],
        "scope": "one complete circular period q*prod_(p<q)p",
    }


def decompose(lo: int, hi: int, function: ComplexFunction) -> DeletionResult:
    """Delete composites in SPF stages and return the exact charge ledger."""
    if lo < 2 or hi <= lo + 1:
        raise ValueError("require 2 <= lo < hi-1")

    spf = smallest_prime_factors(hi)
    size = hi - lo + 1
    values = [function(value) for value in range(lo, hi + 1)]
    active = [True] * size
    previous = [index - 1 for index in range(size)]
    following = [index + 1 for index in range(size)]
    following[-1] = -1

    initial = trapezoid(active, values, lo)
    buckets: dict[int, list[int]] = {}
    for value in range(lo + 1, hi):
        if spf[value] == value:
            continue
        buckets.setdefault(spf[value], []).append(value - lo)

    stages: dict[int, complex] = {}
    deleted_by_stage: dict[int, int] = {}
    for prime in sorted(buckets):
        stage = 0j
        deleted = 0
        for index in buckets[prime]:
            if not active[index]:
                continue
            left = previous[index]
            right = following[index]
            if left < 0 or right < 0:
                raise AssertionError("endpoints must remain active")
            left_gap = index - left
            right_gap = right - index
            stage += 0.5 * (
                right_gap * values[left]
                + left_gap * values[right]
                - (left_gap + right_gap) * values[index]
            )
            following[left] = right
            previous[right] = left
            active[index] = False
            deleted += 1
        stages[prime] = stage
        deleted_by_stage[prime] = deleted

    final = trapezoid(active, values, lo)
    stage_total = sum(stages.values(), 0j)
    identity_error = abs(final - initial - stage_total)
    scale = max(1.0, abs(initial), abs(final), sum(map(abs, stages.values())))
    if identity_error > 5e-11 * scale:
        raise AssertionError(
            f"deletion identity failed: error={identity_error} scale={scale}"
        )

    prime_count = sum(
        1 for value in range(lo, hi + 1) if spf[value] == value
    )
    return DeletionResult(
        lo=lo,
        hi=hi,
        initial=initial,
        final=final,
        stages=stages,
        deleted_by_stage=deleted_by_stage,
        prime_count=prime_count,
        identity_error=identity_error,
    )


def rational_mode(a: int, q: int) -> ComplexFunction:
    if q <= 1 or math.gcd(a, q) != 1:
        raise ValueError("require q>1 and gcd(a,q)=1")
    phase = 2j * math.pi * a / q
    return lambda value: cmath.exp(phase * value)


def log_tent_mode(center: float, width: float, alpha: float, t: float) -> ComplexFunction:
    if center <= 0 or width <= 0:
        raise ValueError("center and width must be positive")

    def mode(value: int) -> complex:
        u = math.log(value / center)
        tent = max(0.0, 1.0 - abs(u) / width)
        return tent * math.exp(alpha * u) * cmath.exp(1j * t * u)

    return mode


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--lo", type=int, default=100_000)
    result.add_argument("--hi", type=int, default=200_000)
    result.add_argument("--mode", choices=("rational", "log"), default="rational")
    result.add_argument("--a", type=int, default=4)
    result.add_argument("--q", type=int, default=17)
    result.add_argument("--center", type=float)
    result.add_argument("--width", type=float, default=math.log(2.0) / 2.0)
    result.add_argument("--alpha", type=float, default=0.49)
    result.add_argument("--t", type=float, default=1000.0)
    result.add_argument("--top", type=int, default=20)
    result.add_argument("--output", type=Path)
    return result


def main() -> None:
    args = parser().parse_args()
    if args.mode == "rational":
        function = rational_mode(args.a, args.q)
    else:
        center = args.center or math.sqrt(args.lo * args.hi)
        function = log_tent_mode(center, args.width, args.alpha, args.t)
    result = decompose(args.lo, args.hi, function)
    payload = result.as_json(args.top)
    if args.mode == "rational":
        payload["rational_stage_diagnostic"] = result.rational_stage_diagnostic(
            args.q, args.a
        )
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(encoded + "\n", encoding="utf-8")
    else:
        print(encoded)


if __name__ == "__main__":
    main()
