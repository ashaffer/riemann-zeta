# The conditional `7/8` angle is strip-strength, not an intermediate theorem

Status: hostile logic audit, 2026-08-12.  The corrected asymmetric
two-lobe hypotheses do imply a `7/8+epsilon` right edge.  Their actual-zeta
common-witness package, including the target-angle clause, is unknown and,
with its natural quantifier over actual offending pairs, is truth-value
equivalent to that strip.  A nonvacuous
uniform version over the abstract configuration class is stronger and
false: the exact completed one-pair quotient makes the aggregate row
parallel to the selected target.  No zero-free strip is proved.

## 1. Binary classification

Fix `epsilon>0` and put

```text
alpha_0=3/8+epsilon.                                 (1.1)
```

The three logically different claims have different verdicts.

```text
(A) corrected conditional implication to a 7/8+epsilon edge:  PASS;
(B) augmented target angle for the actual zeta divisor:        UNKNOWN;
(C) universal angle over configurations allowed by bulk data:  FALSE.  (1.2)
```

The `PASS` in (A) requires one common witness satisfying the grouped
positive-zero conditions, the aggregate arithmetic condition, target
retention, and the completed lower-edge estimates.  Proving the zero part
and arithmetic part for different vectors is not enough.  Pointwise
prime-power nulling is a sufficient overconstraint, not a necessary second
theorem; the minimal arithmetic condition is one real aggregate equation.

Claim (B) is not known even though the condition count has large slack.
The exact completed operator makes target alignment natural, and no current
local density, moment, KMT, or mean-square input supplies a transverse
reservoir.

Claim (C) fails already in an exact one-pair quotient.  This is an abstract
operator/configuration countermodel, not a claim that the artificial divisor
is the zeta divisor.

## 2. Why the formal implication is valid

Choose fixed parameters

```text
a>1/2,               1/2<d_*<2/3                   (2.1)
```

sufficiently close to their limiting values that, uniformly for
`alpha>=alpha_0`,

```text
alpha*d_*>a/2+c_epsilon                             (2.2)
```

with fixed `c_epsilon>0`.  The asymmetric packet ledger is then

```text
retained selected carrier: X^(alpha*d_*-o(1)),
same-lobe prime cost:      X^(a/2+o(1)).             (2.3)
```

Assume for one actual offending pair that a single admissible complex
packet satisfies all of the following.

1. Its positive off-line rows are solved collision-stably at subpower cost,
   and all remaining positive zero contributions are `o` of the carrier.
2. Its selected negative response retains the first scale in (2.3).
3. The one real completed cross aggregate, or the stronger convenient
   complex aggregate, is controlled without losing that response.
4. The same-lobe prime form and every pole, archimedean, collar, and remote
   lower-edge error are `o` of the retained response.

The zero-side evaluation is then at most

```text
-c*X^(alpha*d_*-o(1)),                              (2.4)
```

while the completed arithmetic evaluation is bounded below by

```text
-X^(a/2+o(1))-o(X^(alpha*d_*)).                     (2.5)
```

Equations (2.2), (2.4), and (2.5) contradict the exact explicit formula.
Thus no such pair exists.

This is a contradiction between two evaluations/lower edges of the same
completed form.  It should not be described as invoking an already known
global positivity theorem for the completed form; such positivity would be
Weil's RH criterion.  The needed arithmetic lower edge is one of the
conditional hypotheses.

Complex polarization causes no gap.  If the completed matrix `K` is real
symmetric and `z=u+i*v`, then

```text
conj(z)^T*K*z=u^T*K*u+v^T*K*v.                      (2.6)
```

Hence a negative total complex value gives a negative admissible real
value.  The individual null equations need not descend to that real
component; only the total estimates used in (2.4)--(2.5) must hold before
descent.

## 3. Exact one-pair quotient

Let the coefficient space split into a free and seed lobe.  In reflected
pair coordinates the exact zero operator is

```text
K_zero=K_on+2*sum_j (x_j*x_j^*-y_j*y_j^*),          (3.1)
```

and the completed explicit formula is the operator identity

```text
K_comp=K_zero.                                      (3.2)
```

Fix a seed `r`.  Let `A` contain all positive rows imposed on the free
lobe, put

```text
S=ker A,                                             (3.3)
```

and quotient out their range.  For the selected pair define its projected
negative target

```text
a_0=P_S*y_0^-.                                      (3.4)
```

The Riesz row of the complete cross aggregate is

```text
g=P_-*K_comp*r.                                     (3.5)
```

Suppose, in the one-pair quotient, that the selected negative pair is the
only power-sized remaining term.  From (3.1)--(3.5), exactly at that scale,

```text
g_S=P_S*g
   =-2*a_0*conj(<r,y_0^+>).                         (3.6)
```

If `<r,y_0^+>` is nonzero, the aggregate row and target are parallel.  For
the convenient complex aggregate equation, therefore,

```text
P_(S intersect g^perp)*a_0=0.                       (3.7)
```

This is equality in the hostile direction of the exact augmented-angle
formula

```text
||P_(S intersect g^perp)*a_0||^2
 =||P_S*a_0||^2
  -abs(<P_S*a_0,g_S>)^2/||g_S||^2.                 (3.8)
```

Thus neither a large dimension of `S` nor a small number of aggregate
constraints gives any target leverage.  In this quotient the extra row
removes the entire homogeneous selected direction.

### 3.1 Exact two-dimensional block and factors

The alignment can be realized without asymptotic notation.  Let `u` and
`v` be unit vectors in the free and seed lobes, respectively, and for
`k>0` put

```text
x=sqrt(k/2)*(u direct-sum v),
y=sqrt(k/2)*(u direct-sum (-v)),
K_0=2*(x*x^*-y*y^*).                                (3.9)
```

In the basis `(u,v)`,

```text
K_0=2*k*[[0,1],[1,0]],                              (3.10)
```

so its eigenvalues are `+-2*k`.  Take `r=s*v` and
`ell=t*u`.  Positive-row cancellation is exactly

```text
<ell+r,x>=sqrt(k/2)*(t+s)=0,
t=-s.                                               (3.11)
```

The completed aggregate scalar and its full quadratic cross term are then

```text
<ell,P_-*K_0*r>=2*k*conj(t)*s=-2*k*abs(s)^2,
2*Re<ell,P_-*K_0*r>=-4*k*abs(s)^2.                  (3.12)
```

The negative row has value `-sqrt(2*k)*s`, so the full pair form is also

```text
2*(abs(<ell+r,x>)^2-abs(<ell+r,y>)^2)
 =-4*k*abs(s)^2.                                    (3.13)
```

Thus all factors and signs agree: after the positive null, the completed
cross aggregate is the entire selected carrier.  Even its minimal real
cancellation `Re<ell,P_-K_0r>=0` is infeasible for nonzero `s`; it would
require `-2*k*abs(s)^2=0`.  Adding arbitrarily many dimensions orthogonal
to `u` changes neither conclusion.

The same conclusion holds if the raw-prime aggregate is used instead of
the fully completed row.  Once the pole and archimedean cross terms are
assumed power-negligible, (3.2) says that the raw-prime row differs from
the target-aligned row (3.6) by only those smaller terms.  Making those
remainders smaller sharpens the alignment; it does not create a transverse
direction.

## 4. One real aggregate equation does not escape the countermodel

The completed quadratic form uses only

```text
2*Re <ell,g>.                                       (4.1)
```

Consequently its cancellation needs just

```text
Re <ell,g>=0,                                       (4.2)
```

not the stronger complex equation `<ell,g>=0`.  This halves the real
condition count but does not restore the useful target quadrature.

Indeed, the selected pair's cross contribution is exactly

```text
Q_(0,cross)(ell,r)
 =-4*Re[<ell,y_0^->*conj(<r,y_0^+>)].               (4.3)
```

After quotienting the positive rows, (3.6) gives

```text
2*Re <ell,g_S>=Q_(0,cross)(ell,r).                  (4.4)
```

Thus the minimal real aggregate equation is literally the equation which
sets the favorable selected two-lobe cross carrier to zero in the one-pair
model.  The unused imaginary quadrature is not a hidden real carrier.

To see the descent issue directly, take an all-real representative of the
model, a real seed `r`, and write `ell=u+i*v`.  Then

```text
Q(ell+r)=Q(u+r)+Q(v).                                (4.5)
```

Condition (4.2) removes the target-aligned cross term from `u+r`; the other
real component `v` contains no seed lobe and hence no two-lobe cross
carrier.  Counting `abs(<ell,a_0>)` without tracking the real quadrature
would therefore be a false complexification.  A valid conditional theorem
must retain negativity of the **total** form, not merely the modulus of a
complex target coordinate after imposing (4.2).

## 5. The quantifier determines whether the hypothesis is equivalent or stronger

Let

```text
S_epsilon := zeta has no zero with
             Re rho>7/8+epsilon.                    (5.1)
```

Let `H_epsilon^act` be the corrected common-witness package in Section 2,
quantified over every **actual zeta zero** violating (5.1).  Then

```text
H_epsilon^act  implies S_epsilon                    (5.2)
```

by Section 2.  Conversely,

```text
S_epsilon implies H_epsilon^act                     (5.3)
```

vacuously, because there is no offending pair over which to test the
universal condition.  Hence, as statements about the actual zeta divisor,

```text
H_epsilon^act iff S_epsilon.                         (5.4)
```

This is a truth-value equivalence caused partly by the quantifier.  It does
not mean that the angle theorem is an analytically useful reformulation:
its hard instance exists only if the desired strip fails, and on that
instance the completed row contains the target itself.

There are two other formulations.

1. If the angle is required nonvacuously for virtual target rows at every
   height, even when zeta has no corresponding zero, it is **stronger**
   than (5.1).  A strip gives no such virtual-row conditioning theorem.
2. If the angle is required uniformly over every artificial zero/operator
   configuration satisfying only the current count, density, and bulk
   moment ledgers, it is also stronger and is **false** by Section 3.

It is therefore misleading to call the augmented target angle a genuinely
weaker intermediate result toward a `7/8` strip.  It is a method-specific
certificate of the strip; under the actual-pair quantifier it is equivalent,
and under useful nonvacuous uniform quantifiers it is stronger.

## 6. Why the current abstract operator ledger permits the hostile block

At the abstract operator-ledger level, the one-pair block can be embedded
sparsely into an on-line moment background.  Formally put all but one
reflected pair on the critical line, use quantiles to retain
Riemann--von Mangoldt discrepancy and the unit-window count, and assign the
single block one pair at fixed depth `alpha<1/2`.  Its off-line density is
zero and every fixed-line horizontal density bound permits the resulting
count ledger.  The selected block does have a normalized asymmetric
Paley--Wiener/Gabor realization: two equal fixed-width packets separated by
`d_*L` compress the exact kernel `(2/L^2)cosh(alpha*(t-s))` to a matrix with
off-diagonal scale `X^(alpha*d_*)/L`.  A Lorentz re-factorization balances
its positive and negative rows, and a binomial cutoff imposes the growing
endpoint jets with superpolynomial error.  What remains unrealized is the
actual positive von Mangoldt aggregate, not the selected zero block; see
[`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md).

At a retained separation `d_*<2/3`, the target block has operator scale at
most

```text
X^(alpha*d_*+o(1)),                                  (6.1)
```

and a fixed-rank Frobenius cost at most

```text
X^(2*alpha*d_*+o(1))=o(T),                           (6.2)
```

because `2*alpha*d_*<2/3`.  It is invisible to the normalized first and
Frobenius moments.  Extra orthogonal on-line rows can supply any required
bulk moment background without changing (3.6).

For the exact block (3.9), take `k=X^(alpha*d_*+o(1))`.  Its trace is zero,
its rank is two, and

```text
||K_0||_F^2=8*k^2=X^(2*alpha*d_*+o(1))=o(T).        (6.3)
```

This verifies the abstract moment embedding with the exact normalization.
Formal sparse insertion changes the count and horizontal-density ledgers by
only `O(1)`.

More abstractly, current bulk inputs constrain counts, traces, and average
squared singular values, not the orientation between `a_0` and `g_S`.
They therefore permit the exact aligned rank-one block (3.6).  This proves
that no theorem using only those inputs can establish the universal
augmented angle.

This construction does **not** satisfy the actual Euler product merely by
declaring its completed operator to equal (3.9).  It refutes a universal
premise based only on the audited abstract ledgers and unconstrained
completed-operator algebra; it is not a counterexample to a statement
restricted to the actual zeta prime row.  For actual zeta, collateral
on-line or off-line rows could in principle give `g_S` a transverse
reservoir.  Showing that they do so at subpower cost is unknown and is
precisely the strip-strength coupled theorem.

## 7. Correct formulation of the conditional card

The logically clean conditional statement is:

> For every actual pair with depth `alpha>3/8+epsilon`, assume that one
> admissible packet simultaneously satisfies the collision-stable signed
> zero inequality and the completed arithmetic lower edge at retained
> separation `d_*<2/3`, with a fixed power margin over the same-lobe scale.
> Then no such pair exists.

This statement is valid but tautologically close to the desired conclusion.
The more informative open problem is not the number of constraints.  It is
to find a zeta-specific identity or positivity principle which forces a
transverse term in (3.6) without already assuming the needed completed lower
edge.  No such principle is currently proved.

Primary local sources:

- [`ZETA23-ASYMMETRIC-TWO-LOBE-HALF-PERIOD-GATE-2026-08-11.md`](ZETA23-ASYMMETRIC-TWO-LOBE-HALF-PERIOD-GATE-2026-08-11.md),
  Section 8, for the conditional exponent ledger;
- [`ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md`](ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md),
  Sections 2--4, for exact scalarization and completed target alignment; and
- [`UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md`](UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md),
  Sections 4--5, for the corrected one-row frontier.
