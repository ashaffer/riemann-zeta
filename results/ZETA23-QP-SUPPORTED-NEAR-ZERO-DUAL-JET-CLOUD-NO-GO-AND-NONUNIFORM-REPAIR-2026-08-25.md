# QP phase jets: a supported near-zero-dual cloud and its nonuniform repair

**Date:** 2026-08-25  
**Scope:** exact physical completion-action Fourier modes  
**Verdict:** the proposed **unrestricted** maximum-degree formulation at the
full pair threshold `D^(-1/6)` is false.  There is an exact family of
supported, regular, nonreflected stationary modes with more than
`D^(1+o(1))` distinct tangent fingerprints in one unresolved quotient-jet
ball.  No endpoint, zero-dual, or fold mode is used.

This is not a counterexample to the sharp four-cycle bound.  It is also not
a counterexample to a theorem restricted to tangent charts actually
populated by off-axis primal product-band points: the construction below is
a family of dual Fourier modes, and it does not prove that every tangent in
the dense bin carries a residual primal point.  In particular, the primal
conditions `z=0`, `z=+-d*v`, `H-pU=0`, and `d^2|g` are not even defined for
a bare dual mode.

Two positive conclusions accompany the no-go.

1. The weaker threshold `D^(-7/48)` needed only to close the present
   `D^(7/96)` operator gap is not obstructed.  Its unresolved cloud is at
   most `D^(47/48+o(1))`, below the permitted `D^(49/48+o(1))` degree.
2. Even at the full threshold, retaining the actual nonuniform quadratic
   correlations gives a Schur row sum `D^(7/8+o(1))`, below the squared
   Bessel target `D` by `D^(1/8)`.  Thus the cloud invalidates the coarse
   uniform-degree route, not the desired Bessel conclusion.

## 1. Exact canonical ladder

Put

```text
C=Q^2,                    S_0=2Q.                    (1.1)
```

Let `p>d>0` be coprime and of opposite parity, and let `t>=1`.  Define

```text
h=(p+d)^2*t,
k=(p-d)^2*(t+1),
m=p^2.                                               (1.2)
```

For

```text
F(a,S)=-m*a+C*h/a+C*k/(S-a),                         (1.3)
```

the point

```text
a_0=Q*(p+d)/p,             b_0=Q*(p-d)/p             (1.4)
```

is exactly stationary at `S=S_0`, since

```text
C*(k/b_0^2-h/a_0^2)=p^2*((t+1)-t)=m.                (1.5)
```

All three frequencies are positive.  Hence the saddle is interior,

```text
F_aa=2C*(h/a_0^3+k/b_0^3)>0,                        (1.6)
```

and the mode is neither an endpoint, nor zero-dual, nor a fold.  Reflection
sends `(d,h,k,m)` to `(-d,k,h,-m)` and therefore leaves the positive-`d`,
positive-`m` family.

Let `J(S)` be the critical action on this unique branch.  Exact substitution
in the stationary-action formulas gives

```text
J(S_0) =2Q*p*(p*t-d),
J'(S_0)=-p^2*(t+1),                                  (1.7)

J''(S_0)
 =2*p^3*t*(t+1)/[Q*(2*p*t+p+d)].                    (1.8)
```

The first two quantities in (1.7) are integers.  Thus the value and slope
differences between any two modes in the family are exactly invisible in
the integer Newton quotient.  Put

```text
R=Q*J''(S_0)
 =2*p^3*t*(t+1)/(2*p*t+p+d).                        (1.9)
```

The higher derivatives satisfy uniformly in every fixed tangent collar

```text
J'''=O(J''/Q),              J''''=O(J''/Q^2).       (1.10)
```

These follow either directly from the exact rational formulas or from the
scale-free identities for the quotient curvature jet.

The lifted tangent coordinate is genuinely changing.  Because the parity
divisor is one,

```text
K_2=8*p^4/(p^2-d^2).                                 (1.11)
```

The reduced fraction `K_2/8=p^4/(p^2-d^2)` recovers `(p,d)` for `d>0`.
Consequently distinct pairs `(p,d)` in this family have distinct
`(chi,K_2)` fingerprints.  The cloud is not created by duplicating one
tangent or by reflection.

## 2. All modes fit in the physical support

At the worst endpoint write

```text
Q=D^(33/16),        H=D^(17/16),        N=D^(11/16). (2.1)
```

Take

```text
D^(77/160)<=p<=sqrt(H/64),
p/8<=d<=p/4,
(p,d)=1,            p-d odd,
t=floor(H/(16*p^2)).                                (2.2)
```

The interval in `p` is nonempty by a power:

```text
17/32-77/160=1/20.                                  (2.3)
```

Moreover `t>=4`, and

```text
h <=(5p/4)^2*H/(16p^2) =25H/256,
k <=p^2*(H/(16p^2)+1)   <=5H/64,
m =p^2                         <=H/64.               (2.4)
```

Thus every frequency is strictly inside the Fejer box by an absolute
factor.  The saddle ratio lies in

```text
9/16<=a_0/S_0<=5/8,                                 (2.5)
```

so there is no endpoint loss.

The number of coprime opposite-parity lattice pairs in the collar (2.2) is

```text
asymp H                                               (2.6)
```

up to harmless logarithmic errors.  This is the elementary positive-density
count of primitive lattice points in a fixed planar sector; deleting
`p<D^(77/160)=o(sqrt(H))` does not affect its order.

For the chosen `t`, one has `p^2*t asy H`.  Equation (1.9) therefore puts
all `R` values inside an interval of length `O(H)`.  Partition that interval
into half-open bins of width

```text
W=D^(1+epsilon),          0<epsilon<1/48.            (2.7)
```

There are `O(H/W)` bins.  By (2.6), one bin contains

```text
>>W*D^(-o(1))=D^(1+epsilon-o(1))                    (2.8)
```

distinct `(p,d)` and hence distinct tangent fingerprints.  Every pair in
this bin has

```text
|Delta J''(S_0)| <= W/Q
                  =D^(-(17/16-epsilon)).            (2.9)
```

Across an `N`-block, (1.10) changes this by only

```text
O(H*N/Q^2)=o(W/Q).                                  (2.10)
```

The second derivative therefore stays below the same scale throughout the
physical block.

## 3. Which full-threshold statement fails

For a normalized second-derivative estimate, a scale

```text
lambda=D^(-u)                                       (3.1)
```

can yield the full pair saving `D^(-1/6)` only when

```text
1/3<=u<=25/24.                                      (3.2)
```

The cloud has

```text
u>=17/16-epsilon>25/24                              (3.3)
```

precisely because `epsilon<1/48`.  Equivalently, the inverse term in the
normalized quadratic envelope is

```text
1/(N*sqrt(lambda))
 >=D^(-(5/32+epsilon/2))
 > D^(-1/6).                                        (3.4)
```

The first-difference test cannot repair this on a block containing `S_0`:
after the exact integral slope alias, its initial increment is only
`O(W/Q)` from an integer.  Deleting the resulting stationary endpoint and
using first differences reproduces the inverse term (3.4).  The third
derivative is much too small:

```text
|Delta J'''|<<H/Q^2=D^(-49/16),                     (3.5)
```

outside the useful cubic window by a large power.

Therefore the bin (2.8) is one quotient-jet neighborhood unresolved at
threshold `D^(-1/6)`, yet its degree exceeds `D^(1+o(1))`.

This falsifies the following unrestricted desired assertion:

> Every collection of regular supported completion-action modes has
> full-threshold jet-major-arc degree `Delta<<D^(1+o(1))`, apart from exact
> endpoint, zero-dual, fold, and reflection modes.

It does **not** falsify the finite Schur theorem itself.  That theorem is an
identity conditional on the actual major-arc degree.  Nor does it falsify a
future theorem that first uses the primal product masks to prove that only
a sparse subset of the dual tangent cloud is occupied.  The latter is the
precise mask-sensitive escape left open by this audit.

The fourth action derivative distinguishes the members exactly, in
agreement with quotient-jet rigidity.  That exact injectivity does not
bound the number of distinct fingerprints inside a ball of the physical
resolution (2.9); this is the quantitative gap exposed here.

## 4. The weaker gap-closing threshold survives

For the pair saving needed only to close the current operator deficit,

```text
eta_close=D^(-7/48),                                 (4.1)
```

the quadratic useful window extends to

```text
u<=2N-2*(7/48)=13/12.                               (4.2)
```

Consequently a genuinely unresolved `R=QJ''` interval has width at most

```text
D^(Q-13/12)=D^(47/48).                              (4.3)
```

The cloud has bounded-average density in `R` (proved more quantitatively in
Section 5), so its unresolved degree is at most

```text
D^(47/48+o(1)).                                     (4.4)
```

The allowed degree for closing the present gap is

```text
D^(49/48+o(1)).                                     (4.5)
```

Thus this family lies below that ceiling by `D^(1/24)`.  In particular, it
cannot be cited against the weaker transference theorem.

## 5. Nonuniform Schur closes the whole phase cloud

There is an elementary local-density estimate behind (4.4).  For fixed
`p`, (1.9) is strictly monotone in `d`, and consecutive allowed `d` values
change `R` by `asymp p`.  Hence, for the one-mode-per-tangent family,

```text
#{nu: |R_nu-R_0|<=r}
 <<D^o(1)*(sqrt(H)+r).                              (5.1)
```

The `sqrt(H)` term permits one accidental member for every denominator
`p`; the `r` term is the summed local density `sum_p r/p`.

Put

```text
r_0=Q/N^2=D^(11/16).                                (5.2)
```

For `r<=r_0`, use the trivial correlation bound one.  Equation (5.1) costs

```text
D^(11/16+o(1)).                                     (5.3)
```

For a dyadic annulus `r>=r_0`, (1.10) shows that the second derivative of a
phase difference has constant sign and is comparable with `r/Q` on the
whole block.  The normalized finite quadratic estimate gives

```text
rho(r)<<sqrt(r/Q)+sqrt(Q)/(N*sqrt(r)).              (5.4)
```

Summing (5.4) against (5.1) over dyadic `r<=H` yields four endpoint terms.
The two largest are

```text
H^(3/2)/sqrt(Q)        =D^(9/16),
sqrt(Q*H)/N            =D^(7/8).                    (5.5)
```

The additive `sqrt(H)` terms cost at most `D^(17/32+o(1))`.  Combining
(5.3)--(5.5), every Gram row in this phase-only cloud has

```text
sum_mu |<u_nu,u_mu>| <<D^(7/8+o(1)).                (5.6)
```

Schur therefore bounds its squared Bessel norm by `D^(7/8+o(1))`, with
`D^(1/8)` room under the desired `D` target.

This repair uses the nonuniform form of the already proved phase-jet Schur
theorem.  It says that declaring every correlation larger than one fixed
`eta` to cost one is unnecessarily expensive near the zero-dual ladder.
It closes this canonical flat-amplitude phase cloud only.  A physical proof
must still transfer the stationary cross-amplitudes with bounded Abel
variation and impose the primal masks.

## 6. Finite physical packet fixture

The exact/high-precision fixture

```text
Q=10^6,       C=Q^2,       S_0=2Q,
N=100,        H=1300,
p=26,         t=1,
d=1,3,5,7                                             (6.1)
```

has all frequencies at most `1300`, while the application scales are

```text
Q^(77/330)=25.119...,
Q^(17/33)=1232.85...,
D=Q^(16/33)=811.13....                               (6.2)
```

Thus `p` is above the residual primitive floor and the support discrepancy
is only an immaterial dyadic constant.  Direct bisection of the unique
stationary branch at all 100 consecutive integer completions gives the
correlations with the `d=1` packet

```text
d=3:  0.9793753497...
d=5:  0.9230716962...
d=7:  0.8403778668....                              (6.3)
```

All exceed the finite full-threshold proxy

```text
D^(-1/6)=0.3274549....                               (6.4)
```

This fixture is only a numerical replay of the exact family; the asymptotic
degree no-go is the counting argument in Sections 2--3.

## 7. Corrected architecture and binary status

A viable phase-jet route must use one of the following refinements.

1. Apply the nonuniform row sum (5.4)--(5.6) to a thick neighborhood of
   the zero-dual ladder, rather than placing that whole neighborhood in a
   unit-cost major-arc graph.
2. Prove that the actual primal residual masks occupy only a sufficiently
   sparse subset of the supported dual cloud.
3. For the present `D^(7/96)` gap, use the weaker threshold (4.1), which
   already resolves this family.

The exact construction, exponent ledger, finite cloud enumerator, and
high-precision packet replay are in

```text
src/qp_near_zero_dual_cloud.py
src/test_qp_near_zero_dual_cloud.py
```

```text
canonical stationary family and affine aliases:       PROVED EXACTLY;
physical frequency support and compact collar:         PROVED;
distinct nonreflection tangent fingerprints:           PROVED;
full-threshold unresolved degree >D:                    PROVED;
unrestricted regular-mode degree theorem:               FALSE;
weaker D^(-7/48) threshold obstructed by this cloud:    NO;
nonuniform phase-only Schur row D^(7/8+o(1)):           PROVED;
every cloud tangent populated by a primal residual:     NOT PROVED;
mask-restricted sampled-to-lifted transference:          OPEN;
sharp four-cycle bound:                                 NOT DISPROVED OR PROVED.
```
