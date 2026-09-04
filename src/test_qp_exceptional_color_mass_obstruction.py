from qp_exceptional_color_mass_obstruction import (
    additive_exceptional_ledger,
    flat_additive_mass,
)


def test_explicit_short_kernel_vectors_and_small_determinant() -> None:
    ledger = additive_exceptional_ledger(10_007, 10_009, 10_037, 10_039)
    assert ledger.colors == (10_007, 10_009, 10_037, 10_039)
    assert 0 < abs(ledger.color_determinant) <= 32**2
    assert ledger.successive_product_envelope < 100


def test_actual_prime_interval_has_nontrivial_flat_additive_mass() -> None:
    primes = (
        10_007,
        10_009,
        10_037,
        10_039,
        10_061,
        10_067,
        10_069,
        10_079,
        10_091,
        10_093,
        10_099,
    )
    ledger = flat_additive_mass(primes)
    assert ledger.support_size == 11
    assert ledger.additive_quadruples == 407
    assert ledger.all_distinct_quadruples == 160
    assert ledger.flat_all_distinct_mass > 1.3
    assert ledger.maximum_absolute_determinant <= 100**2
