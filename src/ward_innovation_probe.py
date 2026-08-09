#!/usr/bin/env python3
"""Finite tests of a von Mangoldt Ward identity and Markov innovations.

Two exact identities motivate this diagnostic:

    Lambda(n) log(n) + (Lambda * Lambda)(n) = (mu * log^2)(n),

and, for any Markov averaging operator P,

    P^k|f|^2 - |P^k f|^2
      = sum_(j=0)^(k-1) P^(k-1-j) Gamma(P^j f),
    Gamma(g) = P|g|^2 - |Pg|^2 >= 0.

The second calculation uses an exactly Markov, finite-grid box average and
the completed triangular prime discrepancy.  It is a numerical mechanism
probe, not a proof or an interval certificate.
"""

from __future__ import annotations

import argparse
import bisect
import math
from dataclasses import dataclass

from prime_log_screening_probe import Atom, atoms_for_block, pole_coefficient
from type2_block_mechanism_probe import _arithmetic_sieve, _primes_up_to


@dataclass(frozen=True)
class WardCheck:
    limit: int
    max_error: float
    worst_n: int


@dataclass(frozen=True)
class SemiprimeCheck:
    scale: int
    delta: float
    ell: float
    measured_coefficient: float
    measured_connected: float
    measured_anisotropy: float
    predicted_coefficient: float
    leading_connected: float
    predicted_anisotropy: float
    measured_minus_leading: float
    decomposition_error: float


@dataclass(frozen=True)
class InnovationCheck:
    order: int
    step: float
    raw_energy: float
    retained_energy: float
    innovation_energy: float
    retained_fraction: float
    identity_error: float
    minimum_gamma: float


def verify_ward_identity(limit: int = 5000) -> WardCheck:
    """Check the Dirichlet-convolution Ward identity through ``limit``."""
    if limit < 2:
        raise ValueError("limit must be at least two")
    mu, _, mangoldt, _ = _arithmetic_sieve(limit)
    lambda_convolution = [0.0] * (limit + 1)
    mobius_log_square = [0.0] * (limit + 1)
    for divisor in range(1, limit + 1):
        maximum_cofactor = limit // divisor
        lambda_divisor = mangoldt[divisor]
        mu_divisor = mu[divisor]
        for cofactor in range(1, maximum_cofactor + 1):
            product = divisor * cofactor
            if lambda_divisor:
                lambda_convolution[product] += (
                    lambda_divisor * mangoldt[cofactor]
                )
            if mu_divisor:
                mobius_log_square[product] += (
                    mu_divisor * math.log(cofactor) ** 2
                )

    max_error = 0.0
    worst_n = 1
    for value in range(2, limit + 1):
        left = (
            mangoldt[value] * math.log(value)
            + lambda_convolution[value]
        )
        error = abs(left - mobius_log_square[value])
        if error > max_error:
            max_error = error
            worst_n = value
    return WardCheck(limit, max_error, worst_n)


def semiprime_diagonal_check(
    scale: int = 10_000_000,
    delta: float = 0.1,
    ell: float = 0.4,
) -> SemiprimeCheck:
    """Compare a triangular semiprime diagonal with its PNT coefficient."""
    if scale < 100:
        raise ValueError("scale must be at least 100")
    if not 0.0 < delta < 0.5:
        raise ValueError("delta must lie in (0,1/2)")
    if ell <= 0.0:
        raise ValueError("ell must be positive")
    theta = 0.5 - delta
    p_min = scale**theta
    q_max = math.exp(ell) * scale / p_min
    primes = _primes_up_to(math.ceil(q_max))
    total = 0.0
    connected = 0.0
    anisotropy = 0.0
    for prime in primes:
        if prime <= p_min:
            continue
        q_lower = max(float(prime), scale * math.exp(-ell) / prime)
        q_upper = scale * math.exp(ell) / prime
        begin = bisect.bisect_right(primes, q_lower)
        end = bisect.bisect_left(primes, q_upper)
        for other in primes[begin:end]:
            offset = math.log(prime * other / scale)
            window = max(0.0, 1.0 - abs(offset) / ell)
            log_prime = math.log(prime)
            log_other = math.log(other)
            factor = window / (prime * other)
            total += (log_prime + log_other) ** 2 * factor
            connected += 4.0 * log_prime * log_other * factor
            anisotropy += (log_other - log_prime) ** 2 * factor

    normalization = math.log(scale) * ell
    measured = total / normalization
    measured_connected = connected / normalization
    measured_anisotropy = anisotropy / normalization
    predicted = math.log((1.0 - theta) / theta)
    leading = 4.0 * delta
    return SemiprimeCheck(
        scale,
        delta,
        ell,
        measured,
        measured_connected,
        measured_anisotropy,
        predicted,
        leading,
        predicted - leading,
        measured - leading,
        measured - measured_connected - measured_anisotropy,
    )


def evaluate_discrepancy(
    atoms: list[Atom], points: list[float], ell: float
) -> list[float]:
    """Evaluate the completed triangular discrepancy by an event sweep."""
    if not points:
        return []
    if any(right <= left for left, right in zip(points, points[1:])):
        raise ValueError("points must be strictly increasing")
    lower = points[0]
    upper = points[-1]
    inverse_ell = 1.0 / ell
    value_terms: list[float] = []
    slope_terms: list[float] = []
    events: list[tuple[float, float]] = []
    for atom in atoms:
        left_edge = atom.location - ell
        right_edge = atom.location + ell
        value_terms.append(
            atom.weight
            * max(0.0, 1.0 - abs(lower - atom.location) * inverse_ell)
        )
        if left_edge <= lower < atom.location:
            slope_terms.append(atom.weight * inverse_ell)
        elif atom.location <= lower < right_edge:
            slope_terms.append(-atom.weight * inverse_ell)
        for position, delta_slope in (
            (left_edge, atom.weight * inverse_ell),
            (atom.location, -2.0 * atom.weight * inverse_ell),
            (right_edge, atom.weight * inverse_ell),
        ):
            if lower < position <= upper:
                events.append((position, delta_slope))
    events.sort(key=lambda event: event[0])

    value = math.fsum(value_terms)
    slope = math.fsum(slope_terms)
    cursor = lower
    event_index = 0
    center = pole_coefficient(ell)
    answer: list[float] = []
    for point in points:
        while event_index < len(events) and events[event_index][0] <= point:
            position = events[event_index][0]
            value += slope * (position - cursor)
            cursor = position
            deltas: list[float] = []
            while (
                event_index < len(events)
                and events[event_index][0] == position
            ):
                deltas.append(events[event_index][1])
                event_index += 1
            slope += math.fsum(deltas)
        value += slope * (point - cursor)
        cursor = point
        answer.append(value - center * math.exp(point / 2.0))
    return answer


def _markov_average(values: list[float], width: int) -> list[float]:
    """Apply the uniform Markov average over ``width`` consecutive states."""
    if width < 1 or width > len(values):
        raise ValueError("invalid averaging width")
    prefix = [0.0]
    running = 0.0
    for value in values:
        running += value
        prefix.append(running)
    return [
        (prefix[index + width] - prefix[index]) / width
        for index in range(len(values) - width + 1)
    ]


def innovation_check(
    values: list[float], sample_spacing: float, width: int, order: int
) -> InnovationCheck:
    """Verify the iterated carré-du-champ identity on a finite grid."""
    if order < 1:
        raise ValueError("order must be positive")
    if len(values) <= order * (width - 1):
        raise ValueError("not enough input samples for this order")

    powers: list[list[float]] = [values]
    for _ in range(order):
        powers.append(_markov_average(powers[-1], width))

    raw = [value * value for value in values]
    for _ in range(order):
        raw = _markov_average(raw, width)
    retained = [value * value for value in powers[-1]]
    innovation = [left - right for left, right in zip(raw, retained)]

    accumulated = [0.0] * len(innovation)
    minimum_gamma = math.inf
    for level in range(order):
        square = [value * value for value in powers[level]]
        averaged_square = _markov_average(square, width)
        next_square = [value * value for value in powers[level + 1]]
        gamma = [
            left - right for left, right in zip(averaged_square, next_square)
        ]
        minimum_gamma = min(minimum_gamma, min(gamma))
        for _ in range(order - 1 - level):
            gamma = _markov_average(gamma, width)
        accumulated = [
            left + right for left, right in zip(accumulated, gamma)
        ]

    identity_error = max(
        abs(left - right) for left, right in zip(innovation, accumulated)
    )
    raw_energy = math.fsum(raw) / len(raw)
    retained_energy = math.fsum(retained) / len(retained)
    innovation_energy = math.fsum(innovation) / len(innovation)
    return InnovationCheck(
        order,
        sample_spacing * (width - 1),
        raw_energy,
        retained_energy,
        innovation_energy,
        retained_energy / raw_energy,
        identity_error,
        minimum_gamma,
    )


def prime_innovation_scan(
    lower: float = 8.0,
    upper: float = 10.0,
    ell: float = 0.5,
    step: float = 0.1,
    spacing: float = 0.01,
    orders: tuple[int, ...] = (1, 4, 16, 32),
) -> list[InnovationCheck]:
    """Run innovations on the completed prime discrepancy over one block."""
    ratio = step / spacing
    rounded = round(ratio)
    if not math.isclose(ratio, rounded, rel_tol=0.0, abs_tol=1.0e-12):
        raise ValueError("step must be an integer multiple of spacing")
    width = int(rounded) + 1
    maximum_order = max(orders)
    input_upper = upper + maximum_order * step
    point_count = round((input_upper - lower) / spacing) + 1
    output_count = round((upper - lower) / spacing) + 1
    points = [lower + index * spacing for index in range(point_count)]
    atoms = atoms_for_block(lower, input_upper, ell)
    values = evaluate_discrepancy(atoms, points, ell)
    return [
        innovation_check(
            values[: output_count + order * (width - 1)],
            spacing,
            width,
            order,
        )
        for order in orders
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ward-limit", type=int, default=5000)
    parser.add_argument("--scale", type=int, default=10_000_000)
    parser.add_argument("--delta", type=float, default=0.1)
    args = parser.parse_args()

    ward = verify_ward_identity(args.ward_limit)
    print(
        f"Ward n<={ward.limit}: max_error={ward.max_error:.3g} "
        f"at n={ward.worst_n}"
    )
    semiprime = semiprime_diagonal_check(args.scale, args.delta)
    print(
        f"semiprime X={semiprime.scale} delta={semiprime.delta:g}: "
        f"measured={semiprime.measured_coefficient:.9g} "
        f"predicted={semiprime.predicted_coefficient:.9g} "
        f"connected={semiprime.measured_connected:.9g} "
        f"leading={semiprime.leading_connected:.9g} "
        f"anisotropy={semiprime.measured_anisotropy:.9g} "
        f"predicted_anisotropy={semiprime.predicted_anisotropy:.9g}"
    )
    for row in prime_innovation_scan():
        print(
            f"innovation k={row.order} h={row.step:g}: "
            f"raw={row.raw_energy:.9g} retained={row.retained_energy:.9g} "
            f"innov={row.innovation_energy:.9g} "
            f"retained/raw={row.retained_fraction:.6g} "
            f"identity_error={row.identity_error:.3g} "
            f"min_Gamma={row.minimum_gamma:.3g}"
        )


if __name__ == "__main__":
    main()
