#!/usr/bin/env python3
"""Quantitative barriers for the one-cell growing-jet/Tchakaloff route.

The results here are deliberately scoped.  They concern the Taylor-jet
evaluation geometry used by the conditional four-rows-per-jet envelope; they
are not an upper bound for arbitrary global Pick constructions.

Two facts are encoded.

* The all-jet contour identity cannot have an exact positive quadrature of
  order ``r`` at scaled depth ``o(r)``.  This follows from a truncated
  inverse-phase exponential.
* More decisively, every degree-r evaluation matrix whose physical nodes lie
  in one microscopic phase cell of the right half-plane has condition number
  at least ``4**(r-o(r))`` in the natural Taylor monomial coordinates.  The
  constant 4 is the reciprocal logarithmic capacity of the interval [-1, 0].

The second fact rules out the uniform/subexponential jet-spanning premise of
the advertised four-row Tchakaloff envelope.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from scipy.optimize import minimize_scalar


ALPHA = 0.49
DENSITY = 0.66
CARRIER_DEPTH_FLOOR = ALPHA * DENSITY
PICK_SURCHARGE = 0.0253912552074952


def inverse_phase_depth_barrier(
    order: int,
    *,
    density: float = DENSITY,
    phase_power: float | None = None,
) -> float:
    r"""Finite-r lower bound for the largest scaled quadrature depth.

    On the all-jet contour put

    ``h+lambda_0 = -lambda-i*x/d`` and ``a=d/2``.

    If positive weights annihilate ``exp(-i*x) h**k`` for ``0 <= k <= r``,
    then this function returns a lower bound for ``max(lambda)``.  For
    ``1 < s < 3``, the proof tests the moment equations against the degree-r
    Taylor polynomial of ``exp(-s*a*(h+lambda_0))``.  Its exact, untruncated
    inverse-phase product has positive real part

    ``cos(x/2)**(-s) * cos((1-s/2)*x)``.

    The default ``s=1+1/sqrt(r+1)`` gives

    ``max(lambda)/r >= 2/(e*d)-o(1)``.
    """

    r = int(order)
    d = float(density)
    if r < 1 or d <= 0:
        raise ValueError("require order >= 1 and density > 0")
    s = 1.0 + 1.0 / math.sqrt(r + 1.0) if phase_power is None else float(
        phase_power
    )
    if not (1.0 < s < 3.0):
        raise ValueError("phase_power must lie strictly between 1 and 3")

    phase_margin = math.cos(abs(1.0 - s / 2.0) * math.pi)
    if phase_margin <= 0:
        raise ArithmeticError("positive inverse-phase margin was lost")

    # If s*sqrt((d*Lambda/2)^2+(pi/2)^2) were smaller than R,
    # the relative Taylor remainder would be < phase_margin on every node,
    # producing a strict separating functional and contradicting positivity.
    log_radius = (
        math.lgamma(r + 2.0) + math.log(phase_margin)
    ) / (r + 1.0)
    radius = math.exp(log_radius)
    radicand = (radius / s) ** 2 - (math.pi / 2.0) ** 2
    if radicand <= 0:
        return 0.0
    return (2.0 / d) * math.sqrt(radicand)


def asymptotic_depth_ratio(density: float = DENSITY) -> float:
    """Limit inferior forced by :func:`inverse_phase_depth_barrier`."""

    d = float(density)
    if d <= 0:
        raise ValueError("density must be positive")
    return 2.0 / (math.e * d)


def thin_rectangle_bernstein_tau(
    scale: float,
    anchor: float,
    density: float = DENSITY,
) -> float:
    r"""Bernstein-ellipse log parameter for the one-cell node rectangle.

    Normalize a physical node by ``u=(z-b)/b``.  Right-half-plane
    admissibility gives ``Re(u) in [-1,0]``, while the all-jet phase cell gives
    ``|Im(u)| <= pi/(b*d*L)``.  Under ``zeta=2*u+1`` the rectangle has
    ``Re(zeta) in [-1,1]`` and half-height ``eta=2*pi/(b*d*L)``.

    The returned ``tau`` is chosen so that the Bernstein ellipse
    ``zeta=cosh(tau+i*theta)`` contains that entire rectangle.  It obeys
    ``tau=O(L**(-1/2))``.
    """

    L = float(scale)
    b = float(anchor)
    d = float(density)
    if L <= 0 or b <= 0 or d <= 0:
        raise ValueError("scale, anchor, and density must be positive")
    eta = 2.0 * math.pi / (b * d * L)
    cosh_tau = (eta + math.sqrt(eta * eta + 4.0)) / 2.0
    return math.acosh(cosh_tau)


def log_monic_chebyshev_sup_bound(
    order: int,
    scale: float,
    anchor: float,
    density: float = DENSITY,
) -> float:
    r"""Log of a uniform upper bound for a monic near-null polynomial.

    The polynomial

    ``p_r(u)=2**(1-2*r)*T_r(2*u+1)``

    is monic.  On the one-cell rectangle its supremum is at most

    ``2**(1-2*r)*exp(r*tau)``.
    """

    r = int(order)
    if r < 1:
        raise ValueError("order must be positive")
    tau = thin_rectangle_bernstein_tau(scale, anchor, density)
    return (1.0 - 2.0 * r) * math.log(2.0) + r * tau


def log_vandermonde_condition_lower_bound(
    order: int,
    scale: float,
    anchor: float,
    density: float = DENSITY,
) -> float:
    r"""Rigorous lower bound for the real half-space Taylor condition number.

    The actual row is ``Re(exp(-i*x_j) P(u_j))`` on the real and imaginary
    Taylor coefficients of ``P``.  The two constant-coordinate columns have
    entries ``cos(x_j)`` and ``sin(x_j)``, so at least one has norm
    ``sqrt(N/2)``.  The normalized real coefficient vector of the monic
    Chebyshev polynomial has image norm at most ``sqrt(N)`` times its
    displayed supremum.  Thus only a harmless ``sqrt(2)`` is lost, and the
    bound remains independent of the number of rows.
    """

    return max(
        0.0,
        -log_monic_chebyshev_sup_bound(order, scale, anchor, density)
        - 0.5 * math.log(2.0),
    )


def log_positive_spanning_inradius_upper_bound(
    order: int,
    scale: float,
    anchor: float,
    density: float = DENSITY,
) -> float:
    r"""Log upper bound for the real row convex hull's Euclidean inradius.

    If the origin is in the convex hull at all, the normalized coefficient
    vector of the monic Chebyshev polynomial defines a slab containing every
    row.  Hence no centered Euclidean ball in that convex hull can have radius
    larger than the near-null supremum.
    """

    return log_monic_chebyshev_sup_bound(order, scale, anchor, density)


def taylor_remainder_upper_bound(order: int, radius_ratio: float) -> float:
    r"""Geometric Cauchy-tail bound for a bounded analytic Taylor series."""

    r = int(order)
    q = float(radius_ratio)
    if r < 0 or not (0 <= q < 1):
        raise ValueError("require order >= 0 and 0 <= radius_ratio < 1")
    return q ** (r + 1) / (1.0 - q)


def pair_poisson_kernel(horizontal: float) -> float:
    """Centered reflected-pair Poisson cost used by the old four-row ledger."""

    b = float(horizontal)
    if not (0 <= b < 0.5):
        raise ValueError("horizontal coordinate must lie in [0,1/2)")
    return 1.0 / (0.5 - b) + 1.0 / (0.5 + b)


def schur_step_log_gain(horizontal: float, alpha: float = ALPHA) -> float:
    """Log target gain of one exact Schur zero at the anchor."""

    b = float(horizontal)
    a = float(alpha)
    if not (0 < b < a < 0.5):
        raise ValueError("require 0 < horizontal < alpha < 1/2")
    return math.log((a + b) / (a - b))


def same_b_condition_charged_envelope(
    horizontal: float,
    *,
    alpha: float = ALPHA,
) -> float:
    r"""Diagnostic ceiling after charging the unavoidable ``log(4)`` per jet.

    This retains the *same-b* Poisson bookkeeping of the conditional four-row
    envelope, ``r/L <= 1/(8*K_b)``, and inserts the minimal Taylor inversion
    charge proved above.  It is a ceiling for that advertised ledger, not for
    a redesigned mixed-depth global Pick construction.
    """

    b = float(horizontal)
    net_gain = max(0.0, schur_step_log_gain(b, alpha) - math.log(4.0))
    return net_gain / (8.0 * pair_poisson_kernel(b))


@dataclass(frozen=True)
class ChargedEnvelopeOptimum:
    horizontal: float
    exponent: float
    gap_below_surcharge: float


def optimize_same_b_condition_charged_envelope() -> ChargedEnvelopeOptimum:
    """Optimize the scoped condition-charged diagnostic over the live band."""

    result = minimize_scalar(
        lambda b: -same_b_condition_charged_envelope(float(b)),
        bounds=(CARRIER_DEPTH_FLOOR, ALPHA - 1e-11),
        method="bounded",
        options={"xatol": 1e-14},
    )
    b = float(result.x)
    exponent = -float(result.fun)
    return ChargedEnvelopeOptimum(
        horizontal=b,
        exponent=exponent,
        gap_below_surcharge=PICK_SURCHARGE - exponent,
    )


def self_check() -> dict[str, object]:
    r = 100_000
    depth = inverse_phase_depth_barrier(r)
    depth_ratio = depth / r
    asymptotic_ratio = asymptotic_depth_ratio()
    assert 1.10 < depth_ratio < asymptotic_ratio < 1.12

    L = 1_000_000.0
    jet_order = 20_000
    b = 0.43
    log_condition = log_vandermonde_condition_lower_bound(
        jet_order, L, b
    )
    log_inradius = log_positive_spanning_inradius_upper_bound(
        jet_order, L, b
    )
    assert log_condition / jet_order > 1.37
    assert log_condition / jet_order < math.log(4.0)
    assert log_inradius / jet_order < -1.37

    optimum = optimize_same_b_condition_charged_envelope()
    assert 0.429 < optimum.horizontal < 0.431
    assert 0.0108 < optimum.exponent < 0.0111
    assert optimum.exponent < PICK_SURCHARGE

    return {
        "finite_depth_barrier": {
            "order": r,
            "depth": depth,
            "depth_over_order": depth_ratio,
            "asymptotic_depth_over_order": asymptotic_ratio,
        },
        "thin_cell_condition_barrier": {
            "scale": L,
            "order": jet_order,
            "anchor": b,
            "log_condition_lower": log_condition,
            "log_condition_per_order": log_condition / jet_order,
            "asymptotic_log_condition_per_order": math.log(4.0),
            "log_positive_spanning_inradius_upper": log_inradius,
            "log_inradius_upper_per_order": log_inradius / jet_order,
        },
        "same_b_condition_charged_diagnostic": optimum.__dict__,
        "pick_surcharge": PICK_SURCHARGE,
        "uniform_subexponential_conditioning_possible": False,
        "gp_closed": False,
    }


if __name__ == "__main__":
    print(self_check())
