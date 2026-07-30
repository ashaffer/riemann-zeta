# Uniform-in-support mechanism: multiplicative transfer, not more windows

Status: research reduction and formalization target, 2026-07-30.  Nothing in
this note proves RH.  Its purpose is to replace the obsolete uniform-floor UPT
template by the weakest propagation statement that would actually suffice,
and to isolate the analytic premise that still has RH strength.

## 1. The corrected target

Let `lambda(L)` be the bottom of the localized Weil form at support `L`, and
let `tau : N -> R` be an increasing cofinal sequence with `tau 0 = L0`.  It is
enough to prove

1. `lambda` is nonincreasing;
2. `lambda(L0) > 0`; and
3. for every `n` there is some explicitly positive `theta n` such that

       lambda(tau (n+1)) >= theta n * lambda(tau n).

Then, for each *fixed finite* `N`, induction gives

    lambda(tau N) >= lambda(L0) * product (n < N) (theta n) > 0.

For arbitrary finite `L`, cofinality gives `L <= tau N` for some finite `N`,
and monotonicity gives `lambda(L) >= lambda(tau N) > 0`.

This uses neither a positive lower bound for all `theta n` nor positivity of an
infinite product.  The factors may decay arbitrarily fast.  That is essential:
the measured margins decay super-exponentially.  The old `PROGRAM.md` UPT
template asked for a prime-independent normalized floor; that is sufficient
but much stronger than the actual logical need.

The abstract finite-product and cofinality argument is now being formalized in
`RHBridge.UniformSupportTransfer`.

## 2. Three sufficient analytic realizations

### 2.1 Relative Glide

On every compact support interval, prove a one-sided logarithmic derivative
bound

    D+ lambda(L) >= -G(L) * lambda(L),     G in L1_loc.

Gronwall gives

    lambda(t) >= exp(-integral_s^t G) * lambda(s),

which supplies a positive step factor.  An equivalent finite-difference form
is enough; differentiability of the lowest eigenvalue is not logically
required.

The existing Glide theorem has only an additive estimate

    lambda(s) - lambda(t) <= C / log(1/(t-s)).

That proves continuity but cannot protect a margin that is arbitrarily smaller
than the error term.  Upgrading “absolute error” to “error proportional to the
current form/margin” is the substantive new lemma.

### 2.2 Relative form transfer

Let `D_(s,t) : H_t -> H_s` be the norm-preserving dilation to the smaller
window.  A form-level estimate

    Q_t(f) >= theta(s,t) * Q_s(D_(s,t) f),     theta(s,t) > 0,

immediately gives the corresponding bound for the lowest eigenvalues.  This is
stronger than a minimizer-only Relative Glide inequality, but avoids spectral
regularity and is especially suitable for Lean.

### 2.3 Support-extension Schur transfer

There is another exact algebraic route that reuses the already formalized
FULLINF two-block theorem.  Embed `H_s` isometrically into `H_t` by zero
extension and write

    H_t = U + W,    U = image(H_s),    W = U^perp.

Support consistency gives `Q_t` restricted to `U` equal to `Q_s`.  Suppose

    Q_t(u) >= beta * ||u||^2,
    Q_t(w) >= d    * ||w||^2,
    |B_t(u,w)| <= c * ||u|| * ||w||,

with `beta > 0`, `d > 0`, and the strict Schur condition

    c^2 < beta*d.

Then one explicit new margin is

    gamma = (beta*d - c^2) / (2*(beta+d)) > 0.

Indeed `gamma < beta,d` and

    (beta-gamma)*(d-gamma) - c^2
      = (beta*d-c^2)/2 + gamma^2 > 0.

`FullInfTransfer.starProjection_strict_lower_bound` then proves
`Q_t(f) > gamma*||f||^2`.  Iterating with `beta` equal to the previously
proved coercive bound gives a positive lower-bound recursion directly.  If
`beta=lambda(s)` is used, `theta=gamma/beta` is exactly a factor of the type in
Section 1.  No uniform determinant margin is needed; every finite stage merely
needs a strict determinant.

This formulation identifies a concrete analytic target:

> For every support extension, prove an edge-sector floor and a polarized
> central/edge bound whose squared cross constant is strictly below the old
> margin times the edge floor.

The determinant condition is where relative, rather than absolute, control
enters.  Since `beta` becomes extremely small, a bound on `c` independent of
`beta` cannot work.

There is an important domain caveat.  The original archimedean form is
unbounded, so its central/edge cross term need not admit a finite `L2` operator
bound for the sharp support projection.  The theorem must therefore be applied
either to a bounded lower-comparison form (as in FULLINF's clipped-symbol
argument), or with cross estimates in the common form norm.  Whether the hard
central/edge split satisfies the required strict determinant is a falsifiable
analytic question, not an assumption to hide in the formal wrapper.

## 3. Why simple prime-by-prime perturbation cannot work

Let `a < u < 2a` and consider the entering autocorrelation

    C_u(f) = integral f(x) conjugate(f(x+u)) dx

on `L2(-a,a)`, with functions extended by zero.  Put
`E = (-a,a-u)` and let `J` translate `L2(E)` onto `E+u`.  These two intervals
are disjoint.  For any unit `g in L2(E)`, set

    f_plus  = (g + Jg)/sqrt(2),
    f_minus = (g - Jg)/sqrt(2).

Then `||f_plus|| = ||f_minus|| = 1` and

    C_u(f_plus) = 1/2,      C_u(f_minus) = -1/2.

Thus the entering-prime operator has fixed positive and negative norm on
infinite-dimensional subspaces for every `u < 2a`, however close `u` is to the
threshold.  It is indefinite, infinite-rank, noncompact, and does not converge
to zero in `L2` operator norm as the edge slivers shrink.

Continuity of the restricted form is not contradicted.  Concentrating unit
mass into a sliver of width `epsilon` costs logarithmic analytic energy, so
bounded-energy near-minimizers have autocorrelation of order at most
`1/log(1/epsilon)`.  The current Lemmas B--E use exactly this fact.  They give
absolute control, not control relative to a margin as small as `10^-30` and
beyond.  A successful proof must exploit the Euler--Lagrange equation,
factorization, or an equivalent near-kernel rigidity statement; operator-norm
continuation is ruled out.

The algebraic identity

    -2*w*Re <f,T_u f> = w*||f-T_u f||^2 - 2*w*||f||^2

also suggests viewing the full prime sum as a nonlocal translation Dirichlet
energy minus a killing term.  A uniform proof in this language would be a
nonlocal Poincare/factorization inequality for the *combined* arithmetic and
archimedean form, not positivity of each prime update.

## 4. Qualitative alternative: exclude finite-support kernels

Suzuki proves unconditionally that the lowest eigenvalue `lambda_a` of the
localized Weil operator is continuous in `a`, positive for sufficiently small
`a`, and attained.  He records the consequence, originally due to Yoshida:

    RH iff Q_W^a is nondegenerate for every a > 0.

The reason is exact.  If RH fails, `lambda_a < 0` for some finite `a`; continuity
from the small-`a` positive regime forces `lambda_a = 0` at an intermediate
support.  Hence a qualitative uniform mechanism could instead prove that the
Friedrichs operator `A_a` (equivalently its localized screw-kernel form) has
trivial kernel for every finite `a`.

This avoids quantitative lower bounds, but it is not known to be easier and is
itself RH-equivalent.  Suzuki explicitly notes that controlling the relevant
parameter as `a` varies requires detailed control of the prime contribution
beyond his fixed-`a` arguments.  See M. Suzuki, *Weil's quadratic form via the
screw function*, arXiv:2606.09096, especially Theorems 1.3--1.4 and the
discussion following Corollary 1.6:
https://arxiv.org/abs/2606.09096.

The semilocal Sonin spaces of Connes--Consani--Moscovici are stable when places
are added, but the published stability statement is not a positivity-transfer
theorem for the localized Weil forms:
https://arxiv.org/abs/2310.18423.

## 5. Exact Lean boundary after the p=2 certificate

The abstract algebra can be kernel-checked now.  A zeta instantiation still
requires all of the following:

1. define the support-indexed localized Weil form and its common form domain;
2. identify the existing p=2 multiplier-plus-pole theorem with that form;
3. define nested interval zero extension and prove support consistency;
4. formalize support monotonicity;
5. prove either Relative Glide, relative form transfer, or the Schur
   edge/cross determinant at every stage.

Items 1--4 are substantial analytic plumbing but conceptually local.  Item 5
is the RH-strength theorem.  More fixed-window certificates can test proposed
constants, but they do not replace it.

## 6. Recommended next attack

Use the Schur formulation as the prime-side experimental and formal interface:

- central block: the already-positive old support;
- edge block: isolate the logarithmically costly new slivers;
- cross block: search for a bound carrying a factor `sqrt(beta)`, first on the
  exact minimizer/eigenspace and then on its low spectral cluster;
- if such a factor appears only after the Euler--Lagrange equation is used,
  package that as the minimizer-level Relative Glide lemma;
- if it does not appear, the two-sliver construction supplies a direct
  counterexample to the proposed estimate before any Lean effort is spent.

This is now the sole large-support target.  Additional numerical windows are
useful only as certificate generators or falsifiers for one of these relative
inequalities.
