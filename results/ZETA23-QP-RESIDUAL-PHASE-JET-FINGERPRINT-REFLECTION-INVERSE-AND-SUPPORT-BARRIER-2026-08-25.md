# QP residual phase jets: an exact fingerprint, the reflection orbit, and the support barrier

**Date:** 2026-08-25  
**Verdict:** there is an exact mask-sensitive phase-jet fingerprint for the
genuinely transverse scaled-cusp residual.  At fixed `Q`, its lifted oriented
version recovers the primitive direction, slope error, and physical carrier;
the product bands then recover the content.  After forgetting orientation,
the only collision is the unavoidable reflection

```text
(y,r,s,d,n) -> (-y,s,r,-d,-n).                     (0.1)
```

This is a genuine inverse theorem, not merely a finite observation.  It also
survives the non-square-content, nonaxis family left by the algebraic peels.

It is not yet the physical large sieve.  One of the two canonical probes is a
primitive cubic stationary frequency of size `p^3`.  After the proved
residual floor `p>>D^(77/160)`, that frequency already exceeds the Fejer
cutoff `H=D^(17/16)`.  The regular probe of size `p^2` is physically present
only in the short strip

```text
D^(77/160) << p << D^(17/32).                       (0.2)
```

Thus the remaining breakthrough is a transference theorem: the physically
available nonlinear completion-action jets must control this virtual
fingerprint, or an equivalent one, modulo the integer Newton alias lattice.
The exact inverse algebra is now favorable; its stable Bessel realization is
open.  No sharp four-cycle bound is proved here.

## 1. Two canonical stationary phases

Let a reduced remote point have primitive data `(g,p,d,n)`, so

```text
n=p*y-Q*d,                 p>|d|>0,                 (1.1)
```

and put

```text
chi=gcd(p+d,p-d) in {1,2},
a=(p+d)/chi,               b=(p-d)/chi,
N=a+b=2p/chi,
t=(Q+y)/(2Q),              t_0=a/N.                 (1.2)
```

The physical displacement from the rational tangent is exactly

```text
t-t_0=n/(2Qp),             N*t-a=n/(chi*Q).         (1.3)
```

At `lambda=1/4`, consider the regular stationary phase

```text
Phi_2(t)=1/4*(a^2/t+b^2/(1-t))                     (1.4)
```

and the primitive cubic stationary phase

```text
Phi_3(t)=1/c_0*(a^3/t-b^3/(1-t)+N^3*t),
c_0=gcd(4,N^3).                                     (1.5)
```

Their integer frequencies in coordinates `(-m,h,k)` are

```text
xi_2=(0,a^2,b^2),
xi_3=(N^3/c_0,4a^3/c_0,-4b^3/c_0).                 (1.6)
```

Primitivity gives the useful parity identity

```text
c_0*chi^2=4.                                        (1.7)
```

The first phase has `Phi_2'(t_0)=0` and nonzero curvature.  The second has
`Phi_3'(t_0)=Phi_3''(t_0)=0` and nonzero third derivative.

These phases really see the two masks.  If `xi=(-m,h,k)` and

```text
(A,V,W)=(Q+y,Q-y+r,Q+y+s),
```

then `xi dot (A,V,W)` is integral, whereas the phase on the reciprocal curve
satisfies

```text
2Q*Phi(t)+h*e/(Q+y)+k*f/(Q-y)=xi dot (A,V,W).       (1.8)
```

Thus the curve action modulo one is the weighted pair of physical product
errors, not an invented outer character.

## 2. Exact quadratic and cubic action defects

Two elementary factorizations are decisive:

```text
Phi_2(t)-Phi_2(t_0)
 =-(N*t-a)^2/[4t(t-1)],                             (2.1)

Phi_3(t)-Phi_3(t_0)
 =(N*t-a)^3/[c_0*t(t-1)].                          (2.2)
```

Since

```text
t(t-1)=-(Q^2-y^2)/(4Q^2),                          (2.3)
```

the lifted physical action defects are exactly

```text
J_2:=2Q*(Phi_2(t)-Phi_2(t_0))
    =2Q*n^2/[chi^2*(Q^2-y^2)],                     (2.4)

J_3:=2Q*(Phi_3(t)-Phi_3(t_0))
    =-8n^3/[c_0*chi^3*(Q^2-y^2)].                  (2.5)
```

Using (1.7), their ratio collapses to

```text
J_3/(chi*J_2)=-n/Q.                                (2.6)
```

This is the arithmetic heart of the fingerprint: a quadratic and a cubic
phase response recover the signed first-order slope defect.

The regular tangent curvature is

```text
K_2:=Phi_2''(t_0)
    =N^4/(2ab)
    =8p^4/[chi^2*(p^2-d^2)].                        (2.7)
```

## 3. Exact inverse theorem

> **Residual lifted-jet inverse theorem.** Fix `Q` and an orientation.  On
> the locus `n!=0`, the four quantities
>
> ```text
> (chi,K_2,J_2,J_3)                                  (3.1)
> ```
>
> recover `(p,d,y,n)` exactly.  Replacing `J_3` by `|J_3|` recovers exactly
> the reflection orbit (0.1).  In a fixed compact collar and product bands
> of width `o(Q)`, there is at most one content `g` over each recovered
> oriented tuple.  Hence the full physical point is determined, up to
> reflection in the unoriented version.

The proof is short.  First,

```text
chi^2*K_2/8=p^4/(p^2-d^2).                          (3.2)
```

Since `(p,d)=1`, the fraction on the right is reduced.  Its numerator gives
`p^4`, and its denominator then gives `d^2`.  Thus `(chi,K_2)` recovers
`(p,|d|)`.

Next, (2.6) gives the signed integer `n`, and (2.4) gives

```text
Q^2-y^2=2Q*n^2/(chi^2*J_2).                        (3.3)
```

This recovers `|y|`.  Among the two signs, the equations

```text
d=(p*y-n)/Q,                 |d| already known      (3.4)
```

select exactly one when `n!=0`.  If the sign of `J_3` is forgotten, the two
solutions are precisely the reflected pair.

Finally, changing `g` by one changes the left product error by

```text
(p-d)*(Q+y)/2.                                      (3.5)
```

In the compact collar this is `>>Q`, while `A=o(Q)`.  Two contents cannot
both lie in the same narrow product band.  This completes the inverse.

This theorem also explains why a derivative-only mode theorem and a residual
classification theorem are complementary.  Completion-action derivatives
can identify `(h,k,m)` and its saddle, but the residual intercept still lives
in the affine action heights.  Equations (2.4)--(2.7) supply exactly that
missing arithmetic fingerprint.

### 3.1 What this adds beyond the `q_2,q_3,q_4` rigidity

The regular completion-action calculation concerns a **dual mode**: its
unwrapped nonlinear derivatives recover the saddle and `(h,k,m)`, while its
discrete quotient version leaves the physical reflection symmetry.  That
does not by itself recover which primal product-band point supplied the
affine intercept.  Distinct contents at the same tangent have the same mode
derivatives.

The theorem above concerns precisely that missing **primal packet** datum.
It turns the curve-minus-tangent actions and tangent curvature into

```text
(p,d,y,n,g),                                         (3.6)
```

with `g` supplied by narrow-band uniqueness, and proves that the reflection
seen in the `q_2,q_3,q_4` scan is a real infinite non-square residual family,
not a numerical accident.  It also rules out a second exact collision
component after the affine information is included.

Neither theorem supplies the stability estimate for near jets modulo the
Newton alias lattice.  The dual-mode rigidity plus this primal-packet inverse
is the proposed algebraic input to that still-missing estimate.

## 4. The unavoidable off-axis collision family

The reflection exception is not confined to the already closed axes.  Fix
integers `M>=2`, `d>2`, and put

```text
p=M*d+1,                    ell=p^2-d^2,
g=2d,
Q=(p*ell-1)/d,              y=ell,
r=d*(p-d),                  s=d*(p+d).              (4.1)
```

Then

```text
n=1,                        e=-(p-d),
f=-(p+d).                                           (4.2)
```

In the integral scaled-cusp coordinates `(z,v)` one has

```text
v=0,                        z=2d,
K=(z+d*v)*(z-d*v)=4d^2!=0.                          (4.3)
```

Moreover

```text
d^2 does not divide g=2d                                  (d>2).  (4.4)
```

Thus this family is simultaneously non-square-content, off the balanced
axis `z=0`, and off both one-band axes `K=0`.  Reflection gives another
physical point at the same `Q`.  Their unoriented fingerprints coincide
exactly:

```text
J_2(ref)=J_2,
J_3(ref)=-J_3,
K_2(ref)=K_2.                                       (4.5)
```

At the derivative level, the caustic slope and third derivative agree while
the curvature changes sign.  Consequently a theory that takes absolute
curvature, or otherwise quotients physical orientation, must explicitly
retain this two-point reflection orbit.  It cannot declare every transverse
collision to be one of the three deleted axes.

This is not a counterexample to the desired estimate: each orbit has size
two.  It is the correct exceptional graph for an inverse theorem.

## 5. Action alone is badly conditioned

The exact inverse needs the joint fingerprint.  A scalar action character is
far too coarse.  At `Q=349`, the two non-square transverse points

```text
(y,r,s)=(74,13,20),        (g,p,d,n)=(1,33,7,-1),
(y,r,s)=(102,23,42),       (g,p,d,n)=(1,65,19,-1)  (5.1)
```

have cubic defects

```text
J_3=1/116325,              J_3'=1/111397.           (5.2)
```

Their gap is much smaller than `1/Q`, hence much smaller than any available
completion resolution in this fixture.  Their curvatures (2.7), however,
are different and the joint fingerprints separate them exactly.

This behavior persists at the natural scale.  When `|n|=1` and
`|y|asymp Q`, one has

```text
J_2 asymp Q^(-1),          J_3 asymp Q^(-2).        (5.3)
```

So the inverse map is most ill-conditioned precisely on the smallest
nonzero slope defect.  Exact injectivity by itself cannot yield the Bessel
separation; curvature and higher completion-action differences must be used
quantitatively.

There is also a character-wrap warning.  In the broad diagnostic window
`A=B=max(10,floor(Q/8))`, exact nonreflection collisions of `dist(J_3,Z)`
occur at `Q=2736,2856,3762`.  For example, at `Q=2736` the lifted values

```text
24/7,                      -38/7                    (5.4)
```

have the same distance `3/7` to an integer.  The full fingerprint separates
them.  These wraps do not enter the asymptotic energy core: Section 6 shows
that `J_3=o(1)` there.

## 6. The lift count is affordable

In the worst energy cell,

```text
B=D^(7/6),                 Q=D^(33/16),
|n|<=2B/g.                                         (6.1)
```

Equations (2.4)--(2.5) give

```text
J_2 <<B^2/(g^2*Q),         exponent 13/48,
J_3 <<B^3/(g^3*Q^2),       exponent -5/8.           (6.2)
```

Thus the cubic character is automatically unwrapped.  The quadratic action
has at most

```text
O(1+B^2/(g^2*Q))                                           (6.3)
```

possible integral lifts.  Even at `g=1`, its exponent `13/48` is below the
smallest `sqrt(A)=D^(1/2)` packet budget by

```text
1/2-13/48=11/48.                                    (6.4)
```

Conditionally, therefore, if the physical quotient three-jet determines
`(chi,K_2,J_3,J_2 mod 1)` with bounded distortion, every jet-major-arc fiber
has only

```text
O((1+B^2/Q)*Q^epsilon)                              (6.5)
```

members, apart from the factor-two reflection orbit.  This is much smaller
than either the full anisotropic cluster allowance `A` or the square-root
algebraic packet allowance.  The arithmetic cluster count is not the
remaining numerical obstruction.

The word **conditionally** is essential: no physical intertwining with this
virtual fingerprint has been proved.

## 7. Why the virtual cubic cannot simply be inserted

The noncentral algebraic peels force

```text
p>>D^(77/160),                H=D^(17/16).           (7.1)
```

The regular frequency (1.6) has size `p^2`.  At the residual floor this is

```text
D^(77/80)=D^(H exponent-1/10),                      (7.2)
```

so it remains in support only until

```text
p<=H^(1/2)=D^(17/32).                               (7.3)
```

The width of this residual regular strip is only

```text
17/32-77/160=1/20.                                  (7.4)
```

The primitive cubic frequency has size `p^3`.  Already at the residual
floor its exponent is

```text
3*(77/160)=231/160,
231/160-17/16=61/160.                               (7.5)
```

It is outside the cutoff by a large power everywhere in the residual chart.
Therefore (2.5) is a **virtual phase-jet invariant**, not an available
Fourier column.

This is consistent with the separate physical phase-jet work: third finite
differences of a regular nonlinear stationary action can generate cubic
oscillation without requiring the primitive cubic-caustic frequency itself.
The theorem still needed is a stable comparison between those sampled
completion-action differences, modulo integer Newton polynomials, and the
arithmetic fingerprint above.

The regular action three-jet also has its own exceptional loci.  The
canonical `Phi_2` used here has `m=0`, while `Phi_3` is a fold; they lie on
the boundary of the global regular nonzero-dual three-jet inverse theorem.
This is why the two exact results cannot simply be substituted into each
other.  A successful proof must use regular physical modes to reproduce the
same inverse information away from the already controlled zero-dual and fold
charts.

## 8. Finite collision search

An exact integer scan used

```text
101<=Q<=4000,
A=B=max(10,floor(Q/8)),
|y|<=floor(Q/3),                                    (8.1)
```

and deleted

```text
n=0, L=0, d=0, z=0, K=0, and d^2|g.                (8.2)
```

It contained

```text
238640 oriented residual points
across 3838 nonempty centres.                       (8.3)
```

The results were:

```text
nonreflection collisions of lifted |J_3|:          0;
nonreflection collisions of the full fingerprint: 0;
nonreflection collisions of dist(J_3,Z):           3 centres;
```

with the three character wraps listed in Section 5.  This scan is evidence
for the formulas and catches the exact wrap pathology; the inverse theorem
of Section 3 does not depend on it.

## 9. Correct next theorem

The most concrete phase-jet/coherence inverse target is now:

> **Mask-sensitive quotient-jet transference.** On a full physical
> completion block, after quotienting by integer-valued Newton phases, every
> pair of regular residual packets either satisfies a first-, second-, or
> third-difference correlation estimate strong enough for the phase-jet
> Bessel theorem, or its sampled jet determines the lifted fingerprint
> `(chi,K_2,J_2,J_3)` up to `Q^o(1)` choices.

The exact work here predicts that the second alternative has cluster size at
most (6.5), with the reflection involution as its only geometric symmetry.
Proving the sampled-to-lifted stability, uniformly near `|n|=1`, folds, and
frequency endpoints, would turn the phase-jet Bessel dichotomy into the
desired mask-sensitive large sieve.

## 10. Reproducibility and status

The exact phases, reconstruction map, reflection family, finite residual
enumerator, collision audit, and exponent ledgers are in

```text
src/qp_residual_phase_jet_collision.py
src/test_qp_residual_phase_jet_collision.py
```

```text
quadratic/cubic action factorizations:              PROVED;
lifted oriented fingerprint inverse:                PROVED;
unoriented collisions equal reflection orbits:      PROVED;
non-square off-axis reflection family:              PROVED;
quadratic lift count D^(13/48):                     PROVED;
cubic action unwrapped in the energy core:           PROVED;
broad finite residual collision scan:               VERIFIED;
primitive cubic probe physically supported:         FALSE;
sampled quotient-jet to lifted-fingerprint transfer: OPEN;
mask-sensitive physical Bessel theorem:              OPEN;
sharp four-cycle bound:                              NOT PROVED.
```
