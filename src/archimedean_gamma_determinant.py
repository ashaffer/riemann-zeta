"""Check the degree-two zeta determinant underlying the gamma factor.

For A_s with formal spectrum {s+2n : n>=0},

  zeta_A(w) = 2^(-w) HurwitzZeta(w,s/2)

and det_zeta(A_s)=exp(-zeta_A'(0)).  The closed form is

  2^(1/2-s/2) sqrt(2*pi) / Gamma(s/2).

This is a normalization check for the proposed cyclotomic/THR archimedean
cohomology, not a construction of that cohomology.
"""
from __future__ import annotations

import argparse

import mpmath as mp


def determinant_from_derivative(s: complex) -> complex:
    a = s / 2
    zeta_a = lambda w: mp.power(2, -w) * mp.zeta(w, a)
    return mp.exp(-mp.diff(zeta_a, 0))


def determinant_closed(s: complex) -> complex:
    return (mp.power(2, mp.mpf("0.5") - s / 2)
            * mp.sqrt(2 * mp.pi) / mp.gamma(s / 2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument("--points", nargs="+", type=complex,
                        default=[0.5 + 3j, 1.25 + 0.7j, 2.0 + 5j])
    args = parser.parse_args()
    mp.mp.dps = args.dps
    print("s,relative_error,gamma_ratio_error")
    for raw in args.points:
        s = mp.mpc(raw)
        direct = determinant_from_derivative(s)
        closed = determinant_closed(s)
        relative = abs(direct / closed - 1)
        # completed gamma factor equals the inverse determinant times the
        # elementary normalization 2*sqrt(pi)*(2*pi)^(-s/2).
        recovered = ((1 / direct) * 2 * mp.sqrt(mp.pi)
                     * mp.power(2 * mp.pi, -s / 2))
        target = mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)
        gamma_error = abs(recovered / target - 1)
        print(f"{mp.nstr(s,12)},{mp.nstr(relative,8)},"
              f"{mp.nstr(gamma_error,8)}")


if __name__ == "__main__":
    main()
