# R90 Newton-coefficient cancellation gate

Status: exact fixed-strip equivalence, lossless Poissonization, prime-product
probability model, total-positivity audit, bounded-arity transport no-go, and
finite-prime multiplicative countermodels completed.  The Newton coefficients
give an unusually clean target:

```text
|c_k| << k^(-1/2-delta) for one delta>0
        ==> zeta(s) != 0 for Re(s)>1-2 delta.              (0.1)
```

Conversely, a zero-free strip of width `eta` gives

```text
c_k <<_epsilon k^(-(1+eta)/2+epsilon).                    (0.2)
```

Thus any fixed power beyond the elementary `k^(-1/2)` bound is exactly the
requested breakthrough.  Poissonization does not dilute this target: its
error is `O(k^(-3/2))`.

The off-the-wall probability ideas are mathematically natural, but their
local versions do not create that power.  Under the canonical squarefree
probability measure the prime-divisibility bits really are independent.
However, conditioning their product to have size about `sqrt(k)` destroys
the usable independence, and the resulting conditional parity bias is the
Mertens problem itself.  A fixed number of prime-bit changes cannot repair
this: R89's positive-density smooth vertices are isolated from every
power-local bounded-arity sign flip.  Total positivity is also exact, but it
is variation diminishing rather than cancellation producing and the
Mobius input has unbounded sign variation.

The only surviving version is a genuinely global, growing-arity theorem on
the parity of a multiplicative random walk conditioned on its endpoint, or
an equivalent signed smooth/rough recombination.  No such theorem is proved
here.  In particular, this report proves neither that a fixed zero-free
strip exists nor that it does not exist.

Date: 2026-08-07.

## 1. The coefficient and its elementary scale

Put

```text
c_k = sum_(0<=j<=k) (-1)^j binom(k,j)/zeta(2j+2)
    = sum_(n>=1) mu(n)n^(-2)(1-n^(-2))^k.              (1.1)
```

The second identity follows by expanding `1/zeta(2j+2)` absolutely and
performing the finite binomial sum.  Its unsigned majorant is

```text
Q_k = sum_(n>=1) mu(n)^2 n^(-2)(1-n^(-2))^k.           (1.2)
```

Squarefree integers have density `6/pi^2`.  Partial summation, or the
change of variables `u=sqrt(k)/x`, gives

```text
Q_k ~ (6/pi^2) integral_0^infinity x^(-2)e^(-k/x^2)dx
    = 3/pi^(3/2) k^(-1/2).                             (1.3)
```

In particular,

```text
|c_k| << k^(-1/2)                                      (1.4)
```

is completely elementary and contains no Mobius cancellation.  A fixed
strip requires a fixed power of cancellation relative to the total
variation in (1.3), not merely a better constant.

The Vinogradov--Korobov zero-free region, transferred through the usual
Mertens estimate and partial summation, gives a subpower refinement of the
shape

```text
c_k << k^(-1/2)
       exp{-c (log k)^(3/5)(log log k)^(-1/5)}           (1.5)
```

after harmless changes of constants.  This is the Newton-coefficient form
of the imported baseline.  It is still `k^(-1/2-o(1))`, not (0.1).

## 2. Exact fixed-strip transfer

Define the Pochhammer polynomials

```text
P_k(z)=product_(1<=r<=k)(1-z/r)
      =Gamma(k+1-z)/(Gamma(k+1)Gamma(1-z)).             (2.1)
```

Their generating function is

```text
sum_(k>=0) P_k(z)w^k=(1-w)^(z-1),        |w|<1,         (2.2)
```

and, uniformly on compact `z`-sets,

```text
P_k(z)=k^(-z)/Gamma(1-z)(1+O_z(k^(-1))).                (2.3)
```

Substituting (1.1) into (2.2) gives, initially for `Re(s)>1`,

```text
1/zeta(s)=sum_(k>=0)c_k P_k(s/2).                       (2.4)
```

This is the Newton series which makes the strip transfer immediate.

### Theorem 2.1 (Báez--Duarte, general half-plane form)

Let `alpha` be fixed.  Then

```text
zeta(s) != 0 for Re(s)>2(1-alpha)                       (2.5)
```

if and only if, for every `epsilon>0`,

```text
c_k <<_epsilon k^(-alpha+epsilon).                      (2.6)
```

At `alpha=3/4` this is the usual sequential Riesz criterion for RH.

#### Sufficiency

If `c_k=O(k^(-alpha+epsilon))`, then (2.3) makes (2.4)
locally normally convergent whenever

```text
alpha-epsilon+Re(s)/2>1.                                (2.7)
```

It therefore analytically continues `1/zeta(s)` into every compact subset
of `Re(s)>2(1-alpha)`.  A zeta zero there would be a pole of the reciprocal,
which is impossible.

The pole of zeta at `s=1` causes no exception: `1/zeta(s)` has a zero there.
At positive even integers, the apparent gamma issue in (2.3) is removable
because the Pochhammer polynomials terminate.

In particular, the non-epsilon estimate

```text
c_k=O(k^(-1/2-delta))                                   (2.8)
```

already proves `zeta(s)!=0` for `Re(s)>1-2delta`.

#### Necessity

Suppose zeta has no zeros in `Re(s)>theta`.  On every smaller closed
half-plane `Re(s)>=theta+epsilon`, standard minimum-modulus bounds for zeta,
followed by truncated Perron inversion, give

```text
M(x):=sum_(n<=x)mu(n) <<_epsilon x^(theta+epsilon).      (2.9)
```

Conversely, (2.9) analytically continues the Dirichlet series for
`1/zeta`, so this is the familiar zero-free-half-plane/Mertens equivalence
with an epsilon at the boundary.

Summation by parts in (1.1), with

```text
g_k(x)=x^(-2)(1-x^(-2))^k,                              (2.10)
```

gives

```text
c_k=-integral_1^infinity M(x)g_k'(x)dx.                 (2.11)
```

The derivative is concentrated on `x asymp sqrt(k)`.  Scaling
`x=sqrt(k)y` in (2.11) gives

```text
c_k <<_epsilon k^(-1+theta/2+epsilon).                  (2.12)
```

Taking `theta=1-eta` yields (0.2).

### 2.2 The exact decay index

Let

```text
Theta = sup{Re(rho): zeta(rho)=0, 0<Re(rho)<1},
A_c   = sup{a: c_k=O(k^(-a))}.                          (2.13)
```

The epsilon form of Theorem 2.1 implies the exact identity

```text
A_c=1-Theta/2.                                          (2.14)
```

Indeed, any exponent below the right side follows by using a half-plane
strictly to the right of `Theta`, while any exponent above it would continue
`1/zeta` through a zero.  Consequently

```text
fixed zero-free strip  <=> Theta<1 <=> A_c>1/2,
RH                     <=> Theta=1/2 <=> A_c=3/4.       (2.15)
```

Known critical-line zeros force `A_c<=3/4`.  The elementary estimate (1.4)
gives `A_c>=1/2`.  The whole fixed-strip problem is the question whether the
left endpoint in this interval can be improved by any fixed amount.

An endpoint estimate without `epsilon` contains multiplicity information.
At a boundary zero of multiplicity `m`, the coefficient expansion below has
a polynomial in `log k` of degree `m-1`.  In the RH case, Báez--Duarte proved
that `c_k=O(k^(-3/4))` would force every nontrivial zero to be simple.

## 3. Poissonization is exact enough to use

Define

```text
F(t)=e^(-t)sum_(k>=0)c_k t^k/k!
    =sum_(n>=1)mu(n)n^(-2)e^(-t/n^2).                   (3.1)
```

Thus `F(t)` is the Riesz function divided by `t`.  It is also the Poisson
average of the Newton coefficients.

### Lemma 3.1 (lossless depoissonization at the relevant powers)

For integers `k>=1`,

```text
|c_k-F(k)| << k^(-3/2).                                 (3.2)
```

#### Proof

For `0<=x<=1/4`,

```text
0<=e^(-kx)-(1-x)^k << kx^2e^(-kx).                     (3.3)
```

Use `x=n^(-2)` for `n>=2`, take absolute values, and sum:

```text
|c_k-F(k)|
 << e^(-k)+k sum_(n>=2)n^(-6)e^(-k/n^2)
 << k^(-3/2).                                          (3.4)
```

The last estimate is the corresponding integral after
`n=sqrt(k)y`.  QED.

Since every possible zeta-driven exponent is at most `3/4`, the error in
(3.2) is far below the signal.  Poissonization cannot manufacture a false
fixed power and does not lose a real one.

### 3.2 Mellin transform and the complete pole ledger

For `0<Re(s)<1/2`, absolute convergence gives

```text
integral_0^infinity F(t)t^(s-1)dt
   =Gamma(s)/zeta(2-2s).                                (3.5)
```

This formula displays exactly what any concentration proof must accomplish.
The line `Re(s)=1/2` is the boundary of the absolutely convergent Euler
product.  A bound `F(t)=O(t^(-1/2-delta))` continues the Mellin transform
to `Re(s)<1/2+delta` and therefore excludes zeros with real part greater
than `1-2delta`.

Every nontrivial zeta zero `rho` produces a pole at

```text
s_rho=1-rho/2.                                         (3.6)
```

If `rho` is simple, shifting the Mellin contour to the right gives the local
large-`t` contribution

```text
Gamma(1-rho/2)/(2 zeta'(rho)) t^(rho/2-1).              (3.7)
```

The conjugate zero supplies the conjugate term.  The corresponding local
Norlund--Rice contribution to the discrete coefficient is

```text
B(k+1,1-rho/2)/(2 zeta'(rho))
 =Gamma(1-rho/2)/(2zeta'(rho)) k^(rho/2-1)(1+O_rho(1/k)).
                                                               (3.8)
```

The full zero sum is taken in the usual symmetric height limit; (3.7)--(3.8)
are local residue statements, not an assertion of absolute convergence of
the zero expansion.

If `rho` has multiplicity `m`, the pole in (3.5) has order `m`, and its
inverse-Mellin contribution is

```text
t^(rho/2-1) times a polynomial in log(t) of degree m-1. (3.9)
```

The remaining singularities have the following roles.

* The pole of zeta at `1` maps to `s=1/2`, but it is a **zero** of
  `Gamma(s)/zeta(2-2s)`, not a pole.
* The trivial zero `rho=-2m` maps to `s=m+1`.  Its discrete residue is

  ```text
  B(k+1,m+1)/(2zeta'(-2m))=O_m(k^(-m-1)).               (3.10)
  ```

  The first trivial-zero trend is therefore `O(k^(-2))`, much smaller than
  the nontrivial-zero scale.
* The poles of `Gamma(s)` at nonpositive integers govern the small-`t`
  expansion and do not affect the large-`t` fixed-strip question.

No cancellation among a displayed collection of residues can hide a
stronger uniform coefficient bound: the Newton series would then make the
reciprocal holomorphic at the corresponding zero.  This is the rigorous
version of the statement that an exceptional zero cannot be averaged away.

## 4. The exact independent-prime probability model

Let

```text
Z_sf=sum_(n>=1)mu(n)^2/n^2=zeta(2)/zeta(4)=15/pi^2,     (4.1)

P(N=n)=mu(n)^2/(Z_sf n^2).                              (4.2)
```

Then `N` is squarefree almost surely.  Writing

```text
B_p=1_(p divides N),                                    (4.3)
```

the variables `B_p` are genuinely independent and

```text
P(B_p=1)=1/(p^2+1),
N=product_p p^(B_p),
mu(N)=(-1)^(sum_p B_p).                                 (4.4)
```

Equation (3.1) becomes the exact probabilistic identity

```text
F(t)=Z_sf E[(-1)^(sum B_p)e^(-t/N^2)].                 (4.5)
```

This is the most favorable possible starting point for a prime martingale:
there is no approximation in the independence claim.

### 4.1 Why ordinary concentration stops at the elementary exponent

The random variable `L=log N=sum B_p log p` has an exponential right tail.
The event selected by (4.5) is the rare event

```text
L about (1/2)log t.                                    (4.6)
```

Ignoring the sign, (1.3) says precisely

```text
Z_sf E[e^(-t/N^2)] ~ 3/pi^(3/2)t^(-1/2).               (4.7)
```

Thus ordinary tail concentration recovers the unsigned `t^(-1/2)` scale.
The desired gain is a statement that parity is power-balanced **after
conditioning on the rare endpoint (4.6)**.

For `Re(z)<1`, the signed and unsigned exponential moments are

```text
Z_sf E[(-1)^(sum B_p)N^z]
  =product_p(1-p^(z-2))=1/zeta(2-z),                   (4.8)

Z_sf E[N^z]
  =product_p(1+p^(z-2))=zeta(2-z)/zeta(4-2z).          (4.9)
```

The normalized parity bias in the exponentially tilted ensemble is

```text
E_z[(-1)^(sum B_p)]
 =zeta(4-2z)/zeta(2-z)^2.                              (4.10)
```

As real `z` increases to `1`, (4.10) is only of order `(1-z)^2`.
Under the usual saddle correspondence `1-z` is logarithmic in the endpoint
scale.  Canonical-ensemble independence therefore supplies logarithmic
parity mixing, not a fixed power.

More decisively, the positive moment in (4.9) diverges at `z=1`.  No
Chernoff tilt exists beyond that point.  Continuing the **signed** moment
(4.8) into `Re(z)<1+2delta` is exactly the assertion that zeta has no zero
in `Re(s)>1-2delta`.  Probability independence proves (4.8) only in its
absolute-convergence half-plane; extending it is the target, not a free
consequence of independence.

### 4.2 The prime martingale does not mix the terminal parity

Let the filtration reveal primes in increasing order.  Without the rare
conditioning, the unrevealed parity has expectation

```text
product_(p>y) (p^2-1)/(p^2+1)=1+O(1/(y log y)).         (4.11)
```

It tends to `1`, not `0`, because `sum_p P(B_p=1)<infinity`.  There is no
tail-parity spectral gap in the original product measure.

After conditioning on `N` lying in a multiplicative interval around `X`,
the remaining bits are no longer independent.  Given the revealed product
`d`, the conditional expectation is a signed sum over squarefree cofactors
`m` in an interval around `X/d`.  It is therefore a rough or sifted Mertens
sum.  Azuma, Efron--Stein, and bounded-difference inequalities control
fluctuations of a random observable about its expectation; they do not make
this signed expectation small.  Moreover, flipping a prime bit changes the
sign itself, so the relevant influences are not uniformly small.

The clean microcanonical target is the following.  For a fixed smooth
annular weight `W`, prove for some `delta>0` that

```text
|sum_n mu(n)n^(-2) W(n/X)| <<_W X^(-1-2delta).          (4.12)
```

The unsigned denominator is `asymp X^(-1)`, so (4.12) says that the
conditional parity bias is `O(X^(-2delta))`.  By partial summation this is
another exact fixed-strip target.  Calling it concentration does not weaken
what has to be proved.

## 5. A prime-cascade operator formulation

There is an exact multiplicative cascade behind (4.5).  Let

```text
(D_p f)(t)=f(t/p^2).                                    (5.1)
```

Then, with convergence following from the squarefree expansion,

```text
F(t)=product_p (I-p^(-2)D_p)e^(-t).                    (5.2)
```

The Mellin transform diagonalizes all the commuting dilations:

```text
M[D_p f](s)=p^(2s)M[f](s),                              (5.3)
```

so the cascade multiplier is

```text
product_p(1-p^(2s-2))=1/zeta(2-2s).                    (5.4)
```

This suggests an unusual route: prove a weighted-norm contraction for the
signed dilation cascade rather than estimate Mobius sums directly.  The
fail-fast calculation is equally exact.  In the norm

```text
||f||_alpha=sup_(t>0)t^alpha|f(t)|,                    (5.5)
```

the perturbation `p^(-2)D_p` has size `p^(2alpha-2)`.  For
`alpha=1/2+delta`, these sizes are

```text
p^(-1+2delta),                                         (5.6)
```

whose prime sum diverges.  Triangle inequalities therefore fail precisely
at, and beyond, the elementary `alpha=1/2` boundary.  Any successful cascade
norm must exploit signed interference among infinitely many incommensurate
log-prime translations.  On Mellin characters that interference is exactly
the multiplier (5.4); a uniform minimum-modulus theorem for it is again the
zero-free-strip theorem.

Average control in the Mellin frequency is not enough.  One isolated zero
of zeta gives one pole in (3.5), hence a forbidden power term in `F(t)`.
The cascade requires a pointwise, all-frequency stability theorem rather
than an `L^2` or zero-density estimate.

### 5.1 Exact Muntz quadrature: an exponentially accurate but zero-blind sum

There is a striking exact identity which initially looks stronger than the
cascade formulation.  Directly from (3.1),

```text
sum_(m>=1)m^(-2)F(t/m^2)
 =sum_(m,n>=1)mu(n)(mn)^(-2)e^(-t/(mn)^2)
 =e^(-t),                                               (5.7)
```

because the coefficient of `k=mn` is
`sum_(n divides k)mu(n)`, which vanishes unless `k=1`.

Put

```text
h(x)=x^(-2)F(x^(-2)).                                   (5.8)
```

Then (5.7) is the integer-dilation or Muntz identity

```text
sum_(m>=1)h(mx)=x^(-2)e^(-x^(-2)).                      (5.9)
```

Its Mellin transform makes both its power and its limitation exact.  For
`1<Re(s)<2`, substitution `t=x^(-2)` in (3.5) gives

```text
H(s):=integral_0^infinity h(x)x^(s-1)dx
     =Gamma(1-s/2)/(2zeta(s)).                          (5.10)
```

Integer-dilation summation multiplies a Mellin mode by `zeta(s)`, so

```text
M[sum_m h(m dot)](s)
 =zeta(s)H(s)=Gamma(1-s/2)/2.                           (5.11)
```

This is precisely the Mellin transform of the right side of (5.9).

Now use the known Vinogradov--Korobov bound (1.5).  It makes `h` integrable
at zero as well as infinity, and continuation of (5.10) to `s=1` gives the
ordinary, not merely regularized, identity

```text
integral_0^infinity h(u)du
 =(1/2)integral_0^infinity F(t)t^(-1/2)dt
 =0.                                                    (5.12)
```

Consequently (5.9) says that the mesh-`x` Riemann sum has the
super-exponentially small quadrature error

```text
x sum_(m>=1)h(mx)-integral_0^infinity h(u)du
 =x^(-1)e^(-x^(-2)).                                   (5.13)
```

It is tempting to combine zero integral and (5.13) with an inverse
Euler--Maclaurin theorem and conclude that `h` is less singular than
`x^(-1)` at zero.  That inference is false for an exact, zeta-specific
reason.

#### Theorem 5.2 (zero-mode annihilation gate)

At the level of meromorphic Mellin germs, the Muntz operator

```text
(Th)(x)=sum_(m>=1)h(mx)                                 (5.14)
```

obeys

```text
ord_rho M[Th]=ord_rho H+ord_rho zeta.                  (5.15)
```

If `rho` is a zeta zero of multiplicity `r`, then `H` in (5.10) has a pole
of order `r`, while `zeta(s)H(s)` is regular there.  In boundary language,
a simple-zero residue gives

```text
h(x) contains C_rho x^(-rho),                          (5.16)
```

which is the same as
`F(t)` containing `C_rho t^(-1+rho/2)`.  Formal dilation of this mode gives

```text
sum_m (mx)^(-rho)=zeta(rho)x^(-rho)=0.                 (5.17)
```

Equation (5.15), rather than the formal series in (5.17), is the rigorous
statement: the zero cancels the Mellin pole with its full multiplicity.
The exponentially small output (5.13) is therefore compatible with every
exceptional-zero boundary mode which the fixed-strip problem is trying to
exclude.

Classical Euler--Maclaurin remainders exclude such modes by assuming
boundary derivatives, bounded variation, or a comparable modulus of
regularity.  Here the needed regularity is already the theorem:

```text
h(x)=O(x^(-1+eta+epsilon)) as x downarrow 0
 <=> F(t)=O(t^(-(1+eta)/2+epsilon))
 ==> zeta(s)!=0 for Re(s)>1-eta.                       (5.18)
```

Thus (5.13) cannot bootstrap PNT-level decay without an independent
boundary estimate.  The quadrature operator was designed by Mobius
inversion to erase exactly the forbidden modes.

#### 5.2 A universal linear-dilation no-free-lunch theorem

Changing the quadrature weights does not evade the issue for free.  Let
`a(m)` be an arithmetic weight for which the following sums initially
converge, put

```text
A(s)=sum_m a(m)m^(-s),
c=a*mu,
C(s)=sum_k c(k)k^(-s)=A(s)/zeta(s),                    (5.19)
```

and define `T_a h=sum_m a(m)h(m dot)`.  Expanding (5.8) and grouping
`k=mn` gives the exact heat identity

```text
(T_a h)(x)
 =x^(-2)sum_(k>=1)(a*mu)(k)k^(-2)e^(-1/(kx)^2).        (5.20)
```

On Mellin transforms,

```text
M[T_a h](s)
 =A(s)H(s)
 =Gamma(1-s/2) C(s)/2.                                 (5.21)
```

This yields a dichotomy at every zeta zero `rho`.

* If the output coefficient series `C(s)` is independently regular at
  `rho`, then `A(s)=zeta(s)C(s)` has the compensating zero and `T_a`
  annihilates the exceptional mode.
* If `A(rho)` does not vanish enough to annihilate it, then `C=A/zeta`
  has the compensating pole.  The output in (5.20) now contains the same
  exceptional mode, and obtaining a fixed-power bound for that output is
  the original zero-free problem in new coefficients.

The two most instructive examples are exact.

1. For `a(m)=1`, one has `A=zeta`, `a*mu=delta_1`, and (5.20) is the
   super-small but completely blind identity (5.9).
2. For `a(m)=log m`, one has

   ```text
   A(s)=-zeta'(s),             a*mu=Lambda.             (5.22)
   ```

   Hence

   ```text
   sum_m (log m)h(mx)
    =x^(-2)sum_k Lambda(k)k^(-2)e^(-1/(kx)^2),          (5.23)

   M[(5.23)](s)
    =-Gamma(1-s/2)zeta'(s)/(2zeta(s)).                  (5.24)
   ```

   The zero is no longer annihilated, but it has reappeared as the pole of
   `-zeta'/zeta`.  The positive prime heat sum in (5.23) has pole main term
   `(sqrt(pi)/2)x^(-1)`; after centering that term, a fixed-power bound is a
   prime-number-theorem discrepancy estimate of the required strength.
   This is the linear-dilation bridge back to the complete prime
   discrepancy/R71 problem.

So varying the quadrature offers a useful design principle but no automatic
escape.  A tame right side forces zero blindness; a zero-sensitive right
side inherits a reciprocal-zeta pole.  Any proposed weighted quadrature
should be checked against (5.19)--(5.24) before numerical smoothness is
interpreted as cancellation.

## 6. Total positivity is real but points the wrong way

Set

```text
x_n=1-n^(-2),
K(k,n)=n^(-2)x_n^k.                                    (6.1)
```

For increasing nonnegative integers `k_1<...<k_r` and increasing
`2<=n_1<...<n_r`,

```text
det(K(k_i,n_j))_(i,j)>0.                                (6.2)
```

After removing the positive column factors, this is a generalized
Vandermonde determinant.  It is the ordinary Vandermonde times a Schur
polynomial with positive coefficients.  Thus the Newton kernel is strictly
totally positive of all orders.

This does not give the desired estimate.

1. Total positivity is variation diminishing.  It controls output sign
   changes when the input has controlled sign variation.  The sequence
   `mu(n)` has unbounded sign variation; the primorial subsequence alone
   alternates forever.
2. The desired statement is a norm cancellation, not a sign-variation
   statement.  Replacing `mu(n)` by `mu(n)^2` retains the same kernel and
   support but produces the sharp unsigned asymptotic (1.3).
3. A positive representing measure would make `c_k` a Hausdorff moment
   sequence, but its actual representing measure is

   ```text
   nu=sum_n mu(n)n^(-2)delta_(1-n^(-2)),                (6.3)
   ```

   which is signed.  Its endpoint regularity is the missing theorem.

Indeed, the cumulative mass of (6.3) within distance `y` of `1` is

```text
nu([1-y,1))=sum_(n>=y^(-1/2))mu(n)/n^2.                (6.4)
```

An `O(y^(1/2+delta))` bound for (6.4), after summation by parts in the
opposite direction, is equivalent up to endpoint epsilons to a fixed-power
Mertens bound.  Total positivity faithfully transmits this regularity once
it is known; it does not create it.

## 7. Sign-reversing coupling and the R89 smooth obstruction

The coupling idea does explain geometrically what a fixed power would look
like.  Put `t=X^2` and

```text
w_X(n)=n^(-2)e^(-X^2/n^2).                              (7.1)
```

On `X/2<n<=X`,

```text
|w_X'(x)| << X^(-3).                                   (7.2)
```

If opposite Mobius signs could be paired throughout this annulus with

```text
|n-m|<<X^(1-alpha),                                    (7.3)
```

then each paired difference would be `O(X^(-2-alpha))`.  There are `O(X)`
atoms, so the annular remainder would be

```text
O(X^(-1-alpha))=O(t^(-1/2-alpha/2)).                   (7.4)
```

Thus a power-local sign-reversing transport really would give a fixed
strip.

R89 proves that this cannot be implemented by any fixed bounded-arity
prime exchange.  If an edge changes at most `r` primes on either side and
obeys (7.3), then a positive density of the squarefree integers in the
annulus are sufficiently smooth that every changed factor block is too
small to support even one such edge.  More precisely, a family of
`X^(alpha/r)`-smooth odd squarefree vertices has cardinality

```text
(constant_(alpha,r)+o(1))X,                            (7.5)
```

and every one is isolated in the power-local exchange graph.

Their total squarefree probability mass, and their total `w_X` mass, are
both `asymp X^(-1)`: exactly the unsaved scale.  Consequently none of the
following pointwise mechanisms can prove (7.4) with fixed arity:

* a sign-reversing involution;
* a fractional matching or bounded-congestion transport;
* a local Metropolis or Glauber chain which changes finitely many prime
  bits per step while remaining in the thin endpoint window;
* a Stein coupling based on one bounded-size prime resampling.

This does **not** prove that the signed sum of the isolated smooth vertices
is large.  They may cancel globally among themselves.  It proves that such
cancellation cannot be reduced to a positive local pairing of bounded prime
arity.  A successful coupling must use arity growing with the smoothness
depth, allow power-long jumps and then cancel their flux, or abandon
pointwise pairing.

## 8. An explicit family of parity-barrier countermodels

The obstruction to finite-prime concentration can be made completely
explicit.  Fix `y` and define a squarefree multiplicative coefficient

```text
a_y(n)=0                                      if n is not squarefree,
a_y(n)=(-1)^(#{p<=y:p divides n})             if n is squarefree.   (8.1)
```

It agrees with Mobius on every integer supported on primes at most `y` and
has exactly the same squarefree divisibility process.  Only the unresolved
large-prime parity has been replaced by `+1`.  Its Dirichlet series is

```text
A_y(s)
 =product_(p<=y)(1-p^(-s)) product_(p>y)(1+p^(-s))
 =zeta(s)/zeta(2s)
    product_(p<=y)(1-p^(-s))/(1+p^(-s)).                (8.2)
```

Unlike `1/zeta(s)`, this has a pole at `s=1` with positive residue

```text
R_y=1/zeta(2) product_(p<=y)(p-1)/(p+1).                (8.3)
```

Therefore its Poissonized Newton analogue has the elementary asymptotic

```text
sum_n a_y(n)n^(-2)e^(-t/n^2)
  ~ (sqrt(pi)/2)R_y t^(-1/2).                           (8.4)
```

Mertens' product theorem gives

```text
R_y ~ e^(-2 gamma)/(log y)^2.                           (8.5)
```

Thus arbitrarily many prescribed local prime signs and the full independent
divisibility law are compatible with only a logarithmic improvement over
the unsigned baseline.  No argument stopped at a finite prime-filtration
level, no kernel-only total-positivity theorem, and no concentration theorem
for the magnitudes can distinguish (8.1) from Mobius.

This is a finite-depth no-go, not an impossibility theorem for a filtration
whose depth grows with `t`.  It identifies the necessary ingredient: the
proof must use the coherent `-1` sign of **unboundedly many** prime factors
in a way uniform at the endpoint scale.  That is the classical sieve parity
barrier in an explicit multiplicative model.

There is also a useful statistical-mechanics reality check.  Work of
Cellarosi and of Avdeeva--Li--Sinai rigorously studies signed prime-product
ensembles and signed Dickman-type limits.  At the Mobius parameter the
limiting distributions have singular, regularity-dependent behavior.  This
technology captures canonical/logarithmic parity mixing, but a power-size
microcanonical remainder still requires analytic information about
`1/zeta`; it does not supply a fixed strip for free.

## 9. Smooth/rough recombination: the only coupling loophole left

For any threshold `y`, factor a squarefree integer uniquely as `n=ab`, where
all prime factors of `a` are at most `y` and all prime factors of `b` exceed
`y`.  Define

```text
F_<=y(u)=sum_(P^+(a)<=y)mu(a)a^(-2)e^(-u/a^2).          (9.1)
```

Then the exact identity

```text
F(t)=sum_(P^-(b)>y) mu(b)b^(-2) F_<=y(t/b^2)            (9.2)
```

holds.  It is the probabilistic/cascade counterpart of Daboussi's
smooth--rough decomposition of `M(x)`.

This does evade the narrow statement of the R89 no-go: the smooth sector
can cancel internally and the rough cofactor can perform a move of growing
arity.  But taking absolute values in either `a` or `b` restores the
`t^(-1/2)` scale.  Estimating the two sectors separately by their canonical
concentration laws gives at best logarithmic or Vinogradov--Korobov
subpower gains.  The required theorem is a **signed joint estimate in
(9.2)**, uniform when `y` is a power of `sqrt(t)`.

A concrete promotion gate would be the following.

> Find `delta>0` and a scale choice `y=t^kappa` for which the complete
> right side of (9.2), before absolute values, is
> `O(t^(-1/2-delta))`; the proof must include the positive-density smooth
> sector and the long rough-cofactor flux in one estimate.

By Theorem 2.1 this would prove a fixed zero-free strip.  A bound only for
`F_<=y`, only for almost all endpoint windows, or only in mean square over a
Mellin frequency cannot do so.

## 10. Verdict and next reality check

The Newton route is a good detector and a sharp experimental language, but
the simple probabilistic mechanisms fail at identifiable places:

```text
Newton fixed-strip equivalence                 EXACT
Poissonization/depoissonization                 EXACT, O(k^(-3/2)) loss
prime-divisibility independence                EXACT before conditioning
ordinary concentration                         unsigned k^(-1/2) only
real exponential tilting                       stops at z=1
signed transform beyond z=1                    equivalent to zero-free strip
Muntz quadrature error                          exponentially small, zero-blind
weighted linear quadrature                     tame output or reciprocal-zeta pole
total positivity                               EXACT but non-coercive
bounded-arity local coupling                   KILLED by R89 smooth vertices
finite-prime martingale                        KILLED by countermodels (8.1)
growing-arity conditioned parity theorem       OPEN
signed smooth/rough recombination (9.2)         OPEN
fixed zero-free strip                          NOT PROVED.          (10.1)
```

The most honest new intuition is this: a successful cancellation mechanism
cannot be a local prime resampling theorem.  It must be a microcanonical
theorem for an infinite multiplicative cascade, with growing arity and a
pointwise endpoint estimate.  The smooth vertices which killed R89 cannot
be discarded; their internal parity must cancel jointly with the rough
cofactor sector.  Equation (9.2) is the cleanest place to attempt that, and
(4.12) is the cleanest acceptance test.

Failure of these mechanisms is not evidence that `Theta=1`.  Proving that
no fixed strip exists would require producing zeta zeros with real parts
tending to `1`; nothing in this audit approaches such a theorem.

## Literature anchors

* L. Báez-Duarte,
  [*A sequential Riesz-like criterion for the Riemann hypothesis*](https://doi.org/10.1155/IJMMS.2005.3527),
  Int. J. Math. Math. Sci. 2005, Theorems 1.1 and 1.4.
* K. Maslanka,
  [*Báez-Duarte's criterion for the Riemann hypothesis and Rice's
  integrals*](https://arxiv.org/abs/math/0603713), for the
  Norlund--Rice trivial/nontrivial-zero decomposition.
* F. Cellarosi,
  [*Smooth sums over smooth k-free numbers and statistical
  mechanics*](https://arxiv.org/abs/1304.6610), for independent-prime and
  signed Dickman-type ensembles.
* M. Avdeeva, D. Li, and Ya. G. Sinai, *New limiting distributions for the
  Mobius function*, Moscow J. Combin. Number Theory 4 (2014), for the
  singular signed limiting laws.
* [`R89-MOBIUS-NEAR-ISOMETRIC-FLOW-GATE.md`](R89-MOBIUS-NEAR-ISOMETRIC-FLOW-GATE.md),
  especially the bounded-arity smooth-isolation theorem.
