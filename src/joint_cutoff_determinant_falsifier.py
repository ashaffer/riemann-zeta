#!/usr/bin/env python3
"""Certify that the ramp-evaluated cutoff-table determinant has no fixed sign.

For a cutoff ``Y`` the four Vaughan sectors form an outer-product table at
the Dirichlet-series level.  Applying the one-sided unit ramp entrywise need
not preserve rank one.  This script evaluates the resulting ``2 x 2`` table
for the natural moving cutoff ``Y=floor(X^(3/8))`` at ``X=70`` and ``X=80``.
Arb certifies opposite determinant signs, both with the full von Mangoldt
weight and after retaining actual primes only.

The calculation is a fail-fast test of an exterior-square positivity route;
it bears neither way on RH.  See
``results/JOINT-TYPE-II-CUTOFF-IDENTITY.md``.
"""

from __future__ import annotations

from flint import arb, ctx


CASES = ((70, 4), (80, 5))


def _mobius_up_to(limit: int) -> list[int]:
    mu = [1] * (limit + 1)
    prime = bytearray(b"\x01") * (limit + 1)
    prime[0:2] = b"\x00\x00"
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        for multiple in range(p, limit + 1, p):
            mu[multiple] *= -1
        square = p * p
        if square <= limit:
            for multiple in range(square, limit + 1, square):
                mu[multiple] = 0
            for multiple in range(square, limit + 1, p):
                prime[multiple] = 0
    mu[0] = 0
    return mu


def _von_mangoldt_up_to(limit: int, prime_only: bool = False) -> list[arb]:
    values = [arb(0) for _ in range(limit + 1)]
    composite = bytearray(limit + 1)
    for p in range(2, limit + 1):
        if composite[p]:
            continue
        log_p = arb(p).log()
        if prime_only:
            values[p] = log_p
        else:
            power = p
            while power <= limit:
                values[power] = log_p
                if power > limit // p:
                    break
                power *= p
        if p <= limit // p:
            for multiple in range(p * p, limit + 1, p):
                composite[multiple] = 1
    return values


def _unit_ramp_weights(scale: int) -> list[arb]:
    """Return ``n^-1/2 min(1,max(0,log(scale/n)))`` for ``n<=scale``."""
    log_scale = arb(scale).log()
    weights = [arb(0) for _ in range(scale + 1)]
    for n in range(1, scale):
        transition = log_scale - arb(n).log()
        if transition > 1:
            transition = arb(1)
        elif not transition > 0:
            raise RuntimeError("an interval straddles a ramp endpoint")
        weights[n] = transition / arb(n).sqrt()
    return weights


def certified_cutoff_table(
    scale: int, cutoff: int, dps: int = 50, prime_only: bool = False
) -> dict:
    """Return the Arb-certified ramp evaluation of the four cutoff sectors."""
    if dps < 20:
        raise ValueError("use at least 20 decimal digits")
    if not 1 < cutoff < scale:
        raise ValueError("require 1 < cutoff < scale")
    if not cutoff**8 <= scale**3 < (cutoff + 1) ** 8:
        raise ValueError("cutoff must equal floor(scale^(3/8))")
    ctx.dps = dps

    mu = _mobius_up_to(scale)
    mangoldt = _von_mangoldt_up_to(scale, prime_only=prime_only)
    weights = _unit_ramp_weights(scale)

    table = [[arb(0), arb(0)], [arb(0), arb(0)]]
    for d in range(1, scale + 1):
        if mu[d] == 0:
            continue
        row = int(d > cutoff)
        for b in range(2, scale // d + 1):
            if not mangoldt[b]:
                continue
            column = int(b > cutoff)
            coefficient = mu[d] * mangoldt[b]
            for m in range(1, scale // (d * b) + 1):
                table[row][column] += coefficient * weights[d * b * m]

    determinant = table[0][0] * table[1][1] - table[0][1] * table[1][0]
    return {
        "scale": scale,
        "cutoff": cutoff,
        "prime_only": prime_only,
        "table": table,
        "det": determinant,
    }


def certified_sign_flip(
    dps: int = 50, prime_only: bool = False
) -> tuple[dict, dict]:
    """Certify positive and negative determinants at the two fixed cases."""
    positive = certified_cutoff_table(*CASES[0], dps=dps, prime_only=prime_only)
    negative = certified_cutoff_table(*CASES[1], dps=dps, prime_only=prime_only)
    if not positive["det"] > 0:
        raise RuntimeError("the X=70 determinant is not certified positive")
    if not negative["det"] < 0:
        raise RuntimeError("the X=80 determinant is not certified negative")
    return positive, negative


def main() -> None:
    for prime_only in (False, True):
        print(f"prime_only={prime_only}")
        for result in certified_sign_flip(prime_only=prime_only):
            print(f"X={result['scale']} Y={result['cutoff']} det={result['det']}")
            print(f"table={result['table']}")


if __name__ == "__main__":
    main()
