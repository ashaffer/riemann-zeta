# QP four-cycle: multilevel tangent-reuse obstruction

**Date:** 2026-08-15  
**Verdict:** a literal full-integer product-window construction has `Theta(D)`
exceptional tangent clusters, all in primitive direction `(1,-1)`, while one
color is reused by every cluster.  Flat normalized color weights give global
off-diagonal completion energy `Theta(D)`, but the correct spiked unit vector
gives

```text
P=Theta(D^(5/4)).                                  (0.1)
```

Consequently the proposed global estimate `P<<D q^o(1)` is false for the
pair-unique full-integer shell, not merely inaccessible by a bounded-reuse
proof.  This is **not** a counterexample to the actual QP four-cycle bound:
the construction uses general integers rather than actual prime powers.
It proves that prime-power arithmetic is essential in the exceptional
branch.

---

## 1. Construction

Let `L>=2`, let `m>100000 L^2`, and put

```text
q=2m,                    D=2048 L^2.               (1.1)
```

For

```text
h,l in {L,...,2L},       h!=l,
t in {20L,...,21L},
i,j in {0,1},
```

define

```text
a_i=m+i h+t,
b_j=m+j l-t,
c_ij=m-i h-j l.                                  (1.2)
```

For each ordered pair `(h,l)`, the matrix

```text
C(h,l)=(m,m-l;m-h,m-h-l)                          (1.3)
```

is fixed while `t` supplies `L+1` distinct completions.  Increasing `t` by
one translates both row carriers by `+1` and both column carriers by `-1`.
Thus every fixed-`C` family is a primitive `(1,-1)` tangent cluster.

All eight labels displayed by one rectangle are distinct.  The row labels
lie above `m` by `20L` to `23L`, the column labels lie below `m` by `18L` to
`21L`, and the four colors lie from `m-4L` through `m`; within the colors,
`h!=l` removes the only possible equality.

Moreover,

```text
a_i+b_j+c_ij=3m.                                  (1.4)
```

Hence the resulting full-integer unordered triple system is linear: any two
labels in one triple determine the third.  In particular this obstruction
does use genuine completion incidence and not merely a collection of
uncompleted color matrices.

---

## 2. Literal product window

First put

```text
x=i h,       y=j l,       S=x+y,
R=xy+t(y-x)-t^2.                                  (2.1)
```

Direct expansion gives the exact first-order cancellation

```text
(m+x+t)(m+y-t)(m-x-y)-m^3
  =m(R-S^2)-SR.                                   (2.2)
```

In the stated ranges,

```text
|S|<=4L,      |R|<=487L^2,
|R-S^2|<=503L^2,      |SR|<=1948L^3.              (2.3)
```

Since `q^3=8m^3`, equations (2.2)--(2.3) give

```text
|8 a_i b_j c_ij-q^3|/q
 <=2012L^2+7792L^3/m
 <2048L^2=D.                                      (2.4)
```

Thus every displayed triple satisfies the literal active window

```text
|8abc-q^3|<qD,                                    (2.5)
```

with no hidden enlargement of `D`.  Taking
`L=q^(8/33+o(1))/sqrt(2048)` places (1.1) at the project scale
`D=q^(16/33+o(1))`; the condition on `m` is then automatic.

---

## 3. Exceptional successive-minima branch

For the signed normal of (1.3),

```text
w=(m,-(m-l),-(m-h),m-h-l),                        (3.1)
```

the two independent integral vectors

```text
e0=(1,1,1,1),
e1=(-h,-h-l,0,-l)                                 (3.2)
```

satisfy `w dot e0=w dot e1=0`.  Consequently

```text
lambda_1(C) lambda_2(C)<=10L<D.                   (3.3)
```

Every matrix in the construction therefore lies in the exceptional
two-short-direction branch of the common-level lattice dichotomy.

---

## 4. Exact global weighted count

There are

```text
# fixed-color tangent clusters =L(L+1),
# completions in each cluster  =L+1.               (4.1)
```

The color matrices are distinct because `(h,l)` can be recovered from
`C(h,l)`.  Their combined color support is exactly

```text
{m} union {m-s:L<=s<=4L-1},
```

of size `3L+1`.  In particular the color `m=c_11` occurs in every one of the
`L(L+1)=Theta(D)` clusters.

Put

```text
z_c=(3L+1)^(-1/2)
```

on this support and zero elsewhere, so `||z||_2=1`.  If `m(C)` denotes the
number of exhibited completions of `C`, the ordered off-diagonal energy is

```text
P=sum_C m(C)(m(C)-1)
       |z_c11 z_c12 z_c21 z_c22|

 =L^2(L+1)^2/(3L+1)^2
 =(1/18432+o(1))D.                                (4.2)
```

This simultaneously proves two facts:

1. fixed-color tangent clusters can have polynomial, indeed `Theta(D)`,
   color reuse even in a linear full-integer carry hypergraph satisfying the
   exact product window;
2. flat weights conceal the possible concentration on the shared color.

Indeed, use the unit vector

```text
z_m=1/2,
z_c=1/(2 sqrt(L))       for the other 3L colors.    (4.3)
```

Its squared norm is `1/4+3L/(4L)=1`.  Every matrix `C(h,l)` contains the
anchor `m` and three non-anchor colors, so its weight is exactly

```text
|z_c11 z_c12 z_c21 z_c22|=1/(16L^(3/2)).           (4.4)
```

Therefore

```text
P=L^2(L+1)^2/(16L^(3/2))
  =L^(1/2)(L+1)^2/16
  =Theta(L^(5/2))=Theta(D^(5/4)).                  (4.5)
```

At the project scaling this exceeds `D q^o(1)` by the polynomial factor
`q^(4/33-o(1))`.  The same lower bound survives quotienting transpose or
orientation symmetries, since restricting to (say) `h<l` only changes a
fixed constant.

Thus no overlap-sensitive convolution or Brascamp--Lieb theorem based only
on linearity, shell geometry, and the four product windows can prove the
target global pair-energy estimate.  Any valid exceptional-branch theorem
must use an arithmetic property absent from this integer model, most
naturally simultaneous prime-power support.

---

## 5. Scope

```text
literal qD product window:                         PROVED;
pair-unique full-integer completion incidence:     PROVED;
all displayed labels distinct:                     PROVED;
exceptional lambda1*lambda2<D:                     PROVED;
Theta(D) tangent-cluster color reuse:               PROVED;
flat normalized off-diagonal energy Theta(D):      PROVED;
spiked unit-vector energy Theta(D^(5/4)):           PROVED;
full-integer global P<<D q^o theorem:                FALSE;
actual prime-power realization:                    NOT CLAIMED;
counterexample to the actual QP four-cycle bound:   NO;
global weighted exceptional-branch theorem:         OPEN.
```

The identities and finite ledger are replayed by
`src/qp_multilevel_translation_grid.py` and
`src/test_qp_multilevel_translation_grid.py`.
