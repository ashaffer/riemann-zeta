# A finite near-tie cluster defeats every adaptive positive separation profile

Status: exact convex-dual counterconfiguration for the fixed-width
target-only packet model, 2026-08-12.  A constant-size collateral cluster,
compatible with the current local zero-count inputs, makes the finite-list
adaptive separation problem infeasible on every fixed carrier-producing
separation interval.  This is an abstract allowed divisor configuration,
not a theorem that the zeta divisor contains the cluster, and it proves no
zero-free strip.

## 1. Verdict

The finite-list loophole is **not uniformly available**.

Fix a packet width `w>0` and a selected depth `alpha_0>0` (more
generally, let them range in fixed compact subsets of their admissible
ranges).  Let `[d_0,d_1]` be a compact subinterval of the admissible
fixed-width separation range (for the symmetric length-`L` support this
requires `d_1<1`).  Thus

```text
0<d_0<d_1<1,
D in I_L=[d_0*L,d_1*L].                              (1.1)
```

There are constants

```text
m<infinity,  c_j>0,  lambda_j>0       (1<=j<=m),    (1.2)
```

depending only on `d_0,d_1`, such that the following collateral
configuration defeats **every** positive separation measure on `I_L` for
all sufficiently large `L`:

```text
Delta gamma_j=c_j/L,
alpha_j=alpha_0-L^(-2).                              (1.3)
```

All pairs in (1.3) are simple, distinct, only `L^(-2)` shallower than the
unique selected deepest pair, and lie in one microscopic ordinate cluster.
The number `m` is fixed, whereas the present local count permits `O(L)`
zeros in a unit interval.

Let `R_(j,L)(D)` be the normalized exact fixed-width packet response whose
leading term is the target-only phase factor for collateral pair `j`.
The constants in (1.2) can be chosen so that

```text
sum_j lambda_j*R_(j,L)(D)<0
             for every D in I_L.                    (1.4)
```

Therefore no positive measure `nu` on `I_L` can satisfy

```text
integral R_(j,L)(D) nu(dD)>=0       for every j.    (1.5)
```

Indeed, multiplying (1.5) by `lambda_j`, summing, and using (1.4) gives a
strict contradiction.  This is a pointwise convex-dual certificate, so it
does not depend on how `nu` is adapted after seeing the finite list, nor on
the exponential variation of the selected carrier across `I_L`.

Thus positive separation averaging cannot be guaranteed from local counts,
simplicity, density, or near-tie depth information.  The earlier finite-list
convex feasibility condition is genuinely two-sided: some lists are
feasible, but a constant-size allowed list need not be.

## 2. A positive cosine polynomial negative on any interval away from zero

The key fact is constructive.

### Lemma 2.1 (finite positive-frequency negative barrier)

For every compact interval

```text
I=[a,b] subset (0,infinity)                          (2.1)
```

there are finitely many positive frequencies `c_j`, positive coefficients
`lambda_j`, and `eta>0` such that

```text
P(x)=sum_j lambda_j*cos(c_j*x)<=-eta
                         for every x in I.           (2.2)
```

#### Proof

Let `C` be a centered real Gaussian of variance `sigma^2`, and tilt its
probability law by the positive density factor `C^2/sigma^2`.  Its cosine
transform is

```text
E[(C^2/sigma^2)*cos(x*C)]
 =(1-sigma^2*x^2)*exp(-sigma^2*x^2/2).               (2.3)
```

Choose `sigma*a>1`.  The right side of (2.3) is strictly negative on `I`
and, by compactness, at most `-2*eta` there for some `eta>0`.

Fold the even tilted Gaussian law onto `(0,infinity)`.  First truncate its
tail so that the cosine-transform error is less than `eta/2`.  On the
remaining compact frequency interval, uniform continuity of
`cos(c*x)` permits a positive Riemann quadrature with error less than
`eta/2`, uniformly for `x in I`.  Its nodes and masses are the desired
`c_j,lambda_j`.  Small perturbations make the nodes distinct or rational
without consuming the strict margin.  QED

This lemma is the finite convex dual of the positive-cosine support theorem.
It is stronger than selecting one bad gap: it works for an interval
`[a,b]` of arbitrary finite aspect ratio.

For later stability, apply the lemma on the enlarged fixed interval

```text
I_*=[d_0/2,2*d_1].                                  (2.4)
```

Then the same polynomial has a strict negative margin on every
`x+u/L`, with `x in [d_0,d_1]` and `|u|<=w`, once `L` is large relative to
the fixed packet width `w`.

## 3. Exact fixed-width transfer

Use the centered packet

```text
J=[-w/2,w/2],
M(q)=integral_J exp(q*s)ds,
p_q(ds)=exp(q*s)ds/M(q).                             (3.1)
```

For selected depth `alpha_0`, collateral depth `alpha_1`, and ordinate gap
`omega`, the exact carrier-leading packet overlap derived in the separation
audit is

```text
R_lead(D;omega)
 =a_01*integral cos(omega*(D+s_1+s_2))
                  p_q(ds_1)p_q(ds_2),               (3.2)

q=alpha_0+alpha_1,
a_01=M(q)^2/[M(2*alpha_0)M(2*alpha_1)]>0.           (3.3)
```

The alternative row convention has `s_1-s_2`; in either case the local
shift `u` lies in `[-w,w]`.

Choose all collateral depths equal to

```text
alpha_1=alpha_0-L^(-2)                              (3.4)
```

and their gaps as in (1.3).  Write `D=L*x`.  Since `q`, `a_01`, and the
local probability law are then common to every `j`, (3.2) gives the exact
identity

```text
sum_j lambda_j*R_lead(D;c_j/L)
 =a_01*integral P(x+u/L) dp_q^(2)(u).                (3.5)
```

By Lemma 2.1 on (2.4), the right side is at most `-a_01*eta` throughout
`I_L` for all sufficiently large `L`.

The unnormalized carrier coefficients do not disturb this sign.  Their
ratio to the selected leading cross scale has the common positive form

```text
b_j(D)/b_0(D)
 =r_L*exp(-D/L^2),        r_L>0,                    (3.6)
```

because all collateral depths are equal.  Thus (3.6) factors out of the
sum in (3.5).

For the complete separated fixed-width pair block, the same-lobe and
reverse-cross pieces are respectively

```text
O(exp(-alpha_1*D)),
O(exp(-2*alpha_1*D))                                (3.7)
```

relative to the dominant cross scale.  The exact selected negative mode
differs from its leading cross mode by the same order.  Since
`alpha_1=alpha_0-L^(-2)` stays bounded away from zero and
`D>=d_0*L`, the total perturbation of the finite sum in (3.5) is
`O(exp(-alpha_1*d_0*L))`, while its negative margin is fixed.  Hence (1.4)
holds for the exact fixed-width compressed responses once `L` is large.
The common endpoint-flat cutoff and Fourier-truncation transfer of
`ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md`, Section 5, applies
uniformly to this fixed finite packet family, so its finite-Gabor errors can
also be made smaller than the fixed margin.

## 4. Convex infeasibility on the carrier-weighted ensemble

Let `dw(D)>=0` be arbitrary positive ensemble weights and let `b_0(D)>0`
be the selected cross carrier.  After normalizing by

```text
B_0=integral_(I_L) b_0(D)dw(D),
dnu(D)=b_0(D)dw(D)/B_0,                              (4.1)
```

every possible positive carrier-weighted separation profile is a
probability `nu` on `I_L`; conversely every such probability arises from
positive weights by dividing by `b_0(D)`.

For pair `j`, keeping its collateral contribution nonpositive requires its
normalized cosine response to obey

```text
integral R_(j,L)(D)nu(dD)>=0.                        (4.2)
```

The common positive factor (3.6) can either be retained in the response or
absorbed into a further positive reweighting; the pointwise dual certificate
uses the former.  If all inequalities in (4.2) held, then

```text
0<=sum_j lambda_j*integral R_(j,L)dnu
  =integral [sum_j lambda_j*R_(j,L)(D)]dnu(D)<0,     (4.3)
```

contradiction.  No norm estimate, discrepancy estimate, or minimax limit is
being hidden in (4.3).  It is finite-dimensional Farkas separation with an
explicit strictly negative trigonometric dual.

Because the whole support in (4.1) has `D=Theta(L)`, every constituent is
at carrier scale.  The failure is therefore stronger than the earlier
zero-delay normalization loss: for the adversarial finite cluster, there is
no positive profile on the carrier interval at all.

## 5. Compatibility with the current divisor inputs

Take one selected pair at depth `alpha_0` and the `m` collateral pairs in
(1.3).  The selected pair is uniquely deepest, since the common depth drop
is positive.  Nevertheless

```text
b_j(D)/b_0(D)=exp(-D/L^2+O(L^-2))=1+O(1/L)          (5.1)
```

uniformly on `I_L`, so every collateral row remains carrier-sized.

The ordinate cluster has diameter `O(1/L)` and contains the fixed number
`m` of distinct simple pairs.  Present inputs impose no lower spacing
between distinct simple zeros, and the unit-window Riemann--von Mangoldt
bound permits `O(L)` points.  In the existing carrier range
`2*alpha_0*d_1<1` (in particular the audited `alpha_0<=1/2`,
`d_1<2/3` range), adding or replacing a fixed number of formal pairs
changes:

```text
global and local counts                 O(1),
simple-zero proportion                  O(1/N),
horizontal-density counts               O(1),
leading trace/Frobenius ledgers          o(N).       (5.2)
```

Thus neither a large-sieve argument requiring separated ordinates nor an
average pair-correlation statement excludes the counterconfiguration.
The construction is an allowed abstract divisor model, not a claim about
the actual locations of zeta zeros.

## 6. Coherent arithmetic terms remain

The theorem concerns a **positive ensemble of separate packet forms**, for
which the dependence on `nu` is linear and (4.3) applies.  It does not cover
a coherent superposition

```text
f=integral a(D)f_D dD.                               (6.1)
```

The quadratic form of (6.1) contains every `D,D'` cross term.  An
autocorrelation multiplier such as

```text
|integral a(D)exp(i*omega*D)dD|^2                   (6.2)
```

comes precisely from those off-diagonal terms; it cannot be retained while
evaluating the prime, pole, archimedean, and collateral operators only on
the diagonal `D=D'` blocks.

Accordingly (1.4) sharply falsifies the proposed adaptive **positive-
measure** escape, but does not sign the actual von Mangoldt operator on a
coherent multiscale state.  Such a state is the rank-one/common-space branch
of the previous SDP audit and must supply a carrier-sized favorable
off-block remainder together with acceptable full-form cost.  No current
arithmetic estimate proves that.

## 7. Exact conclusion

For every fixed carrier-producing separation interval
`[d_0L,d_1L]`, a constant-size microscopic near-tie collateral cluster can
be chosen so that every adaptive positive separation profile leaves at
least one collateral pair with the phase-flipped, screening sign.  The
cluster is compatible with all currently used local count and first-moment
inputs.

Hence the finite-list adaptive loophole cannot be used as a uniform
divisor-side theorem.  To proceed one would need either:

1. a new actual-zeta spacing/orientation statement excluding this finite
   near-tie configuration; or
2. a coherent cross-scale construction with all arithmetic off-diagonal
   terms controlled at the same fixed-power carrier scale.

Neither is supplied by positive separation averaging itself.
