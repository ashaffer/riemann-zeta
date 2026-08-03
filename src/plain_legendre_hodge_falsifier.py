"""Cutoff-free finite-section falsifier for the strengthened Hodge row.

The basis consists of zero-extended, L2-normalized Legendre polynomials on
the old interval and on the two collar components.  The full relative space
is imposed before taking the corrected collar complement, so the collar
contains the old moment-lifting directions.  The gamma matrix is assembled
by the untruncated spatial Gauss--digamma identity and every prime shift by
exact polynomial-overlap quadrature.

For the new Weil block ``[[A,X],[X*,C]]`` and Hodge trace ``T``, this checks

    C - X* A^-1 X - T* T >= 0.

At the activation-5 defaults the displayed matrix has a stable negative
eigenvalue.  This falsifies that strengthened sufficient criterion; it does
not falsify the ordinary Weil row or RH.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from scipy.linalg import eigh as generalized_eigh

from event_cross_ratio import combined_basis
from hodge_event_scan import event_catalog
from legendre_hodge_crosscheck import relative_coordinates
from legendre_hodge_sector_scan import event_blocks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-power", type=int, default=5)
    parser.add_argument("--old-degree", type=int, default=32)
    parser.add_argument("--collar-degree", type=int, default=20)
    parser.add_argument("--xquad", type=int, default=128)
    parser.add_argument(
        "--mp-dps", type=int, default=0,
        help="also recompute both Schur minima with this many mp digits")
    parser.add_argument(
        "--output", type=Path,
        default=Path("results/plain-legendre-hodge-witness.npz"))
    args = parser.parse_args()

    catalog = event_catalog()
    positions = {n: index for index, (_, n, _, _) in enumerate(catalog)}
    position = positions[args.prime_power]
    event_support = catalog[position][3]
    old_support = (catalog[position - 1][3] + event_support) / 2
    new_support = (event_support + catalog[position + 1][3]) / 2
    old_radius = old_support / 4
    new_radius = new_support / 4

    (A, X, C, T, _, old_reflection, collar_reflection,
     old_scalar, event_scalar, basis_error, reflection_error,
     shell_isometry_error) = event_blocks(
        old_support, new_support, args.old_degree, args.collar_degree,
        0, args.xquad, 0.0, 1.0, 1)
    ordinary_schur = C - X.T @ np.linalg.solve(A, X)
    ordinary_schur = (ordinary_schur + ordinary_schur.T) / 2
    hodge_loss = T.T @ T
    strengthened_schur = ordinary_schur - hodge_loss
    strengthened_schur = (strengthened_schur
                          + strengthened_schur.T) / 2
    values, vectors = np.linalg.eigh(strengthened_schur)
    collar_witness = vectors[:, 0]
    old_correction = -np.linalg.solve(A, X @ collar_witness)
    relative_coefficients = np.concatenate([
        old_correction, collar_witness])
    coordinates, coordinate_error = relative_coordinates(
        old_support, new_support, args.old_degree, args.collar_degree,
        0, args.xquad)
    raw_legendre_coefficients = coordinates @ relative_coefficients

    total_cost = X.T @ np.linalg.solve(A, X) + hodge_loss
    generalized_values, generalized_vectors = generalized_eigh(total_cost, C)
    generalized_witness = generalized_vectors[:, -1]
    generalized_witness /= np.linalg.norm(generalized_witness)

    ordinary_on_witness = float(
        collar_witness @ ordinary_schur @ collar_witness)
    hodge_on_witness = float(collar_witness @ hodge_loss @ collar_witness)
    strengthened_on_witness = float(
        collar_witness @ strengthened_schur @ collar_witness)
    witness_parity = float(
        collar_witness @ collar_reflection @ collar_witness)

    x, wx, basis = combined_basis(
        old_radius, new_radius, args.old_degree, args.collar_degree,
        0, args.xquad)
    plus = (wx * np.exp(x / 2)) @ basis
    minus = (wx * np.exp(-x / 2)) @ basis
    plus_residual = float(plus @ raw_legendre_coefficients)
    minus_residual = float(minus @ raw_legendre_coefficients)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        args.output,
        prime_power=np.array(args.prime_power),
        old_support=np.array(old_support),
        new_support=np.array(new_support),
        old_radius=np.array(old_radius),
        new_radius=np.array(new_radius),
        old_degree=np.array(args.old_degree),
        collar_degree=np.array(args.collar_degree),
        xquad=np.array(args.xquad),
        old_scalar=np.array(old_scalar),
        event_scalar=np.array(event_scalar),
        A=A, X=X, C=C, T=T,
        ordinary_schur=ordinary_schur,
        hodge_loss=hodge_loss,
        strengthened_schur=strengthened_schur,
        collar_witness=collar_witness,
        old_correction=old_correction,
        relative_coefficients=relative_coefficients,
        raw_legendre_coefficients=raw_legendre_coefficients,
        generalized_witness=generalized_witness,
        old_reflection=old_reflection,
        collar_reflection=collar_reflection,
        basis_error=np.array(max(basis_error, coordinate_error)),
        reflection_error=np.array(reflection_error),
        shell_isometry_error=np.array(shell_isometry_error),
        plus_moment_residual=np.array(plus_residual),
        minus_moment_residual=np.array(minus_residual),
    )

    print(f"old_support={old_support:.15g}")
    print(f"new_support={new_support:.15g}")
    print(f"ordinary_row_ratio={generalized_eigh(X.T @ np.linalg.solve(A, X), C, eigvals_only=True)[-1]:.15g}")
    print(f"strengthened_row_ratio={generalized_values[-1]:.15g}")
    print(f"ordinary_schur_minimum={np.linalg.eigvalsh(ordinary_schur)[0]:.15g}")
    print(f"strengthened_schur_minimum={values[0]:.15g}")
    print(f"ordinary_on_negative_witness={ordinary_on_witness:.15g}")
    print(f"hodge_on_negative_witness={hodge_on_witness:.15g}")
    print(f"strengthened_on_negative_witness={strengthened_on_witness:.15g}")
    print(f"negative_witness_parity={witness_parity:.15g}")
    print(f"plus_moment_residual={plus_residual:.3e}")
    print(f"minus_moment_residual={minus_residual:.3e}")
    print(f"basis_error={max(basis_error, coordinate_error):.3e}")
    print(f"reflection_error={reflection_error:.3e}")
    print(f"shell_isometry_error={shell_isometry_error:.3e}")
    if args.mp_dps:
        import mpmath as mp

        mp.mp.dps = args.mp_dps

        def mp_matrix(array: np.ndarray) -> mp.matrix:
            return mp.matrix([
                [mp.mpf(float(array[i, j]))
                 for j in range(array.shape[1])]
                for i in range(array.shape[0])])

        mp_a, mp_x = mp_matrix(A), mp_matrix(X)
        mp_c, mp_t = mp_matrix(C), mp_matrix(T)
        solved = mp.matrix(mp_a.rows, mp_x.cols)
        for column in range(mp_x.cols):
            solution = mp.lu_solve(mp_a, mp_x[:, column])
            for row in range(mp_a.rows):
                solved[row, column] = solution[row]
        mp_ordinary = mp_c - mp_x.T * solved
        mp_strengthened = mp_ordinary - mp_t.T * mp_t
        ordinary_values, _ = mp.eigsy(
            (mp_ordinary + mp_ordinary.T) / 2)
        strengthened_values, _ = mp.eigsy(
            (mp_strengthened + mp_strengthened.T) / 2)
        print("mp_ordinary_schur_minimum="
              + mp.nstr(ordinary_values[0], args.mp_dps))
        print("mp_strengthened_schur_minimum="
              + mp.nstr(strengthened_values[0], args.mp_dps))
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
