#!/usr/bin/env python3
"""Exact exponent ledger for the late semiprime dispersion gate."""

from fractions import Fraction as F


B_MIN = F(1537, 10_000)
B_MAX = F(33, 133)
U_MIN = F(1, 3)
H_TOP = B_MAX
KAPPA = F(1_974_048_259, 100_000_000_000)


def separated_saving(u: F, b: F) -> F:
    """Power saved by Bazin's separated exact-rational surrogate."""

    return min(b / 2, (u - b) / 2, (1 - 3 * b) / 2)


corners = [
    separated_saving(u, b)
    for u in (U_MIN, F(1, 2))
    for b in (B_MIN, B_MAX)
]
uniform_saving = min(corners)
assert uniform_saving == F(17, 399)
assert separated_saving(U_MIN, B_MIN) == B_MIN / 2
assert separated_saving(U_MIN, B_MAX) == F(17, 399)
assert uniform_saving > KAPPA

# Fourier localization to a block needs theta=H^-1.  Bazin's additive
# twist term is Y Q^(3/2) theta^(1/2).
localized_twist_exponent = 1 + (3 * B_MAX - H_TOP) / 2
assert localized_twist_exponent == F(166, 133)

global_prefix_exponent = 1 - uniform_saving
local_target_exponent = H_TOP - KAPPA
prefix_deficit = global_prefix_exponent - local_target_exponent
assert global_prefix_exponent == F(382, 399)
assert prefix_deficit > F(7, 10)

block_count_exponent = 1 - H_TOP
denominator_count_exponent = H_TOP
forced_average_reuse_exponent = block_count_exponent - denominator_count_exponent
assert block_count_exponent == F(100, 133)
assert forced_average_reuse_exponent == F(67, 133)

# The tempting near-closure at h=1/2 compares Bazin's global-Y bound to the
# wrong scale.  A single block needs H*Y^-kappa, not Y^1-kappa.
h_half = F(1, 2)
raw_lambda_saving_half = (h_half - 3 * B_MIN) / 2
global_localized_exponent_half = 1 - raw_lambda_saving_half
block_target_exponent_half = h_half - KAPPA
local_normalization_deficit = (
    global_localized_exponent_half - block_target_exponent_half
)
formal_whole_y_closure_height = 3 * B_MIN + 2 * KAPPA
true_local_twist_closure_height = F(2, 3) + B_MIN + F(2, 3) * KAPPA
assert raw_lambda_saving_half == F(389, 20_000)
assert raw_lambda_saving_half < KAPPA
assert formal_whole_y_closure_height > h_half
assert true_local_twist_closure_height > F(5797, 10_000)
assert local_normalization_deficit > F(49, 100)

# At h=1/2 every late rectangle u<=1/2 has H<=R=Y^(1-u), hence at most one
# small prime p per fixed large factor r inside a block.
assert U_MIN <= 1 - h_half
assert F(1, 2) == 1 - h_half

print("late Buchstab semiprime dispersion gate: PASS")
print(
    "separated global saving="
    f"{uniform_saving} ({float(uniform_saving):.12f})"
)
print(
    "margin above hostile kappa="
    f"{float(uniform_saving - KAPPA):.12f}"
)
print(
    "top block-localization twist exponent="
    f"{localized_twist_exponent} ({float(localized_twist_exponent):.12f})"
)
print(
    "global-prefix/local-target exponents="
    f"{float(global_prefix_exponent):.12f}/"
    f"{float(local_target_exponent):.12f}"
)
print(f"prefix-difference deficit={float(prefix_deficit):.12f}")
print(
    "forced average denominator-reuse exponent="
    f"{forced_average_reuse_exponent} "
    f"({float(forced_average_reuse_exponent):.12f})"
)
print(
    "h=.5 Bazin-global/block-target exponents="
    f"{float(global_localized_exponent_half):.12f}/"
    f"{float(block_target_exponent_half):.12f}"
)
print(
    "h=.5 local-normalization deficit="
    f"{float(local_normalization_deficit):.12f}"
)
print(
    "formal whole-Y lambda closure height="
    f"{float(formal_whole_y_closure_height):.12f}"
)
print(
    "true local-block lambda closure height="
    f"{float(true_local_twist_closure_height):.12f}"
)
print("unique-large-factor range at h=.5: 1/3<u<=1/2")
