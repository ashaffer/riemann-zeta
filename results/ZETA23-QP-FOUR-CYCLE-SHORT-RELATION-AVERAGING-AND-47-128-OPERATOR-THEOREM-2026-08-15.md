# QP four-cycle: short-relation averaging and `47/128` operator theorem

**Date:** 2026-08-15  
**Verdict:** the fixed-color conic classification can be averaged with a
power saving.  For the truncated actual prime-power carry matrix and every
complex vector `z`, the all-distinct completed four-cycle mass satisfies

```text
|Q_nd(z)| << D^(47/32) q^o(1) ||z||_2^4.            (0.1)
```

Consequently

```text
||A_z||_op << D^(47/128) q^o(1) ||z||_2.            (0.2)
```

This improves the first global consequence of the fixed-color theorem,
`D^(3/2)` in (0.1) and `D^(3/8)` in (0.2), by the powers `D^(1/32)` and
`D^(1/128)` respectively.  Through the already proved smooth band-pass and
Schwartz-tail transfer, the full-shell transverse exponent becomes

```text
1/2+(47/128)*(16/33)=179/264.                       (0.3)
```

The previous `45/66` is `180/264`, so the gain at the transverse level is
exactly `1/264`.  This is still weaker than the four-cycle target
`D^(1+o(1))`, operator exponent `1/4`, and transverse exponent `41/66`.
None of those stronger statements is asserted.

The new ingredient is a sharp weighted theorem for colors having one fixed
short integral relation.  An invertible relation reduces to a multiplicative
band matrix; a rank-one relation reduces to the tangent hyperbola.  Both
have `sqrt(D)` scale.  Splitting color matrices at the critical shortest-
relation length

```text
R0 asymp q/D^2=q^(1/33+o(1))=D^(1/16+o(1))         (0.4)
```

then gives (0.1).

---

## 1. Setup and prior inputs

For an oriented color matrix put

```text
C=(c11,c12;c21,c22),
w_C=(c11,-c12,-c21,c22),
Lambda_C={e in Z^4:w_C dot e=0}.                    (1.1)
```

In the all-distinct actual shell, the four prime powers have distinct prime
bases and are pairwise coprime.  Hence `w_C` is primitive and

```text
det Lambda_C=||w_C||_2 asymp q.                    (1.2)
```

Let

```text
lambda1(C)<=lambda2(C)<=lambda3(C)                 (1.3)
```

be its successive minima.  The preceding reports proved the following
facts, all used below.

1. Every realized product difference `E=M-M'` belongs to `Lambda_C` and
   has `||E||_infinity<<D`.
2. Every nonzero fixed `(C,E)` is realized by at most `q^o(1)` ordered
   completion pairs.
3. If all short differences lie in a rational rank-two plane, the product
   matrices lie on one plane conic.  In reduced lattice coordinates inside
   a square of side `N`, that conic has `O(N^(1/2)q^o(1))` integral points;
   reducible lines have only `O(1)` actual points.
4. Uniformly,

   ```text
   m(C)<<D^(1/2)q^o(1).                             (1.4)
   ```

5. For `||z||_2=1`, the determinant-layer divisor estimate gives

   ```text
   sum_(0<|det C|<<D) w_z(C)<<D q^o(1),
   w_z(C)=|z_c11 z_c12 z_c21 z_c22|.               (1.5)
   ```

Repeated-node and permutation sectors already have total fourth-trace mass
`O(Dq^o(1))`, so only the sector in (1.1) is considered below.

---

## 2. A product-band operator lemma

### Lemma 2.1

Let `N` be an integer, `L>=1`, and let `U,V` range over arbitrary finite
sets of nonzero integers of polynomial size in `q`.  The zero-one matrix

```text
B_(u,v)=1_(|uv-N|<=L)                               (2.1)
```

satisfies

```text
||B||_(2->2)<<sqrt(L) q^o(1).                       (2.2)
```

The same estimate holds after restricting either index to an arithmetic
progression or deleting any entries.

**Proof.**  Split `|u|,|v|` into dyadic blocks `U1,V1`.  If `|N|<=2L`, a
nonempty block has `U1*V1<<L`; its matrix norm is at most the square root of
the number of possible rows times columns, hence `O(sqrt(L))`.  If
`|N|>2L`, a nonempty block has `U1*V1 asymp |N|`.  Its maximum row and column
degrees are

```text
<<1+L/U1,                         <<1+L/V1.          (2.3)
```

The geometric mean of (2.3) is `O(sqrt(L))`: the terms
`sqrt(L/U1),sqrt(L/V1)` are at most `sqrt(L)`, and
`L/sqrt(U1*V1)<=sqrt(L)`.  The row/column Schur bound proves the assertion
on one block.  There are only `O((log q)^2)` blocks.  QED

For `N=0`, this is the familiar hyperbola operator bound.  The square-root
scale is sharp up to logarithms.

---

## 3. Fixed short color relations

For a nonzero integer matrix

```text
e=(e11,e12;e21,e22),                                (3.1)
```

define

```text
S_e(z)=sum_C w_z(C),                                (3.2)
```

where the sum is over all-distinct shell color matrices satisfying

```text
e11*c11+e22*c22-e12*c12-e21*c21=0,
|det C|<<D.                                         (3.3)
```

### Theorem 3.1 (fixed-relation square-root theorem)

If `||e||_infinity<min(S)`, then

```text
S_e(z)
 <<sqrt(D)*max(1,sqrt(|det e|))*q^o(1)||z||_2^4.   (3.4)
```

In particular, if `||e||_infinity<=R`, then

```text
S_e(z)<<R sqrt(D) q^o(1)||z||_2^4.                 (3.5)
```

#### 3.1 Invertible relation

Normalize `||z||_2=1`, write

```text
x=c11, y=c12, zeta=c21, w=c22,
H=e11*x-e12*y=e21*zeta-e22*w.                       (3.6)
```

Put

```text
g1=gcd(e11,e12),                 g2=gcd(e21,e22).
```

Within one nonempty `H` fibre, all left and right ordered color pairs have
parametrizations

```text
(x,y)=u_H+s*(e12/g1,e11/g1),
(zeta,w)=v_H+t*(e22/g2,e21/g2).                    (3.7)
```

Their determinant is

```text
k(s,t)=c*s*t+a*s+b*t+d,
c=-(det e)/(g1*g2).                                 (3.8)
```

When `det e!=0`, `c` is a nonzero integer and

```text
(c*s+b)(c*t+a)=c*k(s,t)+(a*b-c*d).                 (3.9)
```

Neither factor on the left can vanish on an all-distinct shell pair.  For
example, `c*s+b=0` is equivalent, up to the harmless `g2`, to

```text
e21*x=e22*y.                                        (3.10)
```

Since `x,y` are coprime shell prime powers, the primitive coefficient pair
in (3.10) would have size at least `min(x,y)`, contrary to
`||e||_infinity<min(S)`.  The other factor is identical.

Let

```text
alpha_(x,y)=|z_x z_y|,             beta_(zeta,w)=|z_zeta z_w|. (3.11)
```

Both pair vectors have `ell^2` norm at most one.  Fibres with different
`H` are orthogonal blocks.  In one block, (3.9) and `|k|<<D` put its
incidence matrix inside a product band of width `L<<|c|D`.  Lemma 2.1 gives

```text
||G_H||<<sqrt(|c|D)q^o(1).                          (3.12)
```

Taking the maximum over the orthogonal `H` blocks proves

```text
S_e(z)<<sqrt(D)*sqrt(|det e|/(g1*g2))*q^o(1),       (3.13)
```

which is stronger than (3.4).

#### 3.2 Rank-one relation

Suppose `det e=0`.  Factor, after removing a common scalar,

```text
e=r*s^T,
r=(r1,r2),                         s=(s1,s2),
gcd(r1,r2)=gcd(s1,s2)=1.                           (3.14)
```

If one component of `r` or `s` vanishes, (3.3) forces a rational equality
between two distinct coprime shell prime powers with coefficients smaller
than the shell minimum.  Thus the color set is empty.  We may assume all
four components are nonzero.

Choose integers `u0,v0` with

```text
s1*u0-s2*v0=1.                                      (3.15)
```

Equation (3.3) is equivalent to the existence of integers `h,p,q` such
that

```text
(x,y)=r2*h*(u0,v0)+p*(s2,s1),
(zeta,w)=r1*h*(u0,v0)+q*(s2,s1).                   (3.16)
```

The determinant factorizes exactly:

```text
det C=h*ell,                    ell=r2*q-r1*p.      (3.17)
```

For fixed `(h,ell)`, let `T_(h,ell)` be the corresponding four-weight
correlation.  Define the four pair energies

```text
P_h=sum_(s1*x-s2*y=r2*h) |z_x z_y|^2,
Q_h=sum_(s1*zeta-s2*w=r1*h) |z_zeta z_w|^2,
R_ell=sum_(r1*x-r2*zeta=-s2*ell) |z_x z_zeta|^2,
S_ell=sum_(r1*y-r2*w=-s1*ell) |z_y z_w|^2.         (3.18)
```

Each family partitions a subset of the ordered color pairs, so

```text
sum_h P_h,sum_h Q_h,sum_ell R_ell,sum_ell S_ell<=1. (3.19)
```

Cauchy--Schwarz first across rows and then across columns gives

```text
T_(h,ell)<=sqrt(P_h Q_h),
T_(h,ell)<=sqrt(R_ell S_ell),
T_(h,ell)<=(P_h Q_h R_ell S_ell)^(1/4).            (3.20)
```

The sequences

```text
a_h=(P_h Q_h)^(1/4),              b_ell=(R_ell S_ell)^(1/4) (3.21)
```

have `ell^2` norm at most one.  Equations (3.17), (3.20), and the `N=0`
case of Lemma 2.1 therefore give

```text
S_e(z)
 <=sum_(0<|h*ell|<<D) a_h b_ell
 <<sqrt(D)q^o(1).                                  (3.22)
```

This proves the rank-one case and Theorem 3.1.

The rank-one calculation is the exact rational tangent/Hankel mechanism;
it controls it by its fourth trace rather than by the false weighted
`m(C)^2` estimate.

### Corollary 3.2 (bounded-direction tangent sectors satisfy FC)

Let `mathcal R` be a set of `q^o(1)` nonzero integral relations with
entries and determinants of size `q^o(1)`.  The completed all-distinct
sector whose color matrices are killed by at least one `e in mathcal R`
satisfies

```text
sum_(C: some e in mathcal R kills C) m(C)w_z(C)
 <<D q^o(1)||z||_2^4.                              (3.23)
```

Indeed, Theorem 3.1 gives `sqrt(D)q^o(1)` uncompleted color mass per
relation, and (1.4) supplies the other `sqrt(D)`.  Thus every fixed
rational Hankel/tangent direction is already at full four-cycle strength.
Any remaining obstruction must distribute its mass over polynomially many
relation directions or relation heights; one tangent patch cannot cause it.

---

## 4. Long shortest relation: a better completion bound

Let `K0` be a fixed constant such that every realized difference has
Euclidean norm at most `K0 D`.  Choose

```text
R0=c0*q/D^2,                                         (4.1)
```

where `c0>0` is a sufficiently small fixed constant depending only on
`K0` and the fixed lattice constants.  Then

```text
R0=D^(1/16+o(1)).                                   (4.2)
```

### Proposition 4.1

If

```text
lambda1(C)>=R0,                                     (4.3)
```

then

```text
m(C)<<sqrt(D/R0) q^o(1).                            (4.4)
```

**Proof.**  There are two cases.

If

```text
lambda1*lambda2>=R0*D,                              (4.5)
```

the standard minima count and Minkowski's second theorem give

```text
#(Lambda_C intersect [-K0D,K0D]^4)
 <<product_(i=1)^3 (1+D/lambda_i)
 <<D/R0+D^3/q
 <<D/R0.                                            (4.6)
```

Indeed, every linear term is at most `D/R0`, every quadratic term is at
most `D/R0` by (4.5) and `lambda3>=lambda2`, and the cubic term is
`D^3/q=D/(q/D^2)<<D/R0`.  Fixed-`(C,E)` multiplicity is `q^o(1)`, so (4.6)
implies `m(C)(m(C)-1)<<D/R0*q^o(1)`.

If instead

```text
lambda1*lambda2<R0*D,                               (4.7)
```

then

```text
lambda3>>q/(R0D)>2K0D                              (4.8)
```

by the choice of `c0`.  Hence all realized differences lie in one rational
rank-two plane.  In a reduced basis of that plane, (4.3) and the length-
`D` product box put both integral coordinates in a square of side
`O(D/R0)`.  The plane-conic theorem gives at most
`(D/R0)^(1/2)q^o(1)` product matrices; reducible lines are smaller.  This
again proves (4.4).  QED

---

## 5. Short shortest relation: weighted union bound

Let `mathcal C_short` be the color matrices with `lambda1(C)<R0`.  Each has
a nonzero integer vector `e in Lambda_C` with `||e||_infinity<R0`.
There are `O(R0^4)` possible vectors.  Theorem 3.1 and a union bound give

```text
sum_(C in mathcal C_short) w_z(C)
 <<R0^4*(R0 sqrt(D))*q^o(1)
 =R0^5 sqrt(D) q^o(1).                              (5.1)
```

Using the already proved uniform `m(C)<<sqrt(D)q^o(1)`, their completed
four-cycle contribution is

```text
Q_short
 <<D*R0^5*q^o(1)
 =D^(21/16+o(1)).                                   (5.2)
```

This is far below the eventual dominant term.

For the complementary long-relation colors, Proposition 4.1 and (1.5)
give

```text
Q_long
 <<sqrt(D/R0)*D*q^o(1)
 =D^(3/2)*R0^(-1/2)*q^o(1)
 =D^(47/32+o(1)).                                   (5.3)
```

Equations (5.2)--(5.3), together with the previously closed repeated and
permutation sectors, prove (0.1).

---

## 6. Operator and transverse consequences

The exact fourth trace obeys

```text
||A_z||_op^4
 <=tr((A_z^*A_z)^2)
 <=2D||z||_2^4+|Q_nd(z)|.                           (6.1)
```

Taking fourth roots of (0.1) proves (0.2).  The band-pass carry tensor is
smooth and contains all cubic orientations; invoking the already proved
Schwartz truncation/tail transfer, the generic `sqrt(Y)` leverage changes
the transverse exponent according to

```text
1/2+theta*(2-A),
theta=47/128,                 A=50/33.              (6.2)
```

This is (0.3):

```text
1/2+(47/128)*(16/33)=179/264.                       (6.3)
```

The argument reaches a natural elementary threshold at `R0=q/D^2`.
Taking a larger relation cutoff would make the third lattice minimum in
(4.8) enter the length-`D` box.  Improving (0.1) further by this route
requires either a local rank-two cover beyond that threshold or a stronger
weighted treatment of the resulting rank-three secants.

```text
fixed-relation weighted sqrt(D) theorem:            PROVED;
bounded-direction tangent sectors satisfy FC:       PROVED;
lambda1>=q/D^2 completion saving:                   PROVED;
absolute fourth trace D^(47/32+o):                  PROVED;
carry operator D^(47/128+o):                        PROVED;
transverse exponent 179/264 via smooth transfer:    PROVED;
full four-cycle D^(1+o):                            OPEN;
quarter-power operator / 41/66:                     OPEN;
QP or uniform strip:                                NOT CLAIMED.
```
