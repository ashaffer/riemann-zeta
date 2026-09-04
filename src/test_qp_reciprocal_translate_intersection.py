from math import isqrt

import pytest

from qp_reciprocal_translate_intersection import (
    admissible_quotient,
    diamond_slack,
    primitive_normal_form,
    reconstruct_from_midpoint,
    tangent_chain,
    translated_pairs,
    verify_midpoint_identities,
    verify_primitive_identities,
    worst_shift_intersection,
    worst_target_on_interval,
)


def test_narrow_window_quotient_is_exact_and_unique() -> None:
    assert admissible_quotient(101, 10_000, 2) == 99
    assert admissible_quotient(103, 10_000, 2) is None
    with pytest.raises(ValueError):
        admissible_quotient(10, 100, 5)


def test_all_exact_normal_form_identities_on_dense_fixture() -> None:
    pairs = translated_pairs(10_000**2, 190, 3, 10_000, 19_000)
    assert len(pairs) == 27
    for pair in pairs:
        assert verify_midpoint_identities(pair)
        assert verify_primitive_identities(pair)
        assert diamond_slack(pair, 190) >= 0


def test_midpoint_map_reconstructs_every_pair() -> None:
    pairs = translated_pairs(2_003**2 + 711, 76, 7, 2_003, 3_900)
    assert pairs
    for pair in pairs:
        rebuilt = reconstruct_from_midpoint(
            pair.X, pair.Y, pair.shift, pair.k, pair.target
        )
        assert rebuilt == pair


def test_crt_masks_are_the_original_integer_coordinates() -> None:
    for pair in translated_pairs(5_000**2, 128, 5, 5_000, 9_500):
        form = primitive_normal_form(pair)
        assert (form.T + form.Z) // (2 * form.r) == pair.X
        assert (form.T - form.Z) // (2 * form.s) == pair.Y


def test_tangent_chain_realizes_the_square_root_obstruction() -> None:
    root, width, shift = 100_000, 10_000, 3
    chain = tangent_chain(root, width, shift)
    assert len(chain) == isqrt(width) - shift + 1
    for t, pair in enumerate(chain):
        assert pair.e == -(t * t)
        assert pair.f == -((t + shift) ** 2)
        assert verify_midpoint_identities(pair)
        assert verify_primitive_identities(pair)
        assert diamond_slack(pair, width) >= 0


@pytest.mark.parametrize(
    ("root", "width", "max_shift", "ceiling"),
    [
        (500, 34, 80, 16),
        (1_000, 51, 100, 20),
        (2_000, 76, 120, 26),
    ],
)
def test_hostile_square_targets_stay_at_constant_times_sqrt_window(
    root: int, width: int, max_shift: int, ceiling: int
) -> None:
    count, shift = worst_shift_intersection(
        root * root, width, root, 2 * root - 1, max_shift
    )
    assert 1 <= shift <= max_shift
    assert count <= ceiling


def test_exact_target_sweep_agrees_with_direct_enumeration() -> None:
    root, width, shift = 300, 25, 4
    target_min = root * root - 2 * root
    target_max = root * root + 2 * root
    swept_count, swept_target = worst_target_on_interval(
        target_min, target_max, width, shift, root, 2 * root - shift
    )
    direct = translated_pairs(
        swept_target, width, shift, root, 2 * root - shift
    )
    assert swept_count == len(direct)
    brute_max = max(
        len(translated_pairs(target, width, shift, root, 2 * root - shift))
        for target in range(target_min, target_max + 1)
    )
    assert swept_count == brute_max
