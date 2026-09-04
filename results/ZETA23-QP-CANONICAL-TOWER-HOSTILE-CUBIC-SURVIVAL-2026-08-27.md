# QP canonical tower and survival of the hostile cubic transition

**Date:** 2026-08-27
**Verdict:** canonical self-orbit integrality does **not** impose a new
congruence which removes the balanced hostile cubic transition.  There is
an exact critical-scale family of primitive anchors for which one complete
integer self-orbit contains a constant-density all-one unimodular rectangle
with

```text
(R,S)=(R,R+1),             (U,V)=(-1,-1).
```

On that rectangle the self-orbit reciprocal kernel is literally the
balanced completed-strip kernel used in the Fejer-diagonal/Huxley audit.
Its diagonal cubic frequency is exactly

```text
beta_u = ((R+1)/R)*(u/F)^3,
```

so the aligned near-cube equation and the later transition

```text
A*u^3-B*F^3=Delta
```

survive unchanged.  The tower congruence selects the already-hostile
`S=R+1` chart rather than excluding it.

This is a no-go theorem for a proposed shortcut, not a counterexample to
the dyadic reciprocal large sieve.  It does not prove that the hostile
transition has too many solutions, and a future global argument could use
cancellation between this rectangle and the rest of the canonical orbit.

## 1. An exact critical-scale canonical tower

Let `N>=2` be even and put

```text
F=N^8,             R=N^25,
q=2*F*R=2*N^33,    D=F^2=N^16.                    (1.1)
```

Thus, up to the harmless fixed factor `2`,

```text
F=q^(8/33),        D=q^(16/33),
R=q^(25/33),       q/D=2*N^17.                    (1.2)
```

Choose the unimodular basis

```text
d=(R,R+1),         e=(-1,-1),       det(d,e)=1.   (1.3)
```

Define the reflected anchor and the physical anchor by

```text
(C,c)=F*d+e=(F*R-1,F*(R+1)-1),
gamma=(c,C).                                      (1.4)
```

The anchor is primitive, since

```text
gcd(C,c)=gcd(F*R-1,F)=1.                           (1.5)
```

Its short packet direction is `U_0=(1,1)=-e`, and its determinant
remainder is exactly

```text
c-C=F.                                             (1.6)
```

At the top Selberg scale `K=q/D`, the natural packet radius is

```text
R_K^2=q/K=D,       R_K=F.                          (1.7)
```

Hence `(1,1)` is a genuine small-step/small-remainder tower direction:
its step is `1<F` and its remainder `F` is below the critical remainder
scale `D^2/R_K^2=F^2`.

Equivalently, in the short basis `(1,1),(0,1)` one has

```text
(C,c)=(F*R-1)*(1,1)+F*(0,1).                       (1.8)
```

The canonical quotient is therefore `F*R-1 == -1 (mod F)`.  This is the
important congruence: after changing to the long basis `(1.3)`, it becomes
the complementary coefficient `-1` on both physical coordinates, exactly
the aligned hostile chart.

## 2. A balanced all-one rectangle inside one self-orbit

For integers `(m,n)` define

```text
z_(m,n)=m*d+n*e
       =(R*m-n,(R+1)*m-n).                         (2.1)
```

The self-orbit label has the exact form

```text
t_(m,n)=c*(R*m-n)-C*((R+1)*m-n)
       =m-F*n.                                     (2.2)
```

Take

```text
15F/16 <=m<17F/16,
F/4    <=n<3F/4.                                   (2.3)
```

The endpoint convention is immaterial.  Since `N` is even, `F=N^8` is
divisible by `16`.  The rectangle has `asymp F^2=D` points.

It embeds injectively into the label interval.  Indeed, equality of two
labels gives

```text
m-m'=F*(n-n'),                                     (2.4)
```

while the `m`-interval has length `F/8<F`; hence both differences vanish.
Also `(2.2)--(2.3)` give `|t_(m,n)|<F^2=D`.
There is no second shell representative of one of these labels: two
integer solutions with the same label differ by a multiple of `(C,c)`,
whereas the shell diameter is strictly smaller than both `C` and `c`.

Every physical coordinate is in the project shell.  Exactly,

```text
0.9*(q/2)<R*m-n,
(R+1)*m-n<1.1*(q/2)                                (2.5)
```

for this family (with vast room once `R>=32`).  Since

```text
e^(-0.2)<0.9<1.1<e^(0.2),                          (2.6)
```

the rectangle lies inside the standard full-integer shell.

For fixed `m`, varying `n` moves along `e=-(1,1)`, so `(2.3)` consists of
`asymp F` complete short affine lines, each with `asymp F` all-one points.
Changing `m` moves by the long vector `(R,R+1)`, of size `q/F`.  Thus this
is precisely a balanced single tower: `F` parallel translates of length
`F`, with total mass `F^2=D`.

There is also a finite replay with an actual prime-power anchor (in fact,
both coordinates are prime):

```text
C=8000000011,            c=8000000221,
c-C=210,
C=210*38095238+31.                               (2.7)
```

For

```text
d=(38095238,38095239),   e=(-1,-1),
```

one has exactly

```text
(C,c)=210*d-31*e.                                  (2.8)
```

The points `z=m*d+n*e` with

```text
190<=m<=230,             -100<=n<=100
```

have distinct labels

```text
t=-210*n-31*m,
```

all satisfying `|t|<210^2`; they lie in the standard shell centered at
`210*38095238` and form the same aligned `R,R+1,-1,-1` rectangle.  This
finite check shows that anchor primality does not create a formal
incompatibility.  It is not an asymptotic theorem about prime pairs with a
prescribed growing gap; no such assertion is needed for the tower-integrality
no-go statement.

## 3. Exact identification with the completed-strip HSM chart

For two rectangle points, the one-window self-orbit phase is

```text
q^3/[8*b_(m,n)*B_(m',n')]
 =q^3/[8*(R*m-n)*((R+1)*m'-n')].                  (3.1)
```

This is not an approximation.  It is exactly the completed-strip
parameterization

```text
a=R*m+U*n,          c=S*m'+V*n',
(R,S)=(R,R+1),      (U,V)=(-1,-1),
R*V-S*U=1.                                      (3.2)
```

The quotient intervals in `(2.3)` are contiguous and all-one.  Therefore
Poisson/B-process completion produces exactly the two interval transforms

```text
W_1(j)=sum_(n in I) e(j*n/R),
W_2(k)=sum_(n' in I') e(k*n'/(R+1)),               (3.3)
```

with their triangular positive autocorrelations.  No arbitrary coefficient
mask or artificial strip completion has been introduced: `(3.1)` is an
actual constant-density subchart of one canonical full-integer orbit.

## 4. The cubic endpoint is the already-hostile aligned model

On the diagonal stationary fibre the relevant cubic frequency is

```text
beta_u=8*R^2*(R+1)*u^3/q^3.
```

Using `q=2FR` gives the exact identity

```text
beta_u=((R+1)/R)*(u/F)^3.                           (4.1)
```

At `u asy F` and multiplier `a asy q/D=2R/F`, the distinction between
this frequency and the pure cube is precisely the Fejer resolution:

```text
a*|beta_u-(u/F)^3| asy 1/F.                        (4.2)
```

Clearing denominators is equally explicit.  For a nearest integer `b`,

```text
a*beta_u-b
 =[a*(R+1)*u^3-b*R*F^3]/(R*F^3).                 (4.3)
```

Thus the canonical tower supplies the same aligned near-cube numerator
used before the Farey/Huxley decomposition.  That decomposition's primitive
quality-one transition

```text
A*u^3-B*F^3=Delta,
gcd(A,B)=1,
A,B asy F^(9/16),       0<|Delta|<=F^(7/16)        (4.4)
```

is therefore not thinned by an additional tower congruence.  All the
integral restrictions in the tower are already present in `(3.2)--(4.3)`:

```text
det((R,R+1),(-1,-1))=1,
S=R+1,
U=V=-1.                                            (4.5)
```

One can of course reduce the numerator in `(4.3)` modulo `R` or `R+1`,
but those are tautological congruences of the aligned model itself.  They
do not supply a new condition after the tower is imposed.  In particular,
the anchor residue `-1 mod F` creates `(4.5)`; it does not restrict the
dual multiplier and nearest-integer variables beyond the restrictions
already used in deriving `(4.4)`.

## 5. What this rules out, and what remains possible

The exact embedding proves the following limited no-go statement:

> A proof cannot remove the `F^(1/16)` hostile cubic floor merely by saying
> that the balanced completed strip is incompatible with a canonical
> self-orbit tower, or that tower integrality adds a missing congruence.

The most aligned completed strip is itself a canonical tower.

This does **not** prove that `(4.4)` has `F^(5/8)` solutions.  The old
`F^(5/8)` value is a provisional Huxley-IV upper-bound/occupancy floor, not a
constructed arithmetic counterfamily; the accessible corollary used to
quote it excludes integral powers, so the original determinant-form theorem
still has to be checked.  The fully licensed Huxley-II primitive exponent is
`17/24`.  See
`ZETA23-SHIFTED-CUBE-GCD-QUANTIFIER-AND-HUXLEY-AUDIT-2026-08-27.md`.
It also does not imply that the full canonical
orbit moment is at least the localized rectangle moment: Fourier moments
are not monotone under adding the remaining orbit points.  Two viable
routes therefore remain:

1. prove the genuinely new fixed-denominator/shifted-cube energy estimate;
2. exploit global cancellation between canonical tower cells in a way that
   bypasses localized positive Fejer control.

What has been closed is only the hoped-for congruence shortcut.

## 6. Binary status

```text
critical canonical tower family:                         PROVED;
primitive anchor and exact tower decomposition:          PROVED;
Theta(D) all-one balanced rectangle in one self-orbit:   PROVED;
finite two-prime-anchor aligned replay:                  PROVED;
rectangle kernel equals aligned completed-strip kernel:  PROVED;
diagonal beta_u=((R+1)/R)*(u/F)^3:                       PROVED;
extra tower congruence removes hostile cubic transition: FALSE;
hostile transition has too many arithmetic solutions:   NOT CLAIMED;
global canonical-orbit cancellation bypasses transition: OPEN;
dyadic reciprocal large sieve:                           OPEN;
sharp four-cycle bound:                                  NOT PROVED.
```

Exact finite verification is in

```text
src/qp_self_orbit_tower_cubic_survival.py
src/test_qp_self_orbit_tower_cubic_survival.py
lean/weilcert/QPSelfOrbitTowerCubicSurvival.lean
```

Run with

```text
PYTHONPATH=src pytest -q src/test_qp_self_orbit_tower_cubic_survival.py
cd lean/weilcert && lake env lean QPSelfOrbitTowerCubicSurvival.lean
```
