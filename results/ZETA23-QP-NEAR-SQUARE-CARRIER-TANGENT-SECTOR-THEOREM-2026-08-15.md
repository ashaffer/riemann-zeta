# QP four-cycle: near-square carrier tangent-sector theorem

**Date:** 2026-08-15  
**Verdict:** the entire sector in which the four carrier labels

```text
a1,a2,b1,b2
```

have diameter `O(sqrt(D))` satisfies the target weighted four-cycle bound
`O(D q^o(1))` for arbitrary complex coefficients.  This includes the sharp
additive scaling orbit from the integer fixed-color countermodel.  Thus the
local `sqrt(D)` multiplicity is not itself an obstruction after the color
weights are summed correctly.

The surviving generic sector has carrier diameter larger than every fixed
multiple of `sqrt(D)`.  No decomposition of that sector into affordably many
elongated tangent clusters is proved here, so full `(FC)` remains open.

---

## 1. Setup

Let the truncated symmetric carry support satisfy

```text
|8abc-Q|<=H,              Q=q^3, H<<qD,             (1.1)
```

with every shell node between fixed positive multiples of `q`.  The active
exponent has `D=o(q)`, so fixing any two coordinates determines at most one
third coordinate.

For `R>=1`, let `F_R` be the ordered nondegenerate rectangles satisfying

```text
diam{a1,a2,b1,b2}<=R.                               (1.2)
```

The smooth kernel factors have modulus at most one and may be discarded in
an absolute upper bound.

---

## 2. A near-square corner has only `O(R)` positions

Fix a color `c` and an active triple `(a,b,c)` with `|a-b|<=R`.  Put

```text
X=Q/(8c),                   u=(a+b)/2.              (2.1)
```

Then

```text
|ab-X|<=H/(8c),
u^2=ab+(a-b)^2/4,
|u^2-X|<=H/(8c)+R^2/4.                              (2.2)
```

Since `u` and `sqrt(X)` are both `asymp q`, (2.2) gives

```text
|u-sqrt(X)| << (D+R^2)/q.                           (2.3)
```

Together with `|a-u|<=R/2`, this confines `a` to an interval of length

```text
R+O((D+R^2)/q).                                     (2.4)
```

Consequently, if `R<<sqrt(D)`, the first carrier has `O(R+1)` integer
choices.  Once `a` is fixed, pair uniqueness fixes `b`.

This argument uses no primality and is uniform over the fixed color.

---

## 3. Two color-pair projections

Fix the top color pair `(c11,c12)` in a rectangle from `F_R`.

1. By Section 2 applied to `(a1,b1,c11)`, there are `O(R+1)` choices for
   `a1`, and then `b1` is fixed.
2. The pair `(a1,c12)` fixes `b2`.
3. Condition (1.2) puts `a2` in an interval of length `2R`, giving
   `O(R+1)` choices.
4. The pairs `(a2,b1)` and `(a2,b2)` fix `c21` and `c22`.

Thus the projection

```text
pi_top: rectangle -> (c11,c12)                      (3.1)
```

has fiber `O((R+1)^2)`.  The same argument applied to the bottom row shows
that

```text
pi_bottom: rectangle -> (c21,c22)                   (3.2)
```

has the same fiber bound.

For arbitrary complex `z`, Cauchy--Schwarz now gives

```text
sum_(rectangle in F_R) |z_c11 z_c12 z_c21 z_c22|

 <= [sum_F_R |z_c11 z_c12|^2]^(1/2)
    [sum_F_R |z_c21 z_c22|^2]^(1/2)

 << (R+1)^2 ||z||_2^4.                              (3.3)
```

### Theorem 3.1 (near-square carrier sector)

For every fixed `C`, the sector

```text
diam{a1,a2,b1,b2}<=C*sqrt(D)                        (3.4)
```

has absolute weighted mass

```text
<<_C D ||z||_2^4.                                   (3.5)
```

The conclusion is already at the desired four-cycle scale and is stronger
than a fixed-color multiplicity estimate because it sums all colors at
once.

### Theorem 3.2 (anisotropic two-gap tangent sector)

The same proof gives a useful larger sector.  Suppose, in one orientation,

```text
|a1-b1|<=R,             |a2-a1|<=T,
T<=R,                   R*T<<D.                    (3.6)
```

The near-square calculation in Section 2 confines `a1` to `O(R+1)`
positions after `(c11,c12)` is fixed; `b1,b2` are then unique and `a2` has
`O(T+1)` positions.  Thus the top-color projection has fiber `O(RT)`.

For the bottom-color projection, use

```text
|a2-b1|<=|a2-a1|+|a1-b1|<=R+T<=2R.                (3.7)
```

It likewise has fiber `O(RT)`.  Hence the sector (3.6) has weighted mass

```text
<<R*T ||z||_2^4 <<D ||z||_2^4.                    (3.8)
```

Row/column interchange and the four choices of corner give the symmetric
orientations.  This closes elongated tangent boxes as well as round
`sqrt(D)` boxes: a long cross-gap `R` is affordable whenever the adjacent
same-side displacement is at most `D/R`.

---

## 4. Relation to the sharp integer tangent family

In the fixed-color integer family

```text
a=(m+h+s,m+2h+s),
b=(m-h-s,m+h-s),              1<=s<h,
D=h^2,                                             (4.1)
```

the carrier diameter is less than `5h=5sqrt(D)`.  The same color matrix has
`sqrt(D)-1` completions, so any pointwise `O(1)` multiplicity claim fails in
the integer geometry.  Nevertheless all those completions lie in (3.4),
and Theorem 3.1 controls their aggregate arbitrary-weight contribution at
the target `O(D)` scale.

This is the correct treatment of the additive tangent: retain its local
multiplicity and exploit the two bounded-fiber color projections.

---

## 5. Remaining generic gate

After the repeated-node theorem and Theorems 3.1--3.2, it is legitimate to
delete every orientation satisfying (3.6).  In particular the unresolved
rectangles may be required to have
simultaneously

```text
all eight displayed nodes are distinct,
all four unordered hyperedges are distinct,
diam{a1,a2,b1,b2} >> sqrt(D),
no corner cross-gap R has an adjacent gap T<=R
with R*T<<D.                                        (5.1)
```

An additive shift `(a_i+t,b_j-t)` in this region usually has a shorter
allowable range because

```text
(a_i+t)(b_j-t)-a_i*b_j=t(b_j-a_i)-t^2.             (5.2)
```

Turning that observation into a global weighted decomposition requires
controlling which of the four cross-gaps is large and how many separated
prime-power factorization clusters occur.  No uniform summable cluster
decomposition is asserted here.

```text
near-square carrier sector at O(D):                 PROVED;
anisotropic two-gap tangent sectors at O(D):        PROVED;
integer sqrt(D) tangent multiplicity:               ABSORBED;
all-distinct large-diameter sector:                  OPEN;
full four-cycle bound (FC):                         OPEN.
```

The exact interval and projection-fiber envelopes are replayed in
`src/qp_fixed_color_tangent_countermodel.py` and
`src/test_qp_fixed_color_tangent_countermodel.py`.
