#!/usr/bin/env python3
"""Replay the finite radialization normalization ledger."""

from qp_radialization_mass_gate import (
    canonical_positive_return_ledger,
    mass_normalized_depth,
    minimum_prime_count_for_event,
    phase_localization_constant,
    radial_pairing_value,
    radial_depth_from_transverse_return,
    singleton_certificate,
    singleton_height_bounds,
)


def main() -> None:
    prime = 101
    scale = 100.0
    cert = singleton_certificate(prime)
    lower, upper = singleton_height_bounds(prime)
    corrected = mass_normalized_depth(cert.probability_depth, 1, scale)
    paired = radial_pairing_value(50, 1000.0, 0.02)
    long_count = minimum_prime_count_for_event(1_000_000.0, 0.001)
    mixed = radial_depth_from_transverse_return(0.2, 0.25)
    returned = canonical_positive_return_ledger(
        1.0e6, 1.0e6 ** (50.0 / 33.0), 10_000
    )["positive_return_lower"]
    assert abs(cert.cosine + 1.0) < 1.0e-14
    assert lower <= cert.height <= upper
    assert corrected == 0.01
    assert paired == 0.001
    assert long_count == 1000
    assert mixed == 0.04
    assert returned > 0.0
    print(
        "PASS "
        f"p={prime} Y={cert.center:.6g} t={cert.height:.9g} "
        f"cos={cert.cosine:.9g} E_singleton={corrected:.9g} "
        f"phase_constant={phase_localization_constant(7):.9g} "
        f"pairing={paired:.9g} long_count={long_count} mixed={mixed:.9g} "
        f"positive_return={returned:.9g}"
    )


if __name__ == "__main__":
    main()
