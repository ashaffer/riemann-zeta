# QP four-cycle common-neighbor gate: gcd resonance and short divisors

**Date:** 2026-08-15  
**Verdict:** the proposed bound

```text
max_(a1!=a2) deg(a1,a2) << sqrt(D) q^o(1)           (CN)
```

is not proved.  An exact gcd reduction isolates two sharply different
branches.

* For distinct actual prime-power rows, the zero-cross-determinant branch is
  harmless; only nonzero residual classes remain.
* For the full integer shell, rows with a large gcd and a small reduced
  denominator collapse the two carry conditions to one positive short-product
  strip.  Exhaustive finite data in this branch grows materially faster than
  `sqrt(D)` over the tested range.  No asymptotic counterexample is asserted,
  but this branch cannot be dismissed by curvature or determinant spacing.

Thus `(CN)` is still a possible actual-prime-power theorem, but it is not a
credible structure-free integer-shell lemma without a new uniform theorem on
the special short-product strips below.

---

## 1. Exact common-neighbor identity

Use the hard carry core

```text
|8 a b c-q^3|<=E,             E asymp qD,
a,b,c asyp_w q,               D=q^2/B=q^(16/33).   (1.1)
```

Suppose the same column `b` is incident to rows `a1,a2`, with colors `c,d`.
Put

```text
r1=8 a1 b c-q^3,             r2=8 a2 b d-q^3.      (1.2)
```

Then the following identity is exact:

```text
r2-r1=8b(a2 d-a1 c).                                 (1.3)
```

Consequently

```text
k:=a2 d-a1 c in Z,          |k|<=E/(4b)<<_w D.      (1.4)
```

Write

```text
g=gcd(a1,a2),             a1=s g,       a2=r g,
gcd(r,s)=1.                                              (1.5)
```

Equation (1.4) becomes

```text
k=g(rd-sc).                                             (1.6)
```

In particular, if

```text
g>E/(4 b_min),                                        (1.7)
```

then `k=0`.  Coprimality in (1.5) now forces

```text
c=rh,                     d=sh                        (1.8)
```

for one positive integer `h`.  Both cubic residuals become the same integer:

```text
8sr g b h-q^3.                                        (1.9)
```

This is an exact theorem, not an asymptotic model.

---

## 2. What the resonant branch actually asks

Under (1.7), the common degree is the number of factor pairs `(b,h)` in the
legal coordinate boxes satisfying

```text
|8sr g b h-q^3|<=E.                                  (2.1)
```

The allowed interval for the integer product `bh` has full length

```text
E/(4sr g)<<_w D/s,                                   (2.2)
```

because `rg=a2 asyp q` and `E asyp qD`.  The divisor bound gives only

```text
deg(a1,a2)<<_w (1+D/s)q^o(1).                        (2.3)
```

Therefore `(CN)` follows on the resonant branch when

```text
s>=sqrt(D).                                          (2.4)
```

The unresolved integer obstruction is explicit:

```text
g>>D,                 s<sqrt(D),
a1=sg,                a2=rg with small coprime r,s.  (2.5)
```

Here (2.1) is a positive one-window divisor problem of natural length
`D/s`; there are no signs left to cancel.  A generic `O(D/s)` count would be
much larger than `sqrt(D)` for fixed `s`.

---

## 3. Why the actual prime-power zero branch is harmless

The project width satisfies `2w<log 2`.  Hence the shell contains at most one
power of any prime base.  Two distinct prime-power rows therefore have
different bases and

```text
gcd(a1,a2)=1.                                         (3.1)
```

If their cross integer `k` vanishes, (1.8) has

```text
s=a1 asyp q,                r=a2 asyp q.              (3.2)
```

In fact the narrow shell makes this sharper.  Equations (1.8) and (3.2) give

```text
c=a2*h,                    d=a1*h.
```

The ratio of any two shell nodes is less than two, so the positive integer
`h` must equal one.  The remaining interval for `b` has length `O(D/q)<1`.
Consequently the zero branch has at most one common carrier.  Thus an
actual-prime proof of `(CN)` only needs to control

```text
0<|a2 d-a1 c|<<D.                                   (3.3)
```

This is a meaningful reduction, but it is not yet a bound for (3.3).  There
are `O(D)` possible nonzero cross integers, and the elementary line-spacing
argument alone does not save their square root.

### A proved close-row power saving

There is nevertheless a deterministic power saving in the tangent range.
Let

```text
h=|a2-a1|>=1.                                             (3.4)
```

For fixed shell constants and residual cutoff, assume `D<<q^(2/3)` and
`D=o(q)`.  Then every integer-shell row pair, hence every coprime row pair,
satisfies

```text
deg(a1,a2) << (h+1)*sqrt(D) + D^(3/2)/q^(1/3).           (3.5)
```

At the project scale `D=q^(16/33)`, this is

```text
deg(a1,a2) << (h+1)D^(1/2) + D^(13/16).                 (3.6)
```

Here is a proof.  A common carrier has colors `c,d` and, after possibly
interchanging the two rows, put `j=c-d`.  The cross identity gives

```text
|(a2-a1)c-a2*j|<<D.                                     (3.7)
```

Because all variables lie in fixed proportional `q`-shells, (3.7) implies

```text
# possible j << h+1,             |j| asyp h.             (3.8)
```

The case `j=0` is impossible once `D=o(q)`.  Also

```text
bc in I1,                 bd in I2,                     (3.9)
```

where `I1,I2` are intervals of length `O(D)` centred at numbers comparable
with `q^2`.  For fixed `j`, subtraction in (3.9) confines `b*j` to an
interval of length `O(D)`.  Hence all such `b` lie in an interval of length

```text
L_j<<D/h.                                                (3.10)
```

It remains to count lattice points `(b,c)` in such a short interval with

```text
|bc-N|<<D,                    N asyp q^2.                (3.11)
```

Partition the `b` interval into blocks of length `eta*q^(1/3)`, with `eta`
a sufficiently small fixed constant.  For three points

```text
b1=b2-u < b2 < b3=b2+v
```

in one block, write `c_i=N/b_i+e_i`, where `|e_i|<<D/q`.
The integer second determinant is

```text
Delta=u*c3+v*c1-(u+v)c2
     =N*u*v*(u+v)/(b1*b2*b3) + O((D/q)(u+v)).            (3.12)
```

If `uv>C D`, the right side is strictly positive.  But within the chosen
block it has modulus less than one: its two terms are respectively
`O(eta^3)` and `O(eta D/q^(2/3))`.  This contradicts integrality.  Therefore
every such triple has `uv<<D`.  Applying this to the first point, an
intermediate point, and the last point shows that every point in the block
lies within `O(sqrt(D))` of one endpoint.  Since (3.11) has vertical width
`O(D/q)<1`, each `b` supports at most one `c`.  Thus a block contains
`O(sqrt(D))` points, and a fixed `j` contributes

```text
<<sqrt(D)*(1+D/(h*q^(1/3))).                            (3.13)
```

Summing (3.13) over (3.8) proves (3.5).

In particular, for every fixed `eta_0>0`, the range

```text
h<=D^(1/2-eta_0)                                       (3.14)
```

has a genuine exponent below one.  This does **not** prove `(CN)`: coprime
rows with larger transverse separation remain open.  It does rigorously
exclude the observed close-row tangent blocks as a source of degree
`D^(1-o(1))`.

---

## 4. Exhaustive hard-core diagnostics

The finite replay uses the full support

```text
|B log(8abc/q^3)|<=1,              A=50/33,
w=.2.                                                  (4.1)
```

For every row pair it computes the exact intersection of its column
supports.

### Full integer shell

| prime `q` | `D=q^2/B` | `sqrt(D)` | max common degree | maximizing rows | row gcd |
|---:|---:|---:|---:|---:|---:|
| 1,601 | 102.27 | 10.11 | 10 | 705, 710 | 5 |
| 3,203 | 143.14 | 11.96 | 12 | 1,378, 1,382 | 2 |
| 6,421 | 200.55 | 14.16 | 13 | 2,840, 2,845 | 5 |
| 12,853 | 280.77 | 16.76 | 16 | 6,361, 6,362 | 1 |
| 25,013 | 387.75 | 19.69 | 23 | `4*2731,5*2731` | 2,731 |
| 50,021 | 542.60 | 23.29 | 27 | `5*4412,6*4412` | 4,412 |
| 100,003 | 759.20 | 27.55 | 41 | `7*6422,8*6422` | 6,422 |

The final three maximizers are exactly the small-denominator branch (2.5).
For example, at `q=100003`, the gcd is larger than the complete bound in
(1.4), so all 41 common neighbors satisfy

```text
c=8h,                    d=7h                       (4.2)
```

and are counted by the single product strip (2.1).  The observed ratio to
`sqrt(D)` reaches `1.49`.  This does not refute a `q^o(1)`-loss theorem, but
the common degree is about `.05D` at the largest scales, so the data does not
support treating `sqrt(D)` as a formal curvature bound.

For fixed small reduced ratios, the same behavior is stable.  At `q=100003`,
maximizing over all legal `g` gives degrees

```text
r/s:       4/3   5/4   6/5   7/6   8/7   9/8  10/9  11/10
degree:     26    35    33    38    41    34    32     33. (4.3)
```

Restricting instead to coprime integer row pairs removes this resonance.
The exhaustive maxima are:

| prime `q` | `sqrt(D)` | coprime max | max / `sqrt(D)` | maximizing rows |
|---:|---:|---:|---:|---:|
| 1,601 | 10.11 | 8 | .791 | 778, 779 |
| 3,203 | 11.96 | 10 | .836 | 1,445, 1,451 |
| 6,421 | 14.16 | 11 | .777 | 2,986, 2,995 |
| 12,853 | 16.76 | 16 | .955 | 6,361, 6,362 |
| 25,013 | 19.69 | 18 | .914 | 11,215, 11,232 |
| 50,021 | 23.29 | 24 | 1.030 | 23,314, 23,323 |
| 100,003 | 27.55 | 29 | 1.052 | 41,248, 41,251 |

This is diagnostic support for `(CN)`, not a proof.  The final maximizer is
especially structured: its 29 carriers are the consecutive integers
`55038,...,55066`; their first colors are `55066,...,55038`, so `b+c` is
constant, and the second colors are exactly four lower.  The residuals grow
quadratically away from the tangent point.  This is the `sqrt(D)` tangent
block controlled, non-sharply, by (3.5).

### Actual prime-power shell

| prime `q` | 1,601 | 3,203 | 6,421 | 12,853 | 25,013 | 50,021 | 100,003 | 200,003 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| max common degree | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

With the smooth positive core `|xi|<=12`, the corresponding values at
`q=25013,50021,100003,200003` are only `4,4,4,5`.  These computations are
consistent with a strong actual-prime theorem, but do not prove one.

---

## 5. Consequence for the four-cycle route

A common-neighbor Schur proof now has a precise decision tree.

```text
integer rows, g>>D, reduced denominator s<sqrt(D):
    positive short-product strip of length D/s;     UNRESOLVED / HOSTILE;

integer resonant rows with s>=sqrt(D):
    degree <=sqrt(D)q^o by the divisor bound;        PROVED;

distinct actual prime-power rows, k=0:
    degree <=1;                                      PROVED;

integer or actual rows, gap h<=D^(1/2-eta):
    degree <<D^(1-eta)+D^(13/16);                    PROVED;

distinct actual prime-power rows, 0<|k|<<D:
    simultaneous-short-divisor theorem needed;      OPEN.                 (5.1)
```

Thus no estimate `D^theta`, `theta<1`, has been proved uniformly for every
integer row pair.  Proving `(CN)` for the actual shell requires using the
coprime prime-power rows in the nonzero branch (3.3), not importing a false or
unproved structure-free hyperbola heuristic.

---

## 6. Binary status

```text
exact residual/gcd reduction:                       PROVED;
large-gcd resonance classification:                 PROVED;
resonant bound (1+D/s)q^o:                          PROVED;
actual-prime zero branch O(1):                       PROVED;
close-row power saving (3.5):                       PROVED;
integer-shell max-degree sqrt(D)q^o:                NOT PROVED;
actual-prime max-degree sqrt(D)q^o:                 NOT PROVED;
FC from common-neighbor Schur:                      NOT PROVED.
```

Executable replay of the exact identities:

```bash
python3 -m pytest -q src/test_qp_four_cycle_common_neighbor_gate.py
```

The exhaustive finite routine is
`maximum_common_neighbor_degree` in
`src/qp_four_cycle_common_neighbor_gate.py`.
