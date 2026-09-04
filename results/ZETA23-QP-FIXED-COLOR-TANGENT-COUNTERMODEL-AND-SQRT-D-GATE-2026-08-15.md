# QP four-cycle: fixed-color tangent countermodel and square-root gate

**Date:** 2026-08-15  
**Verdict:** the proposed fixed-color completion estimate

```text
m(C) << (D/|det C|) q^o(1)                           (0.1)
```

is false for the underlying integer-shell/rank-one-box geometry.  There is
an exact family with four distinct fixed colors, eight distinct displayed
nodes in every rectangle, `|det C|=2D`, and `sqrt(D)-1` carrier
completions.  The construction uses the full integer shell and the even
formal parameter `q=2m`, so it is **not** an actual odd-prime/prime-power
counterexample.  It proves that (0.1) cannot follow from product-window,
pair-uniqueness, determinant, and all-distinct geometry alone.

The family identifies `sqrt(D)` as the sharp local-cluster scale.  A global
actual-shell bound `m(C)<<sqrt(D)q^o(1)` would be a real exponent gain, but
requires a new theorem saying that the prime-power factorizations occupy
only `q^o(1)` such tangent clusters.  That global clustering statement is
not proved here.

---

## 1. Exact fixed-color family

Let `m>20h>=40`, and set

```text
q=2m,                     D=h^2.                    (1.1)
```

Fix the color matrix

```text
C = [m     m-2h]
    [m-h   m-3h].                                  (1.2)
```

Its four entries are distinct and

```text
det C=m(m-3h)-(m-2h)(m-h)=-2h^2=-2D.              (1.3)
```

For every integer `s` with `1<=s<h`, put

```text
a1=m+h+s,       a2=m+2h+s,
b1=m-h-s,       b2=m+h-s.                          (1.4)
```

The row and column pairs are nondegenerate.  The eight displayed labels are
all distinct: the rows lie strictly above `m+h`, the colors lie between
`m-3h` and `m`, `b2` lies strictly between `m` and `m+h`, and `b1` lies
strictly between `m-2h` and `m-h` but misses both endpoints.  Consequently
all four unordered hyperedges are distinct as well.

There are exactly `h-1=sqrt(D)-1` displayed completions of the same fixed
color matrix.

---

## 2. All four products remain in an `O(qD)` carry window

With `Q=q^3=8m^3`, direct expansion gives the four residuals divided by
eight:

```text
r11/8 = -m(h+s)^2,

r12/8 = -2h^3-3mh^2+2hs^2-ms^2,

r21/8 =  2h^3-3mh^2+3h^2s-3mhs+hs^2-ms^2,

r22/8 = -6h^3-7mh^2+3h^2s-mhs+3hs^2-ms^2.         (2.1)
```

Since `1<=s<h` and `m>20h`, these formulas give, with ample slack,

```text
max_ij |r_ij| <=80*q*D.                             (2.2)
```

Thus every point of the family belongs to one fixed-constant carry
truncation.  Taking, for example,

```text
h=floor(m^(8/33))
```

places `D` at the active exponent `q^(16/33+o(1))`; all labels lie in a
multiplicative shell whose relative width tends to zero.

The full integer support with cap `80qD` is pair-unique for large `m`, since
two third coordinates over a fixed pair would imply

```text
8xy <= 2*(80qD),
```

where the left side is `asymp q^2` and the right side is `qD=o(q^2)`.
Therefore the countermodel retains the same linear-hypergraph property used
in the actual-shell reduction.

Combining (1.3) and the completion count shows

```text
m(C)=sqrt(D)-1,          D/|det C|=1/2.             (2.3)
```

No factor `q^o(1)` can bridge this fixed power gap.

The mechanism is the additive scaling tangent

```text
(a1,a2,b1,b2) -> (a1+t,a2+t,b1-t,b2-t).            (2.4)
```

It changes each carrier product by

```text
(a_i+t)(b_j-t)-a_i*b_j=t(b_j-a_i)-t^2,             (2.5)
```

which is `O(D)` for offsets and `t` of order `sqrt(D)`.  This is not the
previously closed exact conic tangent `u2*v2=0`; it is a second-order tangent
orbit of the rank-one product surface.

---

## 3. Exact scope boundary

The construction does **not** settle the actual fixed-color problem:

* `q=2m` is even, rather than the odd prime used in QP;
* the labels are unrestricted integers, not prime powers;
* retaining many parameters `s` after imposing the eight prime/prime-power
  conditions is a simultaneous affine-prime problem, not established by
  the construction.

Accordingly, (0.1) is marked false only as a geometry-only lemma.  It may
still conceivably hold on the actual prime-power support, but any proof must
use that support in an essential way.  The finite actual-shell observations
of completion multiplicity at most three do not constitute such a proof.

---

## 4. The rigorous local square-root theorem

There is a simple theorem explaining the scale in (2.3).  Fix the four
colors.  In the active window, fixing `a1` puts `b1` in an interval of length

```text
2H/(8*a1*c11)=H/(4*a1*c11)<1.                       (4.1)
```

Thus `b1` is unique.  The corner `(a2,b1,c21)` then fixes `a2`, and
`(a1,b2,c12)` fixes `b2`; the fourth corner is only a check.  Hence:

### Proposition 4.1 (local carrier interval)

If the first-row carriers `a1` of a family of fixed-color completions all
lie in an integer interval of length `R`, then

```text
#completions <=R+1.                                  (4.2)
```

In particular, one additive cluster of diameter `O(sqrt(D))` contains at
most `O(sqrt(D))` completions, and the family above shows this is sharp for
integer shells.

What is missing is a global actual-shell theorem decomposing all completions
into only `q^o(1)` such clusters.  Equivalently, one must rule out power-many
macroscopically separated prime-power factorizations of the four simultaneous
length-`D` product intervals.

If achieved, the uniform bound

```text
m(C)<<sqrt(D) q^o(1)                                (4.3)
```

combined with the proved fixed-determinant color bound would give

```text
|Q_nd(z)| << D^(3/2) q^o(1) ||z||_2^4,             (4.4)
```

improving the old `D^2` scale but not reaching the target `D`.

---

## 5. Status

```text
D/|k| fixed-color law from rank-one geometry:       FALSE;
all-distinct integer tangent family of sqrt(D):      PROVED;
same family on actual odd-prime prime-power shell:   NOT CONSTRUCTED;
local O(sqrt(D)) cluster bound:                      PROVED;
global actual-shell O(sqrt(D) q^o) completion bound: OPEN;
full four-cycle bound (FC):                          OPEN.
```

Finite exact replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_fixed_color_tangent_countermodel.py
```
