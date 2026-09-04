from collections import Counter
from math import sqrt

from qp_tagged_trace_projective_barrier import (
    paley_difference_mask,
    paley_tagged_trace_ledger,
    principal_paley_hard_window_fixture,
)


def test_paley_mask_has_exact_regular_degrees() -> None:
    prime = 11
    mask = paley_difference_mask(prime)
    degree = (prime - 1) // 2
    assert all(sum(row) == degree for row in mask)
    assert all(sum(mask[i][j] for i in range(prime)) == degree for j in range(prime))


def test_exact_paley_singular_and_zero_tag_ledger() -> None:
    prime = 11
    ledger = paley_tagged_trace_ledger(prime)
    degree = 5
    assert ledger.column_degree == degree
    assert ledger.entries == prime * degree
    assert ledger.zero_tag_factorial_mass == prime * degree * (degree - 1)
    assert ledger.rank == prime
    assert ledger.frobenius_squared == ledger.entries
    assert ledger.exceptional_singular_value == degree
    assert ledger.repeated_singular_value == sqrt(prime + 1) / 2
    assert ledger.projective_to_hilbert_schmidt_ratio > ledger.rigorous_ratio_lower_bound
    assert ledger.rigorous_ratio_lower_bound > sqrt((prime - 1) / 2)


def test_paley_selector_embeds_in_four_literal_hard_windows() -> None:
    prime = 7
    fixture = principal_paley_hard_window_fixture(prime)
    degree = (prime - 1) // 2
    assert fixture.D**2 < fixture.q
    assert fixture.D**33 <= fixture.q**16 < (fixture.D + 1) ** 33
    assert len(fixture.edges) == prime * degree
    assert fixture.distinct_bands
    assert all(
        max(map(abs, edge.residuals)) <= fixture.q * fixture.D
        for edge in fixture.edges
    )
    row_degrees = Counter(edge.row_index for edge in fixture.edges)
    endpoint_degrees = Counter(edge.endpoint_index for edge in fixture.edges)
    assert set(row_degrees.values()) == {degree}
    assert set(endpoint_degrees.values()) == {degree}
    assert sum(value * (value - 1) for value in endpoint_degrees.values()) == (
        prime * degree * (degree - 1)
    )
