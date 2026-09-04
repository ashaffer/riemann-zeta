"""Exact ledger and bounded replay for the open global conductor L4 gate.

The analytic theorem ``GCG4(161/1000, 3/8)`` is not proved here.  This
module does two narrower jobs:

* verify the rational exponent arithmetic in its deterministic adapter;
* replay a floating fourth-moment diagnostic on the four already-frozen
  prime-hat scales, using the exact edge-deletion rule.

The finite replay is a FLOAT-SCOUT.  In particular, it cannot extrapolate a
power saving, and at the licensed scales the cutoff retains only twin-prime
edges.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Sequence

from flint import arb, ctx
import numpy as np

from prime_log_hat_tail import (
    TILT,
    WIDTH,
    build_prime_hat_vector,
    float_arb_exact,
    fraction_arb,
    integrate_hat_segment,
    jitter_control,
    odd_half_grid_control,
)


THETA = Fraction(161, 1000)
LOWER_EXPONENT = 1 - THETA
APERTURE = Fraction(50, 33)
CONDUCTOR_EXPONENT = Fraction(13, 8)
CONDUCTOR_GAIN = Fraction(3, 8)
TARGET_C = Fraction(19, 1000)

TAIL_SAVING = Fraction(249, 13000)
L2_SAVING = Fraction(2789, 3250)
MOMENT_DECAY = Fraction(1187, 13000)
PERSISTENCE_POWER = Fraction(9, 2)
PERSISTENCE_DECAY = PERSISTENCE_POWER * TARGET_C
STRICT_MARGIN = MOMENT_DECAY - PERSISTENCE_DECAY
REQUIRED_GAIN = 2 - 2 * L2_SAVING + PERSISTENCE_DECAY
OUTPUT_SAVING = MOMENT_DECAY / PERSISTENCE_POWER

FROZEN_CENTERS = (
    Fraction(1025, 2),
    Fraction(2049, 2),
    Fraction(4097, 2),
    Fraction(8193, 2),
)


def gt_tail_saving(theta: Fraction) -> Fraction:
    """Audited Gafni--Tao tail exponent on the relevant branch."""

    return (45 * theta - 6) / 65


def retained_l2_saving(theta: Fraction) -> Fraction:
    """Exponent q in ``sum lambda_p^2 << Y^(-q+o(1))``."""

    return (59 - 20 * theta) / 65


def required_conductor_gain(
    theta: Fraction,
    point_exponent: Fraction,
) -> Fraction:
    """Strict conductor gain needed by fourth-moment persistence."""

    return 2 - 2 * retained_l2_saving(theta) + Fraction(9, 2) * point_exponent


def ledger_closes_conditionally() -> bool:
    """Check all strict exponent inequalities, conditional on GCG4."""

    return (
        TAIL_SAVING > TARGET_C
        and CONDUCTOR_GAIN > REQUIRED_GAIN
        and MOMENT_DECAY > PERSISTENCE_DECAY
        and OUTPUT_SAVING > TARGET_C
    )


def ledger_payload() -> dict[str, str | bool]:
    """Return the exact rational adapter ledger."""

    return {
        "theta": str(THETA),
        "lower_exponent": str(LOWER_EXPONENT),
        "aperture": str(APERTURE),
        "conductor_exponent": str(CONDUCTOR_EXPONENT),
        "conductor_gain": str(CONDUCTOR_GAIN),
        "tail_saving": str(TAIL_SAVING),
        "l2_saving": str(L2_SAVING),
        "moment_decay": str(MOMENT_DECAY),
        "persistence_decay": str(PERSISTENCE_DECAY),
        "strict_margin": str(STRICT_MARGIN),
        "required_gain": str(REQUIRED_GAIN),
        "output_saving": str(OUTPUT_SAVING),
        "target": str(TARGET_C),
        "closes_conditionally": ledger_closes_conditionally(),
        "gcg4_status": "OPEN",
    }


@dataclass(frozen=True)
class RetainedHatVector:
    """Nodal vector obtained by retaining a specified set of edges."""

    nodes: tuple[arb, ...]
    raw_weights: tuple[arb, ...]
    weights: tuple[arb, ...]
    retained_mass: arb
    kept_edges: tuple[bool, ...]

    @property
    def float_nodes(self) -> np.ndarray:
        return np.array([float(value.mid()) for value in self.nodes])

    @property
    def float_weights(self) -> np.ndarray:
        values = np.array([float(value.mid()) for value in self.weights])
        return values / np.sum(values)

    @property
    def active_count(self) -> int:
        return sum(value.lower() > 0 for value in self.raw_weights)


def retained_hat_vector_from_arb_nodes(
    nodes: Sequence[arb],
    kept_edges: Sequence[bool],
) -> RetainedHatVector:
    """Delete both nodal shares of every rejected finite-element edge."""

    if len(nodes) < 2 or len(kept_edges) != len(nodes) - 1:
        raise ValueError("edge mask must have length len(nodes)-1")
    if not any(kept_edges):
        raise ValueError("at least one edge must be retained")
    for left, right in zip(nodes, nodes[1:]):
        if not left < right:
            raise ValueError("nodes must be strictly increasing")

    width = fraction_arb(WIDTH)
    alpha = fraction_arb(TILT)
    raw = [arb(0) for _ in nodes]
    for index, keep in enumerate(kept_edges):
        if not keep:
            continue
        left = nodes[index]
        right = nodes[index + 1]
        denominator = right - left
        # Left endpoint hat: (right-u)/(right-left).
        raw[index] += integrate_hat_segment(
            left,
            right,
            right / denominator,
            -1 / denominator,
            width,
            alpha,
        )
        # Right endpoint hat: (u-left)/(right-left).
        raw[index + 1] += integrate_hat_segment(
            left,
            right,
            -left / denominator,
            1 / denominator,
            width,
            alpha,
        )

    mass = sum(raw, arb(0))
    if not mass.lower() > 0:
        raise ArithmeticError("retained edge mass is not certified positive")
    weights = tuple(value / mass for value in raw)
    if not sum(weights, arb(0)).contains(1):
        raise ArithmeticError("retained weights do not enclose unit mass")
    return RetainedHatVector(
        tuple(nodes),
        tuple(raw),
        weights,
        mass,
        tuple(bool(value) for value in kept_edges),
    )


def retained_hat_vector_from_float_nodes(
    nodes: np.ndarray,
    kept_edges: Sequence[bool],
    *,
    precision_bits: int = 160,
) -> RetainedHatVector:
    """Recompute retained control weights from frozen binary floats."""

    ctx.prec = precision_bits
    exact_nodes = tuple(float_arb_exact(float(value)) for value in nodes)
    return retained_hat_vector_from_arb_nodes(exact_nodes, kept_edges)


def certified_physical_gap_mask(
    center: Fraction,
    primes: Sequence[int],
    theta: Fraction = THETA,
) -> tuple[tuple[bool, ...], arb]:
    """Certify ``p_{j+1}-p_j <= Y^theta`` edge by edge."""

    cutoff = (fraction_arb(center).log() * fraction_arb(theta)).exp()
    mask: list[bool] = []
    for left, right in zip(primes, primes[1:]):
        gap = arb(int(right - left))
        if gap <= cutoff:
            mask.append(True)
        elif gap > cutoff:
            mask.append(False)
        else:
            raise ArithmeticError("physical gap comparison is ambiguous")
    return tuple(mask), cutoff


def l4_trapezoid(
    nodes: np.ndarray,
    weights: np.ndarray,
    left: float,
    right: float,
    *,
    maximum_step: float = 2.0,
    chunk_size: int = 8192,
) -> float:
    """Floating trapezoid integral of a complex polynomial's fourth power.

    All present nodes lie in ``[-1/5,1/5]``, so ``|F|^4`` has bandwidth at
    most ``4/5``.  The default step is below its Nyquist spacing.  This is
    nevertheless a numerical scout, not interval-certified quadrature.
    """

    nodes = np.asarray(nodes, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if nodes.ndim != 1 or weights.shape != nodes.shape:
        raise ValueError("nodes and weights must be matching vectors")
    if not right > left or maximum_step <= 0 or chunk_size < 2:
        raise ValueError("invalid integration parameters")

    active = weights > 0
    nodes = nodes[active]
    weights = weights[active]
    interval_count = max(1, math.ceil((right - left) / maximum_step))
    step = (right - left) / interval_count
    step_phase = np.exp(1j * nodes * step)

    reusable = min(chunk_size, interval_count + 1)
    powers = np.empty((reusable, len(nodes)), dtype=np.complex128)
    powers[0] = 1.0
    if reusable > 1:
        broadcast_steps = np.broadcast_to(
            step_phase,
            (reusable - 1, len(nodes)),
        )
        np.cumprod(broadcast_steps, axis=0, out=powers[1:])

    total = 0.0
    offset = 0
    while offset <= interval_count:
        count = min(reusable, interval_count + 1 - offset)
        base = np.exp(1j * nodes * (left + offset * step))
        values = (powers[:count] * base) @ weights
        integrand = np.abs(values) ** 4
        if offset == 0:
            integrand[0] *= 0.5
        if offset + count - 1 == interval_count:
            integrand[-1] *= 0.5
        total += float(np.sum(integrand))
        offset += count
    return step * total


def sign_morphology_trapezoid(
    nodes: np.ndarray,
    weights: np.ndarray,
    left: float,
    right: float,
    *,
    maximum_step: float = 2.0,
    chunk_size: int = 8192,
) -> dict[str, float]:
    """Compare complex, real, and negative-real fourth-moment mass."""

    nodes = np.asarray(nodes, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if nodes.ndim != 1 or weights.shape != nodes.shape:
        raise ValueError("nodes and weights must be matching vectors")
    if not right > left or maximum_step <= 0 or chunk_size < 2:
        raise ValueError("invalid integration parameters")
    active = weights > 0
    nodes = nodes[active]
    weights = weights[active]
    interval_count = max(1, math.ceil((right - left) / maximum_step))
    step = (right - left) / interval_count
    step_phase = np.exp(1j * nodes * step)
    reusable = min(chunk_size, interval_count + 1)
    powers = np.empty((reusable, len(nodes)), dtype=np.complex128)
    powers[0] = 1.0
    if reusable > 1:
        broadcast_steps = np.broadcast_to(
            step_phase,
            (reusable - 1, len(nodes)),
        )
        np.cumprod(broadcast_steps, axis=0, out=powers[1:])

    totals = np.zeros(3, dtype=float)
    offset = 0
    while offset <= interval_count:
        count = min(reusable, interval_count + 1 - offset)
        base = np.exp(1j * nodes * (left + offset * step))
        values = (powers[:count] * base) @ weights
        real_values = np.real(values)
        integrands = np.vstack(
            (
                np.abs(values) ** 4,
                real_values**4,
                np.maximum(-real_values, 0.0) ** 4,
            )
        )
        if offset == 0:
            integrands[:, 0] *= 0.5
        if offset + count - 1 == interval_count:
            integrands[:, -1] *= 0.5
        totals += np.sum(integrands, axis=1)
        offset += count
    totals *= step
    return {
        "complex_l4": float(totals[0]),
        "real_l4": float(totals[1]),
        "negative_real_l4": float(totals[2]),
        "real_to_complex": float(totals[1] / totals[0]),
        "negative_to_real": float(totals[2] / totals[1]),
    }


def four_distinct_sharp_moment(
    nodes: np.ndarray,
    weights: np.ndarray,
    left: float,
    right: float,
    *,
    block_size: int = 512,
) -> float:
    """Isolate the all-four-indices-distinct term for a sharp interval.

    Writing unordered pairs as ``p<r`` gives the exact contribution

    ``4 sum_{p<r,q<s, {p,r} disjoint {q,s}} w_p w_r w_q w_s K``,

    where ``K`` is the integral of ``exp(it(v_p+v_r-v_q-v_s))``.  The
    calculation is quadratic in the number of unordered active pairs and is
    used only as a finite scout.
    """

    nodes = np.asarray(nodes, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if nodes.shape != weights.shape or nodes.ndim != 1 or not right > left:
        raise ValueError("invalid vector or interval")
    active = np.flatnonzero(weights > 0)
    if len(active) < 4:
        return 0.0
    pair_left, pair_right = np.triu_indices(len(active), k=1)
    indices_left = active[pair_left]
    indices_right = active[pair_right]
    frequencies = nodes[indices_left] + nodes[indices_right]
    coefficients = weights[indices_left] * weights[indices_right]

    length = right - left
    midpoint = (left + right) / 2
    total = 0.0 + 0.0j
    pair_count = len(frequencies)
    for start in range(0, pair_count, block_size):
        stop = min(start + block_size, pair_count)
        omega = frequencies[start:stop, None] - frequencies[None, :]
        disjoint = (
            (indices_left[start:stop, None] != indices_left[None, :])
            & (indices_left[start:stop, None] != indices_right[None, :])
            & (indices_right[start:stop, None] != indices_left[None, :])
            & (indices_right[start:stop, None] != indices_right[None, :])
        )
        kernel = (
            length
            * np.sinc(omega * length / (2 * math.pi))
            * np.exp(1j * omega * midpoint)
        )
        coefficient_products = (
            coefficients[start:stop, None] * coefficients[None, :]
        )
        total += np.sum(coefficient_products[disjoint] * kernel[disjoint])
    result = 4 * total
    tolerance = 1e-9 * max(1.0, abs(result.real))
    if abs(result.imag) > tolerance:
        raise ArithmeticError("four-distinct conjugate cancellation was unstable")
    return float(result.real)


def four_distinct_integrand(
    nodes: np.ndarray,
    weights: np.ndarray,
    times: np.ndarray,
) -> np.ndarray:
    """Pointwise all-four-indices-distinct part without an O(N^4) loop.

    If ``M=sum w_p z_p``, ``Q=sum w_p^2 z_p^2`` and
    ``A3=sum w_p^3 z_p``, exact incidence subtraction gives

    ``C4 = |M^2-Q|^2 - 4 S2 |M|^2 + 8 Re(M conj(A3))
            + 2 S2^2 - 6 S4``.

    This algebraic identity does not bound ``C4``; the contribution may have
    either sign after pointwise sector subtraction.
    """

    nodes = np.asarray(nodes, dtype=float)
    weights = np.asarray(weights, dtype=float)
    times = np.asarray(times, dtype=float)
    if nodes.ndim != 1 or weights.shape != nodes.shape or times.ndim != 1:
        raise ValueError("expected matching vectors and a time vector")
    phases = np.exp(1j * times[:, None] * nodes[None, :])
    moment = phases @ weights
    square_polynomial = (phases * phases) @ (weights * weights)
    cubic_polynomial = phases @ (weights**3)
    s2 = float(np.sum(weights * weights))
    s4 = float(np.sum(weights**4))
    return (
        np.abs(moment * moment - square_polynomial) ** 2
        - 4 * s2 * np.abs(moment) ** 2
        + 8 * np.real(moment * np.conjugate(cubic_polynomial))
        + 2 * s2 * s2
        - 6 * s4
    )


def four_distinct_trapezoid(
    nodes: np.ndarray,
    weights: np.ndarray,
    left: float,
    right: float,
    *,
    maximum_step: float = 2.0,
    chunk_size: int = 8192,
) -> float:
    """FLOAT-SCOUT integral of the fast four-distinct identity."""

    nodes = np.asarray(nodes, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if nodes.ndim != 1 or weights.shape != nodes.shape:
        raise ValueError("nodes and weights must be matching vectors")
    if not right > left or maximum_step <= 0 or chunk_size < 2:
        raise ValueError("invalid integration parameters")
    active = weights > 0
    nodes = nodes[active]
    weights = weights[active]

    interval_count = max(1, math.ceil((right - left) / maximum_step))
    step = (right - left) / interval_count
    step_phase = np.exp(1j * nodes * step)
    reusable = min(chunk_size, interval_count + 1)
    powers = np.empty((reusable, len(nodes)), dtype=np.complex128)
    powers[0] = 1.0
    if reusable > 1:
        broadcast_steps = np.broadcast_to(
            step_phase,
            (reusable - 1, len(nodes)),
        )
        np.cumprod(broadcast_steps, axis=0, out=powers[1:])

    s2 = float(np.sum(weights * weights))
    s4 = float(np.sum(weights**4))
    total = 0.0
    offset = 0
    while offset <= interval_count:
        count = min(reusable, interval_count + 1 - offset)
        base = np.exp(1j * nodes * (left + offset * step))
        phases = powers[:count] * base
        moment = phases @ weights
        square_polynomial = (phases * phases) @ (weights * weights)
        cubic_polynomial = phases @ (weights**3)
        integrand = (
            np.abs(moment * moment - square_polynomial) ** 2
            - 4 * s2 * np.abs(moment) ** 2
            + 8 * np.real(moment * np.conjugate(cubic_polynomial))
            + 2 * s2 * s2
            - 6 * s4
        )
        if offset == 0:
            integrand[0] *= 0.5
        if offset + count - 1 == interval_count:
            integrand[-1] *= 0.5
        total += float(np.sum(integrand))
        offset += count
    return step * total


def _dyadic_windows(lower: float, aperture: float) -> list[tuple[str, float, float]]:
    windows: list[tuple[str, float, float]] = []
    left = lower
    index = 0
    while left < aperture:
        right = min(2 * left, aperture)
        windows.append((f"lower_{index}", left, right))
        left = right
        index += 1
    windows.append(("top", aperture, 2 * aperture))
    return windows


def moment_profile(
    nodes: np.ndarray,
    weights: np.ndarray,
    center: float,
    *,
    maximum_step: float = 2.0,
) -> dict[str, object]:
    """Compute dyadic, top-window, and global FLOAT-SCOUT statistics."""

    lower = center ** float(LOWER_EXPONENT)
    aperture = center ** float(APERTURE)
    conductor = center ** float(CONDUCTOR_EXPONENT)
    s2 = float(np.sum(weights * weights))
    s4 = float(np.sum(weights**4))
    diagonal_density = 2 * s2 * s2 - s4
    windows: list[dict[str, float | str]] = []
    global_moment = 0.0
    global_four_distinct = 0.0
    top_moment = math.nan
    top_four_distinct = math.nan
    for name, left, right in _dyadic_windows(lower, aperture):
        moment = l4_trapezoid(
            nodes,
            weights,
            left,
            right,
            maximum_step=maximum_step,
        )
        four_distinct = four_distinct_trapezoid(
            nodes,
            weights,
            left,
            right,
            maximum_step=maximum_step,
        )
        diagonal_mass = (right - left) * diagonal_density
        payload = {
            "name": name,
            "left": left,
            "right": right,
            "moment": moment,
            "diagonal_mass": diagonal_mass,
            "off_diagonal_excess": moment - diagonal_mass,
            "moment_to_diagonal": moment / diagonal_mass,
            "norm_sensitive_ratio": moment / ((left + conductor) * s2 * s2),
            "four_distinct": four_distinct,
            "four_distinct_to_moment": four_distinct / moment,
            "four_distinct_norm_sensitive_ratio": (
                four_distinct / ((left + conductor) * s2 * s2)
            ),
        }
        windows.append(payload)
        global_moment += moment
        global_four_distinct += four_distinct
        if name == "top":
            top_moment = moment
            top_four_distinct = four_distinct

    target_power = center ** (-float(MOMENT_DECAY))
    return {
        "trust": "FLOAT-SCOUT",
        "maximum_step": maximum_step,
        "lower": lower,
        "aperture_B": aperture,
        "upper": 2 * aperture,
        "s2": s2,
        "s4": s4,
        "diagonal_density": diagonal_density,
        "windows": windows,
        "top_moment": top_moment,
        "top_four_distinct": top_four_distinct,
        "global_moment": global_moment,
        "global_four_distinct": global_four_distinct,
        "global_norm_sensitive_ratio": (
            global_moment / ((aperture + conductor) * s2 * s2)
        ),
        "literal_power_ratio_not_a_finite_pass_test": global_moment / target_power,
    }


def _control_specs() -> tuple[dict[str, object], ...]:
    controls: list[dict[str, object]] = [{"kind": "half_grid"}]
    controls.extend(
        {"kind": "jitter", "eta": 0.3, "seed": seed}
        for seed in (1729, 2718, 31415, 65537, 104729)
    )
    controls.extend(
        {"kind": "jitter", "eta": 0.1, "seed": seed}
        for seed in (1729, 31415)
    )
    controls.extend(
        {"kind": "jitter", "eta": 0.6, "seed": seed}
        for seed in (1729, 31415)
    )
    return tuple(controls)


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_frozen_replay(
    preregistration_path: Path,
    preflight_path: Path,
    *,
    maximum_step: float = 2.0,
    fine_step: float = 1.0,
) -> dict[str, object]:
    """Execute only the four preregistered centers and matched controls."""

    preregistration = json.loads(preregistration_path.read_text())
    centers = tuple(
        Fraction(int(item["numerator"]), int(item["denominator"]))
        for item in preregistration["construction"]["centers"]
    )
    if centers != FROZEN_CENTERS:
        raise ValueError("the preregistered center list is not the frozen list")

    scales: list[dict[str, object]] = []
    for center in centers:
        prime_vector = build_prime_hat_vector(center, precision_bits=192)
        mask, cutoff = certified_physical_gap_mask(center, prime_vector.primes)
        retained = retained_hat_vector_from_arb_nodes(
            prime_vector.vector.nodes,
            mask,
        )
        nodes = retained.float_nodes
        weights = retained.float_weights
        coarse = moment_profile(
            nodes,
            weights,
            float(center),
            maximum_step=maximum_step,
        )
        fine = moment_profile(
            nodes,
            weights,
            float(center),
            maximum_step=fine_step,
        )
        lower = float(center) ** float(LOWER_EXPONENT)
        band_right = float(center) ** float(APERTURE)
        conductor = float(center) ** float(CONDUCTOR_EXPONENT)
        s2 = float(np.sum(weights * weights))
        top_four_distinct = four_distinct_sharp_moment(
            nodes,
            weights,
            band_right,
            2 * band_right,
        )
        global_four_distinct = four_distinct_sharp_moment(
            nodes,
            weights,
            lower,
            2 * band_right,
        )
        sign_morphology = sign_morphology_trapezoid(
            nodes,
            weights,
            lower,
            2 * band_right,
            maximum_step=fine_step,
        )

        controls: list[dict[str, object]] = []
        for specification in _control_specs():
            if specification["kind"] == "half_grid":
                control_nodes = odd_half_grid_control(nodes, band_right)
                name = "half_grid"
            else:
                eta = float(specification["eta"])
                seed = int(specification["seed"])
                control_nodes = jitter_control(nodes, eta, seed)
                name = f"jitter_eta_{eta:g}_seed_{seed}"
            control_vector = retained_hat_vector_from_float_nodes(
                control_nodes,
                mask,
            )
            controls.append(
                {
                    "name": name,
                    "specification": specification,
                    "retained_mass": float(control_vector.retained_mass.mid()),
                    "profile": moment_profile(
                        control_vector.float_nodes,
                        control_vector.float_weights,
                        float(center),
                        maximum_step=maximum_step,
                    ),
                }
            )

        gaps = [
            right - left
            for left, right in zip(prime_vector.primes, prime_vector.primes[1:])
        ]
        retained_gaps = [gap for gap, keep in zip(gaps, mask) if keep]
        coarse_global = float(coarse["global_moment"])
        fine_global = float(fine["global_moment"])
        scales.append(
            {
                "center": {
                    "numerator": center.numerator,
                    "denominator": center.denominator,
                    "decimal": float(center),
                },
                "prime_count": len(prime_vector.primes),
                "physical_cutoff": float(cutoff.mid()),
                "kept_edge_count": sum(mask),
                "retained_gaps": retained_gaps,
                "active_node_count": retained.active_count,
                "retained_mass": float(retained.retained_mass.mid()),
                "retained_to_original_truncated_mass": (
                    float(retained.retained_mass.mid())
                    / float(prime_vector.vector.truncated_mass.mid())
                ),
                "actual": {
                    "coarse": coarse,
                    "fine": fine,
                    "sharp_four_distinct": {
                        "top": top_four_distinct,
                        "global": global_four_distinct,
                        "top_to_conductor_s2_squared": (
                            top_four_distinct / (conductor * s2 * s2)
                        ),
                        "global_to_conductor_s2_squared": (
                            global_four_distinct / (conductor * s2 * s2)
                        ),
                        "top_to_full_moment": (
                            top_four_distinct / float(fine["top_moment"])
                        ),
                        "global_to_full_moment": (
                            global_four_distinct / fine_global
                        ),
                    },
                    "global_sign_morphology": sign_morphology,
                    "global_relative_discretization_change": (
                        abs(fine_global - coarse_global) / fine_global
                    ),
                },
                "controls": controls,
            }
        )

    all_twin_only = all(
        set(scale["retained_gaps"]) == {2}  # type: ignore[arg-type]
        for scale in scales
    )
    return {
        "schema": "zeta23.gcg4.frozen_replay.v1",
        "claim_status": "OPEN",
        "trust": "FLOAT-SCOUT",
        "theorem": "GCG4(161/1000,3/8)",
        "finite_scope": "exactly four previously frozen centers; no extrapolation",
        "ledger": ledger_payload(),
        "preregistration_file": str(preregistration_path),
        "preregistration_sha256": _file_sha256(preregistration_path),
        "preflight_file": str(preflight_path),
        "preflight_sha256": _file_sha256(preflight_path),
        "source_sha256": _file_sha256(Path(__file__)),
        "maximum_step": maximum_step,
        "fine_step_actual_only": fine_step,
        "all_retained_edges_are_twin_prime_edges": all_twin_only,
        "regime_warning": (
            "At every licensed center Y^theta lies strictly between 2 and 4. "
            "The replay therefore probes a twin-edge vector, not the eventual "
            "mixed-gap asymptotic regime."
        ),
        "scales": scales,
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--preregistration",
        type=Path,
        default=Path("results/context/zeta23_ht_hat_prereg_v1.json"),
    )
    parser.add_argument(
        "--preflight",
        type=Path,
        default=Path("results/context/zeta23_global_conductor_l4_preflight_v1.json"),
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--maximum-step", type=float, default=2.0)
    parser.add_argument("--fine-step", type=float, default=1.0)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    payload = run_frozen_replay(
        args.preregistration,
        args.preflight,
        maximum_step=args.maximum_step,
        fine_step=args.fine_step,
    )
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(serialized, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")


if __name__ == "__main__":
    main()
