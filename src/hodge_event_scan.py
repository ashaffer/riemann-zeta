"""Scan the Hodge tilted-cycle criterion on consecutive prime-power events.

For consecutive activation locations ``e_i=2 log(n_i)``, the support interval

    ((e_(i-1)+e_i)/2, (e_i+e_(i+1))/2)

contains exactly the event ``n_i``.  Collar degrees are chosen to keep the
collar-hat half-width at a fixed ratio to the old-hat half-width, with a
resolution-scaled minimum.  Fourier cutoffs and Simpson interval counts also
scale with the old degree.

The primary output is ``surplus_to_hodge_loss_ratio``: the largest ``c`` for

    F + R - H >= c Y* (I-tau)^2 Y.

The Hodge sufficient criterion passes exactly when this ratio is at least one.
All outputs are finite Galerkin diagnostics.
"""
from __future__ import annotations

import argparse
import math
import sys

import mpmath as mp

from tilted_cycle_completion import diagnose_tilt
from weil_core import PRIME_POWERS


def event_catalog() -> list[tuple[int, int, int, float]]:
    """Return one-based index, prime power, prime, and activation support."""
    events = sorted(
        {(int(n), int(prime)) for n, prime in PRIME_POWERS},
        key=lambda item: math.log(item[0]))
    return [
        (index + 1, n, prime, 2 * math.log(n))
        for index, (n, prime) in enumerate(events)
    ]


def matched_collar_degree(old_support: float, new_support: float,
                          old_degree: int, mesh_ratio: float,
                          minimum_fraction: float) -> int:
    """Match collar/old hat half-widths up to the requested ratio."""
    support_width = new_support - old_support
    raw = support_width * (old_degree + 1) / (
        2 * old_support * mesh_ratio) - 1
    scaled_minimum = max(2, math.ceil(minimum_fraction * old_degree))
    return max(scaled_minimum, int(round(raw)))


def default_cutoff(old_degree: int) -> float:
    """Reproduce 1200,1600,2000,2400 near degrees 61,121,181,241."""
    return 800 + (20 / 3) * old_degree


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-prime-power", type=int, default=8)
    parser.add_argument("--end-prime-power", type=int, default=47)
    parser.add_argument("--old-degrees", nargs="+", type=int, default=[61])
    parser.add_argument("--mesh-ratio", type=float, default=0.42)
    parser.add_argument("--minimum-collar-fraction", type=float, default=1/24)
    parser.add_argument("--cutoff-scale", type=float, default=1.0)
    parser.add_argument("--interval-density", type=float, default=100.0)
    parser.add_argument("--chunk", type=int, default=2000)
    parser.add_argument("--grid-size", type=int, default=3)
    args = parser.parse_args()
    if args.mesh_ratio <= 0:
        parser.error("--mesh-ratio must be positive")
    if args.minimum_collar_fraction <= 0:
        parser.error("--minimum-collar-fraction must be positive")
    if args.grid_size < 2:
        parser.error("--grid-size must be at least two")

    catalog = event_catalog()
    positions = {n: index for index, (_, n, _, _) in enumerate(catalog)}
    if args.start_prime_power not in positions:
        parser.error("start prime power is absent from the event catalog")
    if args.end_prime_power not in positions:
        parser.error("end prime power is absent from the event catalog")
    start = positions[args.start_prime_power]
    end = positions[args.end_prime_power]
    if start > end:
        parser.error("start prime power occurs after end prime power")
    if start == 0 or end + 1 >= len(catalog):
        parser.error("selected events need a predecessor and successor")

    mp.mp.dps = 30
    fields = [
        "event_index", "prime_power", "prime", "old_support", "new_support",
        "old_degree", "collar_degree", "cutoff", "intervals",
        "shell_degree_q2", "old_incidence_minimum",
        "old_incidence_maximum", "old_incidence_condition",
        "q2_over_old_incidence_minimum", "hodge_tau_minimum",
        "hodge_tau_maximum", "fresh_ratio", "full_ratio",
        "hodge_exact_ratio", "hodge_lower_ratio",
        "surplus_to_hodge_loss_ratio",
        "scaled_surplus_to_hodge_loss_ratio",
        "surplus_to_sharp_smoothing_ratio",
        "surplus_to_s2_smoothing_ratio", "full_surplus_minimum",
        "hodge_loss_maximum", "hodge_lower_minimum", "hodge_loss_rank",
        "canonical_margin", "factor_formula_error", "full_endpoint_error",
    ]
    print(",".join(fields))

    for catalog_position in range(start, end + 1):
        event_index, n, prime, event_support = catalog[catalog_position]
        previous_support = catalog[catalog_position - 1][3]
        next_support = catalog[catalog_position + 1][3]
        old_support = (previous_support + event_support) / 2
        new_support = (event_support + next_support) / 2
        for old_degree in args.old_degrees:
            collar_degree = matched_collar_degree(
                old_support, new_support, old_degree,
                args.mesh_ratio, args.minimum_collar_fraction)
            cutoff = args.cutoff_scale * default_cutoff(old_degree)
            intervals = int(round(args.interval_density * cutoff))
            if intervals % 2:
                intervals += 1
            result = diagnose_tilt(
                old_support, new_support, old_degree, collar_degree,
                cutoff, intervals, args.chunk, args.grid_size)
            if result.activated_event_count != 1:
                raise RuntimeError(
                    f"midpoint interval for {n} contains "
                    f"{result.activated_event_count} events")
            values = [
                event_index, n, prime, old_support, new_support,
                old_degree, collar_degree, cutoff, intervals,
                result.shell_degree_q2, result.old_incidence_minimum,
                result.old_incidence_maximum,
                result.old_incidence_condition,
                result.q2_over_old_incidence_minimum,
                result.hodge_tau_minimum, result.hodge_tau_maximum,
                result.ratio_at_zero, result.ratio_at_one,
                result.hodge_tilt_ratio, result.hodge_lower_ratio,
                result.surplus_to_hodge_loss_ratio,
                result.scaled_surplus_to_hodge_loss_ratio,
                result.surplus_to_sharp_smoothing_ratio,
                result.surplus_to_s2_smoothing_ratio,
                result.full_surplus_minimum, result.hodge_loss_maximum,
                result.hodge_lower_minimum, result.hodge_loss_rank,
                result.canonical_margin, result.factor_formula_error,
                result.full_endpoint_error,
            ]
            formatted = []
            for value in values:
                if isinstance(value, int):
                    formatted.append(str(value))
                else:
                    formatted.append(f"{value:.12e}")
            print(",".join(formatted), flush=True)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
