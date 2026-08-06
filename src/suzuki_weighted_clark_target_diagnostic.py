"""Root-free weighted Clark-measure comparison with the xi target.

Let

    S_xi(z) = (ell-L(1/2-i z))/(ell+L(1/2-i z)),
    ell = L(3/2),  L=xi'/xi.

For the Clark parameter ``alpha=-1``, put

    H=(1-S)/(1+S),
    m(z)=(i H(z)-z)/(1+z^2).

Under RH, ``m`` is the Cauchy transform of the normalized reference spectral
measure

    nu = (1/ell) sum_gamma m_gamma/(1+gamma^2) delta_gamma.

The displayed meromorphic formula is unconditional; its interpretation as a
positive measure on the real line is conditional on RH.  Comparing ``m``
avoids locating roots and differentiating a rapidly winding phase.  Local
uniform convergence of the corresponding finite Cauchy transforms is a
necessary consequence of spectral-measure convergence for the named
reference vectors.  It becomes a consequence of varying-space strong
resolvent convergence only after comparison maps are fixed and the embedded
finite reference vectors are proved to converge to a fixed ambient vector.

The finite rows use the already documented one-scalar derivative calibration
of ``FiniteLivsicModel``.  They are high-precision Galerkin diagnostics, not
continuum spectral measures.  Agreement near the normalization point ``i``
is a weak test; probes near the first zeta ordinate are deliberately retained.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from typing import Sequence

import mpmath as mp

from spectral_margins import spectral_form
from suzuki_livsic_calibration import (
    FiniteLivsicModel,
    XiLivsicTarget,
    calibrate_resolvent_ratio,
    exponential_legendre_coefficients,
)


DEFAULT_PROBES = (
    ("i/4", mp.mpc(0, mp.mpf("0.25"))),
    ("2i", mp.mpc(0, 2)),
    ("10i", mp.mpc(0, 10)),
    ("2+.5i", mp.mpc(2, mp.mpf("0.5"))),
    ("14+.5i", mp.mpc(14, mp.mpf("0.5"))),
    ("14+2i", mp.mpc(14, 2)),
)


def cauchy_transform_from_characteristic(
    characteristic_value: complex | mp.mpc | mp.mpf,
    z: complex | mp.mpc | mp.mpf,
) -> mp.mpc:
    """Apply the normalized Clark-to-Cauchy Möbius transform."""

    value = mp.mpc(z)
    characteristic = mp.mpc(characteristic_value)
    if abs(1 + characteristic) == 0:
        raise ZeroDivisionError("the Clark Herglotz denominator vanishes")
    if abs(1 + value**2) == 0:
        raise ZeroDivisionError("use the removable limit at z=+/-i")
    herglotz = (1 - characteristic) / (1 + characteristic)
    return (mp.j * herglotz - value) / (1 + value**2)


def first_symmetric_zero_pair_mass(
    first_ordinate: mp.mpf, ell: mp.mpf
) -> mp.mpf:
    """Mass of a simple pair ``+/-gamma_1`` in the conditional xi measure."""

    ordinate = mp.mpf(first_ordinate)
    normalization = mp.mpf(ell)
    if ordinate <= 0 or normalization <= 0:
        raise ValueError("ordinate and ell must be positive")
    return 2 / (normalization * (1 + ordinate**2))


@dataclass(frozen=True)
class WeightedTargetRow:
    support: float
    dimension: int
    sigma: mp.mpf
    condition_estimate: mp.mpf
    errors: tuple[tuple[str, mp.mpf], ...]
    model_status: str = "finite-Galerkin diagnostic"
    target_measure_status: str = "positive Clark measure conditional on RH"


def build_weighted_target_row(
    support: float,
    dimension: int,
    dps: int,
    target: XiLivsicTarget,
    probes: Sequence[tuple[str, mp.mpc]] = DEFAULT_PROBES,
) -> WeightedTargetRow:
    """Calibrate one finite model and compare root-free Cauchy transforms."""

    with mp.workdps(dps + 15):
        matrix = spectral_form(support, dimension, dps=dps)
        radius = mp.mpf(str(support)) / 4
        forcing = exponential_legendre_coefficients(radius, dimension)
        calibration = calibrate_resolvent_ratio(
            matrix, forcing, target.rho, dps=dps
        )
        model = FiniteLivsicModel(
            matrix, radius, calibration, dps=dps
        )
        errors: list[tuple[str, mp.mpf]] = []
        for label, probe in probes:
            target_cauchy = cauchy_transform_from_characteristic(
                target.characteristic(probe), probe
            )
            model_cauchy = cauchy_transform_from_characteristic(
                model.characteristic(probe), probe
            )
            errors.append((label, +abs(model_cauchy - target_cauchy)))
        return WeightedTargetRow(
            support=float(support),
            dimension=dimension,
            sigma=+calibration.sigma,
            condition_estimate=+calibration.condition_estimate,
            errors=tuple(errors),
        )


def _number(value: mp.mpf, digits: int = 16) -> str:
    return mp.nstr(value, digits)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--supports", type=float, nargs="+", default=[1.75, 2.485, 2.996]
    )
    parser.add_argument(
        "--dimensions", type=int, nargs="+", default=[8, 10, 12]
    )
    parser.add_argument("--dps", type=int, default=50)
    args = parser.parse_args()
    if args.dps < 40:
        parser.error("use at least 40 decimal digits near the calibrated floor")

    with mp.workdps(args.dps + 15):
        target = XiLivsicTarget.compute(dps=args.dps)
        fieldnames = [
            "support",
            "dimension",
            "sigma",
            "condition_estimate",
            *(f"cauchy_error_{label}" for label, _ in DEFAULT_PROBES),
            "model_status",
            "target_measure_status",
        ]
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        for support in args.supports:
            for dimension in args.dimensions:
                row = build_weighted_target_row(
                    support, dimension, args.dps, target
                )
                errors = dict(row.errors)
                writer.writerow(
                    {
                        "support": row.support,
                        "dimension": row.dimension,
                        "sigma": _number(row.sigma),
                        "condition_estimate": _number(
                            row.condition_estimate
                        ),
                        **{
                            f"cauchy_error_{label}": _number(errors[label])
                            for label, _ in DEFAULT_PROBES
                        },
                        "model_status": row.model_status,
                        "target_measure_status": row.target_measure_status,
                    }
                )
                sys.stdout.flush()


if __name__ == "__main__":
    main()
