"""Exact ledgers for the coarse-lift/mod-q^2 carrier decomposition.

The accompanying report proves the analytic statements.  This module keeps
the finite conductor counts, the aligned residual count, and the rational
project-scale exponents executable.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Q2ConductorCounts:
    principal: int
    nonprincipal_conductor_q: int
    primitive_conductor_q_squared: int
    total: int


def q2_conductor_counts(q: int) -> Q2ConductorCounts:
    """Count characters modulo ``q**2`` by exact conductor for prime ``q``."""

    if q <= 2:
        raise ValueError("q must be an odd prime scale")
    answer = Q2ConductorCounts(
        principal=1,
        nonprincipal_conductor_q=q - 2,
        primitive_conductor_q_squared=(q - 1) ** 2,
        total=q * (q - 1),
    )
    if (
        answer.principal
        + answer.nonprincipal_conductor_q
        + answer.primitive_conductor_q_squared
        != answer.total
    ):
        raise AssertionError("conductor counts do not sum to phi(q^2)")
    return answer


def aligned_unit_residual_size(q: int, degree: int) -> int:
    r"""Return ``#{0<|r|<=qD : q does not divide r}``.

    Each sign consists of ``D`` complete blocks, each containing ``q-1``
    units.
    """

    if q <= 1 or degree <= 0:
        raise ValueError("q and degree must be positive")
    return 2 * degree * (q - 1)


def principal_density(q: int, degree: int) -> Fraction:
    """The exact principal coefficient ``|R|/phi(q^2)=2D/q``."""

    return Fraction(aligned_unit_residual_size(q, degree), q * (q - 1))


def unit_fibre_count(q: int, degree: int, residue: int) -> int:
    """Count aligned residuals in a fixed nonzero residue class modulo q."""

    if not 1 <= residue < q:
        raise ValueError("residue must be nonzero modulo q")
    if degree <= 0:
        raise ValueError("degree must be positive")
    return 2 * degree


@dataclass(frozen=True)
class Q2CoarseExponentLedger:
    degree_in_q: Fraction
    residual_length_in_q: Fraction
    coarse_mellin_bandwidth_in_q: Fraction
    additive_packet_count_in_q: Fraction
    packet_centre_maximum_in_q: Fraction
    fine_mellin_bandwidth_in_q: Fraction
    residual_rms_in_q: Fraction
    polya_vinogradov_in_q: Fraction
    burgess_r2_in_q: Fraction
    flat_packet_coefficient_in_q: Fraction
    flat_packet_l2_mass_in_q: Fraction
    square_function_budget_in_q: Fraction
    desired_squared_norm_in_q: Fraction


def project_q2_coarse_exponent_ledger() -> Q2CoarseExponentLedger:
    """Return the exact exponent ledger at ``D=q^(16/33)``.

    A primitive additive packet has normalized coefficient ``D/q``.  There
    are ``q/D`` flat packets.  A vector-valued packet inequality with square
    constant ``q`` would therefore have budget

    ``q * (q/D) * (D/q)^2 = D``.
    """

    d = Fraction(16, 33)
    packet_count = 1 - d
    packet_coefficient = d - 1
    packet_l2 = packet_count + 2 * packet_coefficient
    square_budget = 1 + packet_l2
    return Q2CoarseExponentLedger(
        degree_in_q=d,
        residual_length_in_q=1 + d,
        coarse_mellin_bandwidth_in_q=Fraction(1, 1),
        additive_packet_count_in_q=packet_count,
        packet_centre_maximum_in_q=2 - d,
        fine_mellin_bandwidth_in_q=2 - d,
        residual_rms_in_q=(1 + d) / 2,
        polya_vinogradov_in_q=Fraction(1, 1),
        burgess_r2_in_q=Fraction(7, 8) + d / 2,
        flat_packet_coefficient_in_q=packet_coefficient,
        flat_packet_l2_mass_in_q=packet_l2,
        square_function_budget_in_q=square_budget,
        desired_squared_norm_in_q=d,
    )
