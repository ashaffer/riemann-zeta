# Fail-fast audit: stable lifts and passive Euler cascades

Status: two proposed mechanisms pruned, 2026-07-31.

## 1. The symmetric stable lift is circular

Let

`J^(d,n)(x) = sum_(j=0)^d binom(d,j) gamma(n+j) x^j`

be a xi Jensen polynomial.  Its canonical symmetric multiaffine polarization
`Pol(J)` is characterized by

`Pol(J)(x,...,x) = J(x)`.

The polarization theorem for stable polynomials gives both directions relevant
here:

1. if `Pol(J)` is stable, diagonal specialization makes `J` stable;
2. if the positive-coefficient univariate `J` has only real (hence negative)
   zeros, its symmetric polarization is stable.

Consequently the canonical strongly-Rayleigh/exchangeable lift exists exactly
when the original Jensen polynomial is hyperbolic.  It does not supply an
independent certificate.

The obvious determinantal lift has the same problem.  A polynomial with
positive coefficients and negative real roots can be written, up to a scalar,
as `det(I+xA)` with `A` positive semidefinite by placing the reciprocal root
parameters on the diagonal.  Conversely such a determinant has negative real
roots.  Existence of the representation is again equivalent to the desired
hyperbolicity unless `A` is produced by independent arithmetic structure.

The theta-kernel moment formula does not currently produce that structure.
Positive moment sequences give Hankel positivity/log-convexity; the xi
coefficients acquire their known log-concavity after factorial normalization.
This proves low-degree Turan inequalities but does not furnish the required
multivariate negative-dependence law.

This route is therefore killed in its natural form.  It can be reopened only
if a non-symmetric arithmetic model produces the lift before its stability is
known.

## 2. Finite computation cannot rescue the route

The literature already proves hyperbolicity for every shift through enormous
finite degrees by combining verified zeros with the Jensen criterion, and
proves eventual hyperbolicity for each fixed degree.  The missing region is a
joint unbounded degree/shift regime.  Testing additional small Rayleigh
inequalities cannot touch it and would reproduce known consequences.

## 3. Local Euler factors have the wrong passivity orientation

Set `s(z)=1/2-iz` and

`L_p(z)=(1-p^(-s(z)))^(-1)`.

Direct differentiation gives

`d/dz log L_p(z) = i log(p)/(p^(s(z))-1)`.

For `z=iy` with `y>1/2`, `s(z)=1/2+y>1`, so the denominator is positive and
the displayed logarithmic derivative has positive imaginary part.

By contrast, if a real entire function `F` has only real zeros, the zero terms
in `F'/F` are `1/(z-r)`, each of which has negative imaginary part for
`Im(z)>0` (with the standard real normalization of the affine term).  Thus the
Euler factors point in the opposite Nevanlinna/passivity direction from the
completed real-zero function.

Inverting each Euler factor corrects the sign but exchanges the zero/pole
orientation and no longer realizes completed zeta.  Hence a passive global
realization cannot be assembled as a passivity-preserving cascade of local
Euler factors.  The gamma factor, Poisson summation, and analytic continuation
would have to perform a genuinely global sign/index conversion.

This does not kill every Pontryagin-index formulation.  It kills the proposed
mechanism that made it attractive: local passivity plus index-preserving
composition.  Without that mechanism the missing continuation step again
contains essentially all the difficulty.

## 4. Resulting pivot

The next route is the finite-prime tropical Hodge program.  It survives this
audit because its proposed invariant is not a reformulation of a univariate
zero condition or a local Euler sign.  Connes--Consani explicitly identify
chip-firing, potential theory, and spanning trees as relevant to the missing
existence part of tropical Riemann--Roch.  The later theory of Lorentzian
polynomials supplies Hodge--Riemann signatures for spanning-tree/matroid
polynomials.

The first non-circular target is now:

> Construct a finite graph or arithmetic matroid from finitely many Frobenius
> correspondences such that its divisor intersection pairing, defined before
> reference to Weil positivity, pulls back to the finite-prime explicit-formula
> pairing.

If the construction exists, the basis-generating polynomial is automatically
stable/Lorentzian and its Hodge signature supplies the inequality.  If matching
the pairings requires choosing edge weights from the unknown positive
completion rather than from Frobenius incidence and degree, the route is
circular and must also be killed.

## Primary anchors

- Griffin et al., *Jensen Polynomials for the Riemann Xi Function*:
  https://arxiv.org/abs/1910.01227
- Borcea--Branden, *The Lee--Yang and Polya--Schur Programs I*:
  https://arxiv.org/abs/0809.0401
- Connes--Consani, *The Riemann--Roch strategy, Complex lift of the Scaling
  Site*, especially Section 3:
  https://arxiv.org/abs/1805.10501
- Branden--Huh, *Lorentzian polynomials*:
  https://arxiv.org/abs/1902.03719
