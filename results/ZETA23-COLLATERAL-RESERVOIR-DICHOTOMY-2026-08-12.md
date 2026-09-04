# Collateral zeros can supply a moment-invisible transverse reservoir

Status: exact depth-stratified reduction, an exact abstract two-pair
reservoir block, and count/moment audit, 2026-08-12.  The construction is an
artificial completed-operator configuration, not a proved normalized Gabor
realization, the zeta divisor, or the actual von Mangoldt sequence.  No
zero-free strip is proved or disproved.

Subsequent update: the exact three-coordinate orientation below remains an
abstract model, but a different and simpler normalized target-only screening
mechanism has now been proved.  See
[`ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md`](ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md).

## 1. Verdict

Current zero density, local counts, trace, Frobenius, and pair-correlation
inputs do **not** force the collateral aggregate row to be target-parallel,
and they do not make a carrier-sized transverse component expensive.

There is one useful positive dichotomy.  Let a distinguished rightmost pair
have depth `alpha`, and let the retained asymmetric carrier scale be

```text
k_0=X^(alpha*d-o(1))/L,          1/2<d<2/3.          (1.1)
```

All on-line rows and all collateral pairs of depth at most

```text
beta<=alpha*d-epsilon                              (1.2)
```

have complete compressed operator norm `o(k_0)`.  Hence a carrier-sized
target-transverse completed aggregate requires at least one collateral pair
above the line

```text
Re rho=1/2+alpha*d-epsilon.                          (1.3)
```

This is the exact depth gate supplied by the present sampling bounds.

It does not close a strip.  Every known density theorem permits one such
pair, and one pair can suffice.  An explicit two-pair block has:

1. a unique deepest selected pair;
2. one collateral pair only `L^(-2)` shallower;
3. a constant-cost solution of both positive-row equations and even the
   complex completed aggregate equation;
4. the selected negative carrier intact, with an additional favorable
   collateral square; and
5. only `O(1)` count changes and `o(N)` trace/Frobenius cost.

Thus choosing an almost-rightmost zero does not create a usable gap.  A new
input would have to exclude a second simple pair at depth
`alpha-o(1/L)`, or control its signed orientation relative to the actual
prime aggregate.  None of the current global or local statistics does so.

The scope is binary:

| Statement | Status |
|---|---|
| shallow collateral below (1.2) is subcarrier | proved for the normalized PW/Gabor rows |
| the normalized selected one-pair mirror block is target-aligned | proved in the cited mirror/aggregate audits |
| one near-tie pair can supply the transverse reservoir (4.1)--(4.9) | exact in the abstract hyperbolic operator class |
| the same three-coordinate orientation occurs in a normalized two-pair PW/Gabor compression | open |
| a normalized target-only collateral screen exists by another orientation | proved subsequently by the reciprocal-separation phase flip |
| the actual zeta collateral sum has or lacks the required transverse angle | open |

Thus the card gives a rigorous conditional isolation theorem and a rigorous
moment-level no-go.  It does not promote the latter to a Gabor or actual-zero
counterconfiguration.

## 2. The exact collateral row after quotienting positives

Split the coefficient space into free and seed lobes and fix a seed `r`.
For every reflected off-line pair write

```text
K_j=2*(x_j*x_j^*-y_j*y_j^*).                        (2.1)
```

Let `A` contain the positive rows imposed on the free lobe and put
`S=ker A`.  The completed cross Riesz row is exactly

```text
g=P_-*K_comp*r
 =P_-*K_on*r
  +2*sum_j [x_j^-*conj(<r,x_j^+>)
            -y_j^-*conj(<r,y_j^+>)]
  +g_small.                                         (2.2)
```

Here `g_small` denotes whichever pole, archimedean, collar, and remote terms
have already been proved subcarrier.  For the selected pair `j=0`, after its
positive row is quotiented out,

```text
P_S*g_0=-2*conj(<r,y_0^+>)*P_S*y_0^-.               (2.3)
```

This is the target-parallel obstruction.  Any transverse reservoir must
come from `P_SK_on r` or from the collateral sum `j!=0` in (2.2).

The on-line part cannot do it.  The unit-window count and the elementary
sampling bound give

```text
||K_on||op<=L^O(1),                                 (2.4)
```

whereas (1.1) is a fixed power for every fixed `alpha*d>0`.

## 3. Depth stratification

### Lemma 3.1 (shallow collateral is subcarrier)

Let `C_(<=beta)` be the sum of all reflected-pair operators in the dyadic
band whose depths are at most `beta`.  Under the Riemann--von Mangoldt
unit-window count,

```text
||C_(<=beta)||op<=X^(beta+o(1))*L^O(1).             (3.1)
```

The same estimate holds after every orthogonal lobe, endpoint-jet, positive-
row, or confluent compression.

#### Proof

For a pair at ordinate `gamma_j` and depth `beta_j`, its two exponential
branches are the samples of the same exponential-type-`L/2` transform at
`gamma_j+/-i*beta_j`.  The points lie in the strip `abs(Im z)<=beta`, with
`O(L)` real projections per unit interval.  Apply the unit-window Sobolev
sampling inequality in this horizontal strip: bound the number of samples
by `O(L)` times the local two-dimensional supremum, then control that
supremum by the `x` and `Im z` derivatives of the transform.  Plancherel on
each horizontal line bounds every such derivative by `L^O(1)` times
`exp(beta*L)||p||_2^2`.  Thus no zero-separation hypothesis is being used.
Since `exp(beta*L)=X^(beta+o(1))`, recombining the exponential branches into
the cosh and sinh rows gives

```text
sum_j (abs(<c,x_j>)^2+abs(<c,y_j>)^2)
 <=X^(beta+o(1))*L^O(1)*||c||^2.                    (3.2)
```

The normalization `2/L^2` only improves the displayed polynomial factor.
The norm of the signed difference is bounded by the sum of the two positive
Gram norms.  Orthogonal compression cannot increase operator norm.  QED

Taking `beta=alpha*d-epsilon` in (3.1) proves (1.2)--(1.3).  More generally,
if a transverse component has norm `k_0*X^(-o(1))`, then it cannot be built
from on-line and fixed-gap shallow rows alone.

This is sharp at the level relevant here.  It demands existence of a high
collateral row, not a positive density of them.  The next section shows why
one row is enough.

## 4. Exact two-pair transverse reservoir

Let `u,w` be orthonormal free-lobe coordinates and `v` an orthonormal seed
coordinate.  Fix `k_0,k_1>0` and put

```text
a_j=sqrt(k_j/2).
```

For the selected pair take

```text
x_0=a_0*(u+v),             y_0=a_0*(u-v).           (4.1)
```

For one collateral pair take

```text
x_1=a_1*(u+v),             y_1=a_1*(w-v).           (4.2)
```

Both are algebraically valid rank-`(1,1)` hyperbolic blocks of the form
(2.1) in the abstract completed-operator class.  Section 5 records the
additional normalization issue that prevents calling this a proved Gabor
counterconfiguration.  Fix `r=s*v` and write

```text
ell=t*u+z*w.                                        (4.3)
```

The two positive-row equations coincide and give exactly

```text
t=-s.                                               (4.4)
```

The complete two-pair cross row is

```text
P_-*(K_0+K_1)*(s*v)
 =s*((2*k_0+k_1)*u+k_1*w).                          (4.5)
```

Therefore the complex aggregate equation, and hence its one-real weakening,
is solved by

```text
z=(1+2*k_0/k_1)*s.                                  (4.6)
```

The selected negative coordinate is unchanged:

```text
<ell+r,y_0>=-2*a_0*s,
2*(abs(<ell+r,x_0>)^2-abs(<ell+r,y_0>)^2)
 =-4*k_0*abs(s)^2.                                  (4.7)
```

The collateral positive coordinate also vanishes, while its negative square
is

```text
-4*(k_0^2/k_1)*abs(s)^2.                            (4.8)
```

Thus aggregate cancellation does not delete the negative zero-side value.
It moves the surviving negativity into a collateral free-free square.  If

```text
k_1/k_0=X^o(1),                                     (4.9)
```

then (4.6) has subpower coefficient cost and (4.7) retains the selected
carrier.  For `k_1=k_0`, take `z=3s`; after unit normalization
`abs(s)=1/sqrt(11)`, and every conclusion has a fixed nonzero constant.

This is the requested reservoir: the homogeneous direction `w` is transverse
to the selected target `u`, but it is generated by only one collateral
hyperbolic plane.

## 5. A unique rightmost pair and the realization boundary

Take the selected depth to be `alpha` and the collateral depth to be

```text
alpha_1=alpha-L^(-2).                               (5.1)
```

For equal carrier geometry,

```text
k_1/k_0
 =X^(-(alpha-alpha_1)*d+o(1))
 =exp(-d/L+o(1))=1+o(1).                            (5.2)
```

The selected pair is therefore uniquely rightmost, but (4.9) holds with
room to spare.  Replacing `L^(-2)` by any `o(1/L)` gap gives the same result.

There is no obstruction to **unscaled** finite Paley--Wiener interpolation.
For finitely many distinct evaluation points `z_1,...,z_m` and any nonempty
packet interval `J`, the map

```text
C_c^infinity(J) -> C^m,
f |-> (integral f(t)*exp(i*z_j*t)dt)_(1<=j<=m)     (5.3)
```

is onto.  Indeed, a linear functional annihilating its range would make a
finite exponential polynomial vanish on `J`, hence identically, which is
impossible for distinct exponents.

Surjectivity is not the normalization estimate needed here.  Simultaneously
realizing (4.1)--(4.2) on asymmetric one-sided lobes would require a lower
bound, at the carrier scale, for the relevant joint restriction map

```text
R_J f=(<f,x_0>,<f,y_0>,<f,x_1>,<f,y_1>).            (5.4)
```

Its smallest singular value can hide a fixed power: the two Laplace branches
on a one-sided lobe have naturally unequal norms.  The exact Lorentz
factorization in the one-pair mirror audit removes that imbalance for one
compressed pair, but it does not by itself prescribe the simultaneous
three-coordinate orientation (4.1)--(4.2) for two distinct pairs.  Adding
common-kernel vectors can complete norms only after this carrier-scale
restriction estimate has been proved.

Consequently the reservoir below is rigorous in the abstract hyperbolic
operator/moment class, but this report does **not** claim a normalized
Paley--Wiener/Gabor realization.  Closing that realization would strengthen
the no-go result; failure of the realization would identify a useful new
invariant invisible to the moment ledger.

## 6. Count, density, and moment audit

Start with any legal simple on-line background realizing the leading Zeta23
moments and, at the level of the count/moment model, replace four on-line
points by two reflected pairs assigned the depths above.  Choose their
formal ordinates distinct and a fixed distance apart in the dyadic core.
Then:

```text
Riemann--von Mangoldt discrepancy change       O(1),
unit-window count change                       O(1),
simple-on-line proportion change               O(1/N),
horizontal density count at every line         O(1),
completed-operator perturbation rank            O(1),
leading pair-correlation/Frobenius change       o(N). (6.1)
```

All four formal off-line points may be simple and functional-equation
reflection is exact.  More directly, the abstract blocks themselves have

```text
tr K_0=tr K_1=0,
||K_0||F^2=8*k_0^2,       ||K_1||F^2=6*k_1^2.       (6.2)
```

Indeed, `K_0=2*k_0*(u*v^*+v*u^*)`, while
`K_1=k_1*(u*u^*-w*w^*+u*v^*+v*u^*+w*v^*+v*w^*)`.
Since `alpha<=1/2` and `d<2/3`,

```text
k_0^2+k_1^2=X^(2*alpha*d+o(1))/L^2=o(N).           (6.3)
```

The cross term with the moment-compatible background is `o(N)` by
Cauchy--Schwarz, because `||K_0+K_1||F=o(sqrt(N))`.  Hence the leading trace,
Frobenius, and pair-correlation identities all survive in this abstract
model.  This is precisely the point: counts and the first two operator
moments cannot price the transverse orientation.  It is separate from the
unsettled Gabor-realization question in Section 5.

Horizontal density does not help.  The necessary shallow-row gate (1.3) is
at `Re rho=1/2+alpha*d+o(1)`; Huxley and Guth--Maynard permit a positive power
of `T` there.  The construction uses one pair.  Even at the moving
Vinogradov--Korobov line, an `O(1)` local theorem does not exclude two simple
pairs.  The microscopic Riemann--von Mangoldt bound permits `O(L)` points,
and multiplicity estimates do not constrain two distinct simple zeros.

## 7. Why an almost-rightmost choice does not close the dichotomy

In a finite dyadic zero set one can choose a pair of maximal depth, but no
known theorem gives a uniform gap to the second depth.  The configuration
(5.1) has a unique maximum and an arbitrarily small gap.  It is compatible
with every currently used statistic because those statistics count rows or
average their squared size; none separates the two largest real parts.

The strongest conclusion available from present inputs is therefore:

```text
either
  every collateral pair has depth <=alpha*d-epsilon,
  in which case its aggregate contribution is o(k_0),
or
  at least one high collateral pair exists,
  and present density/moment inputs do not control its target angle.      (7.1)
```

The first branch is a useful **conditional isolation lemma**, not a theorem
about a rightmost zeta zero.  The second branch can occur with one simple
pair, so no iteration, pigeonhole argument, or almost-rightmost selection
forces a density contradiction.

Here are the three natural termination attempts explicitly.

### 7.1 Choose the deepest zero

A deepest zero gives only the weak inequalities `alpha_j<=alpha`.  The
reservoir needs `alpha_j=alpha-o(1/L)`, which is fully compatible with a
unique maximum by (5.1).  Maximality therefore supplies the wrong scale of
separation: the sampling gate needs the fixed depth drop
`alpha-alpha_j>=(1-d)*alpha+epsilon`, not merely a strict inequality.

### 7.2 Iterate through a near-tie chain

Iteration does not manufacture that drop.  A unit ordinate window may, under
the current Riemann--von Mangoldt error, contain `O(L)` distinct simple
points.  For example, the formal depths

```text
alpha_j=alpha-j*L^(-3),       0<=j<=c*L,            (7.2)
```

all have carrier ratios `k_j/k_0=1+o(1)`.  Such a chain changes every global
density or moment ledger by at most a polylogarithmic number of rows.  Even
allowing a much longer chain at separated ordinates is consistent with the
known positive-power horizontal-density bounds.

One could try to impose the negative row of every collateral member of the
chain.  Current counts do not make that a stable operation.  They impose no
lower spacing between distinct simple zeros, and `q+1` ordinates spaced by
`delta` have the normalized finite-difference direction

```text
sum_(j=0)^q (-1)^(q-j)*binom(q,j)*exp(i*j*delta*t)
 =(exp(i*delta*t)-1)^q.                             (7.3)
```

On a lobe of length `O(L)` its size is at most `(delta*L)^q` times the
coefficient scale.  Thus row-by-row elimination can have arbitrarily large
cost when `delta` is arbitrarily small.  Multiplicity bounds do not address
this example because all points are distinct and simple.  A confluent,
target-compatible theorem could overcome (7.3), but no current input is such
a theorem.

### 7.3 Invoke local density or multiplicity

Local counting gives `O(L)` rather than zero possible reservoir rows;
horizontal density gives an average/global upper bound rather than a gap
below the rightmost pair; and multiplicity estimates do not separate two
simple zeros.  Since the abstract reservoir spends one row, all three
estimates are quantitatively on the permissive side.  No finite iteration is
forced to terminate before encountering the unresolved normalized-angle
problem of Section 5.

### 7.4 Adapt the lobe separation or packet offset

Aligning the selected ordinate `gamma_0` and varying the packet separation
does give a genuine Fourier filter, but only away from a confluent cluster.
For `D=D_0+s`, the leading cross coefficient of pair `j`, relative to the
selected exponential growth, has the model factor

```text
exp(-(alpha-alpha_j)*s)
 *exp(i*(gamma_j-gamma_0)*s).                       (7.4)
```

A smooth superposition over `0<=s<=W`, weighted to keep the selected term
coherent, therefore multiplies the collateral term by

```text
(1/W)*integral_0^W psi(s/W)
  *exp(-delta_alpha_j*s+i*delta_gamma_j*s)ds.       (7.5)
```

For `delta_alpha_j*W=O(1)`, repeated integration by parts makes (7.5)
`O_M((1+W*abs(delta_gamma_j))^(-M))`; a positive depth gap gives additional
damping.  Taking `W=L^(1-epsilon)` costs only `exp(O(alpha*W))=X^o(1)` in
endpoint normalization and filters every ordinate gap much larger than
`L^(-1+epsilon)`.

This is a coefficient-level upper-capability calculation.  The positive-row
quotient `S` also changes with the packet geometry, so (7.5) does not by
itself prove that the projected actual aggregate has become small or
transverse.  That only makes the negative conclusion below stronger.

This does not reach the allowed bad case.  A common translation of both
packet centers gives no filter at all, because the exact pair kernel depends
on `t-s` and is translation invariant after demodulation.  Separation
averaging over the whole available aperture has `W=O(L)`, so a same-height
pair survives exactly and a gap `abs(gamma_j-gamma_0)=O(1/L)` receives at
best a constant factor from (7.5).  Flattening the endpoint exponential over
`W` also loses `exp(-Theta(alpha*W))` relative to the endpoint packet; at
`W` proportional to `L` this is a fixed carrier power, not a subpower cost.

The invariant is even clearer without choosing an averaging profile.  On an
interval of length `O(L)`, two ordinate rows obey

```text
||exp(i*gamma_j*t)-exp(i*gamma_0*t)||_2
 <=O(abs(gamma_j-gamma_0)*L)
   *||exp(i*gamma_0*t)||_2.                         (7.6)
```

Thus if `abs(gamma_j-gamma_0)*L=o(1)` (and the depth difference times `L`
is also `o(1)`), every normalized filter that nulls the collateral row while
retaining the selected row pays at least the reciprocal of this small
quantity.  Current local counts and simplicity provide no lower bound on
that separation; they even allow distinct zeros at the same ordinate.
Adaptive separation therefore removes well-separated collateral rows but
does not terminate escape family C uniformly.

## 8. Exact first actual-zeta statement

The missing statement can be written without metaphor.  Let `S=ker A` be
the free-lobe space after **all** positive off-line rows have been imposed,
and let

```text
a=P_S*y_0^-,
c_0=<r,y_0^+>,
h=P_S*(P_-*K_on*r
       +2*sum_(j!=0)[x_j^-*conj(<r,x_j^+>)
                     -y_j^-*conj(<r,y_j^+>)]
       +g_small).                                   (8.1)
```

Then the actual completed aggregate row in the quotient is exactly

```text
g_S=-2*conj(c_0)*a+h.                               (8.2)
```

The first coefficient-specific theorem needed to classify escape family C
is a quantitative bound on

```text
||P_(a^perp)*h||                                    (8.3)
```

together with the affine correction ratio from the augmented projection
formula.  An upper bound `o(k_0*||r||)` proves target alignment under the
chosen isolation hypothesis.  A lower bound
`k_0*X^(-o(1))*||r||`, plus a subpower affine ratio, supplies the transverse
reservoir needed to retain the selected carrier.  Counts and moments give
neither polarity.  Equation (8.3), not another zero count, is the exact
first actual-zeta gate.

## 9. Correct scope frontier

The abstract reservoir proves that count and moment data, viewed as the
constraints they literally impose on the completed operator, do not exclude
escape family C.  It does not prove that a normalized asymmetric Gabor model
has this orientation, or that the actual collateral zeta rows rescue the
asymmetric construction.  For actual zeta one still needs one of three
genuinely new statements:

1. a local depth-isolation theorem strong enough to put every collateral
   pair below `alpha*d-epsilon`; or
2. a signed coefficient-specific theorem showing that the actual collateral
   sum in (2.2) cannot supply the transverse affine correction (4.6) without
   losing the selected carrier elsewhere in the completed form; or
3. a normalized joint Paley--Wiener restriction theorem that either realizes
   (4.1)--(4.2) at scale `k_j=X^(alpha_j*d+o(1))/L`, or proves a quantitative
   invariant forbidding that orientation.

Each statement is substantially stronger than current zero-density,
pair-correlation, or first/Frobenius-moment information.  The exact
one-pair alignment and aggregate scalarization are recorded in
[`ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md`](ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md),
and the normalized one-pair block in
[`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md).
