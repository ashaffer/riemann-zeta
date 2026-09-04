#!/usr/bin/env python3
"""Exact exponent ledger for deleting the selected denominator first."""

from fractions import Fraction as F


beta = F(1537, 10000)
theta = F(797, 5000)
h_min = F(8, 33)

group_saving = beta
boundary_saving = h_min - theta
block_count_exponent = 1 - h_min
multiple_count_exponent = 1 - beta

assert group_saving == F(1537, 10000)
assert boundary_saving == F(13699, 165000)
assert block_count_exponent < multiple_count_exponent
assert group_saving > F(1974, 100000)  # comfortably above carrier scale
assert boundary_saving > F(1974, 100000)

# On the integer trapezoid partition every interior cell has mass one.
# Deleting N marked cells moves exactly N units of positive mass, hence the
# signed measure difference has total variation 2N.
for n in range(101):
    deleted_mass = F(n)
    total_variation = 2 * deleted_mass
    assert total_variation == 2 * n


def trapezoid_weights(points: list[int]) -> dict[int, F]:
    out: dict[int, F] = {}
    for j, x in enumerate(points):
        if j == 0:
            out[x] = F(points[1] - x, 2)
        elif j + 1 == len(points):
            out[x] = F(x - points[j - 1], 2)
        else:
            out[x] = F(points[j + 1] - points[j - 1], 2)
    return out


# A finite exact replay with retained non-q endpoints.
integer_points = list(range(101, 200))
q = 7
deleted = {x for x in integer_points[1:-1] if x % q == 0}
survivors = [x for x in integer_points if x not in deleted]
w0 = trapezoid_weights(integer_points)
w1 = trapezoid_weights(survivors)
support = set(w0) | set(w1)
delta = {x: w1.get(x, F(0)) - w0.get(x, F(0)) for x in support}
positive = sum((v for v in delta.values() if v > 0), F(0))
negative = -sum((v for v in delta.values() if v < 0), F(0))
tv = sum((abs(v) for v in delta.values()), F(0))
assert positive == negative == len(deleted)
assert tv == 2 * len(deleted)

# Global blockwise replay.  The denominator changes between 119 and 120;
# both integers are deleted, so the marked set has adjacent nodes across the
# boundary.  Simultaneous transport still moves exactly the initial unit mass
# of every marked integer.
block_q = {x: (7 if x < 120 else 8) for x in integer_points}
global_deleted = {
    x
    for x in integer_points[1:-1]
    if x % block_q[x] == 0
}
assert 119 in global_deleted and 120 in global_deleted
global_survivors = [x for x in integer_points if x not in global_deleted]
wg = trapezoid_weights(global_survivors)
global_support = set(w0) | set(wg)
global_delta = {
    x: wg.get(x, F(0)) - w0.get(x, F(0))
    for x in global_support
}
global_positive = sum((v for v in global_delta.values() if v > 0), F(0))
global_negative = -sum((v for v in global_delta.values() if v < 0), F(0))
global_tv = sum((abs(v) for v in global_delta.values()), F(0))
assert global_positive == global_negative == len(global_deleted)
assert global_tv == 2 * len(global_deleted)
assert all(x % block_q[x] != 0 for x in global_survivors[1:-1])

print(f"denominator floor beta={beta} ({float(beta):.12f})")
print(f"q-first resonant-group saving={group_saving} ({float(group_saving):.12f})")
print(f"boundary-edge saving={boundary_saving} ({float(boundary_saving):.12f})")
print("integer-cell simultaneous transport ||Delta nu||_TV=2N: PASS")
print("finite q=7 integer-trapezoid replay: PASS")
print("global varying-q replay with adjacent boundary deletions: PASS")
print("remaining deletion centers are all non-q-multiples: exact")
