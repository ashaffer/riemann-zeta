# Audit of nonlocal zero-mode routes

## 1. Fourier / Wiener--Hopf

Verdict: correct language, but the naive entire-multiplier argument fails.

Compact support makes the Fourier transform `F` entire of exponential type.
However, the localized zero-mode equation is

`P_a A P_a f = 0`,

not the global equation `A f = 0`.  In Fourier variables the support
projection becomes convolution, so one cannot conclude

`Omega(z) F(z) = 0`.

Lean now contains the elementary symmetric block countermodel: an operator
output can be orthogonal to every old-supported test while remaining entirely
nonzero in the complementary collar.  Consequently, zeros or meromorphic
factorization of the scalar symbol alone cannot exclude a localized null
vector.

A legitimate Wiener--Hopf route must factor the **compressed finite-interval
operator**, including its boundary Hankel term and rank-two pole perturbation.
For the zeta symbol this is a logarithmically growing almost-periodic symbol,
outside the simplest rational Wiener--Hopf classes.  Establishing a canonical
factorization with zero partial indices would essentially be a nondegeneracy
theorem, but it is at least a correctly posed target.

## 2. Canonical systems / de Branges

Verdict: structurally best aligned with finite-interval nondegeneracy, but the
identification step carries the hard content.

The unconditional Suzuki kernel identity supplies a continuous localized
kernel.  A canonical-system proof would need an independently positive
Hamiltonian and an injective transform whose norm is exactly the Weil form.
Assuming that the zeta Weyl function is Herglotz, or that the screw kernel is
positive definite, already imports RH-strength positivity.

The useful narrower target is qualitative: construct the finite-interval
canonical relation without positivity, and prove that a zero mode would make
its transfer matrix singular in a way incompatible with determinant one.
This avoids requesting a quantitative spectral margin.  No such determinant
identity is currently present in the repository or isolated as a consensus
literature theorem.

## 3. Total positivity / variation diminution

Verdict: unlikely for the full operator.

Gauss's continuous-delay weight is positive, but a positive mixture of
translation **defects** is not automatically a totally positive kernel.  The
finite prime translations enter with the opposing sign, and the rank-two pole
term is indefinite before combination.  Total positivity of the combined
kernel would directly imply strong sign-regularity and appears stronger than
what the explicit decomposition supports.

The restricted claim also fails numerically after parity reduction.  The
ordered hat-Galerkin Green matrix `Q_L^{-1}` has negative entries at some
supports and negative adjacent `2 x 2` minors throughout the tested range
`L = 1.75, 2, 2.485, 2.996`, at both 21 and 41 basis functions.  In
particular, at `L=1.75`, where all tested Green entries were positive, an
adjacent minor was already negative.  The reproducible diagnostic is
`src/total_positivity_falsifier.py`.

This does not disprove a differently conjugated or transformed sign-regular
kernel, and it bears neither way on RH.  It does retire ordinary total
positivity of the natural finite-element Green kernel as a propagation tool.

## Ranking after audit

1. Canonical-system transfer-matrix nondegeneracy.
2. Finite-interval Wiener--Hopf factorization with boundary/Hankel correction.
3. Restricted resolvent total positivity: falsified in the natural ordered
   hat basis and retired unless a mathematically motivated conjugation appears.

The immediate next construction should be an abstract canonical realization
package that separates unconditional realization, determinant-one evolution,
zeta identification, and positivity.  That will reveal whether a qualitative
zero-mode contradiction can be obtained without assuming the desired sign.

### Zero-parameter mechanism

There is one concrete qualitative advantage.  For `J Y' = z H Y`, the
equation at `z=0` says `Y'=0`, independently of positivity of `H`.  Hence a
zero mode mapped to spectral parameter zero is constant.  Lean proves that
two independent endpoint covectors then force `Y=0`.

This reduces the canonical route to three sharply auditable bridges:

1. construct a canonical first-order realization of the localized Suzuki
   equation without assuming kernel positivity;
2. prove that a Weil zero mode maps to spectral parameter `z=0`;
3. identify its two endpoint conditions and prove their determinant is
   nonzero.

The danger is that step 1 may require a positive Hamiltonian, or that the two
endpoint lines coincide exactly when the localized determinant vanishes.  In
either case the apparent contradiction would merely restate nondegeneracy.

Lean formalizes only the safe algebraic core in `CanonicalZeroMode.lean`: at
zero spectral parameter a canonical state is constant, and two independent
endpoint covectors annihilate only the zero state.  It deliberately does not
postulate the zeta realization or endpoint independence.

### Current Bayesian checkpoint

The three-way exploration has produced two negative results and one sharp
conditional reduction:

* scalar-symbol Fourier continuation is invalid for the compressed equation;
* natural Green-kernel total positivity is numerically false;
* a canonical-system argument would work at zero parameter if and only if an
  unconditional realization supplies two independent endpoint conditions.

Thus the next honest target is not a generic determinant-one argument.  It is
to derive, from the Suzuki integral equation alone, a first-order state and
its endpoint covectors, then compute their determinant.  If that determinant
is merely the localized Fredholm determinant in disguise, the route is
circular and should be stopped; if it simplifies to independently nonzero
data, it is a genuine qualitative nondegeneracy mechanism.

### Finite-interval parameter mismatch

A direct audit of Suzuki's finite-interval construction reveals an earlier
obstruction.  Given the lowest Weil eigenvalue `lambda_a`, the construction
chooses a shift `lambda < lambda_a` and completes the smooth core in the norm

`||v||_T^2 = Q_W^a(v) - lambda ||v||_2^2`.

The symmetric operator subsequently studied is differentiation
`i d/dx` in this shifted Hilbert space.  Its de Branges spectral variable is
therefore the differentiation spectral parameter; it is not the eigenvalue
of the Weil operator `A_a`.  If `Q_W^a(v)=0`, then for a negative shift

`||v||_T^2 = -lambda ||v||_2^2 > 0`.

So a nonzero Weil null mode survives as an ordinary nonzero Hilbert-space
vector and does not become a canonical state at spectral parameter zero.  At
shift zero it would again be null, but then the construction does not provide
a Hilbert norm unless nondegeneracy has already been proved.  Lean records
this exact scalar obstruction in `CanonicalShiftObstruction.lean`.

The elementary endpoint theorem in `CanonicalZeroMode.lean` remains correct,
but it cannot be applied to the Weil zero mode without a new intertwining
identity relating `ker A_a` to the zero eigenspace of a first-order operator.
No such identity is supplied by the cited finite-interval construction.

This demotes the canonical route from an active proof mechanism to a precise
research question: construct such an intertwiner independently of Weil
positivity, or prove that one cannot exist in the shifted model.  Merely
repackaging the shifted de Branges space will not establish nondegeneracy.

### Energy-adjoint follow-up

The fixed-shift self-adjoint-extension theorem itself survives a more careful
domain audit.  The v1 preprint's proof passes from energy-norm continuity to
`L2` continuity in the reversed topology direction, but a Gelfand-triple
Riesz argument repairs it without using shift zero: the deficiency vectors
are `(A_a-sigma I)^-1 exp(+/-x)` for every `sigma<lambda_a`.  See
[`SUZUKI-ENERGY-ADJOINT-REPAIR.md`](SUZUKI-ENERGY-ADJOINT-REPAIR.md).

What does not survive generically is independence from the auxiliary shift.
Equivalent shifted energy norms need not identify the full phase-labelled
extension families by a single boundary-phase relabeling; an exact
Dirichlet-energy family proves this pointwise obstruction, and the
completed-Weil Galerkin shadow shows the same strong phase drift numerically.
This does not compare exact zero sets at one specially selected phase.  See
[`SHIFT-PHASE-COVARIANCE-FAIL-FAST.md`](SHIFT-PHASE-COVARIANCE-FAIL-FAST.md).
Thus the requested new intertwiner must conjugate the adjoint derivatives and
their boundary spaces, not merely identify the underlying Hilbert spaces.

The next audit isolates an intrinsic necessary invariant: an exact unitary
adjoint intertwiner carrying each one-dimensional defect line at `z` to the
line with the same label must preserve normalized Gram magnitudes and
Bargmann triples.  Lean proves this Hilbert-space theorem.  A bounded-memory
completed-Weil Galerkin scan rejects exact cross-window equality; allowing an
affine spectral dilation explains most, but not all, of the residual.  This
does **not** reject selected-extension strong-resolvent convergence, which is
strictly weaker than unitary equivalence of the maximal adjoints.

There is a more decisive obstruction to the natural unshifted limit.  Exact
zero-extension preserves the unshifted Weil form and `L2` norm, so it changes
shifted energy by exactly `(sigma_a-sigma_b)||f||_2^2`.  Moreover, for any
antitone window-floor family on a cofinal support sequence, Lean proves that
a strictly admissible shift sequence tending to zero exists if and only if
all window floors are nonnegative.  Thus a zeta construction cannot obtain
the unshifted global Hilbert space by silently choosing `sigma(a)->0`; that
choice already carries the global Weil-positivity target.  See
[`SUZUKI-PROJECTIVE-KERNEL-CHECKPOINT.md`](SUZUKI-PROJECTIVE-KERNEL-CHECKPOINT.md).

On the range where the independent full-space certificates already give
`A_L>0`, this leaves a canonical safe experiment: fix `sigma=-1/4` rather
than tune toward zero.  The resulting selected-divisor test fits one phase on
alternating Platt/LMFDB ordinates and matches held-out ordinates to distinct
finite roots.  It fails throughout `L<=749/250`, including `sigma=-1` and
both exact symmetry-phase controls, but improves with support and therefore does not reject
the cofinal limit.  See
[`SUZUKI-FIXED-SHIFT-DIVISOR-CHECKPOINT.md`](SUZUKI-FIXED-SHIFT-DIVISOR-CHECKPOINT.md).

The subsequent counting audit isolates the correct order-of-limits question.
For the repaired simple symmetric operator, a monotone lift `Phi_L` of the
boundary phasor counts an extension spectrum by an exact floor difference,
with error less than one from `Delta Phi_L/(2*pi)`.  At fixed support the
characteristic has Cartwright type at most `L/4`, hence only linear
high-energy zero density, but the onset and remainder are not uniform in
`L`.  An explicit escaping-spectrum model proves that arbitrarily small
high-energy gaps can coexist with eventually empty fixed compacts.  The
completed-Weil Galerkin phase instead winds close to `L*T/(4*pi)` on the
tested range.  The live theorem is therefore a support-uniform estimate of
`Phi_L(T)-Phi_L(0)` at fixed `T`, not another fixed-`L` Weyl asymptotic.  See
[`SUZUKI-SPECTRAL-COUNTING-CHECKPOINT.md`](SUZUKI-SPECTRAL-COUNTING-CHECKPOINT.md).

The fail-fast follow-up computes the missing density exactly.  If `rho_L(x)`
is the normalized coherence between the reference defect line and the real
defect line, then

```text
Phi_L'(x)=2/[(1+x^2)rho_L(x)^2],
sigma_theta({lambda})=pi(1+lambda^2)rho_L(lambda)^2,
nu_theta({lambda})=rho_L(lambda)^2.
```

An explicit exact-type Hermite--Biehler family has the full far-tail Weyl law
while its fixed-compact phase converges to the single Cayley factor.  Hence
generic de Branges structure cannot close the fork: the remaining raw-count
theorem is zeta-specific defect-line decorrelation.  Moreover, its reciprocal
raw Clark atoms explain why divergent raw counts alone are not a
strong-resolvent obstruction.  See
[`SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md`](SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md).

The weighted follow-up separates the raw Clark measure from the scalar
spectral measure of a named vector.  For the canonical normalized reference
defect vector, the atom is `rho_L(lambda)^2`, and its Stieltjes transform is
root-free: `m_L(z)=[iH_L(z)-z]/(1+z^2)`.  Generic de Branges data still do not
force tightness: in the explicit exact-type countermodel, all normalized mass
escapes at `alpha=-1`, the zeta parameter in the canonical Frostman gauge.
Moreover, strong resolvent convergence would control these moving finite
Clark vectors only after the comparison embeddings are proved to make them
converge to a fixed ambient vector.

There is also an exact target mismatch.  Even under RH, a fixed shift
`sigma=-c<0` changes the global Fourier measure from the pure zeta-zero sum to
`sum m_gamma delta_gamma+c dt/(2*pi)`.  Thus the canonical fixed-shift limit
has an absolutely continuous component.  Recovering the pure target by
admissible shifts tending to zero is already equivalent to all-window
positivity for the antitone floors.  See
[`SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md`](SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md).

The vector-compatibility follow-up closes that question exactly.  The finite
reference defect vector is the Riesz representative of ordinary Fourier
evaluation `fhat(i)`.  Translation preserves every fixed-shift energy norm
but amplifies this evaluation exponentially, so its Riesz norm diverges and
the normalized finite vectors converge weakly to zero under natural zero
extension.  They cannot converge strongly to the global de Branges kernel.

There is a complementary conditional theorem.  Under RH, group mollification
shows that `C_c^infinity(R)` is a graph core for the global Stone translation
generator.  Every finite self-adjoint extension agrees eventually on that
core, so its compressed resolvents converge strongly for every extension
phase.  The correct fixed-core spectral measures therefore converge
automatically, while raw eigenvalues and moving Clark measures remain
uncontrolled.  This makes strong resolvent convergence phase-blind and shifts
the live target to a stronger characteristic, norm-resolvent, or renormalized
boundary-scattering limit.  See
[`SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md`](SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md).

### Exact continuous-kernel reduction

Suzuki's unconditional finite-interval reduction does give one exact and
useful change of coordinates.  The Dirichlet derivative

`D : H_0^1(-a,a) -> L_0^2(-a,a)`

is bijective, and the Weil Rayleigh quotient becomes the generalized compact
operator problem

`G_a u = lambda K_a u`,  where `K_a = (-Delta_N)^{-1}`.

At `lambda=0`, however, this says exactly `G_a u=0`; the comparison operator
`K_a` disappears.  Thus a nonzero Weil zero mode corresponds bijectively to a
nonzero null vector of the compressed continuous Suzuki operator.  Lean
records this coordinate-invariant kernel equivalence in
`SuzukiKernelZeroReduction.lean`.

This is analytically cleaner but not logically weaker.  The remaining path is
now precise: prove injectivity of

`(G_a u)(x) = P_a integral_{-a}^a g(x-y)u(y)dy`

on mean-zero data at every first-crossing window, using special structure of
the explicit zeta screw function.  Generic compact-operator theory,
determinant-one evolution, and the shifted de Branges construction do not
provide that injectivity.  Any future canonical realization must add an
independent local law for this convolution equation, not merely change its
Hilbert-space norm.

There is one final exact simplification.  Since `P_a` subtracts the interval
average and the input `u` is already mean-zero,

`G_a u = 0  iff  integral g(x-y)u(y)dy = C_u`

for every `x` in `(-a,a)`, with a scalar constant `C_u`.  This projection
algebra is formalized by `removeMean_eq_zero_iff`.  Unlike the discarded
finite-interface picture, differentiating this identity still leaves the
full continuous-delay archimedean contribution.  The next genuine theorem
would therefore be a uniqueness result for compactly supported mean-zero
`u` whose convolution with the explicit zeta screw function is constant on
its support interval.

### Log-elliptic reduction

Near the diagonal Suzuki proves

`g(t) = (1/2)|t| log|t| + A|t| + r(t)`

before the first prime ramp, with `r` twice continuously differentiable.  In
the differentiated Weil operator, the finite-part `1/|t|` term has principal
Fourier symbol `log|xi|`; the remaining smooth kernel and finitely many prime
translations are lower-order or bounded perturbations at each fixed window.

This yields regularity and a Fredholm-style reduction, but not unique
continuation.  If the equation is written `(P_a + R_a)u=0` with an invertible
shifted log-elliptic principal part, then exactly

`u = -P_a^{-1} R_a u`.

Thus uniqueness is equivalent to excluding eigenvalue `1` for the associated
Birman--Schwinger map `-P_a^{-1}R_a`.  A strict norm bound below one would do
so, but this is the same kind of delicate cancellation estimate exposed by
the collar experiments; ellipticity alone cannot provide it.  The exact
algebraic reduction is formalized in `LogEllipticReduction.lean`.

The most promising next experiment is therefore not another generic
regularity argument.  It is to construct this preconditioned operator in the
existing high-precision Galerkin basis, track its extremal eigenvalue through
prime-activation windows, and identify whether the observed subunit margin
comes from a sign, monotonicity, or interlacing law that can plausibly be
proved for the explicit zeta remainder.

That checkpoint has now been run.  The extremal Birman--Schwinger vector is
aligned with the original ground state at roughly `0.9993` to
`0.999999999`, its gap depends strongly on the arbitrary coercive shift, and
refinement drives it toward one in step with the original Galerkin margin.
No protective prime-event jump or interlacing law appeared.  See
`BIRMAN-SCHWINGER-CHECKPOINT.md`.  The generic log-elliptic preconditioner is
therefore retired as an independent mechanism.

The subsequent zero-side isolation attempt also fails at a precise point.
Zeta-zero exponentials are overcomplete on every fixed finite window.
Completeness can force a test function to vanish when all its samples vanish,
but it cannot isolate one off-line quartet from the total Guinand--Weil sum.
`ZeroSideOvercompleteness.lean` gives a finite-dimensional nonnegative form
with a negative overcomplete summand and a nonzero radical vector on which no
individual sample vanishes.  See `ZERO-SIDE-ARITHMETIC-CHECKPOINT.md`.

### Global semiboundedness and the fixed-shift fork

The fixed-negative-shift survivor has now been resolved at the level of
quantifiers.  If one constant `c` made

`Q_W(f)+c||f||_2^2 >= 0`

on every compact smooth test, then `W+c delta_0` would be positive definite.
Writing Suzuki's unconditional accelerant identity as `W=-g''` shows that
`g-(c/2)|t|` is a global screw function.  Its Krein--Langer Herglotz transform
is exactly

`i (xi'/xi)(1/2-i z)+i c/2`.

Holomorphy in the upper half-plane excludes every off-critical zero, so this
global semibound is equivalent to RH.  Therefore, if RH fails, the antitone
localized floors do not settle above a fixed negative level: they tend to
`-infinity`.

This closes the fixed shift as an easier global existence theorem.  It does
not rule out using a fixed shift after RH.  The later quantitative audit now
does supply the false-world rate: a zero displaced by `delta` forces eventual
two-bump floors below `-C_epsilon exp((2 delta-epsilon)a)`.  The short proof
uses a pole of the complete translated correlation, while zeta cardinal
interpolation and smooth truncation control the gaps between large values.
When the off-line divisor is finite, the matching upper rate follows from a
finite quartet norm estimate, so the floor exponent is exactly the maximal
displacement.  The conclusion extends to infinitely many exceptions when
their local displacement-square measure is translation bounded.  In the
unrestricted case, standard prime-by-prime Cauchy--Schwarz bounds still grow
like `4 exp(a)`.  Replacing them by the zero-strip estimate for `Psi(x)-x`
gives the correct exponential factor but loses an `H^(1/2)` norm under
Stieltjes partial summation; logarithmic archimedean coercivity cannot absorb
that loss.  On the zero side, a clustered-divisor countermodel preserves the
strip and Riemann--von Mangoldt count to `O(1)` and remains lower semibounded
on every fixed support, yet has superexponentially negative selected floors.
Thus unsigned sampling and qualitative local semiboundedness are also
insufficient; the required signed completed cancellation remains open.  See
`SEMIBOUNDED-WEIL-DICHOTOMY.md` and
`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`.

### Signed packet fork

The subsequent Selberg/Fejer lift has also reached a decisive checkpoint.
Nonnegativity on all modulated interval indicators, even for every width and
position, does not imply positivity of a compressed Hermitian convolution
form.  Minimal Toeplitz, shifted-atom, and real-even entire rank-three
countermodels all retain a negative separated-block direction.  Hence the
diagonal triangular tests do not generate the full autocorrelation cone; see
`TRIANGULAR-PACKET-CONE-NOGO.md`.

The missing mixed datum nevertheless has a sharp scalar zeta specialization.
For any one fixed normalized box, the exponential growth rate of its
translated Weil cross correlation equals

`Delta=sup_rho |Re(rho)-1/2|`.

On the arithmetic side it is exactly one fixed-log-width triangular
von Mangoldt discrepancy.  Its boundedness, or merely subexponential growth,
is equivalent to RH.  This compresses the detector but supplies no
independent bound; see `FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md`.  A continuation
must therefore explain that single cross orbit arithmetically rather than try
to recover it from more diagonal packets.
