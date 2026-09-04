"""Source-resolved finite diagnostic for the completed-zeta Ward inequality.

At the first certified support event ``L5 = 2 log(5)``, this module extracts
the maximizing vector for

    B^* A^{-1} B <= Theta J^* G J,

where ``B = P_old (Q-h) J`` and ``J`` is the reference-harmonic lift from a
literal boundary collar.  It decomposes ``B`` into the completed
archimedean remainder, the pole, and every active prime power, then resolves
the dangerous old generalized eigenmodes and even/odd collar sectors.

All calculations use ordinary high-precision mpmath.  They are cutoff-free
finite Galerkin diagnostics, not interval certificates or operator theorems.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterable

import mpmath as mp

from harmonic_schur_collar_probe import (
    generalized_extreme,
    l2_orthogonalized_blocks,
    mixed_extension_forms,
    unequal_hat_overlap,
)
from hp_margins import hp_lam_min
from weil_core import PRIME_POWERS


def _symmetrize(a: mp.matrix) -> mp.matrix:
    return mp.matrix(
        [[(a[i, j] + a[j, i]) / 2 for j in range(a.cols)] for i in range(a.rows)]
    )


def _submatrix(a: mp.matrix, rows: list[int], cols: list[int]) -> mp.matrix:
    return mp.matrix([[a[i, j] for j in cols] for i in rows])


def _solve_left(a: mp.matrix, b: mp.matrix) -> mp.matrix:
    ans = mp.matrix(a.rows, b.cols)
    for j in range(b.cols):
        col = mp.lu_solve(a, mp.matrix([b[i, j] for i in range(b.rows)]))
        for i in range(a.rows):
            ans[i, j] = col[i]
    return ans


def _cholesky_solve(chol: mp.matrix, b: mp.matrix) -> mp.matrix:
    """Solve ``chol*chol.T*x=b`` with reusable triangular factors."""
    rows = chol.rows
    rhs = b if isinstance(b, mp.matrix) else mp.matrix(b)
    y = mp.matrix(rows, rhs.cols)
    for column in range(rhs.cols):
        for i in range(rows):
            subtotal = sum(chol[i, j] * y[j, column] for j in range(i))
            y[i, column] = (rhs[i, column] - subtotal) / chol[i, i]
    x = mp.matrix(rows, rhs.cols)
    for column in range(rhs.cols):
        for i in range(rows - 1, -1, -1):
            subtotal = sum(chol[j, i] * x[j, column] for j in range(i + 1, rows))
            x[i, column] = (y[i, column] - subtotal) / chol[i, i]
    return x


def _max_abs(a: mp.matrix) -> mp.mpf:
    if not a.rows or not a.cols:
        return mp.mpf(0)
    return max(abs(a[i, j]) for i in range(a.rows) for j in range(a.cols))


def _quadratic(v: mp.matrix, a: mp.matrix, w: mp.matrix | None = None) -> mp.mpf:
    if w is None:
        w = v
    return (v.T * a * w)[0]


def _mpstr(x: mp.mpf, digits: int = 20) -> str:
    return mp.nstr(x, digits, min_fixed=0, max_fixed=0)


def _vector_strings(v: mp.matrix, digits: int = 16) -> list[str]:
    return [_mpstr(v[i], digits) for i in range(v.rows)]


def literal_collar_geometry(
    old_degree: int, collar_degree: int, delta: mp.mpf, event_prime: int
) -> tuple[list[mp.mpf], list[mp.mpf], mp.mpf, mp.mpf]:
    """Return centers, half-widths, old support, and enlarged support."""
    lold = 2 * mp.log(event_prime)
    lnew = lold + delta
    old_radius = lold / 4
    old_width = lold / (2 * (old_degree + 1))
    old_centers = [
        -old_radius + (i + 1) * old_width for i in range(old_degree)
    ]
    physical_collar = delta / 4
    collar_width = physical_collar / (collar_degree + 1)
    left = [
        -old_radius - (j + 1) * collar_width for j in range(collar_degree)
    ]
    right = [
        old_radius + (j + 1) * collar_width for j in range(collar_degree)
    ]
    return (
        old_centers + left + right,
        [old_width] * old_degree + [collar_width] * (2 * collar_degree),
        lold,
        lnew,
    )


def _pole_transform(center: mp.mpf, width: mp.mpf, sign: int) -> mp.mpf:
    s = mp.mpf(sign) / 2
    return mp.exp(s * center) * (2 * mp.cosh(s * width) - 2) / (s * s * width)


def pole_matrix(centers: list[mp.mpf], widths: list[mp.mpf]) -> mp.matrix:
    plus = [_pole_transform(c, d, +1) for c, d in zip(centers, widths)]
    minus = [_pole_transform(c, d, -1) for c, d in zip(centers, widths)]
    n = len(centers)
    return mp.matrix(
        [
            [plus[i] * minus[j] + minus[i] * plus[j] for j in range(n)]
            for i in range(n)
        ]
    )


def prime_translation_matrix(
    centers: list[mp.mpf],
    widths: list[mp.mpf],
    shift: mp.mpf,
    weight: mp.mpf,
) -> mp.matrix:
    """Negative even translation appearing in the zeta explicit formula."""
    n = len(centers)
    out = mp.matrix(n)
    for i in range(n):
        for j in range(i, n):
            separation = centers[j] - centers[i]
            shifted = (
                unequal_hat_overlap(separation - shift, widths[i], widths[j])
                + unequal_hat_overlap(separation + shift, widths[i], widths[j])
            ) / 2
            out[i, j] = out[j, i] = -weight * shifted
    return out


def residual_source_matrices(
    q: mp.matrix,
    h: mp.matrix,
    centers: list[mp.mpf],
    widths: list[mp.mpf],
    project_support: mp.mpf,
) -> tuple[dict[str, mp.matrix], dict[str, dict]]:
    """Split ``R=Q-h`` into arch remainder, pole, and prime powers.

    The completed archimedean remainder is obtained by subtracting the
    explicitly assembled pole and prime matrices from ``Q-h``.  Thus it is
    exactly ``Arch-(1+log(pi))G-Wplus`` in the current normalization.
    """
    sources: dict[str, mp.matrix] = {"pole": pole_matrix(centers, widths)}
    metadata: dict[str, dict] = {
        "pole": {"kind": "pole", "sign_in_explicit_formula": "indefinite"}
    }
    for nn, prime in PRIME_POWERS:
        shift = mp.log(nn)
        if 2 * shift >= project_support:
            continue
        name = f"prime_power_{nn}"
        weight = 2 * mp.log(prime) / mp.sqrt(nn)
        sources[name] = prime_translation_matrix(centers, widths, shift, weight)
        metadata[name] = {
            "kind": "prime_power",
            "prime_power": nn,
            "underlying_prime": prime,
            "shift": _mpstr(shift),
            "weight_magnitude": _mpstr(weight),
            "sign_in_explicit_formula": "negative",
        }

    remainder = q - h
    for matrix in sources.values():
        remainder -= matrix
    ordered = {"archimedean_residual": _symmetrize(remainder)}
    ordered.update(sources)
    metadata = {
        "archimedean_residual": {
            "kind": "archimedean_residual",
            "formula": "Arch-(1+log(pi))*G-Wplus",
        },
        **metadata,
    }
    return ordered, metadata


def _corrected_blocks(
    a: mp.matrix,
    old: list[int],
    collar: list[int],
    correction: mp.matrix,
) -> tuple[mp.matrix, mp.matrix, mp.matrix]:
    aa = _submatrix(a, old, old)
    x = _submatrix(a, old, collar)
    dd = _submatrix(a, collar, collar)
    xo = x - aa * correction
    do = dd - x.T * correction - correction.T * x + correction.T * aa * correction
    return _symmetrize(aa), xo, _symmetrize(do)


def _response(a: mp.matrix, b: mp.matrix) -> mp.matrix:
    chol = mp.cholesky(_symmetrize(a))
    return _symmetrize(b.T * _cholesky_solve(chol, b))


def generalized_max_vector(
    numerator: mp.matrix, denominator: mp.matrix
) -> tuple[mp.mpf, mp.matrix, mp.mpf | None]:
    """Largest generalized eigenpair, normalized by the denominator."""
    chol = mp.cholesky(_symmetrize(denominator))
    left = _solve_left(chol, _symmetrize(numerator))
    whitened = _symmetrize(_solve_left(chol, left.T).T)
    values, vectors = mp.eigsy(whitened)
    idx = max(range(values.rows), key=lambda j: values[j])
    z = mp.matrix([vectors[i, idx] for i in range(vectors.rows)])
    v = mp.lu_solve(chol.T, z)
    v /= mp.sqrt(_quadratic(v, denominator))
    # Canonicalize the otherwise arbitrary eigenvector sign for saved data.
    pivot = max(range(v.rows), key=lambda i: abs(v[i]))
    if v[pivot] < 0:
        v *= -1
    second = None
    if values.rows > 1:
        ordered = sorted(values[i] for i in range(values.rows))
        second = ordered[-2]
    return values[idx], v, second


def _parity_basis(collar_degree: int, sign: int) -> mp.matrix:
    root2 = mp.sqrt(2)
    out = mp.matrix(2 * collar_degree, collar_degree)
    for j in range(collar_degree):
        out[j, j] = 1 / root2
        out[collar_degree + j, j] = sign / root2
    return out


def _reflect_collar(v: mp.matrix, collar_degree: int) -> mp.matrix:
    return mp.matrix(
        [v[collar_degree + j] for j in range(collar_degree)]
        + [v[j] for j in range(collar_degree)]
    )


def _reflect_cross(b: mp.matrix, collar_degree: int) -> mp.matrix:
    """Return P_old B P_collar for the mixed literal-collar ordering."""
    return mp.matrix(
        [
            [
                b[
                    b.rows - 1 - i,
                    (j + collar_degree) % (2 * collar_degree),
                ]
                for j in range(2 * collar_degree)
            ]
            for i in range(b.rows)
        ]
    )


def _safe_ratio(a: mp.mpf, b: mp.mpf) -> str | None:
    if b == 0:
        return None
    return _mpstr(a / b)


def _metric_variant(
    a: mp.matrix, b: mp.matrix, denominator: mp.matrix, go: mp.matrix
) -> dict:
    floor = generalized_extreme(a, go, "min")
    ans = {"old_generalized_floor": _mpstr(floor)}
    if floor <= 0:
        ans.update({"status": "OLD_METRIC_NOT_POSITIVE", "ward_ratio": None})
        return ans
    ratio = generalized_extreme(_response(a, b), denominator, "max")
    ans.update({"status": "OLD_METRIC_POSITIVE", "ward_ratio": _mpstr(ratio)})
    return ans


def _source_group(
    names: Iterable[str],
    matrices: dict[str, mp.matrix],
) -> mp.matrix:
    names = list(names)
    out = mp.matrix(matrices[names[0]].rows, matrices[names[0]].cols)
    for name in names:
        out += matrices[name]
    return out


def analyze_source_resolved_ward(
    old_degree: int,
    collar_degree: int,
    delta: mp.mpf | str | float,
    dps: int = 50,
    event_prime: int = 5,
    low_mode_count: int = 12,
    smear_nodes: int = 9,
    include_consistent_variants: bool = False,
) -> dict:
    """Resolve the Ward maximizer into completed-zeta source channels."""
    if old_degree < 3 or collar_degree < 1:
        raise ValueError("old_degree >= 3 and collar_degree >= 1 are required")
    if smear_nodes < 1:
        raise ValueError("smear_nodes must be positive")
    with mp.workdps(dps + 15):
        delta_mp = mp.mpf(str(delta))
        if delta_mp <= 0:
            raise ValueError("delta must be positive")
        qfull, gfull, hfull, lold, lnew = mixed_extension_forms(
            old_degree, collar_degree, delta_mp, event_prime, dps
        )
        centers, widths, geometry_lold, geometry_lnew = literal_collar_geometry(
            old_degree, collar_degree, delta_mp, event_prime
        )
        old = list(range(old_degree))
        collar = list(range(old_degree, qfull.rows))
        blocks = l2_orthogonalized_blocks(qfull, hfull, gfull, old, collar)
        a, x, dmat = blocks["Q"]
        href, y, zref = blocks["H"]
        go, goc, gc = blocks["G"]
        correction = blocks["l2_correction"]
        k = _solve_left(href, y)
        xtilde = x - a * k
        denominator = _symmetrize(
            k.T * go * k - k.T * goc - goc.T * k + gc
        )

        raw_sources, metadata = residual_source_matrices(
            qfull, hfull, centers, widths, lnew
        )
        old_sources: dict[str, mp.matrix] = {}
        cross_sources: dict[str, mp.matrix] = {}
        collar_sources: dict[str, mp.matrix] = {}
        b_sources: dict[str, mp.matrix] = {}
        for name, raw in raw_sources.items():
            roo, roc, rcc = _corrected_blocks(raw, old, collar, correction)
            old_sources[name] = roo
            cross_sources[name] = roc
            collar_sources[name] = rcc
            b_sources[name] = roc - roo * k

        source_names = list(b_sources)
        btotal = _source_group(b_sources.keys(), b_sources)
        raw_total = _source_group(raw_sources.keys(), raw_sources)
        a_chol = mp.cholesky(_symmetrize(a))
        solved_b_sources = {
            name: _cholesky_solve(a_chol, matrix)
            for name, matrix in b_sources.items()
        }
        response_pairs = {
            (left_name, right_name): b_sources[left_name].T
            * solved_b_sources[right_name]
            for left_name in source_names
            for right_name in source_names
        }

        def fixed_response(coefficients: dict[str, mp.mpf | int]) -> mp.matrix:
            ans = mp.matrix(denominator.rows)
            for left_name in source_names:
                for right_name in source_names:
                    ans += (
                        coefficients.get(left_name, 0)
                        * coefficients.get(right_name, 0)
                        * response_pairs[(left_name, right_name)]
                    )
            return _symmetrize(ans)

        physical_coefficients = {name: mp.mpf(1) for name in source_names}
        response = fixed_response(physical_coefficients)
        direct_response = _response(a, btotal)
        q_poisson = _cholesky_solve(a_chol, x)
        poisson_difference = q_poisson - k
        response_from_poisson_difference = _symmetrize(
            poisson_difference.T * a * poisson_difference
        )
        q_harmonic_schur = _symmetrize(dmat - x.T * q_poisson)
        reference_harmonic_schur = _symmetrize(zref - y.T * k)
        q_energy_at_reference_harmonic_lift = _symmetrize(
            dmat - x.T * k - k.T * x + k.T * a * k
        )
        theta, v, second_theta = generalized_max_vector(response, denominator)
        b_at_v = btotal * v
        u = _cholesky_solve(a_chol, b_at_v)
        old_energy = _quadratic(u, a)
        old_l2 = _quadratic(u, go)
        net_cross = (u.T * b_at_v)[0]
        denominator_value = _quadratic(v, denominator)

        # The physical harmonic vector includes both the L2 correction and K.
        harmonic_old = -(correction + k) * v
        harmonic_collar = v

        source_vectors = {name: matrix * v for name, matrix in b_sources.items()}
        solved_source_vectors = {
            name: solved_b_sources[name] * v for name in source_names
        }
        gamma = mp.matrix(len(source_names))
        for i, left_name in enumerate(source_names):
            for j, right_name in enumerate(source_names):
                gamma[i, j] = (
                    source_vectors[left_name].T
                    * solved_source_vectors[right_name]
                )[0]

        amplitudes = {
            name: (u.T * source_vectors[name])[0] for name in source_names
        }
        absolute_amplitude_sum = sum(abs(value) for value in amplitudes.values())
        diagonal_response_sum = sum(gamma[i, i] for i in range(gamma.rows))

        source_rows = []
        for index, name in enumerate(source_names):
            bs = b_sources[name]
            without = btotal - bs
            flipped = btotal - 2 * bs
            only_coefficients = {source: 0 for source in source_names}
            only_coefficients[name] = 1
            without_coefficients = dict(physical_coefficients)
            without_coefficients[name] = 0
            flipped_coefficients = dict(physical_coefficients)
            flipped_coefficients[name] = -1
            response_only = fixed_response(only_coefficients)
            response_without = fixed_response(without_coefficients)
            response_flipped = fixed_response(flipped_coefficients)
            fixed_only = generalized_extreme(response_only, denominator, "max")
            fixed_without = generalized_extreme(
                response_without, denominator, "max"
            )
            fixed_flipped = generalized_extreme(
                response_flipped, denominator, "max"
            )
            fixed_v_only = gamma[index, index]
            fixed_v_without = _quadratic(v, response_without)
            fixed_v_flipped = _quadratic(v, response_flipped)
            source_rows.append(
                {
                    "name": name,
                    **metadata[name],
                    "extremizer_signed_amplitude": _mpstr(amplitudes[name]),
                    "extremizer_net_amplitude_fraction": _safe_ratio(
                        amplitudes[name], net_cross
                    ),
                    "extremizer_Ainverse_diagonal_response": _mpstr(
                        fixed_v_only
                    ),
                    "old_old_block_max_abs": _mpstr(
                        _max_abs(old_sources[name])
                    ),
                    "cross_reflection_symmetry_max_abs": _mpstr(
                        _max_abs(_reflect_cross(bs, collar_degree) - bs)
                    ),
                    "fixed_old_metric": {
                        "source_only_reoptimized_ward_ratio": _mpstr(fixed_only),
                        "source_removed_reoptimized_ward_ratio": _mpstr(
                            fixed_without
                        ),
                        "source_sign_flipped_reoptimized_ward_ratio": _mpstr(
                            fixed_flipped
                        ),
                        "source_only_at_actual_extremizer": _mpstr(fixed_v_only),
                        "source_removed_at_actual_extremizer": _mpstr(
                            fixed_v_without
                        ),
                        "source_sign_flipped_at_actual_extremizer": _mpstr(
                            fixed_v_flipped
                        ),
                    },
                    "source_consistent": (
                        {
                            "removed": _metric_variant(
                                a - old_sources[name], without, denominator, go
                            ),
                            "sign_flipped": _metric_variant(
                                a - 2 * old_sources[name], flipped, denominator, go
                            ),
                        }
                        if include_consistent_variants
                        else {
                            "status": "SKIPPED_SECONDARY_OLD_METRIC_PERTURBATION"
                        }
                    ),
                }
            )

        # Group powers of the same underlying prime; in particular n=2 and
        # n=4 should not be mistaken for independent Euler-product sources.
        underlying_groups: dict[int, list[str]] = {}
        for name in source_names:
            prime = metadata[name].get("underlying_prime")
            if prime is not None:
                underlying_groups.setdefault(prime, []).append(name)
        grouped_rows = []
        for prime, names in sorted(underlying_groups.items()):
            bg = _source_group(names, b_sources)
            ag = _source_group(names, old_sources)
            without = btotal - bg
            flipped = btotal - 2 * bg
            group_coefficients = {source: 0 for source in source_names}
            without_coefficients = dict(physical_coefficients)
            flipped_coefficients = dict(physical_coefficients)
            for name in names:
                group_coefficients[name] = 1
                without_coefficients[name] = 0
                flipped_coefficients[name] = -1
            grouped_rows.append(
                {
                    "underlying_prime": prime,
                    "source_names": names,
                    "fixed_old_metric": {
                        "group_only_reoptimized_ward_ratio": _mpstr(
                            generalized_extreme(
                                fixed_response(group_coefficients), denominator, "max"
                            )
                        ),
                        "group_removed_reoptimized_ward_ratio": _mpstr(
                            generalized_extreme(
                                fixed_response(without_coefficients), denominator, "max"
                            )
                        ),
                        "group_sign_flipped_reoptimized_ward_ratio": _mpstr(
                            generalized_extreme(
                                fixed_response(flipped_coefficients), denominator, "max"
                            )
                        ),
                    },
                    "source_consistent": (
                        {
                            "removed": _metric_variant(
                                a - ag, without, denominator, go
                            ),
                            "sign_flipped": _metric_variant(
                                a - 2 * ag, flipped, denominator, go
                            ),
                        }
                        if include_consistent_variants
                        else {
                            "status": "SKIPPED_SECONDARY_OLD_METRIC_PERTURBATION"
                        }
                    ),
                }
            )

        # Resolve the actual maximizing collar mode against the smallest old
        # generalized eigenvalues.  These beta rows show whether the completed
        # source sum cancels before division by a microscopic lambda_k.
        mode_count = min(old_degree, low_mode_count)
        lambdas, old_vectors = hp_lam_min(
            a, go, nev=mode_count, dps=dps, vectors=True
        )
        denominator_chol = mp.cholesky(denominator)
        denominator_whitener = _solve_left(
            denominator_chol.T, mp.eye(denominator.rows)
        )
        scaled_source_gram = mp.matrix(len(source_names))
        low_modes = []
        for mode, (lam, coefficients) in enumerate(zip(lambdas, old_vectors)):
            eigenvector = mp.matrix(coefficients)
            beta_sources = {
                name: (eigenvector.T * source_vectors[name])[0]
                for name in source_names
            }
            beta_total = sum(beta_sources.values())
            beta_abs = sum(abs(value) for value in beta_sources.values())
            operator_rows = {
                name: eigenvector.T * b_sources[name] * denominator_whitener
                for name in source_names
            }
            combined_operator_row = mp.matrix(1, denominator.rows)
            for row in operator_rows.values():
                combined_operator_row += row
            operator_norms = {
                name: mp.sqrt(sum(row[j] * row[j] for j in range(row.cols)))
                for name, row in operator_rows.items()
            }
            combined_operator_norm = mp.sqrt(
                sum(
                    combined_operator_row[j] * combined_operator_row[j]
                    for j in range(combined_operator_row.cols)
                )
            )
            for source_i, left_name in enumerate(source_names):
                for source_j, right_name in enumerate(source_names):
                    scaled_source_gram[source_i, source_j] += sum(
                        operator_rows[left_name][column]
                        * operator_rows[right_name][column]
                        / lam
                        for column in range(denominator.rows)
                    )
            low_modes.append(
                {
                    "mode": mode,
                    "lambda": _mpstr(lam),
                    "beta_total": _mpstr(beta_total),
                    "beta_total_over_lambda": _mpstr(beta_total / lam),
                    "beta_total_over_sqrt_lambda": _mpstr(
                        beta_total / mp.sqrt(lam)
                    ),
                    "beta_sources": {
                        name: _mpstr(value) for name, value in beta_sources.items()
                    },
                    "source_cancellation_factor": (
                        None if beta_total == 0 else _mpstr(beta_abs / abs(beta_total))
                    ),
                    "response_contribution": _mpstr(beta_total * beta_total / lam),
                    "response_fraction": _safe_ratio(
                        beta_total * beta_total / lam, theta
                    ),
                    "poisson_mode_identity_error": _mpstr(
                        beta_total
                        - lam
                        * (
                            eigenvector.T
                            * go
                            * poisson_difference
                            * v
                        )[0]
                    ),
                    "operator_row_combined_budget": _mpstr(
                        combined_operator_norm * combined_operator_norm / lam
                    ),
                    "operator_row_source_budgets": {
                        name: _mpstr(norm * norm / lam)
                        for name, norm in operator_norms.items()
                    },
                    "operator_row_cancellation_factor": (
                        None
                        if combined_operator_norm == 0
                        else _mpstr(
                            sum(operator_norms.values()) / combined_operator_norm
                        )
                    ),
                }
            )

        scaled_values, scaled_vectors = mp.eigsy(_symmetrize(scaled_source_gram))
        scaled_min_index = min(
            range(scaled_values.rows), key=lambda index: scaled_values[index]
        )
        scaled_max_index = max(
            range(scaled_values.rows), key=lambda index: scaled_values[index]
        )
        near_null = mp.matrix(
            [scaled_vectors[i, scaled_min_index] for i in range(len(source_names))]
        )
        physical_source_vector = mp.matrix([mp.mpf(1) for _ in source_names])
        physical_source_vector /= mp.sqrt(len(source_names))
        if (near_null.T * physical_source_vector)[0] < 0:
            near_null *= -1
        near_null_alignment = abs((near_null.T * physical_source_vector)[0])
        physical_low_mode_budget = _quadratic(
            mp.matrix([mp.mpf(1) for _ in source_names]), scaled_source_gram
        )

        plus = _parity_basis(collar_degree, +1)
        minus = _parity_basis(collar_degree, -1)
        theta_even = generalized_extreme(
            plus.T * response * plus, plus.T * denominator * plus, "max"
        )
        theta_odd = generalized_extreme(
            minus.T * response * minus, minus.T * denominator * minus, "max"
        )
        reflected = _reflect_collar(v, collar_degree)
        even_part = (v + reflected) / 2
        odd_part = (v - reflected) / 2
        even_mass = _quadratic(even_part, denominator)
        odd_mass = _quadratic(odd_part, denominator)
        parity_cross = _quadratic(even_part, denominator, odd_part)

        # A coefficient-preserving outward p5 smear leaves the old p5 block
        # exactly zero, unlike a symmetric inward/outward smoothing.  This is
        # therefore a clean test of sensitivity to the threshold contact atom.
        pseudonode = None
        p5_name = f"prime_power_{event_prime}"
        if p5_name in b_sources:
            base_shift = mp.log(event_prime)
            p5_weight = 2 * mp.log(event_prime) / mp.sqrt(event_prime)
            smear_width = delta_mp / 4
            b_without_p5 = btotal - b_sources[p5_name]
            solved_without_p5 = mp.matrix(btotal.rows, btotal.cols)
            for name in source_names:
                if name != p5_name:
                    solved_without_p5 += solved_b_sources[name]

            def p5_replacement_response(replacement: mp.matrix) -> mp.matrix:
                solved_replacement = _cholesky_solve(a_chol, replacement)
                return _symmetrize(
                    b_without_p5.T * solved_without_p5
                    + b_without_p5.T * solved_replacement
                    + replacement.T * solved_without_p5
                    + replacement.T * solved_replacement
                )

            shift_rows = []
            for fraction in (0, mp.mpf("0.125"), mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.75"), 1):
                shift = base_shift + mp.mpf(fraction) * smear_width
                raw_shifted = prime_translation_matrix(
                    centers, widths, shift, p5_weight
                )
                roo_shifted, roc_shifted, _ = _corrected_blocks(
                    raw_shifted, old, collar, correction
                )
                b_shifted = roc_shifted - roo_shifted * k
                shift_rows.append(
                    {
                        "outward_fraction_of_delta_over_4": _mpstr(
                            mp.mpf(fraction)
                        ),
                        "shift": _mpstr(shift),
                        "old_old_max_abs": _mpstr(_max_abs(roo_shifted)),
                        "fixed_old_metric_ward_ratio": _mpstr(
                            generalized_extreme(
                                p5_replacement_response(b_shifted), denominator, "max"
                            )
                        ),
                    }
                )
            raw_smear = mp.matrix(qfull.rows)
            for node in range(smear_nodes):
                offset = (mp.mpf(node) + mp.mpf("0.5")) * smear_width / smear_nodes
                raw_smear += prime_translation_matrix(
                    centers, widths, base_shift + offset, p5_weight
                ) / smear_nodes
            roo_smear, roc_smear, _ = _corrected_blocks(
                raw_smear, old, collar, correction
            )
            b_smear = roc_smear - roo_smear * k
            pseudonode = {
                "description": "Equal-weight midpoint smear of the p5 atom outward over [log(5), log(5)+delta/4].",
                "node_count": smear_nodes,
                "coefficient_mass_ratio": "1.0",
                "old_old_max_abs": _mpstr(_max_abs(roo_smear)),
                "fixed_old_metric_ward_ratio": _mpstr(
                    generalized_extreme(
                        p5_replacement_response(b_smear), denominator, "max"
                    )
                ),
                "shift_sweep": shift_rows,
            }

        p5_weight_scan = None
        if p5_name in b_sources:
            p5_weight_scan = []
            for alpha in (-1, 0, mp.mpf("0.5"), mp.mpf("0.9"), 1, mp.mpf("1.1"), mp.mpf("1.5"), 2):
                coefficients = dict(physical_coefficients)
                coefficients[p5_name] = mp.mpf(alpha)
                p5_weight_scan.append(
                    {
                        "p5_coefficient_multiplier": _mpstr(mp.mpf(alpha)),
                        "fixed_old_metric_ward_ratio": _mpstr(
                            generalized_extreme(
                                fixed_response(coefficients), denominator, "max"
                            )
                        ),
                    }
                )

        # Global reversal B -> -B is invisible to B^*A^{-1}B, so fix the
        # first source coefficient to +1 and enumerate the remaining signs.
        sign_pattern_rows = []
        first_name = source_names[0]
        for tail_signs in itertools.product((-1, 1), repeat=len(source_names) - 1):
            signs = {first_name: 1}
            signs.update(
                {name: sign for name, sign in zip(source_names[1:], tail_signs)}
            )
            pattern_ratio = generalized_extreme(
                fixed_response(signs), denominator, "max"
            )
            sign_pattern_rows.append(
                {
                    "signs_relative_to_physical_source_blocks": signs,
                    "ward_ratio": _mpstr(pattern_ratio),
                }
            )
        sign_pattern_rows.sort(key=lambda row: mp.mpf(row["ward_ratio"]))
        physical_pattern_rank = next(
            index + 1
            for index, row in enumerate(sign_pattern_rows)
            if all(sign == 1 for sign in row["signs_relative_to_physical_source_blocks"].values())
        )

        source_sum_error = _max_abs(raw_total - (qfull - hfull))
        b_sum_error = _max_abs(btotal - xtilde)
        gamma_sum = sum(gamma[i, j] for i in range(gamma.rows) for j in range(gamma.cols))
        reflection_old = mp.matrix(
            [[a[old_degree - 1 - i, old_degree - 1 - j] for j in range(old_degree)] for i in range(old_degree)]
        )
        reflected_b = _reflect_cross(btotal, collar_degree)
        reflected_denominator = mp.matrix(
            [
                [
                    denominator[
                        (i + collar_degree) % (2 * collar_degree),
                        (j + collar_degree) % (2 * collar_degree),
                    ]
                    for j in range(2 * collar_degree)
                ]
                for i in range(2 * collar_degree)
            ]
        )

        return {
            "status": "FINITE_DIAGNOSTIC_ONLY",
            "event_prime": event_prime,
            "old_degree": old_degree,
            "collar_degree_each_side": collar_degree,
            "delta_project_support": _mpstr(delta_mp),
            "old_project_support": _mpstr(lold),
            "new_project_support": _mpstr(lnew),
            "dps": dps,
            "included_source_consistent_old_metric_variants": include_consistent_variants,
            "active_sources": source_names,
            "ward_ratio": _mpstr(theta),
            "ward_second_generalized_eigenvalue": (
                None if second_theta is None else _mpstr(second_theta)
            ),
            "ward_absolute_eigengap": (
                None if second_theta is None else _mpstr(theta - second_theta)
            ),
            "ward_relative_eigengap": (
                None
                if second_theta is None or theta == 0
                else _mpstr((theta - second_theta) / abs(theta))
            ),
            "old_generalized_floor": _mpstr(min(lambdas)),
            "extremizer": {
                "JstarGJ_normalization": _mpstr(denominator_value),
                "old_Q_energy": _mpstr(old_energy),
                "net_cross_amplitude": _mpstr(net_cross),
                "HRW_prime_ratio": _mpstr(
                    net_cross * net_cross / (old_energy * denominator_value)
                ),
                "old_L2_mass": _mpstr(old_l2),
                "old_Q_over_L2_Rayleigh": _mpstr(old_energy / old_l2),
                "collar_coefficients": _vector_strings(harmonic_collar),
                "physical_old_harmonic_coefficients": _vector_strings(harmonic_old),
                "old_response_coefficients": _vector_strings(u),
            },
            "poisson_extension_reformulation": {
                "identity": "B=A*(P_Q-P_h), with P_Q=A^-1*X and P_h=H^-1*Y",
                "interpretation": "The Ward response is the old Q-energy of the mismatch between the Q-harmonic and reference-harmonic lifts.",
                "q_harmonic_schur_over_reference_S_min": _mpstr(
                    generalized_extreme(
                        q_harmonic_schur, reference_harmonic_schur, "min"
                    )
                ),
                "q_energy_at_h_lift_over_reference_S_max": _mpstr(
                    generalized_extreme(
                        q_energy_at_reference_harmonic_lift,
                        reference_harmonic_schur,
                        "max",
                    )
                ),
            },
            "parity": {
                "even_ward_ratio": _mpstr(theta_even),
                "odd_ward_ratio": _mpstr(theta_odd),
                "dominant_sector": "even" if theta_even >= theta_odd else "odd",
                "extremizer_even_reference_mass": _mpstr(even_mass),
                "extremizer_odd_reference_mass": _mpstr(odd_mass),
                "even_odd_reference_cross": _mpstr(parity_cross),
                "reference_reflection_correlation": _mpstr(
                    _quadratic(v, denominator, reflected)
                ),
            },
            "source_attribution": {
                "sum_abs_signed_amplitudes_over_net": _safe_ratio(
                    absolute_amplitude_sum, abs(net_cross)
                ),
                "sum_Ainverse_source_diagonals_over_net": _safe_ratio(
                    diagonal_response_sum, net_cross
                ),
                "vector_cancellation_factor": _safe_ratio(
                    sum(mp.sqrt(max(mp.mpf(0), gamma[i, i])) for i in range(gamma.rows)),
                    mp.sqrt(theta),
                ),
                "sources": source_rows,
                "pairwise_Ainverse_gram_source_order": source_names,
                "pairwise_Ainverse_gram": [
                    [_mpstr(gamma[i, j]) for j in range(gamma.cols)]
                    for i in range(gamma.rows)
                ],
                "underlying_prime_groups": grouped_rows,
            },
            "low_old_modes_at_extremizer": low_modes,
            "low_mode_source_scaling": {
                "mode_count": mode_count,
                "source_order": source_names,
                "scaled_source_gram": [
                    [
                        _mpstr(scaled_source_gram[i, j])
                        for j in range(scaled_source_gram.cols)
                    ]
                    for i in range(scaled_source_gram.rows)
                ],
                "smallest_eigenvalue": _mpstr(
                    scaled_values[scaled_min_index]
                ),
                "largest_eigenvalue": _mpstr(
                    scaled_values[scaled_max_index]
                ),
                "near_null_source_scaling_vector": _vector_strings(near_null),
                "alignment_with_physical_all_ones_vector": _mpstr(
                    near_null_alignment
                ),
                "physical_all_ones_low_mode_budget": _mpstr(
                    physical_low_mode_budget
                ),
            },
            "p5_outward_pseudonode_falsifier": pseudonode,
            "p5_coefficient_scan": p5_weight_scan,
            "all_source_sign_patterns_fixed_old_metric": {
                "global_sign_quotiented": True,
                "pattern_count": len(sign_pattern_rows),
                "physical_pattern_rank_from_smallest": physical_pattern_rank,
                "rows": sign_pattern_rows,
            },
            "checks": {
                "geometry_old_support_error": _mpstr(geometry_lold - lold),
                "geometry_new_support_error": _mpstr(geometry_lnew - lnew),
                "raw_source_reconstruction_max_abs": _mpstr(source_sum_error),
                "harmonic_cross_source_reconstruction_max_abs": _mpstr(
                    b_sum_error
                ),
                "pairwise_response_reconstruction_max_abs": _mpstr(
                    _max_abs(response - direct_response)
                ),
                "poisson_difference_response_identity_max_abs": _mpstr(
                    _max_abs(response - response_from_poisson_difference)
                ),
                "Q_poisson_cross_identity_max_abs": _mpstr(
                    _max_abs(x - a * q_poisson)
                ),
                "poisson_energy_decomposition_max_abs": _mpstr(
                    _max_abs(
                        q_energy_at_reference_harmonic_lift
                        - q_harmonic_schur
                        - response
                    )
                ),
                "ward_eigenvalue_minus_old_energy": _mpstr(theta - old_energy),
                "old_energy_minus_net_cross": _mpstr(old_energy - net_cross),
                "pairwise_gamma_sum_minus_old_energy": _mpstr(
                    gamma_sum - old_energy
                ),
                "old_reflection_symmetry_max_abs": _mpstr(
                    _max_abs(reflection_old - a)
                ),
                "cross_reflection_symmetry_max_abs": _mpstr(
                    _max_abs(reflected_b - btotal)
                ),
                "denominator_reflection_symmetry_max_abs": _mpstr(
                    _max_abs(reflected_denominator - denominator)
                ),
                "parity_max_minus_ward_eigenvalue": _mpstr(
                    max(theta_even, theta_odd) - theta
                ),
            },
        }


def parse_cases(text: str) -> list[tuple[int, int, str]]:
    cases = []
    for item in text.split(","):
        old, collar, delta = item.split(":")
        cases.append((int(old), int(collar), delta))
    return cases


def run_source_audit(
    cases: list[tuple[int, int, str]],
    dps: int,
    event_prime: int = 5,
    low_mode_count: int = 12,
    smear_nodes: int = 9,
    include_consistent_variants: bool = False,
) -> dict:
    rows = [
        analyze_source_resolved_ward(
            old,
            collar,
            delta,
            dps=dps,
            event_prime=event_prime,
            low_mode_count=low_mode_count,
            smear_nodes=smear_nodes,
            include_consistent_variants=include_consistent_variants,
        )
        for old, collar, delta in cases
    ]
    return {
        "schema": "zeta23.ward_source_extremizer_probe.v1",
        "interpretation": (
            "Cutoff-free high-precision finite Galerkin evidence only. Fixed-old-"
            "metric source ablations diagnose cross-channel cancellation; they are "
            "not modified-zeta theorems. Matched refinement is mandatory."
        ),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", default="40:1:0.32,48:2:0.4")
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument("--event-prime", type=int, default=5)
    parser.add_argument("--low-mode-count", type=int, default=12)
    parser.add_argument("--smear-nodes", type=int, default=9)
    parser.add_argument(
        "--consistent-variants",
        action="store_true",
        help="also recompute secondary ablations after changing the old metric",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = run_source_audit(
        parse_cases(args.cases),
        args.dps,
        args.event_prime,
        args.low_mode_count,
        args.smear_nodes,
        args.consistent_variants,
    )
    rendered = json.dumps(payload, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
