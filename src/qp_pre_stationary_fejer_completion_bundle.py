"""Exact pre-stationary Fejer lifts and completion-Fourier identities.

The functions in this file are finite algebra.  They do not assert the open
mask-sensitive stationary large-sieve theorem.  In particular, the
``completion_fourier_energy`` identity makes explicit that Fourier analysis
in the completion variable supplies a Kronecker delta, not an additional
decay factor inside one fixed-completion fibre.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import pi, sin, sqrt
from typing import Mapping, Sequence


Pair = tuple[int, int]
Triple = tuple[int, int, int]


def e(theta: float) -> complex:
    """Return ``exp(2*pi*i*theta)``."""

    from cmath import exp

    return exp(2j * pi * theta)


def fejer_coefficients(order: int) -> dict[int, Fraction]:
    """Fourier coefficients of the height-one normalized Fejer kernel.

    The returned coefficients are nonnegative, supported on ``|h|<order``,
    and have sum one.
    """

    if order <= 0:
        raise ValueError("order must be positive")
    return {
        h: Fraction(order - abs(h), order * order)
        for h in range(-order + 1, order)
    }


def convolve_coefficients(
    left: Mapping[int, Fraction], right: Mapping[int, Fraction]
) -> dict[int, Fraction]:
    """Convolve two finitely supported Fourier coefficient sequences."""

    answer: defaultdict[int, Fraction] = defaultdict(Fraction)
    for h, first in left.items():
        for k, second in right.items():
            answer[h + k] += first * second
    return dict(answer)


def jackson_coefficients(order: int, power: int = 2) -> dict[int, Fraction]:
    """Coefficients of ``Fejer_order(theta)**power``.

    These are still nonnegative and sum to one.  Their support is
    ``|h|<power*(order-1)+1``.  Thus a fixed power can be derived using only
    harmonics below a prescribed physical cutoff by reducing ``order`` by
    that fixed factor.
    """

    if power <= 0:
        raise ValueError("power must be positive")
    base = fejer_coefficients(order)
    answer = {0: Fraction(1)}
    for _ in range(power):
        answer = convolve_coefficients(answer, base)
    return answer


def kernel_value(coefficients: Mapping[int, Fraction], theta: float) -> complex:
    """Evaluate the trigonometric kernel with the supplied coefficients."""

    return sum(float(value) * e(h * theta) for h, value in coefficients.items())


def closed_fejer_value(order: int, theta: float) -> float:
    """Evaluate normalized Fejer by its sine quotient."""

    if order <= 0:
        raise ValueError("order must be positive")
    distance = theta - round(theta)
    if abs(distance) < 1.0e-15:
        return 1.0
    return (sin(pi * order * distance) / (order * sin(pi * distance))) ** 2


def harmonic_lift(
    coefficients_in: Mapping[int, complex],
    harmonics: Mapping[int, Fraction],
) -> dict[tuple[int, int], complex]:
    """The canonical coefficient lift ``Jz(c,h)=sqrt(gamma_h) z_c``."""

    return {
        (colour, h): value * sqrt(float(weight))
        for colour, value in coefficients_in.items()
        for h, weight in harmonics.items()
    }


def norm_squared(values: Mapping[object, complex] | Sequence[complex]) -> float:
    """Squared ell-two norm."""

    iterable = values.values() if isinstance(values, Mapping) else values
    return float(sum(abs(value) ** 2 for value in iterable))


def scalar_kernel_operator(
    coefficients_in: Mapping[int, complex],
    amplitudes: Mapping[tuple[int, int], complex],
    phases: Mapping[tuple[int, int], float],
    harmonics: Mapping[int, Fraction],
) -> dict[int, complex]:
    """Apply ``Tz(x)=sum_c z_c W(x,c) K(theta(x,c))``."""

    outputs = {output for output, _ in amplitudes}
    return {
        output: sum(
            coefficients_in.get(colour, 0j)
            * amplitude
            * kernel_value(harmonics, phases[output, colour])
            for (candidate, colour), amplitude in amplitudes.items()
            if candidate == output
        )
        for output in outputs
    }


def lifted_kernel_operator(
    lifted: Mapping[tuple[int, int], complex],
    amplitudes: Mapping[tuple[int, int], complex],
    phases: Mapping[tuple[int, int], float],
    harmonics: Mapping[int, Fraction],
) -> dict[int, complex]:
    """Apply the exact lifted synthesis to ``Jz``.

    The second square root of ``gamma_h`` belongs to the operator.  Hence
    this equals ``scalar_kernel_operator`` while ``J`` itself is an
    isometry.
    """

    outputs = {output for output, _ in amplitudes}
    return {
        output: sum(
            lifted.get((colour, h), 0j)
            * amplitude
            * sqrt(float(weight))
            * e(h * phases[output, colour])
            for (candidate, colour), amplitude in amplitudes.items()
            if candidate == output
            for h, weight in harmonics.items()
        )
        for output in outputs
    }


def reciprocal_phase(q: int, a: int, b: int, colour: int) -> Fraction:
    r"""Return the literal reciprocal defect ``q^3/(8ac)-b``."""

    if min(q, a, b, colour) <= 0:
        raise ValueError("all physical parameters must be positive")
    return Fraction(q**3, 8 * a * colour) - b


def hard_window(q: int, D: int, a: int, b: int, colour: int) -> int:
    """The original pre-stationary edge window."""

    return int(abs(8 * a * b * colour - q**3) <= q * D)


def exact_hard_window_amplitude(
    q: int,
    D: int,
    a: int,
    b: int,
    colour: int,
    harmonics: Mapping[int, Fraction],
) -> complex:
    """Return ``kappa/K(theta)`` for the exact hard-window representation.

    The caller must choose the Fejer order so that the kernel has no zero on
    the physical target window.  A zero denominator is rejected rather than
    hidden.
    """

    selected = hard_window(q, D, a, b, colour)
    if not selected:
        return 0j
    theta = float(reciprocal_phase(q, a, b, colour))
    value = kernel_value(harmonics, theta)
    if abs(value) < 1.0e-14:
        raise ZeroDivisionError("the chosen Fejer kernel vanishes on the window")
    return 1.0 / value


def hard_window_scalar_matrix(
    q: int,
    D: int,
    rows: Sequence[int],
    columns: Sequence[int],
    colours: Sequence[int],
    coefficients_in: Mapping[int, complex],
) -> dict[tuple[int, int], complex]:
    """Build the literal matrix ``A_z(a,b)`` on finite index sets."""

    return {
        (a, b): sum(
            coefficients_in.get(colour, 0j) * hard_window(q, D, a, b, colour)
            for colour in colours
        )
        for a in rows
        for b in columns
    }


def hard_window_stinespring_matrix(
    q: int,
    D: int,
    rows: Sequence[int],
    columns: Sequence[int],
    colours: Sequence[int],
    coefficients_in: Mapping[int, complex],
    harmonics: Mapping[int, Fraction],
) -> dict[tuple[tuple[int, int], int], complex]:
    """Build the exact lifted matrix ``V_z((a,h),b)`` from (2.1)."""

    answer: dict[tuple[tuple[int, int], int], complex] = {}
    for a in rows:
        for h, gamma_h in harmonics.items():
            for b in columns:
                answer[(a, h), b] = sqrt(float(gamma_h)) * sum(
                    coefficients_in.get(colour, 0j)
                    * exact_hard_window_amplitude(
                        q, D, a, b, colour, harmonics
                    )
                    * e(h * float(reciprocal_phase(q, a, b, colour)))
                    for colour in colours
                )
    return answer


def contract_stinespring_matrix(
    lifted: Mapping[tuple[tuple[int, int], int], complex],
    rows: Sequence[int],
    columns: Sequence[int],
    harmonics: Mapping[int, Fraction],
) -> dict[tuple[int, int], complex]:
    """Apply the norm-one row contraction ``R`` to a lifted matrix."""

    return {
        (a, b): sum(
            sqrt(float(gamma_h)) * lifted.get(((a, h), b), 0j)
            for h, gamma_h in harmonics.items()
        )
        for a in rows
        for b in columns
    }


def schatten_fourth_power(
    matrix: Mapping[tuple[object, object], complex]
) -> float:
    r"""Return ``tr((T^*T)^2)`` for a finite sparse matrix."""

    rows = {row for row, _ in matrix}
    columns = {column for _, column in matrix}
    total = 0.0
    for first in columns:
        for second in columns:
            gram_entry = sum(
                matrix.get((row, first), 0j).conjugate()
                * matrix.get((row, second), 0j)
                for row in rows
            )
            total += abs(gram_entry) ** 2
    return total


def pair_bundle_energy(
    pairs: Sequence[Pair],
    weights: Mapping[Pair, complex],
    center: float,
    harmonics: Mapping[int, Fraction],
) -> float:
    r"""Energy of the supported two-inverse/completion vector bundle.

    The feature attached to ``(a,b)`` is

    ``delta_(a+b) tensor v_(C/a) tensor v_(C/b)``,

    where ``v_theta(h)=sqrt(gamma_h)e(h theta)``.
    """

    amplitudes: defaultdict[tuple[int, int, int], complex] = defaultdict(complex)
    for a, b in pairs:
        weight = weights.get((a, b), 0j)
        for h, gamma_h in harmonics.items():
            for k, gamma_k in harmonics.items():
                amplitudes[a + b, h, k] += (
                    weight
                    * sqrt(float(gamma_h * gamma_k))
                    * e(h * center / a + k * center / b)
                )
    return norm_squared(amplitudes)


def pair_gram_energy(
    pairs: Sequence[Pair],
    weights: Mapping[Pair, complex],
    center: float,
    harmonics: Mapping[int, Fraction],
) -> float:
    """The exact Gram expansion of ``pair_bundle_energy``."""

    total = 0j
    for a, b in pairs:
        for c, d in pairs:
            if a + b != c + d:
                continue
            total += (
                weights.get((a, b), 0j)
                * weights.get((c, d), 0j).conjugate()
                * kernel_value(harmonics, center / a - center / c)
                * kernel_value(harmonics, center / b - center / d)
            )
    return float(total.real)


def completion_fourier_energy(
    pairs: Sequence[Pair],
    weights: Mapping[Pair, complex],
    center: float,
    harmonics: Mapping[int, Fraction],
    modulus: int,
) -> float:
    """Unitary completion-DFT realization of the same pair energy.

    Distinct relevant completion sums must be distinct modulo ``modulus``.
    Otherwise this deliberately computes the cyclic version.
    """

    if modulus <= 0:
        raise ValueError("modulus must be positive")
    total = 0.0
    for xi in range(modulus):
        for h, gamma_h in harmonics.items():
            for k, gamma_k in harmonics.items():
                amplitude = sum(
                    weights.get((a, b), 0j)
                    * sqrt(float(gamma_h * gamma_k) / modulus)
                    * e(h * center / a + k * center / b + xi * (a + b) / modulus)
                    for a, b in pairs
                )
                total += abs(amplitude) ** 2
    return total


def scalar_anchored_energy(
    pairs: Sequence[Pair],
    weights: Mapping[Pair, complex],
    center: float,
    harmonics: Mapping[int, Fraction],
) -> float:
    """Energy after contraction against the zero-phase harmonic anchor."""

    sums: defaultdict[int, complex] = defaultdict(complex)
    for a, b in pairs:
        sums[a + b] += (
            weights.get((a, b), 0j)
            * kernel_value(harmonics, center / a)
            * kernel_value(harmonics, center / b)
        )
    return norm_squared(sums)


def factorable_pair_norm(
    left: Mapping[int, complex], right: Mapping[int, complex], pairs: Sequence[Pair]
) -> tuple[float, float]:
    """Return selected pair norm and the full product norm ceiling."""

    selected = sum(abs(left[a] * right[b]) ** 2 for a, b in pairs)
    full = norm_squared(left) * norm_squared(right)
    return float(selected), float(full)


def zero_dual_action(center: Fraction, completion: Fraction, r: int, s: int) -> Fraction:
    r"""Exact action for ``m=0, h=r^2, k=s^2``.

    The stationary point is ``a=S*r/(r+s)`` and the action is
    ``C*(r+s)^2/S``.  Hence changing ``(r,s)`` with fixed sum gives no
    completion-variable cancellation at all.
    """

    if center == 0 or completion <= 0 or min(r, s) <= 0:
        raise ValueError("require C!=0, S>0 and r,s>0")
    return Fraction(center) * (r + s) ** 2 / Fraction(completion)


@dataclass(frozen=True)
class SplitThresholdLedger:
    harmonic_saving: Fraction
    completion_saving: Fraction
    product_saving: Fraction
    block_length: Fraction
    harmonic_cutoff: Fraction
    q: Fraction
    fejer_block_drift: Fraction
    harmonic_cell: Fraction
    allowed_cluster: Fraction
    airy_step: Fraction
    airy_block_range: Fraction


def proposed_split_threshold_ledger() -> SplitThresholdLedger:
    """Exact powers of ``D`` in the proposed two-factor split."""

    q = Fraction(33, 16)
    cutoff = Fraction(17, 16)
    block = Fraction(11, 16)
    harmonic = Fraction(1, 12)
    completion = Fraction(1, 16)
    # Q/(H*eta_h^(1/4)) has exponent Q-H+(1/12)/4.
    cell = q - cutoff + harmonic / 4
    # Airy coordinate step: H^(2/3) q^(-1/3); multiply by block for range.
    airy_step = 2 * cutoff / 3 - q / 3
    return SplitThresholdLedger(
        harmonic_saving=harmonic,
        completion_saving=completion,
        product_saving=harmonic + completion,
        block_length=block,
        harmonic_cutoff=cutoff,
        q=q,
        fejer_block_drift=cutoff + block - q,
        harmonic_cell=cell,
        allowed_cluster=Fraction(49, 48),
        airy_step=airy_step,
        airy_block_range=airy_step + block,
    )


def path_mask_eigenvalues() -> tuple[float, float, float]:
    """Eigenvalues of the diagonal-one three-vertex path Gram candidate."""

    return (1.0 - sqrt(2.0), 1.0, 1.0 + sqrt(2.0))


def ordered_wedge_incidence(
    triples: Sequence[Triple],
) -> dict[tuple[Pair, Pair], int]:
    """Build the literal row-pair/color-pair incidence ``H``.

    A triple is ``(row, carrier, colour)``.  Two distinct triples sharing a
    carrier give the incidence

    ``H[((a,a'),(c,c'))]=1``.

    The physical pair-uniqueness hypothesis is checked: a repeated incidence
    arising from two carriers is rejected.
    """

    by_carrier: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    for row, carrier, colour in triples:
        by_carrier[carrier].append((row, colour))
    answer: dict[tuple[Pair, Pair], int] = {}
    for entries in by_carrier.values():
        for first, (row, colour) in enumerate(entries):
            for second, (other_row, other_colour) in enumerate(entries):
                if first == second:
                    continue
                key = ((row, other_row), (colour, other_colour))
                if key in answer:
                    raise ValueError("one wedge incidence has two carriers")
                answer[key] = 1
    return answer


def color_pair_coefficients(
    coefficients_in: Mapping[int, complex], pairs: Sequence[Pair]
) -> dict[Pair, complex]:
    """Return ``xi_(c,c')=conj(z_c) z_c'`` on supplied ordered pairs."""

    return {
        (first, second): coefficients_in.get(first, 0j).conjugate()
        * coefficients_in.get(second, 0j)
        for first, second in pairs
    }


def apply_wedge_incidence(
    incidence: Mapping[tuple[Pair, Pair], int | complex],
    coefficients: Mapping[Pair, complex],
) -> dict[Pair, complex]:
    """Apply the second physical incidence ``H xi``."""

    answer: defaultdict[Pair, complex] = defaultdict(complex)
    for (row_pair, color_pair), value in incidence.items():
        answer[row_pair] += complex(value) * coefficients.get(color_pair, 0j)
    return dict(answer)


def direct_row_gram(
    triples: Sequence[Triple], coefficients_in: Mapping[int, complex]
) -> dict[Pair, complex]:
    r"""Compute ``sum_b conj(A_z(a,b)) A_z(a',b)`` for ``a!=a'``."""

    cells: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    rows: set[int] = set()
    carriers: set[int] = set()
    for row, carrier, colour in triples:
        cells[row, carrier] += coefficients_in.get(colour, 0j)
        rows.add(row)
        carriers.add(carrier)
    answer = {
        (row, other_row): sum(
            cells[row, carrier].conjugate() * cells[other_row, carrier]
            for carrier in carriers
        )
        for row in rows
        for other_row in rows
        if row != other_row
    }
    return {pair: value for pair, value in answer.items() if value != 0}


def masked_wedge_quadratic(
    incidence: Mapping[tuple[Pair, Pair], int | complex],
    coefficients: Mapping[Pair, complex],
    mask: Mapping[tuple[Pair, Pair, Pair], complex],
) -> complex:
    r"""A mask depending jointly on row pair and two color pairs.

    Keys of ``mask`` are ``(alpha,gamma,gamma')``.  This includes a mask on
    ``H^*H`` and the more refined case where the common row-pair witness is
    retained before summation.
    """

    total = 0j
    for (row_pair, first), first_incidence in incidence.items():
        for (candidate, second), second_incidence in incidence.items():
            if candidate != row_pair:
                continue
            total += (
                coefficients.get(first, 0j).conjugate()
                * mask.get((row_pair, first, second), 0j)
                * complex(first_incidence).conjugate()
                * complex(second_incidence)
                * coefficients.get(second, 0j)
            )
    return total


def absolute_wedge_majorant(
    incidence: Mapping[tuple[Pair, Pair], int | complex],
    coefficients: Mapping[Pair, complex],
) -> float:
    """Return ``sum_alpha (sum_gamma |H_agamma xi_gamma|)^2``."""

    rows: defaultdict[Pair, float] = defaultdict(float)
    for (row_pair, color_pair), value in incidence.items():
        rows[row_pair] += abs(complex(value) * coefficients.get(color_pair, 0j))
    return float(sum(value * value for value in rows.values()))


def incidence_expansion_norms(
    incidence: Mapping[tuple[Pair, Pair], int | complex],
    coefficients: Mapping[Pair, complex],
) -> tuple[float, float]:
    """Original and incidence-expanded coefficient norms.

    Restoring a completion coordinate by replacing ``xi_gamma`` with one
    copy for every incidence ``(alpha,gamma)`` changes the squared norm from
    ``sum_gamma |xi_gamma|^2`` to
    ``sum_(alpha,gamma in H) |xi_gamma|^2``.  The ratio is the exact
    participation loss.
    """

    original = norm_squared(coefficients)
    expanded = sum(
        abs(complex(value) * coefficients.get(color_pair, 0j)) ** 2
        for (_, color_pair), value in incidence.items()
    )
    return original, float(expanded)


def same_center_pair_rank(center_labels: Sequence[int]) -> int:
    """Rank of the selector ``1_(center_i=center_j)``.

    Every nonempty center block is an all-ones rank-one block.  Hence the
    rank is exactly the number of represented centers, exhibiting the first
    non-scalar pair coefficient in the global completion reduction.
    """

    return len(set(center_labels))
