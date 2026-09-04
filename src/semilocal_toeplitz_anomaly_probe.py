#!/usr/bin/env python3
"""Noncyclic Toeplitz reconstruction of the semilocal Weil anomaly.

This is a finite diagnostic for the two-moment relative Ward problem.  It
uses the Cayley map

    z = (t-i)/(t+i) = exp(i theta),   t = -cot(theta/2),

and the lower Hardy projection ``P e_n=e_n`` for ``n<=0``.  With this
orientation, for ``U(theta)=exp(i Theta(theta))`` the regularized diagonal of

    D_U = P-U^* P U

is ``Theta'(theta)`` with respect to normalized circle measure.  Hence

    Tr(M_g D_U) = (1/2pi) integral g(theta) Theta'(theta) dtheta
                = (1/2pi) integral g(t) m_F(t) dt.

The finite matrices below are *noncyclic*.  Fourier coefficients are put in
Laurent matrices and the sums defining the Hardy blocks are padded beyond the
reported central window.  In Hardy coordinates ``H_+=ran(P)`` and
``H_-=ran(1-P)``,

    D_U = [[c^*c, -a^*b], [-b^*a, -b^*b]].

This module reconstructs all four trace contributions on an actual relative
Ward extremizer.  It deliberately does not use an exactly unitary finite DFT
compression, which would erase the anomaly by finite trace cyclicity.

The FFT is only a quadrature for the Fourier coefficients of the continuum
symbols.  Sampling, central-window, and padding convergence must all be
checked before interpreting the block split.  Nothing here proves a
continuum Ward estimate, a zero-free strip, or RH.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from typing import Sequence

import mpmath as mp
import numpy as np
from scipy.linalg import eigh
from scipy.special import digamma, loggamma

from harmonic_schur_collar_probe import mixed_extension_forms
from semilocal_relative_ward_probe import (
    moment_matrix,
    relative_old_collar_coordinates,
)
from ward_source_extremizer_probe import literal_collar_geometry, pole_matrix


def _symmetrize(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.T.conj()) / 2


@dataclass(frozen=True)
class RelativeWardExtremizer:
    centers: np.ndarray
    widths: np.ndarray
    old_vector: np.ndarray
    harmonic_vector: np.ndarray
    direct_pairing: float
    ward_ratio: float
    denominator: float
    numerator: float
    old_floor: float
    parity: str
    moment_residual: float
    algebraic_pairing_error: float


def build_relative_ward_extremizer(
    old_degree: int = 40,
    collar_degree: int = 1,
    delta: float = 0.32,
    dps: int = 55,
    event_prime: int = 5,
) -> RelativeWardExtremizer:
    """Return the top pole-null Ward extremizer in physical hat coordinates.

    ``old_vector`` is ``A^{-1} B v`` on the old relative space and
    ``harmonic_vector`` is the reference-harmonic lift ``J_h v``.  Their
    pole-free Weil pairing is the Ward numerator.
    """

    delta_mp = mp.mpf(str(delta))
    q_mp, g_mp, h_mp, _, _ = mixed_extension_forms(
        old_degree=old_degree,
        collar_degree=collar_degree,
        delta=delta_mp,
        event_prime=event_prime,
        dps=dps,
    )
    centers_mp, widths_mp, _, _ = literal_collar_geometry(
        old_degree, collar_degree, delta_mp, event_prime
    )
    pole_mp = pole_matrix(centers_mp, widths_mp)

    q = np.asarray(q_mp.tolist(), dtype=float)
    g = np.asarray(g_mp.tolist(), dtype=float)
    h = np.asarray(h_mp.tolist(), dtype=float)
    pole = np.asarray(pole_mp.tolist(), dtype=float)
    centers = np.asarray([float(x) for x in centers_mp])
    widths = np.asarray([float(x) for x in widths_mp])
    moments = moment_matrix(centers_mp, widths_mp)
    coordinates, split, coordinate_checks = relative_old_collar_coordinates(
        g, moments, old_degree
    )

    gr = _symmetrize(coordinates.T @ g @ coordinates).real
    hr = _symmetrize(coordinates.T @ h @ coordinates).real
    qr = _symmetrize(coordinates.T @ (q - pole) @ coordinates).real
    a = qr[:split, :split]
    x = qr[:split, split:]
    ho = hr[:split, :split]
    hx = hr[:split, split:]
    correction = np.linalg.solve(ho, hx)
    residual_cross = x - a @ correction
    lift = np.vstack([-correction, np.eye(hr.shape[0] - split)])
    denominator_form = _symmetrize(lift.T @ gr @ lift).real
    response = _symmetrize(
        residual_cross.T @ np.linalg.solve(a, residual_cross)
    ).real

    eigenvalues, eigenvectors = eigh(response, denominator_form)
    collar_vector = eigenvectors[:, -1]
    denominator = float(collar_vector @ denominator_form @ collar_vector)
    collar_vector /= math.sqrt(denominator)
    denominator = float(collar_vector @ denominator_form @ collar_vector)
    old_coordinates = np.linalg.solve(a, residual_cross @ collar_vector)
    harmonic_coordinates = lift @ collar_vector

    old_vector = coordinates[:, :split] @ old_coordinates
    harmonic_vector = coordinates @ harmonic_coordinates
    direct_pairing = float(old_vector @ (q - pole) @ harmonic_vector)
    numerator = float(old_vector @ (q - pole) @ old_vector)
    response_numerator = float(collar_vector @ response @ collar_vector)
    old_floor = float(eigh(a, gr[:split, :split], eigvals_only=True)[0])

    old_slice = old_vector[:old_degree]
    reflection_old = np.linalg.norm(old_slice - old_slice[::-1])
    antireflection_old = np.linalg.norm(old_slice + old_slice[::-1])
    parity = "even" if reflection_old < antireflection_old else "odd"
    moment_residual = max(
        np.linalg.norm(moments @ old_vector),
        np.linalg.norm(moments @ harmonic_vector),
        coordinate_checks["moment_annihilation_error"],
    )
    algebraic_pairing_error = max(
        abs(direct_pairing - numerator),
        abs(direct_pairing - response_numerator),
    )
    return RelativeWardExtremizer(
        centers=centers,
        widths=widths,
        old_vector=old_vector,
        harmonic_vector=harmonic_vector,
        direct_pairing=direct_pairing,
        ward_ratio=float(eigenvalues[-1]),
        denominator=denominator,
        numerator=numerator,
        old_floor=old_floor,
        parity=parity,
        moment_residual=float(moment_residual),
        algebraic_pairing_error=float(algebraic_pairing_error),
    )


def triangular_hat_transform(
    t: np.ndarray, centers: np.ndarray, widths: np.ndarray, coefficients: np.ndarray
) -> np.ndarray:
    r"""Fourier transform of a linear combination of unit triangular hats.

    For ``hat_(c,d)(x)=max(1-|x-c|/d,0)``, the repository convention gives

        hat_hat_(c,d)(t) = d exp(-i c t) sinc(t d/2)^2,

    where NumPy's ``sinc(x)=sin(pi*x)/(pi*x)``.
    """

    tt = np.asarray(t, dtype=float)
    answer = np.zeros(tt.shape, dtype=np.complex128)
    for center, width, coefficient in zip(centers, widths, coefficients):
        profile = width * np.sinc(tt * width / (2 * np.pi)) ** 2
        answer += coefficient * profile * np.exp(-1j * center * tt)
    return answer


def cayley_midpoint_grid(sample_count: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return ``theta,t,dt/dtheta`` on a midpoint Cayley grid."""

    if sample_count < 16 or sample_count & (sample_count - 1):
        raise ValueError("sample_count must be a power of two at least 16")
    theta = 2 * np.pi * (np.arange(sample_count) + 0.5) / sample_count
    half = theta / 2
    t = -1 / np.tan(half)
    jacobian = 0.5 / np.sin(half) ** 2
    return theta, t, jacobian


def semilocal_ratio_vector(t: np.ndarray, primes: Sequence[int] = (2, 3, 5)) -> np.ndarray:
    """Vectorized ``rho_infinity prod rho_p`` in the paper orientation."""

    tt = np.asarray(t, dtype=float)
    z = 0.25 + 0.5j * tt
    # The log-gamma difference is purely imaginary on the critical line.
    log_ratio = -1j * tt * np.log(np.pi) + loggamma(z) - loggamma(np.conj(z))
    answer = np.exp(log_ratio)
    for prime in primes:
        phase = np.exp(1j * tt * np.log(prime))
        root = prime ** -0.5
        answer *= (1 - root * phase) / (1 - root / phase)
    return answer


def semilocal_multiplier_vector(
    t: np.ndarray, primes: Sequence[int] = (2, 3, 5)
) -> np.ndarray:
    """Vectorized pole-free Weil multiplier ``-i conjugate(u) u'``."""

    tt = np.asarray(t, dtype=float)
    answer = digamma(0.25 + 0.5j * tt).real - np.log(np.pi)
    for prime in primes:
        root = prime ** -0.5
        z = root * np.exp(-1j * tt * np.log(prime))
        answer += -2 * np.log(prime) * (z / (1 - z)).real
    return answer


def midpoint_fourier_coefficients(values: np.ndarray, max_mode: int) -> np.ndarray:
    """Return modes ``-max_mode,...,+max_mode`` from midpoint samples."""

    samples = np.asarray(values, dtype=np.complex128)
    count = samples.size
    if max_mode >= count // 2:
        raise ValueError("max_mode must be below the midpoint-grid Nyquist mode")
    transform = np.fft.fft(samples) / count
    modes = np.arange(-max_mode, max_mode + 1)
    # theta_j=2pi(j+1/2)/count contributes this half-grid phase.
    return transform[modes % count] * np.exp(-1j * np.pi * modes / count)


def _coefficients_at(coefficients: np.ndarray, max_mode: int, modes: np.ndarray) -> np.ndarray:
    if np.max(np.abs(modes)) > max_mode:
        raise ValueError("requested Laurent coefficient lies outside stored range")
    return coefficients[modes + max_mode]


def laurent_matrix(
    coefficients: np.ndarray,
    max_mode: int,
    rows: np.ndarray,
    columns: np.ndarray,
) -> np.ndarray:
    """Matrix ``M_f[i,j]=f_(i-j)`` on arbitrary noncyclic index sets."""

    modes = rows[:, None] - columns[None, :]
    return _coefficients_at(coefficients, max_mode, modes)


@dataclass(frozen=True)
class HardyTraceSplit:
    central_modes_per_side: int
    padding_modes_per_side: int
    plus_plus: complex
    plus_minus: complex
    minus_plus: complex
    minus_minus: complex
    total: complex
    c_frobenius_squared: float
    b_frobenius_squared: float


@dataclass(frozen=True)
class NoncyclicSectionTraceSplit:
    modes_per_side: int
    plus_plus: complex
    plus_minus: complex
    minus_plus: complex
    minus_minus: complex
    total: complex
    plus_plus_cstarc_trace: complex
    plus_boundary_trace: complex
    c_frobenius_squared: float
    b_frobenius_squared: float


def noncyclic_section_trace_split(
    u_coefficients: np.ndarray,
    g_coefficients: np.ndarray,
    max_mode: int,
    modes_per_side: int,
) -> NoncyclicSectionTraceSplit:
    r"""Trace ``G_L(P_L-U_L^*P_LU_L)`` on a Laurent finite section.

    Here ``U_L=E_L M_U E_L`` is Toeplitz, not made cyclic and not projected
    back to a unitary matrix.  Its boundary nonunitarity is retained.  This
    control can carry the anomaly, but also an outer-boundary bias; even a
    smooth zero-winding phase can retain such a bias as the section grows.

    The ``++`` block is ``I-a_L^*a_L``.  It is also reported as the sum of
    ``c_L^*c_L`` and the finite-section boundary remainder; replacing it by
    ``c_L^*c_L`` prematurely deletes precisely that remainder.
    """

    length = int(modes_per_side)
    if length < 1:
        raise ValueError("modes_per_side must be positive")
    plus = np.arange(-length + 1, 1)
    minus = np.arange(1, length + 1)
    a = laurent_matrix(u_coefficients, max_mode, plus, plus)
    b = laurent_matrix(u_coefficients, max_mode, plus, minus)
    c = laurent_matrix(u_coefficients, max_mode, minus, plus)

    d_pp = np.eye(length) - a.conj().T @ a
    d_pm = -(a.conj().T @ b)
    d_mp = -(b.conj().T @ a)
    d_mm = -(b.conj().T @ b)
    cstarc = c.conj().T @ c
    boundary = d_pp - cstarc

    g_pp = laurent_matrix(g_coefficients, max_mode, plus, plus)
    g_pm = laurent_matrix(g_coefficients, max_mode, plus, minus)
    g_mp = laurent_matrix(g_coefficients, max_mode, minus, plus)
    g_mm = laurent_matrix(g_coefficients, max_mode, minus, minus)

    pp = np.trace(g_pp @ d_pp)
    pm = np.trace(g_pm @ d_mp)
    mp_value = np.trace(g_mp @ d_pm)
    mm = np.trace(g_mm @ d_mm)
    c_trace = np.trace(g_pp @ cstarc)
    boundary_trace = np.trace(g_pp @ boundary)
    return NoncyclicSectionTraceSplit(
        modes_per_side=length,
        plus_plus=complex(pp),
        plus_minus=complex(pm),
        minus_plus=complex(mp_value),
        minus_minus=complex(mm),
        total=complex(pp + pm + mp_value + mm),
        plus_plus_cstarc_trace=complex(c_trace),
        plus_boundary_trace=complex(boundary_trace),
        c_frobenius_squared=float(np.linalg.norm(c, "fro") ** 2),
        b_frobenius_squared=float(np.linalg.norm(b, "fro") ** 2),
    )


def padded_hardy_trace_split(
    u_coefficients: np.ndarray,
    g_coefficients: np.ndarray,
    max_mode: int,
    central_modes: int,
    padding_modes: int,
) -> HardyTraceSplit:
    r"""Trace the four Hardy blocks on a central, noncyclic Laurent window.

    ``H_+`` is indexed by ``..., -2,-1,0`` and ``H_-`` by ``1,2,...``.
    The trace diagonal is restricted to ``central_modes`` modes on each side,
    but the intermediate index in ``M_gD`` and the Hardy leakage index inside
    ``D`` both range through ``padding_modes`` modes.  This distinction is
    essential: inserting the central projection between ``M_g`` and ``D``
    gives a different, generally nonconvergent conditional trace.
    """

    n, tail = int(central_modes), int(padding_modes)
    if n < 1 or tail < n:
        raise ValueError("require padding_modes >= central_modes >= 1")
    plus = np.arange(-n + 1, 1)
    minus = np.arange(1, n + 1)
    extended_plus = np.arange(-tail + 1, 1)
    extended_minus = np.arange(1, tail + 1)
    positive_output = np.arange(1, tail + 1)
    nonpositive_output = np.arange(-tail + 1, 1)

    c_extended = laurent_matrix(
        u_coefficients, max_mode, positive_output, extended_plus
    )
    c_central = laurent_matrix(u_coefficients, max_mode, positive_output, plus)
    a_extended = laurent_matrix(
        u_coefficients, max_mode, nonpositive_output, extended_plus
    )
    a_central = laurent_matrix(u_coefficients, max_mode, nonpositive_output, plus)
    b_extended = laurent_matrix(
        u_coefficients, max_mode, nonpositive_output, extended_minus
    )
    b_central = laurent_matrix(u_coefficients, max_mode, nonpositive_output, minus)

    # Rectangular blocks: rows are the padded intermediate index of M_g D;
    # columns are the central trace-diagonal index.
    d_pp = c_extended.conj().T @ c_central
    d_pm = -(a_extended.conj().T @ b_central)
    d_mp = -(b_extended.conj().T @ a_central)
    d_mm = -(b_extended.conj().T @ b_central)

    g_pp = laurent_matrix(g_coefficients, max_mode, plus, extended_plus)
    g_pm = laurent_matrix(g_coefficients, max_mode, plus, extended_minus)
    g_mp = laurent_matrix(g_coefficients, max_mode, minus, extended_plus)
    g_mm = laurent_matrix(g_coefficients, max_mode, minus, extended_minus)

    pp = np.trace(g_pp @ d_pp)
    pm = np.trace(g_pm @ d_mp)
    mp_value = np.trace(g_mp @ d_pm)
    mm = np.trace(g_mm @ d_mm)
    total = pp + pm + mp_value + mm
    return HardyTraceSplit(
        central_modes_per_side=n,
        padding_modes_per_side=tail,
        plus_plus=complex(pp),
        plus_minus=complex(pm),
        minus_plus=complex(mp_value),
        minus_minus=complex(mm),
        total=complex(total),
        c_frobenius_squared=float(np.linalg.norm(c_central, "fro") ** 2),
        b_frobenius_squared=float(np.linalg.norm(b_central, "fro") ** 2),
    )


def _complex_json(value: complex) -> dict[str, float]:
    return {"real": float(value.real), "imag": float(value.imag)}


def run_probe(
    sample_count: int = 1 << 18,
    central_modes: Sequence[int] = (8, 16, 32, 64),
    padding_factors: Sequence[int] = (2, 4, 8),
    old_degree: int = 40,
    collar_degree: int = 1,
    delta: float = 0.32,
    dps: int = 55,
) -> dict:
    """Run sampling, Cayley-Jacobian, and padded Hardy-block diagnostics."""

    extremizer = build_relative_ward_extremizer(
        old_degree=old_degree,
        collar_degree=collar_degree,
        delta=delta,
        dps=dps,
    )
    theta, t, jacobian = cayley_midpoint_grid(sample_count)
    u_symbol = semilocal_ratio_vector(t)
    old_hat = triangular_hat_transform(
        t, extremizer.centers, extremizer.widths, extremizer.old_vector
    )
    harmonic_hat = triangular_hat_transform(
        t, extremizer.centers, extremizer.widths, extremizer.harmonic_vector
    )
    g_symbol = old_hat * np.conj(harmonic_hat)
    multiplier = semilocal_multiplier_vector(t)
    circle_direct = np.mean(g_symbol * multiplier * jacobian)

    maximum_central = max(int(x) for x in central_modes)
    maximum_padding = maximum_central * max(int(x) for x in padding_factors)
    # A Hardy-output index and a padded intermediate index can lie at
    # opposite ends, requiring Laurent modes almost 2*maximum_padding.
    maximum_mode = 2 * maximum_padding
    u_coefficients = midpoint_fourier_coefficients(u_symbol, maximum_mode)
    g_coefficients = midpoint_fourier_coefficients(g_symbol, maximum_mode)

    section_rows = []
    # Control diagnostic: a square noncyclic Laurent section.  It exposes the
    # outer-boundary remainder but is not assumed to be the continuum trace.
    for n in central_modes:
        split = noncyclic_section_trace_split(
            u_coefficients, g_coefficients, maximum_mode, int(n)
        )
        absolute_block_sum = (
            abs(split.plus_plus)
            + abs(split.plus_minus)
            + abs(split.minus_plus)
            + abs(split.minus_minus)
        )
        section_rows.append(
            {
                "modes_per_side": split.modes_per_side,
                "plus_plus": _complex_json(split.plus_plus),
                "plus_plus_cstarc_part": _complex_json(
                    split.plus_plus_cstarc_trace
                ),
                "plus_plus_boundary_nonunitarity_part": _complex_json(
                    split.plus_boundary_trace
                ),
                "plus_minus": _complex_json(split.plus_minus),
                "minus_plus": _complex_json(split.minus_plus),
                "minus_minus_minus_bstarb": _complex_json(split.minus_minus),
                "total": _complex_json(split.total),
                "absolute_error_vs_xspace": abs(
                    split.total - extremizer.direct_pairing
                ),
                "absolute_error_vs_circle_quadrature": abs(
                    split.total - circle_direct
                ),
                "c_frobenius_squared": split.c_frobenius_squared,
                "b_frobenius_squared": split.b_frobenius_squared,
                "sonin_fraction_of_absolute_block_sum": abs(split.minus_minus)
                / max(absolute_block_sum, np.finfo(float).tiny),
            }
        )

    interior_rows = []
    for n in central_modes:
        for factor in padding_factors:
            split = padded_hardy_trace_split(
                u_coefficients,
                g_coefficients,
                maximum_mode,
                int(n),
                int(n) * int(factor),
            )
            interior_rows.append(
                {
                    "central_modes_per_side": split.central_modes_per_side,
                    "padding_modes_per_side": split.padding_modes_per_side,
                    "padding_factor": int(factor),
                    "plus_plus_cstarc": _complex_json(split.plus_plus),
                    "plus_minus": _complex_json(split.plus_minus),
                    "minus_plus": _complex_json(split.minus_plus),
                    "minus_minus_minus_bstarb": _complex_json(split.minus_minus),
                    "total": _complex_json(split.total),
                    "absolute_error_vs_xspace": abs(
                        split.total - extremizer.direct_pairing
                    ),
                    "absolute_error_vs_circle_quadrature": abs(
                        split.total - circle_direct
                    ),
                    "c_frobenius_squared": split.c_frobenius_squared,
                    "b_frobenius_squared": split.b_frobenius_squared,
                    "sonin_fraction_of_absolute_block_sum": abs(split.minus_minus)
                    / max(
                        abs(split.plus_plus)
                        + abs(split.plus_minus)
                        + abs(split.minus_plus)
                        + abs(split.minus_minus),
                        np.finfo(float).tiny,
                    ),
                }
            )

    return {
        "schema": "zeta23.semilocal-toeplitz-anomaly-probe.v1",
        "status": "FLOATING_NONCYCLIC_FINITE_DIAGNOSTIC_NOT_A_THEOREM",
        "conventions": {
            "fourier": "fhat(t)=integral f(x) exp(-i t x) dx",
            "cayley": "z=(t-i)/(t+i)=exp(i theta), t=-cot(theta/2)",
            "jacobian": "dt/dtheta=(1+t^2)/2",
            "hardy_plus": "span{z^n:n<=0}",
            "defect": "D=P-U^*PU",
            "laurent": "M_f[row,column]=f_hat[row-column]",
            "trace_target": "mean_theta(g Theta')=(1/2pi) integral_R g(t)m_F(t)dt",
        },
        "case": {
            "old_degree": old_degree,
            "collar_degree_per_side": collar_degree,
            "delta": delta,
            "sample_count": sample_count,
            "dps_for_xspace_assembly": dps,
            "parity": extremizer.parity,
            "old_floor": extremizer.old_floor,
            "ward_ratio": extremizer.ward_ratio,
            "moment_residual": extremizer.moment_residual,
            "algebraic_pairing_error": extremizer.algebraic_pairing_error,
        },
        "reference_values": {
            "xspace_direct_pairing": extremizer.direct_pairing,
            "ward_numerator": extremizer.numerator,
            "ward_denominator": extremizer.denominator,
            "circle_jacobian_quadrature": _complex_json(complex(circle_direct)),
            "circle_vs_xspace_absolute_error": abs(
                circle_direct - extremizer.direct_pairing
            ),
            "u_unimodularity_error": float(
                np.max(np.abs(np.abs(u_symbol) - 1))
            ),
        },
        "noncyclic_section_rows": section_rows,
        "interior_padded_rows": interior_rows,
    }


def _integer_list(text: str) -> list[int]:
    return [int(item) for item in text.split(",") if item]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sample-power", type=int, default=18)
    parser.add_argument("--central-modes", default="8,16,32,64")
    parser.add_argument("--padding-factors", default="2,4,8")
    parser.add_argument("--old-degree", type=int, default=40)
    parser.add_argument("--collar-degree", type=int, default=1)
    parser.add_argument("--delta", type=float, default=0.32)
    parser.add_argument("--dps", type=int, default=55)
    args = parser.parse_args()
    payload = run_probe(
        sample_count=1 << args.sample_power,
        central_modes=_integer_list(args.central_modes),
        padding_factors=_integer_list(args.padding_factors),
        old_degree=args.old_degree,
        collar_degree=args.collar_degree,
        delta=args.delta,
        dps=args.dps,
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
