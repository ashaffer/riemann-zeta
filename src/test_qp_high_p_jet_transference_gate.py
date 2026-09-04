from fractions import Fraction
from math import gcd

import pytest

from qp_high_p_jet_transference_gate import (
    audit_supported_cubic_synthesis,
    content_unique_in_compact_narrow_band,
    count_reduced_differences_in_direction,
    cubic_ray_multiplier,
    direction_fiber_point_bound,
    high_p_transference_exponent_ledger,
    phase_first_second_at_tangent,
    primitive_cubic_frequency,
)


def test_primitive_cubic_ray_in_both_parity_classes() -> None:
    for p, d in ((7, 2), (7, 3), (13, -4), (17, -5)):
        frequency = primitive_cubic_frequency(p, d)
        assert gcd(gcd(abs(frequency[0]), abs(frequency[1])), abs(frequency[2])) == 1
        assert phase_first_second_at_tangent(frequency, p, d) == (0, 0)
        assert cubic_ray_multiplier(frequency, p, d) == 1
        assert max(map(abs, frequency)) >= p**3


def test_only_the_primitive_ray_has_two_zero_derivatives_in_a_finite_box() -> None:
    p, d = 5, 2
    generator = primitive_cubic_frequency(p, d)
    for minus_m in range(-25, 26):
        for h in range(-25, 26):
            for k in range(-25, 26):
                frequency = (minus_m, h, k)
                if phase_first_second_at_tangent(frequency, p, d) == (0, 0):
                    assert cubic_ray_multiplier(frequency, p, d) is not None
    assert max(map(abs, generator)) > 25


def test_supported_integer_synthesis_obeys_the_cubic_mass_gate() -> None:
    p, d, H = 7, 2, 8
    generator = primitive_cubic_frequency(p, d)
    unit_modes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    audit = audit_supported_cubic_synthesis(
        unit_modes, generator, p, d, H
    )
    assert audit.aggregate_frequency == generator
    assert audit.cubic_multiplier == 1
    assert audit.coefficient_mass == sum(map(abs, generator))
    assert audit.forced_mass_lower_bound >= Fraction(p**3, 2 * H)


def test_cubic_gate_uses_only_the_two_fejer_coordinates() -> None:
    p, d, H = 7, 2, 8
    generator = primitive_cubic_frequency(p, d)
    # The Poisson coordinate is deliberately larger than H.  The support
    # obstruction still follows from the h,k coordinates alone.
    audit = audit_supported_cubic_synthesis(
        ((generator[0], 0, 0), (0, 1, 0), (0, 0, 1)),
        (1, generator[1], generator[2]),
        p,
        d,
        H,
    )
    assert audit.primitive_fejer_size >= p**3 // 2


def test_off_ray_synthesis_is_rejected() -> None:
    with pytest.raises(ValueError, match="not a nonzero cubic"):
        audit_supported_cubic_synthesis(
            ((1, 0, 0), (0, 1, 0)), (1, 1), 7, 2, 2
        )


def test_direction_progression_bound_is_exact_up_to_endpoints() -> None:
    fixtures = (
        (1009, 37, 8, 117, 1),
        (349, 33, 7, 41, 1),
        (2736, 65, -19, 200, 3),
    )
    for Q, p, d, B, G in fixtures:
        values = count_reduced_differences_in_direction(Q, p, d, B, G)
        assert len(values) <= direction_fiber_point_bound(B, p, G)
        assert all(value % p == (-Q * d) % p for value in values)
        assert all(abs(value) <= Fraction(2 * B, G) for value in values)


def test_compact_narrow_band_content_spacing() -> None:
    assert content_unique_in_compact_narrow_band(1009, 144, 17, 3, 29)
    assert not content_unique_in_compact_narrow_band(100, 90, 11, 9, 20)


def test_endpoint_direction_fiber_beats_both_cluster_ceilings() -> None:
    ledger = high_p_transference_exponent_ledger()
    assert ledger["bounded_probe_cubic_cost"] == Fraction(61, 160)
    assert ledger["direction_fiber"] == Fraction(329, 480)
    assert ledger["full_cluster_ceiling"] == 1
    assert ledger["closing_cluster_ceiling"] == Fraction(49, 48)
    assert ledger["full_direction_margin"] == Fraction(151, 480)
    assert ledger["closing_direction_margin"] == Fraction(161, 480)
