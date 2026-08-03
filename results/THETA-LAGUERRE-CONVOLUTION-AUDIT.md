# Theta-flow Laguerre convolution audit

Status: exact reduction proved; the global Polya-convexity mechanism is
structurally impossible, 2026-08-01.

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
