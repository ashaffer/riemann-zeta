from fractions import Fraction

import pytest

from qp_fgm_critical_l3_audit import (
    CRITICAL_BLOCK_EXPONENT,
    D_EXPONENT,
    MACROBLOCK_LENGTH_EXPONENT,
    fgm_full_sequence_loss,
    fgm_global_l3_loss,
    local_l3_loss,
)


def test_qp_scale_match() -> None:
    assert D_EXPONENT == Fraction(16, 33)
    assert CRITICAL_BLOCK_EXPONENT == Fraction(8, 33)
    assert CRITICAL_BLOCK_EXPONENT == D_EXPONENT / 2
    assert CRITICAL_BLOCK_EXPONENT < MACROBLOCK_LENGTH_EXPONENT


def test_one_macroblock_hits_the_l3_target() -> None:
    assert local_l3_loss() == Fraction(4, 99)
    assert local_l3_loss() == D_EXPONENT / 12


def test_theorem_7_1_pays_exact_flat_macroblock_loss() -> None:
    p = Fraction(3)
    loss = fgm_full_sequence_loss(p)
    flat_loss = MACROBLOCK_LENGTH_EXPONENT * (Fraction(1, 2) - 1 / p)
    assert loss == Fraction(1, 12)
    assert loss == flat_loss


def test_global_exponent_retains_q_one_twelfth() -> None:
    assert fgm_global_l3_loss() == Fraction(49, 396)
    assert fgm_global_l3_loss() - local_l3_loss() == Fraction(1, 12)
    assert 3 * (fgm_global_l3_loss() - local_l3_loss()) == Fraction(1, 4)


def test_theorem_7_1_range() -> None:
    with pytest.raises(ValueError):
        fgm_full_sequence_loss(Fraction(3, 2))
    with pytest.raises(ValueError):
        fgm_full_sequence_loss(Fraction(7))
