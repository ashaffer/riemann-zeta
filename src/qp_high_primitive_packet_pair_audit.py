"""Exact ledgers for high primitive tangents and packet-pair overlap.

The companion report separates three facts which are easy to conflate:

* a reduced symmetric tangent of slope ``(p+d)/(2p)`` has a primitive
  first-coordinate step of order ``p**4``;
* one exact tangent (or one fixed parallel line) therefore has bounded
  product-band occupancy in the Fejer energy core;
* this local spacing does not imply almost orthogonality of different
  packet pairs in the completion-sum variable.

The routines below replay the exact parity formula, the exponent ledger,
an infinite reflected remote family, and the elementary entrywise
domination which bridges a hereditary completion-energy theorem to a
factorable post-peeling mask.  They do not prove the remaining reciprocal
strip restriction theorem.
"""

from __future__ import annotations

import cmath
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import ceil, gcd, isqrt
from typing import Mapping, Sequence

from qp_coupled_cusp_fejer_inverse import (
    ReducedSymmetricCuspData,
    reduced_symmetric_cusp_data,
)
from qp_dual_tangent_major_arc import symmetric_tangent_alias_data
from qp_dual_tangent_major_arc import symmetric_cyclic_fejer_bound
from qp_four_cycle_rational_tangent import tangent_component_point_bound


@dataclass(frozen=True)
class PrimitiveSymmetricTangentSteps:
    """Primitive direction at ``t=(p+d)/(2p)`` for ``lambda=1/4``."""

    p: int
    d: int
    tangent_numerator: int
    tangent_complement: int
    parity_divisor: int
    parity_index: int
    first_step: int
    decreasing_step: int
    increasing_step: int

    @property
    def left_product_curvature(self) -> int:
        return self.first_step * self.decreasing_step

    @property
    def right_product_curvature(self) -> int:
        return self.first_step * self.increasing_step


@dataclass(frozen=True)
class RemoteReflectionFixture:
    """Two reflected, nonmajor symmetric-cusp points at one centre."""

    Q: int
    h: int
    c: int
    t: int
    required_band: int
    positive: ReducedSymmetricCuspData
    negative: ReducedSymmetricCuspData

    @property
    def first_coordinates(self) -> tuple[int, int]:
        return self.Q + self.positive.y, self.Q + self.negative.y


def primitive_symmetric_tangent_steps(
    p: int, d: int
) -> PrimitiveSymmetricTangentSteps:
    """Return the exact primitive tangent direction, including parity.

    For ``(p,d)=1`` and ``|d|<p``, reduce

    ``(p+d)/(p-d)``

    by ``c=gcd(p+d,p-d)``.  Necessarily ``c`` is one or two.  If ``p,d``
    are both odd, put ``chi=4``; otherwise put ``chi=1``.  The direction is

    ``(R,-P,K)`` with

    ``R=(p^2-d^2)^2/chi``,
    ``P=p^2*(p-d)^2/chi``, and
    ``K=p^2*(p+d)^2/chi``.
    """

    if p <= 0 or abs(d) >= p or gcd(p, abs(d)) != 1:
        raise ValueError("require p>0, |d|<p, and gcd(p,d)=1")
    common = gcd(p + d, p - d)
    if common not in (1, 2):
        raise AssertionError("a primitive (p,d) has only the parity divisor")
    numerator = (p + d) // common
    complement = (p - d) // common
    alias = symmetric_tangent_alias_data(numerator, complement)
    first, minus_decreasing, increasing = alias.direction
    chi = 4 if p % 2 and d % 2 else 1
    assert first == (p * p - d * d) ** 2 // chi
    assert -minus_decreasing == p * p * (p - d) ** 2 // chi
    assert increasing == p * p * (p + d) ** 2 // chi
    return PrimitiveSymmetricTangentSteps(
        p=p,
        d=d,
        tangent_numerator=numerator,
        tangent_complement=complement,
        parity_divisor=chi,
        parity_index=alias.parity_index,
        first_step=first,
        decreasing_step=-minus_decreasing,
        increasing_step=increasing,
    )


def energy_core_height_exponents() -> dict[str, Fraction]:
    """Return the exact powers of ``D`` in the energy-core height ledger.

    The energy tail leaves ``m^2*M^3<D^(1/2)`` with ``1<=m<=M``.  Thus
    ``m<D^(1/10)`` and ``M<D^(1/6)``.  Combining ``B=D*M`` with the remote
    lower bound ``p>>(Q/B)^(1/3)`` and ``Q=D^(33/16)`` gives
    ``p>>D^(43/144)``.
    """

    return {
        "Q": Fraction(33, 16),
        "max_m": Fraction(1, 10),
        "max_M": Fraction(1, 6),
        "max_A": Fraction(11, 10),
        "max_B": Fraction(7, 6),
        "primitive_p_floor": Fraction(43, 144),
        "first_step_floor": Fraction(43, 36),
        "product_curvature_floor": Fraction(43, 18),
        "max_sqrt_A": Fraction(11, 20),
        "first_step_over_sqrt_A": Fraction(29, 45),
        "curvature_over_A": Fraction(58, 45),
        "farey_cardinality_closure_max_p": Fraction(11, 40),
        "farey_to_remote_height_gap": Fraction(17, 720),
        "balanced_height_zero_count": Fraction(23, 96),
        # The older pointwise core m*M^2<D^(1/2), for comparison.
        "pointwise_max_A": Fraction(7, 6),
        "pointwise_p_floor": Fraction(13, 48),
        "pointwise_first_step_floor": Fraction(13, 12),
        "pointwise_first_step_over_sqrt_A": Fraction(1, 2),
    }


def thickened_crt_exponent_ledger() -> dict[str, Fraction]:
    """Powers relevant to the conditional thickened-CRT square function.

    In the Farey-valid hard range, put

    ``N~sqrt(G*P^5/Q)`` and ``W~H*B*P^3/(Q*G)``.

    Then ``N*P^(-4)*sqrt(W)=sqrt(H*B)/Q``.  At the worst energy
    endpoint, multiplying this by the Airy amplitude ``D^(49/48)`` leaves
    ``D^(7/96)``.  This is only a conditional ledger: the required
    square-root summation over the ``W`` residue layers needs an actual
    outer orthogonality variable.

    Also, ``P_f=QG/B`` is always beyond the exact-CRT support threshold
    ``sqrt(H)``.  The gap is ``D^(35/96)`` already at ``G=1``.
    """

    return {
        "H": Fraction(17, 16),
        "max_B": Fraction(7, 6),
        "Q": Fraction(33, 16),
        "airy_amplitude": Fraction(49, 48),
        "sqrt_HB_over_Q": Fraction(-91, 96),
        "conditional_thickened_total": Fraction(7, 96),
        "farey_failure_floor": Fraction(43, 48),
        "exact_crt_support_ceiling": Fraction(17, 32),
        "failure_beyond_exact_support_gap": Fraction(35, 96),
        "exact_weighted_hard_total": Fraction(73, 240),
        "high_plateau_conditional_boundary_at_v0": Fraction(253, 384),
        "farey_failure_physical_lower_bound": Fraction(173, 96),
    }


def thickened_crt_cell_exponents(
    u: Fraction,
    v: Fraction,
    gamma: Fraction,
    pi: Fraction,
    *,
    square_root_layers: bool,
) -> dict[str, Fraction | bool | str]:
    """Return the dyadic exponent ledger for one ``(G,P,u,v)`` cell.

    Parameters mean

    ``A=D^(1+u)``, ``B=D^(1+v)``, ``G=D^gamma``, ``P=D^pi``.

    The function uses only the proved scalar direction counts and the sharp
    shifted-CRT layer envelope.  In the Farey-valid range the direction
    exponent is ``max(0,(gamma+5*pi-33/16)/2)``.  Beyond Farey validity the
    energy inequalities force ``sqrt(QGP)<P^2``, so it uses the physical
    point count rather than the vacuous ``P^2`` alternative.

    If ``square_root_layers`` is true, the layer loss is ``sqrt(W)``.  This
    corresponds to the exact auxiliary residue-character L2 theorem, but its
    identification with completion-sum L2 is still conditional.  If false,
    the function uses the proved pointwise loss ``W``.
    """

    u, v, gamma, pi = map(Fraction, (u, v, gamma, pi))
    if min(u, v, gamma, pi) < 0 or u > v or 2 * u + 3 * v >= Fraction(1, 2):
        raise ValueError("require 0<=u<=v and 2u+3v<1/2")
    q_exp = Fraction(33, 16)
    h_exp = Fraction(17, 16)
    amplitude = Fraction(49, 48)
    target = Fraction(1, 2)
    hard_parameter = gamma + 5 * pi - q_exp
    farey_valid = pi <= Fraction(17, 16) + gamma - v
    if hard_parameter <= 0:
        return {
            "region": "farey_moderate",
            "closed": True,
            "hard_parameter": hard_parameter,
        }
    if farey_valid:
        direction = hard_parameter / 2
        region = "farey_hard"
    else:
        # Failure says pi>17/16+gamma-v.  Since v<1/6, this implies
        # 3*pi>33/16+gamma, so sqrt(QGP) is strictly smaller than P^2.
        assert 3 * pi > q_exp + gamma
        direction = (q_exp + gamma + pi) / 2
        region = "farey_failure"
    width = max(Fraction(), v + 3 * pi - gamma)
    layer = -4 * pi if 2 * pi <= h_exp else -2 * h_exp
    width_loss = width / 2 if square_root_layers else width
    final = amplitude + direction + layer + width_loss
    return {
        "region": region,
        "farey_valid": farey_valid,
        "low_crt": 2 * pi <= h_exp,
        "direction": direction,
        "width": width,
        "layer": layer,
        "width_loss": width_loss,
        "final": final,
        "target": target,
        "closed": final <= target,
        "margin": target - final,
    }


def symmetric_shifted_fejer_layers(
    order: int,
    p: int,
    d: int,
    alpha: Fraction | float = Fraction(),
    beta: Fraction | float = Fraction(),
) -> tuple[complex, ...]:
    """Return all shifted normal-congruence layer sums exactly up to floats.

    Layer ``ell`` contains the triangular Fejer coefficients with

    ``k*K-h*P == ell (mod R)``.

    Each layer is bounded in absolute value by the symmetric cyclic Fejer
    envelope.  The collection is useful for replaying the exact auxiliary
    residue-character Parseval theorem.
    """

    if order <= 0:
        raise ValueError("order must be positive")
    steps = primitive_symmetric_tangent_steps(p, d)
    coefficients = {
        h: Fraction(order - abs(h), order * order)
        for h in range(-order + 1, order)
    }
    layers = [0j for _ in range(steps.first_step)]
    for h, left in coefficients.items():
        for k, right in coefficients.items():
            residue = (
                k * steps.increasing_step - h * steps.decreasing_step
            ) % steps.first_step
            layers[residue] += (
                complex(left)
                * complex(right)
                * cmath.exp(
                    2j * cmath.pi * (h * float(alpha) + k * float(beta))
                )
            )
    return tuple(layers)


def symmetric_shifted_layer_envelope(order: int, p: int, d: int) -> Fraction:
    """Return the exact CRT envelope valid for every shifted residue layer."""

    steps = primitive_symmetric_tangent_steps(p, d)
    return symmetric_cyclic_fejer_bound(
        order, steps.tangent_numerator, steps.tangent_complement
    )


def residue_character_parseval(
    layers: Sequence[complex], selected: Sequence[int] | None = None
) -> tuple[float, float]:
    """Replay the exact auxiliary residue-character L2 identity.

    For ``F(x)=sum_(ell in I) O_ell e_R(x*ell)``, return

    ``((1/R)sum_x |F(x)|^2, sum_(ell in I)|O_ell|^2)``.

    These quantities are equal.  The variable ``x`` is an auxiliary
    character dual to the normal-congruence residue.  No claim is made that
    it is the physical completion-sum variable.
    """

    modulus = len(layers)
    if modulus == 0:
        raise ValueError("layers cannot be empty")
    indices = tuple(range(modulus)) if selected is None else tuple(selected)
    if any(index < 0 or index >= modulus for index in indices):
        raise IndexError("selected residue outside the cyclic group")
    values = [
        sum(
            layers[index]
            * cmath.exp(2j * cmath.pi * x * index / modulus)
            for index in indices
        )
        for x in range(modulus)
    ]
    character_l2 = sum(abs(value) ** 2 for value in values) / modulus
    layer_l2 = sum(abs(layers[index]) ** 2 for index in indices)
    return float(character_l2), float(layer_l2)


def flat_cyclic_residue_masses(
    modulus: int, left_step: int, right_step: int
) -> tuple[Fraction, ...]:
    """Return the residue masses of the flat cyclic character model.

    Put uniform mass ``1/R^2`` on ``(h,k) in (Z/RZ)^2`` and group it by

    ``k*K-h*P (mod R)``.  If ``gcd(R,P,K)=1``, the homomorphism is onto and
    every layer has mass exactly ``1/R``.

    Therefore a positive sum of ``W`` layers is ``W/R``, not
    ``sqrt(W)/R``.  This is the elementary obstruction to interpreting a
    square-root-in-``W`` estimate as a pointwise cyclic-character bound.
    Such a gain is valid only after an independent residue-dual ``L^2``
    average (or some comparably strong cancellation theorem).
    """

    if min(modulus, left_step, right_step) <= 0:
        raise ValueError("modulus and steps must be positive")
    if gcd(gcd(modulus, left_step), right_step) != 1:
        raise ValueError("the cyclic linear form must be primitive")
    return (Fraction(1, modulus),) * modulus


def local_farey_direction_majorant(
    Q: int,
    B: int,
    denominator_scale: int,
    content_floor: int,
    y_interval_length: int,
) -> int:
    """Majorize primitive directions represented in one ``y`` interval.

    Suppose remote points have

    ``P<=p<2P``, ``g>=G``, ``|e|,|f|<=B``

    and their ``y`` coordinates lie in an interval of length ``L``.  Since

    ``|d/p-y/Q|<=2B/(QGP)``,

    all represented fractions lie in an interval of length at most
    ``L/Q+4B/(QGP)``.  Distinct reduced fractions with denominators below
    ``2P`` are separated by more than ``1/(4P^2)``.  Hence their number is
    at most

    ``1+4P^2*L/Q+16B*P/(QG)``.

    The returned integer is the ceiling of this exact elementary bound.
    """

    if min(Q, B, denominator_scale, content_floor) <= 0 or y_interval_length < 0:
        raise ValueError("all scales must be positive and interval length nonnegative")
    P, G = denominator_scale, content_floor
    return 1 + ceil(Fraction(4 * P * P * y_interval_length, Q)) + ceil(
        Fraction(16 * B * P, Q * G)
    )


def dyadic_remote_farey_majorant(
    B: int, denominator_scale: int, content_floor: int
) -> int:
    """Majorize a global dyadic ``(p,g)`` remote sector.

    Work in a fixed compact collar and assume ``B/Q`` is sufficiently small
    (as it is in the application).  The exact cusp equations give

    ``gp = 2Q*y^2/(Q^2-y^2) + E``,

    with ``|E|=O_eta(B/Q)<1/2``.  Thus, for fixed ``y`` and ``p``, at most
    one content ``g`` is possible.  For a fixed reduced direction ``d/p``
    with ``P<=p<2P`` and ``g>=G``, the approximation equation confines
    ``y`` to an interval of length ``4B/(GP)``.  There are fewer than
    ``4P^2`` directions in a compact collar, so

    ``#points <= 4P^2+16BP/G``.

    Constants are deliberately generous.  This is a useful sector bound,
    but the unavoidable ``P^2`` term lies above the square-root budget at
    the surviving remote height.
    """

    if min(B, denominator_scale, content_floor) <= 0:
        raise ValueError("all scales must be positive")
    P, G = denominator_scale, content_floor
    return 4 * P * P + ceil(Fraction(16 * B * P, G))


def rho_continuous_approximation_error(
    point: ReducedSymmetricCuspData,
) -> Fraction:
    """Return ``gp-2Q*y^2/(Q^2-y^2)`` from the exact cusp equations."""

    if abs(point.y) >= point.Q:
        raise ValueError("the continuous cusp coordinate needs |y|<Q")
    denominator = point.Q * point.Q - point.y * point.y
    direct = Fraction(point.g * point.p) - Fraction(
        2 * point.Q * point.y * point.y, denominator
    )
    formula = Fraction(
        point.Q * point.sigma - point.g * point.y * point.n,
        denominator,
    )
    assert direct == formula
    return formula


def exact_tangent_singleton_criterion(
    p: int, d: int, left_half_width: int, right_half_width: int
) -> bool:
    """Test the exact geometric criterion for one lattice tangent point.

    At the symmetric centre ``C=Q^2,S=2Q``, the tangent point has first
    coordinate ``a0=Q*(1+d/p)``.  Along its exact tangent line,

    ``a*v-C=-(a-a0)^2/(1+d/p)^2`` and
    ``(S-a)*w-C=-(a-a0)^2/(1-d/p)^2``.

    The allowed first-coordinate interval therefore has radius

    ``min((1+d/p)*sqrt(A),(1-d/p)*sqrt(B))``.

    If its diameter is strictly smaller than the primitive step ``R``, it
    contains at most one point of any affine lattice coset on that line.
    The comparison below is squared and exact.
    """

    if left_half_width < 0 or right_half_width < 0:
        raise ValueError("product half-widths must be nonnegative")
    steps = primitive_symmetric_tangent_steps(p, d)
    radius_square_numerator = min(
        (p + d) ** 2 * left_half_width,
        (p - d) ** 2 * right_half_width,
    )
    return (
        steps.first_step**2 * p**2
        > 4 * radius_square_numerator
    )


def parallel_line_band_bound(
    product_half_width: int, p: int, d: int, *, left_band: bool = True
) -> int:
    """Bound one connected component on a line parallel to the tangent.

    Unlike :func:`exact_tangent_singleton_criterion`, this permits an
    arbitrary affine intercept.  It uses only the quadratic curvature
    ``R*P`` (or ``R*K``), and hence returns a constant rather than a
    singleton assertion in the high-height range.
    """

    steps = primitive_symmetric_tangent_steps(p, d)
    other_step = (
        steps.decreasing_step if left_band else steps.increasing_step
    )
    return tangent_component_point_bound(
        product_half_width,
        steps.first_step,
        other_step,
    )


def remote_tangent_parameter_mismatch(
    point: ReducedSymmetricCuspData,
) -> Fraction:
    """Return ``t_physical-t_(p,d)=n/(2*Q*p)`` exactly."""

    if point.p == 0:
        raise ValueError("the singular cusp has no primitive tangent")
    direct = Fraction(point.y, 2 * point.Q) - Fraction(point.d, 2 * point.p)
    formula = Fraction(point.n, 2 * point.Q * point.p)
    assert direct == formula
    return formula


def remote_reflection_c_family(
    p: int, d: int = 1, c: int = 1
) -> RemoteReflectionFixture:
    """Construct the integer-``c`` reflected remote family.

    For coprime ``p>d>=1``, put

    ``L0=p^2-d^2``, ``Q=p*L0+c``, ``y=d*L0``,
    ``r=d^2*(p-d)``, and ``s=d^2*(p+d)``.

    Then ``e=c*r``, ``f=c*s`` and the primitive invariants are

    ``g=2*d^2``, ``n=-c*d``, ``T=-2*c*d^2``, ``L=-8*c*d^6``.

    Reflection sends ``(y,r,s)`` to ``(-y,s,r)``.  Both first coordinates
    sum to ``2Q``.  Thus the two ordered singleton packet pairs have exactly
    the same completion output.  The branch ``c=0`` is major
    (``n=L=0``); every nonzero ``c`` is remote in these two labels.
    """

    return remote_reflection_hct_family(p, d, h=1, c=c, t=0)


def remote_reflection_hct_family(
    p: int, d: int, *, h: int, c: int, t: int
) -> RemoteReflectionFixture:
    """Construct the wider exact reflected ``(h,c,t)`` family.

    Put ``L0=p^2-d^2`` and

    ``Q=h*p*L0+c``, ``y=h*d*L0+t``,
    ``r=h*d^2*(p-d)``, ``s=h*d^2*(p+d)``.

    Then ``g=2*h*d^2``, ``n=p*t-c*d``, ``T=-2*c*d^2`` and
    ``L=-8*c*h^2*d^6``.  The explicit error formula is recorded in the
    companion report.  This family strictly contains the ``t=0,h=1``
    integer-``c`` branch.
    """

    if d <= 0 or p <= d or h <= 0 or gcd(p, d) != 1:
        raise ValueError("require h>=1 and coprime integers p>d>=1")
    scale = p * p - d * d
    Q = h * p * scale + c
    y = h * d * scale + t
    if Q <= abs(y):
        raise ValueError("the reflected physical coordinates require Q>|y|")
    r = h * d * d * (p - d)
    s = h * d * d * (p + d)
    positive = reduced_symmetric_cusp_data(Q, y, r, s)
    negative = reduced_symmetric_cusp_data(Q, -y, s, r)
    n = p * t - c * d
    expected = (
        2 * h * d * d,
        p,
        d,
        n,
        -8 * c * h * h * d**6,
        -2 * c * d * d,
    )
    assert (
        positive.g,
        positive.p,
        positive.d,
        positive.n,
        positive.L,
        positive.T,
    ) == expected
    assert (
        negative.g,
        negative.p,
        negative.d,
        negative.n,
        negative.L,
        negative.T,
    ) == (expected[0], p, -d, -n, expected[4], expected[5])
    common = -2 * h * d * scale * t - t * t
    expected_e = h * d * d * (p - d) * (c + t) + common
    expected_f = h * d * d * (p + d) * (c - t) + common
    assert positive.e == expected_e and positive.f == expected_f
    assert negative.e == expected_f and negative.f == expected_e
    return RemoteReflectionFixture(
        Q=Q,
        h=h,
        c=c,
        t=t,
        required_band=max(abs(expected_e), abs(expected_f)),
        positive=positive,
        negative=negative,
    )


def remote_reflection_family(p: int, d: int = 1) -> RemoteReflectionFixture:
    """Return the original ``c=1`` reflected remote family."""

    return remote_reflection_c_family(p, d, 1)


def reflected_c_factorization_solutions(
    Q: int, maximum_abs_c: int
) -> tuple[tuple[int, int, int], ...]:
    """Enumerate ``(c,p,d)`` with ``Q-c=p*(p-d)*(p+d)``.

    For fixed ``c``, the integer ``p`` divides ``Q-c`` and

    ``d^2=p^2-(Q-c)/p``.

    Hence there are at most twice the divisor count of ``Q-c`` solutions.
    Summing ``|c|<=Z`` gives ``O((1+Z)Q^epsilon)`` when ``Z=o(Q)``.  This
    exact enumeration is intended for finite replay, not for computing a
    divisor-function bound efficiently at large ``Q``.
    """

    if Q <= 0 or maximum_abs_c < 0:
        raise ValueError("require Q>0 and maximum_abs_c>=0")
    solutions: list[tuple[int, int, int]] = []
    for c in range(-maximum_abs_c, maximum_abs_c + 1):
        target = Q - c
        if target <= 0:
            continue
        for p in range(2, isqrt(target) + 2):
            if target % p:
                continue
            d_square = p * p - target // p
            if d_square <= 0:
                continue
            d = isqrt(d_square)
            if d < p and d * d == d_square and gcd(p, d) == 1:
                solutions.append((c, p, d))
    return tuple(sorted(set(solutions)))


def reflected_c_branch_exponents(
    u: Fraction, v: Fraction, pi: Fraction
) -> dict[str, Fraction]:
    """Return divisor-branch exponents for the generalized reflection family.

    The remote bound ``|y|>>Q^(2/3)`` and ``y=d*(p^2-d^2)`` imply
    ``d>>Q^(2/3)/P^2``.  Hence the number of admissible integer ``c`` values
    in a dyadic ``P=D^pi`` block is at most

    ``1+A*P^3/Q^(4/3)`` for a reflected pair (the narrow band is seen after
    reflection), and ``1+B*P^3/Q^(4/3)`` for one orientation only.

    The returned positive-part exponents are compared with
    ``sqrt(A)=D^((1+u)/2)``.
    """

    u, v, pi = map(Fraction, (u, v, pi))
    if min(u, v, pi) < 0 or u > v:
        raise ValueError("require 0<=u<=v and pi>=0")
    paired = max(Fraction(), u + 3 * pi - Fraction(7, 4))
    one_sided = max(Fraction(), v + 3 * pi - Fraction(7, 4))
    target = (1 + u) / 2
    return {
        "paired_c_count": paired,
        "one_sided_c_count": one_sided,
        "sqrt_A_target": target,
        "paired_margin": target - paired,
        "one_sided_margin": target - one_sided,
        "paired_closure_ceiling_pi": Fraction(3, 4) - u / 6,
        "one_sided_closure_ceiling_pi": Fraction(3, 4) + u / 6 - v / 3,
    }


def coarse_slope_resolution_exponents(u: Fraction) -> dict[str, Fraction]:
    """Compare frequency resolution with one physical tangent packet.

    For ``A=D^(1+u)``, a symmetric physical tangent packet has normalized
    slope width ``sqrt(A)/Q``.  Frequencies of size ``H`` resolve slope only
    to ``1/H``.  The ratio is ``D^(1/2-u/2)``.  A Farey denominator capable
    of resolving the physical width must reach

    ``sqrt(Q/sqrt(A))=D^(25/32-u/4)``,

    whereas the exact-frequency CRT stops at
    ``sqrt(H)=D^(17/32)``.
    """

    u = Fraction(u)
    if u < 0 or u >= 1:
        raise ValueError("require 0<=u<1")
    physical_width_inverse = Fraction(25, 16) - u / 2
    return {
        "frequency_angular_resolution_inverse": Fraction(17, 16),
        "physical_packet_angular_width_inverse": physical_width_inverse,
        "packets_per_frequency_chart": Fraction(1, 2) - u / 2,
        "frequency_denominator_ceiling": Fraction(17, 32),
        "physical_resolution_denominator": Fraction(25, 32) - u / 4,
        "denominator_gap": Fraction(1, 4) - u / 4,
    }


def remote_balanced_offset_reflection_family(
    p: int, tangent_offset: int
) -> RemoteReflectionFixture:
    """Construct a reflected high-height branch not controlled by small ``c``.

    Put ``d=1``, ``g=2``, ``ell=p^2-1``, ``u=tangent_offset`` and choose
    the balanced height ``c=2*p*u``.  Then

    ``Q=p*ell+c``, ``y=ell+u``,
    ``e=-u*(p+u-1)``, and ``f=u*(p+1-u)``.

    The narrow-band cost is ``O(p*|u|+u^2)``, whereas the small-``c``
    quantity is ``|c|*p=2*p^2*|u|``.  Thus this exact reflected family
    falsifies classification by the ``u=0``/small-``c`` branch alone.
    """

    u = tangent_offset
    if p < 3 or u == 0 or abs(u) >= p:
        raise ValueError("require p>=3 and 0<|tangent_offset|<p")
    c = 2 * p * u
    fixture = remote_reflection_hct_family(p, 1, h=1, c=c, t=u)
    positive, negative = fixture.positive, fixture.negative
    assert (positive.g, positive.p, positive.d) == (2, p, 1)
    assert (positive.n, positive.T, positive.L) == (-p * u, -4 * p * u, -16 * p * u)
    assert positive.e == -u * (p + u - 1)
    assert positive.f == u * (p + 1 - u)
    assert negative.e == positive.f and negative.f == positive.e
    return fixture


def reflected_cusp_normal_form(
    point: ReducedSymmetricCuspData,
) -> dict[str, int | Fraction]:
    """Return the exact reflected ``(c,u,g-2d^2)`` normal coordinates.

    For ``ell=p^2-d^2``, set ``c=Q-p*ell`` and ``u=y-d*ell``.  On the
    central content branch ``g=2d^2``, the coherent transverse height is
    ``h=d*c-2*p*u``; small errors do not force ``c`` or ``u`` separately
    to be small.
    """

    if point.p <= 0 or abs(point.d) >= point.p:
        raise ValueError("require a nonsingular compact primitive point")
    p, d, g = point.p, point.d, point.g
    ell = p * p - d * d
    c = point.Q - p * ell
    u = point.y - d * ell
    half_g = Fraction(g, 2)
    e_formula = (
        (half_g - d * d) * ell * ell
        + half_g * (p - d) * (c + u)
        - 2 * d * ell * u
        - u * u
    )
    f_formula = (
        (half_g - d * d) * ell * ell
        + half_g * (p + d) * (c - u)
        - 2 * d * ell * u
        - u * u
    )
    n_formula = p * u - c * d
    T_formula = p * ell * (g - 2 * d * d) - 2 * c * d * d
    balanced_height = d * c - 2 * p * u
    left_residual = balanced_height - d * u
    right_residual = balanced_height + d * u
    quadratic_residual = left_residual * right_residual
    assert e_formula == point.e
    assert f_formula == point.f
    assert n_formula == point.n
    assert T_formula == point.T
    return {
        "ell": ell,
        "c": c,
        "u": u,
        "content_defect": g - 2 * d * d,
        "balanced_height": balanced_height,
        "left_residual": left_residual,
        "right_residual": right_residual,
        "quadratic_residual": quadratic_residual,
        "e_formula": e_formula,
        "f_formula": f_formula,
        "n_formula": n_formula,
        "T_formula": T_formula,
    }


def central_content_transverse_identity(
    point: ReducedSymmetricCuspData,
) -> dict[str, int | Fraction]:
    """Return the exact identity that excludes a large normal offset.

    On the central-content chart ``g=2*d^2``, with
    ``u=y-d*(p^2-d^2)``, ``n=p*y-Q*d``, and ``sigma=e+f``, one has

    ``u*y=-d*p*n-sigma/2``.

    This identity is particularly useful after the remote cut
    ``|y| >> Q^(2/3)``: product bands of width at most ``B`` then force
    ``|u| << B/Q^(1/3)=o(sqrt(B))`` in the Fejer energy core.
    """

    normal = reflected_cusp_normal_form(point)
    if normal["content_defect"] != 0:
        raise ValueError("identity requires the central content g=2*d^2")
    u = int(normal["u"])
    sigma = point.e + point.f
    left = Fraction(u * point.y)
    right = -point.d * point.p * point.n - Fraction(sigma, 2)
    assert left == right
    return {
        "u": u,
        "sigma": sigma,
        "left": left,
        "right": right,
    }


def central_content_remote_closure_exponents() -> dict[str, Fraction]:
    """Return the sharp power ledger for the central-content remote count.

    The energy core has ``Q=D^(33/16)``, ``B<D^(7/6)``, and ``A>=D``.
    The low-offset count is ``B/Q^(1/3)=D^(23/48)``, saving ``D^(1/48)``
    over the smallest possible ``sqrt(A)`` budget.  The putative high-offset
    sector is empty because its upper bound relative to ``sqrt(B)`` is
    ``sqrt(B)/Q^(1/3)<=D^(-5/48)``.
    """

    q = Fraction(33, 16)
    b = Fraction(7, 6)
    p = q / 3
    count = b - p
    square_root_budget = Fraction(1, 2)
    high_offset_ratio = b / 2 - p
    assert count == Fraction(23, 48)
    assert square_root_budget - count == Fraction(1, 48)
    assert high_offset_ratio == Fraction(-5, 48)
    return {
        "Q": q,
        "B": b,
        "P": p,
        "count": count,
        "sqrt_A_floor": square_root_budget,
        "saving": square_root_budget - count,
        "high_offset_ratio": high_offset_ratio,
    }


def scaled_cusp_normal_form(
    point: ReducedSymmetricCuspData,
) -> dict[str, int | Fraction]:
    """Recenter an arbitrary content ``g`` at its exact scaled cusp.

    Put ``ell=p^2-d^2`` and ``lambda=g/(2*d^2)``.  The exact cusp at this
    content is

    ``Q0=lambda*p*ell,  y0=lambda*d*ell``.

    Clearing denominators in the deviations from that cusp gives

    ``T=g*p*ell-2*Q*d^2``,
    ``v=2*d*y-g*ell``, and ``z=T+2*p*v``.

    They obey the integral normal form

    ``2*d*n=T+p*v``,
    ``4*d^2*e+v^2=-g*(p-d)*(z+d*v)``,
    ``4*d^2*f+v^2=-g*(p+d)*(z-d*v)``.

    This removes the apparently dominant ``(g-2*d^2)*ell^2/2`` term:
    noncentral content is a change of cusp scale, not by itself a lower
    bound for the product errors.
    """

    if point.d == 0 or point.p <= abs(point.d):
        raise ValueError("require a nonsingular compact primitive point")
    p, d, g = point.p, point.d, point.g
    ell = p * p - d * d
    content_defect = g - 2 * d * d
    scale = Fraction(g, 2 * d * d)
    shifted_c = Fraction(point.Q) - scale * p * ell
    shifted_u = Fraction(point.y) - scale * d * ell
    T = g * p * ell - 2 * point.Q * d * d
    v = 2 * d * point.y - g * ell
    z = T + 2 * p * v
    left_error = 4 * d * d * point.e + v * v
    right_error = 4 * d * d * point.f + v * v
    left_formula = -g * (p - d) * (z + d * v)
    right_formula = -g * (p + d) * (z - d * v)
    n_formula = T + p * v
    residual = (z + d * v) * (z - d * v)
    product_formula = g * g * ell * residual
    assert shifted_c == Fraction(-T, 2 * d * d)
    assert shifted_u == Fraction(v, 2 * d)
    assert 2 * d * point.n == n_formula
    assert left_error == left_formula
    assert right_error == right_formula
    assert left_error * right_error == product_formula
    return {
        "ell": ell,
        "content_defect": content_defect,
        "scale": scale,
        "shifted_c": shifted_c,
        "shifted_u": shifted_u,
        "T": T,
        "v": v,
        "z": z,
        "left_residual": z + d * v,
        "right_residual": z - d * v,
        "quadratic_residual": residual,
        "left_error": left_error,
        "right_error": right_error,
        "product_formula": product_formula,
    }


def scaled_cusp_remote_exponents() -> dict[str, Fraction]:
    """Power margins for the arbitrary-content scaled-cusp offset.

    In the remote collar ``g*p >> Q^(1/3)``.  The scaled normal form forces
    ``|v|/|d| << B/(g*p)``.  The energy core places this below
    ``sqrt(A)`` by ``D^(1/48)`` and below ``sqrt(B)`` by ``D^(5/48)``.
    """

    rho_floor = Fraction(11, 16)
    b = Fraction(7, 6)
    sqrt_a_floor = Fraction(1, 2)
    sqrt_b_ceiling = b / 2
    offset = b - rho_floor
    assert offset == Fraction(23, 48)
    return {
        "rho_floor": rho_floor,
        "offset": offset,
        "sqrt_A_floor": sqrt_a_floor,
        "sqrt_B_ceiling": sqrt_b_ceiling,
        "sqrt_A_margin": sqrt_a_floor - offset,
        "sqrt_B_margin": sqrt_b_ceiling - offset,
    }


def scaled_balanced_axis_factor_data(
    point: ReducedSymmetricCuspData,
) -> dict[str, int]:
    """Return the fixed-``Q`` divisor identities on the scaled axis ``z=0``.

    The routine uses the positive-``d`` orientation.  On ``z=0``, one has
    ``p|2Q``, ``v=d*w``, ``g=d*a``, and, for ``M=2Q/p``,

    ``a*(p^2-d^2)+2*w=M*d``.

    Fixed ``w`` gives

    ``p-d | 2*(Q-w)`` and ``p+d | 2*(Q+w)``.

    For the asymmetric bad sign ``w=-t<0``, put
    ``eta=t-g*(p-d)``.  The exact second factorization is

    ``(p-d)*(a*(p-d)+M)=2*(Q+eta)``.

    These identities yield the ``O(sqrt(A)*Q^o(1))`` count after splitting
    ``t<=sqrt(A)`` and ``t>sqrt(A)``; in the latter range the narrow error
    gives ``|eta|<=4*A/t``.
    """

    if point.d <= 0:
        raise ValueError("use the positive-d orientation")
    normal = scaled_cusp_normal_form(point)
    if normal["z"] != 0:
        raise ValueError("point is not on the scaled balanced axis z=0")
    p, d, g, Q = point.p, point.d, point.g, point.Q
    v = int(normal["v"])
    if v % d or g % d or (2 * Q) % p:
        raise AssertionError("z=0 divisibility consequences failed")
    w = v // d
    a = g // d
    M = 2 * Q // p
    assert a * (p * p - d * d) + 2 * w == M * d
    left_target = 2 * (Q - w)
    right_target = 2 * (Q + w)
    assert left_target % (p - d) == 0
    assert right_target % (p + d) == 0
    data = {
        "M": M,
        "a": a,
        "w": w,
        "left_target": left_target,
        "right_target": right_target,
    }
    if w < 0:
        t = -w
        eta = t - g * (p - d)
        x = p - d
        assert a * x * x == M * d + 2 * eta
        bad_target = 2 * (Q + eta)
        assert x * (a * x + M) == bad_target
        data.update({"t": t, "eta": eta, "bad_target": bad_target})
    return data


def scaled_nonzero_residual_exponents() -> dict[str, Fraction]:
    """Return the forced primitive-height exponent after all scaled axes.

    For ``K=(z+d*v)*(z-d*v)!=0``, integrality of the narrow residual and
    the scaled-cusp box force ``g*p << d^2*A``.  In the compact remote
    collar ``g*p/d^2`` is comparable with ``Q/p^2``; hence

    ``p >> sqrt(Q/A)``.

    At the largest energy-core value ``A<D^(11/10)`` this is
    ``p>>D^(77/160)``.
    """

    q = Fraction(33, 16)
    a_ceiling = Fraction(11, 10)
    p_floor = (q - a_ceiling) / 2
    assert p_floor == Fraction(77, 160)
    return {
        "Q": q,
        "A_ceiling": a_ceiling,
        "primitive_floor": p_floor,
        "central_remote_floor": Fraction(43, 144),
        "gain_over_remote_floor": p_floor - Fraction(43, 144),
    }


def _ceil_cuberoot(value: int) -> int:
    """Return the least integer whose cube is at least ``value``."""

    if value <= 0:
        raise ValueError("value must be positive")
    low, high = 0, 1
    while high**3 < value:
        high *= 2
    while high - low > 1:
        middle = (low + high) // 2
        if middle**3 >= value:
            high = middle
        else:
            low = middle
    return high


def reflected_c_family_fixed_q_majorant(Q: int, band: int) -> int:
    """Bound the nonzero-``c`` branch at fixed ``Q`` by cubic gaps.

    Count both signs of ``d`` and require the reflected pair to fit a band
    of half-width ``band``.  Then

    ``|c|*d^2*(p+|d|)<=band`` and ``Q=p*(p^2-d^2)+c``.

    Hence ``p>=ceil((Q-band)^(1/3))`` and ``d^2*p<=band``.  For fixed
    ``|d|``, consecutive cubic values differ by more than ``2p^2``; once
    the floor squared is at least the band, at most one ``p`` occurs for
    each signed ``d``.
    """

    if Q <= 0 or band <= 0 or 2 * band >= Q:
        raise ValueError("require Q,band>0 and 2*band<Q")
    p_floor = _ceil_cuberoot(Q - band)
    if p_floor * p_floor < band:
        raise ValueError("cubic gaps are not yet larger than the band")
    d_cap = isqrt(band // p_floor)
    return 2 * d_cap


def _divisor_count(value: int) -> int:
    """Return the exact number of positive divisors of ``value``."""

    if value <= 0:
        raise ValueError("value must be positive")
    total = 0
    root = isqrt(value)
    for divisor in range(1, root + 1):
        if value % divisor == 0:
            total += 1 if divisor * divisor == value else 2
    return total


def reflected_h_zero_fixed_q_majorant(Q: int, band: int) -> int:
    """Bound the central-content balanced branch ``h=d*c-2*p*u=0``.

    On ``g=2d^2`` the errors are ``e=-r*u-u^2`` and ``f=s*u-u^2``.
    Their difference gives ``p*d^2*|u|<=band``.  For a remote point
    ``u!=0``, hence ``d^2*p<=band``.  Also ``h=0`` and ``gcd(p,d)=1``
    imply ``p|c`` and therefore ``p|Q``.  Finally ``|c|<=2*band`` gives
    ``p>=ceil((Q-2*band)^(1/3))``.  Counting divisors ``p|Q`` and both
    reflected signs of ``d`` yields the returned majorant.
    """

    if Q <= 0 or band <= 0 or 4 * band >= Q:
        raise ValueError("require Q,band>0 and 4*band<Q")
    p_floor = _ceil_cuberoot(Q - 2 * band)
    d_cap = isqrt(band // p_floor)
    return 2 * _divisor_count(Q) * d_cap


def reflected_k_zero_divisor_identity(
    Q: int, p: int, d: int, u: int, branch: int
) -> dict[str, int]:
    """Replay the fixed-``d`` divisor identity on ``h=+-d*u``.

    Here ``branch`` is ``+1`` for ``h=d*u`` and ``-1`` for
    ``h=-d*u``.  With ``c=Q-p*(p^2-d^2)``, the branch equation is

    ``d*c=(2*p+branch*d)*u``.

    It forces ``mu=2*u/d`` to be integral.  For
    ``x=2*p+branch*d`` one then has the exact factorization

    ``8*Q-3*branch*d^3
      =x*(x^2-3*branch*d*x-d^2+4*mu)``.

    Thus, whenever the left side is nonzero, a fixed signed ``d`` has
    at most divisor-many points on either one-band cancellation branch.
    """

    if Q <= 0 or p <= abs(d) or d == 0 or branch not in (-1, 1):
        raise ValueError("require Q>0, p>|d|>0, and branch=+-1")
    c = Q - p * (p * p - d * d)
    x = 2 * p + branch * d
    if d * c != x * u:
        raise ValueError("point is not on the requested k=0 branch")
    mu_fraction = Fraction(2 * u, d)
    if mu_fraction.denominator != 1:
        raise AssertionError("the k=0 divisibility equation must make 2*u/d integral")
    mu = mu_fraction.numerator
    target = 8 * Q - 3 * branch * d**3
    cofactor = x * x - 3 * branch * d * x - d * d + 4 * mu
    assert target == x * cofactor
    return {
        "branch": branch,
        "c": c,
        "mu": mu,
        "x": x,
        "target": target,
        "cofactor": cofactor,
    }


def reflected_k_zero_fixed_q_majorant(Q: int, narrow_band: int) -> int:
    """Divisor majorant for central reflected pairs with ``k=0``.

    In the central-content normal form, put

    ``H0=d*c-2*p*u`` and ``k=(H0-d*u)*(H0+d*u)``.

    If both a point and its reflection obey product bands whose narrower
    half-width is ``narrow_band``, then ``k=0`` forces ``u**2`` into that
    narrow band.  For ``H0=epsilon*d*u`` one has

    ``p | Q-epsilon*u``.

    Once ``epsilon,u,p`` are fixed, ``d`` satisfies a cubic and therefore
    has at most three integer values.  Summing this exact finite divisor
    majorant proves ``O(sqrt(narrow_band)*Q^o(1))`` in the asymptotic range.
    """

    if Q <= 1 or narrow_band <= 0 or isqrt(narrow_band) >= Q:
        raise ValueError("require Q>1 and 0<sqrt(narrow_band)<Q")
    u_cap = isqrt(narrow_band)
    return 3 * sum(
        _divisor_count(Q - epsilon * u)
        for epsilon in (-1, 1)
        for u in range(-u_cap, u_cap + 1)
        if u != 0
    )


def remote_points_in_symmetric_window(
    Q: int, half_width: int, y_limit: int
) -> tuple[ReducedSymmetricCuspData, ...]:
    """Enumerate the remote ``n*L*kappa!=0`` points in a finite fixture."""

    if min(Q, half_width) <= 0 or not 0 <= y_limit < Q // 2:
        raise ValueError("require Q,width>0 and 0<=y_limit<Q/2")

    def candidates(numerator: int, denominator: int) -> tuple[int, ...]:
        lower = numerator // denominator
        return tuple(
            value
            for value in (lower, lower + 1)
            if abs(value * denominator - numerator) <= half_width
        )

    points: list[ReducedSymmetricCuspData] = []
    for y in range(-y_limit, y_limit + 1):
        for r in candidates(y * y, Q + y):
            for s in candidates(y * y, Q - y):
                point = reduced_symmetric_cusp_data(Q, y, r, s)
                if point.n != 0 and point.L != 0 and point.kappa != 0:
                    points.append(point)
    return tuple(points)


def additive_representations(values: Sequence[int]) -> dict[int, int]:
    """Return ordered additive convolution multiplicities."""

    counts = Counter(left + right for left in values for right in values)
    return dict(sorted(counts.items()))


def weighted_completion_energy(
    left_locations: Sequence[int],
    left_weights: Sequence[complex],
    right_locations: Sequence[int],
    right_weights: Sequence[complex],
    *,
    absolute_weights: bool = False,
) -> float:
    """Return the exact mixed completion energy ``||z*y||_2^2``."""

    if len(left_locations) != len(left_weights) or len(right_locations) != len(
        right_weights
    ):
        raise ValueError("locations and weights must have matching lengths")
    convolution: defaultdict[int, complex] = defaultdict(complex)
    for a, z in zip(left_locations, left_weights):
        for b, y in zip(right_locations, right_weights):
            if absolute_weights:
                convolution[a + b] += abs(z) * abs(y)
            else:
                convolution[a + b] += z * y
    return float(sum(abs(value) ** 2 for value in convolution.values()))


def masked_factorable_completion_form(
    left_locations: Sequence[int],
    left_weights: Sequence[complex],
    right_locations: Sequence[int],
    right_weights: Sequence[complex],
    mask: Mapping[tuple[int, int, int, int], complex],
) -> complex:
    """Evaluate a factorable pair mask supported on completion equality.

    A key ``(i,j,k,l)`` denotes the matrix coefficient between ordered
    pairs ``(i,j)`` and ``(k,l)``.  Every nonzero coefficient must have
    modulus at most one and satisfy

    ``a_i+b_j=a_k+b_l``.

    Entrywise absolute values then prove

    ``|form| <= || |z|*|y| ||_2^2``.

    The routine verifies the hypotheses and returns the left-hand side.
    """

    if len(left_locations) != len(left_weights) or len(right_locations) != len(
        right_weights
    ):
        raise ValueError("locations and weights must have matching lengths")
    total = 0j
    for (i, j, k, ell), coefficient in mask.items():
        if not (
            0 <= i < len(left_locations)
            and 0 <= k < len(left_locations)
            and 0 <= j < len(right_locations)
            and 0 <= ell < len(right_locations)
        ):
            raise IndexError("mask index outside the pair space")
        if abs(coefficient) > 1 + 1.0e-12:
            raise ValueError("mask coefficients must have modulus at most one")
        if coefficient and (
            left_locations[i] + right_locations[j]
            != left_locations[k] + right_locations[ell]
        ):
            raise ValueError("mask must be supported on completion equality")
        first = left_weights[i] * right_weights[j]
        second = left_weights[k] * right_weights[ell]
        total += first.conjugate() * coefficient * second
    return total
