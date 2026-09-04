#!/usr/bin/env python3
"""Adversarial LPs for gap-weighted consecutive-residue coherence.

The important normalization is that an atom ``x[a,b,g]`` is *event count
divided by the physical shell length*.  Its contribution to logarithmic gap
mass is therefore ``g*x[a,b,g]``.  Classical prime-in-progressions input can
make the unweighted endpoint marginals of ``x`` uniform without making the
gap-weighted endpoint marginals uniform.  Keeping those two objects separate
is the main purpose of this module.

The finite LP is a falsification and theorem-design tool.  It does not assert
that an optimizer is realized by the actual primes.  Every returned solution
is checked against the assembled primal constraints.  SciPy/HiGHS is used
when available; a small exact vertex enumerator is supplied for dependency-
free test cases.
"""

from __future__ import annotations

import argparse
import cmath
import itertools
import json
import math
from dataclasses import dataclass, replace
from fractions import Fraction
from typing import Iterable, Sequence


Rational = Fraction | int


def _fraction(value: Rational) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def _units(modulus: int) -> tuple[int, ...]:
    if modulus < 2:
        raise ValueError("a modulus must be at least two")
    return tuple(value for value in range(modulus) if math.gcd(value, modulus) == 1)


@dataclass(frozen=True)
class BlockSpec:
    """One physical block and its selected reduced rational frequency."""

    name: str
    q: int
    r: int
    mass: Fraction
    count: Fraction
    phase: float = 0.0

    def __post_init__(self) -> None:
        if self.q < 2 or math.gcd(self.r, self.q) != 1:
            raise ValueError("(r,q) must be a reduced rational with q >= 2")
        if self.mass <= 0 or self.count <= 0:
            raise ValueError("block mass and count must be positive")


@dataclass(frozen=True)
class TailBound:
    """A bound on ``sum_(g>=threshold) g*x`` over all blocks."""

    threshold: int
    cap: Fraction


@dataclass(frozen=True)
class MomentBound:
    """A bound on ``sum g**order*x`` over all blocks."""

    order: int
    cap: Fraction

    def __post_init__(self) -> None:
        if self.order < 1:
            raise ValueError("moment order must be positive")


@dataclass(frozen=True)
class CauchyClassBound:
    """Local count/second-moment data for one congruence or sieve stage.

    The class selects atoms whose gaps lie in ``remainder (mod modulus)``.
    ``mass`` optionally records an exact full-period identity.  The two upper
    bounds imply, without any probabilistic assumption,

    ``|sum_class g*x*z_atom| <= sqrt(count_cap*second_moment_cap)``

    whenever ``|z_atom|<=1``.  A true least-prime-factor deletion stage can
    be fed to this abstraction after its atoms have been identified; mere
    endpoint wheel admissibility is deliberately not treated as that input.
    """

    name: str
    modulus: int
    remainder: int
    count_cap: Fraction
    second_moment_cap: Fraction
    mass: Fraction | None = None
    block_names: tuple[str, ...] | None = None

    def __post_init__(self) -> None:
        if self.modulus < 1:
            raise ValueError("class modulus must be positive")
        if self.count_cap < 0 or self.second_moment_cap < 0:
            raise ValueError("class caps must be nonnegative")


@dataclass(frozen=True)
class ConstraintSet:
    """Toggle the progressively stronger families of constraints."""

    block_count: bool = True
    block_mass: bool = True
    uniform_count_marginals: bool = False
    physical_gap_congruence: bool = False
    wheel_admissibility: bool = False
    consecutive_wheel_survivors: bool = False
    uniform_wheel_count_marginals: bool = False
    gt_tails: bool = False
    moments: bool = False
    cauchy_classes: bool = False
    weighted_uniform_marginals: bool = False
    # This means 1/2*(row l1 discrepancy + column l1 discrepancy) <= budget.
    weighted_marginal_l1_budget: Fraction | None = None


@dataclass(frozen=True)
class Atom:
    """A possible transition carrying normalized event count."""

    block: int
    a: int
    b: int
    gap: int
    wheel_left: int | None
    wheel_right: int | None


@dataclass(frozen=True)
class SparseRow:
    coefficients: dict[int, Fraction]
    rhs: Fraction
    name: str


@dataclass(frozen=True)
class LPProblem:
    blocks: tuple[BlockSpec, ...]
    atoms: tuple[Atom, ...]
    variable_names: tuple[str, ...]
    objective: tuple[complex, ...]
    equalities: tuple[SparseRow, ...]
    inequalities: tuple[SparseRow, ...]
    flags: ConstraintSet
    cauchy_classes: tuple[CauchyClassBound, ...] = ()

    @property
    def atom_count(self) -> int:
        return len(self.atoms)

    @property
    def variable_count(self) -> int:
        return len(self.variable_names)

    @property
    def total_mass(self) -> float:
        return float(sum((block.mass for block in self.blocks), Fraction()))


@dataclass(frozen=True)
class LPSolution:
    success: bool
    status: str
    values: tuple[float, ...]
    objective_projection: float
    objective_complex: complex
    projection_phase: float
    equality_residual: float
    inequality_violation: float
    negativity_violation: float
    exact_values: tuple[Fraction, ...] | None = None


@dataclass(frozen=True)
class ModulusSweep:
    solution: LPSolution
    certified_lower_bound: float
    grid_lipschitz_upper_bound: float
    phase_count: int


@dataclass(frozen=True)
class StageExponentFrontier:
    """Exact max-plus frontier from q-stage count plus the GT gap tail."""

    denominator_exponent: Fraction
    extremal_gap_exponent: Fraction
    forced_saving: Fraction
    gap_square_exponent: Fraction
    gap_third_exponent: Fraction


def gt_tail_saving(gap_exponent: Rational) -> Fraction:
    """The audited local Gafni--Tao saving ``9/13*(h-2/15)``."""

    exponent = _fraction(gap_exponent)
    if exponent < Fraction(2, 15):
        raise ValueError("the power-saving GT branch starts at 2/15")
    return Fraction(9, 13) * (exponent - Fraction(2, 15))


def accessible_stage_frontier(denominator_exponent: Rational) -> StageExponentFrontier:
    """Optimize the known positive q-stage count/tail package.

    If ``N_q/Y <= Y^-b`` and the gap mass above ``Y^h`` is at most
    ``Y^-s(h)``, splitting at ``h`` gives

    ``mass <= Y^(-min(b-h,s(h)))``.

    On the current GT branch the optimum is the exact crossing returned
    here.  A one-scale allocation at that crossing also obeys the displayed
    square/third-moment exponents, so those global known moments cannot
    improve this positive-information frontier.
    """

    b = _fraction(denominator_exponent)
    if b <= Fraction(2, 15):
        raise ValueError("denominator exponent must exceed 2/15")
    gap = (13 * b + Fraction(6, 5)) / 22
    saving = b - gap
    if saving != gt_tail_saving(gap):
        raise AssertionError("stage frontier algebra")
    return StageExponentFrontier(
        denominator_exponent=b,
        extremal_gap_exponent=gap,
        forced_saving=saving,
        gap_square_exponent=1 - b + 2 * gap,
        gap_third_exponent=1 - b + 3 * gap,
    )


def required_stage_second_moment_excess(
    denominator_exponent: Rational, target_saving: Rational
) -> Fraction:
    """Largest ``rho`` for which ``sum G^2 <= Y^(1+rho)`` closes.

    With stage count ``N/Y <= Y^-b``, Cauchy saves ``(b-rho)/2``.
    A strict target saving ``kappa`` therefore requires
    ``rho < b-2*kappa``; the returned value is that strict frontier.
    """

    return _fraction(denominator_exponent) - 2 * _fraction(target_saving)


def _add_term(row: dict[int, Fraction], index: int, value: Rational) -> None:
    coefficient = _fraction(value)
    if not coefficient:
        return
    row[index] = row.get(index, Fraction()) + coefficient
    if not row[index]:
        del row[index]


def build_problem(
    blocks: Sequence[BlockSpec],
    gaps: Sequence[int],
    *,
    flags: ConstraintSet,
    wheel: int = 30,
    tail_bounds: Sequence[TailBound] = (),
    moment_bounds: Sequence[MomentBound] = (),
    cauchy_classes: Sequence[CauchyClassBound] = (),
) -> LPProblem:
    """Assemble the finite transition LP.

    ``x`` is normalized transition count, not gap mass.  Thus block count is
    ``sum x``, block mass is ``sum g*x``, and the selected symmetrized DFT is
    ``sum g*x*(e_q(ra)+e_q(rb))/2``.
    """

    blocks = tuple(blocks)
    cauchy_classes = tuple(cauchy_classes)
    gaps = tuple(sorted(set(int(gap) for gap in gaps)))
    if not blocks or not gaps or gaps[0] <= 0:
        raise ValueError("at least one block and positive gap are required")
    if flags.uniform_count_marginals and not flags.block_count:
        raise ValueError("uniform count marginals require fixed block counts")
    if flags.uniform_wheel_count_marginals and not flags.wheel_admissibility:
        raise ValueError("uniform wheel marginals require wheel admissibility")
    if flags.consecutive_wheel_survivors and not flags.wheel_admissibility:
        raise ValueError("consecutive wheel survivors require wheel admissibility")
    if flags.weighted_uniform_marginals and not flags.block_mass:
        raise ValueError("weighted uniform marginals require fixed block masses")
    if flags.weighted_marginal_l1_budget is not None and not flags.block_mass:
        raise ValueError("weighted l1 control requires fixed block masses")
    if flags.wheel_admissibility and wheel < 2:
        raise ValueError("wheel must be at least two")

    atoms: list[Atom] = []
    for block_index, block in enumerate(blocks):
        q_states = _units(block.q)
        if flags.wheel_admissibility:
            if math.gcd(block.q, wheel) != 1:
                raise ValueError("the finite CRT model requires gcd(q,wheel)=1")
            wheel_states: tuple[int | None, ...] = _units(wheel)
        else:
            wheel_states = (None,)

        for gap in gaps:
            for a in q_states:
                if flags.physical_gap_congruence:
                    candidate_b = (a + gap) % block.q
                    b_states = (candidate_b,) if math.gcd(candidate_b, block.q) == 1 else ()
                else:
                    b_states = q_states
                for b in b_states:
                    for left in wheel_states:
                        if left is None:
                            right = None
                        else:
                            right = (left + gap) % wheel
                            if math.gcd(right, wheel) != 1:
                                continue
                            if flags.consecutive_wheel_survivors and any(
                                math.gcd(left + step, wheel) == 1
                                for step in range(1, gap)
                            ):
                                continue
                        atoms.append(Atom(block_index, a, b, gap, left, right))

    if not atoms:
        raise ValueError("no admissible transition atoms")

    variable_names = [
        f"x[{atom.block},{atom.a},{atom.b},{atom.gap},{atom.wheel_left}]"
        for atom in atoms
    ]
    objective: list[complex] = []
    for atom in atoms:
        block = blocks[atom.block]
        left = cmath.exp(2j * math.pi * block.r * atom.a / block.q)
        right = cmath.exp(2j * math.pi * block.r * atom.b / block.q)
        objective.append(
            atom.gap * (left + right) / 2 * cmath.exp(1j * block.phase)
        )

    equalities: list[SparseRow] = []
    inequalities: list[SparseRow] = []

    by_block: list[list[int]] = [[] for _ in blocks]
    for index, atom in enumerate(atoms):
        by_block[atom.block].append(index)

    for block_index, block in enumerate(blocks):
        indices = by_block[block_index]
        q_states = _units(block.q)
        if flags.block_count:
            equalities.append(
                SparseRow({index: Fraction(1) for index in indices}, block.count,
                          f"block_count[{block.name}]")
            )
        if flags.block_mass:
            equalities.append(
                SparseRow({index: Fraction(atoms[index].gap) for index in indices},
                          block.mass, f"block_mass[{block.name}]")
            )
        if flags.uniform_count_marginals:
            marginal = block.count / len(q_states)
            for state in q_states:
                equalities.append(
                    SparseRow(
                        {index: Fraction(1) for index in indices if atoms[index].a == state},
                        marginal,
                        f"count_row[{block.name},{state}]",
                    )
                )
                equalities.append(
                    SparseRow(
                        {index: Fraction(1) for index in indices if atoms[index].b == state},
                        marginal,
                        f"count_col[{block.name},{state}]",
                    )
                )
        if flags.uniform_wheel_count_marginals:
            wheel_states = _units(wheel)
            marginal = block.count / len(wheel_states)
            for state in wheel_states:
                equalities.append(
                    SparseRow(
                        {index: Fraction(1) for index in indices
                         if atoms[index].wheel_left == state},
                        marginal,
                        f"wheel_row[{block.name},{state}]",
                    )
                )
                equalities.append(
                    SparseRow(
                        {index: Fraction(1) for index in indices
                         if atoms[index].wheel_right == state},
                        marginal,
                        f"wheel_col[{block.name},{state}]",
                    )
                )
        if flags.weighted_uniform_marginals:
            marginal = block.mass / len(q_states)
            for state in q_states:
                equalities.append(
                    SparseRow(
                        {index: Fraction(atoms[index].gap) for index in indices
                         if atoms[index].a == state},
                        marginal,
                        f"weighted_row[{block.name},{state}]",
                    )
                )
                equalities.append(
                    SparseRow(
                        {index: Fraction(atoms[index].gap) for index in indices
                         if atoms[index].b == state},
                        marginal,
                        f"weighted_col[{block.name},{state}]",
                    )
                )

    if flags.gt_tails:
        for bound in tail_bounds:
            row = {
                index: Fraction(atom.gap)
                for index, atom in enumerate(atoms)
                if atom.gap >= bound.threshold
            }
            inequalities.append(SparseRow(row, bound.cap, f"tail[{bound.threshold}]") )

    if flags.moments:
        for bound in moment_bounds:
            row = {
                index: Fraction(atom.gap**bound.order)
                for index, atom in enumerate(atoms)
            }
            inequalities.append(SparseRow(row, bound.cap, f"moment[{bound.order}]") )

    if flags.cauchy_classes:
        block_lookup = {block.name: index for index, block in enumerate(blocks)}
        for stage in cauchy_classes:
            if stage.block_names is None:
                selected_blocks = set(range(len(blocks)))
            else:
                unknown = set(stage.block_names) - set(block_lookup)
                if unknown:
                    raise ValueError(f"unknown class blocks: {sorted(unknown)}")
                selected_blocks = {block_lookup[name] for name in stage.block_names}
            selected = [
                (index, atom)
                for index, atom in enumerate(atoms)
                if atom.block in selected_blocks
                and atom.gap % stage.modulus == stage.remainder % stage.modulus
            ]
            inequalities.append(
                SparseRow(
                    {index: Fraction(1) for index, _ in selected},
                    stage.count_cap,
                    f"class_count[{stage.name}]",
                )
            )
            inequalities.append(
                SparseRow(
                    {index: Fraction(atom.gap**2) for index, atom in selected},
                    stage.second_moment_cap,
                    f"class_second_moment[{stage.name}]",
                )
            )
            if stage.mass is not None:
                equalities.append(
                    SparseRow(
                        {index: Fraction(atom.gap) for index, atom in selected},
                        stage.mass,
                        f"class_mass[{stage.name}]",
                    )
                )

    # Optional exact formulation of the missing weighted-marginal theorem.
    if flags.weighted_marginal_l1_budget is not None:
        discrepancy_indices: list[int] = []
        for block_index, block in enumerate(blocks):
            indices = by_block[block_index]
            q_states = _units(block.q)
            center = block.mass / len(q_states)
            for side in ("row", "col"):
                for state in q_states:
                    aux_index = len(variable_names)
                    variable_names.append(f"d[{block.name},{side},{state}]")
                    objective.append(0j)
                    discrepancy_indices.append(aux_index)
                    positive: dict[int, Fraction] = {}
                    negative: dict[int, Fraction] = {}
                    for index in indices:
                        atom = atoms[index]
                        endpoint = atom.a if side == "row" else atom.b
                        if endpoint == state:
                            _add_term(positive, index, atom.gap)
                            _add_term(negative, index, -atom.gap)
                    _add_term(positive, aux_index, -1)
                    _add_term(negative, aux_index, -1)
                    inequalities.append(
                        SparseRow(positive, center, f"l1_plus[{block.name},{side},{state}]")
                    )
                    inequalities.append(
                        SparseRow(negative, -center, f"l1_minus[{block.name},{side},{state}]")
                    )
        inequalities.append(
            SparseRow(
                {index: Fraction(1) for index in discrepancy_indices},
                2 * flags.weighted_marginal_l1_budget,
                "weighted_marginal_half_l1",
            )
        )

    return LPProblem(
        blocks=blocks,
        atoms=tuple(atoms),
        variable_names=tuple(variable_names),
        objective=tuple(objective),
        equalities=tuple(equalities),
        inequalities=tuple(inequalities),
        flags=flags,
        cauchy_classes=cauchy_classes,
    )


def _dot(row: SparseRow, values: Sequence[float]) -> float:
    return sum(float(coefficient) * values[index]
               for index, coefficient in row.coefficients.items())


def verify_solution(problem: LPProblem, values: Sequence[float], *, tolerance: float = 2e-8) -> tuple[float, float, float]:
    """Return maximum equality, inequality, and nonnegativity violations."""

    if len(values) != problem.variable_count:
        raise ValueError("wrong solution dimension")
    equality = max(
        (abs(_dot(row, values) - float(row.rhs)) for row in problem.equalities),
        default=0.0,
    )
    inequality = max(
        (max(0.0, _dot(row, values) - float(row.rhs)) for row in problem.inequalities),
        default=0.0,
    )
    negativity = max((max(0.0, -value) for value in values), default=0.0)
    if max(equality, inequality, negativity) > tolerance:
        raise AssertionError(
            f"invalid LP certificate: eq={equality:g}, ub={inequality:g}, neg={negativity:g}"
        )
    return equality, inequality, negativity


def rationalize_feasible_solution(
    problem: LPProblem,
    solution: LPSolution,
    *,
    max_denominators: Sequence[int] = (10_000, 1_000_000, 100_000_000),
    zero_tolerance: float = 1e-10,
) -> LPSolution:
    """Recover and exactly verify a rational primal certificate.

    HiGHS vertices of this model are rational because every constraint is.
    This routine does not assume that decimal rounding preserved feasibility:
    it accepts a reconstruction only after replaying every equality and
    inequality with ``Fraction`` arithmetic.
    """

    if not solution.success:
        raise ValueError("a feasible numerical solution is required")
    for max_denominator in max_denominators:
        exact = tuple(
            Fraction(0)
            if abs(value) <= zero_tolerance
            else Fraction(value).limit_denominator(max_denominator)
            for value in solution.values
        )
        if any(value < 0 for value in exact):
            continue
        equality_ok = all(
            sum(
                coefficient * exact[index]
                for index, coefficient in row.coefficients.items()
            ) == row.rhs
            for row in problem.equalities
        )
        inequality_ok = all(
            sum(
                coefficient * exact[index]
                for index, coefficient in row.coefficients.items()
            ) <= row.rhs
            for row in problem.inequalities
        )
        if not equality_ok or not inequality_ok:
            continue
        values = tuple(float(value) for value in exact)
        residuals = verify_solution(problem, values, tolerance=2e-12)
        complex_value = sum(
            problem.objective[index] * values[index]
            for index in range(problem.variable_count)
        )
        projection = (
            cmath.exp(-1j * solution.projection_phase) * complex_value
        ).real
        return LPSolution(
            True,
            f"exact rational reconstruction (denominator <= {max_denominator})",
            values,
            projection,
            complex_value,
            solution.projection_phase,
            *residuals,
            exact_values=exact,
        )
    raise RuntimeError("no exact rational reconstruction passed all constraints")


def _projection_coefficients(problem: LPProblem, phase: float) -> list[float]:
    rotation = cmath.exp(-1j * phase)
    return [(rotation * coefficient).real for coefficient in problem.objective]


def _solve_scipy(problem: LPProblem, phase: float) -> LPSolution:
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import lil_matrix

    n = problem.variable_count

    def matrix(rows: Sequence[SparseRow]):
        out = lil_matrix((len(rows), n), dtype=float)
        for row_index, row in enumerate(rows):
            for column, value in row.coefficients.items():
                out[row_index, column] = float(value)
        return out.tocsr()

    coefficients = np.asarray(_projection_coefficients(problem, phase))
    result = linprog(
        -coefficients,
        A_ub=matrix(problem.inequalities) if problem.inequalities else None,
        b_ub=np.asarray([float(row.rhs) for row in problem.inequalities])
        if problem.inequalities else None,
        A_eq=matrix(problem.equalities) if problem.equalities else None,
        b_eq=np.asarray([float(row.rhs) for row in problem.equalities])
        if problem.equalities else None,
        bounds=(0.0, None),
        method="highs",
    )
    if not result.success:
        return LPSolution(
            False, str(result.message), (), float("nan"), complex(float("nan")),
            phase, float("inf"), float("inf"), float("inf"), None,
        )
    values = tuple(float(value) for value in result.x)
    residuals = verify_solution(problem, values)
    complex_value = sum(
        problem.objective[index] * values[index] for index in range(n)
    )
    projection = (cmath.exp(-1j * phase) * complex_value).real
    if abs(projection + float(result.fun)) > 2e-7:
        raise AssertionError("objective replay mismatch")
    return LPSolution(
        True,
        str(result.message),
        values,
        projection,
        complex_value,
        phase,
        *residuals,
        exact_values=None,
    )


def _rref(rows: Sequence[tuple[list[Fraction], Fraction]], n: int) -> tuple[list[tuple[list[Fraction], Fraction]], bool]:
    matrix = [[*coefficients, rhs] for coefficients, rhs in rows]
    pivot_row = 0
    for column in range(n):
        pivot = next((row for row in range(pivot_row, len(matrix))
                      if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [matrix[row][j] - factor * matrix[pivot_row][j]
                           for j in range(n + 1)]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    for row in matrix:
        if not any(row[:n]) and row[n]:
            return [], False
    independent = [
        (row[:n], row[n]) for row in matrix if any(row[:n])
    ]
    return independent, True


def _dense_row(row: SparseRow, n: int) -> list[Fraction]:
    out = [Fraction() for _ in range(n)]
    for index, coefficient in row.coefficients.items():
        out[index] = coefficient
    return out


def _solve_square_exact(rows: Sequence[tuple[list[Fraction], Fraction]], n: int) -> tuple[Fraction, ...] | None:
    reduced, consistent = _rref(rows, n)
    if not consistent or len(reduced) != n:
        return None
    answer = [Fraction() for _ in range(n)]
    for coefficients, rhs in reduced:
        pivot = next(index for index, value in enumerate(coefficients) if value)
        answer[pivot] = rhs
    return tuple(answer)


def _solve_exact_vertex(problem: LPProblem, phase: float, *, combination_limit: int = 250_000) -> LPSolution:
    """Dependency-free exact feasibility/vertex solver for tiny LPs."""

    n = problem.variable_count
    equality_rows = [(_dense_row(row, n), row.rhs) for row in problem.equalities]
    independent, consistent = _rref(equality_rows, n)
    if not consistent:
        return LPSolution(False, "inconsistent equalities", (), float("nan"),
                          complex(float("nan")), phase, float("inf"),
                          float("inf"), float("inf"), None)
    rank = len(independent)
    active_needed = n - rank
    candidates: list[tuple[list[Fraction], Fraction]] = [
        (_dense_row(row, n), row.rhs) for row in problem.inequalities
    ]
    # Nonnegativity inequalities become x_j=0 when active.
    for index in range(n):
        coefficients = [Fraction() for _ in range(n)]
        coefficients[index] = 1
        candidates.append((coefficients, Fraction()))
    number = math.comb(len(candidates), active_needed)
    if n > 12 or number > combination_limit:
        raise RuntimeError(
            "SciPy is unavailable and the exact fallback is intentionally limited "
            f"to tiny LPs (n={n}, active combinations={number})"
        )

    projection = _projection_coefficients(problem, phase)
    best: tuple[Fraction, ...] | None = None
    best_value = -math.inf
    for selected in itertools.combinations(candidates, active_needed):
        solution = _solve_square_exact([*independent, *selected], n)
        if solution is None or any(value < 0 for value in solution):
            continue
        if any(
            sum(coefficient * solution[index]
                for index, coefficient in enumerate(coefficients)) > rhs
            for coefficients, rhs in candidates[: len(problem.inequalities)]
        ):
            continue
        value = sum(projection[index] * float(solution[index]) for index in range(n))
        if value > best_value:
            best_value = value
            best = solution
    if best is None:
        return LPSolution(False, "no feasible vertex", (), float("nan"),
                          complex(float("nan")), phase, float("inf"),
                          float("inf"), float("inf"), None)
    values = tuple(float(value) for value in best)
    residuals = verify_solution(problem, values, tolerance=1e-12)
    complex_value = sum(problem.objective[index] * values[index] for index in range(n))
    return LPSolution(
        True, "exact vertex enumeration", values, best_value, complex_value,
        phase, *residuals, exact_values=best,
    )


def solve_projection(
    problem: LPProblem,
    phase: float = 0.0,
    *,
    force_exact_fallback: bool = False,
) -> LPSolution:
    """Maximize ``Re(exp(-i*phase) A)`` for the selected symmetrized DFT."""

    if not force_exact_fallback:
        try:
            return _solve_scipy(problem, phase)
        except ImportError:
            pass
    return _solve_exact_vertex(problem, phase)


def maximize_modulus(problem: LPProblem, *, phase_count: int = 72) -> ModulusSweep:
    """Sweep support directions and bracket the maximum DFT modulus.

    The optimizer at every sampled direction is a feasible lower certificate.
    The support function is ``total_mass``-Lipschitz, giving the displayed
    finite-grid upper bound.  Increasing ``phase_count`` sharpens the bracket.
    """

    if phase_count < 4:
        raise ValueError("phase_count must be at least four")
    solutions = [
        solve_projection(problem, 2 * math.pi * index / phase_count)
        for index in range(phase_count)
    ]
    if not all(solution.success for solution in solutions):
        failed = next(solution for solution in solutions if not solution.success)
        raise RuntimeError(failed.status)
    best = max(solutions, key=lambda solution: abs(solution.objective_complex))
    max_support = max(solution.objective_projection for solution in solutions)
    lower = abs(best.objective_complex)
    upper = max(lower, max_support + problem.total_mass * math.pi / phase_count)
    return ModulusSweep(best, lower, upper, phase_count)


def weighted_endpoint_discrepancy(problem: LPProblem, solution: LPSolution) -> dict[str, float]:
    """Replay the exact weighted-marginal lemma on a feasible solution."""

    if not solution.success:
        raise ValueError("a feasible solution is required")
    values = solution.values
    row_l1 = 0.0
    column_l1 = 0.0
    principal = 0j
    for block_index, block in enumerate(problem.blocks):
        states = _units(block.q)
        center = float(block.mass / len(states))
        row = {state: 0.0 for state in states}
        column = {state: 0.0 for state in states}
        for index, atom in enumerate(problem.atoms):
            if atom.block != block_index:
                continue
            mass = atom.gap * values[index]
            row[atom.a] += mass
            column[atom.b] += mass
        row_l1 += sum(abs(value - center) for value in row.values())
        column_l1 += sum(abs(value - center) for value in column.values())
        phase_sum = sum(
            cmath.exp(2j * math.pi * block.r * state / block.q)
            for state in states
        )
        principal += (
            cmath.exp(1j * block.phase) * center * phase_sum
        )
    half_l1 = (row_l1 + column_l1) / 2
    if abs(solution.objective_complex) > abs(principal) + half_l1 + 3e-8:
        raise AssertionError("weighted-marginal inequality replay failed")
    return {
        "row_l1": row_l1,
        "column_l1": column_l1,
        "half_l1": half_l1,
        "principal_modulus": abs(principal),
        "dft_modulus": abs(solution.objective_complex),
        "lemma_upper_bound": abs(principal) + half_l1,
    }


def cauchy_class_certificates(problem: LPProblem, solution: LPSolution) -> list[dict[str, float | str]]:
    """Replay every local count/second-moment Cauchy certificate."""

    if not solution.success:
        raise ValueError("a feasible solution is required")
    block_lookup = {block.name: index for index, block in enumerate(problem.blocks)}
    certificates: list[dict[str, float | str]] = []
    for stage in problem.cauchy_classes:
        selected_blocks = (
            set(range(len(problem.blocks)))
            if stage.block_names is None
            else {block_lookup[name] for name in stage.block_names}
        )
        indices = [
            index for index, atom in enumerate(problem.atoms)
            if atom.block in selected_blocks
            and atom.gap % stage.modulus == stage.remainder % stage.modulus
        ]
        count = sum(solution.values[index] for index in indices)
        second_moment = sum(
            problem.atoms[index].gap**2 * solution.values[index] for index in indices
        )
        mass = sum(
            problem.atoms[index].gap * solution.values[index] for index in indices
        )
        dft = sum(
            problem.objective[index] * solution.values[index] for index in indices
        )
        empirical_bound = math.sqrt(max(0.0, count * second_moment))
        cap_bound = math.sqrt(float(stage.count_cap * stage.second_moment_cap))
        if abs(dft) > empirical_bound + 3e-8 or empirical_bound > cap_bound + 3e-8:
            raise AssertionError("class Cauchy certificate failed")
        certificates.append(
            {
                "name": stage.name,
                "count": count,
                "mass": mass,
                "second_moment": second_moment,
                "dft_modulus": abs(dft),
                "empirical_cauchy_bound": empirical_bound,
                "cap_cauchy_bound": cap_bound,
            }
        )
    return certificates


def atom_support(problem: LPProblem, solution: LPSolution, *, tolerance: float = 1e-9) -> list[dict[str, float | int | None | str]]:
    """Return nonzero physical atoms, sorted by gap-mass contribution."""

    support = []
    for index, atom in enumerate(problem.atoms):
        value = solution.values[index]
        if value <= tolerance:
            continue
        support.append(
            {
                "block": problem.blocks[atom.block].name,
                "a": atom.a,
                "b": atom.b,
                "gap": atom.gap,
                "wheel_left": atom.wheel_left,
                "wheel_right": atom.wheel_right,
                "count": value,
                "gap_mass": atom.gap * value,
            }
        )
    support.sort(key=lambda item: -float(item["gap_mass"]))
    return support


# ---------- Exact one-height rational-cell enumeration ----------


@dataclass(frozen=True)
class RationalCell:
    r: int
    q: int
    radius: Fraction

    def __post_init__(self) -> None:
        if self.q < 2 or math.gcd(self.r, self.q) != 1 or self.radius < 0:
            raise ValueError("invalid reduced rational cell")


@dataclass(frozen=True)
class HeightSelectorBlock:
    name: str
    slope: Fraction
    offset: Fraction
    cells: tuple[RationalCell, ...]

    def __post_init__(self) -> None:
        if self.slope <= 0 or not self.cells:
            raise ValueError("selector slope and cell family must be positive/nonempty")


@dataclass(frozen=True)
class CommonHeightSelector:
    cells: tuple[RationalCell, ...]
    lifts: tuple[int, ...]
    height_left: Fraction
    height_right: Fraction


def _floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def _ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def enumerate_common_height_selectors(
    blocks: Sequence[HeightSelectorBlock],
    height_left: Rational,
    height_right: Rational,
) -> tuple[CommonHeightSelector, ...]:
    """Enumerate exact selector tuples compatible with one real height.

    A cell is legal when

    ``|slope*t+offset-(lift+r/q)| <= radius``.

    This affine form is the rational core of the common-height incidence
    calculation; application-specific curvature maps can feed local affine
    enclosures into the same enumerator.
    """

    left = _fraction(height_left)
    right = _fraction(height_right)
    if left > right:
        raise ValueError("empty height interval")
    options: list[list[tuple[RationalCell, int, Fraction, Fraction]]] = []
    for block in blocks:
        block_options: list[tuple[RationalCell, int, Fraction, Fraction]] = []
        image_left = block.slope * left + block.offset
        image_right = block.slope * right + block.offset
        for cell in block.cells:
            center = Fraction(cell.r, cell.q)
            first_lift = _ceil_fraction(image_left - center - cell.radius)
            last_lift = _floor_fraction(image_right - center + cell.radius)
            for lift in range(first_lift, last_lift + 1):
                interval_left = (lift + center - cell.radius - block.offset) / block.slope
                interval_right = (lift + center + cell.radius - block.offset) / block.slope
                clipped_left = max(left, interval_left)
                clipped_right = min(right, interval_right)
                if clipped_left <= clipped_right:
                    block_options.append(
                        (cell, lift, clipped_left, clipped_right)
                    )
        options.append(block_options)

    selectors: list[CommonHeightSelector] = []
    for choice in itertools.product(*options):
        common_left = max(item[2] for item in choice)
        common_right = min(item[3] for item in choice)
        if common_left <= common_right:
            selectors.append(
                CommonHeightSelector(
                    tuple(item[0] for item in choice),
                    tuple(item[1] for item in choice),
                    common_left,
                    common_right,
                )
            )
    selectors.sort(
        key=lambda selector: (
            selector.height_left,
            selector.height_right,
            tuple((cell.q, cell.r) for cell in selector.cells),
            selector.lifts,
        )
    )
    return tuple(selectors)


def blocks_from_common_selector(
    selector: CommonHeightSelector,
    names: Sequence[str],
    masses: Sequence[Rational],
    counts: Sequence[Rational],
    phases: Sequence[float] | None = None,
) -> tuple[BlockSpec, ...]:
    """Instantiate LP blocks from one exact common-height selector."""

    size = len(selector.cells)
    if len(names) != size or len(masses) != size or len(counts) != size:
        raise ValueError("selector metadata has the wrong length")
    if phases is None:
        phases = (0.0,) * size
    if len(phases) != size:
        raise ValueError("selector phases have the wrong length")
    return tuple(
        BlockSpec(
            names[index],
            cell.q,
            cell.r,
            _fraction(masses[index]),
            _fraction(counts[index]),
            float(phases[index]),
        )
        for index, cell in enumerate(selector.cells)
    )


def _demo() -> dict[str, object]:
    """Run the deterministic finite adversarial progression used in tests."""

    block = BlockSpec("I0", 7, 1, Fraction(1), Fraction(1, 12))
    gaps = tuple(range(2, 43, 2))
    tail = (TailBound(14, Fraction(2, 5)),)
    moments = (MomentBound(2, Fraction(16)), MomentBound(3, Fraction(400)))
    stages = [
        ("normalization", ConstraintSet()),
        ("uniform-count", ConstraintSet(uniform_count_marginals=True)),
        ("physical", ConstraintSet(uniform_count_marginals=True,
                                    physical_gap_congruence=True)),
        ("wheel", ConstraintSet(uniform_count_marginals=True,
                                 physical_gap_congruence=True,
                                 wheel_admissibility=True,
                                 uniform_wheel_count_marginals=True)),
        ("GT", ConstraintSet(uniform_count_marginals=True,
                              physical_gap_congruence=True,
                              wheel_admissibility=True,
                              uniform_wheel_count_marginals=True,
                              gt_tails=True)),
        ("moments", ConstraintSet(uniform_count_marginals=True,
                                   physical_gap_congruence=True,
                                   wheel_admissibility=True,
                                   uniform_wheel_count_marginals=True,
                                   gt_tails=True,
                                   moments=True)),
    ]
    output: dict[str, object] = {"stages": []}
    final_problem = None
    final_solution = None
    for name, flags in stages:
        problem = build_problem((block,), gaps, flags=flags,
                                tail_bounds=tail, moment_bounds=moments)
        solution = solve_projection(problem)
        if not solution.success:
            raise RuntimeError(f"{name}: {solution.status}")
        output["stages"].append(
            {
                "name": name,
                "variables": problem.variable_count,
                "projection": solution.objective_projection,
                "modulus": abs(solution.objective_complex),
                "weighted_half_l1": weighted_endpoint_discrepancy(problem, solution)["half_l1"],
            }
        )
        final_problem, final_solution = problem, solution
    assert final_problem is not None and final_solution is not None
    output["extremizer"] = atom_support(final_problem, final_solution)[:16]

    weighted_flags = replace(stages[-1][1], weighted_uniform_marginals=True)
    weighted_problem = build_problem((block,), gaps, flags=weighted_flags,
                                     tail_bounds=tail, moment_bounds=moments)
    weighted_solution = solve_projection(weighted_problem)
    if not weighted_solution.success:
        raise RuntimeError(weighted_solution.status)
    output["weighted_uniform"] = {
        "projection": weighted_solution.objective_projection,
        "modulus": abs(weighted_solution.objective_complex),
        **weighted_endpoint_discrepancy(weighted_problem, weighted_solution),
    }

    selectors = enumerate_common_height_selectors(
        (
            HeightSelectorBlock("I0", Fraction(1), Fraction(),
                                (RationalCell(1, 7, Fraction(1, 700)),)),
            HeightSelectorBlock("I1", Fraction(2), Fraction(),
                                (RationalCell(2, 7, Fraction(1, 350)),)),
        ),
        Fraction(1, 8),
        Fraction(1, 6),
    )
    output["common_height_selectors"] = [
        {
            "cells": [(cell.r, cell.q) for cell in selector.cells],
            "lifts": selector.lifts,
            "interval": (str(selector.height_left), str(selector.height_right)),
        }
        for selector in selectors
    ]
    selected_blocks = blocks_from_common_selector(
        selectors[0], ("I0", "I1"), (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(1, 24), Fraction(1, 24)),
    )
    common_problem = build_problem(
        selected_blocks,
        gaps,
        flags=stages[-1][1],
        tail_bounds=tail,
        moment_bounds=moments,
    )
    common_solution = solve_projection(common_problem)
    if not common_solution.success:
        raise RuntimeError(common_solution.status)
    output["common_height_lp"] = {
        "projection": common_solution.objective_projection,
        "modulus": abs(common_solution.objective_complex),
        "weighted_half_l1": weighted_endpoint_discrepancy(
            common_problem, common_solution
        )["half_l1"],
    }
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    args = parser.parse_args()
    print(json.dumps(_demo(), indent=None if args.compact else 2, sort_keys=True))


if __name__ == "__main__":
    main()
