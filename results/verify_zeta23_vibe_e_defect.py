"""Replay the exact algebra behind the PQR ``E``-defect addendum."""

from fractions import Fraction
from math import gcd
from random import Random

import sympy as sp


def defect(q: sp.Expr, p_ac: sp.Expr, p_ab: sp.Expr, p_bc: sp.Expr) -> sp.Expr:
    """E_(a,b,c) in terms of its three edge labels."""
    return 2 * (q * p_ac - 2 * p_ab * p_bc)


def main() -> None:
    q, p_ki, p_kj, p_ji = sp.symbols("q p_ki p_kj p_ji")
    d_ki = 2 * p_ki - q
    d_kj = 2 * p_kj - q
    d_ji = 2 * p_ji - q
    curvature = d_ki - d_kj - d_ji
    e_from_curvature = sp.expand(q * curvature - d_kj * d_ji)
    e_from_primes = defect(q, p_ki, p_kj, p_ji)
    assert sp.expand(e_from_curvature - e_from_primes) == 0

    # The four-vertex associator is a polynomial identity, independent of
    # approximation or primality.
    p_li, p_lk, p_lj = sp.symbols("p_li p_lk p_lj")
    e_lki = defect(q, p_li, p_lk, p_ki)
    e_kji = defect(q, p_ki, p_kj, p_ji)
    e_lji = defect(q, p_li, p_lj, p_ji)
    e_lkj = defect(q, p_lj, p_lk, p_kj)
    associator = sp.expand(q * e_lki + 2 * p_lk * e_kji - q * e_lji - 2 * p_ji * e_lkj)
    assert associator == 0

    # For a fixed middle, every 2-by-2 defect minor is a multiple of q.
    p_lj, p_jh, p_kh, p_lh = sp.symbols("p_lj p_jh p_kh p_lh")
    e_ki = defect(q, p_ki, p_kj, p_ji)
    e_kh = defect(q, p_kh, p_kj, p_jh)
    e_li = defect(q, p_li, p_lj, p_ji)
    e_lh = defect(q, p_lh, p_lj, p_jh)
    minor = sp.expand(e_ki * e_lh - e_kh * e_li)
    assert sp.expand(minor.subs(q, 0)) == 0
    assert sp.rem(minor, q, domain=sp.ZZ[
        p_ki, p_kj, p_ji, p_lj, p_jh, p_kh, p_li, p_lh
    ]) == 0

    # Rank-one defect plus the associator has a large formal countermodel:
    # normalized two-dimensional bilinear kernels.
    uk0, uk1, uj0, uj1 = sp.symbols("uk0 uk1 uj0 uj1")
    vi0, vi1, vj0, vj1 = sp.symbols("vi0 vi1 vj0 vj1")
    s_ki = uk0 * vi0 + uk1 * vi1
    s_kj = uk0 * vj0 + uk1 * vj1
    s_ji = uj0 * vi0 + uj1 * vi1
    normalization = uj0 * vj0 + uj1 * vj1
    determinant_product = (uk0 * uj1 - uk1 * uj0) * (vi0 * vj1 - vi1 * vj0)
    kernel_defect = sp.expand(s_ki * normalization - s_kj * s_ji)
    assert sp.expand(kernel_defect - determinant_product) == 0

    # Replay the global completion theorem on a nondegenerate exact family.
    n = 6

    def s_value(k: int, i: int) -> sp.Integer:
        assert k >= i
        return sp.Integer(1 + (k - i) * (i + 1))

    for j in range(2, n):
        defect_slice = sp.Matrix(
            [
                [
                    s_value(k, i) - s_value(k, j) * s_value(j, i)
                    for i in range(1, j)
                ]
                for k in range(j + 1, n + 1)
            ]
        )
        assert defect_slice.rank() <= 1

    terminal_anchor = sp.Matrix(
        [
            [s_value(n - 1, 1), s_value(n - 1, 2)],
            [s_value(n, 1), s_value(n, 2)],
        ]
    )
    assert terminal_anchor.det() != 0
    u = {1: sp.Matrix([[1, 0]])}
    u.update(
        {k: sp.Matrix([[s_value(k, 1), s_value(k, 2)]]) for k in range(2, n + 1)}
    )
    v = {1: sp.Matrix([1, 0]), 2: sp.Matrix([0, 1])}
    for i in range(3, n):
        rhs = sp.Matrix([s_value(n - 1, i), s_value(n, i)])
        v[i] = terminal_anchor.inv() * rhs
    v[n] = sp.Matrix([1 / u[n][0, 0], 0])
    for k in range(1, n + 1):
        for i in range(1, k + 1):
            assert (u[k] * v[i])[0, 0] == s_value(k, i)

    h_exponent = Fraction(16, 33)
    assert 2 * h_exponent == Fraction(32, 33) < 1

    # Random odd-label replay checks parity and modular minor divisibility.
    rng = Random(20260830)
    for _ in range(100):
        q0 = rng.randrange(101, 1000, 2)
        labels = [rng.randrange(3, 1000, 2) for _ in range(8)]
        values = {
            symbol: value
            for symbol, value in zip(
                (p_ki, p_kj, p_ji, p_lj, p_jh, p_kh, p_li, p_lh), labels
            )
        }
        e0 = int(e_from_primes.subs(values | {q: q0}))
        minor0 = int(minor.subs(values | {q: q0}))
        assert e0 % 4 == 2
        assert minor0 % q0 == 0

    # Exact local hostile fixture: all one-pivot invariants survive with
    # composites, so primality and cross-pivot compatibility are essential.
    a, b = 1_000_001, 1_001_005
    q0 = a * b + 2
    rows = (249, 143)
    cols = (249, 143)
    p_row = [(q0 + a * row) // 2 for row in rows]
    p_col = [(q0 + b * col) // 2 for col in cols]
    p_cross = [
        [(q0 + a * row + b * col + row * col) // 2 for col in cols]
        for row in rows
    ]
    labels = p_row + p_col + [value for row in p_cross for value in row]
    assert len(set(labels)) == 8
    assert all(value > q0 / 2 and not sp.isprime(value) for value in labels)
    e_matrix = sp.Matrix(
        [
            [
                2 * (q0 * p_cross[row_index][col_index]
                     - 2 * p_row[row_index] * p_col[col_index])
                for col_index in range(2)
            ]
            for row_index in range(2)
        ]
    )
    assert e_matrix == sp.Matrix(
        [[2 * row * col for col in cols] for row in rows]
    )
    assert e_matrix.rank() == 1
    assert all(gcd(int(value), q0) == 1 for value in e_matrix)
    center = sp.Rational(q0, 2)
    height = sp.N(center ** sp.Rational(16, 33), 30)
    transport_tolerance = sp.N(center ** -sp.Rational(17, 33), 30)
    max_error = sp.Rational(max(rows) * max(cols), q0)
    assert max(abs(int(value)) for value in e_matrix) < height
    assert max_error < transport_tolerance

    print("E-defect expansion: PASS")
    print("four-vertex associator: PASS")
    print("fixed-middle minor divisibility: PASS")
    print("rank-one projective countermodel identity: PASS")
    print("global rank-two completion replay: PASS")
    print("minor-height exponent:", 2 * h_exponent, "< 1")
    print("local composite hostile fixture: PASS")


if __name__ == "__main__":
    main()
