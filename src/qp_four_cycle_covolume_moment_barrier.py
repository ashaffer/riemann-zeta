"""A critical-height obstruction to a naive covolume moment bound.

The exact degenerate-plane covolume is

    P(C,e)^2 = (eta^2 ||r||_2^4 + theta^2 ||s||_2^4)
               / gcd(eta, theta)^2.

It is tempting to sum ``P(C,e)`` against the four-color weight and hope for
an ``O(D)`` bound.  The family below disproves that statement in the full
integer shell model, even at null height ``D^(1/4)`` and below the low-plane
cutoff ``P <= q/D``.  It is deliberately not asserted to consist of primes.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CriticalCovolumeMomentWitness:
    scale: int
    determinant_budget: int
    ambient_scale: int
    row_direction: tuple[int, int]
    column_direction: tuple[int, int]
    row_gap: int
    column_gap: int
    colors: tuple[int, int, int, int]
    color_determinant: int
    relation_defect: int
    null_height: int
    direction_norm_square: int
    covolume_square: int
    low_plane_cutoff: int

    @property
    def distinct_colors(self) -> bool:
        return len(set(self.colors)) == 4

    @property
    def below_determinant_budget(self) -> bool:
        return 0 < abs(self.color_determinant) <= self.determinant_budget

    @property
    def below_low_plane_cutoff(self) -> bool:
        return self.covolume_square <= self.low_plane_cutoff**2

    @property
    def equal_weight_moment_exceeds_d(self) -> bool:
        # Put coefficient 1/2 on each of the four colors.  Its l2 norm is one
        # and this one color matrix contributes P/16.
        return self.covolume_square > (16 * self.determinant_budget) ** 2


def critical_covolume_moment_witness(
    scale: int = 16,
) -> CriticalCovolumeMomentWitness:
    """Return the exact critical family at integral scale ``N=scale``.

    Set

        D=N^16, n=N^2, theta=N^13, T=2N^29,
        r=s=(n,n+1), eta=1.

    The four colors are the integral solution obtained from
    ``K s=eta r_perp`` and ``K^T r=theta s_perp``.  Their common size is
    ``2N^33``; we use ``q=4N^33`` so this is the usual ``q/2`` shell scale.
    """

    if scale < 16:
        raise ValueError("scale must be at least 16")
    n = scale**2
    theta = scale**13
    carrier = 2 * scale**29
    determinant_budget = scale**16
    ambient_scale = 4 * scale**33

    # X + eta + theta is divisible by n+1.  This makes all four entries
    # integral without hiding any denominator in the covolume.
    x_base = (n + 1) * carrier - 1 - theta
    c11 = (n + 1) * x_base
    c12 = n * x_base - 1
    c21 = n * x_base - theta
    c22 = n * n * carrier - n * (1 + theta)
    colors = (c11, c12, c21, c22)

    r1, r2 = n, n + 1
    s1, s2 = n, n + 1
    relation_defect = (
        r1 * s1 * c11
        - r1 * s2 * c12
        - r2 * s1 * c21
        + r2 * s2 * c22
    )
    color_determinant = c11 * c22 - c12 * c21
    norm_square = n * n + (n + 1) * (n + 1)
    covolume_square = (1 + theta * theta) * norm_square * norm_square

    return CriticalCovolumeMomentWitness(
        scale=scale,
        determinant_budget=determinant_budget,
        ambient_scale=ambient_scale,
        row_direction=(n, n + 1),
        column_direction=(n, n + 1),
        row_gap=1,
        column_gap=theta,
        colors=colors,
        color_determinant=color_determinant,
        relation_defect=relation_defect,
        null_height=(n + 1) * (n + 1),
        direction_norm_square=norm_square,
        covolume_square=covolume_square,
        low_plane_cutoff=ambient_scale // determinant_budget,
    )
