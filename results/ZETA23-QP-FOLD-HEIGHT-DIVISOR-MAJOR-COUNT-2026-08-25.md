# Fold-height branch: a sharp divisor-major count

**Date:** 2026-08-25  
**Scope:** the exact branch `H-p*U=0` in the symmetric scaled-cusp chart  
**Verdict:** this entire branch has at most

```text
O(sqrt(A)*Q^o(1))
```

physical points in an arbitrary box `|e|<=A, |f|<=B`, with `A<=B`, in
the four-cycle energy core.  The proof is pointwise and therefore survives
arbitrary selected masks.  No averaging or cancellation is used.

This closes the counting question for the fourth affine-height branch.  It
does not prove the no-wrap phase-jet Bessel theorem or the sharp four-cycle
bound.

## 1. Exact setup

On `H-p*U=0`, with `0<|d|<p` and `gcd(p,d)=1`, the already-proved
parametrization is

```text
Q=p*L,                 g=d*a>0,
a*(p^2-d^2)+3w=2d*L,  y=d*L-w,                     (1.1)

4e=w*(a*(p-d)^2-w),
4f=w*(a*(p+d)^2-w).                                 (1.2)
```

The signs cause no loss.  When `d<0`, the integer `a=g/d` is negative, but

```text
x=p-d>0,                 z=p+d>0                    (1.3)
```

still hold.  We can consequently use the narrow left error `e` for both
orientations, without reflecting the asymmetric mask.

Reducing (1.1) modulo `x` gives the first exact factorization

```text
x*(2L+a*z)=2Q-3w.                                   (1.4)
```

Define the left residual

```text
eta=a*x^2-w,                 4e=w*eta.               (1.5)
```

Substituting `w=a*x^2-eta` into (1.1) gives the second exact
factorization

```text
2x*(a*(p+x)+L)=2Q+3eta.                             (1.6)
```

For completeness, the right-side analogues are

```text
z*(2L-a*x)=2Q+3w,
2z*(a*(p+z)-L)=3eta_+-2Q,
eta_+=a*z^2-w,                 4f=w*eta_+.           (1.7)
```

Only (1.4)--(1.6) are needed.

## 2. The small-`w` chart

Suppose

```text
|w|<=sqrt(A).                                        (2.1)
```

There are `O(sqrt(A))` possible integers `w`.  There are `Q^o(1)` choices
for `p`, because `p|Q`.  For each `(p,w)`, (1.4) says

```text
x | 2Q-3w.                                           (2.2)
```

The target is comparable with `Q` in the energy core, so it has `Q^o(1)`
divisors.  Once `(p,w,x)` is fixed, `d=p-x` is fixed and (1.4) fixes `a`
uniquely.  Thus this chart contributes

```text
O(sqrt(A)*Q^o(1)).                                   (2.3)
```

This includes `w=0`, where `e=f=0` and the divisor target is exactly `2Q`.
No square-content assertion is needed.

## 3. The large-`w` chart

Suppose `|w|>sqrt(A)`.  The narrow error and (1.5) imply

```text
|eta|<=4A/|w|<4sqrt(A).                              (3.1)
```

Hence there are again only `O(sqrt(A))` possible integer labels.  For each
`(p,eta)`, (1.6) gives

```text
x | 2Q+3eta.                                         (3.2)
```

Choosing this divisor fixes `d=p-x`; equation (1.6) then fixes `a`, and
finally (1.5) fixes `w=a*x^2-eta`.  The same divisor bound proves

```text
O(sqrt(A)*Q^o(1)).                                   (3.3)
```

The subcase `e=0`, `w!=0` has `eta=0` and target `2Q`; it is therefore not
exceptional.

## 4. Literal finite majorant and the energy margin

The proof gives the explicit upper bound

```text
tau(Q) * [
  sum_(|w|<=sqrt(A)) tau(|2Q-3w|)
  + sum_(|eta|<4sqrt(A)) tau(|2Q+3eta|)
].                                                    (4.1)
```

In the energy core

```text
Q asymp D^(33/16),       A=D*m,
1<=m<=M,                 m^2*M^3<sqrt(D).             (4.2)
```

Since `m<=M`, one has `m^5<sqrt(D)`, and therefore

```text
A<D^(11/10),             sqrt(A)<D^(11/20),
Q/sqrt(A)>>D^(121/80).                                (4.3)
```

Thus every target in (4.1) is nonzero and comparable with `Q`.  The uniform
divisor estimate turns (4.1) into

```text
# fold-height points <<sqrt(A)*Q^epsilon              (4.4)
```

for every fixed `epsilon>0`.

The case `d=0` is absent: primitivity would force `p=1`, while the defining
formulas give `H-pU=2g!=0`.  The endpoints `|d|=p` are outside the compact
two-inverse chart.

## 5. Status

```text
exact small-w divisor identity:                    PROVED;
exact large-w residual divisor identity:           PROVED;
signed-d/asymmetric-mask audit:                    PROVED;
w=0, e=0, nonsquare-content edge cases:            INCLUDED;
fold branch O(sqrt(A)Q^o(1)) in energy core:        PROVED;
no-wrap mask-sensitive phase-jet Bessel theorem:    OPEN;
sharp four-cycle bound:                             NOT PROVED.
```

Finite exact reconstruction and tests are in
`src/qp_fold_height_divisor_count.py` and
`src/test_qp_fold_height_divisor_count.py`.
