# QP reciprocal strip: coupled cusp TT*, Fejer tails, and a local-packet inverse reduction

**Date:** 2026-08-25  
**Verdict:** the coupled nonzero-dual theorem is not proved, but the use of the
concrete Fejer coefficients gives a sharper reduction than an
arbitrary-coefficient large sieve.

Three statements are rigorous.

1. Fejer--Riesz gives an exact `TT*` identity.  A uniform operator bound at
   scale `H^2*sqrt(D)` would suffice; on the full-integer majorant this scale is
   attained by a rational tangent packet.
2. If `m=min(U,V)` and `M=max(U,V)`, the concrete squared-decay Fejer mask and
   a one-product divisor count close every dyadic mask with
   `m*M^2>=sqrt(D)`.
3. In the remaining core `m*M^2<sqrt(D)`, local determinant rigidity turns
   every populated `q^(1/3)` block into one bi-affine packet (up to two atoms).
   A violation therefore forces many spatially separated packet locations.

The missing theorem is a global packet-counting statement in the smaller core
`min(U,V)*max(U,V)^2<sqrt(D)`.  It is not proved below, so the sharp four-cycle
bound remains open.

## 1. Use a concrete majorant, not arbitrary coefficients

Put

```text
delta=D/q,       H=q/D,       q=D^(33/16).            (1.1)
```

Let

```text
F_N(theta)=N^(-1)|sum_(0<=j<N)e(j*theta)|^2,
P(theta)=C_0 F_N(theta)/N,
N=max(1,floor(kappa*H)) asymp H,                       (1.2)
```

where `kappa>0` is a sufficiently small fixed constant and `C_0` is a fixed
large constant.  On `||theta||<=delta`, the sine quotient in (1.2) is bounded
below, so `P>=1`.  Moreover

```text
P(theta)<<min(1,(H*||theta||)^(-2)),                 (1.3)
c_h=(C_0/N)(1-|h|/N),       |h|<N,                  (1.4)
sum_h |c_h|<<1,             sum_h |c_h|^2<<1/H.     (1.5)
```

These are the concrete positive triangular Fejer coefficients.  Here
"concrete coefficients" refers to the Fourier coefficients in (1.4), not to
the prime-power node weights in the original four-cycle problem.

For fixed `S`, work in a shell where

```text
a asymp S-a asymp q,       C asymp q^2,       0<=W(a)<=1.       (1.6)
```

In either majorant, require `W=1` on the support being counted.  Taking `W`
to be the indicator of the actual prime-power conditions on `a` and `S-a`
keeps the literal outer support, although the Fejer majorant still drops the
prime-power conditions on the carrier variables `v,w`.  Taking `W` to be a
smooth full-integer shell cutoff which equals one on the physical shell is a
stronger all-integer majorant.  Define

```text
theta_1(a)=C/a mod 1,       theta_2(a)=C/(S-a) mod 1.
```

The fixed-sum strip count is at most

```text
mathcal R(S)=sum_a W(a)P(theta_1(a))P(theta_2(a)).    (1.7)
```

## 2. Exact Fejer--Riesz TT* and the sufficient uniform scale

Since `P>=0`, Fejer--Riesz gives

```text
P(theta)=|A(theta)|^2,
A(theta)=sum_(0<=r<N) alpha_r e(r*theta),
sum_r |alpha_r|^2=c_0 asymp 1/H.                    (2.1)
```

Put

```text
b_(r,s)=alpha_r*alpha_s,
phi_a(r,s)=e(r*theta_1(a)+s*theta_2(a)),
G=sum_a W(a) phi_a phi_a^*.                          (2.2)
```

Then exactly

```text
mathcal R(S)=<b,Gb>,       ||b||_2^2=c_0^2 asymp H^(-2).  (2.3)
```

Consequently the uniform operator estimate

```text
||G||_(2->2) << H^2 sqrt(D) q^o(1)                  (2.4)
```

would prove the desired pointwise bound.  This estimate is sufficient, not
logically necessary: the application tests only the single rank-one vector
`b=alpha tensor alpha`.

The scale is attained by the stronger full-integer majorant.  If `C=Q^2`,
`S=2Q`, `|y|<=c*sqrt(D)`, and `W(Q+y)>>1` throughout this interval, then

```text
||C/(Q+y)||=y^2/(Q+y)<<1/H,
||C/(Q-y)||=y^2/(Q-y)<<1/H.                         (2.5)
```

The corresponding `asymp sqrt(D)` sampling vectors in (2.2) are nearly
parallel and each has squared norm `asymp H^2`.  Hence

```text
||G|| >= c H^2 sqrt(D).                              (2.6)
```

Thus (2.4) has no spare power as a uniform theorem for the full-integer
majorant.  For literal prime-power support there is no proved
`asymp sqrt(D)` tangent occupancy, so (2.6) is not a lower bound for the actual
prime-power operator.  The next two sections retain the application vector
rather than postulating (2.4).

## 3. Centered rational cusp coordinates with the Fejer coefficients

For the exact display assume `S=2Q`; the odd case is obtained by doubling the
coordinates.  Put

```text
lambda=C/Q^2,       x=Q+y,
p=h+k,              d=k-h.                          (3.1)
```

For every integer dual frequency `m`, direct division gives

```text
C(h/(Q+y)+k/(Q-y))-m(Q+y)
 =Q*(lambda*p-m)+(lambda*d-m)*y
  +lambda*(Q*p*y^2+d*y^3)/(Q^2-y^2).                (3.2)
```

This is the rational-center version of the cusp normal form.  If
`lambda=A/B` in lowest terms, a centered cubic has `p=0` and
`m=lambda*d`, so it can occur only when `B|d`.  This arithmetic thinning does
not address the regular modes, which were already the dominant term in the
nonzero-saddle audit.

In the symmetric case `lambda=1`, discard the integral affine terms and set

```text
A_y=Q*y^2/(Q^2-y^2),       t_y=y^3/(Q^2-y^2).        (3.3)
```

Then

```text
theta_1=A_y-t_y mod 1,       theta_2=A_y+t_y mod 1.  (3.4)
```

The product coefficients can be regrouped exactly:

```text
P(A-t)P(A+t)=sum_p B_p(t)e(p*A),                    (3.5)
B_p(t)=sum_h c_h*c_(p-h)e((p-2h)*t).                (3.6)
```

Twisted Young convolution and (1.5) give

```text
sum_p |B_p(t)|^2
 <=(sum_h |c_h|)^2 sum_h |c_h|^2
 <<1/H.                                             (3.7)
```

This is a genuine fixed-`t` norm saving supplied by the Fejer coefficients.
It does **not** contain a sum over `a`, and therefore proves no high-frequency
or aggregate cusp cancellation by itself.  A pointwise Cauchy--Schwarz sum
over the `O(H)` values of `p` spends the saving and returns the trivial bound
one.  Equations (3.5)--(3.7) only identify a coupled variable that a future
large sieve could exploit.

## 4. A sharp tail theorem from the actual Fejer decay

For dyadic `1<=U,V<=H`, let

```text
N(U,V)=#{a:
 ||C/a||<=c*U/H,
 ||C/(S-a)||<=c*V/H}.                                (4.1)
```

The decay (1.3) gives the cumulative dyadic majorization

```text
mathcal R(S)
 <<sum_(U,V dyadic) N(U,V)/(U^2 V^2).                (4.2)
```

There is a useful one-coordinate theorem.  The first inequality in (4.1)
produces an integer `v` with

```text
|a*v-C|<<D*U.                                        (4.3)
```

The integer product `a*v` lies in an interval containing `O(1+D*U)`
integers; each has `q^o(1)` divisors in the fixed shell.  Thus

```text
N(U,V) << D*min(U,V)*q^o(1).                         (4.4)
```

This uses only divisor bounds and is uniform in the real centre `C`.

Write

```text
m=min(U,V),       M=max(U,V).                        (4.5)
```

By (4.2)--(4.4), one mask contributes at most

```text
D*m/(U^2*V^2)*q^o(1)
 =D/(m*M^2)*q^o(1).                                  (4.6)
```

There are only logarithmically many masks.  Hence

> **Fejer tail theorem.** The total contribution to (1.7) from all dyadic
> masks with `m*M^2>=sqrt(D)` is `O(sqrt(D)*q^o(1))`.

In particular this includes every mask with `M>=D^(1/4)`.  The unhandled
region satisfies

```text
m*M^2<sqrt(D),                                       (4.7)
```

so necessarily `M<D^(1/4)`; in the balanced range `U asymp V`, it even has
`U,V<D^(1/6)`.  This sharper split uses the squared Fejer decay and disappears
after flattening the majorant coefficients.

## 5. The compact core has a local bi-affine packet inverse reduction

It remains to consider

```text
m=min(U,V),       M=max(U,V),       m*M^2<sqrt(D).   (5.1)
```

Every point counted by `N(U,V)` has carriers `v,w` satisfying

```text
|a*v-C|<<D*U,       |(S-a)*w-C|<<D*V.                (5.2)
```

Take three such points whose `a`-coordinates have diameter
`L<=c*q^(1/3)`.  The two reciprocal determinants obey

```text
|det(1,a_i,v_i)| <<L^3/q+L*D*U/q,
|det(1,S-a_i,w_i)| <<L^3/q+L*D*V/q.                 (5.3)
```

At the critical powers, the second error in either line is at most

```text
D*M*q^(-2/3)<D^(-1/8).                              (5.4)
```

After choosing the fixed constant `c` small enough, both integer
determinants vanish.  Thus in every short arc containing at least three
points, both projections are affine integer lines.  The four coordinates
have the form

```text
a=a_0+R*t,        S-a=b_0-R*t,
v=v_0-P*t,        w=w_0+K*t                         (5.5)
```

For sufficiently large `q`, the inequalities `D*M=o(q)` and
`a,S-a,C/q asymp q` make `v` strictly decrease and `w` strictly increase with
`a`; thus the direction products `R*P,R*K` are positive integers.  Along
(5.5), the two products in (5.2) are quadratics of curvatures `R*P` and
`R*K`.  Hence one such bi-line contains at most

```text
O(1+min(sqrt(D*U/(R*P)),sqrt(D*V/(R*K))))
 <<1+sqrt(D*min(U,V))                                (5.6)
```

points.

Partition the `a`-line by a regular half-open grid of block length
`ell=c_1*q^(1/3)` with `c_1` sufficiently small (the two endpoint fragments
may be shorter).  There are `O(q^(2/3))` blocks.  A block with at least three
points lies on a single bi-affine
line by the preceding determinant argument; a block with one or two points
is recorded as that many atoms.  Consequently every block contains
`O(1+sqrt(D*m))` points.  Selecting one of the three residue classes of
regular block indices retains a constant fraction of any collection while
making the retained block locations `Omega(ell)=Omega(q^(1/3))` apart.  This
separates locations, not necessarily affine directions.

Combining (4.2), the tail theorem, and (5.6) proves the following precise
dichotomy.

> **Spatial packet inverse reduction.** If the desired
> `sqrt(D)*q^o(1)` bound fails, then for some dyadic mask satisfying
> `m*M^2<sqrt(D)` one has
>
> ```text
> N(U,V) >>sqrt(D)*U^2*V^2*q^epsilon,                (5.7)
> ```
>
> after absorbing logarithms into `q^epsilon`.  Dividing by the block
> capacity in (5.6), and then taking a residue class of blocks, gives at least
>
> ```text
> >>m^(3/2)*M^2*q^epsilon                            (5.8)
> ```
>
> spatially separated nonempty packet blocks (including atomic blocks).

Thus a power-sized violation cannot be supplied by one full-integer tangent
packet.  No conclusion about distinct directions, aggregate cubic modes, or
frequency concentration follows from this local argument.

## 6. Exact remaining theorem

The following compact-core estimate is sufficient for the full-integer
majorant, and by the preceding reduction it is the only unhandled mask range
in that stronger route:

```text
N(U,V)
 <<sqrt(D)*U^2*V^2*q^o(1),
min(U,V)*max(U,V)^2<sqrt(D).                         (6.1)
```

For the literal problem one may instead prove (6.1) only on the prime-power
outer support, ideally retaining the prime-power restrictions on the two
carrier variables as well.  Local determinant rigidity proves the structure
of every short block, while the quadratic product bands prove its capacity.
What is missing is a global theorem preventing too many spatially separated
blocks from returning to the same coupled reciprocal mask.

This is strictly more informative than the original absolute
`D^(25/16)` saddle sum:

- every mask with `min(U,V)*max(U,V)^2>=sqrt(D)` is closed at `sqrt(D)`;
- the balanced unresolved core has shrunk to `U,V<D^(1/6)`;
- any remaining excess in the all-integer majorant is a many-location packet
  recurrence phenomenon.

The actual four-cycle support consists of shell prime powers `p^j`, with
arbitrary selected coefficients in the original operator.  Unique
factorization controls the representations of a fixed product but does not
bound the number of occupied sum levels or packet blocks.  Merely inserting
prime-density or prime-pair sieve estimates yields logarithmic savings, not
the fixed power required here.  Thus no prime-power fixed-`S` theorem is being
silently imported into (6.1).

No estimate currently supplied in the project proves (6.1), so this report
does not claim the four-cycle theorem.

### 6.1 The natural sharp special-curve theorem

A cleaner theorem would imply (6.1) with room to spare.  Uniformly in the
same shell, set `m=min(U,V)` and conjecturally prove

```text
N(U,V)
 <<(D^2*U*V/q+sqrt(D*m))*q^o(1).                     (6.2)
```

The first term is the anisotropic volume prediction.  The second is the
one-packet obstruction and is attained, up to constants, by the symmetric
tangent example `C=Q^2`, `S=2Q`.  Inserting (6.2) into (4.2) gives

```text
sum_(U,V) D^2/(q*U*V) <<D^2/q=D^(-1/16),
sqrt(D*m)/(U^2*V^2)=sqrt(D)/(m^(3/2)*M^2)<=sqrt(D).   (6.3)
```

Dyadic logarithms are absorbed by `q^o(1)`.  Thus (6.2) would close every
mask, not merely the current compact core.  It is a special anisotropic
lattice-point theorem for the reciprocal curve, substantially stronger than
the generic result below.  Equation (6.2) is a precise breakthrough target,
not a theorem proved in this report.

## 7. A generic space-curve theorem does not close the smaller core

Normalize

```text
a=q*t,       S=q*s,       C=q^2*c.
```

The ideal carrier curve is

```text
gamma(t)=(t,c/t,c/(s-t)).                              (7.1)
```

It really is a nondegenerate space curve: direct differentiation gives

```text
det(gamma',gamma'',gamma''')
 =12*c^2*s/(t^4*(s-t)^4),                              (7.2)
```

which is bounded away from zero on a fixed positive shell.  Thus the
torsion hypothesis itself is not the obstacle.  Even granting uniformity
over this compact curve family, the isotropic form of Huang's
fixed-denominator theorem with the larger thickness `delta asymp D*M/q`
would give only

```text
N(U,V)
 <<D^2*M^2/q+q^(3/5)*(log q)^(4/5).                   (7.3)
```

See [Huang, *Integral points close to a space
curve*](https://arxiv.org/abs/1809.07796), Theorem 1.  The volume term in
(7.3) is harmless, but at `q=D^(33/16)` the generic error is

```text
q^(3/5)=D^(99/80).                                    (7.4)
```

Inside `u+2v<1/2`, where `m=D^u`, `M=D^v`, and `u<=v`, one has
`u+v<=1/3`.  Even the largest possible right side required in (6.1) is only

```text
D^(1/2+2u+2v)<=D^(7/6).                               (7.5)
```

Thus the generic space-curve error misses every remaining mask, in the most
favourable case by `D^(99/80-7/6)=D^(17/240)`.  The sought estimate must use
the reciprocal/product arithmetic or mask coupling, not nonvanishing torsion
alone.

## Reproducibility

The rational-center identity, concrete Fejer coefficients, cusp convolution,
vertical-shift determinant invariance, torsion formula, and exponent ledger
are in

```text
src/qp_coupled_cusp_fejer_inverse.py
src/test_qp_coupled_cusp_fejer_inverse.py
```
