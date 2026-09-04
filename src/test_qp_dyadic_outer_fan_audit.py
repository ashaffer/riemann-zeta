from fractions import Fraction

from qp_dyadic_outer_fan_audit import (
    actual_reference_alias_fixture,
    dyadic_outer_fan_ledger,
)


def test_dyadic_outer_fan_exponents() -> None:
    ledger = dyadic_outer_fan_ledger()
    assert ledger.low_frequency == Fraction(1, 33)
    assert ledger.top_frequency == Fraction(17, 33)
    assert ledger.fan_size == Fraction(8, 33)
    assert ledger.alias_threshold == Fraction(8, 33)
    assert ledger.top_alias_multiplicity == Fraction(3, 11)
    assert ledger.full_lattice_dual_branches == Fraction(17, 33)


def test_actual_reference_alias_fixture() -> None:
    fixture = actual_reference_alias_fixture()
    assert fixture.reference == (79_889, 79_873)
    assert fixture.color_step == fixture.frequency * fixture.fan_size
    assert fixture.determinant == 1
    assert fixture.alias_increment == -1

    # Trial division is enough for this fixed replay and keeps the module
    # dependency-free.
    for value in (fixture.q, *fixture.reference):
        divisor = 2
        while divisor * divisor <= value:
            assert value % divisor
            divisor += 1
