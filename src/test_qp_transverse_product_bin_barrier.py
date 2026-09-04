from fractions import Fraction

import pytest

from qp_transverse_product_bin_barrier import (
    ProductBinBarrierLedger,
    active_ledger,
    kurtosis_spike_lower,
    pigeonhole_maximum,
)


def test_active_product_bin_and_transverse_exponents() -> None:
    ledger = active_ledger()
    assert ledger.product_bin_exponent == Fraction(16, 33)
    assert ledger.fourth_moment_transverse_exponent == Fraction(49, 66)


def test_every_fixed_power_saving_changes_the_exponent() -> None:
    ledger = active_ledger()
    saved = ledger.proposed_saved_bin_exponent(Fraction(1, 10))
    assert saved == Fraction(24, 55)
    assert saved < ledger.product_bin_exponent
    with pytest.raises(ValueError):
        ledger.proposed_saved_bin_exponent(Fraction(0))


def test_pigeonhole_bin_occupancy() -> None:
    assert pigeonhole_maximum(101, 10) == 11
    assert pigeonhole_maximum(100, 10) == 10
    assert pigeonhole_maximum(0, 7) == 0
    with pytest.raises(ValueError):
        pigeonhole_maximum(10, 0)


def test_rank_one_local_spike_has_m_squared_over_band_scale() -> None:
    first = kurtosis_spike_lower(
        coordinate_count=100,
        band_scale=10_000.0,
        spike_height_fraction=0.2,
        spike_width=0.5,
        density_fraction=0.3,
        quadratic_upper_constant=2.0,
    )
    second = kurtosis_spike_lower(
        coordinate_count=200,
        band_scale=10_000.0,
        spike_height_fraction=0.2,
        spike_width=0.5,
        density_fraction=0.3,
        quadratic_upper_constant=2.0,
    )
    assert second == pytest.approx(4.0 * first)


def test_invalid_ledger_and_spike_inputs() -> None:
    with pytest.raises(ValueError):
        ProductBinBarrierLedger(Fraction(2))
    with pytest.raises(ValueError):
        kurtosis_spike_lower(0, 1.0, 0.2, 0.5, 0.3, 2.0)
