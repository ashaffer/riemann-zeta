# Uniform-strip iteration: the exact frontier after the Gabor and two-lobe audits

Status: synthesis of the completed 2026-08-11 iteration.  The unconditional
statements below are theorem-level results about the explicit finite Gabor
models and their zero-side hypotheses.  The conditional statements are
labelled.  **No uniform zero-free strip for zeta is proved.**

## 1. Executive verdict

The iteration produced four substantive advances.

1. A single fixed-depth off-line pair cannot be screened by any admissible
   collection of simple on-line atoms: after endpoint jets its negative edge
   remains

   ```text
   K >= X^(alpha-o(1))/L.
   ```

2. That conclusion does not extend to several off-line pairs using only the
   current Riemann--von Mangoldt, simple-line-density, trace, Frobenius, and
   pair-correlation inputs.  A hostile-audited sparse tapered `k=3` island
   obeys all of those inputs and has

   ```text
   0<K<=X^(2*alpha/3+o(1)).
   ```

   It is an artificial zero configuration, not a claimed zeta-zero set.
   It proves that the existing bulk information is logically insufficient
   for the previously sought near-isolated carrier bound.

3. The symmetric two-endpoint-lobe construction gives an exact conditional
   ledger, but its universal target hypothesis is now refuted on the current
   bulk input class for every fixed `a<1/2`.  An exact-density, inward-
   truncated, Gevrey-tapered `k=2` island has

   ```text
   ||Q|E_a||<=X^(alpha/2+o(1))
   ```

   while preserving the count, density, trace, Frobenius, and pair-
   correlation ledgers.  Thus neither the formal `0.597907...` edge nor the
   later symmetric conditional `3/4` edge follows from those inputs.

4. An asymmetric allocation crosses the exact-density `k=2` frame threshold,
   but its formal center-carrier target is not countermodel-safe.  Give a free
   lobe relative length `a>1/2` and a short seed lobe length `b=o(1)`.  Their
   center separation is

   ```text
   d=1-(a+b)/2.
   ```

   The formal power gate is

   ```text
   alpha*d>a/2,
   equivalently alpha>a/(2-a-b).
   ```

   Letting `a` decrease to `1/2` and `b` to zero gives `alpha>1/3`, or the
   formal right edge `5/6+epsilon`.  But then `d>2/3`, and the audited
   power-length varying-depth `k=3` island has full edge only
   `X^(2*alpha/3+o(1))`; it refutes that universal target premise.

   The first target not contradicted by the **`k=3` cap alone** uses two
   packet centers at a fixed separation `d_*<2/3` inside the same asymmetric
   lobes.  Its gate is

   ```text
   alpha*d_*>a/2.
   ```

   Letting `a` decrease to `1/2` and `d_*` increase to `2/3` gives the formal
   conditional threshold `alpha>3/8`, or right edge `7/8+epsilon`.  The
   augmented-row audit now refutes derivation of that target from the
   abstract operator-ledger bulk class too: a single completed mirror block makes the
   aggregate row equal to its selected cross carrier.

None of the `0.597907...`, `3/4`, `5/6`, or `7/8` edges is proved.  The
`5/6` premise and the operator-ledger-derived `7/8` premise are both refuted
on their stated abstract classes.  The `7/8` exponent remains only an algebraically
correct actual-zeta implication after its augmented target-angle hypothesis
is assumed explicitly.

## 2. Unconditional carrier theorems

### 2.1 One pair versus on-line atoms

For one core pair of depth `alpha`, put every other local atom simply on the
critical line and impose the endpoint jets.  A binomial-tail packet retains
an endpoint layer of width

```text
s_0=O(sqrt(mL/T)).
```

Its selected hyperbolic response is

```text
kappa_jet
 >=c_alpha*L^(-2)*exp(alpha*L-C*alpha*sqrt(mL/T))
 =X^(alpha-o(1))/L.
```

The unit-window zero count bounds the complete on-line Gram operator by only
`L^O(1)`.  It cannot absorb this response.  This proves the full-power
single-pair edge; it also proves that every successful sparse screen must
use at least one additional off-line positive mate.

Source:
[`ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md`](ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md).

### 2.2 Sparse multipair screening survives the bulk moments

Let `L=log X`, choose pair centers at spacing `6*pi/L`, and taper their
depths from `alpha` at the center to `2*alpha/3` with a Gevrey-flat profile
over an island of ordinate length `H`.  If

```text
H*eta/L^8 -> infinity,
H*X^(4*alpha/3)=o(T),
```

then exact sampling and bilinear Poisson summation give

```text
0<K<=X^(2*alpha/3+o(1)).
```

The same configuration has bounded Riemann--von Mangoldt discrepancy,
global off-line density `o(1)`, and changes the leading trace, Frobenius, and
pair-correlation moments by `o(N)`.  Canonical logarithmic padding permits
`H=X^(alpha/3)` for every fixed `alpha<1/2`; even the weakest admitted
padding is covered for `alpha<3/8`.

Source and independent hostile audit:
[`ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md`](ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md).

### 2.3 What the Frobenius moment does rule out

Concentrating the entire globally allowed off-line fraction into a
positive-length, equal-depth `k=2` block is count-compatible but not
moment-compatible.  Its legal bandwidth-one `q=1` alias has extensive
negative trace

```text
tr((Q_H)_-) >=c*d_H*X_0^(alpha/2).
```

For `H` comparable with `T`, positive on-line filling cannot absorb that
trace, and the squared Frobenius norm exceeds the evaluated Zeta23 moment by
a fixed power.  In contrast, sublinear blocks with

```text
H*X_0^alpha=o(T)
```

remain compatible with all bulk inputs and can have exponentially bad
arbitrary-data frame conditioning.  Bad conditioning alone is not the
selected-row Birman--Schwinger inequality required for screening.

Source:
[`ZETA23-LOCAL-K2-CLUSTER-MOMENT-BARRIER-2026-08-11.md`](ZETA23-LOCAL-K2-CLUSTER-MOMENT-BARRIER-2026-08-11.md).

## 3. Symmetric obstruction and asymmetric conditional escape

Let

```text
C_0=3/2-(1/sqrt(2))*cot(1/sqrt(2))=0.672500703679...,
r_0=(1-C_0)/2=0.163749648160....
```

Anthropic's theorem implies at most `(r_0+o(1))N` off-line hyperbolic
positive rows.  One endpoint lobe of relative length `a` has Shannon
dimension `(a+o(1))N`.  Jets and a mesoscopic collar cost `o(N)`, so the raw
dimension ledger has slack for every `a>r_0`.  The earlier pointwise-prime
version also fit all active cross-prime-power rows into `o(N)`, but the
one-witness audit below proves that this was unnecessary: the whole
cross-prime sum is one aggregate row.

The same-lobe prime term is at most `X^(a/2+o(1))`.  A cross-lobe response to
a depth-`alpha` pair at the lobe-center displacement has scale
`X^(alpha*(1-a)-o(1))`.  Therefore a target-conditioned joint interpolation
theorem with only subpower loss would close when

```text
alpha*(1-a)>a/2.
```

This proves a conditional implication, not its hypothesis.  The sparse
`k=3` island proves that the hypothesis cannot hold uniformly on the current
abstract zero-side class for `a<1/3`: otherwise the constructed test would
force a carrier edge larger than the island's proved operator norm.  Global
dimension counting also fails more generally because a locally saturated
pair block has an explicit binomial singular vector with

```text
sigma_min
 <=C*sqrt(aL)*q^(1/4)*sin(pi*a+o(1))^q,
```

for every fixed `a<1/2`.

The sharper inward-lobe audit closes the apparent gap `1/3<a<1/2` on the
same abstract input class.  At exact local density use pair-center spacing
`4*pi/ell`, terminal depth `alpha/2`, a Gevrey taper to the distinguished
depth `alpha`, and a polylogarithmic island.  Retreat the two physical lobes
a fixed amount inside `+-ell/2`.  The `q=+-2` reciprocal aliases are then
outside the sum-support, while `q=+-1` has scale `X^(alpha/2)`.  Consequently

```text
||Q_(k=2)|E_a||<=X^(alpha/2+o(1)),       a<1/2.      (3.9)
```

The island changes the legal Zeta23 moments by `o(N)`.  Thus the universal
symmetric target lower bound at `a>1/3` is false on the current bulk class.
This is an artificial Gabor configuration, not an actual-zeta claim.

There is nevertheless an exact positive threshold.  The separated Hilbert--
Ingham inequality gives, for row gaps at least `6*pi/L`,

```text
(a-1/3)*L*||c||_2^2
 <=integral_I abs(sum_j c_j*exp(i*gamma_j*t))^2dt,
```

so `a>1/3` stably handles the separated `k=3` frequency skeleton.  For
exact-density `k=2` gaps `4*pi/ell`, the corresponding threshold is
`a>1/2`.

This motivates the asymmetric allocation.  Let the free lobe have length
`aL`, `a>1/2`, and the seed have length `bL`, where

```text
b->0,       bL/sqrt(eta*L)->infinity,
b*L^2/exp(eta)->infinity.
```

The free dimension is `(a+o(1))N`; every zero and jet condition, together
with the single aggregate arithmetic row, still fits algebraically.  A
periodic endpoint mirror has constant cost in the point-packet model.  It has
a finite-band realization with only
`X^o(1)` loss for the polylogarithmic `k=2` island: choose inverse-polylog
packet width.  It does **not** transfer at useful power to the canonical
`H=X^(alpha/3)` varying-depth `k=3` island.  Uniform phase matching requires
packet width `w=o(1/H)`, while the normalized endpoint carrier is
proportional to `w`; this loses a fixed power.  Exact repetitions of the full
row parameter merge harmlessly, but same-ordinate rows of different depths
remain confluent.  What is not proved is the uniform bridge through
aperiodic collision groups of order `O(L)` and near-critical chains.

Localizing ordinates into blocks of width `R=log L` does not produce that
bridge from counts alone.  For rows `exp(i*j*epsilon*t)`, `0<=j<=R`, the
normalized `R`-th finite difference has lobe norm at most

```text
C*sqrt(L)*(C*epsilon*L)^R.
```

RvM gives no lower bound on `epsilon`; `epsilon=exp(-L)` forces an
arbitrary-data inverse cost `exp(Omega(LR))`.  Natural divided differences
can remove this factor only for the matched seed datum, so the exact missing
inequality is a target-conditioned Moore--Penrose/Hermite bound, not a local
dimension surplus.

The formal center carrier has scale

```text
X^(alpha*(1-(a+b)/2)-o(1)),
```

whereas the largest same-lobe prime term is `X^(a/2+o(1))`.  This gives the
formal gate `alpha>a/(2-a-b)` and limiting edge `5/6+epsilon`, whose zero-side
premise the `k=3` island refutes.  Retaining instead a packet separation
`d_*<2/3` gives `alpha*d_*>a/2` and the limiting conditional edge
`7/8+epsilon`.  That exponent ledger survives, but its universal bulk
premise does not: the exact completed one-pair block refutes target retention
after adjoining the aggregate arithmetic row.  The implication remains
valid only when that coupled actual-zeta property is assumed explicitly.  It
does not require pointwise prime-power interpolation.

Source:
[`ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md`](ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md).

New symmetric and asymmetric audits:
[`ZETA23-TWO-LOBE-ONE-THIRD-SIGNED-GATE-2026-08-11.md`](ZETA23-TWO-LOBE-ONE-THIRD-SIGNED-GATE-2026-08-11.md)
and
[`ZETA23-ASYMMETRIC-TWO-LOBE-HALF-PERIOD-GATE-2026-08-11.md`](ZETA23-ASYMMETRIC-TWO-LOBE-HALF-PERIOD-GATE-2026-08-11.md).

## 4. The cross-prime cloud is one target-aligned row

For two independently polarized lobes, fixing the seed `r` makes the full
cross-prime contribution exactly

```text
-2*Re <ell,B_pr*r>,
B_pr*r=sum_n Lambda(n)/sqrt(n)*P_-T_(log n)r.        (4.1)
```

Every prime power and the conjugate orientation are already present in
(4.1).  Hence `Re <ell,B_pr*r>=0` is one real equation; the convenient
stronger condition `<ell,B_pr*r>=0` is one complex row.  Pointwise
prime-power nulling is sufficient but unnecessary.  Its exact Wiener
factorization and atomic dual remain valid for that optional stronger route,
but they are not an independent intrinsic gate.

The simplification does not provide target leverage.  If `A` is the
positive-zero sampling map, `S=ker A`, `g=P_S B_pr*r`, and `a` is the
selected negative row, adjoining the aggregate complex row changes the
homogeneous target leverage by the exact identity

```text
||P_(S intersect g^perp)a||^2
 =||P_S a||^2-|<P_S a,g>|^2/||g||^2.                (4.2)
```

The right side may be zero independently of `dim S`.  This alignment is
not an artificial linear-algebra corner case.  The fully completed
arithmetic operator equals the zero-side operator by the explicit formula.
After the positive rows and smaller terms are removed, its lobe off-diagonal
block contains the selected term

```text
-2*y_0^-*conj(<r,y_0^+>),                           (4.3)
```

which is exactly parallel to the negative target row and has the carrier
scale.  Cancelling the completed aggregate can therefore cancel the carrier
itself.  At the additive edge, where pole and archimedean cross terms are
power-negligible, the raw-prime row differs from this target-aligned row only
by those small terms.

This possibility is now an exact countermodel, not merely a warning.  Take
orthonormal lobe coordinates `u,v` and

```text
x=sqrt(k/2)*(u+v),       y=sqrt(k/2)*(u-v).
```

The pair operator is the pure cross block
`2k*(u*v^*+v*u^*)`.  For a seed `s*v`, positive-row nulling forces the free
coordinate to be `-s*u`, so its aggregate scalar is `-2k*abs(s)^2` and its
full completed cross contribution is `-4k*abs(s)^2`.  Even the minimal
one-real aggregate equation is therefore
infeasible unless `s=0`, which deletes the carrier.  With
`k=X^(alpha*d_*)`, its Frobenius cost is `o(N)` for every
`alpha<1/2,d_*<2/3`; at the abstract operator-ledger level it may be inserted
into the moment-compatible on-line background without changing any leading
bulk input.  The selected pair block also has a normalized asymmetric
Paley--Wiener/Gabor realization.  Two equal fixed-width packets separated by
`d_*L` compress the exact kernel `(2/L^2)cosh(alpha*(t-s))` to

```text
(2*A_alpha^2/L)*[[1,cosh(alpha*d_*L)],
                 [cosh(alpha*d_*L),1]].
```

Its midpoint imbalance is an exact Lorentz boost, so spectral
re-factorization gives the balanced mirror rows; a common binomial cutoff
imposes all growing endpoint jets with superpolynomial transfer error.  What
is not realized is the aggregate as a sum of the actual positive von
Mangoldt atoms.

For the asymmetric center `Y=X^d`, the hypothetical residue itself has size
`Y^alpha`.  A direct fixed saving below that size is strip-strength;
aggregate cancellation converts the same issue into the angle (4.2), not a
dimension theorem.  A high-mode reservoir is not presently certified.  All
legal **absolute** phases remain in `[T,2T]`, so the coherent phase-zero
prime value is unavailable.  For `Y<T`, an ordinary mean square guarantees
only a `sqrt(log Y)` reservoir, while KMT permits a target value of size
`sqrt(Y)/(log Y)^(3/10)`.  Endpoint and positive-row projection can only
worsen this comparison.

Nor does `L=C log T`, `X=T^C`, give a free escape.  For a putative zero at
`1-delta+i*gamma`, the target and pole/main cross scales have ratio

```text
T^(C*(1/2-delta))/T^(C/2-1)=T^(1-C*delta).          (4.4)
```

If `C*delta>1`, the available pole budget is larger.  If `C*delta<1`, that
budget is smaller, but after collateral zero rows are controlled the leading
completed aggregate is the target-aligned block (4.3); without such control,
the collateral rows are the original screening problem.  Equality has no
power margin.  Exact pole nulling only appends a finite row and returns to
(4.3).

The collateral problem now has a sharp but still conditional depth split.
For a selected carrier `k_0=X^(alpha*d-o(1))/L`, normalized strip sampling
proves that on-line rows and all collateral depths
`beta<=alpha*d-epsilon` contribute `o(k_0)`.  Current density and local-count
theorems do not supply that isolation: one pair at depth
`alpha-o(1/L)` is allowed.  An exact two-pair hyperbolic block shows that one
such pair can provide a constant-cost transverse reservoir while changing
the leading count/trace/Frobenius ledgers by `o(N)`.  This last construction
is presently an **abstract operator/moment** countermodel, not a normalized
two-pair PW/Gabor realization.  Neither deepest-zero selection, an `O(L)`
near-tie chain, nor separation averaging resolves the gap; a same-height or
`o(1/L)` ordinate cluster defeats the latter.  The exact actual-zeta question
is a coefficient-specific projected-angle bound, not another density count.

Sources:
[`ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`](ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md)
and
[`ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md`](ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md).

Exact countermodel and scope:
[`ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md`](ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md).
Normalized selected-pair realization:
[`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md).
Collateral depth/angle audit:
[`ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md`](ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md).
The actual-pair quantifier and truth-value equivalence are audited separately
in
[`ZETA23-CONDITIONAL-SEVEN-EIGHTHS-LOGIC-AUDIT-2026-08-12.md`](ZETA23-CONDITIONAL-SEVEN-EIGHTHS-LOGIC-AUDIT-2026-08-12.md).

The optional stronger pointwise route remains documented in
[`ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`](ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md).

## 5. Exact remaining theorem

A zero-free strip from this route now requires one coupled theorem, not a
collection of independent optimistic estimates.  For every hypothetical
core pair of depth at least a fixed `delta>0`, construct an admissible test
such that

1. the complete signed zero carrier, including every other off-line pair,
   has a quantitatively negative target-conditioned edge;
2. endpoint/collar leakage is little-o of that actual edge;
3. the complete prime, pole, and archimedean form is little-o of the same
   edge; and
4. all estimates are uniform in ordinate and in the hypothetical zero
   configuration allowed by actual zeta, not merely by its current bulk
   moments.

At the two-lobe level, the formerly described “countermodel-safe” asymmetric
target is now refuted on the abstract operator-ledger class.  A collision-stable theorem
in a free lobe of width `a>1/2`, seed width `b=o(1)`, and separation
`d_*<2/3` would yield the conditional `7/8+epsilon` edge only if it explicitly
assumed that adjoining the actual aggregate arithmetic row preserves affine
feasibility and the target angle (4.2).  The exact mirror block proves that
the stated counts and moments do not imply this assumption, even for one
off-line pair.  The symmetric `3/4` premise is refuted by the inward sparse
`k=2` island, and the formal asymmetric `5/6` premise is refuted by the
power-length `k=3` island.  Recovering any edge now requires genuinely new
actual-prime/actual-zero information excluding the corresponding geometry.

The completion-preserving Type-II route reaches the same barrier in scalar
form: its first missing estimate is a fixed power saving for the full
ordinary-product energy after every Vaughan head and conductor sector has
been restored.  Current Vinogradov--Korobov/KMT inputs give only subpower or
logarithmic savings.  Calling that estimate “Type II” does not make it
weaker than a strip.

The subsequent escape census closes the remaining generic witness-engineering
variants.  Positive multi-witness/multiscale ensembles reduce to a PSD SDP
whose aligned optimum is rank one; signed weights lose the negative-witness
inference.  Low-order determinants see the selected pair but their adaptive
arithmetic minor is a new correlation theorem.  Critical pole/main resonance
does not add a completed direction because the growing pole row cancels the
continuum prime main row exactly.  Every Mellin-scale filter multiplies a
target residue and its completed arithmetic pole by the same factor.  The
only surviving escape is therefore an actual coefficient-specific
target-transverse prime/collateral state, or a direct strip-strength
arithmetic bound.  The full classification is
[`ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md`](ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md).

The opposite assertion is not established either.  Writing
`Theta=sup Re(rho)`, RH is `Theta=1/2`, whereas failure of every fixed strip
is `Theta=1`.  Standard universality excludes winding targets, a
positive-density winding version contradicts zero-density, and known prime
and Mobius omega theorems remain at exponent `1/2`.  See
[`ZETA23-NO-UNIFORM-STRIP-OPPOSITE-HYPOTHESIS-AUDIT-2026-08-12.md`](ZETA23-NO-UNIFORM-STRIP-OPPOSITE-HYPOTHESIS-AUDIT-2026-08-12.md).

## 6. Publication judgment

The combination of the single-pair theorem, the moment-compatible sparse
screens, the local `k=2` moment barrier, the symmetric no-go, the asymmetric
conditional threshold ledger, and the aggregate-row reduction is
potentially publishable as a focused
obstruction/strategy paper after specialist review.  Its novelty is the
coupled theorem/no-go architecture and the explicit counterconfigurations,
not a result about the actual location of zeta zeros.  A paper must state
prominently that no uniform strip and no RH proof follows.
