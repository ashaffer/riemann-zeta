# QP stationary action: exact three-jet rigidity and the inverse gate

**Date:** 2026-08-25  
**Verdict:** the lifted nonlinear stationary-action three-jet is globally
rigid.  On every interior regular branch with `h*k*m!=0`, its first three
derivatives in the physical completion sum uniquely determine the saddle and
the complete frequency triple `(h,k,m)`.  This statement is not itself
compatible with the physical affine alias, because `J'` is visible only
modulo an integer.  The quotient-compatible replacement is also exact:
`(J'',J''',J'''')` determines the mode up to the unavoidable left--right
reflection, whose actions differ by `m*S`.

This is the rigidity half of a phase-jet Bessel strategy.  A quantitative
bound for clusters of *near*-coincident discrete jets is not proved here, so
the sharp four-cycle bound remains open.

## 1. Critical action and exact jets

Fix `C>0` and write

```text
F(a,S)=-m*a+C*h/a+C*k/(S-a),       b=S-a.           (1.1)
```

At an interior stationary point put

```text
X=h/a^2,             Y=k/b^2,
D=X*b+Y*a.                                             (1.2)
```

Stationarity is `m=C*(Y-X)`, while regularity is `D!=0`.  Let
`psi(S)=F(a(S),S)` be the critical action on the resulting local branch.
The envelope theorem and implicit differentiation give exactly

```text
psi'  =-C*Y,
psi'' =2*C*X*Y/D,
psi'''=-6*C*X*Y*(X^2*b+Y^2*a)/D^3.                 (1.3)
```

The first derivative is precisely where the integral Poisson labels may
alias.  The higher derivatives contain the nonlinear movement of the saddle.

## 2. Exact inversion of the three-jet

Write `q_j=psi^(j)`.  From (1.3),

```text
Y=-q_1/C,
E=1+2*C*Y*q_3/(3*q_2^2),                            (2.1)
X=[S*q_2/(2*C)-Y]/E,
D=2*C*X*Y/q_2,
a=(D-X*S)/(Y-X).                                    (2.2)
```

Finally,

```text
b=S-a,       h=X*a^2,       k=Y*b^2,
m=C*(Y-X).                                           (2.3)
```

The apparent exceptional denominator has the exact factorization

```text
E=a*Y*(X-Y)/(X*D).                                  (2.4)
```

Thus, after excluding endpoints, zero frequencies, and the fold `D=0`, it
vanishes exactly when `m=0`.  That zero-dual branch is already controlled at
the square-root scale.  Equations (2.1)--(2.4) prove:

> **Unwrapped three-jet rigidity.** At fixed `(C,S)`, two regular interior
> nonzero-dual stationary modes with equal real action three-jets are
> identical.

This is stronger than saying that a generic Jacobian is nonzero: it supplies
the global rational inverse explicitly.

## 3. Why the third jet is necessary

At `(C,S)=(100,20)`, the two saddles

```text
(a,h,k,m)=(12,144,128,100),
(a,h,k,m)=(4,8,512,150)                              (3.1)
```

both have

```text
psi'=-200,              psi''=25/2,                 (3.2)
```

but their third derivatives differ.  Hence a slope-curvature pair does not
determine the Poisson branch.  Any inverse theorem using only two action jets
would retain a real one-parameter collision family.

## 4. Rigidity after removing the affine alias

The physical integer samples cannot distinguish `J(S)` from `J(S)+m*S`
when `m` is integral.  Put

```text
t=a/S,                 u=da/dS=a*Y/D,
A=-S*J'''/(3J''),      B=S^2*J''''/(3J'').          (4.1)
```

Exact differentiation gives

```text
A=1+(u-t)^2/[t*(1-t)],
B=4*A^2-5*R*(A-1),    R=u*(1-u)/[t*(1-t)].          (4.2)
```

Off `m=0`, set `w=A-1`, recover `R=(4*A^2-B)/(5*w)`, and put
`L=1-R-w`.  With `x=2*t-1` and `y=2*u-1`,

```text
x^2=L^2/(L^2+4*w),       y/x=(L+2*w)/L.             (4.3)
```

If `L=0`, then `x=0` and `y^2=w`.  Thus the only ambiguity in every case is
`(x,y)->(-x,-y)`, or

```text
(a,h,k,m) -> (S-a,k,h,-m).                          (4.4)
```

The second derivative then recovers the scale:

```text
X=S*t*J''/(2*C*u),       Y=S*(1-t)*J''/[2*C*(1-u)]. (4.5)
```

Under (4.4), the reflected critical action is exactly `J(S)+m*S`.
Consequently the two packets are identical on integer `S` when `m` is
integral, and no valid inverse theorem should separate them.  The exact
Jacobian

```text
det d(A-1,R)/d(t,u)=(t-u)^2/[t^3*(1-t)^3]           (4.6)
```

degenerates only at `m=0` on an interior compact collar.  This proves exact
rigidity in the physical affine quotient.  The fourth derivative is used to
classify persistent third-jet coherence; it is not an invocation of a
fourth-derivative exponential-sum estimate.

## 5. The quantitative theorem still needed

The physical synthesis samples `S` on integers.  Therefore the correct
near-collision labels are discrete action differences modulo the
integer-valued Newton lattice, not raw real derivatives.  The affine part is
handled exactly by Section 4, but possible quadratic/cubic wraps and
quantitative near-collisions still require a lifting or variation argument.

The next theorem must show that a cluster whose sampled jets agree at the
anisotropic resolutions

```text
1/L,               1/L^2,               1/L^3       (4.1)
```

either has the required multiplicity or forces a classified affine-height
branch.  Equations (4.2)--(4.6) are the appropriate starting point because
they already quotient the true reflection alias.  Conditioning can fail at
an endpoint frequency or at `m=0`; the stationary approximation itself also
requires a separate fold treatment.

## 6. Reproducibility and status

The exact jets through order four, both inverse maps, the discrete three-jet
collision, reflection identity, fold check, and zero-dual exception are
replayed in

```text
src/qp_stationary_action_jet_rigidity.py
src/test_qp_stationary_action_jet_rigidity.py
```

```text
stationary-action formulas through order four:       PROVED;
global regular nonzero-dual three-jet inverse:        PROVED;
two action jets determine the mode:                   FALSE;
lifted first-through-third jet determines the mode:   PROVED;
second-through-fourth jet modulo reflection:          PROVED;
reflection is an exact integral-affine alias:         PROVED;
near-jet multiplicity at Bessel resolution:           OPEN;
phase-jet Bessel/inverse theorem:                      OPEN;
sharp four-cycle bound:                               NOT PROVED.
```
