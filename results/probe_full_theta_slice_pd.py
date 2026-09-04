"""High-precision probe for conditional full-theta slice positivity.

This is a numerical falsifier, not an interval certificate.  It evaluates

    H_0(T) = 4 integral_0^infinity Phi(v)^2 cos(2 T v) dv

in the Rodgers--Tao normalization.  Conditional-slice positive definiteness
would require H_0(T) >= 0 for every T.
"""

import mpmath as mp


mp.mp.dps = 50


def phi(u):
    """Exact theta series, using Phi(-u)=Phi(u) for stable evaluation."""
    u = abs(mp.mpf(u))
    e4 = mp.exp(4 * u)
    total = mp.mpf("0")
    for n in range(1, 150):
        term = (
            2 * mp.pi**2 * n**4 * mp.exp(9 * u)
            - 3 * mp.pi * n**2 * mp.exp(5 * u)
        ) * mp.exp(-mp.pi * n * n * e4)
        total += term
        if n > 5 and abs(term) < mp.mpf("1e-75"):
            break
    return total


def slice_transform(t):
    integrand = lambda v: 4 * phi(v) ** 2 * mp.cos(2 * t * v)
    mesh = [mp.mpf(k) / 20 for k in range(41)]
    return mp.fsum(
        mp.quad(integrand, [mesh[k], mesh[k + 1]])
        for k in range(len(mesh) - 1)
    )


if __name__ == "__main__":
    value = slice_transform(mp.mpf(30))
    print(mp.nstr(value, 40))
    print("integrand scale at cutoff:", mp.nstr(4 * phi(2) ** 2, 12))
