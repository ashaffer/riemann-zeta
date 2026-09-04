"""Replay exact algebra and exponent ledgers for the PWCT audit."""

from fractions import Fraction
from math import cos, pi, sin


def fejer_kernel(order: int, theta: float) -> float:
    total = sum(complex(cos(j * theta), sin(j * theta)) for j in range(order))
    return abs(total) ** 2 / order


def positive_fejer_value(order: int, depth: Fraction, theta: float) -> float:
    weights = [
        Fraction(2, 1 + depth) * Fraction(order - d, order * (order - 1))
        for d in range(1, order)
    ]
    return sum(float(weights[d - 1]) * cos(d * theta) for d in range(1, order))


def main() -> None:
    order = 101
    depth = Fraction(1, 2)
    mass = Fraction(1, 1 + depth)
    floor = Fraction(1, (1 + depth) * (order - 1))

    assert abs(positive_fejer_value(order, depth, 0.0) - float(mass)) < 1e-14
    assert abs(positive_fejer_value(order, depth, 2 * pi / order) + float(floor)) < 1e-14
    assert mass + depth * mass == 1
    for numerator in (1, 7, 19, 43):
        theta = numerator / 17
        expected = (fejer_kernel(order, theta) - 1) / (
            float(1 + depth) * (order - 1)
        )
        assert abs(positive_fejer_value(order, depth, theta) - expected) < 2e-14

    tau = Fraction(179, 10_000)
    eta = Fraction(1, 200_000)
    directional = Fraction(1, 1_000)
    dpa = Fraction(19, 1_000)
    pair_count = Fraction(16, 33)
    pair_mass_error = pair_count - 1
    carrier_source_error = pair_count - Fraction(50, 33)
    random_antenna = Fraction(1, 2)
    random_projective = random_antenna - directional

    assert pair_mass_error == -Fraction(17, 33)
    assert pair_mass_error < -directional
    assert carrier_source_error == -Fraction(34, 33)
    assert random_projective == Fraction(499, 1_000)
    assert random_projective > tau + eta
    assert dpa - directional == Fraction(18, 1_000)
    assert dpa - directional > tau + eta
    assert tau + 2 * eta > tau + eta

    # Exact projective normalization for a representative probability
    # antenna with Phi(t0)=x and floor a.
    x = Fraction(1, 10)
    antenna_floor = Fraction(1, 100)
    denominator = depth + x
    scale = 1 / denominator
    assert scale * denominator == 1
    assert scale * antenna_floor == antenna_floor / denominator

    print("unpaired deletion exponent:", pair_mass_error, "<", -directional)
    print("diffuse carrier source-time error:", carrier_source_error)
    print("smooth pseudo-prime projective exponent:", random_projective)
    print("positive Fejer source normalization: PASS")
    print("positive Fejer floor:", floor)
    print("projective probability normalization: PASS")
    print("PDPA/PWCT reserve:", dpa - directional - tau)


if __name__ == "__main__":
    main()
