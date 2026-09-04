from fractions import Fraction

from qp_combinatorial_inverse_bsg_drc_gate import (
    continuous_mixed_label,
    label_dispersing_point,
    mixed_carrier_label,
    popular_difference_exponent_ledger,
)


def test_exact_endpoint_lattice_and_strict_carrier_convexity() -> None:
    step, scale = 1009, 50
    points = [label_dispersing_point(step, scale, k) for k in range(scale, 2 * scale + 1)]
    for left, middle, right in zip(points, points[1:], points[2:]):
        assert right.carrier - 2 * middle.carrier + left.carrier > 0


def test_mixed_label_has_the_claimed_floor_error() -> None:
    step, scale = 1009, 50
    for base in range(scale, 2 * scale - 15):
        for first_shift, second_shift in ((2, 3), (4, 7), (-2, 9)):
            vertices = (
                base,
                base + first_shift,
                base + second_shift,
                base + first_shift + second_shift,
            )
            if min(vertices) < scale or max(vertices) > 2 * scale:
                continue
            exact = mixed_carrier_label(
                step, scale, base, first_shift, second_shift
            )
            model = continuous_mixed_label(
                step, base, first_shift, second_shift
            )
            assert abs(Fraction(exact) - model) < 4


def test_high_product_direction_labels_are_base_injective() -> None:
    step, scale = 1009, 100
    # d*e > step makes the continuous label move by more than the total
    # floor error whenever the base changes.
    d, e = 31, 37
    assert d * e > step
    labels = []
    for base in range(scale, 2 * scale - d - e + 1):
        labels.append(mixed_carrier_label(step, scale, base, d, e))
    assert len(labels) == len(set(labels))


def test_critical_combinatorial_exponents() -> None:
    epsilon = Fraction(1, 100)
    ledger = popular_difference_exponent_ledger(epsilon)
    assert ledger["popular_multiplicity_floor"] == Fraction(3, 4) + epsilon
    assert ledger["matching_headroom"] == Fraction(1, 8) - epsilon
    assert ledger["standard_bsg_subset_floor"] == Fraction(3, 4) + epsilon
    assert ledger["standard_bsg_doubling_ceiling"] == Fraction(1, 2) - 4 * epsilon
    assert ledger["behrend_excess_over_threshold"] == Fraction(1, 8) - epsilon
    assert ledger["low_label_margin_below_behrend_energy"] == Fraction(23, 32)
    assert ledger["generic_u3_cube_floor"] == 3 + 2 * epsilon
    assert ledger["fixed_direction_triple_base_floor"] == 2 * epsilon
    assert ledger["broad_to_third_difference_margin"] == Fraction(1, 32)
    assert ledger["fixture_u3_cubes"] == Fraction(7, 2)
    assert ledger["fixture_low_volume_cube_margin"] == Fraction(51, 32)
