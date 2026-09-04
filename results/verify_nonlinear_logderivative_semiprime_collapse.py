#!/usr/bin/env python3
"""Replay exact algebra in the nonlinear log-derivative / semiprime audit."""

from fractions import Fraction


def factor(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mobius(n):
    f = factor(n)
    if any(e > 1 for e in f.values()):
        return 0
    return -1 if len(f) % 2 else 1


# A quadratic polynomial in formal variables x_p=log(p) is a dictionary
# {(min(p,q), max(p,q)): coefficient}.
def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return {m: c for m, c in out.items() if c}


def scale(poly, scalar):
    return {m: scalar * c for m, c in poly.items() if scalar * c}


def square_log(n):
    f = factor(n)
    out = {}
    for p, ep in f.items():
        for q, eq in f.items():
            key = (min(p, q), max(p, q))
            out[key] = out.get(key, Fraction(0)) + Fraction(ep * eq)
    return out


def von_mangoldt_form(n):
    f = factor(n)
    if len(f) != 1:
        return None
    return next(iter(f))  # formal value x_p


def lambda_log_form(n):
    p = von_mangoldt_form(n)
    if p is None:
        return {}
    out = {}
    for q, exponent in factor(n).items():
        key = (min(p, q), max(p, q))
        out[key] = out.get(key, Fraction(0)) + Fraction(exponent)
    return out


def lambda_convolution_form(n):
    out = {}
    for d in range(2, n + 1):
        if n % d:
            continue
        p = von_mangoldt_form(d)
        q = von_mangoldt_form(n // d)
        if p is not None and q is not None:
            key = (min(p, q), max(p, q))
            out[key] = out.get(key, Fraction(0)) + Fraction(1)
    return out


def zeta_quotient_form(n):
    out = {}
    for d in range(1, n + 1):
        if n % d == 0:
            out = add(out, scale(square_log(n // d), Fraction(mobius(d))))
    return out


def expected_q_form(n):
    f = factor(n)
    if len(f) == 1:
        p, a = next(iter(f.items()))
        return {(p, p): Fraction(2 * a - 1)}
    if len(f) == 2:
        p, q = sorted(f)
        return {(p, q): Fraction(2)}
    return {}


def verify_coefficients(limit=500):
    for n in range(2, limit + 1):
        q = zeta_quotient_form(n)
        linear = lambda_log_form(n)
        semiprime = lambda_convolution_form(n)
        assert q == add(linear, semiprime), (n, q, linear, semiprime)
        assert q == expected_q_form(n), (n, q, expected_q_form(n))


def verify_laurent_ledger():
    # Coefficients of z^{-1} after multiplying by
    # H=H0+H1*z+... .  Work over several exact rational packets.
    packets = [
        (1, Fraction(0), Fraction(7), Fraction(3)),
        (1, Fraction(5), Fraction(-2), Fraction(11, 3)),
        (2, Fraction(0), Fraction(4), Fraction(-5, 2)),
        (5, Fraction(3), Fraction(-7), Fraction(2, 9)),
    ]
    for m, h0, h1, a in packets:
        lhs = Fraction(m * m) * h1 + 2 * m * a * h0
        quotient = Fraction(m * (m - 1)) * h1 + 2 * m * a * h0
        integrated_linear = Fraction(m) * h1
        assert lhs == quotient + integrated_linear
        if m == 1 and h0 == 0:
            assert quotient == 0
            assert lhs == integrated_linear == h1


def verify_reflection_algebra():
    # Exact pointwise expansion behind equation (8):
    # H*L^2 - HR*(A-L)^2
    # = (H-HR)L^2 + 2*HR*A*L - HR*A^2.
    packets = [
        tuple(map(Fraction, (2, 3, 5, 7))),
        (Fraction(-4), Fraction(9, 2), Fraction(-3, 5), Fraction(8)),
    ]
    for h, hr, ell, arch in packets:
        direct = h * ell * ell - hr * (arch - ell) ** 2
        expanded = (h - hr) * ell * ell + 2 * hr * arch * ell - hr * arch * arch
        assert direct == expanded


def main():
    verify_coefficients()
    verify_laurent_ledger()
    verify_reflection_algebra()
    print("coefficient_identity=PASS n<=500 (formal prime-log polynomials)")
    print("laurent_split=PASS")
    print("functional_reflection_expansion=PASS")
    print("simple_target_collapse=PASS")


if __name__ == "__main__":
    main()
