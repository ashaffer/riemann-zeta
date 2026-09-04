# The augmented aggregate-row `7/8` hypothesis fails on the bulk class

Status: exact quantifiers, an exact finite-dimensional counterblock, a
one-real-constraint audit, a normalized Paley--Wiener/Gabor realization,
and a leading-moment compatibility proof, 2026-08-12.  The counterexample is to the current
**abstract bulk-input implication**, not to a statement known for the actual
zeta zeros or the actual von Mangoldt sequence.  No zero-free strip is
proved or disproved.

## 1. Verdict

The conditional hypothesis behind the proposed `7/8+epsilon` edge is false
on the zero-count, simple-line-density, first/Frobenius-moment, local-count,
and completed-operator class presently stated in the synthesis.

One abstract reflected-pair operator block already supplies a
counterconfiguration.  After its positive row is nulled, the completed
aggregate cross row is the selected negative cross carrier itself.  In an exact two-coordinate mirror block,
the positive-row equation makes even the minimal **one-real-equation**
aggregate cancellation infeasible.  Adding arbitrarily many unused free
coordinates does not help.

At the abstract operator-ledger level, the block can be inserted into the
already constructed on-line moment background.  If its carrier scale is

```text
kappa=X^(alpha*d_*+o(1)),       alpha<1/2, d_*<2/3,  (1.1)
```

then its squared Frobenius cost is

```text
X^(2*alpha*d_*+o(1))=o(T)=o(N).                      (1.2)
```

It changes every stated count by only `O(1)`.  Thus the bulk inputs do not
imply the conditional target theorem, even below the `k=3` cap.

What this does **not** prove is equally important.  Although the selected
pair block now has a normalized asymmetric Paley--Wiener/Gabor realization,
the artificial completed arithmetic block has not been realized as the
cross block of the actual positive von Mangoldt atoms at the actual
prime-power logarithms.  The countermodel therefore closes a bulk-input
inference, not the possibility of a genuinely new actual-prime/actual-zero
theorem.

## 2. Exact quantifiers of the conditional edge

Fix `epsilon>0`.  The numerical `7/8+epsilon` implication chooses fixed
parameters

```text
1/2<a<d_*<2/3,
alpha>=3/8+epsilon,
alpha*d_*>a/2+c_epsilon                              (2.1)
```

after decreasing `epsilon` by a harmless constant if needed.  The seed
width `b=b_T` tends to zero under the endpoint conditions in the asymmetric
audit.  Put

```text
K_T=X^(alpha*d_*).                                   (2.2)
```

For a deepest hypothetical pair in the core, let

```text
E_-                    allowed free-lobe space,
r in E_+               normalized seed,
A_T:E_- -> C^p         off-line positive-row map,
b_T=-A_+*r             matched positive-row datum,
g_T in E_-             raw-prime aggregate Riesz row,
a_T in E_-             selected negative-row restriction,
c_T                    selected seed target value.   (2.3)
```

The complex-row version of the missing assertion is the following uniform
statement.  For all sufficiently large `T`, for every actual-zeta
configuration containing such a distinguished pair, there are `r,ell` with

```text
A_T*ell=b_T,
<ell,g_T>=0,
||ell||+||r||<=X^o(1),
abs(c_T+<ell,a_T>)^2>=K_T*X^(-o(1)),                 (2.4)
```

and all same-lobe, on-line, pole, archimedean, collar, and remote terms are
`o(K_T*X^(-o(1)))`.  Exact pole nulls may be appended as finitely many rows.

The minimal scalar version replaces the second line of (2.4) by

```text
Re <ell,g_T>=0.                                     (2.5)
```

A form with `o(K_T)` rather than exact cancellation is equivalent for the
counterexample below.  Conditions (2.4)--(2.5) must be uniform in the target
ordinate, every permitted near-collision geometry, and the actual seed
choice.  An existence statement for one favorable artificial zero set is
not enough for a strip; conversely, one legal abstract configuration is
enough to refute derivation from the abstract bulk inputs.

## 3. Exact two-coordinate completed counterblock

Let

```text
H_-=C*u direct_sum W_-,       H_+=C*v direct_sum W_+,
```

where `u,v` are orthonormal and `W_-,W_+` have arbitrary dimensions.  For a
positive number `k`, define the selected reflected-pair rows

```text
x=sqrt(k/2)*(u+v),
y=sqrt(k/2)*(u-v).                                  (3.1)
```

The exact hyperbolic pair operator is

```text
K_pair=2*(x*x^*-y*y^*)
      =2*k*(u*v^*+v*u^*).                           (3.2)
```

It is purely off-diagonal, has eigenvalues `+-2*k`, trace zero, and squared
Frobenius norm `8*k^2`.

Fix any seed

```text
r=s*v+r_0,          r_0 in W_+.                     (3.3)
```

Write `ell=t*u+ell_0`, `ell_0 in W_-`.  Only `s,t` participate in the
selected carrier.  Nulling the positive row of the full packet `ell+r`
forces

```text
t=-s.                                               (3.4)
```

The completed aggregate cross vector and cross form are

```text
g_pair=P_-*K_pair*r=2*k*s*u,

<ell,g_pair>=2*k*conj(t)*s=-2*k*abs(s)^2,
2*Re <ell,g_pair>=-4*k*abs(s)^2.                    (3.5)
```

Thus, for `s!=0`, (3.4) is incompatible with even

```text
Re <ell,g_pair>=0.                                  (3.6)
```

The phase of `s` does not matter.  Taking `s=0` makes (3.6) possible but
deletes the selected carrier.  Directions in `W_-` do not enter (3.4) or
(3.5), so an arbitrarily large dimension surplus gives no reservoir.

On the positive-null packet, the selected pair has the exact value

```text
<ell+r,K_pair*(ell+r)>=-4*k*abs(s)^2.                (3.7)
```

Taking `k=X^(alpha*d_*+o(1))` and
`abs(s)=X^(-o(1))` gives precisely the required carrier exponent.  Equations
(3.4)--(3.6) prove that the real and complex versions of the augmented
hypothesis both fail.

### Robust form

Suppose the raw-prime aggregate differs from the completed row in (3.5) by
a remainder `e_T` whose action on all subpower-norm packets is `X^o(1)`, as
in the additive-edge pole/archimedean and on-line bounds.  Then every packet
obeying (3.4), `abs(s)>=X^(-o(1))`, and
`||ell||+||r||<=X^o(1)` satisfies

```text
2*Re <ell,g_raw>
 =-4*k*abs(s)^2+X^o(1)
 =-X^(alpha*d_*-o(1)).                              (3.8)
```

It cannot be zero or `o(K_T*X^(-o(1)))`.  If the remainder has a nonzero
projection into `W_-`, exact cancellation costs at least
`X^(alpha*d_*-o(1))` in coefficient norm.  Hence the obstruction is stable
under every subpower completed perturbation used in the conditional ledger.

## 4. General projected-row identity

The alignment is not peculiar to the symmetric coordinates in (3.1).  Let
one reflected pair have arbitrary lobe restrictions

```text
x=x_-+x_+,
y=y_-+y_+,
K_pair=2*(x*x^*-y*y^*).                             (4.1)
```

Fix `r in E_+`, let

```text
A*ell=<ell,x_->,       b=-<r,x_+>,
S=ker A,
a=y_-,
g=P_-*K_pair*r.                                     (4.2)
```

Then exactly

```text
g=2*x_-*conj(<r,x_+>)-2*y_-*conj(<r,y_+>),

P_S*g=-2*conj(<r,y_+>)*P_S*a.                       (4.3)
```

If the seed sees the selected negative row and `P_S*a!=0`, (4.3) gives

```text
P_(S intersect g^perp)*a=0.                         (4.4)
```

Thus the complex augmented homogeneous leverage vanishes exactly in the
one-pair quotient.  If a background contributes an error `e` after
projection, then

```text
dist(P_S*a,span(P_S*g))
 <=norm(e)/(2*abs(<r,y_+>)).                         (4.5)
```

When the selected cross product has scale `K_T` and the on-line/completion
error is `X^o(1)`, (4.5) is a fixed-power loss from the original leverage.

Equation (4.3) is just the off-diagonal form of the explicit-formula
identity.  Proving that the actual aggregate row instead has a large
target-neutral component would require information absent from all the
listed bulk moments.

## 5. The one-real-row nuance

Complex orthogonality and real scalar cancellation are not interchangeable.
For a complex Hilbert space `S`, define the real hyperplane

```text
S_(g,R)={h in S: Re <h,g>=0}.                        (5.1)
```

For every target `a_S=P_S*a`, phase rotation gives the exact identity

```text
sup_(h in S_(g,R), ||h||=1) abs(<h,a_S>)=||a_S||.   (5.2)
```

Indeed choose `h=e^(i*theta)*a_S/||a_S||` and choose `theta` so that the
real part of `<h,g>` vanishes.  Therefore one real **homogeneous** equation
alone never decreases a modulus-valued target leverage.  Formula (4.4)
must not be quoted for (2.5).

The relevant system is affine.  Let `ell_0=A^dagger b`, `S=ker A`, and
`g_S=P_S*g`.  The real aggregate equation has minimum correction norm

```text
abs(Re <ell_0,g>)/norm(g_S),                         (5.3)
```

with the convention that it is infeasible when `g_S=0` and the numerator is
nonzero.  In the mirror block (3.1),

```text
g_S=0,             Re <ell_0,g>=-2*k*abs(s)^2,       (5.4)
```

so infeasibility is exact.  This is why the phase direction in (5.2) does
not rescue the proposed witness.

There is an equivalent carrier statement.  The desired `X^(alpha*d_*)`
gain is the real cross quadrature.  Cancelling that quadrature leaves at most
the same-lobe pair scale `X^(alpha*a+o(1))`.  The power gate in (2.1) and
`alpha<1/2` imply

```text
d_*>a/(2*alpha)>a,                                  (5.5)
```

so the loss is the fixed power

```text
X^(alpha*(d_*-a)-o(1)).                             (5.6)
```

In the pure block (3.2), even that same-lobe remainder is exactly zero.

## 6. Paley--Wiener realization and bulk compatibility

The sign pattern in (3.1) is the carrier-scale part of a normalized
two-packet Paley--Wiener compression.  Take equal real-even packets of fixed
width in the asymmetric lobes, with centers separated by `D=d_*L`.  In the
repository's isolated-pair normalization their exact Hermitian kernel is

```text
(2/L^2)*cosh(alpha*(t-s)),                           (6.1)
```

and their compressed matrix is

```text
m_L*[[1,cosh(alpha*D)],
     [cosh(alpha*D),1]],       m_L=2*A_alpha^2/L.    (6.2)
```

Thus its pure cross part is (3.2) with the exact parameter

```text
k=(A_alpha^2/L)*cosh(alpha*d_*L)
  =X^(alpha*d_*-o(1)).                              (6.3)
```

The remaining diagonal `m_L*I` is smaller by the fixed power
`X^(-alpha*d_*+o(1))`.  The unequal raw Laplace rows caused by the asymmetric
midpoint are an exact Lorentz boost.  A `J`-unitary inverse boost, or simply
the spectral factorization of (6.2), gives the positive and negative rows
`u+v` and `u-v`; positive-row nulling is therefore exactly (3.4) at carrier
scale, not a hidden fixed-power normalization cost.

A common binomial endpoint cutoff, with a fixed fraction of the Fourier
aperture reserved for it, imposes the full growing endpoint-jet system
exactly.  The seed condition `b^2*L/eta->infinity` makes this cutoff equal to
one on both packets up to a superpolynomial error.  Smooth Fourier truncation
then transfers (6.2) to the finite Gabor grid with error
`o(X^(alpha*d_*)/L)`.  The complete factor and endpoint audit is in
[`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md).

Now start with the on-line artificial background in Proposition 6.1 of the
single-core-pair audit.  It has Riemann--von Mangoldt discrepancy `O(1)`,
unit count `O(L)`, and

```text
tr H=N+o(N),             tr(H^2)=(4/3)*N+o(N).       (6.6)
```

At the abstract operator-ledger level, replace two on-line points by this
rank-two compression and assign it one reflected-pair count in the dyadic
core.  This changes:

```text
total and local counts                 O(1),
simple-on-line proportion              O(1/N),
horizontal zero-density counts         O(1),
pair trace                             O(k),
pair squared Frobenius contribution    O(k^2).       (6.4)
```

The pure block has trace zero; an `O(1)` normalization correction can be
absorbed in the background.  Since

```text
2*alpha*d_*<2*(1/2)*(2/3)=2/3,                      (6.5)
```

and `X=T^(1+o(1))`, (1.2) follows.  The cross term with the bounded on-line
background is also `o(N)`.  Hence (6.6) and every listed bulk/count condition
survive.  A collar is unnecessary because the pair is in the core; adding
the standard `o(N)` collar and endpoint jets does not change this conclusion.

Finally define the artificial completed arithmetic operator to equal this
zero-side operator.  This retains the exact completion identity, every
orientation, and conjugation.  The remaining scope boundary is arithmetic:
the resulting aggregate row was not realized as a sum of the actual positive
weights `Lambda(n)/sqrt(n)` at actual prime-power logarithms.

## 7. Exact scope and corrected frontier

The theorem proved here is:

> No uniform augmented-row carrier theorem of the form (2.4) or (2.5), at
> any fixed separation `d_*<2/3`, follows from the currently stated
> Riemann--von Mangoldt count, unit count, simple-line density, first and
> Frobenius moments, endpoint codimension, and abstract completed-operator
> identity.  The failure already occurs for one off-line pair and persists
> with fixed-power margin under subpower background perturbations.

This falsifies the description of `7/8+epsilon` as “countermodel-safe” on
the current abstract **operator-ledger** class, including its normalized
Paley--Wiener/Gabor selected-pair realization.  It does not falsify a theorem
restricted to the actual zeta zeros and actual von Mangoldt row.  It remains
an algebraically correct
**actual-zeta conditional implication** only if its hypotheses explicitly
include the augmented target angle/affine feasibility which the counterblock
violates.  In that form the implication is tautologically valid but its main
hypothesis is not supported by the bulk data.

With the quantifier over actual offending zeta pairs, that full conditional
package is truth-value equivalent to the `7/8+epsilon` strip: it excludes
each offending pair, while the strip makes the universal package vacuous.
A nonvacuous virtual-row or abstract-operator formulation is stronger than
the strip.

The surviving actual-zeta question is narrower and more arithmetic:

```text
Does the actual von-Mangoldt aggregate row, after the actual positive-zero
constraints, possess a target-neutral component of carrier size which is
forbidden in the abstract completed one-pair block?                    (7.1)
```

Answering (7.1) requires a coefficient-specific relation between actual
prime-power logarithms and the actual collateral zero rows.  Neither a
dimension count, a Wiener extremal for pointwise nulls, nor the current
bulk moments provides it.  No lower bound beyond the exact real-hyperplane
identity (5.2) is presently proved for the actual affine system.

Local sources used for the embedding and realization are
[`ZETA23-MULTIBLOCK-UNCERTAINTY-CROSS-TERM-GATE-2026-08-11.md`](ZETA23-MULTIBLOCK-UNCERTAINTY-CROSS-TERM-GATE-2026-08-11.md),
Section 2.3, and
[`ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md`](ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md),
Proposition 6.1.  The complementary quantifier audit is
[`ZETA23-CONDITIONAL-SEVEN-EIGHTHS-LOGIC-AUDIT-2026-08-12.md`](ZETA23-CONDITIONAL-SEVEN-EIGHTHS-LOGIC-AUDIT-2026-08-12.md).
