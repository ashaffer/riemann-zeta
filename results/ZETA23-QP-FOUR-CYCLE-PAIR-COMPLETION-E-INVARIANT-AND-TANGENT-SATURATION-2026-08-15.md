# QP four-cycle: pair-completion `E` invariant and tangent saturation

**Date:** 2026-08-15  
**Verdict:** the four-cycle bound is **not proved**.  The exact
pair-completion reduction is now clean, and it passes a useful hostile test:
for every actual prime-power instance scanned, a nonzero fixed oriented
`(C,E)` has multiplicity one.  This is not yet a theorem.  In fact, fixed
`(C,E)` uniqueness is false in the full-integer shell.

The translation-grid obstruction has the opposite useful feature.  It has
`m(C) asymp sqrt(D)` completions of one color matrix, but every nonzero `E`
is distinct.  With the flat unit vector on its four colors,

```text
sum_C m(C)^2 prod_ij z_cij = m(C)^2/16 asymp D.      (0.1)
```

Thus an `O(D q^o(1))` pair-energy theorem would be sharp in exponent even in
the tangent sector.  The explicit witness gives only `0.02681 D`; it is not
a counterexample.

---

## 1. Exact oriented algebra

Fix the oriented color matrix

```text
C=(c11,c12;c21,c22)                                (1.1)
```

and an ordered carrier completion

```text
X=(a1,a2,b1,b2),
M(X)=(a1*b1,a1*b2;a2*b1,a2*b2).                    (1.2)
```

For two completions `X,X'` of the same oriented `C`, put

```text
E=M(X)-M(X').                                       (1.3)
```

Define the product level

```text
L_C(X)=c11*M11+c22*M22-c12*M12-c21*M21.            (1.4)
```

The exact residuals `rij=8 cij Mij-q^3` satisfy

```text
Sr(X)=r11+r22-r12-r21=8 L_C(X).                    (1.5)
```

Therefore, without any approximation,

```text
c11*E11+c22*E22-c12*E12-c21*E21
  =L_C(X)-L_C(X').                                  (1.6)
```

The residual-rigidity theorem proves that, for sufficiently large `q` at the
active scale, `Sr` is pinned by `C`.  In that regime (1.6) becomes the exact
common-level equation

```text
c11*E11+c22*E22-c12*E12-c21*E21=0.                 (1.7)
```

This distinction matters in finite scans: same `C` need not yet mean the
same level when the effective pinning error is larger than one.

There is a second exact identity.  Write

```text
X =(a1,a2,b1,b2),       X'=(A1,A2,B1,B2),
u=a1*A2-a2*A1,          v=b1*B2-b2*B1.             (1.8)
```

Then

```text
det(E)=-u*v.                                           (1.9)
```

Equivalently, every realized `E` has the integral matrix factorization

```text
E = [ a1 -A1 ] [ b1 b2 ].
    [ a2 -A2 ] [ B1 B2 ]                             (1.10)
```

For two completions of the same color matrix, residual subtraction also
gives

```text
|Eij| <= H/(4 min(S)) << D.                         (1.11)
```

### Lemma 1.1: a distinct actual-shell pair has `det(E) != 0`

Assume the narrow actual prime-power shell, ordered nondegenerate row and
column pairs, its multiplicative Sidon property, and

```text
2H < 8 (min S)^2.                                   (1.12)
```

If `det(E)=0`, (1.9) gives `u=0` or `v=0`.  Suppose `u=0`.  Then
`a1*A2=a2*A1`; multiplicative Sidonicity and the ordered nondegenerate pairs
force `(a1,a2)=(A1,A2)`.  The first-cell residual difference is

```text
r11-r11'=8*a1*c11*(b1-B1).                          (1.13)
```

Its left side has size at most `2H`, so (1.12) forces `b1=B1`; the second
column similarly gives `b2=B2`.  Hence `X=X'`.  The case `v=0` is symmetric.

Thus every off-diagonal actual completion pair has an invertible short
matrix `E`.  This is a rigorous classification, but it does not count the
integral factorizations (1.10).

---

## 2. Translation grids: nonzero `E` is injective

For the asymmetric integer translation grid, write

```text
a1=A+t,                  a2=A+R*ell_r+t,
b1=A-t,                  b2=A+R*ell_c-t.            (2.1)
```

For an ordered pair `t,t'`, set `d=t-t'` and `s=t+t'`.  Direct expansion
gives

```text
E11=-d*s,
E22=d*(R*(ell_c-ell_r)-s),
E22-E11=d*R*(ell_c-ell_r).                          (2.2)
```

When `ell_r != ell_c`, the last coordinate recovers `d`, and then `E11`
recovers `s`; hence `E` recovers the ordered pair `(t,t')`.  For equal steps,

```text
E12-E21=2*R*ell_r*d,                                (2.3)
```

which proves the same statement.  Consequently:

```text
nu(C,E)=1 for E!=0,       nu(C,0)=m(C).             (2.4)
```

For the exact prime-modulus/full-integer witness

```text
q=87,541,837,  D=243253.1803789248,
C=(40042793,40042695;40042688,40042590),
det(C)=-10290,            m(C)=323,                 (2.5)
```

the complete pair ledger is

```text
ordered pairs                         104329
nonzero E pairs                       104006
distinct nonzero (C,E)                104006
maximum nonzero (C,E) multiplicity         1
m(C)^2/16                           6520.5625
(m(C)^2/16)/D                         0.0268057.      (2.6)
```

Deleting the four translations with a repeated coordinate leaves 319
all-eight-distinct completions and

```text
319^2/16=6360.0625=0.0261459 D.                    (2.7)
```

The family therefore saturates the order `D`, not a larger power.

---

## 3. Actual prime-power finite ledger

The following table uses shell width `0.2`, cutoff `U=12`, and exact
oriented colors.  `multi-L` counts color matrices having more than one value
of (1.4).  `nu*` is the maximum multiplicity of a nonzero exact oriented
`(C,E)`; the D4 column first identifies simultaneous row/column/transpose
images and is only a symmetry diagnostic.

| `q` | `D` | rectangles | oriented `C` | repeated `C` | max `m(C)` | multi-L | max `nu*` | max D4 `nu*` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 25013 | 4652.98 | 1419 | 1407 | 12 | 2 | 0 | 1 | 2 |
| 50021 | 6511.25 | 3646 | 3637 | 9 | 2 | 0 | 1 | 2 |
| 100003 | 9110.37 | 6926 | 6905 | 21 | 2 | 6 | 1 | 2 |
| 200003 | 12749.31 | 16096 | 16062 | 32 | 3 | 6 | 1 | 2 |

No nonzero exact oriented `(C,E)` collision occurs in these four scans.
This is a diagnostic, not an asymptotic conclusion.

For flat `z` on every color used by every rectangle, the values of
`sum_C m(C)^2 prod z_cij` are respectively

```text
0.00636872, 0.00416437, 0.00217715, 0.00137026.     (3.1)
```

If `z` is instead flat on the union of colors occurring in a repeated
`C`, while all color matrices supported there are included, the values are

```text
0.30612245, 0.14958449, 0.08326531, 0.12000000.     (3.2)
```

All are far below the corresponding `D`; they are scale checks only.

### Finite pinning warning

At `q=100003`, one of the six multi-level oriented matrices is

```text
C=(60793,56897;56299,52691),       det(C)=-240,
X =(41341,44641,49741,53147),
X'=(48857,52757,42089,44971).                       (3.3)
```

Its two alternating residual sums are

```text
Sr=-74931360, -74930784,                            (3.4)
```

while `det(C) q^3/(c12*c21)=-74930784.3664...`.
Thus the second value is pinned but the first is 576 away.  This does not
contradict the asymptotic residual-rigidity theorem: the finite constants at
this cutoff have not made its `O(D^2/q)` error smaller than one.  It does
show why (1.7) must be invoked only after common-level pinning.

---

## 4. Fixed `(C,E)` uniqueness is false for full integers

At `q=1295`, cutoff `U=1`, in the full-integer shell there are

```text
11858 rectangles, 11177 oriented C, max m(C)=7.     (4.1)
```

The common-level matrix

```text
C=(718,714;714,710),       det(C)=-16,
E=(0,-12;12,0),            det(E)=144,
L_C=-8520                                             (4.2)
```

has four ordered realizations:

```text
(531,534,712,716) -> (534,537,708,712)
(531,534,712,716) -> (712,716,531,534)
(708,712,534,537) -> (534,537,708,712)
(708,712,534,537) -> (712,716,531,534).              (4.3)
```

Hence

```text
max_{E!=0} nu(C,E)=4                                  (4.4)
```

already in this small exact integer instance.  Prime-power rigidity, not
the rank-one algebra alone, is needed for any multiplicity-one theorem.
The flat all-color square energy is only `0.19743`, versus `D=92.28`, so
this is not an FC counterexample.

There is a second obstruction to counting all solutions of (1.7).  For

```text
C=(10009,10039;10069,10099),                         (4.5)
```

the kernel contains

```text
E(u,v)=(2v-u,3v-2u;u,v),       det E=2(u-v)^2.       (4.6)
```

Thus a box of radius `D` contains order `D^2` short kernel vectors.  These
need not be realized as differences of two rank-one product matrices.
The product-window factorization (1.10) is indispensable.

---

## 5. What remains

The exact energy decomposition is

```text
sum_C m(C)^2 w(C)=sum_{C,E} nu(C,E) w(C).            (5.1)
```

The new facts are:

1. asymptotically realized `E` lies in the short common-level hyperplane;
2. every off-diagonal actual-shell `E` is invertible;
3. the translation tangent family has injective nonzero `E` and sharp
   order-`D` total energy;
4. neither the bare hyperplane nor full-integer rank-one algebra gives the
   needed multiplicity theorem.

The smallest live target is therefore a weighted count of the **realized**
integral factorizations (1.10), using prime-power shell rigidity and the four
product windows simultaneously.  Counting all short hyperplane vectors is
provably too expensive.

---

## 6. Reproducibility

Exact identities and ledgers:

```text
src/qp_four_cycle_pair_completion.py
src/test_qp_four_cycle_pair_completion.py
```

The translation witness is replayed by:

```text
src/qp_four_cycle_translation_grid.py
src/test_qp_four_cycle_translation_grid.py
```

The tests verify (1.6), (1.9), D4/oriented separation, translation-pair
recovery, nonzero-`E` injectivity on a finite translation interval, and the
flat `m(C)^2` normalization.

