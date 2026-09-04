#!/usr/bin/env python3
"""Exact ledger for the same-residue consecutive-gap pole-sector audit."""

from fractions import Fraction
import cmath
import math


def close(x: float, y: float, tol: float = 1e-12) -> None:
    if abs(x - y) > tol:
        raise AssertionError((x, y))


beta = Fraction(1537, 10000)
theta = Fraction(797, 5000)
kappa = Fraction(90151617, 5_000_000_000)


def c_gt(b: Fraction) -> Fraction:
    return (45 * b - 6) / 65


c_beta = c_gt(beta)
c_theta = c_gt(theta)
deficit = kappa - c_beta
b_star = (65 * kappa + 6) / 45

assert c_beta == Fraction(141, 10000)
assert c_theta == Fraction(1173, 65000)
assert deficit == Fraction(19651617, 5_000_000_000)
assert b_star == Fraction(796885669, 5_000_000_000)
assert beta < b_star < theta
assert c_theta > kappa

# Corridor and dimension-two pair-sieve ledgers.
assert theta - beta == Fraction(57, 10000)
assert theta - b_star == Fraction(114331, 5_000_000_000)
pair_sieve_exponent = 2 * theta - beta
assert pair_sieve_exponent == Fraction(1651, 10000)
assert pair_sieve_exponent > 0

# A tail allocation saturating the divisor-average Markov count at b=beta.
bad_modulus_exponent = deficit
per_modulus_mass_exponent = -kappa
total_mass_exponent = bad_modulus_exponent + per_modulus_mass_exponent
assert total_mass_exponent == -c_beta
assert bad_modulus_exponent < beta  # enough prime-sized modulus slots

gap_count_exponent = 1 - beta - c_beta
occupied_length_exponent = gap_count_exponent + beta
gap_square_exponent = gap_count_exponent + 2 * beta
gap_third_exponent = gap_count_exponent + 3 * beta
assert gap_count_exponent == Fraction(4161, 5000)  # .8322
assert occupied_length_exponent == 1 - c_beta
assert gap_square_exponent == Fraction(2849, 2500)  # 1.1396
assert gap_third_exponent == Fraction(12933, 10000)  # 1.2933
assert gap_square_exponent < Fraction(123, 100)
assert gap_third_exponent < Fraction(84549, 65000)

# The pair-sieve exponent is q*K^2 with K=Y^(theta-beta).
pair_sieve_from_k = beta + 2 * (theta - beta)
assert pair_sieve_from_k == pair_sieve_exponent

# The principal transition character is harmless at the lower endpoint.
assert beta > kappa

# Exact multiplicative-character transition identity at a prime modulus.
q_char = 7
primitive_root = 3
states_char = list(range(1, q_char))
discrete_log = {}
value = 1
for exponent in range(q_char - 1):
    discrete_log[value] = exponent
    value = value * primitive_root % q_char
assert sorted(discrete_log) == states_char


def character(index: int, residue: int) -> complex:
    angle = 2 * math.pi * index * discrete_log[residue % q_char] / (q_char - 1)
    return cmath.exp(1j * angle)


for left in states_char:
    for right in states_char:
        orthogonality = sum(
            character(index, right) * character(index, left).conjugate()
            for index in range(q_char - 1)
        ) / (q_char - 1)
        expected = 1.0 if left == right else 0.0
        assert abs(orthogonality - expected) < 2e-12

# Verify both weighted transition formulas (5.2)--(5.3) on a finite list.
starts = [1, 2, 3, 4, 5]
ends = [1, 3, 3, 6, 5]
weights = [0.07, 0.11, 0.13, 0.17, 0.19]
r_char = 2
direct_mass = sum(
    weight for left, right, weight in zip(starts, ends, weights) if left == right
)
character_mass = sum(
    sum(
        weight
        * character(index, right)
        * character(index, left).conjugate()
        for left, right, weight in zip(starts, ends, weights)
    )
    for index in range(q_char - 1)
) / (q_char - 1)
assert abs(character_mass - direct_mass) < 2e-12

direct_signed = sum(
    weight * cmath.exp(2j * math.pi * r_char * left / q_char)
    for left, right, weight in zip(starts, ends, weights)
    if left == right
)
character_signed = sum(
    sum(
        weight
        * cmath.exp(2j * math.pi * r_char * left / q_char)
        * character(index, right)
        * character(index, left).conjugate()
        for left, right, weight in zip(starts, ends, weights)
    )
    for index in range(q_char - 1)
) / (q_char - 1)
assert abs(character_signed - direct_signed) < 2e-12

# Finite divisor-sparsity identity: summing pole masses over a dyadic shell
# counts each gap by no more than its divisor function.
finite_gaps = [30, 42, 60, 70, 84, 90]
finite_weights = [Fraction(gap, 1000) for gap in finite_gaps]
q_low, q_high = 10, 20
lhs_divisor = sum(
    sum(
        weight
        for gap, weight in zip(finite_gaps, finite_weights)
        if gap % modulus == 0
    )
    for modulus in range(q_low + 1, q_high + 1)
)


def divisor_count(value: int) -> int:
    return sum(value % divisor == 0 for divisor in range(1, value + 1))


rhs_divisor = sum(
    weight * divisor_count(gap)
    for gap, weight in zip(finite_gaps, finite_weights)
    if gap >= q_low
)
assert lhs_divisor <= rhs_divisor

# Finite exact-marginal witness: a permutation fixes a phase arc and cycles
# its complement.  Both endpoint marginals are uniform, while the signed
# diagonal is macroscopically nonzero.
q = 101
states = list(range(1, q))
arc = [a for a in states if abs(cmath.phase(cmath.exp(2j * math.pi * a / q))) <= math.pi / 3]
complement = [a for a in states if a not in set(arc)]
assert len(complement) >= 2

perm = {a: a for a in arc}
for i, a in enumerate(complement):
    perm[a] = complement[(i + 1) % len(complement)]
assert sorted(perm) == states
assert sorted(perm.values()) == states
assert all(perm[a] == a for a in arc)
assert all(perm[a] != a for a in complement)

# Joint mass 1/(q-1) on (a,perm(a)); verify exact uniform marginals.
row = {a: Fraction(1, q - 1) for a in states}
col = {a: Fraction(0, 1) for a in states}
for a in states:
    col[perm[a]] += Fraction(1, q - 1)
assert len(set(row.values())) == 1
assert col == row

signed_diagonal = sum(cmath.exp(2j * math.pi * a / q) for a in arc) / (q - 1)
diagonal_mass = Fraction(len(arc), q - 1)
assert abs(signed_diagonal) >= 0.5 * float(diagonal_mass) - 1e-12

# Mixing with a derangement scales the diagonal statistic while preserving
# both exact uniform marginals.
mixing_weight = Fraction(3, 10)
mixed_signed_diagonal = float(mixing_weight) * signed_diagonal
assert abs(mixed_signed_diagonal) <= abs(signed_diagonal)

# Block normalization in the final sufficient theorem: local bounds weighted
# by m_I sum without a factor equal to the number of blocks.
block_masses = [Fraction(1, 10), Fraction(2, 10), Fraction(3, 10), Fraction(4, 10)]
assert sum(block_masses) == 1
local_factor = Fraction(1, 1000)
assert sum(mass * local_factor for mass in block_masses) == local_factor

print("PASS same-residue gap pole-sector ledger")
print(f"c_GT(beta)={float(c_beta):.10f}")
print(f"deficit={float(deficit):.10f}")
print(f"b_star={float(b_star):.10f}")
print(f"bad_modulus_exponent={float(bad_modulus_exponent):.10f}")
print(f"pair_sieve_exponent={float(pair_sieve_exponent):.10f}")
print(f"finite_diagonal_mass={float(diagonal_mass):.10f}")
print(f"finite_signed_diagonal={abs(signed_diagonal):.10f}")
print("transition characters, divisor sparsity, and block normalization: PASS")
