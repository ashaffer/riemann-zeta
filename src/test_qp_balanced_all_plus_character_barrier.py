from fractions import Fraction

import pytest

from qp_balanced_all_plus_character_barrier import (
    BalancedAllPlusLedger,
    active_ledger,
    latin_square_uniform_norm,
    nonprincipal_parseval_floor,
    residual_equivalence_on_nodes,
)


def test_active_exponent_ledger() -> None:
    ledger = active_ledger()
    assert ledger.residual_exponent == Fraction(16, 33)
    assert ledger.all_plus_width_exponent == Fraction(49, 33)
    assert ledger.raw_schur_exponent == Fraction(8, 33)
    assert ledger.character_parseval_exponent == Fraction(49, 66)
    assert ledger.character_penalty == Fraction(1, 2)
    assert ledger.principal_exponent == Fraction(-1, 66)


def test_nonprincipal_parseval_floor() -> None:
    group_order = 1000
    set_size = 40
    floor = nonprincipal_parseval_floor(group_order, set_size)
    assert floor == pytest.approx(((group_order * set_size - set_size**2) / 999) ** 0.5)
    assert floor > (set_size / 2) ** 0.5


def test_q_cubed_residual_is_exact_on_project_width_shell() -> None:
    prime = 23
    # These are the prime powers in a representative narrow shell around 23/2.
    nodes = (11, 13)
    width = 500
    assert max(8 * a * b * c for a in nodes for b in nodes for c in nodes) < 2 * prime**3
    assert min(8 * a * b * c for a in nodes for b in nodes for c in nodes) > width
    assert residual_equivalence_on_nodes(nodes, prime, width)


def test_latin_square_saturates_schur_scale() -> None:
    for order in (1, 4, 25, 100):
        assert latin_square_uniform_norm(order) == pytest.approx(order**0.5)


def test_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        BalancedAllPlusLedger(Fraction(3, 2))
    with pytest.raises(ValueError):
        nonprincipal_parseval_floor(10, 10)
    with pytest.raises(ValueError):
        latin_square_uniform_norm(0)
