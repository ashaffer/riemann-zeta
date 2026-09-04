from fractions import Fraction
import math

import pytest

from finite_wheel_transfer_operator import (
    SparseRenewalOperator,
    apply_sparse_entries,
    character_diagonalization,
    cyclic_physical_gaps,
    periodic_units,
    prefix_discrepancy_certificate,
    repeated_base_wheel_operator,
    uniform_wheel_certificate,
)


def independent_period_sum(operator: SparseRenewalOperator) -> tuple[Fraction, ...]:
    """Sum k=h+a*m directly, independently of the sparse recurrence."""
    m = operator.size
    z = operator.z
    x = z**m
    masses = []
    for i, site in enumerate(operator.sites):
        total = Fraction(0)
        for h in range(1, m + 1):
            plus_cycles, plus_index = divmod(i + h, m)
            minus_cycles, minus_index = divmod(i - h, m)
            plus = operator.sites[plus_index] + plus_cycles * operator.period
            minus = operator.sites[minus_index] + minus_cycles * operator.period
            base_distance = plus - minus
            progression = base_distance / (1 - x) + 2 * operator.period * x / (
                1 - x
            ) ** 2
            total += z ** (h - 1) * progression
        masses.append(operator.p**2 * total / (2 * operator.period))
    return tuple(masses)


@pytest.mark.parametrize(
    ("P", "q", "p"),
    [
        (1, 5, Fraction(1, 3)),
        (2, 7, Fraction(2, 5)),
        (6, 5, Fraction(1, 7)),
        (30, 7, Fraction(3, 11)),
    ],
)
def test_sparse_resolvent_equals_independent_infinite_series(
    P: int, q: int, p: Fraction
) -> None:
    operator = SparseRenewalOperator.unit_wheel(P, q, p)
    assert operator.stationary_voronoi_masses() == independent_period_sum(operator)


def test_sparse_cyclic_systems_are_solved_exactly() -> None:
    operator = SparseRenewalOperator.unit_wheel(6, 5, Fraction(2, 9))
    forward, backward = operator.gap_resolvents()
    assert apply_sparse_entries(operator.sparse_system_entries(1), forward) == tuple(
        Fraction(gap) for gap in operator.gaps
    )
    assert apply_sparse_entries(operator.sparse_system_entries(-1), backward) == tuple(
        Fraction(operator.gaps[(i - 1) % operator.size])
        for i in range(operator.size)
    )


def test_dense_geometric_successor_kernel_is_stochastic() -> None:
    operator = SparseRenewalOperator.unit_wheel(30, 7, Fraction(1, 8))
    matrix = operator.transition_matrix()
    for row in matrix:
        assert sum(row, Fraction(0)) == 1
        assert all(entry >= 0 for entry in row)


@pytest.mark.parametrize(
    ("P", "q", "p"),
    [
        (1, 5, Fraction(1, 10)),
        (2, 11, Fraction(1)),
        (6, 7, Fraction(1, 9)),
        (30, 11, Fraction(3, 20)),
        (210, 11, Fraction(1, 5)),
        (1024, 13, Fraction(2, 7)),
    ],
)
def test_uniform_growing_wheel_certificate_is_exact(
    P: int, q: int, p: Fraction
) -> None:
    certificate = uniform_wheel_certificate(P, q, p)
    certificate.validate()
    assert certificate.redistributed_mass == Fraction(1, q)
    assert all(excess >= 0 for excess in certificate.excesses)
    center, radius, total = certificate.exact_triangle_ledger()
    assert center == Fraction(1, q * (q - 1))
    assert radius == Fraction(1, q)
    assert total == certificate.nonprincipal_bound == Fraction(1, q - 1)
    for numerator in range(1, q):
        assert abs(certificate.numerical_nonprincipal_mode(numerator)) <= float(
            certificate.nonprincipal_bound
        ) + 2e-14


def test_p_periodic_base_profile_has_exact_mass_one_over_q_in_every_residue() -> None:
    P, q, p = 30, 11, Fraction(2, 13)
    base = SparseRenewalOperator(P, periodic_units(P), p)
    base_masses = base.stationary_voronoi_masses()
    aggregate = [Fraction(0)] * q
    for block in range(q):
        for site, mass in zip(base.sites, base_masses):
            aggregate[(site + block * P) % q] += mass / q
    assert aggregate == [Fraction(1, q)] * q


def test_additive_and_multiplicative_character_diagonalizations_agree() -> None:
    certificate = uniform_wheel_certificate(30, 11, Fraction(2, 9))
    for numerator in range(1, certificate.q):
        direct, reconstructed = character_diagonalization(
            certificate.residue_masses, certificate.q, numerator
        )
        assert abs(direct - reconstructed) < 2e-14


def test_repeated_base_wheel_has_exact_uniform_q_residue_mass() -> None:
    P, q = 30, 11
    operator = repeated_base_wheel_operator(P, q, Fraction(2, 13))
    masses = operator.residue_masses(q)
    assert masses == (Fraction(1, q),) * q
    certificate = prefix_discrepancy_certificate(operator, q)
    assert certificate.total_residues == (Fraction(P),) * q


def test_interval_truncation_is_exact_endpoint_coboundary() -> None:
    operator = SparseRenewalOperator.unit_wheel(30, 11, Fraction(2, 9))
    certificate = prefix_discrepancy_certificate(operator, 11)
    for left, right in [(-137, 19), (0, 330), (17, 931), (330, 1320)]:
        discrepancy = certificate.interval_discrepancy(left, right)
        coboundary = certificate.endpoint_coboundary(left, right)
        assert discrepancy == coboundary
        assert sum((abs(value) for value in discrepancy), Fraction(0)) <= (
            2 * certificate.max_formal_l1
        )


def test_every_pre_q_eratosthenes_stage_has_zero_full_q_mode() -> None:
    q = 11
    previous_modulus = 1
    for stage_prime in (2, 3, 5, 7):
        new_modulus = previous_modulus * stage_prime
        period = new_modulus * q
        before_sites = tuple(
            n
            for n in range(1, period + 1)
            if math.gcd(n, previous_modulus) == 1
        )
        after_sites = tuple(
            n
            for n in range(1, period + 1)
            if math.gcd(n, new_modulus) == 1
        )
        before = SparseRenewalOperator(period, before_sites, Fraction(1))
        after = SparseRenewalOperator(period, after_sites, Fraction(1))
        expected = (Fraction(period, q),) * q
        before_totals = prefix_discrepancy_certificate(before, q).total_residues
        after_totals = prefix_discrepancy_certificate(after, q).total_residues
        assert before_totals == after_totals == expected
        previous_modulus = new_modulus


def test_physical_gaps_and_argument_validation() -> None:
    assert cyclic_physical_gaps(10, (1, 3, 7)) == (2, 4, 4)
    with pytest.raises(ValueError):
        SparseRenewalOperator.unit_wheel(6, 5, 0)
    with pytest.raises(ValueError):
        SparseRenewalOperator.unit_wheel(5, 5, Fraction(1, 2))
    with pytest.raises(ValueError):
        SparseRenewalOperator.unit_wheel(6, 9, Fraction(1, 2))
    with pytest.raises(ValueError):
        cyclic_physical_gaps(10, (3, 1))
