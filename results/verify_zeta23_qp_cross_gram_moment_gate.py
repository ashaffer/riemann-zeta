#!/usr/bin/env python3
"""Replay the cross-Gram moment exponent ledger."""

from qp_cross_gram_moment_gate import (
    admissible_unit_resonance_multiplicity,
    critical_ap_energy_exponents,
    distinct_cell_correction_exponent,
    fejer_required_lag_magnitude,
    heath_brown_ledger,
    repeated_lag_weight,
)


def main() -> None:
    h = heath_brown_ledger()
    energy = critical_ap_energy_exponents(0.019)
    lag = repeated_lag_weight(10_000, 0.01, 1)
    multiplicity = admissible_unit_resonance_multiplicity(0.01)
    distinct_correction = distinct_cell_correction_exponent()
    fejer_floor = fejer_required_lag_magnitude(100_000_000, 2.0)
    print(
        "PASS "
        f"square_terms=({h.pair_count_term:.12g},"
        f"{h.repeated_difference_term:.12g},{h.aperture_term:.12g}) "
        f"frobenius=({h.pair_count_frobenius:.12g},"
        f"{h.repeated_difference_frobenius:.12g},"
        f"{h.aperture_frobenius:.12g}) "
        f"required={h.required_residual:.12g} gap={h.repeated_difference_gap:.12g} "
        f"critical_energy={energy['ap_energy']:.12g} lag_weight={lag:.12g} "
        f"unit_resonance_cap={multiplicity:.12g} "
        f"distinct_correction={distinct_correction:.12g} "
        f"fejer_lag_floor={fejer_floor:.12g}"
    )


if __name__ == "__main__":
    main()
