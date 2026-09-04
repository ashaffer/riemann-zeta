#!/usr/bin/env python3
"""Growing actual-prime-power audit of a canonical pre-factorial affine peel.

The support comes from ``build_four_cycle_core`` and therefore retains that
diagnostic builder's floating support-selection trust boundary.  Everything
after support materialization--affine ranks, the completion partition,
``H_aff``, residual atoms, graph components, and A4 loads--is exact.

Within each oriented color fibre the canonical completion-consistent rule is:

1. repeatedly peel the lexicographically first largest affine line with at
   least three currently unassigned completion points;
2. then repeatedly peel the lexicographically first largest affine plane
   pinned by three noncollinear currently unassigned points;
3. send the remaining zero, one, or two points to the residual source.

The plane step is intentionally generous: three noncollinear points always
pin a plane.  It is a hostile upper test for pre-factorial plane extraction,
not a proof that every resulting plane is one of the globally certified QP
affine/Hankel patches.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import gcd
from pathlib import Path
import gc
import sys
from typing import Hashable, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_a2_packet_serialization import (  # noqa: E402
    A2CompletionPairAtom,
    A2PacketCell,
    extract_exact_secant_a2_cells,
)
from qp_a4_serialized_participation import (  # noqa: E402
    summarize_a4_unit_balances,
)
from qp_actual_prime_nds import exact_balanced_degree  # noqa: E402
from qp_four_cycle_h_graph_lab import enumerate_rectangles  # noqa: E402
from qp_four_cycle_hostile_lab import build_four_cycle_core  # noqa: E402
from qp_four_cycle_weighted_secant_lab import (  # noqa: E402
    completion_groups_from_generic_rectangles,
)
from qp_hybrid_affine_compression import (  # noqa: E402
    AffinePatchProfile,
    affine_carleson_ledger,
)


Completion = tuple[int, int, int, int]
Colors = tuple[int, int, int, int]
Cell = tuple[int, int, int, int]


FIXTURES = (
    (12_853, 12.0),
    (25_013, 12.0),
    (50_021, 12.0),
    (100_003, 12.0),
    (200_003, 12.0),
    (25_013, 24.0),
    (50_021, 24.0),
    (100_003, 24.0),
    (25_013, 32.0),
    (50_021, 32.0),
    (100_003, 32.0),
    (11_801, 35.0),
    (11_801, 36.0),
    (11_801, 44.0),
    (25_013, 40.0),
    (50_021, 40.0),
    (100_003, 40.0),
)


def primitive(vector: Sequence[int], *, canonical_sign: bool = False) -> tuple[int, ...]:
    divisor = reduce(gcd, (abs(value) for value in vector if value), 0)
    if not divisor:
        raise ValueError("an affine direction must be nonzero")
    answer = tuple(value // divisor for value in vector)
    if canonical_sign and next(value for value in answer if value) < 0:
        answer = tuple(-value for value in answer)
    return answer


def difference(first: Completion, second: Completion) -> Completion:
    return tuple(
        right - left for left, right in zip(first, second, strict=True)
    )  # type: ignore[return-value]


def rref_key(rows: Iterable[Sequence[int | Fraction]]) -> tuple[tuple[Fraction, ...], ...]:
    matrix = [[Fraction(value) for value in row] for row in rows]
    if not matrix:
        return ()
    columns = len(matrix[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (
                row
                for row in range(pivot_row, len(matrix))
                if matrix[row][column]
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        value = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / value for entry in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            value = matrix[row][column]
            matrix[row] = [
                entry - value * pivot_entry
                for entry, pivot_entry in zip(
                    matrix[row], matrix[pivot_row], strict=True
                )
            ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return tuple(tuple(row) for row in matrix if any(row))


def affine_rank(points: Sequence[Completion]) -> int:
    if not points:
        return 0
    anchor = points[0]
    return len(
        rref_key(
            difference(anchor, point)
            for point in points[1:]
        )
    )


def line_key(first: Completion, second: Completion) -> tuple[tuple[int, ...], tuple[int, ...]]:
    direction = primitive(difference(first, second), canonical_sign=True)
    wedge = tuple(
        first[left] * direction[right] - first[right] * direction[left]
        for left, right in combinations(range(4), 2)
    )
    return direction, wedge


def plane_key(points: Sequence[Completion]) -> tuple[tuple[Fraction, ...], ...]:
    if len(points) < 3 or affine_rank(points) != 2:
        raise ValueError("an affine plane needs three noncollinear points")
    return rref_key((1, *point) for point in points)


@dataclass(frozen=True)
class PeeledPatch:
    kind: str
    geometry_key: Hashable
    colors: Colors
    completions: tuple[Completion, ...]


def rich_line_candidates(points: Sequence[Completion]) -> dict[Hashable, tuple[Completion, ...]]:
    candidates: dict[Hashable, set[Completion]] = defaultdict(set)
    for first, second in combinations(points, 2):
        key = line_key(first, second)
        candidates[key].update((first, second))
    return {
        key: tuple(sorted(values))
        for key, values in candidates.items()
        if len(values) >= 3
    }


def rich_plane_candidates(points: Sequence[Completion]) -> dict[Hashable, tuple[Completion, ...]]:
    candidates: dict[Hashable, set[Completion]] = defaultdict(set)
    for triple in combinations(points, 3):
        if affine_rank(triple) != 2:
            continue
        key = plane_key(triple)
        candidates[key].update(triple)
    return {
        key: tuple(sorted(values))
        for key, values in candidates.items()
        if len(values) >= 3
    }


def choose_candidate(
    candidates: Mapping[Hashable, tuple[Completion, ...]],
) -> tuple[Hashable, tuple[Completion, ...]]:
    return min(
        candidates.items(),
        key=lambda item: (-len(item[1]), item[1], repr(item[0])),
    )


def canonical_fibre_peel(
    colors: Colors, completions: Sequence[Completion]
) -> tuple[tuple[PeeledPatch, ...], tuple[Completion, ...]]:
    remaining = set(completions)
    patches: list[PeeledPatch] = []
    while True:
        candidates = rich_line_candidates(tuple(sorted(remaining)))
        if not candidates:
            break
        key, selected = choose_candidate(candidates)
        patches.append(PeeledPatch("line", key, colors, selected))
        remaining.difference_update(selected)
    while True:
        candidates = rich_plane_candidates(tuple(sorted(remaining)))
        if not candidates:
            break
        key, selected = choose_candidate(candidates)
        patches.append(PeeledPatch("plane", key, colors, selected))
        remaining.difference_update(selected)
    return tuple(patches), tuple(sorted(remaining))


def patch_profile(index: int, patch: PeeledPatch) -> AffinePatchProfile:
    c11, c12, c21, c22 = patch.colors
    edges: dict[int, set[tuple[int, int]]] = defaultdict(set)
    for a1, a2, b1, b2 in patch.completions:
        edges[c11].add((a1, b1))
        edges[c12].add((a1, b2))
        edges[c21].add((a2, b1))
        edges[c22].add((a2, b2))
    return AffinePatchProfile(
        packet_id=f"{patch.kind}-{index:08d}",
        color_degrees=tuple(sorted((color, len(values)) for color, values in edges.items())),
    )


@dataclass(frozen=True)
class ResidualComponentSummary:
    component_count: int
    maximum_vertices: int
    maximum_distinct_edges: int
    maximum_atom_edges: int
    maximum_cycle_rank: int
    maximum_left_degree: int
    maximum_right_degree: int
    maximum_component_degree_product: int


class DisjointSet:
    def __init__(self) -> None:
        self.parent: dict[Hashable, Hashable] = {}

    def add(self, value: Hashable) -> None:
        self.parent.setdefault(value, value)

    def find(self, value: Hashable) -> Hashable:
        parent = self.parent[value]
        if parent != value:
            self.parent[value] = self.find(parent)
        return self.parent[value]

    def union(self, left: Hashable, right: Hashable) -> None:
        self.add(left)
        self.add(right)
        left_root, right_root = self.find(left), self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def residual_component_summary(cells: Sequence[A2PacketCell]) -> ResidualComponentSummary:
    total_components = 0
    maxima = [0] * 7
    for cell in cells:
        edge_multiplicity: Counter[
            tuple[tuple[int, int], tuple[int, int]]
        ] = Counter((term.left_vertex, term.right_vertex) for term in cell.terms)
        dsu = DisjointSet()
        for left, right in edge_multiplicity:
            dsu.union((0, left), (1, right))
        vertices_by_root: dict[Hashable, set[Hashable]] = defaultdict(set)
        edges_by_root: dict[
            Hashable, list[tuple[tuple[int, int], tuple[int, int], int]]
        ] = defaultdict(list)
        for vertex in dsu.parent:
            vertices_by_root[dsu.find(vertex)].add(vertex)
        for (left, right), multiplicity in edge_multiplicity.items():
            root = dsu.find((0, left))
            edges_by_root[root].append((left, right, multiplicity))
        total_components += len(vertices_by_root)
        for root, vertices in vertices_by_root.items():
            edges = edges_by_root[root]
            left_degree: Counter[tuple[int, int]] = Counter()
            right_degree: Counter[tuple[int, int]] = Counter()
            for left, right, multiplicity in edges:
                left_degree[left] += multiplicity
                right_degree[right] += multiplicity
            distinct_edges = len(edges)
            atom_edges = sum(multiplicity for _left, _right, multiplicity in edges)
            cycle_rank = distinct_edges - len(vertices) + 1
            left_max = max(left_degree.values())
            right_max = max(right_degree.values())
            values = (
                len(vertices),
                distinct_edges,
                atom_edges,
                cycle_rank,
                left_max,
                right_max,
                left_max * right_max,
            )
            maxima = [max(old, new) for old, new in zip(maxima, values, strict=True)]
    return ResidualComponentSummary(total_components, *maxima)


@dataclass(frozen=True)
class FixtureSummary:
    q: int
    cutoff: int
    degree: int
    shell_nodes: int
    rectangles: int
    color_fibres: int
    maximum_multiplicity: int
    direct_completion_mass: int
    line_patches: int
    plane_patches: int
    affine_completion_mass: int
    residual_completion_mass: int
    h_aff: int
    maximum_h_aff_color: int
    maximum_affine_patch_reuse_per_color: int
    maximum_affine_geometry_reuse_per_color: int
    maximum_source_directions_per_color: int
    maximum_source_direction_color: int
    maximum_residual_directions_per_color: int
    maximum_residual_direction_color: int
    source_factorial_atoms: int
    residual_factorial_atoms: int
    residual_cells: int
    residual_components: int
    maximum_component_vertices: int
    maximum_component_atom_edges: int
    maximum_component_cycle_rank: int
    maximum_component_degree_product: int
    residual_a4: Fraction


def direction_reuse(
    groups: Mapping[Colors, Sequence[Completion]],
) -> tuple[int, dict[int, set[tuple[int, ...]]]]:
    directions: dict[int, set[tuple[int, ...]]] = defaultdict(set)
    for colors, completions in groups.items():
        for first, second in combinations(completions, 2):
            direction = primitive(difference(first, second), canonical_sign=True)
            for color in colors:
                directions[color].add(direction)
    return max((len(values) for values in directions.values()), default=0), directions


def analyze_fixture(q: int, cutoff: float) -> FixtureSummary:
    core = build_four_cycle_core(
        q,
        width=0.2,
        cutoff=cutoff,
        kind="prime_powers",
        quadrature_order=8,
    )
    rectangles = enumerate_rectangles(core)
    groups = completion_groups_from_generic_rectangles(rectangles)
    normalized_groups = {
        tuple(colors): tuple(sorted(completions))
        for colors, completions in groups.items()
    }
    patches: list[PeeledPatch] = []
    residual_groups: dict[Colors, tuple[Completion, ...]] = {}
    for colors, completions in sorted(normalized_groups.items()):
        selected, residual = canonical_fibre_peel(colors, completions)
        patches.extend(selected)
        residual_groups[colors] = residual

    profiles = tuple(patch_profile(index, patch) for index, patch in enumerate(patches))
    carleson = affine_carleson_ledger(profiles)
    color_patch_ids: dict[int, set[int]] = defaultdict(set)
    color_geometry: dict[int, set[tuple[str, Hashable]]] = defaultdict(set)
    for index, (patch, profile) in enumerate(zip(patches, profiles, strict=True)):
        geometry = (
            (patch.kind, patch.geometry_key[0])
            if patch.kind == "line"
            else (patch.kind, patch.geometry_key)
        )
        for color, _degree in profile.color_degrees:
            color_patch_ids[int(color)].add(index)
            color_geometry[int(color)].add(geometry)

    source_direction_max, source_directions = direction_reuse(normalized_groups)
    residual_direction_max, residual_directions = direction_reuse(residual_groups)
    maximum_h_aff_color = min(
        (
            int(color)
            for color, load in carleson.color_loads
            if load == carleson.maximum_color_load
        ),
        default=0,
    )
    maximum_source_direction_color = min(
        (
            int(color)
            for color, directions in source_directions.items()
            if len(directions) == source_direction_max
        ),
        default=0,
    )
    maximum_residual_direction_color = min(
        (
            int(color)
            for color, directions in residual_directions.items()
            if len(directions) == residual_direction_max
        ),
        default=0,
    )
    degree = exact_balanced_degree(q)
    source_factorial_atoms = sum(
        len(completions) * (len(completions) - 1)
        for completions in normalized_groups.values()
    )
    residual_cells = extract_exact_secant_a2_cells(
        q=q,
        degree_parameter=degree,
        completion_groups=residual_groups,
        source_id=f"canonical-affine-residual-q{q}-U{int(cutoff)}",
        parent_masks=(core.values, core.values, core.values, core.values),
    )
    components = residual_component_summary(residual_cells)
    if residual_cells:
        a4 = summarize_a4_unit_balances(residual_cells)
        residual_atoms = a4.term_count
        residual_a4 = a4.worst_upper_bound
    else:
        residual_atoms = 0
        residual_a4 = Fraction(0)
    expected_atoms = sum(
        len(completions) * (len(completions) - 1)
        for completions in residual_groups.values()
    )
    if residual_atoms != expected_atoms:
        raise AssertionError("residual A2 lost a factorial atom")
    if any(len(completions) > 2 for completions in residual_groups.values()):
        raise AssertionError("the canonical line/plane peel left three points")

    answer = FixtureSummary(
        q=q,
        cutoff=int(cutoff),
        degree=degree,
        shell_nodes=core.dimension,
        rectangles=len(rectangles),
        color_fibres=len(groups),
        maximum_multiplicity=max(map(len, groups.values()), default=0),
        direct_completion_mass=sum(map(len, groups.values())),
        line_patches=sum(patch.kind == "line" for patch in patches),
        plane_patches=sum(patch.kind == "plane" for patch in patches),
        affine_completion_mass=sum(len(patch.completions) for patch in patches),
        residual_completion_mass=sum(map(len, residual_groups.values())),
        h_aff=carleson.maximum_color_load,
        maximum_h_aff_color=maximum_h_aff_color,
        maximum_affine_patch_reuse_per_color=max(
            (len(values) for values in color_patch_ids.values()), default=0
        ),
        maximum_affine_geometry_reuse_per_color=max(
            (len(values) for values in color_geometry.values()), default=0
        ),
        maximum_source_directions_per_color=source_direction_max,
        maximum_source_direction_color=maximum_source_direction_color,
        maximum_residual_directions_per_color=residual_direction_max,
        maximum_residual_direction_color=maximum_residual_direction_color,
        source_factorial_atoms=source_factorial_atoms,
        residual_factorial_atoms=residual_atoms,
        residual_cells=len(residual_cells),
        residual_components=components.component_count,
        maximum_component_vertices=components.maximum_vertices,
        maximum_component_atom_edges=components.maximum_atom_edges,
        maximum_component_cycle_rank=components.maximum_cycle_rank,
        maximum_component_degree_product=components.maximum_component_degree_product,
        residual_a4=residual_a4,
    )
    del residual_cells, profiles, patches, residual_groups, groups, rectangles, core
    gc.collect()
    return answer


def main() -> None:
    summaries = tuple(analyze_fixture(q, cutoff) for q, cutoff in FIXTURES)
    violations = tuple(
        summary
        for summary in summaries
        if summary.maximum_component_degree_product > summary.degree**2
        or summary.residual_a4 > summary.degree**2
    )
    print("PASS growing canonical affine-peel diagnostic")
    print(
        "q U D nodes rect fibres mmax direct line plane aff residual "
        "Haff Hcolor H/D patchreuse geomreuse srcdirs srccolor resdirs rescolor sourceatoms residualatoms cells comps "
        "compV compE cycl degprod degprod/D2 A4 A4/D2"
    )
    for value in summaries:
        print(
            value.q,
            value.cutoff,
            value.degree,
            value.shell_nodes,
            value.rectangles,
            value.color_fibres,
            value.maximum_multiplicity,
            value.direct_completion_mass,
            value.line_patches,
            value.plane_patches,
            value.affine_completion_mass,
            value.residual_completion_mass,
            value.h_aff,
            value.maximum_h_aff_color,
            f"{value.h_aff / value.degree:.9g}",
            value.maximum_affine_patch_reuse_per_color,
            value.maximum_affine_geometry_reuse_per_color,
            value.maximum_source_directions_per_color,
            value.maximum_source_direction_color,
            value.maximum_residual_directions_per_color,
            value.maximum_residual_direction_color,
            value.source_factorial_atoms,
            value.residual_factorial_atoms,
            value.residual_cells,
            value.residual_components,
            value.maximum_component_vertices,
            value.maximum_component_atom_edges,
            value.maximum_component_cycle_rank,
            value.maximum_component_degree_product,
            f"{value.maximum_component_degree_product / value.degree**2:.9g}",
            value.residual_a4,
            f"{float(value.residual_a4 / value.degree**2):.9g}",
        )
    print(
        "kill tests: "
        f"component_or_A4_violations={len(violations)}, "
        f"max_Haff_over_D={max(value.h_aff / value.degree for value in summaries):.9g}, "
        f"max_residual_direction_reuse={max(value.maximum_residual_directions_per_color for value in summaries)}"
    )


if __name__ == "__main__":
    main()
