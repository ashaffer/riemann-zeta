#!/usr/bin/env python3
"""Exact combinatorial and exponent ledger for rough first-return weights.

The module deliberately proves only a *method-class* obstruction.  It checks
the empty-prefix expansion of a nearest-survivor distance, its exact
inclusion--exclusion expansion, the gap-square truncation inequality, and the
rank of the prefix kernel.  None of these finite identities is a no-go theorem
for arithmetic cancellation in the actual rough set.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


KAPPA = Fraction(1_974_048_259, 100_000_000_000)
BETA_MIN = Fraction(1537, 10_000)
BETA_MOMENT_MAX = Fraction(4, 25)
SHALLOW_BLOCK = Fraction(33, 133)
COMPANION_H_MIN = Fraction(1, 2)
COMPANION_H_MAX = Fraction(5797, 10_000)

Matrix = tuple[tuple[int, int], tuple[int, int]]
IDENTITY: Matrix = ((1, 0), (0, 1))


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] - right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def transition_matrix(bit: int) -> Matrix:
    if bit not in (0, 1):
        raise ValueError("bit must be Boolean")
    return ((1 - bit, 0), (1, 1))


def automaton_product(bits: list[int], cutoff: int) -> Matrix:
    """Chronological product M(b_G)...M(b_1)."""

    if cutoff < 1 or len(bits) <= cutoff:
        raise ValueError("need bits through the cutoff")
    result = IDENTITY
    for h in range(1, cutoff + 1):
        result = matrix_multiply(transition_matrix(bits[h]), result)
    return result


def automaton_closed_form(bits: list[int], cutoff: int) -> Matrix:
    """Triangular closed form: one empty product and its Jordan cocycle."""

    if cutoff < 1 or len(bits) <= cutoff:
        raise ValueError("need bits through the cutoff")
    alive = 1
    total = 0
    for h in range(1, cutoff + 1):
        total += alive
        alive *= 1 - bits[h]
    return ((alive, 0), (total, 1))


def duhamel_difference(new_bits: list[int], old_bits: list[int], cutoff: int) -> Matrix:
    """Rank-one marked-site expansion of P(new)-P(old).

    This uses new matrices after the marked physical shift and old matrices
    before it.  In the rough-flow application ``new_bits<=old_bits`` and the
    marked scalar is the indicator that the site is deleted in the band.
    """

    if len(new_bits) <= cutoff or len(old_bits) <= cutoff:
        raise ValueError("need both words through the cutoff")
    total: Matrix = ((0, 0), (0, 0))
    for marked in range(1, cutoff + 1):
        later = IDENTITY
        for h in range(marked + 1, cutoff + 1):
            later = matrix_multiply(transition_matrix(new_bits[h]), later)
        earlier = IDENTITY
        for h in range(1, marked):
            earlier = matrix_multiply(transition_matrix(old_bits[h]), earlier)
        insertion = matrix_subtract(
            transition_matrix(new_bits[marked]),
            transition_matrix(old_bits[marked]),
        )
        total = matrix_add(
            total,
            matrix_multiply(matrix_multiply(later, insertion), earlier),
        )
    return total


def first_return(bits: list[int]) -> int:
    """Distance from the anchored survivor at zero to the next survivor."""

    if len(bits) < 2 or bits[0] != 1 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("bits must start with 1 and contain a later survivor")
    try:
        return bits.index(1, 1)
    except ValueError as exc:
        raise ValueError("bits must contain a later survivor") from exc


def truncated_empty_prefix(bits: list[int], cutoff: int) -> int:
    """Return sum_{1<=h<=G} prod_{1<=j<h}(1-b_j)."""

    if cutoff < 1 or len(bits) <= cutoff:
        raise ValueError("need bits through the cutoff")
    total = 0
    prefix_empty = 1
    for h in range(1, cutoff + 1):
        total += prefix_empty
        prefix_empty *= 1 - bits[h]
    return total


def automaton_truncated_return(bits: list[int], cutoff: int) -> int:
    """Evaluate the same law as a bond-dimension-two matrix product.

    With column state ``(alive,total)``, one step with input bit ``b`` is

        [[1-b, 0], [1, 1]] (alive,total)^T.

    This is a genuinely constant-state representation, but it is not a sum
    of separated Dirichlet-convolution coefficients.
    """

    if cutoff < 1 or len(bits) <= cutoff:
        raise ValueError("need bits through the cutoff")
    return automaton_product(bits, cutoff)[1][0]


def inclusion_exclusion_prefix(bits: list[int], cutoff: int) -> int:
    """Exact grouped inclusion--exclusion form of the truncated return."""

    if cutoff < 1 or len(bits) <= cutoff:
        raise ValueError("need bits through the cutoff")
    total = cutoff
    indices = range(1, cutoff)
    for size in range(1, cutoff):
        for subset in combinations(indices, size):
            monomial = 1
            for index in subset:
                monomial *= bits[index]
            total += (-1) ** size * (cutoff - max(subset)) * monomial
    return total


def truncation_tail(gap: int, cutoff: int) -> int:
    if gap < 1 or cutoff < 1:
        raise ValueError("gap and cutoff must be positive")
    return max(gap - cutoff, 0)


def tail_square_certificate(gaps: list[int], cutoff: int) -> tuple[int, Fraction]:
    """Return exact tail mass and the G_2/G upper bound."""

    if cutoff < 1 or any(gap < 1 for gap in gaps):
        raise ValueError("positive gaps and cutoff required")
    tail = sum(truncation_tail(gap, cutoff) for gap in gaps)
    bound = Fraction(sum(gap * gap for gap in gaps), cutoff)
    if tail > bound:
        raise AssertionError("(g-G)_+ <= g^2/G failed")
    return tail, bound


def rational_rank(matrix: list[list[int]]) -> int:
    """Gaussian-elimination rank over Q for a small exact matrix."""

    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged matrix")
    work = [[Fraction(value) for value in row] for row in matrix]
    rank = 0
    for column in range(width):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                value - scale * pivot_value
                for value, pivot_value in zip(work[row], work[rank])
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def prefix_kernel(size: int) -> list[list[int]]:
    """The matrix K(d,h)=1_{h<=d}, 1<=d,h<=size."""

    if size < 1:
        raise ValueError("positive size required")
    return [[int(h <= d) for h in range(1, size + 1)] for d in range(1, size + 1)]


def periodic_parity_ledger(points: list[int], period: int) -> dict[str, int]:
    """Exact unweighted and symmetrized parity modes on a periodic node set."""

    if period < 1 or points != sorted(set(points)) or not points:
        raise ValueError("need sorted distinct points in one positive period")
    if points[0] < 0 or points[-1] >= period:
        raise ValueError("points must lie in [0,period)")
    gaps = [right - left for left, right in zip(points, points[1:])]
    gaps.append(points[0] + period - points[-1])
    unweighted = sum(1 if point % 2 == 0 else -1 for point in points)
    twice_sym = sum(
        (gaps[index - 1] + gaps[index])
        * (1 if point % 2 == 0 else -1)
        for index, point in enumerate(points)
    )
    return {
        "unweighted_parity": unweighted,
        "twice_sym_parity": twice_sym,
        "gap_square": sum(gap * gap for gap in gaps),
        "period": period,
    }


@dataclass(frozen=True)
class Ledger:
    kappa: Fraction = KAPPA
    beta_min: Fraction = BETA_MIN
    moment_max: Fraction = BETA_MOMENT_MAX
    shallow_block: Fraction = SHALLOW_BLOCK
    companion_h_min: Fraction = COMPANION_H_MIN
    companion_h_max: Fraction = COMPANION_H_MAX

    @property
    def minimum_cutoff_exponent(self) -> Fraction:
        """G_2<<Y^(1+o(1)) and tail<=Y^(1-kappa) require G>=Y^kappa."""

        return self.kappa

    @property
    def constant_error_degree_exponent(self) -> Fraction:
        """Paturi's deg(NOR_G)=Theta(sqrt(G)) exponent at minimal G."""

        return self.kappa / 2

    @property
    def bazin_shallow_localization_margin(self) -> Fraction:
        """The shallow h=33/133 slice has no legal Bazin lambda wedge."""

        return self.shallow_block - 3 * self.beta_min

    @property
    def bazin_modulus_range_margin(self) -> Fraction:
        """The selected q-range itself lies below Bazin's x^(1/3) range."""

        return Fraction(1, 3) - self.shallow_block

    @property
    def bazin_companion_bottom_margin(self) -> Fraction:
        """h-3b at the shortest companion block and smallest q."""

        return self.companion_h_min - 3 * self.beta_min

    @property
    def bazin_companion_top_margin(self) -> Fraction:
        return self.companion_h_max - 3 * self.beta_min

    @property
    def bazin_bottom_carrier_margin(self) -> Fraction:
        """Raw localized saving (h-3b)/2 minus kappa at bottom."""

        return self.bazin_companion_bottom_margin / 2 - self.kappa

    @property
    def bazin_carrier_clearance_height(self) -> Fraction:
        """At b=beta_min, raw global-scale saving clears at h>3b+2kappa."""

        return 3 * self.beta_min + 2 * self.kappa

    @property
    def bazin_local_block_target_margin(self) -> Fraction:
        """Best companion h minus height needed to beat H*Y^-kappa.

        The twist term Y*q^(3/2)*H^(-1/2) is at most H*Y^-kappa only
        if h >= 2/3+b+(2/3)kappa.
        """

        threshold = Fraction(2, 3) + self.beta_min + 2 * self.kappa / 3
        return self.companion_h_max - threshold

    @property
    def moment_overlap_width(self) -> Fraction:
        """Only q exponents in [beta_min,.16] can start in the proved G_2 range."""

        return self.moment_max - self.beta_min

    def as_dict(self) -> dict[str, str | bool]:
        return {
            "kappa": str(self.kappa),
            "minimum_cutoff_exponent": str(self.minimum_cutoff_exponent),
            "constant_error_degree_exponent": str(
                self.constant_error_degree_exponent
            ),
            "bazin_shallow_localization_margin": str(
                self.bazin_shallow_localization_margin
            ),
            "bazin_shallow_localization_possible": (
                self.bazin_shallow_localization_margin >= 0
            ),
            "bazin_modulus_range_margin": str(self.bazin_modulus_range_margin),
            "bazin_selected_moduli_in_range": self.bazin_modulus_range_margin > 0,
            "bazin_companion_bottom_margin": str(
                self.bazin_companion_bottom_margin
            ),
            "bazin_companion_top_margin": str(self.bazin_companion_top_margin),
            "bazin_bottom_carrier_margin": str(self.bazin_bottom_carrier_margin),
            "bazin_carrier_clearance_height": str(
                self.bazin_carrier_clearance_height
            ),
            "bazin_local_block_target_margin": str(
                self.bazin_local_block_target_margin
            ),
            "moment_overlap_width": str(self.moment_overlap_width),
        }


def self_check() -> dict[str, object]:
    for gap in range(1, 13):
        bits = [1] + [0] * (gap - 1) + [1] + [0] * 12
        for cutoff in range(1, 9):
            expected = min(gap, cutoff)
            assert truncated_empty_prefix(bits, cutoff) == expected
            assert automaton_truncated_return(bits, cutoff) == expected
            assert automaton_product(bits, cutoff) == automaton_closed_form(
                bits, cutoff
            )
            assert inclusion_exclusion_prefix(bits, cutoff) == expected
            assert expected + max(gap - cutoff, 0) == gap
    for size in range(1, 13):
        assert rational_rank(prefix_kernel(size)) == size
    tail_square_certificate([1, 2, 5, 11, 17], 6)
    ledger = Ledger()
    assert ledger.bazin_shallow_localization_margin < 0
    assert ledger.bazin_companion_bottom_margin > 0
    assert ledger.bazin_bottom_carrier_margin < 0
    assert ledger.bazin_local_block_target_margin < 0
    assert ledger.bazin_modulus_range_margin > 0
    for cutoff in range(1, 8):
        for old_mask in range(1 << cutoff):
            old = [1] + [(old_mask >> index) & 1 for index in range(cutoff)]
            for new_mask in range(1 << cutoff):
                if new_mask & ~old_mask:
                    continue
                new = [1] + [(new_mask >> index) & 1 for index in range(cutoff)]
                direct = matrix_subtract(
                    automaton_product(new, cutoff),
                    automaton_product(old, cutoff),
                )
                assert duhamel_difference(new, old, cutoff) == direct
    m0 = transition_matrix(0)
    m1 = transition_matrix(1)
    assert matrix_subtract(matrix_multiply(m0, m1), matrix_multiply(m1, m0)) == (
        (0, 0),
        (-1, 0),
    )
    parity = periodic_parity_ledger([0, 1, 3, 4], 8)
    assert parity == {
        "unweighted_parity": 0,
        "twice_sym_parity": 4,
        "gap_square": 22,
        "period": 8,
    }
    old = [1] + [1] * 12
    new = [1] + [0] * 12
    worst_difference = matrix_subtract(
        automaton_product(new, 12), automaton_product(old, 12)
    )
    assert worst_difference[1][0] == 11
    return {
        "empty_prefix": True,
        "bond_dimension_two": True,
        "triangular_jordan_cocycle": True,
        "rank_one_duhamel": True,
        "periodic_parity_countermodel": parity,
        "linear_recursive_norm_witness": worst_difference[1][0],
        "inclusion_exclusion": True,
        "tail_square": True,
        "prefix_kernel_rank_12": rational_rank(prefix_kernel(12)),
        "ledger": ledger.as_dict(),
    }


if __name__ == "__main__":
    print(self_check())
