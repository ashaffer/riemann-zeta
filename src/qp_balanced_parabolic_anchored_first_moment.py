"""Exact ledgers for the one-sided parabolic gap-token first moment.

The analytic argument is recorded in the accompanying result note.  Its
key point is that the two valid matching estimates for one color chart
must be minimized, rather than geometrically averaged.  On the formerly
surviving ``(e,t,g,r,s)=(1,0,0,3/16,3/16)`` face this removes much more
than the normalized-GCD line loss.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd


@dataclass(frozen=True)
class AnchoredFirstMomentLedger:
    """Exponent ledger for one determinant-content/direction block."""

    top_bottom_mass: Fraction
    left_right_mass: Fraction
    relation_mass: Fraction
    occupied_line_singleton: Fraction
    occupied_line_curvature: Fraction
    weighted_singleton: Fraction
    weighted_curvature: Fraction


def anchored_first_moment_ledger(
    *,
    row_height: Fraction,
    column_height: Fraction,
    eta_height: Fraction,
    theta_height: Fraction,
    gcd_height: Fraction,
    slice_multiplicity: Fraction,
) -> AnchoredFirstMomentLedger:
    """Return the one-sided relation-mass and occupied-line exponents.

    The inputs encode ``R=D^r``, ``S=D^s``, ``E=D^e``, ``T=D^t``,
    ``G=D^g``, and ``K=D^kappa``.  The two direct matching sums are

    ``R*T/G`` and ``S*E/G``.

    The occupied-line theorem contributes ``K`` for singleton points and
    ``sqrt(D*K/(R*S))`` for the curvature part.
    """

    r = Fraction(row_height)
    s = Fraction(column_height)
    e = Fraction(eta_height)
    t = Fraction(theta_height)
    g = Fraction(gcd_height)
    kappa = Fraction(slice_multiplicity)
    if min(r, s, e, t, g, kappa) < 0:
        raise ValueError("all exponents must be nonnegative")
    if e + t > 1 or r + s > 1:
        raise ValueError("the determinant or direction height exceeds D")
    if g > min(e, t):
        raise ValueError("the gcd height exceeds a determinant factor")

    top_bottom = r + t - g
    left_right = s + e - g
    relation = min(top_bottom, left_right)
    singleton = kappa
    curvature = (1 + kappa - r - s) / 2
    return AnchoredFirstMomentLedger(
        top_bottom_mass=top_bottom,
        left_right_mass=left_right,
        relation_mass=relation,
        occupied_line_singleton=singleton,
        occupied_line_curvature=curvature,
        weighted_singleton=relation + singleton,
        weighted_curvature=relation + curvature,
    )


def former_balanced_face_ledger() -> AnchoredFirstMomentLedger:
    """Return the exact ledger on the former ``37/32`` endpoint."""

    return anchored_first_moment_ledger(
        row_height=Fraction(3, 16),
        column_height=Fraction(3, 16),
        eta_height=Fraction(1),
        theta_height=Fraction(0),
        gcd_height=Fraction(0),
        slice_multiplicity=Fraction(5, 16),
    )


@dataclass(frozen=True)
class SymmetricCurvatureClosureLedger:
    """Flat-bin closure ledger for the symmetric equality face."""

    relation_mass: Fraction
    old_curvature_multiplier: Fraction
    repeated_line_multiplier: Fraction
    chart_count: Fraction
    chart_support_threshold: Fraction
    principal_support_threshold: Fraction
    support_overlap: Fraction
    nonprincipal_mass: Fraction
    nonprincipal_curvature: Fraction


def symmetric_curvature_closure_ledger() -> SymmetricCurvatureClosureLedger:
    """Return the exact powers closing ``e=t=1/2, r=s=7/16``.

    A line contributing beyond its first point has multiplier
    ``n << D/H``.  This replaces the old ``sqrt(D*K/H)`` curvature
    multiplier by ``D/H`` on this face.  The chart and determinant-principal
    support ranges then overlap by ``D^(1/16)``.
    """

    relation = Fraction(15, 16)
    old_curvature = Fraction(7, 32)
    repeated_line = Fraction(1, 8)
    chart_count = Fraction(11, 4)
    chart_threshold = chart_count + repeated_line - 1
    principal_threshold = Fraction(33, 16) - repeated_line
    overlap = principal_threshold - chart_threshold
    nonprincipal = Fraction(97, 128)
    return SymmetricCurvatureClosureLedger(
        relation_mass=relation,
        old_curvature_multiplier=old_curvature,
        repeated_line_multiplier=repeated_line,
        chart_count=chart_count,
        chart_support_threshold=chart_threshold,
        principal_support_threshold=principal_threshold,
        support_overlap=overlap,
        nonprincipal_mass=nonprincipal,
        nonprincipal_curvature=nonprincipal + repeated_line,
    )


@dataclass(frozen=True)
class FinalAffinePrimeGateLedger:
    """Exponent ledger at the final floor/cutoff equality face."""

    eta_height: Fraction
    theta_height: Fraction
    row_height: Fraction
    column_height: Fraction
    direction_height: Fraction
    slice_multiplicity: Fraction
    relation_mass: Fraction
    line_multiplier_floor: Fraction
    inverse_sqrt_line_sum: Fraction
    longitudinal_prefactor: Fraction
    pointwise_curvature: Fraction
    weighted_curvature: Fraction
    line_parameter_length: Fraction


def final_affine_prime_gate_ledger() -> FinalAffinePrimeGateLedger:
    """Return the exact powers of the final positive affine-star gate."""

    e = Fraction(21, 32)
    t = Fraction(11, 32)
    r = Fraction(23, 64)
    s = Fraction(3, 64)
    h = r + s
    kappa = Fraction(5, 16)
    relation = min(r + t, s + e)
    multiplier_floor = abs(r - s)
    inverse_sqrt_sum = min(
        kappa / 2,
        kappa - multiplier_floor / 2,
    )
    longitudinal = (1 - h) / 2
    pointwise = longitudinal + inverse_sqrt_sum
    weighted = relation + pointwise
    parameter_length = (1 - multiplier_floor - h) / 2
    return FinalAffinePrimeGateLedger(
        eta_height=e,
        theta_height=t,
        row_height=r,
        column_height=s,
        direction_height=h,
        slice_multiplicity=kappa,
        relation_mass=relation,
        line_multiplier_floor=multiplier_floor,
        inverse_sqrt_line_sum=inverse_sqrt_sum,
        longitudinal_prefactor=longitudinal,
        pointwise_curvature=pointwise,
        weighted_curvature=weighted,
        line_parameter_length=parameter_length,
    )


@dataclass(frozen=True)
class RegularCommonXModel:
    """Finite translation model saturating all four matching estimates."""

    group_order: int
    lift_degree: int
    chart_count: int
    token_energy: Fraction
    chart_weight: Fraction
    total_chart_mass: Fraction
    p_degrees: tuple[int, ...]
    q_degrees: tuple[int, ...]
    r_degrees: tuple[int, ...]
    s_degrees: tuple[int, ...]

    @property
    def is_regular(self) -> bool:
        target = (self.lift_degree,) * self.group_order
        return (
            self.p_degrees == target
            and self.q_degrees == target
            and self.r_degrees == target
            and self.s_degrees == target
        )


def regular_common_x_model(
    *, group_order: int, lift_degree: int
) -> RegularCommonXModel:
    """Build an exact cyclic common-``X`` principal-mode saturator.

    For ``p in Z/NZ`` and ``a`` in a set of size ``L``, put

    ``r=p+2a+1``, ``q=p+a``, ``s=r+a``.

    The corresponding color chart is

    ``(x,y,z,w)=(X, X+p, X+r, X+p+r+a)``.

    Its four pair differences are exactly ``p,q,r,s``.  Every token family
    is ``L``-regular.  With the flat vector ``z=N^-1/2``, every matching has
    energy ``1/N`` and every chart has weight ``1/N``.
    """

    if group_order < 2:
        raise ValueError("group_order must be at least two")
    if not 1 <= lift_degree <= group_order:
        raise ValueError("lift_degree must lie between one and group_order")
    p_deg = [0] * group_order
    q_deg = [0] * group_order
    r_deg = [0] * group_order
    s_deg = [0] * group_order
    for p in range(group_order):
        for a in range(lift_degree):
            r = (p + 2 * a + 1) % group_order
            q = (p + a) % group_order
            s = (r + a) % group_order
            p_deg[p] += 1
            q_deg[q] += 1
            r_deg[r] += 1
            s_deg[s] += 1
            # Replay the four exact common-X differences at every X.
            for x in range(group_order):
                y = (x + p) % group_order
                zeta = (x + r) % group_order
                w = (x + p + r + a) % group_order
                if (y - x) % group_order != p:
                    raise AssertionError("top token mismatch")
                if (w - zeta) % group_order != q:
                    raise AssertionError("bottom token mismatch")
                if (zeta - x) % group_order != r:
                    raise AssertionError("left token mismatch")
                if (w - y) % group_order != s:
                    raise AssertionError("right token mismatch")
    model = RegularCommonXModel(
        group_order=group_order,
        lift_degree=lift_degree,
        chart_count=group_order * lift_degree,
        token_energy=Fraction(1, group_order),
        chart_weight=Fraction(1, group_order),
        total_chart_mass=Fraction(lift_degree),
        p_degrees=tuple(p_deg),
        q_degrees=tuple(q_deg),
        r_degrees=tuple(r_deg),
        s_degrees=tuple(s_deg),
    )
    if not model.is_regular:
        raise AssertionError("the common-X chart design is not regular")
    return model


@dataclass(frozen=True)
class AffineLineStarLedger:
    """Exact ``A=1`` and variable-``B`` line-star identities."""

    alpha: int
    beta: int
    transverse_gcd: int
    row_multiplier: int
    column_multiplier: int
    common_level: int
    reduced_level: int


def affine_line_star_ledger(
    *,
    eta: int,
    theta: int,
    column_scale: int,
    column_multiplier: int,
    gamma: int,
    u: int,
    v: int,
) -> AffineLineStarLedger:
    """Replay ``alpha=theta*c``, ``beta=eta*c*B`` exactly."""

    if min(
        abs(eta),
        abs(theta),
        abs(column_scale),
        abs(column_multiplier),
    ) < 1:
        raise ValueError("all transverse inputs must be nonzero")
    if gcd(abs(eta), abs(theta)) != 1:
        raise ValueError("the displayed final face has coprime eta, theta")
    alpha = theta * column_scale
    beta = eta * column_scale * column_multiplier
    transverse_gcd = gcd(abs(eta * alpha), abs(theta * beta))
    expected_gcd = abs(eta * theta * column_scale)
    if transverse_gcd != expected_gcd:
        raise AssertionError("the line star did not have A=1")
    row_multiplier = eta * alpha // (eta * theta * column_scale)
    recovered_column_multiplier = theta * beta // (
        eta * theta * column_scale
    )
    common_level = (
        theta * u * beta
        + eta * alpha * v
        + gamma * alpha * beta
    )
    signed_scale = eta * theta * column_scale
    if common_level % signed_scale:
        raise AssertionError("the star level did not divide by g0")
    reduced_level = common_level // signed_scale
    expected_level = (
        column_multiplier * u
        + v
        + gamma * column_scale * column_multiplier
    )
    if reduced_level != expected_level:
        raise AssertionError("the reduced affine-star equation failed")
    return AffineLineStarLedger(
        alpha=alpha,
        beta=beta,
        transverse_gcd=transverse_gcd,
        row_multiplier=row_multiplier,
        column_multiplier=recovered_column_multiplier,
        common_level=common_level,
        reduced_level=reduced_level,
    )


@dataclass(frozen=True)
class RelaxedConstantBoxLedger:
    """Finite replay of the spurious four-energy principal mode.

    This is deliberately a ledger for the *relaxed* geometric-mean form.
    It records why that form appears to lose a factor, and why no actual
    common color-chart mass can attain it when the two matching bounds are
    imbalanced.
    """

    eta_count: int
    row_count: int
    column_count: int
    line_count: int
    top_energy_denominator: int
    cross_energy_denominator: int
    smaller_matching_bound_squared: Fraction
    geometric_mean_bound_squared: Fraction
    artificial_loss_squared: Fraction


def relaxed_constant_box_ledger(
    *, eta_count: int, row_count: int, column_count: int, line_count: int
) -> RelaxedConstantBoxLedger:
    """Return an exact constant-array comparison.

    Per line-``B`` slice take ``P=Q=1/(E*R*S^2)`` and per line-``A``
    slice take ``Renergy=Senergy=1/(R^2*S)``.  When ``R=S``, the relaxed
    geometric mean exceeds the smaller actual matching bound by
    ``sqrt(E)``.  Squared quantities keep the replay rational.
    """

    if min(eta_count, row_count, column_count, line_count) < 1:
        raise ValueError("all finite box sizes must be positive")
    top_denominator = eta_count * row_count * column_count**2
    cross_denominator = row_count**2 * column_count
    top = Fraction(1, top_denominator)
    cross = Fraction(1, cross_denominator)
    smaller_squared = min(top, cross) ** 2
    geometric_squared = top * cross
    return RelaxedConstantBoxLedger(
        eta_count=eta_count,
        row_count=row_count,
        column_count=column_count,
        line_count=line_count,
        top_energy_denominator=top_denominator,
        cross_energy_denominator=cross_denominator,
        smaller_matching_bound_squared=smaller_squared,
        geometric_mean_bound_squared=geometric_squared,
        artificial_loss_squared=geometric_squared / smaller_squared,
    )
