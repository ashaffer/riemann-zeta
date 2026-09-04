#!/usr/bin/env python3
"""Finite checks for the FGF4 character/circle/parity audit."""

from __future__ import annotations

import cmath
import math
from fractions import Fraction


TAU = 2.0 * math.pi
TOL = 2.0e-9


def e(x: float) -> complex:
    return cmath.exp(1j * TAU * x)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def chi4(n: int) -> int:
    if n % 2 == 0:
        return 0
    return 1 if n % 4 == 1 else -1


def primitive_root_prime(q: int) -> int:
    factors = []
    x = q - 1
    p = 2
    while p * p <= x:
        if x % p == 0:
            factors.append(p)
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        factors.append(x)
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in factors):
            return g
    raise AssertionError("no primitive root")


def main() -> None:
    kappa = Fraction(19740482582942, 10**15)
    b_min = Fraction(1537, 10_000)
    delta = kappa / b_min
    assert float(delta) > 0.1284
    assert Fraction(1, 4) - delta > 0

    # chi_4 is exactly the quarter-frequency phase.
    for q in (7, 11, 19, 43):
        a = (q + 1) // 4
        for n in range(101, 180, 2):
            lhs = chi4(n) * e(n / (4.0 * q))
            rhs = -1j * e(a * n / q)
            assert abs(lhs - rhs) < TOL

    # A concrete cousin-pair block.
    lo, hi, q = 101, 260, 19
    a = (q + 1) // 4
    alpha = a / q
    lowers = [n for n in range(lo, hi + 1) if is_prime(n) and is_prime(n + 4)]
    direct = sum((e(alpha * n) for n in lowers), 0j)

    # Exact circle identity via a roots-of-unity quadrature.
    grid = 1024
    circle = 0j
    primes_i = [n for n in range(lo, hi + 1) if is_prime(n)]
    primes_j = [m for m in range(lo + 4, hi + 5) if is_prime(m)]
    for k in range(grid):
        theta = k / grid
        f = sum((e(n * (theta + alpha)) for n in primes_i), 0j)
        g = sum((e(m * theta) for m in primes_j), 0j)
        circle += f * g.conjugate() * e(4 * theta)
    circle /= grid
    assert abs(circle - direct) < 1.0e-7

    # Prime-modulus character expansion and both energy identities.
    g0 = primitive_root_prime(q)
    log_index = {}
    x = 1
    for j in range(q - 1):
        log_index[x] = j
        x = (x * g0) % q

    chars = []
    taus = []
    twists = []
    for j in range(q - 1):
        def char(r: int, j: int = j) -> complex:
            if r % q == 0:
                return 0j
            return e(j * log_index[r % q] / (q - 1))

        chars.append(char)
        taus.append(sum((char(r).conjugate() * e(r / q) for r in range(1, q)), 0j))
        twists.append(sum((char(n) for n in lowers), 0j))

    expanded = sum(
        (chars[j](a) * taus[j] * twists[j] for j in range(q - 1)), 0j
    ) / (q - 1)
    assert abs(expanded - direct) < 1.0e-7
    assert abs(sum(abs(t) ** 2 for t in taus) - (q - 1) ** 2) < 1.0e-7

    residue_counts = [0] * q
    for n in lowers:
        residue_counts[n % q] += 1
    char_energy = sum(abs(t) ** 2 for t in twists)
    residue_energy = (q - 1) * sum(residue_counts[r] ** 2 for r in range(1, q))
    assert abs(char_energy - residue_energy) < 1.0e-7

    # The local admissible-residue Fourier main is O(1), not O(q).
    local = sum((e(a * r / q) for r in range(q) if r not in (0, q - 4)), 0j)
    expected_local = -1 - e(-1 / q)
    assert abs(local - expected_local) < 1.0e-8

    # Exact unit-coefficient translated-autocorrelation saturation.
    length = 180
    coeff = [0j] * (length + 5)
    for r in range(4):
        coeff[r] = 1 + 0j
        n = r
        while n + 4 < len(coeff):
            coeff[n + 4] = coeff[n] * e(alpha * n)
            n += 4
    saturated = sum(
        coeff[n] * coeff[n + 4].conjugate() * e(alpha * n)
        for n in range(length)
    )
    assert abs(saturated - length) < 1.0e-7
    assert all(abs(abs(z) - 1.0) < TOL for z in coeff)

    # Positive order does not pass through a signed/complex functional.
    x_vec = (1.0, 0.0)
    w_vec = (1.0, 1.0)
    u_vec = (1.0, -1.0)
    lhs = abs(sum(u * x for u, x in zip(u_vec, x_vec)))
    rhs = abs(sum(u * w for u, w in zip(u_vec, w_vec)))
    assert lhs == 1.0 and rhs == 0.0

    # Rational separation lemma on a representative legal triple.
    q_sep, r_max = 43, 6
    assert q_sep > r_max * r_max
    min_distance = 1.0
    a_sep = (q_sep + 1) // 4
    for s in range(1, r_max + 1):
        for numer in range(s + 1):
            if math.gcd(numer, s) == 1:
                distance = abs(a_sep / q_sep - numer / s)
                min_distance = min(min_distance, distance)
    assert min_distance >= 1 / (q_sep * r_max * r_max) - TOL

    print("PASS: FGF4 character/circle/parity identities")
    print(f"delta_required={float(delta):.12f}")
    print(f"circle_error={abs(circle-direct):.3e}")
    print(f"character_error={abs(expanded-direct):.3e}")
    print(f"cousin_pairs={len(lowers)}")


if __name__ == "__main__":
    main()
