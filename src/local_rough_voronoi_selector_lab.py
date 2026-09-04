#!/usr/bin/env python3
"""Local common-height lab for rough-Voronoi cutoff increments.

This is a finite diagnostic for the exact object left by the q-first/SPF
telescope.  On a shell ``[Y,2Y]`` it forms

    Delta_P = nu_(2P) - nu_P,

where ``nu_z`` is the endpoint-trapezoid measure on integers with least prime
factor greater than ``z``.  It then samples curvature localizations with tent
half-width ``H=Y/sqrt(T)``, rejects centers lying in a low-denominator
derivative major arc, selects a Dirichlet approximant ``a/q`` with
``Y^beta < q <= min(H,Y^(33/133))``, and reports both the selected rational
coefficient and the true ``T log n`` coefficient after tent localization.

No finite scan is an asymptotic dispersion theorem.  In particular, this
program does not infer a zeta zero-free region from its output.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

from prime_gap_sieve_deletion import smallest_prime_factors


SCHEMA = "zeta23.local-rough-voronoi-selector-lab.v4"
BETA = Fraction(1537, 10_000)
BETA_MAX = Fraction(33, 133)
KAPPA = 0.0197404825829421


def rational_power_floor(base: int, exponent: Fraction) -> int:
    """Return ``floor(base**exponent)`` with an exact integer certificate."""

    if base < 1 or exponent <= 0:
        raise ValueError("require a positive base and exponent")
    numerator = exponent.numerator
    denominator = exponent.denominator
    target = pow(base, numerator)
    guess = max(1, math.floor(base ** float(exponent)))
    while pow(guess, denominator) > target:
        guess -= 1
    while pow(guess + 1, denominator) <= target:
        guess += 1
    return guess


def _is_prime(value: int, spf: list[int]) -> bool:
    return value >= 2 and spf[value] == value


def prime_barriers(lo: int, hi: int, spf: list[int]) -> tuple[int, int]:
    """Return permanent prime barriers inside ``[lo,hi]``."""

    left = next(value for value in range(lo, hi + 1) if _is_prime(value, spf))
    right = next(
        value for value in range(hi, left, -1) if _is_prime(value, spf)
    )
    return left, right


def rough_points(lo: int, hi: int, cutoff: int, spf: list[int]) -> list[int]:
    """Return the finite rough set, retaining shell barriers exactly."""

    if not (2 <= cutoff < lo < hi < len(spf)):
        raise ValueError("invalid rough shell/cutoff")
    return [
        n
        for n in range(lo, hi + 1)
        if n in (lo, hi) or spf[n] > cutoff
    ]


def twice_voronoi_measure(points: Iterable[int]) -> dict[int, int]:
    """Return twice the endpoint-trapezoid mass at every retained point."""

    values = list(points)
    if values != sorted(set(values)) or len(values) < 2:
        raise ValueError("points must be strictly increasing")
    mass: dict[int, int] = {n: 0 for n in values}
    for left, right in zip(values, values[1:]):
        gap = right - left
        mass[left] += gap
        mass[right] += gap
    if sum(mass.values()) != 2 * (values[-1] - values[0]):
        raise AssertionError("trapezoid mass ledger failed")
    return mass


def twice_increment(
    lo: int, hi: int, cutoff: int, spf: list[int]
) -> dict[int, int]:
    """Return the sparse signed measure ``2*(nu_(2P)-nu_P)``."""

    fine = twice_voronoi_measure(rough_points(lo, hi, cutoff, spf))
    coarse = twice_voronoi_measure(rough_points(lo, hi, 2 * cutoff, spf))
    keys = fine.keys() | coarse.keys()
    delta = {n: coarse.get(n, 0) - fine.get(n, 0) for n in keys}
    delta = {n: value for n, value in delta.items() if value}
    if sum(delta.values()) != 0:
        raise AssertionError("rough cutoff increment has nonzero total mass")
    return delta


def twice_increment_between(
    lo: int,
    hi: int,
    fine_cutoff: int,
    coarse_cutoff: int,
    spf: list[int],
) -> dict[int, int]:
    """Return ``2*(nu_coarse-nu_fine)`` for arbitrary nested cutoffs."""

    if not 2 <= fine_cutoff <= coarse_cutoff:
        raise ValueError("cutoffs must satisfy 2 <= fine <= coarse")
    fine = twice_voronoi_measure(rough_points(lo, hi, fine_cutoff, spf))
    coarse = twice_voronoi_measure(rough_points(lo, hi, coarse_cutoff, spf))
    keys = fine.keys() | coarse.keys()
    delta = {n: coarse.get(n, 0) - fine.get(n, 0) for n in keys}
    delta = {n: value for n, value in delta.items() if value}
    if sum(delta.values()) != 0:
        raise AssertionError("rough cutoff increment has nonzero total mass")
    return delta


@dataclass(frozen=True)
class RationalSelector:
    # ``numerator`` is the reduced residue used by e_q(a n).  The lifted
    # integer is retained separately so the Dirichlet approximation to an
    # alpha outside [0,1) can be reconstructed from serialized output.
    numerator: int
    denominator: int
    lifted_numerator: int
    error: float
    low_major_distance: float


def _distance_to_integer(value: float) -> float:
    return abs(value - round(value))


def select_rational(
    alpha: float, h: int, q_min: int, q_max: int | None = None
) -> RationalSelector | None:
    """Select a reduced ``a/q`` after excluding all denominators below q_min.

    The major-arc convention is ``||r alpha|| <= 1/H``.  A returned
    denominator therefore obeys ``q_min < q <= min(H,q_max)`` and
    ``|alpha-a/q| <= 1/(qH)``.
    """

    upper = h if q_max is None else min(h, q_max)
    if upper <= q_min:
        return None
    low = min(_distance_to_integer(alpha * r) for r in range(1, q_min + 1))
    if low <= 1.0 / h:
        return None
    candidates: list[tuple[float, int, int]] = []
    for q in range(q_min + 1, upper + 1):
        a = round(alpha * q)
        residue = abs(alpha * q - a)
        if residue <= 1.0 / h:
            divisor = math.gcd(abs(a), q)
            reduced_q = q // divisor
            reduced_a = a // divisor
            if reduced_q > q_min:
                candidates.append((residue, reduced_q, reduced_a))
    if not candidates:
        return None
    residue, q, a = min(candidates)
    error = abs(alpha - a / q)
    if error > 1.0000001 / (q * h):
        raise AssertionError("Dirichlet selector certificate failed")
    return RationalSelector(a % q, q, a, error, low)


def tent(value: float) -> float:
    return max(0.0, 1.0 - abs(value))


def localized_residue_vector(
    delta2: dict[int, int], center: float, h: int, q: int
) -> tuple[list[float], float]:
    """Return the actual-mass tent-localized residue vector and variation."""

    if q < 2:
        raise ValueError("q must be at least two")
    vector = [0.0] * q
    variation = 0.0
    for n, twice_mass in delta2.items():
        weight = tent((n - center) / h)
        if not weight:
            continue
        signed_mass = 0.5 * twice_mass * weight
        vector[n % q] += signed_mass
        variation += abs(signed_mass)
    return vector, variation


def residue_moment_ledger(vector: Iterable[float]) -> dict[str, float]:
    """Return actual-mass L2 and cyclic-correlation L2 ledgers.

    If ``D(a)=sum_r vector[r] exp(2*pi*i*a*r/q)``, these conventions obey

        sum_a |D(a)|^2 = q ||vector||_2^2,
        sum_a |D(a)|^4 = q sum_s |C(s)|^2,

    where ``C(s)=sum_r vector[r] vector[r+s]`` cyclically.
    """

    values = list(vector)
    q = len(values)
    if q < 2:
        raise ValueError("residue vector must have length at least two")
    l2_squared = sum(value * value for value in values)
    correlation = [
        sum(values[r] * values[(r + shift) % q] for r in range(q))
        for shift in range(q)
    ]
    correlation_l2_squared = sum(value * value for value in correlation)
    return {
        "residue_l2_squared": l2_squared,
        "cyclic_correlation_l2_squared": correlation_l2_squared,
        "zero_shift_correlation": correlation[0],
    }


def localized_coefficients(
    delta2: dict[int, int],
    center: float,
    h: int,
    height: float,
    selector: RationalSelector,
) -> tuple[complex, complex, float]:
    """Return rational/log coefficients and localized total variation.

    The signed dictionary stores twice mass, so all three outputs divide by
    two.  A constant global phase is removed from the logarithmic coefficient.
    """

    rational = 0j
    logarithmic = 0j
    variation = 0.0
    q = selector.denominator
    a = selector.numerator
    for n, twice_mass in delta2.items():
        weight = tent((n - center) / h)
        if not weight:
            continue
        signed_mass = 0.5 * twice_mass * weight
        rational += signed_mass * cmath.exp(2j * math.pi * ((a * n) % q) / q)
        logarithmic += signed_mass * cmath.exp(1j * height * math.log(n / center))
        variation += abs(signed_mass)
    return rational, logarithmic, variation


def _thresholds(y: int, q_floor: int) -> list[int]:
    value = max(3, q_floor + 1)
    result: list[int] = []
    # Include the first band whose upper cutoff has reached every possible
    # least prime factor in [Y,2Y].  Stopping at sqrt(2Y)/2 can miss this
    # terminal band when the geometric ladder jumps across that boundary.
    terminal = math.isqrt(2 * y)
    while True:
        result.append(value)
        if 2 * value >= terminal:
            break
        value *= 2
    return result


def analyze(
    scales: Iterable[int],
    height_exponents: Iterable[float],
    block_samples: int = 12,
) -> dict[str, object]:
    scales = sorted(set(scales))
    exponents = sorted(set(height_exponents))
    if not scales or scales[0] < 1_000:
        raise ValueError("all scales must be at least 1000")
    if not exponents or not all(0.8 <= value <= 1.6 for value in exponents):
        raise ValueError("height exponents must lie in [0.8,1.6]")
    if block_samples < 1:
        raise ValueError("block_samples must be positive")

    max_y = scales[-1]
    spf = smallest_prime_factors(2 * max_y + 2)
    rows: list[dict[str, object]] = []
    blocks: list[dict[str, object]] = []
    skipped_major = 0
    skipped_selector = 0
    skipped_boundary = 0
    empty_post_q = 0
    next_block_id = 0
    for y in scales:
        lo, hi = prime_barriers(y, 2 * y, spf)
        # The analytic condition is q>Y^beta.  For integer q this is exactly
        # q>floor(Y^beta), not q>ceil(Y^beta).
        q_floor = max(2, rational_power_floor(y, BETA))
        q_cap = max(q_floor, rational_power_floor(y, BETA_MAX))
        deltas = {
            cutoff: twice_increment(lo, hi, cutoff, spf)
            for cutoff in _thresholds(y, q_floor)
        }
        for exponent in exponents:
            height = y**exponent
            h = max(2, int(y / math.sqrt(height)))
            if min(h, q_cap) <= q_floor:
                skipped_selector += block_samples
                continue
            # Oversample deterministic midpoints; retain the first requested
            # minor-arc blocks.  Centers stay one H away from shell barriers.
            available = max(1, (y - 2 * h) // h)
            # In the capped-q regime an in-range approximant can have density
            # only about q_cap/H, so eightfold oversampling badly underfills
            # the lower-height rows.  The finite scan can afford this broader
            # deterministic search; it is not a probabilistic assertion.
            probes = min(max(64 * block_samples, block_samples), available)
            accepted = 0
            for index in range(probes):
                center = y + h + (index + 0.5) * (y - 2 * h) / probes
                support_left = center - h
                support_right = center + h
                if support_left < lo or support_right > hi:
                    skipped_boundary += 1
                    continue
                alpha = height / (2.0 * math.pi * center)
                selector = select_rational(alpha, h, q_floor, q_cap)
                if selector is None:
                    skipped_major += 1
                    continue
                block_id = next_block_id
                next_block_id += 1
                eligible = [
                    cutoff
                    for cutoff in deltas
                    if cutoff >= selector.denominator
                ]
                crossing = [
                    cutoff
                    for cutoff in deltas
                    if cutoff < selector.denominator <= 2 * cutoff
                ]
                if not eligible:
                    empty_post_q += 1
                blocks.append(
                    {
                        "block_id": block_id,
                        "Y": y,
                        "height_exponent": exponent,
                        "height": height,
                        "H": h,
                        "center": center,
                        "shell": [lo, hi],
                        "tent_support": [support_left, support_right],
                        "normalization_scale": h,
                        "derivative_alpha": alpha,
                        "q_floor": q_floor,
                        "q_cap": q_cap,
                        "q": selector.denominator,
                        "a": selector.numerator,
                        "lifted_a": selector.lifted_numerator,
                        "dirichlet_error": selector.error,
                        "dirichlet_bound": 1.0
                        / (selector.denominator * h),
                        "low_major_distance": selector.low_major_distance,
                        "complete_cutoffs_P": eligible,
                        "included_crossing_cutoffs_P": crossing,
                        "certificates": {
                            "prime_shell_barriers": _is_prime(lo, spf)
                            and _is_prime(hi, spf),
                            "tent_inside_shell": support_left >= lo
                            and support_right <= hi,
                            "minor_arc_below_q_floor": (
                                selector.low_major_distance > 1.0 / h
                            ),
                            "denominator_below_q_cap": (
                                selector.denominator <= q_cap
                            ),
                            "dirichlet_approximation": (
                                selector.error
                                <= 1.0000001
                                / (selector.denominator * h)
                            ),
                            "lifted_numerator": (
                                selector.lifted_numerator
                                % selector.denominator
                                == selector.numerator
                            ),
                            "primitive_frequency": (
                                math.gcd(
                                    selector.numerator,
                                    selector.denominator,
                                )
                                == 1
                            ),
                        },
                    }
                )
                bands = [
                    (cutoff, "complete", deltas[cutoff])
                    for cutoff in eligible
                ]
                bands.extend(
                    (
                        cutoff,
                        "crossing",
                        twice_increment_between(
                            lo,
                            hi,
                            selector.denominator,
                            2 * cutoff,
                            spf,
                        ),
                    )
                    for cutoff in crossing
                )
                for cutoff, band_kind, delta in bands:
                    # The exact post-q telescope uses
                    # nu_max(2P,q)-nu_max(P,q).  Complete bands P>=q use the
                    # precomputed nu_2P-nu_P increment; the unique crossing
                    # band P<q<=2P is computed as nu_2P-nu_q.
                    rational, logarithmic, variation = localized_coefficients(
                        delta, center, h, height, selector
                    )
                    residue_vector, residue_variation = localized_residue_vector(
                        delta, center, h, selector.denominator
                    )
                    if abs(residue_variation - variation) > 1e-9 * max(
                        1.0, variation
                    ):
                        raise AssertionError("localized variation mismatch")
                    moments = residue_moment_ledger(residue_vector)
                    residue_rational = sum(
                        value
                        * cmath.exp(
                            2j
                            * math.pi
                            * ((selector.numerator * residue) % selector.denominator)
                            / selector.denominator
                        )
                        for residue, value in enumerate(residue_vector)
                    )
                    fourier_error = abs(residue_rational - rational)
                    if fourier_error > 1e-9 * max(1.0, abs(rational)):
                        raise AssertionError("residue/Fourier phase mismatch")
                    norm = float(h)
                    rows.append(
                        {
                            "block_id": block_id,
                            "Y": y,
                            "height_exponent": exponent,
                            "height": height,
                            "H": h,
                            "H_exponent": math.log(h) / math.log(y),
                            "center": center,
                            "q_floor": q_floor,
                            "q": selector.denominator,
                            "a": selector.numerator,
                            "lifted_a": selector.lifted_numerator,
                            "q_exponent": math.log(selector.denominator)
                            / math.log(y),
                            "dirichlet_error": selector.error,
                            "dirichlet_bound": 1.0
                            / (selector.denominator * h),
                            "low_major_distance": selector.low_major_distance,
                            "cutoff_P": cutoff,
                            "band_kind": band_kind,
                            "P_exponent": math.log(cutoff) / math.log(y),
                            "rational_normalized_real": rational.real / norm,
                            "rational_normalized_imag": rational.imag / norm,
                            "rational_normalized_abs": abs(rational) / norm,
                            "logarithmic_normalized_real": (
                                logarithmic.real / norm
                            ),
                            "logarithmic_normalized_imag": (
                                logarithmic.imag / norm
                            ),
                            "logarithmic_normalized_abs": abs(logarithmic) / norm,
                            "localized_variation_normalized": variation / norm,
                            "residue_l2_squared_actual_mass": moments[
                                "residue_l2_squared"
                            ],
                            "cyclic_correlation_l2_squared_actual_mass": moments[
                                "cyclic_correlation_l2_squared"
                            ],
                            "zero_shift_correlation_actual_mass": moments[
                                "zero_shift_correlation"
                            ],
                            "all_frequency_second_moment_actual_mass": (
                                selector.denominator
                                * moments["residue_l2_squared"]
                            ),
                            "all_frequency_fourth_moment_actual_mass": (
                                selector.denominator
                                * moments[
                                    "cyclic_correlation_l2_squared"
                                ]
                            ),
                            "target_weighted_l2": (
                                selector.denominator
                                / norm
                                * moments["residue_l2_squared"]
                            ),
                            "target_weighted_l4": (
                                selector.denominator
                                / norm**3
                                * moments[
                                    "cyclic_correlation_l2_squared"
                                ]
                            ),
                            "selected_fourier_from_residue_error": fourier_error,
                            "target_scaled_rational": abs(rational)
                            / norm
                            * y**KAPPA,
                            "target_scaled_logarithmic": abs(logarithmic)
                            / norm
                            * y**KAPPA,
                        }
                    )
                accepted += 1
                if accepted >= block_samples:
                    break

    return {
        "schema": SCHEMA,
        "parameters": {
            "scales": scales,
            "height_exponents": exponents,
            "block_samples": block_samples,
            "beta": str(BETA),
            "beta_max": str(BETA_MAX),
            "kappa": KAPPA,
        },
        "blocks": blocks,
        "rows": rows,
        "skipped": {
            "low_major_or_no_high_approximant_probes": skipped_major,
            "blocks_with_H_below_q_floor": skipped_selector,
            "probes_with_tent_outside_prime_barriers": skipped_boundary,
            "selected_blocks_with_no_complete_post_q_band": empty_post_q,
        },
        "scope": (
            "finite localized diagnostic for selected rational and true-log "
            "coefficients of complete post-q dyadic rough-Voronoi increments "
            "P>=q plus the exact band P<q<=2P, with the selected "
            "denominator restricted to q<=Y^(33/133); permanent prime shell "
            "barriers are outside every sampled tent; H is the tent half-width "
            "and also its continuum L1 normalization (support diameter 2H); "
            "the rational phase is exp(+2*pi*i*a*n/q) and the true phase is "
            "exp(+i*T*log(n/center)); their reported values are separate "
            "diagnostics, not asserted approximations; no asymptotic, "
            "complete-tail, or zeta-strip inference"
        ),
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--scales", default="10000,30000,100000,300000")
    result.add_argument("--height-exponents", default="0.85,1.0,1.2,1.5")
    result.add_argument("--block-samples", type=int, default=12)
    result.add_argument("--output", type=Path)
    return result


def main() -> None:
    args = parser().parse_args()
    scales = [int(item) for item in args.scales.split(",") if item]
    exponents = [
        float(item) for item in args.height_exponents.split(",") if item
    ]
    payload = analyze(scales, exponents, args.block_samples)
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
