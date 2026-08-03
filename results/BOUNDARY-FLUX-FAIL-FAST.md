# Boundary-flux fail-fast audit

Status: the proposed Poisson/Sonin Wronskian mechanism does not independently
orient the prime-inclusive boundary form; path demoted, 2026-08-01.

## 1. What can be derived

For the pole-free incidence operator `T_a`, moment map `M_a`, and boundary
Weyl matrix

`K_a(z)=M_a^*(T_a-z)^(-1)M_a`,

the constrained Euler--Lagrange equation gives an exact Schur reduction.  A
relative zero mode at zero is equivalent to a zero mode of `K_a(0)`, provided
`T_a` is invertible.  Reflection diagonalizes this matrix into even and odd
scalars.

There is also an exact determinant interpretation.  The matrix determinant
lemma gives

`det(T+r m m^*)=det(T)(1+r <m,T^(-1)m>)`.

Thus a Weyl scalar is the first logarithmic variation of a rank-one boundary
determinant.  This is the only canonical “boundary flux” supplied by the
nonlocal resolvent.

Unlike a Sturm--Liouville operator, `T_a` has continuum delays and prime
translations.  Integration by parts does not reduce its Green identity to
endpoint values: the prime ramps leave shifted interior traces and the gamma
kernel leaves a continuum of interior correlations.  Consequently there is
no local Wronskian whose orientation is fixed by endpoint geometry.

## 2. Sonin/Poisson limitation

Poisson summation supplies Fourier/inversion symmetry and the two moment
conditions.  It explains the parity diagonalization and the relative boundary
classes.  The proved Sonin trace positivity of Connes--Consani is the single
archimedean-place theorem.  With finite primes present, orienting the boundary
determinant is precisely their semilocal positivity problem, not a consequence
of the global Poisson identity alone.

Therefore the implications

`Poisson symmetry => k_even<0<k_odd`

and

`Poisson symmetry => negativeIndex(T)=1`

do not follow from any identified Green/Wronskian identity.

## 3. Arithmetic-coupling falsifier

To distinguish structural Poisson information from the exact arithmetic
balance, write

`T_a(r)=A_infinity-r P_prime`,

where `r=1` is the zeta normalization.  The Fourier symmetry, parity, support,
moment map, and nonlocal operator class remain unchanged as `r` varies.

`src/boundary_weyl_coupling_scan.py` shows that the inertia mechanism is not
protected under this deformation.  At support `2.485`, dimension `24`:

| prime coupling `r` | negative index of `T(r)` | relative minimum |
|---:|---:|---:|
| `0.9990` | 1 | `1.30e-4` |
| `0.9999` | 1 | `2.96e-5` |
| `1.0000` | 1 | `1.84e-5` |
| `1.0001` | 1 | `7.16e-6` |
| `1.0005` | 2 | `-3.79e-5` |
| `1.0010` | 2 | `-9.45e-5` |

Broader scans show additional negative directions on the other side at some
supports.  The Weyl scalar signs can remain `(-,+)` even after the relative
form has become negative; the load-bearing failure is then the change in the
negative index of `T`.

This proves that parity and ordinary Poisson inversion do not determine the
required inertia.  The exact von Mangoldt weights place the operator inside a
spectral-flow chamber whose boundary is a relative zero mode.

## 4. Verdict

The boundary-Weyl reduction remains a useful diagnostic and a compact
equivalent target, but the proposed proof mechanism fails its independence
test:

- the resolvent “flux” is a determinant derivative with no automatic sign;
- the nonlocal Green identity contains the original interior prime/gamma
  balance;
- the one-negative-direction assertion changes exactly at the forbidden
  relative zero modes;
- known Sonin positivity does not include the semilocal prime terms.

Proving the Weyl signs *and* the index-one theorem would prove relative Weil
positivity, but no separately oriented Wronskian has been found.  It should not
be counted as progress toward RH unless a new semilocal trace inequality is
introduced.

## 5. Surviving information

The relative moment reduction is still valuable: it removes the pole
signature and greatly improves numerical conditioning.  The inertia census
also gives an efficient counterexample/proof diagnostic.  What is pruned is
the claim that Poisson boundary orientation supplies the missing theorem for
free.

The next non-circular target should work at the semilocal trace level itself:
construct a monotone positive comparison between the Sonin compression before
and after adjoining one prime, or falsify that monotonicity at the first prime
activation.  This asks for a new operator inequality rather than another
resolvent reformulation.
