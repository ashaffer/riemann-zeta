#!/usr/bin/env python3
"""Replay the FGF4 sparse Fourier/Galois classification theorem."""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fgf4_sparse_fourier_classification import (  # noqa: E402
    degree_sensitive_energy_floor,
    energy_rigidity,
    exhaustive_support_maximum,
    fourier_energy,
    galois_energy_orbit,
    local_sparse_model,
    phase_arc_stability,
    selected_progression_discrepancy,
    sharp_support_extremum,
)


DELTA_REQUIRED = Fraction(1974048259, 100000000000) / Fraction(1537, 10000)


def main() -> None:
    for q in (7, 11):
        for size in range(1, q):
            maximum, maximizers = exhaustive_support_maximum(q, size, 3)
            assert abs(maximum - sharp_support_extremum(q, size)) < 1e-9
            assert maximizers == q

    paley = (1, 2, 4)
    paley_rigidity = energy_rigidity(paley, 7)
    paley_orbit = galois_energy_orbit(paley, 7)
    assert paley_rigidity.is_difference_set
    assert paley_rigidity.excess == 0
    assert paley_orbit.degree == 1
    assert abs(paley_orbit.selected_energy - float(paley_orbit.mu_fourier)) < 1e-9

    generic = (0, 1, 4)
    rigidity = energy_rigidity(generic, 11)
    orbit = galois_energy_orbit(generic, 11, 3)
    assert orbit.cardinality_gcd == 2
    assert orbit.stabilizer == (1, 10)
    assert orbit.degree == 5
    assert orbit.trace == 12
    assert orbit.stabilizer_size * orbit.trace == len(generic) * (11 - len(generic))
    assert orbit.stabilizer_size == (11 - 1) // orbit.degree
    assert orbit.stabilizer_size == 2
    assert orbit.selected_energy < float(orbit.trace_bound) + 1e-9
    assert float(rigidity.centered_energy) + 1e-9 >= degree_sensitive_energy_floor(
        rigidity, orbit
    )

    race = selected_progression_discrepancy(generic, 11, 3)
    assert race.selected_modulus <= 4 * float(race.discrepancy) + 1e-9
    assert pow((11 + 1) // 4, -1, 11) == 4

    stability = phase_arc_stability((0, 1, 2), 101, 1, 0.2)
    assert stability.outliers == 0

    energies = [fourier_energy(generic, 11, frequency) for frequency in range(1, 11)]
    for left in range(1, 11):
        for right in range(1, 11):
            equal = abs(energies[left - 1] - energies[right - 1]) < 1e-8
            assert equal == (right in (left, (-left) % 11))

    model = local_sparse_model(10007, 101)
    assert abs(abs(model.selected_sum) - model.geometric_modulus) < 1e-8
    assert model.geometric_modulus > 0.99 * model.size
    assert all(math.gcd(value * (value + 4), 6) == 1 for value in model.values)

    endpoint_degree_exponent = 1 - 2 * DELTA_REQUIRED
    assert Fraction(7431, 10000) < endpoint_degree_exponent < Fraction(7432, 10000)

    print("FGF4 sparse Fourier/Galois classification: PASS")
    print(
        "sharp-support",
        {"q": 11, "N": 3, "maximum": sharp_support_extremum(11, 3), "maximizers": 11},
    )
    print(
        "generic-degree",
        {
            "q": orbit.q,
            "N": orbit.size,
            "stabilizer": orbit.stabilizer,
            "degree": orbit.degree,
            "trace": orbit.trace,
            "selected_energy": orbit.selected_energy,
        },
    )
    print(
        "energy-rigidity",
        {
            "centered": float(rigidity.centered_energy),
            "continuous_floor": float(rigidity.continuous_floor),
            "integer_floor": float(rigidity.integer_floor),
            "quantized_gap": rigidity.quantized_gap,
        },
    )
    print(
        "local-model",
        {"q": model.q, "N": model.size, "ratio": model.geometric_modulus / model.size},
    )
    print(
        "selected-race",
        {
            "selected": race.selected_modulus,
            "discrepancy": float(race.discrepancy),
            "step": 4,
        },
    )
    print(f"bad-coefficient degree exponent={float(endpoint_degree_exponent):.12f}")


if __name__ == "__main__":
    main()
