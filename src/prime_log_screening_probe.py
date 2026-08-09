#!/usr/bin/env python3
"""Finite-block screening audit for the completed prime logarithmic measure.

For

    d eta(u) = sum_n Lambda(n)n^(-1/2) delta_(log n)(du) - exp(u/2)du

and the triangular window ``w_ell(t) = (1-|t|/ell)_+``, this module
decomposes, without sampling in the scale variable,

    integral_a^b | integral w_ell(u-R)d eta(u) |^2 dR.

The atom sum is piecewise linear in ``R``.  A sweep through its three hat
breakpoints therefore evaluates the atom square and its pairing with the
continuum exactly up to floating-point roundoff.  The output is a mechanism
diagnostic, not a rigorous certificate and not evidence for RH.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Atom:
    """One von Mangoldt atom in logarithmic coordinates."""

    location: float
    weight: float


@dataclass(frozen=True)
class EnergyComponents:
    """Exact algebraic pieces of one finite-block Toeplitz energy."""

    lower: float
    upper: float
    atom_count: int
    atom_diagonal: float
    atom_off_diagonal: float
    atom_continuum: float
    continuum_square: float
    energy: float

    @property
    def connected_screening(self) -> float:
        """Everything except the positive self/diagonal contribution."""
        return (
            self.atom_off_diagonal
            + self.atom_continuum
            + self.continuum_square
        )

    @property
    def screening_ratio(self) -> float:
        """Connected contribution divided by the atom diagonal."""
        if self.atom_diagonal == 0.0:
            return math.nan
        return self.connected_screening / self.atom_diagonal

    @property
    def energy_to_diagonal(self) -> float:
        """Residual energy divided by the atom diagonal."""
        if self.atom_diagonal == 0.0:
            return math.nan
        return self.energy / self.atom_diagonal


@dataclass(frozen=True)
class ScreeningResult:
    """Whole-block decomposition and its two endpoint strips."""

    ell: float
    total: EnergyComponents
    core: EnergyComponents
    boundary: EnergyComponents
    diagonal_asymptotic: float

    @property
    def boundary_energy_fraction(self) -> float:
        if self.total.energy == 0.0:
            return math.nan
        return self.boundary.energy / self.total.energy


def _mangoldt_atoms(maximum: int, minimum: int = 2) -> list[Atom]:
    """Return all prime-power von Mangoldt atoms in ``[minimum, maximum]``."""
    if maximum < 2 or maximum < minimum:
        return []
    sieve = bytearray(b"\x01") * (maximum + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(maximum) + 1):
        if not sieve[prime]:
            continue
        start = prime * prime
        sieve[start : maximum + 1 : prime] = b"\x00" * (
            (maximum - start) // prime + 1
        )

    atoms: list[Atom] = []
    for prime in range(2, maximum + 1):
        if not sieve[prime]:
            continue
        log_prime = math.log(prime)
        power = prime
        while power <= maximum:
            if power >= minimum:
                atoms.append(
                    Atom(math.log(power), log_prime / math.sqrt(power))
                )
            if power > maximum // prime:
                break
            power *= prime
    atoms.sort(key=lambda atom: atom.location)
    return atoms


def atoms_for_block(lower: float, upper: float, ell: float) -> list[Atom]:
    """Construct precisely the atoms whose hats meet ``[lower, upper]``."""
    if not (math.isfinite(lower) and math.isfinite(upper) and lower < upper):
        raise ValueError("require finite lower < upper")
    if not math.isfinite(ell) or ell <= 0.0:
        raise ValueError("ell must be finite and positive")
    maximum = math.floor(math.exp(upper + ell))
    minimum = max(2, math.ceil(math.exp(lower - ell)))
    return _mangoldt_atoms(maximum, minimum)


def pole_coefficient(ell: float) -> float:
    """Return ``integral w_ell(t)exp(t/2)dt``."""
    if not math.isfinite(ell) or ell <= 0.0:
        raise ValueError("ell must be finite and positive")
    return 16.0 * math.sinh(ell / 4.0) ** 2 / ell


def _hat_square(atom: Atom, lower: float, upper: float, ell: float) -> float:
    """Integrate one squared triangular hat over a truncated interval."""
    u = atom.location
    answer = 0.0

    left = max(lower, u - ell)
    right = min(upper, u)
    if left < right:
        z_left = (left - (u - ell)) / ell
        z_right = (right - (u - ell)) / ell
        answer += ell * (z_right**3 - z_left**3) / 3.0

    left = max(lower, u)
    right = min(upper, u + ell)
    if left < right:
        z_left = (u + ell - left) / ell
        z_right = (u + ell - right) / ell
        answer += ell * (z_left**3 - z_right**3) / 3.0
    return atom.weight * atom.weight * answer


def _segment_integrals(
    start: float,
    stop: float,
    value: float,
    slope: float,
    center: float,
) -> tuple[float, float, float]:
    """Integrate ``A^2``, ``-2*A*C*exp(R/2)``, and ``C^2*exp(R)``.

    On this segment ``A(start+t)=value+slope*t`` and ``center`` is ``C``.
    """
    length = stop - start
    atom_square = (
        value * value * length
        + value * slope * length * length
        + slope * slope * length**3 / 3.0
    )
    exp_half = math.exp(start / 2.0)
    int_exp_half = 2.0 * math.expm1(length / 2.0)
    int_t_exp_half = (
        math.exp(length / 2.0) * (2.0 * length - 4.0) + 4.0
    )
    atom_exp = exp_half * (
        value * int_exp_half + slope * int_t_exp_half
    )
    atom_continuum = -2.0 * center * atom_exp
    continuum_square = center * center * math.exp(start) * math.expm1(length)
    return atom_square, atom_continuum, continuum_square


def decompose_energy(
    atoms: Iterable[Atom], lower: float, upper: float, ell: float
) -> EnergyComponents:
    """Decompose the block energy by a piecewise-linear event sweep."""
    if not (math.isfinite(lower) and math.isfinite(upper) and lower <= upper):
        raise ValueError("require finite lower <= upper")
    if not math.isfinite(ell) or ell <= 0.0:
        raise ValueError("ell must be finite and positive")
    selected = [
        atom
        for atom in atoms
        if atom.location + ell > lower and atom.location - ell < upper
    ]
    if lower == upper:
        return EnergyComponents(lower, upper, len(selected), 0.0, 0.0, 0.0, 0.0, 0.0)

    value_terms: list[float] = []
    slope_terms: list[float] = []
    events: list[tuple[float, float]] = []
    inverse_ell = 1.0 / ell
    for atom in selected:
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

        for position, delta in (
            (left_edge, atom.weight * inverse_ell),
            (atom.location, -2.0 * atom.weight * inverse_ell),
            (right_edge, atom.weight * inverse_ell),
        ):
            if lower < position < upper:
                events.append((position, delta))

    events.sort(key=lambda event: event[0])
    value = math.fsum(value_terms)
    slope = math.fsum(slope_terms)
    center = pole_coefficient(ell)
    atom_square_pieces: list[float] = []
    cross_pieces: list[float] = []
    continuum_pieces: list[float] = []

    cursor = lower
    index = 0
    while index < len(events):
        position = events[index][0]
        atom_square, cross, continuum = _segment_integrals(
            cursor, position, value, slope, center
        )
        atom_square_pieces.append(atom_square)
        cross_pieces.append(cross)
        continuum_pieces.append(continuum)
        value += slope * (position - cursor)
        deltas: list[float] = []
        while index < len(events) and events[index][0] == position:
            deltas.append(events[index][1])
            index += 1
        slope += math.fsum(deltas)
        cursor = position

    atom_square, cross, continuum = _segment_integrals(
        cursor, upper, value, slope, center
    )
    atom_square_pieces.append(atom_square)
    cross_pieces.append(cross)
    continuum_pieces.append(continuum)

    atom_square_total = math.fsum(atom_square_pieces)
    atom_diagonal = math.fsum(
        _hat_square(atom, lower, upper, ell) for atom in selected
    )
    atom_off_diagonal = atom_square_total - atom_diagonal
    atom_continuum = math.fsum(cross_pieces)
    continuum_square = math.fsum(continuum_pieces)
    energy = math.fsum(
        (atom_diagonal, atom_off_diagonal, atom_continuum, continuum_square)
    )
    return EnergyComponents(
        lower,
        upper,
        len(selected),
        atom_diagonal,
        atom_off_diagonal,
        atom_continuum,
        continuum_square,
        energy,
    )


def _subtract(
    total: EnergyComponents, part: EnergyComponents
) -> EnergyComponents:
    """Subtract additive interval components (used for endpoint strips)."""
    return EnergyComponents(
        total.lower,
        total.upper,
        total.atom_count,
        total.atom_diagonal - part.atom_diagonal,
        total.atom_off_diagonal - part.atom_off_diagonal,
        total.atom_continuum - part.atom_continuum,
        total.continuum_square - part.continuum_square,
        total.energy - part.energy,
    )


def analyze_block(lower: float, upper: float, ell: float) -> ScreeningResult:
    """Evaluate a block and isolate strips of width ``ell`` at its endpoints."""
    atoms = atoms_for_block(lower, upper, ell)
    total = decompose_energy(atoms, lower, upper, ell)
    core_lower = min(upper, lower + ell)
    core_upper = max(core_lower, upper - ell)
    core = decompose_energy(atoms, core_lower, core_upper, ell)
    boundary = _subtract(total, core)
    diagonal_asymptotic = ell * (upper * upper - lower * lower) / 3.0
    return ScreeningResult(ell, total, core, boundary, diagonal_asymptotic)


def _format(result: ScreeningResult) -> str:
    total = result.total
    return (
        f"I=[{total.lower:g},{total.upper:g}] ell={result.ell:g} "
        f"atoms={total.atom_count} "
        f"diag={total.atom_diagonal:.9g} "
        f"off={total.atom_off_diagonal:.9g} "
        f"atom_cont={total.atom_continuum:.9g} "
        f"cont2={total.continuum_square:.9g} "
        f"energy={total.energy:.9g} "
        f"E/diag={total.energy_to_diagonal:.6g} "
        f"screen/diag={total.screening_ratio:.6g} "
        f"diag/asym={total.atom_diagonal/result.diagonal_asymptotic:.6g} "
        f"boundary_E/E={result.boundary_energy_fraction:.6g}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--centers", nargs="+", type=float, default=[8.0, 10.0, 12.0])
    parser.add_argument("--widths", nargs="+", type=float, default=[2.0, 4.0])
    parser.add_argument("--ells", nargs="+", type=float, default=[0.5, 1.0])
    args = parser.parse_args()
    for center_value in args.centers:
        for width in args.widths:
            for ell in args.ells:
                if width <= 0.0:
                    raise ValueError("block widths must be positive")
                result = analyze_block(
                    center_value - width / 2.0,
                    center_value + width / 2.0,
                    ell,
                )
                print(_format(result))


if __name__ == "__main__":
    main()
