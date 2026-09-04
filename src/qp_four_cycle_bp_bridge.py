"""Exact modular-inversion bridge and its frequency-block loss ledger.

For one common carrier of two fixed rows, the residual class turns the
carrier/shift pair into a modular inversion pair.  Double additive Fourier
transform therefore produces a classical Kloosterman kernel exactly.  The
same calculation also shows why the current arbitrary prime/color weights
do not satisfy the short-frequency support hypothesis of the available
bilinear theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math


@dataclass(frozen=True)
class ReciprocalLayerIdentity:
    modulus: int
    residual: int
    residual_class: int
    shift: int
    multiplier: int | None
    carrier_times_shift: int
    congruence_error: int
    unit_shift: bool


def reciprocal_layer_identity(
    *,
    center_prime: int,
    first_row: int,
    second_row: int,
    carrier: int,
    first_color: int,
    second_color: int,
) -> ReciprocalLayerIdentity:
    """Replay the exact variable-numerator inversion congruence.

    Put ``Q=q^3``, ``r=8*a*b*c-Q`` and
    ``v=a2*d-a1*c``.  The second residual is ``r+8*b*v`` and is congruent
    to ``-Q`` modulo ``a2``.  Hence

    ``b*v == -(Q+r)/8 (mod a2)``.

    If ``v`` is a unit modulo ``a2``, the right side is the multiplier in
    the reciprocal graph ``b == multiplier*inverse(v) (mod a2)``.
    """

    if min(
        center_prime,
        first_row,
        second_row,
        carrier,
        first_color,
        second_color,
    ) <= 0:
        raise ValueError("all inputs must be positive")
    if second_row % 2 == 0:
        raise ValueError("the displayed formula requires an odd row modulus")
    modulus = second_row
    center = center_prime**3
    residual = 8 * first_row * carrier * first_color - center
    shift = second_row * second_color - first_row * first_color
    inverse_eight = pow(8, -1, modulus)
    multiplier = (-(center + residual) * inverse_eight) % modulus
    error = (carrier * shift - multiplier) % modulus
    unit = math.gcd(shift, modulus) == 1
    return ReciprocalLayerIdentity(
        modulus=modulus,
        residual=residual,
        residual_class=residual % modulus,
        shift=shift,
        multiplier=multiplier if unit else None,
        carrier_times_shift=carrier * shift,
        congruence_error=error,
        unit_shift=unit,
    )


@dataclass(frozen=True)
class FourierBlockLossLedger:
    modulus: int
    block_length: int
    blocks: int
    global_delta_fourier_norm_squared: int
    block_norm_sum_lower_bound: float
    one_side_cauchy_loss_lower_bound: float


def delta_frequency_block_loss(
    modulus: int, block_length: int
) -> FourierBlockLossLedger:
    """Return the exact block loss for a physical point mass.

    An unnormalized Fourier transform of a point mass has modulus one at
    every one of the ``modulus`` frequencies.  Splitting those frequencies
    into consecutive blocks of length at most ``block_length`` gives block
    norms ``sqrt(size)``.  Their sum, relative to the global ``sqrt(m)``
    norm, is the unavoidable one-sided triangle/Cauchy loss for applying a
    short-interval bilinear estimate block by block.
    """

    if modulus <= 0 or block_length <= 0 or block_length > modulus:
        raise ValueError("require 1 <= block length <= modulus")
    full, remainder = divmod(modulus, block_length)
    sizes = [block_length] * full
    if remainder:
        sizes.append(remainder)
    norm_sum = sum(math.sqrt(size) for size in sizes)
    return FourierBlockLossLedger(
        modulus=modulus,
        block_length=block_length,
        blocks=len(sizes),
        global_delta_fourier_norm_squared=modulus,
        block_norm_sum_lower_bound=norm_sum,
        one_side_cauchy_loss_lower_bound=norm_sum / math.sqrt(modulus),
    )


def active_bp_bridge_exponents() -> dict[str, Fraction]:
    """Exact powers in the direct frequency-block obstruction."""

    d = Fraction(16, 33)
    blocks = 1 - d
    return {
        "D": d,
        "frequency_blocks": blocks,
        "one_side_block_loss": blocks / 2,
        "two_side_block_loss": blocks,
        "bp_saving": Fraction(19, 1056),
        "allowed_bridge_loss": Fraction(1, 352),
        "one_side_excess_over_allowed": blocks / 2 - Fraction(1, 352),
    }


@dataclass(frozen=True)
class PaleyMixedBlockLedger:
    """Exact Fourier ledger for a positive mask with tunable participation.

    For a prime ``p=3 (mod 4)``, let ``Q`` be the nonzero quadratic
    residues and put

    ``f(0)=sqrt(theta)``,
    ``f(x)=sqrt((1-theta)/|Q|)`` for ``x in Q``.

    The vector is nonnegative and has unit ``ell^2`` norm.  Since the
    quadratic Gauss sum is purely imaginary, every nonzero Fourier
    coefficient has the same explicitly displayed energy.  Varying
    ``theta`` changes the physical participation from atomic to diffuse
    without forcing concentration in additive-frequency blocks.
    """

    modulus: int
    block_length: int
    theta: float
    physical_participation: float
    zero_frequency_energy: float
    nonzero_frequency_energy: float
    block_norm_sum: float
    normalized_block_loss: float


def paley_mixed_block_loss(
    prime: int, block_length: int, theta: float
) -> PaleyMixedBlockLedger:
    """Return the exact positive Paley-mask block loss.

    This is a coefficient-class obstruction, not an assertion that the
    quadratic-residue mask is an actual QP carrier layer.
    """

    p = int(prime)
    if p < 3 or p % 4 != 3:
        raise ValueError("require a prime congruent to 3 modulo 4")
    if any(p % divisor == 0 for divisor in range(2, math.isqrt(p) + 1)):
        raise ValueError("require a prime modulus")
    if block_length <= 0 or block_length > p:
        raise ValueError("require 1 <= block length <= modulus")
    if not 0.0 <= theta <= 1.0:
        raise ValueError("theta must lie in [0,1]")
    residues = (p - 1) // 2
    atom = math.sqrt(theta)
    residue_weight = math.sqrt((1.0 - theta) / residues)
    zero_energy = (atom + residues * residue_weight) ** 2
    nonzero_energy = (
        (atom - residue_weight / 2.0) ** 2
        + p * residue_weight**2 / 4.0
    )
    full, remainder = divmod(p, block_length)
    sizes = [block_length] * full
    if remainder:
        sizes.append(remainder)
    block_norms = [
        math.sqrt(zero_energy + (sizes[0] - 1) * nonzero_energy)
    ]
    block_norms.extend(
        math.sqrt(size * nonzero_energy) for size in sizes[1:]
    )
    participation = 1.0 / (
        theta**2 + (1.0 - theta) ** 2 / residues
    )
    norm_sum = sum(block_norms)
    return PaleyMixedBlockLedger(
        modulus=p,
        block_length=block_length,
        theta=theta,
        physical_participation=participation,
        zero_frequency_energy=zero_energy,
        nonzero_frequency_energy=nonzero_energy,
        block_norm_sum=norm_sum,
        normalized_block_loss=norm_sum / math.sqrt(p),
    )


@dataclass(frozen=True)
class WeightedSparseDiffuseBridgeLedger:
    """Exact exponent ledger for support/participation splitting.

    Existing combinatorics gives ``D*M`` for a roughly uniform support of
    size ``M<=D`` and ``D^3/M`` for ``D<=M<=D^2``.  It therefore closes
    only subpolynomial support and the diffuse endpoint ``M>=D^2``.
    The general participation theorem closes ``M4>=D^2``.

    The all-distinct quartic vanishes on three colors.  Polarizing the
    proved ``D^(21/16)`` bound shows that a vector whose mass outside its
    three largest coordinates is ``tau`` costs ``D^(21/16)*sqrt(tau)``;
    hence ``tau<=D^(-5/8)`` is another proved sparse endpoint.

    Neither literal support nor global ``M4`` controls the frequency-block
    loss on each residual layer.  In particular disjoint layers can each
    see a point mass while global participation is arbitrarily large.
    """

    aperture_exponent_in_q: Fraction
    small_uniform_support_cutoff_exponent_in_q: Fraction
    degree_transition_exponent_in_q: Fraction
    diffuse_participation_cutoff_exponent_in_q: Fraction
    three_atom_tail_cutoff_exponent_in_degree: Fraction
    three_atom_tail_cutoff_exponent_in_q: Fraction
    one_side_block_loss_exponent_in_q: Fraction
    allowed_bp_bridge_loss_exponent_in_q: Fraction
    one_side_excess_over_allowed_exponent_in_q: Fraction
    open_uniform_support_lower_exponent_in_q: Fraction
    open_uniform_support_upper_exponent_in_q: Fraction
    global_participation_controls_each_layer: bool
    bp_bridge_shrinks_open_support_interval: bool
    arbitrary_coefficients_closed: bool


def weighted_sparse_diffuse_bridge_ledger() -> WeightedSparseDiffuseBridgeLedger:
    """Return the exact active sparse/diffuse exponent ranges."""

    degree = Fraction(16, 33)
    block_loss = (1 - degree) / 2
    allowed = Fraction(1, 352)
    return WeightedSparseDiffuseBridgeLedger(
        aperture_exponent_in_q=degree,
        small_uniform_support_cutoff_exponent_in_q=Fraction(0),
        degree_transition_exponent_in_q=degree,
        diffuse_participation_cutoff_exponent_in_q=2 * degree,
        three_atom_tail_cutoff_exponent_in_degree=Fraction(-5, 8),
        three_atom_tail_cutoff_exponent_in_q=-Fraction(5, 8) * degree,
        one_side_block_loss_exponent_in_q=block_loss,
        allowed_bp_bridge_loss_exponent_in_q=allowed,
        one_side_excess_over_allowed_exponent_in_q=block_loss - allowed,
        open_uniform_support_lower_exponent_in_q=Fraction(0),
        open_uniform_support_upper_exponent_in_q=2 * degree,
        global_participation_controls_each_layer=False,
        bp_bridge_shrinks_open_support_interval=False,
        arbitrary_coefficients_closed=False,
    )
