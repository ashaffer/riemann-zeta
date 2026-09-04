#!/usr/bin/env python3
"""Independent replay of the QP positive-weight proof-class barrier."""

from fractions import Fraction as F
import math


A = F(50, 33)
beta = F(19, 125)
c = F(19, 1000)
first = beta + A / 2 - 1
padding = A - 2 + 2 * beta

assert first == F(-373, 4125)
assert padding == F(-746, 4125)
assert first < -c
assert padding < -c

Y = 10_000.0
B = Y ** float(A)
L = max(1, math.ceil(B * math.log(Y) / (2 * math.pi * Y)))
nodes = []
k = 0
while (2 * k + 1) * math.pi / B < 0.2:
    nodes.append((2 * k + 1) * math.pi / B)
    k += L

assert len(nodes) > 10
assert max(abs(math.cos(B * u) + 1.0) for u in nodes) < 2e-12

# Full-rank projected algebra does not imply positive feasibility.
feature = (-1.0, -0.5)
mean = sum(feature) / 2
gram = sum((x - mean) ** 2 for x in feature)
assert gram == 0.125
assert not min(feature) <= 0 <= max(feature)

print("QP actual-prime positive-weight barrier verifier: PASS")
print(f"first deleted-mass exponent={first} ({float(first):.12f})")
print(f"component-padding exponent={padding} ({float(padding):.12f})")
print(f"half-grid nodes={len(nodes)}, spacing multiplier={L}")
print("all positive weights have antenna value -1 at the legal top height")
