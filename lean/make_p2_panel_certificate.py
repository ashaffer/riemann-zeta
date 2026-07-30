#!/usr/bin/env python3
"""Exact-rational scout for the canonical p=2 matrix containment.

This program mirrors the finite approximants in the following Lean modules:

* ``RHBridge.P2DefectApprox``;
* ``RHBridge.P2DigammaPrefix``;
* ``RHBridge.P2SphericalReal``; and
* ``RHBridge.P2PoleApprox``.

It is deliberately *not* a numerical quadrature program.  All polynomial
coefficients, panel integrals, matrix centers, and error bounds are computed
with FLINT rationals.  Irrational square roots enter only through the decimal
centers proved in ``P2ScaleCenters``.  By default the canonical local
polynomials are integrated without coefficient rounding.  An optional older
fixed-grid mode remains available as a faster independent scout.

The default panel layout is

  [0,1/4], four equal panels on every octave through 32,
  [32,38], [38,44], [44,50].

The script compares all 600 upper-triangular parity entries with the exact
centers stored in ``FullInfClipped48.lean``.  A successful scout can emit a
compact Lean data module containing the final rational centers and a common
outward analytic radius.  That data is only an input to a later Lean proof;
the script itself is not trusted by the theorem.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import comb, factorial
import multiprocessing
from pathlib import Path
import re
import sys
from typing import Iterable

from flint import fmpq, fmpq_poly

sys.set_int_max_str_digits(3_000_000)


ROOT = Path(__file__).resolve().parent.parent
STORED_LEAN = ROOT / "lean" / "weilcert" / "FullInfClipped48.lean"
SCALE_CENTERS_LEAN = ROOT / "lean" / "rhbridge" / "RHBridge" / "P2ScaleCenters.lean"

BLOCK = 24
MODES = 48
PANELS = 32
PREFIX_TERMS = 64
GEOMETRIC_TERMS = 32
SPHERICAL_TERMS = 100

# Rounding grids.  These are exact integers, not requested decimal precision
# settings.  The polynomial grid is intentionally shared by every panel.
POLY_DEN = 10**40
FINAL_DEN = 10**30
PANEL_INTEGRAL_DEN = 10**40
ROUNDED_FACTOR_DEN = 10**40
ROUNDED_OUTER_DEN = 10**220
ROUNDED_OUTER_TAIL = Fraction(1, 10**22)

STORED_DEN = 10**18
STORED_RADIUS = Fraction(1, 10**12)
BETA = Fraction(227, 10**7)

ALPHA_CENTER = Fraction(10938711277167, 10**13)
ALPHA_RADIUS = Fraction(1, 10**13)

# Twice the already-certified `p2InvTwoPiCenter`.  Sharing this exact center
# with `P2EntryError` makes the generated aggregate sums plug into its
# normalization lemma without a second numerical constant bridge.
INV_PI_CENTER = 2 * Fraction(15915494309189533576, 10**20)
INV_PI_RADIUS = Fraction(2, 10**20)

# The Lean consumer uses the deliberately coarse uniform panel estimate from
# `P2PanelPartition`, rather than trusting the sharper modewise scout ledger.
# This simple radius covers alpha, normalized-band, pole, aggregate-panel
# rounding, and final-center rounding errors with comfortable slack.
EMITTED_ANALYTIC_RADIUS = Fraction(5, 10**13)

DEFECT_ANALYTIC_ERROR = Fraction(2, 10**14)
DEFECT_ABS_BOUND = Fraction(7447, 1000)
SPHERICAL_UNIFORM_ERROR = Fraction(1, 10**19)
SCALE_RADIUS = Fraction(1, 10**20)

LOG_TWO_CENTER = Fraction(69314718055994535, 10**17)
PRIME_AMPLITUDE_CENTER = Fraction(9802581434685475, 10**16)

TAIL_CENTERS = {
    3: Fraction(12302203694272605164, 10**23),
    5: Fraction(1513318071016888708, 10**26),
    7: Fraction(248187933250395478, 10**29),
    9: Fraction(457876177281654, 10**30),
    11: Fraction(9009664018164, 10**32),
    13: Fraction(1846555525330, 10**35),
    15: Fraction(389237872480, 10**38),
    17: Fraction(83750453653, 10**41),
    19: Fraction(18304725494, 10**44),
    21: Fraction(4050409104, 10**47),
    23: Fraction(905240534, 10**50),
    25: Fraction(203984837, 10**53),
    27: Fraction(46283155, 10**56),
    29: Fraction(10563071, 10**59),
    31: Fraction(2422946, 10**62),
}


def fq(q: Fraction | int) -> fmpq:
    """Convert a Python exact rational to a FLINT exact rational."""
    if isinstance(q, int):
        return fmpq(q)
    return fmpq(q.numerator, q.denominator)


def frac(q: fmpq) -> Fraction:
    """Convert a FLINT exact rational to a Python exact rational."""
    return Fraction(int(q.p), int(q.q))


def round_scaled(q: Fraction, denominator: int) -> int:
    """Nearest integer to ``q * denominator``, ties away from zero."""
    numerator = q.numerator * denominator
    divisor = q.denominator
    if numerator >= 0:
        return (2 * numerator + divisor) // (2 * divisor)
    return -((2 * (-numerator) + divisor) // (2 * divisor))


def ceil_scaled(q: Fraction, denominator: int) -> int:
    """Smallest integer ``n`` with ``q <= n / denominator``."""
    assert q >= 0
    numerator = q.numerator * denominator
    return (numerator + q.denominator - 1) // q.denominator


def floor_scaled(q: Fraction, denominator: int) -> int:
    """Largest integer ``n`` with ``n / denominator <= q``."""
    return (q.numerator * denominator) // q.denominator


def decimal(q: Fraction, digits: int = 8) -> str:
    """Scientific notation used only for human-readable reporting."""
    return f"{float(q):.{digits}e}"


def outward_decimal_fraction(q: Fraction, denominator: int = FINAL_DEN) -> Fraction:
    """A compact exact rational upper bound suitable for a printed ledger."""
    return Fraction(ceil_scaled(q, denominator), denominator)


def poly_comp_linear(poly: fmpq_poly, center: Fraction, half_width: Fraction) -> fmpq_poly:
    """Return the exact polynomial ``poly(center + half_width*t)``."""
    linear = fmpq_poly([fq(center), fq(half_width)])
    result = fmpq_poly()
    for coefficient in reversed(poly.coeffs()):
        result = result * linear + coefficient
    return result


def rounded_poly(poly: fmpq_poly, denominator: int = POLY_DEN) -> tuple[fmpq_poly, Fraction]:
    """Round every coefficient to a common grid and return an l1 error.

    On ``|t| <= 1``, the returned error bounds the evaluation difference.
    The proof is simply the triangle inequality, with at most half a grid
    unit per coefficient.
    """
    if not poly:
        return fmpq_poly(), Fraction(0)
    coefficients = []
    for coefficient in poly.coeffs():
        integer = round_scaled(frac(coefficient), denominator)
        coefficients.append(fmpq(integer, denominator))
    rounded = fmpq_poly(coefficients)
    # Count the full degree range.  This remains valid even when leading
    # coefficients happen to round to zero.
    error = Fraction(poly.degree() + 1, 2 * denominator)
    return rounded, error


def exact_integral_minus_one_one(poly: fmpq_poly) -> Fraction:
    """Exact integral over [-1,1]."""
    return frac(exact_integral_minus_one_one_q(poly))


def exact_integral_minus_one_one_q(poly: fmpq_poly) -> fmpq:
    """FLINT-rational form of the exact integral over [-1,1]."""
    antiderivative = poly.integral()
    return antiderivative(fmpq(1)) - antiderivative(fmpq(-1))


def panels() -> list[tuple[Fraction, Fraction]]:
    """Return ``(center, half_width)`` pairs covering [0,50]."""
    endpoints = [Fraction(0), Fraction(1, 4)]
    left = Fraction(1, 4)
    while left < 32:
        right = 2 * left
        step = (right - left) / 4
        endpoints.extend(left + k * step for k in range(1, 5))
        left = right
    endpoints.extend([Fraction(38), Fraction(44), Fraction(50)])
    assert endpoints[0] == 0 and endpoints[-1] == 50
    assert all(a < b for a, b in zip(endpoints, endpoints[1:]))
    assert len(endpoints) == 33
    return [((a + b) / 2, (b - a) / 2) for a, b in zip(endpoints, endpoints[1:])]


def weight_moment(n: int, m: int) -> Fraction:
    """The exact ``weightMoment n m`` from ``P2SphericalApprox``."""
    result = Fraction(0)
    for ell in range(n + 1):
        power = m + 2 * (n - ell) + 1
        endpoint_difference = 1 - (-1) ** power
        result += (
            (-1) ** (ell + n)
            * comb(n, ell)
            * Fraction(endpoint_difference, power)
        )
    return result


def spherical_j_polynomial(n: int) -> fmpq_poly:
    """Exact ``sphericalJRealPolynomial n 100`` before 7/16 dilation."""
    coefficients = [fmpq(0) for _ in range(n + SPHERICAL_TERMS)]
    base = Fraction(1, 2 ** (n + 1) * factorial(n))
    for m in range(SPHERICAL_TERMS):
        # (I^m).re is zero for odd m and (-1)^(m/2) for even m.
        if m % 2:
            continue
        coefficient = (
            base
            * (-1) ** (m // 2)
            * weight_moment(n, m)
            / factorial(m)
        )
        coefficients[n + m] = fq(coefficient)
    return fmpq_poly(coefficients)


def spherical_global_polynomial(n: int) -> fmpq_poly:
    """Exact ``p2SphericalRealPolynomial n 100`` over the rationals."""
    outer = spherical_j_polynomial(n)
    return poly_comp_linear(outer, Fraction(0), Fraction(7, 16))


def spherical_analytic_error(n: int) -> Fraction:
    """Exact RHS of ``abs_p2SphericalReal_sub_polynomial_le``."""
    z_bound = Fraction(175, 8)
    return Fraction(2) * z_bound ** (n + SPHERICAL_TERMS) / (
        2**n * factorial(n) * factorial(SPHERICAL_TERMS)
    )


def parse_scale_centers() -> list[Fraction]:
    """Read the kernel-checked centers from ``P2ScaleCenters.lean``."""
    text = SCALE_CENTERS_LEAN.read_text(encoding="utf-8")
    start = text.index("def p2ScaleCenterQ")
    end = text.index("\n\nnoncomputable def p2ScaleCenter", start)
    body = text[start:end]
    matches = re.findall(
        r"^\s*\|\s*(\d+)\s*=>\s*(-?\d+)\s*/\s*10\s*\^\s*20\s*$",
        body,
        re.MULTILINE,
    )
    centers: list[Fraction | None] = [None] * MODES
    for mode_text, numerator_text in matches:
        mode = int(mode_text)
        if mode < MODES:
            centers[mode] = Fraction(int(numerator_text), 10**20)
    if any(center is None for center in centers):
        raise RuntimeError("failed to parse all 48 p2ScaleCenter cases")
    return [center for center in centers if center is not None]


def nonprefix_global_polynomial() -> fmpq_poly:
    """Exact ``p2RationalNonPrefixPoly`` over the rationals."""
    degree = 127
    coefficients = [Fraction(0) for _ in range(degree + 1)]

    # Rationalized accelerated tail.
    for k in range(1, 16):
        tail = TAIL_CENTERS[2 * k + 1]
        sign = (-1) ** k
        coefficients[0] += sign * 625**k * tail
        coefficients[2 * k] -= sign * tail / 2 ** (2 * k)

    # amplitude * (1 - cosTaylor 128 (r * logCenter)).  The degree-zero
    # coefficient cancels exactly.
    for m in range(2, 128, 2):
        cosine_coefficient = (-1) ** (m // 2) * LOG_TWO_CENTER**m / factorial(m)
        coefficients[m] -= PRIME_AMPLITUDE_CENTER * cosine_coefficient

    return fmpq_poly([fq(q) for q in coefficients])


def prefix_panel_polynomial(
    center: Fraction, half_width: Fraction
) -> tuple[fmpq_poly, Fraction, Fraction, list[fmpq_poly]]:
    """Exact degree-62 reciprocal polynomial and its uniform tail error.

    The final returned value is the maximum panel rho, useful for diagnostics.
    """
    variable = fmpq_poly([0, 1])
    polynomial = fmpq_poly()
    total_error = Fraction(0)
    maximum_rho = Fraction(0)
    terms: list[fmpq_poly] = []
    for n in range(PREFIX_TERMS):
        a = Fraction(n) + Fraction(1, 4)
        denominator = a * a + (center / 2) ** 2
        q = (
            fq(center * half_width / (2 * denominator)) * variable
            + fq(half_width * half_width / (4 * denominator)) * variable**2
        )
        geometric = fmpq_poly()
        power = fmpq_poly([1])
        for _ in range(GEOMETRIC_TERMS):
            geometric += power
            power *= -q
        term = fq(a / (a * a + 625)) - fq(a / denominator) * geometric
        terms.append(term)
        polynomial += term

        rho = center * half_width / (2 * denominator) + half_width * half_width / (4 * denominator)
        assert 0 <= rho < 1
        maximum_rho = max(maximum_rho, rho)
        total_error += a / denominator * rho**GEOMETRIC_TERMS / (1 - rho)
    return polynomial, total_error, maximum_rho, terms


def pole_rational_core(n: int) -> Fraction:
    """Exact ``p2PoleTaylorRationalCore n``."""
    exponential = fmpq_poly(
        [fq(Fraction(7, 32) ** k / factorial(k)) for k in range(48)]
    )
    legendre = fmpq_poly.legendre_p(n)
    return exact_integral_minus_one_one(exponential * legendre)


@dataclass(frozen=True)
class ModeData:
    mode: int
    scale_lower: Fraction
    scale_center: Fraction
    scale_radius: Fraction
    scale_upper: Fraction
    spherical_error: Fraction
    pole_core: Fraction
    pole_center: Fraction
    pole_error: Fraction


@dataclass
class PanelData:
    center: Fraction
    half_width: Fraction
    defect_poly: fmpq_poly
    defect_error: Fraction
    prefix_error: Fraction
    coefficient_error: Fraction
    max_rho: Fraction
    prefix_term_polys: list[fmpq_poly]
    nonprefix_poly: fmpq_poly
    component_polys: list[fmpq_poly]
    component_errors: list[Fraction]


@dataclass(frozen=True)
class EntryResult:
    block: str
    row: int
    col: int
    rounded_center: Fraction
    center_rounding_error: Fraction
    stored_center: Fraction
    discrepancy: Fraction
    band_error: Fraction
    pole_error: Fraction
    analytic_error: Fraction
    total_required_radius: Fraction
    panel_integral_numerators: tuple[int, ...]


_WORKER_MODE_DATA: list[ModeData] | None = None
_WORKER_PANEL_DATA: list[PanelData] | None = None


def build_mode_data() -> list[ModeData]:
    scale_centers = parse_scale_centers()
    result = []
    for n in range(MODES):
        center = scale_centers[n]
        radius = SCALE_RADIUS
        lower = center - radius
        upper = center + radius
        assert lower > 0
        # The sharper modewise factorial value is useful as an independent
        # generator sanity check, while the emitted ledger deliberately uses
        # the existing uniform Lean theorem at 1e-19.
        assert spherical_analytic_error(n) < SPHERICAL_UNIFORM_ERROR
        spherical_error = SPHERICAL_UNIFORM_ERROR
        core = pole_rational_core(n)

        # sqrt(7(2n+1)/32) is exactly half the spherical scale.  Reusing the
        # same Lean table avoids a second generated square-root certificate.
        pole_center = center / 2 * core
        # P2PoleApprox gives 1e-30 for the exponential/Taylor replacement.
        pole_error = Fraction(1, 10**30) + abs(core) * radius / 2
        result.append(
            ModeData(
                n,
                lower,
                center,
                radius,
                upper,
                spherical_error,
                core,
                pole_center,
                pole_error,
            )
        )
    return result


def build_panel_data(
    mode_data: list[ModeData], *, round_local_polynomials: bool = False
) -> list[PanelData]:
    spherical_globals = [spherical_global_polynomial(n) for n in range(MODES)]
    nonprefix = nonprefix_global_polynomial()
    result = []

    for panel_number, (center, half_width) in enumerate(panels()):
        prefix, prefix_error, max_rho, prefix_terms = prefix_panel_polynomial(
            center, half_width
        )
        local_nonprefix = poly_comp_linear(nonprefix, center, half_width)
        exact_defect = prefix + local_nonprefix
        if round_local_polynomials:
            defect_poly, coefficient_error = rounded_poly(exact_defect)
        else:
            defect_poly, coefficient_error = exact_defect, Fraction(0)
        defect_error = DEFECT_ANALYTIC_ERROR + prefix_error + coefficient_error

        component_polys = []
        component_errors = []
        for n, mode in enumerate(mode_data):
            local_spherical = poly_comp_linear(spherical_globals[n], center, half_width)
            exact_center_component = fq(mode.scale_center) * local_spherical
            if round_local_polynomials:
                component_poly, component_rounding = rounded_poly(exact_center_component)
            else:
                component_poly, component_rounding = exact_center_component, Fraction(0)

            # This is exactly `p2SelectedComponent100PanelError` from
            # P2PanelComposition, followed by coefficientwise rounding:
            #   eps*es + eps*(2+es) + |q|*es.
            component_error = (
                mode.scale_radius * mode.spherical_error
                + mode.scale_radius * (2 + mode.spherical_error)
                + abs(mode.scale_center) * mode.spherical_error
                + component_rounding
            )
            component_polys.append(component_poly)
            component_errors.append(component_error)

        result.append(
            PanelData(
                center,
                half_width,
                defect_poly,
                defect_error,
                prefix_error,
                coefficient_error,
                max_rho,
                prefix_terms,
                local_nonprefix,
                component_polys,
                component_errors,
            )
        )
        left = center - half_width
        right = center + half_width
        print(
            f"panel {panel_number + 1:02d}/32 [{left},{right}]: "
            f"rho={decimal(max_rho, 4)}, prefix_err={decimal(prefix_error, 3)}, "
            f"defect_degree={defect_poly.degree()}",
            flush=True,
        )
    return result


def parse_stored_centers() -> dict[str, list[list[Fraction]]]:
    text = STORED_LEAN.read_text(encoding="utf-8")
    result: dict[str, list[list[Fraction]]] = {}
    for block in ("even", "odd"):
        start = text.index(f"def {block}AFun")
        end = text.index("\ndef ", start + 5)
        body = text[start:end]
        table = [[Fraction(0) for _ in range(BLOCK)] for _ in range(BLOCK)]
        matches = re.findall(r"^\s*\|\s*(\d+),\s*(\d+)\s*=>\s*(-?\d+)\s*$", body, re.MULTILINE)
        if len(matches) != BLOCK * BLOCK:
            raise RuntimeError(f"parsed {len(matches)} entries from {block}AFun")
        for row_text, col_text, value_text in matches:
            row, col, value = int(row_text), int(col_text), int(value_text)
            table[row][col] = Fraction(value, STORED_DEN) + (BETA if row == col else 0)
        result[block] = table
    return result


def pole_product_error(first: ModeData, second: ModeData) -> Fraction:
    """Error in twice the product of two rational pole centers."""
    # Both true coefficients have absolute value <= 1.  If |c-q|<=e, then
    # |c1*c2-q1*q2| <= e1 + (1+e1)e2.
    return 2 * (first.pole_error + (1 + first.pole_error) * second.pole_error)


def integrate_entry(
    first_mode: int,
    second_mode: int,
    panel_data: list[PanelData],
) -> tuple[Fraction, Fraction, tuple[int, ...]]:
    """Return the exact rational band center and its analytic error."""
    integral_center = Fraction(0)
    integral_error = Fraction(0)
    panel_integral_numerators: list[int] = []

    for panel in panel_data:
        product_poly = (
            panel.defect_poly
            * panel.component_polys[first_mode]
            * panel.component_polys[second_mode]
        )
        panel_center_exact = fq(panel.half_width) * exact_integral_minus_one_one_q(product_poly)
        panel_center_integer = round_scaled(frac(panel_center_exact), PANEL_INTEGRAL_DEN)
        panel_integral_numerators.append(panel_center_integer)
        integral_center += Fraction(panel_center_integer, PANEL_INTEGRAL_DEN)

        first_error = panel.component_errors[first_mode]
        second_error = panel.component_errors[second_mode]
        first_bound = 1 + first_error
        second_bound = 1 + second_error
        defect_bound = DEFECT_ABS_BOUND + panel.defect_error
        # These are literally `panelPairError` and `panelTripleError` from
        # P2PanelComposition, so the generated rational ledger can instantiate
        # that theorem without a second bespoke error inequality.
        component_product_error = (
            first_error * second_error
            + first_error * second_bound
            + first_bound * second_error
        )
        integrand_error = (
            panel.defect_error * component_product_error
            + panel.defect_error * (first_bound * second_bound)
            + defect_bound * component_product_error
        )
        # Outward rounding here prevents irrelevant denominator growth in the
        # error ledger.  It does not round the polynomial integral or center.
        integral_error += outward_decimal_fraction(
            2 * panel.half_width * integrand_error
        )

    # The exact positive-half band integral has absolute value at most
    # 50 * 7.447 because each exact Fourier component is bounded by one.
    exact_integral_bound = 50 * DEFECT_ABS_BOUND
    # Each exact canonical panel integral was rounded only after exact FLINT
    # integration.  The common panel grid makes the subsequent Lean table and
    # arithmetic predicates tractable while costing only 16e-40 in total.
    panel_integral_rounding_error = Fraction(len(panel_data), 2 * PANEL_INTEGRAL_DEN)
    band_center = INV_PI_CENTER * integral_center
    band_error = (
        INV_PI_RADIUS * exact_integral_bound
        + INV_PI_CENTER * (integral_error + panel_integral_rounding_error)
    )
    return band_center, band_error, tuple(panel_integral_numerators)


def compute_entry_task(task: tuple[str, int, int, Fraction]) -> EntryResult:
    """Worker entry point; large exact polynomials stay inherited by fork."""
    block, row, col, stored_center = task
    assert _WORKER_MODE_DATA is not None and _WORKER_PANEL_DATA is not None
    mode_data = _WORKER_MODE_DATA
    panel_data = _WORKER_PANEL_DATA
    parity = 0 if block == "even" else 1
    first_mode = 2 * row + parity
    second_mode = 2 * col + parity
    phase = (-1) ** (row + col)
    band_center, band_error, panel_integral_numerators = integrate_entry(
        first_mode, second_mode, panel_data
    )
    band_center *= phase
    panel_integral_numerators = tuple(
        phase * numerator for numerator in panel_integral_numerators
    )

    first = mode_data[first_mode]
    second = mode_data[second_mode]
    pole_center = 2 * first.pole_center * second.pole_center
    if block == "odd":
        pole_center = -pole_center
    pole_error = pole_product_error(first, second)

    generated = band_center + pole_center
    if row == col:
        generated += ALPHA_CENTER
    rounded_integer = round_scaled(generated, FINAL_DEN)
    rounded = Fraction(rounded_integer, FINAL_DEN)
    actual_center_rounding_error = abs(generated - rounded)
    center_rounding_error = Fraction(1, 2 * FINAL_DEN)
    assert actual_center_rounding_error <= center_rounding_error

    analytic_error = band_error + pole_error + (
        ALPHA_RADIUS if row == col else 0
    )
    discrepancy = abs(rounded - stored_center)
    total_required_radius = discrepancy + center_rounding_error + analytic_error
    return EntryResult(
        block,
        row,
        col,
        rounded,
        center_rounding_error,
        stored_center,
        discrepancy,
        band_error,
        pole_error,
        analytic_error,
        total_required_radius,
        panel_integral_numerators,
    )


def build_entries(
    mode_data: list[ModeData], panel_data: list[PanelData], workers: int
) -> list[EntryResult]:
    stored = parse_stored_centers()
    tasks = [
        (block, row, col, stored[block][row][col])
        for block in ("even", "odd")
        for row in range(BLOCK)
        for col in range(row, BLOCK)
    ]
    global _WORKER_MODE_DATA, _WORKER_PANEL_DATA
    _WORKER_MODE_DATA = mode_data
    _WORKER_PANEL_DATA = panel_data
    entries: list[EntryResult] = []
    if workers == 1:
        iterator = map(compute_entry_task, tasks)
        for completed, entry in enumerate(iterator, 1):
            entries.append(entry)
            if completed % 50 == 0:
                print(f"  entries {completed:03d}/600 integrated", flush=True)
    else:
        # FLINT computations occur in independent processes.  `fork` keeps
        # the large immutable panel-polynomial table copy-on-write.
        context = multiprocessing.get_context("fork")
        with context.Pool(processes=workers) as pool:
            iterator = pool.imap_unordered(compute_entry_task, tasks, chunksize=1)
            for completed, entry in enumerate(iterator, 1):
                entries.append(entry)
                if completed % 50 == 0:
                    print(f"  entries {completed:03d}/600 integrated", flush=True)
    entries.sort(key=lambda entry: (entry.block, entry.row, entry.col))
    assert len(entries) == 600
    return entries


def lean_int_function(name: str, values: Iterable[tuple[tuple[int, ...], int]]) -> str:
    lines = [f"def {name} : Nat → Nat → Int"]
    for (row, col), value in values:
        lines.append(f"  | {row}, {col} => {value}")
    lines.append("  | _, _ => 0")
    return "\n".join(lines)


def lean_int_panel_functions(
    name: str, values: Iterable[tuple[tuple[int, ...], int]]
) -> str:
    """Emit 32 small functions instead of one quadratic-size pattern matcher."""
    grouped: list[list[tuple[int, int, int]]] = [[] for _ in range(32)]
    for (panel, row, col), value in values:
        grouped[panel].append((row, col, value))
    chunks = []
    for panel, panel_values in enumerate(grouped):
        lines = [f"def {name}Panel{panel} : Nat → Nat → Int"]
        for row, col, value in panel_values:
            lines.append(f"  | {row}, {col} => {value}")
        lines.append("  | _, _ => 0")
        chunks.append("\n".join(lines))
    dispatcher = [f"def {name} : Nat → Nat → Nat → Int"]
    for panel in range(32):
        dispatcher.append(
            f"  | {panel}, row, col => {name}Panel{panel} row col"
        )
    dispatcher.append("  | _, _, _ => 0")
    chunks.append("\n".join(dispatcher))
    return "\n\n".join(chunks)


def lean_int_function2_nonzero(
    name: str, values: Iterable[tuple[tuple[int, int], int]]
) -> str:
    """A small sparse two-dimensional integer table."""
    lines = [f"def {name} : Nat → Nat → Int"]
    for (row, col), value in values:
        if value != 0:
            lines.append(f"  | {row}, {col} => {value}")
    lines.append("  | _, _ => 0")
    return "\n".join(lines)


def lean_panel_dispatcher(name: str) -> str:
    lines = [f"def {name} : Nat → Nat → Nat → Int"]
    for panel in range(32):
        lines.append(f"  | {panel}, row, col => {name}Panel{panel} row col")
    lines.append("  | _, _, _ => 0")
    return "\n".join(lines)


def lean_rational(q: Fraction) -> str:
    """Print an exact rational without decimal notation."""
    if q.denominator == 1:
        return str(q.numerator)
    return f"{q.numerator} / {q.denominator}"


def emit_pole_lean(path: Path, mode_data: list[ModeData]) -> None:
    """Emit the 48 exact scale-centered finite pole coefficients."""
    lines = [
        "/- Generated exact rational pole-coefficient targets for p=2. -/",
        "import RHBridge.P2EntryCertificate",
        "",
        "namespace RHP2Bridge.P2PoleCoefficientCertificateData",
        "",
        "def poleCoeffQNat : Nat → ℚ",
    ]
    for mode in mode_data:
        lines.append(f"  | {mode.mode} => {lean_rational(mode.pole_center)}")
    lines.extend(
        [
            "  | _ => 0",
            "",
            "def poleCoeffQ (n : Fin 48) : ℚ := poleCoeffQNat n.val",
            "",
            "end RHP2Bridge.P2PoleCoefficientCertificateData",
            "",
        ]
    )
    body = "\n".join(lines)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    print(f"wrote {path} ({len(body) / 1e3:.1f} KB)")


def emit_pole_check_modules(directory: Path, chunk_size: int = 6) -> None:
    """Emit small kernel-reduction modules certifying the 48 pole values."""
    module_names = []
    for chunk, start in enumerate(range(0, MODES, chunk_size)):
        module_name = f"P2PoleCoefficientCertificateCheck{chunk}"
        module_names.append(module_name)
        lines = [
            "import RHBridge.P2PoleCoefficientCertificateData",
            "import RHBridge.P2PoleCanonicalDense",
            "",
            "namespace RHP2Bridge",
            "",
            "set_option maxRecDepth 100000",
            "",
        ]
        for mode in range(start, min(start + chunk_size, MODES)):
            lines.extend(
                [
                    f"theorem p2PoleCoeffCertificate{mode} :",
                    "    DenseRatPoly.p2PoleTaylorCoeffScaleCenterQ",
                    f"        ⟨{mode}, by decide⟩ =",
                    "      P2PoleCoefficientCertificateData.poleCoeffQ",
                    f"        ⟨{mode}, by decide⟩ := by",
                    "  decide +kernel",
                    "",
                ]
            )
        (directory / f"{module_name}.lean").write_text(
            "\n".join(lines + ["end RHP2Bridge", ""]), encoding="utf-8"
        )

    umbrella = [
        *(f"import RHBridge.{name}" for name in module_names),
        "",
        "namespace RHP2Bridge",
        "",
        "theorem p2PoleCoeffCertificate (n : Fin 48) :",
        "    DenseRatPoly.p2PoleTaylorCoeffScaleCenterQ n =",
        "      P2PoleCoefficientCertificateData.poleCoeffQ n := by",
        "  fin_cases n",
    ]
    for mode in range(MODES):
        umbrella.append(f"  · exact p2PoleCoeffCertificate{mode}")
    umbrella.extend(["", "end RHP2Bridge", ""])
    (directory / "P2PoleCoefficientCertificate.lean").write_text(
        "\n".join(umbrella), encoding="utf-8"
    )
    print(
        f"wrote {len(module_names)} pole-check modules and umbrella in {directory}"
    )


def emit_rounded_panel_targets(directory: Path, entries: list[EntryResult]) -> None:
    """Emit 32 coarse panel-center tables for the rounded Lean evaluator.

    Entry ``r`` uses exactly the order of ``p2UpperEntryAt``: the 300 even
    upper-triangular entries followed by the 300 odd entries, both row-major.
    Each value is the independently computed exact canonical panel integral
    rounded to the ``10^-40`` grid.  Lean later proves that its analytic
    rounded ball refines the radius-``10^-18`` ball around this center.
    """
    directory.mkdir(parents=True, exist_ok=True)
    base = """/- Generated base constants for p=2 rounded panel checkpoints. -/
import RHBridge.P2EntryCertificate

namespace RHP2Bridge.P2RoundedPanelTargetData

def panelIntegralScale : Nat := 10 ^ 40

/-- Per-panel coarse radius.  The 32-panel total is `3.2e-17`, well below
the aggregate certificate allowance `10^-15`. -/
def panelAllowanceQ : ℚ := 1 / 10 ^ 18

end RHP2Bridge.P2RoundedPanelTargetData
"""
    (directory / "P2RoundedPanelTargetData.lean").write_text(
        base, encoding="utf-8"
    )

    module_names = []
    for panel in range(32):
        module_name = f"P2RoundedPanelTargetData{panel}"
        module_names.append(module_name)
        lines = [
            "import RHBridge.P2RoundedPanelTargetData",
            "",
            "namespace RHP2Bridge.P2RoundedPanelTargetData",
            "",
            f"def panel{panel}IntegralNumerator : Nat → Int",
        ]
        for r, entry in enumerate(entries):
            lines.append(
                f"  | {r} => {entry.panel_integral_numerators[panel]}"
            )
        lines.extend(
            [
                "  | _ => 0",
                "",
                f"def panel{panel}TargetQ (r : Fin 600) : ℚ :=",
                f"  panel{panel}IntegralNumerator r.val / panelIntegralScale",
                "",
                "end RHP2Bridge.P2RoundedPanelTargetData",
                "",
            ]
        )
        (directory / f"{module_name}.lean").write_text(
            "\n".join(lines), encoding="utf-8"
        )

    umbrella = [
        *(f"import RHBridge.{name}" for name in module_names),
        "import RHBridge.P2PanelCertificateAggregate",
        "",
        "namespace RHP2Bridge.P2RoundedPanelTargetData",
        "",
        "open P2PanelCertificateAggregate",
        "",
        "/-- Panels `0` through `30` retain their independently rounded numerical",
        "centers.  Panel `31` is stored as the exact residual against the published",
        "band target, making the 32-panel center identity algebraic by construction.",
        "Its separate analytic refinement check validates this residual center. -/",
        "def first31PanelTargetSumQ (r : Fin 600) : ℚ :=",
    ]
    for start in range(0, 31, 3):
        terms = [
            f"panel{panel}TargetQ r"
            for panel in range(start, min(start + 3, 31))
        ]
        continuation = " +" if start + 3 < 31 else ""
        indentation = "  " if start == 0 else "    "
        umbrella.append(indentation + " + ".join(terms) + continuation)
    umbrella.extend(
        [
            "",
        "def panelTargetQ (k : Fin 32) (r : Fin 600) : ℚ :=",
        "  match k.val with",
        ]
    )
    for panel in range(31):
        umbrella.append(f"  | {panel} => panel{panel}TargetQ r")
    umbrella.extend(
        [
            "  | 31 => generatedBandIntegralQ (p2UpperEntryAt r).val -",
            "      first31PanelTargetSumQ r",
        ]
    )
    umbrella.extend(
        [
            "  | _ => 0",
            "",
            "end RHP2Bridge.P2RoundedPanelTargetData",
            "",
        ]
    )
    (directory / "P2RoundedPanelTargetDataAll.lean").write_text(
        "\n".join(umbrella), encoding="utf-8"
    )
    print(f"wrote 32 rounded panel target modules in {directory}")


def rounded_factor_scaled_data(
    polynomial: fmpq_poly,
    length: int,
    *,
    denominator: int = ROUNDED_FACTOR_DEN,
    radius: Fraction = Fraction(1),
) -> tuple[list[int], int]:
    """Mirror the certificate-local factor-grid rounding exactly.

    FLINT removes trailing zeroes, whereas the executable Lean dense
    polynomials retain them.  The caller supplies the canonical Lean list
    length.  At radius one, `roundingError` is exactly the sum of the
    coefficientwise absolute losses.
    """
    numerators: list[int] = []
    error = Fraction(0)
    for index in range(length):
        coefficient = (
            frac(polynomial[index]) if index <= polynomial.degree() else Fraction(0)
        )
        numerator = floor_scaled(coefficient, denominator)
        rounded = Fraction(numerator, denominator)
        numerators.append(numerator)
        error += abs(coefficient - rounded) * radius**index
    return numerators, ceil_scaled(error, denominator)


@dataclass(frozen=True)
class ApproxData:
    """Exact generator-side model of ``RoundedRatPoly.Approx``.

    This remains untrusted certificate-generation code.  Every value emitted
    from it is checked against the corresponding Lean operation by ordinary
    kernel reduction.
    """

    coeffs: tuple[Fraction, ...]
    error: Fraction


def dense_add_data(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    length = max(len(left), len(right))
    return tuple(
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(length)
    )


def dense_scale_data(
    scalar: Fraction, coefficients: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    return tuple(scalar * coefficient for coefficient in coefficients)


def dense_mul_data(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    """Mirror the list-shaped ``DenseRatPoly.mul`` including trailing zeros."""
    if not left:
        return ()
    if not right:
        # The recursive Lean definition applies ``xmul`` once per coefficient
        # of its first argument even when the second list is empty.
        return tuple(Fraction(0) for _ in left)
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for first_index, first in enumerate(left):
        for second_index, second in enumerate(right):
            result[first_index + second_index] += first * second
    return tuple(result)


def abs_bound_data(coefficients: tuple[Fraction, ...], radius: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = abs(coefficient) + radius * result
    return result


def lipschitz_bound_data(
    coefficients: tuple[Fraction, ...], radius: Fraction
) -> Fraction:
    absolute_tail = Fraction(0)
    lipschitz_tail = Fraction(0)
    for coefficient in reversed(coefficients):
        lipschitz_tail = radius * lipschitz_tail + absolute_tail
        absolute_tail = abs(coefficient) + radius * absolute_tail
    return lipschitz_tail


def grid_round_data(value: Fraction, denominator: int) -> Fraction:
    return Fraction(floor_scaled(value, denominator), denominator)


def error_ceil_data(value: Fraction, denominator: int) -> Fraction:
    return Fraction(ceil_scaled(value, denominator), denominator)


def round_coeffs_data(
    coefficients: tuple[Fraction, ...], denominator: int
) -> tuple[Fraction, ...]:
    return tuple(grid_round_data(value, denominator) for value in coefficients)


def rounding_error_data(
    raw: tuple[Fraction, ...], radius: Fraction, denominator: int
) -> Fraction:
    rounded = round_coeffs_data(raw, denominator)
    losses = tuple(a - b for a, b in zip(raw, rounded, strict=True))
    return abs_bound_data(losses, radius)


def rounded_approx_data(
    raw: tuple[Fraction, ...], radius: Fraction, denominator: int
) -> ApproxData:
    return ApproxData(
        round_coeffs_data(raw, denominator),
        error_ceil_data(rounding_error_data(raw, radius, denominator), denominator),
    )


def exact_approx_data(coefficients: tuple[Fraction, ...]) -> ApproxData:
    return ApproxData(coefficients, Fraction(0))


def add_approx_data(
    left: ApproxData, right: ApproxData, radius: Fraction, denominator: int
) -> ApproxData:
    raw = dense_add_data(left.coeffs, right.coeffs)
    return ApproxData(
        round_coeffs_data(raw, denominator),
        error_ceil_data(
            left.error
            + right.error
            + rounding_error_data(raw, radius, denominator),
            denominator,
        ),
    )


def scale_approx_data(
    scalar: Fraction, value: ApproxData, radius: Fraction, denominator: int
) -> ApproxData:
    raw = dense_scale_data(scalar, value.coeffs)
    return ApproxData(
        round_coeffs_data(raw, denominator),
        error_ceil_data(
            abs(scalar) * value.error
            + rounding_error_data(raw, radius, denominator),
            denominator,
        ),
    )


def mul_approx_data(
    left: ApproxData, right: ApproxData, radius: Fraction, denominator: int
) -> ApproxData:
    raw = dense_mul_data(left.coeffs, right.coeffs)
    return ApproxData(
        round_coeffs_data(raw, denominator),
        error_ceil_data(
            left.error * right.error
            + left.error * abs_bound_data(right.coeffs, radius)
            + abs_bound_data(left.coeffs, radius) * right.error
            + rounding_error_data(raw, radius, denominator),
            denominator,
        ),
    )


def comp_rounded_approx_data(
    outer: ApproxData, inner: ApproxData, radius: Fraction, denominator: int
) -> ApproxData:
    """Mirror recursive ``RoundedRatPoly.compRounded`` exactly."""
    core = exact_approx_data(())
    for coefficient in reversed(outer.coeffs):
        product = mul_approx_data(inner, core, radius, denominator)
        core = add_approx_data(
            exact_approx_data((coefficient,)), product, radius, denominator
        )
    return ApproxData(
        core.coeffs, error_ceil_data(outer.error + core.error, denominator)
    )


def approx_data_from_scaled(
    numerators: Iterable[int], error: int, denominator: int
) -> ApproxData:
    return ApproxData(
        tuple(Fraction(value, denominator) for value in numerators),
        Fraction(error, denominator),
    )


def approx_data_to_scaled(value: ApproxData, denominator: int) -> tuple[list[int], int]:
    scaled_coefficients = [coefficient * denominator for coefficient in value.coeffs]
    scaled_error = value.error * denominator
    assert all(coefficient.denominator == 1 for coefficient in scaled_coefficients)
    assert scaled_error.denominator == 1
    return [coefficient.numerator for coefficient in scaled_coefficients], scaled_error.numerator


def rounded_panel_piece_data(
    panel: PanelData, denominator: int = ROUNDED_FACTOR_DEN
) -> tuple[list[ApproxData], ApproxData]:
    prefix_terms = []
    for polynomial in panel.prefix_term_polys:
        numerators, error = rounded_factor_scaled_data(
            polynomial, 64, denominator=denominator
        )
        prefix_terms.append(
            approx_data_from_scaled(numerators, error, denominator)
        )
    numerators, error = rounded_factor_scaled_data(
        panel.nonprefix_poly, 129, denominator=denominator
    )
    return prefix_terms, approx_data_from_scaled(numerators, error, denominator)


def rounded_panel_defect_data(
    panel: PanelData, denominator: int = ROUNDED_FACTOR_DEN
) -> ApproxData:
    prefix_terms, nonprefix = rounded_panel_piece_data(panel, denominator)
    result = exact_approx_data(())
    for term in prefix_terms:
        result = add_approx_data(result, term, Fraction(1), denominator)
    return add_approx_data(result, nonprefix, Fraction(1), denominator)


def rounded_spherical_outer_data(
    mode: int, denominator: int = ROUNDED_OUTER_DEN
) -> ApproxData:
    numerators, error = rounded_factor_scaled_data(
        spherical_j_polynomial(mode),
        mode + SPHERICAL_TERMS,
        denominator=denominator,
        radius=Fraction(22),
    )
    return approx_data_from_scaled(numerators, error, denominator)


def truncate_outer_approx_data(
    outer: ApproxData, length: int, radius: Fraction
) -> ApproxData:
    """Mirror the semantic coefficient-prefix truncation used in Lean."""
    assert 0 <= length <= len(outer.coeffs)
    dropped = tuple(Fraction(0) for _ in range(length)) + outer.coeffs[length:]
    return ApproxData(
        outer.coeffs[:length],
        outer.error + abs_bound_data(dropped, radius),
    )


def choose_outer_truncation_length(
    outer: ApproxData,
    radius: Fraction,
    tail_threshold: Fraction = ROUNDED_OUTER_TAIL,
) -> int:
    for length in range(len(outer.coeffs) + 1):
        dropped = tuple(Fraction(0) for _ in range(length)) + outer.coeffs[length:]
        if abs_bound_data(dropped, radius) < tail_threshold:
            return length
    raise AssertionError("the full coefficient prefix must have zero dropped tail")


def comp_once_approx_data(
    outer: ApproxData,
    inner: ApproxData,
    radius: Fraction,
    denominator: int,
) -> ApproxData:
    """Mirror ``RoundedRatPoly.comp`` for the exact-inner use in this scout.

    Production panel inners have zero error.  We nevertheless include the
    general Lipschitz term so this helper continues to mirror Lean if reused.
    """
    raw: tuple[Fraction, ...] = ()
    for coefficient in reversed(outer.coeffs):
        raw = dense_add_data(
            (coefficient,), dense_mul_data(inner.coeffs, raw)
        )
    rounded = round_coeffs_data(raw, denominator)
    inner_domain = abs_bound_data(inner.coeffs, radius) + inner.error
    error = (
        outer.error
        + lipschitz_bound_data(outer.coeffs, inner_domain) * inner.error
        + abs_bound_data(
            tuple(a - b for a, b in zip(raw, rounded, strict=True)),
            radius,
        )
    )
    return ApproxData(rounded, error_ceil_data(error, denominator))


def rounded_panel_component_data(
    modes: list[ModeData],
    panel: PanelData,
    outer: ApproxData,
    kind: str,
    index: int,
    denominator: int = ROUNDED_FACTOR_DEN,
    truncation_length: int | None = None,
    compose_once: bool = False,
) -> ApproxData:
    assert kind in ("even", "odd")
    degree = 2 * index if kind == "even" else 2 * index + 1
    phase = (-1) ** index
    if kind == "odd":
        phase = -phase
    inner = exact_approx_data(
        (
            Fraction(7, 16) * panel.center,
            Fraction(7, 16) * panel.half_width,
        )
    )
    if truncation_length is not None:
        inner_radius = abs_bound_data(inner.coeffs, Fraction(1)) + inner.error
        outer = truncate_outer_approx_data(
            outer, truncation_length, inner_radius
        )
    if compose_once:
        composed = comp_once_approx_data(
            outer, inner, Fraction(1), denominator
        )
    else:
        composed = comp_rounded_approx_data(
            outer, inner, Fraction(1), denominator
        )
    return scale_approx_data(
        Fraction(phase) * modes[degree].scale_center,
        composed,
        Fraction(1),
        denominator,
    )


def interval_moment_data(degree: int) -> Fraction:
    """Exact integral of ``t^degree`` on ``[-1,1]``."""
    return Fraction(2, degree + 1) if degree % 2 == 0 else Fraction(0)


def defect_moments_data(
    defect_coefficients: tuple[Fraction, ...], rows: int = 297
) -> list[Fraction]:
    return [
        sum(
            (
                coefficient * interval_moment_data(shift + index)
                for index, coefficient in enumerate(defect_coefficients)
            ),
            Fraction(0),
        )
        for shift in range(rows)
    ]


def hankel_matvec_from_moments_data(
    moments: list[Fraction],
    component_coefficients: tuple[Fraction, ...],
    rows: int = 149,
) -> list[Fraction]:
    assert rows + len(component_coefficients) - 1 <= len(moments)
    return [
        sum(
            (
                coefficient * moments[shift + index]
                for index, coefficient in enumerate(component_coefficients)
            ),
            Fraction(0),
        )
        for shift in range(rows)
    ]


def hankel_dot_data(
    component_coefficients: tuple[Fraction, ...], matvec: list[Fraction]
) -> Fraction:
    assert len(component_coefficients) <= len(matvec)
    return sum(
        (
            coefficient * matvec[index]
            for index, coefficient in enumerate(component_coefficients)
        ),
        Fraction(0),
    )


def triple_factor_error_data(d: ApproxData, a: ApproxData, b: ApproxData) -> Fraction:
    d_bound = abs_bound_data(d.coeffs, Fraction(1))
    a_bound = abs_bound_data(a.coeffs, Fraction(1))
    b_bound = abs_bound_data(b.coeffs, Fraction(1))
    return (
        d.error * (a_bound + a.error) * (b_bound + b.error)
        + d_bound * a.error * (b_bound + b.error)
        + d_bound * a_bound * b.error
    )


def bounded_triple_factor_error_data(
    d: ApproxData, a: ApproxData, b: ApproxData
) -> Fraction:
    """Tight telescoping ledger using canonical uniform factor bounds.

    ``P2PanelPartition`` bounds the exact degree-100/prefix witness factors by
    ``7447/1000 + 21/10^15`` and ``1 + 2/10^18`` respectively.  Thus no
    coefficient-l1 bound for a highly cancelling composed approximation
    enters the analytic error.
    """
    defect_bound = DEFECT_ABS_BOUND + Fraction(21, 10**15)
    component_bound = Fraction(1) + Fraction(2, 10**18)
    return (
        d.error
        * (component_bound + a.error)
        * (component_bound + b.error)
        + defect_bound * a.error * (component_bound + b.error)
        + defect_bound * component_bound * b.error
    )


def parse_rounded_panel_target_numerators(directory: Path) -> list[list[int]]:
    """Read the currently emitted 32-by-600 panel target table.

    Panel 31 is returned as the residual used by
    ``P2RoundedPanelTargetData.panelTargetQ`` rather than blindly trusting the
    independently rounded panel-31 file.  The two values currently agree, but
    computing the residual here keeps this scout aligned with the actual Lean
    consumer if that representation changes later.
    """
    panel_values: list[list[int]] = []
    for panel in range(32):
        path = directory / f"P2RoundedPanelTargetData{panel}.lean"
        text = path.read_text(encoding="utf-8")
        start = text.index(f"def panel{panel}IntegralNumerator")
        end = text.index("\n  | _ => 0", start)
        values = [
            int(value)
            for _, value in re.findall(
                r"^\s*\|\s*(\d+)\s*=>\s*(-?\d+)\s*$",
                text[start:end],
                re.MULTILINE,
            )
        ]
        if len(values) != 600:
            raise RuntimeError(
                f"parsed {len(values)} entries from panel target {panel}"
            )
        panel_values.append(values)

    aggregate_text = (directory / "P2PanelCertificateData.lean").read_text(
        encoding="utf-8"
    )

    def parse_band_function(name: str) -> dict[tuple[int, int], int]:
        start = aggregate_text.index(f"def {name} : Nat → Nat → Int")
        end = aggregate_text.index("\n  | _, _ => 0", start)
        values = {
            (int(row), int(col)): int(value)
            for row, col, value in re.findall(
                r"^\s*\|\s*(\d+),\s*(\d+)\s*=>\s*(-?\d+)\s*$",
                aggregate_text[start:end],
                re.MULTILINE,
            )
        }
        if len(values) != 300:
            raise RuntimeError(f"parsed {len(values)} entries from {name}")
        return values

    even_band = parse_band_function("evenBandIntegralNumerator")
    odd_band = parse_band_function("oddBandIntegralNumerator")
    band_values = [
        table[(row, col)]
        for table in (even_band, odd_band)
        for row in range(BLOCK)
        for col in range(row, BLOCK)
    ]
    for entry in range(600):
        panel_values[31][entry] = (
            band_values[entry]
            - sum(panel_values[panel][entry] for panel in range(31))
        )
    return panel_values


def scout_rounded_tail_thresholds(
    directory: Path,
    modes: list[ModeData],
    panel_data: list[PanelData],
    thresholds: Iterable[Fraction],
) -> bool:
    """Exact-rational all-panel scout for candidate outer-tail thresholds.

    This is deliberately only a generator-side sizing tool.  Production
    certificate leaves still make Lean recompute every truncation equality,
    moment, matvec, final dot, and analytic radius with ``decide +kernel``.
    """
    targets = parse_rounded_panel_target_numerators(directory)
    entry_labels = [
        (block, row, col)
        for block in ("even", "odd")
        for row in range(BLOCK)
        for col in range(row, BLOCK)
    ]
    outers = [rounded_spherical_outer_data(mode) for mode in range(MODES)]
    passed = True

    for threshold in thresholds:
        exponent = len(str(threshold.denominator)) - 1
        print(f"\nrounded outer-tail scout: threshold=1e-{exponent}", flush=True)
        global_lengths: list[int] = []
        panel_length_stats: list[tuple[int, int, float]] = []
        panel_worsts: list[tuple[Fraction, int, Fraction, Fraction]] = []
        bounded_panel_worsts: list[
            tuple[Fraction, int, Fraction, Fraction]
        ] = []

        for panel, data in enumerate(panel_data):
            defect = rounded_panel_defect_data(data)
            domain = Fraction(7, 16) * (data.center + data.half_width)
            lengths = [
                choose_outer_truncation_length(outer, domain, threshold)
                for outer in outers
            ]
            global_lengths.extend(lengths)
            panel_length_stats.append(
                (min(lengths), max(lengths), sum(lengths) / len(lengths))
            )
            components = [
                rounded_panel_component_data(
                    modes,
                    data,
                    outers[mode],
                    "even" if mode % 2 == 0 else "odd",
                    mode // 2,
                    truncation_length=lengths[mode],
                )
                for mode in range(MODES)
            ]
            defect_poly = fmpq_poly([fq(value) for value in defect.coeffs])
            component_polys = [
                fmpq_poly([fq(value) for value in component.coeffs])
                for component in components
            ]
            defect_products = [
                defect_poly * component for component in component_polys
            ]

            worst = (Fraction(-1), -1, Fraction(0), Fraction(0))
            bounded_worst = (Fraction(-1), -1, Fraction(0), Fraction(0))
            for entry, (block, row, col) in enumerate(entry_labels):
                parity = 0 if block == "even" else 1
                first_mode = 2 * row + parity
                second_mode = 2 * col + parity
                center = data.half_width * exact_integral_minus_one_one(
                    defect_products[first_mode] * component_polys[second_mode]
                )
                target = Fraction(targets[panel][entry], PANEL_INTEGRAL_DEN)
                discrepancy = abs(center - target)
                radius = (
                    2
                    * data.half_width
                    * triple_factor_error_data(
                        defect,
                        components[first_mode],
                        components[second_mode],
                    )
                )
                demand = discrepancy + radius
                if demand > worst[0]:
                    worst = (demand, entry, discrepancy, radius)
                bounded_radius = (
                    2
                    * data.half_width
                    * bounded_triple_factor_error_data(
                        defect,
                        components[first_mode],
                        components[second_mode],
                    )
                )
                bounded_demand = discrepancy + bounded_radius
                if bounded_demand > bounded_worst[0]:
                    bounded_worst = (
                        bounded_demand,
                        entry,
                        discrepancy,
                        bounded_radius,
                    )
            panel_worsts.append(worst)
            bounded_panel_worsts.append(bounded_worst)
            print(
                f"  panel {panel:02d}: coefficient-l1={decimal(worst[0], 6)}, "
                f"bounded={decimal(bounded_worst[0], 6)}, "
                f"lengths={min(lengths)}/{max(lengths)}/"
                f"{sum(lengths) / len(lengths):.2f}",
                flush=True,
            )

        worst_panel = max(range(32), key=lambda panel: panel_worsts[panel][0])
        demand, entry, discrepancy, radius = panel_worsts[worst_panel]
        block, row, col = entry_labels[entry]
        bounded_worst_panel = max(
            range(32), key=lambda panel: bounded_panel_worsts[panel][0]
        )
        (
            bounded_demand,
            bounded_entry,
            bounded_discrepancy,
            bounded_radius,
        ) = bounded_panel_worsts[bounded_worst_panel]
        bounded_block, bounded_row, bounded_col = entry_labels[bounded_entry]
        heaviest_panel = max(
            range(32), key=lambda panel: panel_length_stats[panel][2]
        )
        worst_stats = panel_length_stats[worst_panel]
        heavy_stats = panel_length_stats[heaviest_panel]
        global_average = sum(global_lengths) / len(global_lengths)
        print(
            f"  COEFFICIENT-L1 GLOBAL worst={decimal(demand, 12)} "
            f"at panel {worst_panel}, "
            f"{block}[{row},{col}] (r={entry}); "
            f"discrepancy={decimal(discrepancy, 12)}, "
            f"radius={decimal(radius, 12)}"
        )
        print(
            f"  BOUNDED GLOBAL worst={decimal(bounded_demand, 12)} "
            f"at panel {bounded_worst_panel}, "
            f"{bounded_block}[{bounded_row},{bounded_col}] "
            f"(r={bounded_entry}); "
            f"discrepancy={decimal(bounded_discrepancy, 12)}, "
            f"radius={decimal(bounded_radius, 12)}"
        )
        print(
            "  truncation lengths at refinement-worst panel "
            f"{worst_panel}: min/max/avg="
            f"{worst_stats[0]}/{worst_stats[1]}/{worst_stats[2]:.2f}"
        )
        print(
            f"  truncation lengths at heaviest panel {heaviest_panel}: "
            f"min/max/avg={heavy_stats[0]}/{heavy_stats[1]}/{heavy_stats[2]:.2f}"
        )
        print(
            "  truncation lengths globally: min/max/avg="
            f"{min(global_lengths)}/{max(global_lengths)}/{global_average:.2f}"
        )
        threshold_passed = bounded_demand < Fraction(1, 10**18)
        print(
            "  panelAllowanceQ=1e-18: "
            f"{'PASS' if threshold_passed else 'FAIL'}"
        )
        passed = passed and threshold_passed
    return passed


def scout_rounded_composition_architectures(
    directory: Path,
    modes: list[ModeData],
    panel_data: list[PanelData],
    configs: list[tuple[str, bool, int, int, int, int, bool]] | None = None,
) -> bool:
    """Compare globally viable rounded-composition architectures.

    The defect and component grids are intentionally separate here.  Defect
    arithmetic lives on ``|t| <= 1`` and needs nothing like the precision of
    recursive Horner composition on late panels.
    """
    targets = parse_rounded_panel_target_numerators(directory)
    entry_labels = [
        (block, row, col)
        for block in ("even", "odd")
        for row in range(BLOCK)
        for col in range(row, BLOCK)
    ]
    # name, exact-compose-once, defect exponent, component exponent,
    # outer exponent, tail exponent, perform all 19,200 center checks.
    if configs is None:
        configs = [
            ("A-horner-c180-o300-t21", False, 40, 180, 300, 21, True),
            ("A-horner-c200-o300-t21", False, 40, 200, 300, 21, True),
            ("B-once-c40-o210-t21", True, 40, 40, 210, 21, True),
            ("B-once-c40-o220-t21", True, 40, 40, 220, 21, True),
            ("B-once-c40-o230-t21", True, 40, 40, 230, 21, True),
            ("B-once-c40-o240-t21", True, 40, 40, 240, 21, True),
            ("B-once-c50-o220-t21", True, 40, 50, 220, 21, True),
            # Tail 1e-20 already loses the desired comfort margin even with
            # exact arithmetic.  Radius-only evaluation records that fact.
            ("B-once-c40-o230-t20", True, 40, 40, 230, 20, False),
        ]
    all_full_pass = True

    for (
        name,
        compose_once,
        defect_exponent,
        component_exponent,
        outer_exponent,
        tail_exponent,
        full,
    ) in configs:
        defect_denominator = 10**defect_exponent
        component_denominator = 10**component_exponent
        outer_denominator = 10**outer_exponent
        tail_threshold = Fraction(1, 10**tail_exponent)
        print(f"\ncomposition architecture scout: {name}", flush=True)
        outers = [
            rounded_spherical_outer_data(mode, outer_denominator)
            for mode in range(MODES)
        ]
        max_outer_error = max(outer.error for outer in outers)
        max_defect_error = Fraction(0)
        max_component_error = Fraction(0)
        max_component_location = (-1, -1)
        global_lengths: list[int] = []
        panel_length_stats: list[tuple[int, int, float]] = []
        worst_radius = (Fraction(-1), -1, -1)
        worst_lhs = (Fraction(-1), -1, -1, Fraction(0), Fraction(0))

        for panel, data in enumerate(panel_data):
            defect = rounded_panel_defect_data(data, defect_denominator)
            max_defect_error = max(max_defect_error, defect.error)
            domain = Fraction(7, 16) * (data.center + data.half_width)
            lengths = [
                choose_outer_truncation_length(
                    outer, domain, tail_threshold
                )
                for outer in outers
            ]
            global_lengths.extend(lengths)
            panel_length_stats.append(
                (min(lengths), max(lengths), sum(lengths) / len(lengths))
            )
            components = [
                rounded_panel_component_data(
                    modes,
                    data,
                    outers[mode],
                    "even" if mode % 2 == 0 else "odd",
                    mode // 2,
                    denominator=component_denominator,
                    truncation_length=lengths[mode],
                    compose_once=compose_once,
                )
                for mode in range(MODES)
            ]
            for mode, component in enumerate(components):
                if component.error > max_component_error:
                    max_component_error = component.error
                    max_component_location = (panel, mode)

            if full:
                defect_poly = fmpq_poly([fq(value) for value in defect.coeffs])
                component_polys = [
                    fmpq_poly([fq(value) for value in component.coeffs])
                    for component in components
                ]
                defect_products = [
                    defect_poly * component for component in component_polys
                ]

            for entry, (block, row, col) in enumerate(entry_labels):
                parity = 0 if block == "even" else 1
                first_mode = 2 * row + parity
                second_mode = 2 * col + parity
                radius = (
                    2
                    * data.half_width
                    * bounded_triple_factor_error_data(
                        defect,
                        components[first_mode],
                        components[second_mode],
                    )
                )
                if radius > worst_radius[0]:
                    worst_radius = (radius, panel, entry)
                if full:
                    center = data.half_width * exact_integral_minus_one_one(
                        defect_products[first_mode]
                        * component_polys[second_mode]
                    )
                    target = Fraction(
                        targets[panel][entry], PANEL_INTEGRAL_DEN
                    )
                    discrepancy = abs(center - target)
                    lhs = discrepancy + radius
                    if lhs > worst_lhs[0]:
                        worst_lhs = (
                            lhs, panel, entry, discrepancy, radius
                        )
            if panel % 8 == 7:
                print(f"  completed panels 0..{panel}", flush=True)

        radius, radius_panel, radius_entry = worst_radius
        radius_block, radius_row, radius_col = entry_labels[radius_entry]
        heaviest_panel = max(
            range(32), key=lambda panel: panel_length_stats[panel][2]
        )
        heavy_stats = panel_length_stats[heaviest_panel]
        print(
            f"  outer max Approx.error={decimal(max_outer_error, 12)}; "
            f"defect max error={decimal(max_defect_error, 12)}"
        )
        print(
            f"  component max error={decimal(max_component_error, 12)} "
            f"at panel/mode={max_component_location[0]}/"
            f"{max_component_location[1]}"
        )
        print(
            f"  worst bounded radius={decimal(radius, 12)} at panel "
            f"{radius_panel}, {radius_block}[{radius_row},{radius_col}] "
            f"(r={radius_entry})"
        )
        print(
            "  truncation lengths globally min/max/avg="
            f"{min(global_lengths)}/{max(global_lengths)}/"
            f"{sum(global_lengths) / len(global_lengths):.2f}; "
            f"heaviest panel {heaviest_panel}="
            f"{heavy_stats[0]}/{heavy_stats[1]}/{heavy_stats[2]:.2f}"
        )
        if full:
            lhs, panel, entry, discrepancy, radius_at_lhs = worst_lhs
            block, row, col = entry_labels[entry]
            passes = lhs < Fraction(1, 10**18)
            comfortable = lhs <= Fraction(2, 10**19)
            print(
                f"  FULL GLOBAL LHS={decimal(lhs, 12)} at panel {panel}, "
                f"{block}[{row},{col}] (r={entry}); "
                f"discrepancy={decimal(discrepancy, 12)}, "
                f"radius={decimal(radius_at_lhs, 12)}"
            )
            print(
                "  refinement: "
                f"{'PASS' if passes else 'FAIL'}; comfort <=2e-19: "
                f"{'YES' if comfortable else 'NO'}"
            )
            all_full_pass = all_full_pass and passes
        else:
            print("  radius-only configuration (no center pass)")
    return all_full_pass


def lean_int_list(values: Iterable[int]) -> str:
    return "[" + ", ".join(str(value) for value in values) + "]"


def lean_rat_literal(value: Fraction) -> str:
    if value.denominator == 1:
        return f"({value.numerator} : ℚ)"
    return f"({value.numerator} : ℚ) / {value.denominator}"


def emit_rounded_factor_checkpoints(
    directory: Path, panel_data: list[PanelData], chunk_size: int = 4
) -> None:
    """Emit explicit factor caches and small kernel equality checks.

    The data are untrusted scaled integers.  Each generated check reduces the
    corresponding canonical Lean factor and verifies equality using
    `decide +kernel`.  The expensive defect is never normalized monolithically:
    it is assembled semantically from 64 prefix terms and one nonprefix term.
    """
    directory.mkdir(parents=True, exist_ok=True)
    base = """/- Generated base definitions for p=2 rounded factor checkpoints. -/
import RHBridge.P2RoundedSharedEvaluator

namespace RHP2Bridge.P2RoundedFactorCheckpointData

open P2RoundedSharedEvaluator

/-- Derived from the production evaluator to prevent generator/Lean drift. -/
def factorScale : Nat := P2RoundedCanonical.gridCells + 1

def approxOfScaled (coefficients : List Int) (error : Int) :
    RoundedRatPoly.Approx where
  coeffs := coefficients.map fun z => (z : ℚ) / factorScale
  error := (error : ℚ) / factorScale

/-- Likewise share the exact global-outer grid with the semantic evaluator. -/
def sphericalOuterGridCells : Nat :=
  P2RoundedSharedEvaluator.sphericalOuterCells
def sphericalOuterScale : Nat := sphericalOuterGridCells + 1

def outerApproxOfScaled (coefficients : List Int) (error : Int) :
    RoundedRatPoly.Approx where
  coeffs := coefficients.map fun z => (z : ℚ) / sphericalOuterScale
  error := (error : ℚ) / sphericalOuterScale

def computedSphericalOuter (n : Fin 48) : RoundedRatPoly.Approx :=
  RoundedRatPoly.rounded sphericalOuterGridCells 22
    (DenseRatPoly.sphericalJRealPolynomial n.val 100)

theorem computedSphericalOuter_encloses (n : Fin 48) :
    RoundedRatPoly.Encloses 22
      (RoundedRatPoly.evalReal
        (DenseRatPoly.sphericalJRealPolynomial n.val 100))
      (computedSphericalOuter n) := by
  exact RoundedRatPoly.rounded_encloses sphericalOuterGridCells
    (by norm_num) _

end RHP2Bridge.P2RoundedFactorCheckpointData
"""
    (directory / "P2RoundedFactorCheckpointData.lean").write_text(
        base, encoding="utf-8"
    )

    outer_lines = [
        "import RHBridge.P2RoundedFactorCheckpointData",
        "",
        "namespace RHP2Bridge.P2RoundedFactorCheckpointData",
        "",
    ]
    for mode in range(MODES):
        nums, error = rounded_factor_scaled_data(
            spherical_j_polynomial(mode),
            mode + SPHERICAL_TERMS,
            denominator=ROUNDED_OUTER_DEN,
            radius=Fraction(22),
        )
        outer_lines.extend(
            [
                f"def sphericalOuter{mode} : RoundedRatPoly.Approx :=",
                f"  outerApproxOfScaled {lean_int_list(nums)} {error}",
                "",
            ]
        )
    outer_lines.extend(
        [
            "def sphericalOuter (n : Fin 48) : RoundedRatPoly.Approx :=",
            "  match n.val with",
        ]
    )
    for mode in range(MODES):
        outer_lines.append(f"  | {mode} => sphericalOuter{mode}")
    outer_lines.extend(
        [
            "  | _ => sphericalOuter0",
            "",
            "def sphericalOuters : Vector RoundedRatPoly.Approx 48 :=",
            "  Vector.ofFn sphericalOuter",
            "",
            "end RHP2Bridge.P2RoundedFactorCheckpointData",
            "",
        ]
    )
    (directory / "P2RoundedSphericalOuterData.lean").write_text(
        "\n".join(outer_lines), encoding="utf-8"
    )

    outer_check_modules = []
    for chunk, start in enumerate(range(0, MODES, 4)):
        chunk_modes = list(range(start, min(start + 4, MODES)))
        module_name = f"P2RoundedSphericalOuterCheck{chunk}"
        outer_check_modules.append(module_name)
        propositions = [
            f"P2RoundedFactorCheckpointData.sphericalOuter{mode} =\n"
            f"        P2RoundedFactorCheckpointData.computedSphericalOuter "
            f"⟨{mode}, by decide⟩"
            for mode in chunk_modes
        ]
        theorem_name = f"sphericalOuterChunk{chunk}"
        check_lines = [
            "import RHBridge.P2RoundedSphericalOuterData",
            "",
            "namespace RHP2Bridge",
            "",
            "set_option maxRecDepth 100000",
            "set_option maxHeartbeats 50000000",
            "",
            f"theorem {theorem_name} :",
            "    " + " ∧\n      ".join(propositions) + " := by",
            "  decide +kernel",
            "",
        ]
        for offset, mode in enumerate(chunk_modes):
            projection = theorem_name + ".2" * offset
            if offset < len(chunk_modes) - 1:
                projection += ".1"
            check_lines.extend(
                [
                    f"theorem sphericalOuter{mode}_eq :",
                    f"    {propositions[offset]} := by",
                    f"  exact {projection}",
                    "",
                ]
            )
        check_lines.extend(["end RHP2Bridge", ""])
        (directory / f"{module_name}.lean").write_text(
            "\n".join(check_lines), encoding="utf-8"
        )

    outer_correctness = [
        *(f"import RHBridge.{name}" for name in outer_check_modules),
        "",
        "namespace RHP2Bridge",
        "",
        "open P2RoundedFactorCheckpointData",
        "",
        "theorem generatedSphericalOuter_encloses (n : Fin 48) :",
        "    RoundedRatPoly.Encloses 22",
        "      (RoundedRatPoly.evalReal",
        "        (DenseRatPoly.sphericalJRealPolynomial n.val 100))",
        "      (sphericalOuter n) := by",
        "  fin_cases n",
    ]
    for mode in range(MODES):
        outer_correctness.extend(
            [
                f"  · rw [sphericalOuter, sphericalOuter{mode}_eq]",
                "    exact computedSphericalOuter_encloses _",
            ]
        )
    outer_correctness.extend(
        [
            "",
            "theorem generatedSphericalOuters_enclose :",
            "    P2RoundedSharedEvaluator.SphericalOutersEnclose",
            "      sphericalOuters := by",
            "  constructor",
            "  intro n",
            "  simpa [sphericalOuters,",
            "    P2RoundedSharedEvaluator.sphericalOuterExact] using",
            "      generatedSphericalOuter_encloses n",
            "",
            "end RHP2Bridge",
            "",
        ]
    )
    (directory / "P2RoundedSphericalOuter.lean").write_text(
        "\n".join(outer_correctness), encoding="utf-8"
    )

    for panel, data in enumerate(panel_data):
        factor_defs: list[tuple[str, list[int], int]] = []
        for term, polynomial in enumerate(data.prefix_term_polys):
            nums, error = rounded_factor_scaled_data(polynomial, 64)
            factor_defs.append(
                (f"panel{panel}Prefix{term}", nums, error)
            )
        nonprefix_nums, nonprefix_error = rounded_factor_scaled_data(
            data.nonprefix_poly, 129
        )
        factor_defs.append(
            (f"panel{panel}Nonprefix", nonprefix_nums, nonprefix_error)
        )
        lines = [
            "import RHBridge.P2RoundedFactorCheckpointData",
            "import RHBridge.P2RoundedSphericalOuterData",
            "",
            "namespace RHP2Bridge.P2RoundedFactorCheckpointData",
            "",
            "open P2RoundedSharedEvaluator",
            "",
        ]
        for name, nums, error in factor_defs:
            lines.extend(
                [
                    f"def {name} : RoundedRatPoly.Approx :=",
                    f"  approxOfScaled {lean_int_list(nums)} {error}",
                    "",
                ]
            )
        lines.extend(
            [
                f"def panel{panel}PrefixTerm (i : Fin 64) : RoundedRatPoly.Approx :=",
                "  match i.val with",
            ]
        )
        for index in range(64):
            lines.append(f"  | {index} => panel{panel}Prefix{index}")
        lines.extend(
            [
                "  | _ => panel" + str(panel) + "Prefix0",
                "",
                f"def panel{panel}DefectPieces : DefectPieces where",
                f"  prefixTerms := Vector.ofFn panel{panel}PrefixTerm",
                f"  nonprefix := panel{panel}Nonprefix",
                "",
            ]
        )
        lines.extend(
            [
                f"def panel{panel}EvenComponents : Vector RoundedRatPoly.Approx 24 :=",
                "  componentVectorFromOuters sphericalOuters .even",
                f"    ⟨{panel}, by decide⟩",
                "",
                f"def panel{panel}OddComponents : Vector RoundedRatPoly.Approx 24 :=",
                "  componentVectorFromOuters sphericalOuters .odd",
                f"    ⟨{panel}, by decide⟩",
                "",
                f"def panel{panel}Cache : PanelCache :=",
                f"  panelCacheOfPieces panel{panel}DefectPieces",
                f"    panel{panel}EvenComponents panel{panel}OddComponents",
                "",
                "end RHP2Bridge.P2RoundedFactorCheckpointData",
                "",
            ]
        )
        (directory / f"P2RoundedFactorCheckpointData{panel}.lean").write_text(
            "\n".join(lines), encoding="utf-8"
        )

        factors: list[tuple[str, str]] = []
        for term in range(64):
            factors.append(
                (
                    f"panel{panel}Prefix{term}_eq",
                    f"P2RoundedFactorCheckpointData.panel{panel}Prefix{term} =\n"
                    f"      normalizedPrefixTermAtomApprox ⟨{term}, by decide⟩ "
                    f"⟨{panel}, by decide⟩",
                )
            )
        factors.append(
            (
                f"panel{panel}Nonprefix_eq",
                f"P2RoundedFactorCheckpointData.panel{panel}Nonprefix =\n"
                f"      normalizedNonprefixAtomApprox ⟨{panel}, by decide⟩",
            )
        )
        factor_groups = [
            factors[start : start + chunk_size]
            for start in range(0, 64, chunk_size)
        ]
        factor_groups.append([factors[64]])
        check_modules = []
        for chunk, chunk_factors in enumerate(factor_groups):
            module_name = f"P2RoundedFactorCheckpointCheck{panel}_{chunk}"
            check_modules.append(module_name)
            check_lines = [
                f"import RHBridge.P2RoundedFactorCheckpointData{panel}",
                "",
                "namespace RHP2Bridge",
                "",
                "open P2RoundedCanonical",
                "open P2RoundedSharedEvaluator",
                "",
                "set_option maxRecDepth 100000",
                "set_option maxHeartbeats 50000000",
                "",
            ]
            propositions = [proposition for _, proposition in chunk_factors]
            chunk_theorem = f"panel{panel}FactorChunk{chunk}"
            conjunction = " ∧\n      ".join(propositions)
            check_lines.extend(
                [
                    f"theorem {chunk_theorem} :",
                    f"    {conjunction} := by",
                    "  decide +kernel",
                    "",
                ]
            )
            for offset, (theorem_name, proposition) in enumerate(chunk_factors):
                projection = chunk_theorem + ".2" * offset
                if offset < len(chunk_factors) - 1:
                    projection += ".1"
                check_lines.extend(
                    [
                        f"theorem {theorem_name} :",
                        f"    {proposition} := by",
                        f"  exact {projection}",
                        "",
                    ]
                )
            check_lines.extend(["end RHP2Bridge", ""])
            (directory / f"{module_name}.lean").write_text(
                "\n".join(check_lines), encoding="utf-8"
            )

        correctness = [
            "import RHBridge.P2RoundedSphericalOuter",
            *(f"import RHBridge.{name}" for name in check_modules),
            "",
            "namespace RHP2Bridge",
            "",
            "open P2RoundedCanonical P2RoundedSharedEvaluator",
            "",
            "set_option maxRecDepth 100000",
            "set_option maxHeartbeats 50000000",
            "",
            f"theorem panel{panel}PrefixTerm_eq_computed (i : Fin 64) :",
            f"    P2RoundedFactorCheckpointData.panel{panel}PrefixTerm i =",
            f"      normalizedPrefixTermAtomApprox i ⟨{panel}, by decide⟩ := by",
            "  fin_cases i",
        ]
        for index in range(64):
            correctness.append(f"  · exact panel{panel}Prefix{index}_eq")
        correctness.extend(
            [
            "",
            f"theorem panel{panel}DefectPieces_enclosesCanonical :",
            f"    P2RoundedFactorCheckpointData.panel{panel}DefectPieces.EnclosesCanonical",
            f"      ⟨{panel}, by decide⟩ := by",
                "  constructor",
                "  · intro i",
                f"    simp only [P2RoundedFactorCheckpointData.panel{panel}DefectPieces,",
                "      Vector.get_ofFn]",
                f"    rw [panel{panel}PrefixTerm_eq_computed i]",
                f"    exact normalizedPrefixTermAtomApprox_encloses i ⟨{panel}, by decide⟩",
                f"  · simp only [P2RoundedFactorCheckpointData.panel{panel}DefectPieces]",
                f"    rw [panel{panel}Nonprefix_eq]",
                f"    exact normalizedNonprefixAtomApprox_encloses ⟨{panel}, by decide⟩",
                "",
                f"theorem panel{panel}Cache_enclosesCanonical :",
                f"    P2RoundedFactorCheckpointData.panel{panel}Cache.EnclosesCanonical",
                f"      ⟨{panel}, by decide⟩ := by",
                "  apply panelCacheOfPieces_enclosesCanonical",
                f"      panel{panel}DefectPieces_enclosesCanonical",
                "  · intro i",
                "    exact componentVectorFromOuters_encloses",
                "      generatedSphericalOuters_enclose .even _ i",
            ]
        )
        correctness.extend(
            [
                "  · intro i",
                "    exact componentVectorFromOuters_encloses",
                "      generatedSphericalOuters_enclose .odd _ i",
            ]
        )
        correctness.extend(["", "end RHP2Bridge", ""])
        (directory / f"P2RoundedFactorCheckpoint{panel}.lean").write_text(
            "\n".join(correctness), encoding="utf-8"
        )
    print(f"wrote 32 rounded factor caches and split checks in {directory}")


def emit_rounded_flat_factor_checkpoints(
    directory: Path,
    mode_data: list[ModeData],
    panel_data: list[PanelData],
    *,
    panel_count: int = 1,
    panel_indices: Iterable[int] | None = None,
    chunk_size: int = 1,
) -> None:
    """Materialize already-certified piece/outer computations as flat caches.

    The first layer checks small canonical atoms.  This second layer prevents
    every entry refinement from re-expanding the 65-piece defect sum and the
    two recursive spherical compositions.  Its literal data remain untrusted:
    split ``decide +kernel`` equalities connect every field back to the first
    layer, and the semantic umbrella transports ``EnclosesCanonical`` through
    those equalities.
    """
    if panel_indices is None:
        if not 1 <= panel_count <= len(panel_data):
            raise ValueError(
                "panel_count must be between one and the panel count"
            )
        selected_panels = list(range(panel_count))
    else:
        selected_panels = list(dict.fromkeys(panel_indices))
        if not selected_panels or any(
            not 0 <= panel < len(panel_data) for panel in selected_panels
        ):
            raise ValueError("every selected flat panel must lie in [0, 31]")
    directory.mkdir(parents=True, exist_ok=True)
    outers = [rounded_spherical_outer_data(mode) for mode in range(MODES)]

    for panel in selected_panels:
        data = panel_data[panel]
        defect = rounded_panel_defect_data(data)
        panel_outer_domain = Fraction(7, 16) * (data.center + data.half_width)
        outer_lengths = [
            choose_outer_truncation_length(outer, panel_outer_domain)
            for outer in outers
        ]
        components: dict[str, list[ApproxData]] = {"Even": [], "Odd": []}
        for tag, kind in (("Even", "even"), ("Odd", "odd")):
            for index in range(BLOCK):
                degree = 2 * index if kind == "even" else 2 * index + 1
                components[tag].append(
                    rounded_panel_component_data(
                        mode_data, data, outers[degree], kind, index,
                        truncation_length=outer_lengths[degree],
                        compose_once=True,
                    )
                )

        defect_nums, defect_error = approx_data_to_scaled(
            defect, ROUNDED_FACTOR_DEN
        )
        data_lines = [
            f"import RHBridge.P2RoundedFactorCheckpointData{panel}",
            "import RHBridge.P2RoundedDirectOuterComponent",
            "",
            "namespace RHP2Bridge.P2RoundedFactorCheckpointData",
            "",
            "open P2RoundedSharedEvaluator",
            "open P2RoundedTruncatedOuter",
            "open P2RoundedDirectOuterComponent",
            "",
            "set_option maxRecDepth 100000",
            "set_option maxHeartbeats 50000000",
            "",
            f"def panel{panel}OuterLength (n : Fin 48) : ℕ :=",
            "  match n.val with",
        ]
        for mode, length in enumerate(outer_lengths):
            data_lines.append(f"  | {mode} => {length}")
        data_lines.extend(
            [
                "  | _ => 0",
                "",
                f"def panel{panel}OuterLengthTable",
                "    (_k : Fin 32) (n : Fin 48) : ℕ :=",
                f"  panel{panel}OuterLength n",
                "",
                f"def panel{panel}TruncatedEvenComponents :",
                "    Vector RoundedRatPoly.Approx 24 :=",
                "  componentVectorFromTruncatedOuters",
                "    P2RoundedCanonical.gridCells sphericalOuters",
                f"    panel{panel}OuterLengthTable .even ⟨{panel}, by decide⟩",
                "",
                f"def panel{panel}TruncatedOddComponents :",
                "    Vector RoundedRatPoly.Approx 24 :=",
                "  componentVectorFromTruncatedOuters",
                "    P2RoundedCanonical.gridCells sphericalOuters",
                f"    panel{panel}OuterLengthTable .odd ⟨{panel}, by decide⟩",
                "",
            ]
        )
        data_lines.extend(
            [
            f"def panel{panel}FlatDefect : RoundedRatPoly.Approx :=",
            f"  approxOfScaled {lean_int_list(defect_nums)} {defect_error}",
            "",
            ]
        )
        for tag in ("Even", "Odd"):
            for index, component in enumerate(components[tag]):
                numerators, error = approx_data_to_scaled(
                    component, ROUNDED_FACTOR_DEN
                )
                data_lines.extend(
                    [
                        f"def panel{panel}Flat{tag}{index} : RoundedRatPoly.Approx :=",
                        f"  approxOfScaled {lean_int_list(numerators)} {error}",
                        "",
                    ]
                )
            data_lines.extend(
                [
                    f"def panel{panel}Flat{tag}Component",
                    "    (i : Fin 24) : RoundedRatPoly.Approx :=",
                    "  match i.val with",
                ]
            )
            for index in range(BLOCK):
                data_lines.append(
                    f"  | {index} => panel{panel}Flat{tag}{index}"
                )
            data_lines.extend(
                [
                    f"  | _ => panel{panel}Flat{tag}0",
                    "",
                    f"def panel{panel}Flat{tag}Components :",
                    "    Vector RoundedRatPoly.Approx 24 :=",
                    f"  Vector.ofFn panel{panel}Flat{tag}Component",
                    "",
                ]
            )
        data_lines.extend(
            [
                f"def panel{panel}FlatCache : PanelCache where",
                f"  defect := panel{panel}FlatDefect",
                f"  evenComponents := panel{panel}FlatEvenComponents",
                f"  oddComponents := panel{panel}FlatOddComponents",
                "",
                "end RHP2Bridge.P2RoundedFactorCheckpointData",
                "",
            ]
        )
        data_module = f"P2RoundedFlatFactorCheckpointData{panel}"
        (directory / f"{data_module}.lean").write_text(
            "\n".join(data_lines), encoding="utf-8"
        )

        defect_theorem = f"panel{panel}FlatDefect_eq"
        defect_check_module = (
            f"P2RoundedFlatFactorCheckpointCheck{panel}_defect"
        )
        defect_check = [
            f"import RHBridge.{data_module}",
            "",
            "namespace RHP2Bridge",
            "",
            "open P2RoundedSharedEvaluator",
            "",
            "set_option maxRecDepth 100000",
            "set_option maxHeartbeats 50000000",
            "",
            f"theorem {defect_theorem} :",
            f"    P2RoundedFactorCheckpointData.panel{panel}FlatDefect =",
            f"      P2RoundedFactorCheckpointData.panel{panel}DefectPieces.assemble := by",
            "  decide +kernel",
            "",
            "end RHP2Bridge",
            "",
        ]
        (directory / f"{defect_check_module}.lean").write_text(
            "\n".join(defect_check), encoding="utf-8"
        )

        component_facts: list[tuple[str, str]] = []
        for tag in ("Even", "Odd"):
            for index in range(BLOCK):
                theorem_name = f"panel{panel}Flat{tag}{index}_eq"
                proposition = (
                    f"P2RoundedFactorCheckpointData.panel{panel}Flat{tag}{index} =\n"
                    f"      (P2RoundedFactorCheckpointData.panel{panel}Truncated{tag}Components).get "
                    f"⟨{index}, by decide⟩"
                )
                component_facts.append((theorem_name, proposition))
        component_modules: list[str] = []
        for chunk, start in enumerate(range(0, len(component_facts), chunk_size)):
            facts = component_facts[start : start + chunk_size]
            module_name = f"P2RoundedFlatFactorCheckpointCheck{panel}_{chunk}"
            component_modules.append(module_name)
            chunk_theorem = f"panel{panel}FlatComponentChunk{chunk}"
            propositions = [proposition for _, proposition in facts]
            check_lines = [
                f"import RHBridge.{data_module}",
                "",
                "namespace RHP2Bridge",
                "",
                "set_option maxRecDepth 100000",
                "set_option maxHeartbeats 50000000",
                "",
                f"theorem {chunk_theorem} :",
                "    " + " ∧\n      ".join(propositions) + " := by",
                "  decide +kernel",
                "",
            ]
            for offset, (theorem_name, proposition) in enumerate(facts):
                projection = chunk_theorem + ".2" * offset
                if offset < len(facts) - 1:
                    projection += ".1"
                check_lines.extend(
                    [
                        f"theorem {theorem_name} :",
                        f"    {proposition} := by",
                        f"  exact {projection}",
                        "",
                    ]
                )
            check_lines.extend(["end RHP2Bridge", ""])
            (directory / f"{module_name}.lean").write_text(
                "\n".join(check_lines), encoding="utf-8"
            )

        semantic_lines = [
            f"import RHBridge.P2RoundedFactorCheckpoint{panel}",
            f"import RHBridge.{defect_check_module}",
            *(f"import RHBridge.{name}" for name in component_modules),
            "",
            "namespace RHP2Bridge",
            "",
            "open P2RoundedSharedEvaluator",
            "open P2RoundedTruncatedOuter",
            "open P2RoundedDirectOuterComponent",
            "",
        ]
        for tag in ("Even", "Odd"):
            semantic_lines.extend(
                [
                    f"theorem panel{panel}Flat{tag}Components_get_eq",
                    "    (i : Fin 24) :",
                    f"    (P2RoundedFactorCheckpointData.panel{panel}Flat{tag}Components).get i =",
                    f"      (P2RoundedFactorCheckpointData.panel{panel}Truncated{tag}Components).get i := by",
                    f"  simp only [P2RoundedFactorCheckpointData.panel{panel}Flat{tag}Components,",
                    "    Vector.get_ofFn]",
                    "  fin_cases i",
                ]
            )
            for index in range(BLOCK):
                semantic_lines.append(
                    f"  · exact panel{panel}Flat{tag}{index}_eq"
                )
            semantic_lines.append("")
        semantic_lines.extend(
            [
                f"theorem panel{panel}FlatCache_enclosesCanonical :",
                f"    P2RoundedFactorCheckpointData.panel{panel}FlatCache.EnclosesCanonical",
                f"      ⟨{panel}, by decide⟩ := by",
                "  constructor",
                "  · change RoundedRatPoly.Encloses 1 _",
                f"      P2RoundedFactorCheckpointData.panel{panel}FlatDefect",
                f"    rw [panel{panel}FlatDefect_eq]",
                "    exact DefectPieces.assemble_encloses",
                f"      panel{panel}DefectPieces_enclosesCanonical",
                "  · intro i",
                "    change RoundedRatPoly.Encloses 1 _",
                f"      ((P2RoundedFactorCheckpointData.panel{panel}FlatEvenComponents).get i)",
                f"    rw [panel{panel}FlatEvenComponents_get_eq i]",
                "    exact componentVectorFromTruncatedOuters_encloses",
                "      P2RoundedCanonical.gridCells (by",
                "        norm_num [P2RoundedCanonical.gridCells])",
                "      generatedSphericalOuters_enclose",
                f"      P2RoundedFactorCheckpointData.panel{panel}OuterLengthTable",
                f"      .even ⟨{panel}, by decide⟩ i",
                "  · intro i",
                "    change RoundedRatPoly.Encloses 1 _",
                f"      ((P2RoundedFactorCheckpointData.panel{panel}FlatOddComponents).get i)",
                f"    rw [panel{panel}FlatOddComponents_get_eq i]",
                "    exact componentVectorFromTruncatedOuters_encloses",
                "      P2RoundedCanonical.gridCells (by",
                "        norm_num [P2RoundedCanonical.gridCells])",
                "      generatedSphericalOuters_enclose",
                f"      P2RoundedFactorCheckpointData.panel{panel}OuterLengthTable",
                f"      .odd ⟨{panel}, by decide⟩ i",
                "",
                "end RHP2Bridge",
                "",
            ]
        )
        (directory / f"P2RoundedFlatFactorCheckpoint{panel}.lean").write_text(
            "\n".join(semantic_lines), encoding="utf-8"
        )
        worst_component_error = max(
            component.error
            for tag_components in components.values()
            for component in tag_components
        )
        print(
            f"flat panel {panel}: defect error={decimal(defect.error, 4)}, "
            f"worst component error={decimal(worst_component_error, 4)}",
            flush=True,
        )
    print(
        f"wrote {len(selected_panels)} flat rounded factor caches and split "
        f"checks in {directory}"
    )


def emit_rounded_moment_checkpoint_scout(
    directory: Path,
    mode_data: list[ModeData],
    panel_data: list[PanelData],
    *,
    panel: int = 0,
    chunk_size: int = 64,
) -> None:
    """Emit one panel's exact two-stage moment data and initial kernel scouts."""
    if not 0 <= panel < len(panel_data):
        raise ValueError("panel index is out of range")
    directory.mkdir(parents=True, exist_ok=True)
    data = panel_data[panel]
    defect = rounded_panel_defect_data(data)
    outers = [rounded_spherical_outer_data(mode) for mode in range(MODES)]
    panel_outer_domain = Fraction(7, 16) * (data.center + data.half_width)
    outer_lengths = [
        choose_outer_truncation_length(outer, panel_outer_domain)
        for outer in outers
    ]
    components: list[ApproxData] = []
    for mode in range(MODES):
        kind = "even" if mode % 2 == 0 else "odd"
        components.append(
            rounded_panel_component_data(
                mode_data,
                data,
                outers[mode],
                kind,
                mode // 2,
                truncation_length=outer_lengths[mode],
                compose_once=True,
            )
        )
    moments = defect_moments_data(defect.coeffs)
    matvecs = [
        hankel_matvec_from_moments_data(moments, component.coeffs)
        for component in components
    ]

    data_module = f"P2RoundedMomentCheckpointData{panel}"
    lines = [
        f"import RHBridge.P2RoundedFlatFactorCheckpointData{panel}",
        "import RHBridge.P2RoundedMomentRefinement",
        "",
        "namespace RHP2Bridge.P2RoundedFactorCheckpointData",
        "",
        "open P2RoundedSharedEvaluator",
        "open P2RoundedTripleMoment",
        "open P2RoundedMomentRefinement",
        "",
        f"def panel{panel}DefectMomentAt : ℕ → ℚ",
    ]
    for row, value in enumerate(moments):
        lines.append(f"  | {row} => {lean_rat_literal(value)}")
    lines.extend(
        [
            "  | _ => 0",
            "",
            f"def panel{panel}DefectMoments : Vector ℚ 297 :=",
            f"  Vector.ofFn fun i => panel{panel}DefectMomentAt i.val",
            "",
        ]
    )
    for mode, matvec in enumerate(matvecs):
        lines.append(f"def panel{panel}Mode{mode}MatVecAt : ℕ → ℚ")
        for row, value in enumerate(matvec):
            lines.append(f"  | {row} => {lean_rat_literal(value)}")
        lines.extend(
            [
                "  | _ => 0",
                "",
                f"def panel{panel}Mode{mode}MatVec : Vector ℚ 149 :=",
                f"  Vector.ofFn fun i => panel{panel}Mode{mode}MatVecAt i.val",
                "",
            ]
        )
    lines.extend(
        [
            f"def panel{panel}MomentData : PanelMomentData where",
            f"  moments := panel{panel}DefectMoments",
            "  matvecs kind i :=",
            "    match kind, i.val with",
        ]
    )
    for kind, parity in (("even", 0), ("odd", 1)):
        for index in range(BLOCK):
            mode = 2 * index + parity
            lines.append(
                f"    | .{kind}, {index} => panel{panel}Mode{mode}MatVec"
            )
    lines.extend(
        [
            f"    | _, _ => panel{panel}Mode0MatVec",
            "",
            "end RHP2Bridge.P2RoundedFactorCheckpointData",
            "",
        ]
    )
    data_path = directory / f"{data_module}.lean"
    data_path.write_text("\n".join(lines), encoding="utf-8")

    # A small proof-only layer shared by the semantic assembly and the raw
    # rational refinement leaves.  Keeping it independent of the moment and
    # matvec checks prevents every 32-entry refinement process from loading
    # the much larger CorrectFor assembly DAG.
    lengths_module = f"P2RoundedMomentLengths{panel}"
    lengths_lines = [
        f"import RHBridge.{data_module}",
        "import RHBridge.P2RoundedBoundedTriple",
        "import RHBridge.P2RoundedPanelTargetDataAll",
        "",
        "namespace RHP2Bridge",
        "",
        "open P2RoundedSharedEvaluator",
        "",
        f"theorem panel{panel}ComponentLengthLe",
        "    (kind : P2SelectedKind) (i : Fin 24) :",
        f"    (P2RoundedFactorCheckpointData.panel{panel}FlatCache.component",
        "      kind i).coeffs.length ≤ 149 := by",
        "  cases kind <;> fin_cases i <;> decide +kernel",
        "",
        f"def panel{panel}BoundedRefinementAt (r : Fin 600) : Prop :=",
        "  let e := P2RoundedSharedEvaluator.generatedEntryAt r",
        "  (P2RoundedBoundedTriple.boundedMomentEntryBall",
        f"    P2RoundedFactorCheckpointData.panel{panel}MomentData",
        f"    P2RoundedFactorCheckpointData.panel{panel}FlatCache",
        f"    ⟨{panel}, by decide⟩",
        "    (p2EntrySelectedKind e.block) e.row e.col",
        f"    (panel{panel}ComponentLengthLe _ _)).Refines",
        "      (P2RoundedPanelRefinement.coarsePanelBall",
        f"        ⟨{panel}, by decide⟩ r)",
        "",
        "end RHP2Bridge",
        "",
    ]
    (directory / f"{lengths_module}.lean").write_text(
        "\n".join(lengths_lines), encoding="utf-8"
    )

    # Each finite arithmetic leaf is a closed half-open range theorem.  This
    # lets the ordinary kernel check a memory-safe chunk, while the semantic
    # assembly below combines chunks without recomputing any rationals.
    moment_chunk_size = chunk_size
    matvec_chunk_size = 32
    refinement_chunk_size = 32

    def chunk_bounds(total: int, size: int) -> list[tuple[int, int]]:
        return [
            (start, min(start + size, total))
            for start in range(0, total, size)
        ]

    def combined_ranges(names: list[str]) -> str:
        if not names:
            raise ValueError("cannot combine an empty range family")
        result = names[0]
        for name in names[1:]:
            result = (
                "P2RoundedGeneratedCertificate.FinRangeAll.combine\n"
                f"        ({result}) {name}"
            )
        return result

    # Put the five independently opaque range theorems in one physical file.
    # Lean checks them sequentially, so the peak remains that of one 64-row
    # reduction while avoiding five separate data-module startup costs.
    moment_module = f"P2RoundedMomentCheckpointCheck{panel}_moments"
    moment_theorems: list[str] = []
    moment_check_lines = [
        f"import RHBridge.{data_module}",
        "import RHBridge.P2RoundedGeneratedCertificate",
        "",
        "namespace RHP2Bridge",
        "",
        "set_option maxRecDepth 100000",
        "set_option maxHeartbeats 50000000",
        "",
    ]
    for start, stop in chunk_bounds(297, moment_chunk_size):
        theorem = f"panel{panel}DefectMomentRange{start}"
        moment_theorems.append(theorem)
        moment_check_lines.extend(
            [
            f"theorem {theorem} :",
            "    P2RoundedGeneratedCertificate.FinRangeAll",
            "      (fun row : Fin 297 =>",
            f"        (P2RoundedFactorCheckpointData.panel{panel}MomentData.moments).get row =",
            "          P2RoundedTripleMoment.momentDot row.val",
            f"            P2RoundedFactorCheckpointData.panel{panel}FlatCache.defect.coeffs)",
            f"      {start} {stop} := by",
            "  unfold P2RoundedGeneratedCertificate.FinRangeAll",
            "  decide +kernel",
            "",
            ]
        )
    moment_check_lines.extend(["end RHP2Bridge", ""])
    (directory / f"{moment_module}.lean").write_text(
        "\n".join(moment_check_lines), encoding="utf-8"
    )

    matvec_modules: list[str] = []
    matvec_theorems: dict[int, list[str]] = {}
    for mode in range(MODES):
        kind = "even" if mode % 2 == 0 else "odd"
        index = mode // 2
        module = f"P2RoundedMomentCheckpointCheck{panel}_mode{mode}"
        matvec_modules.append(module)
        mode_theorems: list[str] = []
        matvec_check_lines = [
            f"import RHBridge.{data_module}",
            "import RHBridge.P2RoundedGeneratedCertificate",
            "",
            "namespace RHP2Bridge",
            "",
            "set_option maxRecDepth 100000",
            "set_option maxHeartbeats 50000000",
            "",
        ]
        for start, stop in chunk_bounds(149, matvec_chunk_size):
            theorem = f"panel{panel}Mode{mode}MatVecRange{start}"
            mode_theorems.append(theorem)
            matvec_check_lines.extend(
                [
                f"theorem {theorem} :",
                "    P2RoundedGeneratedCertificate.FinRangeAll",
                "      (fun row : Fin 149 =>",
                f"        (P2RoundedFactorCheckpointData.panel{panel}MomentData.matvecs",
                f"            .{kind} ⟨{index}, by decide⟩).get row =",
                "          (P2RoundedTripleMoment.hankelMatVecFromMoments",
                f"            P2RoundedFactorCheckpointData.panel{panel}MomentData.moments",
                f"            (P2RoundedFactorCheckpointData.panel{panel}FlatCache.component",
                f"              .{kind} ⟨{index}, by decide⟩).coeffs).get row)",
                f"      {start} {stop} := by",
                "  unfold P2RoundedGeneratedCertificate.FinRangeAll",
                "  decide +kernel",
                "",
                ]
            )
        matvec_check_lines.extend(["end RHP2Bridge", ""])
        (directory / f"{module}.lean").write_text(
            "\n".join(matvec_check_lines), encoding="utf-8"
        )
        matvec_theorems[mode] = mode_theorems

    correct_module = f"P2RoundedMomentCorrect{panel}"
    correct_lines = [
        f"import RHBridge.P2RoundedFlatFactorCheckpoint{panel}",
        f"import RHBridge.{lengths_module}",
        f"import RHBridge.{moment_module}",
        *(f"import RHBridge.{module}" for module in matvec_modules),
        "",
        "namespace RHP2Bridge",
        "",
        "open P2RoundedSharedEvaluator",
        "open P2RoundedMomentRefinement",
        "",
        "set_option maxRecDepth 100000",
        "set_option maxHeartbeats 50000000",
        "",
        "private theorem vector_ext_fin",
        "    {α : Type} {n : Nat} {v w : Vector α n}",
        "    (h : ∀ i : Fin n, v.get i = w.get i) : v = w := by",
        "  apply Vector.ext",
        "  intro i hi",
        "  exact h ⟨i, hi⟩",
        "",
        f"theorem panel{panel}DefectMoments_eq :",
        f"    P2RoundedFactorCheckpointData.panel{panel}MomentData.moments =",
        "      P2RoundedTripleMoment.defectMoments",
        f"        P2RoundedFactorCheckpointData.panel{panel}FlatCache.defect.coeffs := by",
        "  apply vector_ext_fin",
        "  intro row",
        "  rw [P2RoundedTripleMoment.defectMoments_get]",
        "  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall",
        f"    ({combined_ranges(moment_theorems)}) row",
        "",
    ]
    for mode in range(MODES):
        kind = "even" if mode % 2 == 0 else "odd"
        index = mode // 2
        correct_lines.extend(
            [
                f"theorem panel{panel}Mode{mode}MatVec_eq :",
                f"    P2RoundedFactorCheckpointData.panel{panel}MomentData.matvecs",
                f"        .{kind} ⟨{index}, by decide⟩ =",
                "      P2RoundedTripleMoment.hankelMatVecFromMoments",
                f"        P2RoundedFactorCheckpointData.panel{panel}MomentData.moments",
                f"        (P2RoundedFactorCheckpointData.panel{panel}FlatCache.component",
                f"          .{kind} ⟨{index}, by decide⟩).coeffs := by",
                "  apply vector_ext_fin",
                "  intro row",
                "  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall",
                f"    ({combined_ranges(matvec_theorems[mode])}) row",
                "",
            ]
        )
    correct_lines.extend(
        [
            f"theorem panel{panel}MomentData_correct :",
            f"    P2RoundedFactorCheckpointData.panel{panel}MomentData.CorrectFor",
            f"      P2RoundedFactorCheckpointData.panel{panel}FlatCache := by",
            "  apply PanelMomentData.CorrectFor.of_vector_eq",
            f"      panel{panel}DefectMoments_eq panel{panel}ComponentLengthLe",
            "  intro kind i",
            "  cases kind with",
            "  | even =>",
            "      fin_cases i",
        ]
    )
    for index in range(BLOCK):
        correct_lines.append(f"      · exact panel{panel}Mode{2 * index}MatVec_eq")
    correct_lines.extend(
        [
            "  | odd =>",
            "      fin_cases i",
        ]
    )
    for index in range(BLOCK):
        correct_lines.append(
            f"      · exact panel{panel}Mode{2 * index + 1}MatVec_eq"
        )
    correct_lines.extend(["", "end RHP2Bridge", ""])
    (directory / f"{correct_module}.lean").write_text(
        "\n".join(correct_lines), encoding="utf-8"
    )

    refinement_modules: list[str] = []
    refinement_theorems: list[str] = []
    for start, stop in chunk_bounds(600, refinement_chunk_size):
        module = f"P2RoundedMomentRefinementCheck{panel}_{start}"
        theorem = f"panel{panel}BoundedRefinementRange{start}"
        refinement_modules.append(module)
        refinement_theorems.append(theorem)
        check_lines = [
            f"import RHBridge.{lengths_module}",
            "import RHBridge.P2RoundedGeneratedCertificate",
            "",
            "namespace RHP2Bridge",
            "",
            "set_option maxRecDepth 100000",
            "set_option maxHeartbeats 50000000",
            "",
            f"theorem {theorem} :",
            "    P2RoundedGeneratedCertificate.FinRangeAll",
            f"      panel{panel}BoundedRefinementAt",
            f"      {start} {stop} := by",
            "  unfold P2RoundedGeneratedCertificate.FinRangeAll",
            f"    panel{panel}BoundedRefinementAt",
            "    P2RoundedSharedEvaluator.QBall.Refines",
            "  decide +kernel",
            "",
            "end RHP2Bridge",
            "",
        ]
        (directory / f"{module}.lean").write_text(
            "\n".join(check_lines), encoding="utf-8"
        )

    refinement_module = f"P2RoundedMomentRefinement{panel}"
    refinement_lines = [
        f"import RHBridge.{correct_module}",
        *(f"import RHBridge.{module}" for module in refinement_modules),
        "",
        "namespace RHP2Bridge",
        "",
        f"theorem panel{panel}BoundedRefinements :",
        "    ∀ r : Fin 600,",
        "      (P2RoundedBoundedTriple.boundedMomentPanelBall",
        f"        P2RoundedFactorCheckpointData.panel{panel}MomentData",
        f"        P2RoundedFactorCheckpointData.panel{panel}FlatCache",
        f"        ⟨{panel}, by decide⟩ panel{panel}MomentData_correct r).Refines",
        "          (P2RoundedPanelRefinement.coarsePanelBall",
        f"            ⟨{panel}, by decide⟩ r) := by",
        "  intro r",
        "  have hraw := P2RoundedGeneratedCertificate.FinRangeAll.to_forall",
        f"    ({combined_ranges(refinement_theorems)}) r",
        f"  simpa only [panel{panel}BoundedRefinementAt,",
        "    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw",
        "",
        "end RHP2Bridge",
        "",
    ]
    (directory / f"{refinement_module}.lean").write_text(
        "\n".join(refinement_lines), encoding="utf-8"
    )
    print(
        f"wrote staged moment data ({data_path.stat().st_size / 1e6:.2f} MB), "
        f"one five-range moment leaf, {len(matvec_modules)} five-range matvec "
        f"leaves, and {len(refinement_modules)} bounded-refinement leaves "
        f"for panel {panel}",
        flush=True,
    )


def emit_rounded_all_panel_assembly(directory: Path) -> None:
    """Emit the final semantic dispatch and canonical containment theorem."""
    module = "P2RoundedBoundedCertificateCheck"
    lines = [
        *(
            f"import RHBridge.P2RoundedMomentRefinement{panel}"
            for panel in range(PANELS)
        ),
        "",
        "namespace RHP2Bridge",
        "",
        "namespace P2RoundedBoundedCertificate",
        "",
        "open P2RoundedSharedEvaluator",
        "open P2RoundedMomentRefinement",
        "open P2RoundedBoundedTriple",
        "open P2PanelCertificateAggregate",
        "",
        "/-- The 32 generated direct-compose caches, dispatched by canonical panel. -/",
        "def canonicalRoundedCache (k : Fin 32) : PanelCache :=",
        "  match k.val with",
    ]
    for panel in range(PANELS):
        lines.append(
            f"  | {panel} => P2RoundedFactorCheckpointData.panel{panel}FlatCache"
        )
    lines.extend(
        [
            "  | _ => P2RoundedFactorCheckpointData.panel0FlatCache",
            "",
            "/-- The 32 generated exact moment/matvec tables. -/",
            "def canonicalRoundedMomentData (k : Fin 32) : PanelMomentData :=",
            "  match k.val with",
        ]
    )
    for panel in range(PANELS):
        lines.append(
            f"  | {panel} => P2RoundedFactorCheckpointData.panel{panel}MomentData"
        )
    lines.extend(
        [
            "  | _ => P2RoundedFactorCheckpointData.panel0MomentData",
            "",
            "/-- Every staged table is kernel-identified with its exact",
            "moment and Hankel-matvec specification. -/",
            "theorem canonicalRoundedMomentData_correct :",
            "    ∀ k, (canonicalRoundedMomentData k).CorrectFor",
            "      (canonicalRoundedCache k) := by",
            "  intro k",
            "  fin_cases k",
        ]
    )
    for panel in range(PANELS):
        lines.append(f"  · exact panel{panel}MomentData_correct")
    lines.extend(
        [
            "",
            "/-- Every direct-compose cache carries the proved analytic",
            "enclosure of the exact canonical panel factors. -/",
            "theorem canonicalRoundedCache_encloses :",
            "    ∀ k, (canonicalRoundedCache k).EnclosesCanonical k := by",
            "  intro k",
            "  fin_cases k",
        ]
    )
    for panel in range(PANELS):
        lines.append(f"  · exact panel{panel}FlatCache_enclosesCanonical")
    lines.extend(
        [
            "",
            "/-- All 19,200 bounded panel balls refine the residual-aware",
            "generated panel targets. -/",
            "theorem canonicalRoundedBoundedRefinements :",
            "    BoundedMomentPanelTargetRefinements",
            "      canonicalRoundedCache canonicalRoundedMomentData",
            "      canonicalRoundedMomentData_correct := by",
            "  intro k r",
            "  fin_cases k",
        ]
    )
    for panel in range(PANELS):
        lines.extend(
            [
                f"  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using",
                f"      panel{panel}BoundedRefinements r",
            ]
        )
    lines.extend(
        [
            "",
            "/-- Canonical aggregate band certificates obtained from the",
            "bounded analytic ledger and the ordinary-kernel rational leaves. -/",
            "theorem roundedBandSumCertificates : BandSumCertificates := by",
            "  exact bandSumCertificates_of_boundedMomentTargetRefinements",
            "    canonicalRoundedCache canonicalRoundedMomentData",
            "    canonicalRoundedMomentData_correct",
            "    canonicalRoundedCache_encloses",
            "    canonicalRoundedBoundedRefinements",
            "",
            "/-- Unconditional canonical `p = 2` matrix containment through",
            "the direct-compose, bounded-value certificate architecture. -/",
            "theorem p2_canonical_matrix_containment :",
            "    (∀ i j,",
            "      FullInfClipped48Real.evenLowerReal i j ≤",
            "          FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ∧",
            "        FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ≤",
            "          FullInfClipped48Real.evenUpperReal i j) ∧",
            "    (∀ i j,",
            "      FullInfClipped48Real.oddLowerReal i j ≤",
            "          FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ∧",
            "        FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ≤",
            "          FullInfClipped48Real.oddUpperReal i j) := by",
            "  exact p2_matrix_containment_of_bandSumCertificates",
            "    roundedBandSumCertificates",
            "",
            "/-- The closed containment theorem discharges the final finite premise",
            "of the fixed-window clipped endpoint theorem. -/",
            "theorem p2_canonical_clipped_endpoint",
            "    {f : FullInfP2Endpoint.P2IntervalL2} (hf : f ≠ 0) :",
            "    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2ClippedForm f f := by",
            "  exact p2_clipped_endpoint_of_matrix_containment_no_parity",
            "    p2_canonical_matrix_containment.1",
            "    p2_canonical_matrix_containment.2 hf",
            "",
            "end P2RoundedBoundedCertificate",
            "",
            "end RHP2Bridge",
            "",
        ]
    )
    (directory / f"{module}.lean").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    print(f"wrote final all-panel assembly {module}.lean", flush=True)


def emit_lean(path: Path, entries: list[EntryResult]) -> None:
    """Emit compact final-center data for the subsequent Lean proof layer."""
    even_values = []
    odd_values = []
    even_panel_values = []
    odd_panel_values = []
    even_band_values = []
    odd_band_values = []
    for entry in entries:
        value = entry.rounded_center.numerator * (FINAL_DEN // entry.rounded_center.denominator)
        target = even_values if entry.block == "even" else odd_values
        target.append(((entry.row, entry.col), value))
        panel_target = (
            even_panel_values if entry.block == "even" else odd_panel_values
        )
        panel_target.extend(
            ((panel, entry.row, entry.col), numerator)
            for panel, numerator in enumerate(entry.panel_integral_numerators)
        )
        band_target = even_band_values if entry.block == "even" else odd_band_values
        band_target.append(
            ((entry.row, entry.col), sum(entry.panel_integral_numerators))
        )

    worst_error = max(
        EMITTED_ANALYTIC_RADIUS,
        max(entry.analytic_error + entry.center_rounding_error for entry in entries),
    )
    outward_error_integer = ceil_scaled(worst_error, FINAL_DEN)
    body = f"""/-
Generated exact-rational center data for the canonical p=2 panel certificate.

This file contains data only.  Its consumer must prove, in Lean, that the
analytic entries lie within `p2PanelAnalyticRadius` of these centers.
Generated by lean/make_p2_panel_certificate.py.
-/
import RHBridge.P2EntryCertificate

namespace RHP2Bridge.P2PanelCertificateData

def centerScale : Nat := 10 ^ 30
def bandIntegralScale : Nat := 10 ^ 40
def panelGridRoundingRadius : ℚ := 32 / (2 * bandIntegralScale)
/-- Deliberately widened checker radius.  The exact panel-grid loss is only
`panelGridRoundingRadius`; this simpler denominator makes the dense rational
comparison substantially cheaper. -/
def bandIntegralRoundingRadius : ℚ := 1 / 10 ^ 15
theorem panelGridRoundingRadius_le :
    panelGridRoundingRadius ≤ bandIntegralRoundingRadius := by
  norm_num [panelGridRoundingRadius, bandIntegralRoundingRadius,
    bandIntegralScale]
def analyticRadiusNumerator : Nat := {outward_error_integer}
def storedRadiusNumerator : Nat := 10 ^ 18
def storedScaleMultiplier : Int := 10 ^ 12
def betaScaledNumerator : Int := 227 * 10 ^ 23

{lean_int_function("evenCenterNumerator", even_values)}

{lean_int_function("oddCenterNumerator", odd_values)}

/- Sum of all 32 exact canonical panel integrals after rounding each panel to
the `10^-40` grid.  The actual total grid loss is at most
`panelGridRoundingRadius = 32/(2*10^40)`. -/
{lean_int_function("evenBandIntegralNumerator", even_band_values)}

{lean_int_function("oddBandIntegralNumerator", odd_band_values)}

def evenBandIntegralQ (i j : Fin 24) : ℚ :=
  evenBandIntegralNumerator i.val j.val / bandIntegralScale

def oddBandIntegralQ (i j : Fin 24) : ℚ :=
  oddBandIntegralNumerator i.val j.val / bandIntegralScale

/-- Exact-arithmetic target for the dense even-panel checker. -/
def EvenBandIntegralSumCertificate
    (exact : Fin 24 → Fin 24 → ℚ) : Prop :=
  ∀ i j, i ≤ j →
    |exact i j - evenBandIntegralQ i j| ≤ bandIntegralRoundingRadius

/-- Exact-arithmetic target for the dense odd-panel checker. -/
def OddBandIntegralSumCertificate
    (exact : Fin 24 → Fin 24 → ℚ) : Prop :=
  ∀ i j, i ≤ j →
    |exact i j - oddBandIntegralQ i j| ≤ bandIntegralRoundingRadius

def evenStoredCenterNumerator (i j : Nat) : Int :=
  FullInfClipped48.evenAFun i j * storedScaleMultiplier +
    if i = j then betaScaledNumerator else 0

def oddStoredCenterNumerator (i j : Nat) : Int :=
  FullInfClipped48.oddAFun i j * storedScaleMultiplier +
    if i = j then betaScaledNumerator else 0

set_option maxRecDepth 4096 in
/-- Pure integer verification that every generated even upper-triangular
center, enlarged by the common analytic radius, fits in the stored radius. -/
theorem evenCenterFitsStored : ∀ i j : Fin 24, i ≤ j →
    Int.natAbs (evenCenterNumerator i.val j.val -
      evenStoredCenterNumerator i.val j.val) + analyticRadiusNumerator ≤
        storedRadiusNumerator := by
  decide

set_option maxRecDepth 4096 in
/-- Odd-block analogue of `evenCenterFitsStored`. -/
theorem oddCenterFitsStored : ∀ i j : Fin 24, i ≤ j →
    Int.natAbs (oddCenterNumerator i.val j.val -
      oddStoredCenterNumerator i.val j.val) + analyticRadiusNumerator ≤
        storedRadiusNumerator := by
  decide

end RHP2Bridge.P2PanelCertificateData
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    print(f"wrote {path} ({len(body) / 1e6:.2f} MB)")


def report(entries: list[EntryResult], panel_data: list[PanelData]) -> bool:
    worst_discrepancy = max(entries, key=lambda entry: entry.discrepancy)
    worst_required = max(entries, key=lambda entry: entry.total_required_radius)
    worst_band = max(entries, key=lambda entry: entry.band_error)
    worst_pole = max(entries, key=lambda entry: entry.pole_error)
    max_prefix = max(panel.prefix_error for panel in panel_data)
    max_round = max(panel.coefficient_error for panel in panel_data)
    max_rho = max(panel.max_rho for panel in panel_data)

    print("\nexact-rational scout summary")
    print(f"  entries checked:                  {len(entries)}")
    print(f"  maximum panel rho:               {decimal(max_rho, 10)}")
    print(f"  maximum reciprocal-tail error:   {decimal(max_prefix, 10)}")
    print(f"  maximum defect coefficient loss: {decimal(max_round, 10)}")
    print(
        "  worst center discrepancy:         "
        f"{decimal(worst_discrepancy.discrepancy, 12)} "
        f"at {worst_discrepancy.block}[{worst_discrepancy.row},{worst_discrepancy.col}]"
    )
    print(
        "  worst band analytic error:        "
        f"{decimal(worst_band.band_error, 12)} "
        f"at {worst_band.block}[{worst_band.row},{worst_band.col}]"
    )
    print(
        "  worst pole analytic error:        "
        f"{decimal(worst_pole.pole_error, 12)} "
        f"at {worst_pole.block}[{worst_pole.row},{worst_pole.col}]"
    )
    print(
        "  worst discrepancy + ledger:       "
        f"{decimal(worst_required.total_required_radius, 12)} "
        f"at {worst_required.block}[{worst_required.row},{worst_required.col}]"
    )
    print(f"  stored radius:                    {decimal(STORED_RADIUS, 12)}")
    print(f"  remaining worst-case margin:      {decimal(STORED_RADIUS - worst_required.total_required_radius, 12)}")

    print("\nworst-entry outward rational ledger (denominator 10^30)")
    print(f"  block/index:          {worst_required.block}[{worst_required.row},{worst_required.col}]")
    print(f"  center discrepancy:   {outward_decimal_fraction(worst_required.discrepancy)}")
    print(f"  center rounding:      {outward_decimal_fraction(worst_required.center_rounding_error)}")
    print(f"  band error:           {outward_decimal_fraction(worst_required.band_error)}")
    print(f"  pole error:           {outward_decimal_fraction(worst_required.pole_error)}")
    diagonal_alpha = ALPHA_RADIUS if worst_required.row == worst_required.col else 0
    print(f"  alpha error:          {outward_decimal_fraction(diagonal_alpha)}")
    print(f"  total required:       {outward_decimal_fraction(worst_required.total_required_radius)}")

    passed = all(entry.total_required_radius < STORED_RADIUS for entry in entries)
    print(f"\ncontainment margins: {'PASS' if passed else 'FAIL'}")
    return passed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--emit-lean",
        type=Path,
        help="write compact generated center data after a successful scout",
    )
    parser.add_argument(
        "--emit-pole-lean",
        type=Path,
        help="write the 48 exact rational pole-coefficient targets",
    )
    parser.add_argument(
        "--pole-only",
        action="store_true",
        help="stop after building and optionally emitting the 48 pole targets",
    )
    parser.add_argument(
        "--emit-pole-checks",
        type=Path,
        help="write split kernel-check modules for the 48 pole targets",
    )
    parser.add_argument(
        "--emit-rounded-panel-targets",
        type=Path,
        help="write 32 exact panel-center checkpoint tables",
    )
    parser.add_argument(
        "--emit-rounded-factor-checkpoints",
        type=Path,
        help="write explicit rounded factor caches and split kernel checks",
    )
    parser.add_argument(
        "--emit-rounded-flat-factor-checkpoints",
        type=Path,
        help="write materialized factor-cache literals and split equality checks",
    )
    parser.add_argument(
        "--emit-rounded-moment-checkpoints",
        type=Path,
        help="write staged exact moment/matvec data and initial kernel scouts",
    )
    parser.add_argument(
        "--scout-rounded-tail-thresholds",
        type=Path,
        metavar="LEAN_DATA_DIRECTORY",
        help=(
            "exactly scout all 32x600 staged panel balls at outer-tail "
            "thresholds 1e-30, 1e-24, 1e-22, 1e-21, and 1e-20"
        ),
    )
    parser.add_argument(
        "--scout-rounded-architectures",
        type=Path,
        metavar="LEAN_DATA_DIRECTORY",
        help=(
            "compare recursive-Horner and one-shot exact composition grids "
            "over all 32x600 panel targets"
        ),
    )
    parser.add_argument(
        "--scout-rounded-production-candidate",
        type=Path,
        metavar="LEAN_DATA_DIRECTORY",
        help=(
            "scout only the direct-compose grid40/outer220/tail1e-22 "
            "production candidate over all panel targets"
        ),
    )
    parser.add_argument(
        "--flat-panel-count",
        type=int,
        default=1,
        help="number of leading flat panel caches to emit (default: one)",
    )
    parser.add_argument(
        "--flat-panel",
        type=int,
        action="append",
        help=(
            "emit this zero-based flat panel instead of a leading prefix; "
            "may be repeated"
        ),
    )
    parser.add_argument(
        "--moment-panel",
        type=int,
        action="append",
        help=(
            "zero-based panel for staged moment emission; may be repeated "
            "(default: panel zero)"
        ),
    )
    parser.add_argument(
        "--all-moment-panels",
        action="store_true",
        help=(
            "emit staged moment/refinement leaves for all 32 panels and the "
            "final canonical containment assembly"
        ),
    )
    parser.add_argument(
        "--factors-only",
        action="store_true",
        help="stop after building and optionally emitting rounded factor caches",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=min(8, multiprocessing.cpu_count()),
        help="parallel exact-integration worker processes (default: up to 8)",
    )
    parser.add_argument(
        "--round-local-polynomials",
        action="store_true",
        help=(
            "use the older 1e-40 coefficient-grid scout; by default centers "
            "come from the exact unrounded canonical rational polynomials"
        ),
    )
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be positive")
    if not 1 <= args.flat_panel_count <= 32:
        parser.error("--flat-panel-count must lie between 1 and 32")
    if args.flat_panel is not None and any(
        not 0 <= panel < 32 for panel in args.flat_panel
    ):
        parser.error("--flat-panel values must lie between 0 and 31")
    if args.moment_panel is not None and any(
        not 0 <= panel < PANELS for panel in args.moment_panel
    ):
        parser.error("--moment-panel values must lie between 0 and 31")
    if args.all_moment_panels and args.moment_panel is not None:
        parser.error("--all-moment-panels cannot be combined with --moment-panel")

    print("building exact mode constants", flush=True)
    mode_data = build_mode_data()
    if args.emit_pole_lean is not None:
        emit_pole_lean(args.emit_pole_lean, mode_data)
    if args.emit_pole_checks is not None:
        emit_pole_check_modules(args.emit_pole_checks)
    if args.pole_only:
        if args.emit_pole_lean is None and args.emit_pole_checks is None:
            parser.error("--pole-only requires a pole emission option")
        return 0
    print("building exact rational panel polynomials", flush=True)
    panel_data = build_panel_data(
        mode_data, round_local_polynomials=args.round_local_polynomials
    )
    if args.emit_rounded_factor_checkpoints is not None:
        emit_rounded_factor_checkpoints(
            args.emit_rounded_factor_checkpoints, panel_data
        )
    if args.emit_rounded_flat_factor_checkpoints is not None:
        emit_rounded_flat_factor_checkpoints(
            args.emit_rounded_flat_factor_checkpoints,
            mode_data,
            panel_data,
            panel_count=args.flat_panel_count,
            panel_indices=args.flat_panel,
        )
    if args.emit_rounded_moment_checkpoints is not None:
        moment_panels = (
            list(range(PANELS))
            if args.all_moment_panels
            else sorted(set(args.moment_panel or [0]))
        )
        for panel in moment_panels:
            emit_rounded_moment_checkpoint_scout(
                args.emit_rounded_moment_checkpoints,
                mode_data,
                panel_data,
                panel=panel,
            )
        if moment_panels == list(range(PANELS)):
            emit_rounded_all_panel_assembly(
                args.emit_rounded_moment_checkpoints
            )
    if args.scout_rounded_tail_thresholds is not None:
        passed = scout_rounded_tail_thresholds(
            args.scout_rounded_tail_thresholds,
            mode_data,
            panel_data,
            (
                Fraction(1, 10**30),
                Fraction(1, 10**24),
                Fraction(1, 10**22),
                Fraction(1, 10**21),
                Fraction(1, 10**20),
            ),
        )
        return 0 if passed else 1
    if args.scout_rounded_architectures is not None:
        passed = scout_rounded_composition_architectures(
            args.scout_rounded_architectures, mode_data, panel_data
        )
        return 0 if passed else 1
    if args.scout_rounded_production_candidate is not None:
        passed = scout_rounded_composition_architectures(
            args.scout_rounded_production_candidate,
            mode_data,
            panel_data,
            [("B-once-c40-o220-t22", True, 40, 40, 220, 22, True)],
        )
        return 0 if passed else 1
    if args.factors_only:
        if (
            args.emit_rounded_factor_checkpoints is None
            and args.emit_rounded_flat_factor_checkpoints is None
            and args.emit_rounded_moment_checkpoints is None
        ):
            parser.error(
                "--factors-only requires a rounded-factor emission option"
            )
        return 0
    print("integrating 600 rational entries", flush=True)
    entries = build_entries(mode_data, panel_data, args.workers)
    passed = report(entries, panel_data)

    if args.emit_lean is not None:
        if not passed:
            print("refusing to emit Lean data because a containment margin failed", file=sys.stderr)
            return 1
        emit_lean(args.emit_lean, entries)
    if args.emit_rounded_panel_targets is not None:
        if not passed:
            print(
                "refusing to emit panel targets because a containment margin failed",
                file=sys.stderr,
            )
            return 1
        emit_rounded_panel_targets(args.emit_rounded_panel_targets, entries)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
