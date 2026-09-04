# Carrier-slice support on the first finite Zeta23 fixtures

Status: exact analytic scalar dual, exact normalized one-pair and abstract
collateral formulas, double-precision regression tests of those formulas,
and a floating actual-prime control, 2026-08-12.  The actual high-height
prime/collateral Gabor remainder has not been assembled.  No zero-free strip
or RH statement is proved.

## 1. Verdict

The one-sided carrier-slice proposal is computationally real and strictly
sharper than taking an operator norm.  In finite dimension it needs no SDP
package: it is one convex scalar minimization of a largest eigenvalue.

Three checks give three different outcomes.

1. On the exact normalized one-pair Paley--Wiener mirror, the positive-null
   space is one-dimensional.  The exact diagonal packet remainder has
   support `m`, while the aligned cross bill is `m*cosh(alpha*D)`.  Its useful
   fraction is exactly `sech(alpha*D)`, hence it is subcarrier.
2. On the abstract two-pair collateral fixture, the support has a closed
   piecewise formula.  For equal pair scales it detects the exact `2/11`
   aggregate-null state from the collateral audit.  It also shows a genuine
   improvement over the unrestricted positive-part norm: when at least
   three quarters of the selected carrier is required, the support is
   negative even though the remainder has a positive eigenvalue.
3. On the older zero-independent `{2,3}` versus `p=5` zeta-coefficient Ritz
   fixture, the actual `p=5` event has ample positive support on the old
   one-dimensional negative carrier.  Nevertheless the full margin is tiny
   because the cross coupling to the complement is nearly critical.  Thus
   `h_eta` is an effective **necessary fail-fast test**, not a sufficient
   positivity or strip test.

The outstanding computation is unchanged but is now completely specified:
assemble the actual high-height two-lobe prime/collateral cross remainder on
the positive-null Gabor quotient, then evaluate the scalar dual below.  No
such matrix fixture is presently stored in the repository.

## 2. The finite SDP is a scalar eigenvalue problem

Let `S` be the positive-null space.  Compress all matrices to `S`, let
`N>=0` measure the retained carrier, and let `R=R*` be the proposed aggregate
remainder.  For `eta>=0`, put

```text
F_eta={Gamma>=0 : Tr(Gamma)=1, Tr(N Gamma)>=eta},

h_eta(R)=max_(Gamma in F_eta) Tr(R Gamma).           (2.1)
```

The slice is nonempty exactly when

```text
eta<=lambda_max(N).                                 (2.2)
```

### Proposition 2.1 (scalar dual)

If `eta<lambda_max(N)`, then

```text
h_eta(R)
 =inf_(mu>=0) [lambda_max(R+mu*N)-mu*eta].          (2.3)
```

At the boundary `eta=lambda_max(N)`, every feasible state is supported on
the top eigenspace `E_max(N)`, so

```text
h_eta(R)=lambda_max((P_E R P_E)|E_max(N)).          (2.4)
```

Moreover, an optimizer of (2.1) may always be chosen rank one.

#### Proof

For every feasible `Gamma` and `mu>=0`,

```text
Tr(R Gamma)
 =Tr((R+mu*N)Gamma)-mu*Tr(N Gamma)
 <=lambda_max(R+mu*N)-mu*eta.                       (2.5)
```

Taking the infimum gives weak duality.  If
`eta<lambda_max(N)`, a top eigenstate of `N` satisfies the carrier inequality
strictly.  Mixing it with a sufficiently small positive-definite normalized
state preserves that strict inequality and gives `Gamma>0`; this is the
primal Slater point, so finite-dimensional semidefinite duality gives
equality.  Equality (2.4) follows directly from the equality case in
`Tr(N Gamma)<=lambda_max(N)Tr(Gamma)`.

Here `(P_E R P_E)|E_max(N)` denotes the restriction to the top eigenspace;
viewing `P_E R P_E` on the whole ambient space would add irrelevant zero
eigenvalues and would be wrong when the restricted maximum is negative.

For the rank statement, take an extreme feasible `Gamma` of rank `r`.  If
the carrier inequality is active, Hermitian perturbations on its range have
real dimension `r^2` and obey at most the two real equations
`Tr Delta=Tr(N Delta)=0`.  If it is inactive, only the trace equation is
needed and small perturbations preserve the strict inequality.  Thus
`r>=2` admits a nonzero two-sided feasible perturbation, contradicting
extremality.  The feasible set is compact, so a linear objective has an
extreme optimizer.  QED

The sign in (2.3) matters: it is `R+mu*N` and then `-mu*eta`.  The immediate
norm bound is recovered by taking `mu=0`,

```text
h_eta(R)<=lambda_max(R)<=||(R)_+||.                 (2.6)
```

If an aligned row obeys `B<=-c*N`, an aggregate-null state retaining carrier
at least `eta` necessarily satisfies

```text
h_eta(R)>=c*eta.                                    (2.7)
```

This is the finite go/no-go comparison used below.

## 3. Exact normalized one-pair mirror

Use the repository's exact packet compression

```text
M=m*[[1,C],[C,1]],
m=2*A_alpha^2/L,          C=cosh(alpha*D)>1.        (3.1)
```

With `e_+=(u+v)/sqrt(2)` and `e_-=(u-v)/sqrt(2)`, write

```text
P=m*(1+C)*e_+e_+^*,
N_spec=m*(C-1)*e_-e_-^*,
B_cross=m*C*(u v^*+v u^*),
R_diag=m*I,
M=B_cross+R_diag.                                   (3.2)
```

Nulling the positive row leaves `S=span{e_-}`.  Hence the only normalized
state is `Gamma=e_-e_-^*`, and for every
`0<=eta<=m(C-1)`,

```text
h_eta(R_diag)=m.                                    (3.3)
```

On the same state,

```text
B_cross=-m*C
       =-[C/(C-1)]*N_spec.                          (3.4)
```

Therefore the diagonal term pays only

```text
h_eta(R_diag)/(m*C)=1/C=sech(alpha*D)               (3.5)
```

of the cross-cancellation bill.  Relative to the report convention
`K=m*C/2`, its support is `2/C` times `K`.  This tends to zero exponentially
in `alpha*D`, or by the corresponding fixed power when `D=d_* log X`.

For the script's legal scale-normalized fixture

```text
alpha=2/5,       d_*=3/5,       L=10,       m=1,
D=6,             C=cosh(12/5)=5.556947166965509,
```

the output is

```text
h_eta(R_diag)             1
cross bill                5.556947166965509
h_eta/cross bill          0.1799549230816372
h_eta/K                   0.3599098461632744.       (3.6)
```

This is an exact structural calculation evaluated in floating arithmetic.
The `m I` term is the exact same-lobe normalization remainder of the pair
form; it is not being relabelled as the unknown actual raw-prime cross row.

## 4. Exact two-pair collateral slice

Now use the abstract three-coordinate fixture from the collateral audit.
Let `u,w,v` be orthonormal, put `a_j=sqrt(k_j/2)`, and take

```text
x_0=a_0*(u+v),             y_0=a_0*(u-v),
x_1=a_1*(u+v),             y_1=a_1*(w-v).           (4.1)
```

The common positive-row null is

```text
S=(u+v)^perp=span{q,w},       q=(u-v)/sqrt(2).      (4.2)
```

The selected aggregate cross row and its carrier are

```text
B_0|S=-N,
N=2*k_0*[[1,0],[0,0]],                              (4.3)
```

while the collateral **aggregate cross** remainder is

```text
R_1=k_1*[[-1,-1/sqrt(2)],
         [-1/sqrt(2),0]].                           (4.4)
```

For a rank-one state `psi=a*q+b*w`, write `x=abs(a)^2`.  Then

```text
Tr(N Gamma)=2*k_0*x,
max_phase Tr(R_1 Gamma)
 =k_1*(-x+sqrt(2*x*(1-x))).                         (4.5)
```

Put

```text
r=eta/(2*k_0),
x_*=1/2*(1-1/sqrt(3)).                              (4.6)
```

The exact support is

```text
h_eta(R_1)=
  k_1*(sqrt(3)-1)/2,                    0<=r<=x_*,
  k_1*(-r+sqrt(2*r*(1-r))),             x_*<=r<=1. (4.7)
```

This verifies two points which the unrestricted norm cannot express.

First, `||(R_1)_+||=k_1*(sqrt(3)-1)/2`, but the positive eigenstate is
excluded as `eta` increases.  At `r=3/4`,

```text
h_eta(R_1)
 =k_1*(-3/4+sqrt(3/8))
 =-0.13762756430420575*k_1<0,                       (4.8)
```

despite `||(R_1)_+||=0.3660254037844386*k_1>0`.

Second, the largest-carrier pure state which cancels `B_0+R_1` has

```text
x_cancel
 =2*k_1^2/((2*k_0+k_1)^2+2*k_1^2).                 (4.9)
```

For `k_0=k_1=1`,

```text
x_cancel=2/11,          eta_cancel=4/11,
psi=(-sqrt(2/11),3/sqrt(11)),
Tr(B_0 Gamma)=-4/11,
Tr(R_1 Gamma)= 4/11.                                (4.10)
```

At this slice,

```text
h_(4/11)(R_1)=(sqrt(3)-1)/2
              =0.3660254037844386
              >4/11=0.3636363636363636.            (4.11)
```

Thus the one-sided gate (2.7) passes, with a small but exact positive slack.
Recovering the full `(u,w,v)` state gives `(-1,3,1)/sqrt(11)`; the selected
and collateral complete hyperbolic pair values are each `-4/11`, exactly as
in the earlier audit.

This is a validation of the diagnostic and of the abstract escape.  The
repository has not proved that the simultaneous row orientation (4.1) occurs
in a normalized two-pair Paley--Wiener/Gabor compression or in the zeta
divisor.

## 5. Zero-independent actual-prime control

There is no stored high-height two-lobe actual-prime Gabor matrix.  There is,
however, an older genuine coefficient control in
`src/prime5_block_rescue.py`.  On the orthonormal Legendre Ritz space, let
`Q_old` contain the zeta archimedean/pole pieces and the actual prime places
`{2,3}`.  For

```text
2*log(5)<L<2*log(7),
```

the difference

```text
R_5=Q_full-Q_old                                    (5.1)
```

is exactly the actual `p=5` event in that truncation.  At `L=3.27` and
dimension `12`, `Q_old` has one resolved negative eigenvector.  On that
one-dimensional carrier space put `N=-Q_old|S`; the carrier slice is again a
singleton.

The reproducible results use 24-decimal mpmath working precision for form
assembly followed by conversion to `float64` for the eigensolves:

| fixture | `eta=N` | `h_eta(R_5)` | `h_eta/eta` | full minimum | normalized old-negative/complement coupling |
|---|---:|---:|---:|---:|---:|
| full zeta form | `5.914975397731e-05` | `4.069486315245e-04` | `6.879971667854` | `5.827736981938e-09` | `0.990443103906` |
| two-pole-moment relative form | `1.480794571583e-05` | `1.387894368583e-04` | `9.372632742023` | `2.505564687246e-05` | `0.877936628358` |

So an actual arithmetic event can easily pass the one-sided carrier-support
gate at a finite stage.  In the full fixture the eventual positive margin is
still only about `5.8e-9`, because the normalized cross block is close to
one.  The diagnostic therefore does exactly one job: it rules a proposed
remainder in or out as a source of the required sign and size.  After a
positive result, the full-form collateral cost and Schur coupling remain to
be controlled.

This control is not evidence for a high-height strip.  It uses small support,
an old negative carrier unrelated to a hypothetical off-line mirror pair,
finite dimension, and ordinary floating Ritz arithmetic.

## 6. Reproducibility

The implementation is

```text
src/carrier_slice_support.py
src/test_carrier_slice_support.py
```

The formula-regression tests and default demonstrations use only NumPy:

```bash
PYTHONPATH=src python3 -m unittest src/test_carrier_slice_support.py
python3 src/carrier_slice_support.py --fixture all
```

The optional actual-prime control reuses the repository's established
Legendre form builder and therefore also loads its mpmath/SciPy dependencies:

```bash
python3 src/carrier_slice_support.py \
  --fixture prime5 --support 3.27 --dimension 12 --dps 24

python3 src/carrier_slice_support.py \
  --fixture prime5 --support 3.27 --dimension 12 --dps 24 --relative
```

Five double-precision unit tests check the mirror formula, the numerical
scalar dual against exact formula (4.7), the `2/11` cancellation state, the
strict carrier-slice improvement over the unrestricted positive part, and
empty-slice rejection.  The exactness claims come from the displayed
analytic proofs, not from NumPy arithmetic.

## 7. What survives as the next theorem target

The computation prunes the exact diagonal mirror remainder and confirms that
an abstract near-tie collateral row could pass the finite gate.  It neither
chooses between those outcomes for zeta nor replaces the coefficient theorem.

The next actual object must be constructed before looking at its sign:

```text
S_T = positive-row-null two-lobe Gabor quotient,
N_T = selected-pair carrier on S_T,
R_T = compressed actual prime/on-line/collateral aggregate cross remainder.
                                                                  (7.1)
```

For each fixed carrier fraction `eta_T`, compute

```text
inf_(mu>=0)
 [lambda_max(R_T+mu*N_T)-mu*eta_T].                 (7.2)
```

There are then only two honest outcomes.

- A uniform upper bound below the aligned bill prunes every positive-ensemble
  reservoir at that carrier fraction.
- A carrier-scale lower value passes this necessary gate and exhibits the
  needed positive sign on some carrier-retaining state.  Exact aggregate
  cancellation, full completed-form cost, and Schur coupling must still be
  proved.

The missing step is the assembly or theorem-level control of `R_T` in (7.1),
not the SDP solver.
