"""Finite carrier-preserving relative-trace certificates.

This module has two deliberately separate models.

``cyclic_*`` implements the exact finite abelian-group analogue

    T(b,c) = sum_a A(a) W(a+b+c).

Its Hankel operator is diagonalized (up to character inversion) by the
finite Fourier transform.  Consequently deleting a set of character modes
leaves operator norm exactly the largest undeleted Fourier coefficient.

``build_actual_carrier_matrix`` constructs the literal integer matrix

    T(b,c) = sum_{a in S(q)} 1_{|8abc-q^3| <= qD},
    D = floor(q^(16/33)),

on the narrow prime-power shell ``S(q)``.  Every comparison is performed
with Python integers; floating point is used only by the optional spectral
diagnostic.

The finite-group identity does not prove the sharp QP estimate.  On the
actual narrow shell, restrictions of induced characters already span the
entire symmetric matrix space.  Thus an automorphic ``polar part`` must be
specified by a norm-controlled synthesis theorem; calling every induced
mode polar would make the subtraction vacuous.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp, pi, sqrt
from typing import Iterable, Literal, Sequence

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import LinearOperator, eigsh

from qp_four_cycle_hostile_lab import shell_values


def exact_balanced_degree(q: int) -> int:
    r"""Return ``floor(q**(16/33))`` using integer comparisons only."""

    modulus = int(q)
    if modulus <= 1:
        raise ValueError("q must exceed one")
    target = modulus**16
    lower = 0
    upper = 1
    while upper**33 <= target:
        upper *= 2
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if middle**33 <= target:
            lower = middle
        else:
            upper = middle
    return lower


@dataclass(frozen=True)
class ActualCarrierMatrix:
    """One literal prime-power/product-window carrier matrix.

    ``support[b,c]`` is one exactly when the product window has an allowed
    label ``a``.  ``labels[b,c]`` stores that integer ``a``.  In the range
    ``D<q/4`` the interval in ``a`` has length below one, so an entry cannot
    contain two labels; the builder checks this rather than assuming it.
    """

    q: int
    degree_parameter: int
    width: float
    kind: Literal["prime_powers", "integers"]
    values: np.ndarray
    support: csr_matrix
    labels: csr_matrix

    @property
    def dimension(self) -> int:
        return int(self.values.size)

    @property
    def edge_count(self) -> int:
        return int(self.support.nnz)


def build_actual_carrier_matrix(
    q: int,
    *,
    degree_parameter: int | None = None,
    width: float = 0.2,
    kind: Literal["prime_powers", "integers"] = "prime_powers",
) -> ActualCarrierMatrix:
    r"""Build the exact matrix ``1_(|8abc-q^3|<=qD)``.

    The nearest candidates are obtained with integer division.  The routine
    is intended for finite experiments up to roughly ``q=2,000,000``, where
    all vectorized products fit in signed 64-bit integers.
    """

    modulus = int(q)
    if modulus <= 2 or modulus % 2 == 0:
        raise ValueError("q must be an odd integer greater than two")
    if width <= 0:
        raise ValueError("width must be positive")
    degree = (
        exact_balanced_degree(modulus)
        if degree_parameter is None
        else int(degree_parameter)
    )
    if degree <= 0:
        raise ValueError("degree_parameter must be positive")
    if modulus**3 > np.iinfo(np.int64).max:
        raise ValueError("q is too large for the vectorized exact builder")

    values = shell_values(modulus / 2.0, width, kind)
    if values.size == 0:
        raise ValueError("the requested shell is empty")
    dimension = int(values.size)
    lower = int(values[0])
    upper = int(values[-1])
    lookup = np.full(upper + 2, -1, dtype=np.int32)
    lookup[values] = np.arange(dimension, dtype=np.int32)

    target = modulus**3
    tolerance = modulus * degree
    row_indices: list[int] = []
    column_indices: list[int] = []
    label_values: list[int] = []

    for row_index, raw_carrier in enumerate(values):
        carrier = int(raw_carrier)
        denominators = 8 * carrier * values
        floors = target // denominators
        for candidates in (floors, floors + 1):
            inside = (candidates >= lower) & (candidates <= upper)
            label_ids = np.full(dimension, -1, dtype=np.int32)
            label_ids[inside] = lookup[candidates[inside]]
            residuals = denominators * candidates - target
            accepted = (label_ids >= 0) & (np.abs(residuals) <= tolerance)
            columns = np.flatnonzero(accepted)
            row_indices.extend([row_index] * int(columns.size))
            column_indices.extend(columns.tolist())
            label_values.extend(int(value) for value in candidates[columns])

    shape = (dimension, dimension)
    support = coo_matrix(
        (
            np.ones(len(row_indices), dtype=np.int8),
            (row_indices, column_indices),
        ),
        shape=shape,
    ).tocsr()
    support.sum_duplicates()
    labels = coo_matrix(
        (
            np.asarray(label_values, dtype=np.int64),
            (row_indices, column_indices),
        ),
        shape=shape,
    ).tocsr()
    labels.sum_duplicates()

    if support.nnz and np.any(support.data != 1):
        raise AssertionError("one carrier-colour cell acquired multiple labels")
    if (support - support.T).nnz:
        raise AssertionError("the exact carrier matrix must be symmetric")
    if (labels - labels.T).nnz:
        raise AssertionError("the exact label matrix must be symmetric")
    return ActualCarrierMatrix(
        q=modulus,
        degree_parameter=degree,
        width=float(width),
        kind=kind,
        values=values,
        support=support,
        labels=labels,
    )


def _project_off_constants(vector: np.ndarray) -> np.ndarray:
    values = np.asarray(vector, dtype=float).reshape(-1)
    return values - float(np.mean(values))


def centered_eigenvalues(
    matrix: csr_matrix,
    *,
    count: int = 1,
    centering: Literal["mean_rank_one", "double", "none"] = "mean_rank_one",
    tolerance: float = 1e-9,
) -> np.ndarray:
    r"""Return the largest-magnitude eigenvalues of a symmetric matrix.

    ``mean_rank_one`` uses ``T-(sum T/n^2)J``, the physical constant-mode
    subtraction.  ``double`` uses ``(I-J/n)T(I-J/n)`` and therefore also
    deletes both degree-fluctuation cross channels (a rank-at-most-two
    strengthening).  The returned order is decreasing in absolute value.
    """

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("matrix must be square")
    if (matrix - matrix.T).nnz:
        raise ValueError("matrix must be symmetric")
    dimension = int(matrix.shape[0])
    number = int(count)
    if dimension == 0 or number <= 0:
        return np.empty(0, dtype=float)

    total = float(matrix.sum())
    mean = total / (dimension * dimension)
    ones = np.ones(dimension, dtype=float)

    def matvec(raw_vector: np.ndarray) -> np.ndarray:
        vector = np.asarray(raw_vector, dtype=float).reshape(-1)
        if centering == "none":
            return np.asarray(matrix @ vector).reshape(-1)
        if centering == "mean_rank_one":
            return np.asarray(matrix @ vector).reshape(-1) - mean * float(
                np.sum(vector)
            ) * ones
        if centering == "double":
            projected = _project_off_constants(vector)
            return _project_off_constants(np.asarray(matrix @ projected).reshape(-1))
        raise ValueError("unknown centering")

    if dimension <= 2 or number >= dimension:
        basis = np.eye(dimension)
        dense = np.column_stack(tuple(matvec(basis[:, index]) for index in range(dimension)))
        eigenvalues = np.linalg.eigvalsh(dense)
        order = np.argsort(np.abs(eigenvalues))[::-1]
        return eigenvalues[order[: min(number, dimension)]]

    operator = LinearOperator(
        (dimension, dimension), matvec=matvec, rmatvec=matvec, dtype=float
    )
    number = min(number, dimension - 1)
    initial = np.linspace(1.0, 2.0, dimension)
    eigenvalues = eigsh(
        operator,
        k=number,
        which="LM",
        return_eigenvectors=False,
        tol=float(tolerance),
        maxiter=20_000,
        v0=initial / np.linalg.norm(initial),
    )
    order = np.argsort(np.abs(eigenvalues))[::-1]
    return np.asarray(eigenvalues[order], dtype=float)


@dataclass(frozen=True)
class ActualCarrierSpectralLedger:
    q: int
    degree_parameter: int
    dimension: int
    edges: int
    mean_degree: float
    maximum_degree: int
    centered_norm: float
    doubly_centered_norm: float
    square_root_degree: float
    centered_ratio: float
    doubly_centered_ratio: float
    threshold_polar_rank_in_computed_spectrum: int
    schur_centered_upper_bound: float
    schur_proves_sqrt_degree: bool
    double_schur_proves_sqrt_degree: bool


@dataclass(frozen=True)
class CarrierDegreeAnovaLedger:
    """Exact scalar data in the constant/degree/broad decomposition."""

    dimension: int
    edges: int
    maximum_degree: int
    mean_degree: float
    degree_variance: float
    degree_channel_norm: float
    exact_product_interval_degree_cap: int


def carrier_degree_anova_ledger(core: ActualCarrierMatrix) -> CarrierDegreeAnovaLedger:
    r"""Return the degree channel and the exact product-interval cap.

    For ``u=1/sqrt(n)`` and ``P=I-u*u^T``, put

    ``d=T*1``, ``dbar=E/n`` and ``delta=d-dbar*1``.

    The mean-centered operator has the exact ANOVA decomposition

    ``T-(dbar/n)J = P*T*P + u*w^T+w*u^T``, ``w=delta/sqrt(n)``.

    The rank-two channel therefore has norm
    ``||w||=sqrt(n^(-1) sum_b (d_b-dbar)^2)``.
    """

    dimension = core.dimension
    degrees = np.asarray(core.support.sum(axis=1), dtype=float).reshape(-1)
    edges = core.edge_count
    mean = float(edges / dimension)
    variance = float(np.mean((degrees - mean) ** 2))

    # For fixed b, ac lies in an interval of exact length qD/(4b).
    # Each integer in it has at most two ordered shell factorizations.
    minimum_carrier = int(core.values[0])
    numerator = core.q * core.degree_parameter
    interval_integer_count_upper = numerator // (4 * minimum_carrier) + 1
    product_cap = 2 * interval_integer_count_upper
    return CarrierDegreeAnovaLedger(
        dimension=dimension,
        edges=edges,
        maximum_degree=int(np.max(degrees, initial=0)),
        mean_degree=mean,
        degree_variance=variance,
        degree_channel_norm=sqrt(variance),
        exact_product_interval_degree_cap=product_cap,
    )


def carrier_anova_dense(
    matrix: csr_matrix,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    r"""Return ``(A,B,C,delta)`` in the exact carrier ANOVA identity.

    ``A=T-(E/n^2)J`` is physical mean centering, ``B=P*T*P`` is the
    doubly centered broad block, and ``C`` is the rank-two degree channel.
    Thus ``A=B+C``.  This helper materializes dense matrices and is intended
    only for finite regression fixtures.
    """

    if matrix.shape[0] != matrix.shape[1] or (matrix - matrix.T).nnz:
        raise ValueError("matrix must be square and symmetric")
    dimension = int(matrix.shape[0])
    if dimension == 0:
        empty = np.empty((0, 0), dtype=float)
        return empty, empty, empty, np.empty(0, dtype=float)
    dense = matrix.toarray().astype(float)
    ones = np.ones(dimension, dtype=float)
    projection = np.eye(dimension) - np.outer(ones, ones) / dimension
    degrees = dense @ ones
    mean_degree = float(np.mean(degrees))
    delta = degrees - mean_degree * ones
    mean_centered = dense - mean_degree * np.outer(ones, ones) / dimension
    broad = projection @ dense @ projection
    degree_channel = (
        np.outer(delta, ones) + np.outer(ones, delta)
    ) / dimension
    return mean_centered, broad, degree_channel, delta


def broad_common_neighbor_identity(
    matrix: csr_matrix,
) -> tuple[np.ndarray, np.ndarray]:
    r"""Return both sides of ``(P T P)^2=P T^2 P-delta delta^T/n``."""

    mean_centered, broad, _, delta = carrier_anova_dense(matrix)
    del mean_centered
    dimension = int(matrix.shape[0])
    if dimension == 0:
        empty = np.empty((0, 0), dtype=float)
        return empty, empty
    dense = matrix.toarray().astype(float)
    ones = np.ones(dimension, dtype=float)
    projection = np.eye(dimension) - np.outer(ones, ones) / dimension
    left = broad @ broad
    right = (
        projection @ dense @ dense @ projection
        - np.outer(delta, delta) / dimension
    )
    return left, right


def exact_schur_sqrt_certificates(
    core: ActualCarrierMatrix,
) -> tuple[bool, bool]:
    r"""Certify the target using only integer degree inequalities.

    If ``Delta`` is the maximum row degree and ``dbar=E/n``, Schur's
    test and the triangle inequality give

    ``||T-(E/n^2)J|| <= Delta+dbar``.

    Double centering is contractive on both sides, so
    ``||(I-J/n)T(I-J/n)|| <= Delta``.  The two returned booleans check
    these bounds against ``sqrt(D)`` after clearing denominators; no
    eigenvalue or floating-point computation enters the certificates.
    """

    dimension = core.dimension
    if dimension <= 0:
        return True, True
    degrees = np.asarray(core.support.sum(axis=1)).reshape(-1)
    maximum = int(np.max(degrees, initial=0))
    edges = core.edge_count
    degree = core.degree_parameter
    mean_centered = (maximum * dimension + edges) ** 2 <= degree * dimension**2
    doubly_centered = maximum**2 <= degree
    return mean_centered, doubly_centered


def actual_carrier_spectral_ledger(
    core: ActualCarrierMatrix, *, eigenvalue_count: int = 12
) -> ActualCarrierSpectralLedger:
    """Return finite norm data before and after degree-channel deletion."""

    dimension = core.dimension
    degrees = np.asarray(core.support.sum(axis=1)).reshape(-1)
    centered = centered_eigenvalues(
        core.support, count=eigenvalue_count, centering="mean_rank_one"
    )
    double = centered_eigenvalues(
        core.support, count=eigenvalue_count, centering="double"
    )
    centered_norm = float(abs(centered[0])) if centered.size else 0.0
    double_norm = float(abs(double[0])) if double.size else 0.0
    threshold = sqrt(core.degree_parameter)
    schur_mean, schur_double = exact_schur_sqrt_certificates(core)
    maximum_degree = int(np.max(degrees, initial=0))
    mean_degree = float(core.edge_count / dimension)
    return ActualCarrierSpectralLedger(
        q=core.q,
        degree_parameter=core.degree_parameter,
        dimension=dimension,
        edges=core.edge_count,
        mean_degree=mean_degree,
        maximum_degree=maximum_degree,
        centered_norm=centered_norm,
        doubly_centered_norm=double_norm,
        square_root_degree=threshold,
        centered_ratio=centered_norm / threshold,
        doubly_centered_ratio=double_norm / threshold,
        threshold_polar_rank_in_computed_spectrum=int(
            np.count_nonzero(np.abs(centered) > threshold * (1 + 1e-10))
        ),
        schur_centered_upper_bound=maximum_degree + mean_degree,
        schur_proves_sqrt_degree=schur_mean,
        double_schur_proves_sqrt_degree=schur_double,
    )


def cyclic_carrier_kernel(
    source_mask: Sequence[complex], window_mask: Sequence[complex]
) -> np.ndarray:
    r"""Return ``f(x)=sum_a A(a)W(a+x)`` on ``Z/NZ`` exactly up to dtype."""

    source = np.asarray(source_mask, dtype=complex)
    window = np.asarray(window_mask, dtype=complex)
    if source.ndim != 1 or window.ndim != 1 or source.size != window.size:
        raise ValueError("source_mask and window_mask need one common length")
    size = int(source.size)
    if size == 0:
        raise ValueError("the cyclic group must be nonempty")
    return np.asarray(
        [
            sum(source[index] * window[(index + shift) % size] for index in range(size))
            for shift in range(size)
        ],
        dtype=complex,
    )


def cyclic_hankel_matrix(kernel: Sequence[complex]) -> np.ndarray:
    """Return the group Hankel matrix ``H[b,c]=f(b+c)``."""

    values = np.asarray(kernel, dtype=complex)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("kernel must be a nonempty vector")
    size = int(values.size)
    rows = np.arange(size)[:, None]
    columns = np.arange(size)[None, :]
    return values[(rows + columns) % size]


def cyclic_character_coefficients(kernel: Sequence[complex]) -> np.ndarray:
    r"""Return ``hat f(k)=sum_x f(x)e(-kx/N)``."""

    values = np.asarray(kernel, dtype=complex)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("kernel must be a nonempty vector")
    return np.fft.fft(values)


def cyclic_character_matrix(
    coefficients: Sequence[complex], modes: Iterable[int] | None = None
) -> np.ndarray:
    r"""Reconstruct selected terms ``hat f(k) chi_k(b)chi_k(c)/N``."""

    fourier = np.asarray(coefficients, dtype=complex)
    if fourier.ndim != 1 or fourier.size == 0:
        raise ValueError("coefficients must be a nonempty vector")
    size = int(fourier.size)
    selected = range(size) if modes is None else tuple(int(mode) % size for mode in modes)
    indices = np.arange(size)
    answer = np.zeros((size, size), dtype=complex)
    for mode in selected:
        character = np.exp(2j * pi * mode * indices / size)
        answer += fourier[mode] * np.outer(character, character) / size
    return answer


def cyclic_regularized_remainder_norm(
    coefficients: Sequence[complex], removed_modes: Iterable[int]
) -> float:
    """Return the exact full-group norm after deleting character modes."""

    fourier = np.asarray(coefficients, dtype=complex)
    if fourier.ndim != 1 or fourier.size == 0:
        raise ValueError("coefficients must be a nonempty vector")
    retained = np.ones(fourier.size, dtype=bool)
    for mode in removed_modes:
        retained[int(mode) % fourier.size] = False
    return float(np.max(np.abs(fourier[retained]), initial=0.0))


def cyclic_threshold_polar_modes(
    coefficients: Sequence[complex], threshold: float
) -> tuple[int, ...]:
    """Return every character whose singular value exceeds ``threshold``."""

    bound = float(threshold)
    if bound < 0:
        raise ValueError("threshold must be nonnegative")
    fourier = np.asarray(coefficients, dtype=complex)
    return tuple(int(index) for index in np.flatnonzero(np.abs(fourier) > bound))


def independent_induced_symmetric_span_rank(
    node_count: int, character_order: int = 3
) -> int:
    r"""Compute the rank of restricted tensors ``v_chi v_chi^T``.

    The model has one independent cyclic character coordinate for each
    shell node.  For order at least three these tensors span every complex
    symmetric ``node_count`` by ``node_count`` matrix.  Enumeration is only
    for small regression fixtures; the exact rank is ``n(n+1)/2``.
    """

    size = int(node_count)
    order = int(character_order)
    if size <= 0:
        raise ValueError("node_count must be positive")
    if order < 3:
        raise ValueError("character_order must be at least three")
    if order**size > 2_000_000:
        raise ValueError("enumeration fixture is too large")
    upper_pairs = tuple((left, right) for left in range(size) for right in range(left, size))
    rows: list[list[complex]] = []
    for exponents in product(range(order), repeat=size):
        vector = np.exp(2j * pi * np.asarray(exponents) / order)
        rows.append([vector[left] * vector[right] for left, right in upper_pairs])
    return int(np.linalg.matrix_rank(np.asarray(rows, dtype=complex), tol=1e-10))


def narrow_shell_has_one_power_per_prime(width: float = 0.2) -> bool:
    """Return the elementary shell condition ``exp(2*width)<2``."""

    if width <= 0:
        raise ValueError("width must be positive")
    return exp(2 * width) < 2
