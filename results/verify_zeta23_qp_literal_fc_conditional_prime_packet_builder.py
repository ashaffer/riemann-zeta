#!/usr/bin/env python3
"""Exact algebra checks for the conditional literal-FC prime packet audit."""

from math import gcd, log

import sympy as sp


x, y, z = 100, 101, 103
n = (x * y * z) ** 2
r1, r2, r3 = (y * z) ** 3, (x * z) ** 3, (x * y) ** 3
a0 = 7_206_685_485_100_449
b0 = -6_994_737_931_165_371
c0 = 107_223

assert n == 1_082_224_090_000
assert (r1, r2, r3) == (
    1_125_837_720_827,
    1_092_727_000_000,
    1_030_301_000_000,
)
assert r1 * r2 * r3 == n**3
assert a0 * x**3 + b0 * y**3 + c0 * z**3 == 3 * x * y * z // 2

T, i, j = sp.symbols("T i j", integer=True)
q = 4 * n * T + 1
A = 2 * r1 * T + a0
B = 2 * r2 * T + b0
C = 2 * r3 * T + c0

base_residual = sp.Poly(sp.expand(8 * A * B * C - q**3), T)
assert base_residual.degree() <= 1

coefficients = (4 * n, 2 * r1, 2 * r2, 2 * r3)
constants = (1, a0, b0, c0)
assert all(gcd(coefficient, constant) == 1 for coefficient, constant in zip(coefficients, constants))

# Modulo 2 there is no root.  Modulo 3, T=1 avoids every root.  Four
# primitive linear forms cannot cover all residues modulo a prime p>=5.
for prime in (2, 3):
    good = [
        residue
        for residue in range(prime)
        if all((coefficient * residue + constant) % prime for coefficient, constant in zip(coefficients, constants))
    ]
    assert good
assert 1 in [
    residue
    for residue in range(3)
    if all((coefficient * residue + constant) % 3 for coefficient, constant in zip(coefficients, constants))
]

rho, alpha, beta = z**3, x**3, y**3
assert rho * (2 * r3) == alpha * (2 * r1)
assert rho * (2 * r3) == beta * (2 * r2)
assert gcd(alpha, beta) == 1
assert gcd(a0, rho) == gcd(b0, rho) == 1
assert gcd(c0, alpha) == gcd(c0, beta) == 1

a_i = A + rho * i
b_j = B + rho * j
c_ij = C - alpha * i - beta * j
packet_residual = sp.Poly(sp.expand(8 * a_i * b_j * c_ij - q**3), T)
assert packet_residual.degree() <= 1
assert sp.Poly(packet_residual.coeff_monomial(T), i, j).total_degree() <= 2
assert sp.Poly(packet_residual.coeff_monomial(1), i, j).total_degree() <= 3

ratios = (r1 / n, r2 / n, r3 / n)
print("n:", n)
print("ratios:", ratios)
print("max |log ratio|:", max(abs(log(value)) for value in ratios))
print("base residual degree:", base_residual.degree())
print("packet T-coefficient degree in (i,j):", sp.Poly(packet_residual.coeff_monomial(T), i, j).total_degree())
print("packet constant degree in (i,j):", sp.Poly(packet_residual.coeff_monomial(1), i, j).total_degree())
print("local admissibility modulo 2 and 3: PASS")
print("all exact checks: PASS")

