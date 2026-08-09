# The Positivity Gate

An instrumented research program on the Riemann Hypothesis, built during intensive
July 2026 human–AI sessions. This repository packages the
program document, the instruments, and the measured results so the investigation is
resumable by anyone — human, machine, or both together.

## What this is, and is not

**It is not a proof or disproof of RH.** Nothing here claims one. Read the honesty
clauses in `PROGRAM.md` §0 and §8 first; they are the house style.

**It is:** a set of numerical and formal instruments aimed at the Weil-positivity
formulation of RH, together with finite-dimensional measurements, explicitly
conditional analytic lemmas, and a research architecture. Claims are separated into
kernel-checked algebra, computer-assisted finite matrices, computer-assisted
full-space theorems at three endpoints in successive prime-power regimes, empirical
extrapolations, and open global
statements in `results/CODEX-REVIEW.md`.

For a conservative, ranked inventory of results that may be suitable for a
paper, corrigendum, or mathlib contribution, including exact nonclaims and
release blockers, see [`PUBLICATION.md`](PUBLICATION.md).

For a human-first account of the mathematics, proof architecture, certificate
role, and exact remaining gap, begin with
[`publication/README.md`](publication/README.md) and
[`publication/MATHEMATICAL-OVERVIEW.md`](publication/MATHEMATICAL-OVERVIEW.md).
For the primary-source theorem baseline governing the R65--R98 analytic
branch, see
[`publication/IMPORTED-ANALYTIC-BASELINE.md`](publication/IMPORTED-ANALYTIC-BASELINE.md).
The current arithmetic and positive-carrier fixed-strip frontiers are
[`results/FULL-R71-RECIPROCAL-RESPONSE-GATE.md`](results/FULL-R71-RECIPROCAL-RESPONSE-GATE.md)
[`results/R92-NONLATTICE-POLE-CANCELLING-CARRIER-GATE.md`](results/R92-NONLATTICE-POLE-CANCELLING-CARRIER-GATE.md),
with calibrated scalar endpoints in
[`results/R90-NEWTON-COEFFICIENT-CANCELLATION-GATE.md`](results/R90-NEWTON-COEFFICIENT-CANCELLATION-GATE.md)
and the higher-order audit in
[`results/R93-HIGHER-ORDER-PARETO-DIVIDED-DIFFERENCE-GATE.md`](results/R93-HIGHER-ORDER-PARETO-DIVIDED-DIFFERENCE-GATE.md).  The sharpest current
signed endpoints are isolated in
[`results/R96-LUROTH-GLOBAL-ALIAS-POISSON-GATE.md`](results/R96-LUROTH-GLOBAL-ALIAS-POISSON-GATE.md),
[`results/R96-MOBIUS-BESICOVITCH-RECURRENCE-GATE.md`](results/R96-MOBIUS-BESICOVITCH-RECURRENCE-GATE.md),
and
[`results/R96-ONE-SIDED-VON-MANGOLDT-RAMP-GATE.md`](results/R96-ONE-SIDED-VON-MANGOLDT-RAMP-GATE.md).
The latest topology and conditional-bootstrap audits are
[`results/R97-NONLINEAR-EULER-PRIME-ZETA-RIGIDITY-GATE.md`](results/R97-NONLINEAR-EULER-PRIME-ZETA-RIGIDITY-GATE.md),
[`results/R97-FERMIONIC-FREDHOLM-TRACE-ANOMALY-GATE.md`](results/R97-FERMIONIC-FREDHOLM-TRACE-ANOMALY-GATE.md),
and
[`results/R98-QUASI-RH-BOOTSTRAP-GATE.md`](results/R98-QUASI-RH-BOOTSTRAP-GATE.md).

The current post-R98 fixed-strip frontier is the center-annihilated R71
energy.  Complete conductor recombination is now exact—proper conductor
classes cancel the primitive Ramanujan correction modulus by modulus—but the
surviving ordinary dual is the original positive energy with canonical
coefficient `-mu(n) log n`, not a new upper bound.  See
[`results/R128-ALL-ARITY-PROPER-CONDUCTOR-GATE.md`](results/R128-ALL-ARITY-PROPER-CONDUCTOR-GATE.md),
with the actual primitive-sign audit in
[`results/R124-ACTUAL-QH-PRIMITIVE-MELLIN-SIGN-GATE.md`](results/R124-ACTUAL-QH-PRIMITIVE-MELLIN-SIGN-GATE.md).
The independent zero-replication and logarithmic-derivative routes currently
stop at quantified topology/sign gates in
[`results/R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md`](results/R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md),
[`results/R127-NEAR-ONE-MIXED-CONTOUR-DENSITY-GATE.md`](results/R127-NEAR-ONE-MIXED-CONTOUR-DENSITY-GATE.md),
and
[`results/R129-SIGMA-DIFFERENCE-LOGDERIVATIVE-GATE.md`](results/R129-SIGMA-DIFFERENCE-LOGDERIVATIVE-GATE.md).
None of these reports proves or disproves a fixed zero-free strip.
The null-tail dilation-frame test also renormalizes the same prime-discrepancy
field to a smaller scale; see
[`results/R130-NULL-TAIL-HADAMARD-DILATION-FRAME-GATE.md`](results/R130-NULL-TAIL-HADAMARD-DILATION-FRAME-GATE.md).
Functional-equation reflection and zero-quartet pairing have now been audited
in
[`results/R131-FUNCTIONAL-EQUATION-PAIRED-RECURRENCE-GATE.md`](results/R131-FUNCTIONAL-EQUATION-PAIRED-RECURRENCE-GATE.md)
and
[`results/R132-FUNCTIONAL-PAIR-SIGMA-KERNEL-GATE.md`](results/R132-FUNCTIONAL-PAIR-SIGMA-KERNEL-GATE.md):
the first loses real-part localization, while the second must choose between
signed vertical lobes and a leading `log T` gamma debt.  The high-jet route in
[`results/R133-HIGH-JET-EULER-RECURRENCE-GATE.md`](results/R133-HIGH-JET-EULER-RECURRENCE-GATE.md)
bypasses contour winding but leaves an explicitly stated exceptional
prime-log-return theorem open.  The independent combinatorial audit
[`results/R134-PRIME-SEMIPRIME-MORSE-GATE.md`](results/R134-PRIME-SEMIPRIME-MORSE-GATE.md)
shows that power-close prime/semiprime replacements exist, but raw
two-sided-recognizable codebooks leave a positive-density exceptional set.
An exact prime-, pole-, and leading-gamma-null explicit-formula carrier is
constructed in
[`results/R135-PRIME-NULL-EXPLICIT-FORMULA-GATE.md`](results/R135-PRIME-NULL-EXPLICIT-FORMULA-GATE.md);
its arithmetic null factor necessarily creates remote chirp bands whose
signed zero cancellation is the remaining issue.
The arithmetic Nyman endpoint has also been sharpened in
[`results/R136-NYMAN-L1-LP-SELF-IMPROVEMENT-GATE.md`](results/R136-NYMAN-L1-LP-SELF-IMPROVEMENT-GATE.md):
the PNT supplies the exact `L1` endpoint, while any fixed improvement to
`L^(1+delta)` (even a suitable weak-tail estimate in reciprocal measure)
would already prove a fixed strip.  Finally,
[`results/R137-EXCEPTIONAL-HIGH-JET-RESONANCE-GATE.md`](results/R137-EXCEPTIONAL-HIGH-JET-RESONANCE-GATE.md)
shows that every Haar/diagonal high-jet resonator pays more entropy than
Cauchy localization permits; only genuinely exceptional finite-height
off-diagonal arithmetic remains outside that theorem.
The new degree-zero quadratic-character construction in
[`results/R138-DEGREE-ZERO-QUADRATIC-VIRTUAL-L-GATE.md`](results/R138-DEGREE-ZERO-QUADRATIC-VIRTUAL-L-GATE.md)
does cancel prime-sign, Gamma, and conductor debts simultaneously.  Its
remaining exact gate is to beat the weighted-conductor localization budget
while keeping the auxiliary quadratic `L`-zeros out of one target disc.
Its character-aspect continuation is audited in
[`results/R139-QUADRATIC-UNIVERSALITY-PAIR-REPLICATION-GATE.md`](results/R139-QUADRATIC-UNIVERSALITY-PAIR-REPLICATION-GATE.md):
quadratic zero density makes the pair-counting step work throughout
`Re(s)>1/2`, even for a polynomially decaying forcing density, but standard
quadratic universality is topologically incapable of producing the required
one-sided ratio event around a zero.  Mishou--Nagoshi's corresponding
single-character statement is already an RH equivalence.
The resulting localization and exceptional-pattern audit is recorded in
[`results/R140-DEGREE-ZERO-LOCALIZATION-AND-FROBENIUS-DICHOTOMY.md`](results/R140-DEGREE-ZERO-LOCALIZATION-AND-FROBENIUS-DICHOTOMY.md):
Bombieri--Perelli gives `>>T log T` genuine zeros and poles of every fixed
R138 quotient, but an explicit positive self-reciprocal Dirichlet model
disproves localization from the broad analytic axioms.  A sub-Cauchy
quadratic Frobenius mask necessarily forces a near-one auxiliary zero and is
quantitatively sparse; interpolation by all even characters removes the
construction problem but hits an exact square-root Fourier wall.  The live
target is therefore a signed theorem using the bounded Boolean prime-power
alphabet, not another general Jensen or universality argument.
The nonlinear and high-degree continuation is
[`results/R141-NONLINEAR-TENSOR-AND-REGULAR-FROBENIUS-GATE.md`](results/R141-NONLINEAR-TENSOR-AND-REGULAR-FROBENIUS-GATE.md).
Reciprocal curvature and an explicit `2,-3,1` combination separate zeta
zeros from auxiliary zeros by pole order, but a general calibration theorem
forces mixed prime/semiprime signs.  A different exact construction using a
Galois regular representation kills every completely split head prime while
charging only the root discriminant.  It would close the strip from a
sub-square-root split-field construction plus local auxiliary nonvanishing;
known constructions cost about `X/log X`, and Dedekind GRH predicts that the
required sub-`sqrt(X)` scale is impossible.  A permutation-character variant
only asks each small Frobenius to move an exponentially tiny fraction of the
embeddings, but its controlled-discriminant realization is open and also
GRH-hostile.  This leaves that realization, a growing pole-order tensor, or a
signed Type-II divisor correlation as the next live tests.
The first of those tests is closed in
[`results/R142-GROWING-POLE-ORDER-AND-COMMON-DIVISOR-GATE.md`](results/R142-GROWING-POLE-ORDER-AND-COMMON-DIVISOR-GATE.md):
the source pole's binomial amplification occurs identically in the remote
ledger, while lower Laurent terms can cancel it exponentially unless the
order is too small to alter the rate.  Differentiated products do give exact
positive common-zero detectors, but leave the unfavorable poles and the
prime half-threshold; every scalar holomorphic common-divisor test also
creates a spurious hypersurface divisor.  The next live arithmetic question
is therefore the low-support permutation-field realization from R141.
The group-theoretic audit in
[`results/R143-SOLVABLE-SUPPORT-QUOTIENT-AND-PRIMITIVE-CLASSIFICATION.md`](results/R143-SOLVABLE-SUPPORT-QUOTIENT-AND-PRIMITIVE-CLASSIFICATION.md)
proves that every solvable realization collapses, with sharp constant `2`,
to a completely split intermediate field of no larger root discriminant.
Primitive classification leaves only natural alternating/symmetric actions
at bounded absolute support.  That survivor leads to the exact new detector
in
[`results/R144-BOUNDED-SUPPORT-VIRTUAL-CHARACTER-ANNIHILATOR.md`](results/R144-BOUNDED-SUPPORT-VIRTUAL-CHARACTER-ANNIHILATOR.md):
the falling factorial `(m-Fix(g))_q` is a nonnegative integral virtual
character which annihilates every element moving fewer than `q` points, at
constant normalized conductor cost.  This removes R141's exponentially
small support-fraction requirement.  Exact annihilation is necessarily
virtual, however, so the live gate is now a cheap prescribed-Frobenius
`A_m/S_m` field together with target-conditioned noncancellation of its
signed auxiliary divisor.  Unconditional Poitou corrections force only
`log rd >> log X`; GRH would force the prohibitive `sqrt(X)` scale.
The analytic closure of that detector is now sharp in
[`results/R145-FULL-STRIP-POSITIVITY-AND-DIVISOR-NULL-GATE.md`](results/R145-FULL-STRIP-POSITIVITY-AND-DIVISOR-NULL-GATE.md).
Full-strip zero positivity forces a `sech(x/2)` test kernel and hence only
the Poitou `1/p` prime weight.  Reciprocal jets do preserve the exact deleted
head and their signed coefficients are dominated by the positive direct
jets, so the Euler tail is no longer the obstruction.  The remaining divisor
gate is genuine: the Artin order pattern `e*reg` is compatible with all
standard holomorphy inequalities and cancels every degree-zero exact mask at
the selected zeta zero simultaneously.  Squarefree parity cancels virtual
conductor but not the absolute numerator/denominator zero ledger.
The ensuing high-density and ramified-head audit is
[`results/R146-FROBENIUS-ENTROPY-AND-INERTIA-ADJOINT-GATE.md`](results/R146-FROBENIUS-ENTROPY-AND-INERTIA-ADJOINT-GATE.md).
It constructs the exterior Euler mask
`det(1-Std)=m 1_(m-cycle)`, which deletes every non-inert unramified prime
and, for `m>=3`, every transposition-ramified factor while cancelling signed
Gamma and conductor terms.  Its absolute Artin cost is `2^(m-1)`.  More generally a
positive mask supported on density `alpha` satisfies the exact uncertainty
law `C[-log(1-alpha)]>=1`.  Exact inertia deletion has an adjoint induced
permutation-character order pattern which kills the whole detector, and a
single such pattern kills every fixed bounded-support inertia bank.  Thus
local rarity and exact ramification do not remove the target-conditioned
divisor gate.
The fixed-degree closure of this construction is now audited in
[`results/R147-EXTERIOR-CYCLE-FAMILY-SELECTION-GATE.md`](results/R147-EXTERIOR-CYCLE-FAMILY-SELECTION-GATE.md).
For cubic fields, current local counting and zero-density theorems really do
produce no-inert fields whose sign and standard factors avoid a prescribed
thin near-one rectangle, but only at `log D_K>(2+o(1))X`.  High-jet
localization requires `log D_K=o(X^kappa)` with `kappa<1/2`; even an
entropy-optimal family count would cost `X/log X`.  Averaging cannot be
treated as independent divisor noise: its deterministic mean is the
head-truncated zeta logarithmic derivative, whose regular part coherently
cancels the retained zeta pole.  Only an exceptional subentropy field or a
centered signed divisor theorem remains on this branch.
The denominator-selection statement is sharpened in
[`results/R148-CUBIC-LOCAL-SELECTION-AND-ZERO-AVOIDANCE-GATE.md`](results/R148-CUBIC-LOCAL-SELECTION-AND-ZERO-AVOIDANCE-GATE.md):
for every fixed rectangle `Re(s)>=sigma`, `|Im(s)|<=T` with
`sigma>51/56`, a no-inert-through-`H` cubic field with
`log D_K=(2+eta)H` can be chosen so that `L(s,Std_K)` is zero-free there.
The quadratic sign factor is in the numerator and need not be avoided.
This suffices to show that it cannot cancel the source divisor.  For a
field-uniform high-jet lower bound, however, other varying numerator zeros
must still be avoided or jointly controlled; same-sign residues can cancel
through their reciprocal-power phases.  R147's stronger selection includes
that avoidance at the same scale.  The incompatible absolute outer-divisor
scale remains.
The global divisor literature is imported in
[`results/R149-DEGREE-ZERO-L-DATA-AND-DISTINCT-DIVISOR-GATE.md`](results/R149-DEGREE-ZERO-L-DATA-AND-DISTINCT-DIVISOR-GATE.md).
Booker's degree-zero classification forces every nontrivial exterior quotient
to have infinitely many genuine zeros and poles; in the cubic case,
Bombieri--Perelli gives `>>T log T` residual mass in both orientations, and
Booker also forces infinitely many zeta zeros to survive the standard
denominator.  None of these results localizes a survivor horizontally.
The regular-order null would make the Galois-closure zeta vanish to order
`e|G|`, but all known unconditional multiplicity bounds still allow that
order once degree, root discriminant, and target height vary.
The two most natural analytic attempts to evade that bill are closed in
[`results/R150-TRANSLATED-CARRIER-AND-FUNCTIONAL-EQUATION-GATE.md`](results/R150-TRANSLATED-CARRIER-AND-FUNCTIONAL-EQUATION-GATE.md).
A translated positive tail does equal one at the selected pole and decay at
the observation point, but its exact high derivative is the isolated pole
jet multiplied by a Poisson lower-tail probability; in the required scaling
that probability is exponentially small.  Equivalently, every enclosing
circle sees left-boundary growth strictly larger than its Cauchy localization
gain.  Functional-equation reflection pays the decay back, and `3-4-1`
positivity gives every auxiliary denominator pole the adverse positive sign.
Moreover, once the common zeta pole and deleted head are imposed, each
field's remote regular part is deterministically forced to cancel that pole
to exponential accuracy; convex centering preserves this mode and signed
centering needs exponential condition number.  The pure highest derivative
is already the optimal absolute finite-order filter.  Only a genuinely
target-correlated signed boundary estimate can escape this gate.
The remaining exceptional arithmetic is sharpened in
[`results/R151-CLASS-CHARACTER-HEAD-QUOTIENT-GATE.md`](results/R151-CLASS-CHARACTER-HEAD-QUOTIENT-GATE.md).
For a real quadratic resolvent `F`, every nontrivial ordinary class character
`eta` gives the exact positive degree-zero quotient
`zeta_F/L_F(eta)`.  Its complete prime head vanishes precisely when `eta`
factors through the quotient of `Cl(F)` by the small split and ramified prime
classes.  The original no-inert cubic condition is exactly an order-three
instance of this least class-character nonresidue problem.  A large quotient
can select a locally zero-free denominator by Hecke zero density, but the
normalized class-field average still costs `asymp log D`; the minimal
`C_3` quotient has no amplification.  GRH-scale class-group generator bounds
would rule out the required sub-square-root discriminant regime, while no
such unconditional polylogarithmic bound or exceptional countersequence is
known.
The genus-theory specialization is computed exactly in
[`results/R152-GENUS-REDEI-AND-BOOLEAN-CLASS-MASK-GATE.md`](results/R152-GENUS-REDEI-AND-BOOLEAN-CLASS-MASK-GATE.md).
The surviving ordinary genus characters are the kernel of a binary matrix
formed from the infinity-sign row, split head-prime rows, and Redei rows.
Ramified constraints and Redei nullity can be engineered cheaply, but every
ordinary genus detector is exactly the R138 biquadratic quotient.  Its
external obstruction is still a missing density-`1/4` Frobenius class.
General elementary-`2` complement interpolation has the same exact
square-root Fourier ledger as R138--R140.
The first mechanism that crosses the old exponent conditionally is
[`results/R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md`](results/R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md).
For `F=1+U` with head support beyond `H`, the logarithmic derivative of
`1-U^q` has support beyond `H^q` while its divisor ledger is only
`O(q log D)`.  A fixed large `q` would make the known `log D asymp H` cubic
scale prove a strip if finitely many mixed factors `N-(1+omega)D` avoided the
target disc.  Those factors are non-Euler linear combinations.  Same-sign
residues can cancel arbitrarily long power-sum blocks, and ordinary Turan
needs `qH` resolution where the Euler support supplies only `q log H`.
Rational, entire, differential-power, and positive-kernel variants either
recreate the mixed `a`-points or repay the outer-growth ledger.  The live
input is a target-local, head-conditioned `a`-point theorem.
The coprime-packet workaround is closed in
[`results/R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md`](results/R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md).
Consecutive filters have only `F=0` in common, and an exact rational identity
does eliminate every finite mixed value while shifting support to
`H^(q+1)`.  The resulting response is
`(1-F)^qF'/F=F'/F+dR_q(F)/ds`: all finite mixed complexity has moved to an
order-`q` pole at `F=infinity` and an uncontrolled regular polynomial germ.
An unweighted contour erases this correction exactly; a weighted contour
pays its full boundary growth.  Rational common-divisor scalars are only
monomials in `F`, which lose the support shift, and an affine packet gives a
sharp local countermodel to vector/Gram recovery.
The mixed-value selection question is decided in
[`results/R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](results/R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md).
If a head-deleted quotient is holomorphic on the connected target disc and
omits two fixed mixed values, Montel normality plus convergence to `1` on the
right-hand cap forces convergence to `1` throughout the disc, contradicting
the retained zeta zero.  Even one-value avoidance is impossible when the
local zero divisor stays bounded: `Log(2-F)` can meet the lattice
`log 2+2 pi i Z` only at zeros of `F`, so boundedly many zeros leave two
lattice values omitted and restore Montel's theorem.  This also closes the
positive repeated-pole filter whose sole artificial value is `F=2`.
Quantitatively, the deterministic truncated-zeta skeleton has characteristic
and a summed three-value reduced count of size at least
`H^alpha/(log H)^(3/2)` with radius slack.  Mixed points are therefore forced
and naturally abundant; the surviving task is a signed joint estimate which
uses them rather than a zero-free selection theorem.
Moving the artificial values and using their topology are audited in
[`results/R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md`](results/R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md).
For a positive rational filter, a node collapsing toward the head value loses
one Euler-support power, while an omitted node escaping to infinity must grow
as a fixed negative power of the head error and repays exactly that power in
the residue at denominator poles.  The Euler and outer inequalities reduce
to an impossible geometry independently of the number of moving nodes.
Moreover, a finite polynomial model with one fixed zero, no poles, power-small
head error, `O(H)` divisor ledger, and sub-`H` outer characteristic makes its
forced `F=2` points cancel the target reciprocal powers exponentially well for
a linearly long order block.  Winding, common residue sign, logarithmic lifts,
and scalar covering theory therefore do not supply the signed estimate.  Any
continuation must use coefficient-specific arithmetic absent from that model.
The class-group determinant alternative is resolved in
[`results/R157-CLASS-GROUP-MATRIX-TREE-AND-DETERMINANT-GATE.md`](results/R157-CLASS-GROUP-MATRIX-TREE-AND-DETERMINANT-GATE.md).
The quotient partial-zeta convolution matrix has eigenvalues `L_F(s,eta)`;
the cofactor of `zeta_F I-Z` is a positive spanning-tree polynomial supported
beyond `H^(|C_H|-1)`.  Multiplying it by `zeta_F` gives a positive raw series
which retains the target zero.  That series has no constant term, however,
and factoring its first monomial preserves every zero while erasing the
absolute support gain.  The correctly normalized class-field ratio is exactly
the product of the R151 deleted-head tails.  It recovers the nonlinear support
shift but pays the full `|C_H| log D` collective determinant ledger and reduces
to the R153 scalar filter when all nonidentity partial zetas are equal.
The quadratic-family alternative is made precise in
[`results/R158-CONDITIONED-MIXED-POINT-FAMILY-AND-SKELETON-GATE.md`](results/R158-CONDITIONED-MIXED-POINT-FAMILY-AND-SKELETON-GATE.md).
After prescribing `chi_d(p)=1` through `H` at `log d asymp H`, denominator
zeros form a power-saving exceptional set.  Conditional on a retained zeta
zero, however, R155 makes `zeta-2L(s,chi_d)` vanish for density one of that
conditioned family on the full connected bridge.  Unconditioned power-saving
mixed-point bounds are also false by quadratic universality.  The exact
factorization through the truncated-zeta skeleton `E_H` leaves a narrower
target-local question: control the winding and boundary conditioning of
`E_H-2`, together with a growing-head functional tail approximation.  An
ordinary approximate functional equation plus the quadratic large sieve
cannot beat the head entropy at the required moment order.
The exact quadratic functional equation is audited in
[`results/R159-QUADRATIC-FUNCTIONAL-EQUATION-MIXED-POINT-GATE.md`](results/R159-QUADRATIC-FUNCTIONAL-EQUATION-MIXED-POINT-GATE.md).
Critical-line `F=2` points lie on a phase lattice, but that lattice has the
full `O(log d)` conductor density and does not constrain the off-line packet.
Reflecting the `H^q` two-value response splits it into the original
target-bearing `H`-supported logarithmic derivative and a delayed
`d`-supported term which is analytic at the target.  An explicit projection
embeds arbitrary right-local mixed packets into exact functional-equation
models while exporting `O(log d)` poles to the critical line.  Reflection
therefore gives no independent target-bearing delayed channel.
The finite collective-cutoff workaround is closed in
[`results/R160-FINITE-COLLECTIVE-CUTOFF-STOKES-HURWITZ-GATE.md`](results/R160-FINITE-COLLECTIVE-CUTOFF-STOKES-HURWITZ-GATE.md).
For fixed even `q` and any fixed number of comparable full cutoffs, the
collective nonlinear numerator factors exactly as `zeta C_H`.  This retains
the common zeta divisor and permits arbitrary complex, cutoff-dependent
scalar weights.  Nevertheless `C_H` has a zero in every fixed open subset of
`1/2<Re(s)<1` for all large `H`, uniformly over those weights.  A full
`1/log H` endpoint phase turn forces two individual cutoff waves to be
co-maximal; microscopic rescaling gives a nonmonomial exponential polynomial,
whose unavoidable zero contradicts zero-freeness by Hurwitz.  The result is
specific to fixed finite full-cutoff banks.  Growing independent signed
choices at the optional primes remain outside it.
The deterministic mixed divisor is resolved more sharply in
[`results/R161-DETERMINISTIC-SKELETON-MICROCLOUD-AND-SPECTRAL-SHIFT-GATE.md`](results/R161-DETERMINISTIC-SKELETON-MICROCLOUD-AND-SPECTRAL-SHIFT-GATE.md).
Every sufficiently large truncated-zeta cutoff has
`gg H^(1-sigma)/log H` simple, uniformly conditioned `E_H=2` points in an
`O(1/log H)` microdisc inside any fixed open strip set, including next to a
hypothetical off-line zero.  Their proportional-order reciprocal-power law
has no internal same-height cancellation, but smaller clouds farther right
can dominate exponentially.  An exact spectral-shift quotient subtracts the
universal cutoff lattice and recovers `zeta'/zeta-c'/c` in the large-product
phase; it also assigns negative residue to the background and leaves a global
Stokes-transport problem finer than PNT error.  The remaining target is a
signed global sheet-coupling estimate, not another local avoidance theorem.
The optional-prime continuum problem is separated in
[`results/R162-BOUNDED-CAUSAL-LAPLACE-CONTROLLABILITY.md`](results/R162-BOUNDED-CAUSAL-LAPLACE-CONTROLLABILITY.md).
At a high nonreal frequency, an explicit truncated Poisson profile with
values in `[0,1]` cancels the past Laplace head to error `H^(-A)` on a
compact neighborhood using only an `O_A(log H)` horizon.  Thus causality and
bounded fractional amplitude are not continuum obstructions, although that
particular profile is saturated and its first prime-density model freezes a
logarithmic weight which varies on the same horizon.
The exact arithmetic lift and a strict-slack repair are proved in
[`results/R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md`](results/R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md).
Blocks of length `x^theta`, `theta>7/12`, normalized by their actual prime
counts lift every slack weighted control with error
`O(H^(theta-sigma)/log H)`; biased sign rounding costs only
`O(H^(1/2-sigma)/sqrt(log H))`.  A late-supported high-degree polynomial in
`exp(h(1-s))` has exponentially small coefficients and approximates any
bounded analytic exact head on a sufficiently small filled conjugate-disc
pair.  It therefore supplies the slack and repairs the exact
`1/(log H+v)` density.  For every fixed nonreal frequency with
`0<delta<5/12`, this yields signs on all primes in `H<p<=H^kappa` whose
Dirichlet tail cancels the exact prime head by a fixed power, and an analogous
local finite-Euler shaping theorem.  This is a new coefficient-specific
mechanism outside R160's fixed-slope no-go.  It cannot approximate
`Log zeta` on a filled contour around a retained zero because of monodromy,
and it does not yet make the nonlinear collective cofactor zero-free.
The subsequent collective-cofactor audit is recorded in
[`results/R164-EXPLICIT-Z-PLANE-COLLECTIVE-COFACTOR-TEMPLATE.md`](results/R164-EXPLICIT-Z-PLANE-COLLECTIVE-COFACTOR-TEMPLATE.md),
[`results/R165-NONLINEAR-SAFE-FIBER-AND-GLOBAL-ENTIRE-GATE.md`](results/R165-NONLINEAR-SAFE-FIBER-AND-GLOBAL-ENTIRE-GATE.md),
[`results/R166-MIXED-PRODUCT-SUPPORT-AMPLIFIER-AND-COLLECTIVE-COFACTOR-GATE.md`](results/R166-MIXED-PRODUCT-SUPPORT-AMPLIFIER-AND-COLLECTIVE-COFACTOR-GATE.md),
and
[`results/R167-QUANTITATIVE-NONNORMAL-RATIO-CLOUD-GATE.md`](results/R167-QUANTITATIVE-NONNORMAL-RATIO-CLOUD-GATE.md).
Local zero-free templates really exist, and independent products retain the
`H -> H^q` gain while replacing the scalar root-of-unity factors by one
collective hypersurface.  The price is unavoidable nonnormality: a safe
family must carry a growing unit-ratio value cloud.  Quantitatively that cloud
costs only `Omega(log H)` characteristic at power cap accuracy, so it fits
rather than contradicts the fixed-power optional-prime ledger.  Fixed global
entire exponential identities are excluded by Borel independence.

The global transition and unit-factorization tests are
[`results/R168-FINITE-UNION-LATE-SUPPORT-AND-TRANSITION-HULL-GATE.md`](results/R168-FINITE-UNION-LATE-SUPPORT-AND-TRANSITION-HULL-GATE.md),
[`results/R169-TWO-UNIT-DECOMPOSITION-AND-PRODUCT-AMPLIFIER-GATE.md`](results/R169-TWO-UNIT-DECOMPOSITION-AND-PRODUCT-AMPLIFIER-GATE.md),
[`results/R170-HIGH-GIRTH-TRANSFER-DETERMINANT-AMPLIFIER.md`](results/R170-HIGH-GIRTH-TRANSFER-DETERMINANT-AMPLIFIER.md),
and
[`results/R171-CAP-NORMALIZED-UNIT-SUM-AND-MATRIX-ESCAPE-AUDIT.md`](results/R171-CAP-NORMALIZED-UNIT-SUM-AND-MATRIX-ESCAPE-AUDIT.md).
Finite separated contour patches admit the full delayed actual-prime lift,
but a fixed nonzero-left/zero-right completed contour violates polynomial-hull
compatibility.  For two scalar product channels, exact cofactor safety is
equivalent to the cap-normalized equation `1+G=R_1+R_2`; constant, bounded
inner, and generic two-good shortcuts do not solve it.  Growing channel count
and a high-girth transfer determinant genuinely escape that exact scalar
normal form.  The latter has a positive closed-walk logarithmic derivative,
support beyond `H^q`, a simple Perron target, and uniformly safe uneven local
slopes.  An exact normalized `GL_2` split confirms the matrix flexibility,
but its edgewise causal realization spends the apparent support gain.  The
remaining test is a globally hull-compatible, divisor-preserving matrix or
growing-channel completion with fixed-power conditioning.

That test has now been split into four quantitative gates in
[`results/R172-HULL-COMPATIBLE-DELAYED-TRUNCATION-AND-PRIME-LIFT.md`](results/R172-HULL-COMPATIBLE-DELAYED-TRUNCATION-AND-PRIME-LIFT.md),
[`results/R173-MATRIX-ARITHMETIC-LIFT-AND-CAUSAL-COFACTOR-GATE.md`](results/R173-MATRIX-ARITHMETIC-LIFT-AND-CAUSAL-COFACTOR-GATE.md),
[`results/R174-EXACT-DIVISOR-PEAK-AND-CONTOUR-CONDITIONING-GATE.md`](results/R174-EXACT-DIVISOR-PEAK-AND-CONTOUR-CONDITIONING-GATE.md),
and
[`results/R175-UNIQUE-ZERO-TRANSFORM-OUTER-GROWTH-CONSERVATION.md`](results/R175-UNIQUE-ZERO-TRANSFORM-OUTER-GROWTH-CONSERVATION.md).
Deleting the low degrees of a Bernstein--Walsh approximant realizes every
quantitatively hull-compatible delayed target, and the actual-prime lift
stays uniform even when fixed-power logarithmic target growth forces an
outer prime horizon exponential in a power of `H`.  This removes the hull
as a standalone obstruction, but not the boundary-growth bill.  Any
exact-divisor family which is `H^(-A)`-close to one on a fixed right cap has
logarithmic oscillation at least a fixed power of `H` and
stretched-exponential two-sided condition number on an enclosing contour.
For the scalar truncated-log unique-zero transform, Cauchy interpolation
makes that lower bound exactly consume the `H^q` support gain: the proposed
high-jet inequality reduces to the impossible strict inequality `q>q` for a
fixed finite divisor.

The explicit matrix normal form retains the common divisor and formal
`H^2` support.  Its literal causal realization nevertheless has a
deterministic coefficient tax: a late tail which impersonates the missing
constant has majorant at least `t H^(r/2)`, while the reciprocal companion
contributes `t^(-1)H^(-r/2+o(1))`.  Their two-cycle is not power-small,
independently of `t` and of sparse prime rounding.  Thus the R171
missing-constant route is closed under positive-majorant high-jet control.
What remains is strictly phase-sensitive: a growing-divisor signed estimate,
a non-Cauchy localization functional, or a nonperturbative matrix cofactor
argument which never replaces its edges by absolute coefficient majorants.
The first non-Cauchy test is settled in
[`results/R176-HARDY-MODE-CARLEMAN-AND-ONE-SIDED-CONTOUR-GATE.md`](results/R176-HARDY-MODE-CARLEMAN-AND-ONE-SIDED-CONTOUR-GATE.md).
The target residue is indeed an exact negative Hardy mode on a complete
circle.  Restricting control to the right arc, however, obeys the sharp
harmonic-measure law `|res B| <= C delta^omega M^(1-omega)`; analytic
Carleman weights cannot improve its exponent, and outer functions attain
it.  The actual `H^q` right-tail decay therefore forces, rather than
contradicts, complementary-boundary growth.  Functional-equation reflection
retains the target only in the original linear `H`-supported channel.  The
surviving contour target is narrower but still coefficient-specific: save a
fixed multiple of `q log H` in the harmonic logarithmic mean on the
uncontrolled boundary.
None of these mechanism theorems proves either side of the fixed-strip
dichotomy.

For negative results, use the canonical theorem cards and proof-debt states in
[`NO-GO-ATLAS.md`](NO-GO-ATLAS.md), not broad wording from historical branch
notes.  Public claims are governed by
[`publication/PROOF-STANDARD.md`](publication/PROOF-STANDARD.md).

## The one-paragraph summary of what was found

RH is equivalent, through Weil's criterion, to positivity at every support of
a quadratic form assembled from pole, archimedean, and prime-power terms.  At
`a=7/16` (`L=7/4` in the program convention), Lean defines that arithmetic
form on its intrinsic logarithmically weighted Fourier domain, proves that the
only active prime power is `2`, identifies it exactly with the certified
prime-2 form, and proves
`(22699/10^9) ||f||² < Q_(7/16)(f)` for every nonzero domain vector.  The proof
combines human-readable Fourier, digamma, Legendre, projection, and two-block
reductions with an exact rational matrix witness; the certificate is the final
finite-arithmetic leaf, not the conceptual proof.  Larger software-certified
endpoints and extensive numerical experiments have separate trust bases.  The
full Guinand--Weil zero-sum equality remains an explicit literature assumption
in Lean, and no theorem establishes positivity uniformly at arbitrary support.
Thus the repository contains a rigorous local theorem and reusable machinery,
not a proof or disproof of RH.

## Repository layout

```
PROGRAM.md              the full research program: findings (§2.1–2.13 with all
                        numbers), target lemma (§3), six tracks (§4), milestones (§5),
                        normalization ledger (§6), related work (§7), postscript (§8)
READING.md              the reading order into the mathematics
publication/README.md   human-facing entry point and reading routes
publication/MATHEMATICAL-OVERVIEW.md
                        main theorem, proof architecture, and exact global gap
PUBLICATION.md          ranked publication portfolio, claim boundaries, artifact map,
                        and new research synthesis
NO-GO-ATLAS.md          exact obstruction classes, evidence levels, survivors,
                        prior-art boundaries, and proof debt
publication/PROOF-STANDARD.md
                        theorem contracts, review protocol, and release states
results/RESULTS.md      every key measured number, as a regression target
results/CODEX-REVIEW.md current audit, theorem tiers, gaps, and next steps
src/weil_core.py        shared primitives: digamma, hat basis, form builders (zeta
                        and Dirichlet), fixed Kronecker symbol
src/oracle.py           the two-sided Guinand–Weil identities — RUN THIS FIRST
src/spectral_instruments.py  Riemann–Siegel scanner, census, Lehmer hunt, GUE gaps,
                        prime-side spectrum, rogue-line scan, Davenport–Heilbronn
src/model_zeros.py      RH-conditional finite-frame comparison of on-line,
                        smooth-staircase, and seeded Poisson ordinates, with
                        cutoff-safe generation and a multi-seed helper
src/margin_experiments.py    margin sweeps, basis escalation, mechanism test, pole
                        flip, Temple bounds, cascade, keyhole
src/family_experiments.py    Dirichlet cartography, twisted margins, conductor law,
                        sign ledger
src/chowla_hunt.py      high-precision numerical central values, scaled hunt, distribution fit,
                        D = 14693 lowest zero
src/hp_margins.py       the margin ladder in extended precision: exact x-space
                        archimedean kernel (no Simpson, no r-truncation), mpmath
                        eigensolve — the instrument that measured the float
                        pipeline's true error and the fate of the p >= 3 margins;
                        now conductor-aware (q, D, prime_set) for the family
src/spectral_margins.py the ladder in an orthonormal Legendre (spectral) basis:
                        Gram = I, overlaps exact by Gauss-Legendre, same x-space
                        kernel — converges past the hat wall and gives decreasing
                        finite Galerkin upper bounds for the full margin
src/certified_margins.py software interval enclosures (mpmath.iv, 220-bit):
                        exact-rational hat autocorrelation pieces, Bernoulli-
                        series kernel with rigorous tails, interval Cholesky
                        lower bounds + interval Rayleigh upper bounds — the
                        finite hat-space positivity margins under the stated trust base
src/certified_spectral.py the same certificates in the Legendre basis (exact
                        universal overlap polynomials, hinge-free): finite
                        Legendre-matrix positivity down to the 1e-20 scale
src/fullinf_class_certificate.py a conservative software-certified application
                        of FULLINF F4 to the class with L=7/4, R=50 and
                        Fourier-tail mass at most 1e-15, plus an explicit
                        degree-28 non-vacuity witness; not the unrestricted
                        infimum or an NT-4 packet certificate
src/arb_fullinf_certificate.py an independent FLINT-Arb reproduction of the
                        finite core, F4 class ledger, and exact-moment witness
src/fullinf_unrestricted_certificate.py the clipped-symbol Arb certificate and
                        F8 transfer proving the unrestricted L=7/4 lower
                        bound >2.2699e-5
src/fullinf_unrestricted_p3_certificate.py the independent 80-mode Arb driver
                        for F9, proving the unrestricted L=497/200 lower
                        bound >9.99e-11
src/fullinf_n4_scout.py fast n=4 parameter reconnaissance; its exterior-floor
                        panel check is rigorous, but its scan is explicitly
                        nonrigorous and it is not a positivity certificate
src/fullinf_unrestricted_n4_certificate.py the resumable 132-mode Arb driver
                        for F10, proving the unrestricted L=749/250 lower
                        bound >9.9e-16
results/fullinf_n4_M132_S110_entries.jsonl outward Arb checkpoint for all
                        4,422 independent n=4 band integrals
ENVELOPE.md             draft note for the frontier authors: the measured
                        envelope law, its validations, the certified ladder,
                        the family universality — NOT yet distributed
THEOREMS.md             proved statements: the Glide Theorem (margin monotone
                        + continuous through thresholds, closed form and compact
                        resolvent, explicit constants), the finite
                        machine-checked window with its Bridge Proposition,
                        and the Arb-certified unrestricted endpoints through
                        L=749/250
lean/weilcert/          Lean 4 + mathlib development: WeilCert.weil_window_positive,
                        kernel-verified (axioms: propext, Classical.choice,
                        Quot.sound; no native_decide) — exact finite matrix
                        positivity; FullInfTransfer formalizes F8's canonical
                        orthogonal-projection step. The Legendre modules now
                        formalize F2 from Rodrigues and the exact coefficient
                        through normalization, interval scaling, L² density,
                        a complete Hilbert basis, Parseval, canonical finite
                        projections, the actual zero-extension/Plancherel band
                        operator, and the exact integrated leakage bound.
                        PoleProjectionL2 proves the two exponential residuals;
                        BoundedSymbolMultiplier and FullInfP2Endpoint compose
                        the bounded real symbol, poles, 48-mode certificate,
                        complement/cross estimates, and F8 determinant;
                        LegendreParityCoordinates supplies canonical matrices,
                        and SymbolQuadraticComparison compares the clipped and
                        original weighted integrals;
                        FullInfClipped48, FullInfClipped48Real, and
                        FullInfClipped48Transfer kernel-check the exact rational
                        certificate, its strict real extension, and its
                        composition with the L=7/4 projection ledger.
                        Identification with the
                        analytic zeta form remains a separate bridge
lean/glide/Glide/       analytic Lean lemmas, including the archimedean kernel
                        sandwich, the positive trigamma series, unconditional
                        locally-uniform GammaSeq convergence and digamma
                        monotonicity, the exact p=2 exterior-symbol comparison,
                        and directed rational p=2 scalar bounds
lean/rhbridge/           cross-project p=2 composition: clipped positivity from
                        canonical matrix containment and transfer to the original
                        weighted integral plus pole term under integrability
```

## How to reproduce

Requirements: Python 3 with `numpy` and `mpmath`; the Arb certificates also
require `python-flint >= 0.9.0`. The optional n=4 scout uses SciPy. No network
is needed after installation.  Install the recorded core ranges with
`python3 -m pip install -r requirements.txt`; the lightweight root test suite
uses `python3 -m pip install -r requirements-test.txt` and
`python3 -m pytest`.

1. **Run the regression oracle first (program law).** `python3 src/oracle.py` — the two-sided
   explicit-formula identities for zeta and for the mod-3/mod-4 characters. All
   downstream conventions are checked by these. This is a high-precision numerical
   cross-check, not an interval or formal certificate. Expected: differences at the
   1e-13-to-1e-29 level depending on precision settings.
2. Each other script is self-contained, has an `if __name__ == "__main__"` demo,
   and carries `EXPECTED:` comments with its measurement/audit date. A
   reproduction that matches those numbers is a regression pass; one that does not
   is either a bug (ours or yours) or a discovery — treat it as a bug until an
   independent oracle says otherwise. That rule caught three fake catastrophes here.
3. `python3 src/hp_margins.py` — the extended-precision ladder (validates the float
   pipeline against the exact x-space archimedean kernel, then re-measures the
   p = 3 window). ~1 minute; EXPECTED values in the module docstring.
4. `python3 src/spectral_margins.py` — the spectral (Legendre) ladder: unit tests,
   then the L = 1.75 and L = 2.485 ladders that pass below the hat wall. ~1 minute.
5. `python3 src/certified_margins.py` — the interval calculations: containment
   sanity, then four two-sided finite Galerkin eigenvalue enclosures (three zeta
   matrices and one chi_{-7} matrix), conditional on the stated `mpmath.iv` trust
   base. ~20 seconds. (Optional speedup for all hp/spectral
   work: `pip install gmpy2` gives mpmath a fast backend; results are identical.)
6. `python3 src/certified_spectral.py` — the spectral-basis certificates: exact
   overlap cross-checks, then certified enclosures at the 1e-10 / 1e-15 / 1e-20
   scales. ~3 minutes.
7. `python3 src/fullinf_class_certificate.py` — rebuilds the m=48 interval
   core and a closed-form tail majorant, proving `Q_(7/4) > 1.1139e-5` for every
   member of the stated frequency-tail class under the documented trust base.
   The same run certifies an explicit normalized polynomial's tail below
   `3e-17`, proving the class is nonempty. ~1 minute.
8. `python3 src/fullinf_unrestricted_certificate.py` — Arb-encloses 600 clipped
   matrix integrals, proves the clipped V₄₈ block above `2.27e-5`, and executes
   F8's two-by-two transfer to certify the unrestricted bound
   `inf Q_(7/4)/||.||² > 2.2699e-5`. About 2 minutes on the audit machine.
9. `python3 src/fullinf_unrestricted_p3_certificate.py` — independently
   encloses 1,640 clipped matrix integrals and executes the same full-space
   transfer with primes 2 and 3, certifying
   `inf Q_(497/200)/||.||² > 9.99e-11`. About 7 minutes on the audit machine.
10. `python3 -u src/fullinf_unrestricted_n4_certificate.py --workers 12` —
   loads or builds the resumable 4,422-entry Arb checkpoint, proves the
   132-mode clipped block above `1e-15`, and transfers it to
   `inf Q_(749/250)/||.||² > 9.9e-16`. The first run took 1,040 seconds on
   12 cores; a completed-checkpoint rerun performs only reconstruction and
   Cholesky. Checkpoint SHA-256:
   `7591f662b1c1a79ed83cb6999881d8face43836dec1131ccff8d56d6bdf7354f`.
   Its metadata binds the cached raw integrals to the source of the numerical
   kernel, so an integrand change fails closed instead of silently reusing it.
11. Lean verification: build `lean/glide`, `lean/weilcert`, and finally
   `lean/rhbridge` (which imports both), then run the focused axiom audits in
   `lean/README-verify.md`. Requires elan; cached rebuilds are short.

## The discipline (read this even if you read nothing else)

Every assembled positivity form must be spot-checked against the zero-side sum
2 Σ |φ̂(γ)|², computed from an independently generated on-line zero list. This is
an excellent regression oracle, but its sum-of-squares interpretation is conditional
on the relevant zeros lying on the critical line; it cannot logically veto an RH
counterexample. Any apparent negativity should first be treated as a likely
implementation bug and then adjudicated with interval bounds, explicit tails, and an
unconditional form of the explicit formula. Observed base rate in this project:
the apparent catastrophes investigated so far were implementation or test errors.

## Diligence status (be honest when citing)

- **Verified July 25, 2026 (second working day):** every EXPECTED number in this
  repository reproduces on a fresh machine, several to all printed digits; the
  |D| ≤ 1e5 hunt reproduces end-to-end; L(½, χ₁₄₆₉₃) confirms against a fully
  independent implementation. See `results/RESULTS.md`, second section. (Dateline
  note: the original documents self-date July 26; the clock on both working days
  read July 25.)
- **Re-audited July 27, 2026:** the interval suites and Lean builds pass after
  the claim-tier repairs; the committed restricted-class certificate and its
  non-vacuity witness reproduce independently in mpmath.iv and FLINT-Arb. The
  three clipped-symbol full-space certificates also pass end-to-end. Lean now also
  checks F8's scalar two-by-two determinant implication and the three exact
  rational block ledgers, while its analytic estimates and Arb bridge remain
  external. The model-zero
  audit found and fixed a silent
  180-point cutoff, so its July 27 EXPECTED table supersedes the older nominal
  Gcut=420 rows. See `results/CODEX-REVIEW.md`.
- **Lean-first update July 28, 2026:** the abstract Hilbert and canonical
  orthogonal-projection F8 transfers, F2's exact oscillatory integral model,
  sharp double-factorial bound, infinite geometric tail, all-degree Rodrigues
  formula, exact plane-wave coefficients, normalized Legendre orthonormality,
  arbitrary-interval scaling, L² completeness, Parseval, canonical projection
  tails, and the explicit pointwise leakage inequality are kernel-checked.
  Zero extension, `L¹∩L²` Fourier compatibility, the exact `z/(2π)`
  normalization, band restriction, and the rational
  `ρ≤81/10^23` endpoint leakage are now kernel-checked as well. The
  exponential pole vectors have norm at most one and 48-mode residual below
  `195/10^95`. Operator algebra derives the complement and cross blocks, and
  `FullInfP2Endpoint.projection_lower_bound_of_fourier_clipped48_p2_symbol`
  composes these with the real interval certificate and exact determinant.
  F7 is unconditional: `GammaUniform` proves locally uniform Euler GammaSeq
  convergence, hence the trigamma derivative and strict monotonicity;
  `P2Symbol` proves the actual exterior-symbol comparison. `DigammaBounds`
  proves `109387/100000 ≤ p2Alpha` and
  `|p2Omega r-p2Alpha| ≤ 7447/1000` on `|r|≤50` by exact series and rational
  tail bounds. `SymbolQuadraticComparison` proves the exact clipped-integral
  identity and its order comparison with the original, possibly unbounded,
  multiplier under the stated weighted-integrability hypothesis. The
  bounded-certificate theorem
  `RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_matrix_containment`
  proves the even/odd canonical matrix containments. Its immediate corollary
  `p2_canonical_clipped_endpoint` proves the strict `22699/10^9` clipped bound;
  the existing original-integral theorem transfers it to the unbounded p=2
  weighted Fourier integral plus the exact pole term under weighted
  integrability. At that date the remaining local p=2 work was identifying
  that expression and its domain with the arithmetic Weil form; the August 5
  update below closes that specialization.
- **Reusable-infrastructure update August 3, 2026:** Gauss's general two-point
  digamma series and positive-vertical-line integral are now proved from the
  locally uniform Gamma sequence.  Lean also has an actual Fourier–Legendre
  Hilbert basis on every interval `[b,c]` with `b<c`, a standalone
  Fourier–Laplace entirety/growth module, finite simple-principal-part removal
  and contour sums, real-line Wiener–Khinchin identities, a quantitative smooth
  cutoff, a bundled exact `LDLᵀ` certificate, and a formally optimal scalar
  two-block lower constant.  These reusable endpoints are Apache-2.0 licensed,
  separately packaged, and axiom-audited.  This is infrastructure hardening,
  not a new RH implication.
- **Arithmetic-form and exposition update August 5, 2026:** Lean now defines
  the general compact-support arithmetic Weil form on its logarithmic Fourier
  domain, proves exact specialization to the certified prime-2 form at
  `a=7/16`, and obtains the strict endpoint bound there.  The residue,
  logarithmic-derivative, right-contour, and transform infrastructure has also
  been expanded, but the global Guinand--Weil zero-sum equality remains an
  explicit literature input.  The publication guides separate human proof
  architecture, reusable Lean machinery, generated witnesses, diagnostics,
  and open global claims.
- The Chowla-scan values are very likely recoverable from existing large computations
  (Rubinstein-era tables, LMFDB); D = 14693 is a record *of our scan*, not
  necessarily of mathematics. Still unchecked against those tables.
- **Keyhole novelty is dead** (checked July 25): arXiv:2605.20224 (Groskin, May 2026)
  already recovers zeros from the truncated form's ground state to 300+ digits.
  §2.13 is full-pipeline validation, not discovery. The Lehmer "record" is a record
  of this scan's range only — and by *normalized* gap the classic 7005.06 pair is
  the tighter one; far closer pairs are known at large height.
- Remaining plausible novelties: the sign ledger, the pole flip, the conductor
  coasting law, the safety-factor decay, and the systematic per-prime margin data —
  now including the hp ladder's findings (float-pipeline bias +0.7–0.9e−9, the p = 2
  basis-limit bracket [3.18, 3.30]e−5, the m^{−3.6} transient law, the floor-bias of
  κ). Check against Connes–Consani(–Moscovici), Suzuki, and Groskin before claiming.
- Every positive finite Galerkin value by itself is one-sided evidence for the
  full operator, not a lower bound for it. F8–F10 are different: they add a proved
  exterior floor, an orthogonal-complement band-defect bound, and a cross-block
  determinant. Their three endpoint conclusions use FLINT-Arb plus explicit
  analytic lemmas and are not yet theorems about zeta in Lean. For the p=2
  endpoint, however, the transfer machinery, scalar bounds, Fourier/pole
  constants, canonical matrix containment, and clipped endpoint are now
  kernel-checked, and the arithmetic form/domain specialization is now proved.
  The zero-side Guinand--Weil equality retains explicit literature assumptions.

## Where the door is

`PROGRAM.md` §3 states the intended uniform target.  The arithmetic form and
its intrinsic logarithmic domain are now connected to the Lean-certified
endpoint at `a=7/16`.  The larger endpoints remain software-certified results
with their stated Arb and analytic trust bases.  Extending positivity to every
support size and proving the complete zero-side Guinand--Weil equality in Lean
remain open; uniform all-support positivity would be RH-strength work.

## Lean reuse and upstreaming

Several general-purpose results have been separated from their RH applications:
finite simple-pole residue identities, quantitative smooth cutoffs,
autocorrelation/Plancherel identities, digamma kernel formulas, arbitrary-
interval Legendre `L²` bases, and reusable certificate/coercivity lemmas.  See
[`lean/UPSTREAMING.md`](lean/UPSTREAMING.md) for their public endpoints, proof
status, and proposed small upstream-review units.

## License

Original material in this repository is released under the
[Apache License 2.0](LICENSE).  Third-party dependencies retain their own
licenses.  Named author attribution should be confirmed before any upstream
submission; the current Lean headers use the collective project attribution.
