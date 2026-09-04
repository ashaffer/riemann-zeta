"""Finite actual-prime diagnostics for ``LTRAD_full(c_rad,d_dir)``.

The implication under study is

    E(I,Y,t) >= N**(-d_dir)  ==>  r_+(H_Y; S_Y) >= N**(-c_rad).

The named exponents are intentional: older project reports reverse the
positional order of ``c`` and ``d``.  Here ``c_rad`` always denotes the
radial conclusion exponent and ``d_dir`` the directional/Turan premise
exponent.

This module does not test an asymptotic theorem from finitely many values.
It only turns floating lower/upper brackets for ``E`` and ``r_+`` into an
explicit finite-scale exponent frontier.  In particular, a definite
constant-one violation at one sampled center requires both

    d_dir >= -log(E_lower)/log(N),
    c_rad <  -log(r_upper)/log(N).

The continuum guards in :mod:`qp_radialization_lab` are analytic, but the LP
and cosine arithmetic are floating point.  Consequently even a ``definite``
status below is definite only relative to those floating brackets, not an
interval-arithmetic theorem certificate.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import math

from qp_radialization_lab import run_instance


def _power_exponent(value: float, scale: float) -> float:
    if scale <= 1.0 or not 0.0 < value < 1.0:
        raise ValueError("power exponents require scale > 1 and value in (0,1)")
    return -math.log(value) / math.log(scale)


@dataclass(frozen=True)
class FiniteLTRADFrontier:
    N: int
    prime_count: int
    directional_lower: float
    directional_upper: float
    radius_lower: float
    radius_upper: float
    premise_d_definite: float
    premise_d_possible: float
    conclusion_failure_c_definite: float
    conclusion_failure_c_possible: float
    definite_violation_rectangle_meets_c_gt_d: bool
    effective_E_as_power_of_R: float
    effective_E_as_power_of_R_lower: float
    effective_E_as_power_of_R_upper: float


def finite_ltrad_frontier(
    N: int,
    prime_count: int,
    directional_lower: float,
    directional_upper: float,
    radius_lower: float,
    radius_upper: float,
) -> FiniteLTRADFrontier:
    """Return the constant-one finite implication frontier.

    ``premise_d_definite`` is the least ``d`` for which the lower bracket
    already proves the premise.  ``conclusion_failure_c_definite`` is the
    largest (open-endpoint) ``c`` for which the upper bracket proves that the
    conclusion fails.
    """

    if N <= 1 or prime_count < 1:
        raise ValueError("invalid scale or prime count")
    if not 0.0 < directional_lower <= directional_upper < 1.0:
        raise ValueError("invalid directional bracket")
    if not 0.0 < radius_lower <= radius_upper < 1.0:
        raise ValueError("invalid radius bracket")

    d_definite = _power_exponent(directional_lower, N)
    d_possible = _power_exponent(directional_upper, N)
    c_definite = _power_exponent(radius_upper, N)
    c_possible = _power_exponent(radius_lower, N)
    e_mid = 0.5 * (directional_lower + directional_upper)
    r_mid = 0.5 * (radius_lower + radius_upper)
    effective_power = math.log(e_mid) / math.log(r_mid)
    # For lambda=log(E)/log(R), lambda decreases with E and increases with R
    # on (0,1)^2.  These endpoints therefore guard the whole input bracket.
    effective_power_lower = math.log(directional_upper) / math.log(radius_lower)
    effective_power_upper = math.log(directional_lower) / math.log(radius_upper)
    return FiniteLTRADFrontier(
        N=N,
        prime_count=prime_count,
        directional_lower=directional_lower,
        directional_upper=directional_upper,
        radius_lower=radius_lower,
        radius_upper=radius_upper,
        premise_d_definite=d_definite,
        premise_d_possible=d_possible,
        conclusion_failure_c_definite=c_definite,
        conclusion_failure_c_possible=c_possible,
        definite_violation_rectangle_meets_c_gt_d=c_definite > d_definite,
        effective_E_as_power_of_R=effective_power,
        effective_E_as_power_of_R_lower=effective_power_lower,
        effective_E_as_power_of_R_upper=effective_power_upper,
    )


@dataclass(frozen=True)
class PairDiagnostic:
    c_rad: float
    d_dir: float
    premise_lower_ratio: float
    premise_upper_ratio: float
    conclusion_lower_ratio: float
    conclusion_upper_ratio: float
    count_ceiling_ratio: float
    premise_status: str
    conclusion_status: str
    implication_status: str


def diagnose_pair(
    N: int,
    prime_count: int,
    directional_lower: float,
    directional_upper: float,
    radius_lower: float,
    radius_upper: float,
    *,
    c_rad: float,
    d_dir: float,
) -> PairDiagnostic:
    """Diagnose one exponent pair at one finite center.

    Ratios are relative to ``N**(-d_dir)`` and ``N**(-c_rad)``.
    The count ceiling uses the exact inequality ``E <= #primes/N``.
    """

    if c_rad <= 0.0 or d_dir <= 0.0:
        raise ValueError("c_rad and d_dir must be positive")
    premise_threshold = N ** (-d_dir)
    conclusion_threshold = N ** (-c_rad)
    premise_lower_ratio = directional_lower / premise_threshold
    premise_upper_ratio = directional_upper / premise_threshold
    conclusion_lower_ratio = radius_lower / conclusion_threshold
    conclusion_upper_ratio = radius_upper / conclusion_threshold
    count_ceiling_ratio = (prime_count / N) / premise_threshold

    if premise_lower_ratio >= 1.0:
        premise_status = "holds"
    elif premise_upper_ratio < 1.0:
        premise_status = "fails"
    else:
        premise_status = "bracket-ambiguous"

    if conclusion_lower_ratio >= 1.0:
        conclusion_status = "holds"
    elif conclusion_upper_ratio < 1.0:
        conclusion_status = "fails"
    else:
        conclusion_status = "bracket-ambiguous"

    if count_ceiling_ratio < 1.0:
        implication_status = "premise-impossible-by-count-at-this-center"
    elif premise_status == "fails":
        implication_status = "premise-not-observed"
    elif premise_status == "holds" and conclusion_status == "fails":
        implication_status = "finite-constant-one-violation"
    elif premise_status == "holds" and conclusion_status == "holds":
        implication_status = "finite-instance-satisfies-implication"
    else:
        implication_status = "unresolved-by-brackets"

    return PairDiagnostic(
        c_rad=c_rad,
        d_dir=d_dir,
        premise_lower_ratio=premise_lower_ratio,
        premise_upper_ratio=premise_upper_ratio,
        conclusion_lower_ratio=conclusion_lower_ratio,
        conclusion_upper_ratio=conclusion_upper_ratio,
        count_ceiling_ratio=count_ceiling_ratio,
        premise_status=premise_status,
        conclusion_status=conclusion_status,
        implication_status=implication_status,
    )


def pnt_shell_count_crossover_log10(
    d: float,
    *,
    shell_width: float = 0.2,
    center_ratio: float = 1.0,
) -> float:
    """PNT-model crossover where shell count first reaches ``N**(1-d)``.

    With ``Y=center_ratio*N``, the PNT model is

        #shell primes / N ~= 2*center_ratio*sinh(width) / log(Y).

    The returned base-10 logarithm is heuristic calibration, not a rigorous
    prime-count threshold.
    """

    if not 0.0 < d < 1.0 or shell_width <= 0.0 or center_ratio <= 0.0:
        raise ValueError("invalid crossover parameters")
    coefficient = 2.0 * center_ratio * math.sinh(shell_width)
    log_ratio = math.log(center_ratio)

    def equation(log_n: float) -> float:
        return (
            d * log_n
            - math.log(log_n + log_ratio)
            + math.log(coefficient)
        )

    lower = max(2.0, 1.0 / d)
    while equation(lower) > 0.0 and lower > 2.0:
        lower = max(2.0, 0.5 * lower)
    upper = max(4.0, 2.0 * lower)
    while equation(upper) <= 0.0:
        upper *= 2.0
        if upper > 1.0e9:
            raise RuntimeError("failed to bracket the PNT crossover")
    for _ in range(100):
        middle = 0.5 * (lower + upper)
        if equation(middle) <= 0.0:
            lower = middle
        else:
            upper = middle
    return 0.5 * (lower + upper) / math.log(10.0)


def run_numeric_audit(
    N: int,
    center_ratio: float,
    *,
    c_rad: float,
    d_dir: float,
    antipode_phase_step: float,
    directional_phase_step: float,
    iterations: int,
) -> dict:
    Y = math.floor(center_ratio * N) + 0.5
    instance = run_instance(
        N,
        center_offset=Y - N,
        antipode_phase_step=antipode_phase_step,
        directional_phase_step=directional_phase_step,
        max_exchange_iterations=iterations,
    )
    direction = instance["direction_any_interval"]
    radius = instance["antipode_full_band"]
    frontier = finite_ltrad_frontier(
        N,
        instance["prime_nodes"],
        direction["lower"],
        direction["upper_guard"],
        radius["lower"],
        radius["upper_guard"],
    )
    pair = diagnose_pair(
        N,
        instance["prime_nodes"],
        direction["lower"],
        direction["upper_guard"],
        radius["lower"],
        radius["upper_guard"],
        c_rad=c_rad,
        d_dir=d_dir,
    )
    return {
        "N": N,
        "Y": Y,
        "center_ratio": Y / N,
        "prime_power_count": instance["prime_power_nodes"],
        "prime_count": instance["prime_nodes"],
        "winning_prime_count": direction["prime_count"],
        "winning_time": direction["time"],
        "frontier": asdict(frontier),
        "requested_pair": asdict(pair),
        "floating_diagnostic_only": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--N", type=int, default=600)
    parser.add_argument("--center-ratio", type=float, default=1.0)
    parser.add_argument("--c-rad", type=float, default=0.0189)
    parser.add_argument("--d-dir", type=float, default=0.001)
    parser.add_argument("--antipode-phase-step", type=float, default=0.12)
    parser.add_argument("--directional-phase-step", type=float, default=0.08)
    parser.add_argument("--iterations", type=int, default=6)
    args = parser.parse_args()
    payload = run_numeric_audit(
        args.N,
        args.center_ratio,
        c_rad=args.c_rad,
        d_dir=args.d_dir,
        antipode_phase_step=args.antipode_phase_step,
        directional_phase_step=args.directional_phase_step,
        iterations=args.iterations,
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
