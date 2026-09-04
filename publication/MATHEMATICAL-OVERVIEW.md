# Mathematical overview

## 1. The strongest present conclusion

Let

```text
H_a = L²([-a,a], ℝ)
```

with each vector extended by zero to the real line.  In mathlib's
ordinary-frequency Fourier convention, write `fHat` for that zero extension's
Fourier transform and set

```text
D_a = {f in H_a : integral log(1 + (2*pi*xi)^2) |fHat(xi)|² dxi < infinity}.
```

The repository defines on `D_a` the arithmetic compact-support Weil form

```text
Q_a(f) = pole_a(f) + arch_a(f) - prime_a(f),
```

where

```text
pole_a(f)  = 2 <f, exp(x/2)> <f, exp(-x/2)>,

arch_a(f)  = integral
               (Re digamma(1/4 + i*pi*xi) - log(pi)) |fHat(xi)|² dxi,

prime_a(f) = sum over log(n) < 2a
               2 Lambda(n)/sqrt(n) * integral f(x) f(x + log(n)) dx.
```

The sum is finite because `f` and its translate have disjoint support once
`|log n| >= 2a`.

At

```text
a = 7/16                         (L = 4a = 7/4 in the program convention),
```

the only active prime power is `n=2`.  Lean proves that the general arithmetic
form is exactly the previously certified prime-2 time-domain form and proves,
for every nonzero `f in D_(7/16)`,

```text
(22699 / 10^9) ||f||² < Q_(7/16)(f).
```

The principal declarations are

- `RHP2Bridge.GeneralZetaWeilForm.weilForm_seven_sixteenths`;
- `RHP2Bridge.GeneralZetaWeilForm.weilForm_seven_sixteenths_strict_lower_bound`.

They are in
[`GeneralZetaWeilForm.lean`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean),
and the focused
[`GeneralZetaWeilFormAudit.lean`](../lean/rhbridge/RHBridge/GeneralZetaWeilFormAudit.lean)
reports only Lean/mathlib's standard logical axioms.

This is a local theorem about a precisely defined arithmetic form.  It is not
a theorem about all support sizes and is not RH.

| Theorem-card field | Record |
|---|---|
| Evidence class | Lean theorem |
| Scope | Real `L²` vectors supported in `[-7/16,7/16]` and lying in the logarithmic form domain |
| Bound | Strict lower bound `22699/10^9` times the squared norm |
| Formal trust base | The standard axioms printed by `GeneralZetaWeilFormAudit.lean`; no project literature axiom |
| Semantic boundary | Arithmetic pole–archimedean–prime form; the Guinand–Weil zero-side equality is not proved in this repository's Lean build |
| Nearest nonclaim | No positivity conclusion for arbitrary support and no RH conclusion |
| Focused check | `cd lean/rhbridge && env LEAN_NUM_THREADS=1 lake env lean RHBridge/GeneralZetaWeilFormAudit.lean` |

## 2. Why the logarithmic domain matters

The archimedean multiplier grows like `log(1+xi²)`.  Consequently the Weil
form is not an everywhere-defined bounded quadratic form on plain `L²`.
Putting the logarithmic Fourier weight into the domain is therefore not a
technical embellishment: it is the natural form domain.

[`GeneralZetaWeilForm.lean`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean)
proves that this domain is closed under zero, addition, and real scalar
multiplication and packages it as a real submodule.  The theorem at `a=7/16`
is stated on this full intrinsic domain, not merely on smooth vectors or a
finite Galerkin space.

## 3. The proof architecture behind the endpoint

The final inequality is short only because several independent mathematical
reductions have already been proved.

### 3.1 Fourier and interval geometry

The interval vector is extended by zero, transformed in `L²`, and related to
its time-domain autocorrelation by Plancherel.  This fixes every factor of
`2*pi` and converts the prime term into a translation correlation rather than
an unexplained matrix entry.

Relevant reusable modules include

- [`IntervalZeroExtension.lean`](../lean/weilcert/IntervalZeroExtension.lean);
- [`AutocorrelationPlancherelCore.lean`](../lean/rhbridge/RHBridge/AutocorrelationPlancherelCore.lean);
- [`AutocorrelationPlancherel.lean`](../lean/rhbridge/RHBridge/AutocorrelationPlancherel.lean).

### 3.2 Archimedean analysis

The real part of the digamma function is represented by a positive Gauss
integral and bounded by explicit logarithmic weights.  This turns the
archimedean contribution into a controlled Fourier multiplier and supplies
the comparison needed by the full-space transfer.

The general special-function content is isolated in the `Glide` digamma and
Gamma modules; the prime-2 normalization is kept in downstream compatibility
modules.  The general package is useful independently of zeta.

### 3.3 Legendre decomposition and full-space transfer

Normalized Legendre polynomials provide a complete orthonormal basis on the
interval.  The proof separates a finite low-mode block from its orthogonal
complement.  Exact projection formulas, Fourier leakage estimates, pole
residuals, and a two-block coercivity inequality control the complement and
the cross term.  Thus positivity is transferred from a finite block to the
entire logarithmic form domain.

The key point is conceptual: finite-matrix positivity alone would only be a
Galerkin statement.  The complement and cross estimates are what make the
endpoint a full-domain theorem.

### 3.4 Exact finite arithmetic

The remaining finite block is represented by rational interval data.  An
exact `LDL^T` congruence and perturbation bound prove positivity for every real
matrix in the certified entrywise interval.  Lean checks the integer and
rational identities.  Generated files store witnesses; the reusable theorem
explaining why those witnesses imply positivity lives in the ordinary
certificate framework.

This separation is essential for readability:

```text
analytic reduction
    -> finite interval matrix
    -> generic certificate soundness theorem
    -> generated exact witness.
```

The generated witness is the last line of the argument, not the argument's
mathematical motivation.  See
[`CERTIFICATE-GUIDE.md`](CERTIFICATE-GUIDE.md) for the detailed trust ledger.

### 3.5 Exact specialization

Finally, Lean proves that at `a=7/16` the active-prime set is exactly `{2}`,
that its von Mangoldt coefficient agrees with the prime-2 normalization, and
that the pole and archimedean terms are definitionally the same as those in
the certified fixed-window form.  This prevents a positive certificate for a
surrogate normalization from being silently relabeled as a theorem about the
arithmetic Weil form.

## 4. Smaller supports

[`CertifiedBaseInterval.lean`](../lean/rhbridge/RHBridge/CertifiedBaseInterval.lean)
transports the same lower bound to `0 <= a <= 7/16` by nested zero extension.
The vector norm is preserved, and newly listed prime shifts lie beyond the
smaller support diameter, so their autocorrelations vanish.

This propagation currently depends on the explicitly declared standard lemma
`ActivationCancellation.intervalAutocorrelation_eq_zero_of_two_mul_le`.
That lemma says that compactly supported vectors have zero autocorrelation
after a translation by at least the support diameter.  It is consensus
analysis, but until it is proved in Lean the propagated theorem is properly
described as literature-conditional.  The endpoint theorem in Section 1 does
not have this dependency.

## 5. The zero-side bridge and the exact remaining gap

The classical Guinand--Weil explicit formula identifies the arithmetic form
with a transform sum over nontrivial zeta zeros.  The repository formalizes
substantial infrastructure toward that equality:

- local factorization of zeta at a nontrivial zero;
- the logarithmic-derivative principal part;
- the von Mangoldt Dirichlet series on the right half-plane;
- the completed-zeta gamma and reflected contour identities;
- weighted Fourier--Laplace `L¹`/`L²` facts and Plancherel;
- smooth compact-support transform decay;
- finite simple-pole contour machinery.

The global contour limit and the complete zero-sum equality are nevertheless
still imported inside this repository through
[`GuinandWeilLiterature.lean`](../lean/rhbridge/RHBridge/GuinandWeilLiterature.lean).
For the logarithmic form domain, the zero sum is correctly formulated by
symmetric exhaustion through closed disks rather than by asserting an
unconditionally convergent scalar series.

Anthropic's independent
[Zeta23 formalization](https://github.com/anthropics/zeta-23-lean) now proves
a smooth compact-support Weil explicit formula from source, together with the
analytic inputs it uses.  A convention-by-convention audit found a concrete
adapter from that theorem to this repository's smooth zero-side statement.
The adapter has not yet been implemented, and the external theorem does not
by itself prove passage to this repository's full logarithmic form domain.
See
[`ANTHROPIC-ZETA23-INTEGRATION.md`](ANTHROPIC-ZETA23-INTEGRATION.md).

Therefore the logical situation is

```text
unconditional Lean theorem:
    strict positivity of Q_(7/16)

literature-conditional identification:
    Q_a = symmetric zero-side limit

missing theorem needed for RH:
    Q_a >= 0 uniformly for every a > 0.
```

Even accepting the classical explicit formula, one local positive interval is
far from the all-support assertion equivalent to RH.

### 5.1 What the new density theorem changes

The same external development proves unconditionally that at least

```text
C = 3/2 - (1/sqrt(2)) cot(1/sqrt(2)) = 0.672500703679...
```

of zeta zeros are simple and on the critical line in the asymptotic
multiplicity-weighted sense; it also proves a distinct-zero proportion of at
least `(1+C)/2`.  Its key new mechanism is a finite Gabor compression of the
Weil Hermitian form followed by rank, inertia, trace, and Frobenius estimates.
Off-line functional-equation pairs are treated as hyperbolic `(1,1)` blocks,
not incorrectly declared positive.

The external Lean theorem uses the exact trigonometric expression.  The
displayed decimal and the comparison with `2/3` are mathematical evaluations,
not separately certified numerical inequalities in that artifact.

This strengthens the external analytic baseline and supplies reusable formal
linear algebra, but it does not strengthen the uniform-strip conclusion.  A
sparse `o(N)` set of off-line zeros is invisible to a density theorem and can
still determine the rightmost zero.  There is also a scale mismatch: a fixed
support such as `[-7/16,7/16]` produces only `O(T)` Gabor directions against
`N(T,2T)` of order `T log T`; the positive-proportion argument requires
support growing like `log T`.  For this program the lesson is sharper: trace
moments control the bulk, while a strip requires a new lower-spectral-edge or
single-exception-sensitive estimate.

The integration audit has nevertheless produced a genuine refinement of that
research boundary.  A varying support

```text
L = log(T/(2*pi)) + (2 log 2-1) + eta(T)
```

may enter a mesoscopic range (for example `eta(T)=theta log log T`, fixed
`0<theta<1`) while the unsimplified prime errors and smooth remote tail still
tend to zero; the resulting dimension exceeds the full local zero count.
Inside the sharp Gabor span, spending part of that surplus on vanishing
endpoint jets preserves exact Cauchy--Vandermonde interpolation and makes the
remote-zero operator exponentially small.  Thus the earlier dimension and
qualitative sharp-tail objections are not terminal.  What remains is exactly
an effective asymptotic rate for the signed carrier edge and a scale-matched
prime-side lower-edge estimate on the same constrained space.  These are not
independently sufficient gates: for a depth-`alpha` pair, write the actual
normalized carrier margin as `K=(X^alpha/L)r_T`, where `X=exp(L)`, and put
`B_X=osc(A_X)+(2/L)max|D_X|`.  Besides `E_remote=o(K)`, the scalar route needs
`B_X=o(X^alpha r_T)`.  A direct constrained Pick/Loewner route may avoid the
separate scalar bounds, but its normalized prime negative edge must still be
`o(K)` at that actual carrier scale.  Collision compactness proves that the
signed edge is strictly negative at each fixed
set of parameters without any zero-spacing assumption, but gives no rate.
The sharp arithmetic matrix has exact Loewner displacement rank at most two
before and after jet compression; its confluent diagonal remains
uncontrolled.  First and second moments, and even a long prefix of
exterior-power signs, do not supply that control.  See
[`ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md)
and
[`ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md).
The quantitative carrier target has since been narrowed twice.  Endpoint
jets suppress a distinguished pair in the padding collar at the same
exponential scale as the remote tail, so the zero under test must be
recentered in the core.  In the core, a bilinear Poisson construction gives
`K<<X^(2*alpha/3)` from counts alone.  The imported simple-line density
excludes that particular configuration, but a `k=7` periodic configuration
still obeys all count and density constraints and gives
`K<<X^(6*alpha/7)`.  Probing the same hypothetical zeros with Zeta23's legal
Montgomery--Taylor window shows that this `k=7` configuration has Frobenius
energy `asymp d*X^(12*alpha/7)`, contradicting the proved `O(d)` moment.
An exact residue-class diagonalization also proves that its least eigenvalue
really has magnitude `asymp X^(6*alpha/7)` after endpoint jets and any
count-bounded on-line filler; the upper carrier scale is not merely a loose
norm estimate.
Thus the density theorem removes the densest screen, and the moment theorem
removes the remaining regular positive-density screen; neither argument yet
controls a sparse or aperiodic screen around one exceptional pair.  See
[`ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md),
[`ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md`](../results/ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md),
[`ZETA23-FIXED-PERIODIC-MASK-SIGNED-EDGE-THEOREM-2026-08-11.md`](../results/ZETA23-FIXED-PERIODIC-MASK-SIGNED-EDGE-THEOREM-2026-08-11.md),
and
[`ZETA23-K7-GABOR-MOMENT-INCOMPATIBILITY-2026-08-11.md`](../results/ZETA23-K7-GABOR-MOMENT-INCOMPATIBILITY-2026-08-11.md).
At the opposite extreme, the exact one-pair problem is now closed on the
carrier side.  A unit-count sampling bound makes the entire simple on-line
Gram operator only polylogarithmic.  An explicit real binomial-tail packet
lies in the endpoint-jet space and retains the pair evaluation at distance
only `O(sqrt(mL/T))` from the amplifying endpoint, proving

```text
K >= X^(alpha-o(1))/L
```

when this is the only off-line pair in the carrier.  The first two Zeta23
moments are compatible with that large sparse edge.  Consequently any
remaining zero-side power screen must use at least one additional off-line
pair; neither on-line filling, endpoint jets, nor the bulk moments alone can
create it.  See
[`ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md`](../results/ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md).
That last zero-side possibility is now realized by a hostile-audited
artificial configuration.  A Gevrey-tapered `k=3` island has sublinear rank,
global off-line density `o(1)`, and a distinguished depth-`alpha` core pair,
yet

```text
0<K<=X^(2*alpha/3+o(1)).
```

It preserves the Riemann--von Mangoldt discrepancy and the leading
trace/Frobenius/pair-correlation moments.  Canonical logarithmic padding
supports the construction for every fixed `alpha<1/2`; even the weakest
admissible padding supports it for `alpha<3/8`.  Therefore the present count,
density, and two-moment inputs do not imply a full-power carrier edge.  This
does not assert that an Euler product can realize the island.  The exact
construction and independent endpoint/moment audit are in
[`ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md`](../results/ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md).

The symmetric two-lobe threshold is exact but conditional, and its universal
target premise is now refuted on the current bulk input class.  The original
dimension ledger suggested the formal right edge `0.597907...`; the sparse
`k=3` island first disproved target retention for `a<1/3`.  A sharper inward-
lobe construction closes the apparent gap above `1/3`: an exact-density,
Gevrey-tapered `k=2` island with terminal depth `alpha/2` satisfies all
current count, density, trace, Frobenius, and pair-correlation inputs while

```text
||Q|E_a||<=X^(alpha/2+o(1)),       every fixed a<1/2.
```

Thus the formerly advertised `alpha>1/4`, or `3/4+epsilon`, symmetric edge
is also only a refuted formal consequence of the present bulk hypotheses.
This artificial Gabor configuration is not asserted to be a zeta-zero set.

There is an exact positive frequency threshold behind the failure.  The
separated Hilbert--Ingham inequality is stable above lobe width `1/3` for
`k=3` spacing and above `1/2` for exact-density `k=2` spacing.  This motivates
an asymmetric conditional escape: take a free lobe of length `aL`, `a>1/2`,
and a short seed lobe `bL`, `b=o(1)`.  Their center separation is
`dL`, `d=1-(a+b)/2`; the carrier/same-lobe comparison is

```text
alpha*d>a/2,
equivalently alpha>a/(2-a-b).
```

Letting `a` decrease to `1/2` and `b` to zero gives the formal right edge
`5/6+epsilon`.  This formal premise is also refuted on the
current bulk class: the power-length varying-depth `k=3` island has full edge
only `X^(2*alpha/3+o(1))`, while the center separation above tends to `3/4`.
The exact periodic mirror is a point-packet identity.  It transfers with only
`X^o(1)` loss to a polylogarithmic `k=2` island using inverse-polylog packet
width, but uniform phase matching across the power-length `k=3` island forces
a narrow packet whose normalized carrier loses a fixed power.

The first present target not contradicted by that cap uses packet separation
`d_*<2/3` inside the asymmetric lobes.  Its comparison is

```text
alpha*d_*>a/2.
```

Taking `a` down to `1/2` and `d_*` up to `2/3` gives the conditional right
edge `7/8+epsilon`.  The latest augmented-row audit shows that this target is
not countermodel-safe on the abstract operator-ledger class either.  In the exact mirror
block for one reflected pair, positive-row nulling fixes the completed
aggregate cross scalar at the nonzero carrier value; even one-real-equation
cancellation is infeasible.  Its Frobenius cost is `o(N)` for
`alpha<1/2,d_*<2/3`, so the abstract leading count and moment ledgers all
survive.  The selected block now has a normalized asymmetric
Paley--Wiener/Gabor realization: equal fixed-width packets separated by
`d_*L` compress the exact reflected-pair kernel to
`(2*A_alpha^2/L)[[1,cosh(alpha*d_*L)],[cosh(alpha*d_*L),1]]`.  Lorentz
re-factorization gives the balanced mirror rows, and a common binomial
cutoff transfers them to the growing endpoint-jet grid with superpolynomial
error.  This still does not realize the aggregate row using the actual
positive von Mangoldt atoms.  Thus a
`7/8` implication must explicitly assume a collision-stable actual-zeta
target theorem which remains feasible after adjoining the actual aggregate
arithmetic row.  Pointwise prime-power nulling and its Wiener-atomic theorem
are a sufficient overconstraint, not an independent intrinsic gate.  None of
the `0.597907...`, `3/4`, `5/6`, or `7/8` edges has been proved for zeta.  See
[`ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md`](../results/ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md),
[`ZETA23-TWO-LOBE-ONE-THIRD-SIGNED-GATE-2026-08-11.md`](../results/ZETA23-TWO-LOBE-ONE-THIRD-SIGNED-GATE-2026-08-11.md),
[`ZETA23-ASYMMETRIC-TWO-LOBE-HALF-PERIOD-GATE-2026-08-11.md`](../results/ZETA23-ASYMMETRIC-TWO-LOBE-HALF-PERIOD-GATE-2026-08-11.md),
and
[`ZETA23-LOCAL-K2-CLUSTER-MOMENT-BARRIER-2026-08-11.md`](../results/ZETA23-LOCAL-K2-CLUSTER-MOMENT-BARRIER-2026-08-11.md),
as corrected by
[`ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md`](../results/ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md)
and
[`ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md`](../results/ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md).
The selected-pair realization is
[`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](../results/ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md).
The collateral audit adds one proved normalized statement and one explicitly
weaker abstract obstruction.  Collateral pairs below depth
`alpha*d-epsilon` are subcarrier by strip sampling, but present density and
local-count inputs allow one `alpha-o(1/L)` near-tie.  A two-pair abstract
hyperbolic block uses that one row to create a transverse reservoir with
`o(N)` moment cost.  The exact abstract orientation is now excluded at
carrier scale for separated fixed-width packets after **every** represented
positive row is imposed: normalized near-tie rows have a collision-stable
Hermite limit and their leading mirror cross terms retain one sign.  That
sign does not survive the target-only quotient.  A strictly deepest target
plus two slightly shallower pairs at ordinate gaps `+/-pi/D`, with
`epsilon_L*D->0`, gives a genuine normalized fixed-width/Gabor screen of
`(1-o(1))*kappa` on the target carrier.  Current count, density, simplicity,
and leading-moment inputs permit this sparse three-pair configuration, but do
not assert that zeta realizes it.  A universal positive average over packet
separations cannot repair the phase flip without importing zero-delay mass
and losing the entire fixed-power carrier; only the finite-list adaptive
separation problem remains open.  See
[`ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md`](../results/ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md),
[`ZETA23-NEAR-TIE-GRAM-AND-MIRROR-ALIGNMENT-2026-08-12.md`](../results/ZETA23-NEAR-TIE-GRAM-AND-MIRROR-ALIGNMENT-2026-08-12.md),
[`ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md`](../results/ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md),
and
[`ZETA23-SEPARATION-AVERAGE-POSITIVE-COSINE-NOGO-2026-08-12.md`](../results/ZETA23-SEPARATION-AVERAGE-POSITIVE-COSINE-NOGO-2026-08-12.md).
The conditional quantifier is audited in
[`ZETA23-CONDITIONAL-SEVEN-EIGHTHS-LOGIC-AUDIT-2026-08-12.md`](../results/ZETA23-CONDITIONAL-SEVEN-EIGHTHS-LOGIC-AUDIT-2026-08-12.md).

The explicit endpoint-flat packet also makes the surviving arithmetic gate
one-dimensional.  Its completed form retains every pole, gamma, continuum,
and prime-power term, and its only power-sized contribution is a centered
smooth von Mangoldt polynomial at length `Y`.  A depth-`alpha` exclusion
requires `o(Y^alpha)`, while the best directly applicable unconditional
estimate is `Y^(1/2-o(1))`.  For a single witness the whole cross-prime sum
is exactly one scalar `<ell,B_pr r>`, so cancelling it needs only one real
equation (or one convenient complex row), not one row per prime power.
After the positive-zero constraints, however, that aggregate row can be
parallel to the selected negative row.  The completed arithmetic operator
equals the zero-side operator, and its leading off-diagonal block in the
one-pair quotient is exactly the target rank-one block.  Thus an algebraic
dimension surplus does not bound the required augmented target angle.
At the asymmetric center `Y=X^(1-(a+b)/2)`, a direct fixed saving below
`Y^alpha` is itself the desired strip-strength residue estimate at the
hypothetical zero; exponent-pair estimates do not close this gate.  Prime
nulling is meant to bypass that estimate, not to derive it from dimension.
See
[`ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`](../results/ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md)
and
[`ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md`](../results/ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md).
The stronger pointwise construction remains mathematically valid: its exact
factorization norm is Wiener `sum|h_k|`, and finite duality gives the stated
`l^infinity` prime-log extremal.  It is now retained only as an optional
overconstrained route; see
[`ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`](../results/ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md).
The subsequent positive-QP audit separates that full extremal from its
arithmetic-progression subroute.  For the actual nodes `u_j`, a depth-`r`
positive antipode is equivalent to a symmetric probability measure on
`{0} union +/-H` whose Fourier transform vanishes at every `u_j` and whose
mass at zero is `r/(1+r)`.  If `A_H` is the corresponding one-sided Delsarte
antenna value, strong duality gives the exact identities
`p_*=1/A_H` and `r_+=1/(A_H-1)`.  A gapped Bernoulli convolution proves legal
feasibility but has depth `1/(2^M-1)`; any one-sided product with only
bounded or polylogarithmically many groups has the same exponential-loss
barrier.  Conversely, tent weights prove that the full continuum problem for
independent uniform nodes is KILL with failure probability exponentially
small in `M r^2`.  The missing step is thus a deterministic, sign-sensitive
estimate of `A_H` for the actual prime-power logarithms, not merely a
finite-aperture AP recurrence.  KMT's natural von Mangoldt twist covers the
entire polynomial aperture and gives enough covariance to repair one bad
packet exactly with a positive tilt, but it gives only logarithmic saving for
fixed coefficients and does not control simultaneous adaptive packets.
Moreover, the proposed packet-count-to-Gram upgrade is false: a binomial
finite difference makes consecutive packet Gramians exponentially ill
conditioned, and an abstract critical sign design shows that even perfect
unprojected orthogonality need not leave a carrier gap.  The minimum
packet-zeroing dual is exactly the normalized carrier residual; controlling
it on the whole band is equivalent to the original one-sided Delsarte
certificate.  Applying KMT termwise pays the sharp source-rank factor
`R*delta_KMT^2`; replacing it by a natural modulus saving `Y^-c` on the
half-power-to-top subband would already imply the strip
`Re(s)>1-(33c/50)^2` by Turán.  Thus a scalar fixed-power
upgrade is not an intermediate shortcut.  Local covariance repairs a
fixed-radius packet cluster, but stable simultaneous square repair forces a
block of size `Omega(R)` and termwise KMT then pays `eta*R`; the
coefficient-sensitive residual is the live statement.  Neither PROMOTE nor
KILL is presently proved; see
[`ZETA23-QP-SPECTRAL-NULL-DELSARTE-AND-GROUPING-GATE-2026-08-14.md`](../results/ZETA23-QP-SPECTRAL-NULL-DELSARTE-AND-GROUPING-GATE-2026-08-14.md),
[`ZETA23-QP-PROJECTED-GRAM-CLUSTER-AND-SOURCE-GATE-2026-08-14.md`](../results/ZETA23-QP-PROJECTED-GRAM-CLUSTER-AND-SOURCE-GATE-2026-08-14.md),
[`ZETA23-QP-ACTUAL-PRIME-POSITIVE-WEIGHT-BARRIER-2026-08-14.md`](../results/ZETA23-QP-ACTUAL-PRIME-POSITIVE-WEIGHT-BARRIER-2026-08-14.md),
[`ZETA23-QP-ACTUAL-PRIME-MULTIPLICATIVE-EXPLICIT-FORMULA-GATE-2026-08-14.md`](../results/ZETA23-QP-ACTUAL-PRIME-MULTIPLICATIVE-EXPLICIT-FORMULA-GATE-2026-08-14.md),
[`ZETA23-QP-KMT-CLUSTER-SQUARE-RANK-TAX-2026-08-14.md`](../results/ZETA23-QP-KMT-CLUSTER-SQUARE-RANK-TAX-2026-08-14.md), and
[`ZETA23-QP-ACTUAL-NODE-DELSARTE-GRAM-LITERATURE-HOSTILE-AUDIT-2026-08-14.md`](../results/ZETA23-QP-ACTUAL-NODE-DELSARTE-GRAM-LITERATURE-HOSTILE-AUDIT-2026-08-14.md).
The exact one-way strip bridge is now pinned down.  A uniform strip of width
`delta` makes the smooth von Mangoldt shell weights a positive Delsarte
certificate at every power `c<delta`.  No reverse follows from node data:
`zeta(s)(1+p^(beta-s))` retains positive Dirichlet coefficients and every
prime-power node location while inserting arbitrarily high zeros on
`Re(s)=beta`; an explicit nonzero Fejer family separately shows that coherent
moving-band certificates need not control fixed ordinates.  The centered von
Mangoldt discrepancy has a separate exact strip equivalence, but it is not a
QP equivalence.  See
[`ZETA23-QP-STRIP-BRIDGE-AND-SUPPORT-NONIMPLICATION-2026-08-15.md`](../results/ZETA23-QP-STRIP-BRIDGE-AND-SUPPORT-NONIMPLICATION-2026-08-15.md).

The proposed reverse adapter required a normalization repair.  The old
probability-normalized directional depth is identically one on actual primes
because a half-integer center can place a singleton prime at phase `-1`; it
cannot be compared to a QP radius tending to zero.  With the correct
`N`-mass normalization, phase localization proves that a Turan prime-modulus
event yields a negative actual-shell event.  The weakest surviving statement
is the thresholded, full-band implication `LTRAD_full(c,d)`: a negative event
of mass at least `N^-d` must force full QP radius at least `N^-c`.

Two nontrivial pieces of that implication are proved.  Every one-sided actual
prime cell returns to the positive side on the full legal band.  More
generally, a two-cluster divided-difference frame handles all cross-shell gaps
down to `Y^-2` and first proves transverse feasibility for every calibrated
residual.  The integer-log structure then gives a stronger fourth-moment
theorem.  At the full aperture `A=50/33`, bounded prime-power product
multiplicity yields

```text
s_v, r_+(H_Y;S_Y) >> sqrt(log Y) Y^(-49/66).
```

The exponent improves the dimension-only value `1` by `17/66`.
Near-reflection endpoints number only `Y^(16/33+o(1))`; they are included in
the theorem, and a Turan-long event also survives deleting them.  The usual
fixed `2k`-moment hierarchy is optimized at `k=2`, so higher standard moments
do not improve `49/66`.  A separate signed cubic incidence argument reaches
the same exponent, while an exact binning lower bound shows that unsigned
short-product energy cannot improve the power `2-A`.  A further gain must use
signed packet cancellation or joint calibrated leverage--skew control.  For
a legal singleton residual there is also a rigorous VK subpower upper bound,
but no matching power upper is known.  On the construction side, an exact
actual-log rigidity theorem shows that worst-case Lipschitz transfer of a
harmonic Fejer core is limited to `L<<Y^(16/33)` terms at this aperture, so
that method cannot certify a floor below `Y^(-16/33)`.  This is a method
ceiling, not an actual upper bound for `s_v`.

Two restricted arithmetic sectors now break the `49/66` exponent, without
changing the balanced full-shell statement.  First, for any central integer
packet `0<|n-Y|<=H<=Y^(1/2-epsilon)`, odd half-integer parity removes every
cubic resonance, including reflected divided-difference modes, and gives

```text
s_v, r_+ >> M_H^(-1/2).
```

Second, at a prime half-center `Y=q/2`, with `q` odd prime, Burgess
cancellation for the one-sided actual prime-power shell gives

```text
s_v^+, r_+^+ >> q^(-755/1056-o(1))
```

for every prime `q`; an eighth-moment multiplicative-large-sieve argument
improves this to `q^(-361/528-o(1))` for a density-one set of prime centers.
These are coordinate-projected/strongly imbalanced sector theorems.  They do
not control balanced two-sided duals, composite centers, or the unrestricted
QP radius.  See the
[central-packet theorem](../results/ZETA23-QP-CENTRAL-PACKET-SQRT-DIMENSION-TRANSVERSE-THEOREM-2026-08-15.md),
[prime-center Burgess theorem](../results/ZETA23-QP-PRIME-CENTER-ONE-SIDED-BURGESS-CUBIC-SAVING-2026-08-15.md), and
[independent hostile audit](../results/ZETA23-QP-PRIME-CENTER-BURGESS-CUBIC-HOSTILE-AUDIT-2026-08-15.md).

The sector-combination audit makes the remaining obstruction explicit.  Every
fixed-power side-dominant or central-dominant direction improves `49/66`, but
balanced far-side vectors retain the rank-one tensor

```text
hat(psi)(B log(abc/Y^3)),       |8abc-q^3| << q^3/B.
```

Its current norm is only `O(sqrt(R))`.  Passing to characters modulo `q^3`
makes the residual identity exact, but Parseval forces the separate-character
closure to cost `sqrt(qR)`, which is worse; this is a method barrier, not an
actual lower bound.  See the
[sector-combination gate](../results/ZETA23-QP-SECTOR-COMBINATION-BALANCED-CROSS-GATE-2026-08-15.md)
and [balanced-character barrier](../results/ZETA23-QP-BALANCED-ALL-PLUS-CHARACTER-METHOD-BARRIER-2026-08-15.md).

Thus transverse return exists at a proved fixed-power scale, still far from
the strip-scale exponent near `.019`.  A hereditary Fejer hard-core construction
shows that cardinality, ordering, and long-interval negativity alone cannot
remove this dimension loss; universal Sidon interpolation on the polynomial
band likewise costs `Y^(1/2-o(1))`.  Actual-prime `LTRAD_full`, QP, a reverse
QP-to-strip theorem, and the strip remain open.  See the
[mass-normalization gate](../results/ZETA23-QP-RADIALIZATION-MASS-NORMALIZATION-GATE-2026-08-15.md),
[cluster-frame theorem](../results/ZETA23-QP-TRANSVERSE-RETURN-CLUSTER-FRAME-GATE-2026-08-15.md),
[fourth-moment scale theorem](../results/ZETA23-QP-TRANSVERSE-FOURTH-MOMENT-AND-ACTUAL-UPPER-GATE-2026-08-15.md),
[mixed-cubic barrier](../results/ZETA23-QP-TRANSVERSE-MIXED-CUBIC-INCIDENCE-BARRIER-2026-08-15.md),
[Fejer-transfer rigidity gate](../results/ZETA23-QP-ACTUAL-FEJER-TRANSFER-RIGIDITY-GATE-2026-08-15.md),
[near-reflection audit](../results/ZETA23-QP-RADIAL-COVARIANCE-NEAR-REFLECTION-AUDIT-2026-08-15.md),
[hereditary obstruction](../results/ZETA23-QP-LTRAD-HEREDITARY-BOOSTING-GATE-2026-08-15.md), and
[Sidon support-entropy gate](../results/ZETA23-QP-SIDON-POSITIVE-INTERPOLATION-SUPPORT-ENTROPY-NOGO-2026-08-15.md).
Unconditionally, the positive tent on the actual prime-power nodes gives only
the Vinogradov--Korobov subpower floor, not the fixed power required by QP.
The coefficient-sensitive square estimate clears every term except a
weighted repeated-difference correlation; a Fejer argument excludes the
stable uniform critical-AP extremizer but not general mixtures.  An
all-line Fourier-positive signed kernel cannot amplify the subpower result:
Turán capacity forces the suppressed mass to reappear off resonance.  See
the [tent theorem](../results/ZETA23-QP-TENT-EXPLICIT-FORMULA-STRIP-AND-AMPLIFICATION-GATE-2026-08-15.md),
[cross-Gram gate](../results/ZETA23-QP-COEFFICIENT-SENSITIVE-CROSS-GRAM-MOMENT-GATE-2026-08-15.md),
and [signed-kernel barrier](../results/ZETA23-QP-SIGNED-KERNEL-CAPACITY-GATE-2026-08-15.md).
The complete current frontier is consolidated in
[`UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md`](../results/UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md).
The subsequent structural escape census tests positive multi-witness and
multiscale ensembles, unused quadratures, randomization, local gluing,
nonlinear determinant/Pick tests, operator preconditioning and functional
calculus, shifted de Branges forms, collateral-zero reservoirs, critical
pole/main resonance, and Mellin-scale filters.  None
supplies a free closure.  All surviving versions require a carrier-sized
target-transverse component of the **actual** compressed
prime/collateral operator, or a direct fixed-power arithmetic theorem already
of strip strength.  See
[`ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md`](../results/ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md).
A category-theoretic consolidation now reduces that census, together with the
older local-gluing and trace/polarization branches, to four exact lemmas:
positive constraints factor through dagger kernels and leave one
carrier-grade transverse class; conservative adapters preserve the original
sign problem while lossy ones do not reflect it and nonlinear ones create new
mixed-place correlations; local probe cones and low moments need not reflect
global positivity; and trace/supertrace or functional-equation duality does
not construct a positive polarization.  After carrier normalization the
remaining datum is the actual prime/collateral remainder in the carrier
grade.  When that normalized remainder is uniformly bounded it defines one
corona class `tau`; if it is unbounded, that carrier-or-larger growth is a
separate analytic case rather than a morphism of the corona category.  All
proved subcarrier terms vanish in either formulation.  This is a structural
consolidation, not a strip theorem.  See
[`ZETA23-CATEGORICAL-CONSOLIDATION-FOUR-LEMMA-2026-08-12.md`](../results/ZETA23-CATEGORICAL-CONSOLIDATION-FOUR-LEMMA-2026-08-12.md),
with its operator-level dagger-kernel formulation in
[`ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md`](../results/ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md)
and independent scope audit in
[`CATEGORY-THEORETIC-CONSOLIDATION-REFEREE-AUDIT-2026-08-12.md`](../results/CATEGORY-THEORETIC-CONSOLIDATION-REFEREE-AUDIT-2026-08-12.md).
A second categorical pass turns those lemmas into a search grammar with five
possible nonformal inputs: relative order reflection, a carrier-grade
transverse arithmetic term, a signed nonlinear cross-effect, an independently
positive polarization, or a carrier-conservative limit/index.  This prunes
ordinary sheaf gluing, bare derived or Tannakian structure, generic
`K`-theory, positive mixtures, higher exterior powers without correlation
estimates, and weak/trace limits as free sources of a strip.  Cross-aware
pair-groupoid descent and ultraproduct/corona language remain honest
containers, but they still owe the same uniform arithmetic order theorem.
See
[`ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md`](../results/ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md)
and the broader stress test
[`ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md`](../results/ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md).

That pass also leaves three concrete positive experiments.  Local probes need
reflect order only on a zero-independent arithmetic operator system, not on
all Hermitian matrices; exact or approximate completely positive recovery is
a finite Choi-matrix test for this.  For the actual one-real aggregate
constraint, the sharp remainder test is the **one-sided carrier-slice support**
`sup Tr(R Gamma)`, not the two-sided norm of `R`.  A Stinespring covariance is
a canonical positive multiplicative defect worth testing only if it enters the
completed arithmetic identity with the required sign.  Finally, a
zero-independent positive metric satisfying

```text
-epsilon G <= A*G+GA-G <= epsilon G,       epsilon<1,
```

would already confine `Re(lambda)` to
`[1/2-epsilon/2,1/2+epsilon/2]`; exact RH-level polarization is unnecessary.
No such recovery, covariance identity, or quasi-polarization is currently
proved for zeta.  The exact theorem cards and fail-fast tests are in
[`ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md`](../results/ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md).
The expanded package has independent verdict **PASS AFTER PATCHES** in
[`CATEGORY-THEORETIC-SEARCH-PRUNING-REFEREE-AUDIT-2026-08-12.md`](../results/CATEGORY-THEORETIC-SEARCH-PRUNING-REFEREE-AUDIT-2026-08-12.md).
Those proposed admissions were executed first on the smallest
zero-independent fixtures and then on an actual-coefficient high-height
sharp-Gabor model.  The first asymmetric two-packet arithmetic system is all
of `Sym_2(R)`, so no fixed finite scalar-probe cover reflects its positive
cone; parity CP recovery merely reads the original two eigenvalues, and the
natural Stinespring covariance is exactly the old Schur coupling squared.
Any ungraded polarization model retaining invariant pole/Tate eigenvalues
`0,1` has defect at least one; the semilocal prime--gamma scaling model has
defect zero only because its on-line multiplication spectrum is built in,
with no zeta-divisor identification.

The high-height execution produced a material correction to the remaining
carrier route.  If `K_ar,T` is the completed prime/pole/gamma matrix, `N_T`
the selected rank-one carrier, and `S_T` nulls only the hypothetical target's
positive row, then the target-subtracted operator is exactly

```text
R_full,T=N_T+K_ar,T|S_T.
```

Hence its one-sided support is baseline-contaminated:

```text
q_eta=inf_(mu>=0) Phi_eta(mu),
h_eta(R_full,T)=eta+inf_(mu>=1) Phi_eta(mu).
```

Target subtraction deletes the dual interval `[0,1)` and adds the carrier
baseline; it supplies no independent collateral theorem.  The surviving
quantity is the direct constrained arithmetic edge `q_eta(K_ar,T)`.  A
low-memory fixture retaining every active von Mangoldt prime power and the
pole and gamma terms reproduced the independent completion identity to about
`4e-14` and found positive `q_eta` at five scan heights `T=32,...,512`.
Those are floating diagnostics at hypothetical scan points, not interval
certificates or evidence for a uniform strip.

The smallest honest closing package now has two independent halves: prove a
uniform arithmetic admission `q_eta>=0`, and prove that an actual off-strip
target would force `q_eta<0` by excluding carrier-scale deep/collateral
screening.  Current estimates prove neither uniformly; at full carrier the
arithmetic half is the same centered von Mangoldt scalar already known to be
strip-strength.  The first adversarial execution of this corrected target
covered 61,896 full-carrier and 11,565 sub-full finite configurations, found
no negative, and used 192-bit Arb arithmetic to prove that its closest sampled
full-carrier value was still positive.  This is a rigorous finite
falsification pipeline, not evidence for a uniform sign.  An exact
two-dimensional Ritz theorem further reduces sub-full admission to the joint
orientation inequality

```text
theta*r+(1-theta)*d
 +2*sqrt(theta*(1-theta))*abs(c) >= -epsilon*kappa.
```

For a prime-independent companion the three entries remain linear completed
prime/pole/gamma scalars; bounding them separately by KMT loses the joint
orientation and returns the same fixed-power barrier.  A Lanczos companion
captures almost all of the finite edge but introduces quadratic and cubic
prime correlations.  The target-only phase-flip theorem above shows that the
matching divisor-isolation half cannot be obtained from current packet
geometry and bulk zero statistics alone.  See
[`ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md`](../results/ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md),
[`ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md`](../results/ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md),
and
[`ZETA23-DIRECT-CARRIER-SLICE-FRONTIER-SYNTHESIS-2026-08-12.md`](../results/ZETA23-DIRECT-CARRIER-SLICE-FRONTIER-SYNTHESIS-2026-08-12.md),
as updated by
[`ZETA23-THREE-STEP-SUBFULL-CARRIER-ITERATION-SYNTHESIS-2026-08-12.md`](../results/ZETA23-THREE-STEP-SUBFULL-CARRIER-ITERATION-SYNTHESIS-2026-08-12.md).
This high-height package has independent verdict **PASS AFTER PATCHES** in
[`HIGH-HEIGHT-CARRIER-SLICE-REFEREE-AUDIT-2026-08-12.md`](../results/HIGH-HEIGHT-CARRIER-SLICE-REFEREE-AUDIT-2026-08-12.md).
The three-step iteration and phase-flip follow-on have independent verdicts
**PASS AFTER PATCHES** in
[`ZETA23-THREE-STEP-DIRECT-CARRIER-PROGRAM-REFEREE-AUDIT-2026-08-12.md`](../results/ZETA23-THREE-STEP-DIRECT-CARRIER-PROGRAM-REFEREE-AUDIT-2026-08-12.md)
and
[`ZETA23-PHASE-FLIP-AND-SEPARATION-AVERAGE-REFEREE-ADDENDUM-2026-08-12.md`](../results/ZETA23-PHASE-FLIP-AND-SEPARATION-AVERAGE-REFEREE-ADDENDUM-2026-08-12.md).
The earlier admission package has independent verdict **PASS AFTER PATCHES**
in
[`CATEGORICAL-ADMISSION-TESTS-REFEREE-AUDIT-2026-08-12.md`](../results/CATEGORICAL-ADMISSION-TESTS-REFEREE-AUDIT-2026-08-12.md).

The latest carrier iteration closes one previously open geometric step
exactly.  Given a hypothetical target at ordinate `gamma`, center an odd
critical grid at `gamma` and choose the endpoint-jet order even.  The selected
positive row and inherited Hahn anchor are even, while the negative carrier
row is odd.  Hence the inherited-anchor threshold is exactly

```text
theta_*=1,
dim S_m^odd=(d-m-1)/2.
```

Choosing even `m` from the outset is compatible with the existing
endpoint-flat packet theorem and retains carrier `X^(alpha-o(1))/L`; no
unproved Hahn-tail asymptotic or one-step projection ratio is needed.  The
same parity reduces the completed arithmetic square to a cosine-only
von-Mangoldt--continuum correlation.  It does not sign that correlation, and
unknown collateral positive rows need not preserve parity.  See
[`ZETA23-CENTERED-EVEN-JET-PARITY-COMPANION-2026-08-12.md`](../results/ZETA23-CENTERED-EVEN-JET-PARITY-COMPANION-2026-08-12.md).

That cosine correlation is now explicit: for the unprojected centered
carrier it is a single linear combination of `P_T` and `P_T'` at
`1/2+/-alpha+i*gamma`, with the sinh-tent autocorrelation as weight.  A
rigorous Arb value disproves pointwise positivity of the evenized completed
multiplier, and a Jensen zero-count theorem shows that carrier-local positive
height averaging cannot annihilate all prime logs.  The functional equation
reduces the completed expression to a signed curvature of `log|Xi|`, not a
square; an exact symmetric-quartet countermodel proves that functional
equation, reality, order, and critical-line phase alone cannot supply the
sign.  See
[`ZETA23-CENTERED-COSINE-ONE-SQUARE-ARITHMETIC-GATE-2026-08-12.md`](../results/ZETA23-CENTERED-COSINE-ONE-SQUARE-ARITHMETIC-GATE-2026-08-12.md)
and
[`ZETA23-CENTERED-SINH-TENT-FUNCTIONAL-EQUATION-NOGO-2026-08-12.md`](../results/ZETA23-CENTERED-SINH-TENT-FUNCTIONAL-EQUATION-NOGO-2026-08-12.md).

A natural positive trigonometric amplifier does not restore the missing sign.
The extremal polynomial `3+4*cos(theta)+cos(2*theta)` preserves the matched
negative quartet at full scale, but the exact sinh-tent prime weight changes
sign, while its unavoidable constant harmonic creates a larger same-sign
pole term.  Within this harmonic ledger, cancelling that pole remotely costs
quadratic coefficient mass.  See
[`ZETA23-HARMONIC-CENTER-SINH-TENT-AMPLIFICATION-NOGO-2026-08-12.md`](../results/ZETA23-HARMONIC-CENTER-SINH-TENT-AMPLIFICATION-NOGO-2026-08-12.md).

On the divisor side, coherent phase transport removes the previously found
`+/-pi/D` obstruction and, more generally, every bounded rescaled
microscopic collateral cluster.  One fixed-degree, endpoint-flat packet
keeps all mixed terms, signs an arbitrary number of such near-confluent rows
in the favorable direction, and retains carrier `X^(alpha*d-o(1))`.  This is
a genuine geometric advance.  Moreover, balanced bipartite assignment of
collateral conditions to the two endpoint legs removes the apparent
same-state square loss: the selected positive-row equation pays one total
Blaschke product, and fixed polynomially-conditioned lists have an exact real
compact realization.  A unit-width growing list still requires a uniform
compact discrete-Pick/phase-cell theorem.  Conditional on one effective
condition per phase cell, the corrected density ledger retains exponent
`0.0133834...` at `alpha=1/2,d=2/3`; this is not yet an actual-zeta bound.
See
[`ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md`](../results/ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md),
[`ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md`](../results/ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md),
and
[`ZETA23-BLASCHKE-DENSITY-ISOLATION-FACTOR-TWO-GATE-2026-08-12.md`](../results/ZETA23-BLASCHKE-DENSITY-ISOLATION-FACTOR-TWO-GATE-2026-08-12.md).
An exact one-zero-per-cell inner lattice does sign the full collateral
continuum, but it spends the entire carrier.  Finite dummy completion plus
ordinary delay repair obeys a sharp phase/exponent conservation law.  The
surviving broad route is therefore tailored discrete Pick interpolation on
the actually occupied clusters, not uniform lattice completion; see
[`ZETA23-GLOBAL-PHASE-CELL-COMPRESSION-PICK-LATTICE-GATE-2026-08-12.md`](../results/ZETA23-GLOBAL-PHASE-CELL-COMPRESSION-PICK-LATTICE-GATE-2026-08-12.md).
For the exact half-disk Pick problem, an alternating critical configuration
has an explicit inner solution with target amplitude `1/sqrt(cosh(a))`, the
half-product exponent.  A separate five-point cell forces double-zero local
behavior, so one simple root per occupied cell is false; the global
half-product theorem remains open.  See
[`ZETA23-HALF-DISK-PICK-EXTREMAL-PROBE-2026-08-12.md`](../results/ZETA23-HALF-DISK-PICK-EXTREMAL-PROBE-2026-08-12.md).
Finite clusters can force every prescribed fixed Schur-jet order, but no
theorem multiplies those local losses across a growing collection of cells.
The dimension-corrected density ledger leaves small factor-two clusters
affordable and becomes adverse only for sufficiently large fixed
multiplicity, conditionally on such multiplication.  See
[`ZETA23-TAILORED-DISCRETE-PICK-JET-OBSTRUCTION-2026-08-12.md`](../results/ZETA23-TAILORED-DISCRETE-PICK-JET-OBSTRUCTION-2026-08-12.md).

The arithmetic side has also been reduced more sharply.  A positive spectral
measure solving the active prime-power cosine moments descends, through a
compact positive-definite multiplier and continuous spectral factorization,
to an honest compact scalar two-lobe packet with the predicted carrier and
exact cross-prime zeros.  If the upper spectral cap is removed, explicit
prime-coordinate torus densities solve all active prime-power moments with
`r>>1/log Y` for rational centers, and scalar Kronecker density gives a
finite atomic realization.  The unresolved condition is return before the
polynomial cap `T=Y^(1/d)`.  Exact Riesz-product norms

```text
||P_r||_A=exp(Theta(r*M)),
||P_r||_2^2=exp(Theta(r^2*M))
```

show that the audited bounded-degree absolute and stably Gram-corrected
transfers stop at `Y^(-1+o(1))` and `Y^(-1/2+o(1))`.  They do not upper-bound
the unrestricted finite-band convex problem.  The direct ordinary
Montgomery-mean-value/derivative conversion also stops exactly at the
conductor transition: for every fixed moment order the normalized exponent
is `max(1/d,q)-q>=0`, and the explicit `4^q q!` uniform form shows that
growing the order does not rescue this estimate.  See
[`ZETA23-PRIME-LOG-EARLY-RETURN-MEAN-VALUE-GATE-2026-08-12.md`](../results/ZETA23-PRIME-LOG-EARLY-RETURN-MEAN-VALUE-GATE-2026-08-12.md).
The hostile-audited synthesis
is
[`ZETA23-BREAKTHROUGH-SPRINT-CENTERED-PARITY-AND-PRIME-MOMENT-SYNTHESIS-2026-08-12.md`](../results/ZETA23-BREAKTHROUGH-SPRINT-CENTERED-PARITY-AND-PRIME-MOMENT-SYNTHESIS-2026-08-12.md),
with the prime-moment theorem cards
[`ZETA23-POSITIVE-SPECTRAL-PRIME-NULL-SQUARE-ROOT-GATE-2026-08-12.md`](../results/ZETA23-POSITIVE-SPECTRAL-PRIME-NULL-SQUARE-ROOT-GATE-2026-08-12.md)
and
[`ZETA23-PRIME-RIESZ-PRODUCT-SCALAR-ORBIT-GATE-2026-08-12.md`](../results/ZETA23-PRIME-RIESZ-PRODUCT-SCALAR-ORBIT-GATE-2026-08-12.md).
The new bipartite divisor filters are algebraically compatible with the
arithmetic rows at fixed complexity.  Exact branch-stable nulling is
equivalent to Hermite prime zeros through order `2K`; efficient chosen
filters reduce the growing problem to a twisted moment-hull inradius or an
aggregate Schur angle.  Neither uniform estimate is known.  See
[`ZETA23-BIPARTITE-BLASCHKE-ARITHMETIC-COUPLING-GATE-2026-08-12.md`](../results/ZETA23-BIPARTITE-BLASCHKE-ARITHMETIC-COUPLING-GATE-2026-08-12.md).

These results materially narrow the program but do not tighten a known bound
on zeta zeros.  A strip still requires a uniform centered one-square
arithmetic sign and an actual-zeta collateral support-function bound on the
same state.

The logically opposite hypothesis was also audited: failure of every fixed
strip means `Theta=sup Re(rho)=1`, which is strictly stronger than merely
falsifying RH.  No accepted theorem proves even one zeta zero with
`Re(rho)>1/2`, and neither universality nor current omega theorems supplies
that conclusion.  See
[`ZETA23-NO-UNIFORM-STRIP-OPPOSITE-HYPOTHESIS-AUDIT-2026-08-12.md`](../results/ZETA23-NO-UNIFORM-STRIP-OPPOSITE-HYPOTHESIS-AUDIT-2026-08-12.md).
The exact remaining Schur and prime-polynomial theorem cards are
[`ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md`](../results/ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md)
and
[`ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`](../results/ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md).
For these exact scalar polynomials, the sharp prime-twist theorem of
Klurman--Mangerel--Teravainen does yield the unconditional transition-scale
bound

```text
B_X << X^(1/2)/(log X)^(3/10),     X=T log(T)^O(1).
```

This is a genuine logarithmic improvement over absolute values, but its power
exponent tends to `1/2`; it neither matches an unknown small carrier factor
`r_T` nor excludes a zero at any fixed depth below `1/2`.  The exact Abel
transfer, derivative weight, and quantifier audit are in
[`ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md`](../results/ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md).
The completed Pick audit restores the continuum pole term exactly and still
obtains only a normalized `sqrt(X)/(log X)^(13/10)` certificate.  A separate
cutoff calculus recovers a complex triangular prime shell from continuum
values of the two real Loewner observables, but the available cutoffs occupy
only `X=T^(1+o(1))` and the saving remains logarithmic; this misses both
fixed-power requirements in Turan's localization criterion.  See
[`ZETA23-COMPLETED-CONSTRAINED-PICK-KMT-OBSTRUCTION-2026-08-11.md`](../results/ZETA23-COMPLETED-CONSTRAINED-PICK-KMT-OBSTRUCTION-2026-08-11.md)
and
[`ZETA23-VARYING-CUTOFF-OFFSET-TURAN-BLINDNESS-2026-08-11.md`](../results/ZETA23-VARYING-CUTOFF-OFFSET-TURAN-BLINDNESS-2026-08-11.md).
Nor do the endpoint jets automatically improve this exponent.  Their
codimension is `m`, so interlacing can discard only `m` lower-edge
eigenvalues; an exact leverage estimate shows that all but at most
`m/epsilon` coordinate directions remain within
`O(sqrt(epsilon)*L*B_X)` of their original prime diagonal.  This finite
dimensional obstruction is proved in
[`ZETA23-ENDPOINT-JET-PRIME-COMPRESSION-OBSTRUCTION-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-PRIME-COMPRESSION-OBSTRUCTION-2026-08-11.md).

## 6. What the negative results contribute

The failed branches are not presented as evidence that RH is inaccessible.
They identify exact hypotheses under which tempting local-to-global mechanisms
cannot work.  The recurring obstruction is that compact local data can be
made blind to global spectral information, while positive local repair terms
do not automatically assemble into a coherent global polarization.

The useful output is a collection of scoped theorems with explicit escape
hatches: a successful construction must change at least one hypothesis of the
corresponding no-go result.  See
[`NO-GO-THEOREM-GUIDE.md`](NO-GO-THEOREM-GUIDE.md) and
[`../NO-GO-ATLAS.md`](../NO-GO-ATLAS.md).

## 7. Reusable mathematical contributions

Several formal packages stand independently of the RH program:

- digamma difference series, vertical Gauss integral, and logarithmic bounds;
- Fourier `L¹`/`L²` compatibility and Wiener--Khinchin identities;
- complete Legendre `L²` bases, Parseval, and interval transport;
- finite simultaneous simple-pole regularization;
- compact-support Fourier--Laplace entirety and exponential-type bounds;
- exact matrix perturbation certificates and optimal two-block coercivity.

Their mathematical narratives, exact declarations, and extraction seams are
collected in
[`LEAN-ANALYTIC-INFRASTRUCTURE.md`](LEAN-ANALYTIC-INFRASTRUCTURE.md) and
[`../lean/UPSTREAMING.md`](../lean/UPSTREAMING.md).

## 8. Appropriate claims

The following formulations match the current artifacts.

- **Appropriate:** “Lean proves a strict lower bound for the explicitly
  defined arithmetic compact-support Weil form at `a=7/16`.”
- **Appropriate:** “The repository formalizes reusable analytic and exact
  certificate machinery used in that proof.”
- **Appropriate:** “Several obstruction theorems rule out specified classes of
  local-to-global mechanisms.”
- **Not appropriate:** “This repository's Lean build proves the full
  Guinand--Weil formula.”
- **Not appropriate:** “A finite matrix certificate proves RH.”
- **Not appropriate:** “The repository proves positivity at arbitrary
  support.”

The goal of this exposition is not to make criticism difficult.  It is to make
the exact point of any criticism easy to locate: the theorem statement, the
analytic reduction, the formal dependency ledger, the generated witness, or
the remaining global conjecture.
