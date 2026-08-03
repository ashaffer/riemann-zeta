# Plain-Legendre Hodge falsifier

## Verdict

The strengthened Hodge row used in the current propagation route has a stable
numerical counterexample on the intended logarithmic form domain.  At the
activation of the prime power `5`, a cutoff-free plain-Legendre section gives

`lambda_max(C^-1/2 (X* A^-1 X + T* T) C^-1/2) = 1.0000575016`

and

`lambda_min(C - X* A^-1 X - T* T) = -8.9466136e-5`.

Here `[[A,X],[X*,C]]` is the enlarged Weil block and `T` is the Hodge return
trace.  The negative value is stable under the spatial quadrature ladder and
is accompanied by an explicit saved witness.

This is decisive fail-fast evidence for pruning the route, but it is not an
interval-arithmetic certificate.  A formally certified counterexample would
require rigorous enclosures for the matrix entries and the negative Rayleigh
quotient.

This falsifies only the strengthened sufficient criterion

`X* A^-1 X + T* T <= C`.

It does **not** disprove RH.  The ordinary Weil row remains numerically
saturated and nonnegative in these sections, and a different event
propagation argument could still work.

## Independent discretization

The calculation uses no hat functions.  It takes zero-extended,
`L^2`-normalized Legendre polynomials on each of

`[-R_old,R_old]`, `[-R_new,-R_old]`, and `[R_old,R_new]`.

The full two-moment relative nullspace is formed first.  The embedded old
two-moment nullspace is then split off orthogonally.  Consequently the collar
has dimension `2 * collar_degree` and includes the old moment-correction
directions; it is not the smaller space of separately moment-zero collar
functions.

For the default section:

- old degree: `32` (`30` relative old modes);
- collar degree: `20` per component (`40` corrected collar modes);
- old support: `2.99573227355399`;
- new support: `3.55534806148941`.

All old modes, not just the first four, are included in `X* A^-1 X` and in
`T* T`.

## Cutoff-free assembly

Prime translations are integrated by exact polynomial-overlap quadrature.
The gamma term is not frequency truncated.  If `S(u)` denotes the symmetric
shift overlap of the piecewise Legendre basis and

`w(u) = exp(-u/2) / (1-exp(-2u))`,

the code evaluates the Gauss--digamma identity

`(psi(1/4)-log(pi)) I`

` + 2 integral_0^(2 R_new) (I-S(u)) w(u) du`

` + 2 I integral_(2 R_new)^infinity w(u) du`,

then adds the pole matrix.  The `u` integral is split at every difference of
support endpoints.  On each resulting interval `S(u)` is polynomial, so
Gauss--Legendre quadrature only has to resolve the analytic kernel factor.

## Stability and validation

| spatial order | strengthened ratio | strengthened minimum | ordinary ratio | ordinary minimum |
|---:|---:|---:|---:|---:|
| `96` | `1.000057503855` | `-8.946614111e-5` | `.999999995308` | `9.29484e-9` |
| `128` | `1.000057501614` | `-8.946613579e-5` | `.999999987387` | `2.34922e-8` |
| `160` | `1.000057504502` | `-8.946614326e-5` | `.999999994699` | `1.04954e-8` |

The negative minimum varies by less than `7.5e-12`; the strengthened ratio
varies by less than `2.9e-9`.  The sign of the tiny ordinary minimum is not a
numerical theorem, but its uncertainty is immaterial to the strengthened
failure, whose negative eigenvalue is about four orders of magnitude larger.

Further checks:

- the old `m=8` block agrees with the independent high-precision
  `spectral_margins.spectral_form` assembly in operator norm to `2.34e-12`;
- basis Gram error at order `128`: `6.87e-15`;
- reflection-involution error: `1.34e-14`;
- new-event old--old shell error: exactly `0` after exact spatial assembly;
- analytic-Fourier cutoff ratios at `xmax=300,1000,2400` are respectively
  `1.000056824`, `1.000057253`, and `1.000057420`, approaching the cutoff-free
  spatial result from the same side.
- recomputing the Schur solve and eigensystem at `70` decimal digits from the
  assembled matrices gives `-8.94661357118627e-5`; its difference from the
  double-precision minimum is `7.18e-15`.

## Saved witness

For the unit Euclidean collar eigenvector `w` of the negative Schur surplus:

| quantity | value |
|:---|---:|
| `w* (C-X*A^-1X) w` | `2.16863624e-6` |
| `||T w||^2` | `9.16347720e-5` |
| difference | `-8.94661357e-5` |
| reflection parity | `-.999999999999972` |
| plus moment residual | `1.02e-16` |
| minus moment residual | `3.91e-17` |

Thus the counterexample is odd.  The ordinary row has a small positive budget
on this vector, but the Hodge trace cost is about `42` times larger.

The archive `results/plain-legendre-hodge-witness.npz` contains `A`, `X`,
`C`, `T`, both Schur matrices, the normalized collar witness, the minimizing
old correction `-A^-1 Xw`, relative and raw piecewise-Legendre coefficients,
reflection matrices, moment residuals, and all support metadata.  Its SHA-256
at generation is

`5b46d7e668b3348199dd3c5e27b3b898968c5f862d151a4697121d805cfc772b`.

## Domain admissibility

A compactly supported piecewise polynomial with finite endpoint jumps has
Fourier transform `O(1/|xi|)`.  Hence

`integral log(2+|xi|) |fhat(xi)|^2 dxi < infinity`.

The saved vector also annihilates both exponential pole moments.  It is
therefore in the logarithmically weighted relative form domain even though it
is not a smooth compactly supported function.  Boundary-vanishing polynomial
bumps gave positive finite-section results because they suppress precisely
this jump trace; they cannot establish the claimed full-domain inequality.

## Reproduction

Run the cutoff-free falsifier and regenerate the witness with:

```bash
python3 src/plain_legendre_hodge_falsifier.py --xquad 128 --mp-dps 70
```

Quadrature-order and low-sector ladders are available through:

```bash
python3 src/legendre_hodge_sector_scan.py \
  --old-degree 32 --collar-degrees 20 --smooth-power 0 \
  --xquad 96 --xmax 0 --dxi 1 --low-counts 1 2 4
```

For `smooth-power=0`, `xmax` and `dxi` are ignored because the spatial gamma
identity is untruncated.

## Consequence for the roadmap

The earlier positive hat and smooth-bump sections diagnosed a restricted
boundary-regular subspace.  They do not extend uniformly to the logarithmic
form domain.  The present Hodge-loss absorption route should therefore be
pruned in its strengthened form.  What survives is the ordinary near-saturated
Weil row and the broader question of whether event propagation can be proved
without subtracting the extra `T* T` term.
