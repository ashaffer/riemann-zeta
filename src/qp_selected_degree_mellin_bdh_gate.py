"""Exponent and scale ledgers for the selected-degree Mellin/BDH gate.

The accompanying report derives the centered dual Perron formula and audits
two existing positive mean-value routes:

* ordinary under-Nyquist sampling at bandwidth ``T=q^2/D``;
* the Heath--Brown sparse mean-value theorem used by
  Matomaki--Teravainen.

The routines here merely replay exact scale algebra.  They do not assert
the missing mask-sensitive selected-degree BDH estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class SelectedDegreeMellinLedger:
    q_exponent: Fraction
    d_exponent: Fraction
    support_exponent: Fraction
    mellin_bandwidth_exponent: Fraction
    desired_squared_exponent: Fraction
    ordinary_sampling_squared_exponent: Fraction
    ordinary_sampling_deficit: Fraction
    heath_brown_nonpolar_squared_exponent: Fraction
    heath_brown_nonpolar_deficit: Fraction
    heath_brown_support_threshold_exponent: Fraction
    improved_mean_shift_exponent: Fraction


def selected_degree_mellin_ledger(
    *,
    q_exponent: Fraction = Fraction(33, 16),
    d_exponent: Fraction = Fraction(1, 1),
    support_exponent: Fraction = Fraction(15, 8),
) -> SelectedDegreeMellinLedger:
    r"""Return the balanced Perron/mean-value exponent ledger.

    If ``q=D^Q`` and ``M=D^m``, then

    ``T=q^2/D``, the desired squared dual norm is ``M*D``, the
    optimistic ordinary large-sieve ledger is ``q*M``, and the nonpolar
    term supplied by the cited Heath--Brown sparse theorem is ``q^2``.
    """

    Q = Fraction(q_exponent)
    d = Fraction(d_exponent)
    m = Fraction(support_exponent)
    bandwidth = 2 * Q - d
    desired = m + d
    ordinary = Q + m
    heath_brown = 2 * Q
    return SelectedDegreeMellinLedger(
        q_exponent=Q,
        d_exponent=d,
        support_exponent=m,
        mellin_bandwidth_exponent=bandwidth,
        desired_squared_exponent=desired,
        ordinary_sampling_squared_exponent=ordinary,
        ordinary_sampling_deficit=ordinary - desired,
        heath_brown_nonpolar_squared_exponent=heath_brown,
        heath_brown_nonpolar_deficit=heath_brown - desired,
        # q^2 <= M*D is exactly M >= q^2/D = T.
        heath_brown_support_threshold_exponent=bandwidth,
        # The improved mean theorem sees additive shifts N/T=D for N=q^2.
        improved_mean_shift_exponent=d,
    )


@dataclass(frozen=True)
class HeathBrownZeroLineScales:
    coherent_term: Fraction
    nonpolar_term: Fraction
    mellin_weighted_coherent_term: Fraction
    mellin_weighted_nonpolar_term: Fraction


def heath_brown_zero_line_scales(
    *,
    q_exponent: Fraction,
    bandwidth_exponent: Fraction,
    beta_support_exponent: Fraction,
) -> HeathBrownZeroLineScales:
    r"""Translate the sparse theorem to a normalized beta block.

    Let a dual vector have ``R`` coordinates of size ``R^(-1/2)``.
    With the sparse polynomial at length ``q`` and the other polynomial at
    length ``q^2``, the zero-line theorem gives

    ``integral <= R*q^4 + T*q^2``

    after suppressing logarithms and coefficient heights.  Multiplication
    by the squared Mellin-window scale ``eta=1/T`` leaves

    ``R*q^4/T + q^2``.
    """

    Q = Fraction(q_exponent)
    tau = Fraction(bandwidth_exponent)
    rho = Fraction(beta_support_exponent)
    return HeathBrownZeroLineScales(
        coherent_term=rho + 4 * Q,
        nonpolar_term=tau + 2 * Q,
        mellin_weighted_coherent_term=rho + 4 * Q - tau,
        mellin_weighted_nonpolar_term=2 * Q,
    )

