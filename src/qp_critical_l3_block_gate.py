"""Exact exponent ledger for the critical QP absolute-L3 block gate."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class CriticalL3Ledger:
    """Power ledger with ``B=Y**A`` and ``D=Y**(2-A)``."""

    A: Fraction = Fraction(50, 33)

    @property
    def D(self) -> Fraction:
        return 2 - self.A

    @property
    def block(self) -> Fraction:
        """Exponent of ``R=Y/sqrt(B)=sqrt(D)``."""

        return 1 - self.A / 2

    @property
    def l3_norm_loss(self) -> Fraction:
        """Exponent of ``R**(1/6)=D**(1/12)``."""

        return self.block / 6

    @property
    def third_moment_loss(self) -> Fraction:
        """Exponent of ``sqrt(R)=D**(1/4)``."""

        return self.block / 2

    @property
    def aligned_l4_peak(self) -> Fraction:
        """Exponent of ``K**2/B`` for ``K=Y**(1+o(1))``."""

        return 2 - self.A

    @property
    def aligned_l3_peak(self) -> Fraction:
        """Exponent of ``K**(3/2)/B`` for one global aligned peak."""

        return Fraction(3, 2) - self.A


def local_block_l3_loss(block_size: float) -> float:
    """The elementary ``L2``--``L-infinity`` loss ``block_size**(1/6)``."""

    if block_size <= 0:
        raise ValueError("block_size must be positive")
    return block_size ** (1.0 / 6.0)


def normalized_aligned_peak(node_count: float, time_length: float, moment: int) -> float:
    """Contribution of one unit-width aligned peak for normalized weights."""

    if node_count <= 0 or time_length <= 0:
        raise ValueError("node_count and time_length must be positive")
    if moment <= 0:
        raise ValueError("moment must be positive")
    return node_count ** (moment / 2.0) / time_length


def dirichlet_reverse_square_ratio(index_count: float) -> float:
    """Power-size ratio ``J**(2/3)/J**(1/2)=J**(1/6)``."""

    if index_count <= 0:
        raise ValueError("index_count must be positive")
    return index_count ** (1.0 / 6.0)
