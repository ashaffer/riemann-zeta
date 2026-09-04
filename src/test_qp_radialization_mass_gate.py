import math

from qp_radialization_mass_gate import (
    CENTER_FACTOR,
    PROJECT_WIDTH,
    canonical_positive_return_ledger,
    mass_normalized_depth,
    minimum_prime_count_for_event,
    phase_localization_constant,
    probability_depth_from_mass_event,
    radial_depth_from_transverse_return,
    radial_pairing_value,
    required_transverse_return,
    singleton_certificate,
    singleton_height_bounds,
)


def test_singleton_is_exactly_negative_one() -> None:
    cert = singleton_certificate(101)
    assert cert.center == 101.5
    assert cert.node < PROJECT_WIDTH
    assert math.isclose(cert.cosine, -1.0, abs_tol=1.0e-14)
    assert math.isclose(cert.probability_depth, 1.0, abs_tol=1.0e-14)


def test_singleton_height_bounds_and_polynomial_band() -> None:
    cert = singleton_certificate(101)
    lower, upper = singleton_height_bounds(101)
    assert lower <= cert.height <= upper
    reference_scale = 100.0
    assert reference_scale**0.5 <= cert.height <= reference_scale**1.5
    assert reference_scale <= cert.center <= CENTER_FACTOR * reference_scale


def test_larger_half_integer_offset_covers_sublinear_top_band() -> None:
    prime = 101
    offset = 12.5
    cert = singleton_certificate(prime, offset)
    lower, upper = singleton_height_bounds(prime, offset)
    assert lower <= cert.height <= upper
    assert math.isclose(cert.cosine, -1.0, abs_tol=1.0e-14)


def test_mass_normalization_removes_singleton_saturation() -> None:
    assert math.isclose(mass_normalized_depth(1.0, 1, 1000.0), 0.001)
    assert math.isclose(mass_normalized_depth(0.2, 50, 1000.0), 0.01)


def test_phase_localization_constant() -> None:
    assert math.isclose(phase_localization_constant(7), 28.0 / 3.0)


def test_radial_pairing_has_exact_mass_factor() -> None:
    assert math.isclose(radial_pairing_value(50, 1000.0, 0.02), 0.001)


def test_threshold_event_forces_long_prime_interval() -> None:
    assert minimum_prime_count_for_event(1_000_000.0, 0.001) == 1000
    assert math.isclose(probability_depth_from_mass_event(0.001, 2000, 1_000_000), 0.5)


def test_transverse_return_mixes_to_exact_radial_depth() -> None:
    assert math.isclose(radial_depth_from_transverse_return(0.2, 0.25), 0.04)
    needed = required_transverse_return(0.2, 0.04)
    assert math.isclose(needed, 0.25)


def test_full_band_forces_canonical_positive_return_at_ledger_scale() -> None:
    center = 1.0e6
    ledger = canonical_positive_return_ledger(
        center, center ** (50.0 / 33.0), 10_000
    )
    assert ledger["second_moment_lower"] > 0.0
    assert ledger["mean_error"] < ledger["second_moment_lower"]
    assert ledger["positive_return_lower"] > 0.0
