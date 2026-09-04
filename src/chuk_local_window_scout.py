"""Floating scout for the Chuk ``a = 0.8`` compact Weil window.

This is deliberately *not* an interval certificate.  It assembles the
band-clipped Weil form in normalized Legendre coordinates using independent
Gauss--Legendre panels and SciPy's spherical Bessel functions.  Its jobs are

* to falsify or support proposed clipping parameters before an Arb run;
* to provide a deterministic negative Rayleigh witness when a proposal fails;
* to reproduce the well-conditioned part of Chuk's reported head spectrum.

Conventions agree with ``fullinf_unrestricted_n4_certificate.py``.  Physical
half-width is ``a`` and project ``L_program = 4*a``.  At ``a = 4/5`` the
active prime powers are exactly 2, 3, and 4, and

    Omega(r) = Re psi(1/4 + i r/2) - log(pi)
               - sqrt(2) log(2) cos(r log(2))
               - 2 log(3)/sqrt(3) cos(r log(3))
               - log(2) cos(2 r log(2)).

For cutoff T and exterior floor alpha, the even/odd clipped form is

    alpha I + (1/pi) int_0^T (Omega-alpha) F(r) F(r)^* dr + pole,

where the Fourier transform of normalized Legendre mode k is
``sqrt(2*a*(2*k+1))*(-i)^k*j_k(a*r)``.

Evidence label: FLOATING-POINT DIAGNOSTIC.  Tiny eigenvalues at the 1e-15
level are below trustworthy double-precision resolution.  A negative value
near 4e-13 which persists across quadrature orders is a strong method
falsifier, but theorem certification still requires outward-rounded balls.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import pi

import numpy as np
from scipy.special import digamma, roots_legendre, spherical_in, spherical_jn


A = 4.0 / 5.0
PRIME_AMPLITUDE = (
    np.sqrt(2.0) * np.log(2.0)
    + 2.0 * np.log(3.0) / np.sqrt(3.0)
    + np.log(2.0)
)


# Optimizer of the even M=80, T=110, alpha=.29 block at 96 nodes per
# unit panel.  Coefficients correspond to normalized Legendre degrees
# 0,2,...,78.  The decimal strings, rather than regenerated eigendata, define
# the replay object and make its checksum independent of BLAS eigenvector
# conventions.
S110_WITNESS_DECIMALS = (
    "4.91523578781001058e-01", "-3.14364625588642657e-02",
    "-5.43994282467147761e-01", "6.01309720659136238e-01",
    "-3.08618627781932553e-01", "6.42617725118485167e-02",
    "1.60992694164635228e-02", "-1.57284175950281567e-02",
    "5.43455716832188119e-03", "-1.33143526408859383e-03",
    "4.35264287524278677e-04", "-2.18897960956828069e-04",
    "1.06249475297030160e-04", "-4.75019274738244579e-05",
    "1.75191002938029083e-05", "-5.78993506746700196e-06",
    "7.09484573862585838e-07", "1.24507507180682285e-06",
    "-2.64144316461378867e-07", "6.00382909152208483e-07",
    "-3.58411506548236942e-07", "-3.41080917752589805e-07",
    "-2.42320628464440993e-07", "1.17827855961732979e-07",
    "4.11052132805525656e-07", "2.66476165239820240e-08",
    "-2.16039855217148355e-07", "-1.79220175848310259e-07",
    "1.32508373509431675e-07", "1.21772183882869921e-07",
    "2.19656705576290501e-08", "-1.70972081691908610e-07",
    "-1.38178937359075027e-08", "1.62871022857738494e-07",
    "-1.16251097485343990e-08", "-1.89433419151095098e-07",
    "1.76358133350510071e-07", "-2.31636918715093992e-08",
    "-6.07223324003512137e-08", "5.12094402906754314e-09",
)


def witness_checksum() -> str:
    payload = json.dumps(list(S110_WITNESS_DECIMALS), separators=(",", ":"))
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def chuk_alpha(cutoff: int | float) -> float:
    """Chuk's conservative exterior floor beta-star."""
    cutoff = float(cutoff)
    return np.log(cutoff / (2.0 * pi)) - 1.0 / cutoff - PRIME_AMPLITUDE


def omega(r: np.ndarray) -> np.ndarray:
    log2 = np.log(2.0)
    log3 = np.log(3.0)
    return (
        np.real(digamma(0.25 + 0.5j * r))
        - np.log(pi)
        - np.sqrt(2.0) * log2 * np.cos(r * log2)
        - 2.0 * log3 / np.sqrt(3.0) * np.cos(r * log3)
        - log2 * np.cos(2.0 * r * log2)
    )


def panel_rule(cutoff: int, nodes_per_panel: int) -> tuple[np.ndarray, np.ndarray]:
    """Gauss--Legendre nodes and weights on consecutive unit panels."""
    x, w = roots_legendre(nodes_per_panel)
    r = np.concatenate([left + (x + 1.0) / 2.0 for left in range(cutoff)])
    weights = np.tile(w / 2.0, cutoff)
    return r, weights


def clipped_block(
    *,
    a: float,
    degree_cutoff: int,
    cutoff: int,
    alpha: float,
    nodes_per_panel: int,
    parity: int,
) -> np.ndarray:
    """Return one parity block for Legendre degrees below ``degree_cutoff``."""
    r, weights = panel_rule(cutoff, nodes_per_panel)
    weighted_symbol = weights * (omega(r) - alpha)
    degrees = np.arange(parity, degree_cutoff, 2)
    normalizers = np.sqrt(2.0 * a * (2.0 * degrees + 1.0))
    bessel = spherical_jn(degrees[:, None], a * r[None, :])
    phase = (-1.0) ** ((degrees[:, None] - degrees[None, :]) // 2)
    block = (
        alpha * np.eye(len(degrees))
        + phase
        * (normalizers[:, None] * normalizers[None, :])
        / pi
        * ((bessel * weighted_symbol) @ bessel.T)
    )

    # int b_k(x)e^(x/2) dx = sqrt(2a(2k+1)) i_k(a/2), and reflection
    # multiplies the coefficient by (-1)^k.
    pole_plus = normalizers * spherical_in(degrees, a / 2.0)
    reflection = (-1.0) ** degrees
    block += np.outer(pole_plus, pole_plus) * (
        reflection[:, None] + reflection[None, :]
    )
    return (block + block.T) / 2.0


def eigenvalues(block: np.ndarray, count: int = 3) -> list[float]:
    return [float(x) for x in np.linalg.eigvalsh(block)[:count]]


def fixed_witness() -> np.ndarray:
    vector = np.array([float(x) for x in S110_WITNESS_DECIMALS])
    return vector / np.linalg.norm(vector)


def rayleigh(block: np.ndarray, vector: np.ndarray) -> float:
    return float(vector @ block @ vector / (vector @ vector))


def run_scout() -> dict:
    witness = fixed_witness()
    convergence = []
    for nq in (16, 24, 32, 48, 64, 96):
        block = clipped_block(
            a=A,
            degree_cutoff=80,
            cutoff=110,
            alpha=0.29,
            nodes_per_panel=nq,
            parity=0,
        )
        convergence.append(
            {
                "nodes_per_panel": nq,
                "lambda_min": eigenvalues(block, 1)[0],
                "fixed_witness_rayleigh": rayleigh(block, witness),
            }
        )

    dimension_scan = []
    for degree_cutoff in (80, 100, 144, 200):
        block = clipped_block(
            a=A,
            degree_cutoff=degree_cutoff,
            cutoff=110,
            alpha=0.29,
            nodes_per_panel=64,
            parity=0,
        )
        dimension_scan.append(
            {
                "degree_cutoff": degree_cutoff,
                "even_modes": (degree_cutoff + 1) // 2,
                "lowest_three": eigenvalues(block),
            }
        )

    chuk_scan = []
    for cutoff in (120, 130, 140, 145, 150, 200):
        alpha = chuk_alpha(cutoff)
        even = clipped_block(
            a=A,
            degree_cutoff=80,
            cutoff=cutoff,
            alpha=alpha,
            nodes_per_panel=64,
            parity=0,
        )
        odd = clipped_block(
            a=A,
            degree_cutoff=80,
            cutoff=cutoff,
            alpha=alpha,
            nodes_per_panel=64,
            parity=1,
        )
        chuk_scan.append(
            {
                "cutoff": cutoff,
                "alpha": float(alpha),
                "even_lowest_three": eigenvalues(even),
                "odd_lowest_three": eigenvalues(odd),
            }
        )

    return {
        "schema": "zeta23.chuk_local_window_scout.v1",
        "evidence_label": "FLOATING_POINT_DIAGNOSTIC",
        "physical_half_width": A,
        "L_program": 4.0 * A,
        "active_prime_powers": [2, 3, 4],
        "prime_amplitude": float(PRIME_AMPLITUDE),
        "reported_chuk_alpha_150_replay": float(chuk_alpha(150)),
        "reported_chuk_alpha_200_replay": float(chuk_alpha(200)),
        "s110_witness": {
            "basis_degrees": list(range(0, 80, 2)),
            "coefficient_decimal_strings": list(S110_WITNESS_DECIMALS),
            "coefficient_sha256": witness_checksum(),
            "normalized_l2_norm": float(witness @ witness),
        },
        "s110_quadrature_convergence": convergence,
        "s110_dimension_scan": dimension_scan,
        "chuk_head_scan_degree_cutoff_80": chuk_scan,
        "warning": (
            "Values near 1e-15 are not sign-reliable in float64. "
            "The stable order-1e-13 S=110 negative witness is a method "
            "falsifier, not an interval theorem."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()
    result = run_scout()
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
        return
    print("a=0.8, L_program=3.2, active prime powers 2,3,4")
    print("prime amplitude", result["prime_amplitude"])
    print("alpha(150)", result["reported_chuk_alpha_150_replay"])
    print("alpha(200)", result["reported_chuk_alpha_200_replay"])
    print("S=110 witness sha256", result["s110_witness"]["coefficient_sha256"])
    for row in result["s110_quadrature_convergence"]:
        print("S110 quadrature", row)
    for row in result["s110_dimension_scan"]:
        print("S110 dimension", row)
    for row in result["chuk_head_scan_degree_cutoff_80"]:
        print("Chuk head", row)
    print(result["warning"])


if __name__ == "__main__":
    main()
