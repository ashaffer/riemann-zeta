"""Finite Nevanlinna--Pick probes for phase-cell half-disk constraints.

The mathematical core is exact.  If ``K[i,j] = 1/(z[i] + conj(z[j]))``, a
value vector ``w`` is interpolated by a right-half-plane Schur function iff

    [[K, diag(w) K], [K diag(conj(w)), K]] >= 0.

This affine block LMI is just the Schur-complement form of the Pick matrix.
The SciPy routine below is only a floating-point probe of that finite SDP;
its output is not a proof or a certified SDP bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np
from numpy.typing import NDArray
from scipy.optimize import minimize
from scipy.linalg import solve_triangular


ComplexArray = NDArray[np.complex128]


def cauchy_kernel(nodes: Sequence[complex]) -> ComplexArray:
    """Return the right-half-plane Szego/Cauchy kernel matrix."""

    z = np.asarray(nodes, dtype=np.complex128)
    if z.ndim != 1 or len(z) == 0:
        raise ValueError("nodes must be a nonempty one-dimensional sequence")
    if np.any(z.real <= 0):
        raise ValueError("all nodes must lie in the open right half-plane")
    return 1.0 / (z[:, None] + z.conj()[None, :])


def pick_matrix(nodes: Sequence[complex], values: Sequence[complex]) -> ComplexArray:
    """Return the ordinary Pick matrix for the supplied node/value data."""

    z = np.asarray(nodes, dtype=np.complex128)
    w = np.asarray(values, dtype=np.complex128)
    if z.shape != w.shape:
        raise ValueError("nodes and values must have the same shape")
    kernel = cauchy_kernel(z)
    return kernel * (1.0 - w[:, None] * w.conj()[None, :])


def affine_pick_lmi(nodes: Sequence[complex], values: Sequence[complex]) -> ComplexArray:
    """Return the affine block LMI equivalent to Pick positivity."""

    w = np.asarray(values, dtype=np.complex128)
    kernel = cauchy_kernel(nodes)
    if w.shape != (len(kernel),):
        raise ValueError("nodes and values must have the same length")
    cross = w[:, None] * kernel
    return np.block([[kernel, cross], [cross.conj().T, kernel]])


def realify_hermitian(matrix: ComplexArray) -> NDArray[np.float64]:
    """Real symmetric representation preserving Hermitian eigenvalues twice."""

    matrix = np.asarray(matrix, dtype=np.complex128)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("matrix must be square")
    return np.block([[matrix.real, -matrix.imag], [matrix.imag, matrix.real]])


def phase_margins(values: Sequence[complex], phases: Sequence[float]) -> NDArray[np.float64]:
    """Return ``Re(exp(-i phase_j) value_j)`` for collateral values."""

    w = np.asarray(values, dtype=np.complex128)
    phi = np.asarray(phases, dtype=float)
    if w.shape != phi.shape:
        raise ValueError("values and phases must have the same shape")
    return np.real(np.exp(-1j * phi) * w)


def zero_blashke_target(target: complex, collateral: Sequence[complex]) -> float:
    """Target modulus of the Blaschke product vanishing at every collateral."""

    target = complex(target)
    if target.real <= 0:
        raise ValueError("target must lie in the open right half-plane")
    nodes = np.asarray(collateral, dtype=np.complex128)
    if np.any(nodes.real <= 0):
        raise ValueError("collateral nodes must lie in the open right half-plane")
    factors = np.abs((target - nodes) / (target + nodes.conj()))
    return float(np.prod(factors))


def odd_half_cell_configuration(
    scaled_depth: float,
    positive_indices: Iterable[int],
    *,
    jitter: Sequence[float] | None = None,
) -> tuple[ComplexArray, NDArray[np.float64]]:
    """Symmetric vertical-line nodes near odd half-cell phases.

    The normalization is ``D=1``.  For each nonnegative integer ``k`` the
    positive ordinate is ``(2*k+1)*pi + jitter[k]``; its reflected negative
    ordinate is also inserted.  Returned nodes use the report convention
    ``z=beta-i*delta`` and phases are ``delta``.
    """

    depth = float(scaled_depth)
    if depth <= 0:
        raise ValueError("scaled_depth must be positive")
    indices = tuple(int(k) for k in positive_indices)
    if any(k < 0 for k in indices) or len(set(indices)) != len(indices):
        raise ValueError("positive_indices must be distinct nonnegative integers")
    if jitter is None:
        offsets = np.zeros(len(indices), dtype=float)
    else:
        offsets = np.asarray(jitter, dtype=float)
        if offsets.shape != (len(indices),):
            raise ValueError("jitter must have one entry per positive index")
        if np.any(np.abs(offsets) >= np.pi):
            raise ValueError("each jitter must stay inside its phase cell")
    positive = np.array([(2 * k + 1) * np.pi for k in indices]) + offsets
    phases = np.concatenate((-positive[::-1], positive))
    nodes = depth - 1j * phases
    return nodes.astype(np.complex128), phases


def affine_jet_obstruction_data(
    alpha: float,
    length: float,
    cell_index: int,
    *,
    separation_ratio: float = 2.0 / 3.0,
) -> tuple[complex, ComplexArray, NDArray[np.float64], complex]:
    """Return the exact five-point affine-jet obstruction fixture.

    Here ``D=separation_ratio*length`` and the cell center obeys
    ``D*delta_c=(2*cell_index+1)*pi``.  The returned phases are reduced to
    ``pi+x_j``; these are equivalent to the physical phases modulo ``2*pi``.
    ``cell_center`` is returned for comparison with its squared Blaschke cost.
    """

    alpha = float(alpha)
    length = float(length)
    d = float(separation_ratio)
    if alpha <= 0 or length <= 0 or d <= 0:
        raise ValueError("alpha, length, and separation_ratio must be positive")
    offsets = np.array([-np.pi, -np.pi / 2, 0.0, np.pi / 2, np.pi])
    depths = np.array([1.0, 1.0, 1.0, 1.0, 8.0])
    delta_center = (2 * int(cell_index) + 1) * np.pi / (d * length)
    cell_center = alpha - 1j * delta_center
    nodes = alpha - depths / length - 1j * (
        delta_center + offsets / (d * length)
    )
    phases = np.pi + offsets
    return complex(alpha), nodes.astype(np.complex128), phases, complex(cell_center)


def affine_jet_normals(
    *, separation_ratio: float = 2.0 / 3.0
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """Return the five real affine-jet normals and their positive dependence."""

    d = float(separation_ratio)
    if d <= 0:
        raise ValueError("separation_ratio must be positive")
    offsets = np.array([-np.pi, -np.pi / 2, 0.0, np.pi / 2, np.pi])
    depths = np.array([1.0, 1.0, 1.0, 1.0, 8.0])
    cosine = np.cos(offsets)
    sine = np.sin(offsets)
    normals = np.column_stack(
        (
            cosine,
            sine,
            -depths * cosine - (offsets / d) * sine,
            (offsets / d) * cosine - depths * sine,
        )
    )
    weights = np.array([1.0, 14.0 / (3.0 * np.pi), 2.0, 14.0 / (3.0 * np.pi), 1.0])
    return normals, weights


def pseudohyperbolic_distance(left: complex, right: complex) -> float:
    """Right-half-plane pseudohyperbolic distance between two points."""

    left = complex(left)
    right = complex(right)
    if left.real <= 0 or right.real <= 0:
        raise ValueError("both points must lie in the open right half-plane")
    return float(abs((left - right) / (left + right.conjugate())))


def symmetric_opposite_pair_extremal(depth: float, ordinate: float) -> tuple[float, float]:
    """Exact half-disk optimum for the conjugate hostile pair.

    The nodes are ``depth +/- i*ordinate`` and both constraints are
    ``Re(w)<=0``.  The return value is ``(A_star,t_star)``.  With the nodes
    ordered as ``depth + i*ordinate, depth - i*ordinate``, their extremal
    values are ``-i*t_star, +i*t_star`` respectively.
    """

    x = float(depth)
    y = abs(float(ordinate))
    if x <= 0 or y <= 0:
        raise ValueError("depth and nonzero ordinate must be positive")
    radical = np.sqrt(4 * x**4 + 5 * x**2 * y**2 + y**4)
    t_star = (-2 * x**2 - y**2 + radical) / (x * y)
    numerator = y**2 + 2 * t_star * x * y - t_star**2 * (4 * x**2 + y**2)
    denominator = 4 * x**2 + y**2 + 2 * t_star * x * y - t_star**2 * y**2
    return float(numerator / denominator), float(t_star)


def alternating_lattice_inner(value: complex, depth: float) -> complex:
    """Half-density inner function for the exact alternating cell lattice.

    Its zeros on ``Re(s)=depth`` correspond to ordinates
    ``y=(4*k+1)*pi`` in the convention ``s=depth-i*y``.  The function is
    normalized to take a positive value at ``s=depth``.
    """

    a = float(depth)
    if a <= 0:
        raise ValueError("depth must be positive")
    s = complex(value)
    raw = np.sinh((s - a + 1j * np.pi) / 4) / np.sinh(
        (s + a + 1j * np.pi) / 4
    )
    raw_target = np.sinh(1j * np.pi / 4) / np.sinh(a / 2 + 1j * np.pi / 4)
    return complex(raw * np.exp(-1j * np.angle(raw_target)))


def alternating_lattice_configuration(
    depth: float, cell_indices: Iterable[int]
) -> tuple[ComplexArray, NDArray[np.float64]]:
    """One-node-per-cell data signed by ``alternating_lattice_inner``.

    Even cells use offset ``pi`` (and are zeros of the inner function);
    odd cells use offset zero and have a favorable positive real value.
    """

    a = float(depth)
    indices = np.asarray(tuple(int(j) for j in cell_indices), dtype=int)
    offsets = np.where(indices % 2 == 0, np.pi, 0.0)
    phases = 2 * np.pi * indices + offsets
    return (a - 1j * phases).astype(np.complex128), phases.astype(float)


def _unpack_variables(vector: NDArray[np.float64], count: int) -> ComplexArray:
    values = np.empty(count + 1, dtype=np.complex128)
    values[0] = vector[0]
    values[1:] = vector[1 : 1 + count] + 1j * vector[1 + count :]
    return values


@dataclass(frozen=True)
class PickProbeResult:
    """Uncertified floating-point result of the finite SDP probe."""

    target_amplitude: float
    values: ComplexArray
    min_lmi_eigenvalue: float
    min_phase_margin: float
    success: bool
    message: str
    iterations: int


@dataclass(frozen=True)
class PickBarrierResult:
    """Floating primal/dual bracket from the affine SDP log barrier.

    ``dual_upper_bound`` includes an l1 stationarity-residual correction,
    using the fact that every real SDP variable has modulus at most one.
    It is still a floating-point diagnostic, not an interval certificate.
    """

    target_amplitude: float
    dual_upper_bound: float
    duality_gap: float
    stationarity_l1: float
    values: ComplexArray
    min_lmi_eigenvalue: float
    min_phase_margin: float
    success: bool
    message: str
    iterations: int


def _normalized_lmi_basis(nodes: Sequence[complex]) -> tuple[ComplexArray, list[ComplexArray]]:
    """Return identity constant and affine bases after Cauchy congruence."""

    kernel = cauchy_kernel(nodes)
    count = len(kernel)
    cholesky = np.linalg.cholesky(kernel)
    bases: list[ComplexArray] = []
    # Variable order: real w_0, ..., real w_m, imag w_1, ..., imag w_m.
    row_specs = [(j, 1.0) for j in range(count)] + [(j, 1j) for j in range(1, count)]
    for row, scalar in row_specs:
        diagonal_times_l = np.zeros_like(cholesky)
        diagonal_times_l[row, :] = scalar * cholesky[row, :]
        transfer = solve_triangular(cholesky, diagonal_times_l, lower=True)
        basis = np.zeros((2 * count, 2 * count), dtype=np.complex128)
        basis[:count, count:] = transfer
        basis[count:, :count] = transfer.conj().T
        bases.append(basis)
    return np.eye(2 * count, dtype=np.complex128), bases


def probe_halfdisk_extremal_barrier(
    target: complex,
    collateral: Sequence[complex],
    phases: Sequence[float],
    *,
    final_barrier: float = 1e-5,
    barrier_ratio: float = 0.2,
    newton_tolerance: float = 2e-11,
    max_newton: int = 80,
) -> PickBarrierResult:
    """Probe the exact finite SDP with a primal--dual logarithmic barrier.

    The returned point is strictly primal feasible.  At barrier parameter
    ``mu``, ``Z=mu*M^{-1}`` and ``lambda=mu/h`` are positive dual variables.
    Newton stationarity therefore provides a numerical upper bound as well
    as a lower bound.  No claim of machine-certified rounding is made.
    """

    target = complex(target)
    nodes_c = np.asarray(collateral, dtype=np.complex128)
    phi = np.asarray(phases, dtype=float)
    if abs(target.imag) > 1e-15 or target.real <= 0:
        raise ValueError("the target must be a positive real node")
    if nodes_c.shape != phi.shape or nodes_c.ndim != 1:
        raise ValueError("collateral and phases must be one-dimensional and equally long")
    if not (0 < final_barrier < 1 and 0 < barrier_ratio < 1):
        raise ValueError("barrier parameters must lie strictly between zero and one")

    nodes = np.concatenate(([target], nodes_c))
    constant, bases = _normalized_lmi_basis(nodes)
    variable_count = len(bases)
    collateral_count = len(nodes_c)
    objective = np.zeros(variable_count, dtype=float)
    objective[0] = 1.0
    halfplanes = np.zeros((collateral_count, variable_count), dtype=float)
    for j, angle in enumerate(phi):
        halfplanes[j, 1 + j] = np.cos(angle)
        halfplanes[j, 1 + collateral_count + j] = np.sin(angle)

    # A small value pointing strictly into every requested half-disk is an
    # interior point.  Back off if roundoff sees the normalized LMI boundary.
    vector = np.zeros(variable_count, dtype=float)
    epsilon = 0.02
    vector[0] = epsilon
    vector[1 : 1 + collateral_count] = epsilon * np.cos(phi)
    vector[1 + collateral_count :] = epsilon * np.sin(phi)

    def matrix_at(point: NDArray[np.float64]) -> ComplexArray:
        matrix = constant.copy()
        for coefficient, basis in zip(point, bases):
            matrix += coefficient * basis
        return (matrix + matrix.conj().T) / 2

    while np.min(np.linalg.eigvalsh(matrix_at(vector))) <= 0:
        vector *= 0.5
    if collateral_count and np.min(halfplanes @ vector) <= 0:
        raise RuntimeError("failed to construct a strict half-plane interior point")

    total_iterations = 0
    mu = 0.1
    message = "barrier schedule completed"
    while True:
        for _ in range(max_newton):
            total_iterations += 1
            matrix = matrix_at(vector)
            margins = halfplanes @ vector
            inverse = np.linalg.inv(matrix)
            traces = np.array(
                [np.trace(inverse @ basis).real for basis in bases], dtype=float
            )
            gradient = -objective - mu * traces
            if collateral_count:
                gradient -= mu * (halfplanes.T @ (1.0 / margins))

            hessian = np.empty((variable_count, variable_count), dtype=float)
            inverse_bases = [inverse @ basis for basis in bases]
            for i in range(variable_count):
                for j in range(i + 1):
                    entry = mu * np.trace(inverse_bases[i] @ inverse_bases[j]).real
                    hessian[i, j] = entry
                    hessian[j, i] = entry
            if collateral_count:
                hessian += mu * (
                    halfplanes.T @ ((1.0 / margins**2)[:, None] * halfplanes)
                )
            try:
                step = np.linalg.solve(hessian, -gradient)
            except np.linalg.LinAlgError:
                step = np.linalg.lstsq(hessian, -gradient, rcond=1e-13)[0]
            decrement = float(-gradient @ step)
            if decrement / 2 <= newton_tolerance:
                break

            sign, logdet = np.linalg.slogdet(matrix)
            if sign <= 0:
                raise RuntimeError("lost positive definiteness on the central path")
            value = -objective @ vector - mu * logdet.real
            if collateral_count:
                value -= mu * np.sum(np.log(margins))
            scale = 1.0
            directional = float(gradient @ step)
            accepted = False
            while scale >= 2.0**-50:
                candidate = vector + scale * step
                candidate_margins = halfplanes @ candidate
                candidate_matrix = matrix_at(candidate)
                candidate_eigenvalue = float(np.min(np.linalg.eigvalsh(candidate_matrix)))
                if candidate_eigenvalue > 0 and (
                    not collateral_count or np.min(candidate_margins) > 0
                ):
                    candidate_sign, candidate_logdet = np.linalg.slogdet(candidate_matrix)
                    candidate_value = -objective @ candidate - mu * candidate_logdet.real
                    if collateral_count:
                        candidate_value -= mu * np.sum(np.log(candidate_margins))
                    if candidate_sign > 0 and candidate_value <= value + 0.01 * scale * directional:
                        vector = candidate
                        accepted = True
                        break
                scale *= 0.5
            if not accepted:
                message = "Newton line search stalled"
                break
        if mu <= final_barrier:
            break
        mu = max(final_barrier, mu * barrier_ratio)

    matrix = matrix_at(vector)
    margins = halfplanes @ vector
    inverse = np.linalg.inv(matrix)
    dual_matrix = mu * inverse
    dual_halfplanes = mu / margins if collateral_count else np.empty(0)
    dual_coefficients = np.array(
        [np.trace(dual_matrix @ basis).real for basis in bases], dtype=float
    )
    stationarity = objective + dual_coefficients
    if collateral_count:
        stationarity += halfplanes.T @ dual_halfplanes
    stationarity_l1 = float(np.sum(np.abs(stationarity)))
    dual_objective = float(np.trace(dual_matrix @ constant).real)
    corrected_upper = dual_objective + stationarity_l1
    values = _unpack_variables(vector, collateral_count)
    primal = float(vector[0])
    return PickBarrierResult(
        target_amplitude=primal,
        dual_upper_bound=corrected_upper,
        duality_gap=corrected_upper - primal,
        stationarity_l1=stationarity_l1,
        values=values,
        min_lmi_eigenvalue=float(np.min(np.linalg.eigvalsh(matrix))),
        min_phase_margin=float(np.min(margins)) if collateral_count else float("inf"),
        success=bool(
            np.min(np.linalg.eigvalsh(matrix)) > 0
            and (not collateral_count or np.min(margins) > 0)
            and corrected_upper >= primal
        ),
        message=message,
        iterations=total_iterations,
    )


def probe_halfdisk_extremal(
    target: complex,
    collateral: Sequence[complex],
    phases: Sequence[float],
    *,
    starts: int = 4,
    maxiter: int = 3000,
    feasibility_tolerance: float = 2e-8,
    random_seed: int = 0,
) -> PickProbeResult:
    """Numerically maximize the target value in the exact finite Pick LMI.

    This uses SLSQP rather than a certified conic solver.  Convexity of the
    underlying LMI problem does not turn its floating-point answer into a
    proof; callers should inspect the returned primal residuals.
    """

    target = complex(target)
    nodes_c = np.asarray(collateral, dtype=np.complex128)
    phi = np.asarray(phases, dtype=float)
    if target.imag != 0 or target.real <= 0:
        raise ValueError("the probe currently normalizes the target to a positive real node")
    if nodes_c.shape != phi.shape or nodes_c.ndim != 1:
        raise ValueError("collateral and phases must be one-dimensional and equally long")
    nodes = np.concatenate(([target], nodes_c))
    count = len(nodes_c)
    kernel = cauchy_kernel(nodes)
    kernel_scale = float(np.linalg.norm(kernel, ord=2))

    def lmi_eigenvalues(vector: NDArray[np.float64]) -> NDArray[np.float64]:
        values = _unpack_variables(vector, count)
        cross = values[:, None] * kernel
        lmi = np.block([[kernel, cross], [cross.conj().T, kernel]]) / kernel_scale
        return np.linalg.eigvalsh(lmi)

    def margins(vector: NDArray[np.float64]) -> NDArray[np.float64]:
        return phase_margins(_unpack_variables(vector, count)[1:], phi)

    zero_bound = zero_blashke_target(target, nodes_c)
    base = np.zeros(1 + 2 * count, dtype=float)
    # Strictly shrink the exact zero-interpolation datum off its singular face.
    base[0] = 0.95 * zero_bound
    candidates = [base]
    rng = np.random.default_rng(random_seed)
    for _ in range(max(0, starts - 1)):
        trial = np.zeros_like(base)
        trial[0] = rng.uniform(0.0, max(1e-12, 0.8 * zero_bound))
        candidates.append(trial)

    constraints = [
        {"type": "ineq", "fun": lmi_eigenvalues},
        {"type": "ineq", "fun": margins},
    ]
    bounds = [(0.0, 1.0)] + [(-1.0, 1.0)] * (2 * count)
    best = None
    for initial in candidates:
        result = minimize(
            lambda vector: -vector[0],
            initial,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"ftol": 1e-12, "maxiter": maxiter, "disp": False},
        )
        values = _unpack_variables(result.x, count)
        min_eigenvalue = float(np.min(lmi_eigenvalues(result.x)))
        min_margin = float(np.min(margins(result.x))) if count else float("inf")
        feasible = min_eigenvalue >= -feasibility_tolerance and min_margin >= -feasibility_tolerance
        score = float(result.x[0]) if feasible else -np.inf
        if best is None or score > best[0]:
            best = (score, result, values, min_eigenvalue, min_margin, feasible)

    assert best is not None
    _, result, values, min_eigenvalue, min_margin, feasible = best
    return PickProbeResult(
        target_amplitude=float(values[0].real),
        values=values,
        min_lmi_eigenvalue=min_eigenvalue,
        min_phase_margin=min_margin,
        success=bool(result.success and feasible),
        message=str(result.message),
        iterations=int(result.nit),
    )
