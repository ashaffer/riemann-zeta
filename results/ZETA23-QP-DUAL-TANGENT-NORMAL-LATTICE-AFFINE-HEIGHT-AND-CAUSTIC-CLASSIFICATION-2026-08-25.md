# QP reciprocal curve: exact dual tangent lattices, affine height, and caustics

**Date:** 2026-08-25  
**Verdict:** the exact stationary and repeated-stationary geometry is now
classified.  There is no second exact interior degeneracy beyond the cubic
binormal of a rational tangent.  However, an exact cubic saddle need not come
from a physical integer tangent packet.  The missing arithmetic datum is a
rank-two affine-height character on the stationary normal lattice.

This gives a more precise major/minor-arc programme, but it does not prove the
aggregate nonzero-dual cancellation or the sharp four-cycle bound.

## 1. Normalization and the stationary quartic

Put

```text
lambda=C/S^2,
gamma(t)=(t,lambda/t,lambda/(1-t)),
xi=(-m,h,k),
Phi(t)=xi dot gamma(t)
      =lambda*(h/t+k/(1-t))-m*t.                     (1.1)
```

The original phase is `S*Phi(a/S)`.  Its derivatives are

```text
Phi'  =-lambda*h/t^2+lambda*k/(1-t)^2-m,
Phi'' = 2*lambda*h/t^3+2*lambda*k/(1-t)^3,
Phi'''=-6*lambda*h/t^4+6*lambda*k/(1-t)^4.           (1.2)
```

Clearing the harmless interior denominator gives the stationary quartic

```text
P(t)=m*t^2*(1-t)^2+lambda*h*(1-t)^2-lambda*k*t^2
    =-t^2*(1-t)^2*Phi'(t).                           (1.3)
```

Its discriminant factors exactly as

```text
Disc_t(P)
 =-16*lambda^2*h*k*m*Delta(h,k,m),                   (1.4)

Delta(h,k,m)
 =(m+lambda*(h-k))^3+27*lambda^2*h*k*m.              (1.5)
```

The factors `h`, `k`, and `m` include endpoint, one-inverse, and degree-drop
cases.  For `h*k<0` and the physical sign of `m`, `Delta=0` is precisely the
interior cubic caustic.

## 2. Complete cubic classification

If `Phi'=Phi''=0` in the interior, then `h` and `k` have opposite signs.  At
a rational point

```text
t=r/(r+s),        (r,s)=1,                           (2.1)
```

all integer solutions of `Phi''=0` have the form

```text
h=d*r^3,        k=-d*s^3.                            (2.2)
```

The stationary equation then forces

```text
m=-lambda*d*(r+s)^3.                                 (2.3)
```

Write `lambda=P/Q` in lowest terms and `n=r+s`.  The primitive integer
caustic frequency, in coordinates `xi=(-m,h,k)`, is

```text
c=gcd(Q,n^3),
xi_c=(P*n^3/c, (Q/c)*r^3, -(Q/c)*s^3).               (2.4)
```

Conversely, for rational `lambda`, every integer interior cubic has this
form.  Indeed, if `u=|h|` and `v=|k|`, integrality of `m` makes

```text
(u^(1/3)+v^(1/3))^3
```

rational.  This happens exactly when

```text
u=d*r^3,        v=d*s^3,        (r,s)=1.             (2.5)
```

Equivalently, after putting `z=-m/lambda`, `x=h`, and `y=-k` in the
positive-left case, (1.5) is

```text
(z-x-y)^3=27*x*y*z.                                  (2.6)
```

Taking real cube roots factors the equation by
`z^(1/3)-x^(1/3)-y^(1/3)`; the remaining quadratic factor is positive.
Thus there is no extra Pell, CRT, or other exact component hidden in the
caustic surface.

At (2.2)--(2.3),

```text
Phi'''(r/n)=-6*lambda*d*n^5/(r*s) !=0.               (2.7)
```

Every repeated interior saddle is therefore exactly cubic.  Quartic and
higher stationary points do not occur.

## 3. The complete rational stationary lattice

The caustic ray is only one line inside the full stationary normal plane.
At `t=r/n`, the stationary equation is the exact Diophantine relation

```text
Q*m*r^2*s^2=P*n^2*(k*r^2-h*s^2).                    (3.1)
```

Set

```text
g=gcd(P*n^2,Q*r^2*s^2),
A=P*n^2/g,          B=Q*r^2*s^2/g.                  (3.2)
```

Choose integers `u,v` with

```text
u*r^2-v*s^2=1.                                       (3.3)
```

Then every integer stationary frequency is uniquely

```text
xi=d*xi_0+ell*xi_1,
xi_0=(0,r^2,s^2),
xi_1=(-A,B*v,B*u),             d,ell in Z.           (3.4)
```

This is a saturated rank-two lattice.  The zero-dual ray `xi_0` is the
same-sign tangent family.  The primitive caustic (2.4) is one vector in the
same lattice.  Regular nonzero stationary modes occupy the rest of it.

The physical tangent direction is obtained by clearing denominators in
`gamma'(r/n)`.  Its primitive integer vector is

```text
V=(Q*r^2*s^2, -P*n^2*s^2, P*n^2*r^2)/g.             (3.5)
```

Equations (3.4)--(3.5) give exactly

```text
Lambda_(r,s)={xi in Z^3:xi dot V=0}
             =Z*xi_0+Z*xi_1.                        (3.6)
```

Thus every rational stationary mode is normal to a rational tangent
direction.  There is no different local geometric model.  This statement
alone does **not** say that the affine tangent line contains physical lattice
points.

## 4. Affine height is the packet criterion

Let

```text
z_0=S*gamma(r/n)
   =(S*r/n, P*S*n/(Q*r), P*S*n/(Q*s)).                (4.1)
```

The tangent line is

```text
L_(r,s)=z_0+R*V.                                      (4.2)
```

Define its stationary character

```text
chi_(r,s)(xi)=xi dot z_0 mod 1,
xi in Lambda_(r,s).                                  (4.3)
```

Since `xi dot V=0`, this phase is constant along the tangent line.  Because
`V` is primitive and (3.6) is saturated, elementary unimodular lattice
duality proves

> **Affine-height criterion.** The rational tangent line `L_(r,s)` meets
> `Z^3` if and only if
>
> ```text
> xi_0 dot z_0 in Z,       xi_1 dot z_0 in Z.         (4.4)
> ```
>
> Equivalently, the full stationary character `chi_(r,s)` is trivial.

The forward implication is immediate.  For the converse, extend the
primitive vector `V` to a unimodular basis of `Z^3`.  The two integral
normal heights in (4.4) fix an integral affine fibre; translating in the
`V` direction then reaches an integer point.

This is the exact distinction between a rational tangent direction and a
physical tangent packet.  Testing only the caustic vector is insufficient.

### 4.1 A hostile exact example

Take

```text
lambda=1/2,       S=5,       t=1/3.                  (4.5)
```

Then

```text
V=(8,-36,9),
xi_0=(0,1,4),       xi_1=(-9,0,8),
z_0=(5/3,15/2,15/4).                                (4.6)
```

The two affine heights are

```text
xi_0 dot z_0=45/2,       xi_1 dot z_0=15.            (4.7)
```

Consequently the tangent line misses `Z^3`.  Nevertheless its primitive
cubic frequency is

```text
xi_c=(27,2,-16),       xi_c dot z_0=0.               (4.8)
```

So there is an exact integral cubic saddle with integral stationary phase,
and even an index-two kernel of stationary phases, but no integer tangent
packet.  This disproves the literal rule

```text
integral cubic major arc  =>  physical tangent packet.                (4.9)
```

The concrete Fejer coefficients must cancel the nontrivial affine-character
cosets.  An analysis which isolates only the cubic ray cannot see that
cancellation.

### 4.2 Common product is too narrow

Conversely, a tangent packet need not contain an integer common-product
centre.  If

```text
lambda=1/4,       S odd,       t=1/2,                (4.10)
```

then `C=S^2/4` and the centre is half-integral, but the tangent line is

```text
(a,v,w)=(a,S-a,a),                                   (4.11)
```

which contains integer points.  Its two product errors are

```text
a*v-C=(S-a)*w-C=-(a-S/2)^2.                          (4.12)
```

Thus the correct primal obstruction is an affine lattice tangent packet,
not necessarily a packet with an integer zero-error centre.

### 4.3 Exact cyclic Fejer regrouping of one normal lattice

Write the primitive direction as

```text
V=(R,-P_0,K_0),       gcd(R,P_0,K_0)=1.              (4.13)
```

The tangent line has the intercept form

```text
(a,alpha-(P_0/R)*a,beta+(K_0/R)*a).                  (4.14)
```

An integer frequency pair `(h,k)` has an integer stationary Poisson mode
exactly when

```text
k*K_0-h*P_0==0 (mod R).                              (4.15)
```

For any finitely supported coefficients `c_h`, put

```text
P_c(theta)=sum_h c_h*e(h*theta).                     (4.16)
```

The congruence detector gives the exact identity

```text
sum_(h,k: (4.15)) c_h*c_k*e(h*alpha+k*beta)
 =1/R sum_(j mod R)
     P_c(alpha-j*P_0/R)*P_c(beta+j*K_0/R).           (4.17)
```

For the concrete triangular Fejer coefficients, the right side is an
average of nonnegative two-mask values along the cyclic rational tangent
orbit.  Moreover, one orbit point has both coordinates integral if and only
if the full affine character is trivial.  Thus exact stationary-frequency
grouping recovers the primal packet criterion without guessing it from the
cubic ray.

There is also a quantitative exact-major-arc parameter.  Put

```text
eta=min_(j mod R) max(
      ||alpha-j*P_0/R||,
      ||beta+j*K_0/R||).                              (4.18)
```

For the height-one normalized Fejer polynomial

```text
P_N(theta)=N^(-2)|sum_(0<=n<N)e(n*theta)|^2,          (4.19)
```

one has

```text
P_N(theta)<=min(1,1/(4*N^2*||theta||^2)).            (4.20)
```

Indeed, `|sin(pi*theta)|>=2||theta||` on the centred fundamental
interval.  At every orbit point in (4.17), at least one of the two distances
is at least `eta`; the other Fejer factor is at most one.  Hence

```text
1/R sum_(j mod R)
 P_N(alpha-j*P_0/R) P_N(beta+j*K_0/R)
 <=min(1,1/(4*N^2*eta^2))                             (4.21)
```

when `eta>0`, with the trivial bound one at `eta=0`.

Since `N asymp H`, the condition `eta<=c/H` is exactly the assertion that
some integer first coordinate on the rational tangent has both carrier
coordinates within `O(1/H)` of integers.  Multiplying by the shell size
`q` turns this into product tolerance `q/H=D`: it is an approximate physical
tangent packet, not merely a dual label.  If `eta>>1/H`, (4.21) gives a
genuine suppression before stationary amplitudes are inserted.

Identity (4.17) omits the frequency-dependent stationary-phase amplitude.
It therefore does not by itself estimate the actual Poisson aggregate.  Its
value is that the missing vector theorem now has an explicit core: control
the cyclic orbit when it has no point simultaneously within `H^(-1)` of the
integer lattice, and treat a near hit as an approximate tangent packet.

### 4.4 Sharp symmetric CRT orbit theorem

For the symmetric chart `lambda=1/4`, the cyclic orbit admits a stronger
uniform estimate than (4.21).  Let `r,s` be coprime, put `n=r+s`, and set

```text
g_0=gcd(n^2,4).
```

The primitive tangent direction is

```text
V=(R,-P_0,K_0)
 =(4*r^2*s^2,-n^2*s^2,n^2*r^2)/g_0.                 (4.22)
```

There are exactly two parity cases.

If `n` is even, then `r,s` are both odd, `g_0=4`, and, with `p=n/2`,

```text
R=r^2*s^2,       P_0=p^2*s^2,       K_0=p^2*r^2.    (4.23)
```

Moreover `(p,rs)=1`.  Reducing the stationary congruence

```text
k*K_0-h*P_0==0 (mod R)                              (4.24)
```

first modulo `r^2` and then modulo `s^2` gives exactly

```text
r^2|h,       s^2|k.                                  (4.25)
```

The converse is immediate.  Hence the cyclic orbit is the full CRT product
of an `r^2` grid and an `s^2` grid.

If `n` is odd, then one of `r,s` is even, `g_0=1`, and

```text
R=4*r^2*s^2,       P_0=n^2*s^2,       K_0=n^2*r^2.  (4.26)
```

Since `(n,2rs)=1`, (4.24) is now exactly

```text
h=r^2*a,       k=s^2*b,       b-a==0 (mod 4).        (4.27)
```

Thus the orbit is an average of four shifted CRT product grids.  This
index-four condition is the only gcd exception.

For the normalized Fejer polynomial `P_N`, define

```text
B_N(M)=max_theta 1/M sum_(u mod M) P_N(theta+u/M).   (4.28)
```

Writing `N=q*M+z`, with `0<=z<M`, residue-class orthogonality gives the
exact formula

```text
B_N(M)=[z*(q+1)^2+(M-z)*q^2]/N^2.                   (4.29)
```

Indeed, split `0,...,N-1` into residue classes modulo `M`.  The grid average
is the sum of the squared class sums divided by `N^2`; each class sum is at
most its cardinality, with simultaneous equality at `theta=0`.  In
particular,

```text
M>=N:       B_N(M)=1/N,
M<N:        B_N(M)<=1/M+M/(4N^2)<=5/(4M).           (4.30)
```

Combining the two parity cases proves the sharp uniform theorem

> **Symmetric cyclic Fejer theorem.** For every intercept pair `alpha,beta`,
>
> ```text
> 1/R sum_(j mod R)
>  P_N(alpha-j*P_0/R) P_N(beta+j*K_0/R)
> <=B_N(r^2)*B_N(s^2)
> <<(1/r^2+1/N)*(1/s^2+1/N).                         (4.31)
> ```

For even `n`, the left side factors exactly into the two grid averages.  For
odd `n`, it is the average of four shifted products, each bounded by the same
two maxima.  This proof uses simultaneous orbit spacing and is independent
of the affine intercepts; it is stronger than the single closest-point
parameter `eta` when the orbit is long.

The exact intercept-uniform maximum is also explicit in the index-four case.
If

```text
C_(M,c)=sum_(a==c mod 4) (N-|M*a|)/N^2,
                         |M*a|<N,                    (4.31a)
```

then positivity of every Fourier coefficient gives

```text
max_(alpha,beta) cyclic average
 =sum_(c mod 4) C_(r^2,c)*C_(s^2,c).                 (4.31b)
```

The maximum is attained at `alpha=beta=0`.  Formula (4.31) follows by
discarding the common residue condition; this can lose only a constant, not
a power.

The frequency aliases are also explicit.  In both cases write

```text
h=r^2*a,       k=s^2*b.
```

Then the stationary Poisson mode is

```text
m=n^2*(b-a)/4,                                        (4.32)
```

with (4.27) guaranteeing integrality in the odd-`n` case.  Hence there are
no hidden shorter stationary vectors: the first possible nonzero `h` and
`k` scales are `r^2` and `s^2`.  The diagonal `a=b` is the zero-dual tangent;
the off-diagonal aliases are its integer Poisson translates.

### 4.5 Consequence for the remote primitive denominator

Use the primitive cusp variables from Section 7 below.  If `(p,d)=1`, the
candidate rational tangent is

```text
t=(p+d)/(2p).                                        (4.33)
```

When `p,d` have opposite parity, its reduced numerator and complement are

```text
r=p+d,       s=p-d,
R=(p^2-d^2)^2.                                       (4.34)
```

When `p,d` are both odd, divide `r,s` by two; then

```text
R=(p^2-d^2)^2/4,                                     (4.35)
```

and the index-four case (4.27) applies.  These are the only parity changes.

In a fixed compact collar, `|d|<=(1-c)*p`, so in either case

```text
r asymp s asymp p.                                   (4.36)
```

Equation (4.31), with `N asymp H`, becomes

```text
cyclic coefficient mass <<(p^(-2)+H^(-1))^2.        (4.37)
```

The remote primal reduction gives, at its worst endpoint,

```text
p>>D^(13/48),       H=D^(17/16).                     (4.38)
```

Until the still stronger `H^(-2)` plateau `p^2>=H` is reached, (4.37) is
bounded by

```text
p^(-4)
 <<D^(-13/12)
 =H^(-1)*D^(-1/48).                                  (4.39)
```

Thus the exact symmetric cyclic orbit supplies **one full `H` saving plus
`D^(1/48)`**, rather than only a square-root saving, relative to the unit
`l^1` mass of the two Fejer coefficient sequences.

There are two apparent exceptions, both already classified.  If `p-d` or
`p+d` is small, one grid modulus is small; this is an endpoint tangent and is
excluded by the compact collar.  If `d=0`, primitivity forces `p=1`.  This is
exactly the bounded-denominator translated-tangent sector (`kappa=0`) already
paid by the square-root packet budget.  Small nonzero `d/p` causes no loss in
(4.31): both grid moduli remain comparable to `p^2`.

The content `g=gcd(rho,kappa)` in the primal cusp changes the translate, not
the primitive direction.  Controlling the number of contents and passing
from an approximate rational tangent to exact stationary classes remain
separate tasks.  Likewise, the actual stationary-phase amplitude varies
with `(a,b)`.  Consequently (4.39) is a rigorous per-direction coefficient
gain, not yet the global remote-minor estimate.

### 4.6 The exact rational-stationary remote sector closes

The amplitude variation does not destroy the saving for **exact** rational
stationary points.  It can be handled by absolute value after a dyadic
frequency decomposition.

Fix primitive directions `p asymp P` in a compact collar.  There are

```text
O(P^2)                                                  (4.40)
```

choices of the coprime pair `(p,d)`.  For a fixed direction, frequencies in
dyadic boxes `|h|asymp K_1`, `|k|asymp K_2` must have

```text
h=r^2*a,       k=s^2*b,       r,s asymp P.            (4.41)
```

Hence the number of nonzero alias pairs is

```text
O((1+K_1/P^2)*(1+K_2/P^2)),                           (4.42)
```

with the all-zero pair removed.  Each triangular Fejer coefficient is
`O(H^(-1))`.

For opposite signs, the uniform third-derivative estimate is

```text
|I(h,k,m)|<<q^(2/3)*max(K_1,K_2)^(-1/3).              (4.43)
```

The main two-nonzero term in (4.42), summed over all directions, is therefore

```text
q^(2/3)*H^(-2)*P^(-2)*K_1*K_2*max(K_1,K_2)^(-1/3).
                                                               (4.44)
```

This is increasing in both frequency scales, so dyadic summation is
dominated by `K_1=K_2=H` and costs

```text
q^(2/3)*H^(-1/3)*P^(-2)
 =D^(49/48)*P^(-2).                                   (4.45)
```

The one-zero terms in (4.42) use the ordinary one-inverse
second-derivative bound and are smaller.  For same-sign nonzero frequencies,

```text
|I(h,k,m)|<<sqrt(q/max(K_1,K_2)),                     (4.46)
```

and the analogue of (4.44) is at most

```text
sqrt(q)*H^(-1/2)*P^(-2)=D^(1/2)*P^(-2).              (4.47)
```

Thus (4.45) is the worst exact-stationary contribution.  Summing dyadic
`P>=P_0`, where

```text
P_0=D^(13/48),                                        (4.48)
```

is dominated by the first block and gives

```text
D^(49/48)*P_0^(-2)
 =D^(23/48)
 =D^(1/2-1/48).                                      (4.49)
```

There is no hidden Poisson multiplicity in this count.  For each direction
and alias pair, (4.32) determines exactly one integer `m`.  Conversely, for
fixed `(h,k,m)`, `Phi''` has no interior zero in the same-sign case and one
in the opposite-sign case, so `Phi'` has at most two interior roots.  A
stationary partition therefore counts each triple only `O(1)` times.  The
identically zero triple `(h,k,m)=(0,0,0)` must, and does, remain in the
separate zero mode rather than being assigned to every direction.

Consequently:

> **Exact remote rational-stationary theorem.** After the translated-tangent
> and endpoint sectors are removed, all exact rational stationary points
> whose primitive denominator satisfies `p>=D^(13/48)` contribute
> `O(D^(23/48)q^o(1))`, even when the stationary amplitudes are estimated
> absolutely.

This is below the square-root target by `D^(-1/48)`.  It does not yet close
the remote primal theorem: irrational stationary points, quantitative
neighbourhoods of rational tangents, and the transfer from the approximate
primal slope in (7.11) to exact stationary classes are not included in
(4.49).

## 5. Every genuine lattice tangent has exactly the predicted capacity

Let

```text
a_0=S*r/n,       b_0=S*s/n,       C=lambda*S^2.      (5.1)
```

At an arbitrary first coordinate `a`, the tangent line has

```text
v_tan=C/a_0-C*(a-a_0)/a_0^2,
w_tan=C/b_0+C*(a-a_0)/b_0^2.                         (5.2)
```

Direct multiplication gives the exact identities

```text
a*v_tan-C       =-C*(a-a_0)^2/a_0^2,
(S-a)*w_tan-C   =-C*(a-a_0)^2/b_0^2.                (5.3)
```

If (4.4) holds, the integer points on the line have their `a`-coordinates
spaced by

```text
R=V_1=Q*r^2*s^2/g >=1.                               (5.4)
```

Therefore the number satisfying product widths `D*U,D*V` is at most

```text
1+(2/R)*min(a_0*sqrt(D*U/C),b_0*sqrt(D*V/C)).        (5.5)
```

On the fixed shell this is

```text
O(1+sqrt(D*min(U,V))/R).                             (5.6)
```

This is precisely the packet term in the conjectural special-curve theorem,
with an additional direction-denominator gain.  Hence no single exact
rational tangent packet exceeds the desired obstruction.

## 6. What the special physical centre changes

For the actual centre

```text
C=q^3/(8*x),
lambda=q^3/(8*x*S^2)=P/Q                             (6.1)
```

in lowest terms, one has explicitly

```text
G=gcd(q^3,8*x*S^2),
P=q^3/G,       Q=8*x*S^2/G.                          (6.2)
```

At slope `r/s`, the primitive caustic multiplier and largest Fejer
frequency are

```text
d=Q/gcd(Q,(r+s)^3),
max(|h|,|k|)=d*max(r,s)^3.                           (6.3)
```

Since `(r+s)^3<=8*max(r,s)^3`, an exact caustic inside
`|h|,|k|<=H` necessarily satisfies

```text
Q<=8*H.                                              (6.4)
```

Thus a large reduced denominator deletes exact cubic modes completely.
There is no uniform lower bound forcing `Q>8H`, however; resonant physical
parameters can have a small reduced denominator.  Equation (6.2) therefore
does not provide a uniform power saving.

Even when exact cubics occur, their common-cube classification gives only
`O(H)` frequency pairs.  The previously proved coefficient ledger remains

```text
exact cubic total:          D^(-1/24),
one near-Airy mode/pair:    D^(49/48),
regular absolute total:     D^(25/16),
target:                      D^(1/2).                 (6.5)
```

The missing factor in the absolute regular sum is still

```text
D^(25/16-1/2)=D^(17/16)=H.                           (6.6)
```

The new classification explains where that cancellation must live: across
the full normal-lattice character, not inside the sparse caustic ray.

## 7. Exact primal-dual cusp correspondence

For `C=Q_0^2,S=2Q_0`, write

```text
a=Q_0+y,       b=Q_0-y,
v=Q_0-y+r_0,   w=Q_0+y+s_0.                          (7.1)
```

The product errors are

```text
e=r_0*(Q_0+y)-y^2,
f=s_0*(Q_0-y)-y^2.                                   (7.2)
```

Put

```text
rho=r_0+s_0,       kappa=s_0-r_0,
sigma=e+f,         tau=e-f.                          (7.3)
```

Then exactly

```text
tau=y*rho-Q_0*kappa,                                 (7.4)

Q_0*(rho^3-kappa^2*(rho+2Q_0))
 =sigma*rho^2+tau*kappa*(rho+4Q_0)+2*tau^2.          (7.5)
```

On the zero-error curve,

```text
A_y=Q_0*y^2/(Q_0^2-y^2),
t_y=y^3/(Q_0^2-y^2),
rho=2*A_y,       kappa=2*t_y,                        (7.6)
```

and (7.5) becomes

```text
rho^3=kappa^2*(rho+2Q_0).                            (7.7)
```

This is exactly the primal version of the centered dual cusp.  With

```text
p=h+k,       d=k-h,       ell=d-m,                   (7.8)
```

the centered phase is

```text
constant+ell*y+p*A_y+d*t_y
 =constant+ell*y+(p*rho+d*kappa)/2.                  (7.9)
```

Thus `(p,d,ell)` are the Fourier-conormal variables to the primal
`(rho,kappa,y)` cusp.  The centered cubic `p=ell=0` is the binormal at its
singular tangent packet.

There is one immediate sharp slice.  In the compact core
`D*max(U,V)=o(Q_0)`, if `rho=0`, then (7.4) and `|tau|<<D*max(U,V)` force
`kappa=0`.  Hence `r_0=s_0=0`, and (7.2) gives

```text
|y|<<sqrt(D*min(U,V)).                               (7.10)
```

This recovers the tangent packet exactly.  For `rho!=0`, however, (7.5)
alone is not a counting theorem.  One must retain the divisibility

```text
rho | Q_0*kappa+tau,
y=(Q_0*kappa+tau)/rho,                               (7.11)
```

and control the two short error labels jointly.  Summing `sigma,tau`
absolutely loses the desired power.  No approximate stability estimate is
proved here.

## 8. The revised breakthrough target

The exact classification suggests an **affine-height stationary large
sieve**, rather than a theorem which calls every caustic a packet.

A successful argument would:

1. decompose regular Poisson modes by their rational tangent normal lattices
   `Lambda_(r,s)`;
2. retain the full character `chi_(r,s)`, including both generators in
   (3.4);
3. use the exact cyclic Fejer identity (4.17), while controlling the varying
   stationary amplitudes;
4. convert trivial or `H^(-1)`-near-trivial characters into the packet bound
   (5.6), and suppress nontrivial orbit cosets such as (4.5)--(4.8);
5. square-sum over tangent locations or denominators so that the regular
   `D^(25/16)` ledger gains the missing factor `H`.

This route has the correct obstruction and now has an exact major-arc
classifier.  The quantitative character cancellation in steps 3--5 remains
unproved.

## Reproducibility

The stationary lattice, discriminant, affine-height criterion, special-centre
denominator gate, tangent product errors, and primal-dual cusp identities are
implemented and checked in

```text
src/qp_dual_tangent_major_arc.py
src/test_qp_dual_tangent_major_arc.py
```

Nineteen focused tests pass, including an exhaustive small-parameter comparison
between the affine-height criterion and direct integer intersections of the
tangent line, direct verification of the cyclic Fejer regrouping, and the
exact `eta` envelope.  Both parity forms of (4.22)--(4.27), the exact grid
maximum (4.29), its exact index-four refinement, and the exponent gains
(4.39) and (4.49) are also checked.

## Binary status

```text
exact rational stationary lattice:                    CLASSIFIED;
all interior repeated saddles exactly cubic:          PROVED;
hidden exact Pell/CRT caustic component:               EXCLUDED;
caustic phase alone implies physical packet:           FALSE;
full affine character trivial iff integer packet:      PROVED;
one lattice tangent packet <= sqrt(D*min(U,V)):         PROVED;
aggregate affine-character cancellation:               OPEN;
sharp four-cycle bound:                                NOT PROVED.
```
