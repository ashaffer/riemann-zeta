"""Numerical falsification screen for the CCM even-ground hypothesis.

This uses the high-precision Legendre Galerkin realization of the actual zeta
Weil form, splits it by reflection parity, and reports the two lowest block
eigenvalues.  It is diagnostic only: Galerkin values are not uniform operator
bounds and do not prove simplicity or parity ordering.
"""

import argparse
import mpmath as mp

from spectral_margins import spectral_form, spectral_lam_min


def parity_block(matrix, parity):
    indices = list(range(parity, matrix.rows, 2))
    return mp.matrix([[matrix[i, j] for j in indices] for i in indices])


def scan(supports, dimension=16, dps=35):
    mp.mp.dps = dps
    print("support,even_min,even_second,odd_min,odd_second,parity_gap")
    for support_text in supports:
        support = mp.mpf(support_text)
        matrix = spectral_form(support, dimension, dps=dps)
        even = spectral_lam_min(parity_block(matrix, 0), 2, dps=dps - 5)
        odd = spectral_lam_min(parity_block(matrix, 1), 2, dps=dps - 5)
        row = [support, even[0], even[1], odd[0], odd[1], odd[0] - even[0]]
        print(",".join(mp.nstr(value, 14) for value in row), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dimension", type=int, default=16)
    parser.add_argument("--dps", type=int, default=35)
    parser.add_argument(
        "supports",
        nargs="*",
        default=["1", "1.75", "2.485", "2.996", "3.555", "4", "5", "6", "8"],
    )
    args = parser.parse_args()
    scan(args.supports, args.dimension, args.dps)


if __name__ == "__main__":
    main()
