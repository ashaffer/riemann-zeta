# Less-obvious escapes from the coupled uniform-strip obstruction

Status: structural escape census and exact pass/fail/open classification,
2026-08-12.  This audit concerns the present completed Weil/Gabor route.  It
does not purport to enumerate every conceivable proof of a zero-free strip.
No uniform strip, failure of a uniform strip, or RH is proved here.

## 1. Scope and headline verdict

After the normalized asymmetric mirror-block construction, the obstruction
is no longer a shortage of coefficient dimension.  In the one-pair quotient,
the completed aggregate arithmetic row is aligned with the negative carrier.
Consequently, imposing the row that was meant to cancel the prime cross term
can erase the very carrier it was meant to preserve.

This note tests the structurally different ways around that alignment.  The
outcomes are:

```text
positive multi-witness / aligned direct-sum ensembles         CLOSED;
coherent off-block multi-scale terms                          REDUCE TO ACTUAL TRANSVERSE GATE;
unused phase / real-imaginary quadrature                      CLOSED IN THE AFFINE MIRROR BLOCK;
soft positive-row leakage                                     CLOSED BY M=mI+B;
signed ensembles                                              INVALID INFERENCE;
block randomization or dephasing                              CLOSED;
local certified positivity and partition gluing              CLOSED AS A PURE CONE ARGUMENT;
fixed predetermined low-order nonlinear test bank             NOT DERIVABLE FROM CURRENT MOMENTS;
adaptive target minor / Pick test                              OPEN, DIRECT STRIP-STRENGTH;
shifted-xi de Branges criterion                               EXACT, DOMAIN-INCOMPATIBLE;
fixed-order higher moments / Type-II energy                   STRIP-STRENGTH;
shallow collateral-zero reservoir                            TOO SMALL, PROVED;
one nearly as deep collateral pair                            GENUINE OPEN ESCAPE;
actual-prime target-transverse aggregate state                GENUINE OPEN ESCAPE;
critical pole resonance                                      NO DETERMINISTIC COMPLETED RESERVOIR;
rational / archimedean completion reservoir                   TOO SMALL, PROVED;
support-scale filters                                        SAME-RESIDUE MULTIPLIER;
invertible preconditioning / nonunitary metric change        SAME INERTIA;
positive-block Schur / Birman--Schwinger / resolvent          EQUIVALENT LAST PIVOT;
square / absolute value / positive heat flow                 ERASES THE SIGN;
sign-preserving nonlinear functional calculus                SAME SIGN, NONADDITIVE PRIME SIDE;
positive logarithmic derivatives / Stechkin pairing           MOVING-SCALE ONLY;
finite computation / formal verification                      NOT AN ASYMPTOTIC ESCAPE;
zeros approaching Re(s)=1                                    NOT PROVED; STRICTLY STRONGER THAN NOT RH.
```

The two genuine **witness-engineering** survivors are coupled by the explicit
formula.  They are not two independent estimates that can be proved in
arbitrary order: an opposite-sign actual-prime state becomes a
collateral-zero, pole, or inter-scale state after completion.  Adaptive
nonlinear and transformed arithmetic theorems remain logically possible,
but the census classifies them as direct strip-strength estimates rather
than free engineering escapes.

## 2. Exact normalized obstruction

For two equal normalized packets separated by `D=dL`, one reflected pair at
depth `alpha` compresses to

```text
M=m_L*[[1,C],[C,1]],
C=cosh(alpha*D),                    m_L>0.            (2.1)
```

Its eigenvectors are the symmetric and antisymmetric packet combinations,
and

```text
lambda_-=m_L*(1-C)<0,
K=(m_L/2)*C=X^(alpha*d-o(1))/L,
-lambda_-=2*K-m_L.                                   (2.2)
```

The common binomial endpoint cutoff transfers (2.1) to the growing-jet
finite Gabor space with superpolynomial relative error.  Thus (2.1) is not
merely an abstract `2 x 2` analogy.

In the balanced mirror coordinates, write the seed coefficient as `s` and
the free coefficient as `t`.  Nulling the positive row forces `t=-s`.  The
completed aggregate scalar and full cross are then

```text
aggregate scalar = -2*K*|s|^2,
full cross       = -4*K*|s|^2.                         (2.3)
```

These two identities are exact for the off-diagonal cross block; the full
pair value is `-4*K*|s|^2+2*m_L*|s|^2`.  Thus its retained negative size is
`4*K*(1+o(1))`, while (2.2) gives the exact negative eigenvalue.  The phase
of `s` has disappeared.  Even the minimal one-real aggregate constraint is
infeasible unless `s=0`, which kills the carrier.  This is the alignment that
every proposed escape must genuinely alter.

Sources:
[`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md)
and
[`ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md`](ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md).

## 3. Multiple witnesses, phases, and scales

### 3.1 Positive ensembles are one semidefinite problem

If `w_j>=0`, the ensemble of tests `z_j` is represented by the covariance

```text
Gamma=sum_j w_j*z_j*z_j^* >=0.                         (3.1)
```

Every quadratic objective and every aggregate cancellation is linear in
`Gamma`.  On a common witness space, normalization plus one real aggregate
row has a rank-one optimum.  Thus a positive ensemble cannot improve on one
coherent witness.  On a direct sum of mirror blocks, positive-row nulling
makes all completed cross terms have the same sign, so different phases,
quadratures, or support scales cannot cancel while their carriers add.

Signed weights can cancel them, but

```text
sum_j w_j Q(z_j)<0,       some w_j<0,                  (3.2)
```

does not imply that any `Q(z_j)` is negative.  It is not a Weil-criterion
witness.

See
[`ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md`](ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md).

### 3.2 Randomization and multiblock splitting

Keeping every block coordinate makes signs and phases a unitary conjugacy;
the spectrum is unchanged.  Averaging over them applies the same conditional
expectation to the prime and zero matrices.  A two-coordinate hyperbolic
pair can place its whole negative edge in the off-diagonal block, which
dephasing sends to zero.  Fragmenting physical support also cannot remove all
prime-power translations once its total measure has the time-bandwidth size
needed for `T log T` coordinates.

See
[`ZETA23-MULTIBLOCK-UNCERTAINTY-CROSS-TERM-GATE-2026-08-11.md`](ZETA23-MULTIBLOCK-UNCERTAINTY-CROSS-TERM-GATE-2026-08-11.md).

An almost-all-height variant is logically strong enough but not supplied by
the same averaging.  One zero at height `gamma` belongs to `[T,2T]` for a
positive-measure interval of `T`, so a genuinely uniform lower edge outside
`o(T)` exceptional heights would exclude it.  Existing mean estimates are
for fixed vectors or global traces, whereas the bad eigenvector depends on
`T` in dimension `~T log T`.  They give no union bound for the least edge.
Changing the packet offset also does not regularize a fixed close zero
cluster: the corresponding Vandermonde factor persists throughout the
whole membership interval.

### 3.3 Soft positive-row leakage does not rescue the mirror

The exact obstruction does not depend on nulling the selected positive row
before the aggregate is treated.  On the normalized two-packet block, write

```text
M=m_L*I+B,
B=m_L*C*[[0,1],[1,0]].                              (3.3)
```

Here `B` is exactly the completed cross block.  For a single witness `z`, or
for any positive covariance `Gamma`, cancellation of the completed cross
scalar gives respectively

```text
<z,B*z>=0                    or Tr(B*Gamma)=0.       (3.4)
```

Consequently

```text
<z,M*z>=m_L*||z||^2>=0,
Tr(M*Gamma)=m_L*Tr(Gamma)>=0.                       (3.5)
```

Allowing a nonzero positive coordinate therefore cannot retain a negative
carrier while canceling the cross aggregate.  Requiring only an
`o(K)` cross remainder leaves at most `m_L*X^o(1)+o(K)=o(K)` negative size,
not a carrier.  Off-block collateral or actual-prime terms can invalidate
(3.3), but those are precisely the open transverse-reservoir class, not a
soft-nulling escape.

## 4. Nonlinear certificates

The selected pair itself has the exact detector

```text
det M=-m_L^2*sinh(alpha*D)^2<0.                         (4.1)
```

So nonlinearization is not intrinsically misguided.  What fails is deriving
the sign of the corresponding completed arithmetic minor from the known
global moments.  There are Hermitian matrices with the exact Zeta23 trace and
Frobenius ledger, one eigenvalue `-kappa`, the required positive mate, and
all remaining eigenvalues at least `1/3`, for which every coordinate
principal block through order

```text
r<=N/(1+3*kappa)                                      (4.2)
```

is positive semidefinite.  A predetermined proper test bank can likewise be
oriented away from the negative vector.  An adaptive `2 x 2` detector remains
possible, but its arithmetic side is exactly a signed two-correlation
Andreief/Pick inequality not controlled by the first two moments, KMT, or
rank-two displacement.

Higher exterior order does not make the arithmetic free.  At the carrier
scale in this project, (4.2) can force order at least `T^(2/3+o(1))`, far
beyond any available prime-correlation theorem.

See
[`ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md`](ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md)
and
[`ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md`](ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md).

## 5. Exact strip forms outside the arithmetic domain

The shifted-xi de Branges kernels give an exact criterion for

```text
|Re(rho)-1/2|<=delta.                                  (5.1)
```

This even detects one offending zero on a diagonal kernel value.  It does
not import into the certified compact-support Weil domain: the gamma factor
forces the natural Fourier image of a nonzero compactly supported test to
have zero intersection with the relevant de Branges space.  The shifted
prime perturbation is also indefinite, and below `Re(s)=1` its termwise prime
split is not absolutely convergent.  A new gamma-smoothing intertwiner would
need an independently proved exact comparison to the arithmetic form.

See
[`SHIFTED-WEIL-FIXED-STRIP-GATE-2026-08-11.md`](SHIFTED-WEIL-FIXED-STRIP-GATE-2026-08-11.md).

## 6. Local positivity, translations, and gluing

Positivity on every translated or modulated short interval does not imply
positivity of the coherent full compression.  The exact `3 x 3` Toeplitz
matrix

```text
[[1,0,5/4],[0,1,0],[5/4,0,1]]                       (6.1)
```

is positive on every consecutive modulated box but negative on
`(1,0,-1)`.  Therefore certified short-support positivity cannot be chained
by a partition of unity, convexity, or diagonal packet estimates alone.
An IMS-style repair would have to bound the same nonlocal prime-translation
cross terms whose edge is currently open.

See
[`TRIANGULAR-PACKET-CONE-NOGO.md`](TRIANGULAR-PACKET-CONE-NOGO.md).

## 7. Moment, Type-II, and scalar-polynomial reformulations

For every fixed `p>=2`, the complete fixed-window detector satisfies an
exact exponent identity

```text
limsup_R log(1+U_p(R))/R=p*Delta,                       (7.1)
```

where `Delta=sup_rho |Re(rho)-1/2|`.  Consequently a fixed power saving in
the proposed fourth or higher moment is already exponent-equivalent to a
fixed zero-free strip.  Product-cell grouping, high-order scale filters, and
the completed Vaughan/reciprocal transformation all retain a zero-conductor
ordinary-product component.  Current estimates give logarithmic or
subpower savings, not a fixed exponent.

This does not make those formulations false; it classifies them as direct
strip-strength arithmetic theorems rather than easier consequences of the
present inputs.

See
[`FIXED-STRIP-FOURTH-MOMENT-PROOF-ATTEMPT.md`](FIXED-STRIP-FOURTH-MOMENT-PROOF-ATTEMPT.md)
and
[`TYPEII-FIXED-SAVING-THEOREM-CARD-2026-08-11.md`](TYPEII-FIXED-SAVING-THEOREM-CARD-2026-08-11.md).

## 8. The collateral-zero escape

There is a useful rigorous depth gate.  If the selected retained carrier is

```text
K_0=X^(alpha*d-o(1))/L,                                (8.1)
```

then all on-line rows and all collateral pairs of depth

```text
beta<=alpha*d-epsilon                                  (8.2)
```

have compressed norm `o(K_0)`.  Thus a carrier-sized transverse reservoir
requires at least one collateral pair above
`Re(s)=1/2+alpha*d-epsilon`.

Current density, local-count, multiplicity, and first-two-moment theorems do
not exclude one such simple pair.  An abstract two-pair completed block can
use a collateral pair only `L^(-2)` shallower than the selected one to solve
the positive-row and aggregate equations while retaining the selected
negative carrier.  It changes counts by `O(1)` and moments by `o(N)`.

Choosing an almost-rightmost zero does not repair this.  No theorem supplies
a uniform gap between the two largest local real parts; a chain of `O(L)`
near-ties is compatible with the microscopic count, and its moment cost is
still dominated by the first member.  The abstract orientation is not yet a
proved normalized joint Gabor realization or the actual zeta divisor, so it
is an exact insufficiency result for the current statistics, not an actual
zeta counterexample.

Varying or averaging the lobe separation is a useful partial filter, not a
uniform solution.  Once the selected ordinate is demodulated, averaging the
separation multiplies a collateral row by a Fourier kernel in its ordinate
difference.  A separation range `W=o(L)` suppresses gaps much larger than
`1/W` at subpower carrier cost.  A same-height cluster, or one with
`|Delta gamma|L=o(1)`, survives.  Taking `W` comparable to `L` loses a fixed
carrier power and gives only constant suppression at the natural
`1/L` gap.  No known zero-spacing theorem prevents a distinct simple pair at
that scale.  Handling the residual cluster requires a target-conditioned
Hermite/divided-difference estimate with natural multiplicity weights; the
Riemann--von Mangoldt `O(L)` local count alone gives no such condition number.

See
[`ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md`](ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md).

## 9. The actual-prime transverse-state escape

After positive rows are removed, let `S` be the homogeneous feasible face,
`a` the selected negative row, and `g` the complete aggregate arithmetic
row.  Put `a_S=P_S*a` and `g_S=P_S*g`.  For the convenient **complex**
aggregate equation, the exact surviving homogeneous leverage is

```text
||P_(S intersect g_S^perp) a_S||^2
 =||a_S||^2-|<a_S,g_S>|^2/||g_S||^2,                  (9.1)
```

when `g_S!=0`; if `g_S=0`, the homogeneous complex row imposes no further
restriction on `S`.

For the isolated completed pair, `P_S g` is parallel to `P_S a`, and (9.1)
vanishes.

The minimal one-real equation has a different homogeneous formula: phase
rotation alone preserves modulus-valued target leverage.  Its obstruction is
instead affine.  If `ell_0` solves the positive-row datum and `g_S=P_S*g`,
the minimum real correction norm is

```text
abs(Re <ell_0,g>)/||g_S||,                          (9.2)
```

with infeasibility when `g_S=0` and the numerator is nonzero.  The isolated
mirror has exactly that latter pattern.  Thus (9.1) must not be quoted for
the one-real homogeneous hyperplane, although both versions fail on the
affine mirror block.

A genuine escape therefore requires an opposite-sign, target-neutral actual
state of carrier size.  Completion says that such a state must be supplied
by the centered actual von Mangoldt correlations together with
collateral-zero, critical pole/main, or nonorthogonal inter-scale terms.
The rational and archimedean completion terms are already proved subcarrier
on the audited packet geometry.  Dimension alone does not give the surviving
terms' sign or angle.

The pointwise prime-null construction is a sufficient but unnecessarily
strong version of this demand.  The intrinsic single-witness problem has
only one real aggregate equation.  Reducing the number of equations does
not cure (9.1).

Replacing prime nulls by prime **sign** constraints is another semidefinite
formulation, not an automatic positivity theorem.  Each positive coefficient
`Lambda(n)` multiplies an indefinite translation correlation.  Positivity of
the coefficients therefore gives no Loewner sign for their sum.  A separating
dual certificate for an infeasible sign cone is itself a positive aggregate
of prime translations; after completion it returns to the target/collateral
alignment in (9.1).  This route remains viable only if one proves a new
coefficient-specific sign theorem for the actual prime aggregate.

## 10. Critical pole resonance and scale filtering

Let `L=C log T`, let the packet separation be `D=dL`, and write a putative
right-side zero as `1-delta+i gamma`.  The selected carrier and crude leading
pole/main scales tie when

```text
C*d*delta=1.                                            (10.1)
```

The tie is not a new completed direction.  Splitting
`d psi(e^y)=e^y dy+d[psi(e^y)-e^y]` shows the exact operator identity

```text
Pole_cross-Prime_cross
 =Rational_cross-CenteredPrime_cross.                  (10.2)
```

The growing `e^(y/2)` pole branch is exactly the continuum main part of the
raw prime sum, so it cancels in (10.2), not merely asymptotically.  The
remaining rational branch is subcarrier.  One can null the **raw** prime
scalar and deliberately leave a negative pole/main scalar at (10.1), but
this is exactly the carrier-sized equation

```text
CenteredPrime_cross=-Main_cross.                       (10.3)
```

No current theorem gives its projected target angle or controls the
collateral balance.  The same-lobe exponent ledger leaves a formal window
only for `delta<1/8` in the limiting asymmetric geometry; this recovers the
conditional `7/8` threshold, not a proof of it.

Scale filters are equally exact.  For a signed measure of logarithmic shifts
`a`, the pole-normalized Mellin multiplier is

```text
m_a(s)=integral exp((1-s)h) da(h).                     (10.4)
```

Both the selected zero residue and the corresponding completed arithmetic
pole are multiplied by `m_a(rho)`.  A filter with `m_a(rho)=0` deletes the
carrier.  A pole-killing filter with `m_a(1)=0` and `m_a(rho)!=0` exists, for
example `I-S_h`, but then the surviving signed prime estimate is itself
strip-strength.  Coherent filtered witnesses retain every cross-scale term;
signed averages with negative weights lose the witness inference.

See
[`ZETA23-CRITICAL-POLE-MAIN-AND-MELLIN-SCALE-ESCAPE-AUDIT-2026-08-12.md`](ZETA23-CRITICAL-POLE-MAIN-AND-MELLIN-SCALE-ESCAPE-AUDIT-2026-08-12.md).

## 11. Preconditioning, Schur complements, and functional calculus

An invertible nonunitary change of metric cannot alter the obstruction.  If
`S` is invertible, then

```text
inertia(S^*MS)=inertia(M),
det(S^*MS)=abs(det S)^2*det M.                         (11.1)
```

Measuring the transformed form against its transported metric `S^*S` gives
exactly the old Rayleigh quotient.  Apparent carrier amplification against
the untransported Euclidean norm is a condition-number debt.  Completion is
congruent on both sides: `S^*K_comp S=S^*K_zero S`.

Schur elimination has the same property.  For the exact mirror

```text
M=m*[[1,C],[C,1]],                  C>1,              (11.2)
```

eliminating one positive diagonal lobe gives the pivot

```text
m*(1-C^2).                                             (11.3)
```

Its harmonic lift is `(x,-C*x)`, with squared norm
`(1+C^2)|x|^2`.  The normalized quotient is therefore

```text
m*(1-C^2)/(1+C^2) -> -m,                              (11.4)
```

not the exponential carrier `-m*C`.  Eliminating the true positive
eigenmode simply leaves the original negative eigenvalue.  In general,
Haynsworth inertia makes the Schur complement exactly the unresolved last
pivot, while its effective norm retains the full harmonic-response cost.
Schur complementation is nonlinear in a sum, so it does not split into
separate prime, pole, and archimedean complements.

Likewise, for `K=P-R`, `P>0`,

```text
K>=0 iff lambda_max(P^(-1/2)R P^(-1/2))<=1.          (11.5)
```

This Birman--Schwinger or resolvent crossing is equivalent to the original
sign.  For the mirror with `P=mI`, the transformed matrix has largest
eigenvalue `C>1`.  A resolvent expansion is tractable under a norm bound
below one, but that bound is already the desired positivity theorem.

Functional calculus gives an exact dichotomy.  Squaring, absolute value,
or `exp(-tK^2)` makes every operator positive and erases the negative
carrier.  If a real scalar function sends zero to zero and preserves sign
away from zero, then

```text
negative_index(f(K))=negative_index(K),
f(K)>=0 iff K>=0.                                    (11.6)
```

For the isolated mirror, `sign(M)=[[0,1],[1,0]]`; for an invertible full
completed operator, constructing `sign(K)=I-2P_-` is exactly constructing
the forbidden negative spectral projection.  No genuinely nonlinear map preserves the
additive place decomposition: continuity and

```text
f(A+B)=f(A)+f(B)-f(0)                                (11.7)
```

even just for scalar `A,B` force `f(x)=f(0)+c*x`.  Every nonlinear amplifier
therefore creates mixed prime--prime, prime--archimedean, and collateral
products.  Applying it separately to the pieces is not functional calculus
of the completed operator.

Finite-dimensional heat smoothing `T_t^*KT_t` is another congruence while
`T_t` is invertible.  A singular limit can lose the negative packet only by
collapsing it; recovery requires the corresponding unbounded inverse or
observability estimate.  Regular virial commutators also have zero
expectation on every eigenvector, so a strict estimate on the negative
spectral subspace already assumes that subspace is empty.  Singular boundary
versions retain exactly the existing endpoint/collar flux.

These transformations are closed as **generic shortcuts**, not as possible
coordinates for a new arithmetic theorem.  An arithmetically canonical,
uniformly conditioned preconditioner with an independently proved
prime-event sign would be real progress; the transformation alone supplies
no such sign.

See
[`ZETA23-OPERATOR-PRECONDITIONING-FUNCTIONAL-CALCULUS-AUDIT-2026-08-12.md`](ZETA23-OPERATOR-PRECONDITIONING-FUNCTIONAL-CALCULUS-AUDIT-2026-08-12.md),
[`BIRMAN-SCHWINGER-CHECKPOINT.md`](BIRMAN-SCHWINGER-CHECKPOINT.md),
[`HODGE-LOW-SECTOR-DTN-NOGO.md`](HODGE-LOW-SECTOR-DTN-NOGO.md),
and
[`COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md`](COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md).

## 12. Finite computation and formal verification

Exact SDP computations, interval arithmetic, and Lean can certify any fixed
finite height, support, and prime cutoff.  They cannot by themselves turn an
unbounded family of changing prime matrices into a finite problem.  A proof
would need a monotonicity, recurrence, or uniform tail theorem.  The present
form has no such monotonicity: enlarging support activates new indefinite
prime translations, and local positivity does not glue by Section 6.

Thus computation is valuable for falsifying proposed finite inequalities and
for certifying base intervals, but it is not a separate asymptotic escape.

## 13. Positive logarithmic derivatives and Stechkin pairing

One can leave the compact-support form and work in `Re(s)>1`, where

```text
(-1)^m*(-zeta'/zeta)^(m)(s)
 =sum_n Lambda(n)*(log n)^m*n^(-s)                       (13.1)
```

has genuinely positive coefficients.  Differentiation removes the
archimedean `log T` term.  It also replaces each zero by a reciprocal power.
To resolve the `O(log T)` local zero cloud, the order must satisfy

```text
m >> (sigma-1)*log T,                                   (13.2)
```

whereas retaining a zero at `beta=1-epsilon` against the pole at one requires

```text
m*epsilon/(sigma-1)=O(1).                               (13.3)
```

Together these force `epsilon=O(1/log T)`, the moving classical scale, not a
fixed strip.  Functional-equation/Stechkin pairing can make the target-to-pole
ratio exceed one half in a fixed-gap parameter window, but every globally
positive pair has a positive mass which incurs an unavoidable logarithmic
gamma debt.  Normalized by the retained fixed-gap target, that debt tends to
infinity.

See
[`R89-DIFFERENTIATED-POSITIVITY-GATE.md`](R89-DIFFERENTIATED-POSITIVITY-GATE.md)
and
[`R132-FUNCTIONAL-PAIR-SIGMA-KERNEL-GATE.md`](R132-FUNCTIONAL-PAIR-SIGMA-KERNEL-GATE.md).

## 14. The opposite hypothesis: no fixed strip exists

The adversarial branch also fails, for a much more basic reason.  Put

```text
Theta=sup{Re(rho): zeta(rho)=0, 0<Re(rho)<1}.             (14.1)
```

Then

```text
RH                 iff Theta=1/2,
not RH             iff Theta>1/2,
no fixed strip     iff Theta=1.                          (14.2)
```

Thus proving that no uniform strip exists would be substantially stronger
than disproving RH.  No accepted theorem currently proves even one Riemann
zeta zero with real part strictly greater than `1/2`.

The exact arithmetic promotion target is

```text
limsup_x log(1+|psi(x)-x|)/log x=1,                       (14.3)
```

equivalently the same exponent-one statement for `M(x)`.  Known omega
theorems remain at power `1/2` up to logarithmic or subpower factors.

Universality does not bridge the gap.  Standard Voronin universality
requires a nonvanishing target.  A winding-one target would force a zero by
Rouche, but a positive-density version is unconditionally impossible: the
measure of its good shifts is at most a constant times
`N(sigma,T)=o(T)`.  A sparse sequence-only winding theorem is logically
possible, but it is already an off-critical-zero theorem.  Random Euler
products, zero density, functional symmetry, and classical zero-free regions
all permit either outcome and prove neither.

The assertion `Theta=1` is compatible with the usual density hypothesis,
because that hypothesis is an upper bound and permits a sparse exceptional
sequence.  It contradicts RH.  No ZFC-independence result is known, and
independence would not itself prove `Theta=1` in the standard complex
numbers.

See
[`ZETA23-NO-UNIFORM-STRIP-OPPOSITE-HYPOTHESIS-AUDIT-2026-08-12.md`](ZETA23-NO-UNIFORM-STRIP-OPPOSITE-HYPOTHESIS-AUDIT-2026-08-12.md).

## 15. Honest frontier

All currently tested witness-engineering escapes reduce to one of the
following three mathematical statements:

1. **Actual transverse theorem.**  Prove that the completed actual-prime and
   collateral operator has a carrier-sized target-neutral state with the
   required sign, while its same-lobe/full-form cost is little-o of the
   retained negative edge.
2. **Actual exclusion theorem.**  Prove a local depth-isolation or signed
   orientation theorem excluding every carrier-sized collateral reservoir.
3. **Direct arithmetic theorem.**  Prove a fixed power saving for the
   completed scalar prime polynomial, adaptive Pick minor, or all-sector
   Type-II energy.  By the exact pole argument, this is already
   strip-strength.

The first two alternatives are mutually informative through the explicit
formula; neither follows from the present count and moment ledger.  Further
changes of basis, positive averaging, or renaming the scalar as a determinant
do not create a fourth alternative.
