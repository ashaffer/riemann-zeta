"""Exact replay for the error-labelled spectral-coherence method fixture.

The construction retains a common integer product centre and short
individual product errors.  It intentionally does not satisfy the common
QP shell or prime-power conditions, so it is a method fixture rather than a
counterexample to the physical conjecture.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt, prod


@dataclass(frozen=True)
class ErrorLabelPoint:
    index: int
    completion: int
    carrier: int
    error: int


@dataclass(frozen=True)
class ErrorCoherenceLedger:
    size: int
    error_modulus: int
    progression_step: int
    product_center: int
    raw_completion_energy: int
    tagged_energy: int
    coherence: Fraction
    maximum_error_fibre: int
    maximum_pair_cell: int
    no_three_completion_error_collinear: bool
    no_three_completion_carrier_collinear: bool
    common_shell_ratio: Fraction


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def _next_prime(value: int) -> int:
    candidate = max(2, value + 1)
    while not _is_prime(candidate):
        candidate += 1
    return candidate


def _primes_up_to(limit: int) -> list[int]:
    return [value for value in range(2, limit + 1) if _is_prime(value)]


def _centered_residue(value: int, modulus: int) -> int:
    residue = value % modulus
    if 2 * residue > modulus:
        residue -= modulus
    return residue


def _pairwise_crt(residues: list[int], moduli: list[int]) -> tuple[int, int]:
    """Return ``(x, M)`` with ``x == residues[i] (mod moduli[i])``."""

    value = 0
    modulus = 1
    for residue, new_modulus in zip(residues, moduli, strict=True):
        if gcd(modulus, new_modulus) != 1:
            raise ValueError("CRT moduli must be pairwise coprime")
        multiplier = ((residue - value) * pow(modulus, -1, new_modulus)) % new_modulus
        value += modulus * multiplier
        modulus *= new_modulus
        value %= modulus
    return value, modulus


def _collinear(first: tuple[int, int], second: tuple[int, int], third: tuple[int, int]) -> bool:
    x1, y1 = first
    x2, y2 = second
    x3, y3 = third
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def _has_collinear_triple(points: list[tuple[int, int]]) -> bool:
    return any(_collinear(*triple) for triple in combinations(points, 3))


def method_fixture(size: int) -> tuple[int, int, list[ErrorLabelPoint]]:
    """Build the exact non-shell product-band fixture from Section 5."""

    if size < 4:
        raise ValueError("size must be at least four")

    error_modulus = _next_prime(2 * size)
    step = prod(_primes_up_to(size))
    indices = list(range(1, size + 1))
    completions = [1 + index * step for index in indices]
    if any(gcd(left, right) != 1 for left, right in combinations(completions, 2)):
        raise AssertionError("the progression moduli are not pairwise coprime")

    errors = [_centered_residue(index * index, error_modulus) for index in indices]
    base_center, center_modulus = _pairwise_crt(
        [(-error) % completion for error, completion in zip(errors, completions, strict=True)],
        completions,
    )

    # A pair equality or a collinear triple excludes at most one shift of the
    # CRT centre.  The finite search below makes the promised avoidance exact.
    number_of_bad_conditions = size * (size - 1) // 2 + size * (size - 1) * (size - 2) // 6
    for shift in range(1, number_of_bad_conditions + 3):
        center = base_center + shift * center_modulus
        carriers = [
            (center + error) // completion
            for error, completion in zip(errors, completions, strict=True)
        ]
        if len(set(carriers)) != size:
            continue
        carrier_projection = list(zip(completions, carriers, strict=True))
        if not _has_collinear_triple(carrier_projection):
            points = [
                ErrorLabelPoint(index, completion, carrier, error)
                for index, completion, carrier, error in zip(
                    indices, completions, carriers, errors, strict=True
                )
            ]
            return error_modulus, center, points
    raise AssertionError("finite shift avoidance unexpectedly failed")


def tangent_shell_fixture(root: int, radius: int) -> tuple[int, list[ErrorLabelPoint]]:
    """Return the exact shell-faithful tangent resonance ``C=root**2``.

    The points lie on the affine packet ``completion + carrier = 2*root``
    and have product errors ``-h**2``.  They calibrate the local
    square-root cluster; they are not a packet-free fixture.
    """

    if radius < 1:
        raise ValueError("radius must be positive")
    if root <= 2 * radius:
        raise ValueError("root must dominate the tangent radius")
    center = root * root
    points = [
        ErrorLabelPoint(
            index=offset,
            completion=root + offset,
            carrier=root - offset,
            error=-(offset * offset),
        )
        for offset in range(-radius, radius + 1)
    ]
    return center, points


def completion_energy(points: list[ErrorLabelPoint]) -> int:
    pair_sums = Counter(
        first.completion + second.completion for first in points for second in points
    )
    return sum(multiplicity * multiplicity for multiplicity in pair_sums.values())


def tagged_energy(points: list[ErrorLabelPoint]) -> tuple[int, int]:
    cells = Counter(
        (
            first.completion + second.completion,
            first.error + second.error,
        )
        for first in points
        for second in points
    )
    return sum(multiplicity * multiplicity for multiplicity in cells.values()), max(cells.values())


def error_coherence_ledger(size: int) -> ErrorCoherenceLedger:
    error_modulus, center, points = method_fixture(size)
    raw_energy = completion_energy(points)
    joint_energy, maximum_pair_cell = tagged_energy(points)
    nodes = [point.completion for point in points] + [point.carrier for point in points]
    return ErrorCoherenceLedger(
        size=size,
        error_modulus=error_modulus,
        progression_step=points[1].completion - points[0].completion,
        product_center=center,
        raw_completion_energy=raw_energy,
        tagged_energy=joint_energy,
        coherence=Fraction(raw_energy, joint_energy),
        maximum_error_fibre=max(Counter(point.error for point in points).values()),
        maximum_pair_cell=maximum_pair_cell,
        no_three_completion_error_collinear=not _has_collinear_triple(
            [(point.completion, point.error) for point in points]
        ),
        no_three_completion_carrier_collinear=not _has_collinear_triple(
            [(point.completion, point.carrier) for point in points]
        ),
        common_shell_ratio=Fraction(max(nodes), min(nodes)),
    )


def verify_method_fixture(size: int = 6) -> ErrorCoherenceLedger:
    error_modulus, center, points = method_fixture(size)
    for point in points:
        assert point.completion * point.carrier - center == point.error
        assert abs(point.error) <= error_modulus // 2
    ledger = error_coherence_ledger(size)
    assert ledger.raw_completion_energy == (2 * size**3 + size) // 3
    assert ledger.tagged_energy == 2 * size**2 - size
    assert ledger.maximum_error_fibre == 1
    assert ledger.maximum_pair_cell == 2
    assert ledger.no_three_completion_error_collinear
    assert ledger.no_three_completion_carrier_collinear
    assert ledger.common_shell_ratio > 2
    return ledger


def verify_tangent_shell_fixture(root: int = 10_000, radius: int = 10) -> int:
    center, points = tangent_shell_fixture(root, radius)
    assert all(point.completion * point.carrier - center == point.error for point in points)
    assert all(abs(point.error) <= radius * radius for point in points)
    assert all(point.completion + point.carrier == 2 * root for point in points)
    size = 2 * radius + 1
    energy = completion_energy(points)
    assert energy == (2 * size**3 + size) // 3
    return energy


if __name__ == "__main__":
    print(verify_method_fixture())
    print(verify_tangent_shell_fixture())
