# QP Airy shifts: exact vector Plancherel, fixed-lattice closure, and the completion repetition no-go

**Date:** 2026-08-25  
**Verdict:** the missing `sqrt(H/d)` factor on one genuinely localized
curvature layer of one fixed normal lattice is an exact finite-dimensional
theorem.  Vector-valued Plancherel recovers it for arbitrary complex layer
values, arbitrary deletion, and arbitrary contractive coefficient vectors.
At the Airy scale `d=J=D^(1/48)`, it lowers the amplitude
`D^(49/48)` exactly to the target `D^(1/2)`.

This corrects the earlier conclusion that Fourier spread by itself leaves an
unavoidable fixed-lattice Airy loss.  The spread is harmful under `l1`
summation, but harmless when the two exact Parseval identities and the
physical layer support are retained.

Two qualifications are essential.

1. Smoothness or derivative bounds without actual layer localization do
   not imply the gain.  Positive and complex amplitudes can concentrate a
   Fourier shift exactly on a major character.
2. The fixed-lattice theorem does not create orthogonality in the physical
   completion variable `S`.  Repeating one legal fiber at `L` completions
   costs exactly `sqrt(L)`.  A genuine completion character, with bounded
   label multiplicity, or another outer Bessel theorem is still required.

Consequently this closes the local Airy amplitude problem, not the global
varying-chart/mask intertwining, reciprocal-strip restriction theorem, or
the sharp four-cycle bound.

## 1. Exact vector shifted-orbit theorem

Let

```text
G=(Z/MZ)^2                                               (1.1)
```

and let `A:G->C`.  Let `b_(h,k)` be arbitrary vectors in a Hilbert space,
with arbitrary entries deleted.  Define

```text
Ahat(u,v)=M^(-2) sum_(h,k in G)
 A(h,k)e_M(-u*h-v*k),                                  (1.2)

O(u,v)=sum_(h,k in G)b_(h,k)e_M(u*h+v*k).              (1.3)
```

The field `b` may include a normal-lattice congruence, arbitrary phases,
primal mask deletion, and contractive internal vectors.  Finite Fourier
inversion gives

```text
sum_(u,v) Ahat(u,v) O(u,v)
 =sum_(h,k) A(h,k)b_(h,k).                             (1.4)
```

The two Parseval identities are

```text
sum_(u,v)|Ahat(u,v)|^2
 =M^(-2)sum_(h,k)|A(h,k)|^2,                           (1.5)

sum_(u,v)||O(u,v)||^2
 =M^2 sum_(h,k)||b_(h,k)||^2.                          (1.6)
```

Cauchy--Schwarz in the shift variables therefore proves the exact
coefficient-uniform theorem

```text
||sum_(u,v) Ahat(u,v)O(u,v)||
 <=||A||_(l2(G))*||b||_(l2(G)).                        (1.7)
```

This is also immediate from the right side of (1.4), but (1.5)--(1.6)
explain precisely where the desired shifted-character square function
comes from.  No sign, positivity, Fourier localization, or scalar
coefficient assumption is used in (1.7).

For the normal-lattice problem, take

```text
b_(h,k)=c_h*c_k*1_Lambda(h,k)*e(h*alpha+k*beta)*v_(h,k), (1.8)
```

where `Lambda` is any selected congruence subset and
`||v_(h,k)||<=1`.  For the height-one Fejer coefficients

```text
c_h=(H-|h|)/H^2,              |h|<H,                 (1.9)
```

one has the exact identity

```text
sum_h c_h^2=(2H^2+1)/(3H^3)<=1/H.                   (1.10)
```

Thus

```text
||b||_2<=sum_h c_h^2<=1/H                            (1.11)
```

uniformly under every deletion and contraction.

## 2. A localized curvature layer recovers the missing square root

Suppose the dyadic curvature symbol `A_d` is genuinely supported on a strip

```text
E_d subset {|h|,|k|<H},
#E_d<<d*H,                 |A_d(h,k)|<<sqrt(q/d).    (2.1)
```

The cardinality in (2.1) is the ordinary lattice count for a strip of width
`d` in the primitive normal-frequency coordinate and length `H` in the
tangent coordinate.  It is precisely the support statement implicit in a
smooth cutoff to one curvature layer; a derivative bound alone is weaker
and is treated in Section 4.

Equations (1.7), (1.10), and (2.1) give

```text
|S_(A_d)|
 <<sqrt(q/d)*sqrt(d*H)/H
 =sqrt(q/H).                                          (2.2)
```

This is the required gain

```text
sqrt(d/H)                                             (2.3)
```

over the Fourier-algebra estimate `sqrt(q/d)`.  It is hereditary under
arbitrary packet deletion and remains valid for Hilbert-valued contractive
coefficients.

There is an even stronger scalar/fiberwise estimate when only coordinatewise
Fejer domination is needed.  Since

```text
|c_h*c_k|<=H^(-2),                                   (2.4)
```

triangle inequality on the layer gives

```text
|S_(A_d)|<<sqrt(q/d)*(d/H).                          (2.5)
```

Estimate (2.2), rather than (2.5), is the robust vector square-function
statement requested by the operator architecture.  Formula (2.5) is useful
as a check on scalar fixed-fiber normalizations but is not substituted for
the later global operator bookkeeping.

## 3. Exact Airy exponent closure

At the critical endpoint,

```text
q=D^(33/16),       H=D^(17/16),
J=(H^2/q)^(1/3)=D^(1/48),
A_Airy=D^(49/48).                                    (3.1)
```

The Fourier spread is

```text
H/J=D^(25/24),                                       (3.2)
```

but the `l2` layer factor in (2.3) is

```text
sqrt(J/H)=D^(-25/48).                                (3.3)
```

Therefore

```text
D^(49/48)*D^(-25/48)=D^(24/48)=D^(1/2).             (3.4)
```

The fixed-lattice vector theorem reaches the target exactly.  There is no
power slack at this stage.  The coordinatewise scalar factor `J/H` would
instead give

```text
D^(49/48)*D^(-50/48)=D^(-1/48),                     (3.5)
```

which confirms that the spread loss in the earlier `l1` Fourier estimate
was an artifact of discarding the original layer support.

The theorem is not special to `J`.  Every quadratic curvature layer with
amplitude `sqrt(q/d)` satisfies the same right side `sqrt(q/H)`.

## 4. Exact hostile boundaries

### 4.1 Smoothness without support is insufficient

Take `A(h,k)=1` on all of `G` and let `b` be a positive singleton at
`(0,0)`.  Every derivative of `A` vanishes, its DFT is concentrated at one
shift, and

```text
sum A*b=1.                                            (4.1)
```

There is no factor `sqrt(d/H)` for any declared `d<H`.  Thus the statement

```text
"A varies no faster than scale d"
  => square-root spread gain                          (4.2)
```

is false.  The actual support/cardinality hypothesis in (2.1), or an
equivalent `l2` norm bound, is indispensable.

The same example shows that a completely arbitrary coefficient field cannot
be allowed under only an `l1` normalization: a singleton coefficient
concentrates all mass on one shifted character.  What the physical Fejer
weights supply is exactly the `l2` estimate (1.11).

### 4.2 Positive amplitudes can place Fourier mass on a chosen shift

For any `(u_0,v_0)`, the amplitude

```text
A(h,k)=1+cos(2*pi*(u_0*h+v_0*k)/M)                   (4.3)
```

is nonnegative and has normalized DFT masses

```text
1, 1/2, 1/2                                          (4.4)
```

at shifts `(0,0),(u_0,v_0),(-u_0,-v_0)`.  Hence
positivity does not prevent a low Fourier mode from translating an affine
intercept exactly onto a major character.  Localization, not positivity,
is the mechanism behind (2.2).

### 4.3 An actual transverse nonsquare primal fixture

There is an infinite integral family

```text
g=1+637*j,
Q=349+223080*j,
y=74+47320*j,
r=13*g,                 s=20*g,              j>=0.  (4.5)
```

Its exact reduced data are

```text
(p,d,n)=(33,7,-1),
e=23+14703*j,          f=24+15340*j,
T=118.                                                   (4.6)
```

Since `g==1 (mod 49)`, square content `d^2|g` never occurs.  In the scaled
cusp coordinates every member has

```text
v=-4,             z=-146,
(z+d*v)(z-d*v)=20532,
z+p*v=-278.                                             (4.7)
```

Thus it is off the balanced, both one-band, fold-height, and square-content
branches.  This is a broad-mask physical fixture, not an energy-core family.

The primitive tangent direction is

```text
(R,-P_0,K_0)=(270400,-184041,435600),                (4.8)
```

and the affine intercepts are, modulo integers,

```text
alpha=921447/1600,
beta =-161179/676.                                   (4.9)
```

Both denominators divide `R`.  On every torus of size `M=R*L`, one Fourier
shift therefore makes `alpha+u/M` and `beta+v/M` integers simultaneously.
For the positive amplitude (4.3), one of its `1/2` Fourier masses lands on
that exact major orbit.  Since the height-one Fejer orbit is nonnegative and
its `j=0` term is one, the transferred value has a contribution at least

```text
1/(2R).                                               (4.10)
```

As `L` grows, this contradicts any universal `sqrt(d/M)` gain based only on
smoothness or positivity.  It does not contradict (2.2), because (4.3) is
supported on the full torus rather than on `O(dH)` sites.

## 5. Why completion-`S` orthogonality remains open

The theorem in Section 1 applies fiberwise for every fixed normal lattice
and every fixed completion.  It does not say that different completion
fibers are orthogonal.

The exact hostile model is rank one.  Let one legal synthesis row be
`r=(r_i)`, and repeat it at `L` completion values:

```text
(Tx)(S)=sum_i r_i*x_i,          1<=S<=L.             (5.1)
```

As a map into unnormalized `l2(S)`,

```text
||T||=sqrt(L)*||r||_2.                               (5.2)
```

Thus tensoring the fixed-lattice theorem with the completion set costs
exactly `sqrt(L)` unless a new character or Bessel mechanism is present.

If the rows instead carry genuine normalized completion characters

```text
psi_ell(S)=L^(-1/2)e_L(ell*S),                       (5.3)
```

their Gram matrix is exactly

```text
<psi_ell,psi_ell'>=1_(ell==ell' mod L).              (5.4)
```

Its norm is the maximum multiplicity of one completion label.  Equation
(5.4) states the remaining global theorem precisely: after stationary
partitioning and chart transport, the physical packets must retain genuine
completion labels with controlled fibers.  The fixed-lattice shift variable
`(u,v)` cannot be declared to be this label; the tangent chart, intercept,
and `C/S^2` all vary with `S`.

The repetition model (5.1) is an obstruction to an automatic implication,
not an actual-prime counterexample.  It proves that completion orthogonality
requires additional physical information.

## 6. Consequences and status

The corrected Airy architecture is now:

1. decompose the stationary symbol into genuine primitive-normal curvature
   layers;
2. retain their `O(dH)` support and apply vector Plancherel (1.7);
3. use (2.2) to remove the local `sqrt(H/d)` amplitude loss;
4. transport the resulting rows through the physical completion variable;
5. prove the completion-label Bessel/multiplicity statement (5.4) while
   summing varying tangent charts.

Steps 1--3 close the fixed-normal-lattice Airy shift problem.  Steps 4--5
are not consequences of finite Fourier algebra and remain the global
intertwining problem.

The finite identities, exponent ledger, hostile amplitudes, completion
repetition audit, and actual residual fixture are implemented in

```text
src/qp_airy_shift_square_function.py
src/test_qp_airy_shift_square_function.py
```

```text
vector shifted-field Parseval identity:               PROVED EXACTLY;
arbitrary complex localized-layer square function:    PROVED;
fixed-lattice sqrt(H/d) recovery:                      PROVED;
Airy D^(49/48) reduced to D^(1/2):                    PROVED, NO SLACK;
gain from smoothness without support:                  FALSE;
gain for arbitrary concentrated coefficients:         FALSE;
positive amplitude avoids major shifted character:    FALSE;
transverse nonsquare primal shift fixture:             PROVED;
automatic orthogonality across completion S:           FALSE ABSTRACTLY;
physical completion-label Bessel intertwining:         OPEN;
global varying-chart Airy aggregate:                    OPEN;
sharp four-cycle bound:                                NOT PROVED.
```
