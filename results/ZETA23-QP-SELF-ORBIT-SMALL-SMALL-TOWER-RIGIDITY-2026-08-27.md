# QP self-orbit small/small sector: unique tower and product-action gate

**Date:** 2026-08-27  
**Verdict:** the residual small-step/small-remainder sector has only **one**
primitive direction at each dyadic scale.  In fact, once one hard direction
is present, every realized radius-`R` direction is parallel to it.  The
complete integer orbit is therefore a single exact tower of at most `|rho|`
contiguous affine lines, and different lines are separated by `asymp
q/|rho|` in both physical coordinates.

Strong convexity then separates the stationary-frequency images of distinct
line-pair cells by at least `q/D^2=q^(1/33)` throughout the active range.
This removes direction multiplicity and stationary-index overlap from the
open problem.  It still does **not** prove translate Bessel or `(DRPLS)`:
the reciprocal Legendre action collapses from the two stationary indices
`(m,n)` to their product `mn`.  Distinct, widely separated tower cells can
therefore have the same scalar action, and near-product cancellation is the
same signed HSM/MSPD endpoint already known to be open.

The sharp four-cycle bound is not proved.

## 1. Scale and notation

Fix a primitive anchor `gamma=(c,C)` and put

```text
t(z)=c*b-C*B,               z=(b,B),       |t(z)|<=D,
K*R^2=q,                    sqrt(D)<=R<=D.                 (1.1)
```

For a primitive direction `U=(p,P)`, write

```text
rho_U=c*p-C*P,              u=||U||_infinity.              (1.2)
```

Use the following constant-safe version of the surviving hard conditions:

```text
u*R<=D,                    |rho_U|*R^2<=2D^2.              (1.3)
```

Every primitive direction `V=(s,S)` realized by two radius-`R` orbit points
satisfies

```text
||V||_infinity<=R,          |rho_V|<=2D.                   (1.4)
```

The second inequality follows because a difference `gV` changes the orbit
label by `g*rho_V`, while both labels lie in `[-D,D]`.

## 2. New theorem: one hard direction absorbs every radius direction

For any two directions `U=(p,P)` and `V=(s,S)`, direct expansion gives

```text
C*det(U,V)=rho_U*s-rho_V*p,
c*det(U,V)=rho_U*S-rho_V*P.                         (2.1)
```

Apply the first identity to `(1.3)--(1.4)`:

```text
|C*det(U,V)|
 <=|rho_U|*|s|+|rho_V|*|p|
 <=2D^2/R+2D^2/R
 =4D^2/R.                                           (2.2)
```

Since `R^2>=D`, this is at most `4DR`.  The already established dynamic
packet hypothesis `8DR<min(c,C)` therefore makes `(2.2)` strictly smaller
than `C`.  As the determinant is integral,

```text
det(U,V)=0.                                         (2.3)
```

After the standard common orientation, primitive `U,V` are equal.  Thus:

> **Unique hard-tower theorem.** If one realized primitive direction obeys
> `(1.3)`, every nontrivial component of the radius-`R` self-orbit graph has
> that same primitive direction.

This is stronger than showing that two small/small directions agree: `V`
in the proof is an arbitrary realized radius direction.  At the critical
scaling,

```text
D^(3/2)=q^(8/11)=o(q),                              (2.4)
```

so the integrality margin is a fixed power.

## 3. Exact global tower and macroscopic separation

Choose `V_0` with `det(U,V_0)=1`.  There are integers `a,rho` such that

```text
(C,c)=a*U+rho*V_0,            gcd(a,rho)=1.          (3.1)
```

For `z=nU+sV_0`, the label and coordinates satisfy exactly

```text
t=rho*n-a*s,
rho*b=p*t+C*s,
rho*B=P*t+c*s.                                    (3.2)
```

Thus fixed `s=det(U,z)` is one affine `U`-line and its labels form one
residue class modulo `rho`.  The intersection with the two shell intervals
and `|t|<=D` is a contiguous interval in `n`.

If two short-orbit points lie on distinct `U`-lines, subtraction in `(3.2)`
gives

```text
|rho|*|Delta b| >= C-2D*|p|,
|rho|*|Delta B| >= c-2D*|P|.                       (3.3)
```

Under `(1.3)` and `8DR<min(c,C)`, both right sides are positive and
comparable with `q`.  In particular distinct lines are separated by
`asymp q/|rho|` in **both** coordinate projections.  Combining
`|rho|<=2D^2/R^2` with `8DR<min(c,C)` makes the gap greater than a fixed
multiple of `R`.  Consecutive points on one line differ by `U`, whose norm
is at most `D/R<=R`.  Hence, for the complete integer orbit, the radius
components are exactly the nonempty tower lines.

There are at most `|rho|` such lines.  Indeed, if two line indices are
congruent modulo `rho`, `(3.1)--(3.2)` make their point difference

```text
k*U+l*(C,c),               |k|<=2D/|rho|.           (3.4)
```

The project shell diameter `W` satisfies

```text
W+2D*u/|rho|<min(c,C)                              (3.5)
```

for all sufficiently large `q`, so `(3.4)` forces `l=0` and the two lines
are the same.  Their residues are distinct modulo `rho`.

For the finite fixture

```text
q=200000, D=371, R=20,
gamma=(104467,111006), U=(17,16), rho=-157,          (3.6)
```

the complete orbit has 50 tower lines: 49 nontrivial dynamic components
and one singleton.  This is well below `|rho|=157`, and the exact gaps in
`(3.3)` are certified by the accompanying tests.

## 4. Stationary-frequency cells separate by a power

Adding an integral linear phase does not change the exponential sum, so use

```text
Phi(x,y)=q^3/(8*x*y)+x+y.                           (4.1)
```

Its Hessian is

```text
Hess Phi =
 [ 2T/(x^3*y)    T/(x^2*y^2) ]
 [ T/(x^2*y^2)   2T/(x*y^3) ],       T=q^3/8,

det(Hess Phi)=3T^2/(x^4*y^4)>0.                    (4.2)
```

On a fixed shell `alpha*q<=x,y<=beta*q`, both eigenvalues are comparable
with `1/q`.  One explicit lower bound is

```text
Hess Phi >= [3*alpha^4/(32*beta^8*q)]*I.            (4.3)
```

This follows from `lambda_min>=det/trace`.  Strong convexity and `(3.3)`
show that the gradient images of two distinct Cartesian tower-line cells
are separated by `c_0/|rho|`.  In line coordinates, multiplication by
`diag(p,P)` can only increase this lower bound by
`min(|p|,|P|)>=1`.  At Fourier frequency `h~K`, the stationary Poisson
images are therefore separated by

```text
>>K/|rho|
 >=q/(2D^2)
 =q^(1/33).                                         (4.4)
```

Thus a stationary lattice frequency belongs to at most one translated
line-pair cell.  This is a genuine multiplicity-one theorem for the
two-dimensional B-process support.

## 5. Why `(4.4)` still does not prove translate Bessel

For `A=hT`, stationarity of `A/(xy)+m*x+n*y` gives

```text
m=A/(x^2*y),              n=A/(x*y^2).              (5.1)
```

Writing `f=A/(xy)`, one has the exact identities

```text
f+m*x+n*y=3f,             f^3=A*m*n.                (5.2)
```

Consequently the scalar stationary action is

```text
3*(A*m*n)^(1/3),                                  (5.3)
```

which remembers only the product `m*n`, not the separated two-dimensional
stationary index.  Disjoint B-process supports therefore do not imply
orthogonality after their scalar outputs are summed.  Exact equal products
have divisor multiplicity and are harmless, but near products are precisely
the shifted-multiplication-table/HSM discrepancy.

The obstruction already occurs inside a unique tower.  For

```text
gamma=(50000,50007),       U=(1,1),       rho=-7,   (5.4)
```

the distinct ordered line pairs `(-6,-8)` and `(-8,-6)` contain points with

```text
42891*57176=57188*42882.                            (5.5)
```

Their stationary cells are spatially and gradient separated, yet their
reciprocal/product actions agree exactly.  Equation `(5.5)` is
divisor-harmless; it is a decisive warning against treating `(4.4)` as a
Cotlar theorem.

In the single-tower coordinates the physical product has the exact form

```text
b_t*B_j=((C*s+p*t)*(c*sigma+P*j))/rho^2,            (5.6)

t==-a*s (mod rho),          j==-a*sigma (mod rho).
```

Thus the remaining `(MSPD)` is no longer a multidirectional problem.  It is
a signed Möbius discrepancy for the one canonical rational tower `(5.6)`.
No available Poisson, van der Corput, or positive large-sieve estimate
controls the near-product actions in `(5.3)` with the required lossless
normalization.

## 6. A proved quantitative subrange

The known one-fan estimate gives, for each ordered pair of complete tower
lines,

```text
|S_(lambda,mu)(h)| <<(q/h)q^o(1).                  (6.1)
```

There are at most `rho^2` ordered line pairs.  Absolute summation followed
by the dyadic square gives the rigorous bound

```text
sum_(K<h<=2K)|S_gamma(h)|^2
 <<|rho|^4*(q^2/K)q^o(1).                           (6.2)
```

Therefore `(DRPLS)` is proved whenever `|rho|=q^o(1)`.  In particular, the
hard sector is closed throughout every polylogarithmic neighborhood of the
bottom frequency:

```text
R>=D/(log q)^A
  => |rho|<=2(log q)^(2A)
  => (DRPLS).                                       (6.3)
```

This includes the adjacent/bounded-remainder tower.  It is not a fixed-power
portion of the active band and does not change the global four-cycle
exponent.

## 7. Binary status

```text
hard U versus arbitrary realized V direction collapse: PROVED;
all nontrivial dynamic directions equal one U:          PROVED;
exact global tower coordinates:                         PROVED;
at most |rho| complete-orbit tower lines:               PROVED;
interline physical gap asymp q/|rho|:                   PROVED;
stationary-gradient cell multiplicity one:              PROVED;
reciprocal stationary action depends only on m*n:       PROVED;
DRPLS for |rho|=q^o(1):                                PROVED;
positive near-pair counting after tower reduction:      STILL TOO LARGE;
signed product-action/HSM estimate for polynomial rho:  OPEN;
full DRPLS:                                             OPEN;
sharp four-cycle bound:                                 NOT PROVED.
```

Machine checks:

```text
PYTHONPATH=src pytest -q src/test_qp_self_orbit_small_small_tower.py
cd lean/weilcert && lake env lean QPSelfOrbitSmallSmallTower.lean
```

Files:

```text
src/qp_self_orbit_small_small_tower.py
src/test_qp_self_orbit_small_small_tower.py
lean/weilcert/QPSelfOrbitSmallSmallTower.lean
```
