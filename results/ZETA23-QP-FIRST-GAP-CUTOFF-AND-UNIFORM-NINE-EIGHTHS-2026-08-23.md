# QP four-cycle: first-gap cutoff and the uniform `9/8` theorem

**Date:** 2026-08-23  
**Verdict:** two occupied points on one parabolic carrier line obey two
first-difference inequalities which were absent from the earlier
occupied-line ledger.  They lower the complete parabolic curvature term
from

```text
D^(37/32+o(1)) ||z||_2^4
```

to

```text
D^(71/64+o(1)) ||z||_2^4.                         (0.1)
```

The mixed-`H^2` product-large-sieve theorem already bounds every broad and
one-point/singleton sector by `D^(9/8+o(1))`.  Since

```text
71/64 < 9/8,
```

the complete fourth trace now satisfies

```text
tr((A_z^* A_z)^2)
 <<D^(9/8+o(1)) ||z||_2^4.                         (0.2)
```

Consequently

```text
||A_z||_(S_4) <<D^(9/32+o(1)) ||z||_2,             (0.3)
```

and the established `D=q^(16/33+o(1))` transfer gives transverse exponent

```text
1/2+(9/32)*(16/33)=7/11.                          (0.4)
```

This is an unconditional improvement, not the sharp four-cycle theorem.
After (0.1), the remaining sharp gap is exactly the one-point
high-completion tail.

## 1. Exact first color gaps

Fix one signed color matrix

```text
C=(x,y;zeta,w)
```

and a completion `(a,b)`, with `a=(a_1,a_2)` and `b=(b_1,b_2)`.  Put

```text
rho_11=8*a_1*b_1*x-q^3,      rho_12=8*a_1*b_2*y-q^3,
rho_21=8*a_2*b_1*zeta-q^3.
```

On the already-truncated carry core, the project window gives
`|rho_ij|<<qD`, while every shell carrier is
comparable with `q`.  Therefore

```text
e_top =x*b_1-y*b_2       =(rho_11-rho_12)/(8*a_1)=O(D),
f_left=x*a_1-zeta*a_2    =(rho_11-rho_21)/(8*b_1)=O(D).           (1.1)
```

Let one maximal parabolic line be

```text
a(t)=a+t*A*r,             b(t)=b+t*B*s,             (A,B)=1,     (1.2)
```

where `r=(r_1,r_2)`, `s=(s_1,s_2)`.  If both `t` and `t+h` are occupied,
the exact token equations give

```text
s_1*x-s_2*y       =r_2*eta,
r_1*x-r_2*zeta    =-s_2*theta.                                    (1.3)
```

Subtract (1.1) at the two parameters.  There is no approximation in the
increments:

```text
Delta_h e_top
 =h*B*(s_1*x-s_2*y)=h*B*r_2*eta,

Delta_h f_left
 =h*A*(r_1*x-r_2*zeta)=-h*A*s_2*theta.             (1.4)
```

Use the bottom gap if the other row coordinate is maximal, and the right
gap if the other column coordinate is maximal.  Equations (1.1)--(1.4)
prove the uniform necessary conditions

```text
|h|*B*E*R <<D,
|h|*A*T*S <<D.                                    (1.5)
```

The former `37/32` affine-prime face had

```text
B*E*R=D^(85/64),
```

so every one of its carrier lines is in fact a singleton.  Its purported
repeated-point curvature packet is empty.

For comparison, subtracting the four products directly also gives the
literal wedge identities

```text
s_1*Delta P_(i2)-s_2*Delta P_(i1)=h*A*r_i*beta,
r_1*Delta P_(2j)-r_2*Delta P_(1j)=h*B*s_j*alpha,   (1.6)
```

where `alpha=det(r,a)` and `beta=det(s,b)`.  Since the already proved
transverse scales are `|alpha|~ST`, `|beta|~RE`, (1.6) is equivalent to
the same first-gap restrictions after the exact multiplier-ratio identity
in the next section.  Thus (1.5) is not a sign or indexing artifact.

## 2. Dyadic line ledger

Write

```text
R=D^r, S=D^s, E=D^e, T=D^t, G=D^g,
A=D^a, B=D^b.                                     (2.1)
```

Let `D^ell` be the number-scale of additional integral parameters on one
line.  The old quadratic product-band bound and the two new first gaps give

```text
2*ell+a+b+r+s <=1,
ell+b+e+r     <=1,
ell+a+t+s     <=1.                                (2.2)
```

In transverse coordinates,

```text
A=eta*alpha/g_0,       B=-theta*beta/g_0,
|alpha|~S*T,           |beta|~R*E.
```

Hence, up to the harmless dyadic `q^o(1)` slack,

```text
b-a=r-s.                                           (2.3)
```

Let `D^j` count the occupied maximal lines in this `(A,B)` block.  The
pinned nonzero integral level has divisor-many lifts for fixed `(A,B)`:
`g_0|kL` fixes the transverse content, after which the primitive affine
level equation is one maximal line.  Therefore

```text
j<=a+b.                                            (2.4)
```

The ambient third-slice cap also gives

```text
j<=kappa,
p=max(e+2r,t+2s)-g,
kappa=max(0,p-17/16),       p<=11/8.               (2.5)
```

Finally, the anchored one-sided matching theorem gives relation mass
`D^w`, where

```text
w<=r+t-g,
w<=s+e-g.                                         (2.6)
```

Thus one curvature block costs at most

```text
D^(w+j+ell+o(1)) ||z||_2^4.                       (2.7)
```

## 3. Exact `71/64` optimization

Consider first the high-slice branch

```text
p=e+2r-g >=t+2s-g,
kappa=p-17/16.                                    (3.1)
```

The following positive linear combination is an exact dual certificate:

```text
  1/2 * (e+t<=1)
+ 3/4 * (j<=a+b)
+ 1/4 * (j<=e+2r-g-17/16)
+ 1/2 * (w<=r+t-g)
+ 1/2 * (w<=s+e-g)
+ 5/8 * (2ell+a+b+r+s<=1)
+ 1/4 * (ell+b+e+r<=1).                           (3.2)
```

Using (2.3), its left side is

```text
w+j+(3/2)*ell+(5/4)*g,
```

whereas its right side is

```text
1/2-17/64+5/8+1/4=71/64.                          (3.3)
```

Since `ell,g>=0`, (3.2)--(3.3) imply

```text
w+j+ell<=71/64.                                   (3.4)
```

The opposite branch is obtained by transposition.  The inactive branch is
also immediate from the same inequalities.  If `p<=17/16`, then
`kappa=j=0`.  Put

```text
v=r+s,       d=r-s,       u=a+r=b+s,
m=max(e+d,t-d).
```

Then `p=v+m-g`, (2.6) gives `w<=p-v/2`, and the two first-gap bounds give
`ell<=1-u-m`.  Since `u=(a+b+v)/2>=v/2`,

```text
w+ell<=1+v/2-u-g<=1.
```

This proves (0.1) on every branch.

The high-slice equality point in (3.4) is

```text
(e,t,r,s,g)=(1/2,1/2,25/64,25/64,0),
(a,b,j,ell,w)=(7/64,7/64,7/32,0,57/64).           (3.5)
```

In particular, the remaining `71/64` auxiliary endpoint consists of
`O(1)`-length lines, not a long tangent packet.

## 4. Global sector synthesis

The canonical mixed-`H^2` report proves, uniformly on every coefficient
bin and after Schatten-four recombination,

```text
broad and singleton sectors
 <<D^(9/8+o(1)) ||z||_2^4.                         (4.1)
```

Its only larger term was the old parabolic curvature estimate.  Replacing
that term by (0.1), and retaining the already closed repeated-node,
opposite-pair, and permutation sectors, gives

```text
max(9/8,71/64,1)=9/8,                              (4.2)
```

which is (0.2).

The exact identities and exponent ledger are replayed in
`src/qp_first_gap_uniform_nine_eighths.py` and its test module.

## 5. What remains sharp

The failed weighted-Schur shortcut is now immaterial for repeated points:
(1.5) kills its old extremal packet before any carrier-lift norm is formed.
It does **not** control a family having one occupied point on each of many
different lines.  Such a family has no nonzero parameter difference to
which (1.4) can be applied.

Thus the remaining sharp theorem is the dyadic high-completion estimate

```text
sum_(C: K<=m(C)<2K) w_z(C)
 <<D/K*q^o(1)||z||_2^4.                            (5.1)
```

Equivalently, one needs the mask-sensitive one-point/secant aggregation
which the existing positive principal determinant term and diffuse bound
both miss by `D^(1/8)` at their crossover.  The present report does not
claim (5.1).

The critical singleton block can be normalized as

```text
(e,t,r,s,g)=(1/2,1/2,7/16,7/16,0),
K=D^(5/16),        M=D^(15/8),
A,B~D^(5/32).
```

After the divisor-many transverse content is frozen, it permits a
line-sparse `A x B` family with one selected integer point on each affine
level line.  Subtracting two different lines yields only the already-known
bilinear residual matching; unlike (1.4), there is no common-line parameter
difference.  The available two-sided residual lattices have capacity
`sqrt(D)>K`, so geometry of numbers alone gives no power saving.  This is
the precise obstruction left by the new theorem.

```text
exact first color gaps (1.1):                       PROVED;
two new line-separation bounds (1.5):               PROVED;
fixed-(A,B) divisor multiplicity:                   PREVIOUSLY PROVED;
parabolic curvature D^(71/64+o(1)):                 PROVED;
broad/singleton D^(9/8+o(1)):                       PREVIOUSLY PROVED;
uniform fourth trace D^(9/8+o(1)):                  PROVED;
carry/Schatten exponent 9/32:                       PROVED;
transferred exponent 7/11:                          PROVED;
sharp fourth trace D^(1+o(1)):                      OPEN.
```
