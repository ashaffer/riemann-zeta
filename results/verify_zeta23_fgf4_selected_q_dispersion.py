#!/usr/bin/env python3
"""Replay the FGF4 selected-q dispersion and Buchstab fail-fast audit."""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fgf4_selected_q_dispersion import (  # noqa: E402
    buchstab_bilinear_audit,
    buchstab_sector_cauchy_audit,
    endpoint_parity_countermodel,
    selected_dispersion_audit,
)


KAPPA = Fraction(1974048259, 100000000000)
BETA_MIN = Fraction(1537, 10000)
ONE_EIGHTH = Fraction(1, 8)
H_TOP = Fraction(33, 133)


def close(left: complex | float, right: complex | float, scale: float = 1.0) -> None:
    assert abs(left - right) <= 5e-8 * max(1.0, scale)


def exponent_ledger() -> dict[str, Fraction]:
    delta = KAPPA / BETA_MIN
    eta = delta - ONE_EIGHTH
    l2_close_ratio = 1 + 2 * delta
    largest_b_for_top_h = H_TOP / l2_close_ratio
    assert delta > ONE_EIGHTH
    assert eta > Fraction(34351502, 10_000_000_000)
    assert largest_b_for_top_h < H_TOP
    return {
        "delta_required": delta,
        "eta_beyond_one_eighth": eta,
        "l2_required_h_over_b": l2_close_ratio,
        "largest_b_for_top_h": largest_b_for_top_h,
        "endpoint_l2_q_exponent_deficit": delta,
        "endpoint_l4_energy_exponent": 3 - 4 * delta,
    }


def main() -> None:
    exponents = exponent_ledger()

    endpoint = selected_dispersion_audit(100003, 101005, 1003)
    assert endpoint.pair_count == 8
    assert endpoint.positive_q_shift_pairs == 0
    close(endpoint.twisted_sum, -1j * endpoint.additive_sum)
    close(
        endpoint.selected_square_from_differences,
        abs(endpoint.additive_sum) ** 2,
        abs(endpoint.additive_sum) ** 2,
    )
    assert endpoint.centered_variance == endpoint.centered_variance_from_q_shifts
    assert endpoint.centered_variance == Fraction(
        endpoint.pair_count * (endpoint.modulus - endpoint.pair_count),
        endpoint.modulus,
    )
    close(
        endpoint.parseval_second_lhs,
        endpoint.parseval_second_rhs,
        endpoint.parseval_second_rhs,
    )
    close(
        endpoint.parseval_fourth_lhs,
        endpoint.parseval_fourth_rhs,
        endpoint.parseval_fourth_rhs,
    )

    buchstab = buchstab_bilinear_audit(10003, 14003, 83, 7)
    assert buchstab.subtraction_rows > 0
    close(
        buchstab.direct,
        buchstab.rough_term - buchstab.subtraction_term,
        abs(buchstab.rough_term) + abs(buchstab.subtraction_term),
    )
    close(
        buchstab.subtraction_term,
        buchstab.transformed_bilinear_term,
        abs(buchstab.subtraction_term),
    )

    cauchy = buchstab_sector_cauchy_audit(10003, 40003, 83, 7, 7, 200)
    assert cauchy.outer_rows > 0 and cauchy.diagonal_zero_mode > 0
    close(cauchy.cauchy_energy, cauchy.expanded_energy, cauchy.cauchy_energy)
    assert abs(cauchy.direct_form) ** 2 <= (
        cauchy.outer_rows * cauchy.cauchy_energy + 1e-7
    )

    countermodel = endpoint_parity_countermodel(100003, 1003)
    assert countermodel.arc_width_radians < math.pi / 2
    assert (
        abs(countermodel.twisted_sum)
        >= countermodel.geometric_lower_bound - 1e-9
    )
    assert countermodel.geometric_lower_bound > countermodel.support_size / 2

    print("FGF4 selected-q dispersion audit: PASS")
    for name, value in exponents.items():
        print(f"{name}={float(value):.12f}")
    print(
        "endpoint",
        {
            "q": endpoint.modulus,
            "pairs": endpoint.pair_count,
            "q_shift_offdiagonal_pairs": endpoint.positive_q_shift_pairs,
            "centered_variance": float(endpoint.centered_variance),
            "selected_abs": abs(endpoint.twisted_sum),
        },
    )
    print(
        "buchstab",
        {
            "subtraction_rows": buchstab.subtraction_rows,
            "identity_error": abs(
                buchstab.direct - buchstab.rough_term + buchstab.subtraction_term
            ),
            "bilinear_transform_error": abs(
                buchstab.subtraction_term - buchstab.transformed_bilinear_term
            ),
        },
    )
    print(
        "cauchy",
        {
            "outer_rows": cauchy.outer_rows,
            "zero_mode": cauchy.diagonal_zero_mode,
            "energy": cauchy.cauchy_energy,
            "expansion_error": abs(cauchy.cauchy_energy - cauchy.expanded_energy),
        },
    )
    print(
        "local-admissibility countermodel",
        {
            "support": countermodel.support_size,
            "arc_width": countermodel.arc_width_radians,
            "selected_abs": abs(countermodel.twisted_sum),
            "certified_lower": countermodel.geometric_lower_bound,
        },
    )


if __name__ == "__main__":
    main()
