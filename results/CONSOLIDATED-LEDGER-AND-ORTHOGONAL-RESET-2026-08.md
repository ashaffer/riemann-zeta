# Consolidated theorem ledger and orthogonal reset

Status: evidence audit and research reset, 2026-08-04.  This document does not
claim RH.  It supersedes the active-path recommendations in the earlier broad
roadmaps, but not their individual proofs, computations, or counterexamples.

## 1. Executive conclusion

The project has produced real mathematics, but its achievements and its RH
progress must be kept in different columns.

The strongest outputs are:

1. a substantial collection of reusable, axiom-audited Lean analysis;
2. an exact Lean theorem identifying the general arithmetic zeta Weil form at
   `a=7/16` with the certified `p=2` form and proving a strict full-domain lower
   bound there;
3. computer-assisted full-space positivity at three small supports, under the
   stated analytic and FLINT-Arb trust base;
4. exact analytic and algebraic no-go lemmas which eliminate broad classes of
   local, finite-order, or purely formal proof mechanisms;
5. a much cleaner understanding of what a successful proof must add.

The project has not proved RH, all-support positivity, determinant convergence
to completed xi, or a new arithmetic exclusion principle for off-line zeros.

The central conceptual correction is this:

> An Euler product, trace formula, functional equation, duality, or exact
> transform is an equality-producing structure.  RH needs an order or
> exclusion structure.  Rewriting the equality does not create the order.

A viable route must therefore supply a second, independently constructed
engine: dynamical contraction, probabilistic correlation, an arithmetic inverse
theorem, or a genuine geometric polarization.

## 2. Claim tiers and current build health

The following vocabulary is used below.

- **Lean-checked:** the current source compiled and `#print axioms` reported
  only `propext`, `Classical.choice`, and `Quot.sound`.
- **Lean-conditional:** the implication compiled, but its axiom audit lists
  named project interfaces for consensus literature.
- **analytic proof:** a complete paper proof is present, but it is not checked
  by Lean.
- **computer-assisted:** a full theorem is claimed only with its numerical
  library, interval, and analytic trust base.
- **diagnostic:** ordinary numerical evidence, with no theorem claim.

### Current source audit

On 2026-08-05 the focused source checks and audits for the following current
files compiled:

- `GeneralZetaWeilForm.lean`;
- `GuinandWeilFormula.lean`;
- `Stage2DefectCharacterization.lean`;
- `CompletedIncidenceComplexNoGo.lean`;
- `CertifiedBaseInterval.lean`;
- `Stage4NormalizedComparator.lean` and its audit.

The first, second, and fourth groups have only the standard Lean axioms on the
theorems listed below.  Stage 2 exposes its Guinand--Weil and Suzuki
closed-domain literature assumptions exactly as intended.  The propagated
base-window bound uses the explicitly declared standard compact-support fact
that translating by at least the support diameter gives zero autocorrelation.
For Stage 4, self-polarization uses only standard axioms; the three convergence
and noncoercivity conclusions expose the same four declared sampling and
zero-counting/zero-free-region literature assumptions as their inputs.

The umbrella now imports both formerly blocked modules.  Focused checks were
run serially; a full umbrella replay was deliberately not attempted on this
memory-constrained host.  The Stage-4 checks peaked around 6.5 GiB RSS, while
individual generated certificate chunks peaked around 8.5 GiB, so these are
not safe parallel build targets on this machine.

## 3. The new theorem ledger

### 3.1 General logarithmic zeta form and the certified base endpoint

`GeneralZetaWeilForm.lean` now supplies, with no project axioms:

- the intrinsic logarithmically weighted Fourier form domain;
- closure of that domain under zero, addition, and real scalar multiplication;
- its packaging as a real submodule;
- the finite active-prime-power set and its monotonicity in support;
- the exact old-plus-new prime-shell identity;
- the pole, archimedean, prime-power, and total arithmetic Weil forms;
- the exact active set `{2}` at `a=7/16`;
- exact identification of the general form at that support with the previously
  certified `p=2` time-domain form.

The principal endpoint is

`GeneralZetaWeilForm.weilForm_seven_sixteenths_strict_lower_bound`:

`(22699/10^9) ||f||^2 < Q_(7/16)(f)`

for every nonzero vector in the logarithmic form domain.  The current axiom
audit reports only the standard Lean axioms.

This closes the former *definition/specialization* gap at the `L=7/4`
endpoint.  It does not by itself prove the zero-sum explicit formula in Lean or
say anything about unbounded support.  As a novelty claim, the safe wording is
“a kernel-checked local positivity theorem for the explicitly defined
arithmetic zeta Weil form”; priority against all formal and computer-assisted
literature still needs expert review.

`CertifiedBaseInterval.lean` propagates this same strict constant to every
`0 <= a <= 7/16` by isometric zero extension and exact cancellation of
not-yet-active prime terms.  Its smooth compact-support bridge identifies the
selected interval representative, after zero extension, with the original
global function almost everywhere and identifies their pointwise Fourier
transforms.  The propagation is conditional only on the declared standard
compact-support autocorrelation lemma noted in the source audit above; it does
not propagate beyond the certified endpoint.

### 3.2 Logarithmic derivative and right-contour infrastructure

The current `GuinandWeilFormula.lean` proves, with only standard Lean axioms:

- positivity of the analytic multiplicity of a nontrivial zeta zero;
- local factorization of zeta at such a zero;
- the logarithmic-derivative principal-part identity;
- the von Mangoldt Dirichlet series on the right half-plane;
- decomposition of the completed-zeta logarithmic derivative into gamma and
  zeta terms;
- the gamma logarithmic derivative in terms of digamma;
- the reflected right/left-contour identities;
- weighted Fourier--Laplace `L1`/`L2` membership;
- weighted Plancherel and the centered vertical-line/autocorrelation identity;
- smooth compact-support transform decay.

This is genuine reusable analytic scaffolding.  It is not yet the full
Guinand--Weil equality: the global contour limit and zero sum are still
provided through the explicit, unconditional `GuinandWeilLiterature`
interface when needed elsewhere.

### 3.3 Higher differentials cannot repair degree zero

`CompletedIncidenceComplexNoGo.lean` proves, with only standard Lean axioms,
that once the primary differential `d_0` is fixed,

`degreeZeroHodgeEnergy(d_0,d_1,x)=||d_0 x||^2`

is independent of every later differential.  Thus adding a square-zero
`d_1` can reorganize degree-one cohomology but cannot improve the shifted
degree-zero form.  Its positivity is exactly the original relative Poincare
inequality.

The mathematics is elementary, but it closes a recurring false escape hatch:
higher categorical structure does not repair the RH-facing degree unless it
changes the primary map, the degree where the Weil object lives, or the
polarization itself.

### 3.4 Fixed finite places are eventually indefinite

For any fixed finite prime set `P`, the pole-zero subspace of the standard
semilocal form has Fourier multiplier

`M_P(t) = -log pi + Re psi(1/4+i t/2)`

`         - 2 sum_(p in P) log p sum_(m>=1) p^(-m/2)
                                      cos(m t log p)`.

At zero, `M_P(0)<0`.  For a nonzero smooth compactly supported `phi`, set

`phi_R(x)=R^(-1/2)phi(x/R)`,

`v_R=(-partial_x^2+1/4)phi_R`.

Then `vhat_R(+-i/2)=0` exactly and

`Q_P(v_R)/||v_R||^2 -> M_P(0)<0`.

Meanwhile `M_P(t)->+infinity` because the digamma term grows logarithmically
and the finite-prime oscillation is bounded.  Hence every fixed finite-place
form is genuinely indefinite on sufficiently large compact supports.

This is an analytic proof, not presently a Lean theorem.  The `{2,3}` case and
normalization are recorded in `TWO-PRIME-INFINITY-FAIL-FAST.md`.

### 3.5 Positive-trace gluing has a precise finite obstruction

Two elementary algebraic results sharpen the categorical audit.

First, let `tau` be a faithful finite trace and `0<=P,Q<=1`.  If

`tau(P)=tau(P^2)`, `tau(Q)=tau(Q^2)`, and `tau(PQ)=0`,

then `P,Q` are orthogonal projections.  Therefore a positive-trace model using

`-tau log(1-z_2 P-z_3 Q)`

cannot both saturate the first two pure Euler moments and delete the first
mixed moment except by separating the local sectors.

Second, if `U_2,U_3` are commuting invertible finite matrices and a trace or
supertrace `L` kills `L(U_2^m U_3^n)` for all `m,n>=1`, then finite-dimensional
invertibility expresses the identity as a polynomial in positive powers and
forces all pure moments and `L(1)` to vanish too.

These are proved in the ordinary mathematical sense in the two-prime audit,
but have not been formalized in Lean.  Their scope matters: they do not rule
out noncommuting, infinite, signed, non-type-I, or differently organized
models.

The structural lesson is stronger than the bare no-go:

> The signed Lefschetz trace and the positive polarization must be different
> pieces of structure.  Asking one faithful positive trace to perform both
> jobs forces trivial block locality.

This is exactly how successful function-field cohomology is organized: the
alternating trace gives the explicit formula, while a separate Hodge
polarization controls eigenvalues.

### 3.6 What the new computation does and does not prove

The fixed `{2,3}` Ritz form becomes negative just after the prime 5 activates,
while the same finite section with every active prime remains positive:

| `L` | fixed `{2,3}` | all active primes |
|---:|---:|---:|
| 3.270 | `-1.48e-5` | `+2.51e-5` |
| 3.400 | `-6.36e-2` | `+2.34e-5` |
| 4.000 | `-1.50e-1` | `+1.33e-7` |

This is a diagnostic.  It suggests that the new prime repairs an old negative
direction; it is not a proof of positivity at any displayed support.

### 3.7 What normalized Stage-4 comparators establish

`Stage4NormalizedComparator.lean` proves the self-polarization identity
`weilCross a f f = weilForm a f` without project axioms.  Conditional on the
four declared Stage-4 sampling and zeta-counting literature inputs, the Weil
values of a certified comparator family tend to zero.  Unit normalization
then makes its Rayleigh values tend to zero and rules out a strictly positive
uniform coercivity constant on that family.

This is not an operator-domain construction, a residual-norm estimate, or a
Weyl-sequence theorem, and it has no direct RH conclusion.

## 4. Consolidated reusable contributions

The clearest outputs suitable for separate mathematical or formal-methods
presentation are the following.

| Package | Human-facing endpoint | Mathematical novelty |
|---|---|---|
| finite simple-pole residue infrastructure | remove finitely many simple principal parts, obtain one entire remainder, and recover finite residue sums on circles/rectangles | classical theorem; finite regularization may complement active mathlib residue PRs, while the rectangle theorem overlaps them |
| digamma series and Gauss kernel | general two-point digamma series and positive vertical-line integral with logarithmic bounds | classical/folklore; formal package appears useful |
| arbitrary-interval Legendre `L2` theory | complete orthonormal basis, Parseval, finite projections, exact plane-wave coefficients | classical; substantial formalization |
| autocorrelation Plancherel | real-line cross-correlation and Wiener--Khinchin with the exact Fourier normalization | classical; reusable formal bridge |
| compact-support Fourier--Laplace theory | entirety and exponential-type bounds from finite-interval `L2` data | classical; reusable formal bridge |
| quantitative smooth cutoff | exact two-sided cutoff, derivative formula, and scaled slope bound | classical construction; reusable API |
| certificate algebra | exact `LDL^T` perturbation certificate and optimal scalar two-block coercivity constant | generic verified-numerics infrastructure |
| local Weil endpoint | strict full logarithmic-domain positivity at `L=7/4` for the explicitly defined arithmetic form | potentially novel formal/computer-assisted theorem; review needed |
| effective glide theorem | attained margin, monotonicity, and an explicit threshold-safe logarithmic continuity modulus | qualitative result has prior art; explicit refinement may be project-new |

None of the classical rows is a new mathematical discovery merely because it
is new to mathlib.  They remain worthwhile contributions.

## 5. Results that must not be promoted

The following remain conditional, computational, or open:

- the full Guinand--Weil zero-sum equality inside Lean;
- propagation of certified positivity beyond `a=7/16`;
- an unconditional operator-domain or Weyl-sequence upgrade of the normalized
  Stage-4 comparator result;
- positivity at the displayed post-5 supports;
- all-support positivity or nondegeneracy;
- CCM/Suzuki determinant convergence to completed xi;
- parity ordering and comparator/ground-state alignment;
- the envelope law and family universality;
- the Lee--Yang GHS scan beyond its status as a numerical necessary-condition
  check;
- every claimed exclusion of an actual off-line zeta zero.

The software-assisted full-space bounds through `L=749/250` remain genuine
local theorems only under their documented FLINT-Arb and analytic trust base;
the later two are not Lean theorems.

## 6. The common anatomy of the failed paths

The many branches compress to five failures.

### 6.1 Detector without engine

Li coefficients, Nyman--Beurling model spaces, Nevanlinna negative squares,
Sonine reflection, shifted-xi Schur kernels, and Weil signatures all detect an
off-line zero very well.  None supplies an arithmetic reason for its detector
to vanish.

### 6.2 Equality mistaken for order

Poisson summation, Mobius cancellation, functional equations, exact trace
formulas, duality, and categorical composition explain identities and signs.
They do not imply a positive metric.  When positivity was inserted formally,
it was usually RH or an equivalent Hermite--Biehler/Weil statement.

### 6.3 Local positivity destroyed by completion

Individual Euler atoms can be positive or contractive after normalization.
The exact zeta object also contains scalar counterterms, gamma terms, poles,
and renormalization.  Those global subtractions remove the local order.
Fixed-place broad bumps make the obstruction exact.

### 6.4 Finite information misses a remote exceptional zero

Finite Taylor/EFT inequalities, GUE statistics, density-one results, finite
Jensen data, and cryptographic average-case tests survive the insertion of a
sufficiently remote or zero-density off-line quartet.  An RH mechanism must be
infinite-order or carry a quantized invariant which arithmetic can compute.

### 6.5 Limits carry the missing theorem

Self-adjoint finite approximants, real-zero polynomials, finite positive
windows, and semilocal traces do not determine their global limit.  Tightness,
compact-local convergence, domain control, and no escape at infinite height
are not technical cleanup; they carry the global content.

These failures imply a five-part admission test for future proposals:

1. construct the object without using zeta's zero locations;
2. include primes, gamma, and poles before claiming a sign;
3. identify a separate exclusion engine, not merely a detector;
4. show sensitivity to a single arbitrarily high off-line quartet;
5. state the global limit/no-escape theorem at the beginning.

## 7. The control path: the 5-event rescue

The best continuation of the existing Weil program is not mathematically
orthogonal, but it is a valuable control experiment.

At a support just above `2 log 5`, split the fixed `{2,3}` form into its
negative spectral subspace `E_-` and complement `E_+`, then write the complete
`{2,3,5}` form in blocks

`[ A  B ]`

`[ B* D ]`.

The sharp finite-stage theorem is:

- `A>0`: the 5-event correction repairs the old negative sector;
- `D>0`: it does not destabilize the complement;
- `||A^(-1/2) B D^(-1/2)||<1`: the repaired sector and complement remain
  compatible.

The prime-5 update is indefinite on the whole ambient space, so global Loewner
positivity is the wrong target.  This block theorem is finite and falsifiable.
Success would explain one event, not RH; uniform repetition would recover the
global difficulty.

## 8. A genuinely orthogonal research portfolio

The following paths use different primary objects and different exclusion
engines.  None is promoted merely because it is equivalent to RH.

### Path A: a virial identity for the Farey transfer operator

Bonanno's generalized Farey operator gives an exact non-Weil detector in a
specified **singular boundary class**: a fixed function with `c=0` and `b!=0`
exists exactly when `2q` is a nontrivial zeta zero (apart from the stated
exceptional parameter).  This is not an ordinary `L2` eigenvector: the same
fixed equation also has a Maass branch, while the zeta branch contains a
non-square-integrable `t^(-1)` cusp component.  RH becomes the claim that this
boundary cancellation occurs only when `Re q=1/4`.

The proposed new engine is a dissipative or virial identity derived from the
Bessel-kernel realization, not from zeta zeros:

`(4 Re(q)-1) E_q(f) = boundary_q(f)`.

The first fail-fast task is to compute the adjoint of the Bessel operator in a
fixed, `q`-independent Hilbert or Krein space and derive the exact real-part
identity for an eigenfunction.  The route survives only if

- `E_q(f)>0` follows from the operator geometry;
- the admissible eigenfunction class forces the boundary term to vanish;
- neither statement assumes the desired zero location.

If the metric depends on `q` in a way fitted to the eigenfunction, or the
boundary term is sign-indefinite, kill the path immediately.  This is the
highest-priority orthogonal gate because the detector is already exact and the
adjoint calculation is finite work.

There is a known dynamical hazard to expose at the start: the Farey map has an
indifferent fixed point and corresponding continuous/essential spectrum, so a
naive Lasota--Yorke spectral-gap claim cannot be true.  An induced Gauss-map
operator or a renormalized scattering space is mandatory.  If the exact virial
identity fails but the induced operator admits a resolvent estimate for one
fixed `Re q >= 1/4+epsilon`, that would still give a meaningful partial
zero-free half-plane.  The Riemann zeros enter the modular surface through its
scattering coefficient, not through the self-adjoint cusp spectrum; confusing
that coefficient with Mayer's Selberg determinant would merely hide the same
zero-free problem.

Primary anchor: C. Bonanno, *On the Generalised Transfer Operators of the Farey
Map with Complex Temperature*, <https://doi.org/10.3390/math11010134>.

**Follow-up resolution, 2026-08-04.**  This fail-fast gate is now closed.  The
fixed-metric adjoint leaves a nonzero singular source.  The canonical
Knapp--Stein operator has the Weyl symmetry `q -> 1-q`, not the arithmetic
reflection `q -> 1/2-conj(q)`; the Casimir eigenvalues rule out the latter as a
principal-series intertwiner.  After automorphization its boundary scalar is
exactly `Lambda(2q-1)/Lambda(2q)`, so the desired pole-free positivity would
already contain the RH obstruction.  See
`results/FAREY-VIRIAL-AND-PRIME5-CONTROL-2026-08.md`.

### Path B: a super-square-root inverse theorem for multiplicative resonance

An off-line zero of zeta, hence a pole of `1/zeta`, produces a smoothed,
twisted Mobius resonance of size `x^beta`, with `beta>1/2`.  Random
multiplicative behavior lives near the square-root scale.  The missing
arithmetic engine would say that persistent power-saving failure above that
scale forces pretence to a character times `n^(it)`, which Mobius cannot
sustain prime by prime.

The route has two deliberately separate gates.

1. **Residue-to-density gate:** prove that one off-line zero creates
   `x^(1/2+delta)` resonance on a log-syndetic family of scales for one
   bounded-complexity smoothing, rather than only on an arbitrarily sparse
   subsequence after cancellation by other zeros.
2. **Inverse gate:** prove that such log-syndetic super-square-root resonance
   forces bounded pretentious distance.

Our earlier entropy and random-sieve failures show exactly why Gate 1 is
essential.  If complex-analytic residue theory supplies only sparse `Omega`
peaks, or deterministic nonpretentious countermodels satisfy the same
hypothesis, prune the route.

Primary anchors: Granville--Soundararajan's pretentious framework
<https://arxiv.org/abs/math/0608407> and the sharp Halasz theorem
<https://arxiv.org/abs/1706.03755>.

**Follow-up resolution, 2026-08-04.**  The first gate was understated but the
two-gate route is now pruned.  Pintz proves that one zero
`rho=beta+i gamma` forces both signs of `M(x)` at size `x^beta` in every
window `[Y exp(-5(log_2 Y)^(3/2)),Y]`: this is near-syndetic in log scale, not
an arbitrary sparse `Omega` sequence, but it still has growing rather than
constant log gaps and is a sharp-cutoff statement.  More decisively, the
inverse gate is false even if resonance is granted at every large scale.
For `f_z(n)=mu(n)^2 z^omega(n)`, `|z|=1`, `z!=-1`, Selberg--Delange gives
`sum_(n<=x) f_z(n) ~ C_z x(log x)^(z-1)`, while its pretentious distance from
every fixed character twist diverges.  The phase `z` may approach `-1`
arbitrarily closely; at exactly `-1`, `1/Gamma(-1)=0` and the family becomes
`1/zeta`, a singular endpoint.  Any surviving theorem must therefore exploit
the exact Mobius Euler factor and is no longer a density-driven general
inverse theorem.  See `results/MOBIUS-RESIDUE-TO-DENSITY-FINAL-2026-08.md`.

### Path C: a genuine Lee--Yang thermodynamic inverse problem

Seek explicit finite ferromagnetic systems `Z_N(h)`, built from theta or prime
data without using xi's zeros, such that their normalized partition functions
converge locally uniformly to the rotated completed xi function.  Lee--Yang at
finite `N` plus Hurwitz would then give the zero location.

The GHS third-cumulant test has passed a numerical scan, so the next gate must
be stronger.  Before proposing a Hamiltonian, solve the finite inverse problem:

- impose the exact first several xi cumulants;
- impose Griffiths/GKS/GHS and Lee--Yang moment-cone constraints;
- require nonnegative couplings and projective consistency under marginalizing
  the last prime/spin;
- require a tightness bound strong enough for local-uniform partition-function
  convergence.

An infeasible exact or interval semidefinite moment problem kills the natural
ferromagnetic class.  A feasible fit is not evidence for RH unless the
couplings are generated by an arithmetic rule independent of the target
coefficients.

Primary anchor for nontrivial Lee--Yang closure and its limitations:
Newman--Wu, <https://arxiv.org/abs/1708.08820>.

**Follow-up resolution, 2026-08-04.**  The final defensible finite inverse-cone
test is complete.  Arb certifies the Newman reciprocal-zero Stieltjes
localizers through 40 log moments and dimension 20; the general Lee--Yang
shadow survives, which is only finite RH consistency.  A genuinely stronger
independent weighted-Rademacher cone is killed by two negative dimension-16
Hankel determinants.  The audit also found that the proposed combined cone
was ill-posed: strongly Rayleigh and ferromagnetic GKS constraints have
opposite correlation signs, stable polarization is equivalent to the original
univariate stability, and diagonal Taylor data cannot determine nonnegative
multivariate couplings or projective consistency.  The broad interacting path
is parked unless an explicit prime-and-gamma Hamiltonian is supplied.  See
`results/LEE-YANG-INVERSE-CONE-FINAL-2026-08.md`.

### Path D: cyclotomic cohomology rather than decorative categorification

Topological Hochschild/cyclic homology already contains genuine cyclotomic
Frobenius maps and is connected to zeta special values and functional-equation
shadows.  The new question is whether it can supply the missing *global
spectral* object for `Spec Z`, not merely another special-value formula.

The first gate is a finite but nontrivial Lefschetz calculation.  Construct a
single graded object whose signed trace recovers, with predetermined
normalization,

- the `p` and `p^2` von Mangoldt coefficients;
- compatibility under adjoining a second prime;
- the archimedean correction through a real realization;
- no mixed `p^a q^b` primitive term in the final trace.

Only after this trace gate passes should one seek a separate cup/star pairing
with `Theta^dagger=1-Theta`.  The positive pairing must not be the signed trace
and must not be fitted after seeing the spectrum.

If the construction remains a product of independent `p`-complete theories,
recovers only integer special values, or lacks a global real/cross-place cup
product, park it.  This is the highest-upside and longest-horizon path.

Primary anchors: Morin's THH/TC zeta-value construction
<https://arxiv.org/abs/2011.11549> and Connes--Consani's arithmetic site
<https://arxiv.org/abs/1405.4527>.

**Follow-up resolution, 2026-08-04.**  The narrow finite one-trace gate is
closed; the general path remains open but unconstructed.  Hesselholt's local
finite-field determinant supplies genuine pure prime-power traces.  Their
direct sum recovers the Euler product but adds no cross-place geometry.
Tensor/Fock gluing has mixed raw states, yet a connected logarithm can delete
them while a distinct Hilbert pairing remains positive; this is not a no-go.
Cayley--Hamilton rules out only finite commuting invertible models that demand
one linear trace kill all raw mixed moments while retaining pure ones.  Current
special-value theories supply the real place through a separate complex
rather than a global positive Frobenius object.  See
`results/CYCLOTOMIC-TWO-PRIME-TRACE-FINAL-2026-08.md`.

### Path E: proof-theoretic calibration as a sidecar

Lagarias gives an elementary universal inequality equivalent to RH, so RH has
a `Pi^0_1` presentation: a false statement has a finite standard witness.
This sharply constrains, but does not rule out, independence from ZFC.

The useful first task is not to speculate about large cardinals.  Formalize a
primitive-recursive verifier for a Lagarias-equivalent inequality and prove its
equivalence to the analytic RH statement over an explicitly weak base theory.
Then determine which parts of the current analytic development genuinely need
stronger axioms.

If RH were independent of a sound theory in this presentation, it could only
be true but unprovable there; a standard false witness would yield a finite
refutation.  Establishing such independence is not expected to be easier than
RH and would not provide an ordinary ZFC proof, so this receives a small,
foundational allocation rather than becoming the main program.

Primary anchor: Lagarias, *An Elementary Problem Equivalent to the Riemann
Hypothesis*, <https://arxiv.org/abs/math/0008177>.

## 9. Allocation and kill order

The recommended order is based on information gained per unit effort, not on
optimistic RH probabilities.

1. **Farey adjoint/virial gate -- completed and pruned.**  The canonical
   nonlocal continuation exposes the zeta scattering quotient.
2. **Prime-5 rescue block -- finite control completed.**  A generated Lean
   theorem kernel-checks robust full positivity, old negativity, and repair on
   one exact witness.  It does not address refinement or uniform support.
3. **Lee--Yang finite inverse cone -- completed.**  The independent/product
   class is pruned; the general univariate cone survives but supplies no
   interacting Hamiltonian or independent exclusion engine.
4. **Mobius residue-to-density lemma -- completed and pruned as a two-gate
   route.**  Pintz already beats the sparse-scale barrier up to growing
   `O((log log X)^(3/2))` log windows; the proposed general inverse theorem is
   false even under every-scale resonance.
5. **Cyclotomic finite one-trace gate -- completed.**  Direct sums reproduce
   the known Euler product, and the narrow raw-moment architecture is
   impossible.  Connected trace plus a separate polarization remains an open,
   long-horizon program with no all-place construction.
6. **Proof-theory formalization.**  Maintain as a low-cost sidecar.

Do not reopen generic canonical systems, finite graphs, GUE statistics,
prime-by-prime positive updates, higher-differential repairs, stable Jensen
polarizations, or topological heat-flow indices without a new independent
engine.  The repository already contains the corresponding countermodels or
circularity audits.

## 10. Bayesian interpretation

The local formal theorem and reusable infrastructure materially increase
confidence that the program's normalizations and finite-window claims are
real.  They do not materially increase the probability of RH being solved by
the present positivity-propagation mechanism.

The negative results are nevertheless valuable Bayesian progress: they remove
large, tempting regions of search space and identify the exact missing type of
structure.  The Farey gate has since failed for a precise circularity reason,
while the certified prime-5 rescue succeeded only as a finite control and did
not supply uniform propagation.  The next substantial update should come only
from one of these events:

- an arithmetic rule producing a projectively consistent Lee--Yang family;
- a residue-to-density theorem strong enough to trigger a new multiplicative
  inverse theorem;
- a genuine signed-trace/positive-polarization bridge in global arithmetic
  cohomology.

Until one of those occurs, more coordinate changes around the localized Weil
near-kernel should receive essentially no Bayesian credit.
