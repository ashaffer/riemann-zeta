"""Exact arithmetic and entropy checks for the QP Sidon-support no-go.

The main bound is deterministic although its proof uses the probabilistic
method.  For ``m`` frequencies in ``[-w,w]`` and an interval of length ``L``,
the local Sidon interpolation constant is at least

    m / (2*sqrt(m*log(8*(2 + L*w*m))) + 1).

This module only evaluates the proved formulas; it does not claim that the
special all-negative antipode has the universal interpolation cost.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from typing import Iterable


def local_sidon_entropy_lower(m: int, interval_length: float, max_frequency: float) -> float:
    """Return the random-sign lower bound for the local Sidon constant."""

    if m < 1 or interval_length < 0.0 or max_frequency <= 0.0:
        raise ValueError("require m>=1, interval_length>=0, and max_frequency>0")
    grid_upper = 2.0 + interval_length * max_frequency * m
    denominator = 2.0 * math.sqrt(m * math.log(8.0 * grid_upper)) + 1.0
    return m / denominator


def necessary_interval_length(m: int, max_frequency: float, constant: float) -> float:
    """Necessary interval length if the local Sidon constant is at most ``constant``.

    This is the exact inversion of :func:`local_sidon_entropy_lower`, with a
    zero result when the inverted lower bound is vacuous.
    """

    if m < 1 or max_frequency <= 0.0 or constant <= 0.0:
        raise ValueError("require m>=1, max_frequency>0, and constant>0")
    log_length = log_necessary_interval_length(m, max_frequency, constant)
    if log_length == -math.inf:
        return 0.0
    if log_length > math.log(float.fromhex("0x1.fffffffffffffp+1023")):
        return math.inf
    return math.exp(log_length)


def log_necessary_interval_length(m: int, max_frequency: float, constant: float) -> float:
    """Logarithm of :func:`necessary_interval_length`, without overflow."""

    if m < 1 or max_frequency <= 0.0 or constant <= 0.0:
        raise ValueError("require m>=1, max_frequency>0, and constant>0")
    positive_part = max(m / constant - 1.0, 0.0)
    exponent = positive_part * positive_part / (4.0 * m)
    if exponent <= math.log(16.0):
        return -math.inf
    correction = math.log1p(-16.0 * math.exp(-exponent)) if exponent < 750.0 else 0.0
    return exponent + correction - math.log(8.0 * max_frequency * m)


def florek_mass_bound(local_sidon_constant: float, epsilon: float) -> float:
    """Mass bound displayed by Florek's geometric correction proof.

    Page 118 gives ``16*C^4/epsilon`` for one correction.  Summing the
    displayed geometric sequence gives ``32*C^4/epsilon``.
    """

    if local_sidon_constant <= 0.0 or not 0.0 < epsilon <= 0.5:
        raise ValueError("require a positive constant and 0<epsilon<=1/2")
    return 32.0 * local_sidon_constant**4 / epsilon


def normalized_depth_guarantee(local_sidon_constant: float, epsilon: float) -> float:
    """Depth obtained by normalizing Florek's mass upper bound."""

    return 1.0 / florek_mass_bound(local_sidon_constant, epsilon)


def centered_log_independence_witness(
    coefficients: Iterable[int],
    odd_prime_bases: Iterable[int],
    power_exponents: Iterable[int],
) -> tuple[int, int] | None:
    """Return a nonzero prime valuation witnessing a nontrivial relation.

    For ``Y=a/2`` with odd ``a``, a putative relation among
    ``log(p_j**e_j/Y)`` first has 2-adic valuation ``sum coefficients``.
    If that vanishes, distinct odd prime bases expose a nonzero valuation.
    ``None`` is returned only for the zero coefficient vector.
    """

    coeffs = tuple(int(value) for value in coefficients)
    bases = tuple(int(value) for value in odd_prime_bases)
    exponents = tuple(int(value) for value in power_exponents)
    if not (len(coeffs) == len(bases) == len(exponents)):
        raise ValueError("coefficient, base, and exponent lists must have equal length")
    if len(set(bases)) != len(bases) or any(base <= 2 or base % 2 == 0 for base in bases):
        raise ValueError("bases must be distinct odd primes")
    if any(exponent < 1 for exponent in exponents):
        raise ValueError("power exponents must be positive")
    total = sum(coeffs)
    if total:
        return 2, total
    for coefficient, base, exponent in zip(coeffs, bases, exponents):
        valuation = coefficient * exponent
        if valuation:
            return base, valuation
    return None


@dataclass(frozen=True)
class ScaleRow:
    Y: int
    node_proxy: int
    band_length: float
    local_constant_lower: float
    target_constant: float
    log_necessary_length_for_target: float
    florek_depth_upper_from_lower_constant: float


def scale_row(
    Y: int,
    *,
    width: float = 0.2,
    aperture: float = 50.0 / 33.0,
    target_exponent: float = 0.019,
    epsilon: float = 0.5,
) -> ScaleRow:
    """Evaluate the theorem on the PNT proxy ``m=floor(Y/log Y)``."""

    if Y < 3:
        raise ValueError("Y must be at least 3")
    m = max(1, int(Y / math.log(Y)))
    length = Y**aperture - Y**0.01
    lower = local_sidon_entropy_lower(m, length, width)
    target_constant = Y**target_exponent
    log_needed = log_necessary_interval_length(m, width, target_constant)
    return ScaleRow(
        Y=Y,
        node_proxy=m,
        band_length=length,
        local_constant_lower=lower,
        target_constant=target_constant,
        log_necessary_length_for_target=log_needed,
        florek_depth_upper_from_lower_constant=normalized_depth_guarantee(lower, epsilon),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Y", nargs="+", type=int, default=[10**3, 10**4, 10**5, 10**6])
    parser.add_argument("--width", type=float, default=0.2)
    parser.add_argument("--aperture", type=float, default=50.0 / 33.0)
    parser.add_argument("--target-exponent", type=float, default=0.019)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = [
        asdict(
            scale_row(
                Y,
                width=args.width,
                aperture=args.aperture,
                target_exponent=args.target_exponent,
            )
        )
        for Y in args.Y
    ]
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
