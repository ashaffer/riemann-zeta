#!/usr/bin/env python3
"""Mixed-depth affine finite-difference screens for the compact Pick gate.

This module generalizes the centered equal-depth binomial screen to a sloped
line segment.  Two interlaced chains still have exact polynomial finite-
difference cancellation, but their horizontal depths now vary by a fixed
amount across ``Theta(L)`` phase cells.  Consequently this family is not a
one-cell growing Taylor fixture.

The formulas below distinguish two quantities.

* ``attenuation`` is a rigorous asymptotic lower obstruction for the scalar
  Schur problem, conditional only on the displayed affine screen.
* ``poisson_load`` is the necessary pointwise reflected-pair load of that
  abstract screen.  A screen is called admissible here only when its load is
  at most the completed ``L/2`` budget after normalization.

An admissible obstruction below the GP surcharge does not prove the desired
upper construction.  It only clears this particular global mixed-depth
family as a counterexample.
"""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, differential_evolution, linprog, minimize_scalar


ALPHA = 0.49
DENSITY = 0.66
MIN_DEPTH = ALPHA * DENSITY
PICK_SURCHARGE = 0.0253912552074952


def complex_lagrange_rate_at(target_parameter: complex) -> float:
    r"""Return ``1+integral_0^1 log|t-x| dx`` for ``t`` off ``[0,1]``.

    The integral is evaluated by the analytic primitive

    ``Re[(t-1) Log(t-1)-t Log(t)]-1``.

    Hence the requested quantity is just the real part of the two logarithmic
    terms, with orientation ``t Log(t)-(t-1) Log(t-1)``.  The expression is
    continuous across branch choices after taking the real part.  Screen
    parameters keep ``t`` off the integration segment.
    """

    t = complex(target_parameter)
    if abs(t.imag) < 1e-14 and 0.0 <= t.real <= 1.0:
        raise ValueError("target parameter must lie off [0,1]")
    return float((t * np.log(t) - (t - 1.0) * np.log(t - 1.0)).real)


def segment_geometry(
    center_depth: float,
    ordinate_width: float,
    slope: float,
    *,
    ordinate_center: float = 0.0,
    alpha: float = ALPHA,
) -> tuple[float, complex, float, float]:
    """Return Taylor radius, target parameter, and endpoint depths.

    The physical segment is

    ``z(x)=b+s*H*(x-1/2)-i*(v0+H*(x-1/2))``, ``0<=x<=1``.
    """

    b = float(center_depth)
    H = float(ordinate_width)
    s = float(slope)
    v0 = float(ordinate_center)
    if H <= 0:
        raise ValueError("ordinate width must be positive")
    left_depth = b - s * H / 2.0
    right_depth = b + s * H / 2.0
    target_parameter = 0.5 + complex(alpha - b, v0) / (
        H * complex(s, -1.0)
    )
    endpoint_left = complex(left_depth - alpha, -v0 + H / 2.0)
    endpoint_right = complex(right_depth - alpha, -v0 - H / 2.0)
    radius = max(abs(endpoint_left), abs(endpoint_right))
    return radius, target_parameter, left_depth, right_depth


def affine_screen_attenuation(
    center_depth: float,
    ordinate_width: float,
    slope: float,
    *,
    ordinate_center: float = 0.0,
    alpha: float = ALPHA,
    density: float = DENSITY,
) -> float:
    r"""Asymptotic forced attenuation of a sloped two-chain screen.

    With ``K/L -> c=d*H/pi``, Taylor remainder, positive binomial dependence,
    and complex Lagrange continuation give

    ``F=c*(log(alpha/(2R))-J(t_*))``.

    The formula is available only when the whole segment lies in the Taylor
    disk ``|z-alpha|<alpha``.
    """

    R, target_parameter, _, _ = segment_geometry(
        center_depth,
        ordinate_width,
        slope,
        ordinate_center=ordinate_center,
        alpha=alpha,
    )
    if R >= alpha:
        return float("-inf")
    c = density * ordinate_width / math.pi
    return c * (
        math.log(alpha / (2.0 * R))
        - complex_lagrange_rate_at(target_parameter)
    )


def reflected_pair_kernel(depth: float, offset: float) -> float:
    """Completed reflected-pair kernel on the limiting centered line x=1/2."""

    b = float(depth)
    v = float(offset)
    if not (0.0 <= b < 0.5):
        return float("inf")
    return (0.5 - b) / ((0.5 - b) ** 2 + v * v) + (
        0.5 + b
    ) / ((0.5 + b) ** 2 + v * v)


def microscopic_cluster_poisson_ceiling(
    row_rate: float, depth: float
) -> float:
    r"""Uniform normalized Poisson ceiling for a microscopic cluster.

    Put ``floor(row_rate*L)`` distinct ordinates at a common depth, with any
    spacing.  Since each translated reflected-pair kernel is at most its
    centered value, the entire cluster has pointwise load divided by ``L`` at
    most ``row_rate*K_depth(0)`` (up to the harmless floor).

    This constructs a triangular-array quantifier wall for fixed-``N``
    Carleson interpolation; it is not a Pick obstruction because nearly
    identical half-space rows may be analytically redundant.
    """

    rate = float(row_rate)
    if rate < 0:
        raise ValueError("row rate must be nonnegative")
    return rate * reflected_pair_kernel(depth, 0.0)


def fixed_color_separation_upper_bound(
    scale: float,
    depth: float,
    color_count: int,
) -> float:
    r"""Pigeonhole upper bound for one color in an ``L^-3`` cluster.

    Among any ``color_count+1`` consecutive nodes, two share a color.  Their
    ordinate gap is at most ``color_count/L^3``.  At common depth ``b`` their
    right-half-plane pseudohyperbolic distance is therefore at most the
    returned quantity.  It tends to zero for every fixed number of colors.
    """

    L = float(scale)
    b = float(depth)
    colors = int(color_count)
    if L <= 0 or b <= 0 or colors < 1:
        raise ValueError("require positive scale/depth/color count")
    gap = colors / L**3
    return gap / math.hypot(2.0 * b, gap)


def affine_screen_poisson_load_at(
    ordinate: float,
    center_depth: float,
    ordinate_width: float,
    slope: float,
    *,
    density: float = DENSITY,
) -> float:
    """Leading ``L``-normalized load at one ordinate.

    The two interlaced chains have combined ordinate density ``2*d*L/pi``.
    """

    t = float(ordinate)
    b = float(center_depth)
    H = float(ordinate_width)
    s = float(slope)
    integral, _ = quad(
        lambda v: reflected_pair_kernel(b + s * v, t - v),
        -H / 2.0,
        H / 2.0,
        epsabs=2e-11,
        epsrel=2e-11,
        limit=160,
    )
    return 2.0 * density * integral / math.pi


def affine_screen_max_poisson_load(
    center_depth: float,
    ordinate_width: float,
    slope: float,
    *,
    density: float = DENSITY,
) -> tuple[float, float]:
    """Maximize the pointwise load and return ``(load, ordinate)``.

    A compact numerical interval suffices: outside the segment the positive
    kernel decreases after the nearest endpoint.  We seed all endpoint and
    center candidates, then use bounded scalar searches between them.
    """

    H = float(ordinate_width)
    scale = max(1.0, H)
    bound = H / 2.0 + 4.0 * scale

    def negative(t: float) -> float:
        return -affine_screen_poisson_load_at(
            t,
            center_depth,
            H,
            slope,
            density=density,
        )

    grid = np.linspace(-bound, bound, 49)
    values = np.array([-negative(float(t)) for t in grid])
    candidates: list[tuple[float, float]] = [
        (float(values[i]), float(grid[i])) for i in range(len(grid))
    ]
    for i in range(1, len(grid) - 1):
        if values[i] >= values[i - 1] and values[i] >= values[i + 1]:
            result = minimize_scalar(
                negative,
                bounds=(float(grid[i - 1]), float(grid[i + 1])),
                method="bounded",
                options={"xatol": 2e-10},
            )
            candidates.append((-float(result.fun), float(result.x)))
    return max(candidates)


@dataclass(frozen=True)
class MixedDepthScreenOptimum:
    center_depth: float
    ordinate_width: float
    slope: float
    ordinate_center: float
    left_depth: float
    right_depth: float
    target_parameter_real: float
    target_parameter_imag: float
    taylor_radius: float
    attenuation: float
    poisson_load: float
    poisson_peak_ordinate: float
    surcharge_gap: float


def optimize_affine_screen(
    *,
    alpha: float = ALPHA,
    density: float = DENSITY,
    minimum_depth: float = MIN_DEPTH,
    seed: int = 230813,
) -> MixedDepthScreenOptimum:
    """Search all affine segments in the live depth strip.

    The Poisson cap is imposed by a quadratic exterior penalty during the
    global search and checked exactly at the returned point.  This is a
    reproducible floating optimization, not an interval global certificate.
    """

    max_width = 2.0 * alpha * 0.999

    def unpack(x: np.ndarray) -> tuple[float, float, float, float]:
        b, H, q, v0 = map(float, x)
        max_slope = 2.0 * min(b - minimum_depth, alpha - b) / H
        return b, H, q * max_slope, v0

    def objective(x: np.ndarray) -> float:
        b, H, slope, v0 = unpack(x)
        attenuation = affine_screen_attenuation(
            b,
            H,
            slope,
            ordinate_center=v0,
            alpha=alpha,
            density=density,
        )
        if not math.isfinite(attenuation):
            return 100.0
        load, _ = affine_screen_max_poisson_load(
            b, H, slope, density=density
        )
        excess = max(0.0, load - 0.5)
        return -attenuation + 200.0 * excess * excess + 20.0 * excess

    result = differential_evolution(
        objective,
        bounds=(
            (minimum_depth + 1e-5, alpha - 1e-5),
            (1e-4, max_width),
            (-1.0, 1.0),
            (-0.49, 0.49),
        ),
        seed=seed,
        popsize=12,
        maxiter=90,
        tol=2e-8,
        polish=True,
        workers=1,
    )
    b, H, slope, v0 = unpack(result.x)

    # Include the exactly one-dimensional centered face explicitly.  The
    # exterior-penalty search can otherwise stop a few 1e-6 below its active
    # Poisson boundary in four variables.
    def centered_width(depth: float) -> float:
        return brentq(
            lambda width: affine_screen_max_poisson_load(
                depth, width, 0.0, density=density
            )[0]
            - 0.5,
            1e-8,
            max_width,
            xtol=2e-12,
            rtol=2e-12,
        )

    centered_result = minimize_scalar(
        lambda depth: -affine_screen_attenuation(
            depth,
            centered_width(float(depth)),
            0.0,
            alpha=alpha,
            density=density,
        ),
        bounds=(minimum_depth + 1e-5, alpha - 1e-5),
        method="bounded",
        options={"xatol": 2e-11},
    )
    centered_b = float(centered_result.x)
    centered_H = centered_width(centered_b)
    centered_attenuation = affine_screen_attenuation(
        centered_b, centered_H, 0.0, alpha=alpha, density=density
    )
    searched_attenuation = affine_screen_attenuation(
        b,
        H,
        slope,
        ordinate_center=v0,
        alpha=alpha,
        density=density,
    )
    if centered_attenuation >= searched_attenuation:
        b, H, slope, v0 = centered_b, centered_H, 0.0, 0.0

    R, target_parameter, left, right = segment_geometry(
        b, H, slope, ordinate_center=v0, alpha=alpha
    )
    attenuation = affine_screen_attenuation(
        b,
        H,
        slope,
        ordinate_center=v0,
        alpha=alpha,
        density=density,
    )
    load, peak = affine_screen_max_poisson_load(
        b, H, slope, density=density
    )
    return MixedDepthScreenOptimum(
        center_depth=b,
        ordinate_width=H,
        slope=slope,
        ordinate_center=v0,
        left_depth=left,
        right_depth=right,
        target_parameter_real=target_parameter.real,
        target_parameter_imag=target_parameter.imag,
        taylor_radius=R,
        attenuation=attenuation,
        poisson_load=load,
        poisson_peak_ordinate=peak + v0,
        surcharge_gap=PICK_SURCHARGE - attenuation,
    )


def self_check() -> dict[str, object]:
    # The slope-zero formula must reproduce the earlier centered screen.
    b = 0.4709446182
    c = 0.0079215710
    H = math.pi * c / DENSITY
    attenuation = affine_screen_attenuation(b, H, 0.0)
    load, peak = affine_screen_max_poisson_load(b, H, 0.0)
    assert abs(attenuation - 0.0139849236) < 2e-8
    assert abs(load - 0.5) < 2e-7
    assert abs(peak) < 1e-6

    optimum = optimize_affine_screen()
    assert optimum.poisson_load <= 0.50001
    cluster_ceiling = microscopic_cluster_poisson_ceiling(0.01, 0.47)
    separation = fixed_color_separation_upper_bound(10_000, 0.47, 20)
    assert cluster_ceiling < 0.5
    assert separation < 3e-11
    return {
        "equal_depth_regression": {
            "attenuation": attenuation,
            "poisson_load": load,
            "poisson_peak_ordinate": peak,
        },
        "mixed_depth_optimum": asdict(optimum),
        "pick_surcharge": PICK_SURCHARGE,
        "fixed_N_carleson_quantifier_wall": {
            "depth": 0.47,
            "rows_over_L": 0.01,
            "poisson_ceiling": cluster_ceiling,
            "example_scale": 10_000,
            "fixed_color_count": 20,
            "same_color_separation_upper": separation,
        },
        "obstruction_crosses_surcharge": optimum.attenuation
        > PICK_SURCHARGE,
        "gp_closed": False,
    }


def cyclotomic_three_interpolation_log_cost(
    order: int,
    target_parameter: complex,
    *,
    target_angle_samples: int = 32,
) -> float:
    r"""Floating LP cost for the one-chain cubic-root positive screen.

    This is an exploratory diagnostic for the positive convolution

    ``(1+z+z^2)^K`` at ``z=exp(-2*pi*i/3)``.

    Its coefficients are positive and the associated moment functional has a
    zero of order ``K``.  There are ``2K+1`` real half-space rows for a
    complex polynomial of degree below ``K``.  After the positive dependence,
    row ``n`` is known only to accuracy inverse to its trinomial probability.
    The returned number is the log of the largest target evaluation found by
    solving the resulting real linear programs over several target phases.

    It is not a theorem-grade bound and is not used by the GP verdict.
    """

    K = int(order)
    if K < 2:
        raise ValueError("order must be at least two")
    t = complex(target_parameter)
    # Exact normalized coefficients of (1+z+z^2)^K, accumulated stably as a
    # probability distribution.
    probabilities = np.array([1.0])
    for _ in range(K):
        probabilities = np.convolve(probabilities, np.ones(3) / 3.0)
    nodes = np.linspace(0.0, 1.0, 2 * K + 1)
    # Chebyshev coordinates on [0,1] keep the finite LP reasonably scaled.
    vandermonde = np.polynomial.chebyshev.chebvander(2.0 * nodes - 1.0, K - 1)
    phases = 2.0 * math.pi * np.arange(2 * K + 1) / 3.0
    matrix = np.hstack(
        (
            np.cos(phases)[:, None] * vandermonde,
            np.sin(phases)[:, None] * vandermonde,
        )
    )
    weighted = probabilities[:, None] * matrix
    inequality = np.vstack((weighted, -weighted))
    rhs = np.ones(2 * len(nodes))

    target_vander = np.polynomial.chebyshev.chebvander(
        np.array([2.0 * t - 1.0], dtype=complex), K - 1
    )[0]
    maxima: list[float] = []
    for angle in np.linspace(
        0.0, 2.0 * math.pi, int(target_angle_samples), endpoint=False
    ):
        phase = np.exp(-1j * angle)
        # Re[phase*(A(t)+iB(t))].
        objective = np.concatenate(
            (
                np.real(phase * target_vander),
                np.real(1j * phase * target_vander),
            )
        )
        result = linprog(
            -objective,
            A_ub=inequality,
            b_ub=rhs,
            bounds=[(None, None)] * (2 * K),
            method="highs",
        )
        if not result.success:
            return float("inf")
        maxima.append(-float(result.fun))
    largest = max(maxima)
    return math.log(largest) if largest > 0 else float("-inf")


if __name__ == "__main__":
    print(self_check())
