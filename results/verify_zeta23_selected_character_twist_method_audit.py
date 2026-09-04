#!/usr/bin/env python3
"""Check the exact identities and exponent arithmetic in the twist audit."""

import cmath
import math


THETA = 797 / 5000
BETA = 1537 / 10000
KAPPA = 0.0180303234


def legendre(a: int, q: int) -> complex:
    a %= q
    if a == 0:
        return 0j
    return complex(1 if pow(a, (q - 1) // 2, q) == 1 else -1)


def close(a: complex, b: complex, tol: float = 2e-12) -> None:
    if abs(a - b) > tol:
        raise AssertionError((a, b, abs(a - b)))


q = 7
primes = [11, 13, 17, 19, 23, 29]
y = 17.0
v = [math.log(p / y) for p in primes]
# A nonconstant smooth endpoint amplitude.
phi = [cmath.exp(0.17 * z) * (1 + 0.03 * z) for z in v]
d = [math.log(primes[j + 1] / primes[j]) for j in range(len(primes) - 1)]
chi = [legendre(p, q) for p in primes]

# (1.1)
edge = sum(
    d[j] * (phi[j] * chi[j] + phi[j + 1] * chi[j + 1]) / 2
    for j in range(len(d))
)

# (1.2)--(1.3)
h = [0j] * len(primes)
h[0] = phi[0] * d[0] / 2
for j in range(1, len(primes) - 1):
    h[j] = phi[j] * (d[j - 1] + d[j]) / 2
h[-1] = phi[-1] * d[-1] / 2
collected = sum(hj * cj for hj, cj in zip(h, chi))
close(edge, collected)

# (1.4)
prefix = []
s = 0j
for cj in chi:
    s += cj
    prefix.append(s)
abel = h[-1] * prefix[-1] + sum(
    (h[j] - h[j + 1]) * prefix[j] for j in range(len(primes) - 1)
)
close(edge, abel)

# (1.6)--(1.7)
conditioned = 0j
for j, gap in enumerate(
    primes[k + 1] - primes[k] for k in range(len(primes) - 1)
):
    ratio = (1 + gap * pow(primes[j], -1, q)) % q
    close(chi[j + 1], chi[j] * legendre(ratio, q))
    conditioned += (
        d[j]
        * chi[j]
        * (phi[j] + phi[j + 1] * legendre(ratio, q))
        / 2
    )
close(edge, conditioned)

# Section 3 exponent arithmetic.
sigma = 1 - THETA - KAPPA
cgl_first = 2 * (THETA + KAPPA)
hybrid_bad = THETA + 2 * KAPPA
triangle_average = BETA / 2 + KAPPA
assert abs(sigma - 0.8225696766) < 1e-12
assert abs(cgl_first - 0.3548606468) < 1e-12
assert abs(hybrid_bad - 0.1954606468) < 1e-12
assert abs(triangle_average - 0.0948803234) < 1e-12
assert cgl_first > THETA
assert hybrid_bad > THETA

print("selected character-twist method audit: PASS")
print(f"sigma={sigma:.10f}")
print(f"CGL first-term exponent={cgl_first:.10f}")
print(f"hybrid bad-character exponent={hybrid_bad:.10f}")
print(f"triangle average saving at beta={triangle_average:.10f}")
