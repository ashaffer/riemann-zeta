# R93 Luroth dynamics and infinite-divisibility gate

Status: exact dynamical identification of the R92 Pareto carrier, an exact
finite-smoothing obstruction to infinite divisibility on every shifted right
half-plane, and a two-moment calculation showing that ordinary transfer
iteration loses the zeta divisor.  These results do not prove a fixed
zero-free strip and do not prove that no such strip exists.

Date: 2026-08-07.

## 1. Verdict

The positive R92 carrier is not an isolated floor-function accident.  After
the inversion `y=1/x` it is the full-branch harmonic sawtooth

```text
T(y)=n(n+1)y-n,             1/(n+1)<y<=1/n.           (1.1)
```

Thus

```text
integral_0^1 T(y)y^(s-1)dy
  =[(s-1)/(s(s+1))]zeta(s),             Re(s)>0.      (1.2)
```

The map in (1.1) is the classical Luroth map.  Each branch maps affinely
onto `(0,1]`, and Lebesgue measure is invariant.  This supplies a genuine
Bernoulli/transfer-operator structure that is unusual in a direct zeta
carrier.

Two tempting consequences fail exactly.

1. Convolving the carrier with any finite collection of exponential kernels
   makes it positive and arbitrarily differentiable, but cannot make the
   corresponding probability law infinitely divisible.  The unique
   candidate Levy measure has a negative continuous part between every pair
   of sufficiently large prime-power atoms.
2. Mixing of the Luroth map does not propagate the zeta factor to later
   iterates or powers.  Already the second positive moment contains an
   independent shifted value `zeta(s-1)`.

The dynamical reformulation is therefore useful, but neither a spectral gap
nor generic probability positivity supplies the desired strip.  A survivor
would have to estimate the *one-step signed correlation* in (1.2), or the
equivalent prime-atom versus continuous-pole measure, without taking total
variation.

## 2. Exact identification with the harmonic sawtooth

The R92 carrier is

```text
A(x)=N(N+1-x)/x,               N=floor(x), x>=1.      (2.1)
```

Put `y=1/x`.  On

```text
1/(N+1)<y<=1/N
```

one has

```text
A(1/y)=N((N+1)y-1)=N(N+1)y-N=T(y).                   (2.2)
```

Changing variables in the R92 Mellin identity gives (1.2).  This exact
unit-interval formula appeared as the "harmonic sawtooth map" in
[Crowley (2012)](https://arxiv.org/abs/1210.5652).  The calculation here is
independent of any dynamical claims made there.

For completeness, let `X` be uniform on `(0,1)`, let `N=n` when
`X` belongs to the `n`-th branch, and put `Y=T(X)`.  The inverse branch is

```text
X=(n+Y)/(n(n+1)),             0<Y<=1.                 (2.3)
```

and

```text
dX=dY/[n(n+1)].                                      (2.4)
```

Consequently

```text
P(N=n)=1/[n(n+1)],
Y is uniform on (0,1),
N and Y are independent.                              (2.5)
```

In particular `T` preserves Lebesgue measure and its branch digits form the
standard independent Luroth coding.  Equation (1.2) can be read as the
one-step correlation

```text
E[T(X)X^(s-1)]
  =[(s-1)/(s(s+1))]zeta(s).                           (2.6)
```

At a zeta zero this correlation vanishes.  Marginal invariance alone cannot
exclude that orthogonality: the oscillatory factor `X^(it)` is coupled to
the first branch and its remainder.

## 3. Finite exponential smoothing and the exact logarithmic derivative

Let `a_1,...,a_m>0`.  The zero-preserving finite smoothing factors produced
by the Pareto divided differences have the form

```text
G_a(s)=(s-1)zeta(s)/product_j(s+a_j).                 (3.1)
```

An additional factor `1/s` makes no difference to the argument below.  On
the real interval `s>1`, the Euler product gives

```text
-d/ds log G_a(s)
 =sum_j 1/(s+a_j)
  +sum_(n>=2) Lambda(n)n^(-s)
  -1/(s-1).                                           (3.2)
```

Every term in (3.2) has an elementary Laplace inverse.  The unique signed
inverse measure is

```text
dnu_a(u)
 =sum_(n>=2) Lambda(n) delta_(log n)(du)
  +[sum_j exp(-a_j u)-exp(u)]du.                      (3.3)
```

This identity exposes the exact prime--pole cancellation which a
probabilistic argument would have to retain.

## 4. A finite-smoothing infinite-divisibility no-go theorem

**Theorem 4.1.**  For no real `sigma_0` is

```text
Psi_a(s)=-d/ds log G_a(s)                             (4.1)
```

completely monotone throughout `(sigma_0,infinity)`.  The same conclusion
holds after adjoining finitely many further factors `1/(s+b)` with real
`b>0` or a factor `1/s`.

### Proof

Suppose `Psi_a(sigma_0+x)` were completely monotone for `x>0`.  Bernstein's
theorem would give a positive measure `mu` on `[0,infinity)` such that

```text
Psi_a(sigma_0+x)=integral exp(-xu)dmu(u).              (4.2)
```

For `x` sufficiently large, (3.2)--(3.3) also give

```text
Psi_a(sigma_0+x)
 =integral exp(-xu)exp(-sigma_0 u)dnu_a(u).            (4.3)
```

Uniqueness of the Laplace transform for locally finite measures of
exponential order forces

```text
dmu(u)=exp(-sigma_0 u)dnu_a(u).                        (4.4)
```

But away from the discrete set `{log n:n is a prime power}`, the absolutely
continuous density in (4.4) has the sign of

```text
sum_j exp(-a_j u)-exp(u),                              (4.5)
```

which is strictly negative for all sufficiently large `u`.  Every bounded
interval contains a subinterval avoiding the locally finite prime-power
set, so (4.4) assigns negative mass to some open interval.  This contradicts
positivity of `mu`.

Adding finitely many rational factors only appends finitely many decaying
densities `exp(-bu)` (or the constant density for `1/s`) to (4.5).  None can
dominate `-exp(u)` at infinity.  QED.

### Consequence

Even if enough positive Volterra smoothing turns a derivative of the
carrier into a probability density, its Laplace transform is not the
transform of an infinitely divisible law on any exponential tilt.  Thus
the standard implication

```text
infinitely divisible Laplace law
       => exponential Levy representation
       => zero-free right half-plane                    (4.6)
```

cannot prove a strip here.  Low-order numerical cumulants may all have the
correct sign; Theorem 4.1 says that some order must eventually fail.  This
is a structural obstruction, not a numerical one.

The theorem does **not** say that `G_a` has a zero in every proposed strip.
Complete monotonicity is sufficient for zero-freeness, not necessary.

## 5. Transfer iteration loses the divisor at the second moment

One could instead try to use the Bernoulli mixing of `T`.  The first
fail-fast check is to ask whether powers or iterates of the positive
observable retain the zeta zero.

For an integer `k>=0`, put

```text
M_k(s)=integral_0^1 T(x)^k x^(s-1)dx.                 (5.1)
```

On the `n`-th branch, expanding

```text
T(x)^k=[n(n+1)x-n]^k                                 (5.2)
```

and integrating term by term expresses `M_k` as a finite rational
combination of

```text
zeta(s),zeta(s-1),...,zeta(s-k+1).                    (5.3)
```

The first two nonconstant moments are

```text
M_1(s)
 =[(s-1)/(s(s+1))]zeta(s),                            (5.4)

M_2(s)
 =[(s-1)/(s(s+1))]zeta(s)
  -[2(s-2)/(s(s+1)(s+2))]zeta(s-1).                  (5.5)
```

The endpoint constants cancel exactly in (5.5).  Thus if `zeta(rho)=0`,

```text
M_2(rho)
 =-[2(rho-2)/(rho(rho+1)(rho+2))]zeta(rho-1),         (5.6)
```

which is generically nonzero.  Squaring the observable, taking positive
moment matrices, or invoking mixing of later Luroth coordinates therefore
does not preserve the target zero set.

The same logical dichotomy seen in the mod-6 matrix gate reappears.  Extra
dynamical moments either remain nonzero at a zeta zero and are spectators,
or they must be projected back onto the unique one-step combination (5.4),
where the strip problem returns unchanged.

## 6. Why a spectral gap is not yet a zeta estimate

Let `L` be the Perron--Frobenius operator of `T`:

```text
(Lf)(y)=sum_(n>=1)
 f((n+y)/(n(n+1)))/[n(n+1)].                          (6.1)
```

Then `L1=1`, and (2.6) is

```text
M_1(s)=integral_0^1 y (L x^(s-1))(y)dy.               (6.2)
```

A spectral gap controls `L^k f` after many iterations in a regularity norm.
It does not give a lower bound for the single signed matrix coefficient
(6.2).  Replacing it by a later coefficient changes `M_1` to a new
correlation whose Mellin expansion contains spectator shifted zeta values,
as (5.5) already demonstrates for the simplest positive lift.

Moreover the regularity norm of `x^(sigma-1+it)` grows with `abs(t)` and is
singular at zero when `sigma<1`.  Choosing the iteration count with the
height may smooth the test, but no identity propagates the vanishing of
`M_1` to that smoothed coefficient.  Mixing therefore supplies an upper
decorrelation estimate for the wrong observable, not nonvanishing of the
right one.

## 7. Exact surviving target

The probability and dynamics viewpoint reduces the next possible theorem
to one of two equivalent signed estimates.

**Luroth correlation form.**  Prove, for some fixed `eta>0`, that

```text
E[T(X)X^(sigma-1+it)] !=0,
                  sigma>1-eta.                        (7.1)
```

**Prime--pole Levy form.**  Control the signed transform of

```text
sum_(n>=2)Lambda(n)delta_(log n)-exp(u)du              (7.2)
```

after the exact finite rational corrections, without replacing it by its
total variation.

By (1.2), (7.1) is precisely the desired fixed-strip theorem.  By (3.2), a
fixed analytic control of (7.2) is another form of the same prime-number
remainder.  The new value of the formulation is that it sharply identifies
why generic Bernoulli mixing and generic infinite divisibility do not close
the estimate.

## 8. Bottom line

The R92 positive carrier is the Luroth map in disguise.  That gives an exact
full-branch probabilistic model, but not an automatic zero-free theorem.
Finite exponential smoothing cannot make its transform infinitely
divisible because the continuous pole field in (3.3) remains negative
between discrete prime-power atoms.  Ordinary positive moments and transfer
iterations lose the clean zeta divisor at once through `zeta(s-1)`.

No fixed strip and no failure of every fixed strip is proved.  The remaining
work is genuinely zeta-specific: sign the one-step Luroth correlation, or
equivalently obtain cancellation between the prime atom train and the
continuous pole field beyond what total variation or a generic spectral gap
can see.
