# Target-conditioned harmonic cascades and the critical-line compensation wall

Status: R90 exact centered harmonic ledger, optimal target-reserve bound,
all-degree trigonometric moment countermodel, critical-line compensation
construction, and quantitative branching audit.  A zero at `1-e+iT` does
not, by prime-side positivity and zero counting alone, force a near-right
zero at `2T` or at any other harmonic.  Ordinary critical-line zeros can
carry the entire required signed displacement.  Consequently the proposed
cascade stops before its first generation.

This report does **not** prove a fixed zero-free strip, and it does not prove
that no fixed zero-free strip exists.  It closes the idea that the signed
cross-dilate estimate left open in R88 can be obtained by iterating
nonnegative trigonometric polynomials, tensoring them, or feeding their
compensating Poisson mass into zero-density estimates.

```text
conductor-cancelled prime positivity                    EXACT
target pole at T                                        RETAINED
sample 2+cos(theta)-cos(2theta)                         NO TARGET RESERVE
best leading target/pole reserve                        <=(sqrt(2)-1)^2/e
forced Poisson mass at a child                          AGGREGATE ONLY
forced near-right child zero                            FALSE FROM THESE INPUTS
critical-line compensation budget                       >> TARGET RESERVE
single-child cascade                                    ZERO-DENSITY COMPATIBLE
uniform branching from positivity                       NOT AVAILABLE
fixed zero-free strip                                   NOT PROVED.       (1.1)
```

## 2. Exact centered ledger

Put

```text
D(s)=-zeta'(s)/zeta(s),                 sigma=1+delta>1.          (2.1)
```

For a finite real trigonometric polynomial

```text
P(theta)=a_0+sum_(1<=k<=m)a_k cos(k theta),                       (2.2)
```

absolute convergence gives

```text
F_P(delta,T)
 :=a_0D(1+delta)+sum_(1<=k<=m)a_k Re D(1+delta+i kT)

 =sum_(n>=2)Lambda(n)n^(-1-delta)P(T log n).                     (2.3)
```

Thus

```text
P>=0  ==>  F_P(delta,T)>=0.                                     (2.4)
```

Use the notation from R88

```text
Z_delta(u)
 =sum_rho (1+delta-beta)/[(1+delta-beta)^2+(u-gamma)^2],          (2.5)
```

and write the real explicit formula as

```text
Re D(1+delta+iu)=H_delta(u)-Z_delta(u),                           (2.6)
```

where

```text
H_delta(u)=1/2 log(|u|/(2pi))+O_delta(1),       |u|>=2.           (2.7)
```

The `O_delta(1)` in (2.7) is explicit from the pole, trivial zeros,
digamma term, and the harmless Hadamard convention constant.

Assume the high conductor is cancelled:

```text
sum_(k>=1)a_k=0.                                                 (2.8)
```

Then

```text
sum_(k>=1)a_k H_delta(kT)
 =C_P+O_(P,delta)(T^(-2)),

C_P=1/2 sum_(k>=1)a_k log(k/(2pi))+C_(P,delta),                  (2.9)
```

where `C_(P,delta)` is independent of `T`.  Equivalently, if

```text
X_delta(u)=Z_delta(u)-1/2 log(|u|/(2pi)),                         (2.10)
```

then the whole harmonic question is a signed estimate for
`sum a_k X_delta(kT)`.  The logarithmic background has cancelled, but its
bounded prime-side fluctuation has not:

```text
X_delta(u)=-Re D(1+delta+iu)+O_delta(1),
abs(X_delta(u))<=D(1+delta)+O_delta(1).                           (2.11)
```

Let

```text
rho_0=1-e+iT,                         e>0.                        (2.12)
```

Remove its functional-equation quartet from (2.5).  The member `rho_0`
contributes

```text
a_1/(delta+e)+O_P((delta+e)/T^2)                                (2.13)
```

to the signed harmonic zero sum.  The other three members contribute a
bounded term or `O_P(T^(-2))`.  If `J_P^off(delta,T)` denotes the remaining
signed zero sum, (2.3)--(2.9) give

```text
0<=F_P(delta,T)
 =a_0D(1+delta)+C_P
  -a_1/(delta+e)-J_P^off(delta,T)+O_(P,delta)(T^(-2)).            (2.14)
```

Therefore a positive target reserve can force only

```text
J_P^off(delta,T)
 <=a_0D(1+delta)+C_P-a_1/(delta+e)+o(1).                         (2.15)
```

If the right side is negative, the negative harmonic coefficients must
carry more Poisson mass than the positive ones.  Formula (2.15) is an
**aggregate signed demand**.  It does not say where that mass lies
horizontally, and it does not say that any individual negative harmonic
contains a near-right zero.

## 3. The sample polynomial cannot seed the cascade

The motivating example was

```text
P_2(theta)=2+cos(theta)-cos(2theta)
           =(1+cos(theta))(3-2cos(theta))>=0.                    (3.1)
```

It has

```text
a_0=2,              a_1=1,              a_2=-1.                 (3.2)
```

In the small-gap regime,

```text
D(1+delta)=1/delta+O(1).                                        (3.3)
```

Even after deleting every collateral zero and every fixed constant in the
most favorable direction, its target-to-pole comparison is

```text
1/(delta+e) < 1/delta < 2/delta.                                (3.4)
```

Thus (3.1) has no positive target reserve as `delta,e ->0`.  It is an exact
example showing that conductor cancellation and a positive target
coefficient are algebraically compatible; it is not a polynomial capable
of starting a zero-repulsion cascade.

This distinction matters.  Interpreting the `+Z_delta(2T)` in the explicit
formula as a forced compensating zero at `2T` silently deletes the larger
`2D(1+delta)` zero-frequency budget.

## 4. Optimal reserve: even the best polynomial asks for only `O(1/e)`

For every nonnegative trigonometric polynomial,

```text
abs(a_1)<=2a_0.                                                  (4.1)
```

Write

```text
r=a_1/a_0,                         0<r<=2.                       (4.2)
```

Ignore all collateral zeros and all fixed explicit-formula constants.  This
makes the proposed mechanism stronger, so the largest optimistic target
reserve per unit `a_0` is

```text
R_r(delta,e)=r/(delta+e)-1/delta.                               (4.3)
```

If `r<=1`, it is negative for every `delta`.  If `r>1`, elementary
calculus gives

```text
delta_opt=e/(sqrt(r)-1),

max_(delta>0) R_r(delta,e)=(sqrt(r)-1)^2/e.                      (4.4)
```

Consequently

```text
max R_r(delta,e)<=(sqrt(2)-1)^2/e
                  =(3-2sqrt(2))/e.                              (4.5)
```

The shifted Fejer family in R88 approaches `r=2`, so (4.5) is the true
limit of the positive cone, not an artifact of a low-degree search.  The
terms omitted from (4.3) can change fixed constants and degree-dependent
bookkeeping, but they cannot turn the target into a scale larger than
`O(a_0/e)`.

There is a second, more structural way to see the same ceiling.  Normalize
the positive von Mangoldt measure by

```text
dmu_(delta,T)(theta)
 =D(1+delta)^(-1)
  sum_(n>=2)Lambda(n)n^(-1-delta)
  delta_(T log n mod 2pi)(dtheta).                               (4.6)
```

This is a probability measure on the circle, and

```text
c_k:=integral cos(k theta)dmu_(delta,T)(theta)
    =Re D(1+delta+i kT)/D(1+delta).                              (4.7)
```

The normalized size of the target principal part at the first harmonic is

```text
q(delta,e)
 =1/[(delta+e)D(1+delta)]
 =(1+o(1))delta/(delta+e)<1                                     (4.8)
```

in the small-gap regime with `delta/e` fixed (in particular at (4.4)).  So
a target zero does not push the first trigonometric moment outside the unit
moment cone in the regime which maximizes its reserve.  The pole at one is
horizontally closer than the target zero, and that strict inequality is the
leading source of `q<1`.

## 5. An all-degree moment countermodel

The inequality `q<1` admits a particularly simple countermodel to every
harmonic-positivity branching argument at once.  For `0<=q<=1`, define

```text
mu_q=(1-q)dtheta/(2pi)+q delta_pi.                               (5.1)
```

Its real Fourier moments are

```text
integral cos(k theta)dmu_q=q(-1)^k,               k>=1.          (5.2)
```

For every nonnegative trigonometric polynomial, of arbitrary degree,

```text
integral P(theta)dmu_q(theta)
 =(1-q)a_0+qP(pi)>=0.                                           (5.3)
```

Thus the simultaneous harmonic pattern

```text
Re D(1+delta+i kT)=q(-1)^kD(1+delta)                             (5.4)
```

is compatible with **all** scalar trigonometric positivity inequalities,
all Toeplitz/Gram inequalities, and every limit of such inequalities.  At
odd harmonics it supplies a negative prime fluctuation of exactly the scale
which a target requires; at even harmonics it supplies the matching positive
fluctuation.  No near-right child zero has been used.

Phase-shifting the polynomial does not help: `P(theta+phi)>=0`, and its
integral against the same positive measure is still nonnegative.  Thus the
countermodel covers the full complex first-moment information, not only an
accidental cosine projection.

Equation (5.1) is not asserted to be the actual prime phase measure at the
ordinate of a zeta zero.  Its role is logical and exact: the positive moment
cone plus the target magnitude (4.8) does not separate a target-zero
configuration from a legal all-harmonic moment sequence.  Any proof must
use arithmetic information about the actual measure (4.6) conditioned on
`rho_0`, not another consequence of its positivity.

The countermodel also disposes of three apparent enlargements.

1. **Growing degree.**  Formula (5.3) is simultaneous in the degree, so
   taking `m=m(T)` does not expose a forbidden finite moment.

2. **Products and tensor powers.**  If `P>=0`, then `P^j>=0` and

   ```text
   integral P(theta)^j dmu_q
    =(1-q) integral P(theta)^j dtheta/(2pi)+qP(pi)^j>=0.          (5.5)
   ```

   Multiplying positivity certificates therefore does not create a sign
   contradiction.  It also ceases to be a linear explicit formula for
   zeta zeros.

3. **Matrix Gram lifts.**  The Fourier sequence of a positive measure is
   positive definite.  Hence every Toeplitz matrix generated by (5.2) is
   positive semidefinite.  The matrix cone contains the same obstruction.

## 6. Ordinary critical-line zeros can realize the required budget

The moment countermodel is not merely a formal coefficient trick.  Its
required displacement at each harmonic is small enough to be carried by
the ordinary critical-line zero cloud while respecting every marginal input
available to the cascade.

### Proposition 6.1 (abstract critical-line compensation model)

Fix `e,delta>0` in the small-gap regime with `delta/e` fixed, put

```text
q=1/[(delta+e)D(1+delta)] in (0,1),                              (6.0)
```

and take `T` sufficiently large that `log T >> 1/e`.  There is a symmetric
abstract multiset of zeros with the following properties.

* It contains the quartet generated by `1-e+iT`.
* Every other zero has real part `1/2`.
* Its counting function satisfies the Riemann--von Mangoldt main term with
  error `O_delta(log U)`.
* In disjoint bounded neighborhoods of every positive harmonic `kT`, its
  critical-line zeros can be arranged so that

  ```text
  Z_delta(kT)
   =1/2 log(kT/(2pi))-q(-1)^kD(1+delta)+O_delta(1),               (6.1)
  ```

  Here `Z_delta` includes the target quartet; its contribution at `k=1` is
  accounted for before the critical-line zeros in that block are adjusted.

In particular, this model has no near-right child zero at any `kT`,
`k>=2`, but it pays the all-harmonic signed budget (5.4).

#### Construction and budget audit

For a concrete baseline, choose positive ordinates by inverting the smooth
Riemann--von Mangoldt main term, then reflect them through zero.  Its
counting discrepancy from the main term is `O(1)`.  Stieltjes summation
against the integrable kernel and its derivative shows that its Poisson sum
at `u` is

```text
1/2 log(u/(2pi))+O_delta(1).                                    (6.2)
```

Equivalently, this is a critical-line multiset having local density

```text
(1/(2pi))log(u/(2pi)).                                          (6.3)
```

and the Riemann--von Mangoldt counting main term.  In a fixed block around
`u=kT` there are `asymp log(kT)` available zeros.  The Poisson kernel of one
critical-line zero is

```text
K_delta(x)=(1/2+delta)/[(1/2+delta)^2+x^2].                      (6.4)
```

Moving one zero from distance, say, `2` to distance `0` changes the value at
the block center by the fixed positive amount

```text
K_delta(0)-K_delta(2)>0.                                        (6.5)
```

Moving in the opposite direction changes it by the negative of this amount.
Continuous motion supplies intermediate values.  Hence moving

```text
O_delta(qD(1+delta)+1)=O_delta(1)                               (6.6)
```

zeros inside each block realizes the displacement in (6.1).  Taking, for
example, blocks of radius `3`, they are disjoint once `T>6`, and the total
interaction from all other blocks is

```text
O_delta(D(1+delta)T^(-2)
        sum_(j not equal k)(j-k)^(-2))=O_delta(T^(-2)).           (6.7)
```

The response map from the block displacements to the sampled Poisson values
has a diagonal bounded away from zero and off-diagonal row sum
`O_delta(T^(-2))`.  For sufficiently large `T` it is invertible by a
Neumann series.  Thus the cross-interactions can be absorbed by simultaneous
continuous adjustments in the same blocks; this justifies the infinite
all-harmonic construction rather than only each finite truncation.
Each move stays inside a bounded interval, so the counting discrepancy
returns to zero after that interval and is `O_delta(1)` inside it.
Symmetrize the construction under `gamma -> -gamma` and add the target
quartet.  This proves the proposition at the level claimed.

For the fixed-strip problem `e` may be small, and it is useful to retain its
scale.  Taking `delta` proportional to `e`, (6.6) becomes `O(1/e)`.  The
imported Vinogradov--Korobov region gives for every possible high zero

```text
1/e << (log T)^(2/3)(log log T)^(1/3)=o(log T).                  (6.8)
```

Thus the unit block contains far more ordinary zeros than the number which
must be moved.  The target reserve (4.5) is below the ordinary local budget,
not above it.

Proposition 6.1 is deliberately an abstract zero configuration, not a fake
zeta function: it need not satisfy the prime explicit formula at every real
ordinate.  It proves the precise no-go needed here.  Riemann--von Mangoldt
counting, zero density near one, functional-equation symmetry, coefficient
conservation, and the existence of the target do not rule out critical-line
payment of the harmonic demand.  A closure using only those inputs cannot
turn (2.15) into a near-right child.

## 7. Why the branching step fails

Write

```text
B_- =sum_(a_k<0)|a_k|.                                          (7.1)
```

If (2.15) yields a deficit `Q>0`, positivity of each Poisson kernel implies
only

```text
sum_(a_k<0)|a_k| Z_delta^off(kT)>=Q,                             (7.2)
```

after favorable terms are discarded.  Pigeonhole gives at best

```text
Z_delta^off(kT)>=Q/B_-                                          (7.3)
```

for one negative harmonic.  Three gaps separate this from a cascade.

### 7.1 Large Poisson mass is not a near-right zero

At `sigma=1+delta`, one critical-line zero within distance one contributes a
positive constant.  Riemann--von Mangoldt permits `O(log(kT))` such zeros in
a unit block, and Proposition 6.1 realizes a block with that capacity.
Therefore the marginal inputs do not exclude payment of any demand of size

```text
Q/B_- << log(kT)                                                (7.4)
```

can be paid without a zero to the right of the critical line.  Equations
(4.5) and (6.8) put the target demand strictly in this range.

### 7.2 Aggregate mass does not force several children

Coefficient conservation gives

```text
sum_(a_k>0)a_k=B_- >=a_1,                                       (7.5)
```

but (7.5) is conservation of **weight**, not of the number of occupied
harmonics.  All of (7.2) may be carried at one harmonic.  Negative support
on many harmonics does not force positive mass at every support point.
Using several polynomials does not repair this: the single moment law
(5.1) satisfies all their inequalities simultaneously.

### 7.3 Even a forced single child would not contradict density

Suppose, much more strongly than proved, that a near-right zero at `U`
forced one near-right zero in `[2U,KU]`.  Iteration would produce only

```text
O(log X/log 2)                                                  (7.6)
```

zeros below `X`.  Every known zero-density theorem permits this.  A single
chain can continue forever without challenging Riemann--von Mangoldt or
near-one density.

For comparison, suppose a genuine theorem forced `b` children per node, all
below `KU`, and each child could arise from at most `M<b` parents.  After
`j` generations it would give at least approximately `(b/M)^j` distinct
near-right zeros below `K^jT`, hence a density exponent

```text
log(b/M)/log K.                                                  (7.7)
```

The imported Guth--Maynard estimate at `sigma=1-eta` has exponent

```text
theta(eta)=15eta/(8-5eta)                                       (7.8)
```

in its displayed range.  Such a hypothetical branching theorem could
contradict density only if

```text
log(b/M)/log K > theta(eta).                                    (7.9)
```

Prime-side positivity supplies neither distinct children, bounded overlap,
nor any `b>M`.  Formula (7.9) identifies what a real cascade theorem would
need; it is not a consequence of coefficient conservation.

## 8. What remains genuinely open

The R88 survivor was a target-conditioned signed joint estimate.  R90 shows
that its word **conditioned** carries all the difficulty.  An estimate
strong enough to proceed would have to exclude the legal moment pattern
(5.1) specifically when `T` is the ordinate of a near-one zeta zero.

One sufficient form is the following.  For a fixed nonnegative,
conductor-cancelled `P` with `a_1/a_0>1`, prove uniformly for every target
`rho_0=1-e+iT` in a proposed strip that

```text
J_P^off(delta,T)>=-R_P(delta,e),                                (8.1)
```

where, for some admissible `delta` proportional to `e`,

```text
R_P(delta,e)
 <a_1/(delta+e)-a_0D(1+delta)-C_P.                              (8.2)
```

Equations (2.14), (8.1), and (8.2) would immediately contradict the target.
But (8.1) must cancel or control the full critical-line cloud jointly across
`T,2T,...`; marginal zero density cannot do it.

A weaker branching version would have to prove that the part of the
negative-harmonic mass in (7.2) contributed by zeros with
`beta<=1-eta` is too small, then force enough distinct right-edge children
to satisfy (7.9).  Proposition 6.1 shows that this is false for the available
counting and positivity axioms.  It would require a new coefficient-specific
prime/zero correlation theorem.

In prime language, the missing statement is a conditional exclusion of

```text
mu_(delta,T) approximately
(1-q)dtheta/(2pi)+q delta_pi                                   (8.3)
```

or of its less rigid finite-moment analogues, under the condition
`zeta(1-e+iT)=0`.  Kronecker almost periodicity makes related phase patterns
possible at unconditioned ordinates, so the target condition cannot be
dropped.

## 9. Decision

The off-wall harmonic cascade does not close the fixed-strip problem.

* The concrete two-harmonic polynomial has no seed reserve.
* The optimal positive polynomial has target reserve only `O(1/e)`.
* For every possible high zeta zero, the known zero-free region places this
  below the `Theta(log T)` critical-line capacity of a unit block.
* A positive circle measure gives an exact all-degree moment pattern which
  pays every polynomial inequality without a near-right child.
* An abstract critical-line zero configuration realizes the same budget
  while preserving Riemann--von Mangoldt counting and all marginal
  near-one density statements.
* The first implication required for iteration--compensating mass implies a
  near-right child--is therefore unavailable.  Even one forced child per
  generation would be too sparse to contradict density.

The surviving research target is not another trigonometric polynomial.  It
is the genuinely arithmetic, target-conditioned cross-dilate estimate
(8.1), or a theorem that forces uniform branching with exponent (7.9).
Neither has been proved here.
