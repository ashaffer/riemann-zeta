# QP-PROMOTE nodal-product and singular-cluster gate

**Date:** 2026-08-13

**Verdict:** **no QP promotion and no strip.**  There is, however, a new
theorem-grade support obstruction.  A TV-normalized cosine measure which
annihilates all `M` actual prime-power log nodes and retains a polynomial-size
carrier cannot have all its atoms in a shallow aperture.  Uniformly for every
choice of coefficients and support points, its maximum time must be

```text
D >= (1-o(1)) M/(2 e w)  asymp Y/log Y.              (0.1)
```

The exact actual-node nodal product gives a substantially stronger finite
frontier (about `2.27 M` in the limiting canonical `w=.2` diagnostic).  Thus
boundary stencils, confluent/derivative jets, and adaptive near-alias clusters
living below the Nyquist scale cannot meet the required
`Y^(-kappa_min)` carrier.  The full aperture `Y^(50/33)` is much larger than
`Y/log Y`, so this does **not** obstruct measures using genuinely remote
atoms.  That remote directional problem remains open.

## 1. Polarity and object

Let

```text
N_Y={p^k : Y exp(-w)<=p^k<=Y exp(w)},
u_n=log(n/Y),       M=#N_Y,
phi(u)=(1-|u|/w) exp(alpha u),
b(t)=integral_[-w,w] phi(u) cos(tu) du.
```

For an aperture `D`, define the truncated primal extremal

```text
E_D=sup |integral b(t) dh(t)|,
```

where `h` is real signed, `supp h subset [0,D]`, `||h||_TV<=1`, and

```text
integral cos(t u_n) dh(t)=0       (n in N_Y).         (1.1)
```

The strip-facing direction is:

```text
E_B >= Y^(-kappa_min+epsilon)     PROMOTES QP;
E_B <= Y^(-c), c>kappa            KILLS only this optional carrier route.
```

Here `kappa_min=.0180303234...`.  Every inequality below is an **upper**
bound for a restricted `E_D`.  It is therefore an obstruction to proposed
PROMOTE constructions, never positive evidence for a zero-free strip.

## 2. Exact nodal-product theorem

### Theorem 2.1 (actual-node shallow-aperture bound)

Put

```text
L_Y(u)=product_(n in N_Y) |u-u_n|,
A_Y=(1/M!)*integral_[-w,w] phi(u)L_Y(u)du.            (2.1)
```

Then, for every `D>=0`,

```text
E_D <= D^M A_Y.                                      (2.2)
```

In particular, with `m_phi=integral phi`,

```text
E_D <= m_phi * D^M/M! * max_[-w,w] L_Y(u)            (2.3)
    <= m_phi * (2wD)^M/M!.
```

#### Proof

For a feasible measure set

```text
F(u)=integral_[0,D] cos(tu) dh(t).
```

It is real and `C^infinity`, it vanishes at the `M` distinct actual nodes,
and differentiation under the finite measure gives

```text
sup_u |F^(M)(u)| <= integral t^M d|h|(t) <=D^M.       (2.4)
```

Apply the real Lagrange interpolation remainder to `F` at all `M` nodes.
For each `u` in the shell (with the nodal cases following by continuity),

```text
|F(u)| <=D^M/M! * product_n |u-u_n|.                 (2.5)
```

Finally, Fubini gives

```text
integral b dh=integral_[-w,w] phi(u)F(u)du,
```

and `phi` is positive.  Equations (2.2)--(2.3) follow.  No spacing,
genericity, sign pattern, condition number, or restriction on the number of
atoms was used.  In particular, arbitrarily ill-conditioned coefficients are
already included through the TV normalization.  QED

### Corollary 2.2 (polynomial carrier forces Nyquist-scale support)

Stirling and the last member of (2.3) imply that for every fixed
`epsilon>0`,

```text
D <=(1-epsilon) M/(2 e w)
    => E_D <=exp(-c_(epsilon) M).                    (2.6)
```

Since `M=Y^(1+o(1))`, an extremal with
`E_D>=Y^(-kappa_min+o(1))` must satisfy

```text
D >=(1-o(1)) M/(2 e w).                              (2.7)
```

At the canonical `w=.2`, the rigorous distribution-free constant in (2.7)
is

```text
1/(2 e w)=.9196986029... .                           (2.8)
```

This closes the whole `D=Y^.01`, fixed-frequency, boundary-stencil, and
`D=Y^(o(1))` singular-support sector.  It does not close the legal range
`D` between `asymp Y/log Y` and `B=Y^(50/33)`.

## 3. Actual-node potential refinement

The exact factor in (2.3) is much smaller than `(2w)^M`.  Prime powers of
exponent at least two are negligible in number, and PNT predicts the
empirical node density

```text
rho_w(x)=exp(x)/(2 sinh w),       -w<=x<=w.
```

Define its logarithmic potential

```text
U_w(u)=integral_[-w,w] rho_w(x) log|u-x| dx.          (3.1)
```

The resulting limiting cutoff ratio is

```text
c_w=exp(-1-max U_w).                                  (3.2)
```

For `w=.2`, floating quadrature gives

```text
max U_w=-1.818726676470978... at u=-w,
c_w=2.267610596526286... .                           (3.3)
```

The tool also maximizes the **finite actual-node** product.  Its critical
points are exhaustive: the logarithmic derivative
`sum_n 1/(u-u_n)` decreases from `+infinity` to `-infinity` in every nodal
gap, so there is exactly one candidate in each gap, in addition to the two
endpoints.  These finite values are floating diagnostics, not interval
certificates.

| `Y` | `M` | cutoff where (2.3) equals `Y^-kappa_min` | cutoff / `M` | low-cutoff log-bound minus target |
|---:|---:|---:|---:|---:|
| 300 | 23 | 60.824 | 2.645 | -93.17 |
| 1000 | 61 | 164.320 | 2.694 | -307.00 |
| 3000 | 151 | 345.027 | 2.285 | -870.30 |
| 10000 | 440 | 1039.800 | 2.363 | -3016.06 |

The enormous negative last column is the useful fail-fast conclusion:
putting the entire measure near the formal split point `Y^.01` is not merely
slightly short of the budget; after exact annihilation its carrier is
superpolynomially too small.

The existing continuous actual-node extremizer at `Y=1000` evades the theorem
in exactly the permitted way.  Its carrier atom is at `t=6.54`, but its 61
cancellation atoms run from `t=1147` to `33323`, with median `16401`; the
finite nodal-product frontier is only `164`.  The remote atoms have irregular
signs and phase cells rather than a colliding cluster.  This is consistent
with the theorem and sharpens the next target: the live geometry is the
macroscopically spread remote cloud, not the low carrier atom or a boundary
stencil.

## 4. Why colliding atoms do not create a free derivative direction

There is a second elementary audit relevant to singular directional minors.
Let a portion `mu_J` of a candidate measure have TV `C_J` and support in a
time interval `J` of diameter `Delta`.  Replace it by one atom at any center
`tau in J`, with coefficient `mu_J(J)`.  Since

```text
|cos(tu)-cos(tau u)|<=w|t-tau|,
```

the feature-vector and carrier errors are at most

```text
||error_feature||_2 <=w sqrt(M) C_J Delta,           (4.1)
|error_carrier|     <=w m_phi C_J Delta.             (4.2)
```

Consequently, a collision with `C_J Delta=o(1)` collapses to a lower-atom
design.  A derivative jet requires coefficients of order `1/Delta`, and its
TV bill records that blow-up exactly.  A vanishing Cramer denominator by
itself is therefore not a cheap QP construction.  What could still work is
not a collision, but several macroscopically separated remote phase vectors
whose *directional* convex combination hits the carrier.

## 5. Literature audit

The relevant classical theories identify the finite optimization but do not
supply the missing actual-prime asymptotic.

* [Elfving's original c-optimal-design theorem](https://doi.org/10.1214/aoms/1177729442)
  identifies the carrier ray with the boundary of a symmetric convex hull and
  yields sparse support.  It gives no arithmetic lower bound on the exposed
  radius; singular versions do not make a colliding derivative direction
  free in TV.
* [Studden's Elfving-theorem audit](https://doi.org/10.1016/j.jspi.2003.05.004)
  relates c-optimality to approximation theory and singular designs.  Again,
  it is a finite geometric equivalence, not a prime-log directional estimate.
* [Ingham's nonharmonic exponential inequalities](https://doi.org/10.1007/BF01180426)
  and modern biorthogonal-family norm bounds control `L2` interpolation under
  gap or condensation hypotheses.  The QP gate is an `L1`/TV, carrier-specific
  extrapolation problem; converting the frame solution gives the already
  known square-root bill.
* [Candès--Fernandez-Granda super-resolution](https://doi.org/10.1002/cpa.21455)
  constructs dual polynomials for separated spikes.  Its polarity is recovery
  certification and its separation is in the unknown support; it does not
  imply a cheap representation of the low carrier by the one-dimensional
  prime-log high phase curve.
* Sidon/`Sidon(U)` interpolation theorems can interpolate bounded data on
  lacunary or quasi-independent frequency sets using measures on small open
  sets.  The actual nodes form a dense shell of size `Y/log Y`, not such a
  set, and those theorems provide no uniform constant with the required
  support separation and carrier direction.

No surveyed theorem upgrades (2.7) to the full legal aperture, and no
no-go theorem found in this literature has eliminated the surviving remote
atomic designs.

## 6. Disposition

```text
cheap legal measure C<=Y^(kappa_min-epsilon): NOT FOUND;
QP-PROMOTE:                                    OPEN;
all-support-below-o(Y/log Y) constructions:    KILLED;
bounded-TV collision/derivative-jet loophole:  KILLED;
remote separated actual-node directional span: OPEN;
zero-free strip:                               NOT PROVED.
```

The next construction attempt must place meaningful geometry at times
`Omega(Y/log Y)` and use macroscopically separated atoms.  Re-running a
near-boundary stencil, a confluent directional minor, or a generic frame is
now redundant.

## 7. Replay

```bash
python3 src/test_qp_nodal_product_gate.py
python3 results/verify_zeta23_qp_nodal_product_gate.py
python3 src/qp_nodal_product_gate.py --Y 300 1000 3000 10000
```
