#!/usr/bin/env python3
"""Verify the exact identities and exponent ledger in the transfer kill test."""

import cmath
import math
from fractions import Fraction as F


BETA = F(1537, 10000)
THETA = F(797, 5000)
KAPPA = F(90_151_617, 5_000_000_000)
B = F(39, 250)


def close(a: complex, b: complex, tol: float = 2e-10) -> None:
    if abs(a - b) > tol:
        raise AssertionError((a, b, abs(a - b)))


def nodes_from_gaps(start: int, gaps: list[int]) -> list[int]:
    out = [start]
    for gap in gaps:
        out.append(out[-1] + gap)
    return out


def trapezoid(nodes: list[int], z: complex) -> complex:
    return sum(
        (nodes[j + 1] - nodes[j])
        * (z ** nodes[j] + z ** nodes[j + 1])
        / 2
        for j in range(len(nodes) - 1)
    )


# Section 1: exact geometric/cotangent transfer.
q = 101
a = 1
z = cmath.exp(2j * math.pi * a / q)
p = 10001
g = 18
edge_t = g * z**p * (1 + z**g) / 2
edge_g = z**p * (1 - z**g) / (1 - z)
symbol = g * (1 - z) * (1 + z**g) / (2 * (1 - z**g))
close(edge_t, symbol * edge_g)
symbol_abs = g * abs(math.sin(math.pi * a / q)) * abs(
    1 / math.tan(math.pi * a * g / q)
)
assert abs(abs(symbol) - symbol_abs) < 2e-12

# The pole is genuine at an even resonant gap.
resonant_gap = 2 * q
resonant_g = z**p * (1 - z**resonant_gap) / (1 - z)
resonant_t = resonant_gap * z**p * (1 + z**resonant_gap) / 2
assert abs(resonant_g) < 2e-9
assert abs(resonant_t) > resonant_gap * 0.999999

# The opposite exact null: z^g=-1 makes T and m vanish while G survives.
q_null = 12
z_null = cmath.exp(2j * math.pi / q_null)
g_null = q_null // 2
null_t = g_null * z_null**p * (1 + z_null**g_null) / 2
null_g = z_null**p * (1 - z_null**g_null) / (1 - z_null)
null_symbol = (
    g_null
    * (1 - z_null)
    * (1 + z_null**g_null)
    / (2 * (1 - z_null**g_null))
)
assert abs(null_t) < 2e-9
assert abs(null_symbol) < 2e-9
assert abs(null_g) > 1

# Section 2: Wronskian and derivative identities on a nonuniform mesh.
nodes = [10001, 10007, 10017, 10029, 10047]
x = [z**n for n in nodes]
t_direct = trapezoid(nodes, z)
wronskian = (
    nodes[-1] * x[-1]
    - nodes[0] * x[0]
    + sum(
        nodes[j + 1] * x[j] - nodes[j] * x[j + 1]
        for j in range(len(nodes) - 1)
    )
) / 2
close(t_direct, wronskian)

# Per-edge form (D-c)D_j, evaluating D=z d/dz algebraically.
derivative_form = 0j
for left, right in zip(nodes[:-1], nodes[1:]):
    delta_value = z**right - z**left
    delta_derivative = right * z**right - left * z**left
    midpoint = (left + right) / 2
    derivative_form += delta_derivative - midpoint * delta_value
close(t_direct, derivative_form)

# Vertex collection agrees with the edge form.
gaps = [nodes[j + 1] - nodes[j] for j in range(len(nodes) - 1)]
weights = [gaps[0] / 2]
weights += [(gaps[j - 1] + gaps[j]) / 2 for j in range(1, len(nodes) - 1)]
weights += [gaps[-1] / 2]
close(t_direct, sum(w * phase for w, phase in zip(weights, x)))

# Exact Abel comparison with log weights.
ell = [math.log(n) for n in nodes]
difference = [w - e for w, e in zip(weights, ell)]
prefix = []
running = 0.0
for value in difference:
    running += value
    prefix.append(running)
abel = prefix[-1] * x[-1] + sum(
    prefix[j] * (x[j] - x[j + 1]) for j in range(len(nodes) - 1)
)
close(sum(v * phase for v, phase in zip(difference, x)), abel)
for k in range(len(nodes) - 1):
    expected = nodes[k] - nodes[0] + gaps[k] / 2 - sum(ell[: k + 1])
    assert abs(prefix[k] - expected) < 2e-12

# Section 3: exact consecutive-pair expansion for the same finite node set.
pair_expansion = 0j
for left, right in zip(nodes[:-1], nodes[1:]):
    h = right - left
    pair_expansion += h * (1 + z**h) * z**left / 2
close(t_direct, pair_expansion)

# Section 4: paired 2q relocation gadget.
d = 6
h_extension = 2 * q
# A base mesh of total length 2q, with the final even remainder merged.
n_full = (2 * q) // d
remainder = 2 * q - n_full * d
base_gaps = [d] * n_full
if remainder:
    base_gaps[-1] += remainder
assert sum(base_gaps) == 2 * q
assert all(gap % 2 == 0 for gap in base_gaps)
l = q // (2 * d)
assert 0 < l < len(base_gaps)
gaps_a = base_gaps.copy()
gaps_b = base_gaps.copy()
gaps_a[0] += h_extension
gaps_b[l] += h_extension
nodes_a = nodes_from_gaps(p, gaps_a)
nodes_b = nodes_from_gaps(p, gaps_b)
assert nodes_a[-1] == nodes_b[-1]
assert all(n % 2 == 1 for n in nodes_a + nodes_b)

# Every corresponding rational phase, and hence the ordinary sum, is exact.
for left_phase, right_phase in zip(nodes_a, nodes_b):
    close(z**left_phase, z**right_phase)
close(sum(z**n for n in nodes_a), sum(z**n for n in nodes_b))

t_a = trapezoid(nodes_a, z)
t_b = trapezoid(nodes_b, z)
relocation_formula = (
    h_extension
    * (1 + z**d)
    * (z**p - z ** (p + l * d))
    / 2
)
close(t_a - t_b, relocation_formula)
assert abs(t_a - t_b) > 2.5 * q

# Only the nodes between the two relocation edges move.  Check the exact
# log-weight difference and its elementary Lipschitz bound.
log_difference = sum(math.log(n) * z**n for n in nodes_a) - sum(
    math.log(n) * z**n for n in nodes_b
)
explicit_log_difference = sum(
    (math.log(nodes_b[j] + h_extension) - math.log(nodes_b[j]))
    * z ** nodes_b[j]
    for j in range(1, l + 1)
)
close(log_difference, explicit_log_difference, tol=2e-9)
log_bound = l * h_extension / min(nodes_b[1 : l + 1])
assert abs(log_difference) <= log_bound * (1 + 1e-12)

# Sections 4.2 and 5: exact exponent arithmetic.
gt_tail = F(9, 13) * (B - F(2, 15))
gap_square_exponent = 1 + B - KAPPA
gap_third_exponent = 1 + 2 * B - KAPPA
cached_third_exponent = F(84_549, 65_000)
smooth_mode_exponent = -1 + B - KAPPA
vaughan_saving = BETA / 2
allowable_transfer_loss = vaughan_saving - KAPPA
condition_loss_bottom = 1 - BETA
condition_loss_top = 1 - THETA

assert gt_tail == F(51, 3250)
assert gt_tail < KAPPA
assert gap_square_exponent == F(5_689_848_383, 5_000_000_000)
assert gap_square_exponent < F(123, 100)
assert gap_third_exponent == F(6_469_848_383, 5_000_000_000)
assert gap_third_exponent < cached_third_exponent
assert smooth_mode_exponent == F(-4_310_151_617, 5_000_000_000)
assert vaughan_saving == F(1537, 20_000)
assert allowable_transfer_loss == F(294_098_383, 5_000_000_000)
assert condition_loss_bottom == F(8463, 10_000)
assert condition_loss_top == F(4203, 5000)
assert condition_loss_top > allowable_transfer_loss

print("rational discrete-transfer kill test: PASS")
print(f"relocation |Delta T|/q={abs(t_a - t_b) / q:.12f}")
print(f"GT tail saving at b=.156={float(gt_tail):.12f}")
print(f"gap-square exponent={float(gap_square_exponent):.10f}")
print(f"gap-third exponent={float(gap_third_exponent):.10f}")
print(f"smooth ordinary-mode exponent={float(smooth_mode_exponent):.10f}")
print(f"Vaughan allowable transfer loss={float(allowable_transfer_loss):.10f}")
print(f"minimum shell condition loss={float(condition_loss_top):.10f}")
