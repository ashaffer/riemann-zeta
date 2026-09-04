#!/usr/bin/env python3
"""Verify the weighted rough-transition exponent and finite identities."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from weighted_rough_transition_gate import (  # noqa: E402
    B_MAX,
    B_MIN,
    KAPPA_MAX,
    closure_exponent_ledger,
    finite_post_q_audit,
    linear_sieve_frontier,
    localized_sieve_parameter,
)


bottom = linear_sieve_frontier(B_MIN)
top = linear_sieve_frontier(B_MAX)
assert bottom["s"] == str(Fraction(6926, 1537))
assert top["s"] == str(Fraction(67, 33))
assert bottom["lower_u_threshold"] == str(Fraction(2821, 10_000))
assert top["lower_u_threshold"] == str(Fraction(100, 399))
assert not bottom["fixed_s_gives_power_discrepancy"]
assert not top["fixed_s_gives_power_discrepancy"]
assert localized_sieve_parameter(B_MAX, B_MIN, B_MIN) == Fraction(-78842, 204421)
assert localized_sieve_parameter(B_MAX, B_MAX, B_MAX) == -1

delta = Fraction(1, 10_000)
closure = closure_exponent_ledger(KAPPA_MAX, delta)
target = 1 - KAPPA_MAX - delta
assert closure["l2_output_exponent"] == str(target)
assert closure["l4_output_exponent"] == str(target)
assert closure["l2_current_deficit_at_delta_zero"] == str(
    Fraction(797, 5000) + 2 * KAPPA_MAX
)
assert closure["l4_current_deficit_at_delta_zero"] == str(
    Fraction(797, 5000) + 4 * KAPPA_MAX
)

# The arbitrary-selector L2 target is impossible at q=H: blockwise residue
# reduction can be injective, while retained balanced semiprimes contribute
# Y/log Y physical diagonal mass.  The discarded integer lengths are
# power-smaller than Y/log Y.
l2_target_at_delta_zero = 1 - 2 * KAPPA_MAX
long_edge_length_exponent = Fraction(63827, 65000)
crossing_edge_length_exponent = 1 - B_MAX + Fraction(797, 5000)
assert l2_target_at_delta_zero < 1
assert long_edge_length_exponent < 1
assert crossing_edge_length_exponent == Fraction(606001, 665000) < 1

audit = finite_post_q_audit()
assert all(audit["certificates"].values())
assert audit["band"]["deleted_centres"] > 0
assert audit["band"]["twice_positive_mass"] == audit["band"]["twice_negative_mass"]

print("weighted rough-transition gate: PASS")
print(
    "first-band linear-sieve s-range="
    f"[{float(Fraction(top['s'])):.12f}, {float(Fraction(bottom['s'])):.12f}]"
)
print(
    "lower-positive u-thresholds="
    f"[{float(Fraction(top['lower_u_threshold'])):.12f}, "
    f"{float(Fraction(bottom['lower_u_threshold'])):.12f}]"
)
print(
    "critical-block per-(I,p,residue) s-range="
    f"[{float(localized_sieve_parameter(B_MAX, B_MAX, B_MAX)):.12f}, "
    f"{float(localized_sieve_parameter(B_MAX, B_MIN, B_MIN)):.12f}]"
)
print(
    "L2 input/output exponents="
    f"{float(Fraction(closure['l2_input_exponent'])):.12f}/"
    f"{float(Fraction(closure['l2_output_exponent'])):.12f}"
)
print(
    "L4 input/output exponents="
    f"{float(Fraction(closure['l4_input_exponent'])):.12f}/"
    f"{float(Fraction(closure['l4_output_exponent'])):.12f}"
)
print(
    "coefficient-blind L2/L4 closure deficits="
    f"{float(Fraction(closure['l2_current_deficit_at_delta_zero'])):.12f}/"
    f"{float(Fraction(closure['l4_current_deficit_at_delta_zero'])):.12f}"
)
print(
    "injective-selector L2 floor/required exponent="
    f"1-o(1)/{float(l2_target_at_delta_zero):.12f}"
)
print(
    "finite band deleted/components="
    f"{audit['band']['deleted_centres']}/{audit['band']['deleted_components']}"
)
