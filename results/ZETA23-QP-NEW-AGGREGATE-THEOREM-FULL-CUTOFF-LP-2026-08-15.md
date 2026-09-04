# QP four-cycle: full cutoff LP after aggregate relation averaging

**Date:** 2026-08-15  
**Verdict:** the new aggregate rank-one estimate improves the bounded-slice
parabolic branch to `D^(5/4)`, but no cutoff in
`P=lambda1*lambda2` improves the current global fourth-trace exponent
`11/8`.  Within the proved estimates, there is an exact high-product
plateau at

```text
lambda1=lambda2=D^(5/8),
P=D^(5/4),
K=D^(3/16),
m(C)<=D^(3/8).                                     (0.1)
```

The conclusion is an optimization barrier for the present inequalities,
not a construction attaining (0.1) with actual prime powers.

---

## 1. Exponent variables and feasible polytope

Write all scales as powers of `D`:

```text
q=D^Q,                    Q=33/16,
lambda1=D^a, lambda2=D^b, P=D^p,                  (1.1)
p=a+b,
lambda3=D^(Q-p).
```

Successive-minimum ordering gives

```text
0<=a<=b<=Q-p,
p/2<=b<=min(p,Q-p),
0<=p<=2Q/3=11/8.                                  (1.2)
```

The third-coordinate slice factor is

```text
K=1+DP/q=D^(kappa+o(1)),
kappa=(p-17/16)_+.                                (1.3)
```

---

## 2. Aggregate low-branch estimate with `K>1`

For a fixed dyadic `P` sector, the degenerate multi-slice estimate is

```text
m_e(C)<<K(1+sqrt(D/h)).                            (2.1)
```

Split total multiplicity at `M>>K`.  Low colors cost `MD`.  A high color
has

```text
h<<H:=D*K^2/M^2.                                  (2.2)
```

For directions of height `h~J<=sqrt(D)`, the new aggregate theorem gives
color mass `J*sqrt(D)`, while (2.1) gives multiplicity
`K*sqrt(D/J)`.  Their product is `K*D*sqrt(J)`.  The optimal threshold is

```text
M=D^(1/4)K,                 H=sqrt(D),             (2.3)
```

and both the low and high contributions are

```text
D^(5/4)K.                                           (2.4)
```

If one chooses a smaller `M`, the aggregate color estimate becomes its
trivial branch `D` above `J=sqrt(D)` and still gives `K*D^(5/4)` at the
turning point.  A larger `M` increases `MD`.  Thus (2.4) is the exact
optimizer furnished by the current aggregate estimate.  The bare `K` term
in (2.1) contributes only `KD`.

For a low cutoff `p<=tau`, use the largest slice factor in that sector.
Its fourth-trace exponent is therefore

```text
L(tau)=5/4+(tau-17/16)_+.                          (2.5)
```

---

## 3. Exact pointwise high-branch LP

The universal shear and parabolic slice estimates give, at fixed `(p,b)`,
the multiplicity exponent

```text
mu(p,b)=min( (1-b)_+,
             (p-17/16)_+ +(1-(p-b))_+/2 ).         (3.1)
```

The harmless `+1` terms are exactly the positive parts in (3.1).  Over the
polytope (1.2), the relevant variables at every optimizer are below one.
The one-dimensional linear program

```text
mu(p)=max_(p/2<=b<=min(p,Q-p)) mu(p,b)             (3.2)
```

has the exact solution

```text
mu(p)= 1/2,                 0<=p<=1/2;
       (2-p)/3,             1/2<=p<=17/16;
       (p-1/8)/3,           17/16<=p<=5/4;
       1-p/2,               5/4<=p<=11/8.          (3.3)
```

For the two middle pieces, the optimizer is the intersection of the two
affine terms in (3.1).  Above `p=5/4` that intersection falls below the
constraint `b>=p/2`, so the optimizer is the balanced boundary `b=p/2`.
The unique maximum after `p=7/8` is

```text
mu(5/4)=3/8,              a=b=5/8.                (3.4)
```

Consequently the high-tail multiplicity exponent is

```text
B(tau)=sup_(p>=tau) mu(p)
 =1/2,                    0<=tau<=1/2;
  (2-tau)/3,              1/2<=tau<=7/8;
  3/8,                    7/8<=tau<=5/4;
  1-tau/2,                5/4<=tau<=11/8.          (3.5)
```

The corresponding fourth-trace exponent is `1+B(tau)` because the global
determinant-layer color mass is `D`.

---

## 4. Cutoff optimization

A split at `P=D^tau` therefore proves the exponent

```text
F(tau)=max(L(tau),1+B(tau)).                       (4.1)
```

The high branch equals `11/8` throughout `7/8<=tau<=5/4`.  The aggregate
low branch obeys `L(tau)<=11/8` exactly when

```text
tau<=19/16.                                        (4.2)
```

Thus

```text
min_(0<=tau<=11/8) F(tau)=11/8,                   (4.3)
```

and the full interval of minimizing cutoffs is

```text
7/8<=tau<=19/16.                                   (4.4)
```

The old cutoff `tau=17/16`, corresponding to `P=q/D`, lies inside this
plateau but is no longer uniquely preferred.  Moving it up through
`19/16` spends exactly the new low-branch saving; moving beyond `19/16`
makes (2.5) exceed `11/8`.  Moving below `7/8` exposes small-`P` pointwise
configurations with multiplicity above `D^(3/8)`.

---

## 5. Why the aggregate gain stops at the balanced witness

At (3.4),

```text
kappa=5/4-17/16=3/16,
h>=lambda1=D^(5/8)>sqrt(D).                        (5.1)
```

The new relation-mass estimate is

```text
min(D,h*sqrt(D))=D,                               (5.2)
```

so it has already reverted to the determinant-layer bound.  Meanwhile

```text
K*sqrt(D/h)=D^(3/16)*D^(3/16)=D^(3/8),
D/lambda2=D^(3/8).                                (5.3)
```

Both proved pointwise mechanisms meet exactly.  Any exponent below `11/8`
therefore needs a new estimate in this balanced high-`P` sector: for
example, a coupling that saves in the slice factor `K`, a relation-mass
gain for heights above `sqrt(D)`, or extra arithmetic excluding simultaneous
saturation of (5.2)--(5.3).  Changing only the `P` cutoff cannot do it.

```text
aggregate multi-slice optimizer D^(5/4)K:           PROVED;
exact fixed-p pointwise LP:                          PROVED;
minimum cutoff exponent 11/8:                        PROVED;
global improvement below 11/8 from current bounds:  NO;
actual saturation by prime-power colors:             NOT CLAIMED.
```

The rational exponent ledger is replayed in
`src/qp_four_cycle_cutoff_lp.py` and its test module.
