# Probabilistic Poincaré audit for the completed contraction

Status: the Lévy/Markov structure is exact, but generic Poincaré,
log-Sobolev, tensorization, and convexity methods cannot reach the sharp Weil
threshold, 2026-08-01.

## 1. Exact infinitely-divisible law

For `q=p^(-1/2)`, the normalized Euler contraction has Fourier expansion

`C_p(t)=((1-q)/(1+q)) sum_(k in Z) q^|k| exp(i k t log p)`.

It is the characteristic function of `(log p)K`, where `K` has the symmetric
geometric law

`P(K=k)=((1-q)/(1+q))q^|k|`.

Moreover

`log C_p(t)=2 sum_(n>=1) q^n/n (cos(n t log p)-1)`,

so it is infinitely divisible with symmetric Lévy atoms of mass `q^n/n` at
`+/-n log p`.

The normalized gamma contraction is the characteristic function of

`(log X-log Y)/2`,

where `X,Y` are independent Gamma(`1/4`,1) variables.  Its Lévy density is

`exp(-|z|/2) / (|z|(1-exp(-2|z|))) dz`.

Thus the finite completed product is the characteristic function of an
independent gamma-plus-geometric sum.  Its exponent is conditionally negative
definite and defines a symmetric convolution Markov semigroup.  The associated
Dirichlet form is exactly the continuum-plus-prime translation-defect energy.

This probabilistic identification is genuine and unconditional.

## 2. Exact threshold

Let `E_a` be this positive incidence energy with all prime powers active in
the support window, and put

`D(a)=2 sum_(log n<2a) Lambda(n)/sqrt(n)
      -(psi(1/4)-log pi)`.

On the two-moment relative subspace,

`Q_a(f)=E_a(f)-D(a)||f||^2`.

Abel summation gives, for `X=exp(2a)`,

`sum_(n<X) Lambda(n)/sqrt(n)
 = psi(X)/sqrt(X)+(1/2) integral_1^X psi(u)u^(-3/2)du`.

Consequently the prime number theorem gives

`D(a)=4 exp(a)+o(exp(a))`.

The fixed archimedean contribution is

`gamma + pi/2 + 3 log 2 + log pi = 5.372...`.

## 3. Exact nested-support sharpness

Suppose `f` satisfies both moment conditions and is supported in `[-b,b]`.
Embed it by zero extension into `[-a,a]`, `a>b`.  Every newly active shift
`h>2b` has zero autocorrelation, hence its difference-square energy is exactly

`2 Lambda(n)/sqrt(n) ||f||^2`.

Therefore

`E_a(f)-D(a)||f||^2 = E_b(f)-D(b)||f||^2`.

Lean formalizes the preservation of the two moments and this exact excess
identity in `RHP2Bridge.SharpIncidenceTransport`.  The only named analytic
input is the standard disjoint-support autocorrelation fact.

This is the decisive obstruction to generic functional inequalities.  An
embedded fixed-window near-minimizer has constant additive excess while

`E_a(f)/[D(a)||f||^2]-1 = O(exp(-a))`.

No uniform inequality of the form

`E_a >= (1+c)D(a)` with `c>0`

can hold.  No additional lower-order reserve growing with `a` can hold either.
The coefficient `4 exp(a)` is exactly sharp for structural reasons, regardless
of RH.

## 4. Numerical scale

`src/incidence_poincare_ratio.py` computes both the relative Galerkin excess
and the separately minimized continuum and prime incidence floors.  At
dimension 28:

| support | `D` | joint excess | continuum floor | prime floor | separate floors minus `D` | joint synergy |
|---:|---:|---:|---:|---:|---:|---:|
| 1.750 | `6.35244` | `9.26e-2` | `5.68473` | `0.49200` | `-0.17571` | `0.26834` |
| 2.485 | `7.62101` | `1.73e-5` | `5.32967` | `1.38599` | `-0.90535` | `0.90537` |
| 2.996 | `8.31416` | `1.34e-9` | `5.13834` | `1.92811` | `-1.24771` | `1.24771` |
| 3.555 | `9.75368` | `2.81e-12` | `4.96107` | `3.10091` | `-1.69170` | `1.69170` |
| 4.040 | `11.22465` | `1.07e-14` | `4.82634` | `4.56387` | `-1.83444` | `1.83444` |

The continuum-only and prime-only lower bounds miss the threshold by order
one.  The full coupled form closes that deficit, but only barely: at the last
window the observed joint excess is at floating-point resolution.  Thus the
entire useful gain comes from incompatibility of the two component
near-minimizers.  A generic estimate must hit the leading constant essentially
exactly; ordinary comparison losses are fatal.

## 5. Why standard probabilistic tools fail

### Ordinary Poincaré and tensorization

The variance of the finite completed law grows by

`2 sum_(p in S) (log p)^2 q_p/(1-q_p)^2`.

It diverges as places are added, so no support-uniform Poincaré constant comes
from tensorization.  More fundamentally, the convolution multiplier equals
one at frequency zero.  On the ambient line, its norm remains one after any
finite-codimensional restriction; low-frequency packets evade a strict gap.
Compact support creates a gap at each fixed window, but the exact transport
identity shows why it cannot have uniform multiplicative slack.

All completed jump generators act on the same logarithmic coordinate, not on
independent product coordinates.  Ordinary tensorization therefore returns at
best the sum of the separately constrained component floors.  The numerical
table shows that this bound is already negative relative to the required
threshold.  What restores positivity is the angle between the continuum and
prime near-null spaces, which tensorization explicitly forgets.

### Log-Sobolev

The completed law has exponential rather than Gaussian tails.  A classical
Gross log-Sobolev inequality would imply Gaussian concentration and is therefore
unavailable.

### Brascamp--Lieb

The log-gamma-ratio potential is asymptotically linear, so its uniform convexity
constant is zero.  Adding discrete geometric jumps does not create a positive
Hessian lower bound.

### Moment mismatch

The moment-generating functions of both the gamma and Euler laws exist only
for exponents strictly inside `(-1/2,1/2)`.  The Weil constraints use exactly
`+/-1/2`, the divergent boundary.  They are conditions on compactly supported
test functions, not ordinary centered observables of the invariant probability
law.  Standard covariance Poincaré arguments therefore do not even encode the
correct constraints.

## 6. Verdict

The probabilistic interpretation explains the positive defect energy and its
infinite divisibility, but it does not prove the required threshold.  Generic
Poincaré, entropy, convexity, and tensorization approaches are pruned.

The exact identity

`Q_a=E_a-D(a)||.||^2`

shows what a successful theorem must add: an arithmetic/support-specific
comparison with *exact leading constant one*.  Because smaller-window excesses
transport unchanged, this cannot arise from large-support mixing alone.

The remaining plausible use of the Markov structure is a phase-sensitive
angle theorem or an exact intertwining/ground-state transform that identifies
`E_a-D(a)` with `A_a^*A_a` plus the two moment squares.  Such an identity must
be derived independently from the gamma--Euler arithmetic.  Defining `A_a` as
the square root of the desired operator would merely assume its positivity and
is circular.  Any inequality with lossy constants is now known in advance to
fail.
