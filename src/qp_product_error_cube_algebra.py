"""Exact finite-difference identities for the QP product-error cube gate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class RectangleAlgebra:
    mixed_carrier: int
    mixed_product_error: int
    leibniz_rhs: int


@dataclass(frozen=True)
class CubeAlgebra:
    third_carrier: int
    third_product_error: int
    leibniz_rhs: int
    mixed_rs: int
    mixed_rh: int
    mixed_sh: int


@dataclass(frozen=True)
class DeterminantAlgebra:
    alpha: int
    beta: int
    delta: int
    mixed_error_a: int
    mixed_error_b: int
    first_elimination_lhs: int
    first_elimination_rhs: int
    second_elimination_lhs: int
    second_elimination_rhs: int


@dataclass(frozen=True)
class CubeDeterminantAlgebra:
    """The three wedge eliminations of the two product-error cube laws."""

    delta_uv: int
    delta_hu: int
    delta_hv: int
    third_error_a: int
    third_error_b: int
    elimination_lhs: tuple[int, int, int]
    elimination_rhs: tuple[int, int, int]


def rectangle_algebra(
    a: int,
    r: int,
    s: int,
    carriers: Mapping[tuple[int, int], int],
    center: int = 0,
) -> RectangleAlgebra:
    """Replay ``Box(a*v-C)`` on a completion rectangle."""

    v00 = carriers[(0, 0)]
    v10 = carriers[(1, 0)]
    v01 = carriers[(0, 1)]
    v11 = carriers[(1, 1)]
    rho = v10 - v00
    sigma = v01 - v00
    tau = v00 + v11 - v10 - v01
    errors = {
        (0, 0): a * v00 - center,
        (1, 0): (a + r) * v10 - center,
        (0, 1): (a + s) * v01 - center,
        (1, 1): (a + r + s) * v11 - center,
    }
    mixed_error = (
        errors[(0, 0)]
        + errors[(1, 1)]
        - errors[(1, 0)]
        - errors[(0, 1)]
    )
    rhs = s * rho + r * sigma + (a + r + s) * tau
    return RectangleAlgebra(tau, mixed_error, rhs)


def _mixed_pair(
    carriers: Mapping[tuple[int, int, int], int],
    first: int,
    second: int,
) -> int:
    zero = [0, 0, 0]
    p = zero.copy()
    p[first] = 1
    q = zero.copy()
    q[second] = 1
    pq = zero.copy()
    pq[first] = 1
    pq[second] = 1
    return (
        carriers[tuple(zero)]
        + carriers[tuple(pq)]
        - carriers[tuple(p)]
        - carriers[tuple(q)]
    )


def _third_difference(values: Mapping[tuple[int, int, int], int]) -> int:
    total = 0
    for bits, value in values.items():
        total += (-1) ** (3 - sum(bits)) * value
    return total


def cube_algebra(
    a: int,
    r: int,
    s: int,
    h: int,
    carriers: Mapping[tuple[int, int, int], int],
    center: int = 0,
) -> CubeAlgebra:
    """Replay the exact three-direction product Leibniz identity."""

    errors: dict[tuple[int, int, int], int] = {}
    for bits, carrier in carriers.items():
        i, j, k = bits
        errors[bits] = (a + i * r + j * s + k * h) * carrier - center

    mixed_rs = _mixed_pair(carriers, 0, 1)
    mixed_rh = _mixed_pair(carriers, 0, 2)
    mixed_sh = _mixed_pair(carriers, 1, 2)
    third_carrier = _third_difference(carriers)
    third_error = _third_difference(errors)
    rhs = (
        (a + r + s + h) * third_carrier
        + h * mixed_rs
        + r * mixed_sh
        + s * mixed_rh
    )
    return CubeAlgebra(
        third_carrier,
        third_error,
        rhs,
        mixed_rs,
        mixed_rh,
        mixed_sh,
    )


def ap_third_identity(
    a: int, step: int, carriers: tuple[int, int, int, int], center: int = 0
) -> tuple[int, int, int]:
    """Return ``(Delta^3 error, Delta^3 v, Leibniz RHS)``."""

    v0, v1, v2, v3 = carriers
    second = v2 - 2 * v1 + v0
    third = v3 - 3 * v2 + 3 * v1 - v0
    errors = tuple((a + j * step) * v - center for j, v in enumerate(carriers))
    third_error = errors[3] - 3 * errors[2] + 3 * errors[1] - errors[0]
    rhs = (a + 3 * step) * third + 3 * step * second
    return third_error, third, rhs


def determinant_algebra(
    a: int,
    b: int,
    r: int,
    p: int,
    s: int,
    ell: int,
    carriers: Mapping[tuple[int, int], int],
    center_a: int = 0,
    center_b: int = 0,
) -> DeterminantAlgebra:
    """Replay the two exact determinant/error elimination identities."""

    rect_a = rectangle_algebra(a, r, s, carriers, center_a)
    rect_b = rectangle_algebra(b, p, ell, carriers, center_b)
    v00 = carriers[(0, 0)]
    rho = carriers[(1, 0)] - v00
    sigma = carriers[(0, 1)] - v00
    tau = rect_a.mixed_carrier
    alpha = a * p - b * r
    beta = a * ell - b * s
    delta = r * ell - p * s
    lhs1 = p * rect_a.mixed_product_error - r * rect_b.mixed_product_error
    rhs1 = -delta * rho + (alpha - delta) * tau
    lhs2 = ell * rect_a.mixed_product_error - s * rect_b.mixed_product_error
    rhs2 = delta * sigma + (beta + delta) * tau
    return DeterminantAlgebra(
        alpha,
        beta,
        delta,
        rect_a.mixed_product_error,
        rect_b.mixed_product_error,
        lhs1,
        rhs1,
        lhs2,
        rhs2,
    )


def cube_determinant_algebra(
    a: int,
    b: int,
    r: int,
    p: int,
    s: int,
    ell: int,
    h: int,
    g: int,
    carriers: Mapping[tuple[int, int, int], int],
    center_a: int = 0,
    center_b: int = 0,
) -> CubeDeterminantAlgebra:
    """Replay all three determinant eliminations on a completion cube.

    The three completion directions are ``U=(r,p)``, ``V=(s,ell)`` and
    ``H=(h,g)``.  Our signs are

    ``delta_uv=det(U,V)``, ``delta_hu=det(H,U)``, and
    ``delta_hv=det(H,V)``.
    """

    cube_a = cube_algebra(a, r, s, h, carriers, center_a)
    cube_b = cube_algebra(b, p, ell, g, carriers, center_b)
    omega = cube_a.third_carrier
    tau_uv = cube_a.mixed_rs
    tau_uh = cube_a.mixed_rh
    tau_vh = cube_a.mixed_sh

    alpha = a * p - b * r
    beta = a * ell - b * s
    gamma = a * g - b * h
    delta_uv = r * ell - p * s
    delta_hu = h * p - g * r
    delta_hv = h * ell - g * s

    error_a = cube_a.third_product_error
    error_b = cube_b.third_product_error
    lhs = (
        p * error_a - r * error_b,
        ell * error_a - s * error_b,
        g * error_a - h * error_b,
    )
    rhs = (
        delta_hu * tau_uv
        - delta_uv * tau_uh
        + (alpha - delta_uv + delta_hu) * omega,
        delta_hv * tau_uv
        + delta_uv * tau_vh
        + (beta + delta_uv + delta_hv) * omega,
        -delta_hu * tau_vh
        - delta_hv * tau_uh
        + (gamma - delta_hu - delta_hv) * omega,
    )
    return CubeDeterminantAlgebra(
        delta_uv,
        delta_hu,
        delta_hv,
        error_a,
        error_b,
        lhs,
        rhs,
    )


def exponent_ledger() -> dict[str, float]:
    """Critical powers relative to ``D``."""

    return {
        "q": 33 / 16,
        "rounding_error_D_over_q": -17 / 16,
        "three_point_threshold_sqrt_q": 33 / 32,
        "four_point_threshold_q_two_thirds": 11 / 8,
        "cube_scale_ratio_q_over_D": 17 / 16,
    }
