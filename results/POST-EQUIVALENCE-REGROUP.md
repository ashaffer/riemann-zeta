# Post-equivalence regroup: detectors, engines, and the next research portfolio

Status: synthesis after the Li--Keiper, Nicolas--Robin, and
Nyman--Beurling--Báez-Duarte fail-fast audits; literature scan 2026-08-01.

## Executive conclusion

The three branches did not fail for the same superficial reason, but they did
expose the same architecture:

1. **Li** supplies exponential exceptional-zero gain but no independent
   arithmetic positivity engine.
2. **Nicolas--Robin** supplies exact arithmetic extremizers but no order law
   controlling their vanishing vertical margin.
3. **Nyman--Beurling** supplies exact dual witnesses and even a quantized model
   space, but the invariant is simply the forbidden-zero Blaschke factor or
   zero count.

The literature has largely solved the **detector design** problem.  It has not
solved the **exclusion engine** problem.  Another equivalence should not enter
the active portfolio merely because its statement is elementary, geometric,
or discrete.

## I. Concrete lessons

### 1. Detection and exclusion must be scored separately

An object can detect one off-line zero perfectly and still offer no way to
exclude it.

- Li powers turn it into exponential oscillation.
- Nyman evaluation gives an exact dual obstruction.
- The Nyman model-space dimension counts it with integer multiplicity.
- Robin/Nicolas convert it into infinitely many sign failures.

All four are excellent detectors.  None explains why the Euler product,
completion, or another independently positive structure makes the detector
vanish.

**New rule:** every proposal must display two arrows separately:

`arithmetic/geometric theorem -> engine invariant -> zero exclusion`.

Rewriting the second arrow is not progress on the first.

### 2. Transformations conserve difficulty unless they add a law

Conformal maps, Mellin transforms, extremal reductions, and Hardy
factorizations can amplify or quantize the forbidden signal.  They do not
create a sign, an index computation, or a monotonicity law.

- Li moves local square-summable mass to an exponentially growing conformal
  mode, but its positivity is a restricted Weil test.
- Mellin--Hardy theory turns an off-line zero into a reproducing-kernel
  annihilator, but outerness of the zeta multiplier is RH.
- Colossal abundance gives a concave envelope, but Robin asks for comparison
  with another concave curve.

**New rule:** identify the theorem that is true *because the object is zeta*,
not because it is an arbitrary completed entire function or an arbitrary
Euler product.

### 3. Quantization helps only when arithmetic computes the index

Integer-valued negative index, winding, degree, or quotient dimension is the
right topology for a tiny exceptional zero: a small amplitude cannot erase
one unit.  But the Nyman audit gives the warning in exact form.  The model
space `K_B` has dimension equal to the forbidden-zero count; computing it from
`B` uses the argument principle, while proving it is zero from the arithmetic
side is the original problem.

**New rule:** an index proposal is admitted only with an arithmetic-side
Fredholm pair or homotopy on which the index can be computed without locating
zeta zeros.

### 4. Renormalization is where local positivity dies

The Li prime kernel is oscillatory and pairs with a signed PNT discrepancy.
The Robin transition subtracts two asymptotically equal slopes.  The Weil form
requires prime, pole, and archimedean terms together.  In each case the local
positive pieces become faithful to zeta only after a global subtraction, and
that subtraction removes the order.

**New rule:** never infer global sign from positive Euler atoms before writing
the complete counterterm and archimedean contribution.

### 5. Extremality compresses the test set, not the proof

Primorial and colossally abundant reductions are mathematically meaningful:
they discard irrelevant integers.  But the extremal score remains real-valued
with a margin tending to zero.  The CA envelope's concavity controls slopes,
not its vertical position relative to Robin's barrier.

**New rule:** after an extremal reduction, ask what controls the *height* of
the frontier.  Slope ordering alone is insufficient when the barrier has the
same curvature sign.

### 6. Finite computation is most deceptive at delayed reversals

The Nicolas score decreases at every prime below two million, yet the
literature shows this monotonicity is incompatible with Cramér's conjecture.
Its second differences already change sign tens of thousands of times.  A
long monotone prefix can be an asymptotic cancellation artifact rather than a
law.

**New rule:** numerical monotonicity needs an asymptotic transition theorem or
an explicit stability invariant before receiving Bayesian weight.

### 7. The critical exponent is rigid

Beurling's `Lp` theorem moves the zero-free boundary to `Re(s)=1/p`.
Only `p=2` places it at the functional-equation fixed line.  Moving to a
stronger or non-Hilbert norm either weakens the conclusion or makes the
density statement false because of known critical-line zeros.

**New rule:** changing topology must preserve the symmetry-fixed boundary;
otherwise apparent extra coercivity answers a different question.

## II. Literature results underused by this program

"Underused" here means underused in this repository, not unknown to experts.

### A. Burnol's local conductor and bounded commutator calculus

At every finite or archimedean completion, Burnol realizes the local explicit
formula through the self-adjoint conductor operator

`H = log|x| + log|y|`,

where `x` and `y` are Fourier-dual variables.  Its generalized eigenvalue is
the logarithmic derivative of the local Tate gamma factor.  He also studies

`K = i[log|y|,log|x|]`,

which is bounded, dilation invariant, and has higher-commutator analogues.

**Why this matters:** our program repeatedly decomposed the completed Weil
form into prime and archimedean kernels, but it mostly used quadratic forms.
The commutator retains phase and is insensitive to adding scalar
renormalizations.  It is a plausible raw material for a relative Fredholm or
spectral-flow index in which all places are native.

**Limitation:** Burnol's theorem realizes the local explicit formula, not a
global positive operator whose spectrum is the nontrivial zeros.  A naive sum
of local commutators may be non-Fredholm or have no zeta-sensitive index.

### B. Burnol's complete and minimal Sonine zero systems

Burnol combines co-Poisson summation with de Branges--Sonine spaces and proves
that systems indexed by the zeta zeros are complete and minimal in specified
extended Sonine spaces, with explicit biorthogonal structure.

**Why this matters:** completeness is unconditional and retains the actual
zeros and functional equation.  Minimality supplies canonical dual vectors,
so an off-line quartet cannot be hidden by density or averaging.  This is a
more rigid starting point than trying to invent a Hilbert--Pólya operator from
its desired eigenvalues.

**Limitation:** unconditional completeness also proves that completeness alone
does not locate the zeros.  The missing theorem would be positivity or
unitarity of a reflection metric on the biorthogonal system, and that may be
RH in disguise.

### C. Generalized Nevanlinna functions and finite negative squares

Krein--Langer/Pontryagin theory replaces positive Herglotz kernels by kernels
with exactly `kappa` negative squares.  Zeros or poles of nonpositive type are
then controlled by a quantized negative index.  Suzuki's zeta screw function
already places RH at the `kappa=0` endpoint of this theory, and its finite
window operators are unconditionally trace class.

**Why this matters:** instead of repeatedly trying to prove positivity, first
classify the defect.  A single off-line quartet should create an integer
negative-square obstruction even when its eigenvalue is arbitrarily small.
This directly addresses coherence without mass.

**Limitation:** if the negative index can only be computed from the zero-side
factorization, it repeats the Nyman model-space tautology.  The research value
depends entirely on an arithmetic computation of the index.

### D. The Balazard--Saias--Yor harmonic defect

Their weighted critical-line integral of `log|zeta|` equals a nonnegative sum
of Green/Blaschke contributions from zeros to the right of the line and
vanishes exactly under RH.  Burnol's projection formula is the corresponding
Hardy-space statement.  Later work shows that truncated versions have
nontrivial oscillatory behavior even under RH.

**Why this matters:** this is a nonlinear scalar defect with no cancellation
between forbidden zeros.  It is a useful checksum for any proposed global
index or outer-factor argument.

**Limitation:** a high or near-line zero contributes only
`(2 beta-1)/|rho|^2` at first order.  Fixed-basepoint harmonic defects retain
the collapsing-margin problem; differentiation leads back toward Li-type
oscillation.

### E. Mean-periodicity of zeta boundary terms

Fesenko--Ricotta--Suzuki relate meromorphic continuation and functional
equation of arithmetic zeta functions to mean-periodicity of explicit boundary
functions.  Suzuki also proves unconditional mean-periodicity for the zeta
screw function in suitable spaces.

**Why this matters:** spectral synthesis retains complex exponents and their
multiplicities, rather than averaging them into mass.  It supplies a natural
language for phase-coherent global modes.

**Limitation:** for Riemann zeta, continuation and functional equation are
already known and are compatible with off-line zeros.  Mean-periodicity must
be paired with a new sign or involution theorem to constrain real parts.

### F. A useful no-go result from complete/minimal systems

Burnol's zero systems and the Nyman inner-factor theorem together show that
one can have exact spectral synthesis, complete systems, canonical duals, and
quantized defect spaces without proving RH.  This rules out a broad class of
future claims of the form "the zeros form a complete spectral system,
therefore they lie on the critical line."

## III. Revised active portfolio

### Path 1: Negative-square census for the completed screw kernel

**Objective.** Extend the binary statement "positive or not" to an exact
Pontryagin index and determine whether finite-window negative index stabilizes
to the number of off-line zero pairs in the corresponding conformal region.

**First fail-fast gate.** Prove the abstract zero-side index formula for finite
symmetric zero multisets, then instantiate the arithmetic screw kernel and
check whether its index has any prime-side expression other than minimizing
the Weil form.

**Promotion condition.** An arithmetic relative-index formula stable under
completion and not requiring a uniform spectral gap.

**Prior:** `35%` for a clean index theorem; `8%` for a genuinely independent
arithmetic bridge; below `1%` that this path alone reaches RH.

### Path 2: Adelic conductor-commutator relative index

**Objective.** Use Burnol's bounded local commutators to assemble a global
Fredholm pair whose index can be computed locally and whose nonzero value is
forced by an off-line quartet.

**First fail-fast gate.** Determine domains, summability, and whether the
completed prime/archimedean difference is compact or trace class.  Reject the
path immediately if the proposed index is undefined, identically zero by
symmetry, or just the argument-principle zero count.

**Promotion condition.** A place-by-place index computation with the gamma and
pole terms included from the start.

**Prior:** `15%` for a well-defined nontrivial global index; `2%` for an
arithmetic proof it vanishes; roughly `0.2%` for RH through this route.

### Path 3: Sonine biorthogonal reflection rigidity

**Objective.** Start with Burnol's unconditional complete-minimal zero system
and its canonical dual.  Seek a co-Poisson/Fourier reflection pairing whose
positivity would force each evaluation node to be fixed by
`rho -> 1-conjugate(rho)`.

**First fail-fast gate.** On a finite synthetic off-line quartet, derive the
exact Gram block and determine whether the desired metric positivity is
automatic, false, or precisely Weil positivity.  Only the first option with a
zeta-specific co-Poisson hypothesis promotes the path.

**Promotion condition.** Positivity derived from Fourier support or
intertwining, not assumed as a de Branges/Hermite--Biehler property.

**Prior:** `20%` for a useful rigidity lemma; `3%` for an independent positive
metric; below `0.5%` for RH.

### Reference path: harmonic/inner defect

Use the Balazard--Saias--Yor/Burnol defect as a scalar checksum for the first
three paths.  Do not pursue fixed-weight boundary estimates as a standalone
proof program.

## IV. What not to do next

- Do not move automatically to Speiser, Riesz, Farey, or Redheffer merely
  because they remain in the atlas.
- Do not infer zero location from completeness, spectral realization, or
  self-adjoint models whose boundary condition was fitted using zeta's phase.
- Do not treat positivity of finite Gram matrices as evidence when it is
  automatic from their construction.
- Do not use an integer index unless its arithmetic-side computation is
  independent of zero counting.
- Do not invest in finer finite-window numerics without an asymptotic stability
  theorem at the collapsing scale.

## V. Recommended next checkpoint

Start with **Path 1**, because it fails fastest and determines whether Paths 2
and 3 have a meaningful target.  If generalized Nevanlinna/Pontryagin theory
merely relabels the negative spectrum of the Weil form, stop.  If it yields an
exact stable index with a local trace or commutator formula, immediately test
whether Burnol's conductor calculus computes that index place by place.

This is a narrower portfolio than before, but it is better aligned with the
evidence: the missing object is not another sensitive scalar.  It is an
**arithmetically computable, completion-native, phase-sensitive integer
invariant**.

## Primary literature map

- J.-F. Burnol, *The Explicit Formula and the conductor operator* (1999).
- J.-F. Burnol, *Two complete and minimal systems associated with the zeros of
  the Riemann zeta function* (2004).
- J.-F. Burnol, *Entrelacement de co-Poisson* (2007).
- M. Suzuki, *Aspects of the screw function corresponding to the Riemann
  zeta-function* (2023).
- M. Suzuki, G. Ricotta, and I. Fesenko, *Mean-periodicity and zeta functions*
  (2012).
- M. Balazard, E. Saias, and M. Yor, *Notes sur la fonction zeta de Riemann,
  2* (1999).
- H. M. Bui, S. J. Lester, and M. B. Milinovich, *On Balazard, Saias, and
  Yor's equivalence to the Riemann Hypothesis* (2014).
