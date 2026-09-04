# QP four-cycle: top-`k`/tail nonuniform refinement

**Date:** 2026-08-22
**Verdict:** a top-`k` decomposition gives a stronger sufficient
coefficient-profile theorem, but it does not close the uniform endpoint.
Normalize `||z||_2=1`, let `z_top` contain the `k` largest coordinates,
put `z_tail=z-z_top`, and write

```text
tau_k=||z_tail||_2^2.                                (0.1)
```

Then the retained all-distinct form satisfies

```text
Q_nd(z) <<q^o(1) [
 D
 +min(D^(5/4), D^(1/2) k) + D^(5/4) tau_k^(3/2)
 +min(D^(21/16),D^(5/16)k) + D^(21/16)tau_k^(3/2)]. (0.2)
```

Consequently

```text
k<=D^(1/2),       tau_k<=D^(-5/24)
   ==> Q_nd(z)<<D q^o(1).                            (0.3)
```

Equation (0.3) is nonuniform: a flat vector on `D` colors is not covered,
and iterating the same split over dyadic levels does not change that fact.

---

## 1. Mixed determinant-band interpolation

For any fixed geometric sector, symmetrize its positive coefficient tensor
and denote the resulting four-linear form by `Lambda`.  Every projection
of the active determinant band onto three coordinates is injective.  The
four endpoint inequalities are therefore

```text
Lambda(f1,f2,f3,f4)
 <=||f_i||_infinity product_(j!=i)||f_j||_1.         (1.1)
```

Multilinear interpolation permits every reciprocal-exponent vector
`(r_1,...,r_4)` with

```text
0<=r_i<=1,        sum_i r_i=3.                       (1.2)
```

Besides the equal `L^(4/3)` endpoint, the two choices needed here are

```text
(5/6,5/6,5/6,1/2),       i.e. (6/5,6/5,6/5,2),
(1,1,1/2,1/2),           i.e. (1,1,2,2).            (1.3)
```

Since `z_top` has support at most `k` and norm at most one,

```text
||z_top||_(6/5)<=k^(1/3),
||z_top||_1<=k^(1/2),
||z_tail||_2=sqrt(tau_k).                           (1.4)
```

Thus the determinant-band mass of terms with respectively zero, one, and
two tail coordinates is bounded, up to an absolute permutation factor, by

```text
k,             k sqrt(tau_k),             k tau_k. (1.5)
```

In particular, the one- and two-tail terms do **not** vanish and are not
charged to `tau_k^(3/2)`.  Since `0<=tau_k<=1`, all three quantities in
(1.5) are `O(k)`.

For terms with at least three tail coordinates, polarize the already proved
sectorwise `L^2` diagonal estimate.  Three tail inputs cost
`tau_k^(3/2)` and four cost `tau_k^2<=tau_k^(3/2)`.  If `A` is the
pointwise determinant-band coefficient and `B` the uniform sector bound,
the whole sector is therefore

```text
O(min(B,A k)+B tau_k^(3/2)).                         (1.6)
```

This is the exact place where positivity/symmetrization and the proved
diagonal theorem are used; (1.6) is not being asserted for an arbitrary
unsigned nonsymmetric tensor.

---

## 2. Insert the proved sector bounds

For the parabolic/tangent sector the existing inputs are

```text
A_par=D^(1/2),             B_par=D^(5/4).            (2.1)
```

For the broad nondegenerate and identically-zero sectors they are

```text
A_broad=D^(5/16),          B_broad=D^(21/16).        (2.2)
```

Applying (1.6) to (2.1) and (2.2), then adding the already sharp
`O(Dq^o(1))` repeated-coordinate sectors, proves (0.2).

Write `k=D^kappa` and `tau_k=D^(-nu)`.  The resulting trace exponent is

```text
max(1,
    min(5/4,  1/2+kappa),  5/4-(3/2)nu,
    min(21/16,5/16+kappa), 21/16-(3/2)nu).           (2.3)
```

The top contribution is at most `D` when `kappa<=1/2`.  The parabolic tail
requires `nu>=1/6`, while the broad tail requires the stronger

```text
nu>=5/24.                                           (2.4)
```

This proves (0.3).

---

## 3. Exact flat-profile barrier

Let `z` be flat and `L^2`-normalized on exactly `D` colors.  Then for every
`0<=k<=D`,

```text
tau_k=1-k/D.                                        (3.1)
```

If `k<=sqrt(D)`, then `tau_k=1-o(1)`, so the broad tail term in (0.2)
remains `D^(21/16-o(1))`.  To force
`tau_k<=D^(-5/24)` one needs

```text
k>=D-D^(19/24),                                     (3.2)
```

where the top contribution has already saturated its uniform bound.  A
dyadic iteration merely partitions the identity (3.1): until almost all
`D` coordinates are promoted into the head, the union of the remaining
levels still has constant `L^2` mass.  Applying (1.6) at each level cannot
create a negative power of `D` absent from (3.1).

There is also an abstract method barrier.  A cyclic Latin four-tensor

```text
i+j+k+l=0 (mod D)                                   (3.3)
```

has every three-coordinate projection injective.  After deleting the
`O(D^2)` repeated-coordinate tuples it retains `D^3-O(D^2)` edges.  Its
flat-vector mass and its `L^2` diagonal norm are both of order `D` after
the natural normalization.  Scaling its coefficients by `D^(5/16)`
therefore saturates `D^(21/16)`.  This is a countermodel to the present
matching/interpolation method, not an embedding into the arithmetic
determinant band.

Thus top-`k`/tail splitting proves a real nonuniform theorem but supplies no
uniform gain on the flat-on-`D` profile.  Any uniform improvement needs an
arithmetic statistic beyond three-coordinate injectivity and the existing
sectorwise `L^2` bounds.

The exact fractions and finite tail checks are in
`src/qp_four_cycle_topk_tail_profile.py` and
`src/test_qp_four_cycle_topk_tail_profile.py`.
