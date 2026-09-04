"""Exponent ledgers for the two-star BDH and sharp-Selberg inverse gate."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class BDHLedger:
    """Powers of ``D`` after division by the critical ``M^2`` target."""

    diagonal_ratio: Fraction
    principal_ratio: Fraction


def critical_bdh_ledger() -> BDHLedger:
    """Return the two exponents in (2.4), with ``M=D^(15/8)``."""

    m = Fraction(15, 8)
    q = Fraction(33, 16)
    return BDHLedger(
        diagonal_ratio=1 - m,
        principal_ratio=2 - q,
    )


@dataclass(frozen=True)
class SelbergInverseLedger:
    """Powers in the maximal local sharp-Selberg block."""

    frequency_length: Fraction
    term_count: Fraction
    normalized_average_coefficient: Fraction
    chang_dimension_allowance: Fraction
    centered_variance: Fraction
    uniform_background: Fraction
    relative_centered_excess: Fraction


def selberg_inverse_ledger(epsilon: Fraction = Fraction(0)) -> SelbergInverseLedger:
    """Return the exponents from (4.3)--(4.10).

    ``epsilon`` is the putative power failure in
    ``sum_l |S_l| >= q D^epsilon``.
    """

    h = Fraction(17, 16)
    n = Fraction(2)
    return SelbergInverseLedger(
        frequency_length=h,
        term_count=n,
        normalized_average_coefficient=-1 + epsilon,
        chang_dimension_allowance=2 - 2 * epsilon,
        centered_variance=2 + 2 * epsilon,
        uniform_background=Fraction(47, 16),
        relative_centered_excess=-Fraction(15, 16) + 2 * epsilon,
    )


def latin_selberg_l1(q: int, d: int, block_size: int) -> int:
    """Return ``H L^2`` for the aligned cyclic Latin phase model."""

    if q <= 0 or d <= 0 or q % d or not 1 <= block_size <= d:
        raise ValueError("need q,d>0, d|q, and 1<=block_size<=d")
    return (q // d) * block_size**2

