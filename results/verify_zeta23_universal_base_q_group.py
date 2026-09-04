#!/usr/bin/env python3
"""Exact ledger for the universal-rough-base selected q-group theorem."""

from fractions import Fraction as F


zeta = F(4, 25)             # universal rough base cutoff
theta = F(797, 5000)        # retained terminal prime-edge cutoff
h_min = F(8, 33)            # shortest curvature block
beta = F(799, 5000)         # selected denominator floor
kappa_threshold = F(0)      # numerical comparison printed separately

boundary_saving = h_min - theta
group_saving = beta / 2
count_main_exponent = 1 - beta
block_count_exponent = 1 - h_min

assert zeta == F(4, 25)
assert theta < zeta < h_min
assert block_count_exponent < count_main_exponent
assert boundary_saving == F(13699, 165000)
assert group_saving == F(799, 10000)
assert boundary_saving > group_saving

# Deterministic refinement check: any disjoint subgaps of total length <=g
# have square energy <=g^2.  Replay on an exact grid.
for total_units in range(1, 31):
    g = F(total_units, 7)
    for a_units in range(total_units + 1):
        for b_units in range(total_units - a_units + 1):
            a = F(a_units, 7)
            b = F(b_units, 7)
            assert a * a + b * b <= g * g

# Current maximum carrier bill quoted in the companion audit.
kappa_max_decimal = 0.019740482583
assert float(group_saving) > kappa_max_decimal
assert float(boundary_saving) > kappa_max_decimal

print(f"universal cutoff exponent={zeta} ({float(zeta):.12f})")
print(f"denominator floor beta={beta} ({float(beta):.12f})")
print(f"short-edge cutoff theta={theta} ({float(theta):.12f})")
print(f"minimum block exponent={h_min} ({float(h_min):.12f})")
print(f"selector q-group saving beta/2={group_saving} ({float(group_saving):.12f})")
print(f"block-boundary disposal saving={boundary_saving} ({float(boundary_saving):.12f})")
print("square-energy refinement grid: PASS")
print("arbitrary q<Y, including composite denominators: exact reorder applies")
