# QP four-cycle: repeated-node and permutation-sector theorem

**Date:** 2026-08-15

**Verdict:** the complete repeated-node sector of the symmetric carry
four-cycle satisfies the requested `D q^o(1)` bound.  Consequently the
unresolved four-cycle sum may be restricted to rectangles for which

```text
a1,a2,b1,b2,c11,c12,c21,c22 are all distinct
```

and the four underlying unordered hyperedges are distinct.  This is a real
reduction, not a proof of the remaining all-distinct four-cycle bound.

---

## 1. Symmetric pair-unique setup

Let `T` be the truncated carry support

```text
|8xyz-q^3|<=H,                 H<<qD,
x,y,z in the prime-power shell S.                    (1.1)
```

Membership and the kernel weight are symmetric in `(x,y,z)`.  The truncation
is narrower than the spacing obtained after fixing two coordinates.  More
precisely, if the same pair `x,y` had two third nodes `u!=v`, subtraction
would give

```text
8*x*y*|u-v|<=2H,
```

which contradicts `2H<8(min S)^2`.  Thus every unordered two-submultiset
determines at most one third node.  Write

```text
E_ij={a_i,b_j,c_ij}                                   (1.2)
```

as an unordered multiset.  A nondegenerate rectangle has `a1!=a2` and
`b1!=b2`.

Let

```text
Delta=max_x #{ordered (y,z):{x,y,z} in T}.            (1.3)
```

For fixed `x`, the integer product `yz` lies in an interval of length
`O(D)`.  Multiplicative Sidonicity of the narrow prime-power shell gives at
most two ordered factorizations per product.  Hence

```text
Delta<<D q^o(1).                                      (1.4)
```

There is also at most one `u` for which `{u,u,x}` lies in `T`: two such roots
would give

```text
8*x*|u^2-v^2|<=2H,
```

while the left side is at least `16(min S)^2` and `H=o(q^2)`.  Denote the
maximum number of such roots by `sigma`; the actual shell has `sigma<=1`.

---

## 2. Exact multiset classification

### Lemma 2.1 (adjacent intersection)

Two adjacent cells already share their row or column.  If their unordered
hyperedges share any second node, pair uniqueness makes the hyperedges
identical.  For example,

```text
E_11=E_12  ==>  c11=b2, c12=b1,                      (2.1)
```

so `b1*c11-b2*c12=0`.  The other three orientations are identical.

### Lemma 2.2 (opposite intersection)

Suppose `E_11` and `E_22` share a node.  Unless an adjacent equality from
Lemma 2.1 is forced, one of exactly three things happens:

```text
a1=b2,                    so E_12 is a square triple;
b1=a2,                    so E_21 is a square triple;
c11=c22,                  opposite colors coincide.  (2.2)
```

Indeed, the other four possible cross-identifications share an unordered
pair with `E_12` or `E_21`; pair uniqueness then makes that adjacent
hyperedge equal to `E_11` or `E_22`.  The same statement, with the indices
switched, holds for `E_12` and `E_21`.

These two lemmas include repeated coordinates inside a cell.  Therefore:

### Theorem 2.3 (complete repeated-node trichotomy)

If any two among

```text
a1,a2,b1,b2,c11,c12,c21,c22                         (2.3)
```

are equal, then the rectangle belongs to at least one of:

1. two adjacent unordered hyperedges are identical;
2. one cell is a square hyperedge `{x,x,y}`;
3. `c11=c22` or `c12=c21`.

The statement includes all multiset edge cases.  The finite module replays
all `4,140` set partitions of the eight displayed positions, then retains
the nondegenerate pair-unique patterns.  Thus the check also includes the
case of one repeated pair and six otherwise distinct labels.

---

## 3. Weighted projection lemma

Let a family of configurations carry four color labels `(x1,x2,x3,x4)`.
Suppose the projections to `(x1,x2)` and `(x3,x4)` both have fibers of size
at most `M`.  For arbitrary complex `z`, Cauchy--Schwarz gives

```text
sum_config |z_x1 z_x2 z_x3 z_x4|
 <=[sum_config |z_x1 z_x2|^2]^(1/2)
   [sum_config |z_x3 z_x4|^2]^(1/2)
 <=M ||z||_2^4.                                      (3.1)
```

Every event in Theorem 2.3 has two projections whose fiber bounds have
geometric mean at most `Delta*sqrt(max(1,sigma))`.  Here are the details.

* **Adjacent permutation.**  In `E_11=E_12`, project to
  `(b1,c21)` and `(b2,c22)`.  Either pair fixes `a2`; the remaining
  incident ordered pair has at most `Delta` choices.
* **Square cell.**  It is enough to display `E_11`; row/column rotations give
  the other cells.  The following table gives a partition of the four
  weighted color labels and the two fiber bounds:

  ```text
  equality in E_11       color-pair partition                 fibers
  a1=b1                  (c11,c12) | (c21,c22)               sigma*Delta, Delta
  a1=c11                 (c11,c12) | (c21,c22)               Delta, sigma*Delta
  b1=c11                 (c11,c21) | (c12,c22)               Delta, sigma*Delta.
  ```

  For example, in the first line, fixing `(c11,c12)` gives at most `sigma`
  choices for the repeated root `a1=b1`, then pair uniqueness fixes `b2`,
  and the incident degree at `b1` gives at most `Delta` choices for
  `(a2,c21)`; `c22` is then fixed.  In the reverse projection, an incident
  triple carrying `c21` gives at most `Delta` choices and all other labels
  are fixed.  The other two lines are the same argument with the repeated
  root occupying a weighted coordinate.  Cauchy--Schwarz therefore costs
  `Delta*sqrt(sigma)`, which is at most `Delta` in the actual shell.
* **Opposite equal colors.**  If `c11=c22=c`, use
  `(c,c12)|(c,c21)`.  Fixing `(c,c12)` leaves at most the `Delta` triples
  carrying color `c12`; pair uniqueness determines the other three nodes.
  The second projection is symmetric.

The smooth kernel factors have modulus at most one, so they only decrease
the absolute sums.  A union bound has four adjacent-equality events, twelve
oriented square events, and two opposite-color events.  Thus (3.1) gives the
fully explicit envelope

```text
sum_repeated |z_c11 z_c12 z_c21 z_c22|
 <=18*Delta*sqrt(max(1,sigma))*||z||_2^4.           (3.2)
```

Combining `sigma<=1`, (1.4), and (3.2) proves

```text
|Q_repeated(z)|<<D q^o(1) ||z||_2^4.                 (3.3)
```

This holds for arbitrary complex `z`; no positivity or Fourier cancellation
is used.

---

## 4. Surviving core

After (3.2), every unresolved rectangle has eight distinct displayed nodes.
In particular all four unordered hyperedges are distinct, no cell is a
square, and the opposite colors differ.  The exact residual determinant and
carrier constraints from the earlier reports remain in force.  Bounding
this all-distinct linear-hypergraph sector by `D q^o(1)` is still open.

```text
complete repeated-node classification:              PROVED;
adjacent permutation/tangent contribution:           O(D q^o) / PROVED;
square-hyperedge contribution:                        O(D q^o) / PROVED;
opposite-equal-color contribution:                    O(D q^o) / PROVED;
all repeated-node contribution:                       O(D q^o) / PROVED;
all-distinct four-cycle contribution:                 OPEN;
full four-cycle bound (FC):                           NOT PROVED.
```

Finite replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_four_cycle_permutation_sector.py
```
