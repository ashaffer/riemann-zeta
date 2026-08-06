# A theorem guide to the obstruction results

Status: expository companion, 2026-08-06.

This guide explains the mathematics behind the project's exact negative
results.  It is written for a reader who wants to understand the mechanism of
each theorem before opening a Lean file or a computational artifact.  The
canonical claim boundaries remain in
[`../NO-GO-ATLAS.md`](../NO-GO-ATLAS.md), and the release rules remain in
[`PROOF-STANDARD.md`](PROOF-STANDARD.md).

The results do **not** form a no-go theorem for RH.  They identify four common
ways in which a plausible argument can discard the global information it
later needs:

1. a local or weak topology can forget a remote divisor;
2. placewise positive pieces cannot reproduce essential cross-place
   cancellation for free;
3. symmetry, analyticity, or complex structure alone does not imply a
   coercive quadratic form;
4. a fixed sparse arithmetic rule can miss a positive-density part of its
   domain.

The point of grouping the results this way is predictive.  A new construction
should say, before calculation, which hypothesis of the relevant obstruction
it violates.

## 1. Four kinds of statement

Four logically different objects occur below.

- An **analytic theorem** has a conventional mathematical proof in the linked
  report.  It is not thereby formalized.
- A **Lean theorem** is the exact named declaration checked by Lean under the
  axioms printed by its focused audit.  It does not, by itself, identify the
  abstract objects with the zeta Weil form.
- A **countermodel** satisfies a proposed list of hypotheses and violates the
  desired conclusion.  It disproves that inference, not the corresponding
  zeta-specific conclusion.
- A **diagnostic** is a finite symbolic, interval, or floating-point
  experiment.  It may choose the next theorem to prove, but it is not an
  infinite theorem.

Several results have more than one component.  For example, Lean checks the
finite quartet algebra in NG-01, while the compact-open estimate is presently
an analytic theorem.  These evidence levels must not be merged in citation or
exposition.

## 2. Obstruction I: localization can erase the divisor

The common issue in NG-01, NG-02, and NG-10 is not that zeros are impossible
to detect.  Contours detect them perfectly.  The issue is that an invariant
is first constructed in a topology or limiting model which has already
forgotten the relevant zero.

### 2.1 Remote quartets are invisible to compact-local phase data (NG-01)

For positive `gamma, delta`, define

```text
Q(z)=((z-gamma)^2+delta^2)((z+gamma)^2+delta^2),
A=gamma^2+delta^2.
```

The four roots are `+-gamma +- i delta`.  On the real axis both quadratic
factors are positive, so multiplication by `Q` changes neither sign nor
phase.  More strongly,

```text
Q(z)/A^2
 = 1 + 2(delta^2-gamma^2)z^2/A^2 + z^4/A^2,
```

and on `|z| <= R`,

```text
|Q(z)/A^2-1| <= 2R^2/A + R^4/A^2.
```

For fixed `R` and `delta`, the right side tends to zero as `gamma` tends to
infinity.  Thus a normalized off-line quartet can approach the identity on
every fixed compact while remaining a genuine four-zero perturbation.

**Proof idea.**  Expand the even polynomial, use
`|delta^2-gamma^2| <= A`, and apply the triangle inequality.  Real-axis
positivity is immediate from the two sums of squares.  A continuous
integer-valued detector is locally constant, so it cannot change on every
member of a family converging to the baseline.

**Exact scope.**  This is an ambient stress test for compact-open normalized
divisor data and real boundary phase.  The factor `Q/A^2` changes global
growth and need not preserve an Euler product.  It is not a construction of a
second zeta function and does not obstruct a weighted global topology that
retains arithmetic growth.

**Formal status.**  Lean checks the rational polynomial algebra, positivity,
and sign preservation.  It does not currently check the complex
compact-open estimate.  The exact declarations are:

```text
RHBridge.QuantizedPhaseIndexNoGo.quartetFactor_expansion
RHBridge.QuantizedPhaseIndexNoGo.quartetFactor_even
RHBridge.QuantizedPhaseIndexNoGo.quartetFactor_pos
RHBridge.QuantizedPhaseIndexNoGo.mul_quartet_nonneg_iff
```

They are in
[`QuantizedPhaseIndexNoGo.lean`](../lean/rhbridge/RHBridge/QuantizedPhaseIndexNoGo.lean),
with the focused axiom report in
[`QuantizedPhaseIndexNoGoAudit.lean`](../lean/rhbridge/RHBridge/QuantizedPhaseIndexNoGoAudit.lean).
The analytic argument is in
[`QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`](../results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md).

**Escape hatch.**  Specify a genuinely global weighted topology in which one
remote quartet has nonvanishing size, and prove that the proposed arithmetic
object converges in that same topology.

### 2.2 Finite Euler loops and the all-prime topology do not carry the same
index (NG-02)

For `|r|<1` and `|z|=1`, consider the local unit phase

```text
U_r(z)=(1-r conjugate(z))/(1-r z).
```

Replacing `r` by `t r`, `0 <= t <= 1`, contracts this loop to the constant
one through continuous, nonzero, unit-modulus functions.  Every finite product
of these local loops therefore has trivial ordinary winding.

There are then two distinct all-prime calculations.

1. The literal two-sided shifted quotient has local squared norm

   ```text
   1+(r_- - r_+)^2/(1-r_+^2),
   ```

   and the corresponding prime sum diverges for a shift inside the critical
   strip.  Its finite products are not even bounded in the relevant
   Besicovitch `B^2` norm.
2. The functional-equation-normalized right phase is `B^2`-Cauchy for every
   positive shift.  For shifts up to the line `Re(s)=1`, however, Kronecker
   approximation aligns arbitrarily large finite sets of prime phases, and
   the accumulated angles diverge.  The products are not uniformly Cauchy.

**Proof idea.**  The finite contraction is the radial disk homotopy.  Haar
orthogonality on independent prime circles gives the exact `B^2` norm
identities.  Divergence of the applicable prime sums yields unboundedness or
nonuniformity.  Ordinary winding is stable under a uniform limit of
invertible continuous symbols, but `B^2` convergence alone produces only an
equivalence class and supplies no such symbol.

**Exact conclusion.**  Ordinary winding cannot be inherited through a
uniform invertible continuous-symbol limit of these two specified
finite-prime models.  This says neither that every almost-periodic algebra
lacks an index nor that convergence fails in every strong, Calkin, strict, or
semifinite operator topology.

**Formal status.**  Lean checks only the local contraction:

```text
RHBridge.QuantizedPhaseIndexNoGo.localEulerHomotopy_zero
RHBridge.QuantizedPhaseIndexNoGo.localEulerHomotopy_one
RHBridge.QuantizedPhaseIndexNoGo.localEulerDenominator_ne_zero
RHBridge.QuantizedPhaseIndexNoGo.localEulerHomotopy_norm_eq_one
RHBridge.QuantizedPhaseIndexNoGo.localEulerHomotopy_ne_zero
RHBridge.QuantizedPhaseIndexNoGo.localEulerHomotopy_continuousOn
```

The source and audit are the same two Lean files as in NG-01.  The norm,
prime-sum, and Kronecker arguments are analytic and are recorded in the
quantized-phase report linked above.

**Escape hatch.**  Construct a completion-native relative index with an
explicit operator topology, all-place summability, and a continuity theorem
showing that an off-line quartet has nonzero charge.  Merely renaming the
`B^2` limit as a symbol does not supply those steps.

### 2.3 A zero-bearing continued tail lies outside the zero-free random-tail
support (NG-10)

Fix a prime cutoff `y` and a disk `K` contained in
`1/2 < Re(s) < 1`.  Removing the finite Euler factors gives

```text
R_y(s)=zeta(s) product_(p<=y)(1-p^(-s)).
```

The conditioned Bagchi tail after fixing the first prime phases is modeled by

```text
Z_y(s,omega)=product_(p>y)(1-omega_p p^(-s))^(-1).
```

On compact subsets of the strip its logarithm converges locally uniformly
almost surely, so `Z_y` is the exponential of a holomorphic function and is
zero-free.  If `R_y` has a zero in `K`, then for

```text
m_y=min_(s in boundary K)|R_y(s)|
```

the event

```text
sup_(boundary K)|Z_y-R_y| < epsilon,   0<epsilon<m_y,
```

is empty: Rouche's theorem would otherwise give the zero-free `Z_y` the same
number of zeros in `K` as `R_y`.

**Proof idea.**  Finite Euler factors are nonzero in the strip, so `R_y` and
`zeta` have the same zeros.  Local uniform convergence of the random
logarithm proves zero-freeness of the limiting tail.  Rouche separates the
two supports.  A separate zero-density argument gives zero relative frequency
for the analogous actual shifts at fixed `y`.

**Status and trust boundary.**  This is an analytic theorem conditional on
the named Bagchi functional-limit construction; the actual-shift formulation
also uses a classical zero-density estimate.  It has no Lean endpoint.  The
full phase convention, literature inputs, and proof are in
[`BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md`](../results/BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md).

**Exact scope.**  The cutoff is fixed before the height limit.  A cutoff
growing with height is a different shrinking-target problem.  It would need
a zeta-specific zero-bearing conditional approximation theorem, not a
stronger concentration inequality for the zero-free random Euler tail.

## 3. Obstruction II: placewise positivity has an irreducible cost

NG-03, NG-04, and NG-05 explain why positivity cannot be manufactured by
treating prime places independently and postponing their interaction with
infinity.  The missing resource is not a cleverer completion of each local
square; it is essential cross-place cancellation.

### 3.1 Every fixed finite-place Weil form is indefinite on large support
(NG-03)

Fix a finite set `P` of primes.  On the real test domain

```text
D={(-partial_x^2+1/4)phi : phi in C_c^infinity(R), phi real},
```

the two pole moments vanish.  In the repository's Fourier convention the
fixed-place Weil form is

```text
Q_P(v)=(1/(2 pi)) integral M_P(t)|vhat(t)|^2 dt,
```

where

```text
M_P(t)=-log(pi)+Re psi(1/4+i t/2)
       -2 sum_(p in P) log(p) sum_(m>=1) p^(-m/2) cos(m t log p).
```

The multiplier is negative at zero.  The archimedean value is already
negative, and every finite-prime contribution at zero is negative.  At high
frequency the digamma term grows like `log |t|`, while the finite prime sum is
bounded; hence `M_P(t)` is eventually positive.

**Proof idea.**  For a broad bump
`phi_R(x)=R^(-1/2)phi(x/R)`, apply
`-partial_x^2+1/4`.  Its Fourier transform has the factor `t^2+1/4`, which
kills both pole moments, and its mass concentrates at zero.  Dominated
convergence makes its Rayleigh quotient tend to `M_P(0)<0`.  Modulating the
bump by `cos(Tx)` concentrates the mass at `+-T`; for a sufficiently large
`T`, the quotient tends to `M_P(T)>0`.  Thus the form is genuinely
indefinite, so reversing its sign is not a repair.

**Status.**  This is an analytic theorem, not a Lean theorem.  Its
load-bearing premise is the displayed normalized multiplier identity,
including its Fourier sign and constants.  A standalone derivation and
independent normalization audit remain required before submission.  The
proof is in
[`TWO-PRIME-INFINITY-FAIL-FAST.md`](../results/TWO-PRIME-INFINITY-FAIL-FAST.md).

**Exact scope and escape.**  The prime set is fixed while support grows.  The
full Weil form activates new prime powers as support expands and is not
covered.  Any global positivity mechanism must therefore couple the active
place set to support and explain how newly activated places repair the modes
lost by every preceding finite set.

### 3.2 Splitting one prime edge among more positive channels cannot lower its
diagonal cost (NG-04)

If two vectors in a real inner-product space satisfy
`inner(u,v)=w`, then

```text
2w <= ||u||^2+||v||^2.
```

This is sharp at `u=v`.  Consequently, if independent positive Gram channels
are used to reproduce a fixed negative cross coefficient, their total
endpoint diagonal mass cannot beat the ordinary difference square.

**Proof idea.**  Expand `0 <= ||u-v||^2`.  For a scalar square
`(a x-b y)^2` with `ab=w`, the same assertion is
`2w <= a^2+b^2`, obtained from `(a-b)^2>=0`.

**Formal status.**  Lean checks:

```text
RHBridge.PrimeEdgePolarization.differenceSquare_identity
RHBridge.PrimeEdgePolarization.gram_diagonal_cost
RHBridge.PrimeEdgePolarization.rankOne_diagonal_cost
RHBridge.PrimeEdgePolarization.rankOne_cost_sharp
```

See
[`PrimeEdgePolarization.lean`](../lean/rhbridge/RHBridge/PrimeEdgePolarization.lean)
and
[`PrimeEdgePolarizationAudit.lean`](../lean/rhbridge/RHBridge/PrimeEdgePolarizationAudit.lean).
The arithmetic interpretation is developed in
[`PRIME-EDGE-POLARIZATION-NOGO.md`](../results/PRIME-EDGE-POLARIZATION-NOGO.md).

**Exact scope.**  The channels are positive and assigned independently to
one edge at a time.  The theorem does not exclude a block whose prime and
archimedean components have essential off-diagonal coupling.  The repository's
currently negative zeta residual is diagnostic only; until one witness is
proved analytically or by a frozen interval certificate, the full
zeta-specific local-edge no-go is not a theorem.

### 3.3 A nonzero pure mixed pairing is necessarily indefinite (NG-05)

For vectors `u,v` in a real inner-product space, the proposed quadratic cross
term changes sign when `v` is replaced by `-v`.  Therefore a pure mixed block
cannot be nonnegative for both signs unless `inner(u,v)=0`.

The arithmetic identity

```text
moebius * log = vonMangoldt
```

does provide exact global divisor cancellation.  It naturally presents that
cancellation as a mixed pairing, however, and the identity alone does not
turn the pairing into a positive form.

**Proof idea.**  One of a nonzero real number and its negative is negative.
The polarization identity

```text
2 inner(u,v)=||u+v||^2-||u||^2-||v||^2
```

makes explicit that a mixed term is a difference of positive quantities, not
itself a square.

**Formal status.**  Lean checks:

```text
RHBridge.GlobalMobiusCancellation.moebiusLog_eq_vonMangoldt
RHBridge.GlobalMobiusCancellation.mixedPairing_polarization
RHBridge.GlobalMobiusCancellation.mixedPairing_has_negative_direction
RHBridge.GlobalMobiusCancellation.mixedPairing_nonnegative_for_both_signs_forces_zero
```

See
[`GlobalMobiusCancellation.lean`](../lean/rhbridge/RHBridge/GlobalMobiusCancellation.lean)
and
[`GlobalMobiusCancellationAudit.lean`](../lean/rhbridge/RHBridge/GlobalMobiusCancellationAudit.lean).

**Escape hatch.**  A mixed term may occur inside a positive block with
independently controlled diagonal terms.  The theorem rules out only the
claim that the nonzero pure mixed pairing is itself the desired positive
quadratic form.

## 4. Obstruction III: formal structure does not imply coercivity

NG-06 through NG-08 and NG-11, together with two small countermodels, all
refute the same style of inference: a construction has the right symmetry,
complex, commutator, or analytic form, so its final sign should follow
automatically.  Each example shows that a quantitative gap or a positive
metric is an additional theorem.

### 4.1 A later differential cannot improve degree-zero Hodge energy (NG-06)

In a two-step Hilbert complex

```text
C0 --d0--> C1 --d1--> C2,
```

the degree-zero Hodge energy is `||d0 x||^2`.  If a scalar degree term is
subtracted, positivity is precisely

```text
degree ||x||^2 <= ||d0 x||^2.
```

Changing `d1` cannot affect this inequality, even when both choices satisfy
`d1 d0=0`.

**Proof idea.**  The assertion is the degree-zero definition of the Hodge
Laplacian.  The square-zero law organizes degree-one cohomology but introduces
no new term at degree zero.

**Formal status.**  For bounded continuous maps on ambient real Hilbert
spaces, Lean checks:

```text
RHP2Bridge.CompletedIncidenceComplexNoGo.degreeZeroHodgeEnergy_independent
RHP2Bridge.CompletedIncidenceComplexNoGo.shiftedDegreeZeroForm_nonnegative_iff
RHP2Bridge.CompletedIncidenceComplexNoGo.no_higherDifferential_repair
RHP2Bridge.CompletedIncidenceComplexNoGo.twoStepComplex_closes_iff_relativePoincare
```

See
[`CompletedIncidenceComplexNoGo.lean`](../lean/rhbridge/RHBridge/CompletedIncidenceComplexNoGo.lean)
and
[`CompletedIncidenceComplexNoGoAudit.lean`](../lean/rhbridge/RHBridge/CompletedIncidenceComplexNoGoAudit.lean).

**Exact scope.**  This is an elementary supporting lemma.  A zeta incidence
application still needs a densely defined closed or closable `d0`, its domain
and metric, and an exactly normalized identification with the Weil form.
Changing `d0`, the grading, domain, or pairing is outside the theorem, but
then the target form must be derived again.

### 4.2 Separate block positivity and analytic convolution do not force a
Schur contraction (NG-07)

Eliminating a positive exterior scalar block from

```text
lambda t^2 + 2 r t w + d w^2
```

leaves the exact pivot

```text
lambda-r^2/d.
```

Thus the desired contraction is not a qualitative consequence of `d>0`; it
is the quantitative inequality `r^2/d < lambda`.

The constant-kernel form

```text
Q(f)=||f||_2^2-alpha |integral f|^2
```

gives a countermodel.  On disjoint sets of measures `m,n`, choose

```text
alpha m<1,  alpha n<1,  alpha(m+n)>1.
```

The old and exterior compressions are separately positive, and the
convolution kernel is even and entire, but the union has a negative constant
mode.  With `m=n=1` and `alpha=3/4`, both diagonal gaps are `1/4`, the
exterior response is `9/4`, and the harmonic extension has energy `-2`.

**Proof idea.**  Complete the square.  In the rank-one model, direct algebra
gives

```text
response-oldGap
 = (alpha(m+n)-1)/(1-alpha n)>0.
```

The same completion records the off-diagonal correction in the final
two-mode pivot; omitting it changes the sign criterion.

**Formal status.**  Lean checks the identities and the countermodel:

```text
RHP2Bridge.HodgeLowSectorNoGo.scalar_harmonic_extension_identity
RHP2Bridge.HodgeLowSectorNoGo.negative_harmonic_extension_of_response_gt
RHP2Bridge.HodgeLowSectorNoGo.rankOneResponse_sub_oldGap
RHP2Bridge.HodgeLowSectorNoGo.analytic_rankOne_convolution_breaks_contraction
RHP2Bridge.HodgeLowSectorNoGo.rational_analytic_rankOne_countermodel
RHP2Bridge.HodgeLowSectorNoGo.twoMode_completion_identity
RHP2Bridge.HodgeLowSectorNoGo.twoMode_determinant_pos_iff_finalPivot_pos
```

See
[`HodgeLowSectorNoGo.lean`](../lean/rhbridge/RHBridge/HodgeLowSectorNoGo.lean),
[`HodgeLowSectorNoGoAudit.lean`](../lean/rhbridge/RHBridge/HodgeLowSectorNoGoAudit.lean),
and the mathematical account
[`HODGE-LOW-SECTOR-DTN-NOGO.md`](../results/HODGE-LOW-SECTOR-DTN-NOGO.md).

**Exact conclusion.**  Evenness, analytic convolution structure, separate
block positivity, and the weak old equation do not imply contraction.  The
countermodel is not the zeta kernel.  An exact prime--archimedean cancellation
estimate could still prove the required zeta-specific pivot bound.

### 4.3 Functional-equation duality is weaker than positive polarization
(NG-08)

For nonzero rational `a`, let

```text
A_a=diag(1/2+a,1/2-a),       J=[[0,1],[-1,0]].
```

Then

```text
A_a^T J+J A_a=J,
```

so the off-line pair has the expected alternating duality.  But if a matrix
`G` satisfies the corresponding positive-adjoint equation

```text
A_a^T G+G A_a=G,
```

its first diagonal entry is zero.  It therefore cannot define a strictly
positive quadratic form.  By contrast, the real block for
`1/2 +- i gamma` admits the identity metric.

**Proof idea.**  Read the `(0,0)` entry of the adjoint equation.  It reduces
to `a G_00=0`; since `a` is nonzero, positivity fails on the first coordinate
vector.  The on-line control is a direct matrix calculation.

**Formal status.**  Lean checks the rational two-dimensional statements:

```text
RHBridge.FinitePolarizationNoGo.offLine_preserves_alternating_duality
RHBridge.FinitePolarizationNoGo.offLine_adjoint_forces_g00_zero
RHBridge.FinitePolarizationNoGo.no_positive_adjoint_metric_offLine
RHBridge.FinitePolarizationNoGo.onLine_identity_adjoint
RHBridge.FinitePolarizationNoGo.identity_strictQuadraticPositive
```

See
[`FinitePolarizationNoGo.lean`](../lean/rhbridge/RHBridge/FinitePolarizationNoGo.lean)
and
[`FinitePolarizationNoGoAudit.lean`](../lean/rhbridge/RHBridge/FinitePolarizationNoGoAudit.lean).
The standard finite-dimensional generalization and its prior-art boundary are
in
[`GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`](../results/GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md).

Over the complex numbers, a positive Hermitian solution exists precisely when
`A-1/2` is similar to a skew-Hermitian matrix, equivalently when `A` is
diagonalizable with spectrum on the critical line.  This general
characterization is analytic/classical, not formalized here.  Solving for
`G` after the spectrum is known therefore repackages the desired spectral
conclusion rather than deriving it.

**Escape hatch.**  Construct a canonical positive metric from arithmetic or
geometry before knowing the spectrum, and prove its adjoint law independently.
Functional-equation symmetry alone is insufficient.

### 4.4 A regular virial commutator cannot order a pure-point spectrum (NG-11)

Suppose `H psi=lambda psi` and all products below are defined.  Symmetry of
`H` gives

```text
<psi,[H,G]psi>
 = <H psi,G psi>-<psi,G H psi>
 = 0.
```

Thus a strict positive-commutator estimate on a nonempty eigenspace is
impossible.  For the lower-semibounded compact-resolvent Weil operator, asking for
strict positivity on its nonpositive spectral projection is therefore already
asking that this projection be empty.  It is a reformulation of the target,
not a near-null-sector test.  The lower bound also makes that projection
finite rank, so a compact remainder can absorb any discrepancy there.  In
finite dimension the obstruction becomes `trace([H,G])=0`, so a pure matrix
commutator cannot be positive definite.

Compression does not evade the identity.  If `P^2=P` and `R=I-P`, then

```text
P[H,X]P=[PHP,PXP]+PHRXP-PXRHP.
```

The first term has zero trace.  A nonzero compressed trace comes from the two
leakage terms.  The exact control

```text
H=[[0,1],[1,0]],       X=(1/2)[[0,-1],[1,0]]
```

has `[H,X]=diag(1,-1)`: keeping one coordinate only hides the compensating
negative channel.

For the completed localized Weil form, this is not merely an abstract
warning.  Geometric dilation produces the smooth-core multiplier

```text
r tau_(1/4)(r)
 + sum_(log n<2a) (2 Lambda(n)/sqrt(n))(log n) r sin(r log n).
```

Already in the prime-2-only window, the negative prime oscillation is linear
along an explicit frequency sequence, while the archimedean slope is bounded
and the form multiplier grows only logarithmically.  Kronecker approximation
makes every active prime-power slope negative simultaneously at each fixed
larger support.  Hence adding any fixed nonnegative multiple of the Weil form
cannot repair the commutator.

For a first-order flow preserving the interval, the proposed obstruction has
generator `G_v=v d/dx+v'/2` with `v` zero at both endpoints.  Every nonzero
`v` has `v'<0` somewhere.  A high-frequency packet supported in a subinterval
of width less than `log 2` there has no prime-shift overlap and negligible
pole moments.  Its claimed negative limiting archimedean commutator depends on
a localized pseudodifferential packet lemma whose symbol/remainder proof is
still a named publication obligation.

**Formal status.**  Lean checks the finite eigenvector, trace, compression,
and `2x2` leakage identities in
[`VirialCommutatorNoGo.lean`](../lean/rhbridge/RHBridge/VirialCommutatorNoGo.lean),
with the focused axiom output in
[`VirialCommutatorNoGoAudit.lean`](../lean/rhbridge/RHBridge/VirialCommutatorNoGoAudit.lean).
It also checks the domain-safe form statement: if `B u=lambda J u`, `B` is
Hermitian, and `G^*J+JG=0`, then
`< (G^*B+BG)u,u >_V=0`.  See
[`FormDomainVirial.lean`](../lean/rhbridge/RHBridge/FormDomainVirial.lean) and
[`FormDomainVirialAudit.lean`](../lean/rhbridge/RHBridge/FormDomainVirialAudit.lean).
This avoids assuming that a weak form eigenvector belongs to an unbounded
operator domain.  The completed dilation multiplier is analytic, not
formalized; the transport wave-packet step remains Amber pending the explicit
localized remainder lemma.  Their derivation and the finite prime-5
diagnostic are separated in
[`COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md`](../results/COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md).

**Exact scope and escape.**  The result prunes regular strict Mourre estimates
as an independent pure-point test, pure finite-section commutator
certificates, and geometric dilation with fixed scalar repair once a prime
power is active.  The stated real-transport conclusion is conditional on the
packet lemma.  The result does not establish a negative Weil direction.
Other local generators and a genuinely nonlocal global mixed inequality are
not excluded.  A singular support-moving generator must retain and sign its
full completed boundary defect; that is a new collar inequality, not an
ordinary virial shortcut.

### 4.5 A support-uniform negative shift is already RH-strength (NG-16)

Let `lambda(a)` be the bottom Rayleigh value of the zeta Weil form on tests
supported in `(-a,a)`.  The floors are antitone.  Pure order theory says that
one strict common shift below every `lambda(a)` is equivalent to a uniform
lower bound, and that failure of such a bound forces `lambda(a)` to tend to
`-infinity`.  Lean checks this abstract statement in
[`SemiboundedFloorDichotomy.lean`](../lean/rhbridge/RHBridge/SemiboundedFloorDichotomy.lean).

For the zeta form, the common bound has much stronger content.  If

```text
Q_W(f)+c||f||_2^2 >= 0
```

globally, then `W+c delta_0` is positive definite.  Suzuki's unconditional
identity `W=-g''` turns this into a global screw function
`g-(c/2)|t|`.  The Krein--Langer transform of that function is

```text
i (xi'/xi)(1/2-i z)+i c/2.
```

It must be holomorphic in the upper half-plane, whereas every zero to the
right of the critical line would create a nonremovable pole.  The functional
equation handles the left side.  Thus a global `L2` semibound is equivalent
to RH; under failure of RH, `lambda(a)` tends to `-infinity`.

**Exact scope and escape.**  This does not disprove the uniform inequality.
It says that the inequality is the destination, not weaker scaffolding.
Standard termwise prime bounds grow exponentially with support and therefore
cannot prove it.  The subsequent quantitative audit closes the lower
false-world rate: displacement `delta` forces
`lambda(a)<=-C_epsilon exp((2 delta-epsilon)a)` for every sufficiently large
support.  A Laplace-pole proof controls the complete divisor along a
subsequence, and Bondarenko--Radchenko--Seip cardinal interpolation plus
smooth truncation gives the all-support upgrade.  The remaining target is the
reverse stability estimate in terms of the supremal displacement.  That
reverse estimate is sharp and elementary when the off-line divisor is finite:
each exceptional quartet has norm `O(exp(2 delta a))`, so the floor exponent
equals the maximal displacement.  The same conclusion holds for infinitely
many exceptions if their local displacement-square measure is translation
bounded.  For the unrestricted infinite divisor, ordinary prime-counting
error does not suffice: Abel summation incurs an `H^(1/2)` loss that the
logarithmic archimedean energy cannot absorb.  Nor do strip width and the full
Riemann--von Mangoldt count suffice: a sparse clustered-divisor countermodel
preserves counting to `O(1)` and has a finite floor on every fixed support,
while selected growing-support floors decay superexponentially.  The full
proof and normalization ledger are in
[`SEMIBOUNDED-WEIL-DICHOTOMY.md`](../results/SEMIBOUNDED-WEIL-DICHOTOMY.md).
The rate theorem is in
[`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](../results/QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md).

### 4.6 Diagonal Fejer packets do not determine a Toeplitz form (NG-21)

The triangular Selberg calculation naturally tests normalized vectors

```text
ell^(-1/2)e^(i tau x)1_I(x).
```

It is tempting to infer positivity of the compressed convolution operator
from nonnegativity on every such vector, allowing every interval `I`, width
`ell`, and modulation `tau`.  That inference is false.  A `3 x 3` Toeplitz
matrix with diagonal one and second off-diagonal `5/4` is positive on every
consecutive modulated box but negative on `(1,0,-1)`.  This is the smallest
possible dimension.

Two continuum versions isolate the mechanism.  A shifted-delta kernel on
`L2(0,3/2)` passes all interval packets with a uniform normalized margin
`1/6`, yet has a separated antisymmetric direction of quotient `-1/4`.  A
real-even entire rank-three kernel gives the same conclusion without any
distributional singularity.  Its packet inequality reduces to

```text
sinc^2(x-alpha)+sinc^2(x+alpha) >= (1/4)sinc^2(x),
|alpha|<=pi/4.
```

The failure is geometric: one connected interval must fill the gap between
two correlated endpoint blocks, while a coherent two-block vector can choose
their relative phase without paying mass in that gap.  Width, position, and
carrier phase do not recover this mixed Gram entry.

**Formal status.**  Lean checks the minimal Toeplitz witness, the uniform
rational continuum margin, and the negative two-block quotient in
[`SelbergPacketConeNoGo.lean`](../lean/rhbridge/RHBridge/SelbergPacketConeNoGo.lean).
The continuous and entire proofs are analytic and are written in
[`TRIANGULAR-PACKET-CONE-NOGO.md`](../results/TRIANGULAR-PACKET-CONE-NOGO.md).

**Exact scope and escape.**  This rules out a generic convex-cone lift from
diagonal packets, not a zeta-specific relation among mixed packet terms.  The
smallest visible survivor is precisely a separated-box cross orbit.  For one
fixed box, its completed zeta cross correlation has growth exponent equal to
the maximal horizontal zero displacement; the exact reduction is in
[`FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md`](../results/FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md).
Proving that orbit bounded remains RH-equivalent.

### 4.7 Two supporting countermodels

These are useful guardrails, not headline research theorems.

1. A quantitative collar lower bound does not exclude a new radical
   direction.  In `R^2`, the form `q(x,y)=x^2` is strictly positive on the old
   `x`-axis, while `(0,1)` has maximal collar coordinate and lies in the
   radical.  Lean's bundled endpoint is

   ```text
   RHP2Bridge.Stage3BoundaryNoGo.quantitative_collar_size_does_not_exclude_radical
   ```

   in
   [`Stage3BoundaryNoGo.lean`](../lean/rhbridge/RHBridge/Stage3BoundaryNoGo.lean),
   audited by
   [`Stage3BoundaryNoGoAudit.lean`](../lean/rhbridge/RHBridge/Stage3BoundaryNoGoAudit.lean).
   A useful boundary estimate must couple the new coordinate to the actual
   kernel, not merely bound its norm.
2. A simple ground state of a reflection-commuting operator need not be even.
   The two-dimensional model has a one-dimensional zero eigenspace generated
   by an odd vector, which an even boundary functional annihilates.  Lean's
   bundled endpoint is

   ```text
   RHP2Bridge.Stage3ParityNoGo.simplicity_does_not_force_evenness
   ```

   in
   [`Stage3ParityNoGo.lean`](../lean/rhbridge/RHBridge/Stage3ParityNoGo.lean),
   audited by
   [`Stage3ParityNoGoAudit.lean`](../lean/rhbridge/RHBridge/Stage3ParityNoGoAudit.lean).
   A parity argument needs a comparison of the even and odd spectral blocks.

## 5. Obstruction IV: fixed sparse substitutions miss positive density

### 5.1 Summable static prime dictionaries cannot pair almost every collar
vertex (NG-09)

Let

```text
S_N={m:N/2<m<=N, m odd and squarefree}.
```

A template `(p;q,r)` replaces a support containing `p` with one containing
`q,r`, thereby reversing the Mobius sign.  Requiring

```text
1/2 < p/(qr) < 2
```

is necessary for the two corresponding integers to occur in one dyadic
collar.  Let `T` be a fixed countable dictionary, independent of `N`, and
assume

```text
sum_((p;q,r) in T) 1/(qr) < infinity.
```

Then a positive-density set of odd squarefree integers admits no template in
`T`.  Consequently

```text
#{m in S_N : no template applies}=c_T N+o(N)
```

for some `c_T>0`, and every matching using only these edges leaves linearly
many collar vertices unmatched.  Bounded reuse of primes in the pair roles
implies the summability hypothesis.  The same argument applies to disjoint
finite prime-set substitutions of opposite parity under the corresponding
summable endpoint weights.

**Proof idea.**  On odd squarefree integers, finitely many prime-divisibility
indicators have the exact product law

```text
Pr(p divides n)=1/(p+1).
```

The cylinder in which `(p;q,r)` might apply is contained in the two support
patterns `100` and `011`, of total probability at most
`1/p+1/(qr)`.  Scale compatibility transfers summability from `1/(qr)` to
`1/p`.  Kill a finite prefix by conditioning all its primes to be absent;
this has positive density.  A union bound makes the remaining tail cost less
than one.  Finally, a deterministic count of multiples bounds every
countable tail uniformly in the height, allowing passage from finite Euler
densities to a positive natural density.  No independence between overlapping
templates is assumed.

**Status.**  This is an analytic theorem with no Lean endpoint.  A full
standalone proof and the hypertemplate extension are in
[`MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md`](../results/MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md).
Independent proof review and a specialist prior-art comparison remain
necessary before a novelty claim.

**Exact scope and escape.**  The dictionary is fixed and has summable
incidence.  A viable substitution program must use an `N`-dependent
dictionary, unbounded prime incidence, a dynamically generated move, or
global sequential matching state.  The theorem proves no Mertens estimate
and does not rule out those adaptive mechanisms.

## 6. Diagnostics and finite controls

The following artifacts should be cited as experiments or counterexamples to
an intermediate inference, never as infinite RH results.

| Artifact | What it establishes | What it does not establish |
|---|---|---|
| [`LEE-YANG-INVERSE-CONE-FINAL-2026-08.md`](../results/LEE-YANG-INVERSE-CONE-FINAL-2026-08.md) | A tested finite moment cone may hold while a stronger independent-spin cone fails | An infinite Lee--Yang theorem or a zeta zero theorem |
| [`MOBIUS-RESIDUE-TO-DENSITY-FINAL-2026-08.md`](../results/MOBIUS-RESIDUE-TO-DENSITY-FINAL-2026-08.md) | The proposed generic inverse gate fails for bounded multiplicative functions, and the Mobius parameter is singular | Failure of every Mobius-specific inverse theorem |
| [`CYCLOTOMIC-TWO-PRIME-TRACE-FINAL-2026-08.md`](../results/CYCLOTOMIC-TWO-PRIME-TRACE-FINAL-2026-08.md) | Exact finite Euler algebra has no mixed coefficient in the tested block | Nonexistence of a global geometric trace with extra coupling |
| [`TWO-WAVE-ORTHOGONAL-FAIL-FAST-2026-08.md`](../results/TWO-WAVE-ORTHOGONAL-FAIL-FAST-2026-08.md) | A reproducible ledger of explicit gates and finite falsifiers | One theorem eliminating all ten motivating fields |
| [`COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md`](../results/COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md) | The exact finite commutator identities and a floating prime-5 control agree with the analytic no-go | Failure of every nonlocal or singular positive-commutator construction |
| [`SHIFT-PHASE-COVARIANCE-FAIL-FAST.md`](../results/SHIFT-PHASE-COVARIANCE-FAIL-FAST.md) | Equivalent coercive energy norms do not generically identify full phase-labelled self-adjoint-extension families by one boundary relabeling; the exact Dirichlet control proves that pointwise obstruction | Inequality of exact zeta zero sets at one selected phase, nonexistence of a zeta-specific intertwiner, or nonexistence of a tuned shift/phase sequence; the completed-Weil scan remains diagnostic |
| [`SUZUKI-PROJECTIVE-KERNEL-CHECKPOINT.md`](../results/SUZUKI-PROJECTIVE-KERNEL-CHECKPOINT.md) | Exact line-preserving adjoint intertwiners preserve projective Gram/Bargmann data; natural nesting is rigid in the shift; cofinal admissible shifts tending to zero are equivalent to nonnegative antitone floors | Failure of selected-extension strong-resolvent convergence; the cross-window Galerkin residual tests a stronger exact equivalence |
| [`SUZUKI-LIVSIC-CALIBRATION-FAIL-FAST.md`](../results/SUZUKI-LIVSIC-CALIBRATION-FAIL-FAST.md) | One derivative plus weak imaginary-axis matches are a near-Cayley calibration effect; strong held-out probes remain nonmonotone in the tested models | Failure of compact-local convergence at larger support; unconditional positivity of the xi model kernel, which is RH-equivalent |
| [`SUZUKI-FIXED-SHIFT-DIVISOR-CHECKPOINT.md`](../results/SUZUKI-FIXED-SHIFT-DIVISOR-CHECKPOINT.md) | `sigma=-1/4` is continuum-safe through the certified endpoint, and a no-root-reuse train/holdout test fails on that finite range even under `sigma=-1` and both symmetry-phase controls | Failure of cofinal selected-extension convergence; the errors improve with support, and the finite characteristics are not a certified graph approximation |
| [`SUZUKI-SPECTRAL-COUNTING-CHECKPOINT.md`](../results/SUZUKI-SPECTRAL-COUNTING-CHECKPOINT.md) | A lifted boundary phase gives an exact floor count; fixed-support linear Weyl density does not imply support-uniform compact crowding, as an escaping-onset spectrum proves | Failure of the Suzuki limit: the required fixed-compact phase-mass estimate is still open, and even divergent counts would not alone refute strong-resolvent convergence |
| [`SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md`](../results/SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md) | Phase density is inverse squared defect-line coherence; an exact-type Hermite--Biehler family retains its full far-tail Weyl density while all added compact phase escapes | Failure of every zeta-specific fixed-shift decorrelation estimate, or of weighted Clark-measure convergence; generic type and symmetry alone are what is pruned |
| [`SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md`](../results/SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md) | The raw Clark atom and fixed-vector probability are different; generic normalized convergence can fail by mass escape at the canonical zeta phase, and a fixed negative shift canonically adds a Lebesgue spectral component | Failure of every Suzuki limit or of RH; the follow-up proves natural moving-vector compatibility fails, while an honest mixed-spectrum target or stronger boundary topology remains possible |
| [`SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md`](../results/SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md) | Natural finite defect vectors weakly escape because their Riesz norms grow exponentially; under RH, group mollification makes the compact core a generator core, so every phase choice has the same generalized strong-resolvent limit and the correct fixed-core measures converge | RH, characteristic/determinant convergence, or raw eigenvalue convergence; the positive ambient space is RH-conditional and strong resolvent topology forgets the escaping boundary data |
| [`SEMIBOUNDED-WEIL-DICHOTOMY.md`](../results/SEMIBOUNDED-WEIL-DICHOTOMY.md) | One support-independent `L2` lower bound for the actual zeta Weil form is equivalent to RH; failure of RH forces the localized floors to `-infinity` | A proof of the uniform completed bound; the false-world witness rate is now supplied by the quantitative follow-up |
| [`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](../results/QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md) | An off-line zero of displacement `delta` forces eventual two-bump floors below `-C_epsilon exp((2 delta-epsilon)a)`; subexponential negative-floor growth is RH-equivalent; the exponent equals the maximal displacement if the off-line divisor is finite | RH, existence of an off-line zero, or the reverse upper rate for a potentially infinite off-line divisor; cumulative prime-counting error alone loses a half derivative |

These artifacts are valuable when they prevent a false lemma from being
reintroduced.  Their publication role is methodological unless one of their
finite statements is promoted under the computer-assisted proof protocol.

## 7. The reusable mathematical lesson

The common failure can be expressed without claiming a universal theorem:

```text
global coherent defect
        |
        +-- localized or averaged too early --> defect becomes invisible
        |
        +-- split into independent positive pieces --> cross cancellation is lost
        |
        +-- replaced by symmetry or complex structure --> quantitative gap is missing
        |
        +-- attacked by a fixed sparse rule --> positive-density residue survives
```

Accordingly, a serious new RH mechanism should answer five questions.

1. What exact object changes when one off-line zero is present?
2. In what topology does that change have nonzero size?
3. How are every finite place and the archimedean place completed in that
   topology?
4. What theorem supplies positivity, contraction, or exclusion without
   assuming the desired spectral location?
5. Why is the global limit closed in the same topology in which the estimate
   was proved?

NG-01, NG-02, and NG-10 test questions 1, 2, and 5.  NG-03 through NG-08,
NG-11, NG-12, and NG-16 test questions 3 and 4.  NG-09 tests whether a nominally global
arithmetic move actually reaches almost every part of its domain.

## 8. What is presently suitable for mathematical exposition

There are three different publication roles.

- **Standalone analytic candidates:** fixed-finite-place indefiniteness
  (NG-03) and summable static prime substitutions (NG-09).  Both have concise
  mathematical cores and plausible value beyond this project, but both still
  need independent proof and prior-art review.
- **Reusable formal machinery:** the Gram-cost bound, mixed-pairing sign gate,
  degree-zero Hilbert-complex identity, Schur-complement formulas, and finite
  polarization and commutator identities, together with the partial-adjoint
  Riesz interface (NG-04 through NG-08 and the formal parts of NG-11--NG-12).
  These should be presented under their ordinary
  functional-analytic names, with RH as motivation rather than as part of the
  theorem.
- **Research-program guardrails:** the compact-local quartet, Euler topology,
  zero-free tail, collar radical, and parity examples.  Their value is to
  state exactly which tempting implication is unavailable and what additional
  theorem would revive it.

This division is deliberate.  A short transparent proof with an exact scope
is more useful than a large certificate attached to an inflated conclusion.
The Lean modules should function as independently readable verification of
the displayed lemmas; the mathematical explanation above remains the primary
route by which a human reader understands why they matter.
