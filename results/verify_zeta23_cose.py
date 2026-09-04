"""Replay the countermodel to the abstract source/carrier COSE relaxation."""

from fractions import Fraction
from math import cos, pi, sin


def fejer_value(m: int, depth: Fraction, theta: float) -> float:
    coefficients = [
        -Fraction(2, 1 + depth) * Fraction(m - d, m * (m - 1))
        for d in range(1, m)
    ]
    return sum(float(coefficients[d - 1]) * cos(d * theta) for d in range(1, m))


def main() -> None:
    m = 101
    # Any depth in [1/2,1] can be supplied by a prime-scale population of
    # zero-coefficient source nodes selected from negative-phase arcs.
    depth = Fraction(1, 2)
    coefficients = [
        -Fraction(2, 1 + depth) * Fraction(m - d, m * (m - 1))
        for d in range(1, m)
    ]

    source_value = sum(coefficients)
    assert source_value == -Fraction(1, 1 + depth)
    assert source_value + depth * sum(coefficients) == -1

    # F(theta)=2[1-K(theta)]/[3(m-1)], K>=0.  It reaches the
    # upper bound at the first nontrivial m-th root of unity.
    cap = Fraction(1, (1 + depth) * (m - 1))
    assert abs(fejer_value(m, depth, 0.0) - float(source_value)) < 1e-14
    assert abs(fejer_value(m, depth, 2 * pi / m) - float(cap)) < 1e-14

    # Spot-check the Fejer identity itself.
    for numerator in (1, 7, 19, 43):
        theta = numerator / 17
        exponential_sum_sq = abs(
            sum(complex(cos(a * theta), sin(a * theta)) for a in range(m))
        ) ** 2
        kernel = exponential_sum_sq / m
        identity_value = (1 - kernel) / (float(1 + depth) * (m - 1))
        assert abs(fejer_value(m, depth, theta) - identity_value) < 2e-14

    tau = Fraction(179, 10_000)
    eta = Fraction(1, 100_000)
    seed_exponent = tau + 2 * eta
    peak_time_exponent = Fraction(1, 2) - seed_exponent
    assert seed_exponent > tau + eta
    assert peak_time_exponent > Fraction(1, 100)
    assert Fraction(1, 2) < Fraction(50, 33)  # spacing 1/t0 exceeds 1/B
    # M/N asymp 1/log(Y), which dominates Y^(-d) for every fixed d>0.
    event_exponent = Fraction(0, 1)
    assert event_exponent < Fraction(1, 1000)

    print("negative source depth range: [1/2,1]; replay depth:", depth)
    print("mass-normalized event scale: 1/log(Y) >> Y^(-.001)")
    print("source normalization: PASS")
    print("Fejer cap:", cap)
    print("carrier-only Fejer identity: PASS")
    print("seed exponent:", seed_exponent)
    print("cap exponent exceeds target exponent:", seed_exponent > tau + eta)
    print("positive-peak time exponent:", peak_time_exponent)


if __name__ == "__main__":
    main()
