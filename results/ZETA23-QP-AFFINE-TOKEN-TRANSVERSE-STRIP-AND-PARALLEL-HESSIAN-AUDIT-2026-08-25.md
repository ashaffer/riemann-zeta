# QP affine token charts: transverse strip theorem and parallel Hessian gate

**Date:** 2026-08-25  
**Verdict:** every fixed **transverse** Cartesian token chart satisfies the
sharp occupied-cell scale `O(D log D)` using the middle determinant alone.
For parallel token directions, the restored product mask has a universal
positive-definite hexagonal Hessian unless the common direction is `K`-null;
the null case is exactly a coordinate tangent ruling.  This yields a sharp
`O(D)` theorem for short parallel charts whose physical row is locked to the
stationary affine law.

It does **not** finish NDS.  Generic actual-prime charts do not automatically
have that integral row lock, and a cover by fixed charts has up to `D^2`
directions with no proved Carleson summability.  The sharp four-cycle bound
therefore remains open.

## 1. Strongest unconditional fixed-chart theorem

Let

```text
P(r)=P0+rV,             R(s)=R0+sW
```

with `r` and `s` in integer intervals of lengths `R,S<<D`.  The middle
transition determinant is

```text
k(r,s)=A+B*r+C*s+E*r*s,       E=det(V,W).             (1.1)
```

Every physical cell has `|k(r,s)|<<D`.  If `E!=0`, fix `r`.  The slope in
`s` is the integer

```text
C+E*r.                                                       (1.2)
```

At most one `r` makes this slope zero.  Every other fibre contains at most

```text
1+2D/|C+E*r|                                             (1.3)
```

integer values of `s`.  The nonzero slopes in `(1.2)` are distinct integers,
so their reciprocal sum is at most twice a harmonic sum.  Therefore

```text
#{(r,s):|k(r,s)|<<D}
 <<R+S+D log(2+R)
 <<D log D.                                             (1.4)
```

This proof needs neither a product window nor an actual-node relaxation.
Thus:

> **Transverse fixed-chart theorem.** Every affine Cartesian token chart
> with `det(V,W)!=0` contributes `D q^o(1)` cells.

Equivalently, the only fixed-direction branch not closed by the determinant
strip is

```text
det(V,W)=0.                                             (1.5)
```

## 2. Exact elementary escape inside the parallel branch

When `E=0`, `(1.1)` is the affine strip `A+B*r+C*s`.  The elementary bounds
are

```text
N <=R(1+2D/|C|)       if C!=0,
N <=S(1+2D/|B|)       if B!=0.                         (2.1)
```

Hence the strip already closes at scale `D` if, for example,

```text
|C|>>R       or       |B|>>S.                          (2.2)
```

The exact escaping coefficient range is

```text
E=0,        |C|<<R,        |B|<<S.                     (2.3)
```

At its endpoint `B=C=0`, the determinant is constant and an entire `R*S`
block survives.  Taking `R=S=D` gives `D^2` cells, so determinant algebra
alone is genuinely insufficient in `(2.3)`.

## 3. Parallel tokens and the radial null dichotomy

In the Bezout chart, write the physical centre direction corresponding to
`V` as

```text
U=(p,P)=(u*V1-C*V2, v*V1-c*V2).                       (3.1)
```

If `W=tV`, its endpoint direction is

```text
Z=-t(P,p).                                             (3.2)
```

Consequently

```text
p*Z1=P*Z2=-t*p*P,
V^T K V=-2pP.                                          (3.3)
```

Thus every parallel token chart is signed-tangent, but it has two sharply
different subcases.

1. If `V^T K V!=0`, both coordinate-product cross terms are nonzero and the
   radial/product mask has genuine quadratic curvature.
2. If `V^T K V=0`, then `pP=0`; the two physical directions lie on opposite
   coordinate axes.  Both product Hessians degenerate.  This is exactly the
   coordinate rank-one/tangent ruling.

The second statement is an equivalence **within the parallel branch**.  Full
signed tangency alone is weaker than Hessian degeneracy.  For example,
`U=Z=(1,1)` is signed-tangent but both product Hessians are nondegenerate.

## 4. Universal hexagonal Hessian

Consider one restored product leg

```text
b(r)=b0+p*r,       d(s)=d0+z*s.                       (4.1)
```

The stationary affine row is

```text
x(r,s)=x0-(x0*p/b0)r-(x0*z/d0)s.                      (4.2)
```

Put `A=p*r/b0` and `G=z*s/d0`.  Direct multiplication gives

```text
x(r,s)b(r)d(s)-x0*b0*d0
 =-x0*b0*d0 {A^2+A*G+G^2+A*G(A+G)}.                  (4.3)
```

The quadratic Hessian has determinant

```text
3*x0^2*p^2*z^2.                                       (4.4)
```

It is definite exactly when `p*z!=0`.  If `|A|+|G|<=1/4`, then

```text
|A*G(A+G)| <=(1/4)(A^2+A*G+G^2),
A^2+A*G+G^2 >=(A^2+G^2)/2.                            (4.5)
```

If the base and cell are both in a product window of unscaled width
`qD/8`, shell comparability in `(4.3)--(4.5)` yields

```text
p^2*r^2+z^2*s^2 <<D.                                  (4.6)
```

Therefore the number of cells is

```text
<<D/|pz|+sqrt(D)/|p|+sqrt(D)/|z|+1 <<D.               (4.7)
```

This proves:

> **Stationary parallel-chart theorem.** A short parallel non-null chart
> whose actual row equals the integral affine law `(4.2)` has `O(D)` cells.

The principal adjacent chart is `p=-1,z=1`, for which `(4.3)` becomes the
previous `A^2-A*s+s^2` law.

## 5. The row-lock hypothesis is real

Equation `(4.2)` is integral only if

```text
b0 | x0*p,              d0 | x0*z.                    (5.1)
```

For distinct actual prime-power nodes, `gcd(x0,b0)=1`.  If the direction is
short, `0<|p|<b0`, the first divisibility in `(5.1)` is impossible.  Thus the
exact affine row law used by the full-integer principal chart does not
automatically survive the actual-prime mask.

The two hard product legs do show why the remaining regime is narrow.  In a
parallel chart the affine determinant coefficients are

```text
B=p*d0-P*E0,
C=t(p*B0-P*b0).                                       (5.2)
```

If `(2.3)` holds, the stationary row slopes inferred from the two coordinate
products differ by only

```text
O(|B|/q)+O(|C|/q).                                    (5.3)
```

But “nearby rational slopes” is not an integral row lock.  Proving that the
rounded actual rows obey a bounded collection of affine laws, or proving a
two-leg curved-surface estimate without such a lock, is the precise local
parallel-direction theorem still missing.

## 6. Fixed charts do not sum for free

The token box contains `Theta(D^2)` primitive directions.  Even after the
fixed-chart bounds above, summing an `O(D)` capacity over all directions
would give the useless ceiling

```text
O(D^3).                                                (6.1)
```

The physical fixed anchor has only `O(D)` selected `P` tokens and `O(D)`
selected `R` tokens, but their pair differences can still determine
`O(D^2)` distinct directions.  A single cell also belongs to many
noncanonical affine charts.  Hence there is no bounded-overlap chart cover.

After maximal charts are chosen, the needed summability statement is a
Carleson packing of the form

```text
sum_over_directions
  (# selected P points on the direction)
  (# selected R points on the parallel direction)
 <<D q^o(1).                                           (6.2)
```

Pair counting only controls the separate second moments of the two line
populations and permits order `D^2` in `(6.2)`.  The affine biclique has one
direction and saturates `(6.2)` at `D`; scattered direction sets show why
local capacities cannot simply be added.  This is the same anchored
chart-overlap/Carleson obstruction identified by ACCT, now in exact token
coordinates.

## 7. Verification and status

```text
src/qp_affine_four_completion_hessian.py
src/test_qp_affine_four_completion_hessian.py
lean/weilcert/QPAffineFourCompletionHessian.lean
```

```text
affine determinant expansion:                         PROVED;
transverse fixed-chart O(D log D):                     PROVED;
parallel determinant-strip escape (2.3):              PROVED / SHARP;
stationary cubic and Hessian determinant:              PROVED;
parallel non-null stationary chart O(D):               PROVED;
parallel K-null iff coordinate tangent ruling:         PROVED;
full tangent iff Hessian-degenerate:                    FALSE;
generic actual-prime integral row lock:                 FALSE AS AUTOMATIC STEP;
rounded-row parallel fixed-chart theorem:               OPEN;
global fixed-chart Carleson summability:                OPEN;
sharp four-cycle bound:                                 NOT PROVED.
```
