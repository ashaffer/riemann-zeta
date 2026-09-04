from fractions import Fraction
from itertools import combinations
from math import gcd

from qp_error_labelled_spectral_gate import (
    completion_energy,
    error_coherence_ledger,
    method_fixture,
    tangent_shell_fixture,
    tagged_energy,
    verify_method_fixture,
    verify_tangent_shell_fixture,
)


def test_exact_product_band_and_coprime_progression() -> None:
    modulus, center, points = method_fixture(6)
    assert 12 < modulus < 24
    assert all(point.completion * point.carrier - center == point.error for point in points)
    assert all(abs(point.error) <= modulus // 2 for point in points)
    assert all(
        gcd(first.completion, second.completion) == 1
        for first, second in combinations(points, 2)
    )


def test_energy_and_tagged_cell_identities() -> None:
    _, _, points = method_fixture(7)
    assert completion_energy(points) == (2 * 7**3 + 7) // 3
    joint_energy, maximum_cell = tagged_energy(points)
    assert joint_energy == 2 * 7**2 - 7
    assert maximum_cell == 2


def test_coherence_and_scope_ledger() -> None:
    ledger = error_coherence_ledger(6)
    assert ledger.coherence == Fraction((2 * 6**3 + 6) // 3, 2 * 6**2 - 6)
    assert ledger.maximum_error_fibre == 1
    assert ledger.maximum_pair_cell == 2
    assert ledger.no_three_completion_error_collinear
    assert ledger.no_three_completion_carrier_collinear
    assert ledger.common_shell_ratio > 2


def test_full_replay() -> None:
    assert verify_method_fixture(6).size == 6


def test_tangent_shell_resonance_is_exact_affine_packet() -> None:
    root = 10_000
    radius = 12
    center, points = tangent_shell_fixture(root, radius)
    assert all(point.completion * point.carrier - center == point.error for point in points)
    assert all(abs(point.error) <= radius**2 for point in points)
    assert all(point.completion + point.carrier == 2 * root for point in points)
    assert verify_tangent_shell_fixture(root, radius) == completion_energy(points)
