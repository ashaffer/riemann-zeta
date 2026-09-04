# QP broad rectangles: third differences and the two-label obstruction

**Date:** 2026-08-24  
**Verdict:** fixing both completion directions and the mixed carrier label
does force all bases into an interval of length `O(D/t)`.  A fixed nonzero
completion determinant also has only `D^(3/2+o(1))` possible direction
pairs.  These are genuine gains, but summing the mixed labels restores the
missing base multiplicity.

An exact quadratic lattice fixture shows that `(t,Delta)` divisor counting
alone cannot prove the packet-free `D^(5/2)` energy bound: it has
`D^(3-o(1))` broad rectangles, no three-point full affine packet,
`Delta=0`, and `t asymp r*s/q`.  The fixture deliberately violates the
individual product bands, so it is a proof-mechanism obstruction and not a
physical counterexample.  The remaining theorem must use those individual
bands across different bases, not only their mixed labels.

No packet-free energy theorem or sharp four-cycle estimate is claimed.

## 1. Fixed mixed label forces base clustering

Consider two occupied broad rectangles with the same completion directions
`r,s` and bases separated by the completion displacement `u`.  Suppose they
also have the same integer mixed carrier label

```text
t=Box_(r,s) v.                                        (1.1)
```

Their eight points form an additive cube.  Equality of the two labels says

```text
Box_(u,r,s) v=0.                                      (1.2)
```

Here `u,r,s` are signed, nonzero integer displacements and all eight cube
vertices lie in the fixed positive shell.  The conclusions below concern
absolute values, so no common-sign assumption is used.

Write `v(z)=C/z+epsilon(z)`, where `C asymp q^2` and
`|epsilon(z)|<<D/q`.  Repeated finite differences have the integral form

```text
Box_(u,r,s) (C/z)
 =-6*C*u*r*s * integral_[0,1]^3
   (a+theta_1*u+theta_2*r+theta_3*s)^(-4) dtheta.     (1.3)
```

Every point in the integration box is a convex combination of the eight
shell vertices.  Consequently

```text
|Box_(u,r,s) (C/z)| asymp |u*r*s|/q^2,                (1.4)
|Box_(u,r,s) epsilon|<<D/q.                           (1.5)
```

Equations `(1.2)--(1.5)` prove

```text
|u|<<D*q/|r*s|.                                       (1.6)
```

For a broad rectangle, the second mixed-difference identity gives

```text
|t|asymp |r*s|/q,                                     (1.7)
```

so every pair of bases with fixed `(r,s,t)` satisfies

```text
|u|<<D/|t|.                                           (1.8)
```

Thus all such base completions lie in one `a`-interval of length
`O(D/|t|)`; this is pairwise clustering, not merely a union of separated
clusters.

There is a useful inverse-chart version.  If `w` is the signed inverse step
and

```text
J<<1+|w|*D/q                                          (1.9)
```

is the number of unwrapped branches, each branch meets an `a`-interval of
length `L` at most `O(1+L/|w|)` times.  Therefore

```text
B(r,s,t)
 <<(1+|w|*D/q)*(1+D/(|t|*|w|)).                      (1.10)
```

At the local-beta endpoint `w=D^(73/64)`, the first factor is
`D^(5/64+o(1))`.  Uniformly one also has the elementary consequence

```text
B(r,s,t)<<1+D/|t|.                                   (1.11)
```

This last bound follows directly because the distinct integer base
completions lie in the interval from `(1.8)`; it is not obtained by
discarding factors from `(1.10)`.

In particular, every label with `|t|>=sqrt(D)` has at most `O(sqrt(D))`
bases.  The unresolved labels are `1<=|t|<sqrt(D)`.

## 2. Exact determinant coordinates and a fixed-label bound

Let `u_0=x^(-1) (mod y)`.  Write a completion direction in the determinant-
`y` lattice as

```text
r=u_0*d-y*m,             |d|<<D, |m|<<D.             (2.1)
```

For a second direction `s=u_0*e-y*n`, put
`p=(x*r-d)/y` and `ell=(x*s-e)/y` for the corresponding directions in the
other completion coordinate.  The completion determinant is exactly

```text
Delta=r*ell-p*s=(d*s-e*r)/y=e*m-d*n.                  (2.2)
```

Thus the direction labels are ordinary integer vectors `z=(m,d)` in a
`D`-box, with `Delta=det(z,z')` for `z'=(n,e)`.

### Lemma 2.1 (fixed nonzero determinant)

If `Z` is any set of `O(D)` nonzero integer vectors in a `D`-box and
`Delta!=0`, then

```text
#{(z,z') in Z^2:det(z,z')=Delta}
 <<D^(3/2)*tau(|Delta|).                              (2.3)
```

**Proof.**  Write `z=g*p`, with `p` primitive.  The determinant equation
forces `g|Delta`.  For fixed `p` and `g`, all possible `z'` lie on one
affine lattice line of direction `p`, so their number in the box is

```text
O(1+D/||p||_infinity).                               (2.4)
```

For each divisor `g`, at most `O(D)` distinct primitive vectors occur.
There are `O(R^2)` primitive vectors of norm at most `R`, whence for any
`O(D)` distinct primitive vectors

```text
sum_p 1/||p||_infinity<<sqrt(D).                      (2.5)
```

Summing `(2.4)` over `p` and then over `g|Delta` proves `(2.3)`. `square`

The zero determinant is exceptional: `D` vectors on one primitive ray give
`D^2` zero-determinant pairs.  This is exactly the completion-collinear
sector left by two-point secants.

## 3. Why the gains do not sum to `D^(5/2)`

For fixed directions, the reciprocal mixed phase ranges through

```text
O(1+|r*s|/q)                                         (3.1)
```

integer labels as the base traverses the shell.  Multiplying this by the
elementary fixed-label cluster size from `(1.8)` gives

```text
(|r*s|/q)*(D*q/|r*s|) asymp D.                       (3.2)
```

Thus summing `t` exactly restores the trivial possible number of bases for
one direction pair.  Lemma 2.1 counts direction pairs for fixed nonzero
`Delta`.  Equation `(2.2)` and the shell bounds `|r|,|s|<<q` give
`|Delta|<<D`, so `Delta` has `O(D)` values; it still does not restrict the
base.
No combination of `(1.10)` and `(2.3)` removes the factor in `(3.2)`.

The same issue appears in higher mixed differences.  Two bases with the
same `t` produce the useful zero third difference `(1.2)`; bases with
different `t` need not.  Additive energy can be supported on isolated
two-point secants at each label, so packet-freeness does not identify those
bases.

## 4. A sharp two-label fixture

Let `L` tend to infinity and put

```text
y=L^2+1,                    x=L^2-L+1.                (4.1)
```

Then `(x,y)=1` and

```text
x*L-y*(L-1)=1.                                      (4.2)
```

Take `Q=2y`, `D_Q=Q^(16/33)`, and any integer
`N<=c D_Q`; in particular `N=o(L)`.  For `0<=j<N`, define

```text
k_j=j,
a_j=y+L*j,
b_j=x+(L-1)*j,
v_j=L^2-L*j+j^2.                                    (4.3)
```

All four coordinates are `(1+o(1))*Q/2`, and `(4.2)` gives the exact defect
identity

```text
x*a_j-y*b_j=j.                                       (4.4)
```

The single `j=0` point may be deleted if only nonzero physical defect labels
are permitted; every asymptotic count below is unchanged.

The projection `(k_j,v_j)=(j,L^2-Lj+j^2)` lies on a nondegenerate parabola.
Therefore no affine line contains three full points `(k_j,a_j,b_j,v_j)`:
the fixture is packet-free in the literal three-point sense.

For a parameter rectangle with base `j` and positive increments `h,l`,

```text
r=L*h,                 s=L*l,
p=(L-1)*h,             ell=(L-1)*l,                 (4.5)
Delta=r*ell-p*s=(h*s-l*r)/y=0,                        (4.6)
t=v_j+v_(j+h+l)-v_(j+h)-v_(j+l)=2*h*l.              (4.7)
```

In particular

```text
t*L^2=2*r*s,             so t asymp r*s/Q.           (4.8)
```

Every positive pair `h,l` is broad once the harmless fixed constant in
`|rs|>>Q` is chosen below `1/2`.  The exact number of bases and positive
direction pairs is

```text
sum_(h,l>=1) max(N-h-l,0)=binom(N,3)asymp N^3.       (4.9)
```

The complete additive energy is

```text
E^+([0,N-1])=(2*N^3+N)/3.                            (4.10)
```

Even fixing `t` leaves the base factor: `(4.7)` reconstructs `(h,l)` up to
the divisor function, while each admissible pair has `asymp N` translates.
Thus the pair of labels `(t,Delta)` can have perfect divisor control and
still coexist with `N^(3-o(1))` broad energy.

### Exact scope of the fixture

This is not an actual product-band counterexample.  Indeed

```text
a_j*v_j
 =L^4+L^2+L*j^3+j^2-L*j.                            (4.11)
```

At `j asymp N asymp D_Q`, the cubic drift is

```text
L*N^3=L^(129/33+o(1)) >>D_Q=L^(32/33+o(1)).         (4.12)
```

So more than the first two points cannot lie in one physical width-`D_Q`
product band.  The fixture preserves the shell, coprime endpoint lattice,
exact Freiman defect map, broad mixed-label scale, determinant label, and
packet-free condition; it intentionally fails precisely the individual
reciprocal bands.  It proves that a successful `(BR)` argument must use
those bands coherently across bases.  Counting only `t`, `Delta`, and
packet lines cannot work.

## 5. Status

```text
fixed-(r,s,t) base diameter O(D/t):              PROVED;
inverse-chart fixed-label bound (1.10):          PROVED;
fixed nonzero-Delta direction bound D^(3/2+o):   PROVED;
summed t,Delta label theorem at D^(5/2):          NOT OBTAINED;
packet-free quadratic two-label obstruction:     EXACT INTEGER FIXTURE;
fixture satisfies physical product bands:        NO;
broad reciprocal rectangle theorem (BR):         OPEN;
```

Executable replay:

```text
src/qp_broad_rectangle_label_fixture.py
src/test_qp_broad_rectangle_label_fixture.py
```
