# QP reflected algebraic major arcs: the integer-c branch and its offset obstruction

**Date:** 2026-08-25  
**Verdict:** the literal integer-`c` reflected family is exact and cheap.  At
fixed `Q` it contributes

```text
O(1+sqrt(B/Q^(1/3)))=O(D^(23/96))                   (0.1)
```

physical points in the energy core, well inside the `sqrt(A)` packet budget.
This argument does not put the family inside the smaller volume allowance
`Z=1+AB/Q`.

Classification by small `c=Q-p(p^2-d^2)` alone is false.  An exact balanced
tangent-offset family has product errors `O(p|u|+u^2)` while its small-`c`
cost is `2p^2|u|`.  It is high primitive, has arbitrarily small tangent
character mismatch, and gives the same exact reflected completion collision.
The correct local coordinates are `(g-2d^2,c,u)`, not `c` alone.

The first two cancellation axes in those coordinates are now also cheap.
The balanced axis `h=0` and both one-band axes
`h=+-d*u` each contribute `O(sqrt(A)Q^epsilon)` at fixed `Q`, even for the
asymmetric window `|e|<=A<=B`, `|f|<=B`.  The surviving algebraic gate is
the genuinely nonzero residual `k=h^2-d^2*u^2`.

On the central-content chart `g=2d^2`, that residual gate is now closed as
well.  In the already-reduced remote collar `|y|>>Q^(2/3)`, every point has
`|u|<sqrt(B)`, and all nonzero offsets together contribute

```text
O(B/Q^(1/3))=O(D^(23/48))=o(sqrt(A)).                (0.2)
```

Thus no central-content `k!=0` obstruction remains.  The next chart is the
noncentral content defect `g-2d^2!=0`.  Recentring that chart at its natural
scaled cusp closes its balanced and both one-band axes at
`O(sqrt(A)Q^epsilon)`.  Only the genuinely two-sided scaled residual remains.

No sharp four-cycle theorem is proved here.

## 1. Exact integer-c family

Let `p>d>=1` be coprime, put

```text
ell=p^2-d^2,
Q=p*ell+c,                 y=d*ell,
r=d^2*(p-d),               s=d^2*(p+d),              (1.1)
```

and allow any integer `c` for which `Q>|y|`.  Then

```text
rho=r+s=2p*d^2,            kappa=s-r=2d^3,
g=gcd(rho,kappa)=2d^2.                                (1.2)
```

Direct multiplication gives

```text
e=r*(Q+y)-y^2=c*d^2*(p-d),
f=s*(Q-y)-y^2=c*d^2*(p+d).                            (1.3)
```

The reduced invariants are

```text
n=p*y-Q*d=-c*d,
T=g*p*(p^2-d^2)-2Q*d^2=-2c*d^2,
L=g^2*T=-8c*d^6.                                     (1.4)
```

Thus `c=0` is the exact common-product/cusp major arc, while every `c!=0`
has `n*T*L*kappa!=0`.  Reflection

```text
(y,r,s) -> (-y,s,r)                                  (1.5)
```

swaps `e,f`, changes `(p,d)` to `(p,-d)`, and preserves `L,T`.  The first
coordinates sum exactly to `2Q`, so the two ordered singleton packets have
the same completion output.

There is no parity loss: `g=2d^2` makes both
`r=g(p-d)/2` and `s=g(p+d)/2` integral for every coprime `p,d`.

## 2. Fixed-Q factorization and the sharp elementary count

At fixed `Q`, the family satisfies

```text
Q-c=p*(p-d)*(p+d).                                    (2.1)
```

For fixed `c`, every solution is an ordered divisor triple of `Q-c`, with
the extra relation `(p-d)+(p+d)=2p`.  Hence there are at most
`tau_3(Q-c)=Q^o(1)` solutions for that `c`.

The product bands give a stronger count.  It is enough to impose the wider
reflected-pair condition

```text
|c|*d^2*(p+d)<=B.                                    (2.2)
```

Assume `c!=0` and `2B<Q`.  Then

```text
p^3>=p*(p^2-d^2)=Q-c>=Q-B,
d^2*p<=B.                                             (2.3)
```

Put `P_0=ceil((Q-B)^(1/3))`.  For fixed `d`, define

```text
F_d(p)=p^3-p*d^2.                                     (2.4)
```

For `p>d`, consecutive values have the exact gap

```text
F_d(p+1)-F_d(p)=3p^2+3p+1-d^2>2p^2.                 (2.5)
```

Two admissible values for the same `d` would differ by at most `2B`, since
`F_d(p)=Q-c` and `|c|<=B`.  Once `P_0^2>=B`, (2.5) rules this out.  Therefore
there is at most one `p` for each signed `d`, and (2.3) proves

```text
# integer-c reflected points
 <=2*floor(sqrt(B/P_0)).                              (2.6)
```

This counts both signs of `d`; coprimality only reduces it.  In the energy
core

```text
Q=D^(33/16),             B<D^(7/6),
P_0 asymp Q^(1/3)=D^(11/16),                         (2.7)
```

so

```text
sqrt(B/P_0)<=D^(23/96)<D^(1/2)<=sqrt(A).             (2.8)
```

The margin is `25/96`.  If both reflected orientations must fit the narrower
`A` band, replace `B` by `A` and gain further.

The estimate (2.8) assigns this branch to the existing square-root algebraic
packet budget.  It does **not** prove a `Z=1+AB/Q` count: at balanced masks
`Z` can stay bounded while the right side of (2.6) is a positive power.
No fixed-`Q` counterexample to a stronger `ZQ^o(1)` count was found, but it
does not follow from factorization and cubic gaps alone.

## 3. Exact reflected normal coordinates

For an arbitrary primitive point define

```text
ell=p^2-d^2,          c=Q-p*ell,
u=y-d*ell.                                               (3.1)
```

Then

```text
n=p*u-c*d,                                             (3.2)
T=p*ell*(g-2d^2)-2c*d^2,                              (3.3)
```

and exact expansion gives

```text
e=(g/2-d^2)*ell^2
  +(g/2)*(p-d)*(c+u)-2d*ell*u-u^2,

f=(g/2-d^2)*ell^2
  +(g/2)*(p+d)*(c-u)-2d*ell*u-u^2.                    (3.4)
```

On the central content branch `g=2d^2`, this becomes

```text
e=d*(p-d)*[d*c-(2p+d)*u]-u^2,
f=d*(p+d)*[d*c-(2p-d)*u]-u^2.                         (3.5)
```

Put

```text
h=d*c-2p*u.                                           (3.6)
```

Then the same equations are

```text
e=d*(p-d)*(h-d*u)-u^2,
f=d*(p+d)*(h+d*u)-u^2.                                (3.7)
```

The `c`-family is only the axis `u=0`.  Equations (3.7) show an independent
balanced axis `h=0`, as well as the one-band cancellation directions
`h=+-d*u`.  Therefore small physical errors do not force `c` itself to be
small: `c` may be of order `p*u/d` and cancel coherently.

The leading term in (3.4) also shows why a complete classification must
track the content defect `g-2d^2`.  This report does not prove that every
high primitive obstruction lies in finitely many exact rays of the
three-variable normal form.

## 4. Peel the balanced height `h=0`

On `g=2d^2`, suppose

```text
h=d*c-2p*u=0.                                         (4.1)
```

Since `(p,d)=1`, this forces `p|c`.  Write

```text
c=p*lambda,             2u=d*lambda.                 (4.2)
```

Thus `d*lambda` must be even, and conversely (4.2) parametrizes every
integral solution of `h=0`.  The physical centre becomes

```text
Q=p*(ell+lambda),       y=d*(ell+lambda/2),           (4.3)
```

so in particular

```text
p|Q.                                                   (4.4)
```

Equations (3.7) reduce exactly to

```text
e=-d^2*(p-d)*u-u^2,    f=d^2*(p+d)*u-u^2.            (4.5)
```

If `u=0`, then (4.1) also gives `c=0`, which is the already-removed exact
cusp.  Hence a remote `h=0` point has `|u|>=1`.  Subtracting (4.5),

```text
|e-f|=2p*d^2*|u|<=A+B<=2B,                           (4.6)
```

and therefore

```text
d^2*p<=B.                                              (4.7)
```

Moreover (4.1) and (4.6) give

```text
|c|=2p*|u|/|d|<=2B/|d|^3<=2B.                        (4.8)
```

Consequently `p^3>=Q-2B`, so `p>>Q^(1/3)`.  For fixed `Q`, first choose the
divisor `p|Q`, then `d`; (4.2) determines `lambda,u,c`.  Counting both
reflected signs gives

```text
# {remote h=0 points}
 <<tau(Q)*sqrt(B/Q^(1/3))
 <<D^(23/96)*Q^epsilon
 <<sqrt(A)*Q^epsilon.                                 (4.9)
```

Thus the balanced-height branch is a second affordable algebraic major arc.
Like the `u=0` branch, this proof assigns it to the square-root budget, not
uniformly to `Z`.

### 4.1 The next residual invariant

After deleting `h=0`, put

```text
j_-=h-d*u,             j_+=h+d*u,
k=j_-*j_+=h^2-d^2*u^2.                               (4.10)
```

Equations (3.7) give the exact factorization

```text
(e+u^2)*(f+u^2)=d^2*(p^2-d^2)*k.                     (4.11)
```

The next algebraic major arcs are exactly `k=0`, namely

```text
h= d*u  => d*c=(2p+d)*u,
h=-d*u  => d*c=(2p-d)*u.                              (4.12)
```

Let `gamma=gcd(d,2)`.  Since
`gcd(d,2p+-d)=gamma`, their integral parametrizations are

```text
u=(d/gamma)*lambda,
c=((2p+d)/gamma)*lambda                 (h=d*u),

u=(d/gamma)*lambda,
c=((2p-d)/gamma)*lambda                 (h=-d*u).     (4.13)
```

They cancel one of the two linear bands exactly:

```text
h=d*u:     e=-u^2,
h=-d*u:    f=-u^2.                                  (4.14)
```

These branches have a fixed-`d` divisor parametrization.  Write
`epsilon=+1` for `h=d*u` and `epsilon=-1` for `h=-d*u`, and put

```text
mu=2u/d,                x=2p+epsilon*d.              (4.15)
```

The divisibility in (4.12)--(4.13) makes `mu` integral.  Substitution into
`Q=p*(p^2-d^2)+c` gives the exact identity

```text
8Q-3epsilon*d^3
 =x*[x^2-3epsilon*d*x-d^2+4mu].                     (4.16)
```

Thus a fixed signed `d` supports at most
`tau(|8Q-3epsilon*d^3|)` points: choose the divisor `x`, after which `p`,
`mu`, `u`, and `c` are all determined.  The possible zero target causes no
exception in the energy core.  Indeed a non-cusp point on either branch has
`|u|>=|d|/2`, while (4.14) gives `|u|<=sqrt(B)`.  Hence
`|d|<=2sqrt(B)` and

```text
|d|^3=O(B^(3/2))=o(Q),                               (4.17)
```

so the integer in (4.16) is comparable with `Q`.

It remains to count `d`.  On the `epsilon=+1` branch, `e=-u^2`, so
`|u|<=sqrt(A)` and directly `|d|<=2sqrt(A)`.  On the
`epsilon=-1` branch put `r=d^2*(p-d)>0`; then

```text
f=-u^2,                 e=-u*(2r+u).
```

If `u>=0`, the narrow condition `|e|<=A` again gives
`u^2<=A`.  If `u=-v<0` and `v<=r`, then
`A>=v*(2r-v)>=r*v`; using `v>=|d|/2` and the fixed compact collar
`r>>d^2*p` gives `|d|<<A^(1/3)`.  Finally, if `v>r`, then
`r<sqrt(B)`, so `|d|<<B^(1/4)`.  In the energy core
`A>=D` and `B<D^(7/6)`, whence both of the latter bounds are
`O(sqrt(A))`.  Therefore, without requiring the reflected point to satisfy
the same asymmetric mask,

```text
# {k=0 one-band points at fixed Q}
 <<sqrt(A)*Q^epsilon.                                (4.18)
```

The case `u=0` is the already-deleted exact cusp.  Equivalently, reducing
(4.12) modulo `p` gives `p|(Q-epsilon*u)`; when a reflected-pair mask puts
the square error in the narrow band for both signs, summing these divisors
over `|u|<=sqrt(A)` gives the same estimate even more directly.

After deleting `k=0`, both residual factors are nonzero and (4.11) gives

```text
1<=|k|<=((A+u^2)*(B+u^2))/(d^2*(p^2-d^2)).           (4.19)
```

This is the next minor label in the recursive algebraic peeling.  Treating
all `h!=0` points as dispersed before the two proved peels would miss exact
cancellations.  The transverse identity below closes this remaining label
without needing to sum (4.19) factor by factor.

### 4.2 The nonzero-`k` central chart closes automatically

There is an additional exact identity which is stronger than applying
(4.19) divisor by divisor.  Recall

```text
n=p*y-Q*d,                  sigma=e+f.
```

On `g=2d^2`, direct substitution in (3.4), or adding the two equations in
(3.7), gives

```text
u*y=-d*p*n-sigma/2.                                  (4.20)
```

Since `e-f=2d^2*n`, the bands imply

```text
|n|<=B/d^2,             |sigma|<=2B,
|u*y|<=p*B/|d|+B.                                    (4.21)
```

The slope equation `p*y=Q*d+n` also gives

```text
p/|d| << Q/|y|.                                      (4.22)
```

Here and below the constants depend only on the fixed compact collar; the
error `n` is negligible because `B=o(Q)`.  Combining (4.20)--(4.22),

```text
|u| << Q*B/y^2+B/|y|.                                (4.23)
```

The surviving remote chart already has `|y|>>Q^(2/3)`.  Therefore

```text
|u| << B/Q^(1/3)=o(sqrt(B)),                          (4.24)
```

where the last ratio is
`sqrt(B)/Q^(1/3)<=D^(-5/48)`.  Consequently the proposed
`|u|>sqrt(B)` sector is empty for sufficiently large `D`; the apparent
large-offset relative-divisor problem never occurs in this remote chart.

It remains to count `|u|<=sqrt(B)`.  Put

```text
a=e+u^2=d*(p-d)*j_-,       b=f+u^2=d*(p+d)*j_+.
```

Then `|a|,|b|<=2B`.  Since `p+-d` is comparable with `p` in the compact
collar,

```text
|j_-|+|j_+| << B/(|d|*p).                            (4.25)
```

Using `j_+-j_-=2d*u` and `j_++j_-=2h`, this yields

```text
|u| << B/(d^2*p),          |h| << B/(|d|*p),
|c|=|(h+2p*u)/d| << B/|d|^3.                         (4.26)
```

As `Q=p*(p^2-d^2)+c`, compactness and `B=o(Q)` now force

```text
p asymp P:=Q^(1/3).                                  (4.27)
```

For nonzero integral `u`, summing (4.26) over signed `d` gives

```text
sum_{d!=0} floor(C*B/(d^2*P)) << B/P.                (4.28)
```

There is no hidden multiplicity in `p`.  For fixed `(d,u)`, define

```text
H_{d,u}(p)=d*Q-d*p*(p^2-d^2)-2p*u=h.                 (4.29)
```

Every candidate has `|H_{d,u}(p)|<<B/(|d|P)`, whereas consecutive values
change by

```text
|H_{d,u}(p+1)-H_{d,u}(p)|
 >=2|d|P^2-2|u| >> |d|P^2.                           (4.30)
```

Because `B=o(P^3)`, the gap in (4.30) exceeds twice the allowed interval in
(4.29).  Hence each signed `(d,u)` supports at most one `p`.  The case
`u=0` is the already-counted integer-`c` axis.  Altogether,

```text
# {central-content remote points with k!=0}
 << B/Q^(1/3)
 <=D^(23/48)
 <=D^(-1/48)*sqrt(A).                                (4.31)
```

This closes the full nonzero-`k` chart under the existing remote and energy
cuts.  It does not use a divisor estimate for (4.19); the transverse identity
(4.20) and the cubic gap are stronger.

### 4.3 Noncentral content: recenter at the scaled cusp

Write

```text
Delta=g-2d^2,                 lambda=g/(2d^2)
      =1+Delta/(2d^2).                                (4.32)
```

The term `Delta*ell^2/2` in (3.4) cannot be used as an unconditional lower
bound.  Its cancellation changes the exact cusp scale from `1` to `lambda`.
Define the rational deviations

```text
c_lambda=Q-lambda*p*ell,
u_lambda=y-lambda*d*ell,
h_lambda=d*c_lambda-2p*u_lambda.                      (4.33)
```

Direct expansion gives the same normal form at this new scale:

```text
e=lambda*d*(p-d)*(h_lambda-d*u_lambda)-u_lambda^2,
f=lambda*d*(p+d)*(h_lambda+d*u_lambda)-u_lambda^2.    (4.34)
```

Thus a large `Delta*ell^2` is harmless precisely when `(c,u)` move toward
the scaled cusp in (4.33).  Clearing all denominators produces the integral
cancellation coordinates

```text
T=g*p*ell-2Q*d^2,          v=2d*y-g*ell,
z=T+2p*v.                                             (4.35)
```

They satisfy

```text
c_lambda=-T/(2d^2),        u_lambda=v/(2d),
h_lambda=-z/(2d),          2d*n=T+p*v,                (4.36)

4d^2*e+v^2=-g*(p-d)*(z+d*v),
4d^2*f+v^2=-g*(p+d)*(z-d*v).                          (4.37)
```

In particular,

```text
(4d^2*e+v^2)*(4d^2*f+v^2)
 =g^2*(p^2-d^2)*(z^2-d^2*v^2).                       (4.38)
```

This is the correct arbitrary-content analogue of (4.11).  The old exact
cusp is `T=v=0`; the new balanced and one-band axes are

```text
z=0,                    z=d*v,                    z=-d*v.  (4.39)
```

There is again a transverse identity which prevents a genuinely large
shift from hiding in (4.37).  From (4.34), or directly from the definitions,

```text
u_lambda*y=-(g*p/(2d))*n-sigma/2,
v*y=-g*p*n-d*sigma.                                  (4.40)
```

Since `|n|<=2B/g`, the remote slope equation gives

```text
|u_lambda| << Q*B/y^2+B/|y|
             << B/Q^(1/3)
             <=D^(23/48).                            (4.41)
```

This is below `sqrt(A)` by `D^(1/48)` and below `sqrt(B)` by
`D^(5/48)`.  Consequently `v^2=o(d^2*A)`, so the asymmetric widths in
(4.37) retain their full strength.  Using `p+-d asymp p`, (4.37) yields
the quantitative scaled-cusp box

```text
|z+d*v| << d^2*A/(g*p),
|z-d*v| << d^2*B/(g*p),
|v|     << d*B/(g*p),
|T|     << d*B/g.                                    (4.42)
```

Thus any point outside (4.42) has at least one product error exceeding its
band.  In particular `g>>dB` forces `T=0`, so that sector is already the
deleted `L=0` cusp; and `g*p>>dB` forces an automatic reduction to the
`v=0` scaled axis.

The first new axis has useful arithmetic rigidity.  If `z=0`, then

```text
p*(g*ell+2v)=2Q*d^2,
```

and `(p,d)=1` implies

```text
p | 2Q,                    2d | p*v.                 (4.43)
```

Hence its primitive denominator is divisor-many.  If `v!=0`, then `d|v`;
writing `v=d*w`, (4.37) becomes

```text
4e+w^2=-g*(p-d)*w,
4f+w^2= g*(p+d)*w,
g*p*|w|<=2(A+B).                                     (4.44)
```

The scaled balanced axis is in fact affordable, including the asymmetric
bad sign.  Work first with `d>0`, put

```text
M=2Q/p,                    a=g/d.
```

Then (4.43) and the definition of `T` give

```text
a*(p^2-d^2)+2w=M*d.                                 (4.45)
```

Reducing (4.45) modulo `p-d` and `p+d` gives

```text
p-d | 2(Q-w),                p+d | 2(Q+w).           (4.46)
```

Consequently a fixed `w` has only `Q^epsilon` possibilities: choose the
divisor `p|2Q`, then the divisors in (4.46); `d` and `a` are determined.
If `w>0`, (4.44) says

```text
4e=-w*[g*(p-d)+w],
```

so `w<=2sqrt(A)`.  If `w=-t<0`, then

```text
4f=-t*[g*(p+d)+t],                                  (4.47)
```

and hence `t<=2sqrt(B)`.  The range `t<<sqrt(A)` is again counted by
(4.46).  In the remaining range put

```text
eta=t-g*(p-d).
```

The narrow error is now

```text
4e=-t*eta,                 |eta|<=4A/t<<sqrt(A).     (4.48)
```

Substituting `t=eta+d*a*(p-d)` into (4.45), with `w=-t`, collapses the
large second-root cancellation to

```text
a*(p-d)^2=M*d+2eta,
(p-d)*[a*(p-d)+M]=2(Q+eta).                          (4.49)
```

For fixed `eta`, first choose `p|2Q` (and hence `M`) and then the divisor
`p-d|2(Q+eta)`; this determines `d` and `a`.  Thus each `eta` is
divisor-many, and the number of possible `eta` is `O(sqrt(A))`.  The
negative-`d` half-collar is identical after interchanging the two product
errors and replacing `w` by `-w`.  Therefore

```text
# {scaled balanced-axis points z=0}
 <<sqrt(A)*Q^epsilon.                                 (4.50)
```

The one-band axes `z=+-d*v` similarly put `-v^2/(4d^2)` into one physical
error and obey the congruences

```text
v = +2Q*d (mod p)       or       v = -2Q*d (mod p).  (4.51)
```

They too are affordable.  Integrality of the square error gives
`v=2d*xi`.  On the left axis `z=-d*v`,

```text
e=-xi^2,                 n=-(p+d)*xi,
p | Q-xi,                p+d | Q+xi.                 (4.52)
```

Thus `|xi|<=sqrt(A)` and a fixed `xi` is divisor-many.  On the asymmetric
right axis `z=d*v`,

```text
f=-xi^2,                 e=-xi*[g*(p-d)+xi],
n=-(p-d)*xi.                                        (4.53)
```

The ranges `xi>=0` and `|xi|<<sqrt(A)` are again immediate.  In the only
bad range write `xi=-t`, `t>>sqrt(A)`, and
`eta=t-g*(p-d)`.  Then `e=-t*eta`, so
`|eta|<<A/t<<sqrt(A)`.  If `a=p-d` and `g=d*h`, exact
substitution gives

```text
a | 2(Q+eta),             a-d | 2(Q+3eta),           (4.54)
```

apart from the single primitive case `(p,d)=(2,1)`.  Fixed `eta` is
therefore divisor-many.  Consequently both scaled one-band axes satisfy

```text
# {z=d*v or z=-d*v} <<sqrt(A)*Q^epsilon.             (4.55)
```

The remaining noncentral minor label is

```text
K=z^2-d^2*v^2 !=0,                                  (4.56)
```

with the exact product factorization (4.38) and the thin box (4.42).  Since
both integral factors `z+d*v` and `z-d*v` are now nonzero, the narrow one
immediately forces

```text
g*p << d^2*A,                                        (4.57)

1<=|K| << d^4*A*B/(g^2*p^2).                        (4.58)
```

The continuous remote identities give

```text
g*p/d^2 asymp Q/p^2
```

in the fixed compact collar.  Therefore every surviving residual point has

```text
p >> sqrt(Q/A) >=D^(77/160).                         (4.59)
```

This improves the original remote floor `D^(43/144)` substantially.  The
region `g*p>>d^2*A` is automatically empty after the three axis peels.
Unlike the central chart, summing the possible contents `g` in (4.42) has
not yet been closed at `sqrt(A)`: its expected two-rounding size is the
volume `AB/Q`, but an entrywise divisor bound loses the joint rounding.
This is now the precise noncentral gate.

The need for the scaled recentering is not cosmetic.  For every integer
`lambda=t>=1`, take `d=1` and

```text
Q=t*p*(p^2-1)+2p*u,       y=t*(p^2-1)+u,
g=2t,                     r=t*(p-1), s=t*(p+1).      (4.60)
```

Then `Delta=2(t-1)` and the raw leading term is
`(t-1)*(p^2-1)^2`, while

```text
e=-u*[t*(p-1)+u],          f=u*[t*(p+1)-u],
z=0.                                                   (4.61)
```

Thus arbitrarily large nonzero content defect can coexist with small
physical errors through an exact scaled balanced cancellation.  This family
falsifies any attempted lower bound based on `Delta*ell^2` alone, but it
lies on the explicitly isolated divisor axis (4.43), since `p|Q`.

## 5. Hostile balanced-offset branch

Take `d=1`, `g=2`, and integers `p>=3`, `0<|u|<p`.  Choose the balanced
height

```text
c=2p*u,               Q=p*(p^2-1)+2p*u,
y=p^2-1+u,            r=p-1,        s=p+1.           (5.1)
```

Here `h=c-2pu=0`.  Equations (3.7) give

```text
e=-u*(p+u-1),          f=u*(p+1-u).                  (5.2)
```

The remote invariants are

```text
n=-p*u,                T=-4p*u,
L=-16p*u,              kappa=2.                      (5.3)
```

Its physical/exact-tangent mismatch is

```text
t_phys-t_(p,1)=n/(2Qp)=-u/(2Q).                      (5.4)
```

For fixed nonzero `u` and `p` tending to infinity,

```text
Q asymp p^3,           max(|e|,|f|) asymp p*|u|,
D=Q^(16/33) asymp p^(16/11),                         (5.5)
```

so the family lies deep inside the central energy mask and is much closer
than `H^(-1)` to the exact rational character.  Reflection again gives an
exact completion collision.

But the small-`c` criterion costs

```text
|c|*p=2p^2*|u|,                                      (5.6)
```

a full factor `p` larger than the actual errors.  For example, with `u=1`
and width `D`, (4.2) fits while (4.6) exceeds the width by a power.  This is
an infinite exact counterexample to the assertion

```text
every high-P reflected near-character obstruction has
|c|*d^2*p <= B.                                       (5.7)
```

It does not disprove the desired global bound.  At fixed `Q`, this particular
`d=1,h=0` branch satisfies

```text
Q=p*(p^2+2u-1),                                      (5.8)
```

so `p|Q` and `u` is then determined by `p`; it has only `Q^o(1)` points.
It should be treated as a second algebraic major arc, not as dispersed
minor mass.

## 6. Correct status of the classification

```text
integer-c formulas (1.2)--(1.4):                     PROVED;
factorization Q-c=p(p-d)(p+d):                       PROVED;
fixed-Q c-family count (2.6):                        PROVED;
c-family fits sqrt(A) in the energy core:             PROVED;
c-family fits Z by this argument:                     NOT PROVED;
exact (c,u,g-2d^2) normal form:                       PROVED;
small-c-only reflected classification:               FALSE;
balanced-offset hostile family:                      PROVED;
balanced d=1 branch has fixed-Q divisor count:        PROVED;
h=0 branch has sqrt(A)Q^epsilon count:                PROVED;
next invariant k=h^2-d^2u^2:                         PROVED;
k=0 one-band branch count:                            PROVED;
nonzero-k residual bound (4.19):                      PROVED;
large-u central remote sector:                        EMPTY;
nonzero-k central count O(B/Q^(1/3)):                PROVED;
central-content chart fits sqrt(A):                   PROVED;
arbitrary-content scaled normal form (4.35)--(4.38): PROVED;
scaled-offset bound below sqrt(A):                    PROVED;
noncentral thin box (4.42):                           PROVED;
raw Delta*ell^2 lower bound without recentering:      FALSE;
scaled balanced axis z=0 count:                      PROVED;
scaled one-band axes z=+-d*v count:                  PROVED (companion);
nonzero scaled residual forces p>>D^(77/160):        PROVED;
noncentral residual K count at sqrt(A):               OPEN;
finite complete algebraic-branch classification:     OPEN;
sharp four-cycle bound:                               NOT PROVED.
```

The exact fixtures, normal form, cubic-gap majorant, and replay tests are in

```text
src/qp_high_primitive_packet_pair_audit.py
src/test_qp_high_primitive_packet_pair_audit.py
```
