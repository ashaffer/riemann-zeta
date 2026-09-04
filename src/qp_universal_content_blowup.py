"""Exact arithmetic for the arbitrary-content reflected cusp blow-up.

This module records three local facts used by the companion report:

* every integral multiplier chart ``g=2*J*d^2`` has the same normal
  crossing as the central chart, with a factor ``J``;
* clearing denominators gives a universal normal crossing for arbitrary
  content ``g``;
* the two one-band axes of that universal crossing have fixed-``Q``
  divisor parametrizations, including the asymmetric second-root branch.

The last genuinely two-factor locus is deliberately not claimed here.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from qp_coupled_cusp_fejer_inverse import (
    ReducedSymmetricCuspData,
    reduced_symmetric_cusp_data,
)


@dataclass(frozen=True)
class MultiplierChartData:
    """One point on ``g=2*J*d^2`` in integral cusp coordinates."""

    point: ReducedSymmetricCuspData
    multiplier: int
    ell: int
    c: int
    u: int
    h: int
    left_residual: int
    right_residual: int


@dataclass(frozen=True)
class UniversalContentBlowup:
    """Denominator-cleared normal coordinates at content ``g``."""

    point: ReducedSymmetricCuspData
    ell: int
    C: int
    U: int
    H: int
    left_residual: int
    right_residual: int


def primitive_point_from_content(
    Q: int, y: int, g: int, p: int, d: int
) -> ReducedSymmetricCuspData:
    """Build a primitive symmetric-cusp point from ``(g,p,d)``."""

    if Q <= abs(y) or g <= 0 or p <= abs(d) or gcd(p, abs(d)) != 1:
        raise ValueError("require Q>|y|, g>0, p>|d|, and gcd(p,d)=1")
    if g * (p - d) % 2 or g * (p + d) % 2:
        raise ValueError("the two half-content coordinates must be integral")
    r = g * (p - d) // 2
    s = g * (p + d) // 2
    point = reduced_symmetric_cusp_data(Q, y, r, s)
    assert (point.g, point.p, point.d) == (g, p, d)
    return point


def multiplier_chart_data(
    p: int, d: int, multiplier: int, c: int, u: int
) -> MultiplierChartData:
    """Return and verify the exact ``g=2*J*d^2`` normal form.

    Put ``ell=p^2-d^2``,

    ``Q=J*p*ell+c`` and ``y=J*d*ell+u``.

    If ``h=d*c-2*p*u``, then

    ``e+u^2=J*d*(p-d)*(h-d*u)`` and
    ``f+u^2=J*d*(p+d)*(h+d*u)``.
    """

    if multiplier <= 0 or d <= 0 or p <= d or gcd(p, d) != 1:
        raise ValueError("require J>=1 and coprime p>d>=1")
    ell = p * p - d * d
    Q = multiplier * p * ell + c
    y = multiplier * d * ell + u
    g = 2 * multiplier * d * d
    point = primitive_point_from_content(Q, y, g, p, d)
    h = d * c - 2 * p * u
    left = h - d * u
    right = h + d * u
    assert point.e + u * u == multiplier * d * (p - d) * left
    assert point.f + u * u == multiplier * d * (p + d) * right
    assert point.n == p * u - c * d
    assert point.e - point.f == g * point.n
    assert u * y == -multiplier * d * p * point.n - Fraction(
        point.e + point.f, 2
    )
    return MultiplierChartData(
        point=point,
        multiplier=multiplier,
        ell=ell,
        c=c,
        u=u,
        h=h,
        left_residual=left,
        right_residual=right,
    )


def multiplier_chart_count_exponents() -> dict[str, Fraction]:
    """Return the energy-core powers in the all-multiplier count.

    The height enumeration costs ``X=B/Q^(1/3)``.  With
    ``Q=D^(33/16)`` and ``B<D^(7/6)``, this is ``D^(23/48)``, saving
    ``D^(1/48)`` over the smallest ``sqrt(A)`` budget.  The balanced
    height ``h=0`` costs only ``X^(1/3)``.
    """

    q = Fraction(33, 16)
    b = Fraction(7, 6)
    x = b - q / 3
    sqrt_a = Fraction(1, 2)
    assert x == Fraction(23, 48)
    return {
        "Q": q,
        "B": b,
        "height_count": x,
        "balanced_height_count": x / 3,
        "sqrt_A_floor": sqrt_a,
        "saving": sqrt_a - x,
    }


def universal_content_blowup(
    point: ReducedSymmetricCuspData,
) -> UniversalContentBlowup:
    """Return the universal integral normal crossing.

    For ``ell=p^2-d^2`` set

    ``C=2*d^2*Q-g*p*ell``, ``U=2*d*y-g*ell``, and ``H=C-2*p*U``.

    Then

    ``2*d*n=-(H+p*U)``,
    ``4*d^2*e+U^2=g*(p-d)*(H-d*U)``, and
    ``4*d^2*f+U^2=g*(p+d)*(H+d*U)``.
    """

    p, d, g = point.p, point.d, point.g
    if d == 0 or p <= abs(d):
        raise ValueError("require a nonsingular primitive point")
    ell = p * p - d * d
    C = 2 * d * d * point.Q - g * p * ell
    U = 2 * d * point.y - g * ell
    H = C - 2 * p * U
    left = H - d * U
    right = H + d * U
    assert 2 * d * point.n == -(H + p * U)
    assert 4 * d * d * point.e + U * U == g * (p - d) * left
    assert 4 * d * d * point.f + U * U == g * (p + d) * right
    assert (
        4
        * d
        * d
        * ((p - d) * point.f - (p + d) * point.e)
        == 4 * d * d * U * point.y
    )
    return UniversalContentBlowup(
        point=point,
        ell=ell,
        C=C,
        U=U,
        H=H,
        left_residual=left,
        right_residual=right,
    )


def one_band_axis_certificate(
    point: ReducedSymmetricCuspData,
) -> dict[str, int | str]:
    """Return fixed-``Q`` divisor data on either one-band axis.

    ``left_residual=0`` puts ``e=-xi^2`` and gives
    ``p|(Q-xi)``, ``p+d|(Q+xi)``.

    ``right_residual=0`` puts ``f=-xi^2``.  In its asymmetric bad range
    ``xi=-t`` set ``eta=t-g*(p-d)``.  With ``a=p-d``, one has
    ``a|2*(Q+eta)`` and, unless ``(p,d)=(2,1)``,
    ``a-d|2*(Q+3*eta)``.
    """

    normal = universal_content_blowup(point)
    p, d, g, Q = point.p, point.d, point.g, point.Q
    if d <= 0:
        raise ValueError("use the positive-d orientation")
    left_zero = normal.left_residual == 0
    right_zero = normal.right_residual == 0
    if left_zero == right_zero:
        raise ValueError("require exactly one vanishing one-band residual")
    if normal.U % (2 * d):
        raise AssertionError("integrality of the square error forces 2d|U")
    xi = normal.U // (2 * d)
    if g % d:
        raise AssertionError("a one-band axis forces d|g")
    data: dict[str, int | str] = {"xi": xi, "content_quotient": g // d}
    if left_zero:
        assert point.e == -xi * xi
        assert point.n == -(p + d) * xi
        assert (Q - xi) % p == 0
        assert (Q + xi) % (p + d) == 0
        data.update(
            {
                "axis": "left",
                "p_target": Q - xi,
                "second_target": Q + xi,
                "second_divisor": p + d,
            }
        )
        return data

    assert point.f == -xi * xi
    assert point.n == -(p - d) * xi
    assert (Q + xi) % p == 0
    assert (Q - xi) % (p - d) == 0
    data.update(
        {
            "axis": "right",
            "p_target": Q + xi,
            "second_target": Q - xi,
            "second_divisor": p - d,
        }
    )
    if xi < 0:
        t = -xi
        eta = t - g * (p - d)
        a = p - d
        assert point.e == -t * eta
        assert 2 * (Q + eta) % a == 0
        data.update({"t": t, "eta": eta, "eta_target": 2 * (Q + eta)})
        if a != d:
            assert 2 * (Q + 3 * eta) % (a - d) == 0
            data.update(
                {
                    "third_target": 2 * (Q + 3 * eta),
                    "third_divisor": a - d,
                }
            )
        else:
            assert (p, d) == (2, 1)
            data["primitive_exception"] = 1
    return data


def nondivisible_zero_offset_family(
    d: int, slope_multiplier: int = 2
) -> ReducedSymmetricCuspData:
    """An infinite residual family with ``d^2`` not dividing ``g``.

    Put ``p=m*d+1``, ``g=2*d``, ``ell=p^2-d^2``,

    ``Q=(p*ell-1)/d`` and ``y=ell``.

    Then ``U=0``, ``H=-2*d`` and
    ``(e,f)=(-(p-d),-(p+d))``.  For fixed ``m>=2`` this is a compact
    remote family as ``d`` grows.  It is a genuine surviving two-factor
    chart, not a counterexample to the desired global estimate.
    """

    m = slope_multiplier
    if d <= 2 or m < 2:
        raise ValueError("require d>2 and m>=2")
    p = m * d + 1
    ell = p * p - d * d
    numerator = p * ell - 1
    assert numerator % d == 0
    Q = numerator // d
    y = ell
    g = 2 * d
    point = primitive_point_from_content(Q, y, g, p, d)
    normal = universal_content_blowup(point)
    assert normal.U == 0 and normal.H == -2 * d
    assert normal.left_residual == normal.right_residual == -2 * d
    assert (point.e, point.f) == (-(p - d), -(p + d))
    assert g % (d * d) != 0
    return point

