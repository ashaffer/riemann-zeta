# Suzuki screw-kernel alignment

Status: full identity imported from consensus literature; the prime-ramp
normalization and finite summation have additionally been reduced in Lean to
one elementary two-variable integration-by-parts lemma. Positivity is not
imported.

## Normalization dictionary

| RHBridge | Suzuki 2026 | Match |
|---|---|---|
| support space on `[-a,a]` | `L²(-a,a)` | same support parameter `a` |
| `weilForm a f` | `Q_W^a(f)` | same pole, archimedean, and von Mangoldt normalization |
| ordinary transform `∫f(x)e^{-2πiξx}dx` | angular transform `∫f(x)e^{izx}dx` | `z=-2πξ` |
| prime shift `log n` | prime shift `log n` | identical logarithmic coordinate |
| `log n < 2a` active convention | `n ≤ exp(2a)` | equality is harmless on the smooth core because endpoint overlap vanishes |
| `quarterDigammaReal 0` | `ψ(1/4)` | identical real value |

Suzuki defines the explicit continuous even function

`g(t) = pole part + prime ramp part + digamma/Lerch part`

and proves on `C_c^∞(-a,a)` that

`Q_W^a(v) = ∫∫ g(x-y) v'(y) conjugate(v'(x)) dx dy`.

RHBridge's smooth core is real-valued, so conjugation disappears. The explicit
function, kernel form, and equality are encoded in
`RHBridge/SuzukiScrewLiterature.lean`.

The prime component is encoded separately in
`RHBridge/SuzukiPrimeRamp.lean`. For each `n`, its kernel is exactly

`Λ(n) / sqrt(n) * max (abs(t) - log(n)) 0`.

Assuming only the single-ramp integration-by-parts identity, Lean proves that
its form is `-primePowerTerm`, including both translates and the factor `2`.
Finite summation then proves

`primeRampForm φ = -primeTerm a φ.toTestSpace`.

Thus no arithmetic normalization or summation issue remains hidden in the
Suzuki alignment. The remaining local axiom is the analytic statement
obtained by splitting the integration square along
`x-y = ±log(n)` and applying FTC on the resulting polygonal regions.

## Assumption boundary

The equality is unconditional. It is a representation of the same indefinite
quadratic form by a continuous kernel.

The following statement is **not** imported:

`g(t-u) - g(t) - g(-u) + g(0)` is positive definite on all real points.

Suzuki's screw-function criterion makes that global positivity RH-equivalent.
Likewise, localized kernel positivity at every `a` is exactly smooth-core Weil
positivity after the alignment theorem; it is a target, not progress by itself.

## What the alignment buys us

1. Distributional Weil positivity can now be attacked through an ordinary
   continuous kernel and derivative test functions.
2. The prime part is visibly a finite sum of ramps
   `(abs(t)-log n)_+`, suggesting spline and conditionally-negative-definite
   decompositions.
3. Suzuki's finite-interval operators and canonical-system tools can be stated
   against exactly the same support parameter and form used by RHBridge.
4. Any proposed positive decomposition can be checked componentwise against
   the arithmetic normalization, preventing a hidden sign or `2π` mismatch.

## Next non-circular lemmas

1. Discharge the isolated single-ramp integration-by-parts axiom by formalizing
   the polygonal-domain split (the arithmetic and finite-sum stages are done).
2. Prove the pole and digamma/Lerch components reproduce the existing pole and
   archimedean terms, shrinking the literature axiom to analytic convergence.
3. Define the localized zero-mean projection `G_a` and the derivative map `D`,
   then prove the abstract identity `B_a = D* G_a D` on the smooth core.
4. Search for a decomposition of `G_a` into an unconditional positive operator
   plus a remainder whose sign is genuinely weaker than RH.

## Primary source

M. Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096,
especially equations (1.3), (1.5), (1.6), and (2.9):
<https://arxiv.org/abs/2606.09096>.
