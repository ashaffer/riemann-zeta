"""Exact ledgers for the pre-factorial affine-compression transfer theorem.

The positive four-cycle form is a first moment in the number of physical
completions.  Affine/Hankel completions may therefore be charged directly,
provided they are peeled *before* ordered completion pairs are formed.  The
remaining completions can then be factorialized and sent through A2/A4.

This module checks the finite algebra behind that transfer.  It does not
construct affine packets and does not prove their asymptotic Carleson bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Hashable, Mapping, Sequence


Color = Hashable


@dataclass(frozen=True)
class AffinePatchProfile:
    """Color-incidence data for one pair-unique affine/Hankel patch.

    ``color_degrees`` stores ``l_(t,c)``, the number of occupied matrix
    entries carrying color ``c``.  The local patch trace lemma has coefficient

        L_t min(L_t, M_t),

    while the sharper global certificate charges color ``c`` by
    ``min(L_t,M_t) l_(t,c)``.
    """

    packet_id: str
    color_degrees: tuple[tuple[Color, int], ...]

    def __post_init__(self) -> None:
        colors = [color for color, _degree in self.color_degrees]
        if not self.packet_id:
            raise ValueError("an affine packet id must be nonempty")
        if not self.color_degrees:
            raise ValueError("an affine patch must contain at least one color")
        if len(set(colors)) != len(colors):
            raise ValueError("affine patch colors must be unique")
        if any(degree <= 0 for _color, degree in self.color_degrees):
            raise ValueError("affine patch color degrees must be positive")

    @property
    def color_count(self) -> int:
        return len(self.color_degrees)

    @property
    def maximum_color_degree(self) -> int:
        return max(degree for _color, degree in self.color_degrees)

    @property
    def compression_factor(self) -> int:
        return min(self.maximum_color_degree, self.color_count)

    @property
    def local_trace_coefficient(self) -> int:
        return self.maximum_color_degree * self.compression_factor


@dataclass(frozen=True)
class AffineCarlesonLedger:
    """Exact value of the direct affine color-load certificate."""

    color_loads: tuple[tuple[Color, int], ...]
    maximum_color_load: int


def affine_carleson_ledger(
    profiles: Sequence[AffinePatchProfile],
) -> AffineCarlesonLedger:
    """Return ``H_aff=max_c sum_t min(L_t,M_t) l_(t,c)``."""

    loads: dict[Color, int] = {}
    packet_ids: set[str] = set()
    for profile in profiles:
        if profile.packet_id in packet_ids:
            raise ValueError("affine packet ids must be unique")
        packet_ids.add(profile.packet_id)
        factor = profile.compression_factor
        for color, degree in profile.color_degrees:
            loads[color] = loads.get(color, 0) + factor * degree
    ordered = tuple(sorted(loads.items(), key=lambda item: repr(item[0])))
    return AffineCarlesonLedger(
        color_loads=ordered,
        maximum_color_load=max(loads.values(), default=0),
    )


@dataclass(frozen=True)
class AffineEnergyCertificate:
    """Replay of the global summation following the local patch lemma."""

    total_color_energy: Fraction
    local_patch_majorant: Fraction
    carleson_majorant: Fraction
    carleson_load: int
    local_does_not_exceed_carleson: bool


def certify_affine_energy(
    profiles: Sequence[AffinePatchProfile],
    color_energy: Mapping[Color, Fraction],
) -> AffineEnergyCertificate:
    r"""Check the exact global affine-packet inequality.

    Put ``x_c=|z_c|^2``, ``X_t=sum_(c in K_t)x_c`` and
    ``F_t=sum_c l_(t,c)x_c``.  The local trace proof gives

        Q_t <= min(L_t,M_t) X_t F_t.

    Since ``X_t<=X=sum_c x_c``, summing gives

        sum_t Q_t <= H_aff X^2.

    The input values are exact nonnegative rationals.
    """

    energies = {color: Fraction(value) for color, value in color_energy.items()}
    if any(value < 0 for value in energies.values()):
        raise ValueError("color energies must be nonnegative")
    total = sum(energies.values(), Fraction(0))
    local = Fraction(0)
    for profile in profiles:
        patch_energy = sum(
            (energies.get(color, Fraction(0)) for color, _ in profile.color_degrees),
            Fraction(0),
        )
        weighted_degree = sum(
            (
                degree * energies.get(color, Fraction(0))
                for color, degree in profile.color_degrees
            ),
            Fraction(0),
        )
        local += profile.compression_factor * patch_energy * weighted_degree
    carleson = affine_carleson_ledger(profiles)
    global_bound = carleson.maximum_color_load * total * total
    if local > global_bound:
        raise AssertionError("the affine Carleson summation failed")
    return AffineEnergyCertificate(
        total_color_energy=total,
        local_patch_majorant=local,
        carleson_majorant=global_bound,
        carleson_load=carleson.maximum_color_load,
        local_does_not_exceed_carleson=True,
    )


@dataclass(frozen=True)
class CompletionFiber:
    """One completion-consistent affine/residual split."""

    affine_count: int
    residual_count: int
    color_weight: Fraction

    def __post_init__(self) -> None:
        if self.affine_count < 0 or self.residual_count < 0:
            raise ValueError("completion counts must be nonnegative")
        if self.color_weight < 0:
            raise ValueError("color weights must be nonnegative")


@dataclass(frozen=True)
class HybridMassLedger:
    """Exact first- and second-factorial masses of a hybrid split."""

    direct_mass: Fraction
    affine_direct_mass: Fraction
    residual_direct_mass: Fraction
    residual_presence_mass: Fraction
    residual_factorial_mass: Fraction
    affine_factorial_mass: Fraction
    affine_residual_cross_mass: Fraction
    full_factorial_mass: Fraction
    residual_pointwise_majorant: Fraction
    direct_split_exact: bool
    factorial_split_exact: bool
    residual_pointwise_bound: bool


def hybrid_mass_ledger(fibers: Sequence[CompletionFiber]) -> HybridMassLedger:
    """Replay the legal pre-factorial split and the illegal omitted terms.

    For ``m=a+r`` the first moment splits linearly.  The full ordered
    factorial mass instead contains

        m(m-1)=a(a-1)+r(r-1)+2ar.

    The hybrid theorem never claims to reconstruct that full factorial form.
    It uses only the residual factorial form to control the residual first
    moment.
    """

    affine_direct = sum(
        (fiber.affine_count * fiber.color_weight for fiber in fibers), Fraction(0)
    )
    residual_direct = sum(
        (fiber.residual_count * fiber.color_weight for fiber in fibers), Fraction(0)
    )
    direct = sum(
        (
            (fiber.affine_count + fiber.residual_count) * fiber.color_weight
            for fiber in fibers
        ),
        Fraction(0),
    )
    presence = sum(
        (
            fiber.color_weight
            for fiber in fibers
            if fiber.residual_count > 0
        ),
        Fraction(0),
    )
    residual_factorial = sum(
        (
            fiber.residual_count
            * (fiber.residual_count - 1)
            * fiber.color_weight
            for fiber in fibers
        ),
        Fraction(0),
    )
    affine_factorial = sum(
        (
            fiber.affine_count
            * (fiber.affine_count - 1)
            * fiber.color_weight
            for fiber in fibers
        ),
        Fraction(0),
    )
    cross = sum(
        (
            2
            * fiber.affine_count
            * fiber.residual_count
            * fiber.color_weight
            for fiber in fibers
        ),
        Fraction(0),
    )
    full_factorial = sum(
        (
            (fiber.affine_count + fiber.residual_count)
            * (fiber.affine_count + fiber.residual_count - 1)
            * fiber.color_weight
            for fiber in fibers
        ),
        Fraction(0),
    )
    pointwise_majorant = presence + residual_factorial / 2
    if direct != affine_direct + residual_direct:
        raise AssertionError("the completion first moment did not split")
    if full_factorial != affine_factorial + residual_factorial + cross:
        raise AssertionError("the factorial split identity failed")
    if residual_direct > pointwise_majorant:
        raise AssertionError("the residual first-moment majorant failed")
    return HybridMassLedger(
        direct_mass=direct,
        affine_direct_mass=affine_direct,
        residual_direct_mass=residual_direct,
        residual_presence_mass=presence,
        residual_factorial_mass=residual_factorial,
        affine_factorial_mass=affine_factorial,
        affine_residual_cross_mass=cross,
        full_factorial_mass=full_factorial,
        residual_pointwise_majorant=pointwise_majorant,
        direct_split_exact=True,
        factorial_split_exact=True,
        residual_pointwise_bound=True,
    )

