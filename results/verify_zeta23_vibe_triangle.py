"""Replay exact algebra and the finite fixture for the PQR triangle audit."""

from fractions import Fraction

import sympy as sp


def main() -> None:
    x, y = sp.symbols("x y")
    identity = sp.simplify(
        sp.exp(x) + sp.exp(y) - sp.exp(x + y) - 1
        + (sp.exp(x) - 1) * (sp.exp(y) - 1)
    )
    assert identity == 0

    tau = Fraction(179, 10_000)
    assert Fraction(1, 2) + tau == Fraction(5179, 10_000)
    assert 2 * Fraction(8, 33) - 1 == -Fraction(17, 33)
    assert 2 * Fraction(8, 33) == Fraction(16, 33)

    # Section 5's one-cut sanity check.  Rational arithmetic constructs the
    # affine entries exactly; high-precision SymPy arithmetic checks transport.
    center = sp.Rational(20_000_012_837, 2)
    seed = (1, 5, 16, 24)
    low = (0, 1)
    high = (2, 3)
    lam = sp.Rational(15, 2)
    omega = lam / center
    matrix = sp.Matrix(
        [
            [center + lam * (seed[i] - seed[j]) for j in low]
            for i in high
        ]
    )
    expected = sp.Matrix(
        [
            [10_000_006_531, 10_000_006_501],
            [10_000_006_591, 10_000_006_561],
        ]
    )
    assert matrix == expected
    assert all(sp.isprime(int(value)) for value in matrix)
    assert matrix.det() == 1800

    tolerance = sp.N(center ** (-sp.Rational(17, 33)), 60)
    errors = []
    for i in high:
        for j in low:
            reference = center * sp.exp(omega * (seed[i] - seed[j]))
            affine = center + lam * (seed[i] - seed[j])
            error = sp.N(reference - affine, 60)
            assert 0 < error < tolerance
            errors.append(error)

    print("triangle exponential identity: PASS")
    print("target span exponent:", tau + Fraction(1, 2))
    print("affine Taylor-error exponent:", 2 * Fraction(8, 33) - 1)
    print("affine minor-height exponent:", 2 * Fraction(8, 33))
    print("prime fixture determinant:", matrix.det())
    print("prime fixture max transport error:", max(errors))
    print("transport tolerance:", tolerance)


if __name__ == "__main__":
    main()
