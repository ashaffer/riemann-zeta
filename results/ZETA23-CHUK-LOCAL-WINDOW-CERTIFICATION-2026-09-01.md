# Chuk local-window certification

**Date:** 2026-09-01  
**Status:** local theorem certified under the explicit Arb-plus-analytic trust base below  
**Global status:** RH remains open; global Weil positivity and actual-zeta support propagation remain open

## Certified theorem

Let

```text
a = 4/5,
F(t) = integral_(-a)^a f(x) exp(i t x) dx,
D_log = {f : integral log(2+|t|) |F(t)|^2 dt < infinity}.
```

For every complex `f` supported in `[-4/5,4/5]` and belonging to
`D_log`, the completed-zeta Weil form in the project's normalization obeys

```text
Q(f) >= 8.9e-18 ||f||_2^2.                        (1)
```

The inequality is strict for every nonzero `f`; at `f=0`, both sides vanish.
Equivalently, extend `Q` by `+infinity` outside `D_log`, in which case the
weak inequality holds for every supported `L2` function. This independently
certifies the local support-`1.6` lower bound claimed in
[Marcus Chuk, arXiv:2608.24827v1](https://arxiv.org/abs/2608.24827v1).
It does not rely on numerical matrices or certificate data from that paper.

## Proof chain

1. At `a=0.8`, the active von Mangoldt terms are exactly `n=2,3,4`.
   Their mass is enclosed by

   ```text
   A_L = [2.94197352522362045550390939018 +/- 2.71e-30].
   ```

2. Set `T=200` and `alpha=1/2`.  Chuk's elementary exterior digamma
   envelope gives

   ```text
   beta_*(200) = [0.513466774915070738 +/- 3.89e-19] > 1/2.
   ```

   Hence `Q` dominates the bounded clipped minorant

   ```text
   R(f) = alpha ||f||^2
          + (1/pi) integral_0^200 (Omega(t)-alpha)|F(t)|^2 dt
          + pole(f).
   ```

3. The finite core uses normalized Legendre degrees `0,...,249`, or 125
   modes in each parity sector.  Every unit frequency panel uses a common
   80-point Arb Gauss--Legendre rule.  This is not sampled quadrature: each
   entry is continued to a Bernstein ellipse with `|Im t|<=1/4`, inside the
   nearest digamma poles at `|Im t|=1/2`.  Binet's formula gives
   `|Omega(t)-alpha|<21` there.  Chebyshev coefficient decay and exactness of
   Gauss--Legendre through degree 159 give

   ```text
   entry quadrature error <= 1.21884933566808127e-29,
   parity-block operator error <= 1.52356166958510158e-27.
   ```

   The largest final entry-ball radius was
   `1.21884934136585485e-29`.

4. An approximate eigensolver is used only to propose a dyadic change of
   basis.  Arb then recomputes the exact interval congruence and interval
   Cholesky from the enclosed matrix.  At the exact shift `9e-18`, the
   resulting margins are

   ```text
   even smallest shifted pivot > 1.184984588553443791708767e-18,
   odd  smallest shifted pivot > 1.136872836967865838917864e-14.
   ```

   Thus the finite block exceeds `9e-18 I`.  The approximate eigenvalues
   printed by the program are diagnostics, not premises.

5. The infinite Legendre complement is retained.  The normalized
   plane-wave coefficient formula and double-factorial spherical-Bessel
   majorant give

   ```text
   rho_tail  < 5.971e-32,
   pole_delta < 1.911e-592,
   complement diagonal = 0.5 - O(1e-30),
   head/tail coupling < 3.910e-15.
   ```

   After subtracting the target `8.9e-18`, the two-by-two Schur determinant
   is enclosed by

   ```text
   [4.999999998471481200248958e-20 +/- 2.35e-45] > 0.
   ```

   This transfers the finite inequality to the full real form domain.
   Parity orthogonality and splitting into real and imaginary parts give
   `(1)` for arbitrary complex `f`.

## Independent numerical-kernel replay

The optional adaptive replay uses `acb.integral`, holomorphic digamma
symmetrization, and direct spherical-Bessel/`0F1` formulas.  It shares neither
the common Gauss nodes nor the Bernstein remainder.  All nine entries

```text
(0,0), (0,20), (20,20), (40,80), (80,80),
(1,1), (1,21), (81,121), (249,249)
```

overlapped their common-node Arb enclosures.  The complete cross-check run
then repeated the head and full-tail PASS.

## Why the smaller cutoffs were rejected

- `T=150` with Chuk's crude `alpha=0.224...` has an explicit Rayleigh
  quotient below `5.0e-18`.  Even importing the sharper valid exterior floor
  `alpha=0.29`, the independently replayed full even core is about
  `4.5136784504e-18`; a `5e-18` shifted proof fails while `4.5e-18` passes.
- `T=180`, `alpha=0.41` looked promising on a 40-mode witness
  (`1.01009937684e-17`), but the full 110-mode-per-parity interval
  congruence fails the `9e-18` head shift.  A shifted pivot is enclosed near
  `-2.254609750e-19`.

These are certificate-architecture falsifiers, not refutations of local
positivity.  They explain why the successful run uses `T=200`.

## Trust base and scope

The computational trust base is Python 3.12.3, python-flint 0.9.0 / FLINT
3.6.0, 512-bit construction of global transcendental balls, and 384-bit
matrix arithmetic.  The analytic inputs are the exterior digamma envelope,
Parseval and parity decomposition, the normalized Legendre plane-wave
identity, the elementary spherical-Bessel tail, the pole Taylor remainder,
and the Bernstein-ellipse Chebyshev bound.  Several generic analytic pieces
have Lean counterparts elsewhere in the repository, but this result is not
an end-to-end Lean theorem.

This is a fixed-window theorem.  It improves the local Weil seed from
`a=7/16` to `a=4/5`; it supplies no adjacent-support estimate across the
nearby `p=5` activation, no global positivity, and no proof of RH.

## Replay and provenance

```bash
PYTHONPATH=src python3 -m pytest -q src/test_chuk_l08_arb_certificate.py
PYTHONPATH=src python3 src/chuk_l08_arb_certificate.py --quiet
PYTHONPATH=src python3 src/chuk_l08_arb_certificate.py --quiet --cross-check
```

The first two commands take well under a minute on the audit machine.  The
nine-entry adaptive cross-check takes several minutes.

```text
driver SHA-256:
  5170c5c04d7bad0808ca9cc35470fa16e9e7ed03c99a9b5bec9664bb1c2a0144
test SHA-256:
  c39f517122c1dd57c955c9e55a577edb5be95ec737d3b8da1c3f4248af89c734
machine-readable ledger:
  results/chuk_l08_T200_M250_arb_certificate_2026_09_01.json
```
