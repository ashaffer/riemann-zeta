# QP four-cycle: `21/64` operator and `29/44` transverse theorem

**Date:** 2026-08-17  
**Verdict:** the parabolic gap-token aggregation theorem improves the full
all-distinct fourth trace to

```text
Q_nd(z)<<D^(21/16)q^o(1)||z||_2^4.                (0.1)
```

Together with the separately closed repeated-node and permutation sectors,

```text
||A_z||_op<<D^(21/64)q^o(1)||z||_2,               (0.2)
```

and the established smooth transfer gives transverse exponent

```text
1/2+(21/64)*(16/33)=29/44.                        (0.3)
```

This supersedes the previous `11/32` operator and `2/3` transverse theorem.
It does not prove the literal four-cycle bound `D^(1+o(1))`, QP, or a
uniform strip.

**Subsequent coefficient-profile refinement (2026-08-22).**  The
three-coordinate matching structure of the determinant band gives
`sum_C w_z(C)<=||z||_(4/3)^4`.  Combined with the pointwise and parabolic
multiplicity theorems, this proves the sharp `D` four-cycle bound whenever
`||z||_(4/3)^4/||z||_2^4<=sqrt(D)`, and a strict exponent improvement
through effective support `D^(1-o(1))`.  See
`ZETA23-QP-FOUR-CYCLE-L43-PARTICIPATION-PROFILE-2026-08-22.md`.  The
arbitrary-coefficient exponent in this report remains the uniform endpoint.

---

## 1. Inputs

For a fixed all-distinct color matrix, let

```text
lambda1<=lambda2<=lambda3,
P=lambda1*lambda2,
K_C=1+D/lambda3<<1+D*P/q.                         (1.1)
```

Minkowski and ordering give

```text
lambda1*lambda2*lambda3~q,
P<=q^(2/3)=D^(11/8+o(1)).                         (1.2)
```

Therefore

```text
K_C<<1+D^(1+11/8-33/16)=D^(5/16+o(1)).           (1.3)
```

The binary slice dichotomy gives three cases:

* a nondegenerate restriction has `m(C)<<K_C q^o(1)`;
* an identically-zero restriction has at most one actual completion per
  slice, hence the same estimate;
* a nonzero degenerate restriction has one assigned primitive rank-one
  direction `e_C`, common to all slices, and

  ```text
  m(C)<<K_C*(1+sqrt(D/h_C))q^o(1).                 (1.4)
  ```

The determinant-layer color mass is

```text
sum_C w_z(C)<<Dq^o(1)||z||_2^4.                   (1.5)
```

The new gap-token theorem gives, for every dyadic `H<=D`,

```text
sum_(C assigned, h_C~H) w_z(C)
 <<sqrt(DH)q^o(1)||z||_2^4.                       (1.6)
```

---

## 2. Every slice type costs at most `K_max*D`

The nondegenerate and identically-zero cases follow immediately from
(1.3), (1.5):

```text
Q_ndeg+Q_zero<<D^(5/16)*D*q^o(1).                 (2.1)
```

For a degenerate dyadic block `h_C~H<=D`, equations (1.4) and (1.6) give

```text
sum_C m(C)w_z(C)
 <<K_max*(1+sqrt(D/H))*sqrt(DH)q^o(1)
 <<K_max*(sqrt(DH)+D)q^o(1)
 <<K_max*Dq^o(1).                                 (2.2)
```

If `H>D`, the square-root term in (1.4) is `O(1)`, and (1.5) gives the same
bound.  Degenerate directions with a zero component cannot support a
nonconstant active parabolic chart; their bounded-per-slice remnants are
also covered by `K_max*D`.  The selected binary plane assigns one common
direction to each remaining degenerate color, with only the already proved
`q^o(1)` chart multiplicity.

There are only logarithmically many dyadic height blocks.  Combining
(1.3), (2.1), and (2.2) proves (0.1).

---

## 3. Scope

Repeated-node, opposite-color-equality, square-edge, and permutation sectors
were proved separately at `Dq^o(1)`, below (0.1).  Taking the fourth root of
the absolute fourth trace gives (0.2); the band-pass and Schwartz-tail
transfer are inherited unchanged and give (0.3).

The remaining power `D^(5/16)` is exactly the worst possible third-slice
factor allowed by minima ordering.  Removing it requires weighted
orthogonality among occupied slices, a `K_C`-weighted strengthening of the
gap-token theorem, or a direct broad affine/Hankel merger.

```text
gap-token relation mass sqrt(DH):                   PROVED;
all-distinct fourth trace D^(21/16):                 PROVED;
operator exponent 21/64:                            PROVED;
transverse exponent 29/44:                          PROVED;
literal fourth-cycle D^(1+o):                       OPEN;
QP and uniform strip:                               OPEN.
```

The exact exponent identities are replayed in
`src/qp_four_cycle_twenty_one_sixty_fourths.py` and its test module.
