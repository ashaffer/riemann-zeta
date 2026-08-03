# Hodge low-sector spectral gate audit

Status: the first four old relative modes are a plausible continuum spectral
cluster, but the currently displayed odd `2 x 2` determinant is not yet a
sufficient continuum target.  The exact high-tail theorem does not reduce the
continuum problem to four modes, and the even two-mode block is becoming just
as critical as the odd block.  The quickest sound falsifier is therefore a
certified negative smooth witness for the complete strengthened event form,
not another unsigned Galerkin extrapolation.

## 1. Continuum operator behind the split

On a fixed old interval `I`, let `H_0` be the codimension-two subspace of
`L^2(I)` annihilating the two exponential moments.  Its logarithmic form
domain is

`D_log = {f in H_0 : integral log(1+xi^2) |fhat(xi)|^2 dxi < infinity}`.

The archimedean multiplier is comparable, up to bounded terms, with
`log(1+xi^2)`.  Prime translations and the pole term are bounded on `L^2`.
Consequently the localized Weil form is a bounded perturbation of the
positive logarithmic form.  It is closed and semibounded on `D_log`.

The embedding `D_log -> L^2(I)` is compact.  Indeed, a form-norm bounded set
has the uniform Fourier-tail estimate

`integral_(|xi|>R) |fhat(xi)|^2 dxi`

` <= C / log(1+R^2)`,

and compact support supplies tightness.  The Kolmogorov--Riesz criterion then
gives compactness.  The associated Friedrichs operator therefore has compact
resolvent and a discrete min--max spectrum tending to infinity.  Restricting
to the closed moment kernel does not change this conclusion.

This justifies a finite low spectral sector for each fixed event.  It does not
give a uniform number of low modes, a positive old gap, or the desired collar
contraction.

## 2. When four modes define a genuine projection

For exact conforming form-core spaces `V_N`, Rayleigh--Ritz eigenvalues
converge to the continuum eigenvalues.  Nesting is convenient but unnecessary
if `V_N` approximates every form-domain vector in the form norm.  Because the
resolvent is compact, there is no spectral pollution for these exact
compressions.  If

`lambda_4 < lambda_5`,

then the projection onto the first four modes is intrinsic, and the discrete
rank-four projections converge to it.  Without a certified gap, selecting
"the first four" is only a dimension-dependent coordinate choice.

A cutoff-free Legendre diagnostic on the relative moment kernel at the hard
old support `L=log 20` gives

| dimension | first five relative Ritz values |
|---:|:---|
| `24` | `1.18e-8, 3.51e-7, 8.06e-5, 2.951e-3, 9.488e-2` |
| `32` | `1.03e-9, 1.16e-7, 4.13e-5, 2.729e-3, 9.197e-2` |

Thus the observed `lambda_4`--`lambda_5` separation is strong evidence for a
true rank-four cluster.  A proof still needs an upper enclosure for
`lambda_4` and a full-space lower enclosure for `lambda_5` with disjoint
intervals.

## 3. Why the current matrices are not yet a convergence proof

`src/hodge_sector_scan.py` is conforming in its piecewise-linear trial
functions, but its archimedean matrix is integrated only over a finite Fourier
window and is then evaluated by floating-point Simpson quadrature.  Hence it
is not the exact Rayleigh--Ritz compression of the continuum form.  Ordinary
no-pollution theorems do not apply until one proves a uniform tail and
quadrature estimate, or replaces this assembly by the cutoff-free time-domain
incidence integral.

At each fixed hat dimension the cutoff diagnostic is stable: at old degree
`61`, raising the angular cutoff from `1200` to `4800` changes the odd
low-sector contraction from about `.966550` to `.966390`.  This is useful
numerical hygiene, but not a simultaneous `N -> infinity` error estimate.
The issue becomes decisive near the collapsing old ground value.  At degree
`241` the hat/cutoff old gap is about `3.96e-8`, while cutoff-free spectral
approximations are already near `1e-9` and the independent full-space
certificate at the nearby endpoint lives at the `1e-15` scale.  Double
precision and unsigned cutoff errors cannot resolve that limiting mode.

## 4. Schur convergence requires a second gap

Let `A` be the positive old operator and `P` its rank-four projection.  Write
`B` for the old--collar row and include the high Hodge trace in

`D_hat = C - B^* (1-P) A^(-1) (1-P) B - T_high^* T_high`.

If the old rank-four spectral gap is certified, the rows converge in the
appropriate operator topology, and

`D_hat >= delta I` for some `delta>0`,

then the discrete inverses converge and so do the finite response entries
`h_ij=<r_i,D_hat^(-1)r_j>`.  Only under these hypotheses do the two parity
determinants converge to fixed continuum determinants.  If the residual
collar floor tends to zero, inversion is unstable and convergence of the old
spectral projection alone is insufficient.

The formal raw high-sector estimate closes modes above approximately
`mu=3` in the hard diagnostic.  The fifth old eigenvalue is only about
`.09`.  It therefore leaves dozens of medium modes, not four.  Showing
`D_hat>0` after eliminating every mode from the fifth onward is a proper
medium/high-sector theorem that is not presently proved.  Assuming it is not
identical to assuming the final low determinant, but it cannot be treated as
automatic compact-resolvent bookkeeping.

## 5. The odd determinant is not the whole low gate

Reflection decomposes the four-mode cluster into two even and two odd modes.
Unless one parity block is independently certified, the continuum low target
is the conjunction of two `2 x 2` principal-minor inequalities.  The odd
block is only the hardest one at the current resolutions.  At old degree
`241`, the contractions after numerical high elimination are

`rho_even = .9959133`, `rho_odd = .9962161`.

The even value has caught up rapidly as the unresolved even ground mode
descends.  There is no theorem that the odd block remains dominant in the
continuum.  Thus proving only the displayed odd determinant would not close
the strengthened event inequality.

## 6. A rigorous spectral gate

A sufficient convergence package is:

1. exact forms on a common smooth/form core, with Mosco convergence of the
   numerical forms;
2. a certified continuum separation `lambda_4 + eta <= lambda_5`;
3. operator-norm convergence of the cross and Hodge rows on the isolated
   low cluster;
4. a certified residual floor `D_hat >= delta I` after modes `j>=5` are
   removed;
5. interval errors smaller than both parity determinant margins.

These hypotheses imply convergence of the rank-four Riesz projections,
resolvent convergence of `D_hat`, and convergence of both low determinants.
A determinant interval lying wholly below zero then falsifies the route; an
interval wholly above zero proves the fixed-event low gate.  Mere positive
floating-point determinants tending to zero decide neither sign.

## 7. Fastest complete falsification procedure

The coordinate-free strengthened event form has a smooth core.  Therefore,
if it has any strictly negative direction, it has a smooth finite-trial
negative direction.  This gives a complete semidecision procedure for strict
failure:

1. use the present scan only to optimize a candidate in the full old-plus-
   collar space, prioritizing the even sector;
2. reassemble its prime and archimedean energies with cutoff-free formulas or
   rigorous Fourier-tail enclosures;
3. bound the Hodge functional calculus with interval rational approximation;
4. certify an upper bound for the complete strengthened Rayleigh quotient.

Any upper bound below zero kills the proposed propagation mechanism without
needing spectral-projection or Schur-limit theorems.  Positive finite trial
values do not validate it.  If this direct witness search survives at high
precision, the next investment should be the two-gap convergence package in
Section 6, beginning with the even block and the medium-sector residual floor.
