# QP four-cycle: hostile audit of the global `11/32` operator theorem

**Date:** 2026-08-15  
**Verdict:** **PASS.**  The all-distinct completed four-cycle mass satisfies

```text
Q_nd(z)<<D^(11/8)q^o(1)||z||_2^4,                  (0.1)
```

and therefore the carry operator has exponent `11/32`; the inherited
smooth transfer gives transverse exponent `2/3`.  The proof does not claim
the four-cycle target `D^(1+o(1))`, QP, or a uniform strip.

## 1. Exact split

Put

```text
P=lambda1*lambda2,
K=1+D/lambda3 << 1+D*P/q.                          (1.1)
```

The reduced-basis slice dichotomy gives, for a fixed color:

* if `det|span(v1,v2)` is nondegenerate, `m(C)<<Kq^o(1)`;
* if it vanishes identically, each slice has at most one actual point, so
  the same bound holds;
* if it is a nonzero square, its primitive repeated direction `e` has
  height `h>=c lambda1`, and

  ```text
  m(C)<<K(1+sqrt(D/h))q^o(1).                       (1.2)
  ```

The factor `K` counts the third-coordinate slices.  Formula (1.2) is
pointwise; no cross-color aggregation is assumed in the high branch.

## 2. Low `P`

If

```text
P<=q/D=D^(17/16+o(1)),                              (2.1)
```

then `K=O(1)`.  Nondegenerate and identically-zero restrictions cost only
the determinant-layer mass `Dq^o(1)`.  The proved common-direction height
sum for the degenerate restriction costs

```text
D^(11/8)q^o(1).                                    (2.2)
```

That height sum does not require a lower bound on `lambda1`: low chart
multiplicity uses the total determinant-layer mass, while high charts have
height at most `D^(1/4)` after optimization and are covered by the fixed
rank-one-relation theorem.

## 3. High `P`

Assume `P>=q/D`.

If `lambda2>=D^(5/8)`, the universal nonparabolic shear theorem gives

```text
m(C)<<1+D/lambda2<<D^(3/8).                         (3.1)
```

Now suppose `lambda2<D^(5/8)`.  Since `lambda1<=lambda2`,

```text
K<<1+D*lambda2^2/q<<D^(3/16),                      (3.2)
```

and the nondegenerate/identically-zero cases are smaller than required.
For the degenerate case, the `+1` in both (1.1) and (1.2) must be retained.
The product part obeys

```text
(D*P/q)*sqrt(D/lambda1)
 =D^(3/2)*sqrt(lambda1)*lambda2/q
 <=D^(3/2)*lambda2^(3/2)/q
 <=D^(3/8).                                        (3.3)
```

The bare curvature term is also safe.  From `P>=q/D` and
`lambda2<D^(5/8)`,

```text
lambda1>D^(7/16),
sqrt(D/lambda1)<D^(9/32)<D^(3/8).                  (3.4)
```

Finally the bare slice term `K` is at most `D^(3/16)`.  Thus every high-`P`
color satisfies `m(C)<<D^(3/8)q^o(1)`.  Multiplication by the global color
mass `Dq^o(1)` gives (0.1).

## 4. Scope checks

The argument is for the oriented all-distinct sector, where every nonzero
same-color completion difference has nonzero determinant.  That fact is
used to bound rational line components of a slice.  Repeated-node,
permutation, square-edge, and opposite-color-equality sectors were proved
separately at `O(Dq^o(1))` and are therefore below (0.1).  Schwartz tails
and the smooth band-pass transfer are inherited separately; they are not
silently folded into the finite all-distinct count.

```text
low-P degenerate height sum D^(11/8):               PASS;
high-P pointwise multiplicity D^(3/8):              PASS;
bare +1 terms in K and curvature count:             PASS;
repeated/permutation sector coverage:               PASS (separate theorem);
global all-distinct trace D^(11/8):                  PROVED;
operator exponent 11/32, transverse exponent 2/3:   PROVED;
four-cycle target D^(1+o), QP, uniform strip:        OPEN.
```
