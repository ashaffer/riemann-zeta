import math

import pytest

from prime_singular_trace_probe import primes_up_to, psi_scale, residues


def test_sieve_small() -> None:
    assert primes_up_to(1) == []
    assert primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_scale_is_positive_and_increasing() -> None:
    values = [psi_scale(n) for n in (1, 10, 100, 1000)]
    assert all(value > 0 for value in values)
    assert values == sorted(values)


def test_residue_input_guards() -> None:
    with pytest.raises(ValueError):
        residues([], 0.1, 1.0)
    with pytest.raises(ValueError):
        residues([2, 3], 0.0, 1.0)
    with pytest.raises(ValueError):
        residues([2, 3], 0.1, 0.0)


def test_finite_residue_identities() -> None:
    primes = primes_up_to(10_000)
    row = residues(primes, epsilon=0.1, height=0.7)
    assert row.count == len(primes)
    assert row.prime_residue > 0
    assert 0 < row.horizontal_distance < row.prime_residue
    assert 0 < row.vertical_distance < 2 * row.prime_residue
    assert 0 <= row.vertical_complex_abs <= row.prime_residue
    assert row.ordinary_dixmier_ratio > 0
    assert math.isfinite(row.vertical_distance)

