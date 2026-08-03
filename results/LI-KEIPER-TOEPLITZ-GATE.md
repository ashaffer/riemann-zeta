# Li--Keiper fail-fast checkpoint II: differences and Toeplitz kernels

Status: finite-difference route rejected; natural conditional/Toeplitz route
proved equivalent to RH rather than an independent amplifier; 2026-08-01.

## 1. Finite-difference positivity fails

Set `lambda_0=0`.  A natural discrete Bernstein law would be

`(-1)^(k-1) Delta^k lambda_n >= 0` for every `k>=1, n>=0`.

It fails at `k=2`: the initial Li sequence is strictly convex, with

`Delta^2 lambda_0 = 0.046154317... > 0`,

where the Bernstein sign demands a nonpositive value.  Dividing by `n` repairs
the second-difference sign but fails at the next order:

`Delta^3(lambda_n/n)|_(n=0) = -1.85024...e-5 < 0`,

where the Bernstein sign demands nonnegativity.  Higher initial differences
also alternate in pairs rather than with the completely monotone pattern.

Thus neither natural normalization is a Bernstein sequence, and ordinary
finite-difference positivity cannot explain Li positivity.

## 2. A natural conditional-definiteness theorem

Extend `lambda` evenly to the integers by `psi(n)=lambda_|n|`, with `psi(0)=0`.
Recall that `psi` is conditionally negative definite (CND) on `Z` when

`sum_(j,k) c_j conjugate(c_k) psi(j-k) <= 0`

for every finite complex vector with `sum_j c_j=0`.

### Theorem

RH holds if and only if `psi(n)=lambda_|n|` is CND on `Z`.

### Proof: CND implies RH

Use the zero-sum vector supported at `0,n` with coefficients `1,-1`.  The CND
inequality becomes

`-2 psi(n) <= 0`,

so `lambda_n>=0` for every `n>=1`.  Li's criterion gives RH.

### Proof: RH implies CND

On RH, write a zero as `rho=1/2+i gamma`.  Then

`w_rho=(rho-1)/rho`

lies on the unit circle.  Conjugate pairing turns the zero-side contribution
into a positive-multiplicity sum of kernels proportional to

`1-cos(n theta_rho)`.

For every fixed angle `theta`, the function

`n -> 1-cos(n theta)`

is CND, because for `sum c_j=0`,

```
sum_(j,k) c_j conjugate(c_k)
  [1-cos((j-k)theta)]
= - |sum_j c_j exp(i j theta)|^2 <= 0
```

after taking the equivalent symmetric real form.  Positive sums and the
standard symmetric zero limit preserve the inequality.  Hence `psi` is CND.

This theorem is useful compression, but not new leverage: its reverse
implication contains Li positivity in the two-point test vector.

## 3. The associated Toeplitz kernel

Define the central second difference of the even sequence,

`a_n = psi(n+1)-2psi(n)+psi(n-1)`.

On RH the zero-side representation gives

`a_n = sum_theta 2(1-cos theta) cos(n theta)`

with positive multiplicities (and the appropriate symmetric limiting
interpretation).  Therefore every Toeplitz matrix `(a_(j-k))` is positive
semidefinite.  Conversely, this Fourier positivity can be integrated back to
conditional negative definiteness after fixing `psi(0)=0` and the evenness
conditions.  It is the discrete Lévy--Khintchine transform of the same zero
measure.

So the natural Toeplitz candidate is not an arithmetic positivity mechanism:
it is zero-side/Weil positivity after taking two differences.

## 4. Why damping does not help

The raw Toeplitz sequence `(lambda_|j-k|)` cannot be positive semidefinite:
its diagonal is `lambda_0=0` while its first off-diagonal is nonzero.  Adding
geometric damping `r^|n|` does not fix that obstruction.  Introducing an
arbitrary positive diagonal can force finite matrices positive, but the
required diagonal then becomes a free domination constant rather than an
RH-sensitive invariant.

For `(lambda_n/n)`, initial CND matrices happen to be numerically negative on
the zero-sum subspace.  This is not a termwise theorem: even a single
critical-line atom `(1-cos(n theta))/n` fails CND for suitable `theta` and
matrix size.  Hence that observation cannot be derived from completion and
critical-line location alone and supplies no robust route without an
additional arithmetic identity.

## 5. Reproducible diagnostic

`src/li_keiper_structure_scan.py` now prints:

- Li coefficients from the exact generating function;
- leading Hankel determinants;
- finite-difference sign ranges;
- eigenvalue ranges of the Toeplitz kernel on the zero-sum subspace.

At size ten the raw `lambda` kernel has zero-sum eigenvalues from approximately
`-3.78` to numerical zero, as predicted by CND.  This is evidence for the
known-zero range, not an unconditional certificate for all coefficients.

## 6. Gate verdict

Two proposed sources of independent structure are now closed:

1. ordinary moment/Hankel and finite-difference positivity fail at very low
   order;
2. the natural conditional/Toeplitz positivity is exactly RH in Fourier
   language and exposes Li positivity in its smallest test vector.

Li--Keiper remains an excellent exceptional-zero detector but currently has
no independent positivity engine.  The only justified remaining cheap test is
an **arithmetic recurrence/order audit** of the completed Bombieri--Lagarias
formula.  Unless its prime-indexed summands have a monotonicity or domination
law that fails for symmetric entire countermodels, the Li branch should be
demoted and the portfolio should move to Nicolas--Robin extremality.
