# RH-equivalence atlas: mechanisms, not disguises

Status: first-pass literature and mechanism audit, 2026-08-01.

## Purpose

An RH-equivalent statement is not automatically an easier target.  This atlas
scores equivalences by whether their native language supplies structure not
already present in the explicit formula: order, integrality, extremality,
total positivity, or a topology in which one exceptional zero has nonvanishing
size.

The admission test is the six-part rule in
`FAILURE-MECHANISM-SYNTHESIS.md`: carrier, topology, completion, amplifier,
closed limit, and countermodel separation.

## Ranked atlas

Scores run from 0 (absent) to 3 (strong).  `Gain` asks whether one off-line
zero is amplified; `structure` asks whether the formulation contributes a new
proof language; `closure` asks whether the assertion is already global rather
than a limit of finite certificates.

| Rank | Equivalence family | Carrier | Gain | Structure | Closure | Assessment |
|---:|---|---|---:|---:|---:|---|
| 1 | Nyman--Beurling--Báez-Duarte closure | distance from `1` to a dilation span | 2 | 1 | 2 | Demoted: exact inner-factor and dual obstruction is the forbidden-zero Blaschke product; model-space dimension is zero count; `Lp` changes shift the boundary; discrete convergence returns Möbius cancellation. |
| 2 | Nicolas--Robin extremal inequalities | primorial totient ratios or divisor-sum maxima | 2 | 2 | 3 | Demoted after transition audit: primorial monotonicity reduces to Chebyshev error; CA concavity is genuine but does not order the score against Robin's concave barrier. |
| 3 | Li--Keiper coefficients | conformal power sums of completed-zeta zeros | 3 | 1 | 3 | Demoted after fail-fast audit: exceptional amplification succeeds, but moment/difference structure fails and the surviving CND, Toeplitz, and prime-domination laws are restricted Weil/RH criteria. |
| 4 | Speiser derivative-zero criterion | zeros of `zeta'` in the left half of the strip | 2 | 2 | 3 | Supplies geometric critical-point language, but no known independent sign or index prevents the forbidden critical points. |
| 5 | Riesz/Báez-Duarte growth criteria | one entire function or one arithmetic sequence | 2 | 1 | 3 | Excellent diagnostic compression; likely another square-root cancellation estimate rather than a new invariant. |
| 6 | Farey/Franel, Redheffer, and prime-error criteria | discrepancy, determinants, or summatory errors | 1 | 1 | 2 | Low priority: magnitude/averaging formulations repeat coherence-without-mass or Mertens-scale barriers. |

The Weil, Suzuki/de Branges, de Bruijn--Newman, Laguerre, Mertens/Chowla,
zero-spacing, and naive cohomological families are omitted from the active
ranking because this repository has already reduced or stress-tested them.

## 1. Li--Keiper: the leading candidate

With the standard symmetric interpretation over nontrivial zeros,

`lambda_n = sum_rho [1 - (1 - 1/rho)^n]`.

Li's theorem says RH is equivalent to `lambda_n >= 0` for every positive
integer `n`.  The exact normalization is completion-native: the coefficients
are derivatives of `log xi` at `s=1`.

### Why this survives our failure synthesis

For `w_rho = 1 - 1/rho`,

`|w_rho|^2 - 1 = (1 - 2 Re(rho)) / |rho|^2`.

Thus the left member of any off-line functional-equation pair lies strictly
outside the unit circle.  Its `n`th powers grow exponentially and generate the
non-tempered oscillations analyzed by Voros.  This is the opposite of the
local-prime `L2` picture: an exceptional zero cannot fade merely because its
local amplitudes are square summable.

The formulation also has a one-sided order assertion, not a small positive
margin produced by window truncation.  These are real advantages.

### Main danger

Li positivity is closely related to Weil's quadratic functional, so it may be
only a carefully chosen countable family of Weil tests.  The exponential
amplifier proves that RH failure is visible; it does not explain why the
arithmetic side must be nonnegative.  Alternating derivatives of `log xi` and
the Bombieri--Lagarias arithmetic formula contain global cancellation at
increasing order.

### Fail-fast program

1. Audit the exact completed-zeta normalization and prove the conformal
   exceptional-zero amplification lemma, including quartet cancellation.
2. Write `lambda_n = M_n + E_n`, with the pole/gamma main term separated from
   the von Mangoldt contribution, and identify the exact positivity margin.
3. Test whether a finite-difference, Hankel, Toeplitz, Stieltjes-moment, or
   total-positivity representation exists for the *completed arithmetic*
   coefficients.  Any such representation must include the gamma terms
   natively.
4. Construct symmetric completed-entire countermodels with inserted off-line
   quartets.  Reject every proposed positivity mechanism that survives those
   countermodels without using the Euler product.
5. Kill the path if the desired positivity reduces algebraically to Weil
   positivity or to an RH-strength prime-error bound with no additional
   invariant.

Parameterized Li criteria are worth testing inside this program: moving the
base point changes the conformal gain and may reveal a stable moment kernel.
They are not counted as an independent route.

## 2. Nicolas--Robin: discrete extremality

Nicolas uses the primorials `N_k` and the ratio `N_k / phi(N_k)`; Robin uses

`sigma(n) < exp(gamma) n log log n` for every `n >= 5041`.

The latter is equivalent to RH.  In the former family, RH gives the strict
primorial inequality at every stage, while failure gives infinitely many sign
changes.  Robin's reduction to colossally abundant numbers and Nicolas's to
primorials are genuine compression: only arithmetic extremizers matter.

This route contributes exact discrete order and multiplicative extremality,
features absent from local Weil energy.  Its decisive audit is whether the
extremizer transitions yield a monotonic or interlacing invariant stronger
than Mertens' product theorem.  If every proposed argument needs a uniform
bound at precisely the square-root prime-error scale, the formulation is a
disguise, not leverage.

## 3. Nyman--Beurling: constructive but topologically suspect

RH is equivalent to a density/closure statement for spans of dilates of the
fractional-part function in `L2(0,1)`; Báez-Duarte gives a discrete version.
Burnol's quantitative refinement relates the projection defect to a product
over off-line zeros, so the carrier is exact rather than heuristic.

This offers explicit approximants, Gram matrices, dual witnesses, and an
optimization problem.  But our main negative lesson applies directly: RH
corresponds to a distance tending to zero, and all finite-dimensional margins
can collapse.  It stays in the portfolio only if one can find a non-Hilbertian
dual order, exact interpolation law, or integrality phenomenon that prevents
that collapse.  Generic improvements to `L2` approximation rates are not a
new path.

## 4. Secondary equivalences

- **Speiser:** RH iff `zeta'` has no zeros in the left half of the critical
  strip.  This is useful for geometric exploration of level curves and
  critical-point indices.  It becomes promising only if an independently
  signed global degree can be found; local argument-principle bookkeeping is
  merely zero counting in new coordinates.
- **Riesz/Báez-Duarte:** compress RH into sharp growth of an explicit entire
  function or sequence built from reciprocal zeta values.  Use it for rapid
  symbolic and numerical falsification of proposed Tauberian inequalities,
  not as the primary proof route until extra order is found.
- **Farey/Franel, Redheffer, prime-error forms:** retain as a reference shelf.
  Their natural norms and determinants average sparse exceptions or require
  square-root cancellation directly.

## Portfolio decision

The Li, Nicolas--Robin, and Nyman--Beurling fail-fast gates have now been run.  Li supplies an
excellent amplifier but no independent positivity engine.  Nicolas--Robin
supplies arithmetic extremizers, but its transition order collapses to fine
prime error and its variational concavity does not control the shrinking
barrier.  Nyman--Beurling's exact dual and model-space invariants turn out to
be the forbidden-zero Blaschke product and zero count themselves.  All three
are demoted; the portfolio now requires regrouping before another equivalence
is promoted.

The regroup is recorded in `POST-EQUIVALENCE-REGROUP.md`.  Its leading target
is not another scalar equivalence but a negative-square/relative-index census
for the completed screw kernel, followed conditionally by Burnol's local
conductor-commutator calculus and Sonine biorthogonal rigidity.

## Primary literature map

- X.-J. Li, *The positivity of a sequence of numbers and the Riemann
  hypothesis*, J. Number Theory 65 (1997), 325--333.
- A. Voros, *Sharpenings of Li's criterion for the Riemann Hypothesis*, 2005.
- J. C. Lagarias, *Li coefficients for automorphic L-functions*, 2004.
- J.-L. Nicolas, *Petites valeurs de la fonction d'Euler*, J. Number Theory
  17 (1983), 375--388.
- G. Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse
  de Riemann*, J. Math. Pures Appl. 63 (1984), 187--213.
- L. Báez-Duarte, *A strengthening of the Nyman--Beurling criterion for the
  Riemann hypothesis*, 2002.
- J.-F. Burnol, *A note on Nyman's equivalent formulation of the Riemann
  Hypothesis*, 1999.
