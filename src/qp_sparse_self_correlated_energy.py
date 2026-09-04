"""Exponent ledger for the critical sparse self-correlated energy.

The theorem interpolates the mixed ``BH^2`` product-large-sieve energy with
the character second moment.  It saves ``D^(11/32)`` from the classical
critical bound.  The principal character caps any possible full-energy
saving at ``D^(3/8)``.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


Q_IN_D = Fraction(33, 16)
CRITICAL_MU = Fraction(11, 8)


def classical_energy_exponent(mu: Fraction) -> Fraction:
    """Exponent of ``q M D`` in powers of ``D``."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("support exponent must be nonnegative")
    return Q_IN_D + mu + 1


def mixed_energy_exponent(mu: Fraction) -> Fraction:
    """Exponent of ``q^(1/2) M^(3/2) D`` in powers of ``D``."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("support exponent must be nonnegative")
    return Q_IN_D / 2 + 3 * mu / 2 + 1


def principal_energy_exponent(mu: Fraction) -> Fraction:
    """Exponent of ``M^3 D^2/q`` in powers of ``D``."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("support exponent must be nonnegative")
    return 3 * mu + 2 - Q_IN_D


def elliott_target_energy_exponent(mu: Fraction) -> Fraction:
    """Exponent of ``M^(3/2)D^2`` supplied by the conjectural sparse LS."""

    mu = Fraction(mu)
    if mu < 0:
        raise ValueError("support exponent must be nonnegative")
    return 3 * mu / 2 + 2


@dataclass(frozen=True)
class SparseEnergyLedger:
    critical_support_in_d: Fraction
    critical_support_in_q: Fraction
    classical_energy: Fraction
    mixed_energy: Fraction
    principal_energy: Fraction
    proved_saving: Fraction
    principal_ceiling: Fraction
    open_gap: Fraction
    conjectural_energy: Fraction
    proper_power_energy: Fraction


def sparse_energy_ledger() -> SparseEnergyLedger:
    classical = classical_energy_exponent(CRITICAL_MU)
    mixed = mixed_energy_exponent(CRITICAL_MU)
    principal = principal_energy_exponent(CRITICAL_MU)
    conjectural = elliott_target_energy_exponent(CRITICAL_MU)
    proved = classical - max(mixed, principal)
    ceiling = classical - principal
    return SparseEnergyLedger(
        critical_support_in_d=CRITICAL_MU,
        critical_support_in_q=Fraction(2, 3),
        classical_energy=classical,
        mixed_energy=mixed,
        principal_energy=principal,
        proved_saving=proved,
        principal_ceiling=ceiling,
        open_gap=ceiling - proved,
        conjectural_energy=conjectural,
        proper_power_energy=Fraction(251, 64),
    )


def mixed_upper_bound(q: int, support_size: int, determinant_width: int) -> float:
    """Return ``M^3D^2/q + sqrt(q)M^(3/2)D`` numerically."""

    if min(q, support_size, determinant_width) <= 0:
        raise ValueError("all scales must be positive")
    principal = support_size**3 * determinant_width**2 / q
    nonprincipal = q**0.5 * support_size**1.5 * determinant_width
    return principal + nonprincipal


def critical_classical_bound(q: int, support_size: int, determinant_width: int) -> int:
    """Return the benchmark ``q M D``."""

    if min(q, support_size, determinant_width) <= 0:
        raise ValueError("all scales must be positive")
    return q * support_size * determinant_width

