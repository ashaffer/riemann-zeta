"""Finite certificates for the two-index Poincare/polar-projection audit.

The accompanying report derives the exact automorphic identity from
Blomer's level-one GL(3) Kuznetsov formula and the level-N formula of
Blomer--Buttcane--Maga.  This module records the pieces that have useful
finite linear-algebra checks:

* the complete list of generic spectral and Weyl channels;
* Pythagorean contraction after projecting complete Eisenstein rows;
* the distinction between that automorphic norm and the physical source
  ``ell^2`` norm; and
* the rank-one cuspidal alignment obstruction, including finite Satake
  prime-power fixtures.

It does not assert a sharp large sieve for the restricted QP hyperbolic
window.  That finite-scale arithmetic estimate remains the open gate.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Iterable, Sequence


ComplexRow = Sequence[complex]


@dataclass(frozen=True)
class TwoIndexKuznetsovChannels:
    cuspidal: bool
    minimal_eisenstein: bool
    maximal_eisenstein_from_gl2_cusp: bool
    residual_constant_generic_coefficient: bool
    identity_weyl: bool
    short_weyl_w4: bool
    short_weyl_w5: bool
    long_weyl_w6: bool
    other_weyl_elements_for_generic_indices: bool
    short_weyl_channels_are_spectral_projections: bool


def two_index_kuznetsov_channels() -> TwoIndexKuznetsovChannels:
    """Return the exact channel inventory for two positive GL(3) indices."""

    return TwoIndexKuznetsovChannels(
        cuspidal=True,
        minimal_eisenstein=True,
        maximal_eisenstein_from_gl2_cusp=True,
        residual_constant_generic_coefficient=False,
        identity_weyl=True,
        short_weyl_w4=True,
        short_weyl_w5=True,
        long_weyl_w6=True,
        other_weyl_elements_for_generic_indices=False,
        short_weyl_channels_are_spectral_projections=False,
    )


def spectral_row_value(data: ComplexRow, row: ComplexRow) -> complex:
    r"""Return the linear spectral coefficient ``sum_i data_i row_i``."""

    if len(data) != len(row):
        raise ValueError("data and spectral row must have the same length")
    return sum(complex(value) * complex(coefficient) for value, coefficient in zip(data, row))


def spectral_family_squared_norm(data: ComplexRow, rows: Iterable[ComplexRow]) -> float:
    """Return the squared norm of all supplied orthonormal spectral rows."""

    return float(sum(abs(spectral_row_value(data, row)) ** 2 for row in rows))


@dataclass(frozen=True)
class PolarProjectionLedger:
    source_squared_norm: float
    complete_automorphic_squared_norm: float
    polar_squared_norm: float
    cuspidal_residual_squared_norm: float
    pythagorean_error: float
    automorphic_projection_is_contractive: bool
    physical_source_contraction_holds: bool


def polar_projection_ledger(
    data: ComplexRow,
    cusp_rows: Iterable[ComplexRow],
    minimal_eisenstein_rows: Iterable[ComplexRow] = (),
    maximal_eisenstein_rows: Iterable[ComplexRow] = (),
    tolerance: float = 1e-12,
) -> PolarProjectionLedger:
    r"""Project away all finite-model Eisenstein rows and compare norms.

    Rows are understood to include the square roots of their Plancherel
    weights.  They model mutually orthogonal target coordinates, so the
    complete target norm is the sum of their squared evaluations.

    Orthogonal projection is always contractive relative to the complete
    *target* norm.  It need not be contractive relative to the source
    coefficient norm; that would be an additional large-sieve estimate.
    """

    values = tuple(complex(value) for value in data)
    cusp = tuple(tuple(complex(entry) for entry in row) for row in cusp_rows)
    minimal = tuple(
        tuple(complex(entry) for entry in row) for row in minimal_eisenstein_rows
    )
    maximal = tuple(
        tuple(complex(entry) for entry in row) for row in maximal_eisenstein_rows
    )
    source = float(sum(abs(value) ** 2 for value in values))
    cusp_norm = spectral_family_squared_norm(values, cusp)
    polar_norm = spectral_family_squared_norm(values, minimal + maximal)
    complete = cusp_norm + polar_norm
    error = complete - polar_norm - cusp_norm
    return PolarProjectionLedger(
        source_squared_norm=source,
        complete_automorphic_squared_norm=complete,
        polar_squared_norm=polar_norm,
        cuspidal_residual_squared_norm=cusp_norm,
        pythagorean_error=error,
        automorphic_projection_is_contractive=cusp_norm <= complete + tolerance,
        physical_source_contraction_holds=cusp_norm <= source + tolerance,
    )


def satake_prime_power_coefficients(
    parameters: Sequence[complex], maximum_power: int
) -> tuple[complex, ...]:
    r"""Return ``A(1,p^k)`` from ``prod_i(1-alpha_i X)^(-1)``.

    The output consists of the complete homogeneous symmetric polynomials
    in the supplied Satake parameters for ``0 <= k <= maximum_power``.
    """

    degree = int(maximum_power)
    if degree < 0:
        raise ValueError("maximum_power must be nonnegative")
    if not parameters:
        raise ValueError("at least one Satake parameter is required")
    coefficients = [0j] * (degree + 1)
    coefficients[0] = 1 + 0j
    for raw_parameter in parameters:
        parameter = complex(raw_parameter)
        if parameter == 0:
            raise ValueError("Satake parameters must be nonzero")
        previous = tuple(coefficients)
        coefficients = [0j] * (degree + 1)
        for total_degree in range(degree + 1):
            coefficients[total_degree] = sum(
                previous[total_degree - exponent] * parameter**exponent
                for exponent in range(total_degree + 1)
            )
    return tuple(coefficients)


@dataclass(frozen=True)
class CuspAlignmentLedger:
    coefficient_squared_energy: float
    normalized_source_squared_norm: float
    retained_cusp_squared_norm: float
    amplification_over_source: float


def cusp_alignment_ledger(
    coefficient_row: ComplexRow,
    whittaker_weight_over_form_norm: float = 1.0,
) -> CuspAlignmentLedger:
    r"""Align unit source data with one retained cuspidal spectral row.

    If ``a_i`` are Fourier coefficients of one cusp form and
    ``c=|<W,Phi>|^2/||phi||^2``, take
    ``f_i=conj(a_i)/(sum |a_i|^2)^(1/2)``.  Its source norm is one, while
    that single cuspidal coordinate contributes ``c*sum |a_i|^2``.
    """

    row = tuple(complex(value) for value in coefficient_row)
    energy = float(sum(abs(value) ** 2 for value in row))
    if energy <= 0:
        raise ValueError("coefficient row must be nonzero")
    weight = float(whittaker_weight_over_form_norm)
    if weight < 0:
        raise ValueError("spectral weight must be nonnegative")
    normalization = sqrt(energy)
    data = tuple(value.conjugate() / normalization for value in row)
    source = float(sum(abs(value) ** 2 for value in data))
    retained = weight * abs(spectral_row_value(data, row)) ** 2
    return CuspAlignmentLedger(
        coefficient_squared_energy=energy,
        normalized_source_squared_norm=source,
        retained_cusp_squared_norm=retained,
        amplification_over_source=retained / source,
    )


def finite_support_cusp_operator_lower_bound(
    coefficient_squared_energy: float,
    whittaker_weight_over_form_norm: float,
) -> float:
    r"""Lower bound for ``||Pi_cusp S_Phi||^2`` on one finite support."""

    energy = float(coefficient_squared_energy)
    weight = float(whittaker_weight_over_form_norm)
    if energy < 0 or weight < 0:
        raise ValueError("energy and weight must be nonnegative")
    return energy * weight

