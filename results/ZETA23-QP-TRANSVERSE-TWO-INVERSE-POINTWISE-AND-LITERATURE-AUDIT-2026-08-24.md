# QP transverse two-inverse pointwise audit

**Date:** 2026-08-24  
**Binary verdict:** a new inverse-step sector closes through `w=D^(73/64)`
by applying Bourgain's local `beta(alpha)` bound to the exact unwrapped
reciprocal branches.  Euclidean rebranching extends to every primitive
direction in the defect lattice and closes genuine later-convergent sectors,
but a bounded-partial-quotient two-chart trajectory escapes every resulting
derivative sector and the current local-`beta` table.  The uniform transverse
bound therefore remains open.
No checked primary short-reciprocal, Kloosterman, lattice-point, exponent-pair,
or `beta` theorem yields the required `D^(7/8+o(1))` pointwise bound in the
remaining sector.

More precisely, let

```text
D=q^(16/33),             T=q^3/8,             delta asymp D/q,
N(x,y)=sum_(v in S)
  1_(||T/(xv)||<=delta) 1_(||T/(yv)||<=delta),              (0.1)
```

where `x,y,v` lie in the fixed project shell and distinct actual endpoints
are coprime.  Put `g=y-x`, and define the two least absolute inverse steps

```text
w_y=min(u_y,y-u_y),      u_y=x^(-1) (mod y),
w_x=min(u_x,x-u_x),      u_x=-y^(-1) (mod x),
w=min(w_x,w_y).                                           (0.2)
```

For every integer degree

```text
1<=K<=min(q/D,q/w^2),       wD/q<<1,

N(x,y)<<D^2/q+D/K+D*w*sqrt(K/q)+sqrt(q)/(w*sqrt(K)).       (0.3)
```

Taking

```text
K asymp (q/w^2)^(1/3)
```

gives

```text
N(x,y)<<D^2/q+D*(w^2/q)^(1/3)+(q/w^2)^(1/3).               (0.4)
```

Consequently

```text
w<=D^(27/32)      =>       N(x,y)<<D^(7/8).                (0.5)
```

A third-derivative estimate extends this.  For

```text
1<=K<=min(q/D,q^2/w^3),       J=1+wD/q,

N(x,y)
 <<D^2/q+D/K+D*w^(1/2)*q^(-1/3)*K^(1/6)
   +sqrt(DJ)*q^(1/3)*w^(-1/2)*K^(-1/6).                   (0.6)
```

Taking `K asymp q^(2/7)w^(-3/7)` and combining with `(0.5)` gives

```text
w<=D^(13/12)      =>       N(x,y)<<D^(7/8).                (0.7)
```

For `w>q/D`, an exponent pair `(kappa,lambda)` gives

```text
N(x,y)
 <<D^2/q+D/K
   +D*q^(lambda-1)*w^(1+kappa-lambda)*K^kappa*q^o(1).     (0.8)
```

The Bourgain pair `(13/84,55/84)` closes through `w=D^(109/96)`.  The best
fixed pair in the checked current ANTEDB hull is
`(4742/38463,35731/51284)`, which closes through
`w=D^(1194107/1050032)`.  A local `beta` bound is stronger than every fixed
pair here.  Bourgain's

```text
beta(alpha)<=1/12+(2/3)alpha,       5/12<alpha<=3/7,      (0.9)
```

together with the adjacent line `beta(alpha)<=13/84+alpha/2`, gives

```text
w<=D^(73/64)       =>       N(x,y)<<D^(7/8+o(1)).         (0.10)
```

Combined with the previously proved close-row estimate, the genuinely
unresolved pointwise sector may therefore be restricted to

```text
g>D^(3/8),       w_x>D^(73/64),       w_y>D^(73/64).      (0.11)
```

There is an additional arithmetic closure inside `(0.11)`.  In either signed
completion chart let `Q_0` be its host modulus (`x` or `y`), let `w` be its
least inverse step, and put

```text
rho=min(r,w-r),             r=Q_0 (mod w).                (0.12)
```

A second-derivative Euclidean rebranch proves the target whenever

```text
w>=D^(21/16),       rho<=D^(27/32),
w*rho>=D^(27/16).                                      (0.13)
```

A third-derivative version, which does not require a small-remainder
transition, proves it whenever

```text
w>=D^(25/16),       rho<=D^(13/12),
w*rho>=D^(7/3).                                        (0.14)
```

Either condition in either completion chart is sufficient.  These are real
new closed sectors, but they do not cover all pairs in `(0.11)`.

This is a real enlargement of the closed region.  It is not a proof of the
full transverse codegree estimate and hence not a proof of the sharp
four-cycle theorem.

---

## 1. Exact defect chart for the positive majorant

Fix shell constants `0<c_0<c_1`.  All variables in the project shell are
between `c_0 q` and `c_1 q`; constants below may depend on this fixed shell.
For every summand in `(0.1)`, choose nearest integers `a,b` and write

```text
T/(xv)=a+epsilon,       T/(yv)=b+eta,
|epsilon|,|eta|<=delta.                                (1.1)
```

The shell bounds imply `a,b asymp q`, even though their primality has been
dropped.  Since

```text
T/v=x(a+epsilon)=y(b+eta),                              (1.2)
```

the integer defect

```text
k=xa-yb=y*eta-x*epsilon                                (1.3)
```

satisfies

```text
|k|<<D.                                                 (1.4)
```

Conversely, after `k` and one completion `a` are fixed, the other completion
is fixed by

```text
b=(xa-k)/y.                                             (1.5)
```

The carrier is also unique.  Indeed, `(1.1)` gives the exact identity

```text
T/(xa)-v=v*epsilon/a,                                   (1.6)
```

so

```text
||T/(xa)||<<delta.                                      (1.7)
```

For large `q`, the interval in `(1.6)` has length less than one: explicitly,
`2 sup(v/a) delta<1` on the fixed shell.  Thus two different carriers cannot
have the same `(k,a)`.

Modulo `y`, equation `(1.3)` is

```text
a == u_y*k (mod y),       u_y=x^(-1) (mod y).           (1.8)
```

The completion range has fixed length `O(q)` while `y asymp q`, so each
defect has only `O(1)` possible integer lifts.  This proves the safe exact
reduction

```text
N(x,y)
 <<sum_(|k|<<D) sum_(a == u_y*k (mod y), a asymp q)
      1_(||T/(xa)||<<delta).                            (1.9)
```

There is a symmetric chart modulo `x` using `b`.

Notice also that `x=y-g` gives

```text
g*u_y == -1 (mod y),       g*u_x == -1 (mod x),         (1.10)
```

up to the harmless sign in the definition of `u_x`.  Thus `(0.2)` really
measures the modular-inverse transversality of the physical gap.

---

## 2. The inverse-step branch theorems

Choose the signed representative `sigma` of `u_y (mod y)` with
`|sigma|=w_y`.  As `k` runs through `O(D)` consecutive integers, cut the
lift graph `(1.8)` whenever the residue wraps modulo `y` or a completion
leaves one of the `O(1)` fixed lift intervals.  This produces affine
branches

```text
a(k)=a_0+sigma*k                                        (2.1)
```

with

```text
number of branches J <<1+w_y*D/q,
sum_(branches) branch_length <<D.                       (2.2)
```

On a branch of length `L`, put

```text
f(t)=T/[x(a_0+sigma*t)].                                (2.3)
```

Uniformly on the shell,

```text
|f''(t)| asymp w_y^2/q.                                 (2.4)
```

Majorize `1_(||f||<<delta)` by a Selberg polynomial of an integer degree

```text
1<=K<=q/D.                                               (2.5)
```

Its constant coefficient is `O(delta+1/K)`, and every nonzero coefficient
is also `O(delta+1/K)`.  Under `(2.5)` these are `O(1/K)`.  For `1<=h<=K`,
the standard second-derivative estimate gives

```text
|sum_(t in branch)e(hf(t))|
 <<L*w_y*sqrt(h/q)+sqrt(q)/(w_y*sqrt(h)).               (2.6)
```

Choose additionally

```text
K<=q/w_y^2.                                              (2.7)
```

Then `h w_y^2/q<=1` throughout the differentiated family.  Summing `(2.6)`
over `h` and using the Selberg coefficient bound gives

```text
#{t in branch: ||f(t)||<<delta}
 <<delta*L+L/K+L*w_y*sqrt(K/q)+sqrt(q)/(w_y*sqrt(K)).   (2.8)
```

If `w_yD/q<<1`, equation `(2.2)` gives only `O(1)` lift branches.  Their
total length is `O(D)`, so summing `(2.8)` proves

```text
N(x,y)
 <<D^2/q+D/K+D*w_y*sqrt(K/q)+sqrt(q)/(w_y*sqrt(K)).     (2.9)
```

Repeating the proof in the `b (mod x)` chart and choosing the smaller step
proves `(0.3)`.

Put

```text
R=(q/w^2)^(1/3),              K=max(1,floor(R)).          (2.10)
```

For `w<=D^(27/32)`, one has

```text
R>=D^(1/8),       K asymp R,       K<=q/D,
K<=q/w^2,         wD/q<=D^(-7/32).                       (2.11)
```

Thus `(2.9)` becomes `(0.4)`.  Its three powers at the endpoint
`w=D^(27/32)` are

```text
D^(-1/16),       D^(7/8),       D^(1/8).                 (2.12)
```

For smaller `w`, the middle term decreases; the last term is largest at
`w=1`, where it is only

```text
q^(1/3)=D^(11/16).                                      (2.13)
```

This proves `(0.5)`.

### 2.1 Third derivative and the wrap transition

The same branch phase has

```text
|f'''(t)| asymp w_y^3/q^2.                              (2.14)
```

The standard third-derivative estimate therefore gives

```text
|sum_(t in branch)e(hf(t))|
 <<L*(h*w_y^3/q^2)^(1/6)
   +sqrt(L)*(h*w_y^3/q^2)^(-1/6).                       (2.15)
```

As before, a degree-`K` Selberg majorant has all coefficients `O(1/K)`
when `K<=q/D`.  Choose also `K<=q^2/w_y^3`, so the differentiated family
stays in the low-derivative range.  Summing `(2.15)` over `h<=K` on all
branches uses

```text
sum L_j<<D,
sum sqrt(L_j)<=sqrt(JD),       J<<1+w_yD/q.             (2.16)
```

This proves the general third-derivative bound `(0.6)` (and its symmetric
`b (mod x)` version).

Now put

```text
R_3=q^(2/7)w^(-3/7),          K=max(1,floor(R_3)).       (2.17)
```

For

```text
D^(1/2)<=w<=D^(13/12),                                  (2.18)
```

one has `R_3>=D^(1/8)`, `K asymp R_3`, `K<=q/D`, and
`K w^3/q^2<=D^(-3/4)`.  The first three terms of `(0.6)` reduce to

```text
D^2/q+D*q^(-2/7)w^(3/7).                               (2.19)
```

The last term, including all wrap branches, satisfies

```text
sqrt(DJ)*q^(2/7)w^(-3/7)
 <<sqrt(D)*q^(2/7)w^(-3/7)
   +D*q^(-3/14)w^(1/14).                               (2.20)
```

On the interval `(2.18)`, the main term in `(2.19)` is largest at the
right endpoint and equals `D^(7/8)`.  The first term in `(2.20)` is largest
at the left endpoint and also equals `D^(7/8)`.  The wrap term is largest
at the right endpoint and is only

```text
D^(61/96).                                              (2.21)
```

Thus the third-derivative argument closes `(2.18)`.  It overlaps the
second-derivative range `(0.5)`, proving `(0.7)` with no gap.  In
particular, the slight wrap transition at `w=q/D=D^(17/16)` is harmless;
at `w=D^(13/12)` the number of branches is only `O(D^(1/48))`, and its
square-root cost is already included in `(2.20)`.

This argument uses the raw positive majorant: it does not use primality of
the two completions or cancellation from the actual mask.  The only
arithmetic inputs are coprimality of the endpoints and the fixed shell.

### 2.2 Exponent pairs and the stronger local-beta wrap theorem

Assume now that `w=w_y>q/D`; the symmetric `b (mod x)` chart is identical.
An unwrapped branch has natural length

```text
M asymp q/w,                                               (2.22)
```

although the first and last branches may be truncated.  After `O(1)` cuts
depending only on the fixed shell, translate the integer parameter so that

```text
a=w(n+theta),       0<=theta<1,       n asymp M.           (2.23)
```

The sign of the least residue only reverses the interval.  On taking a
complex conjugate when necessary, the frequency-`h` phase becomes

```text
h*T/[xw(n+theta)]
  =T_h F_M(n/M),
T_h=h*T/(xwM) asymp hq,
F_M(u)=-1/(u+theta/M).                                    (2.24)
```

For every fixed derivative order, `F_M` converges uniformly to the model
phase `-1/u`, whose first derivative is `u^(-2)`.  It is therefore a model
phase of parameter `sigma=2` in the sense of the non-asymptotic definition
of `beta` and exponent pairs.  Also

```text
T_h/M asymp hw>=1.                                        (2.25)
```

Thus an exponent pair `(kappa,lambda)` gives, uniformly for an arbitrary
truncated branch interval,

```text
|sum e(hf)|
 <<(hw)^kappa*(q/w)^lambda*q^o(1).                        (2.26)
```

This normalization is important: the exponent-pair parameter is `T_h asymp
hq`, not `hw`; the latter is the ratio `T_h/M`.

There are

```text
J<<1+wD/q<<wD/q                                           (2.27)
```

branches in this regime.  A degree-`K` Selberg majorant, with `K<=q/D`, has
every nonconstant coefficient `O(1/K)`.  Summing `(2.26)` over all branches
and `h<=K` proves `(0.8)`.  Balancing its last two terms gives

```text
K=q^((1-lambda)/(1+kappa))
  *w^(-(1+kappa-lambda)/(1+kappa)).                       (2.28)
```

If `w=D^b`, the requirement `K>=D^(1/8)` is exactly

```text
b <= [ (33/16)(1-lambda)-(1+kappa)/8 ]
     /(1+kappa-lambda).                                  (2.29)
```

For Bourgain's pair `(13/84,55/84)`, `(2.28)` is
`K=q^(29/97)w^(-42/97)` and `(2.29)` is `b<=109/96`
(equivalently `763/672`).  Checking the vertices in the current ANTEDB
convex-hull table improves the fixed-pair cutoff slightly: the maximum of
`(2.29)` is

```text
(kappa,lambda)=(4742/38463,35731/51284),
b=1194107/1050032=1.137210... .                           (2.30)
```

The four new Tao--Trudgian--Yang pairs and the later ANTEDB vertices are
all weaker for this particular linear-fractional objective.  Since `(2.29)`
is linear-fractional with positive denominator, its maximum over a convex
polygon is attained at a vertex.  The positive Heath--Brown tail is also
harmless: its numerator in `(2.29)` is already negative from its second
member onward.  The exact finite scan is reproduced in the ledger code.

The local `beta` table does a little better because `beta` is not known to
be convex.  Fix

```text
K=floor(D^(1/8)).                                         (2.31)
```

For a dyadic frequency block `h asymp H`, the factor `H/K` from the number
of Selberg coefficients must be retained.  Definition 9 and the
non-asymptotic formulation of `beta` give the total contribution

```text
J*(H/K)*(Hq)^(beta(alpha_H)+o(1)),
alpha_H=log(q/w)/log(Hq).                                (2.32)
```

Write

```text
w=q^(rho+o(1)),       H=q^(s+o(1)),
d=16/33,              tau=2/33,       0<=s<=tau.         (2.33)
```

For `q/D<w<=D^(73/64)`, one has

```text
59/140<=alpha_H=(1-rho)/(1+s)<=16/33.                    (2.34)
```

Only the two adjacent Bourgain lines are needed on this interval:

```text
beta(alpha)<=1/12+(2/3)alpha,       5/12<=alpha<=3/7,
beta(alpha)<=13/84+(1/2)alpha,      3/7<=alpha<=1/2.     (2.35)
```

If one of these lines is written `a+b alpha`, the `q`-exponent in `(2.32)`
is

```text
E(rho,s)=rho+d-1+s-tau+(1+s)beta((1-rho)/(1+s)).          (2.36)
```

On that line, `E` increases with `s` with slope `1+a>0`, and with `rho`
with slope `1-b>0`.  The two formulae in `(2.35)` agree at `alpha=3/7`
(both equal `31/84`), so crossing between them causes no jump.  Hence the
worst dyadic block and inverse step are `H=K` and `w=D^(73/64)`.

At that endpoint the complete exact ledger is

```text
M=q/w=D^(59/64),           T_K=Kq=D^(140/64),
alpha_K=59/140,            beta(alpha_K)<=51/140,
J<<wD/q=D^(5/64).                                      (2.37)
```

Consequently the top block contributes

```text
J*T_K^(51/140)
 <<D^(5/64)*D^(51/64)=D^(7/8),                          (2.38)
```

while the Selberg resolution term is `D/K=D^(7/8)` and the constant term
is `D^2/q=D^(-1/16)`.  All lower dyadic blocks are smaller by `(2.36)`, and
the `O(log q)` blocks are absorbed in `q^o(1)`.  This proves `(0.10)`.

For an exact check of the line crossing, write `H=D^eta` at the endpoint.
The transition `alpha_H=3/7` occurs at `eta=17/192`.  The full exponent in
`(2.32)`, including `J` and `H/K`, is

```text
657/896+(97/84)eta,       0<=eta<=17/192,
71/96 +(13/12)eta,        17/192<=eta<=1/8.             (2.39)
```

Both formulae equal `1925/2304` at the transition, and the second rises to
`7/8` at `eta=1/8`.  Thus no small-frequency block has been hidden by the
top-block shorthand in `(2.38)`.

The endpoint `73/64` is also optimal for this Selberg-plus-current-beta
route.  At `H=K=D^(1/8)`, put
`alpha=log(q/w)/log(Kq)`.  The target is equivalent to

```text
alpha-beta(alpha)>=2/35.                                 (2.40)
```

On the middle line of `(2.35)`, equality holds exactly at
`alpha=59/140`.  An exact scan of the remaining current ANTEDB beta-table
pieces gives no recovery for smaller `alpha`; on every intervening affine
piece, `alpha-beta(alpha)` decreases as `alpha` decreases.  Taking
`K>D^(1/8)` only increases the oscillatory exponent because the intercepts
of the active beta lines are positive.

The phase and interval hypotheses in this application are genuine, not
formal substitutions.  Arbitrary subintervals `I subset [M,2M]` are allowed
in the definitions; the fixed shell needs only `O(1)` such intervals; and
the perturbation `theta/M` tends to zero in every fixed derivative.  The
non-asymptotic uniformity lemma absorbs the perturbation and the variation
of `alpha_H` inside each dyadic exponent range.

### 2.3 Euclidean rebranch: two additional closed sectors

There is another exact coordinate change in the wrapped range.  Work in one
signed `y`-chart and reflect `k,n` if necessary so that the lift is

```text
a=w*k-y*n.                                                (2.41)
```

Use nearest Euclidean division

```text
y=L*w+r,             rho=|r|=min(y mod w,w-(y mod w)).    (2.42)
```

Since `gcd(y,w)=1`, `rho` is nonzero.  The unimodular change

```text
t=k-L*n
```

gives the exact identities

```text
k=t+L*n,             a=w*t-r*n.                           (2.43)
```

The old organization fixed `n` and moved `k` with step `w`.  The new one
fixes `t` and moves `n` with the potentially much smaller step `rho`.

The shell rectangle has `k`-width `O(D)` and `a`-width `O(q)`.  From
`n=(w*k-a)/y` and `(2.43)`, the number of nonempty `t`-sequences is

```text
B << 1+q/w+rho*D/q << q/w+rho*D/q,
sum_t length(I_t)<<D.                                     (2.44)
```

The harmless `O(1)` boundary pieces are absorbed after the same fixed shell
partition used above; the second inequality uses `w<=y/2` and `y asymp q`.
On one sequence the reciprocal phase is

```text
f_t(n)=T/[x(w*t-r*n)],
|f_t''(n)|asymp rho^2/q,
|f_t'''(n)|asymp rho^3/q^2.                              (2.45)
```

First suppose `rho*D/q<<1`.  Then `(2.44)` gives `B<<q/w`.  Applying the
second-derivative estimate on every sequence, summing their lengths, and
using a degree-`K` Selberg majorant proves

```text
N(x,y)
 <<D^2/q+D/K+D*rho*sqrt(K/q)
   +q^(3/2)/(w*rho*sqrt(K)),                             (2.46)

1<=K<=min(q/D,q/rho^2).                                 (2.47)
```

To make the first oscillatory term in `(2.46)` no larger than the target it
is useful to record the stronger target ceiling

```text
K<=q/[rho^2*D^(1/4)].                                   (2.48)
```

Choose

```text
K asymp max(D^(1/8),q^3/[w^2*rho^2*D^(7/4)]).           (2.49)
```

The three conditions in `(0.13)` have distinct exact roles.  The remainder
condition makes the first choice in `(2.49)` satisfy `(2.48)`; the lower
bound `w>=q/D^(3/4)=D^(21/16)` makes the second choice satisfy `(2.48)`; and
`w*rho>=q/D^(3/8)=D^(27/16)` makes it at most `q/D`.  The ceiling in `(2.48)`
is stronger than `q/rho^2`.  Also

```text
rho*D/q<=D^(-7/32),                                     (2.50)
```

so the small-remainder hypothesis is automatic.  Equations `(2.46)--(2.50)`
prove `(0.13)`.

The third derivative handles a larger remainder without `(2.50)`.  From
`(2.44)`, Cauchy--Schwarz gives `sum_t sqrt(length(I_t))<=sqrt(BD)`.  Thus

```text
N(x,y)
 <<D^2/q+D/K+D*rho^(1/2)*q^(-1/3)*K^(1/6)
   +sqrt(D*(q/w+rho*D/q))*q^(1/3)*rho^(-1/2)*K^(-1/6),  (2.51)

1<=K<=min(q/D,q^2/rho^3).                              (2.52)
```

Splitting the square root in the last term produces

```text
D^(1/2)*q^(5/6)*(w*rho)^(-1/2)*K^(-1/6)
   +D*q^(-1/6)*K^(-1/6).                               (2.53)
```

The second summand is at most `D^(61/96)` because `K>=D^(1/8)`.  For the
first choose

```text
K asymp max(D^(1/8),q^5/[w^3*rho^3*D^(9/4)]).           (2.54)
```

The target ceiling supplied by the curvature term is

```text
K<=q^2/[rho^3*D^(3/4)].                                (2.55)
```

Now `rho<=D^(13/12)` puts `D^(1/8)` below `(2.55)`,
`w>=q/D^(1/2)=D^(25/16)` puts the second choice in `(2.54)` below `(2.55)`,
and

```text
w*rho>=q^(4/3)/D^(5/12)=D^(7/3)                        (2.56)
```

puts it below `q/D`.  Again `(2.55)` is stronger than the remaining
low-derivative ceiling.  This proves `(0.14)`.  The symmetric `x`-chart is
identical with `y,w,rho` replaced by its host modulus, inverse step, and
nearest Euclidean remainder.

### 2.4 Exact cross-wrap Poisson transform and its standard-method barrier

It is natural to ask whether the wrap branches can instead be cancelled
against one another.  The exact transform shows both the opportunity and
the obstruction.  Smooth one shell rectangle with compactly supported
`W,V`, put `C_h=hT/x`, and orient signs as

```text
S_h=sum_n sum_(a == n*y mod w)
 W((a-n*y)/(wD))*V(a/q)*e(C_h/a).                       (2.57)
```

Poisson summation in the residue class gives the exact identity

```text
S_h=(1/w) sum_m integral V(t/q)e(C_h/t-m*t/w) D_m(t) dt,

D_m(t)=sum_n W((t-n*y)/(wD))*e(m*n*y/w).                (2.58)
```

With `J_0=wD/y asymp J=wD/q`, a second Poisson summation in `n` gives

```text
D_m(t)=J_0 sum_l
 hat W(J_0*(m*y/w-l))*e((m*y/w-l)*t/y),                 (2.59)
```

and hence the exact completed formula

```text
S_h=(D/y) sum_(m,l) hat W(D*(m*y-l*w)/y)
       *integral V(t/q)e(C_h/t-l*t/y) dt.               (2.60)
```

Formula `(2.59)` is the smooth Dirichlet kernel across wrap labels.  Uniformly
in `t`,

```text
|D_m(t)| <<_A J*(1+J*||m*y/w||)^(-A),
sum_(m mod w)|D_m(t)| << w,
sum_(m mod w)|D_m(t)|^2 << wJ.                          (2.61)
```

For a sharp interval, the first sum acquires only `log(2J)`.  Coprimality of
`y,w` is essential here: multiplication by `y` permutes the residues modulo
`w`.

In `(2.58)`, stationarity requires `m<0` and

```text
|m|asymp h*w,          t_m=sqrt(C_h*w/|m|)asymp q.      (2.62)
```

There are `asymp h` full residue periods.  Standard stationary phase gives

```text
I_m <<sqrt(q/h),
phase(I_m)=2*sqrt(C_h*|m|/w)+O(1).                      (2.63)
```

The derivative bounds for `D_m(t)` have the same decay as `(2.61)`, so it is
a legitimate stationary-phase amplitude.  Taking the `L^1` norm in `(2.61)`
therefore gives only

```text
|S_h|<<sqrt(hq)*q^o(1).                                (2.64)
```

At the top Selberg frequency `h=K=D^(1/8)`, this is

```text
sqrt(Kq)=D^(35/32),                                    (2.65)
```

which misses `D^(7/8)` by `D^(7/32)`.

The same barrier is visible arithmetically in `(2.60)`.  Rapid decay of
`hat W` restricts the dual lattice to the determinant strip

```text
|m*y-l*w| << y/D.                                      (2.66)
```

The stationary `l`-range has length `asymp h*y`; because multiplication by
`w` permutes residues modulo `y`, `(2.66)` contains `asymp h*y/D` modes up
to fixed endpoint factors.  The prefactor `D/y`, this mode count, and the
stationary amplitude `sqrt(q/h)` multiply to `sqrt(hq)` again.  The dual
stationary phase

```text
Psi(l)=2*sqrt(C_h*|l|/y),       |Psi''(l)|asymp 1/(hq)  (2.67)
```

on an interval of length `hq` also gives exactly `sqrt(hq)` under the
ordinary second-derivative theorem.  Its first derivative crosses integers,
so a uniform first-derivative estimate supplies no missing power.

Nor does a plain large sieve.  Grouping the `asymp h` aliases of each
residue modulo `w` and applying the additive large sieve across the `J`
wraps gives at best

```text
|sum_n S_(h,n)| <<sqrt(J*h*q).                          (2.68)
```

At `w=D^(73/64)`, where `J=D^(5/64)`, the right side is
`D^(145/128)`, even worse than `(2.65)` and above the target by `D^(33/128)`.
Even granting unproved square-root cancellation among the `h` exact aliases
would give only `sqrt(Jq)=sqrt(wD)=D^(137/128)`, still above the target by
`D^(25/128)`.

The precise coherent-frequency fixture is

```text
||m*y/w|| <<1/J.                                       (2.69)
```

It contains `asymp w/J=q/D` residues in every period and
`asymp hq/D` stationary modes altogether; on it `|D_m|asymp J`.  Thus the
wrap labels are genuinely coherent on a band large enough to saturate the
`L^1` calculation in `(2.64)`.  This is an exact **integer-frequency
fixture**, not a counterexample to the desired count: the stationary phases
inside `(2.69)` may still cancel.  It proves only that Dirichlet-kernel
size, ordinary first/second derivative bounds, or an unstructured additive
large sieve cannot by themselves improve the Bourgain branch threshold.
Any global gain from `(2.58)` must use new cancellation along the sparse
determinant strip `(2.66)` (or the Euclidean arithmetic exploited in
`(2.41)--(2.56)`).

### 2.5 Every primitive Euclidean direction, and the iteration barrier

The first remainder is only one primitive direction in the exact defect
lattice

```text
Lambda(Q,w)={(k,a): a=w*k-Q*n for some n in Z}.          (2.70)
```

For arbitrary integers `p,m` with `gcd(p,m)=1`, put

```text
r=w*p-Q*m !=0.                                          (2.71)
```

Then `(p,r)` is saturated in `Lambda`, the fibres are labelled exactly by
`ell=(-r*k+p*a)/Q`, and

```text
B<<min(D,1+|p|+|r|D/q),       sum_ell |I_ell|<<D.       (2.72)
```

Write `|p|=D^(u+o(1))`, `|r|=D^(v+o(1))`, and use the fibre-budget exponent

```text
b=min(1,max(0,u,v+1-33/16)).                            (2.73)
```

Repeating the second- and third-derivative proofs gives the exact feasibility
polytopes for these recorded derivative bounds

```text
C_2: v<=27/32, b<=3/4, b-v<=3/8;
C_3: v<=13/12, b<=1/2, v-b>=13/48.                     (2.74)
```

On the same fibres a dyadic block `h asymp H` contributes

```text
B*(H/K)*(Hq)^(
  beta(log(q/|r|)/log(Hq))+o(1)).                       (2.75)
```

Thus all current local-`beta` lines give a finite additional polyhedral
complex which can be tested at every continued-fraction vector.  This
strictly enlarges the first-remainder result: an explicit family has a later
convergent with `(u,v,b)=(3/5,4/5,3/5)` in `C_2`, while its original and first
remainders are both `asymp q`.

There is also a sharp limitation.  For bounded-partial-quotient rotations,
best approximation forces every useful primitive vector above the lower
envelope `u+v=33/16`; equality is the most favourable case, where the shell
line count forces

```text
u+v=33/16,          b>=min(1,max(u,1-u)).               (2.76)
```

This trajectory misses both polytopes in `(2.74)`.  An exact scan of all
current ANTEDB `beta` pieces is best at `u=1/2`, where the top-block bound is

```text
D^(6535/6624)=D^(7/8+739/6624).                         (2.77)
```

Consecutive Fibonacci endpoints put both inverse charts on `(2.76)`.  They
are a coprime lattice fixture, not an actual-prime counterexample, but they
prove that continued-fraction iteration plus the same fibrewise derivative
or local-`beta` input cannot supply a uniform closure.

---

## 3. What elementary determinant and scalar Fourier methods actually give

The exact scale ledger is

```text
D=q^(16/33),         target D^(7/8)=q^(14/33),
delta=q^(-17/33),    H=delta^(-1)=q^(17/33).           (3.1)
```

The defect chart has `O(D)` labels.  A divisor bound for the equivalent
short-product strip therefore gives only

```text
N(x,y)<<D*q^o(1),                                      (3.2)
```

missing the target by `D^(1/8)`.

Fourier expansion produces the injective frequencies

```text
ell=r*y+s*x,          |r|,|s|<=H,                      (3.3)
```

and reciprocal sums

```text
S_ell=sum_(v in S)e((T/(xy))*ell/v).                   (3.4)
```

The map in `(3.3)` is injective because `2H<min(x,y)`.  Dirichlet
approximation nevertheless supplies nonzero combinations with
`|ell|<<q/H<<D`; removing the visible `(1,-1)` ray by assuming a large gap
does not remove all such rational-approximation rays.

For one scalar sum the second-derivative estimate is

```text
S_ell <<sqrt(|ell|)+q/sqrt(|ell|).                     (3.5)
```

Triangle inequality over `(3.3)` does not improve `(3.2)`.  At the other
extreme, an ordinary additive large sieve for the `H^2` sparse frequencies,
whose ambient diameter is `qH=q^2/D`, gives the bilinear scale

```text
sqrt(q)*sqrt(qH)*(D/q)=sqrt(qD)=D^(49/32),             (3.6)
```

again much worse than the trivial defect count.  Even a hypothetical plain
square-root discrepancy `q^(1/2)` is

```text
q^(1/2)=D^(33/32)=D^(7/8)*D^(5/32),                   (3.7)
```

so an unstructured `L^2` large sieve is intrinsically short by `D^(5/32)`.
The target is a sub-square-root, rank-one/mask-sensitive statement.

The carrier curve does not acquire ambient torsion:

```text
gamma(v)=(v,T/(xv),T/(yv)),
gamma_3=(x/y)*gamma_2.                                 (3.8)
```

It lies in a fixed plane, and its last two coordinates lie on one line.
This is why a generic space-curve determinant theorem is not an available
shortcut.

---

## 4. Primary-literature applicability audit

### 4.1 Huang's space-curve theorem

[Huang, *Integral points close to a space
curve*](https://arxiv.org/abs/1809.07796), Theorem 1, proves

```text
A(q,delta)<<delta^2*q+q^(3/5)(log q)^(4/5)              (4.1)
```

for compact `C^3` curves with nowhere-vanishing torsion.  Equation `(3.8)`
has identically zero torsion, so the hypothesis fails.  Moreover the
`q^(3/5)` error would exceed `q^(14/33)` even if it were formally inserted.
The paper explicitly explains that its conclusion can fail for zero-torsion
embedded plane curves.

### 4.2 Bettin--Chandee and Wright

[Bettin--Chandee, *Trilinear forms with Kloosterman
fractions*](https://arxiv.org/abs/1502.00769), Theorem 1, can formally see
`(3.4)` by fixing its `m` variable to `1`.  After dyadic decomposition the
top frequency block has

```text
M=1,       N=q,       A=qH=q^2/D,       theta=T/(xy)asymp q.
```

The theorem then contains the rapid-phase factor

```text
(1+|theta|A/(MN))^(1/2) asymp A^(1/2),                 (4.2)
```

and gives no improvement over the trivial sum.  Already in the block
`A asymp D`, using the sharper lattice count of only `O(H)` represented
frequencies, its displayed bound is `q^(122/165+o(1))`, still far above

```text
q^(14/33)=q^(70/165).                                  (4.3)
```

[Wright, *Trilinear Kloosterman fractions I: partially fixed moduli and
unbalanced convolutions*](https://arxiv.org/abs/2604.25177), Theorem 2.1,
improves a denominator with a fixed factor in a genuine trilinear
Kloosterman-fraction form.  It does not legally encode the present phase in
a useful `M=1,R=1` interface: its phase parameter is integral, while an exact
fixed-factor encoding requires `theta=q^3` and `R=8xy` (or an equivalent
huge numerator support), outside the theorem's useful `M=1` regime.  Its
displayed rapid-phase factor is a fourth root rather than the square root in
`(4.2)`, but the remaining hypotheses and bracket terms still give no
two-frequency pointwise estimate here.

### 4.3 Very short linear Kloosterman sums

[Bourgain--Garaev, *Sumsets of reciprocals in prime fields and multilinear
Kloosterman sums*](https://arxiv.org/abs/1211.4184), Theorem 16, gives for a
standard linear incomplete Kloosterman sum a logarithmic relative saving

```text
N*(log log p)^3*log p/(log N)^(3/2).                   (4.4)
```

At `N=p^(16/33)`, this is only
`N*(log log p)^3/(log p)^(1/2)`, whereas the required saving from the
`D`-candidate defect chart is the fixed power

```text
D^(-1/8)=q^(-2/33).                                    (4.5)
```

More importantly, `(1.9)` is a reciprocal evaluated along a modular
rotation of the completion lift, not the standard phase
`e_p(A*k^(-1)+B*k)`.  Thus `(4.4)` is only a favorable benchmark, not a
theorem applicable to `(0.1)`.

### 4.4 Complete bilinear Kloosterman forms

[Blomer--Pascadi, *Bilinear forms with Kloosterman sums via quadratic
characters*](https://arxiv.org/abs/2607.24311), Theorem 1.1, treats two free
interval variables against a **complete**, fixed-modulus Kloosterman sum.
The exact pointwise object `(1.9)` is a nested graph with one completion and
one carrier jointly determined by the defect; it has neither two free
variables nor the internal complete unit sum.  The existing detailed audit
is `ZETA23-QP-BLOMER-PASCADI-ROUNDING-HSM-APPLICABILITY-AUDIT-2026-08-22.md`.

For orientation only, the weakest relative saving of that theorem in the
hypothetical modulus-`q`, length-`D` box is `q^(-19/1056)`, while the present
pointwise reduction needs `q^(-2/33)=q^(-64/1056)`.  There is no legal bridge
on which to spend even that smaller saving.

### 4.5 Exponent pairs and the local `beta` table

[Bourgain, *Decoupling, exponential sums and the Riemann zeta
function*](https://arxiv.org/abs/1408.5794), Theorem 6, proves the exponent
pair `(13/84,55/84)`.  The stronger input used in `(2.35)` is Bourgain's
local exponential-sum bound from equation (3.18), recorded as the two
relevant `beta` pieces in Table 1 of [Tao--Trudgian--Yang, *New exponent
pairs, zero density estimates, and zero additive energy estimates: a
systematic approach*](https://arxiv.org/abs/2501.16779).  Definitions 5, 9,
and 11 and Lemma 10 there give exactly the model-phase, `beta`, exponent-pair,
and uniform non-asymptotic interfaces used in `(2.24)--(2.35)`.

The same Tao--Trudgian--Yang paper proves four new exponent pairs in Theorem
20.  The finite scan in `(2.30)` was checked against those pairs and the
vertices in the current [ANTEDB exponent-pair
table](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html).
For this objective the best fixed pair is still the earlier
`(4742/38463,35731/51284)` vertex from [Trudgian--Yang, *Toward optimal
exponent pairs*](https://arxiv.org/abs/2306.05599), but the nonconvex local
`beta` piece is stronger and yields `(0.10)`.

### 4.6 The August 2026 centered ratio fourth moment

[Yao Zhi, *Five-Term and Higher Congruences Involving Arbitrary Sets and
Short Intervals Modulo a Prime*](https://arxiv.org/abs/2608.15458), Theorem
1.1, proves the uniform centered estimate

```text
sum_(a!=0)|sum_(m in M,k in I)e_p(a*m*k^(-s))|^4
 <<p*|I|^2*|M|^2*(|I|+min(|M|,sqrt(p)))^2*p^o(1).     (4.6)
```

For `p asymp q` and `|I|=|M|=D=p^(16/33)`, this is `p*D^6*p^o(1)`.
Its five-term application starts at `p^(14/29+epsilon)`, tantalizingly close
to the project scale since

```text
16/33-14/29=2/957.                                    (4.7)
```

It does not prove the present four-cycle estimate.  Eliminating one wedge
has the schematic congruence `k*v==T+x*e (mod y)`, but the physical wedges
form a selected graph `m=m(k)` cut by an arbitrary carrier mask.  Theorem
1.1 controls the full Cartesian ratio set, not graph coefficients.  The
packet-free energy relation also has four arbitrary carrier denominators,
whereas the paper's sub-square-root conclusion uses a fifth free summand.
Finally, its modulus is prime, while an actual endpoint is uniformly only a
prime power.  A positivity completion to the Cartesian object lands at the
`D^6` centered-correlation scale, far above the required `D^(5/2)` energy.
Thus the centering mechanism is relevant inspiration for a mask-sensitive
extension, but `(4.6)` is not an applicable theorem here.

There is an exact graph-weighted audit of that possibility.  For a graph
`m=m(k)`, injective phases `v_k=m(k)k^(-1)`, and coefficients `c_k`, additive
orthogonality and Young's inequality give

```text
(1/p) sum_(a!=0) |sum_k c_k e_p(a*v_k)|^4
 <=||c||_1^2 ||c||_2^2
 <=|K| ||c||_2^4.                                    (4.8)
```

For `|K|=D` and flat coefficients this is `D^3`, not `D^(5/2)`, and the
power is sharp.  Indeed `m(k)=k^2` on `1<=k<=D` gives `v_k=k`; the graph is
a matching with no three collinear points, while its centered fourth moment
is

```text
(2D^3+D)/3-D^4/p.                                    (4.9)
```

This is a theorem-method fixture, not a physical product-band
counterexample.  It proves that reciprocal rounding or post-peeling packet
geometry must enter before graph centering; support on a matching alone
cannot supply the missing square root.

---

## 5. Exact remaining theorem

After the close-gap theorem, `(0.10)`, and the all-primitive refinement
`(2.70)--(2.77)`, it is enough to prove the following restricted statement.

> **Doubly transverse two-inverse target.**  Uniformly for coprime actual
> shell endpoints `x<y` satisfying
> `y-x>D^(3/8)` and both least absolute inverse steps in `(0.2)` exceeding
> `D^(73/64)`, and such that every primitive direction in both signed
> completion charts lies outside `C_2`, `C_3`, and the full current
> local-`beta` complex, prove
> `N(x,y)<<D^(7/8)q^o(1)`.

No checked scalar theorem proves this.  The exact ledgers show why:

* positive divisor/determinant counting stops at `D`;
* completion/ordinary square-root discrepancy stops above the target by
  `D^(5/32)`;
* the available space-curve theorem has the wrong torsion and exponent;
* short linear Kloosterman results do not give the required fixed power or
  the correct composed phase;
* complete bilinear Kloosterman theorems require a kernel absent from the
  pointwise graph.

What remains would be genuinely new: either a mask-sensitive vector-valued
two-inverse large-sieve theorem, or a determinant/continued-fraction theorem
which couples the two large inverse steps to the reciprocal carrier rather
than estimating them separately.

### 5.1 The two inverse rotations share one Bezout coordinate

There is an exact warning against interpreting the last target as a product
of two independent discrepancies.  Choose signed integers `s,m` with

```text
g*s+1=m*x,                 m*x-g*s=1.                  (5.1)
```

Then all solutions of `xa-yb=k` have the common parametrization

```text
a=(s+m)k+y*n,              b=s*k+x*n.                  (5.2)
```

The residue `s (mod x)` is `-y^(-1)`, while `s+m (mod y)` is `x^(-1)`.
Thus `w_x` and `w_y` are the two least lattice distances arising from one
Bezout pair.  They are not independent modular rotations.

The two reciprocal phases are also identical to physical precision:

```text
T/(xa)-T/(yb)=-T*k/(x*y*a*b)<<D/q.                    (5.3)
```

For `|k|<<D`, one window condition therefore implies the other after a
constant enlargement of the tolerance.  The joint positive majorant is,
on the exact defect chart, uniformly equivalent to a scalar reciprocal
window.  In Fourier language the diagonal modes are coherent all the way
to degree `q/D`.  A coefficient-blind theorem cannot gain a square root by
separating the two windows.

The dual completion-gap chart does not repair this.  Equation `(5.1)` makes
`m` an inverse of `x (mod g)`, but its natural branch length is again
`q/w`, and differentiating its reciprocal carrier phase gives the same
scales `w^r/q^(r-1)`.  Its Fourier cutoff is at most `g/D`, no larger than
the cutoff already used above.

Consequently the genuinely new input must be frequency-averaged across
wrap branches, retain the selected mask, or classify and peel coherent
affine/tangent packets.  A product of two scalar inverse estimates is not
the missing theorem.

---

## 6. Reproducibility and status

Exact modular lifts and exponent arithmetic are in
`src/qp_transverse_two_inverse_ledger.py` and
`src/qp_iterated_euclidean_rebranch_ledger.py`; tests are in the
corresponding `src/test_*.py` files.

```text
exact defect chart and carrier uniqueness:             PROVED;
free-degree inverse-step branch estimate (0.3):        PROVED;
third-derivative wrap estimate (0.6):                  PROVED;
exponent-pair wrap estimate (0.8):                     PROVED;
local-beta wrap estimate (0.10):                       PROVED;
sector min(w_x,w_y)<=D^(73/64):                        CLOSED;
Euclidean rebranch identities (2.41)-(2.45):           PROVED;
second-derivative remainder sector (0.13):             CLOSED;
third-derivative remainder sector (0.14):              CLOSED;
all-primitive rebranch criterion and line count:        PROVED;
exact all-primitive polytopes C_2,C_3:                  PROVED;
arbitrary-vector local-beta formula (2.75):             PROVED;
later-convergent strict enlargement:                    PROVED;
bounded-partial-quotient two-chart method obstruction:  PROVED;
graph-weighted centering bound D^3 and sharp fixture:    PROVED;
cross-wrap Poisson formulae (2.58)-(2.60):             PROVED;
coherent band as a standard-method obstruction:        PROVED;
coherent band as a counterexample to the count:        NOT CLAIMED;
shared Bezout chart and phase coherence (5.1)-(5.3):   PROVED;
physical close-gap sector g<=D^(3/8):                  CLOSED (prior);
doubly transverse pointwise majorant:                  OPEN;
existing primary theorem giving D^(7/8) uniformly:     NOT FOUND;
faithful actual-prime counterexample to D^(7/8):        NOT FOUND;
sharp four-cycle theorem:                              NOT PROVED.
```
