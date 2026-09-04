"""Exact algebra used by the arithmetic-provenance synthesis.

This module does not prove an analytic estimate.  It records two structural
facts without floating-point error:

* a zero-mass measure on an ordered path is the boundary of its cumulative
  edge flux; and
* symmetric squaring sends that boundary to a sum of product-graph
  divergences.

It also supplies the elementary composition law for adapter-loss ledgers.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import FrozenSet, Iterable, Sequence, Tuple, TypeVar


Scalar = TypeVar("Scalar")


def path_boundary(edge_flux: Sequence[Scalar]) -> list[Scalar]:
    """Return the vertex boundary of oriented path-edge coefficients.

    Edge ``j`` is oriented from vertex ``j + 1`` to vertex ``j``.  Thus a
    flux ``c`` has boundary

        (c_0, c_1-c_0, ..., c_{n-2}-c_{n-3}, -c_{n-2}).
    """

    if not edge_flux:
        # An edge list of length zero is the unique one-vertex path.
        return [0]  # type: ignore[list-item]
    zero = edge_flux[0] - edge_flux[0]
    out = [edge_flux[0]]
    out.extend(edge_flux[j] - edge_flux[j - 1] for j in range(1, len(edge_flux)))
    out.append(zero - edge_flux[-1])
    return out


def cumulative_flux(zero_mass: Sequence[Scalar]) -> list[Scalar]:
    """Invert ``path_boundary`` on vertex vectors whose total mass is zero."""

    if not zero_mass:
        raise ValueError("a path must have at least one vertex")
    if len(zero_mass) == 1:
        if zero_mass[0] != zero_mass[0] - zero_mass[0]:
            raise ValueError("a one-vertex boundary must vanish")
        return []

    total = sum(zero_mass[1:], zero_mass[0])
    zero = zero_mass[0] - zero_mass[0]
    if total != zero:
        raise ValueError("vertex vector does not have zero total mass")

    flux: list[Scalar] = []
    running = zero
    for value in zero_mass[:-1]:
        running = running + value
        flux.append(running)
    return flux


def outer(left: Sequence[Scalar], right: Sequence[Scalar]) -> list[list[Scalar]]:
    """Exact outer product, returned as a rectangular list of lists."""

    return [[x * y for y in right] for x in left]


def matrix_add(*matrices: Sequence[Sequence[Scalar]]) -> list[list[Scalar]]:
    """Add equally shaped matrices."""

    if not matrices:
        return []
    rows = len(matrices[0])
    cols = len(matrices[0][0]) if rows else 0
    if any(len(matrix) != rows for matrix in matrices):
        raise ValueError("row counts differ")
    if any(any(len(row) != cols for row in matrix) for matrix in matrices):
        raise ValueError("column counts differ")
    return [
        [sum((matrix[i][j] for matrix in matrices), matrices[0][i][j] - matrices[0][i][j])
         for j in range(cols)]
        for i in range(rows)
    ]


def matrix_subtract(
    left: Sequence[Sequence[Scalar]], right: Sequence[Sequence[Scalar]]
) -> list[list[Scalar]]:
    """Subtract equally shaped matrices."""

    if len(left) != len(right) or any(len(a) != len(b) for a, b in zip(left, right)):
        raise ValueError("matrix shapes differ")
    return [[a - b for a, b in zip(left_row, right_row)]
            for left_row, right_row in zip(left, right)]


def boundary_first(edge_vertex: Sequence[Sequence[Scalar]]) -> list[list[Scalar]]:
    """Apply the path boundary in the first coordinate of an edge x vertex array."""

    if not edge_vertex:
        return []
    cols = len(edge_vertex[0])
    if any(len(row) != cols for row in edge_vertex):
        raise ValueError("ragged matrix")
    columns = [[edge_vertex[i][j] for i in range(len(edge_vertex))] for j in range(cols)]
    bounded = [path_boundary(column) for column in columns]
    return [[bounded[j][i] for j in range(cols)] for i in range(len(edge_vertex) + 1)]


def boundary_second(vertex_edge: Sequence[Sequence[Scalar]]) -> list[list[Scalar]]:
    """Apply the path boundary in the second coordinate of a vertex x edge array."""

    if not vertex_edge:
        return []
    cols = len(vertex_edge[0])
    if any(len(row) != cols for row in vertex_edge):
        raise ValueError("ragged matrix")
    return [path_boundary(row) for row in vertex_edge]


def symmetric_square_defect(
    natural: Sequence[Scalar], discrepancy: Sequence[Scalar]
) -> list[list[Scalar]]:
    """Compute ``(natural+discrepancy)^2 - natural^2`` as outer products."""

    if len(natural) != len(discrepancy):
        raise ValueError("vector lengths differ")
    weighted = [x + y for x, y in zip(natural, discrepancy)]
    return matrix_subtract(outer(weighted, weighted), outer(natural, natural))


def polarized_symmetric_square_defect(
    natural: Sequence[Fraction], discrepancy: Sequence[Fraction]
) -> list[list[Fraction]]:
    """Return the rank-at-most-two polarization of the square defect.

    For ``weighted = natural + discrepancy`` and
    ``summed = weighted + natural``, the identity is

        weighted^2 - natural^2
          = (discrepancy tensor summed + summed tensor discrepancy) / 2.
    """

    if len(natural) != len(discrepancy):
        raise ValueError("vector lengths differ")
    summed = [Fraction(2) * x + y for x, y in zip(natural, discrepancy)]
    return [
        [(a + b) / 2 for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(
            outer(discrepancy, summed), outer(summed, discrepancy)
        )
    ]


def product_divergence_defect(
    natural: Sequence[Scalar], edge_flux: Sequence[Scalar]
) -> list[list[Scalar]]:
    """Express the symmetric-square defect as product-graph divergences.

    If ``delta = boundary(c)``, this returns

        boundary_1(c tensor natural)
        + boundary_2(natural tensor c)
        + boundary_1 boundary_2(c tensor c).
    """

    if not edge_flux:
        if len(natural) != 1:
            raise ValueError("an edge-free path has exactly one vertex")
        zero = natural[0] - natural[0]
        return [[zero]]
    discrepancy = path_boundary(edge_flux)
    if len(natural) != len(discrepancy):
        raise ValueError("natural vector and boundary lengths differ")
    mixed_left = boundary_first(outer(edge_flux, natural))
    mixed_right = boundary_second(outer(natural, edge_flux))
    double_boundary = boundary_second(boundary_first(outer(edge_flux, edge_flux)))
    return matrix_add(mixed_left, mixed_right, double_boundary)


def polarized_product_divergence_defect(
    natural: Sequence[Fraction], edge_flux: Sequence[Fraction]
) -> list[list[Fraction]]:
    """Return the minimal two-channel product divergence of the square defect."""

    if not edge_flux:
        if len(natural) != 1:
            raise ValueError("an edge-free path has exactly one vertex")
        return [[Fraction(0)]]
    discrepancy = path_boundary(edge_flux)
    if len(natural) != len(discrepancy):
        raise ValueError("natural vector and boundary lengths differ")
    summed = [Fraction(2) * x + y for x, y in zip(natural, discrepancy)]
    horizontal = boundary_first(outer(edge_flux, summed))
    vertical = boundary_second(outer(summed, edge_flux))
    return [
        [(a + b) / 2 for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(horizontal, vertical)
    ]


def semiprime_difference_diagonal(
    discrepancy: Sequence[Fraction], summed: Sequence[Fraction]
) -> Fraction:
    """Exact unordered-semiprime diagonal of ``delta * summed``.

    Off-diagonal prime products carry coefficient
    ``delta_i * summed_j + delta_j * summed_i`` and prime squares carry
    ``delta_i * summed_i``.
    """

    if len(discrepancy) != len(summed):
        raise ValueError("vector lengths differ")
    delta_norm = sum((x * x for x in discrepancy), Fraction(0))
    summed_norm = sum((x * x for x in summed), Fraction(0))
    pairing = sum((x * y for x, y in zip(discrepancy, summed)), Fraction(0))
    repeated = sum(
        (x * x * y * y for x, y in zip(discrepancy, summed)), Fraction(0)
    )
    return delta_norm * summed_norm + pairing * pairing - repeated


@dataclass(frozen=True)
class AdapterLoss:
    """A minimal exact ledger for composing proof adapters.

    Numerical exponent losses add.  Forgotten passport fields remain open
    obligations unless a later, separately proved reconstruction morphism is
    recorded in ``certified_recoveries``.
    """

    exponent_loss: Fraction = Fraction(0)
    mass_loss_exponent: Fraction = Fraction(0)
    complexity_exponent: Fraction = Fraction(0)
    resolution_loss_exponent: Fraction = Fraction(0)
    forgotten_fields: FrozenSet[str] = frozenset()
    certified_recoveries: FrozenSet[str] = frozenset()

    def __post_init__(self) -> None:
        numeric_losses = (
            self.exponent_loss,
            self.mass_loss_exponent,
            self.complexity_exponent,
            self.resolution_loss_exponent,
        )
        if any(value < 0 for value in numeric_losses):
            raise ValueError("adapter losses must be nonnegative")
        if self.forgotten_fields & self.certified_recoveries:
            raise ValueError("one adapter step cannot both forget and recover a field")

    def then(self, later: "AdapterLoss") -> "AdapterLoss":
        return AdapterLoss(
            exponent_loss=self.exponent_loss + later.exponent_loss,
            mass_loss_exponent=self.mass_loss_exponent + later.mass_loss_exponent,
            complexity_exponent=self.complexity_exponent + later.complexity_exponent,
            resolution_loss_exponent=(
                self.resolution_loss_exponent + later.resolution_loss_exponent
            ),
            forgotten_fields=(
                (self.forgotten_fields - later.certified_recoveries)
                | later.forgotten_fields
            ),
            certified_recoveries=(
                (self.certified_recoveries | later.certified_recoveries)
                - later.forgotten_fields
            ),
        )

    def fits(
        self,
        *,
        exponent_budget: Fraction,
        mass_budget: Fraction = Fraction(0),
        complexity_budget: Fraction = Fraction(0),
        resolution_budget: Fraction = Fraction(0),
        required_fields: Iterable[str] = (),
    ) -> bool:
        required = frozenset(required_fields)
        return (
            self.exponent_loss <= exponent_budget
            and self.mass_loss_exponent <= mass_budget
            and self.complexity_exponent <= complexity_budget
            and self.resolution_loss_exponent <= resolution_budget
            and not (self.forgotten_fields & required)
        )


def finite_dual_certificate(
    target: Sequence[Fraction],
    functional: Sequence[Fraction],
    atoms: Sequence[Sequence[Fraction]],
    atom_costs: Sequence[Fraction],
) -> Tuple[bool, Fraction]:
    """Check a finite atomic-gauge dual certificate exactly.

    If the Boolean result is true, every representation
    ``target = sum coefficient_i * atom_i`` costs at least the returned
    number under ``sum |coefficient_i| * atom_cost_i``.
    """

    if len(target) != len(functional):
        raise ValueError("target and functional lengths differ")
    if len(atoms) != len(atom_costs):
        raise ValueError("atom and cost counts differ")
    if any(len(atom) != len(functional) for atom in atoms):
        raise ValueError("atom dimension differs")
    if any(cost < 0 for cost in atom_costs):
        raise ValueError("atomic-gauge costs must be nonnegative")

    def pair(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
        return sum((x * y for x, y in zip(left, right)), Fraction(0))

    valid = all(abs(pair(functional, atom)) <= cost
                for atom, cost in zip(atoms, atom_costs))
    return valid, abs(pair(functional, target))
