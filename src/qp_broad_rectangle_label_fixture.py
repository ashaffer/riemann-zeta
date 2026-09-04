"""Exact ledger for the broad reciprocal-rectangle label obstruction.

The fixture preserves the shell scale, the coprime endpoint/defect lattice,
the mixed carrier label ``t ~ r*s/q``, determinant label ``Delta=0``, and
packet-freeness.  It deliberately fails the individual product bands.  It
therefore tests label-counting arguments, not the physical QP theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb


@dataclass(frozen=True)
class BroadFixturePoint:
    defect: int
    completion_a: int
    completion_b: int
    carrier: int


@dataclass(frozen=True)
class BroadRectangleLabels:
    step_a_1: int
    step_a_2: int
    step_b_1: int
    step_b_2: int
    mixed_carrier: int
    completion_determinant: int


def fixture_endpoints(scale: int) -> tuple[int, int]:
    """Return coprime ``x<y`` with ``x*L-y*(L-1)=1``."""

    if scale < 2:
        raise ValueError("scale must be at least two")
    y = scale * scale + 1
    x = scale * scale - scale + 1
    return x, y


def fixture_point(scale: int, index: int) -> BroadFixturePoint:
    """Return the exact quadratic-carrier point indexed by ``index``."""

    x, y = fixture_endpoints(scale)
    return BroadFixturePoint(
        defect=index,
        completion_a=y + scale * index,
        completion_b=x + (scale - 1) * index,
        carrier=scale * scale - scale * index + index * index,
    )


def defect_identity(scale: int, index: int) -> int:
    """Replay ``x*a-y*b=index`` exactly."""

    x, y = fixture_endpoints(scale)
    point = fixture_point(scale, index)
    return x * point.completion_a - y * point.completion_b


def rectangle_labels(
    scale: int, base: int, first_step: int, second_step: int
) -> BroadRectangleLabels:
    """Return the exact labels of one additive parameter rectangle."""

    p00 = fixture_point(scale, base)
    p10 = fixture_point(scale, base + first_step)
    p01 = fixture_point(scale, base + second_step)
    p11 = fixture_point(scale, base + first_step + second_step)

    r = p10.completion_a - p00.completion_a
    s = p01.completion_a - p00.completion_a
    p = p10.completion_b - p00.completion_b
    ell = p01.completion_b - p00.completion_b
    mixed = p00.carrier + p11.carrier - p10.carrier - p01.carrier
    determinant = r * ell - p * s
    first_defect_step = p10.defect - p00.defect
    second_defect_step = p01.defect - p00.defect
    _, y = fixture_endpoints(scale)
    defect_numerator = first_defect_step * s - second_defect_step * r
    if defect_numerator % y:
        raise AssertionError("defect determinant numerator is not divisible by y")
    if determinant != defect_numerator // y:
        raise AssertionError("completion and defect determinant conventions disagree")
    return BroadRectangleLabels(r, s, p, ell, mixed, determinant)


def interval_additive_energy(length: int) -> int:
    """Return ``E^+({0,...,length-1})`` exactly."""

    if length < 0:
        raise ValueError("length must be nonnegative")
    return (2 * length**3 + length) // 3


def positive_broad_rectangle_count(length: int) -> int:
    """Count bases and positive steps with ``base+h+j<length``."""

    if length < 0:
        raise ValueError("length must be nonnegative")
    return comb(length, 3) if length >= 3 else 0


def completion_a_product(scale: int, index: int) -> int:
    """Return ``a_n*v_n``; its cubic drift records product-band failure."""

    point = fixture_point(scale, index)
    return point.completion_a * point.carrier


def completion_a_product_formula(scale: int, index: int) -> int:
    """Closed form for ``a_n*v_n`` used by the hostile audit."""

    L = scale
    n = index
    return L**4 + L**2 + L * n**3 + n**2 - L * n


def exponent_ledger() -> dict[str, float]:
    """Return powers relative to ``D`` at ``q=D^(33/16)``."""

    return {
        "q": 33 / 16,
        "sqrt_q": 33 / 32,
        "fixture_size": 1.0,
        "fixture_energy": 3.0,
        "pfre_target": 2.5,
        "inverse_endpoint_branches": 5 / 64,
    }


def replay(scale: int = 101, length: int = 20) -> dict[str, int | float]:
    """Run a small exact replay suitable for command-line inspection."""

    if length >= scale:
        raise ValueError("take length < scale so the fixture remains in one shell")
    for n in range(length):
        assert defect_identity(scale, n) == n
        assert completion_a_product(scale, n) == completion_a_product_formula(
            scale, n
        )
    labels = rectangle_labels(scale, 1, 2, 3)
    assert labels.mixed_carrier == 12
    assert labels.completion_determinant == 0
    assert labels.mixed_carrier * scale**2 == 2 * labels.step_a_1 * labels.step_a_2
    return {
        "scale": scale,
        "length": length,
        "energy": interval_additive_energy(length),
        "positive_broad_rectangles": positive_broad_rectangle_count(length),
        "sample_mixed_carrier": labels.mixed_carrier,
        "sample_determinant": labels.completion_determinant,
        **exponent_ledger(),
    }


if __name__ == "__main__":
    print(replay())
