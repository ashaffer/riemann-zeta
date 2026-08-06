# Moving Type-II norm checkpoint

Status: analytic fail-fast checkpoint, 2026-08-06.  This note does **not**
prove RH.

The exact joint cutoff table, all-mode reconstruction, and divisor-involution
continuation is recorded in
[`JOINT-TYPE-II-CUTOFF-IDENTITY.md`](JOINT-TYPE-II-CUTOFF-IDENTITY.md).

## 1. Verdict

The centered moving-cutoff Type-II proxy from R68 survives, but its natural
ambient norm route does not.

1. In logarithmic coordinates the near-square kernel converges to the
   triangular Volterra--Hankel operator.  Its singular values are
   `2L/((2j-1)pi)`.
2. Removing any fixed number of pole, zero-mode, or other moment directions
   leaves operator norm comparable to `L`.  Fixed-width smoothing does not
   change this conclusion.
3. Absolute values lose a factor of order `sqrt(x)log x` already on one
   central plateau rectangle.  As a heuristic comparison, independent
   random signs for the Möbius factor alone would still leave order
   `x^(1/4)log x` on that rectangle.
4. Estimates that use only the displayed Schur, Hilbert--Schmidt, fixed-rank
   SVD, or coefficient norms, as well as separate-block estimates, therefore
   cannot reach even a polylogarithmic bound.  This does not classify every
   arithmetic large-sieve or dispersion inequality.
5. Equal moving cutoffs give an exact reflection-even central-divisor
   collar, but reflection reinforces a prime--prime plateau block of size
   `asymp x^theta/log x` rather than cancelling it.
6. The structure retained by the present tests is the joint identity
   `beta_V=Lambda_(>V)*1`: all cofactors and singular modes must be retained
   together with the two R68 centerings.

A useful heuristic checkpoint is a uniform variance-scale estimate for the
**full centered aggregate**, with `0<theta<=theta_k` in the R68 range, for
example

```text
abs(B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)) <<_(ell,k,theta) sqrt(log x).  (1.1)
```

Any fixed power of `log x` would already be enough: by the exact R68 width
law it implies RH, after which the fixed-test explicit formula upgrades the
bound to `O(1)`.  Thus (1.1) is a methodological checkpoint, not an easier
logical consequence of known estimates.

## 2. Exact kernel geometry

Fix the smoothing order `k`, take

```text
U=V=x^theta,        theta<1/2,
N=x/U,
L=log(N/U)=(1-2theta)log x,                                (2.1)
```

and restrict to `U<d,r<=N`.  The balanced kernel is

```text
K_x(d,r)=(dr)^(-1/2)Phi_(h,k)(log(x/(dr))).                (2.2)
```

Schur's test with `p_n=n^(-1/2)` gives

```text
p_d^(-1) sum_r K_x(d,r)p_r
 <=sum_(U<r<=x/d)1/r <=L+O(1),                            (2.3)
```

whereas the Rayleigh quotient of `p` is `L/2+O_(ell,k)(1)`.
Moreover,

```text
norm(K_x)_HS^2=L^2/2+O_(ell,k)(L).                         (2.4)
```

There is a sharper description.  Map the basis vector at `n` to the
normalized indicator of
`[log n,log(n+1))`.  This logarithmic conjugation turns (2.2), up to a
quadrature error tending to zero, into the integral operator on `L^2[0,L]`

```text
(T_(L,k)f)(u)=integral_0^L
 Phi_(h,k)(L-u-v)f(v)dv.                                  (2.5)
```

The smoothed kernel differs from the sharp triangular kernel

```text
(T_L f)(u)=integral_0^(L-u)f(v)dv                          (2.6)
```

only on a strip of fixed width.  Their Hilbert--Schmidt distance is
`O_(ell,k)(sqrt(L))=o(L)`.  Solving the elementary eigenvalue equation for
(2.6) gives alternating eigenvalues whose absolute values are

```text
sigma_j(T_L)=2L/[(2j-1)pi],       j=1,2,... .              (2.7)
```

Consequently, for each fixed `j`,

```text
sigma_j(K_x)=2L/[(2j-1)pi]+o_(ell,k,theta)(L).             (2.8)
```

The approximation-number identity now proves, for every fixed `m`,

```text
inf_(rank Q<=m) norm(K_x-Q)
 >=2L/[(2m+1)pi]+o(L).                                    (2.9)
```

This is the finite-mode no-go.  It does not say that the actual arithmetic
vectors cannot cancel.  It says that no fixed-rank subtraction makes the
ambient near-square operator contractive.

## 3. Why coefficient norms and blocks lose the problem

For `beta_V(r)=sum_(b|r,b>V)Lambda(b)`, squarefree density and the prime
number theorem give, at fixed `theta`,

```text
norm(mu 1_(U,N])_2 asymp sqrt(N),

sum_(r<=N) beta_V(r)=NL+O(N),
norm(beta_V 1_(V,N])_2 asymp_theta sqrt(N)log x.           (3.1)
```

Here the lower bound in the last line follows from Cauchy--Schwarz and the
upper bound from `0<=beta_V(r)<=log r`.  Equations (2.3)--(3.1) put every
plain operator-norm estimate at the scale

```text
N(log x)^2=x^(1-theta)(log x)^2,                           (3.2)
```

not at scale one.

The loss is present locally.  Choose fixed constants `0<a<b<exp(-ell/2)`
and take `d,r` in `[a sqrt(x),b sqrt(x)]`.  For large `x` this rectangle lies
inside `(U,N]^2`, and the ramp is on its plateau.  The restricted kernel is
exactly rank one, so

```text
B_rect
 =[sum_d mu(d)/sqrt(d)] [sum_r beta_V(r)/sqrt(r)].         (3.3)
```

The second factor is `asymp x^(1/4)log x`, while

```text
sum_rect mu(d)^2 beta_V(r)/sqrt(dr)
 asymp sqrt(x)log x.                                      (3.4)
```

Thus absolute values discard cancellation of relative order at least
`1/[sqrt(x)log x]`.  As a heuristic comparison, independent random signs in
the first factor of (3.3) give only scale `O(1)`, still leaving
`x^(1/4)log x`.  Estimating such rectangles separately is therefore the
wrong problem: under RH their large pieces must cancel across rectangles and
cofactors.

The same obstruction appears in Mellin language.  The large singular modes
have frequencies `t` of order `j/L`, where every fixed-order ramp multiplier
is nonzero.  Plancherel reproduces (2.7), while squaring and separating the
blocks deletes the cross-cofactor terms that supply the cancelling `zeta`
factor in R68.

## 4. The variance-scale gate

On a fixed central multiplicative block, the prime terms alone give

```text
sum_(d,r) mu(d)^2 beta_V(r)^2/(dr) >> log x.               (4.1)
```

This makes `sqrt(log x)` the scale predicted by a fully decorrelated model;
it is not a theorem that this is the natural or optimal scale.  A
proof of (1.1) would have to correlate both arithmetic sides and then retain
the cancellations between all blocks.  Möbius randomness on only one side,
ordinary operator orthogonality, or a finite collection of low modes cannot
do it.

For fixed `k` and `0<theta<=theta_k`, the gap to present uniform technology
is nearly `sqrt(x)`.  The
Vinogradov--Korobov zero-free region and prime-number-theorem remainder give

```text
B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)
 << sqrt(x) exp(-c' (log x)^(3/5)(loglog x)^(-1/5)),        (4.2)
```

after partial summation against the fixed ramp.  Explicit modern versions
of the zero-free region and this remainder shape are recorded by
[Mossinghoff--Trudgian--Yang](https://link.springer.com/article/10.1007/s40993-023-00498-y).

More elaborate decompositions do not themselves provide the missing sign.
[Heath-Brown's generalized Vaughan identity](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/prime-numbers-in-short-intervals-and-a-generalized-vaughan-identity/D6C21FF61C1489E5856AA5ED276CB0A9)
reorganizes `sum Lambda(n)f(n)` into Type-I/II inputs; R68 performs the
relevant two-variable Vaughan decomposition.  Higher-order identities can
expose different multilinear partitions, but supply no cancellation unless
that extra structure supports a new estimate.  Modern density estimates,
including the bound of
[Guth--Maynard](https://ora.ox.ac.uk/objects/uuid%3Aad11b8bf-ad2b-4ebf-a627-647f023c378f),
can show that exceptional zeros or large values are sparse, but one off-line
zero already forces exponential growth of this fixed-width proxy.  Likewise,
[Matomaki--Radziwill](https://annals.math.princeton.edu/2016/183-3/p06)
obtain cancellation of multiplicative functions in almost all short
intervals, whereas (1.1) is a supremum over every moving hyperbola.

Neither kind of exceptional-set result eliminates all exceptions: (1.1)
requires every basepoint and the absence of every off-line zero.

## 5. Moving central-collar geometry

The equal-cutoff aggregate has a useful exact form.  Put `y=x^theta` and
`T=(1-2theta)log x`.  Expanding `r=bm` in `beta_y(r)` gives

```text
B_(y,y)(x)
 =sum_(d>y,b>y,m>=1) mu(d)Lambda(b)/(dbm)^(1/2)
    Phi_(h,k)(T-a-c-w),                                   (5.1)

a=log(d/y),   c=log(b/y),   w=log m.
```

Thus the moving form is a triple convolution on the simplex
`a,c>0`, `w>=0`, `a+c+w<T`; in particular the cofactor satisfies
`m<=exp(T)=x^(1-2theta)`.  Group the two central variables by

```text
g_y(q)=sum_(db=q,d>y,b>y)mu(d)Lambda(b).                   (5.2)
```

For `q=y^2 exp(v)`, its divisors lie in the central collar
`d=y exp(a)`, `0<a<v`.  Because the domain is symmetric under `d<->b`,

```text
g_y(q)=1/2 sum_(db=q,d,b>y)
             [mu(d)Lambda(b)+mu(b)Lambda(d)].              (5.3)
```

This is a genuine equal-cutoff central-collar reflection law, but it has no
favorable sign.  Since `mu*Lambda=-mu log` and `q>y^2` makes the two Type-I
tails disjoint,

```text
g_y(q)
 =-mu(q)log q
  -sum_(d|q,d<=y)mu(d)Lambda(q/d)
  -sum_(d|q,q/d<=y)mu(d)Lambda(q/d).                       (5.4)
```

More decisively, fix `c>1`.  Once
`c^2 y^2<=x exp(-ell)`, every `m=1` product of primes
`p,q in (y,cy]` lies on the ramp plateau.  For distinct primes
`g_y(pq)=-log(pq)`, while `g_y(p^2)=-log p`.  The entire prime--prime block
therefore equals

```text
-A_y B_y,
A_y=sum_(y<p<=cy)(log p)/sqrt(p),
B_y=sum_(y<p<=cy)1/sqrt(p),                                (5.5)
```

and the prime number theorem gives

```text
-A_y B_y
 ~-4(sqrt(c)-1)^2 y/log y.                                (5.6)
```

Reflection has reinforced a coherent negative semiprime block.  No local
divisor-pair involution, positivity argument, or absolute central-collar
estimate can control the centered aggregate.  Its cancellation must cross
the local Möbius-parity sectors, permit the retained cofactor sum to cancel
jointly, and include `Z_(y,y)`.

The role of the moving centering is also exact.  When `y` increases through
an integer `n`, put
`F_x(t)=t^(-1/2)Phi_(h,k)(log(x/t))`.  The raw balanced sum jumps by

```text
Delta B
 =-mu(n) sum_(b>=n,m) Lambda(b)F_x(nbm)
  -Lambda(n) sum_(d>=n,m) mu(d)F_x(dnm)
  +mu(n)Lambda(n) sum_m F_x(n^2m).                         (5.7)
```

The exact unevaluated Type-I centering has the opposite jump, because
Vaughan's identity is cutoff-independent.  Replacing it by the explicit
`Z_(y,y)` of R68 leaves only the stated Euler-evaluation error, which is
`o(1)` below the fixed-order endpoint and bounded at the endpoint.  This is
the automatic cutoff-motion cancellation identified here.  Freezing or
bounding `B` and `Z` independently destroys it.

## 6. What still survives

Let `u_j,v_j` denote the moving singular vectors of (2.2).  The unresolved
statement can be written schematically as

```text
sum_j sigma_j(K_x)
  inner(mu,u_j) inner(beta_V,v_j)
   =Z_(U,V)^(k)(x)+O(1),                                  (6.1)
```

with all modes and all cofactors retained.  The center in (6.1) is essential:
R68 proves that its critical zero-mode is unbounded when removed.

The next proposal must therefore supply a specifically arithmetic coupling
between the two singular projections in (6.1).  A nonlinear Euler-product
martingale, a sign-reversing cofactor involution with controlled moving
boundary, or a genuinely joint dispersion identity would qualify.  A norm
bound, finite-rank correction, mean-value theorem, or independent block
estimate would not.

### Growing-order fork

There is one useful sharpening.  If the smoothing order is `q` and
`h=ell/q`, its exact Perron kernel is

```text
H_q(s)=exp(-ell s/2)/s
       [sinh(ell s/(2q))/(ell s/(2q))]^q.                 (6.2)
```

Thus `H_q(s)` tends to the nonzero shifted sharp-cutoff kernel
`exp(-ell s/2)/s` at every fixed nonzero `s`.  On the critical axis,

```text
abs(H_q(i gamma))
 =abs(gamma)^(-1)abs(sinc(ell gamma/(2q)))^q,              (6.3)
```

so its effective spectral bandwidth is of order `sqrt(q)`.  Under RH the
absolute zero sum is `O_ell((log q)^2)`, rather than uniformly `O(1)`.

Proposition 6.2 of R68 now proves the uniform Euler bound
`exp(O_ell(q log(q+2)))`.  Hence one may take `q=q(x)->infinity`,
`q log q=o(log x)`, and `theta=1/2-c/q` with fixed `c>1/4`.  The Type-I
error is then `O(x^(-(2c-1/2)+o(1)))`, while

```text
d,r in [x^(1/2-c/q+o(1)),x^(1/2+c/q+o(1))],
cofactor m<=x^(2c/q)=x^o(1).                              (6.4)
```

This is an unconditional `x^(1/2+o(1))` arithmetic localization, and RH
implies a polylogarithmic residual through the absolute zero sum.  It is not
an RH-equivalent moving-test reduction.  Once `q=q(x)` there is no single
Laplace transform, so the fixed-test Landau argument does not supply the
required limsup lower bound.  Although (6.2) filters no fixed off-line zero,
an explicit regular or locally constant schedule requires a new uniform
oscillation theorem; arbitrary adaptive jumps are not covered.  Until that
theorem is proved, a subpower moving-order residual must not be claimed to
imply RH.

This checkpoint closes the standard functional-analytic Type-II route.  It
does not close the exact aggregate, and it does not prove or disprove RH.

## 7. Evidence boundary

Equations (2.3)--(2.9) are elementary operator estimates and logarithmic
Riemann-sum limits.  The asserted asymptotics and identities in
(3.1)--(5.7) use exact convolution identities, squarefree density, and the
prime number theorem; the random-sign comparison after (3.4) is explicitly
heuristic.  Equation (4.2) imports the classical Vinogradov--Korobov
remainder.  The exact RH equivalence and the necessity of joint cofactor
cancellation for the fixed-block and termwise strategies considered are
proved in
[`ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md`](ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md).
None of these arguments is formalized in Lean.
