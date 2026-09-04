# AFE--Lee--Yang local holographic kill card

**Date:** 2026-08-13

**Truth boundary:** no zero-free strip is proved here.

## Binary verdict

```text
additive primal+dual AFE lift
  + coordinatewise invertible real GL(2) holographic changes:  KILLED

nonlocal primal--dual interaction / non-real circular-domain lift: OPEN-NARROW
```

This is a new scoped obstruction, not a restatement of the earlier
prime-separable Fejer or independent-spin failures.  It does not kill every
possible meaning of H10.

## 1. Smallest honest AFE cylinder

Write the functional-equation scalar as

\[
 \chi(s)=\pi^{s-1/2}
          \frac{\Gamma((1-s)/2)}{\Gamma(s/2)},
 \qquad \zeta(s)=\chi(s)\zeta(1-s).
\]

Select the Boolean `2,3` cylinder from a sharp or smoothed approximate
functional equation, and put every omitted head entry and the analytic tail
in the exact remainder `R_(2,3)(s)`.  Then the identity

\[
 \zeta(s)=(1+2^{-s})(1+3^{-s})
  +\chi(s)(1+2^{s-1})(1+3^{s-1})+R_{2,3}(s)             \tag{1.1}
\]

is exact by the displayed definition of `R_(2,3)`.  Thus it does not mistake
a finite Dirichlet head for zeta.  The associated real-coefficient,
multiaffine partition polynomial is

\[
 F=(1+x_2)(1+x_3)+g(1+y_2)(1+y_3)+r,                  \tag{1.2}
\]

with physical specialization

\[
 x_p=p^{-s},\quad y_p=p^{s-1},\quad
 g=\chi(s),\quad r=R_{2,3}(s).                         \tag{1.3}
\]

The gamma scalar and the exact tail are therefore present, not silently
dropped.  Freezing `g` at any positive real value already suffices for the
real-stability test below; the variable `r` is not needed for the failure.

## 2. Exact Rayleigh minor

For a real multiaffine polynomial, put

\[
 \Delta_{ij}F=F_iF_j-FF_{ij}.
\]

Real stability requires every `Delta_(ij)F` to be nonnegative on all real
specializations.  Direct differentiation of (1.2) gives

\[
 \boxed{\Delta_{x_2x_3}F=-g(1+y_2)(1+y_3)-r.}          \tag{2.1}
\]

At `g=1,r=0`, this minor equals `-1` for `(y_2,y_3)=(0,0)` and `+1` for
`(y_2,y_3)=(-2,0)`.  Hence it has both signs, and `F` is not real stable.

The obstruction is independent of the unit weights.  For

\[
 F=a_0+a_2x_2+a_3x_3+a_{23}x_2x_3+cD(y)+r,
\]

one has

\[
 \Delta_{x_2x_3}F
 =a_2a_3-a_{23}a_0-a_{23}\{cD(y)+r\}.                 \tag{2.2}
\]

Consequently any retained `23` primal coefficient, together with any
nonconstant additive dual sector (or an independent exact-tail variable),
makes the minor affine with nonzero slope and therefore sign-indefinite.
This applies to nonzero sharp or smoothed AFE weights as well.

For three primes the natural cylinder

\[
 F_3=\prod_{p\in\{2,3,5\}}(1+x_p)
     +g\prod_{p\in\{2,3,5\}}(1+y_p)+r
\]

has

\[
 \Delta_{x_2x_3}F_3
 =-(1+x_5)\left\{g\prod_p(1+y_p)+r\right\},           \tag{2.3}
\]

so the third prime does not repair the two-prime obstruction.

## 3. Why no local real holographic basis change repairs it

Let `H_+` and `H_-` be the upper and lower half-planes.  If a real
multiaffine `f` is nonvanishing on a product
`H_(epsilon_1) x ... x H_(epsilon_m)`, then changing variables
`z_i -> epsilon_i z_i` and applying the Rayleigh criterion gives the
necessary inequalities

\[
 \epsilon_i\epsilon_j\Delta_{ij}f(x)\ge 0
 \quad\hbox{for every }x\in\mathbb R^m.                \tag{3.1}
\]

A polynomial which has a Rayleigh minor of both signs therefore fails in
**every** product of upper/lower half-planes.

An invertible coordinatewise real holographic change is precisely the
homogenized Mobius action

\[
 f\longmapsto
 \prod_i(c_i z_i+d_i)
 f\left(\frac{a_i z_i+b_i}{c_i z_i+d_i}\right).
\]

Each factor maps `H_+` to `H_+` or `H_-` according to the sign of its real
determinant.  If the transformed polynomial were real stable, the original
one would be nonvanishing on the corresponding product domain, contradicting
(2.1) and (3.1).  Thus even allowing a different invertible real `GL(2)`
matrix at every primal, dual, gamma, and tail variable cannot rescue the
additive AFE lift.

## 4. Exact survivor and scope audit

H10 survives only by leaving the killed class.  A survivor must do at least
one of the following:

1. introduce genuine mixed primal--dual monomials before specialization, so
   it is not `P(x)+gD(y)+r`;
2. use a nonlocal transform which couples primal, dual, and completion
   channels, rather than a tensor product of local `GL(2,R)` changes; or
3. formulate a complex circular-domain stability cone and prove separately
   that the physical AFE specialization lies in its exclusion domain.

It must also encode the exact remainder constraint and an all-prime
consistency law.  Otherwise finite-head nonidentifiability still applies.

The earlier project evidence implicitly warned against symmetric stable
polarization and prime-separable models, but it did **not** contain the
two-prime cross-AFE minor (2.1).  Therefore the local/additive version is now
explicitly killed; the broader nonlocal H10 is still open, very narrow, and
has produced no strip.
