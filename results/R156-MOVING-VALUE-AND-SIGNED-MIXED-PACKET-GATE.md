# R156 moving-value and signed mixed-packet gate

## Status

R155 proves that fixed artificial values cannot be selected away.  This
report tests the two remaining scalar loopholes:

1. move the artificial values with the head, toward `1` or infinity; or
2. keep the forced mixed points and try to recover the target from their
   common residue sign, winding, or logarithmic monodromy.

Both fail at the level of general analytic information available in the
current program.

For a Pareto-minimal positive rational response, nodes which collapse toward
`1` lose one Euler-support power each.  A node which escapes to infinity and
is omitted from the target domain must grow at least like a fixed negative
power of the head error.  Exactly the same power appears in the residue at
every denominator pole.  Combining the optimistic Euler and outer-divisor
budgets cancels the number of moving nodes and leaves an impossible geometric
inequality.

Independently, there is a finite polynomial countermodel at the exact
`O(H)` divisor scale.  It has one fixed target zero, no poles, power-small
right-cap error, and sub-`H` outer characteristic, yet its forced `F=2`
points cancel the target reciprocal powers exponentially well throughout a
linearly long block of useful orders.  Thus holomorphy, bounded target-zero
divisor, favorable residues, winding, and coarse conductor growth do not
imply the signed estimate.

```text
moving finite artificial values                            CLOSED
collapsed values near F=1                                  LOSE EULER POWERS
values escaping to infinity                                REPAY IN POLE RESIDUE
absolute moving-node Cauchy closure                        IMPOSSIBLE
two-simple-value H^q response                              EXACT
support gain of that response                              EXACT BOUNDARY GERM
same-sign/local-winding reciprocal-power lower bound       FALSE
universal-cover scalar monodromy escape                    CLOSED
coefficient-specific arithmetic mixed-divisor estimate     OPEN
fixed uniform zeta zero-free strip                         NOT PROVED
zeros approaching one                                      NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md`](R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md),
[`R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md`](R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md),
and
[`R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md).

## 1. The minimal moving-node response

Write

```text
F=1+U,
M=q-1,                                                     (1.1)
```

and take `q` even.  Among rational differentials with

* residue `+1` at `F=0`, or `U=-1`;
* a zero of order `M` at `U=0`; and
* only simple finite value poles and logarithmic behavior at infinity,

the Pareto-minimal form has `M` artificial nodes.  For distinct positive
nodes `t_1,...,t_M`, it is

```text
Q_t(U)=C_0 U^M/
       [(1+U) product_(j=1)^M(1-U/t_j)],

A_t(s)=-U'(s)Q_t(U(s)),

C_0=product_j(1+1/t_j).                                    (1.2)
```

The sign in (1.2) uses that `M` is odd.  Its target residue is `+1`.  At an
`F`-pole of multiplicity `m`,

```text
Res A_t=-m C_infinity,
C_infinity=product_j(1+t_j).                               (1.3)
```

At the artificial value `U=t_j`, its logarithmic residue is

```text
w_j=
t_j^M product_(k!=j)(1+t_k)
-------------------------------- .                         (1.4)
       product_(k!=j)(t_k-t_j)
```

These weights alternate when the nodes are ordered.  Residue conservation
and the `M`-fold Taylor gap give the exact identities

```text
sum_j w_j=C_infinity-1,

sum_j w_j/t_j^ell=(-1)^(ell+1),       1<=ell<=M.            (1.5)
```

They make explicit that moving the finite poles does not remove the bill; it
transfers it between the target normalization, artificial residues, and the
residue at infinity.

There is also the exact product uncertainty law

```text
C_0 C_infinity
=product_j (1+t_j)^2/t_j>=4^M.                             (1.6)
```

The Taylor series of `Q_t(U)/U^M` is nonnegative exactly when at least one
node satisfies `t_j<=1`.  Sufficiency follows by pairing that node with the
factor `1/(1+U)`; necessity follows because otherwise `U=-1` is the unique
nearest singularity and its Taylor coefficients eventually alternate.  In
particular its linear coefficient forces

```text
sum_j 1/t_j>=1.                                             (1.7)
```

Thus at least one node remains bounded unless another node collapses toward
zero.  This is the elementary rational form of Pringsheim's positive-real
singularity principle.

## 2. Moving-value logarithmic lifts

Let `Omega` be a fixed simply connected disc, let

```text
V={|s-z_*|<r_0} compactly contained in Omega,
|rho-z_*|=d,
r_0<d<R,                                                   (2.1)
```

and assume `F_H in Hol(Omega)` has a uniformly bounded number of distinct
zeros, including `F_H(rho)=0`.  On `V` suppose

```text
F_H=1+U_H,
sup_V |U_H|<=E_H,
E_H ->0.                                                   (2.2)
```

### 2.1 Nodes tending to zero

If `t_H>0`, `t_H=O(1)`, `E_H/t_H ->0`, and `F_H` omits
`1+t_H`, define

```text
g_H=Log(1-U_H/t_H)/log(1+1/t_H).                            (2.3)
```

At an `F_H`-zero, `g_H` lies on a vertical lattice with real part one.
Boundedly many zeros leave two moving lattice values omitted which converge
to two distinct finite values.  Moving-value Montel normality and (2.2)
force `g_H ->0` throughout the disc, contradicting its value at `rho`.

Consequently a bounded artificial node can evade R155 only by satisfying,
optimistically,

```text
t_H=O(E_H).                                                 (2.4)
```

In (1.2), every such collapsed node contributes `E_H^(-1)` to `C_0` and
cancels one of the nominal `U` powers.  It supplies no net Euler-support
power in the right-cap estimate.

### 2.2 Nodes tending to infinity

The infinity case has a quantitative version.  Suppose `t_H -> infinity`,
`F_H` omits `1+t_H`, and set

```text
h_H=Log(1-U_H/t_H),
L_H=log(1+1/t_H).                                           (2.5)
```

The lattice of `h_H` at the zeros of `F_H` is

```text
L_H+2 pi i Z.                                               (2.6)
```

Boundedly many zeros again leave two lattice values omitted.  Montel makes
`h_H` normal, (2.2) makes its limit zero on `V`, and the identity theorem
makes it zero on compacta of `Omega`.  In particular the branch index at
`rho` is eventually zero and

```text
h_H(rho)=L_H asymp1/t_H.                                   (2.7)
```

Choose the radius `R` in (2.1) with a little outer slack.  Normality bounds
`h_H` on `|s-z_*|<=R`, while on the inner circle

```text
|h_H|<<E_H/t_H.                                             (2.8)
```

Hadamard three-circles at radii `r_0<d<R` now gives

```text
t_H>>E_H^(-kappa),

kappa=log(R/d)/log(d/r_0).                                  (2.9)
```

Thus an omitted value cannot drift to infinity slowly.  The minimum escape
rate is exactly a power of the right-cap error.

## 3. Exact exponent cancellation

Split the `M=q-1` nodes of (1.2), after a subsequence, into

```text
a collapsed nodes,       t_j=O(E_H),
b escaping nodes,        t_j -> infinity,
a+b=M.                                                       (3.1)
```

Any node remaining in a fixed compact subset of `(0,infinity)` is forbidden
by R155, and the intermediate `t_j ->0`, `E_H/t_j ->0` regime is forbidden by
Section 2.1.

Give the construction every optimistic advantage: assume the collapsed-node
denominators are separated on the control circle and ignore their tiny
artificial residues.  Equations (1.2) and (3.1) then leave at best

```text
right-cap size E_H^(b+1).                                  (3.2)
```

On the other hand, (1.3) and (2.9) give

```text
C_infinity>>E_H^(-kappa b).                                (3.3)
```

At the known arithmetic scale, write

```text
E_H=H^(-mu+o(1)),
log conductor asymp H,
H=exp(beta k),

A=log(d/r_0),
B=log(R/d),
kappa=B/A.                                                  (3.4)
```

The Euler upper bound (3.2) can beat a target at distance `d` only if

```text
beta mu(b+1)>A.                                             (3.5)
```

The absolute outer denominator ledger is at least

```text
H C_infinity=H^(1+mu kappa b+o(1)),                         (3.6)
```

so outer localization requires

```text
beta[1+mu kappa b]<B.                                      (3.7)
```

Combining (3.5)--(3.7) and using `kappa=B/A` cancels `b`
exactly and leaves

```text
A/mu<B.                                                     (3.8)
```

For the R153 geometry, one may take any inner radius `r_0<r` and then

```text
mu=r-r_0,
d=r+delta,
R<r+eta.                                                    (3.9)
```

In fact (3.8) is impossible for every such choice, because

```text
mu B<mu(eta-delta)/d<mu/d
     <(mu+delta)/d<=log(d/r_0)=A.                           (3.10)
```

For the convenient circle used in R153,

```text
r_0=r/2,
mu=r/2,                                                     (3.11)
```

so (3.8) becomes

```text
log(2d/r)<(r/2)log(R/d).                                   (3.12)
```

This is false: the left side exceeds `log 2`, while the right side is less
than `(R-d)/2<1/4` in the fixed-strip geometry.  The number of moving nodes
does not matter.  Nodes near `1` lose the Euler power, and nodes at infinity
repay precisely the same power in the denominator residue.

The theorem closes moving values for the present **absolute** Cauchy/Turan
scheme.  It does not rule out a new arithmetic signed cancellation of the
amplified denominator ledger; that would be a genuinely different input.

## 4. The exact two-value response

There is an especially economical response which keeps only `F=0` and
`F=2` as finite value divisors.  For even `q`, set

```text
C_q(s)=-2 U(s)^(q-1)U'(s)/[1-U(s)^2].                      (4.1)
```

Its Dirichlet coefficients are nonnegative, since

```text
C_q=2[-U']U^(q-1)sum_(j>=0)U^(2j),                         (4.2)
```

and its support starts beyond `H^q`.  Both `F=0` and `F=2` have simple
residue `+1`.  But

```text
C_q=C_2+d/ds[sum_(j=1)^(q/2-1) U^(2j)/j].                  (4.3)
```

All support beyond `H^2` is carried by an exact polynomial-at-infinity
germ.  An unweighted contour erases it, and every localizing weight pays it
on the boundary.  Equation (4.3) is the two-value form of the R154
conservation law.

## 5. A cutoff-complete local cancellation countermodel

The following finite construction shows that topology and favorable residue
sign cannot replace arithmetic information.

Normalize

```text
x=(s-z_*)/(rho-z_*),                                       (5.1)
```

so the observation point is `x=0` and the target is `x=1`.  Fix

```text
S>1,
0<kappa_0<1,
log S<tau<2 log S.                                         (5.2)
```

For large `N`, put

```text
S_N(x)=sum_(j=1)^N x^j/j,
L_N=floor(exp(tau N)/N),
E_N(x)=sum_(ell=0)^L_N S_N(x)^ell/ell!,
F_N(x)=(1-x)E_N(x).                                        (5.3)
```

On `|x|<=S`, one has `|S_N(x)|=O(S^N/N)`, while
`L_N/(S^N/N)` grows exponentially.  The standard exponential-tail estimate
therefore gives

```text
E_N(x)/exp(S_N(x))=1+o(1)                                  (5.4)
```

uniformly on that disc.  In particular `E_N` is zero-free there.  Hence
`F_N` is a polynomial with exactly one zero in `|x|<=S`, the simple target
`x=1`, and no poles.

Because `L_N>N`, the Taylor identity

```text
(1-x)exp(S_N(x))
=exp[-sum_(j>N)x^j/j]
=1+O(x^(N+1))                                               (5.5)
```

also holds through degree `N` with `E_N` in place of the exponential.  Thus

```text
F_N=1+O(x^(N+1)),
sup_(|x|<=kappa_0)|F_N-1|<<kappa_0^N/N.                    (5.6)
```

Let

```text
G_N=F_N(2-F_N)=1-(F_N-1)^2.                                (5.7)
```

If `M_N=deg F_N=NL_N+1=exp(tau N+o(N))`, then `G_N` has degree
at most `2M_N`, satisfies `G_N(0)=1`, and

```text
G_N=1+O(x^(2N+2)).                                         (5.8)
```

Factoring the polynomial at zero shows, for every
`1<=m<=2N+1`,

```text
sum_(G_N(c)=0) mult(c)c^(-m)=0.                             (5.9)
```

Inside `|x|<=S`, the zeros in (5.9) are exactly the target `c=1` and
the points where `F_N=2`.  The zeros outside the disc contribute at most

```text
2M_N S^(-m).                                               (5.10)
```

Choose

```text
tau/log S<theta<2.                                         (5.11)
```

Then throughout the linearly long block

```text
theta N<=m<=2N+1,                                          (5.12)
```

the local target plus forced mixed packet satisfies

```text
|1+sum_(F_N(b)=2, |b|<=S)mult(b)b^(-m)|
 <=exp[-(theta log S-tau)N+o(N)].                          (5.13)
```

Every residue in (5.13) is positive.  Nevertheless the reciprocal powers
cancel the target exponentially well for `Theta(N)` consecutive orders.

This is at the exact scale of the arithmetic gate:

```text
total divisor ledger       O(M_N),
right-cap error             M_N^[-log(1/kappa_0)/tau+o(1)],
log max_(|x|<=S)|F_N|       O(S^N)=o(M_N).                  (5.14)
```

Thus the cancellation is local, cutoff-complete, and compatible with an
`O(H)` divisor ledger after identifying `H=M_N`.  It is not imported from
far zeros or an uncontrolled entire-function genus.

The countermodel is a polynomial in the local coordinate.  It is not an
Euler quotient and does not have the actual nonnegative Dirichlet coefficient
alphabet.  That missing coefficient-specific arithmetic is precisely the
only kind of hypothesis which can now distinguish the zeta problem from
(5.3).

## 6. Winding and universal covers do not add a scalar invariant

Let `omega` be a meromorphic differential on the value sphere with residue
one at the target value `0` and a zero of order at least `q-1` at the head
value `1`.  Since

```text
deg div(omega)=-2,                                         (6.1)
```

if every pole is simple, `omega` has at least `q+1` poles on the sphere.
After counting the target and infinity, at least `q-1` artificial finite
values remain.  This is the divisor-theoretic reason the root-of-unity packet
is degree-optimal.

If higher poles are permitted, every rational differential decomposes
uniquely as

```text
omega=sum_a r_a dz/(z-a)+dS(z).                            (6.2)
```

Only the logarithmic part has periods.  For a holomorphic contour weight
`phi`,

```text
integral_Gamma phi F^*omega
=2 pi i sum_a r_a sum_(F(alpha)=a)ord_alpha(F-a)phi(alpha)
 -integral_Gamma phi'(s)S(F(s))ds.                         (6.3)
```

An unweighted contour retains topology but erases localization.  A
localizing weight pays the full exact-germ boundary term.

The same statement holds on a universal or branched cover.  A scalar
primitive with path-independent additive monodromy has a differential which
descends and therefore obeys (6.2).  In logarithmic coordinates,

```text
Phi(h+2 pi i e_j)-Phi(h)=C_j

implies

Phi(h)=sum_j C_j h_j/(2 pi i)+P(h),                         (6.4)
```

where `P` is deck-periodic and descends to the exact term.  Sheet-dependent
increments are not path-independent invariants and cannot be charged only to
the `O(log conductor)` winding count.  Ahlfors, Bloch, and Nevanlinna
covering arguments can count the forced sheets and value points, but do not
control their angular reciprocal moments; (5.13) is an explicit witness.

## 7. Consequence

The mixed points are unavoidable, moving them does not improve the absolute
exponent ledger, and their positive local degrees do not prevent long signed
reciprocal-power cancellation.  The surviving statement is narrower than
the former mixed-`a`-point selection problem:

```text
prove a coefficient-specific signed joint estimate for the actual Euler/
Artin quotient, using information which fails for the polynomial model
(5.3).                                                          (7.1)
```

Possible sources would be an exact relation among the mixed divisor and
prime coefficients, a class-group determinant with a new sign, or a family
correlation theorem retaining the growing head.  Pure scalar functional
calculus, normality, winding, value avoidance, and absolute divisor counting
are now exhausted on this branch.

This report proves neither existence nor nonexistence of a fixed zeta
zero-free strip.

Successors:
[`R157-CLASS-GROUP-MATRIX-TREE-AND-DETERMINANT-GATE.md`](R157-CLASS-GROUP-MATRIX-TREE-AND-DETERMINANT-GATE.md)
and
[`R158-CONDITIONED-MIXED-POINT-FAMILY-AND-SKELETON-GATE.md`](R158-CONDITIONED-MIXED-POINT-FAMILY-AND-SKELETON-GATE.md).
