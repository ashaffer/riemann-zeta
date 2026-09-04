"""Bounded actual-prime falsifier for the center-density direction.

This is a floating finite diagnostic, not an asymptotic theorem.  It uses
the exact ordinary-prime shell and adjacent physical-gap retention mask,
floating Gauss quadrature for the retained nodal-hat weights, and two
independent stratified samples of the top band.  A fixed contiguous prime
interval supplies ``S_I(tau)``.  Common ordinates are then scanned for phase
arcs that are unusually enriched in high retained-hat L4 energy.

The diagnostic cannot test the asymptotic legal-event premise: at accessible
scales the prime-count ceiling is far below ``N**(-1/1000)``.  It also does
not approximate the LTRAD radius.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
import math
from pathlib import Path

import numpy as np
from scipy.stats import pearsonr, spearmanr

from global_conductor_l4_gate import (
    APERTURE,
    CONDUCTOR_EXPONENT,
    THETA,
    certified_physical_gap_mask,
    retained_hat_vector_from_arb_nodes,
)
from prime_log_hat_tail import TILT, WIDTH, build_prime_hat_vector
from qp_radialization_lab import primes_up_to


DEFAULT_N = 8000
DEFAULT_CENTER_FIRST = 8000.5
DEFAULT_CENTER_LAST = 9000.5
DEFAULT_SOURCE_LEFT = 8200
DEFAULT_SOURCE_RIGHT = 9060
DEFAULT_KAPPA = 0.75


@dataclass(frozen=True)
class FloatingRetainedHat:
    primes: np.ndarray
    nodes: np.ndarray
    weights: np.ndarray
    kept_edge_count: int


def _profile(u: np.ndarray) -> np.ndarray:
    width = float(WIDTH)
    alpha = float(TILT)
    return np.exp(alpha * u) * (1.0 - np.abs(u) / width)


def _gauss_edge_shares(left: float, right: float) -> tuple[float, float]:
    """Integrate the two linear edge hats against the tilted tent.

    Eight-point Gauss--Legendre quadrature is applied separately on either
    side of the cusp at zero.  At the present prime-gap mesh its error is far
    below the Monte Carlo error in the top-band scout.
    """

    abscissae, quadrature_weights = np.polynomial.legendre.leggauss(8)
    cuts = [left]
    if left < 0.0 < right:
        cuts.append(0.0)
    cuts.append(right)
    left_share = 0.0
    right_share = 0.0
    gap = right - left
    for subleft, subright in zip(cuts, cuts[1:]):
        midpoint = 0.5 * (subleft + subright)
        radius = 0.5 * (subright - subleft)
        points = midpoint + radius * abscissae
        values = radius * quadrature_weights * _profile(points)
        left_share += float(np.sum(values * (right - points) / gap))
        right_share += float(np.sum(values * (points - left) / gap))
    return left_share, right_share


def floating_retained_hat(
    center: float,
    all_primes: np.ndarray,
) -> FloatingRetainedHat:
    """Build the moving retained-hat vector on actual consecutive primes."""

    width = float(WIDTH)
    first = int(np.searchsorted(all_primes, center * math.exp(-width), side="left"))
    stop = int(np.searchsorted(all_primes, center * math.exp(width), side="right"))
    primes = all_primes[first:stop]
    if len(primes) < 2:
        raise ValueError("sampled shell has fewer than two primes")
    nodes = np.log(primes.astype(float) / center)
    gaps = np.diff(primes)
    keep = gaps <= center ** float(THETA)
    if not np.any(keep):
        raise ValueError("sampled shell has no retained edge")

    raw = np.zeros(len(primes), dtype=float)
    for index in np.flatnonzero(keep):
        left_share, right_share = _gauss_edge_shares(
            float(nodes[index]), float(nodes[index + 1])
        )
        raw[index] += left_share
        raw[index + 1] += right_share
    active = raw > 0.0
    weights = raw[active]
    weights /= float(np.sum(weights))
    return FloatingRetainedHat(
        primes=primes[active],
        nodes=nodes[active],
        weights=weights,
        kept_edge_count=int(np.sum(keep)),
    )


def top_band_scout(
    vector: FloatingRetainedHat,
    center: float,
    strata: np.ndarray,
) -> dict[str, float]:
    """Sample one stratified realization of the top-band morphology."""

    band_left = center ** float(APERTURE)
    times = band_left * (1.0 + strata)
    values = np.exp(1j * np.outer(times, vector.nodes)) @ vector.weights
    fourth = np.abs(values) ** 4
    s2 = float(np.sum(vector.weights**2))
    s4 = float(np.sum(vector.weights**4))
    diagonal = 2.0 * s2 * s2 - s4
    mean_fourth = float(np.mean(fourth))
    return {
        "mean_fourth": mean_fourth,
        "top_integral": band_left * mean_fourth,
        "diagonal_density": diagonal,
        "diagonal_ratio": mean_fourth / diagonal,
        "minimum_real": float(np.min(np.real(values))),
        "maximum_absolute": float(np.max(np.abs(values))),
        "s2": s2,
    }


def _source_sums(primes: np.ndarray, taus: np.ndarray) -> np.ndarray:
    logs = np.log(primes.astype(float))
    output = np.empty(len(taus), dtype=np.complex128)
    chunk = 512
    for start in range(0, len(taus), chunk):
        stop = min(start + chunk, len(taus))
        output[start:stop] = np.sum(
            np.exp(-1j * np.outer(taus[start:stop], logs)), axis=1
        )
    return output


def _phase_masks(
    centers: np.ndarray,
    taus: np.ndarray,
    source_sums: np.ndarray,
    kappa: float,
) -> tuple[np.ndarray, np.ndarray]:
    phases = np.exp(1j * np.outer(taus, np.log(centers))) * source_sums[:, None]
    absolute = np.abs(source_sums)
    normalized_real = np.real(phases) / absolute[:, None]
    return normalized_real <= -kappa, normalized_real


def _group_difference(mask: np.ndarray, energy: np.ndarray) -> np.ndarray:
    counts = np.sum(mask, axis=1)
    aligned_sum = mask @ energy
    total = float(np.sum(energy))
    return aligned_sum / counts - (total - aligned_sum) / (len(energy) - counts)


def _selection_payload(
    index: int,
    *,
    centers: np.ndarray,
    taus: np.ndarray,
    source_sums: np.ndarray,
    masks: np.ndarray,
    normalized_real: np.ndarray,
    metric: np.ndarray,
    replicate_metrics: tuple[np.ndarray, np.ndarray],
    source_count: int,
    n_scale: int,
    kappa: float,
) -> dict[str, object]:
    mask = masks[index]
    aligned = metric[mask]
    unaligned = metric[~mask]
    phase_score = -normalized_real[index]
    pearson = pearsonr(phase_score, metric)
    spearman = spearmanr(phase_score, metric)
    replicate_differences = []
    for replicate in replicate_metrics:
        replicate_differences.append(
            float(np.mean(replicate[mask]) - np.mean(replicate[~mask]))
        )
    absolute_sum = float(abs(source_sums[index]))
    return {
        "index": int(index),
        "tau": float(taus[index]),
        "source_absolute_sum": absolute_sum,
        "source_coherence_per_prime": absolute_sum / source_count,
        "source_random_scale_ratio": absolute_sum / math.sqrt(source_count),
        "guaranteed_aligned_D": kappa * absolute_sum / source_count,
        "guaranteed_aligned_mass_depth_e": kappa * absolute_sum / n_scale,
        "aligned_count": int(np.sum(mask)),
        "aligned_fraction": float(np.mean(mask)),
        "metric_aligned_mean": float(np.mean(aligned)),
        "metric_unaligned_mean": float(np.mean(unaligned)),
        "metric_mean_difference": float(np.mean(aligned) - np.mean(unaligned)),
        "metric_replicate_mean_differences": replicate_differences,
        "pearson_phase_score_vs_metric": {
            "statistic": float(pearson.statistic),
            "naive_pvalue_not_autocorrelation_corrected": float(pearson.pvalue),
        },
        "spearman_phase_score_vs_metric": {
            "statistic": float(spearman.statistic),
            "naive_pvalue_not_autocorrelation_corrected": float(spearman.pvalue),
        },
    }


def run_probe(
    *,
    n_scale: int = DEFAULT_N,
    center_first: float = DEFAULT_CENTER_FIRST,
    center_last: float = DEFAULT_CENTER_LAST,
    source_left: int = DEFAULT_SOURCE_LEFT,
    source_right: int = DEFAULT_SOURCE_RIGHT,
    sample_count: int = 512,
    tau_count: int = 2048,
    shift_count: int = 128,
    seed: int = 20260831,
    kappa: float = DEFAULT_KAPPA,
) -> dict[str, object]:
    """Run the bounded actual-prime center/source co-resonance probe."""

    if center_first % 1 != 0.5 or center_last % 1 != 0.5:
        raise ValueError("center endpoints must be half-integers")
    if not center_last >= center_first or not 0.0 < kappa < 1.0:
        raise ValueError("invalid center range or kappa")
    centers = np.arange(center_first, center_last + 0.25, 1.0)
    prime_limit = math.ceil(center_last * math.exp(float(WIDTH)))
    all_primes = np.asarray(primes_up_to(prime_limit), dtype=np.int64)
    source_primes = all_primes[
        (all_primes >= source_left) & (all_primes <= source_right)
    ]
    if len(source_primes) < 2:
        raise ValueError("source interval has fewer than two primes")
    if math.log(source_right / source_left) > float(WIDTH) / 2:
        raise ValueError("source interval exceeds the audited log width w/2")
    if source_left < center_last * math.exp(-float(WIDTH)):
        raise ValueError("source interval is not inside the last center shell")
    if source_right > center_first * math.exp(float(WIDTH)):
        raise ValueError("source interval is not inside the first center shell")

    rng = np.random.default_rng(seed)
    strata = []
    for _ in range(2):
        strata.append((np.arange(sample_count) + rng.random(sample_count)) / sample_count)

    rows: list[dict[str, float | int]] = []
    replicate_mean_fourth = [[], []]
    replicate_top_integral = [[], []]
    replicate_diagonal_ratio = [[], []]
    for center in centers:
        vector = floating_retained_hat(float(center), all_primes)
        scouts = [top_band_scout(vector, float(center), sample) for sample in strata]
        for index, scout in enumerate(scouts):
            replicate_mean_fourth[index].append(scout["mean_fourth"])
            replicate_top_integral[index].append(scout["top_integral"])
            replicate_diagonal_ratio[index].append(scout["diagonal_ratio"])
        rows.append(
            {
                "center": float(center),
                "active_prime_count": int(len(vector.primes)),
                "kept_edge_count": vector.kept_edge_count,
                "s2": scouts[0]["s2"],
                "mean_fourth_rep1": scouts[0]["mean_fourth"],
                "mean_fourth_rep2": scouts[1]["mean_fourth"],
                "top_integral_rep1": scouts[0]["top_integral"],
                "top_integral_rep2": scouts[1]["top_integral"],
                "diagonal_ratio_rep1": scouts[0]["diagonal_ratio"],
                "diagonal_ratio_rep2": scouts[1]["diagonal_ratio"],
                "minimum_real_rep1": scouts[0]["minimum_real"],
                "minimum_real_rep2": scouts[1]["minimum_real"],
                "maximum_absolute_rep1": scouts[0]["maximum_absolute"],
                "maximum_absolute_rep2": scouts[1]["maximum_absolute"],
            }
        )

    mean_fourth_replicates = tuple(np.asarray(item) for item in replicate_mean_fourth)
    top_integral_replicates = tuple(np.asarray(item) for item in replicate_top_integral)
    diagonal_ratio_replicates = tuple(np.asarray(item) for item in replicate_diagonal_ratio)
    diagonal_ratio = 0.5 * (
        diagonal_ratio_replicates[0] + diagonal_ratio_replicates[1]
    )
    metric = np.log(diagonal_ratio)
    replicate_metrics = (
        np.log(diagonal_ratio_replicates[0]),
        np.log(diagonal_ratio_replicates[1]),
    )

    taus = np.linspace(math.sqrt(n_scale), float(n_scale), tau_count)
    source_sums = _source_sums(source_primes, taus)
    masks, normalized_real = _phase_masks(
        centers, taus, source_sums, kappa
    )
    counts = np.sum(masks, axis=1)
    if np.min(counts) == 0 or np.max(counts) == len(centers):
        raise ArithmeticError("a scanned phase arc has an empty comparison group")
    differences = _group_difference(masks, metric)
    source_index = int(np.argmax(np.abs(source_sums)))
    coherent = np.abs(source_sums) >= math.sqrt(len(source_primes))
    hostile_candidates = np.flatnonzero(coherent)
    if len(hostile_candidates) == 0:
        hostile_candidates = np.arange(len(taus))
    hostile_index = int(
        hostile_candidates[np.argmax(differences[hostile_candidates])]
    )

    source_choice = _selection_payload(
        source_index,
        centers=centers,
        taus=taus,
        source_sums=source_sums,
        masks=masks,
        normalized_real=normalized_real,
        metric=metric,
        replicate_metrics=replicate_metrics,
        source_count=len(source_primes),
        n_scale=n_scale,
        kappa=kappa,
    )
    hostile_choice = _selection_payload(
        hostile_index,
        centers=centers,
        taus=taus,
        source_sums=source_sums,
        masks=masks,
        normalized_real=normalized_real,
        metric=metric,
        replicate_metrics=replicate_metrics,
        source_count=len(source_primes),
        n_scale=n_scale,
        kappa=kappa,
    )

    # Circular shifts preserve the center-energy autocorrelation.  The first
    # control tests the source-coherence choice; the second repeats the full
    # hostile tau selection and therefore charges the ordinate scan.
    nonzero_shifts = rng.choice(
        np.arange(1, len(centers)), size=min(shift_count, len(centers) - 1), replace=False
    )
    source_shift_differences = []
    hostile_shift_maxima = []
    for shift in nonzero_shifts:
        shifted = np.roll(metric, int(shift))
        shifted_differences = _group_difference(masks, shifted)
        source_shift_differences.append(float(shifted_differences[source_index]))
        hostile_shift_maxima.append(
            float(np.max(shifted_differences[hostile_candidates]))
        )
    source_observed = float(differences[source_index])
    hostile_observed = float(differences[hostile_index])
    source_shift_p = (
        1 + sum(value >= source_observed for value in source_shift_differences)
    ) / (1 + len(source_shift_differences))
    hostile_shift_p = (
        1 + sum(value >= hostile_observed for value in hostile_shift_maxima)
    ) / (1 + len(hostile_shift_maxima))

    # Validate the fast floating weights against the existing Arb path at
    # three centers.  The mask and shell are independently reconstructed.
    validation = []
    for center in (centers[0], centers[len(centers) // 2], centers[-1]):
        fast = floating_retained_hat(float(center), all_primes)
        exact_center = Fraction(int(round(2 * center)), 2)
        prime_vector = build_prime_hat_vector(exact_center, precision_bits=128)
        exact_mask, _ = certified_physical_gap_mask(exact_center, prime_vector.primes)
        arb_vector = retained_hat_vector_from_arb_nodes(
            prime_vector.vector.nodes, exact_mask
        )
        exact_active = arb_vector.float_weights > 0
        exact_weights = arb_vector.float_weights[exact_active]
        exact_primes = np.asarray(prime_vector.primes)[exact_active]
        if not np.array_equal(fast.primes, exact_primes):
            raise ArithmeticError("floating and Arb active-prime masks disagree")
        validation.append(
            {
                "center": float(center),
                "weight_l1_difference": float(np.sum(np.abs(fast.weights - exact_weights))),
                "weight_max_difference": float(np.max(np.abs(fast.weights - exact_weights))),
            }
        )

    top_average = 0.5 * (
        top_integral_replicates[0] + top_integral_replicates[1]
    )
    relative_replicate_difference = np.abs(
        top_integral_replicates[0] - top_integral_replicates[1]
    ) / top_average
    expected_density = math.acos(kappa) / math.pi
    legal_threshold = n_scale ** (-0.001)
    source_count_ceiling = len(source_primes) / n_scale
    return {
        "schema": "zeta23.center_density.actual_prime_probe.v1",
        "claim_status": "FINITE_DIAGNOSTIC_ONLY",
        "trust": "FLOATING_POINT_STRATIFIED_TOP_BAND_SCOUT",
        "preflight": "results/context/zeta23_center_density_actual_prime_probe_preflight_v1.json",
        "scope": {
            "N": n_scale,
            "center_first": center_first,
            "center_last": center_last,
            "center_count": len(centers),
            "source_left": source_left,
            "source_right": source_right,
            "source_prime_count": len(source_primes),
            "source_log_width": math.log(source_right / source_left),
            "tau_first": float(taus[0]),
            "tau_last": float(taus[-1]),
            "tau_count": len(taus),
            "top_band_sample_count_per_replicate": sample_count,
            "retention_theta": str(THETA),
            "top_aperture": str(APERTURE),
            "kappa": kappa,
            "expected_phase_arc_density": expected_density,
        },
        "finite_legality_warning": {
            "legal_mass_depth_threshold_N^-0.001": legal_threshold,
            "prime_count_ceiling_M_over_N": source_count_ceiling,
            "premise_is_possible_at_this_scale": source_count_ceiling >= legal_threshold,
            "interpretation": (
                "The diagnostic cannot furnish or refute an asymptotically legal "
                "Turan event; it tests only actual-prime center/source morphology."
            ),
        },
        "weight_validation_against_arb": validation,
        "monte_carlo_replicate": {
            "pearson_log_diagonal_ratio_between_replicates": float(
                pearsonr(replicate_metrics[0], replicate_metrics[1]).statistic
            ),
            "median_relative_top_integral_difference": float(
                np.median(relative_replicate_difference)
            ),
            "p90_relative_top_integral_difference": float(
                np.quantile(relative_replicate_difference, 0.9)
            ),
        },
        "phase_count_range": {
            "minimum_fraction": float(np.min(counts) / len(centers)),
            "median_fraction": float(np.median(counts) / len(centers)),
            "maximum_fraction": float(np.max(counts) / len(centers)),
        },
        "primary_metric": "log(top-band sampled fourth moment / long-time diagonal density)",
        "source_coherence_choice": source_choice,
        "hostile_energy_enrichment_choice": hostile_choice,
        "circular_shift_controls": {
            "shift_count": len(nonzero_shifts),
            "source_choice_one_sided_empirical_p": source_shift_p,
            "hostile_scan_one_sided_empirical_p": hostile_shift_p,
            "warning": "Finite autocorrelation-preserving controls, not inferential theorem tests.",
        },
        "center_summary": {
            "active_prime_count_min": int(min(row["active_prime_count"] for row in rows)),
            "active_prime_count_median": float(
                np.median([row["active_prime_count"] for row in rows])
            ),
            "active_prime_count_max": int(max(row["active_prime_count"] for row in rows)),
            "kept_edge_count_min": int(min(row["kept_edge_count"] for row in rows)),
            "kept_edge_count_median": float(
                np.median([row["kept_edge_count"] for row in rows])
            ),
            "kept_edge_count_max": int(max(row["kept_edge_count"] for row in rows)),
            "diagonal_ratio_min": float(np.min(diagonal_ratio)),
            "diagonal_ratio_median": float(np.median(diagonal_ratio)),
            "diagonal_ratio_max": float(np.max(diagonal_ratio)),
        },
        "rows": rows,
        "status_ledger": {
            "finite_actual_prime_co_resonance_probe": "COMPLETED",
            "averaged_GCG4": "OPEN",
            "event_conditioned_density_radialization": "OPEN",
            "uniform_zero_free_strip": "OPEN",
            "RH": "OPEN",
        },
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=512)
    parser.add_argument("--taus", type=int, default=2048)
    parser.add_argument("--shifts", type=int, default=128)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    payload = run_probe(
        sample_count=args.samples,
        tau_count=args.taus,
        shift_count=args.shifts,
    )
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(serialized, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")


if __name__ == "__main__":
    main()
