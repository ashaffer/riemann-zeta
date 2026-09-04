# QP four-cycle `4/11` theorem: hostile audit

**Date:** 2026-08-15  
**Audited artifact:**
`ZETA23-QP-FOUR-CYCLE-FOUR-ELEVENTHS-OPERATOR-AND-491-726-TRANSVERSE-THEOREM-2026-08-15.md`  
**Binary verdict:** **PASS**, conditional on the earlier fixed-relation,
fixed-`(C,E)`, and smooth-transfer inputs explicitly inherited there.

The theorem proves

```text
|Q_nd(z)| << D^(16/11+o(1)) ||z||_2^4,
||A_z||_op << D^(4/11+o(1)) ||z||_2,
transverse exponent = 491/726.
```

It does not prove the full `D^(1+o(1))` four-cycle bound.

## 1. Universal broad-slice lemma

The determinant polar form is nondegenerate on the full matrix space.  If
`K=(c11,-c12;-c21,c22)` and `N=adj(K)^T`, then

```text
B(N,E)=w_C dot E,             B(N,N)=2 det C!=0.
```

Thus its restriction to the three-dimensional common-level lattice is
nondegenerate.  For a reduced basis `v1,v2,v3`, the infinity discriminant

```text
delta(t)=disc(det(x v1+y(v2+t v3)))
```

is a nonzero polynomial of degree at most two.  Some `t in {0,1,2}` therefore
makes the binary restriction nondegenerate.  The basis shear is unimodular,
and its third coordinate is `s=n3-t*n2`; consequently it has only
`O(1+D/lambda2)` values, even if `v2+t v3` has `lambda3` size.

For fixed `s`, completing squares gives a binary norm equation with
polynomial-size data and congruence restrictions.  A nonzero right side has
`q^o(1)` points by ideal divisors and the `O(log q)` unit powers in a
polynomial box.  A zero right side either leaves only the origin or gives
lines.  Each rational line contains at most one actual completion because
any difference along it has determinant zero.  This proves

```text
m(C) << (1+D/lambda2(C))q^o(1).
```

The former cubic lattice-volume term is therefore genuinely absent.

## 2. Middle degenerate slices

In the middle range there are

```text
K << 1+R/Rcrit
```

parallel third-coordinate slices.  If the common binary quadratic part is
degenerate, all slices have the same primitive rank-one direction `e` of
height `h`.  The quadratic-congruence root set on each slice has a
`q^o(1)` arithmetic-progression cover.  Reparametrizing a progression makes
the product matrix integer-valued quadratic, so its second difference is an
integral nonzero multiple of `e`.  There is no hidden denominator loss, and

```text
m_e(C) << K(1+sqrt(D/h))q^o(1).
```

Splitting this total multi-slice multiplicity at `M`, rather than splitting
the slices separately, gives

```text
Q_low  << M D,
Q_high << D^(5/2) K^4 M^(-3).
```

The optimizer `M=D^(3/8)K` yields `D^(11/8)K`.  With
`R=D^(1/11)` and `Rcrit=D^(1/16)`, the nondegenerate and degenerate middle
exponents are respectively `181/176` and `247/176`, both below `16/11`.

## 3. Global partition and transfer

For `lambda1<R`, the `O(R^4)` relation union and the coefficient-sensitive
fixed-relation theorem give `D R^5`.  For
`lambda1>=R, lambda1*lambda2>=RD`, the universal slice lemma gives
`D^(3/2)R^(-1/2)`.  These balance at `R=D^(1/11)`, both equal to
`D^(16/11)`.  The middle branch is smaller by Section 2.

Taking a fourth root gives `4/11`.  The established transverse transfer is

```text
1/2+(4/11)*(16/33)=491/726.
```

```text
universal broad slice:                 PASS;
middle degenerate multi-slice sum:     PASS;
short/broad/middle partition:          PASS;
operator and transverse exponents:     PASS;
full four-cycle bound:                 NOT CLAIMED.
```

The finite discriminant, shear, parabolic-height, and exponent ledgers are
replayed in `src/qp_four_cycle_parabolic_height.py` and its tests.
