import pytest

from qp_two_index_poincare_polar_gate import (
    cusp_alignment_ledger,
    finite_support_cusp_operator_lower_bound,
    polar_projection_ledger,
    satake_prime_power_coefficients,
    spectral_row_value,
    two_index_kuznetsov_channels,
)


def test_complete_generic_two_index_channel_inventory() -> None:
    channels = two_index_kuznetsov_channels()
    assert channels.cuspidal
    assert channels.minimal_eisenstein
    assert channels.maximal_eisenstein_from_gl2_cusp
    assert not channels.residual_constant_generic_coefficient
    assert channels.identity_weyl
    assert channels.short_weyl_w4
    assert channels.short_weyl_w5
    assert channels.long_weyl_w6
    assert not channels.other_weyl_elements_for_generic_indices
    assert not channels.short_weyl_channels_are_spectral_projections


def test_complete_eisenstein_projection_is_target_contractive_but_not_source_contractive() -> None:
    size = 9
    data = tuple(1 / size**0.5 for _ in range(size))
    cusp_rows = (tuple(1 for _ in range(size)),)
    minimal_rows = (tuple(1 if index == 0 else 0 for index in range(size)),)
    maximal_rows = (tuple(1 if index == 1 else 0 for index in range(size)),)
    ledger = polar_projection_ledger(
        data,
        cusp_rows,
        minimal_eisenstein_rows=minimal_rows,
        maximal_eisenstein_rows=maximal_rows,
    )
    assert ledger.source_squared_norm == pytest.approx(1)
    assert ledger.cuspidal_residual_squared_norm == pytest.approx(size)
    assert ledger.complete_automorphic_squared_norm == pytest.approx(
        ledger.cuspidal_residual_squared_norm + ledger.polar_squared_norm
    )
    assert ledger.pythagorean_error == pytest.approx(0)
    assert ledger.automorphic_projection_is_contractive
    assert not ledger.physical_source_contraction_holds


def test_satake_coefficients_are_complete_homogeneous_symmetric_polynomials() -> None:
    # For alpha=(1,1,1), A(1,p^k)=binomial(k+2,2).
    coefficients = satake_prime_power_coefficients((1, 1, 1), 8)
    assert coefficients == pytest.approx(
        tuple((power + 1) * (power + 2) / 2 for power in range(9))
    )


def test_unitary_satake_fixture_has_growing_non_square_summable_energy() -> None:
    # (1,i,-i) has product one and poles on the unit circle.
    short = satake_prime_power_coefficients((1, 1j, -1j), 8)
    long = satake_prime_power_coefficients((1, 1j, -1j), 80)
    short_energy = sum(abs(value) ** 2 for value in short)
    long_energy = sum(abs(value) ** 2 for value in long)
    assert long_energy > 5 * short_energy


def test_cusp_alignment_survives_every_eisenstein_projection() -> None:
    row = satake_prime_power_coefficients((1, 1, 1), 12)
    ledger = cusp_alignment_ledger(row, whittaker_weight_over_form_norm=0.25)
    expected_energy = sum(abs(value) ** 2 for value in row)
    assert ledger.coefficient_squared_energy == pytest.approx(expected_energy)
    assert ledger.normalized_source_squared_norm == pytest.approx(1)
    assert ledger.retained_cusp_squared_norm == pytest.approx(0.25 * expected_energy)
    assert ledger.amplification_over_source == pytest.approx(0.25 * expected_energy)
    assert finite_support_cusp_operator_lower_bound(expected_energy, 0.25) == pytest.approx(
        ledger.retained_cusp_squared_norm
    )


def test_spectral_row_uses_both_physical_indices_after_flattening() -> None:
    # Flattened labels may be (b,n), but no sum over b is lost.
    data = (2 + 1j, -3, 4 - 2j)
    two_index_coefficients = (5, 7j, -2 + 3j)
    assert spectral_row_value(data, two_index_coefficients) == sum(
        value * coefficient
        for value, coefficient in zip(data, two_index_coefficients)
    )

