# R169 two-unit decomposition and product-amplifier gate

## Status

The collective product amplifier has an exact function-theoretic
normal form.  For two channels put

```text
P=1-(F_1-1)(F_2-1).                                      (0.1)
```

Requiring `F_1`, `F_2`, and `P` to have exactly the same fixed divisor
does not create a hidden algebraic obstruction.  It is equivalent to one
specific additive factorization problem:

```text
1+G=R_1+R_2,                                             (0.2)
```

where `G` has the fixed divisor and `R_1,R_2` are holomorphic units.  The
right-cap normalization is exactly

```text
G -> 1,               R_1 -> 1,               R_2 -> 1. (0.3)
```

Given (0.2), the channels and output are

```text
P  =G/(R_1R_2),
F_1=G/R_2,
F_2=G/R_1.                                               (0.4)
```

Conversely, every successful pair in (0.1) arises this way.  Thus the
nonlinear cofactor question is neither a scalar omitted-value problem nor
a generic vector-hyperbolicity problem.  It is a **cap-normalized two-unit
decomposition** problem for `1+G`.

At a fixed cutoff on a relatively compact bridge, decomposing a bounded
holomorphic function into two units is easy if cap normalization is
discarded: a constant outside its range works.  Along a deleted-head
sequence, however, both units must converge to `1` on the same fixed
interior cap.  That is the hard quantifier.  The scalar Blaschke formula

```text
F=2(1-exp[-(log 2)B])                                    (0.5)
```

does give a bounded, exact-divisor function omitting `2` at one fixed
stage, but it cannot converge to `1` on a fixed interior cap while retaining
the fixed divisor.  R155's logarithmic-lattice theorem rules that out.

There is also a quantitative necessity.  If the cap error is `epsilon`,
then at least one unit ratio in any successful product construction has a
logarithm of size

```text
>> epsilon^(-alpha)                                      (0.6)
```

on a fixed larger bridge, where `alpha>0` depends only on the localization
geometry.  For `epsilon=H^(-A)`, this is a fixed power of `H`.  Consequently
normal-family arguments force a real outer-growth bill, but do **not** by
themselves exceed the polynomial budget available to the optional-prime
construction.

```text
exact product-amplifier/two-unit equivalence               THEOREM
fixed-stage divisor-adaptive construction                  AVAILABLE
fixed-cap scalar Blaschke sequence                         IMPOSSIBLE
vector complement hyperbolicity                            FALSE
quantitative propagation/outer-growth tax                 THEOREM
cap-normalized two-unit decomposition with power control   OPEN
fixed uniform zeta zero-free strip                         NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md),
[`R160-FINITE-COLLECTIVE-CUTOFF-STOKES-HURWITZ-GATE.md`](R160-FINITE-COLLECTIVE-CUTOFF-STOKES-HURWITZ-GATE.md),
and
[`R162-BOUNDED-CAUSAL-LAPLACE-CONTROLLABILITY.md`](R162-BOUNDED-CAUSAL-LAPLACE-CONTROLLABILITY.md).

## 1. Admissible divisor class

Let `Omega` be a simply connected domain and let `V` be a nonempty open
subset of `Omega`, the fixed right cap.  Fix a nonzero holomorphic function
`Z` on `Omega`.  Its zero divisor, including multiplicities, is denoted by
`D`.

A holomorphic function `F` is in the exact divisor class of `Z` when

```text
F=Z A,                    A in O(Omega)^x,                (1.1)
```

where `O(Omega)^x` denotes the nowhere-zero holomorphic functions.  Because
`Omega` is simply connected, every such multiplier is an exponential.

For a sequence indexed by `nu`, call `F_nu` head normalized if

```text
F_nu -> 1 locally uniformly on V.                         (1.2)
```

The phrase "fixed cap" in (1.2) is essential.  Spatial convergence as
`Re(s)->infinity` for one fixed function is not a substitute for (1.2).

## 2. Exact two-unit equivalence

### Theorem 2.1 -- product amplifier normal form

For every index `nu`, the following data are equivalent.

1. Functions `P,F_1,F_2` in the exact divisor class of `Z` satisfying

   ```text
   P=1-(F_1-1)(F_2-1).                                   (2.1)
   ```

2. A function `G` in the exact divisor class of `Z` and units `R_1,R_2`
   satisfying

   ```text
   1+G=R_1+R_2.                                          (2.2)
   ```

The correspondence from 2 to 1 is (0.4).  The inverse correspondence is

```text
R_j=F_j/P,
G=P R_1R_2=F_1F_2/P.                                    (2.3)
```

Moreover, head normalization of `G,R_1,R_2` as in (0.3) is equivalent to
head normalization of `P,F_1,F_2`.

#### Proof

Assume (2.2) and define (0.4).  Division by a unit preserves the exact
divisor, so `P,F_1,F_2` all have divisor `D`.  Also

```text
F_1-1=(G-R_2)/R_2=(R_1-1)/R_2,
F_2-1=(G-R_1)/R_1=(R_2-1)/R_1.                           (2.4)
```

It follows that

```text
1-(F_1-1)(F_2-1)
 =[R_1R_2-(R_1-1)(R_2-1)]/(R_1R_2)
 =(R_1+R_2-1)/(R_1R_2)
 =G/(R_1R_2)=P.                                          (2.5)
```

Conversely, exact equality of the divisors makes each quotient `F_j/P` a
unit; removable singularities at the points of `D` are filled by the ratio
of the first nonzero local coefficients.  Substitute `F_j=P R_j` into
(2.1).  After expansion and division by `P`,

```text
1=R_1+R_2-P R_1R_2.                                     (2.6)
```

Thus `G=P R_1R_2` satisfies (2.2) and is `P` times a unit.  Equations
(2.3) and (0.4) are inverse to one another.  The cap assertions follow
directly from these formulas.  QED.

### Corollary 2.2 -- exact zero-free cofactor

Writing `G=Z A`, the output in (0.4) is

```text
P=Z C,                 C=A/(R_1R_2) in O(Omega)^x.        (2.7)
```

Thus a successful two-unit decomposition produces a cofactor which is
zero-free identically, not merely on a selected contour.

### Remark 2.3 -- arbitrary positive weights

For

```text
P=1-sum_j w_j(F_j-1)^2,             w_j>0, sum_jw_j=1,   (2.8)
```

put `R_j=F_j/P`.  Exact divisor equality gives the related identity

```text
1=2 sum_j w_jR_j-P sum_j w_jR_j^2,                       (2.9)
```

and hence

```text
P=[2 sum_jw_jR_j-1]/[sum_jw_jR_j^2].                     (2.10)
```

At a target zero,

```text
sum_jw_jR_j(rho)=1/2,                                    (2.11)

```

whereas on the cap every `R_j` tends to `1`.  Positivity does not make the
denominator in (2.10) coercive: it is a sum of complex squares, not a sum of
modulus squares.

## 3. Why ordinary hyperbolicity does not close the gate

For two product channels, ratio coordinates identify the nonzero part of
the solution space with

```text
X={(R_1,R_2) in (C^x)^2:R_1+R_2!=1}.                     (3.1)
```

This complement is not Brody hyperbolic.  For example,

```text
R_1(z)=exp(z),                 R_2(z)=1                  (3.2)
```

defines a nonconstant entire curve in `X`, since
`R_1+R_2-1=exp(z)` never vanishes.  A vector Montel theorem based only on
omitted coordinate and cofactor divisors therefore cannot work.

The fixed target and fixed-cap data remain important.  At a zero `rho` of
`P`, (2.6) gives

```text
R_1(rho)+R_2(rho)=1,                                     (3.3)

```

while cap normalization gives `R_1,R_2->1`.  Any successful sequence must
therefore become nonnormal in its unit ratios.  Section 4 quantifies that
statement.

## 4. Propagation lower bound for the unit ratios

Fix compact sets

```text
K_0 subset V,       rho in K subset interior(K') subset K' compactly in Omega,
                                                               (4.1)
```

where `K_0` has nonempty interior and a finite chain of overlapping discs
inside `K'` joins `K_0` to `rho`.

The standard three-circles propagation argument supplies constants

```text
theta in (0,1),       C_0>=1                              (4.2)
```

depending only on this fixed geometry such that every `g in Hol(Omega)`
satisfies

```text
|g(rho)|
 <=C_0 [sup_(K_0)|g|]^theta [max(1,sup_K|g|)]^(1-theta).
                                                               (4.3)
```

One obtains (4.3) by applying Hadamard's three-circles theorem on the first
disc and then iterating across the finite overlapping chain.  No arithmetic
parameter enters `theta` or `C_0`.

### Theorem 4.1 -- fixed-power nonnormality tax

Assume the data of Theorem 2.1 and suppose, on `K_0`,

```text
max(|P-1|,|F_1-1|,|F_2-1|)<=epsilon,       0<epsilon<1/4.
                                                               (4.4)
```

Choose logarithms

```text
R_j=exp(g_j)                                             (4.5)
```

with the branches for which `g_j=O(epsilon)` on `K_0`.  There are constants
`c>0` and

```text
alpha=theta/(1-theta)>0                                  (4.6)
```

depending only on the fixed geometry such that

```text
max_j sup_K|g_j| >= c epsilon^(-alpha).                   (4.7)
```

#### Proof

Equation (4.4) and `R_j=F_j/P` give

```text
sup_(K_0)|R_j-1|<=4epsilon.                               (4.8)
```

For small fixed `epsilon`, the logarithm branch near `1` therefore obeys

```text
sup_(K_0)|g_j|<=C_1epsilon.                               (4.9)
```

At `rho`, (3.3) holds.  If both `|g_j(rho)|<1/4`, then

```text
|R_1(rho)+R_2(rho)-2|
 <=2(exp(1/4)-1)<1,                                      (4.10)
```

contradicting (3.3).  Hence one `|g_j(rho)|>=1/4`.  Apply
(4.3) and (4.9) to that logarithm and rearrange.  QED.

### Corollary 4.2 -- symmetric outer size

After enlarging `K` slightly inside `K'`, Borel--Caratheodory applied along
the same finite disc chain converts (4.7) into

```text
max_j sup_(K') |Re g_j| >= c' epsilon^(-alpha).           (4.11)
```

Equivalently, at least one of `R_j` and `1/R_j` has logarithmic outer size
`>>epsilon^(-alpha)` on the larger bridge.  A boundary-integral version
follows by applying the Poisson formula to `Re g_j` on a smooth intermediate
domain.  Thus a symmetric characteristic which charges both a unit and its
inverse has the same lower bound.

If `epsilon=H^(-A)`, then

```text
max_j characteristic^+-(R_j) >> H^(A alpha).             (4.12)
```

This is a fixed-power cost.  It proves that a successful collective channel
cannot be normal, but it does not conflict formally with a prime-control
horizon `Y=H^kappa` or another polynomial ledger.  A no-go theorem needs a
sharper comparison of `A alpha` with the nonlinear support gain; normality
alone is insufficient.

The same proof applied to (2.9) gives a corresponding bound for positive
weighted quadratic sums.  Indeed, (2.11) is a fixed distance from the cap
value `sum w_jR_j=1`.

## 5. The scalar avoidance formulation

Fix `G` and put

```text
W=1+G.                                                    (5.1)
```

Choosing the first unit as `R_1=exp(h)` makes the second unit

```text
R_2=W-exp(h).                                             (5.2)
```

Thus (0.2) is equivalent to finding `h in Hol(Omega)` such that

```text
W(s)-exp(h(s))!=0                       for every s,       (5.3)
exp(h)->1,        W-exp(h)->1           on the fixed cap. (5.4)
```

This is a moving-graph avoidance problem.  Where `W` is nonzero, it can be
written locally as

```text
h(s)-Log W(s) notin 2 pi i Z.                            (5.5)
```

At a zero of `W`, (5.3) is automatic, but the global logarithmic sheets in
(5.5) carry the zero-count bill.

If `W=R_1+R_2`, set `k=Log(R_1/R_2)`.  Then

```text
W=R_2[1+exp(k)].                                         (5.6)
```

Consequently every zero of `W`, with its multiplicity, is a point at which

```text
k in (2 Z+1) pi i.                                       (5.7)
```

This explains the exact relation to R155.  If the number of zeros of `W`
were bounded while the units converged to `1` on the cap, two fixed lattice
values would eventually be omitted and Montel would close the construction.
For the present application `W=1+G` may have a polynomially growing
mixed-point cloud.  Those zeros provide the lattice sheets required for a
nonnormal decomposition, so R155 does not by itself decide (5.3).

## 6. Relation to stable rank and corona statements

Equation (0.2) resembles a stable-rank or corona problem, but the usual
statements are not the required theorem.

1. A corona theorem begins with a quantitative lower bound for a tuple and
   solves a Bezout equation.  Here the problem is to choose the two summands
   themselves, require each to be a unit, and prescribe their common cap
   asymptotics.
2. Bass stable rank one, when available for a chosen holomorphic function
   algebra, reduces a unimodular pair by adding a multiple of one component
   to the other.  It does not automatically represent a prescribed `W` as
   the sum of two units with `R_1,R_2->1`.
3. In a bounded-function algebra, invertibility also demands a uniform lower
   bound.  The optional-prime application presently asks only for
   zero-freeness plus an explicit power ledger; these are different
   quantitative categories.

At one fixed stage on a relatively compact bridge, choose a constant `M`
outside the compact range of `W`.  Then

```text
W=M+(W-M)                                                  (6.1)
```

is a two-unit decomposition.  It is useless asymptotically because its
summands approach `M` and `2-M`, not `1` and `1`, on the cap.  Any appeal to
stable rank or corona theory must therefore include the interpolation
condition (5.4) and quantitative control compatible with (4.12).

## 7. The finite-stage Blaschke model and its quantifier defect

Let `B` be a finite Blaschke product on a simply connected bridge, with the
same zero divisor as `Z`, normalized at a right boundary prime end.  Then

```text
F=2(1-exp[-(log 2)B])                                    (7.1)
```

has exactly the zeros of `B`: since `|B|<1`, the equation `F=0` forces
`(log 2)B in 2 pi i Z`, hence `B=0`.  Also

```text
2-F=2 exp[-(log 2)B]                                     (7.2)
```

is zero-free.  Therefore the scalar quadratic cofactor

```text
[1-(F-1)^2]/Z=F(2-F)/Z                                  (7.3)
```

is zero-free at that fixed stage.

This is a useful exact target, but not a deleted-head sequence.  A bounded
family `B_nu` which tends to `1` on a fixed interior open cap would be normal;
the identity theorem would force the limit to be `1` throughout, in
conflict with its retained zero.  Allowing a nonnormal family returns the
power bill in Section 4 and the lattice proliferation in Section 5.

### 7.1 Fixed affine splittings are closed

The simplest cap-normalized splitting of `1+G` is

```text
R_1=1+b(G-1),
R_2=b+(1-b)G.                                             (7.4)
```

Both summands equal `1` when `G=1`.  For fixed
`b notin {0,1}`, zero-freeness requires `G` to omit

```text
a_b=(b-1)/b,                    c_b=b/(b-1),
a_b c_b=1.                                               (7.5)
```

Except at `b=1/2`, these are two distinct fixed values, so R155's
two-value theorem excludes a cofinal head-normalized sequence.  At
`b=1/2`, both units are `(1+G)/2`; the required omission of `-1` is closed
by R155's one-value logarithmic-lattice theorem when the zero divisor of
`G` stays fixed.

Thus a fixed affine splitting is not the missing construction.  An
`H`-dependent affine parameter can evade this statement only through a
singular limit `b->0,1,infinity` or through coalescence at `b=1/2`.  These
are nonnormal, ill-conditioned regimes rather than a cost-free corona
argument.

## 8. General even `q` and the growing-channel audit

Let `q>=2` be even and put

```text
P=1-product_(j=1)^q(F_j-1).                              (8.1)
```

Assume `P,F_1,...,F_q` all have exactly divisor `D`, and define the unit
ratios

```text
R_j=F_j/P.                                                (8.2)
```

Write `e_k(R)` for the elementary symmetric polynomial of degree `k` in
the `R_j`.

### Theorem 8.1 -- general unit-coordinate normal form

Equation (8.1) is equivalent to

```text
1=e_1(R)-P e_2(R)+P^2 e_3(R)-...+(-1)^(q+1)P^(q-1)e_q(R).
                                                               (8.3)
```

At every target zero `rho`,

```text
sum_(j=1)^q R_j(rho)=1,                                  (8.4)
```

whereas head normalization gives `R_j->1` on the cap.

#### Proof

Since `q` is even,

```text
product_j(F_j-1)=product_j(1-P R_j).                     (8.5)
```

Expand the right side in elementary symmetric polynomials, insert it in
(8.1), and divide by `P`.  Evaluation at `P=0` gives (8.4).  QED.

There is a useful additive shadow of (8.3).  Put

```text
G=e_1(R)-1.                                               (8.6)
```

Then

```text
G=P D_q(P,R),
D_q=sum_(k=2)^q (-1)^k P^(k-2)e_k(R).                    (8.7)
```

For `q=2`, `D_2=R_1R_2` is automatically a unit and (8.7) is exactly the
two-unit theorem.  For `q>=3`, `D_q` can vanish.  This is the precise new
freedom: the sum `e_1(R)-1` may acquire extra zeros which are absorbed by
the higher symmetric layers without becoming zeros of `P`.  Hence growing
`q` is not formally reducible to the two-unit gate.

Conversely, units `R_j` give a product construction exactly when the
degree-`q-1` equation (8.3) has a single-valued holomorphic branch `P` with
the prescribed divisor and cap germ.  Locally this is transparent:

- near the cap, `R_j=1+o(1)` selects the branch `P=1+o(1)`;
- near a target, (8.4) and `e_2(R)(rho)!=0` give

  ```text
  P=[e_1(R)-1]/e_2(R)+O([e_1(R)-1]^2).                   (8.8)
  ```

The global obstruction is therefore algebraic branch/discriminant
avoidance together with the exact divisor, not a local implicit-function
problem.

### Theorem 8.2 -- growing-`q` propagation ledger

Use the fixed geometry and exponent `theta` from Section 4, and put

```text
p=1/(1-theta),                 alpha=p-1.                 (8.9)
```

Suppose on `K_0`

```text
max_j|F_j-1|<=epsilon,             |P-1|<=epsilon,
0<epsilon<1/4.                                            (8.10)
```

Choose `R_j=exp(g_j)` with `g_j=O(epsilon)` on `K_0`, and let

```text
M_j=max(1,sup_K|g_j|).                                   (8.11)
```

Then, for all sufficiently large even `q`,

```text
sum_(j=1)^q M_j
 >=c epsilon^(-alpha)(log q)^p.                          (8.12)
```

#### Proof

At `rho`, equation (8.4) implies

```text
q-1
 =|sum_j[exp(g_j(rho))-1]|
 <=sum_j[exp(|g_j(rho)|)-1].                             (8.13)
```

Let `a_j=|g_j(rho)|` and `A=(sum_j a_j^p)^(1/p)`.  Since
`a_j<=A` and `sum_j a_j<=q^(1-1/p)A`,

```text
q-1<=exp(A) q^(1-1/p)A.                                  (8.14)
```

It follows that `A>=c_p log q`; hence

```text
sum_j a_j^p>=c_p(log q)^p.                               (8.15)
```

The propagation estimate (4.3), applied to each `g_j`, gives

```text
a_j^p<=C epsilon^(alpha) M_j.                             (8.16)
```

Sum (8.16) and use (8.15).  QED.

Thus extra channels cannot distribute the nonnormality cost to zero.  They
increase its lower bound only by a power of `log q`, however.  If
`epsilon=H^(-A)` and `q asymp c log H`, (8.12) is only

```text
H^(A alpha)(log log H)^(1+alpha).                         (8.17)
```

Normality therefore still does not rule out a fixed-power optional-prime
ledger.

### 8.3 Support and algebra ledger

If every `F_j-1` has Dirichlet support above `H`, then

```text
product_j(F_j-1) has support above H^q.                   (8.18)
```

Writing `F_j=Z a_j` gives the exact cofactor

```text
P=Z C,
C=sum_(k=1)^q(-1)^(k+1)Z^(k-1)e_k(a_1,...,a_q).          (8.19)
```

There are `2^q-1` subset monomials in (8.19), but their logarithmic
triangle-inequality ledger is linear in `q`:

```text
log product_j(1+|Za_j|)=sum_j log(1+|Za_j|).              (8.20)
```

For

```text
q asymp c log H,                                         (8.21)
```

the raw expansion size `2^q=H^(c log 2)` is only a fixed power, while the
support threshold is

```text
H^q=exp[c(log H)^2].                                     (8.22)
```

This is a genuine formal escape from every fixed-`q` normal-family gate.
It is not yet a construction: one must still keep the algebraic branch in
(8.3), the discriminant, and the cofactor (8.19) zero-free, while realizing
all `q` units with the actual signed-prime coefficient budget.  A binary
tree of two-unit gates is a sufficient construction but pays a new
propagation bill at every level; the direct `q`-coordinate equation (8.3)
does not automatically pay that stronger tree cost.

## 9. Decision and next lemma

The abstract assumptions

```text
same divisor + cap normalization + positive weights       (9.1)
```

do not yield a pointwise sign, a hyperbolic target
complement, or a bounded-normal-family contradiction for a collective
product.  What they do yield is the exact reduction (0.2), the general
unit-coordinate equation (8.3), and the mandatory fixed-power nonnormality
taxes (4.12) and (8.12).

The next useful theorem must decide the following quantitative statement.

> **Cap-normalized two-unit problem.**  For an actual coefficient-controlled
> exact-divisor channel `G_H`, can one write
>
> ```text
> 1+G_H=R_(1,H)+R_(2,H)
> ```
>
> with both units tending to `1` on the fixed right cap and with the
> symmetric characteristics of the units bounded by the fixed power allowed
> by the optional-prime horizon?

A positive answer, inserted into (0.4), gives an exactly zero-free
collective cofactor.  A negative answer must be quantitative: it must show
that every such decomposition costs more than the nonlinear gain.  Merely
showing that the units are nonnormal recovers (4.12) and is not enough.
