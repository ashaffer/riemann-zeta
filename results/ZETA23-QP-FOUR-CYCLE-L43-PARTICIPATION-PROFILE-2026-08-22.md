# QP four-cycle: the `L^(4/3)` participation-profile theorem

**Date:** 2026-08-22
**Verdict:** there is a genuine coefficient-sensitive improvement of the
four-cycle theorem.  Put

```text
R_43(z)=||z||_(4/3)^4/||z||_2^4                  (z!=0).       (0.1)
```

Then the retained QP fourth-cycle form satisfies

```text
|Q_nd(z)|
 <<q^o(1) ||z||_2^4 * [
      D
     +min(D^(5/4),  D^(1/2)*R_43(z))
     +min(D^(21/16),D^(5/16)*R_43(z))].             (0.2)
```

In particular,

```text
R_43(z)<=D^(1/2)
  ==> |Q_nd(z)|<<D q^o(1)||z||_2^4.                 (0.3)
```

Thus the literal four-cycle target, the `D^(1/4)` carry-operator bound,
and (under the established uniform smooth transfer) transverse exponent
`41/66` all hold for this coefficient profile.  A vector supported on at
most `sqrt(D)` colors automatically satisfies (0.3), with no flatness
assumption.

This is not a uniform proof of FC: `R_43(z)` can be as large as the full
shell.  For `R_43(z)>=D`, (0.2) returns the existing `D^(21/16)` theorem.

---

## 1. The determinant band is a three-coordinate matching

Let `mathcal D` be the oriented all-distinct color tuples

```text
C=(c11,c12,c21,c22),       0<|c11*c22-c12*c21|<=C_0 D, (1.1)
```

where all four coordinates lie in the project shell and hence are
comparable with `q`.  For all sufficiently large `q`,

```text
2*C_0*D<min(project shell).                          (1.2)
```

Every projection of `mathcal D` onto three coordinates is injective.  For
example, if two tuples agree in `c11,c12,c21`, then

```text
|c11*(c22-c22')|<=2*C_0*D<|c11|,                   (1.3)
```

so the integer `c22-c22'` is zero.  Omitting any of the other coordinates
is identical, with another retained shell coordinate as coefficient.

For nonnegative finitely supported functions define

```text
Lambda(f1,f2,f3,f4)=sum_(C in mathcal D)
                     f1(c11)f2(c12)f3(c21)f4(c22). (1.4)
```

Injectivity after deleting coordinate `i` gives the four endpoint bounds

```text
Lambda(f1,f2,f3,f4)
 <=||f_i||_infinity * product_(j!=i)||f_j||_1.     (1.5)
```

Equal-weight multilinear interpolation of these four endpoints puts each
input at reciprocal exponent

```text
(0+1+1+1)/4=3/4.                                   (1.6)
```

Therefore

```text
Lambda(f1,f2,f3,f4)<=product_i ||f_i||_(4/3).      (1.7)
```

Taking all four functions equal to `|z|` proves the new determinant-band
mass estimate

```text
sum_(C in mathcal D) |z_c11 z_c12 z_c21 z_c22|
 <=||z||_(4/3)^4.                                  (1.8)
```

This complements the earlier arbitrary-coefficient determinant-layer
bound

```text
sum_(C in mathcal D) |z_c11 z_c12 z_c21 z_c22|
 <<D q^o(1)||z||_2^4.                              (1.9)
```

The key point is that (1.8) sums the whole determinant interval at once;
paying separately for its `O(D)` integer determinant values would erase
the participation gain.

---

## 2. Insert the two proved multiplicity theorems

Write

```text
w_z(C)=|z_c11 z_c12 z_c21 z_c22|.                 (2.1)
```

The exact all-distinct fourth-cycle coefficient is `m(C)w_z(C)`.  The
fixed-color theorem gives, for every actual color matrix,

```text
m(C)<<D^(1/2) q^o(1).                              (2.2)
```

Equations (1.8) and (2.2) imply the whole-sector estimate

```text
sum_C m(C)w_z(C)
 <<D^(1/2) q^o(1)||z||_(4/3)^4.                   (2.3)
```

The sharper geometric decomposition has two pieces.

* The determinant-content theorem gives the complete parabolic/tangent
  contribution

  ```text
  Q_par(z)<<D^(5/4)q^o(1)||z||_2^4.                (2.4)
  ```

  Combining (2.4) with the restriction of (2.3) to this subfamily gives

  ```text
  Q_par(z)
   <<min(D^(5/4)||z||_2^4,
          D^(1/2)||z||_(4/3)^4)q^o(1).             (2.5)
  ```

* On the nondegenerate and identically-zero broad pieces, the slice theorem
  gives

  ```text
  m(C)<<D^(5/16)q^o(1),                            (2.6)
  ```

  while the uniform theorem gives total exponent `21/16`.  Hence

  ```text
  Q_broad(z)
   <<min(D^(21/16)||z||_2^4,
          D^(5/16)||z||_(4/3)^4)q^o(1).            (2.7)
  ```

All repeated-node, permutation, square-edge, and opposite-color-equality
pieces are already `O(Dq^o(1)||z||_2^4)`.  Adding them to (2.5)--(2.7)
proves (0.2).

---

## 3. Exact exponent profile

Write

```text
R_43(z)=D^(mu+o(1)).                               (3.1)
```

The fourth-trace exponent supplied by (0.2) is

```text
kappa(mu)
 =max(1,
      min(5/4,  1/2+mu),
      min(21/16,5/16+mu)).                         (3.2)
```

Equivalently,

```text
kappa(mu)=
  1,             0<=mu<=1/2;
  1/2+mu,        1/2<=mu<=3/4;
  5/4,           3/4<=mu<=15/16;
  5/16+mu,       15/16<=mu<=1;
  21/16,         mu>=1.                            (3.3)
```

Taking fourth roots gives the carry-operator profile

```text
1/4;
1/8+mu/4;
5/16;
5/64+mu/4;
21/64,                                                   (3.4)
```

on the same five intervals.  If the profile is uniform for every weight
vector entering the already-established band transfer, the corresponding
transverse exponents are

```text
41/66;
(37+8*mu)/66;
43/66;
71/132+4*mu/33;
29/44.                                                   (3.5)
```

For literal support size `M`, Holder gives

```text
||z||_(4/3)<=M^(1/4)||z||_2,
R_43(z)<=M.                                          (3.6)
```

Thus (3.3) applies with `mu=log_D M` to every vector on that support,
regardless of how uneven its coefficients are.

---

## 4. Scope and remaining uniform endpoint

The theorem removes the entire low-participation obstruction:

```text
effective support <=sqrt(D):  sharp FC D;           PROVED;
effective support <=D^(15/16): trace D^(5/4);       PROVED;
effective support <D:          strict power gain;    PROVED;
arbitrary coefficients:        trace D^(21/16);      BEST CURRENT;
uniform FC D:                   OPEN.                (4.1)
```

The unresolved vectors have `R_43(z)>=D^(1-o(1))` and can place their
determinant-band mass on balanced, broad, nondegenerate fibers with

```text
lambda1~lambda2~lambda3~D^(11/16),
K_C~D^(5/16).                                      (4.2)
```

The new interpolation does not supply a weighted tail excluding that
endpoint.  It is nevertheless an unconditional four-cycle improvement on
a polynomially large coefficient regime, rather than a conditional
slope-block statement.

A complementary top-`k` refinement proves sharp FC when the normalized
`L^2` mass outside the largest `sqrt(D)` coordinates is at most
`D^(-5/24)`.  See
`ZETA23-QP-FOUR-CYCLE-TOPK-TAIL-NONUNIFORM-REFINEMENT-2026-08-22.md`.
The flat vector on `D` colors remains outside both profile theorems.

The exact rational exponent ledger and finite projection checks are in
`src/qp_four_cycle_l43_profile.py` and
`src/test_qp_four_cycle_l43_profile.py`.

---

## 5. Chapman--Mudgal fixed determinants do not supply the weighted HSM

[Chapman--Mudgal, *Counting 2x2 integer matrices with a given
determinant*](https://arxiv.org/abs/2509.20259), Theorem 1.1, proves the
unweighted hard-box asymptotic

```text
#{(a,b,c,d) in [-N,N]^4: a*b-c*d=h}
 =16/zeta(2)*N^2*sum_(r|h)1/r
  +O_epsilon(N^epsilon*(N+h)),                    (5.1)
```

for `1<=h<=2N^2`.  Its formal scale is attractive at the balanced HSM
point.  There

```text
N=J=K=q^(42/33),       X=N^2=q^(84/33),
B_0=q^(34/33)<N,       P=Q=q^(8/33),
P*Q=D=q^(16/33),       HSM target=D*X=q^(100/33). (5.2)
```

If the centered error in (5.1) were stable under the four HSM
Dirichlet-kernel weights with their natural `L^2` density `P*Q=D`, then
absolute summation over `|h|<=B_0` would cost only

```text
B_0*D*(N+B_0)=q^(92/33),                          (5.3)
```

which lies below the HSM target by `q^(8/33)=sqrt(D)`.  This is a formal
margin, not an application of the theorem.

The required stability is absent from both the statement and the proof.
Lemma 3.1 uses the positivity of the unweighted boundary discrepancy
`tilde r-r`; the residue-class step in Section 4 counts units and their
inverses with weight one.  Inserting the four kernels turns that step into
incomplete inverse-twisted sums of Kloosterman type, and positivity no
longer controls the boundary.  Moreover, (5.1) has a genuine nonzero
`N^2` main term.  Deleting the joint coherent residue does not by itself
identify, much less cancel, the corresponding weighted singular integral.

The exact naive loss makes the missing input visible.  Expanding the four
kernels creates

```text
P^2*Q^2=D^2=q^(32/33)                             (5.4)
```

additive twists.  Even if one additionally granted an `O(N q^o(1))`
centered error uniformly for every twist--which Chapman--Mudgal do not
prove--absolute twist summation would give

```text
B_0*D^2*N=q^(108/33),                             (5.5)
```

exceeding the target by `q^(8/33)=sqrt(D)`.  A square-function saving
across those twists, together with a theorem cancelling the weighted main
term, is exactly what would be needed.  That is a new weighted shifted
multiplication-table/HSM estimate, not a corollary of (5.1).

```text
Chapman--Mudgal unweighted fixed determinant:       APPLICABLE TO (5.1);
four-kernel weighted error stability:               NOT PROVED;
weighted main-term cancellation:                    NOT PROVED;
formal q^(8/33) margin if both were granted:         VERIFIED;
absolute-twist q^(8/33) loss:                       VERIFIED;
HSM / slope-block / uniform FC closure from source: NO.
```
