# QP high-completion tail: two-sided residual-lattice incidence audit

**Date:** 2026-08-22  
**Verdict:** after deletion of every residual affine line containing three
selected completions on either projection, the rigorous two-sided point cap
is

```text
m << min(1+sqrt(EF/|k|), 1+sqrt(GH/|k|)).           (0.1)
```

Here `E,F` are row-residual rectangle widths and `G,H` are the transpose
(carrier-residual) widths.  The exact matched bilinear level adds a support
exclusion, but it supplies no further factor of `m`.  In particular, it does
not turn (0.1) into a product improvement and it does not force a rich line.

This limitation is rigorous, not just a failure of one proof.  There are
arbitrarily large exact nonzero-level integer matchings in which both
projections have no three collinear points.  More sharply, there are
simultaneously line-sparse matchings of size

```text
m >> N/sqrt(log N)                                  (0.2)
```

inside two `O(N)` integer squares on the exact level `r dot s=1`.  Thus the
square-root-of-normalized-area exponent in (0.1) is best possible from the
stated finite-dimensional hypotheses, up to a logarithm.

For the actual QP fibre, the conclusion is therefore a **rich-line or
two-large-normalized-areas dichotomy**, not a smaller point cap:

```text
either a row/carrier residual line contains >=3 selected points,
or EF >> |k|m^2 and GH >> |k|m^2.                  (0.3)
```

The rich-line alternatives still require an arithmetic packet merger or an
inverse theorem.  No global high-tail or four-cycle promotion follows.

---

## 1. Exact setup and the strongest elementary theorem

Let `K` be an integral `2 x 2` matrix with `det K=k!=0`.  For the completions
of one fixed color fibre write

```text
r_i=K^T a_i in Lambda_r=K^T Z^2,
s_i=K b_i   in Lambda_s=K Z^2.                     (1.1)
```

Both lattices have covolume `|k|`.  The QP pair-uniqueness statement makes
both projections injective.  Suppose the row points lie in a rectangle of
widths `E,F`, the carrier points lie in one of widths `G,H`, and every affine
line contains at most `T_r`, respectively `T_s`, selected points.

Choose a primitive shortest vector after anisotropically scaling the first
rectangle to a unit square.  Minkowski gives scaled length
`O(sqrt(|k|/(EF)))`.  Parallel lattice cosets are separated by `|k|` under
the determinant functional, while its total range on the rectangle is
`O(sqrt(|k|EF))`.  Hence only

```text
O(1+sqrt(EF/|k|))                                  (1.2)
```

such lines meet the rectangle.  Multiplication by `T_r` bounds the row
projection.  The identical argument for `K Z^2` bounds the carrier
projection.  Since these are two upper bounds for the **same indexed set**,
one takes their minimum:

```text
m << min(T_r(1+sqrt(EF/|k|)),
         T_s(1+sqrt(GH/|k|))).                     (1.3)
```

There is no legitimate multiplication of the two estimates.  Setting
`T_r=T_s=2` proves (0.1) and (0.3).

## 2. What the exact bilinear level does—and does not do

The two residuals obey

```text
r_i^T adj(K) s_i=kL                                (2.1)
```

for each matched index `i`.  If every entry of `adj(K)` is `O(q)` and the
active pinning gives `|L| >> |k|q`, then

```text
(|r_i1|+|r_i2|)(|s_i1|+|s_i2|) >> |k|^2.          (2.2)
```

On origin-controlled dyadic boxes this is the exponent constraint

```text
max(e,f)+max(g,h)>=2 ell.                          (2.3)
```

It is a non-emptiness condition on every matched point, not a point-count
gain.  A technical qualification matters: (2.2) uses coordinate **radii**.
It cannot be inferred from the widths of arbitrarily translated rectangles.
Widths and radii are comparable only after the residual coordinates have
been put into origin-controlled/dyadic-magnitude boxes.

The incidence graph in (2.1) contains only the `m` matched edges
`(r_i,s_i)`.  It does not assert that `r_i^T adj(K)s_j=kL` for cross pairs
`i!=j`.  Point-line incidence theorems therefore see a sparse matching, not
a dense incidence configuration.  Their usual superlinear incidence terms
have nothing to act on.

## 3. Exact nonzero level does not force a rich line

The elementary family

```text
r_t=(t,t^2+1),
s_t=(t^2-t+1,1-t)                                  (3.1)
```

satisfies `r_t dot s_t=1` identically.  Both projections lie on
nondegenerate parabolas, so no affine line contains three of their points.
This already disproves a rich-line conclusion from injectivity, bilinearity,
and an exact nonzero level alone.

There is also an exponent-sharp balanced version by a short probabilistic
argument.  For every coprime pair

```text
N<=x,y<=2N                                          (3.2)
```

choose the centered solution `xu+yv=1`, with `|u|<=y/2`, and replace it by

```text
s=(u+y,v-x).                                       (3.3)
```

Then `r=(x,y)` and `s` have exact dot product one, both lie in `O(N)`
squares, and `|s|_infinity >> N`.  There are `asymp N^2` choices of `r`.
For fixed `s`, all solutions of `r dot s=1` differ by the primitive vector
`(s_2,-s_1)` of size `>>N`, so only `O(1)` members of (3.2) map to one `s`.

The number of collinear triples in an `O(N)` integer square is

```text
O(N^4 log N).                                      (3.4)
```

Indeed, for primitive directions of height `h`, there are `O(h)` directions,
`O(N^2)` starting points, and `O((N/h)^2)` choices of the other two points;
summing `N^4/h` over `h<=O(N)` proves (3.4).  The bounded carrier fibre gives
the same estimate for carrier triples in the pair pool.

Select every pair independently with probability
`c/(N sqrt(log N))`.  The expected vertex count and expected total number of
bad row/carrier triples are both on the `N/sqrt(log N)` scale; choosing `c`
small makes the former dominate.  Duplicate carrier pairs have only bounded
total multiplicity and negligible expected cost.  Deleting one member from
each remaining bad triple or duplicate leaves (0.2).  This proves that no
fixed power improvement over (0.1) follows from the finite-dimensional data.

## 4. Modular-parabola hostile test

For a prime `p`, put

```text
y_t = least residue of t^2 mod p,
r_t=(t,y_t),             s_t=(-y_t,t).             (4.1)
```

Both projections have `p` points in `p`-scale squares and no three are
collinear: an integer collinearity would reduce modulo `p`, while a line
meets the finite-field parabola in at most two points.  Moreover
`r_t dot s_t=0` **as an exact integer identity**.  Hence this construction
simultaneously saturates both one-sided square caps at level zero.

The nonzero modular analogue is a useful warning.  For `t!=0`, take

```text
r_t=(t,t^2),              s_t=(t^(-1),t^(-2))      (mod p).       (4.2)
```

Both are finite-field parabolas and `r_t dot s_t=2 (mod p)`.  Least integer
lifts remain line-sparse, but their exact dot products split among many
integers congruent to `2 mod p`.  Thus (4.2) is a hostile model for any
argument using only a congruence-level bilinear equation, but it is **not**
an exact fixed-level QP counterexample.  The exact construction in Section 3
is what rules out the abstract rich-line and power-saving claims.

## 5. Consequence for the critical QP ledger

With `m~D^kappa` and `|k|~D^ell`, the literal two-point-line sector requires

```text
e+f >= ell+2kappa,
g+h >= ell+2kappa.                                 (5.1)
```

At `kappa=5/16`, this is

```text
e+f,g+h >= ell+10/16.                              (5.2)
```

Together with the radius-qualified bilinear support condition (2.3), this
is the complete elementary two-sided polytope.  Two-sided general position
does not lower the multiplicity exponent further.  Any improvement must use
one of the hypotheses absent from the countermodels: actual prime-power
support, the four product windows, cross-pair incidences, or a theorem that
identifies and merges the residual rich lines.

Reproduction code is in
`src/qp_two_sided_residual_incidence_audit.py`, with tests in
`src/test_qp_two_sided_residual_incidence_audit.py`.
