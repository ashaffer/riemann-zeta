# Fejer correlation does not amplify to a full harmonic signature

**Date:** 2026-08-25  
**Scope:** actual triangular Fejer weights, Newton-direction response  
**Verdict:** a large scalar or rank-one block Gram correlation at threshold
`eta=D^(-7/48)` does **not** force simultaneous control of the supported
harmonics.  The sharp scalar inverse scale is

```text
1/(H*sqrt(eta)),                                    (0.1)
```

not `eta/H`.  At the QP exponents this permits a fixed-centre direction
cluster of size

```text
D^(103/96),                                         (0.2)
```

which misses the allowed `D^(49/48)=D^(98/96)` by `D^(5/96)`.

If two comparable reciprocal Fejer factors are simultaneously present, the
sharp scale improves to `1/(H*eta^(1/4))`, but the resulting cluster
`D^(199/192)` still misses the budget `D^(196/192)` by `D^(1/64)`.

There is, however, a rigorous way around the failed amplification.  If the
whole triangular block is retained on the physical one-dimensional grid,
one can sum the **actual correlation sizes** instead of declaring every
above-threshold edge to have weight one.  Exact Fourier orthogonality, or a
separated-grid argument for the nonlinear Newton response, gives

```text
max row sum <<Q/H=D.                                 (0.3)
```

This is already inside the full anisotropic target.  Thus the result is a
no-go for correlation-to-signature thresholding, paired with a positive
weighted-block theorem.  The remaining issue is the physical intertwining:
the stationary packet Gram must retain this Fejer block rather than lose it
through mode selection, amplitudes, folds, or absolute summation.

Explicit half-lobe examples saturate both statements, contain a maximally
misaligned supported harmonic, and remain large at every dyadic-prefix
scale.  Tensor powers and ordinary high-trace amplification do not change
the conclusion because they also raise the correlation threshold to the
same power.

This is a no-go for deriving the full harmonic signature from **one weighted
correlation number**.  It is not a counterexample to a theorem which retains
the individual harmonic blocks before summation, nor is it an actual
prime-power or fixed-`Q` residual construction.

Here the scalar correlation is the triangular kernel `P_H` itself.  If the
quantity thresholded is instead the unsquared Fejer--Riesz Gram amplitude
`|H^(-1)sum_(r<H)e(r theta)|=sqrt(P_H(theta))`, the inverse is weaker still:
its radius is `1/(H*eta)` and its threshold cluster exponent is `55/48`,
missing the budget by `1/8`.  The weighted-block bypass below handles both
factorizations at the operator level.

## 1. Exact triangular response

The height-one normalized Fejer polynomial is

```text
P_H(theta)
 =sum_(|j|<H) [1/H*(1-|j|/H)] e(j*theta)
 =|sum_(0<=r<H)e(r*theta)|^2/H^2
 =sin^2(pi*H*theta)/(H^2*sin^2(pi*theta)).          (1.1)
```

It is the Gram response of the actual weighted feature vector

```text
v_H(theta)=(sqrt(c_j)*e(j*theta))_(|j|<H),
<v_H(theta),v_H(0)>=P_H(theta).                     (1.2)
```

Thus the counterexamples below are positive-semidefinite Gram examples
using exactly the triangular coefficients, not arbitrary phases or signed
surrogate weights.

The elementary bound `sin(pi||theta||)>=2||theta||` gives

```text
P_H(theta)>=eta
  ==> ||theta||<=1/(2H*sqrt(eta)).                  (1.3)
```

No better power of `eta` follows.

## 2. A sharp half-lobe counterexample

Let `L` be odd, let `L|H`, and put

```text
theta=L/(2H).                                       (2.1)
```

Then `sin(pi*H*theta)=+-1`, while the standard sine bounds give

```text
4/(pi^2*L^2)<=P_H(theta)<=1/L^2.                   (2.2)
```

Taking `L asymp eta^(-1/2)` yields

```text
P_H(theta)asymp eta,
||theta||asymp1/(H*sqrt(eta)).                      (2.3)
```

But the supported harmonic

```text
j_*=H/L                                             (2.4)
```

obeys

```text
j_* theta=1/2 (mod 1).                              (2.5)
```

It is maximally far from alignment.  Hence correlation of the complete
weighted vectors at level `eta` cannot imply that even all of a carefully
chosen low-frequency subfamily is close, much less the simultaneous
`eta/H` signature used by the high-`p` information theorem.

There is also a large abstract star, not just one exceptional point.  For
odd `L` in a constant-proportion interval around `eta^(-1/2)`, an interval
of width `c/H` around each half-lobe has `P_H>=c'*eta`.  These intervals are
disjoint and have total measure

```text
asymp1/(H*sqrt(eta)).                               (2.6)
```

On a grid of mesh `1/Q`, the central vector therefore has

```text
asymp Q/(H*sqrt(eta))                               (2.7)
```

neighbors above a constant multiple of the threshold.  Their Gram matrix
is automatically positive semidefinite because all columns are the genuine
vectors (1.2).  Thus Schur, positivity, or an abstract high-trace inequality
cannot delete this star without additional physical structure.

## 3. Dyadic multiscale prefixes do not help

The same point survives every dyadic prefix.  Put `H_r=H/2^r`.  From (1.1),

```text
P_(H_r)(theta)/P_H(theta)
 =4^r*sin^2(pi*L/2^(r+1)).                          (3.1)
```

Because `L` is odd, its distance from a multiple of `2^(r+1)` is at least
one.  Therefore

```text
|sin(pi*L/2^(r+1))|>=sin(pi/2^(r+1))>=2^(-r),
P_(H_r)(theta)>=P_H(theta).                         (3.2)
```

So even simultaneous lower bounds for every dyadic-prefix Fejer
correlation do not force a main-lobe signature.  A frequency-band or entropy
argument needs information stronger than the scalar prefix correlations.

## 4. Why high trace and Riesz powers are neutral

Taking an `r`-fold tensor power replaces the response by

```text
P_H(theta)^r.                                       (4.1)
```

The hypothesis `P_H>=eta` then supplies only `P_H^r>=eta^r`.  Inverting
(4.1) at threshold `eta^r` returns exactly (1.3).  Treating the powered
response as though it remained above `eta` would be an illicit threshold
amplification.

Similarly, a normalized polynomial amplifier which maps `eta` to a
constant must pay coefficients of size at least a negative power of `eta`;
that cost has to be carried through the operator estimate.  No such reserve
exists in the current `D^(7/96)` ledger.

This does not rule out genuinely independent factors.  If `r` comparable
Fejer responses have product at least `eta`, their common one-parameter
radius is

```text
H^(-1)*eta^(-1/(2r)),                               (4.2)
```

and the fixed-centre grid exponent is

```text
1+7/(96r).                                          (4.3)
```

Three factors still miss `49/48`; four factors would close it by the tiny
margin

```text
49/48-[1+7/384]=1/384.                              (4.4)
```

Ordinary tensor powering does not manufacture these four factors at the
original threshold.  They would have to come from four genuinely retained
physical responses or a new multilinear estimate.

## 5. Exact exponent ledger

With

```text
Q=D^(33/16),       H=D^(17/16),       eta=D^(-7/48), (5.1)
```

the scalar inverse radius (0.1) is

```text
D^(-95/96).                                         (5.2)
```

Multiplying by the physical grid density `Q` gives

```text
Q/(H*sqrt(eta))=D^(103/96).                         (5.3)
```

The desired `D^(49/48)` cluster budget corresponds to radius

```text
D^(49/48)/Q=D^(-25/24).                             (5.4)
```

Thus (5.3) misses by `5/96`.  A scalar Fejer correlation would need the
stronger threshold

```text
P_H>=D^(-1/24)                                      (5.5)
```

to close by this route.

For two comparable reciprocal factors,

```text
radius=D^(-197/192),
cluster=D^(199/192),
miss=199/192-49/48=1/64.                            (5.6)
```

The two-factor threshold would need strengthening to `D^(-1/12)`.

For the unsquared Fejer--Riesz amplitude at threshold `eta`, the radius and
cluster are

```text
radius=D^(-11/12),           cluster=D^(55/48),     (5.7)
```

so entrywise thresholding is even less effective in that presentation.

By contrast, actual simultaneous harmonic control at resolution `eta/H`
gave the much smaller `D^(41/48)` fiber in the high-`p` information report.
The gap between these statements is exactly the missing
correlation-to-signature amplification.

## 6. What remains viable

### 6.1 Exact weighted-block bypass

The large level set (2.6) does not itself have a large weighted Gram norm.
On the exact linear grid, Fourier orthogonality gives, for `H<=Q`,

```text
sum_(n mod Q) P_H((n-a)/Q)
 =sum_(|j|<H)c_j*e(-j*a/Q)*sum_(n mod Q)e(j*n/Q)
 =Q*c_0=Q/H.                                        (6.1)
```

Because `P_H>=0`, every subset has no larger row sum.  Schur therefore gives

```text
||Gram||_(2->2)<=Q/H                                (6.2)
```

for the complete triangular feature vectors on any subset of the grid.
This includes all side lobes and is sharp at the scale of one main-lobe
packet.

The literal Fejer--Riesz square root has feature vectors

```text
w_H(theta)=H^(-1/2)*(e(r*theta))_(0<=r<H),
<w_H(theta),w_H(theta')>
 =H^(-1)*sum_(0<=r<H)e(r*(theta-theta')).           (6.2a)
```

On the complete linear `Q`-grid these vectors form a tight frame with
operator norm exactly `Q/H`; every subset is a compression and has no larger
norm.  Even absolute Schur summation loses only a logarithm, since the
Dirichlet amplitude is bounded by

```text
min(1,1/(2H*||theta||)).                            (6.2b)
```

Thus both the triangular kernel and its actual Fejer--Riesz factor have the
required `Q/H` scale up to `q^o(1)`.

The same power bound survives the actual first-Newton response.  For the
supported probe `(h,k,m)=(1,0,0)`, put

```text
t_y=(Q+y)/(2Q),
Theta_Q(t)=Delta[2Q/(4(t+s/(2Q)))]_(s=0)
          =-1/[4*t*(t+1/(2Q))].                    (6.3)
```

On a fixed collar, `Theta_Q` is strictly monotone and its derivative is
bounded above and below.  Its real range crosses only `O(1)` integers.
After splitting at those wraps, points with index gap `n` have torus
separation `>>min(n/Q,1)` from the relevant lift.  Consequently

```text
sum_(y') P_H(Theta_Q(t_y)-Theta_Q(t_(y')))
 <<1+sum_(n>=1) min(1,Q^2/(H^2*n^2))
 <<1+Q/H.                                           (6.4)
```

There are only `O(1)` wrap branches, so the same bound holds on the whole
collar.  A second reciprocal factor can only reduce the row sum because its
Fejer response is at most one.

At the project exponents,

```text
Q/H=D,                                               (6.5)
```

which is below the weaker cluster allowance `D^(49/48)` by `D^(1/48)` and
equals the full anisotropic squared-Bessel scale.  In particular, the
threshold side-lobe star of size `D^(103/96)` is harmless when its actual
edge weights are retained.

This theorem is exact for the harmonic feature block.  It does not prove
that the completed stationary packets have Gram entries bounded by (6.4).
That requires an intertwining which preserves the common harmonic block and
controls frequency-dependent stationary amplitudes, especially near folds.

### 6.2 Remaining routes

The half-lobe family proves that none of the following is sufficient by
itself:

1. one scalar triangular Fejer Gram entry at level `eta`;
2. positivity or positive-semidefiniteness of that Gram matrix;
3. all dyadic-prefix scalar Fejer correlations at the same level;
4. tensor/high-trace powers with the honestly powered threshold.

A viable physical theorem must retain additional information before scalar
contraction.  Concrete possibilities are:

1. a block Gram estimate controlling individual harmonic bands, not just
   their sum;
2. four genuinely independent comparable Fejer responses at the original
   threshold;
3. fixed-centre arithmetic proving that the half-lobe grid cannot be
   occupied by residual product-band points;
4. signed cancellation across side lobes before absolute values are taken.

## 7. Status

```text
sharp scalar Fejer inverse radius 1/(H sqrt(eta)):  PROVED;
half-lobe saturator with antipodal harmonic:        PROVED;
dyadic-prefix multiscale no-go:                     PROVED;
PSD abstract star of size Q/(H sqrt(eta)):          PROVED;
scalar cluster exponent D^(103/96):                 PROVED;
two-comparable-factor exponent D^(199/192):         PROVED;
ordinary tensor/high-trace threshold amplification: NO;
four-independent-factor ledger margin 1/384:        PROVED CONDITIONAL;
exact linear-grid weighted Gram norm Q/H:           PROVED;
Fejer--Riesz block norm Q/H (absolute: log loss):   PROVED;
nonlinear first-Newton grid row sum O(Q/H):          PROVED;
physical stationary-packet/Fejer-block intertwining: OPEN;
physical residual occupation of the abstract star: NOT PROVED;
correlation-to-full-signature theorem:              FALSE ABSTRACTLY;
sharp four-cycle bound:                             NOT PROVED.
```

Exact coefficients, half-lobe fixtures, multiscale checks, and exponent
ledgers are in `src/qp_fejer_correlation_signature_barrier.py` and
`src/test_qp_fejer_correlation_signature_barrier.py`.
