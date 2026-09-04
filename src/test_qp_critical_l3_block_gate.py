from fractions import Fraction

import pytest

from qp_critical_l3_block_gate import (
    CriticalL3Ledger,
    dirichlet_reverse_square_ratio,
    local_block_l3_loss,
    normalized_aligned_peak,
)


def test_active_exponents() -> None:
    ledger = CriticalL3Ledger()
    assert ledger.D == Fraction(16, 33)
    assert ledger.block == Fraction(8, 33)
    assert ledger.l3_norm_loss == Fraction(4, 99)
    assert ledger.third_moment_loss == Fraction(4, 33)
    assert ledger.aligned_l4_peak == Fraction(16, 33)
    assert ledger.aligned_l3_peak == Fraction(-1, 66)


def test_local_loss_and_dirichlet_gap_match() -> None:
    assert local_block_l3_loss(64.0) == pytest.approx(2.0)
    assert dirichlet_reverse_square_ratio(64.0) == pytest.approx(2.0)


def test_aligned_peak_normalization() -> None:
    assert normalized_aligned_peak(16.0, 8.0, 4) == pytest.approx(32.0)
    assert normalized_aligned_peak(16.0, 8.0, 3) == pytest.approx(8.0)


@pytest.mark.parametrize("bad", [0.0, -1.0])
def test_positive_inputs_required(bad: float) -> None:
    with pytest.raises(ValueError):
        local_block_l3_loss(bad)
    with pytest.raises(ValueError):
        dirichlet_reverse_square_ratio(bad)
    with pytest.raises(ValueError):
        normalized_aligned_peak(bad, 1.0, 3)


def test_positive_moment_required() -> None:
    with pytest.raises(ValueError):
        normalized_aligned_peak(1.0, 1.0, 0)
