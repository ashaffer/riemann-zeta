from fractions import Fraction

from qp_four_cycle_cutoff_lp import (
    BALANCED_PEAK,
    MAX_PRODUCT_EXPONENT,
    SLICE_THRESHOLD,
    aggregate_low_trace_exponent,
    cutoff_trace_exponent,
    feasible_second_minimum_interval,
    pointwise_multiplicity_exponent,
    tail_pointwise_multiplicity,
    worst_pointwise_multiplicity_at_product,
)


def test_fixed_product_lp_breakpoints() -> None:
    expected = {
        Fraction(0): Fraction(1, 2),
        Fraction(1, 2): Fraction(1, 2),
        Fraction(7, 8): Fraction(3, 8),
        SLICE_THRESHOLD: Fraction(5, 16),
        BALANCED_PEAK: Fraction(3, 8),
        MAX_PRODUCT_EXPONENT: Fraction(5, 16),
    }
    for product, value in expected.items():
        assert worst_pointwise_multiplicity_at_product(product) == value


def test_fixed_product_formula_matches_dense_exact_grid() -> None:
    denominator = 384
    for numerator in range(0, int(MAX_PRODUCT_EXPONENT * denominator) + 1):
        p = Fraction(numerator, denominator)
        lower, upper = feasible_second_minimum_interval(p)
        candidates = {lower, upper}

        # The only possible interior maximizer is where the two affine
        # pointwise bounds cross.  Include both crossing formulas.
        candidates.add((1 + p) / 3)
        candidates.add(Fraction(25, 24) - p / 3)
        candidates = {b for b in candidates if lower <= b <= upper}
        brute = max(pointwise_multiplicity_exponent(p, b) for b in candidates)
        assert brute == worst_pointwise_multiplicity_at_product(p)


def test_tail_and_cutoff_plateau_are_exact() -> None:
    assert tail_pointwise_multiplicity(Fraction(7, 8)) == Fraction(3, 8)
    assert tail_pointwise_multiplicity(Fraction(19, 16)) == Fraction(3, 8)
    assert aggregate_low_trace_exponent(Fraction(19, 16)) == Fraction(11, 8)

    denominator = 384
    values = []
    minimizers = []
    for numerator in range(0, int(MAX_PRODUCT_EXPONENT * denominator) + 1):
        tau = Fraction(numerator, denominator)
        value = cutoff_trace_exponent(tau)
        values.append(value)
        if value == Fraction(11, 8):
            minimizers.append(tau)
    assert min(values) == Fraction(11, 8)
    assert min(minimizers) == Fraction(7, 8)
    assert max(minimizers) == Fraction(19, 16)


def test_balanced_plateau_witness() -> None:
    p = Fraction(5, 4)
    a = b = Fraction(5, 8)
    lower, upper = feasible_second_minimum_interval(p)
    assert lower <= b <= upper
    assert p - b == a
    assert pointwise_multiplicity_exponent(p, b) == Fraction(3, 8)
    assert p - SLICE_THRESHOLD == Fraction(3, 16)

