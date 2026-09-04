"""Exact exponent ledger for the Fu--Guth--Maldague QP audit."""

from fractions import Fraction


TIME_EXPONENT = Fraction(50, 33)
D_EXPONENT = 2 - TIME_EXPONENT
CRITICAL_BLOCK_EXPONENT = 1 - TIME_EXPONENT / 2
MACROBLOCK_LENGTH_EXPONENT = Fraction(1, 2)


def fgm_full_sequence_loss(p: Fraction) -> Fraction:
    """The exponent ``1/4-1/(2p)`` in FGM Theorem 7.1."""

    if p < 2 or p > 6:
        raise ValueError("Theorem 7.1 requires 2<=p<=6")
    return Fraction(1, 4) - Fraction(1, 2) / p


def local_l3_loss() -> Fraction:
    """The q-exponent of ``R^(1/6)=D^(1/12)``."""

    return CRITICAL_BLOCK_EXPONENT / 6


def fgm_global_l3_loss() -> Fraction:
    """The q-exponent after Theorem 7.1 at p=3."""

    return local_l3_loss() + fgm_full_sequence_loss(Fraction(3))
