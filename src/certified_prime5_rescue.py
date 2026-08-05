#!/usr/bin/env python3
"""Software-interval certificate for the first prime-event rescue.

At ``L = 327/100`` the only newly active prime place beyond ``{2, 3}`` is 5.
In the 12-dimensional Legendre Ritz space this script certifies that

* the ``{2, 3}`` form has an explicit negative rational test vector;
* the prime-5 correction is positive on that same vector; and
* the completed ``{2, 3, 5}`` matrix is positive definite, with generalized
  lower bound ``10^-9`` relative to the exact Legendre Gram matrix.

This is a finite-dimensional, software-assisted interval theorem.  It is not
an operator-level positivity result and does not provide a support-uniform
prime-event mechanism.
"""

from __future__ import annotations

from fractions import Fraction

import mpmath as mp
from mpmath import iv

from certified_margins import F2iv, iv_cholesky_pd
from certified_spectral import certified_spectral_form
from spectral_margins import spectral_form, spectral_lam_min


SUPPORT = Fraction(327, 100)
DIMENSION = 12
LOWER_BOUND = Fraction(1, 10**9)


def rational_old_negative_vector() -> list[Fraction]:
    """Rationalize a high-precision scout vector in the unnormalized basis."""
    scout = spectral_form(
        float(SUPPORT),
        DIMENSION,
        dps=50,
        prime_set={2, 3},
    )
    _, vectors = spectral_lam_min(scout, nev=1, dps=50, vectors=True)
    half_length = mp.mpf(SUPPORT.numerator) / SUPPORT.denominator / 4
    return [
        Fraction(
            float(vectors[0][k] * mp.sqrt((2 * k + 1) / (2 * half_length)))
        ).limit_denominator(10**12)
        for k in range(DIMENSION)
    ]


def interval_rayleigh(
    matrix: list[list[iv.mpf]],
    gram: list[Fraction],
    vector: list[Fraction],
) -> iv.mpf:
    coeffs = [F2iv(value) for value in vector]
    numerator = iv.mpf(0)
    denominator = iv.mpf(0)
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            numerator += coeffs[i] * matrix[i][j] * coeffs[j]
        denominator += coeffs[i] * coeffs[i] * F2iv(gram[i])
    return numerator / denominator


def main() -> None:
    iv.prec = 220
    full, gram = certified_spectral_form(SUPPORT, DIMENSION)
    old, old_gram = certified_spectral_form(
        SUPPORT,
        DIMENSION,
        prime_set={2, 3},
    )
    if gram != old_gram:
        raise RuntimeError("the exact Gram matrices differ")

    shifted = [
        [
            full[i][j]
            - (F2iv(LOWER_BOUND * gram[i]) if i == j else iv.mpf(0))
            for j in range(DIMENSION)
        ]
        for i in range(DIMENSION)
    ]
    full_positive = iv_cholesky_pd(shifted)

    vector = rational_old_negative_vector()
    event = [
        [full[i][j] - old[i][j] for j in range(DIMENSION)]
        for i in range(DIMENSION)
    ]
    old_value = interval_rayleigh(old, gram, vector)
    event_value = interval_rayleigh(event, gram, vector)
    full_value = interval_rayleigh(full, gram, vector)

    print(f"support={SUPPORT} dimension={DIMENSION}")
    print(f"full generalized lower bound > {float(LOWER_BOUND):.12e}: {full_positive}")
    print(
        "old {2,3} witness Rayleigh interval: "
        f"[{float(old_value.a):.12e}, {float(old_value.b):.12e}]"
    )
    print(
        "prime-5 event witness Rayleigh interval: "
        f"[{float(event_value.a):.12e}, {float(event_value.b):.12e}]"
    )
    print(
        "full witness Rayleigh interval: "
        f"[{float(full_value.a):.12e}, {float(full_value.b):.12e}]"
    )

    if not full_positive:
        raise RuntimeError("the full positivity certificate failed")
    if not old_value.b < 0:
        raise RuntimeError("the old negative-witness certificate failed")
    if not event_value.a > 0:
        raise RuntimeError("the event-rescue certificate failed")


if __name__ == "__main__":
    main()
