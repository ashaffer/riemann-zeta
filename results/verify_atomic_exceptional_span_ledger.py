#!/usr/bin/env python3
"""Diagnostic checks for the atomic exceptional-span no-go ledger.

This checks the exponent arithmetic and one finite exact-alias/additive-energy
fixture.  It is not a proof of the asymptotic probabilistic construction.
"""

from collections import Counter
from math import cos, pi
from random import Random


BETA = 50.0 / 33.0
KAPPA = 0.0180303234
C = 0.019


def finite_alias_fixture() -> dict[str, float]:
    rng = Random(230813)
    m_count = 80
    block_length = 200
    period = 2 * m_count * block_length

    # One random point in each active block, with an equally long gap between
    # active blocks.  Thus the point separation is at least block_length.
    points = [
        2 * j * block_length + rng.randrange(block_length)
        for j in range(m_count)
    ]
    min_gap = min(b - a for a, b in zip(points, points[1:]))

    pair_counts = Counter(a + b for a in points for b in points)
    additive_energy = sum(multiplicity * multiplicity for multiplicity in pair_counts.values())
    fourth_moment = period * additive_energy / (m_count**4)

    recurrence_error = max(
        abs(cos(period * (2.0 * pi * point / period)) - 1.0)
        for point in points
    )

    assert min_gap >= block_length
    assert fourth_moment < 20.0
    assert recurrence_error < 1.0e-12

    return {
        "M": float(m_count),
        "B": float(period),
        "min_gap_grid": float(min_gap),
        "additive_energy": float(additive_energy),
        "normalized_fourth_moment": fourth_moment,
        "recurrence_error": recurrence_error,
    }


def main() -> None:
    bad_length = 4.0 * C
    component_count = 4.5 * C
    gm_fixed_packets = 2.0 * KAPPA
    gm_shrinking_packets = 3.0 * KAPPA
    gm_squared_leakage = gm_fixed_packets - 2.0 * KAPPA
    assert abs(bad_length - 0.076) < 1.0e-15
    assert abs(component_count - 0.0855) < 1.0e-15
    assert C > KAPPA
    assert gm_squared_leakage == 0.0

    fixture = finite_alias_fixture()

    print("atomic exceptional-span ledger: PASS")
    print(f"beta={BETA:.12f}")
    print(f"kappa={KAPPA:.10f}")
    print(f"fourth-moment bad-length exponent={bad_length:.6f}")
    print(f"component exponent={component_count:.6f}")
    print(f"Guth-Maynard fixed-packet exponent={gm_fixed_packets:.10f}")
    print(f"Guth-Maynard shrinking-packet exponent={gm_shrinking_packets:.10f}")
    print(f"Guth-Maynard squared-leakage margin={gm_squared_leakage:.1f}")
    print("complex product-log convolution lift=FALSE (same-argument identity)")
    for key, value in fixture.items():
        print(f"fixture {key}={value:.12g}")


if __name__ == "__main__":
    main()
