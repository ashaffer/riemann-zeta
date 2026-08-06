# Theta-flow Laguerre convolution audit

Status: exact reduction proved; the Polya-convexity and positive
Gaussian-mixture mechanisms are structurally impossible, updated 2026-08-06.

Let `a_t` be the even theta heat kernel on the real line and

`F_t(x) = integral_R a_t(u) exp(i x u) du`.

Direct differentiation and symmetrization give

`F_t'(x)^2 - F_t(x) F_t''(x) = integral_R b_t(w) exp(i x w) dw`,

where

`b_t(w) = (1/2) integral_R (2u-w)^2 a_t(u) a_t(w-u) du >= 0`.

This cleanly identifies the first Laguerre inequality as Fourier positivity
of an explicit positive convolution density.  Pointwise positivity of `b_t`
does not imply positivity of its Fourier transform.

## A failed sufficient mechanism

A classical Polya criterion would suffice if `b_t` were decreasing and convex
on `[0,infinity)`.  The script `src/xi_laguerre_polya_falsifier.py` finds that
`b_t` is decreasing on the sampled interval but concave near zero:

| `t` | sampled minimum second difference |
|---:|---:|
| 0 | -0.0219354 |
| 0.05 | -0.0219562 |
| 0.25 | -0.0220402 |
| 0.5 | -0.0221462 |

The obstruction is structural, not numerical.  Every differentiable even
function has right derivative zero at the origin.  If it is convex on the
positive half-line, its derivative is thereafter nonnegative; if it is also
decreasing, its derivative is nonpositive.  It must therefore be constant.
So no nonconstant smooth even convolution density can satisfy this version of
the criterion.

For this particular kernel the exact curvature identity is

`b_t''(0) = integral_R u^2(a_t a_t'' - a_t'^2) du`

`         = integral_R a_t^2 du - 2 integral_R u^2 a_t'^2 du`.

The scan evaluates this as negative, consistently with the finite
differences.

## A positive Gaussian mixture is also impossible

A stronger full-kernel proposal is to seek a Schoenberg-type representation

`b_t(w)=integral_[0,infinity) exp(-lambda w^2) d nu_t(lambda)`

with `nu_t` a nonzero positive measure.  This would make
`g_t(r)=b_t(sqrt(r))` completely monotone and would make
`b_t(w)=g_t(w^2)` positive definite (indeed radially positive definite in
every Euclidean dimension).  The proposal respects the full theta sum, but
its required tail behavior is impossible.

### Theorem

For every fixed finite real `t`, the exact theta convolution density `b_t`
has no representation as a nonzero positive Gaussian mixture.

### Proof

In the Rodgers--Tao normalization, put

`a_t(u)=exp(t u^2)Phi(abs(u))`.

After changing variables by `v=u-w/2`, the convolution density is

`b_t(w)=2 integral_R v^2 a_t(v+w/2)a_t(v-w/2)dv`.          (1)

The theta series gives, for `y>=0`,

`0<Phi(y)<=C exp(9y-pi exp(4y))`.                          (2)

For completeness, put `E=exp(4y)>=1`.  Positivity holds term by term because
`2 pi n^2 E-3>0`; after discarding the smaller polynomial factor, the tail is
bounded by

`sum_n n^4 exp(-pi n^2 E)
 <=exp(-pi E)sum_n n^4 exp(-pi(n^2-1)).`

For `w>=0`, set `p=abs(v+w/2)` and `q=abs(v-w/2)`.  Then

`p^2+q^2=2v^2+w^2/2`,

`p+q<=2abs(v)+w`,

`exp(4p)+exp(4q)>=2exp(2w)`,

and `exp(4p)+exp(4q)>=exp(4abs(v))`.  Split the last negative
exponential in (2) into two equal parts.  One part controls the `v` integral
in (1), while the other supplies the `w` decay.  Thus

```text
b_t(w)
 <=2C^2 exp(t w^2/2+9w-pi exp(2w))
   *integral_R v^2 exp(2t v^2+18abs(v)
                       -(pi/2)exp(4abs(v)))dv
 <=C_t exp(t w^2/2+9w-pi exp(2w)).                         (3)
```

The displayed integral is finite for every fixed real `t`.

Consequently `g_t(r)=b_t(sqrt(r))` decays faster than `exp(-M r)` for every
fixed finite `M`.  If

`g_t(r)=integral exp(-lambda r)d nu_t(lambda)`

for a nonzero positive measure, then `g_t(0)<infinity` makes `nu_t` finite.
For some finite `M`, the mass `m=nu_t([0,M])` is positive, and hence

`g_t(r)>=m exp(-M r)`.

This contradicts (3).  QED.

The theorem eliminates only positive mixtures of centered Gaussians.  It
does not refute positive definiteness of `b_t`, a signed modular
decomposition, or a different full-theta no-collision identity.

## What survives

The convolution identity is useful compression, but it exposes the real gate:
one needs a theta/modular reason that `b_t` is positive definite, not merely
positive.  Declaring it positive definite is exactly the desired Laguerre
inequality.  The next admissible candidate must provide an independent
factorization, variation-diminishing theorem, or modular identity implying
that property; generic Fourier or convexity arguments are pruned.

## Termwise modular decomposition also fails

Writing the positive-half theta kernel as its standard sum over `n`, the most
obvious stronger proposal is to prove the Laguerre inequality separately for
each summand and then control cross terms.  Its first premise is false.  For
the dominant `n=1` summand at `t=0`, 70-digit quadrature at `x=46` gives

`H = -1.0424350579242065769e-5`,

`H' = 2.7701864383602884e-8`,

`H'' = -3.3397193453196410e-8`,

and

`H'^2 - H H'' = -3.473766596285598e-13`.

Its scale-normalized value is about `-0.9956`, so this is not a rounding-level
sign.  The script `src/xi_theta_summand_falsifier.py` reproduces the scan.
The full theta sum is positive at the same tested height, meaning cross-summand
cancellation repairs the sign.  Modularity must therefore organize those
cross terms globally; a diagonal positive decomposition or a small-tail
perturbation argument is pruned.
