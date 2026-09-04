from fractions import Fraction

import pytest

from qp_stationary_action_jet_rigidity import (
    recover_reflection_orbit_from_higher_three_jet,
    recover_saddle_from_three_jet,
    stationary_action_four_jet,
    stationary_action_three_jet,
    three_jet_collision_is_identical,
)


def test_exact_three_jet_inversion_recovers_the_integer_mode() -> None:
    data = stationary_action_three_jet(C=100, S=20, a=12, h=144, k=128, m=100)
    assert data["X"] == 1
    assert data["Y"] == 2
    assert data["D"] == 32
    assert data["first"] == -200
    assert data["second"] == Fraction(25, 2)
    assert data["third"] == Fraction(-525, 256)
    recovered = recover_saddle_from_three_jet(
        100, 20, data["first"], data["second"], data["third"]
    )
    assert (recovered["a"], recovered["h"], recovered["k"], recovered["m"]) == (
        12,
        144,
        128,
        100,
    )


def test_two_jets_do_not_break_the_poisson_alias_but_three_do() -> None:
    first = stationary_action_three_jet(C=100, S=20, a=12, h=144, k=128, m=100)
    second = stationary_action_three_jet(C=100, S=20, a=4, h=8, k=512, m=150)
    assert first["first"] == second["first"] == -200
    assert first["second"] == second["second"] == Fraction(25, 2)
    assert first["third"] != second["third"]
    assert not three_jet_collision_is_identical(first, second)


def test_exact_three_jet_collision_forces_identical_saddles() -> None:
    left = stationary_action_three_jet(
        C=63, S=17, a=7, h=98, k=150, m=Fraction(-63, 2)
    )
    right = stationary_action_three_jet(
        C=63, S=17, a=7, h=98, k=150, m=Fraction(-63, 2)
    )
    assert three_jet_collision_is_identical(left, right)


def test_zero_dual_and_fold_are_the_exact_exceptions() -> None:
    zero_dual = stationary_action_three_jet(C=100, S=20, a=12, h=144, k=128, m=100)
    # Modify to X=Y=1, hence m=0.  Its first three jets exist, but the
    # three-jet inverse intentionally rejects this already-controlled branch.
    zero_dual = stationary_action_three_jet(C=100, S=20, a=12, h=144, k=64, m=0)
    with pytest.raises(ValueError, match="zero-dual"):
        recover_saddle_from_three_jet(
            100, 20, zero_dual["first"], zero_dual["second"], zero_dual["third"]
        )

    with pytest.raises(ValueError, match="fold"):
        stationary_action_three_jet(
            C=100,
            S=20,
            a=12,
            h=144,
            k=Fraction(-128, 3),
            m=Fraction(-500, 3),
        )


def test_higher_three_jet_recovers_exactly_one_reflection_orbit() -> None:
    data = stationary_action_four_jet(C=100, S=20, a=5, h=-12, k=-36, m=32)
    orbit = recover_reflection_orbit_from_higher_three_jet(
        100, 20, data["second"], data["third"], data["fourth"]
    )
    parameters = {(item["a"], item["h"], item["k"], item["m"]) for item in orbit}
    assert parameters == {
        (Fraction(5), Fraction(-12), Fraction(-36), Fraction(32)),
        (Fraction(15), Fraction(-36), Fraction(-12), Fraction(-32)),
    }


def test_reflection_is_the_exact_integral_affine_alias() -> None:
    left = stationary_action_four_jet(C=63, S=17, a=7, h=98, k=150, m=-Fraction(63, 2))
    right = stationary_action_four_jet(
        C=63,
        S=17,
        a=10,
        h=150,
        k=98,
        m=Fraction(63, 2),
    )
    assert right["action"] - left["action"] == left["m"] * left["S"]
    assert right["first"] - left["first"] == left["m"]
    assert tuple(right[name] for name in ("second", "third", "fourth")) == tuple(
        left[name] for name in ("second", "third", "fourth")
    )


def test_fourth_jet_breaks_a_nonreflection_discrete_three_jet_collision() -> None:
    left = stationary_action_four_jet(C=100, S=20, a=5, h=-12, k=-36, m=32)
    right = stationary_action_four_jet(C=100, S=20, a=5, h=-3, k=-54, m=-12)
    assert (left["action"] - right["action"]).denominator == 1
    assert (left["first"] - right["first"]).denominator == 1
    assert (left["second"], left["third"]) == (right["second"], right["third"])
    assert left["fourth"] != right["fourth"]


def test_central_higher_jet_inverse_has_only_the_swap_ambiguity() -> None:
    data = stationary_action_four_jet(C=100, S=20, a=10, h=-80, k=-79, m=1)
    orbit = recover_reflection_orbit_from_higher_three_jet(
        100, 20, data["second"], data["third"], data["fourth"]
    )
    assert {(item["h"], item["k"], item["m"]) for item in orbit} == {
        (Fraction(-80), Fraction(-79), Fraction(1)),
        (Fraction(-79), Fraction(-80), Fraction(-1)),
    }
