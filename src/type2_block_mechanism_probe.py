#!/usr/bin/env python3
"""Exploratory block audit for the centered Type-II ``B - Z`` sum.

The probe uses the first-order logarithmic ramp from the fixed-window
Type-II reduction.  For an integer scale ``x``, equal cutoff
``y = floor(x**theta)``, and ramp width ``ell``, it evaluates

    B = sum_{d>y, b>y, m>=1} mu(d) Lambda(b) W_x(d*b*m),

where

    W_x(n) = n**(-1/2) Phi_ell(log(x/n)),
    Phi_ell(t) = 0             for t <= 0,
                 t/ell         for 0 < t < ell,
                 1             for t >= ell.

It independently evaluates the exact divisor-fiber regrouping ``q=d*m``
and checks that the two signed sums agree.  It also checks the centered
identity

    B - Z = C_full + E_Euler,

where ``E_Euler`` is the measured difference between the explicit Type-I
Euler approximation and the exact Type-I complement ``S_full - B``.

The output is a finite, floating-point mechanism diagnostic.  It is not an
interval certificate and bears neither way on the Riemann Hypothesis.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable, TextIO


# Stable mathematical constants used only in the explicit Type-I centering.
ZETA_HALF = -1.46035450880958681288949915251529801247
ZETA_PRIME_HALF = -3.92264613920915172747153144671459951373


def ramp_profile(log_gap: float, ell: float = 1.0) -> float:
    """Return the continuous ramp with explicit closed-endpoint conventions."""
    if not math.isfinite(log_gap):
        raise ValueError("log_gap must be finite")
    if not math.isfinite(ell) or ell <= 0.0:
        raise ValueError("ell must be finite and positive")
    if log_gap <= 0.0:
        return 0.0
    if log_gap >= ell:
        return 1.0
    return log_gap / ell


def ramp_weight(scale: int, n: int, ell: float = 1.0) -> float:
    """Return ``n^-1/2 Phi_ell(log(scale/n))``.

    Thus ``n == scale`` has weight zero and the plateau boundary
    ``log(scale/n) == ell`` has weight one.  Both conventions agree with
    the continuous ramp limits.
    """
    if scale <= 1:
        raise ValueError("scale must exceed one")
    if n <= 0:
        raise ValueError("n must be positive")
    if n >= scale:
        return 0.0
    profile = ramp_profile(math.log(scale / n), ell)
    return profile / math.sqrt(n)


def _arithmetic_sieve(
    limit: int,
) -> tuple[list[int], list[int], list[float], bytearray]:
    """Return mu, omega, Lambda, and a prime indicator through ``limit``."""
    if limit < 1:
        raise ValueError("sieve limit must be positive")
    mu = [0] * (limit + 1)
    omega = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = bytearray(limit + 1)

    for value in range(2, limit + 1):
        if not composite[value]:
            primes.append(value)
            mu[value] = -1
            omega[value] = 1
        for prime in primes:
            product = value * prime
            if product > limit:
                break
            composite[product] = 1
            if value % prime == 0:
                mu[product] = 0
                omega[product] = omega[value]
                break
            mu[product] = -mu[value]
            omega[product] = omega[value] + 1

    mangoldt = [0.0] * (limit + 1)
    prime_indicator = bytearray(limit + 1)
    for prime in primes:
        prime_indicator[prime] = 1
        log_prime = math.log(prime)
        power = prime
        while power <= limit:
            mangoldt[power] = log_prime
            if power > limit // prime:
                break
            power *= prime
    return mu, omega, mangoldt, prime_indicator


def _primes_up_to(limit: int) -> list[int]:
    """Return the primes through ``limit`` by an Eratosthenes sieve."""
    if limit < 2:
        return []
    indicator = bytearray(b"\x01") * (limit + 1)
    indicator[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if not indicator[prime]:
            continue
        start = prime * prime
        count = (limit - start) // prime + 1
        indicator[start : limit + 1 : prime] = b"\x00" * count
    return [value for value in range(2, limit + 1) if indicator[value]]


def _add(mapping: dict, key: object, value: float) -> None:
    mapping[key] = mapping.get(key, 0.0) + value


def _close_or_raise(
    label: str, left: float, right: float, absolute_scale: float
) -> float:
    """Check a floating identity and return its signed discrepancy."""
    discrepancy = left - right
    tolerance = 2.0e-12 * max(1.0, absolute_scale, abs(left), abs(right))
    if abs(discrepancy) > tolerance:
        raise RuntimeError(
            f"{label} failed: left={left!r}, right={right!r}, "
            f"difference={discrepancy!r}, tolerance={tolerance!r}"
        )
    return discrepancy


@dataclass
class ProbeResult:
    """Scalar results plus detailed block decompositions for one scale."""

    scale: int
    cutoff: int
    theta: float
    ell: float
    term_count: int
    balanced: float
    fiber_balanced: float
    centering: float
    centered_residual: float
    full_discrepancy: float
    euler_defect: float
    triple_fiber_error: float
    centered_identity_error: float
    block_closure_error: float
    raw_l1: float
    fiber_l1: float
    positive_l1: float
    negative_l1: float
    cofactor_l1: float
    dyadic_cell_l1: float
    dyadic_diagonal: float
    dyadic_off_diagonal: float
    dyadic_diagonal_l1: float
    dyadic_off_diagonal_l1: float
    cofactor_diagonal_energy: float
    cofactor_cross_energy: float
    cell_diagonal_energy: float
    cell_cross_energy: float
    centered_diagonal_energy: float
    centered_cross_energy: float
    m_one: float
    m_one_l1: float
    prime_prime_m_one: float
    independent_d_sigma: float
    cofactor_sums: dict[int, float] = field(repr=False)
    dyadic_cells: dict[tuple[int, int], float] = field(repr=False)
    omega_sums: dict[int, float] = field(repr=False)

    def scalar_row(self) -> dict[str, int | float]:
        """Return the CSV-safe scalar fields."""
        row = asdict(self)
        row.pop("cofactor_sums")
        row.pop("dyadic_cells")
        row.pop("omega_sums")
        return row


def analyze_scale(
    scale: int,
    theta: float = 3.0 / 8.0,
    ell: float = 1.0,
) -> ProbeResult:
    """Evaluate and internally cross-check the Type-II decomposition."""
    if scale < 16:
        raise ValueError("use an integer scale of at least 16")
    if not math.isfinite(theta) or not 0.0 < theta < 0.5:
        raise ValueError("theta must lie strictly between zero and one half")
    if not math.isfinite(ell) or ell <= 0.0:
        raise ValueError("ell must be finite and positive")

    cutoff = int(scale**theta)
    if cutoff <= 1:
        raise ValueError("the resulting cutoff must exceed one")
    if cutoff * cutoff > scale * math.exp(-ell):
        raise ValueError("the support condition cutoff^2 <= scale*exp(-ell) fails")

    # Since d,b >= cutoff+1 and n=scale has zero weight, this is the largest
    # d or b that can enter a nonzero term.
    limit = (scale - 1) // (cutoff + 1)
    mu, omega, mangoldt, prime_indicator = _arithmetic_sieve(limit)
    log_scale = math.log(scale)

    dyadic_bin = [0] * (limit + 1)
    for value in range(cutoff + 1, limit + 1):
        dyadic_bin[value] = int(math.log2(value / cutoff))

    cofactor_sums: dict[int, float] = {}
    dyadic_cells: dict[tuple[int, int], float] = {}
    omega_sums: dict[int, float] = {}
    d_amplitudes = [0.0] * (limit + 1)

    positive_l1 = 0.0
    negative_l1 = 0.0
    dyadic_diagonal = 0.0
    dyadic_off_diagonal = 0.0
    dyadic_diagonal_l1 = 0.0
    dyadic_off_diagonal_l1 = 0.0
    m_one = 0.0
    m_one_l1 = 0.0
    prime_prime_m_one = 0.0
    term_count = 0

    def weight(n: int) -> float:
        log_gap = log_scale - math.log(n)
        profile = 1.0 if log_gap >= ell else log_gap / ell
        return profile / math.sqrt(n)

    for b in range(cutoff + 1, limit + 1):
        lambda_b = mangoldt[b]
        if lambda_b == 0.0:
            continue
        b_bin = dyadic_bin[b]
        maximum_d = (scale - 1) // b
        for d in range(cutoff + 1, maximum_d + 1):
            mu_d = mu[d]
            if mu_d == 0:
                continue
            d_bin = dyadic_bin[d]
            amplitude_for_d = 0.0
            maximum_m = (scale - 1) // (b * d)
            for cofactor in range(1, maximum_m + 1):
                n = b * d * cofactor
                amplitude = lambda_b * weight(n)
                signed = mu_d * amplitude
                amplitude_for_d += amplitude
                term_count += 1

                if mu_d > 0:
                    positive_l1 += amplitude
                else:
                    negative_l1 += amplitude
                _add(cofactor_sums, cofactor, signed)
                _add(dyadic_cells, (d_bin, b_bin), signed)
                _add(omega_sums, omega[d], signed)

                if d_bin == b_bin:
                    dyadic_diagonal += signed
                    dyadic_diagonal_l1 += amplitude
                else:
                    dyadic_off_diagonal += signed
                    dyadic_off_diagonal_l1 += amplitude
                if cofactor == 1:
                    m_one += signed
                    m_one_l1 += amplitude
                    if prime_indicator[d] and prime_indicator[b]:
                        prime_prime_m_one += signed
            d_amplitudes[d] += amplitude_for_d

    balanced = math.fsum(cofactor_sums.values())
    raw_l1 = positive_l1 + negative_l1
    signed_split = positive_l1 - negative_l1

    # Independent exact divisor-fiber evaluation with q=d*m.
    mobius_tail = [0] * (limit + 1)
    for d in range(cutoff + 1, limit + 1):
        if mu[d] == 0:
            continue
        for q in range(d, limit + 1, d):
            mobius_tail[q] += mu[d]

    fiber_parts: list[float] = []
    fiber_l1 = 0.0
    for b in range(cutoff + 1, limit + 1):
        lambda_b = mangoldt[b]
        if lambda_b == 0.0:
            continue
        subtotal: list[float] = []
        maximum_q = (scale - 1) // b
        for q in range(cutoff + 1, maximum_q + 1):
            tail = mobius_tail[q]
            if tail == 0:
                continue
            signed = lambda_b * weight(b * q) * tail
            subtotal.append(signed)
            fiber_l1 += abs(signed)
        fiber_parts.append(math.fsum(subtotal))
    fiber_balanced = math.fsum(fiber_parts)
    triple_fiber_error = _close_or_raise(
        "triple/fiber identity", balanced, fiber_balanced, raw_l1
    )

    cell_total = math.fsum(dyadic_cells.values())
    omega_total = math.fsum(omega_sums.values())
    diagonal_total = dyadic_diagonal + dyadic_off_diagonal
    closure_errors = (
        balanced - signed_split,
        balanced - cell_total,
        balanced - omega_total,
        balanced - diagonal_total,
    )
    block_closure_error = max(closure_errors, key=abs)
    _close_or_raise(
        "block decomposition", balanced, balanced - block_closure_error, raw_l1
    )

    # Direct full von Mangoldt ramp, independent of the Type-II enumeration.
    def full_terms() -> Iterable[float]:
        for prime in _primes_up_to(scale - 1):
            log_prime = math.log(prime)
            power = prime
            while power < scale:
                yield log_prime * weight(power)
                if power > (scale - 1) // prime:
                    break
                power *= prime

    full_sum = math.fsum(full_terms())
    exp_half = math.exp(-ell / 2.0)
    j_zero = 4.0 * (1.0 - exp_half) / ell
    j_one = 4.0 * ((ell + 4.0) * exp_half - 4.0) / ell
    full_discrepancy = full_sum - j_zero * math.sqrt(scale)

    m_one_value = math.fsum(mu[d] / d for d in range(1, cutoff + 1))
    m_one_derivative = math.fsum(
        -mu[d] * math.log(d) / d for d in range(1, cutoff + 1)
    )
    m_half = math.fsum(
        mu[d] / math.sqrt(d) for d in range(1, cutoff + 1)
    )
    l_one = math.fsum(
        mangoldt[b] / b for b in range(2, cutoff + 1)
    )
    l_half = math.fsum(
        mangoldt[b] / math.sqrt(b) for b in range(2, cutoff + 1)
    )

    i_polar = math.sqrt(scale) * (
        m_one_value * (j_zero * log_scale + j_one)
        + j_zero * (m_one_derivative - m_one_value * l_one)
    )
    i_zero = (
        -ZETA_PRIME_HALF * m_half
        + l_half
        - ZETA_HALF * m_half * l_half
    )
    approximate_type_one = i_polar + i_zero
    centering = j_zero * math.sqrt(scale) - approximate_type_one
    centered_residual = balanced - centering

    exact_type_one = full_sum - balanced
    euler_defect = approximate_type_one - exact_type_one
    centered_identity_error = _close_or_raise(
        "centered/full identity",
        centered_residual,
        full_discrepancy + euler_defect,
        raw_l1 + abs(centering),
    )

    cofactor_l1 = math.fsum(abs(value) for value in cofactor_sums.values())
    dyadic_cell_l1 = math.fsum(abs(value) for value in dyadic_cells.values())
    cofactor_diagonal_energy = math.fsum(
        value * value for value in cofactor_sums.values()
    )
    cofactor_cross_energy = balanced * balanced - cofactor_diagonal_energy
    cell_diagonal_energy = math.fsum(
        value * value for value in dyadic_cells.values()
    )
    cell_cross_energy = balanced * balanced - cell_diagonal_energy
    centered_diagonal_energy = cell_diagonal_energy + centering * centering
    centered_cross_energy = (
        centered_residual * centered_residual - centered_diagonal_energy
    )
    independent_d_sigma = math.sqrt(
        math.fsum(
            amplitude * amplitude
            for d, amplitude in enumerate(d_amplitudes)
            if d > cutoff and mu[d] != 0
        )
    )

    return ProbeResult(
        scale=scale,
        cutoff=cutoff,
        theta=theta,
        ell=ell,
        term_count=term_count,
        balanced=balanced,
        fiber_balanced=fiber_balanced,
        centering=centering,
        centered_residual=centered_residual,
        full_discrepancy=full_discrepancy,
        euler_defect=euler_defect,
        triple_fiber_error=triple_fiber_error,
        centered_identity_error=centered_identity_error,
        block_closure_error=block_closure_error,
        raw_l1=raw_l1,
        fiber_l1=fiber_l1,
        positive_l1=positive_l1,
        negative_l1=negative_l1,
        cofactor_l1=cofactor_l1,
        dyadic_cell_l1=dyadic_cell_l1,
        dyadic_diagonal=dyadic_diagonal,
        dyadic_off_diagonal=dyadic_off_diagonal,
        dyadic_diagonal_l1=dyadic_diagonal_l1,
        dyadic_off_diagonal_l1=dyadic_off_diagonal_l1,
        cofactor_diagonal_energy=cofactor_diagonal_energy,
        cofactor_cross_energy=cofactor_cross_energy,
        cell_diagonal_energy=cell_diagonal_energy,
        cell_cross_energy=cell_cross_energy,
        centered_diagonal_energy=centered_diagonal_energy,
        centered_cross_energy=centered_cross_energy,
        m_one=m_one,
        m_one_l1=m_one_l1,
        prime_prime_m_one=prime_prime_m_one,
        independent_d_sigma=independent_d_sigma,
        cofactor_sums=dict(sorted(cofactor_sums.items())),
        dyadic_cells=dict(sorted(dyadic_cells.items())),
        omega_sums=dict(sorted(omega_sums.items())),
    )


def geometric_scales(minimum: int, maximum: int, count: int) -> list[int]:
    """Return unique rounded geometric scales including both endpoints."""
    if minimum < 16 or maximum < minimum:
        raise ValueError("require 16 <= minimum <= maximum")
    if count <= 0:
        raise ValueError("count must be positive")
    if count == 1 or minimum == maximum:
        return [minimum]
    ratio = (maximum / minimum) ** (1.0 / (count - 1))
    values = {minimum, maximum}
    values.update(round(minimum * ratio**index) for index in range(count))
    return sorted(values)


def _write_csv(results: list[ProbeResult], stream: TextIO) -> None:
    rows = [result.scalar_row() for result in results]
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)


def _print_summary(result: ProbeResult) -> None:
    cofactor_ratio = abs(result.balanced) / max(result.cofactor_l1, 1.0e-300)
    cell_ratio = abs(result.balanced) / max(result.dyadic_cell_l1, 1.0e-300)
    print(
        f"x={result.scale} y={result.cutoff} terms={result.term_count} "
        f"B={result.balanced:+.9g} Z={result.centering:+.9g} "
        f"B-Z={result.centered_residual:+.9g} "
        f"C={result.full_discrepancy:+.9g} E={result.euler_defect:+.3e}"
    )
    print(
        f"  L1 raw={result.raw_l1:.9g} fiber={result.fiber_l1:.9g} "
        f"cofactor={result.cofactor_l1:.9g} cells={result.dyadic_cell_l1:.9g}; "
        f"|B|/cofactor={cofactor_ratio:.6g} |B|/cells={cell_ratio:.6g}"
    )


def _print_details(result: ProbeResult) -> None:
    print(f"  omega sectors: {result.omega_sums}")
    print(f"  cofactor sectors: {result.cofactor_sums}")
    maximum_bin = max((max(cell) for cell in result.dyadic_cells), default=-1)
    print("  dyadic cells (d-bin rows, b-bin columns):")
    for d_bin in range(maximum_bin + 1):
        entries = [
            f"{result.dyadic_cells.get((d_bin, b_bin), 0.0):+.6g}"
            for b_bin in range(maximum_bin + 1)
        ]
        print(f"    {d_bin}: " + " ".join(entries))


def _parse_integer_set(text: str) -> set[int]:
    if not text.strip():
        return set()
    values = {int(piece.strip()) for piece in text.split(",")}
    if any(value < 16 for value in values):
        raise ValueError("detail scales must be at least 16")
    return values


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--xmin", type=int, default=10_000)
    parser.add_argument("--xmax", type=int, default=10_000_000)
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--theta", type=float, default=3.0 / 8.0)
    parser.add_argument("--ell", type=float, default=1.0)
    parser.add_argument(
        "--details-at",
        default="",
        help="comma-separated scales whose block dictionaries should be printed",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        help="write scalar results as CSV; use '-' for standard output",
    )
    args = parser.parse_args(argv)

    try:
        detail_scales = _parse_integer_set(args.details_at)
        scales = set(geometric_scales(args.xmin, args.xmax, args.count))
        scales.update(detail_scales)
        results = [
            analyze_scale(scale, theta=args.theta, ell=args.ell)
            for scale in sorted(scales)
        ]
    except (ValueError, RuntimeError) as error:
        parser.error(str(error))

    if args.csv is not None:
        if str(args.csv) == "-":
            _write_csv(results, sys.stdout)
        else:
            with args.csv.open("w", encoding="utf-8", newline="") as stream:
                _write_csv(results, stream)
            print(f"wrote {args.csv}", file=sys.stderr)
        return

    for result in results:
        _print_summary(result)
        if result.scale in detail_scales:
            _print_details(result)


if __name__ == "__main__":
    main()
