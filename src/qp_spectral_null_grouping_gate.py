"""Exact finite-aperture tools for the positive QP spectral-null problem.

The module contains only finite identities and exponent ledgers.  In
particular, it does not claim that the actual prime-log QP extremal promotes
or is killed at the required power scale.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Sequence

import numpy as np


QP_KAPPA = 0.0180303234
FULL_APERTURE_EXPONENT = 50.0 / 33.0


def central_atom_from_depth(depth: float) -> float:
    """Return ``p=r/(1+r)`` for a positive-antipode depth ``r``."""
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return depth / (1.0 + depth)


def depth_from_central_atom(atom: float) -> float:
    """Return ``r=p/(1-p)`` for a spectral-null atom at zero."""
    if not 0.0 <= atom < 1.0:
        raise ValueError("atom must lie in [0,1)")
    return atom / (1.0 - atom)


def odd_alias_at_or_above(node: float, lower: float) -> float:
    """Smallest positive ``s=(2m+1)pi/|node|`` with ``s>=lower``.

    It obeys ``s < lower+2*pi/|node|`` and
    ``exp(i*s*node)=-1`` (up to the sign of ``node``).
    """
    magnitude = abs(float(node))
    if magnitude == 0.0:
        raise ValueError("a zero node cannot be spectrally nulled")
    if lower < 0.0:
        raise ValueError("lower must be nonnegative")
    threshold = lower * magnitude / math.pi
    odd = max(1, int(math.ceil(threshold)))
    if odd % 2 == 0:
        odd += 1
    return odd * math.pi / magnitude


def bernoulli_aliases(nodes: Sequence[float], lower: float) -> np.ndarray:
    """One odd-half-period increment for every nonzero node."""
    values = np.asarray(nodes, dtype=float)
    return np.asarray(
        [odd_alias_at_or_above(float(node), lower) for node in values],
        dtype=float,
    )


@dataclass(frozen=True)
class BernoulliNullCertificate:
    aliases: np.ndarray
    lower: float
    upper: float
    central_atom: float
    depth: float
    max_fourier_residual: float


def bernoulli_null_certificate(
    nodes: Sequence[float], lower: float
) -> BernoulliNullCertificate:
    """Certify the one-sided Bernoulli convolution and its symmetrization.

    The one-sided measure is the convolution of
    ``(delta_0+delta_{s_j})/2``.  Its Fourier transform vanishes at node
    ``u_j`` because the corresponding factor is zero.  Symmetrization makes
    the measure even without changing its atom at zero.  Every nonzero
    support point has modulus at least ``lower`` and at most ``sum(s_j)``.
    """
    values = np.asarray(nodes, dtype=float)
    aliases = bernoulli_aliases(values, lower)
    phases = aliases[:, None] * values[None, :]
    factors = 0.5 * (1.0 + np.exp(1j * phases))
    transform = np.prod(factors, axis=0)
    atom = math.ldexp(1.0, -len(values))
    return BernoulliNullCertificate(
        aliases=aliases,
        lower=float(lower),
        upper=float(np.sum(aliases)),
        central_atom=atom,
        depth=depth_from_central_atom(atom),
        max_fourier_residual=float(np.max(np.abs(transform), initial=0.0)),
    )


def reciprocal_node_sum_bound(y: float, width: float) -> float:
    """Elementary all-integer bound for a half-integer shell centre.

    For ``y=N+1/2`` and integers ``n`` in the multiplicative width-``width``
    shell, this returns a valid upper bound for
    ``sum 1/|log(n/y)|``.  Prime powers are a subset of those integers.
    """
    if y <= 2.5 or width <= 0:
        raise ValueError("use y>2.5 and positive width")
    if abs((y - 0.5) - round(y - 0.5)) > 1e-10:
        raise ValueError("the elementary bound assumes y=N+1/2")
    radius = int(math.ceil(y * max(1.0 - math.exp(-width), math.exp(width) - 1.0)))
    # |log(1+x)| >= |x| exp(-width) throughout the shell.
    # For the decreasing function f(x)=1/(x+1/2), isolate k=0 and
    # dominate every k>=1 term by the integral on [k-1,k].
    harmonic_half = 2.0 + math.log(2.0 * radius + 1.0)
    return 2.0 * y * math.exp(width) * harmonic_half


def bernoulli_support_upper_bound(
    *, y: float, width: float, node_count: int, lower: float
) -> float:
    """Bound ``sum s_j`` by ``M*T+2*pi*sum 1/|u_j|``."""
    return (
        float(node_count) * float(lower)
        + 2.0 * math.pi * reciprocal_node_sum_bound(y, width)
    )


def grouped_product_depth_upper(group_count: int) -> float:
    """Best possible depth from the universal ``p_g<=1/2`` factor bound.

    This applies to one-sided convolution architectures with ``group_count``
    nonempty spectral-null factors.  Nonnegative supports ensure that the
    atom at zero of the convolution is exactly the product of factor atoms.
    """
    if group_count < 1:
        raise ValueError("group_count must be positive")
    return 1.0 / (2.0**group_count - 1.0)


def max_groups_for_target_depth(depth: float) -> int:
    """Largest group count not already excluded by ``p_g<=1/2``."""
    if not 0.0 < depth < 1.0:
        raise ValueError("depth must lie in (0,1)")
    return int(math.floor(math.log2(1.0 + 1.0 / depth)))


def required_group_size(node_count: int, depth: float) -> int:
    """Pigeonhole group size needed by a grouped product at depth ``depth``."""
    groups = max(1, max_groups_for_target_depth(depth))
    return int(math.ceil(node_count / groups))


def haar_adaptive_support_log_bound(
    *, node_count: int, max_harmonic: int, depth: float
) -> float:
    """Log of ``D exp(-M r^2/2)`` for adaptive harmonic supports.

    If a positive antipode of depth at least ``r`` uses any subset of
    harmonics ``1,...,D``, pairing with the all-ones vector forces one of the
    ``D`` cosine sums below ``-rM``.  Hoeffding and a union bound give this
    probability for iid Haar phases.
    """
    if node_count < 1 or max_harmonic < 1 or not 0.0 < depth < 1.0:
        raise ValueError("invalid metric parameters")
    return math.log(max_harmonic) - 0.5 * node_count * depth * depth


def target_metric_power(eta: float = 0.0) -> float:
    """Power in ``M r^2=Y^(1-2*kappa+2*eta-o(1))``."""
    return 1.0 - 2.0 * QP_KAPPA + 2.0 * eta


def finite_pool_positive_depth(atoms: np.ndarray, tolerance: float = 1e-9) -> float:
    """Solve the finite-pool positive-antipode LP for small replay fixtures."""
    from scipy.optimize import linprog

    matrix = np.asarray(atoms, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] < 1 or matrix.shape[1] < 1:
        raise ValueError("atoms must be a nonempty coordinate-by-atom matrix")
    coordinates, count = matrix.shape
    # Variables are probability weights followed by depth r.
    objective = np.zeros(count + 1)
    objective[-1] = -1.0
    equality = np.zeros((coordinates + 1, count + 1))
    equality[:coordinates, :count] = matrix
    equality[:coordinates, -1] = 1.0
    equality[-1, :count] = 1.0
    rhs = np.zeros(coordinates + 1)
    rhs[-1] = 1.0
    result = linprog(
        objective,
        A_eq=equality,
        b_eq=rhs,
        bounds=[(0.0, None)] * count + [(0.0, 1.0)],
        method="highs",
    )
    if not result.success:
        return 0.0
    depth = float(result.x[-1])
    residual = np.max(np.abs(equality @ result.x - rhs))
    if residual > tolerance:
        raise RuntimeError(f"LP residual {residual} exceeds tolerance")
    return depth


def finite_pool_delsarte_value(atoms: np.ndarray, tolerance: float = 1e-9) -> float:
    """Compute ``A_H`` for a finite atom pool.

    For a coordinate-by-atom matrix ``A``, maximize
    ``1+sum(lambda_j)`` subject to ``1+A[:,l].lambda>=0`` for every atom.
    The reciprocal identity predicts ``r_+=1/(A_H-1)``.
    """
    from scipy.optimize import linprog

    matrix = np.asarray(atoms, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] < 1 or matrix.shape[1] < 1:
        raise ValueError("atoms must be a nonempty coordinate-by-atom matrix")
    coordinates = matrix.shape[0]
    result = linprog(
        -np.ones(coordinates),
        A_ub=-matrix.T,
        b_ub=np.ones(matrix.shape[1]),
        bounds=[(None, None)] * coordinates,
        method="highs",
    )
    if not result.success:
        return math.inf
    slack = 1.0 + matrix.T @ result.x
    if float(np.min(slack)) < -tolerance:
        raise RuntimeError("Delsarte solver returned an infeasible polynomial")
    return 1.0 + float(np.sum(result.x))
