"""Exact exponent ledger for the center-density strip adapter.

This module does not prove the averaged conductor fourth moment, LTRAD, a
zero-free strip, or RH.  It records two elementary consequences of the
existing reductions:

* a fixed Turan interval sum is negatively aligned at a positive density of
  eligible half-integer centers;
* an averaged fourth-moment estimate bounds the number of centers at which
  the retained-hat upper antenna can fail.

The two center sets must intersect when the lower-return success set is
larger than the upper exceptional set.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math


FULL_APERTURE = Fraction(50, 33)
BENCHMARK_TURAN_APERTURE = Fraction(1, 1)
FOURTH_MOMENT_DECAY = Fraction(1187, 13000)
# The fixed-hat adapter proves every exponent strictly below .019, not the
# endpoint itself.  Freeze the safely licensed midpoint between .0189 and
# .019 for the density ledger.
POINTWISE_UPPER_EXPONENT = Fraction(379, 20000)
RADIAL_LOWER_EXPONENT = Fraction(189, 10000)
SOURCE_DEPTH_EXPONENT = Fraction(1, 1000)
PERSISTENCE_POWER = Fraction(9, 2)
CENTER_EXCEPTION_SAVING = (
    FOURTH_MOMENT_DECAY
    - PERSISTENCE_POWER * POINTWISE_UPPER_EXPONENT
)


def phase_discrepancy_saving(aperture: Fraction) -> Fraction:
    """Power saving from optimized Erdos--Turan plus van der Corput.

    For ``N^(1/2) <= tau <= N^aperture`` and ``aperture < 2``, truncating
    Erdos--Turan at ``H=N^eta`` gives

        D_N << N^-eta + N^((aperture+eta)/2-1) + N^-1/4.

    Balancing the first two terms gives ``eta=(2-aperture)/3``.  The last
    term caps the resulting saving at ``1/4``.
    """

    aperture = Fraction(aperture)
    if not Fraction(1, 2) <= aperture < 2:
        raise ValueError("aperture must lie in [1/2,2)")
    return min((2 - aperture) / 3, Fraction(1, 4))


def negative_arc_density(kappa: float) -> float:
    """Normalized measure of ``{theta: cos(theta) <= -kappa}``."""

    if not 0.0 < kappa < 1.0:
        raise ValueError("kappa must lie strictly between zero and one")
    return math.acos(kappa) / math.pi


def eligible_interval_min_fraction(width: float) -> float:
    """Guaranteed ``#J/N`` lower factor for the partitioned Turan interval."""

    if width <= 0:
        raise ValueError("width must be positive")
    return math.expm1(width)


def absolute_witness_min_density(kappa: float, width: float) -> float:
    """Guaranteed asymptotic witness density relative to a length-N block."""

    return negative_arc_density(kappa) * eligible_interval_min_fraction(width)


def center_exception_saving(
    moment_decay: Fraction,
    pointwise_exponent: Fraction,
    *,
    persistence_power: Fraction = PERSISTENCE_POWER,
) -> Fraction:
    """Return ``gamma-r*c`` in the averaged-moment Markov argument."""

    return Fraction(moment_decay) - Fraction(persistence_power) * Fraction(
        pointwise_exponent
    )


def center_sets_must_intersect(
    exception_saving: Fraction,
    lower_success_loss: Fraction,
) -> bool:
    """Check the strict exponent condition for the two center sets.

    An upper exceptional set of size ``N^(1-m+o(1))`` cannot contain a lower
    success set of size ``N^(1-rho-o(1))`` when ``rho < m``.
    """

    return Fraction(lower_success_loss) < Fraction(exception_saving)


@dataclass(frozen=True)
class CenterDensityLedger:
    """Frozen benchmark for the conditional center-density adapter."""

    moment_decay: Fraction = FOURTH_MOMENT_DECAY
    pointwise_upper_exponent: Fraction = POINTWISE_UPPER_EXPONENT
    radial_lower_exponent: Fraction = RADIAL_LOWER_EXPONENT
    source_depth_exponent: Fraction = SOURCE_DEPTH_EXPONENT

    @property
    def exception_saving(self) -> Fraction:
        return center_exception_saving(
            self.moment_decay,
            self.pointwise_upper_exponent,
        )

    def closes_conditionally(self, lower_success_loss: Fraction) -> bool:
        """Check only the deterministic strict-exponent conditions.

        The answer is conditional on the averaged fourth-moment estimate and
        the stated event-conditioned radialization multiplicity theorem.
        """

        return (
            self.pointwise_upper_exponent > self.radial_lower_exponent
            and self.exception_saving > 0
            and center_sets_must_intersect(
                self.exception_saving,
                lower_success_loss,
            )
        )


def ledger_payload() -> dict[str, str | bool | float]:
    """Return the exact benchmark ledger in serialization-friendly form."""

    ledger = CenterDensityLedger()
    return {
        "fourth_moment_decay": str(ledger.moment_decay),
        "pointwise_upper_exponent": str(ledger.pointwise_upper_exponent),
        "radial_lower_exponent": str(ledger.radial_lower_exponent),
        "source_depth_exponent": str(ledger.source_depth_exponent),
        "persistence_power": str(PERSISTENCE_POWER),
        "center_exception_saving": str(ledger.exception_saving),
        "full_aperture_phase_discrepancy_saving": str(
            phase_discrepancy_saving(FULL_APERTURE)
        ),
        "benchmark_phase_discrepancy_saving": str(
            phase_discrepancy_saving(BENCHMARK_TURAN_APERTURE)
        ),
        "three_quarter_negative_arc_density": negative_arc_density(0.75),
        "eligible_interval_min_fraction_at_width_one_fifth": (
            eligible_interval_min_fraction(0.2)
        ),
        "absolute_three_quarter_witness_min_density": (
            absolute_witness_min_density(0.75, 0.2)
        ),
        "positive_density_ltrad_closes_conditionally": (
            ledger.closes_conditionally(Fraction(0))
        ),
        "averaged_gcg4_status": "OPEN",
        "event_conditioned_density_ltrad_status": "OPEN",
        "uniform_zero_free_strip_status": "OPEN",
        "RH_status": "OPEN",
    }
