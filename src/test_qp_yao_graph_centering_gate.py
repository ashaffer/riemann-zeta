from fractions import Fraction

from qp_yao_graph_centering_gate import (
    graph_centering_exponent_ledger,
    graph_phase_points,
    interval_additive_energy,
    unweighted_modular_additive_energy,
)


def test_interval_energy_formula() -> None:
    for size in range(1, 40):
        direct = sum(
            1
            for a in range(1, size + 1)
            for b in range(1, size + 1)
            for c in range(1, size + 1)
            for d in range(1, size + 1)
            if a - b == c - d
        )
        assert direct == interval_additive_energy(size)


def test_parabolic_matching_has_interval_carrier_energy() -> None:
    prime = 1009
    size = 20
    denominators = tuple(range(1, size + 1))
    numerators = tuple(value * value for value in denominators)
    assert len(set(numerators)) == size
    phases = graph_phase_points(prime, denominators, numerators)
    assert phases == denominators
    assert unweighted_modular_additive_energy(prime, phases) == (
        interval_additive_energy(size)
    )


def test_exact_power_losses() -> None:
    ledger = graph_centering_exponent_ledger()
    assert ledger.target_energy == Fraction(5, 2)
    assert ledger.best_direct_graph_energy == 3
    assert ledger.direct_loss == Fraction(1, 2)
    assert ledger.pairwise_minkowski == 4
    assert ledger.completed_cartesian_principal == Fraction(95, 16)
    assert ledger.completed_best_power == 6
    assert ledger.completed_loss == Fraction(7, 2)
    assert ledger.graph_centering_baseline == Fraction(31, 16)
