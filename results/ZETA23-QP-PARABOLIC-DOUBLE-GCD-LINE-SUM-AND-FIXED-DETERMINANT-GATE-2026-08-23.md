# QP parabolic curvature: the double-GCD line sum and fixed-determinant gate

**Date:** 2026-08-23  
**Verdict:** the endpoint divisor saving is genuine and extends to a
uniform double-GCD theorem.  It lowers the one-sided endpoint curvature
from `D^(37/32)` to `D^(35/32)`.  It does **not** lower the uniform
curvature maximum: the balanced grid

```text
E~D,  T~1,  R~S~D^(3/16)
```

still gives `D^(37/32)`.  On that grid the exact common-level equation is
a fixed-determinant incidence.  Its uniform operator norm is
`U^(1/2)q^o(1)`, where `U=D^(5/32)`, and this is sharp without two-sided
primitivity.  If it could be inserted without duplicating gap-token mass,
the block would fall to `D^(69/64)` (and to `D` on the two-sided primitive
subgrid).  That insertion is presently **conditional** on the already-open
varying-secant token-lift estimate.  The determinant incidence alone does
not prove it.

## 1. Exact transverse scales

Use the notation of the parabolic gap-token report.  In unimodular carrier
coordinates,

```text
U^T K V=(0,theta;eta,gamma),
a=U(u,alpha),             b=V(v,beta),
```

with primitive relation directions `r,s`, of sizes `R,S`.  Product-band
subtraction in one row and one column gives

```text
x*b1-y*b2=O(D),            x*a1-zeta*a2=O(D).
```

Combining these with the four token equations gives, after choosing a
maximal coordinate of `r` and `s`,

```text
x*beta = r_i*eta*b_j+O(SD),
x*alpha=-s_j*theta*a_i+O(RD).
```

All shell coordinates are comparable with `q`, and `RD/q,SD/q=o(1)`.
Consequently, uniformly on a dyadic block,

```text
|alpha|~S*T,                |beta|~R*E.             (1.1)
```

At the old one-sided endpoint

```text
E=D, T=S=1, R=D^(3/16),
```

this specializes to `|alpha|~1`, `|beta|~RD`.

## 2. Uniform double-GCD line sum

Put

```text
G=gcd(|eta|,|theta|), eta=G*m, theta=G*n, gcd(m,n)=1,
X=S*T,                Y=R*E.
```

For one maximal occupied line, let

```text
g0=gcd(eta*alpha,theta*beta),
A=eta*alpha/g0,       B=-theta*beta/g0.
```

Its inverse quadratic multiplier is

```text
1/sqrt(|A*B|)
 =gcd(m*alpha,n*beta)/sqrt(m*n*|alpha*beta|).       (2.1)
```

Fixed `(alpha,beta)` has only `q^o(1)` line lifts by the pinned level and
divisor theorem.  It remains to sum (2.1) over `alpha~X`, `beta~Y`.

The elementary prime-by-prime inequality

```text
gcd(m*alpha,n*beta)
 <=gcd(m,beta)*gcd(n,alpha)*gcd(alpha,beta)         (2.2)
```

uses only `(m,n)=1`.  Expand the last GCD with
`gcd(a,b)=sum_(d|a,d|b) phi(d)`.  For every `v,L`,

```text
sum_(j<=L) gcd(v,j)
 =sum_(h|v) phi(h)*floor(L/h)
 <=L*tau(v).                                       (2.3)
```

Applying (2.3) after writing `alpha=d*a`, `beta=d*b` yields

```text
sum_(alpha<=X,beta<=Y) gcd(m*alpha,n*beta)
 <=X*Y*tau(m)*tau(n)
   *sum_(d<=min(X,Y)) phi(d)*gcd(m*n,d)/d^2
 <<X*Y q^o(1).                                     (2.4)
```

The final sum is at most `tau(mn) log(2XY)`.  Enlarging dyadic intervals
to initial intervals only changes constants.  Dividing (2.4) by the
denominator in (2.1), and using `XY=E*T*R*S`, proves

```text
sum_(occupied lines) 1/sqrt(|A*B|)
 <<G*sqrt(R*S) q^o(1).                             (2.5)
```

This is uniform and has no endpoint boundary term.

The curvature factor per color is therefore at most

```text
sqrt(D/(R*S))*G*sqrt(R*S)=G*sqrt(D).               (2.6)
```

Multiplying by the proved determinant-content color mass
`sqrt(E*T*R*S)/G` gives the alternative block exponent

```text
(1+e+t+r+s)/2.                                    (2.7)
```

At `(e,t,r,s,g)=(1,0,3/16,0,0)`, (2.7) is `35/32`.

## 3. The surviving balanced grid

Take instead

```text
(e,t,r,s,g)=(1,0,3/16,3/16,0).
```

Then

```text
H=R*S=D^(3/8),
K=D^(5/16),
U=D^(5/32),
sqrt(D/H)=U^2,
color mass=sqrt(E*T*R*S)=D^(11/16).                (3.1)
```

The generic occupied-line estimate has `K=U^2` lines with
`A,B~U`, hence

```text
sum 1/sqrt(A*B)~U.                                (3.2)
```

The double-GCD estimate gives `sqrt(H)=D^(3/16)`, which is larger than
`U`; thus one retains (3.2).  Equations (3.1)--(3.2) reproduce

```text
D^(11/16)*U^2*U=D^(37/32).                         (3.3)
```

So the endpoint theorem is real but does not by itself improve the
uniform exponent.

## 4. Exact fixed-determinant chart

The common level is

```text
L=theta*u*beta+eta*alpha*v+gamma*alpha*beta.
```

After dividing by the transverse GCD and separating signs,

```text
B*u+A*v+gamma*h*A*B=C,                             (4.1)
```

where `h*A=alpha` in the `theta=1` normalization.  The integral shift

```text
w=u+gamma*alpha
```

turns (4.1) into

```text
B*w+A*v=C.                                         (4.2)
```

At (3.1), `A,B` and the integer parameter length on each line are all
`~U`.  Thus (4.2) is exactly the global `A x B` chart suggested by the
surviving polytope point.

## 5. Sharp norm of the determinant incidence

Let `T_C` be the bipartite incidence matrix of (4.2), with `A,B~U` and
`gcd(A,B)=1`.  Put

```text
g=gcd(A,w),                 h=gcd(B,v).
```

The equation implies `g*h|C`.  On a fixed `(g,h)` block, divide by the
contents.  For a fixed left vertex the admissible `B/h` occupy one residue
class modulo `A/g`, and conversely.  Therefore

```text
maximum row degree    <<1+g/h,
maximum column degree <<1+h/g.                    (5.1)
```

Schur's test and the divisor-many choices of `g,h|C` give

```text
||T_C||_(2->2)<<U^(1/2) C^o(1).                   (5.2)
```

This is sharp in the unrestricted integer chart.  Let `C=3U^2`, take the
single right vertex `(B,v)=(U,U)`, and the left vertices

```text
(A,w)=(A,3U-A),       U<=A<2U, gcd(A,3U)=1.
```

All are incident, the left contents are one, the right content is `U`,
and the star has norm `asymp sqrt(U)`.

On the special two-sided primitive subgrid, actual carrier coprimality can
give

```text
gcd(A,w)=gcd(B,v)=1,
```

and then (5.1) gives norm `O(1)`.  This useful restricted fact is not a
uniform statement over all rational-content lines.

## 6. Exact bridge obstruction

If (5.2) acted on refined token arrays whose squared masses were bounded
by the four base gap-token energies, it would replace (3.2) by `sqrt(U)`.
The exponent would be

```text
11/16+5/16+5/64=69/64.                             (6.1)
```

The primitive `O(1)` block would give exactly

```text
11/16+5/16=1.                                     (6.2)
```

The missing hypothesis is material.  Refining a base pair token by
`(A,w)` or `(B,v)` repeats its color-pair weight once for every actual
carrier/two-point chord.  The determinant graph controls incidences
*between the refined vertices*; it does not prove

```text
sum_(refined lifts over one base token) P_lift
 <<q^o(1) P_base.                                  (6.3)
```

Equation (6.3) is the varying-secant residual estimate already isolated
as (7.6) in the parabolic gap-token report.  A perfect matching makes the
logical gap transparent: copying one base token of squared mass one to
`N` matched vertices leaves the graph norm equal to one, but the refined
squared mass and the positive bilinear value are both `N`.

Actual prime-power masks do not presently supply (6.3).  They plausibly
thin the congruence stars by logarithms, but logarithms cannot provide the
required power saving, and arbitrary color weights may concentrate on the
surviving carriers.

## 7. Direct audit of the token-lift estimate

There is an exact one-token description.  Fix the top color pair `(x,y)`
and put

```text
d=s1*x-s2*y=r2*eta,
e=x*b1-y*b2,
beta=s1*b2-s2*b1.
```

Inverting this two-by-two system gives

```text
b1=(s1*e+y*beta)/d,
b2=(s2*e+x*beta)/d.                               (7.1)
```

Thus integrality is the lattice congruence

```text
s1*e+y*beta=0 (mod d).                             (7.2)
```

At the surviving block,

```text
|s1|~R, |d|~R*D, |e|<<D, beta=g0*B, B~U.          (7.3)
```

After the divisor/content data determining `g0` are frozen, there are
`O(U)` possible `B`.  The `(e,B)` box has normalized area `U/R<1`, but
this does **not** give `O(1)` points: a rank-two lattice in a thin box may
have a short primitive vector, and then all its points are collinear.  In
the present variables this is precisely a tangent chain

```text
(e,beta)=(e0,beta0)+j*(Delta_e,Delta_beta),
0<=j<U,                                            (7.4)
```

with

```text
s1*Delta_e+y*Delta_beta=0 (mod d).
```

So the strongest uniform count supplied by one-token product uniqueness
on a frozen critical content block is `U q^o(1)`, and the integer chart can
saturate that power.  The area argument proves collinearity, not sparsity.

Adding the opposite horizontal token gives no transverse equation.  If

```text
e_top   =x*b1-y*b2,
e_bottom=zeta*b1-w*b2,
```

then the four token identities imply exactly

```text
r1*e_top-r2*e_bottom=theta*beta.                   (7.5)
```

At `E=D,T=1,R=S=D^(3/16)`, every term in (7.5) has size `R*D` while each
residual is allowed size `D`.  It removes only a constant proportion of
the one-token box.  On the row-carrier side, with

```text
f_left =x*a1-zeta*a2,
f_right=y*a1-w*a2,
alpha  =r1*a2-r2*a1,
```

the companion identity is

```text
s1*f_left-s2*f_right=-eta*alpha.                   (7.6)
```

It has the same aligned scale.  Consequently the four simultaneous token
refinements still allow an `A x B` family of `U^2=K` line vertices.  This
recovers, rather than improves, the occupied-third-slice cap.

Along a tangent chain the two carrier coordinates are affine integer
forms in the chain parameter.  Requiring both to be actual primes or
prime powers is therefore a positive two-linear-form sieve problem.  Its
expected/principal density is logarithmic, of order `U/log^2 q` in a
nondegenerate admissible family, not a fixed power saving.  A
multiplicative-character expansion cannot delete that principal term.
No theorem asserting the expected lower bound is used here; equally, no
known uniform upper bound turns it into `q^o(1)`.

This is a method obstruction, not an actual-prime counterexample to FC.
The finite tangent congruence replay uses unrestricted integers.  An
asymptotic actual-prime family saturating all four product masks has not
been constructed.

```text
transverse scales alpha~ST, beta~RE:                PROVED;
uniform double-GCD line sum G*sqrt(RS):              PROVED;
one-sided endpoint curvature D^(35/32):              PROVED;
balanced D^(37/32) survivor:                          EXACT;
fixed-determinant chart B*w+A*v=C:                   PROVED;
uniform determinant-incidence norm sqrt(U):          PROVED, SHARP;
two-sided primitive incidence norm O(1):              PROVED, RESTRICTED;
conditional survivor exponent D^(69/64):              CORRECT LEDGER;
conditional primitive survivor exponent D:            CORRECT LEDGER;
refined-token no-duplication bridge:                  OPEN;
one-token lift count on a frozen critical content block U q^o: PROVED;
four-token product-uniqueness count U^2 q^o on that block: BEST CURRENT LEDGER;
actual-prime tangent saturation:                       NOT CONSTRUCTED;
fixed-determinant merger alone:                       INSUFFICIENT;
uniform parabolic curvature improvement below 37/32:  NOT PROVED.
```

The exact finite mechanisms are replayed in
`src/qp_parabolic_double_gcd_and_fixed_determinant.py` and its test module.
