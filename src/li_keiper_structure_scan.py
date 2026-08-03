"""Small, high-precision fail-fast tests for naive Li-coefficient moment structure.

This is diagnostic, not an RH verification.  It expands

    log xi(1 / (1-z)) = log xi(1) + sum_{n>=1} lambda_n z^n / n

and tests leading Hankel determinants of (lambda_n) and (lambda_n/n).
"""

from __future__ import annotations

import argparse
import mpmath as mp
import numpy as np


def xi(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def li_coefficients(count: int) -> list[mp.mpf]:
    def generating_function(z: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
        # Avoid the removable 0 * zeta(1) expression in xi(1).
        if z == 0:
            return mp.log(mp.mpf("0.5"))
        return mp.log(xi(1 / (1 - z)))

    coefficients = mp.taylor(generating_function, mp.mpf("0"), count)
    return [mp.mpf("0")] + [n * coefficients[n] for n in range(1, count + 1)]


def leading_hankel_determinants(sequence: list[mp.mpf], max_size: int) -> list[mp.mpf]:
    determinants = []
    for size in range(2, max_size + 1):
        matrix = mp.matrix(size)
        for row in range(size):
            for column in range(size):
                matrix[row, column] = sequence[row + column + 1]
        determinants.append(mp.det(matrix))
    return determinants


def forward_difference_rows(sequence: list[mp.mpf], max_order: int) -> list[list[mp.mpf]]:
    rows = []
    current = sequence[:]
    for _ in range(max_order):
        current = [current[index + 1] - current[index] for index in range(len(current) - 1)]
        rows.append(current)
    return rows


def zero_sum_toeplitz_eigenvalues(sequence: list[mp.mpf], size: int) -> np.ndarray:
    kernel = np.array(
        [[float(sequence[abs(row - column)]) for column in range(size)] for row in range(size)]
    )
    projection = np.eye(size) - np.ones((size, size)) / size
    return np.linalg.eigvalsh(projection @ kernel @ projection)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--max-hankel", type=int, default=6)
    parser.add_argument("--digits", type=int, default=80)
    parser.add_argument("--max-difference", type=int, default=6)
    parser.add_argument("--toeplitz-size", type=int, default=10)
    args = parser.parse_args()
    if args.count < 2 * args.max_hankel - 1:
        parser.error("count must be at least 2 * max-hankel - 1")

    mp.mp.dps = args.digits
    lambdas = li_coefficients(args.count)
    for n in range(1, min(args.count, 10) + 1):
        print(f"lambda[{n}] = {mp.nstr(lambdas[n], 30)}")

    for label, sequence in (
        ("lambda", lambdas),
        ("lambda/n", [mp.mpf("0")] + [lambdas[n] / n for n in range(1, len(lambdas))]),
    ):
        print(f"\nLeading Hankel determinants for {label}:")
        for size, determinant in enumerate(
            leading_hankel_determinants(sequence, args.max_hankel), start=2
        ):
            print(f"  size {size}: {mp.nstr(determinant, 20)}")

        print(f"\nForward-difference sign test for {label}:")
        for order, row in enumerate(
            forward_difference_rows(sequence, args.max_difference), start=1
        ):
            sample = row[: min(12, len(row))]
            bernstein_sample = [(-1) ** (order - 1) * value for value in sample]
            print(
                f"  order {order}: range [{mp.nstr(min(sample), 12)}, "
                f"{mp.nstr(max(sample), 12)}], Bernstein minimum "
                f"{mp.nstr(min(bernstein_sample), 12)}"
            )

        eigenvalues = zero_sum_toeplitz_eigenvalues(sequence, args.toeplitz_size)
        print(
            f"\nZero-sum Toeplitz eigenvalue range for {label}, size "
            f"{args.toeplitz_size}: [{eigenvalues[0]:.12g}, {eigenvalues[-1]:.12g}]"
        )


if __name__ == "__main__":
    main()
