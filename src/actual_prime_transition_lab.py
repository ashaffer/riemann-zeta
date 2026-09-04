#!/usr/bin/env python3
"""Actual-prime consecutive-transition laboratory.

This module is a deterministic conjecture-discovery tool for the live
high-denominator gap-coherence problem.  It deliberately keeps apart:

* exact logarithmic Voronoi cell masses;
* the symmetrized consecutive-gap trapezoid;
* pole and near-residue sectors of the successor transition; and
* additive and multiplicative (character) spectra.

All sums are finite sums over primes produced by a segmented sieve.  Floating
point numbers enter only through logarithms, window integrals, and roots of
unity.  The word ``exact`` below refers to the displayed finite definitions,
not to exact-real computer arithmetic and not to an asymptotic theorem about
the primes.
"""

from __future__ import annotations

import argparse
import cmath
from dataclasses import asdict, dataclass
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable, Sequence


SCHEMA = "zeta23.actual-prime-transition-lab.v1"
TAU = 2.0 * math.pi


@dataclass(frozen=True)
class LabConfig:
    """Configuration for a multiplicative-shell scan."""

    start: int = 100_000
    ratio: float = 2.0
    window: str = "tent"
    q_min: int = 11
    q_max: int = 97
    near_radius: int = 3
    top_modes: int = 5
    segment_size: int = 1 << 18
    heights: tuple[float, ...] = ()
    curvature_scale: float = 0.5
    max_height_blocks: int = 256
    height_detail_blocks: int = 12
    rough_presieve: bool = True
    wheel_steps: tuple[int, ...] = (2, 6, 30)

    @property
    def end(self) -> int:
        return int(math.floor(self.start * self.ratio))

    def validate(self) -> None:
        if self.start < 5:
            raise ValueError("start must be at least 5")
        if not math.isfinite(self.ratio) or self.ratio <= 1.0:
            raise ValueError("ratio must be finite and greater than one")
        if self.end <= self.start + 2:
            raise ValueError("the shell must contain at least three integers")
        if self.window not in {"tent", "flat"}:
            raise ValueError("window must be 'tent' or 'flat'")
        if self.q_min < 2 or self.q_max < self.q_min:
            raise ValueError("invalid modulus interval")
        if self.q_max >= self.start:
            raise ValueError("q_max must be below the shell start (unit residues)")
        if self.near_radius < 0:
            raise ValueError("near_radius must be nonnegative")
        if self.top_modes < 1:
            raise ValueError("top_modes must be positive")
        if self.segment_size < 128:
            raise ValueError("segment_size must be at least 128")
        if self.curvature_scale <= 0.0 or not math.isfinite(self.curvature_scale):
            raise ValueError("curvature_scale must be positive and finite")
        if self.max_height_blocks < 1 or self.height_detail_blocks < 0:
            raise ValueError("invalid height block limits")
        if any((not math.isfinite(t) or t <= 0.0) for t in self.heights):
            raise ValueError("heights must be positive and finite")
        if not isinstance(self.rough_presieve, bool):
            raise ValueError("rough_presieve must be Boolean")
        if any(step <= 0 or step % 2 for step in self.wheel_steps):
            raise ValueError("wheel_steps must be positive even integers")

    @classmethod
    def from_json(cls, value: dict[str, Any]) -> "LabConfig":
        fields = dict(value)
        fields["heights"] = tuple(float(t) for t in fields.get("heights", ()))
        fields["wheel_steps"] = tuple(int(step) for step in fields.get("wheel_steps", (2, 6, 30)))
        return cls(**fields)


@dataclass(frozen=True)
class PrimeNode:
    prime: int
    log_coordinate: float
    window_value: float
    voronoi_weight: float


@dataclass(frozen=True)
class GapEdge:
    left_prime: int
    right_prime: int
    gap: int
    log_gap: float
    left_weight: float
    right_weight: float

    @property
    def mass(self) -> float:
        return self.left_weight + self.right_weight

    @property
    def midpoint(self) -> float:
        return 0.5 * (self.left_prime + self.right_prime)


@dataclass(frozen=True)
class ShellData:
    config: LabConfig
    primes: tuple[int, ...]
    nodes: tuple[PrimeNode, ...]
    edges: tuple[GapEdge, ...]


def _simple_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    mark = bytearray(b"\x01") * (limit + 1)
    mark[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if mark[p]:
            start = p * p
            mark[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [n for n in range(2, limit + 1) if mark[n]]


def segmented_primes(low: int, high: int, segment_size: int = 1 << 18) -> list[int]:
    """Return all primes in the half-open interval ``[low, high)``."""

    if high <= low or high <= 2:
        return []
    low = max(low, 2)
    base = _simple_primes(math.isqrt(high - 1))
    answer: list[int] = []
    for segment_low in range(low, high, segment_size):
        segment_high = min(high, segment_low + segment_size)
        mark = bytearray(b"\x01") * (segment_high - segment_low)
        for p in base:
            first = max(p * p, ((segment_low + p - 1) // p) * p)
            if first >= segment_high:
                continue
            mark[first - segment_low : segment_high - segment_low : p] = b"\x00" * (
                (segment_high - 1 - first) // p + 1
            )
        answer.extend(segment_low + i for i, flag in enumerate(mark) if flag)
    return answer


def _primes_with_two_neighbors(
    start: int, end: int, segment_size: int
) -> tuple[int, ...]:
    margin = max(256, 2 * math.isqrt(end) + 16)
    while True:
        low = max(2, start - margin)
        high = end + margin + 1
        primes = segmented_primes(low, high, segment_size)
        lower = sum(p < start for p in primes)
        upper = sum(p > end for p in primes)
        if lower >= 2 and upper >= 2:
            first = next(i for i, p in enumerate(primes) if p >= start) - 2
            last_inside = max(i for i, p in enumerate(primes) if p <= end)
            return tuple(primes[first : last_inside + 3])
        margin *= 2


def window_value(kind: str, u: float, length: float) -> float:
    if u < 0.0 or u > length:
        return 0.0
    if kind == "flat":
        return 1.0
    if kind != "tent":
        raise ValueError(kind)
    if u <= 0.5 * length:
        return 2.0 * u / length
    return 2.0 * (length - u) / length


def _window_primitive(kind: str, u: float, length: float) -> float:
    u = min(max(u, 0.0), length)
    if kind == "flat":
        return u
    if kind != "tent":
        raise ValueError(kind)
    midpoint = 0.5 * length
    if u <= midpoint:
        return u * u / length
    return length / 4.0 + 2.0 * (u - midpoint) - (u * u - midpoint**2) / length


def window_integral(kind: str, left: float, right: float, length: float) -> float:
    if right <= left:
        return 0.0
    clipped_left = min(max(left, 0.0), length)
    clipped_right = min(max(right, 0.0), length)
    if clipped_right <= clipped_left:
        return 0.0
    return _window_primitive(kind, clipped_right, length) - _window_primitive(
        kind, clipped_left, length
    )


def build_shell(config: LabConfig) -> ShellData:
    """Build exact finite Voronoi nodes and symmetrized gap edges."""

    config.validate()
    primes = _primes_with_two_neighbors(config.start, config.end, config.segment_size)
    length = math.log(config.end / config.start)
    coordinates = [math.log(p / config.start) for p in primes]
    values = [window_value(config.window, u, length) for u in coordinates]

    nodes: list[PrimeNode] = []
    for i in range(1, len(primes) - 1):
        cell_left = 0.5 * (coordinates[i - 1] + coordinates[i])
        cell_right = 0.5 * (coordinates[i] + coordinates[i + 1])
        weight = window_integral(config.window, cell_left, cell_right, length)
        if weight > 0.0:
            nodes.append(PrimeNode(primes[i], coordinates[i], values[i], weight))

    edges: list[GapEdge] = []
    for i in range(len(primes) - 1):
        delta = coordinates[i + 1] - coordinates[i]
        left_weight = 0.5 * delta * values[i]
        right_weight = 0.5 * delta * values[i + 1]
        if left_weight + right_weight > 0.0:
            edges.append(
                GapEdge(
                    left_prime=primes[i],
                    right_prime=primes[i + 1],
                    gap=primes[i + 1] - primes[i],
                    log_gap=delta,
                    left_weight=left_weight,
                    right_weight=right_weight,
                )
            )
    if not nodes or not edges:
        raise RuntimeError("the selected shell produced no weighted prime data")
    return ShellData(config, primes, tuple(nodes), tuple(edges))


def _primitive_root(prime: int) -> int:
    phi = prime - 1
    factors: list[int] = []
    remaining = phi
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append(remaining)
    for candidate in range(2, prime):
        if all(pow(candidate, phi // factor, prime) != 1 for factor in factors):
            return candidate
    raise RuntimeError(f"no primitive root found modulo {prime}")


def _complex_json(value: complex) -> dict[str, float]:
    real = 0.0 if abs(value.real) < 5e-16 else value.real
    imag = 0.0 if abs(value.imag) < 5e-16 else value.imag
    return {"real": real, "imag": imag, "abs": abs(value)}


def _additive_spectrum(histogram: Sequence[float], prime: int) -> list[complex]:
    return [
        sum(
            weight * cmath.exp(1j * TAU * mode * residue / prime)
            for residue, weight in enumerate(histogram)
            if weight
        )
        for mode in range(prime)
    ]


def _character_spectrum(histogram: Sequence[float], prime: int) -> list[complex]:
    generator = _primitive_root(prime)
    log_table = [0] * prime
    residue = 1
    for exponent in range(prime - 1):
        log_table[residue] = exponent
        residue = residue * generator % prime
    return [
        sum(
            histogram[r]
            * cmath.exp(-1j * TAU * index * log_table[r] / (prime - 1))
            for r in range(1, prime)
            if histogram[r]
        )
        for index in range(prime - 1)
    ]


def _relative_error(left: complex | float, right: complex | float) -> float:
    return abs(left - right) / max(1.0, abs(left), abs(right))


def _spectrum_summary(histogram: Sequence[float], prime: int) -> tuple[dict[str, Any], list[complex]]:
    mass = sum(histogram)
    if mass <= 0.0:
        raise ValueError("spectral histogram has zero mass")
    additive = _additive_spectrum(histogram, prime)
    principal = -mass / (prime - 1)
    residual = [0j] + [additive[a] - principal for a in range(1, prime)]
    max_mode = max(range(1, prime), key=lambda a: (abs(residual[a]), -a))
    raw_max_mode = max(range(1, prime), key=lambda a: (abs(additive[a]), -a))
    additive_energy = sum(abs(value) ** 2 for value in additive)
    additive_parseval = prime * sum(weight * weight for weight in histogram)

    characters = _character_spectrum(histogram, prime)
    character_energy = sum(abs(value) ** 2 for value in characters)
    character_parseval = (prime - 1) * sum(
        histogram[r] ** 2 for r in range(1, prime)
    )
    nonprincipal_char_energy = sum(abs(value) ** 2 for value in characters[1:])
    nonprincipal_char_max = max((abs(value) for value in characters[1:]), default=0.0)
    summary = {
        "mass": mass,
        "principal_additive_coefficient": principal,
        "principal_normalized_abs": abs(principal) / mass,
        "raw_max": {
            "mode": raw_max_mode,
            "coefficient": _complex_json(additive[raw_max_mode]),
            "normalized_abs": abs(additive[raw_max_mode]) / mass,
        },
        "principal_subtracted_max": {
            "mode": max_mode,
            "coefficient": _complex_json(residual[max_mode]),
            "normalized_abs": abs(residual[max_mode]) / mass,
        },
        "additive_nonzero_l2_normalized": math.sqrt(
            sum(abs(additive[a]) ** 2 for a in range(1, prime)) / (prime - 1)
        )
        / mass,
        "additive_principal_subtracted_l2_normalized": math.sqrt(
            sum(abs(residual[a]) ** 2 for a in range(1, prime)) / (prime - 1)
        )
        / mass,
        "character": {
            "principal": _complex_json(characters[0]),
            "nonprincipal_energy_normalized": nonprincipal_char_energy / (mass * mass),
            "nonprincipal_rms_normalized": math.sqrt(
                nonprincipal_char_energy / max(1, prime - 2)
            )
            / mass,
            "nonprincipal_max_normalized": nonprincipal_char_max / mass,
        },
        "checks": {
            "additive_parseval_relative_error": _relative_error(
                additive_energy, additive_parseval
            ),
            "character_parseval_relative_error": _relative_error(
                character_energy, character_parseval
            ),
        },
    }
    return summary, additive


def _top_mode_indices(values: Sequence[complex], count: int) -> list[int]:
    return sorted(range(1, len(values)), key=lambda a: (-abs(values[a]), a))[:count]


def _sector_bins(
    prime: int,
    mode: int,
    near_radius: int,
    left_by_difference: Sequence[Sequence[float]],
    right_by_difference: Sequence[Sequence[float]],
    mass_by_difference: Sequence[float],
    count_by_difference: Sequence[int],
) -> list[dict[str, Any]]:
    radius = min(near_radius, (prime - 1) // 2)
    inverse_mode = pow(mode, -1, prime)
    phases = [cmath.exp(1j * TAU * mode * r / prime) for r in range(prime)]
    answer: list[dict[str, Any]] = []
    for distance in range(radius + 1):
        signed_residues = (0,) if distance == 0 else (distance, -distance)
        coefficient = 0j
        mass = 0.0
        count = 0
        physical_differences: list[int] = []
        for signed in signed_residues:
            difference = (signed * inverse_mode) % prime
            physical_differences.append(difference)
            increment = cmath.exp(1j * TAU * mode * difference / prime)
            coefficient += sum(
                phases[r]
                * (
                    left_by_difference[difference][r]
                    + increment * right_by_difference[difference][r]
                )
                for r in range(prime)
            )
            mass += mass_by_difference[difference]
            count += count_by_difference[difference]
        answer.append(
            {
                "phase_increment_distance": distance,
                "gap_residues": physical_differences,
                "edge_count": count,
                "mass": mass,
                "coefficient": _complex_json(coefficient),
            }
        )
    return answer


def _modulus_report(shell: ShellData, prime: int) -> dict[str, Any]:
    if shell.config.near_radius >= prime / 2:
        effective_near_radius = (prime - 1) // 2
    else:
        effective_near_radius = shell.config.near_radius

    voronoi_hist = [0.0] * prime
    for node in shell.nodes:
        voronoi_hist[node.prime % prime] += node.voronoi_weight

    sym_hist = [0.0] * prime
    left_by_difference = [[0.0] * prime for _ in range(prime)]
    right_by_difference = [[0.0] * prime for _ in range(prime)]
    mass_by_difference = [0.0] * prime
    count_by_difference = [0] * prime
    transition_ratio_hist = [0.0] * prime
    for edge in shell.edges:
        left_residue = edge.left_prime % prime
        right_residue = edge.right_prime % prime
        difference = edge.gap % prime
        sym_hist[left_residue] += edge.left_weight
        sym_hist[right_residue] += edge.right_weight
        left_by_difference[difference][left_residue] += edge.left_weight
        right_by_difference[difference][left_residue] += edge.right_weight
        mass_by_difference[difference] += edge.mass
        count_by_difference[difference] += 1
        ratio = right_residue * pow(left_residue, -1, prime) % prime
        transition_ratio_hist[ratio] += edge.mass

    voronoi_summary, voronoi_additive = _spectrum_summary(voronoi_hist, prime)
    sym_summary, sym_additive = _spectrum_summary(sym_hist, prime)
    sym_mass = sym_summary["mass"]
    sym_principal = -sym_mass / (prime - 1)
    sym_residual = [0j] + [sym_additive[a] - sym_principal for a in range(1, prime)]

    pole_hist = [
        left_by_difference[0][r] + right_by_difference[0][r]
        for r in range(prime)
    ]
    pole_additive = _additive_spectrum(pole_hist, prime)
    pole_mass = mass_by_difference[0]
    pole_max_mode = max(range(1, prime), key=lambda a: (abs(pole_additive[a]), -a))

    transition_characters = _character_spectrum(transition_ratio_hist, prime)
    transition_char_energy = sum(abs(value) ** 2 for value in transition_characters)
    transition_parseval = (prime - 1) * sum(
        transition_ratio_hist[r] ** 2 for r in range(1, prime)
    )
    pole_from_characters = sum(transition_characters) / (prime - 1)

    top_indices = _top_mode_indices(sym_residual, shell.config.top_modes)
    top_modes: list[dict[str, Any]] = []
    all_sector_bins: dict[int, list[dict[str, Any]]] = {}
    max_near_mass = (-1.0, 0)
    max_near_signed = (-1.0, 0, 0j)
    for mode in range(1, prime):
        bins = _sector_bins(
            prime,
            mode,
            effective_near_radius,
            left_by_difference,
            right_by_difference,
            mass_by_difference,
            count_by_difference,
        )
        cumulative_mass = sum(entry["mass"] for entry in bins)
        cumulative_coefficient = sum(
            complex(entry["coefficient"]["real"], entry["coefficient"]["imag"])
            for entry in bins
        )
        if (cumulative_mass, -mode) > (max_near_mass[0], -max_near_mass[1]):
            max_near_mass = (cumulative_mass, mode)
        if (abs(cumulative_coefficient), -mode) > (
            max_near_signed[0],
            -max_near_signed[1],
        ):
            max_near_signed = (abs(cumulative_coefficient), mode, cumulative_coefficient)
        if mode in top_indices:
            all_sector_bins[mode] = bins

    for mode in top_indices:
        top_modes.append(
            {
                "mode": mode,
                "sym_coefficient": _complex_json(sym_additive[mode]),
                "sym_principal_subtracted": _complex_json(sym_residual[mode]),
                "sym_principal_subtracted_normalized_abs": abs(sym_residual[mode])
                / sym_mass,
                "voronoi_coefficient": _complex_json(voronoi_additive[mode]),
                "pole_coefficient": _complex_json(pole_additive[mode]),
                "phase_increment_sectors": all_sector_bins[mode],
            }
        )

    nonprincipal_transition_energy = sum(
        abs(value) ** 2 for value in transition_characters[1:]
    )
    renewal = 1.0 / prime
    fixed_small_gap_capture: dict[str, Any] | None = None
    maximum_gap = max(edge.gap for edge in shell.edges)
    if prime > maximum_gap and effective_near_radius > 0:
        half_mode = (prime - 1) // 2
        half_bins = _sector_bins(
            prime,
            half_mode,
            effective_near_radius,
            left_by_difference,
            right_by_difference,
            mass_by_difference,
            count_by_difference,
        )
        captured_mass = sum(entry["mass"] for entry in half_bins)
        small_gap_mass = sum(
            edge.mass
            for edge in shell.edges
            if edge.gap <= 2 * effective_near_radius
        )
        fixed_small_gap_capture = {
            "mode": half_mode,
            "identity": (
                "for even g<q, mode=(q-1)/2 has centered phase distance g/2"
            ),
            "maximum_gap_below_q": True,
            "small_gap_cutoff": 2 * effective_near_radius,
            "captured_mass": captured_mass,
            "small_gap_mass": small_gap_mass,
            "mass_fraction": captured_mass / sym_mass,
            "relative_identity_error": _relative_error(captured_mass, small_gap_mass),
        }
    wheel_captures: list[dict[str, Any]] = []
    if prime > maximum_gap and effective_near_radius > 0:
        for wheel_step in shell.config.wheel_steps:
            if wheel_step % prime == 0 or wheel_step * effective_near_radius >= prime:
                continue
            wheel_mode = pow(wheel_step, -1, prime)
            wheel_bins = _sector_bins(
                prime,
                wheel_mode,
                effective_near_radius,
                left_by_difference,
                right_by_difference,
                mass_by_difference,
                count_by_difference,
            )
            captured_mass = sum(entry["mass"] for entry in wheel_bins)
            literal_mass = sum(
                edge.mass
                for edge in shell.edges
                if edge.gap % wheel_step == 0
                and edge.gap <= wheel_step * effective_near_radius
            )
            wheel_captures.append(
                {
                    "wheel_step": wheel_step,
                    "mode": wheel_mode,
                    "identity": (
                        "mode*wheel_step = 1 mod q; with q above every even gap, "
                        "radius R captures exactly wheel_step,2*wheel_step,...,R*wheel_step"
                    ),
                    "captured_mass": captured_mass,
                    "literal_wheel_gap_mass": literal_mass,
                    "mass_fraction": captured_mass / sym_mass,
                    "relative_identity_error": _relative_error(
                        captured_mass, literal_mass
                    ),
                }
            )
    distinguished_modes: list[dict[str, Any]] = []
    if prime % 4 == 3 and prime > 4:
        cousin_mode = (prime + 1) // 4
        gap_four_coefficient = sum(
            edge.left_weight
            * cmath.exp(1j * TAU * cousin_mode * edge.left_prime / prime)
            + edge.right_weight
            * cmath.exp(1j * TAU * cousin_mode * edge.right_prime / prime)
            for edge in shell.edges
            if edge.gap == 4
        )
        gap_four_mass = sum(edge.mass for edge in shell.edges if edge.gap == 4)
        cousin_bins = _sector_bins(
            prime,
            cousin_mode,
            effective_near_radius,
            left_by_difference,
            right_by_difference,
            mass_by_difference,
            count_by_difference,
        )
        distinguished_modes.append(
            {
                "name": "gap_four_residue_one",
                "mode": cousin_mode,
                "identity": "4*mode = q+1, so the gap-four phase increment is 1/q",
                "sym_principal_subtracted_normalized_abs": abs(
                    sym_residual[cousin_mode]
                )
                / sym_mass,
                "gap_four_edge_count": sum(edge.gap == 4 for edge in shell.edges),
                "gap_four_mass": gap_four_mass,
                "gap_four_mass_fraction": gap_four_mass / sym_mass,
                "gap_four_coefficient": _complex_json(gap_four_coefficient),
                "gap_four_signed_normalized_abs": abs(gap_four_coefficient) / sym_mass,
                "phase_increment_sectors": cousin_bins,
            }
        )
    return {
        "q": prime,
        "modes_scanned": prime - 1,
        "effective_near_radius": effective_near_radius,
        "voronoi": voronoi_summary,
        "symmetrized_gap": sym_summary,
        "transition": {
            "mass": sym_mass,
            "pole_edge_count": count_by_difference[0],
            "pole_mass": pole_mass,
            "pole_mass_fraction": pole_mass / sym_mass,
            "pole_signed_max": {
                "mode": pole_max_mode,
                "coefficient": _complex_json(pole_additive[pole_max_mode]),
                "normalized_abs": abs(pole_additive[pole_max_mode]) / sym_mass,
            },
            "character": {
                "principal": _complex_json(transition_characters[0]),
                "nonprincipal_energy_normalized": nonprincipal_transition_energy
                / (sym_mass * sym_mass),
                "nonprincipal_rms_normalized": math.sqrt(
                    nonprincipal_transition_energy / max(1, prime - 2)
                )
                / sym_mass,
                "pole_reconstruction": _complex_json(pole_from_characters),
            },
        },
        "near_residue": {
            "definition": "circular distance of a*(p_next-p) modulo q",
            "max_cumulative_mass": {
                "mode": max_near_mass[1],
                "mass": max_near_mass[0],
                "mass_fraction": max_near_mass[0] / sym_mass,
            },
            "max_cumulative_signed": {
                "mode": max_near_signed[1],
                "coefficient": _complex_json(max_near_signed[2]),
                "normalized_abs": max_near_signed[0] / sym_mass,
            },
            "fixed_small_gap_capture": fixed_small_gap_capture,
            "wheel_captures": wheel_captures,
        },
        "renewal_q_inverse_baseline": {
            "normalized_scale": renewal,
            "sym_principal_subtracted_max_ratio": sym_summary[
                "principal_subtracted_max"
            ]["normalized_abs"]
            / renewal,
            "sym_principal_subtracted_l2_ratio": sym_summary[
                "additive_principal_subtracted_l2_normalized"
            ]
            / renewal,
            "transition_character_rms_ratio": math.sqrt(
                nonprincipal_transition_energy / max(1, prime - 2)
            )
            / sym_mass
            / renewal,
        },
        "top_modes": top_modes,
        "distinguished_modes": distinguished_modes,
        "checks": {
            "sym_histogram_mass_relative_error": _relative_error(
                sum(sym_hist), sum(edge.mass for edge in shell.edges)
            ),
            "pole_histogram_mass_relative_error": _relative_error(
                sum(pole_hist), pole_mass
            ),
            "pole_character_reconstruction_relative_error": _relative_error(
                pole_from_characters, pole_mass
            ),
            "transition_character_parseval_relative_error": _relative_error(
                transition_char_energy, transition_parseval
            ),
        },
    }


def _segmented_smallest_sieving_prime(
    low: int, high: int, sieving_primes: Sequence[int]
) -> list[int]:
    """Smallest factor from ``sieving_primes`` on the half-open interval.

    Zero means that no supplied prime divides the integer; it does not claim
    primality.  This is exactly the information needed for every q-rough
    stage with q at most the largest supplied prime.
    """

    smallest = [0] * (high - low)
    for prime in sieving_primes:
        first = ((low + prime - 1) // prime) * prime
        for value in range(first, high, prime):
            index = value - low
            if smallest[index] == 0:
                smallest[index] = prime
    return smallest


def _rough_presieve_reports(
    config: LabConfig, moduli: Sequence[int]
) -> dict[int, dict[str, Any]]:
    """Return exact finite ledgers for integers with least factor >= q."""

    margin = max(1024, 8 * max(moduli))
    low = max(2, config.start - margin)
    high = config.end + margin + 1
    sieving_primes = _simple_primes(max(moduli))
    smallest = _segmented_smallest_sieving_prime(low, high, sieving_primes)
    length = math.log(config.end / config.start)
    physical_span = config.end - config.start
    expected_window_mass = window_integral(config.window, 0.0, length, length)
    reports: dict[int, dict[str, Any]] = {}

    for q in moduli:
        points = [
            value
            for value in range(low, high)
            if smallest[value - low] == 0 or smallest[value - low] >= q
        ]
        below = sum(value < config.start for value in points)
        above = sum(value > config.end for value in points)
        if below < 2 or above < 2:
            raise RuntimeError("rough pre-sieve margin did not contain two neighbors")
        first = next(i for i, value in enumerate(points) if value >= config.start) - 2
        last_inside = max(i for i, value in enumerate(points) if value <= config.end)
        points = points[first : last_inside + 3]
        coordinates = [math.log(value / config.start) for value in points]
        values = [window_value(config.window, u, length) for u in coordinates]

        total_voronoi_mass = 0.0
        divisible_voronoi_mass = 0.0
        divisible_node_count = 0
        weighted_node_count = 0
        for i in range(1, len(points) - 1):
            cell_left = 0.5 * (coordinates[i - 1] + coordinates[i])
            cell_right = 0.5 * (coordinates[i] + coordinates[i + 1])
            weight = window_integral(config.window, cell_left, cell_right, length)
            if weight <= 0.0:
                continue
            weighted_node_count += 1
            total_voronoi_mass += weight
            if points[i] % q == 0:
                divisible_node_count += 1
                divisible_voronoi_mass += weight

        gaps = [
            right - left
            for left, right in zip(points, points[1:])
            if config.start <= 0.5 * (left + right) <= config.end
        ]
        interior_count = sum(config.start <= value <= config.end for value in points)
        mean_gap = sum(gaps) / len(gaps)
        second_moment = sum(gap * gap for gap in gaps) / len(gaps)
        fraction = divisible_voronoi_mass / total_voronoi_mass
        reports[q] = {
            "definition": "integers n with no prime factor below q",
            "interior_point_count": interior_count,
            "weighted_node_count": weighted_node_count,
            "divisible_node_count": divisible_node_count,
            "total_voronoi_mass": total_voronoi_mass,
            "divisible_voronoi_mass": divisible_voronoi_mass,
            "divisible_mass_fraction": fraction,
            "baselines": {
                "q_inverse": 1.0 / q,
                "q_inverse_sqrt": 1.0 / math.sqrt(q),
                "ratio_to_q_inverse": fraction * q,
                "ratio_to_q_inverse_sqrt": fraction * math.sqrt(q),
            },
            "rough_gaps": {
                "gap_count": len(gaps),
                "mean": mean_gap,
                "second_moment": second_moment,
                "second_moment_over_mean_squared": second_moment / (mean_gap * mean_gap),
                "sum_squares_per_shell_length": sum(gap * gap for gap in gaps)
                / physical_span,
            },
            "checks": {
                "voronoi_partition_relative_error": _relative_error(
                    total_voronoi_mass, expected_window_mass
                ),
                "divisible_mass_le_total": divisible_voronoi_mass
                <= total_voronoi_mass + 2e-15,
            },
        }
    return reports


def _centered_unit_difference(left: float, right: float) -> float:
    return (left - right + 0.5) % 1.0 - 0.5


def _best_rational_frequency(
    alpha: float, block_length: float, moduli: Sequence[int]
) -> tuple[int, int, float, float]:
    fractional = alpha % 1.0
    best: tuple[float, int, int, float] | None = None
    for q in moduli:
        center = fractional * q
        candidates = {int(math.floor(center)) % q, int(math.ceil(center)) % q}
        for mode in candidates:
            if mode == 0:
                continue
            error = abs(_centered_unit_difference(fractional, mode / q))
            drift = error * block_length
            key = (q * drift, q, mode, error)
            if best is None or key < best:
                best = key
    if best is None:
        raise RuntimeError("no nonzero rational mode was available")
    cell_ratio, q, mode, error = best
    return q, mode, error, cell_ratio


def _edge_phase_sum(edges: Iterable[GapEdge], frequency: float) -> complex:
    return sum(
        edge.left_weight * cmath.exp(1j * TAU * frequency * edge.left_prime)
        + edge.right_weight * cmath.exp(1j * TAU * frequency * edge.right_prime)
        for edge in edges
    )


def _common_height_report(
    shell: ShellData, height: float, moduli: Sequence[int]
) -> dict[str, Any]:
    span = shell.config.end - shell.config.start
    nominal = shell.config.curvature_scale * shell.config.start / math.sqrt(height)
    minimum_for_cap = span / shell.config.max_height_blocks
    block_length = max(2.0, nominal, minimum_for_cap)
    coarsened = block_length > max(2.0, nominal) * (1.0 + 1e-15)
    block_count = max(1, int(math.ceil(span / block_length)))
    block_length = span / block_count

    details: list[dict[str, Any]] = []
    exact_aggregate = 0j
    rational_aggregate = 0j
    total_mass = 0.0
    selected_counts: dict[int, int] = {}
    passing_cells = 0
    for block_index in range(block_count):
        left = shell.config.start + block_index * block_length
        right = (
            shell.config.end
            if block_index + 1 == block_count
            else shell.config.start + (block_index + 1) * block_length
        )
        block_edges = [edge for edge in shell.edges if left <= edge.midpoint < right]
        if not block_edges:
            continue
        center = 0.5 * (left + right)
        alpha = height / (TAU * center)
        q, mode, frequency_error, cell_ratio = _best_rational_frequency(
            alpha, right - left, moduli
        )
        integer_part = round(alpha - mode / q)
        rational_frequency = integer_part + mode / q
        alignment = cmath.exp(
            1j
            * (
                height * math.log(center / shell.config.start)
                - TAU * rational_frequency * center
            )
        )
        rational_sum = alignment * _edge_phase_sum(block_edges, rational_frequency)
        exact_sum = sum(
            edge.left_weight
            * cmath.exp(1j * height * math.log(edge.left_prime / shell.config.start))
            + edge.right_weight
            * cmath.exp(1j * height * math.log(edge.right_prime / shell.config.start))
            for edge in block_edges
        )
        mass = sum(edge.mass for edge in block_edges)
        exact_aggregate += exact_sum
        rational_aggregate += rational_sum
        total_mass += mass
        selected_counts[q] = selected_counts.get(q, 0) + 1
        if cell_ratio <= 1.0:
            passing_cells += 1

        pole_mass = sum(edge.mass for edge in block_edges if edge.gap % q == 0)
        near_mass = sum(
            edge.mass
            for edge in block_edges
            if min((mode * edge.gap) % q, (-mode * edge.gap) % q)
            <= shell.config.near_radius
        )
        details.append(
            {
                "block_index": block_index,
                "left": left,
                "right": right,
                "center": center,
                "edge_count": len(block_edges),
                "mass": mass,
                "alpha_fractional": alpha % 1.0,
                "selected_q": q,
                "selected_mode": mode,
                "frequency_error": frequency_error,
                "rational_cell_ratio": cell_ratio,
                "inside_rational_cell": cell_ratio <= 1.0,
                "exact_log_coefficient": _complex_json(exact_sum),
                "selected_rational_coefficient": _complex_json(rational_sum),
                "linearization_error_normalized": abs(exact_sum - rational_sum) / mass,
                "pole_mass_fraction": pole_mass / mass,
                "near_mass_fraction": near_mass / mass,
            }
        )

    ranked = sorted(
        details,
        key=lambda row: (-row["linearization_error_normalized"], row["block_index"]),
    )[: shell.config.height_detail_blocks]
    return {
        "height": height,
        "nominal_curvature_block_length": nominal,
        "used_block_length": block_length,
        "coarsened_by_block_cap": coarsened,
        "nonempty_block_count": len(details),
        "rational_cell_pass_fraction": passing_cells / max(1, len(details)),
        "selected_modulus_counts": {
            str(q): selected_counts[q] for q in sorted(selected_counts)
        },
        "mass": total_mass,
        "exact_log_aggregate": _complex_json(exact_aggregate),
        "selected_rational_aggregate": _complex_json(rational_aggregate),
        "aggregate_difference_normalized": abs(exact_aggregate - rational_aggregate)
        / total_mass,
        "largest_block_errors": ranked,
    }


def _payload_digest(result: dict[str, Any]) -> str:
    payload = dict(result)
    payload.pop("payload_sha256", None)
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def run_lab(config: LabConfig) -> dict[str, Any]:
    """Run the complete finite scan and return a deterministic JSON object."""

    shell = build_shell(config)
    moduli = segmented_primes(config.q_min, config.q_max + 1, config.segment_size)
    if not moduli:
        raise ValueError("the modulus interval contains no primes")
    rough_reports = (
        _rough_presieve_reports(config, moduli) if config.rough_presieve else {}
    )
    window_length = math.log(config.end / config.start)
    expected_mass = window_integral(config.window, 0.0, window_length, window_length)
    voronoi_mass = sum(node.voronoi_weight for node in shell.nodes)
    sym_mass = sum(edge.mass for edge in shell.edges)
    interior_primes = [p for p in shell.primes if config.start <= p <= config.end]
    prime_fingerprint = hashlib.sha256(
        ",".join(map(str, shell.primes)).encode("ascii")
    ).hexdigest()
    result: dict[str, Any] = {
        "schema": SCHEMA,
        "scope": (
            "finite actual-prime experiment; exact for the stated finite sums; "
            "not an asymptotic theorem or evidence of a zero-free strip"
        ),
        "config": asdict(config),
        "shell": {
            "end": config.end,
            "log_length": window_length,
            "interior_prime_count": len(interior_primes),
            "weighted_node_count": len(shell.nodes),
            "weighted_edge_count": len(shell.edges),
            "prime_data_sha256": prime_fingerprint,
            "first_interior_prime": interior_primes[0],
            "last_interior_prime": interior_primes[-1],
            "maximum_gap": max(edge.gap for edge in shell.edges),
            "mean_gap": sum(edge.gap for edge in shell.edges) / len(shell.edges),
            "window_integral": expected_mass,
            "voronoi_mass": voronoi_mass,
            "symmetrized_gap_mass": sym_mass,
            "voronoi_partition_relative_error": _relative_error(
                voronoi_mass, expected_mass
            ),
            "voronoi_vs_sym_mass_relative_difference": abs(voronoi_mass - sym_mass)
            / expected_mass,
        },
        "moduli": [],
        "common_height": [
            _common_height_report(shell, height, moduli) for height in config.heights
        ],
    }
    for q in moduli:
        report = _modulus_report(shell, q)
        report["q_rough_presieve"] = rough_reports.get(q)
        result["moduli"].append(report)
    result["payload_sha256"] = _payload_digest(result)
    return result


def verify_result(result: dict[str, Any], *, recompute: bool = False) -> None:
    """Verify schema, hashes, algebraic closure checks, and optionally rerun."""

    if result.get("schema") != SCHEMA:
        raise AssertionError("unexpected schema")
    if result.get("payload_sha256") != _payload_digest(result):
        raise AssertionError("payload digest mismatch")
    shell = result["shell"]
    if shell["voronoi_partition_relative_error"] > 2e-12:
        raise AssertionError("Voronoi cells do not partition the window mass")
    if not result["moduli"]:
        raise AssertionError("no modulus reports")
    for report in result["moduli"]:
        if report["modes_scanned"] != report["q"] - 1:
            raise AssertionError("not all nonzero additive modes were scanned")
        checks = [
            report["voronoi"]["checks"]["additive_parseval_relative_error"],
            report["voronoi"]["checks"]["character_parseval_relative_error"],
            report["symmetrized_gap"]["checks"]["additive_parseval_relative_error"],
            report["symmetrized_gap"]["checks"]["character_parseval_relative_error"],
            *report["checks"].values(),
        ]
        if max(checks) > 2e-10:
            raise AssertionError((report["q"], max(checks)))
        if report["transition"]["pole_mass"] < -1e-15:
            raise AssertionError("negative pole mass")
        capture = report["near_residue"]["fixed_small_gap_capture"]
        if capture is not None and capture["relative_identity_error"] > 2e-12:
            raise AssertionError("fixed-small-gap near-residue identity failed")
        if any(
            row["relative_identity_error"] > 2e-12
            for row in report["near_residue"]["wheel_captures"]
        ):
            raise AssertionError("wheel-aligned near-residue identity failed")
        rough = report.get("q_rough_presieve")
        if rough is not None:
            if rough["checks"]["voronoi_partition_relative_error"] > 2e-12:
                raise AssertionError("q-rough Voronoi partition failed")
            if not rough["checks"]["divisible_mass_le_total"]:
                raise AssertionError("q-rough divisible mass exceeds total mass")
    if recompute:
        rerun = run_lab(LabConfig.from_json(result["config"]))
        if rerun["payload_sha256"] != result["payload_sha256"]:
            raise AssertionError("deterministic recomputation mismatch")


def _write_json(result: dict[str, Any], output: Path | None) -> None:
    encoded = json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n"
    if output is None:
        print(encoded, end="")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded, encoding="utf-8")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path, help="verify and deterministically rerun JSON")
    parser.add_argument("--start", type=int, default=LabConfig.start)
    parser.add_argument("--ratio", type=float, default=LabConfig.ratio)
    parser.add_argument("--window", choices=("tent", "flat"), default=LabConfig.window)
    parser.add_argument("--q-min", type=int, default=LabConfig.q_min)
    parser.add_argument("--q-max", type=int, default=LabConfig.q_max)
    parser.add_argument("--near-radius", type=int, default=LabConfig.near_radius)
    parser.add_argument("--top-modes", type=int, default=LabConfig.top_modes)
    parser.add_argument("--segment-size", type=int, default=LabConfig.segment_size)
    parser.add_argument("--height", type=float, action="append", default=[])
    parser.add_argument("--curvature-scale", type=float, default=LabConfig.curvature_scale)
    parser.add_argument("--max-height-blocks", type=int, default=LabConfig.max_height_blocks)
    parser.add_argument(
        "--height-detail-blocks", type=int, default=LabConfig.height_detail_blocks
    )
    parser.add_argument(
        "--no-rough-presieve",
        action="store_true",
        help="skip the intermediate q-rough sequence ledger",
    )
    parser.add_argument(
        "--wheel-step",
        type=int,
        action="append",
        help="even wheel step to diagnose (repeatable; default: 2,6,30)",
    )
    parser.add_argument("--output", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.verify is not None:
        result = json.loads(args.verify.read_text(encoding="utf-8"))
        verify_result(result, recompute=True)
        print(f"PASS {args.verify} {result['payload_sha256']}")
        return 0
    config = LabConfig(
        start=args.start,
        ratio=args.ratio,
        window=args.window,
        q_min=args.q_min,
        q_max=args.q_max,
        near_radius=args.near_radius,
        top_modes=args.top_modes,
        segment_size=args.segment_size,
        heights=tuple(args.height),
        curvature_scale=args.curvature_scale,
        max_height_blocks=args.max_height_blocks,
        height_detail_blocks=args.height_detail_blocks,
        rough_presieve=not args.no_rough_presieve,
        wheel_steps=tuple(args.wheel_step) if args.wheel_step else (2, 6, 30),
    )
    result = run_lab(config)
    verify_result(result)
    _write_json(result, args.output)
    if args.output is not None:
        print(f"WROTE {args.output} {result['payload_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
