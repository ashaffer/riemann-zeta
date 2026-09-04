#!/usr/bin/env python3
"""Replay the nonpole near-residue transfer obstruction.

This verifies finite algebra and the exponent ledger only.  It does not
estimate cousin primes, reprove Vaughan's theorem, or prove a zero-free strip.
"""

from __future__ import annotations

import math
from fractions import Fraction

import mpmath as mp


mp.mp.dps = 80


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(left: mp.mpf, right: mp.mpf, tolerance: str = "1e-55") -> None:
    if abs(left - right) > mp.mpf(tolerance):
        raise AssertionError(f"{left!s} != {right!s}")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for divisor in range(3, math.isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def carrier_kappa() -> mp.mpf:
    alpha = mp.mpf(47) / 100
    depth = mp.mpf(133) / 200
    bw = mp.mpf(".10076")
    y = mp.pi * bw / (alpha * (2 * depth - 1))
    response = (y * mp.log(1 + y**-2) + 2 * mp.atan(y)) / mp.pi
    return alpha * (depth - mp.mpf(".5")) * (1 - response) / depth


def main() -> None:
    theta = mp.mpf(397) / 2500
    beta = mp.mpf(799) / 5000
    natural_denominator = mp.mpf(33) / 133
    kappa = carrier_kappa()

    require(theta < beta < natural_denominator, "nonpole denominator shell")
    close(
        kappa,
        mp.mpf(".0175222684497434081049372283207859393"),
        "1e-37",
    )

    # Global Vaughan is the optimistic one-prime input.  At the bottom shell
    # the q^(-1/2) term is binding: beta/2 is smaller than both the 1/5
    # term and the (1-beta)/2 term.  Thus this is the largest admissible
    # transfer loss from that theorem.
    vaughan_saving = beta / 2
    require(vaughan_saving < mp.mpf(1) / 5,
            "Vaughan four-fifths term is nonbinding")
    require(vaughan_saving < (1 - beta) / 2,
            "Vaughan square-root-q term is nonbinding")
    allowed_loss = vaughan_saving - kappa
    near_pole_overrun = beta - allowed_loss
    require(allowed_loss > 0, "Vaughan has some nominal room")
    require(beta > allowed_loss, "a q-sized condition number cannot fit")
    close(
        allowed_loss,
        mp.mpf(".0623777315502565918950627716792140607"),
        "1e-37",
    )
    close(near_pole_overrun, beta / 2 + kappa)

    # Exact odd-lattice edge transfer.  For q == 3 (mod 4), a=(q+1)/4 and
    # g=4, one has 4a == 1 (mod q), but never an exact recurrence.
    for q in (7, 11, 19, 43, 103, 10007, 1000003):
        require(is_prime(q) and q % 4 == 3, f"bad test prime {q}")
        a = (q + 1) // 4
        g = 4
        require(math.gcd(a, q) == 1 and q > g, "reduced nonpole example")
        require((a * g) % q == 1, "least residue is one")

        z = mp.e ** (2j * mp.pi * a / q)
        p = 1
        trapezoid = g * z**p * (1 + z**g) / 2
        odd_block = z**p * (1 + z**2)
        direct = abs(trapezoid / odd_block)
        formula = 4 * mp.cos(mp.pi / (2 * q)) * mp.cot(mp.pi / q)
        close(direct, formula, "1e-50")

        # General sharp universal bound for a nonzero residue.
        require(direct <= g * mp.cot(mp.pi / q), "cotangent upper bound")

        # The nearby low rational is 1/4, at exact distance 1/(4q).
        require(Fraction(a, q) - Fraction(1, 4) == Fraction(1, 4 * q),
                "near-quarter identity")

    q = 1000003
    a = (q + 1) // 4
    z = mp.e ** (2j * mp.pi * a / q)
    condition = abs((4 * z * (1 + z**4) / 2) / (z * (1 + z**2)))
    require(abs(condition / q - 4 / mp.pi) < mp.mpf("1e-5"),
            "q-sized asymptotic condition number")

    # At height t=Y^A, eta=Y^(-33/133).  Since b<33/133, q*eta=o(1),
    # so even residue one lies outside its associated low-denominator cell.
    require(beta - natural_denominator < 0, "q eta tends to zero")

    # Freezing a fixed physical gap in t log x has phase error
    # O(t*g^2/Y^2); at the top aperture this saves 2-A=66/133.
    aperture = mp.mpf(200) / 133
    fixed_gap_freezing_saving = 2 - aperture
    close(fixed_gap_freezing_saving, mp.mpf(66) / 133)
    require(fixed_gap_freezing_saving > kappa,
            "fixed-gap logarithmic freezing error")

    # To reduce q/r to the admissible loss, residue r would have to be at
    # least Y^(b/2+kappa); the cover supplies no positive-power exclusion.
    required_residue_exponent = beta - allowed_loss
    close(required_residue_exponent, near_pole_overrun)
    require(required_residue_exponent > mp.mpf(".0974"),
            "missing small-residue exclusion")

    # Even an unrealistically favorable gap-size scalarization cannot combine
    # Vaughan with the current positive Gafni--Tao tail.  That tail starts at
    # lambda=2/15, already beyond the entire beta/2 cancellation budget.
    gt_branch_start = mp.mpf(2) / 15
    optimistic_short_saving = beta / 2 - gt_branch_start
    require(optimistic_short_saving < 0 < kappa,
            "no admissible positive-tail split")
    formal_crossing = mp.mpf(13) / 22 * (beta / 2 + mp.mpf(6) / 65)
    require(formal_crossing < gt_branch_start,
            "formal split optimizer lies outside the proved tail branch")

    # For p>3, p and p+4 prime force p+2 composite modulo 3; hence this is
    # an exact consecutive-gap sector, not a pseudoprime countermodel.
    primes = [n for n in range(5, 500) if is_prime(n)]
    consecutive_four = {primes[j] for j in range(len(primes) - 1)
                        if primes[j + 1] - primes[j] == 4}
    cousin_four = {p for p in primes if is_prime(p + 4) and p + 4 < 500}
    require(consecutive_four == cousin_four, "gap-four/cousin identity")

    print("PASS nonpole near-residue transfer fail-fast")
    print(f"kappa={mp.nstr(kappa, 18)}")
    print(f"theta={mp.nstr(theta, 8)} beta={mp.nstr(beta, 8)}")
    print(f"allowed Vaughan transfer loss={mp.nstr(allowed_loss, 18)}")
    print(f"q-loss overrun={mp.nstr(near_pole_overrun, 18)}")
    print(f"required residue exponent={mp.nstr(required_residue_exponent, 18)}")
    print(f"natural denominator exponent={mp.nstr(natural_denominator, 18)}")


if __name__ == "__main__":
    main()
