# QP Bezout self-orbit: Beatty-chart globalization audit

**Date:** 2026-08-25  
**Verdict:** the width-one digital-strip observation genuinely reduces the
number of physical token directions, so the crude picture of two arbitrary
`D`-point clouds is wrong.  It does **not** globalize the transverse
fixed-chart estimate.  After the exact endpoint reflection, both token sides
are one short modular orbit, and the middle determinant is automatically
`O(D)` on its whole `O(D) x O(D)` label square.  Thus the determinant strip
has essentially no global selectivity.  The radial/actual-row mask must prove
the missing weak-`ell^1` Carleson packing.

The best conclusion from the present local ingredients remains
`W(gamma) << D^(3/2) q^o(1)`, losing exactly `D^(1/2)` from the desired
anchored bound.  No actual-prime counterexample is produced here.

## 1. One centre orbit, not two independent token sets

Fix a primitive anchor `gamma=(c,C)` and choose

```text
c*u-C*v=1.
```

For every label `t` for which the physical shell contains a centre pair,
write

```text
P_t=(t,n_t),
b_t=u*t-C*n_t,             B_t=v*t-c*n_t.            (1.1)
```

If an endpoint has determinant label `h=-j`, its endpoint token and physical
pair are exactly

```text
R^j=-P_j=(-j,-n_j),
eta^j=(B_j,b_j).                                      (1.2)
```

This is immediate from the endpoint inverse map:

```text
d=-v*(-j)+c*(-n_j)=B_j,
E=-u*(-j)+C*(-n_j)=b_j.                              (1.3)
```

Moreover `P_0=(0,-1)` corresponds to `(C,c)`, so its reflected endpoint is
the original anchor `(c,C)`.

Define a symmetric kernel `X(t,j)` to be one when an actual row `x` satisfies
the two middle hard windows

```text
8*x*b_t*B_j = q^3+O(qD),
8*x*B_t*b_j = q^3+O(qD).                             (1.4)
```

Then `X(t,j)=X(j,t)`, the anchor mask is exactly `X(t,0)`, and

```text
W(gamma)=sum_t X(t,0) sum_j X(t,j).                  (1.5)
```

Thus NDS is an anchored degree-sum theorem for one selected modular-orbit
graph.  A decomposition into two unrelated direction families throws away
this exact symmetry.

## 2. The whole orbit lies in one digital strip

The reconstruction formula gives

```text
n_t-(u/C)t=-b_t/C.                                   (2.1)
```

If the physical shell is `[L,U]`, then all centre tokens lie in

```text
-U/C <= n_t-(u/C)t <= -L/C.                         (2.2)
```

For the project width-`.2` shell, `(U-L)/C<1`.  Hence there is at most one
token over a fixed integer `t`.

This also corrects the raw direction count.  If

```text
P_t-P_s=(r,z),
```

then

```text
z-(u/C)r=-(b_t-b_s)/C.                               (2.3)
```

For fixed `r`, the right side ranges in an interval of length less than two,
so there are at most two integral `z`.  The physical orbit therefore has
only `O(D)` difference directions, not `O(D^2)` arbitrary ones.

More quantitatively, an `N`-term exact affine progression with step
`V=(r,z)` inside the strip must obey

```text
|r| << D/N,
|z-(u/C)r| << 1/N.                                   (2.4)
```

This is the correct Beatty/continued-fraction restriction on a rich lane.
It is useful for inverse classification, but it does not count translated
lane pairs.

## 3. Why the determinant theorem becomes globally vacuous

For two points of the same orbit, the reflected middle determinant is

```text
kappa(t,j)
 =det(P_t,-P_j)
 =b_t*B_j-B_t*b_j
 =(t*b_j-j*b_t)/C.                                   (3.1)
```

Consequently, whenever `|t|,|j|<<D` and all physical coordinates remain in
the fixed shell,

```text
|kappa(t,j)|<<D                                      (3.2)
```

for **every** pair `(t,j)`.  The small-determinant condition does not thin
the ambient orbit square at all.  The principal adjacent family

```text
P_t=(t,t-1),              -P_j=(-j,1-j)              (3.3)
```

is the literal model: it has `asymp D^2` primitive shell pairs satisfying
the determinant band before the radial/product diamond is restored.

The transverse fixed-chart theorem remains correct.  Its mixed coefficient
detects two different affine lane directions.  Globally, however, all
accepted cells already live in the near-parallel self-orbit collar `(3.2)`.
Splitting that collar into transverse subcharts cannot manufacture a saving
which the determinant predicate itself does not possess.

## 4. Directions are few; translated lanes are not

A width-one digital graph need not be one affine line.  For a fixed affine
direction it may meet many parallel translates, and the actual mask may
retain an arbitrary subset of those translates.  At an arm scale `N`, a
disjoint lane cover can have `O(D/N)` lanes on either side, hence as many as

```text
O(D^2/N^2)                                           (4.1)
```

translated Cartesian lane pairs.  A local bound of
`min(N^2,D q^o(1))` per pair does not sum below the ambient `D^2` ceiling.
The direction restriction `(2.4)` does not control this translation index.

This is visible in the audited full-integer digital strip with `289` orbit
points, `344` primitive difference directions, and largest exact affine line
of size `18`: even before either diamond, at least `17` exact lines are
needed.  It is also visible under literal hard windows in the multilevel
tangent construction: for one fixed anchor, `sqrt(D)` partner charts coexist,
each with `sqrt(D)` common completions.  Their true mass is `D`, but charging
the available `O(D)` fixed-chart capacity to each chart gives `D^(3/2)`.
Thus naive chart summation loses exactly `sqrt(D)` even on a legal
full-integer hard-window family.  That fixture is not on the actual
prime-power mask, so it is a method obstruction, not a counterexample to
NDS.

## 5. Exact remaining theorem

Put

```text
r_0(j)=sum_t X(0,t)X(t,j).                            (5.1)
```

Then `(1.5)` is `W(gamma)=sum_j r_0(j)`.  Shell injection gives `O(D)`
possible `j`, while the proved pointwise theorem gives

```text
r_0(j)<<sqrt(D)q^o(1).                               (5.2)
```

These facts yield only

```text
W(gamma)<<D^(3/2)q^o(1).                             (5.3)
```

The missing assertion is precisely

```text
#{j:r_0(j)>=R} << D/R*q^o(1).                        (5.4)
```

Equivalently, it is a mask-sensitive Carleson theorem for the symmetric
self-orbit kernel `(1.4)`.  A successful Beatty-lane proof must charge the
**translations and actual rounded rows** in `(1.4)`, not merely the rational
direction in `(2.4)`.  Proving `(5.4)` would prove NDS; no such charge follows
from the current fixed-chart determinant estimate.

```text
endpoint side is the reflected centre orbit:          PROVED;
anchor mask is the j=0 self-orbit edge:                PROVED;
middle kernel is symmetric:                            PROVED;
physical difference directions are O(D), not O(D^2): PROVED;
middle determinant is O(D) on the whole orbit square: PROVED;
width-one strip gives bounded translated-lane reuse:  FALSE AS A METHOD;
fixed-chart bounds sum with only q^o loss:             NOT PROVED;
actual-prime self-orbit Carleson bound:                OPEN;
sharp four-cycle bound:                                NOT PROVED.
```

The reflection, one-orbit cross-products, and the `289`-point width-one
strip obstruction are replayed in
`src/qp_scattered_token_search.py`,
`src/test_qp_scattered_token_search.py`, and
`lean/weilcert/QPScatteredTokenOrbitReflection.lean`.  The two focused
Python tests for those structural claims pass.
