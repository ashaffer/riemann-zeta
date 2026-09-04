"""Exact ledgers for the mod-q^3 character attack on the QP carry core.

The analytic report contains the proof.  This module keeps the elementary
conductor counts, interval counts, filtration constants, and exponent
comparisons executable without implementing a full Dirichlet-character
package.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


def euler_phi_prime_power(prime: int, exponent: int) -> int:
    if prime <= 1 or exponent <= 0:
        raise ValueError("prime and exponent must be positive")
    return prime ** (exponent - 1) * (prime - 1)


@dataclass(frozen=True)
class ConductorCounts:
    conductor_one: int
    conductor_q: int
    conductor_q_squared: int
    conductor_q_cubed: int
    total: int


def conductor_counts(q: int) -> ConductorCounts:
    """Count characters modulo ``q**3`` by exact conductor.

    ``q`` is assumed prime by the theorem; primality is not tested here.
    """

    if q <= 2:
        raise ValueError("q must be an odd prime scale")
    phi1 = euler_phi_prime_power(q, 1)
    phi2 = euler_phi_prime_power(q, 2)
    phi3 = euler_phi_prime_power(q, 3)
    answer = ConductorCounts(
        conductor_one=1,
        conductor_q=phi1 - 1,
        conductor_q_squared=phi2 - phi1,
        conductor_q_cubed=phi3 - phi2,
        total=phi3,
    )
    if sum(
        (
            answer.conductor_one,
            answer.conductor_q,
            answer.conductor_q_squared,
            answer.conductor_q_cubed,
        )
    ) != answer.total:
        raise AssertionError("conductor counts do not sum to phi(q^3)")
    return answer


def symmetric_unit_interval_size(q: int, degree: int) -> int:
    """Return ``#{0<|r|<=q*D : q does not divide r}`` exactly."""

    if q <= 1 or degree <= 0:
        raise ValueError("q and D must be positive")
    return 2 * degree * (q - 1)


def residue_count_mod_q(q: int, degree: int, residue: int) -> int:
    """Count the symmetric interval in one nonzero residue class mod q."""

    if not 1 <= residue < q:
        raise ValueError("residue must be nonzero modulo q")
    # Positive and negative halves each contain D complete q-blocks.
    return 2 * degree


@dataclass(frozen=True)
class CompleteBlockDecomposition:
    complete_blocks_per_half: int
    boundary_length_per_half: int


def complete_q_block_decomposition(q: int, endpoint: int) -> CompleteBlockDecomposition:
    """Split ``1,...,endpoint`` into complete q-blocks and one boundary.

    Nonprincipal conductor-q characters cancel on the complete blocks.  The
    boundary is absent exactly when ``endpoint`` is divisible by ``q``.
    """

    if q <= 1 or endpoint < 0:
        raise ValueError("q must be positive and endpoint nonnegative")
    blocks, boundary = divmod(endpoint, q)
    return CompleteBlockDecomposition(blocks, boundary)


@dataclass(frozen=True)
class CharacterExponentLedger:
    degree_exponent_in_q: Fraction
    target_exponent_in_q: Fraction
    old_twenty_one_sixteenths_exponent_in_q: Fraction
    hilbert_schmidt_fourth_exponent_in_q: Fraction
    principal_fourth_exponent_in_q: Fraction
    low_conductor_hs_squared_exponent_in_q: Fraction
    low_conductor_fourth_exponent_in_q: Fraction
    residual_length_exponent_in_q: Fraction
    residual_l2_exponent_in_q: Fraction
    burgess_r2_exponent_in_q: Fraction
    burgess_is_worse_than_residual_l2: bool
    character_method_improves_old_exponent: bool


def project_character_exponent_ledger() -> CharacterExponentLedger:
    """Return the exact project-scale exponent comparison.

    Here ``D=q^(16/33)`` and ``L=q*D``.  The primitive character moment
    argument gives no better than the Hilbert--Schmidt fourth bound ``D^2``.
    Burgess with ``r=2`` for modulus ``q^3`` has size

    ``L^(1/2) * (q^3)^(3/16)``.
    """

    d = Fraction(16, 33)
    length = 1 + d
    residual_l2 = length / 2
    burgess = residual_l2 + Fraction(9, 16)
    target = d
    old = Fraction(21, 16) * d
    hs_fourth = 2 * d
    principal_fourth = 4 * d - 2
    low_hs_squared = 2 * d - 1
    low_fourth = 2 * low_hs_squared
    return CharacterExponentLedger(
        degree_exponent_in_q=d,
        target_exponent_in_q=target,
        old_twenty_one_sixteenths_exponent_in_q=old,
        hilbert_schmidt_fourth_exponent_in_q=hs_fourth,
        principal_fourth_exponent_in_q=principal_fourth,
        low_conductor_hs_squared_exponent_in_q=low_hs_squared,
        low_conductor_fourth_exponent_in_q=low_fourth,
        residual_length_exponent_in_q=length,
        residual_l2_exponent_in_q=residual_l2,
        burgess_r2_exponent_in_q=burgess,
        burgess_is_worse_than_residual_l2=burgess > residual_l2,
        character_method_improves_old_exponent=hs_fourth < old,
    )
