# Finite-place pairing and normalized contraction generator

Status: ordinary finite pairings are ruled out; a normalized positive-definite
contraction survives and generates exactly the completed incidence defects,
2026-08-01.

## 1. Raw finite pairings do not order

For `q_p=p^(-1/2)` and `theta_p=t log p`, write

`w_p(t)=|L_p(1/2+it)|^2`

`      =1/(1+q_p^2-2q_p cos(theta_p))`.

Every factor exceeds one near phase zero and is below one near phase pi.  The
numbers `log p` for distinct primes are rationally independent, so Kronecker
approximation makes any prescribed finite collection of prime phases
simultaneously as close to zero or pi as desired.  Consequently none of the
following has a pointwise ordering relative to one:

- a nonempty finite product of Euler weights;
- the reflected pair `w_p(t)w_p(-t)=w_p(t)^2`;
- products over distinct primes;
- Poisson-mean-normalized products;
- the reciprocal/Möbius local inverse;
- a convex average over distinct primes.

The functional-equation scattering ratio has modulus one on the critical
line, so multiplying by it cannot repair the crossing.  An antipodal phase
pair also has both signs after natural normalization.

The archimedean gamma factor cannot make a raw finite product uniformly above
one: its modulus decays exponentially with `|t|`.  Thus no finite raw
completion has the desired Loewner positivity.

## 2. Moment-compression falsification

The sign-changing multiplier is visible in the canonical semilocal moment
filtration.  Direct two-prime examples for the even basis `{1,s^2,...}` give:

| pair | dimension | min update | max update |
|---:|---:|---:|---:|
| `(2,3)` | 2 | `-0.240` | `34.5` |
| `(2,5)` | 2 | `-0.263` | `19.9` |
| `(3,5)` | 2 | `-0.235` | `9.13` |
| `(5,7)` | 3 | `-0.229` | `4.02` |

Same-prime reflection and antipodal pairings also become indefinite.  Some
large-prime pairs look positive in dimension two but fail after one or two
additional moments, as polynomial localization predicts.

Mass normalization is especially decisive.  If `M` is a paired multiplier
and it is normalized by its archimedean mean, the constant moment update is
zero.  On `{1,s^2}` the determinant of the update is

`-Cov_mu(s^2,M)^2 / E_mu(M)^2`,

which is strictly negative whenever the covariance is nonzero.  Hence ordinary
mean preservation forces an indefinite two-dimensional update rather than a
positive one.

## 3. Surviving zero-phase contraction

There is one canonical normalization with a different purpose.  For
`sigma>0`, define

`C_(p,sigma)(t)`

` = |L_p(sigma+it)|^2 / |L_p(sigma)|^2`

` = (1-p^(-sigma))^2`

`   / (1+p^(-2sigma)-2p^(-sigma)cos(t log p))`.

The denominator differs from the numerator by

`2 p^(-sigma)(1-cos(t log p)) >= 0`,

so

`0<C_(p,sigma)(t)<=1`, `C_(p,sigma)(0)=1`.

Lean proves this exact contraction and its algebraic defect in
`RHBridge.NormalizedLocalContraction`.

Moreover `C_(p,sigma)` is positive definite.  Its Fourier expansion is the
characteristic function of a symmetric geometric law.  Thus it is a genuine
Hilbert contraction, not merely a pointwise trick.

## 4. Logarithmic generator identity

For `q=p^(-sigma)`, the convergent expansion is

`log C_(p,sigma)(t)`

` = -2 sum_(k>=1) q^k (1-cos(k t log p))/k`.

Differentiating in `sigma` gives

`partial_sigma log C_(p,sigma)(t)`

` = 2 log p sum_(k>=1) p^(-k sigma)
      (1-cos(k t log p))`.

At `sigma=1/2`, this is exactly the positive prime-power incidence-defect
symbol

`2 sum_(k>=1) Lambda(p^k)/sqrt(p^k)
    (1-cos(t log(p^k)))`.

The normalized archimedean factor has the parallel form

`A_sigma(t)=|Gamma_R(sigma+it)|^2/Gamma_R(sigma)^2 <=1`.

The inequality follows from the gamma integral and the triangle inequality.
Its logarithmic derivative is

`partial_sigma log A_sigma(t)`

` = Re psi((sigma+it)/2)-psi(sigma/2)`.

At `sigma=1/2`, this is precisely Gauss's positive archimedean
continuous-delay defect.

Therefore, for finite `S`,

`C_(S,sigma)(t)=A_sigma(t) product_(p in S) C_(p,sigma)(t)`

is a positive-definite contraction, and

`partial_sigma log C_(S,sigma)|_(sigma=1/2)`

is exactly the sum of the archimedean continuum incidence energy and all
prime-power defect energies from `S`.  Taking the logarithm is what cancels
all unwanted cross-place terms.

This gives a completion-native origin for the relative incidence complex
constructed earlier.

## 5. What it does not prove

The original Weil form is not just this positive generator.  Completing each
prime adjacency to a defect square leaves the scalar counterterm

`[psi(1/4)-log pi - 2 sum_active Lambda(n)/sqrt(n)] ||f||^2`

and the pole boundary form.  The two moment conditions remove the pole form,
but positivity still requires the relative Poincaré inequality saying the
generator dominates the scalar deficit.

Contractivity only proves that the generator is nonnegative.  It has value
zero at spectral phase zero, so it supplies no pointwise positive lower bound.
The moment constraints must create the missing uncertainty gap.

There is also an exhaustion obstruction.  For fixed `t != 0`,

`log C_(p,1/2)(t)
  =-2p^(-1/2)(1-cos(t log p))+O(p^-1)`,

and the prime sum diverges.  Hence the unrenormalized product over all primes
collapses to zero away from `t=0`.  It is meaningful as a finite-window or
infinitesimal generator, not as a nondegenerate global metric.

## 6. Assessment and next target

Finite raw place pairing is pruned.  The normalized contraction is a genuine
structural advance: it unifies Möbius/logarithmic cancellation, gamma Poisson
defects, and prime incidence squares as one logarithmic deformation.

The next sharp question is whether the two moment conditions imply a spectral
gap for this specific infinitely-divisible generator.  Equivalently, seek a
Poincaré inequality for the compound gamma--geometric law with exponential
type/support constraint.  This formulation may admit probabilistic tools
(tensorization, spectral-gap comparison, or entropy methods), but any bound
must retain the exact scalar counterterm and remain sharp as support grows.
