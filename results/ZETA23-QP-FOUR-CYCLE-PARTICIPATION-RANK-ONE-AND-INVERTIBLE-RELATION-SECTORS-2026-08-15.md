# QP four-cycle: participation gains on short-relation sectors

**Date:** 2026-08-15  
**Verdict:** participation ratio gives a genuine extra saving on the
rank-one (rational tangent) part of the short-relation sector.  If

```text
||z||_2=1,                    M_4=(sum_c |z_c|^4)^(-1),
```

then one fixed primitive rank-one color relation has uncompleted color mass

```text
S_e(z)<<min(sqrt(D),D/M_4)q^o(1).                  (0.1)
```

Consequently the union of all primitive rank-one relations of height at most
`R` has completed all-distinct four-cycle mass

```text
Q_rank1(R;z)
 <<R^2 sqrt(D)*min(sqrt(D),D/M_4)q^o(1).           (0.2)
```

In particular this sector satisfies the literal four-cycle bound when

```text
M_4>=R^2 sqrt(D)q^o(1).                            (0.3)
```

At the critical relation height

```text
R_0=q/D^2=q^(1/33+o(1))=D^(1/16+o(1)),            (0.4)
```

condition (0.3) is

```text
M_4>=D^(5/8+o(1))=q^(10/33+o(1)).                 (0.5)
```

This lies strictly inside the previously unresolved participation window
`q^(8/33)<M_4<q^(8/11)`.  It is a theorem for the stated rank-one sector,
not for the full four-cycle sum.

There is also an exact participation refinement for an invertible relation.
Writing

```text
r=||e||_infinity,
c=|det e|/(gcd(e11,e12)gcd(e21,e22)),
```

one has

```text
S_e(z)
 <<min(sqrt(cD), (rq)^(1/2)(cD)^(3/4)/M_4)q^o(1). (0.6)
```

Thus a fixed bounded invertible relation also satisfies the completed
four-cycle bound once

```text
M_4>=q^(1/2)D^(1/4)q^o(1)=q^(41/66+o(1)).         (0.7)
```

However, unioning (0.6) over all `O(R_0^4)` invertible relation directions
requires

```text
M_4>=R_0^6 q^(1/2)D^(1/4)q^o(1)
    =q^(53/66+o(1)),                               (0.8)
```

which is above `q^(8/11)=q^(48/66)`.  Therefore this coefficient refinement
does not close the full short-relation sector in the requested window and
does not improve the global `D^(47/128)` operator theorem.  A direct-sum
example at the end shows why the product-band norm plus pair `ell^4`
information alone cannot remove this loss.

---

## 1. Setup and inherited inputs

For an oriented all-distinct color matrix

```text
C=(x,y;zeta,w),                   w_C=(x,-y,-zeta,w),
```

put

```text
w_z(C)=|z_x z_y z_zeta z_w|.
```

For a nonzero integral relation matrix `e`, let

```text
S_e(z)=sum_(w_C dot e=0, 0<|det C|<<D) w_z(C).     (1.1)
```

The preceding short-relation theorem proved, uniformly in every color,

```text
m(C)<<sqrt(D)q^o(1),                               (1.2)
```

where `m(C)` is its number of product-matrix completions.  It also gave the
two exact fixed-relation parametrizations used below:

* if `det e=0`, then `det C=h*ell`;
* if `det e!=0`, then on each common linear level `H`,

  ```text
  (cs+b)(ct+a)=c det(C)+N_H.                       (1.3)
  ```

The factors on the left of (1.3) are nonzero on the actual all-distinct
prime-power shell.  All relation heights considered below are smaller than
the shell minimum, as required for that exclusion.

---

## 2. A capped hyperbola lemma

### Lemma 2.1

Let `a_h,b_ell` be nonnegative finitely supported sequences with

```text
||a||_2,||b||_2<=1,
||a||_infinity,||b||_infinity<=M^(-1/2).           (2.1)
```

For `D,M>=1`,

```text
sum_(0<|h*ell|<=D) a_h b_ell
 <<min(sqrt(D),D/M)q^o(1).                         (2.2)
```

Here and below `q^o(1)` absorbs the logarithmic number of dyadic blocks and
harmless fixed changes in the product cutoff.

**Proof.**  Restrict to `|h|asymp H`, `|ell|asymp L`, with `HL<<D`.
On such a block,

```text
sum a_h<=min(sqrt(H),H/sqrt(M)),
sum b_ell<=min(sqrt(L),L/sqrt(M)).                  (2.3)
```

Their product is at most `sqrt(D)`.  If `M>=sqrt(D)`, it is also at most
`D/M`: when both `H,L<=M` this is immediate from `HL/M`; if, say, `H>M`,
then `L<=D/H<M` and

```text
sqrt(H)*L/sqrt(M)<=D/sqrt(HM)<=D/M.                (2.4)
```

The case `L>M` is symmetric.  Summing the dyadic blocks proves (2.2).
QED

---

## 3. Rank-one relations

Write a primitive rank-one relation as

```text
e=r_vec*s_vec^T,
r_vec=(r1,r2),                    s_vec=(s1,s2),
```

with both two-vectors primitive.  The exact tangent parametrization from the
short-relation theorem gives

```text
det C=h*ell.                                        (3.1)
```

For each `h,ell`, define pair energies

```text
P_h=sum_(s1*x-s2*y=r2*h) |z_x z_y|^2,
Q_h=sum_(s1*zeta-s2*w=r1*h) |z_zeta z_w|^2,
R_ell=sum_(r1*x-r2*zeta=-s2*ell) |z_x z_zeta|^2,
T_ell=sum_(r1*y-r2*w=-s1*ell) |z_y z_w|^2.         (3.2)
```

Two Cauchy--Schwarz inequalities give the fixed-cell four-weight bound

```text
W_(h,ell)<=(P_h Q_h R_ell T_ell)^(1/4).            (3.3)
```

Put

```text
a_h=(P_hQ_h)^(1/4),              b_ell=(R_ellT_ell)^(1/4).
```

As before, the four energy families each have total mass at most one, so

```text
||a||_2,||b||_2<=1.                                (3.4)
```

The new observation is the pointwise participation cap.  Each equation in
(3.2) is a matching between its two color coordinates.  Hence, by
Cauchy--Schwarz,

```text
P_h,Q_h,R_ell,T_ell
 <=sum_c |z_c|^4=1/M_4.                            (3.5)
```

Therefore

```text
||a||_infinity,||b||_infinity<=M_4^(-1/2).         (3.6)
```

Equations (3.1), (3.3), and Lemma 2.1 prove (0.1).

### Counting rank-one directions

Scalar multiples define the same color hyperplane, so retain only primitive
relation matrices.  A primitive rank-one integer matrix factors, uniquely up
to a simultaneous sign, as `r_vec*s_vec^T` with both factors primitive.  If
`||r_vec||_infinity=t`, then there are `O(t)` possible primitive `r_vec`, and
there are `O((R/t)^2)` possible `s_vec` with
`||r_vec*s_vec^T||_infinity<=R`.  Thus

```text
# {primitive rank-one directions of height <=R}
 <<sum_(t<=R) t*(R/t)^2
 <<R^2 log(2R)=R^2q^o(1).                          (3.7)
```

Multiplying the union bound obtained from (0.1) and (3.7) by the completion
bound (1.2) proves (0.2).  For `M_4>=sqrt(D)`, its right side is

```text
R^2 D^(3/2)/M_4*q^o(1),                            (3.8)
```

which is `O(Dq^o(1))` under (0.3).  Substitution of (0.4) gives (0.5).

---

## 4. An `ell^4` product-band theorem for invertible relations

Suppose `det e!=0`, set

```text
g1=gcd(e11,e12),                  g2=gcd(e21,e22),
c=|det e|/(g1g2)>=1,              r=||e||_infinity. (4.1)
```

The common level

```text
H=e11*x-e12*y=e21*zeta-e22*w                     (4.2)
```

ranges over at most

```text
B_e<<rq                                               (4.3)
```

integers because all colors lie in a fixed compact interval of size
`asymp q`.

Let `alpha` be the vector indexed by all left color pairs, with coordinate
`|z_xz_y|`, and let `beta` be its right-pair analogue.  Each pair belongs to
exactly one `H` block.  Consequently

```text
||alpha||_4^4<= (sum_x |z_x|^4)(sum_y |z_y|^4)=M_4^(-2),
||beta||_4^4 <=M_4^(-2).                            (4.4)
```

On one `H` block, (1.3) embeds the determinant condition in

```text
|u*v-N_H|<<cD,                     u,v!=0.           (4.5)
```

Put `L=O(cD)`.  Split `u,v` dyadically.  In one dyadic rectangle, the maximum
row and column degrees `d_1,d_2` satisfy

```text
d_1*d_2<<L.                                         (4.6)
```

Indeed, if `|N_H|<=2L`, nonemptiness gives `UV<<L` and the two degrees are
bounded by `min(V,1+L/U)` and `min(U,1+L/V)`.  If `|N_H|>2L`, then
`UV asymp |N_H|` and the degrees are at most `1+L/U`, `1+L/V`; their product
is again `O(L)`.

There are only `Lq^o(1)` edges in the rectangle for each `H`: for every
nonzero integer in the length-`O(L)` product interval, the number of factor
pairs is `q^o(1)`.  Across all `H`, the direct-sum rectangle therefore has

```text
E<<B_e Lq^o(1)                                      (4.7)
```

edges.  Its operator norms obey

```text
||G||_(2->2)<<L^(1/2),              ||G||_(infinity->1)<=E. (4.8)
```

Riesz--Thorin interpolation at parameter `1/2` gives

```text
||G||_(4->4/3)
 <<L^(1/4)E^(1/2)
 <<B_e^(1/2)L^(3/4)q^o(1).                         (4.9)
```

Apply (4.9) to (4.4), sum the logarithmically many dyadic rectangles, and
combine with the old `ell^2` product-band estimate.  This proves

```text
S_e(z)
 <<min((cD)^(1/2), B_e^(1/2)(cD)^(3/4)/M_4)q^o(1), (4.10)
```

and hence (0.6).

For a family of `T` invertible relations of height at most `R`, use
`c<=R^2`, (1.2), and a union bound to obtain

```text
Q_inv(T,R;z)
 <<T sqrt(D)*min(R sqrt(D),
                 R^2 q^(1/2)D^(3/4)/M_4)q^o(1).   (4.11)
```

The participation branch in (4.11) is at four-cycle strength if

```text
M_4>=T R^2 q^(1/2)D^(1/4)q^o(1).                  (4.12)
```

For one bounded relation this is (0.7).  There are `O(R^4)` primitive
invertible relation directions of height at most `R`; taking `T=R^4` and
`R=R_0` gives (0.8).

---

## 5. Why the invertible cap does not automatically become `D/M_4`

The loss in (4.9) is intrinsic to the information used there.  Let
`K>=1`, `T>=1`, and take a direct sum of `T` copies of the all-one `K` by
`K` matrix.  Each copy is contained in the product band

```text
0<|u*v|<=K^2,                    1<=u,v<=K.          (5.1)
```

Put `N=TK` and take both input vectors to be constant `N^(-1/2)` on their
`N` coordinates.  Then

```text
||alpha||_2=||beta||_2=1,
||alpha||_4^4=||beta||_4^4=1/N,
<alpha,G beta>=K.                                    (5.2)
```

If `N=M_4^2`, (5.2) has exactly the pair-vector fourth-moment scale in
(4.4), while

```text
<alpha,G beta>=K=sqrt(K^2).                          (5.3)
```

Thus arbitrarily large pair participation can coexist with saturation of
the square-root product-band norm by distributing mass over sufficiently
many orthogonal `H` blocks.  Formula (4.9) detects the only obstruction
visible to this model: with at most `B_e` blocks, saturation remains possible
whenever `M_4^2<=B_e sqrt(cD)`.

This is an operator-model barrier, not an actual-prime counterexample.  It
shows that an improvement beyond (0.6) must use compatibility among the
different `H` fibres coming from the single underlying color vector or new
prime-power arithmetic.  The product-band norm and participation data alone
do not supply it.

```text
capped hyperbola lemma:                              PROVED;
fixed rank-one relation bound (0.1):                 PROVED;
all rank-one directions <=R0 satisfy FC for
  M_4>=q^(10/33+o(1)):                               PROVED;
fixed invertible relation refinement (0.6):          PROVED;
fixed bounded invertible sector FC for
  M_4>=q^(41/66+o(1)):                               PROVED;
all invertible directions <=R0 closed in the
  window q^(8/33)<M_4<q^(8/11):                     NO;
full short-relation sector in that window:           OPEN;
full four-cycle bound:                               OPEN.
```
