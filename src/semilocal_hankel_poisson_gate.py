#!/usr/bin/env python3
"""Exact gates for a semilocal Hankel-to-Poisson bridge.

The Connes--Consani local-factor product is an exact source for the
*pole-free* semilocal Weil multiplier.  It does not by itself provide a
positive square root of the localized Weil form.  This module records the
normalization and three obstructions which any finite bridge must respect.

* A cyclic finite-dimensional unitary model erases the Weil trace anomaly.
* The polar Hankel contribution of ``rho_infinity prod rho_p`` at ``s=0``
  has rank ``1 + number_of_primes``, not the universal rank two of the zeta
  pole form.
* Even a smooth (hence rapidly compact Hankel) phase and an exact
  ``X-U^* X U`` representation do not imply a floor-independent Ward bound.

These are exact algebraic/mathematical gates.  They neither disprove an
arithmetic factorization using more structure nor prove a zero-free strip.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import argparse
import json
import math
from typing import Iterable, Sequence

import mpmath as mp
import numpy as np


def gamma_r(s: complex | mp.mpc) -> mp.mpc:
    """The completed real gamma factor ``pi^(-s/2) Gamma(s/2)``."""

    value = mp.mpc(s)
    return mp.power(mp.pi, -value / 2) * mp.gamma(value / 2)


def rho_infinity(t: float | mp.mpf) -> mp.mpc:
    """Connes--Consani's archimedean ratio on ``s=1/2+i t``."""

    s = mp.mpf("0.5") + 1j * mp.mpf(t)
    return gamma_r(s) / gamma_r(1 - s)


def rho_prime(prime: int, t: float | mp.mpf) -> mp.mpc:
    """Connes--Consani's finite-place ratio on the critical line."""

    if prime < 2:
        raise ValueError("prime must be at least two")
    s = mp.mpf("0.5") + 1j * mp.mpf(t)
    return (1 - mp.power(prime, -(1 - s))) / (
        1 - mp.power(prime, -s)
    )


def semilocal_ratio(
    t: float | mp.mpf, primes: Sequence[int] = (2, 3, 5)
) -> mp.mpc:
    """Return ``rho_infinity prod_(p in primes) rho_p``."""

    value = rho_infinity(t)
    for prime in primes:
        value *= rho_prime(int(prime), t)
    return value


def prime_multiplier(prime: int, t: float | mp.mpf) -> mp.mpf:
    r"""Closed form of the full prime-power logarithmic derivative.

    This equals

    ``-2 log(p) sum_(k>=1) p^(-k/2) cos(k t log(p))``.
    """

    if prime < 2:
        raise ValueError("prime must be at least two")
    tt = mp.mpf(t)
    z = mp.power(prime, -mp.mpf("0.5")) * mp.exp(
        -1j * tt * mp.log(prime)
    )
    return -2 * mp.log(prime) * mp.re(z / (1 - z))


def semilocal_weil_multiplier(
    t: float | mp.mpf, primes: Sequence[int] = (2, 3, 5)
) -> mp.mpf:
    """The exact pole-free semilocal Weil multiplier."""

    tt = mp.mpf(t)
    value = mp.re(mp.digamma(mp.mpf("0.25") + 0.5j * tt)) - mp.log(
        mp.pi
    )
    return value + sum(prime_multiplier(int(p), tt) for p in primes)


def ratio_logarithmic_derivative(
    t: float | mp.mpf, primes: Sequence[int] = (2, 3, 5)
) -> mp.mpc:
    """Numerically evaluate ``-i conjugate(u_F) u_F'`` without a log branch."""

    tt = mp.mpf(t)
    value = semilocal_ratio(tt, primes)
    derivative = mp.diff(lambda x: semilocal_ratio(x, primes), tt)
    return -1j * mp.conj(value) * derivative


def reference_multiplier(t: float | mp.mpf) -> mp.mpf:
    """Multiplier of the repository reference form ``G+W_plus``."""

    tt = mp.mpf(t)
    return 1 + mp.log(1 + 4 * tt * tt) / 2


def reference_phase(t: float | mp.mpf) -> mp.mpf:
    """A phase whose derivative is :func:`reference_multiplier`."""

    tt = mp.mpf(t)
    return (
        tt * mp.log(1 + 4 * tt * tt) / 2
        + mp.atan(2 * tt) / 2
    )


def finite_trace_defect(
    projection: np.ndarray,
    unitary_multiplier: np.ndarray,
    test_multiplier: np.ndarray,
) -> complex:
    r"""Return the forbidden finite cyclic approximation to the Weil trace.

    The inputs ``unitary_multiplier`` and ``test_multiplier`` are diagonal.
    For every finite projection ``P`` this is identically zero:

    ``tr(M_g (P-M_u^* P M_u)) = 0``.

    The continuum Weil value is a non-cyclic trace anomaly; consequently an
    exactly unitary finite collocation cannot approximate it.
    """

    p = np.asarray(projection, dtype=complex)
    u = np.asarray(unitary_multiplier, dtype=complex)
    g = np.asarray(test_multiplier, dtype=complex)
    if p.ndim != 2 or p.shape[0] != p.shape[1]:
        raise ValueError("projection must be square")
    if u.shape != p.shape or g.shape != p.shape:
        raise ValueError("all matrices must have the same shape")
    if np.linalg.norm(u - np.diag(np.diag(u))) > 1.0e-12:
        raise ValueError("unitary_multiplier must be diagonal")
    if np.linalg.norm(g - np.diag(np.diag(g))) > 1.0e-12:
        raise ValueError("test_multiplier must be diagonal")
    defect = p - u.conj().T @ p @ u
    return complex(np.trace(g @ defect))


def fourier_hardy_projection(order: int, rank: int | None = None) -> np.ndarray:
    """A deterministic finite cyclic Hardy projection used only as a no-go."""

    if order < 3:
        raise ValueError("order must be at least three")
    if rank is None:
        rank = (order + 1) // 2
    if not 0 < rank < order:
        raise ValueError("rank must lie strictly between zero and order")
    rows = np.arange(order)[:, None]
    columns = np.arange(order)[None, :]
    fourier = np.exp(2j * np.pi * rows * columns / order) / math.sqrt(order)
    basis = fourier[:, :rank]
    return basis @ basis.conj().T


def origin_polar_hankel_sequence(
    order: int, length: int, pole_location: float = -1 / 3
) -> np.ndarray:
    r"""Negative Fourier coefficients of ``(z-pole_location)^(-order)``.

    A pole of order ``r`` gives a polynomial-exponential sequence of exact
    Hankel rank ``r``.  The local-factor product has such a pole at the Cayley
    image of ``s=0``, namely ``-1/3``.
    """

    if order < 1 or length < 2 * order + 1:
        raise ValueError("need order>=1 and length>=2*order+1")
    x = float(pole_location)
    values = np.zeros(length, dtype=float)
    # values[k-1] is the coefficient of z^(-k), k>=1.
    for k in range(order, length + 1):
        values[k - 1] = math.comb(k - 1, order - 1) * x ** (k - order)
    return values


def hankel_from_negative_coefficients(
    coefficients: Sequence[float], dimension: int
) -> np.ndarray:
    """Return ``H[i,j]=a_{-(i+j+1)}`` from a coefficient sequence."""

    values = np.asarray(coefficients)
    if dimension < 1 or values.size < 2 * dimension - 1:
        raise ValueError("insufficient coefficients for requested dimension")
    indices = np.add.outer(np.arange(dimension), np.arange(dimension))
    return values[indices]


def semilocal_origin_pole_order(primes: Iterable[int]) -> int:
    """Order at ``s=0`` of ``rho_infinity prod rho_p``."""

    return 1 + len(tuple(primes))


@dataclass(frozen=True)
class SmoothQuasiInnerWardCountermodel:
    epsilon: float
    phase_amplitude: float
    old_q_floor: float
    residual_cross: float
    reference_collar_metric: float
    ward_ratio: float
    enlarged_determinant: float


@dataclass(frozen=True)
class RelativeSoninWardCountermodel:
    """One two-dimensional block of the relative Sonin countermodel."""

    delta: float
    epsilon: float
    rotation_weight: float
    sonin_weight: float
    old_q_floor: float
    residual_cross_squared: float
    ward_ratio: float


def smooth_quasi_inner_ward_countermodel(
    epsilon: float, phase_amplitude: float = 1.0
) -> SmoothQuasiInnerWardCountermodel:
    r"""Exact smooth-phase countermodel to a generic Hankel implication.

    On ``L2(S1)`` take ``N=-i d/dtheta`` and
    ``U=exp(i b sin(theta))``.  Its Hankel block has rapidly decreasing
    singular values because the symbol is smooth (indeed its Fourier
    coefficients are Bessel functions).  Nevertheless

    ``N-U^*NU = -b cos(theta)``.

    On ``old=span{1}``, ``collar=span{exp(i theta)}``, and with reference
    matrix ``diag(epsilon,1)``, the old Q floor is epsilon while the residual
    cross is ``-b/2``.  The Ward response is ``b^2/(4 epsilon)``.
    """

    eps = float(epsilon)
    b = float(phase_amplitude)
    if eps <= 0.0 or b == 0.0:
        raise ValueError("require epsilon>0 and nonzero phase amplitude")
    cross = -b / 2.0
    return SmoothQuasiInnerWardCountermodel(
        epsilon=eps,
        phase_amplitude=b,
        old_q_floor=eps,
        residual_cross=cross,
        reference_collar_metric=1.0,
        ward_ratio=cross * cross / eps,
        enlarged_determinant=eps - cross * cross,
    )


def relative_sonin_ward_countermodel(delta: float) -> RelativeSoninWardCountermodel:
    r"""Exact block showing that two moments and harmonicity do not suffice.

    Take a projection difference ``D`` with orthonormal eigenvectors ``t,s``
    and eigenvalues ``delta,-1``.  The ``s`` direction lies in an isometric
    reverse-Hankel/Sonin channel, while the positive eigenvalues ``delta_n``
    may come from compact two-dimensional rotation blocks with
    ``delta_n -> 0``.  Put ``epsilon=delta^2`` and

    ``u=A t+B s``, ``w=-B t+A s``,

    where ``A^2=(1+epsilon)/(1+delta)`` and
    ``B^2=(delta-epsilon)/(1+delta)``.  Then ``u,w`` are orthonormal, so for
    reference form ``h=I`` the vector ``w`` is exactly h-harmonic relative to
    ``old=span(u)``.  Both can lie in a fixed codimension-two moment kernel.
    Nevertheless

    ``D(u,u)=epsilon`` and
    ``|D(u,w)|^2=(1+epsilon)(delta-epsilon)``,

    so the Ward ratio is ``(1+delta^2)(1/delta-1) -> infinity``.  Duplicating
    the construction supplies reflection parity.  Thus one-sided compactness,
    reflection, two moments, bounded ``D-h``, and h-harmonicity still do not
    imply a uniform relative Ward theorem.
    """

    dd = float(delta)
    if not 0.0 < dd < 1.0:
        raise ValueError("delta must lie strictly between zero and one")
    epsilon = dd * dd
    a2 = (1.0 + epsilon) / (1.0 + dd)
    b2 = (dd - epsilon) / (1.0 + dd)
    cross_squared = (1.0 + epsilon) * (dd - epsilon)
    return RelativeSoninWardCountermodel(
        delta=dd,
        epsilon=epsilon,
        rotation_weight=a2,
        sonin_weight=b2,
        old_q_floor=epsilon,
        residual_cross_squared=cross_squared,
        ward_ratio=cross_squared / epsilon,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--epsilon", type=float, default=1.0e-8)
    parser.add_argument("--cyclic-order", type=int, default=31)
    args = parser.parse_args()

    mp.mp.dps = args.dps
    points = (mp.mpf("0"), mp.mpf("0.7"), mp.mpf("3.25"))
    normalization_errors = []
    unimodularity_errors = []
    for point in points:
        ratio = semilocal_ratio(point)
        direct = ratio_logarithmic_derivative(point)
        expected = semilocal_weil_multiplier(point)
        normalization_errors.append(abs(direct - expected))
        unimodularity_errors.append(abs(abs(ratio) - 1))

    n = args.cyclic_order
    projection = fourier_hardy_projection(n)
    phases = np.linspace(-1.2, 2.3, n)
    unitary = np.diag(np.exp(1j * phases))
    test = np.diag(1.0 + np.cos(np.linspace(0, 2 * np.pi, n, endpoint=False)))
    cyclic_trace = finite_trace_defect(projection, unitary, test)

    polar_order = semilocal_origin_pole_order((2, 3, 5))
    coefficients = origin_polar_hankel_sequence(polar_order, 40)
    polar_hankel = hankel_from_negative_coefficients(coefficients, 16)
    polar_rank = int(np.linalg.matrix_rank(polar_hankel, tol=1.0e-10))
    countermodel = smooth_quasi_inner_ward_countermodel(args.epsilon)
    relative_countermodel = relative_sonin_ward_countermodel(
        max(math.sqrt(args.epsilon), 1.0e-12)
    )

    print(json.dumps({
        "schema": "zeta23.semilocal-hankel-poisson-gate.v1",
        "status": "EXACT_NORMALIZATION_AND_METHOD_OBSTRUCTIONS",
        "max_unimodularity_error": mp.nstr(max(unimodularity_errors), 12),
        "max_log_derivative_error": mp.nstr(max(normalization_errors), 12),
        "finite_cyclic_trace_abs": f"{abs(cyclic_trace):.12e}",
        "semilocal_origin_pole_order": polar_order,
        "semilocal_origin_polar_hankel_rank": polar_rank,
        "completed_zeta_pole_form_rank": 2,
        "smooth_quasi_inner_countermodel": asdict(countermodel),
        "relative_sonin_countermodel": asdict(relative_countermodel),
    }, indent=2))


if __name__ == "__main__":
    main()
