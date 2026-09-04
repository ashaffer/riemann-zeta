# QP phase-jet inverse theorem and the fourth affine-height branch

**Date:** 2026-08-25  
**Scope:** symmetric reciprocal chart, exact completion action, lifted affine
heights  
**Verdict:** the proposed phase-jet idea has an exact algebraic core.  A
regular completion action is uniquely determined by its first three
derivatives.  The rational inverse degenerates only on the zero-Poisson
branch.  Endpoint and cubic-fold modes are the other two places where the
regular action itself degenerates.

There is a complementary quotient theorem: even after discarding `J'`, the
three nonlinear derivatives `(J'',J''',J'''')` recover the saddle response
up to physical left-right reflection.  Its quantitative Jacobian degenerates
only on the same zero-Poisson branch.

The universal scaled-cusp factors have a direct geometric meaning: they are
exactly the two affine-intercept defects from the rational tangent.  The
left endpoint, right endpoint, and zero-Poisson normals probe the already
peeled loci

```text
z=-d*v,             z=d*v,              z=0.
```

The cubic-fold normal probes one additional invariant,

```text
H-p*U=0,             equivalently z=-p*v.            (0.1)
```

This fourth branch is real and does not force square content.  It does force
`p|Q` and `d|g`, and it has an exact two-error factorization.  Splitting its
shared parameter at `sqrt(A)` proves that its entire fixed-centre count is
`O(sqrt(A)Q^epsilon)` in the remaining energy collar.  Thus all four exact
degenerate affine-height branches are now inside the packet budget.

There is also an exact warning.  If the first action derivative is discarded
and arbitrary independent affine slopes are allowed, the second and third
derivatives admit a rational mirror involution.  Thus a successful
phase-jet Bessel theorem must retain the full physical action slope; orders
two and three alone do not separate packets.

No scalar Fourier orthogonality, aggregate Bessel inequality, reciprocal-
strip restriction theorem, or sharp four-cycle bound is claimed.

## 1. The physical completion action

Fix `C>0` and a completion sum `S`.  The Poisson phase is

```text
F(S,a)=C*h/a+C*k/(S-a)-m*a.                          (1.1)
```

Let

```text
r=p+d,       s=p-d,       t_0=r/(2p),
a_0=S*r/(2p),             b_0=S*s/(2p).             (1.2)
```

Stationarity at this point is exactly

```text
m=(4*C*p^2/S^2)*(k/s^2-h/r^2).                      (1.3)
```

Let `J(S)` be the critical value obtained by continuing this critical point
while `C,h,k,m` remain fixed.  Put

```text
mathsf H=h/a_0^3,       mathsf K=k/b_0^3,
mathsf T=mathsf H+mathsf K.                          (1.4)
```

Implicit differentiation and the envelope theorem give

```text
J'  =-C*k/b_0^2,
J'' =2*C*mathsf H*mathsf K/mathsf T,

J'''=-6*C*mathsf H*mathsf K
       *(mathsf K^2/a_0+mathsf H^2/b_0)/mathsf T^3. (1.5)
```

These are exact identities, not stationary-phase asymptotics.  The saddle
response is

```text
da_0/dS=mathsf K/mathsf T,
db_0/dS=mathsf H/mathsf T.                           (1.6)
```

Writing

```text
mathcal F=h*s^3+k*r^3,                               (1.7)
```

the complete closed form is

```text
J   =(4*C*p/S)*(h/r-k*d/s^2),
J'  =-4*C*p^2*k/(S^2*s^2),
J'' =16*C*p^3*h*k/(S^3*mathcal F),

J'''=-96*C*p^4*h*k*(k^2*r^5+h^2*s^5)
       /(S^4*mathcal F^3).                           (1.8)
```

Thus the endpoint modes are `h*k=0`, and the cubic fold is exactly
`mathcal F=0`, in agreement with the earlier stationary discriminant.

### 1.1 Exact dependence on `S/Q`

For the physical centre `C=Q^2`, put

```text
sigma=S/(2Q).                                        (1.9)
```

Then the tangent intercepts and stationarity relation are

```text
alpha_0=2Q*p/(sigma*r),
beta_0=-2Q*p*d/(sigma*s^2),

m=sigma^(-2)*p^2*(k/s^2-h/r^2),                    (1.10)
```

and `J=h*alpha_0+k*beta_0`.  Derivatives in the normalized completion
coordinate obey

```text
dJ/dsigma       =-2Q*p^2*k/(sigma^2*s^2),
d^2J/dsigma^2   = 8Q*p^3*h*k/(sigma^3*mathcal F),
d^3J/dsigma^3   =-48Q*p^4*h*k*(k^2*r^5+h^2*s^5)
                   /(sigma^4*mathcal F^3).           (1.11)
```

A genuinely affine outer completion character changes only `J` and `J'`.
It cannot change (1.5)'s second and third derivatives.  Conversely, one may
not assign a different artificial affine slope to every packet: Section 3
shows that doing so destroys injectivity.

## 2. Exact three-jet inversion

Assume `J'J''!=0` and the saddle is regular.  Define directly from its
action jet

```text
q_1=-J'/C,             R_2=J''/(2C),
c=R_2/q_1,             R_3=-J'''/(3J'').            (2.1)
```

Then the right critical coordinate is recovered by the rational formula

```text
b_0=(R_3*S-1)/(R_3+c^2*S-2c),       a_0=S-b_0.      (2.2)
```

After this,

```text
mathsf K=q_1/b_0,
mathsf H=R_2*mathsf K/(mathsf K-R_2),
k=q_1*b_0^2,          h=mathsf H*a_0^3,
m=C*(q_1-h/a_0^2).                                  (2.3)
```

Hence `(J',J'',J''')` uniquely determines the critical position and the
whole real frequency triple.

The inverse denominator has two exact factorizations:

```text
R_3+c^2*S-2c
 =(1-c*S)^2/a_0
 =m^2/(C^2*a_0*b_0^2*mathsf T^2).                  (2.4)
```

It vanishes precisely when `m=0`.  The complete exceptional list for this
three-jet inverse is therefore

```text
h=0 or k=0:          one-inverse/endpoint mode;
mathcal F=0:          cubic fold;
m=0:                  zero-Poisson mode.             (2.5)
```

On every compact subregion separated from (2.5), (2.2)--(2.3) are rational
functions with denominators bounded away from zero.  The ordinary mean
value theorem consequently gives a quantitative inverse statement: two
near-equal first-three jets have nearby saddle positions and frequency
labels, with a loss polynomial in the reciprocal endpoint, fold, and
zero-Poisson separations.  Near the fold, `mathsf T` is small but (2.4)'s
denominator grows rather than shrinks when `m!=0`; nonlinear completion
action is especially sensitive there.

This is the exact local mechanism a phase-jet large sieve could exploit.
It is not yet a global Bessel theorem because physical action values are
periodic and the selected packets can still alias modulo one.

## 3. Orders two and three alone do not classify packets

Put

```text
rho=mathsf K/mathsf T,        t=a_0/S.               (3.1)
```

Equation (1.5) gives the invariant ratio

```text
-S*J'''/(3J'')
 =rho^2/t+(1-rho)^2/(1-t)
 =1+(rho-t)^2/(t*(1-t)).                             (3.2)
```

Thus `J'''/J''` sees only the square of `rho-t`.  Reflect

```text
rho^*=2t-rho,
mathsf T^*=mathsf T*rho*(1-rho)
             /(rho^* * (1-rho^*)).                  (3.3)
```

Then

```text
mathsf H^*=mathsf T^*(1-rho^*),
mathsf K^*=mathsf T^*rho^*                           (3.4)
```

defines a generally different rational pair `(h^*,k^*)` with exactly the
same `J''` and `J'''`.  At `t=1/2` this is the familiar left-right
reflection.  At a general rational tangent it is a nontrivial rational
involution.  Clearing denominators gives infinitely many integral
examples.

The first derivative normally separates the two mirrors.  Therefore a
jet theorem which keeps only orders two and three, while treating every
packet's affine slope as freely adjustable, is false.  The physical first
derivative or an equivalent genuine outer label is indispensable.

### 3.1 The fourth derivative repairs the mirror, modulo physical reflection

Differentiating (1.5) one more time and retaining the same notation gives an
exact quotient identity.  Define

```text
A=-S*J'''/(3J''),        B=S^2*J''''/(3J''),
R=rho*(1-rho)/(t*(1-t)).                              (3.5)
```

Then

```text
A=1+(rho-t)^2/(t*(1-t)),
B=4A^2-5R*(A-1).                                     (3.6)
```

Off the zero-Poisson branch `A=1`, this recovers

```text
R=(4A^2-B)/(5(A-1)).                                 (3.7)
```

The pair

```text
E=A-1=(rho-t)^2/(t*(1-t)),
R=rho*(1-rho)/(t*(1-t))                              (3.8)
```

determines `(t,rho)` up to the simultaneous reflection

```text
(t,rho) -> (1-t,1-rho).                              (3.9)
```

Indeed, its exact Jacobian is

```text
det d(E,R)/d(t,rho)
 =(t-rho)^2/(t^3*(1-t)^3)
 =E/(t^2*(1-t)^2).                                  (3.10)
```

Thus on a compact `t` collar, quotient inversion is uniformly conditioned
modulo reflection whenever `E` is bounded below.  Recovering `R` from
(3.7) costs one factor `(A-1)^(-1)`, and (3.10) records the remaining local
inverse loss.  Both failures occur only as `rho->t`, equivalently `m->0`.
More explicitly,

```text
E=m^2/(C^2*a_0*b_0*mathsf T^2).                     (3.11)
```

Near a fold `mathsf T->0` with `m!=0`, `E` grows.  The nonlinear completion
geometry therefore becomes more, not less, separated there.  The analytic
stationary amplitude is still large, but its action quotient is strongly
transverse.

The reflection (3.9) is exactly physical.  It acts by

```text
(d,h,k,m) -> (-d,k,h,-m),                            (3.12)
```

and the two critical actions differ by the affine completion term `m*S`.
Consequently their derivatives of orders two, three, and four agree, while
their first derivatives differ by `m`.  No nonlinear action theorem can or
should distinguish this ordered left-right symmetry.

## 4. Scaled cusp factors are tangent-intercept defects

Return to the symmetric centre `C=Q^2,S=2Q`.  For a physical point with
primitive data `(g,p,d)`, write

```text
ell=p^2-d^2,
U=2d*y-g*ell,
mathcal C=2d^2*Q-g*p*ell,
H=mathcal C-2p*U,
j_-=H-d*U,                 j_+=H+d*U.               (4.1)
```

These are the universal-content coordinates.  The physical reciprocal
point is

```text
a=Q+y,
V=Q-y+g*(p-d)/2,
W=Q+y+g*(p+d)/2.                                   (4.2)
```

Write the line through this point parallel to the rational tangent as

```text
V=alpha-(p^2/(p+d)^2)*a,
W=beta +(p^2/(p-d)^2)*a.                            (4.3)
```

The exact curve tangent has

```text
alpha_0=2Qp/(p+d),
beta_0=-2Qpd/(p-d)^2.                               (4.4)
```

Direct expansion gives the key bridge:

```text
alpha-alpha_0=j_-/(2*(p+d)^2),
beta-beta_0  =j_+/(2*(p-d)^2).                      (4.5)
```

In the alternative notation of the scaled-cusp report,

```text
z=-H,                  v=U.                          (4.6)
```

Consequently

```text
H=0       <=> z=0,
j_-=0     <=> z=-d*v,
j_+=0     <=> z=d*v.                                (4.7)
```

Under physical reflection `(y,d)->(-y,-d)`, the quantities `U,H,z` remain
fixed while `j_-` and `j_+` swap.  Thus the unavoidable quotient reflection
(3.9) merely exchanges the two one-band axes in (4.7).  The balanced axis,
square-content condition, and the fold invariant `H-pU` are unchanged; only
the signed fold probe `d*(H-pU)` changes sign.

The three algebraically peeled axes are therefore not merely convenient
factors: they are the balanced and two one-sided affine-height collision
loci.

For every stationary normal `(h,k,m)`, where

```text
m=p^2*(k/(p-d)^2-h/(p+d)^2),                        (4.8)
```

the physical action minus the exact-tangent action is

```text
E_(h,k)
 =h*j_-/(2*(p+d)^2)+k*j_+/(2*(p-d)^2)

 =H/2*(h/(p+d)^2+k/(p-d)^2)
   +d*U*m/(2p^2).                                   (4.9)
```

This formula retains the affine intercept rather than replacing it by a
scalar cubic label.

## 5. Four distinguished jet probes

The stationary normal plane contains four useful modes:

```text
left:   (h,k,m)=((p+d)^2,0,-p^2),
right:  (h,k,m)=(0,(p-d)^2,p^2),
zero:   (h,k,m)=((p+d)^2,(p-d)^2,0),
fold:   (h,k,m)=((p+d)^3,-(p-d)^3,-2p^3).           (5.1)
```

Equation (4.9) evaluates them exactly:

```text
E_left =j_-/2,
E_right=j_+/2,
E_zero =H,
E_fold =d*(H-p*U).                                  (5.2)
```

This produces the following lifted collision classification.

1. A left one-inverse height collision lies on `z=-d*v`.
2. A right one-inverse height collision lies on `z=d*v`.
3. A zero-Poisson height collision lies on `z=0`.
4. A fold height collision lies on `z=-p*v`; Section 6 closes its full count.
5. Simultaneous left and right collisions give `H=U=0`.  Then the two
   product errors vanish and elementary divisibility forces `d^2|g`.

For the last assertion, `U=0` first gives `d|g`, since
`g*ell=2d*y` and `(d,ell)=1`.  Writing `g=d*g_1`, the equation `H=0`
then gives `d|g_1`, because `(d,p*ell)=1`.

The word **lifted** matters.  The physical exponential sees (5.2) modulo
one.  For example, `j_-/2` aliases whenever `j_-` changes by an even
integer.  Torus-distance smallness alone therefore does not imply that the
real quantity in (5.2) is small.  A future Bessel theorem must obtain the
lift from nonlinear completion-action variation or another genuine outer
average.  Scalar Fourier orthogonality has not been assumed here.

There is also a frequency-support limit.  The endpoint probes in (5.1) have
size about `p^2`.  They lie in the Fejer box only for `p^2<=H_top`.  Above
that threshold the exact identities remain true, but they cannot simply be
inserted as available Fourier probes.  This is the dual form of the known
high-denominator plateau.

## 6. The new fold-height branch

Set

```text
W_fold=H-p*U.                                        (6.1)
```

If `W_fold=0`, the slope identity

```text
2d*n=-(H+pU)                                        (6.2)
```

gives `d*n=-p*U`.  Since `(p,d)=1`, one obtains

```text
U=d*w,          n=-p*w,          p|Q.               (6.3)
```

The defining equation for `H` also gives `d|g`.  Write

```text
Q=p*M,          g=d*a.                               (6.4)
```

Then the whole branch has the exact parametrization

```text
a*(p^2-d^2)+3w=2d*M,
y=d*M-w,                                             (6.5)

4e=w*(a*(p-d)^2-w),
4f=w*(a*(p+d)^2-w).                                 (6.6)
```

Thus the primitive height `p` is a divisor of the fixed centre, and both
errors reduce to one shared parameter `w`.

The branch does not reduce to square content.  The exact fixture

```text
p=5,       d=2,       Q=30,       g=2,       y=11   (6.7)
```

has

```text
U=2,       H=10=pU,
j_-=6,     j_+=14,
e=2,       f=12,
d^2 does not divide g.                              (6.8)
```

It lies off all three axes in (4.7), but its cubic-fold affine height is
exactly zero.  Therefore any inverse theorem claiming that every fold jet
collision forces `z=0`, `z=+-d*v`, or square content is false.  The fourth
invariant (6.1) is necessary.

### 6.1 The whole fold-height branch is affordable

The count can be made without reflecting the two unequal masks.  Allow
signed `d` and `a=g/d`; then `a*d>0`, while

```text
x=p-d>0,                 z=p+d>0.                    (6.9)
```

Equations (6.5)--(6.6) imply the two exact divisor identities

```text
x*(2*M+a*z)=2Q-3w,
eta=a*x^2-w,             4e=w*eta,
2*x*(a*(p+x)+M)=2Q+3eta.                           (6.10)
```

These use the narrow left error `e` for both signs of `d`, so no asymmetric
band is swapped.  Split first at

```text
|w|<=sqrt(A).                                       (6.11)
```

There are `O(sqrt(A))` possible integral `w`.  For each divisor `p|Q`, the
first identity in (6.10) makes `x` a divisor of `2Q-3w`; then `d=p-x` and
`a` are fixed.  This costs `O(sqrt(A)Q^epsilon)`.

If `|w|>sqrt(A)`, the narrow mask and the middle identity in (6.10) give

```text
|eta|<=4A/|w|<4sqrt(A).                             (6.12)
```

For each of the `O(sqrt(A))` possible `eta` and each `p|Q`, the final
identity in (6.10) makes `x` a divisor of `2Q+3eta`, again fixing `d,a,w`.
In the energy core `Q/sqrt(A)` is a positive power, so all divisor targets
are nonzero and comparable with `Q`.  Uniform divisor bounds give

```text
# {H-pU=0 fold-height points}
 <<sqrt(A)*Q^epsilon.                               (6.13)
```

This bound is hereditary under arbitrary packet deletion, since it is a
cardinality estimate for the complete signed branch.  It includes `w=0`
and `e=0`, and does not require square content, the residual primitive
floor, or the wide mask `B`.  Thus the new invariant is necessary for
classification but is no longer an open counting obstruction.  A literal
finite divisor majorant is recorded in the dedicated fold-height report.

## 7. Consequence for a phase-jet/Bessel programme

The exact algebra suggests the following viable architecture.

1. Keep the full physical critical action through order three in the
   completion variable; do not retain curvature alone.
2. On the regular set separated from (2.5), use the rational inverse
   (2.2)--(2.4) to convert a large Gram entry into proximity of the whole
   saddle-frequency packet.
3. Charge the endpoint and zero-Poisson degeneracies to the three affine
   factors in (5.2), already counted by divisor peels.
4. Charge the fold-height branch to the count (6.13).
5. Prove a no-wrap lifting or nonlinear van der Corput/Bessel estimate so
   that equality modulo one cannot hide large integer changes in (5.2).
6. Above `p^2=H_top`, replace the unavailable endpoint probes by the full
   action inverse rather than extrapolating the false `p^(-4)` layer mass.

Steps 1--4 are now exact algebra and counting.  Step 5 is the genuinely new
analytic theorem.

## 8. Status and reproducibility

```text
physical J,J',J'',J''' through arbitrary S/Q:        PROVED;
generic (J',J'',J''') inverse:                       PROVED;
inverse degeneracy iff m=0 (regular nonendpoint):   PROVED;
second/third-jet mirror collision:                   PROVED;
nonlinear (J'',J''',J'''') reflection rigidity:      PROVED;
exact quotient Jacobian and conditioning locus:      PROVED;
scaled factors equal affine-intercept defects:       PROVED;
z=0 and z=+-d*v as distinguished height collisions: PROVED;
double intercept collision forces d^2|g:             PROVED;
new fold invariant H-pU:                             PROVED NECESSARY;
fold branch p|Q, d|g and factorization (6.6):        PROVED;
fold branch count O(sqrt(A)Q^epsilon):               PROVED;
no-wrap nonlinear action Bessel theorem:             OPEN;
sharp four-cycle bound:                              NOT PROVED.
```

The exact rational identities and replay fixtures are implemented in

```text
src/qp_phase_jet_inverse.py
src/test_qp_phase_jet_inverse.py
```
