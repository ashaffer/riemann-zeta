"""Exact graph-weighted centering ledgers for Yao's fourth moment.

For a graph ``m=m(k)`` in the reciprocal phase ``m/k``, the phase points
are the selected carriers ``v(k)=m(k)/k``.  The nonzero-frequency fourth
moment is exactly their centered additive energy.  The interval fixture
below shows that graph support and matching alone stop at cubic energy.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction


def interval_additive_energy(size: int) -> int:
    """Return ``E^+([1,size])=(2*size**3+size)/3``."""

    if size < 1:
        raise ValueError("size must be positive")
    return (2 * size**3 + size) // 3


def graph_phase_points(
    prime: int, denominators: tuple[int, ...], numerators: tuple[int, ...]
) -> tuple[int, ...]:
    """Return the finite-field phases ``m*k^{-1} (mod prime)``."""

    if len(denominators) != len(numerators):
        raise ValueError("the graph coordinate lists must have equal length")
    if prime <= 2:
        raise ValueError("prime modulus must exceed two")
    answer = []
    for denominator, numerator in zip(denominators, numerators):
        if denominator % prime == 0:
            raise ValueError("denominators must be nonzero modulo prime")
        answer.append((numerator * pow(denominator, -1, prime)) % prime)
    return tuple(answer)


def unweighted_modular_additive_energy(prime: int, points: tuple[int, ...]) -> int:
    """Count ordered ``v1-v2=v3-v4 (mod prime)`` quadruples."""

    differences = Counter((first - second) % prime for first in points for second in points)
    return sum(multiplicity * multiplicity for multiplicity in differences.values())


@dataclass(frozen=True)
class GraphCenteringExponentLedger:
    """Powers in ``D`` at ``p=D^(33/16)`` and graph size ``N=D``."""

    target_energy: Fraction
    best_direct_graph_energy: Fraction
    direct_loss: Fraction
    pairwise_minkowski: Fraction
    pairwise_minkowski_loss: Fraction
    completed_cartesian_centered: Fraction
    completed_cartesian_principal: Fraction
    completed_best_power: Fraction
    completed_loss: Fraction
    graph_centering_baseline: Fraction


def graph_centering_exponent_ledger() -> GraphCenteringExponentLedger:
    """Return the exact Cauchy/completion/centering power ledger."""

    target = Fraction(5, 2)
    completed_centered = Fraction(6)
    completed_principal = Fraction(8) - Fraction(33, 16)
    completed = max(completed_centered, completed_principal)
    return GraphCenteringExponentLedger(
        target_energy=target,
        best_direct_graph_energy=Fraction(3),
        direct_loss=Fraction(1, 2),
        pairwise_minkowski=Fraction(4),
        pairwise_minkowski_loss=Fraction(3, 2),
        completed_cartesian_centered=completed_centered,
        completed_cartesian_principal=completed_principal,
        completed_best_power=completed,
        completed_loss=completed - target,
        graph_centering_baseline=Fraction(4) - Fraction(33, 16),
    )
