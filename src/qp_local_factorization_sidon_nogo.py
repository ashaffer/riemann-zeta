"""Exponent ledger for the local-factorization Sidon counterexample.

The probabilistic theorem and its proof are recorded in
``results/ZETA23-QP-LOCAL-FACTORIZATION-SIDON-NOGO-2026-08-15.md``.
This module checks only its exact exponent inequalities.  It does not use a
finite random experiment as a substitute for the theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class LocalSidonLedger:
    aperture: Fraction
    low_endpoint: Fraction
    target_power: Fraction
    support_power: Fraction
    integrations: int

    @property
    def antenna_power(self) -> Fraction:
        """Power in ``K/sqrt(K log Y)=Y^(eta/2-o(1))``."""

        return self.support_power / 2

    @property
    def sidon_union_power(self) -> Fraction:
        """Power in the bad-quadruple union bound ``K^4/B``."""

        return 4 * self.support_power - self.aperture

    @property
    def mean_bias_power(self) -> Fraction:
        """Power in ``K*T0^-N`` after integrations by parts."""

        return self.support_power - self.integrations * self.low_endpoint

    @property
    def integer_sidon_union_power(self) -> Fraction:
        """Power in the lattice bad-quadruple bound ``K^4/Y``."""

        return 4 * self.support_power - 1

    @property
    def integer_high_bias_power(self) -> Fraction:
        """Power in ``K*sqrt(B)/Y`` from van der Corput."""

        return self.support_power + self.aperture / 2 - 1

    def verify(self) -> None:
        if min(
            self.aperture,
            self.low_endpoint,
            self.target_power,
            self.support_power,
        ) <= 0:
            raise ValueError("all exponents must be positive")
        if self.integrations < 1:
            raise ValueError("integrations must be positive")
        if not 2 * self.target_power < self.support_power:
            raise ValueError("support power must exceed twice the QP target")
        if not self.sidon_union_power < 0:
            raise ValueError("K^4/B must tend to zero")
        if not self.mean_bias_power < self.antenna_power:
            raise ValueError("smooth sampling bias must be below sqrt(K)")

    def verify_integer_log_version(self) -> None:
        """Check the additional all-integer logarithmic-lattice bounds."""

        self.verify()
        if not self.integer_sidon_union_power < 0:
            raise ValueError("integer-log K^4/Y union bound must decay")
        if not self.integer_high_bias_power < self.antenna_power:
            raise ValueError("integer high-band mean must be below sqrt(K)")


def active_ledger() -> LocalSidonLedger:
    """Return the exact ledger ``c=.019, eta=.04, A=50/33``."""

    ledger = LocalSidonLedger(
        aperture=Fraction(50, 33),
        low_endpoint=Fraction(1, 100),
        target_power=Fraction(19, 1000),
        support_power=Fraction(1, 25),
        integrations=4,
    )
    ledger.verify_integer_log_version()
    return ledger


if __name__ == "__main__":
    item = active_ledger()
    print(f"antenna_power={float(item.antenna_power):.12f}")
    print(f"target_power={float(item.target_power):.12f}")
    print(f"sidon_union_power={float(item.sidon_union_power):.12f}")
    print(f"mean_bias_power={float(item.mean_bias_power):.12f}")
    print(f"integer_sidon_union_power={float(item.integer_sidon_union_power):.12f}")
    print(f"integer_high_bias_power={float(item.integer_high_bias_power):.12f}")
