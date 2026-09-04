# QP four-cycle: coarse critical-cube recombination countermodel

**Date:** 2026-08-15  
**Verdict:** critical-cube affine rank, local `O(D)` fourth trace, coarse
hyperbola/partial-permutation support, and the global color-degree cap do
**not** by themselves recombine to the global four-cycle bound.  An exact
abstract model satisfying all four properties has

```text
Q_nd=Theta(D^(3/2)).                                (0.1)
```

The obstruction is block-diagonal accumulation of affine Hankel cubes that
reuse one color cube.  It is not realized by the product shell: the new
shared-progression slope pinning theorem is precisely an arithmetic property
that excludes this repetition.  Thus a successful coarse induction must
carry that cross-cube pinning/packing information; local plane structure and
Cotlar orthogonality alone are insufficient.

---

## 1. Construction

Let the critical side be `R`, put `D=R^2`, and take

```text
K=R,                 ell=floor(R/3),
M=2ell-1<=R.                                           (1.1)
```

Use `K` disjoint row--column coarse-block pairs.  Inside block `p`, take
fine indices `0<=i,j<ell` and color the cell by

```text
c=i+j.                                                (1.2)
```

All blocks reuse the same `M` colors.  Numerically one may label the rows
and columns in block `p` by `pB+i,pB+j` and the colors by `C-i-j`; then all
triples in that cube satisfy one affine equation

```text
a+b+c=2pB+C.                                          (1.3)
```

Thus every local cube has affine rank two.  The fine triple system is
pair-unique: any two of `(row,column,color)` determine the third.  At the
coarse level the sole color cube maps row block `p` to column block `p`, so
its support is a partial permutation, stronger than the coarse-hyperbola
property.

One fine color occurs at most `ell` times per block and hence at most

```text
K ell<=R^2=D                                           (1.4)
```

times globally.  Every fine row has degree `ell<=R`.  The usual degree
resources are therefore respected.

---

## 2. Exact fourth trace

Put `z_c=M^(-1/2)` on the shared colors.  Every local matrix is the constant
`ell by ell` matrix with entry `M^(-1/2)`.  Its unique nonzero singular value
is `ell/sqrt(M)`, so

```text
tr((A_p A_p*)^2)=ell^4/M^2=Theta(R^2)=Theta(D).      (2.1)
```

The blocks have disjoint row and column supports.  Their fourth traces add
exactly, while the nondegenerate mass is

```text
Q_nd
 =K [ell(ell-1)]^2/M^2
 =Theta(R^3)=Theta(D^(3/2)).                         (2.2)
```

Thus even perfect block orthogonality does not remove the loss: it makes
the Schatten-fourth mass additive.  Any recombination principle based only
on local `O(D)` trace and coarse partial permutations must lose as much as
the number `R=sqrt(D)` of reusable coherence blocks in this resource range.

---

## 3. Positive coarse-block recombination lemma

There is nevertheless a useful positive recombination lemma.  Fix one color
cube, and split its coarse row--column support into a bounded number of
partial matchings.  Within one matching the fine matrices `A_p` have
disjoint row and column blocks, so their fourth traces add.  Put

```text
F_p^2=||A_p||_F^2.
```

If every fine color occurs at most `L` times in one local cube, the color-
block mass `s^2=sum_(c in K)|z_c|^2` gives

```text
max_p F_p^2<=L s^2.                                 (3.1)
```

If every fine color has global degree at most `D`, then

```text
sum_p F_p^2<=D s^2.                                 (3.2)
```

Consequently

```text
sum_p tr((A_p A_p*)^2)
 <=sum_p F_p^4
 <=(max_p F_p^2) sum_p F_p^2
 <=D L s^4.                                         (3.3)
```

There is no square root of the number of coarse blocks in (3.3).  For a
critical-cube plane with primitive normal `(u,v,w)`, `g=gcd(u,v)`, the local
line bound gives

```text
L<<1+R g/max(|u|,|v|).                              (3.4)
```

Thus the genuinely broad range `max(|u|,|v|)/g>=R` recombines at `O(Ds^4)`.
The countermodel has normal complexity one and `L asymp R`; it shows the
remaining factor `L` in (3.3) is sharp without cross-cube arithmetic.

---

## 4. Why this is not an arithmetic counterexample

The blocks in (1.2) share an exact color progression but place it in `R`
independent carrier cubes.  In the actual product window, the thickened
shared-progression theorem proves the opposite behavior.  Endpoint
localization, three-point curvature, and anchor quantization pin the slope
product and give for the union

```text
M_color L_color<<D q^o(1).                          (3.1)
```

Hence the actual arithmetic cannot realize (1.2) at power multiplicity.
The countermodel identifies the indispensable datum for a coarse induction:
one must propagate the slope-product pinning or an equivalent color-pair
reuse bound between different critical cubes.

```text
local affine-plane cubes:                           YES;
coarse color slice a partial permutation:           YES;
global fine-color degree at most D:                 YES;
each local fourth trace O(D):                       YES;
global fourth trace O(D):                           FALSE;
actual product-window realization:                  NOT CLAIMED;
coarse induction without cross-cube arithmetic:     IMPOSSIBLE.
```

The exact scale ledger is in
`src/qp_four_cycle_coarse_cube_countermodel.py` and its test module.
