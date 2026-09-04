# Second-order major theorem distillation

Date: 2026-09-01

> **Recursive fixed-point update.**  A later same-day pass strictly improves
> the Weil propagation reduction in this report: qualitative compact-form
> localization replaces the required `NR_log` rate, Fredholm reduction
> replaces all-vector `HRW` by exact nullspace charge cancellation, and a
> maximal-support proof removes the separate non-Zeno gate.  See
> [the fixed-point consolidation](ZETA23-RECURSIVE-CONSOLIDATION-FIXED-POINT-2026-09-01.md).
> All open global statuses remain unchanged.

## Status and verdict

This is a hostile, architecture-preserving review of the current project
corpus.  It distills results that recur under different notation and promotes
only statements with an exact proof, a cited imported theorem, or an explicit
countermodel.

The review produces eight cross-cutting major theorem packages, one
project-specific arithmetic theorem, and seven supporting lemmas.
Three conclusions are especially useful:

1. there is an actual projection-defect Ward catastrophe whose favorable and
   cross blocks lie in every Schatten class while its Ward quotient diverges
   at any prescribed rate;
2. the total singular Hardy anomaly is independent of the choice of heat,
   Poisson, or Fejer common regulator under one precise approximate-identity
   hypothesis;
3. a reserve-localized Schur theorem gives a division-free positive
   propagation mechanism that remains meaningful when the old spectral floor
   collapses.

None of these proves the zeta-specific reserve estimate, a uniform zero-free
strip, the sharp four-cycle bound, or RH.  The later recursive pass removes
the need for a separate non-Zeno input and replaces the propagation role of
the reserve estimate by `KNC`; the still later last-mile audit shows that
universal completed-zeta `KNC` is RH-equivalent, not a lower-strength global
conjecture.  The global claim ledger is unchanged.

## 1. Audit scope and architectural firewall

The review used the 1,216 pre-existing `results/` artifacts, the 46 canonical
cards in the [no-go atlas](../NO-GO-ATLAS.md), the verified 92-node typed
proof tree, the current 123-module aggregate Lean import, and the latest
September 1 semilocal reports.  Repetitive generated certificates were treated
as instances of their common range-composition schema rather than as distinct
mathematical ideas.

The branches remain separate:

- **Weil branch:** local P5 crossing followed by `NR_log` and uniform `HRW`
  would still yield effective positive steps.  The later fixed-point pass
  proves that qualitative compact-form localization and pointwise
  Fredholm--Ward reduction suffice instead; `KNC` is the exact local
  right-openness condition, and its universal completed-zeta assertion is
  RH-equivalent.  The trace theorem below is a representation theorem, not
  that arithmetic condition.
- **QP/Turan branch:** `DPA_P(.019)` and
  `LTRAD_P(.0189,.001)` remain the recorded route to a fixed strip.
  `COSE` and `PWCT` are one-way subclasses.  `CA4` and the sharp four-cycle
  bound remain open and are not direct strip gates.
- **R71/R87/R89 branch:** exact recompletion returns the original energy, and
  the proposed fourth-moment square locus has zero coefficient on the required
  one-axis signed contact.

The review therefore claims reusable mathematics and sharper pruning, not a
cross-architecture implication.

## 2. Unifying principle: relative information is the conserved resource

Most failed routes apply a forgetful map and then ask the image to recover
structure that the map discarded.  The repeated examples are:

- compactness without the relative graph norm;
- moments without a conditioned right inverse;
- positivity without the signed charge;
- one flattening without all-cut tensor coherence;
- asymptotic recurrence without the finite observation window;
- a natural mask without its atomic transport cost;
- a change of variables without the recombination contacts.

The exact common theorem is the following stable-descent criterion.

### Major Theorem A: stable descent and quantitative lifting

Let `X,Y,Z` be Hilbert spaces and let `T:X->Y` and `L:X->Z` be bounded.
The following are equivalent:

1. there is a bounded linear map `S:closure(ran T)->Z` such that `L=ST`;
2. there is `0<=C<infinity` such that
   
   \[
   \|Lx\|\le C\|Tx\|\qquad(x\in X);
   \]

3. there is `0<=C<infinity` such that
   `L^*L <= C^2 T^*T` as quadratic forms.

The least admissible `C` is the norm of the induced quotient map.  The proof
defines `S(Tx)=Lx`; condition 2 makes it well-defined and bounded, and the
form inequality is its squared norm statement.

Dually, for bounded linear `B:W->Y`, a bounded linear lift `R:W->X` with
`B=TR` exists exactly
under the Douglas range/factorization condition for some `lambda>=0`,

\[
 BB^*\le \lambda TT^*.
\]

The least `\lambda` is the squared norm of the reduced lift.  If `T` has closed
range, the minimum-norm lift is `T^\dagger B`.

**Consequence.**  Mere constancy on fibers, `ker T subset ker L`, gives only an
algebraic descent and can induce an unbounded quotient map.  Every application
through this linear stability socket needs a bound on that quotient norm.
Affine serialization, moment correction, source reconstruction, edge-flux
lifting, and Ward/Douglas factorization share this socket, but their
positivity, cone, support, and normalization constraints remain separate
passport data.

## 3. Relative graph norms and the Ward obstruction

### Major Theorem B: complete relative graph-norm factorization

Let `A:X->X` and `H:Y->Y` be bounded positive self-adjoint operators, and let
`B:Y->X` be bounded.  For `C>=0`, the following are equivalent:

\[
 |\langle x,By\rangle|^2
 \le C\langle x,Ax\rangle\langle y,Hy\rangle
 \quad(x\in X,y\in Y),                              \tag{3.1}
\]

\[
 B=A^{1/2}KH^{1/2}\quad\hbox{for some }\|K\|^2\le C, \tag{3.2}
\]

and positivity of the corresponding `2 x 2` block form

\[
 \begin{pmatrix}CA&B\\B^*&H\end{pmatrix}\ge0.       \tag{3.3}
\]

The proof applies Riesz representation to
`(A^(1/2)x,H^(1/2)y) -> <x,By>`.  In particular, separate norm, compactness,
or Schatten estimates for `A` and `B` do not control the relevant object
`A^(-1/2)B`.

### Major Theorem C: arbitrary-rate all-Schatten Ward catastrophe

For every finite constraint budget `r in N_0` and every sequence `M_n>=0`, there are
a separable Hilbert space, a projection `P`, and a unitary `U` such that every
closed subspace `E` of codimension at most `r` contains orthogonal subspaces
`O,W` with the following properties for `Delta=P-U^*PU`:

- the forward leakage belongs to every `S_p`, `p>0`;
- the reverse leakage has essential norm one;
- `A=P_O Delta|_O` is positive, injective, and belongs to every `S_p`;
- `B=P_O Delta|_W` belongs to every `S_p`;
- `W` is exactly harmonic relative to `O` for the reference form `h=I`;
- the `n`th squared Ward quotient exceeds `M_n`.

The construction starts with the infinite-multiplicity coisometric reservoir

\[
 U_0=\begin{pmatrix}S&E_0\\0&S^*\end{pmatrix},
 \qquad P-U_0^*PU_0=0\oplus(-E_0),                  \tag{3.4}
\]

and appends multiplicity-`r+1` rotation defects with eigenvalues
`+/-delta_n`, where `delta_n=2^(-n)`.  A finite-codimensional `E` must meet
every positive eigenspace and leaves an infinite orthonormal family in the
`-1` reservoir.  Mix paired unit vectors with

\[
 \epsilon_n=\frac{\delta_n}{M_n+2},\qquad
 \alpha_n^2=\frac{1+\epsilon_n}{1+\delta_n},\qquad
 \beta_n^2=\frac{\delta_n-\epsilon_n}{1+\delta_n}.  \tag{3.5}
\]

Then

\[
 A_n=\epsilon_n,qquad
 |B_n|^2=(1+\epsilon_n)(\delta_n-\epsilon_n),        \tag{3.6}
\]

so

\[
 \frac{|B_n|^2}{A_n}=(1+\epsilon_n)(M_n+1)>M_n.    \tag{3.7}
\]

At the same time `A_n<=delta_n` and
`|B_n|<=sqrt(2delta_n)`, proving all-Schatten membership.  Duplicating the
construction in both eigenspaces of a commuting reflection handles a genuine
parity constraint.

This strengthens the construction in the
[operator theorem suite](ZETA23-OPERATOR-LEMONADE-THEOREM-SUITE-2026-09-01.md).
Its classical ingredients are Halmos two-projection geometry, Calkin
invariance, and Douglas factorization.  The simultaneous finite-constraint,
essential-asymmetry, all-Schatten, arbitrary-rate configuration is
project-proved and plausibly new as a synthesis, but literature-level novelty
has not been established.

**Kill-switch.**  Compactness, arbitrarily rapid Schatten decay, exact
harmonicity, finitely many moments, or finite parity bookkeeping cannot prove
`HRW` by themselves.  Some additional relative or joint structure is
necessary; equivalently, a successful Ward estimate supplies the graph-norm
factorization of Major Theorem B, while a reserve estimate is one sufficient
way to establish it.

## 4. A positive replacement for floor division

### Major Theorem D: reserve-localized, gap-free Schur closure

Let `a,s,g>=0`, let `d` be real, and let `b` be a cross term.  Suppose

\[
 d\ge s-Mg,\qquad |b|^2\le Cag,\qquad g\le\omega s, \tag{4.1}
\]

where `M,C,omega>=0` and

\[
 (M+C)\omega\le1.                                  \tag{4.2}
\]

Then

\[
 a+2\operatorname{Re}b+d\ge0.                     \tag{4.3}
\]

Indeed, `(M+C)g<=s`, so `Cg<=s-Mg<=d`.  Hence
`|b|^2<=ad`, and (4.3) is the scalar Schur inequality.  No lower bound on
`a` is used.

For the nested Weil spaces there is a second exact input: every newly
activated prime-power shift is zero on the embedded old support, so the old
block is preserved exactly.  Therefore a sequence of activation steps is
positive provided the collar/reference estimates (4.1)--(4.2) hold with
locally uniform constants and the event sequence is non-Zeno.  Cofinality
then invokes the already formalized support-propagation theorem.  This is the
earlier quantitative route; the recursive fixed-point update cited above
replaces it, for existence-only continuation, by qualitative localization,
pointwise `KNC`, and the maximal-support argument.

The scalar core is kernel-checked in
[SemilocalWardDistillation.lean](../lean/rhbridge/RHBridge/SemilocalWardDistillation.lean).
The zeta-specific estimates `NR_log` and `HRW`, and the required uniformity,
remain open.  This theorem identifies their correct socket; it does not prove
them.

## 5. Trace anomalies and regulator independence

### Major Theorem E: regulated anomaly transgression

For finite matrices, put `D=P-VPU`.  For arbitrary `W,F,P,U,V`, cyclicity
and the commutator product rule give

\[
\begin{aligned}
 \operatorname{tr}(WFD)
 &=\operatorname{tr}\bigl(W(FU-UF)VP\bigr)\\
 &\quad+\operatorname{tr}\bigl((WU-UW)FVP\bigr)\\
 &\quad+\operatorname{tr}\bigl(WF(I-UV)P\bigr).     \tag{5.1}
\end{aligned}
\]

If `UV=I` and `FU=UF`, the entire regulated anomaly is the regulator
commutator

\[
 \operatorname{tr}(WFD)
 =\operatorname{tr}\bigl((WU-UW)FVP\bigr).          \tag{5.2}
\]

Thus finite cyclic traces do not destroy the anomaly; they move it to the
failure of the regulator to commute with the phase.  This identity is
kernel-checked in
[SemilocalHankelTraceNoGo.lean](../lean/rhbridge/RHBridge/SemilocalHankelTraceNoGo.lean).

### Major Theorem F: regulator-independent total singular Hardy anomaly

Let `P` be the lower Hardy projection on the circle,
`D_u=P-M_u^*PM_u`, let `u` be unimodular and `C^1` away from a nonempty finite
set `Sigma`, and let `g` be bounded.  (The empty-set case is the ordinary
smooth theorem.)  Put

\[
 \delta(x)=\operatorname{dist}(x,\Sigma),\qquad
 \Lambda_u(x)=\sup_{d(x,y)<\delta(x)/2}|u'(y)|.
\]

Assume

\[
 |g|(1+\Lambda_u+\delta^{-1})\in L^1.              \tag{5.3}
\]

Let `T_epsilon` be a trace-class convolution operator whose continuous kernel
`h_epsilon` is nonnegative, even, has mass one, and, for every `eta>0`, obeys

\[
 \int_{d(r,0)>\eta}h_\epsilon(r)\,d\mu(r)\longrightarrow0.
\]

If
`T_epsilon>=0` as an operator and `R_epsilon=T_epsilon^(1/2)`, then

\[
 \lim_{\epsilon\downarrow0}
 \operatorname{Tr}(R_\epsilon M_gD_uR_\epsilon)
 =\int g(-i\bar u u')\,d\mu.                        \tag{5.4}
\]

The proof uses the removable diagonal of

\[
 K_u(x,y)=p_-(x-y)(1-\bar u(x)u(y)),
\]

the pointwise bound

\[
 |K_u(x,y)|\ll1+\Lambda_u(x)+\delta(x)^{-1},        \tag{5.5}
\]

and dominated convergence for the approximate identity.  Heat,
Poisson/Abel, and Fejer regulators satisfy the hypotheses.  The recursive
pass weakens the regulator assumptions to mass one, uniformly bounded `L1`
norm, and vanishing absolute tails; signed or complex kernels are allowed for
the interior total limit.  Spectral positivity is needed only for a common
square-root sandwich.

Uniform `L1`-bounded domination is a substantive sufficient hypothesis;
operator positivity alone does not provide that domination.  Dirichlet
spectral projections have sign-changing kernels and unbounded `L1` norms, so
they are not covered by this theorem.  No failure of the anomaly limit is
inferred from that fact alone.  The conclusion concerns the **total** pairing
only; it does not give separate limits for the four Hardy blocks.  The full proof and the
singular boundary-flux formula are in the
[common-regulator theorem](ZETA23-SINGULAR-WEIGHTED-HEAT-ANOMALY-THEOREM-2026-09-01.md).

## 6. Mask transport: exact obstruction and constructive complement

### Major Theorem G: atomic-gauge lower bound and symmetric boundary lift

Let `A_k` be atoms with costs `w_k>0`, fix `C>0`, and define the decomposition gauge

\[
 \gamma(X)=\inf_{X=\sum c_kA_k+E}
 \left(\sum|c_k|w_k+\|E\|_1\right).                \tag{6.1}
\]

If a dual matrix `B` obeys

\[
 |\langle B,A_k\rangle|\le Cw_k,qquad
 \|B\|_\infty\le C,                                \tag{6.2}
\]

then

\[
 \gamma(X)\ge\frac{|\langle B,X\rangle|}{C}.       \tag{6.3}
\]

This is immediate from duality and is the correct invariant for replacing a
coefficient mask.  Applied to the CA4 interval-probability dictionary with
the discrete-variation witness `B=bb^T`, it yields a project-specific lower
bound of order `TV(lambda)^2`; for the retained actual-prime hats this is far
above the required transference budget.  With positive mixture coefficients,
probability-vector atoms, and a probability-vector rank-one target, an exact
rank-one mixture is more rigid still: every atom carrying positive mass must
equal the target.

There is, however, an exact signed constructive complement.  On a finite
connected graph—or on a finite connected subgraph spanning the support of a
finitely supported difference—equal-mass vertex vectors `lambda,eta` have
`delta=lambda-eta=partial c` for a finite edge chain `c`.  For every `k>=1`,

\[
 \lambda^{\otimes k}-\eta^{\otimes k}
 =\sum_{a=0}^{k-1}
   \lambda^{\otimes a}\otimes\partial c\otimes
   \eta^{\otimes(k-1-a)}.                           \tag{6.4}
\]

For a character `M`, this becomes

\[
 M_\lambda^k-M_\eta^k
 =M_\delta\sum_{a=0}^{k-1}M_\lambda^aM_\eta^{k-1-a}. \tag{6.5}
\]

For `k=2`, double summation by parts moves both divergences onto the common
translated kernel and creates the desired edge factors.  Existence of `c` is
automatic and supplies no estimate: the still-open theorem must control its
norm in the actual signed two-channel kernel.  Thus scalar natural-mask
transference is closed, while the joint product-graph edge-flux route remains
credible.

## 7. Finite-window observability and tensor coherence

### Major Theorem H: participation-limited observability

Let `(Omega,rho)` be a probability space, let a measurable real field `F` be assembled
from a finite family of nonnegative block sizes `r_b`, and fix
`c,C,c_0>0`.  Set

\[
 E=\sum_b r_b^2,\qquad S=\sum_b r_b,\qquad
 P_{\rm eff}=\frac{S^2}{E}.                         \tag{7.1}
\]

Assume

\[
 \int F^2d\rho\ge cE,qquad
 \|F\|_\infty\le CS,qquad
 \left|\int Fd\rho\right|\le\frac{c}{2C}\frac ES,
 \qquad S\ge c_0.                                  \tag{7.2}
\]

Then

\[
 \operatorname*{ess\,sup}_\Omega F
 \ge\frac{cc_0}{4C}\frac1{P_{\rm eff}}.             \tag{7.3}
\]

Indeed, `int |F| >= cE/(CS)` and the small mean leaves at least half of the
corresponding positive mass.  This converts finite-aperture observability into
an effective-participation problem.

The clustered/source-normalized LTRAD instantiation is project-proved.  A
rank-two Fejer family satisfies

\[
 \sup F_A=\frac1{2(m-1)},\qquad
 P_{\rm eff}=(9/8+o(1))m,qquad
 (\sup F_A)P_{\rm eff}\to9/16,                     \tag{7.4}
\]

showing the scale is sharp for the abstract proof class.  This does not
refute actual-prime `COSE`; it says the missing result must turn diffuse
near-saturation into **source-preserving actual-prime structure before the
finite cutoff**.  Rational independence alone gives recurrence only at
unbounded times.

### Project Theorem I: all-cut secant/tangent arithmetic rigidity

Assume the full faithful binary-product passport of the
[SR2PF report](ZETA23-SR2PF-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md), including
its source, mask, positivity, distinctness, and resolution hypotheses.  In
particular, for sufficiently large `Y`, with all implied constants uniform in
`r`, distinct primes `p_s asymp Y`, indexed by `s in {0,1}^r`, lie within
`O(Y/B)` of the specified positive product reference, with `B=Y^(50/33)`.
After deletion of at most one coordinate, the reference digit ratios have
displacement from one and pairwise separation
`>>Y^(-.0179-o(1))`, which dominates `B^(-1/2)`.  Every `3 x 3` minor of every
flattening is then an integer of size

\[
 O(Y^3/B^2)=O(Y^{-1/33}),
\]

and hence vanishes.  Imported secant-variety classification places the tensor
in the second secant of the Segre variety: an honest two-product secant or a
tangent/W degeneration.  The project-specific arithmetic arguments then give

\[
 r\ll\frac{\log Y}{\log\log Y}                     \tag{7.5}
\]

in both branches: `p`-adic parallelograms and factorial determinant height in
the rational tangent branch, and uniform Pell/divisor counting in the honest
or quadratic-conjugate secant branch.

This closes the faithful all-cut algebraic terminator recorded in the
[SR2PF report](ZETA23-SR2PF-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md).  One
matrix flattening is not enough, and fixed-size W examples rule out an
absolute-`r` theorem.  The upstream source-, mask-, coefficient-, floor-, and
resolution-preserving transport into this passport remains open.

## 8. Conservation theorems that explain repeated failures

### Lemma 1: finite-surgery conservation

Let `A=A^*` be bounded on a Hilbert space, let `L:H->C^m` be bounded, let
`J=J^*` act on `C^m`, and put `K=L^*JL`.  Then

- the quadratic forms of `A` and `A+K` agree on `ker L`;
- `rank K<=m` and the essential spectra agree;
- `n_-(A+K)>=n_-(A)-m`, with the symmetric reverse inequality.

Thus an infinite negative reservoir survives every finite list of moments,
boundary conditions, or pole corrections.  This is the common operator form
of finite-codimension immunity.

### Lemma 2: recombination conservation and charge selection

For a Hermitian quadratic form `Q` and `T=sum_sigma T_sigma`,

\[
 Q(T)=\sum_{\sigma,\tau}Q(T_\sigma,T_\tau).         \tag{8.1}
\]

Replacing `T_sigma` by `T_sigma+K_sigma` with `sum K_sigma=0` cannot improve
`Q(T)`; every apparent diagonal gain is exactly repaid by polarized contacts.
If a compact-group symmetry is present, Reynolds projection annihilates every
nontrivial isotypic charge.  In R89 the even square locus therefore has
exactly zero coefficient on the required one-axis odd contact.  This is a
selection rule, not a general claim that positive moments lose all contacts.

### Lemma 3: harmonic-completion Pythagoras

Let `U,H` be Hilbert spaces, let `A:H->H` and `D:U->U` be bounded
self-adjoint operators, let `P,K:U->H` be bounded, and put `X=AP`.  Then

\[
 D-X^*K-K^*X+K^*AK
 =(D-X^*P)+(P-K)^*A(P-K).                           \tag{8.2}
\]

For `A>=0`, the harmonic lift `P` minimizes the displayed expression in the
Loewner order over `K`, and every completion error is exactly quadratic.  This
explains why large isolated
source responses can cancel in their physical sum without contradicting the
positive source Gram matrix.

### Lemma 4: finite-moment retraction

If `V` is normed, `L:V->K^m` and `J:K^m->V` are bounded linear maps, and
`LJ=I`, then

\[
 \Pi=I-JL,qquad L\Pi=0,qquad \Pi^2=\Pi,qquad
 \operatorname{ran}\Pi=\ker L.                    \tag{8.3}
\]

Moreover `||Pi||<=1+||J||||L||`.  Thus a corrected-collar construction is
precisely a problem of producing a uniformly conditioned moment right
inverse; solvability at each finite stage is insufficient.

### Lemma 5: exceptional-set coupling

Fix `c,C>0`.  If, in the same finite choice universe at scale `N`, a lower
mechanism succeeds on at least `cN^(1-rho)` choices and an upper mechanism
fails on at most `CN^(1-m)` choices, then for `rho<m` the lower-success set
contains an upper-success choice for all sufficiently large `N`.  This replaces two
unnecessary pointwise hypotheses by compatible density budgets.  In the
center-density adapter, the required averaged lower moment and
density-radialization inputs remain open.

### Lemma 6: additive-error propagation

If

\[
 a_{n+1}\ge\lambda_na_n-\epsilon_n,qquad\lambda_n\ge0,
\]

then

\[
 a_n\ge\left(\prod_{k<n}\lambda_k\right)a_0-E_n,
 \qquad E_0=0,\quad E_{n+1}=\lambda_nE_n+\epsilon_n. \tag{8.4}
\]

This is the correct ledger for approximate propagation.  It makes the total
local-to-global tax explicit and prevents a sequence of individually small
errors from being silently discarded.

### Lemma 7: gauge quotient and collapsing margins

For an observation map `U`, a target descends exactly when it is constant on
every fiber of `U`.  If a gauge group acts by observation-invisible
transformations, gauge invariance is necessary; it is sufficient only when
the gauge orbits are exactly the observation fibers.  In the linear phase
model where observation is precisely restriction/pairing of the logarithmic
derivative against `G`, a perturbation in `G^perp` is invisible; a
Hardy/Hankel target that changes along such an orbit therefore cannot descend.

Separately, let forbidden points `b_n` approach admissible points `a_n` in a
compact metric model.  Any finite family of continuous tests that is globally
valid on the admissible class is equicontinuous and hence cannot retain a
fixed positive margin on `b_n`.  A successful family in that topology must
pay a collapsing margin, lose a common continuity modulus, use a
discontinuous/quantized invariant, or strengthen the topology.  This is the
precise FP9 form of the remote-quartet, fixed-window-margin, and finite-probe
obstruction.

## 9. Novelty ledger

| Package | Mathematical status | Novelty assessment |
|---|---|---|
| stable descent / Douglas factorization | standard | none claimed |
| finite surgery, recombination, atomic gauge | standard or elementary | none claimed |
| arbitrary-rate all-Schatten projection-defect catastrophe | exact project construction | plausibly new synthesis; not established |
| reserve-localized Schur closure | exact elementary theorem, Lean checked | useful new packaging |
| singular weighted Hardy anomaly | project-proved analytic theorem | novelty unknown |
| regulator universality for total anomaly | standard-strength extension of that theorem | none claimed separately |
| actual-prime variation mask obstruction | project-proved, unrefereed | possibly project-specific novelty |
| faithful all-cut arithmetic secant/tangent exclusion | imported classification plus project proof | potentially novel arithmetic component; not established |
| participation theorem and sharp Fejer family | exact project synthesis | elementary inequality; specialized sharpness unrefereed |

The closest classical comparators are Halmos and Douglas for projection
geometry and factorization; Hartman and Adamyan--Arov--Krein for Hankel
compactness/approximation; Helton--Howe, Connes, and JLO for trace anomalies;
and secant-variety classification for the tensor fork.  No claim above is
labelled literature-new without a specialist review.

Primary anchors include Halmos,
[*Two subspaces*](https://www.ams.org/tran/1969-144-00/S0002-9947-1969-0251519-5/S0002-9947-1969-0251519-5.pdf);
Douglas,
[*On majorization, factorization, and range inclusion of operators on Hilbert space*](https://www.ams.org/proc/1966-017-02/S0002-9939-1966-0203464-1/S0002-9939-1966-0203464-1.pdf);
Helton--Howe's
[*Integral operators: commutators, traces, index and homology*](https://mathweb.ucsd.edu/~helton/BILLSPAPERSscanned/HHo75.pdf);
and the Landsberg--Manivel and Raicu sources listed in the
[SR2PF report](ZETA23-SR2PF-PROOF-OR-COUNTEREXAMPLE-2026-08-30.md).

## 10. Revised decision tree

The review changes the next moves as follows.

1. **Semilocal Weil propagation:** stop spending effort on stronger
   compactness, better Schatten exponents, finite moment correction, or
   division by the old Ritz floor.  The recursive pass proves qualitative
   compact-form localization and removes a separate non-Zeno gate.  At a
   singular semidefinite contact, the remaining exact socket is completed-
   zeta residual charge cancellation from the finite-dimensional radical
   into the full reference-harmonic collar germ (`KNC`).  Uniform `HRW` and
   an explicit `NR_log` rate remain stronger quantitative refinements, not
   prerequisites for existence-only continuation.  Universal `KNC` is
   RH-equivalent under the accepted interfaces; this is an exact normal form,
   not a claim that the arithmetic became easier.
2. **Trace route:** use the regulator-independent theorem to remove total
   trace-definition ambiguity, but do not infer positivity or separate block
   convergence from it.
3. **CA4:** scalar natural-mask replacement is ruled out at the required
   scale.  The surviving route is the signed joint product-graph edge-edge
   estimate that retains the actual selector and common kernel.
4. **LTRAD:** generic frame or recurrence arguments are saturated by the
   Fejer family.  The missing theorem must extract source-preserving
   actual-prime structure within the finite aperture.
5. **SR2PF:** the all-cut terminator is already closed.  Work belongs upstream
   on faithful transport; weakening to one flattening loses the theorem.
6. **R71/R87/R89:** exact recompletion and parity selection close the proposed
   gain mechanisms.  Reopening them requires a genuinely signed off-axis
   input, not another rearrangement.

## 11. Formal and analytic artifacts

- [Operator theorem suite](ZETA23-OPERATOR-LEMONADE-THEOREM-SUITE-2026-09-01.md)
- [Singular common-regulator theorem](ZETA23-SINGULAR-WEIGHTED-HEAT-ANOMALY-THEOREM-2026-09-01.md)
- [Arithmetic provenance and higher-structure synthesis](ZETA23-ARITHMETIC-PROVENANCE-DESCENT-AND-HIGHER-STRUCTURE-SYNTHESIS-2026-08-31.md)
- [Harmonic-resolvent Ward audit](ZETA23-HARMONIC-RESOLVENT-WARD-PROPAGATION-AUDIT-2026-09-01.md)
- [Semilocal Ward formalization](../lean/rhbridge/RHBridge/SemilocalWardDistillation.lean)
- [Semilocal anomaly formalization](../lean/rhbridge/RHBridge/SemilocalHankelTraceNoGo.lean)
- [Second-order preflight](context/zeta23_second_order_distillation_preflight_v1.json)

## Final claim ledger

- Major Theorems A, B, D, E, G, H and Lemmas 1--7: exact standard,
  elementary, or project-proved statements as marked.
- Major Theorem C: exact analytic construction; its scalar arbitrary-near-zero
  blowup core is Lean-checked.
- Major Theorem F: analytic proof under the displayed singular-integrability
  and positive-kernel approximate-identity hypotheses.
- Project Theorem I: proved in the faithful all-cut passport using an imported
  secant classification; upstream transport remains open.
- New uniform zero-free strip: **not proved**.
- Sharp four-cycle bound / `CA4`: **not proved**.
- RH: **not proved**.
