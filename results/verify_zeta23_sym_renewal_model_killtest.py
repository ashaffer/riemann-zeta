#!/usr/bin/env python3
"""Exact checks for the symmetrized periodic-renewal model card.

This verifies identities inside a random model.  It makes no assertion about
the actual primes or a zero-free region.
"""

from __future__ import annotations

import cmath
import math


def exact_mode(q: int, p: float, r: int) -> complex:
    """Expected normalized symmetric mode for Bernoulli marks on U_q.

    q is prime and 0 < r < q.  The finite expression is obtained by writing
    k = a(q-1)+h and summing the geometric a-series exactly.
    """
    m = q - 1
    z = 1.0 - p
    omega = cmath.exp(2j * math.pi * r / q)
    den = 1.0 - z**m

    # h=0, a>=1.
    total = -2.0 * q * z ** (m - 1) / den**2
    partial = 0j
    for h in range(1, m):
        partial += omega**h
        boundary_dft = 2.0 * partial.real
        total += z ** (h - 1) * (
            -2.0 * q * z**m / den**2
            - 2.0 * h / den
            + boundary_dft / den
        )
    return p * p * total / (2.0 * q)


def brute_mode(q: int, p: float, r: int, terms: int) -> complex:
    """Directly sum the defining infinite renewal series up to ``terms``."""
    m = q - 1
    z = 1.0 - p
    omega = cmath.exp(2j * math.pi * r / q)
    total = 0j
    for i in range(1, m + 1):
        phase = omega**i
        inner = 0.0
        for k in range(1, terms + 1):
            a, h = divmod(k, m)
            if h == 0:
                d_plus = d_minus = a * q
            else:
                d_plus = a * q + h + (i > m - h)
                d_minus = a * q + h + (i <= h)
            inner += z ** (k - 1) * (d_plus + d_minus)
        total += phase * inner
    return p * p * total / (2.0 * q)


def no_wrap_asymptotic(q: int, p: float, r: int) -> complex:
    z = 1.0 - p
    omega = cmath.exp(2j * math.pi * r / q)
    return -1.0 / q + (p / q) * (omega / (1.0 - z * omega)).real


def resolvent_mode(q: int, p: float, r: int) -> complex:
    """Closed stationary resolvent obtained from the residue cell masses."""
    z = 1.0 - p
    omega = cmath.exp(2j * math.pi * r / q)
    zm = z ** (q - 1)
    return -1.0 / q + (p / (q * (1 - zm))) * (
        (omega - zm) / (1 - z * omega)
    ).real


def stationary_residue_masses(q: int, p: float) -> list[float]:
    """Expected normalized Voronoi mass in each nonzero residue."""
    m = q - 1
    z = 1.0 - p
    den = 1 - z**m
    return [
        1 / q + p * (z ** (m - i) + z ** (i - 1)) / (2 * q * den)
        for i in range(1, m + 1)
    ]


def sharp_remainder_bound(q: int, p: float) -> float:
    """Uniform bound for resolvent_mode - no_wrap_asymptotic."""
    z = 1.0 - p
    return p * (1 + z) * z ** (q - 2) / (2 * q * (1 - z ** (q - 1)))


def exact_wheel_mode(P: int, q: int, p: float, r: int) -> complex:
    """Exact period sum after adjoining q to an auxiliary wheel P."""
    Q = P * q
    units = [n for n in range(1, Q + 1) if math.gcd(n, Q) == 1]
    m = len(units)
    z = 1 - p
    omega = cmath.exp(2j * math.pi * r / q)
    phases = [omega ** (n % q) for n in units]
    phase_sum = sum(phases)
    den = 1 - z**m

    # k=a*m, a>=1.
    total = 2 * Q * phase_sum * z ** (m - 1) / den**2
    for h in range(1, m):
        finite_dft = 0j
        for i, n in enumerate(units):
            j_plus = i + h
            d_plus = units[j_plus % m] + (Q if j_plus >= m else 0) - n
            j_minus = i - h
            d_minus = n - (units[j_minus % m] - (Q if j_minus < 0 else 0))
            finite_dft += phases[i] * (d_plus + d_minus)
        total += z ** (h - 1) * (
            2 * Q * phase_sum * z**m / den**2 + finite_dft / den
        )
    return p * p * total / (2 * Q)


def brute_wheel_mode(P: int, q: int, p: float, r: int, terms: int) -> complex:
    """Direct defining renewal series on a general Pq candidate wheel."""
    Q = P * q
    units = [n for n in range(1, Q + 1) if math.gcd(n, Q) == 1]
    m = len(units)
    z = 1 - p
    omega = cmath.exp(2j * math.pi * r / q)
    total = 0j
    for i, n in enumerate(units):
        inner = 0.0
        for k in range(1, terms + 1):
            plus_index = i + k
            plus_cycle, plus_residue = divmod(plus_index, m)
            plus_node = units[plus_residue] + plus_cycle * Q
            minus_index = i - k
            minus_cycle, minus_residue = divmod(minus_index, m)
            minus_node = units[minus_residue] + minus_cycle * Q
            inner += z ** (k - 1) * (plus_node - minus_node)
        total += omega ** (n % q) * inner
    return p * p * total / (2 * Q)


def main() -> None:
    # The period decomposition agrees with the defining renewal sum.
    for q, p, r in [(5, 0.17, 1), (7, 0.11, 2), (11, 0.08, 3)]:
        direct = brute_mode(q, p, r, terms=800)
        closed = exact_mode(q, p, r)
        assert abs(direct - closed) < 2e-12, (q, p, r, direct, closed)

        # The independently derived stationary cell masses normalize to one
        # and have exactly the same nonzero DFT.
        masses = stationary_residue_masses(q, p)
        assert abs(sum(masses) - 1) < 2e-14
        omega = cmath.exp(2j * math.pi * r / q)
        mass_dft = sum(mass * omega**i for i, mass in enumerate(masses, 1))
        assert abs(mass_dft - closed) < 2e-13
        assert abs(resolvent_mode(q, p, r) - closed) < 2e-13

    # The sharp resolvent remainder is uniform in the numerator.  Unlike a
    # coefficient-blind absolute tail estimate, it remains useful even when
    # p*q tends to infinity very slowly.
    for q, p, r in [(101, 0.10, 1), (101, 0.10, 37), (211, 0.06, 1)]:
        err = abs(exact_mode(q, p, r) - no_wrap_asymptotic(q, p, r))
        assert err <= sharp_remainder_bound(q, p) * (1.0 + 1e-11), (
            q,
            p,
            r,
            err,
        )

    slow_q = 5003
    slow_p = math.log(math.log(slow_q)) / slow_q
    slow_err = abs(
        exact_mode(slow_q, slow_p, 1)
        - no_wrap_asymptotic(slow_q, slow_p, 1)
    )
    assert slow_p * slow_q > 2
    assert slow_err <= sharp_remainder_bound(slow_q, slow_p) * (1 + 1e-9)
    assert slow_q * sharp_remainder_bound(slow_q, slow_p) < 1e-3

    # Fixed-q symmetrization removes the O(p) nonprincipal term: the
    # remainder after the principal Ramanujan mass is O_q(p^2).
    q = 5
    vals = []
    for p in (0.004, 0.002, 0.001):
        nonprincipal = exact_mode(q, p, 1).real + 1.0 / (q - 1)
        vals.append(nonprincipal / p**2)
    assert max(vals) - min(vals) < 7e-4, vals

    # In the target joint limit, the uniform nonprincipal systematic bound
    # has exponent b, comfortably larger than kappa.
    beta = 1537 / 10000
    theta = 797 / 5000
    kappa = 0.0180303234
    assert beta > kappa
    assert theta > beta

    # The multiplier in the leading nonprincipal term is at most one:
    # p/|1-(1-p)e(theta)| <= 1.
    for q in (101, 211, 401):
        p = 0.07
        z = 1 - p
        for r in range(1, q):
            omega = cmath.exp(2j * math.pi * r / q)
            assert p / abs(1 - z * omega) <= 1 + 2e-14

    # Independently compare the general-wheel period resolvent with the
    # defining infinite renewal series, and audit total-mass normalization.
    for P, q, p, r in [(2, 5, 0.17, 1), (6, 5, 0.13, 2), (30, 7, 0.11, 2)]:
        direct = brute_wheel_mode(P, q, p, r, terms=800)
        closed = exact_wheel_mode(P, q, p, r)
        assert abs(direct - closed) < 3e-11, (P, q, p, r, direct, closed)
        assert abs(exact_wheel_mode(P, q, p, 0) - 1) < 3e-12

    # A P-periodic mass profile has exactly zero nonzero q-mode over Pq.
    P, q, r = 6, 31, 7
    omega = cmath.exp(2j * math.pi * r / q)
    profile = {1: 0.7, 5: 1.3}
    base_mode = sum(
        profile[n % P] * omega ** (n % q)
        for n in range(1, P * q + 1)
        if math.gcd(n, P) == 1
    )
    assert abs(base_mode) < 2e-12

    # Exact finite auxiliary wheels show the same q-power crossover.  These
    # are identity checks/diagnostics, not numerical evidence about primes.
    for P in (2, 6, 30):
        values = []
        for q in (31, 61, 101):
            if math.gcd(P, q) != 1:
                continue
            nonprincipal = exact_wheel_mode(P, q, 0.1, 1).real + 1 / (q - 1)
            values.append(q * abs(nonprincipal))
        assert max(values) < 0.5, (P, values)

    print("sym-renewal model identity: PASS")
    print("stationary normalization and exact resolvent: PASS")
    print("uniform slow-pq resolvent remainder: PASS")
    print("fixed-q first nonprincipal order: p^2 (PASS)")
    print(f"joint-limit systematic saving: q^-1, exponent >= {beta:.4f}")
    print(f"margin over kappa: {beta-kappa:.10f}")
    print("fixed auxiliary-wheel coupling/resolvent: PASS")
    print("scope: exact random-model calculation; no actual-prime claim")


if __name__ == "__main__":
    main()
