# Operator lemonade: theorem suite distilled from the semilocal failure

Date: 2026-09-01

## Verdict

The failed compact-Hankel proof does yield a useful general theorem package.
Its strongest negative statement is not merely that compactness is too weak:
for a unitary colligation with one compact leakage direction, the reverse
direction is **binary in the Calkin algebra**.  It is either compact too, or
it has essential norm exactly one and contributes `-1` to the essential
spectrum of the signed projection defect.

Moreover, this maximal reverse channel survives every finite list of moment
constraints.  A genuine projection-difference construction shows that the
old energy and the Ward cross can both lie in every Schatten class while the
Ward/Schur response diverges at any prescribed rate.  Thus neither more
moments nor arbitrarily strong qualitative Schatten decay can repair this
class of argument.

The corresponding positive theorem is equally precise: a Ward estimate
follows when every cross-channel contamination is factored through an
independently available positive reserve in the old energy.  This
``reserve-absorbed alignment`` principle gives the exact shape of useful new
mathematics.

A later recursive pass sharpens the propagation interpretation: at a fixed
semidefinite support, exact kernel null-charge is the necessary and sufficient
local condition; reserve-absorbed alignment is one stronger sufficient route
to it.

These are reusable operator-theoretic results.  They do not prove zeta
propagation, a zero-free strip, or RH.

## 1. Bidirectional leakage identity

Let

\[
 \mathcal H=\mathcal H_+\oplus\mathcal H_-,\qquad
 P=\begin{pmatrix}I&0\\0&0\end{pmatrix},\qquad
 U=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]

with `U` unitary, and put

\[
 \Delta=P-U^*PU.
\]

### Theorem 1: bidirectional leakage

One has

\[
 \Delta=
 \begin{pmatrix}
 c^*c&-a^*b\\
 -b^*a&-b^*b
 \end{pmatrix}
 =
 \begin{pmatrix}
 c^*c&c^*d\\
 d^*c&-b^*b
 \end{pmatrix},                                      \tag{1.1}
\]

\[
 \Delta^2=
 \begin{pmatrix}c^*c&0\\0&b^*b\end{pmatrix},
 \qquad
 |\Delta|=|c|\oplus|b|.                              \tag{1.2}
\]

Consequently, for every Schatten exponent `p>0`,

\[
 \|\Delta\|_p^p=\|c\|_p^p+\|b\|_p^p,
 \qquad
 \|\Delta\|_{\rm ess}
 =\max(\|c\|_{\rm ess},\|b\|_{\rm ess}).           \tag{1.3}
\]

Proof.  Unitarity gives `a^*a+c^*c=I` and
`a^*b+c^*d=0`, yielding (1.1).  Either direct multiplication or the fact that
`P` and `U^*PU` are projections gives (1.2); functional calculus gives the
remaining assertions.  This is standard two-projection geometry, going back
to [Halmos](https://www.ams.org/tran/1969-144-00/S0002-9947-1969-0251519-5/S0002-9947-1969-0251519-5.pdf),
with index refinements due to
[Avron--Seiler--Simon](https://phsites.technion.ac.il/avron/wp-content/uploads/sites/3/2013/05/J_Func_Anal_120_220_1994_index_pair.pdf).

The important interpretation is that the full defect measures both directed
leakages exactly.  Compactness or Schatten control of `c` alone says nothing
quantitative about `Delta` until `b` is controlled.

There is also an exact spectral-pairing identity.  With `Q=U^*PU` and
`J=P+Q-I`,

\[
 J\Delta=-\Delta J,\qquad J^2=I-\Delta^2.            \tag{1.4}
\]

Thus every nonzero eigenvalue in `(-1,1)` is paired with its negative, with
the same multiplicity.  The endpoint defect spaces at `+/-1` need not pair in
infinite dimension.  This is why the construction in Section 4 retains an
unused `-delta_n` companion for every small positive mode while drawing its
fixed negative reservoir from the `-1` endpoint.

## 2. One-sided Calkin dichotomy

### Theorem 2: compact-or-maximal reverse leakage

Assume `c` is compact.  Then exactly one of the following holds:

1. `b` is compact, and `Delta` is compact;
2. `b` is noncompact,
   \[
   \|b\|_{\rm ess}=\|\Delta\|_{\rm ess}=1,
   \qquad -1\in\sigma_{\rm ess}(\Delta).             \tag{2.1}
   \]

More precisely, if `pi` denotes the Calkin quotient, then

\[
 e=\pi(b^*b)
\]

is a projection and

\[
 \pi(\Delta)=0\oplus(-e).                            \tag{2.2}
\]

Proof.  Since `a^*b=-c^*d`, the cross block is compact.  Also

\[
 b^*b-(b^*b)^2
 =b^*aa^*b=(a^*b)^*(a^*b),                           \tag{2.3}
\]

which is compact.  Hence `e` is a projection in the Calkin algebra.  If
`e=0`, then `b^*b`, hence `b`, is compact, and every block in (1.1) is
compact.  If `e` is nonzero, every nonzero projection in a C*-algebra has
norm one.  Equations (2.1)--(2.2) follow.

This corollary is elementary Calkin algebra and is probably standard.  Its
use as a quasi-inner/Ward dichotomy is the useful synthesis: the uncontrolled
polarization is not merely potentially large; modulo compact operators it is
an all-or-nothing negative projection.

## 3. Finite constraints are invisible to essential channels

### Theorem 3: finite-codimension immunity

Let `E` be a closed finite-codimensional subspace of a Hilbert space and
`P_E` its projection.  For every bounded operator `T`,

\[
 \|T|_E\|_{\rm ess}=\|T\|_{\rm ess}.                \tag{3.1}
\]

If `T` is self-adjoint, the compression has the same essential spectrum:

\[
 \sigma_{\rm ess}(P_ET|_E)=\sigma_{\rm ess}(T).      \tag{3.2}
\]

Indeed, `T-TP_E=T(I-P_E)` and `T-P_ETP_E` are finite rank.  This is an
elementary Calkin fact.  In particular, no finite list of bounded moment,
parity, or boundary constraints can remove the `-1` channel in Theorem 2.

There is also an exact, rather than essential, version.  If `b` is an
isometry on an infinite-dimensional space `S`, then `S intersect E` remains
infinite-dimensional and `b` is still an isometry there.

The kernel-checked finite-dimensional shadow says that `m` scalar constraints
remove at most `m` dimensions.  It is formalized in
`RHBridge.SemilocalWardDistillation`.

## 4. A genuine projection-defect Ward catastrophe

The preceding theorems concern essential spectrum.  The following
construction shows that the precise Ward failure can occur inside an actual
unitary projection defect, even with extremely strong compactness on every
apparently favorable block.

### Theorem 4: all-Schatten spectral-mixing obstruction with arbitrary rate

For every finite constraint count `r`, there exist a separable Hilbert space,
an orthogonal projection `P`, and a unitary `U` with the following universal
property: for every closed subspace `E` of codimension at most `r`, there are
orthogonal old/collar subspaces `O,W` contained in `E` such that, for
`Delta=P-U^*PU`:

1. the forward block `c` belongs to every Schatten class `S_p`, `p>0`;
2. the reverse block has essential norm one;
3. `A=P_O Delta|_O` is positive, injective, and compact, but not bounded below;
4. `A` and `B=P_O Delta|_W` belong to every `S_p`, `p>0`;
5. with reference form `h=I`, `W` is exactly h-harmonic relative to `O`;
6. nevertheless `A^{-1/2}B` is unbounded.

More strongly, for every prescribed sequence `M_n>=0`, the witnesses may be
chosen so that the `n`th squared Ward quotient is greater than `M_n`.  Thus
the instability can diverge at an arbitrary preassigned rate while both
visible defect blocks have faster-than-polynomial singular-value decay.

The construction can be duplicated so that the obstruction occurs in both
parities of a commuting reflection.

#### Construction

Let `K=ell^2(N_0) tensor ell^2(N)`, let `S` be the unilateral shift of
infinite multiplicity, and let `E_0=I-SS^*`.  On `K_+ direct-sum K_-`, set

\[
 U_0=\begin{pmatrix}S&E_0\\0&S^*\end{pmatrix}.       \tag{4.1}
\]

This is unitary, its forward block is zero, and

\[
 P-U_0^*PU_0=0\oplus(-E_0).                          \tag{4.2}
\]

Thus it supplies an infinite `-1` reservoir.  Put `m=r+1`,
`delta_n=2^{-n}`, `gamma_n=(1-delta_n^2)^{1/2}`, and append the rotation
blocks

\[
 U_n=
 \begin{pmatrix}
 \gamma_nI_m&-\delta_nI_m\\
 \delta_nI_m&\gamma_nI_m
 \end{pmatrix}.                                     \tag{4.3}
\]

Their defects have eigenvalues `+/-delta_n`, each with multiplicity `m`.
The total forward block is `0 direct-sum diag(delta_n I_m)`, so it lies in
every `S_p`.  Every positive eigenspace meets `E` because its dimension is
`r+1`; choose a unit `t_n` in that intersection.  Choose orthonormal `s_n`
from the `-1` reservoir inside `E`.

For the basic divergent family, set `epsilon_n=delta_n^2` and

\[
 \alpha_n^2=\frac{1+\epsilon_n}{1+\delta_n},\qquad
 \beta_n^2=\frac{\delta_n-\epsilon_n}{1+\delta_n},  \tag{4.4}
\]

\[
 u_n=\alpha_nt_n+\beta_ns_n,
 \qquad
 w_n=-\beta_nt_n+\alpha_ns_n.                       \tag{4.5}
\]

The families are orthonormal.  With
`O=closure(span{u_n})` and `W=closure(span{w_n})`, exact algebra gives

\[
 \langle u_n,\Delta u_n\rangle=\delta_n^2,          \tag{4.6}
\]

\[
 |\langle u_n,\Delta w_n\rangle|^2
 =(1+\delta_n^2)(\delta_n-\delta_n^2).              \tag{4.7}
\]

Therefore

\[
 \frac{|\langle u_n,\Delta w_n\rangle|^2}
      {\langle u_n,\Delta u_n\rangle\|w_n\|^2}
 =(1+\delta_n^2)(\delta_n^{-1}-1)\longrightarrow\infty. \tag{4.8}
\]

Because `delta_n=2^{-n}`, the cross singular values are asymptotic to
`sqrt(delta_n)`, so `B` in fact belongs to every Schatten class.  The unused
`-delta_n` eigenvector in every rotation block supplies the spectral companion
required by two-projection geometry.

For the arbitrary-rate strengthening, start with the prescribed sequence
`M_n>=0` and put

\[
 \widetilde M_n=\max(M_n,n).
\]

Thus `widetilde M_n>=M_n` and `widetilde M_n->infinity`.  Keep
`delta_n=2^{-n}`, but replace the choice above by

\[
 \epsilon_n=\frac{\delta_n}{\widetilde M_n+2},\qquad
 \alpha_n^2=\frac{1+\epsilon_n}{1+\delta_n},\qquad
 \beta_n^2=\frac{\delta_n-\epsilon_n}{1+\delta_n}. \tag{4.9}
\]

The same two-eigenvalue calculation gives

\[
 \langle u_n,\Delta u_n\rangle=\epsilon_n,
 \qquad
 |\langle u_n,\Delta w_n\rangle|^2
 =(1+\epsilon_n)(\delta_n-\epsilon_n),              \tag{4.10}
\]

and hence

\[
 \frac{|\langle u_n,\Delta w_n\rangle|^2}
      {\langle u_n,\Delta u_n\rangle\|w_n\|^2}
 =(1+\epsilon_n)(\widetilde M_n+1)
 >\widetilde M_n\ge M_n.                          \tag{4.11}
\]

Here `epsilon_n<=delta_n` and the cross singular value is at most
`sqrt(2 delta_n)`.  Therefore both `A` and `B` lie in every `S_p`, independently
of how rapidly the prescribed `M_n` grows, while (4.11) also proves the
unboundedness in item 6 when the prescribed sequence itself is bounded.

This is a project-proved synthetic operator theorem, with its scalar algebra
checked in Lean.  The ingredients are classical, but this simultaneous
realization of arbitrary finite constraints, one-sided and cross-block
all-Schatten decay, exact harmonic splitting, and arbitrarily prescribed
divergent response is the
most plausible literature-novel synthesis in the package.  No novelty claim
is made without a dedicated referee-level search.

The broader lesson is familiar in inverse problems: compactness of `A` and
`B` separately does not control the graph norm `A^{-1/2}B`.  What matters is
their relative singular-value scale.

### Corollary 4.1: arbitrary visible singular-value envelope

The all-Schatten conclusion can be strengthened to a prescribed envelope.
Let `eta_k>0` be any nonincreasing null sequence (rescaled so `eta_k<=1`),
let `M_n>=0` with `M_n->infinity` be arbitrary, and retain a finite constraint
count `r`.
Put `m=r+1` and choose a decreasing sequence

\[
 0<\delta_n\le {1\over4}\eta_{mn}^{2},
 \qquad
 \epsilon_n={\delta_n\over1+M_n^2}.                \tag{4.12}
\]

Use the same multiplicity-`m` rotation defects and the same mixing formulas
with `epsilon_n` in place of (4.9).  Then

\[
 A_n=\epsilon_n,
 \qquad
 |B_n|^2=(1+\epsilon_n)(\delta_n-\epsilon_n),       \tag{4.13}
\]

so

\[
 {|B_n|\over\sqrt{A_n}}
 =\sqrt{(1+\epsilon_n)M_n^2}\ge M_n.               \tag{4.14}
\]

Meanwhile the forward singular values are at most `delta_n`, the selected
cross singular values are at most `sqrt(2 delta_n)`, and the old block is
smaller still.  Monotonicity of `eta`, together with the multiplicity
indexing, gives the requested singular-value bounds after harmless initial
reindexing.  The reverse essential norm remains one and finite-codimensional
immunity is unchanged.

Thus membership in **any** separately specified compact spectral ideal, or
even domination by any strictly positive null envelope, is insufficient for
Ward stability.  Strict positivity of the envelope is necessary: an
eventually zero envelope would require finite rank and is a different claim.

## 5. Positive converse: reserve-absorbed alignment

The obstruction also identifies a clean sufficient theorem.

### Theorem 5: reserve-absorbed Ward factorization

Let `X,Y,Z` be Hilbert spaces.  Let all displayed maps be bounded, let
`A,R:X->X` be positive self-adjoint, fix `eta>=0`, and suppose

\[
 A\succeq C^*C+R,\qquad R\succeq0,                  \tag{5.1}
\]

where `A,R` act on `X` and `C:X to Z`.  Let

\[
 B=C^*D+E,                                          \tag{5.2}
\]

with `D:Y to Z` and `E:Y to X`.  If

\[
 EE^*\preceq\eta^2R,                                \tag{5.3}
\]

then Douglas factorization gives `E=R^{1/2}F`, `norm(F)<=eta`, and

\[
 |\langle x,By\rangle|^2
 \le \langle x,Ax\rangle
      \langle y,(D^*D+F^*F)y\rangle.                \tag{5.4}
\]

Consequently, if `H:Y->Y` is positive self-adjoint, `C_0>=0`, and

\[
 D^*D+F^*F\preceq C_0H,
\]

then

\[
 |\langle x,By\rangle|^2
 \le C_0\langle x,Ax\rangle\langle y,Hy\rangle.    \tag{5.5}
\]

Proof.  Stack

\[
 Tx=(Cx,R^{1/2}x),\qquad Vy=(Dy,Fy).
\]

Then `B=T^*V`, `T^*T<=A`, and (5.4) is Cauchy--Schwarz.  No inverse or
closed-range hypothesis is used.  The factorization input is the classical
[Douglas lemma](https://www.ams.org/proc/1966-017-02/S0002-9939-1966-0203464-1/S0002-9939-1966-0203464-1.pdf).

Exact alignment is `R=E=0`.  For the Hardy block in (1.1), take `C=c` and
`D=d`; since `d` is a contraction, this gives Ward constant one.  Approximate
alignment says something more useful than ``small error``: every contamination
must be paid by a matching positive reserve before the collapsing old metric
is inverted.

This is noncircular only when `C,D,R,E` and (5.3) are established from
independent geometry.  Defining `E` to be the whole unknown Ward block merely
renames the target.

The scalar exact-alignment and reserve-absorption inequalities are
kernel-checked in Lean.

## 6. Trace anomalies: an exact discretization budget

### Theorem 6: finite anomaly budget

For arbitrary finite square matrices `F,P,U,V`,

\[
 \begin{aligned}
 \operatorname{Tr}\bigl(F(P-VPU)\bigr)
 &=\operatorname{Tr}\bigl((FU-UF)VP\bigr)\\
 &\quad+\operatorname{Tr}\bigl(F(I-UV)P\bigr).      \tag{6.1}
 \end{aligned}
\]

No projection, adjoint, or invertibility assumption is needed.  The proof is
expansion followed by one cyclic rotation.  If `V=U^*`, `U` is unitary, and
`F` commutes with `U`, both accounts vanish.

Thus every finite anomaly-preserving scheme must carry its value in at least
one of two ledgers:

1. multiplier commutation error;
2. boundary nonunitarity/right-inverse error.

An exactly unitary cyclic DFT has neither and must return zero.  A padded
Toeplitz section can carry the anomaly only through its boundary defect.  A
valid convergence proof must track these accounts rather than merely compare
the final scalar.

Equation (6.1) and its zero corollary are proved in Lean.  Conceptually they
belong to the trace-of-commutator tradition of
[Helton--Howe](https://mathweb.ucsd.edu/~helton/BILLSPAPERSscanned/HHo75.pdf)
and [Connes's cyclic cohomology](https://pmihes.centre-mersenne.org/articles/10.1007/BF02698807/),
but the identity itself is elementary.

With a regulator `W`, the exact product-rule refinement is

\[
\begin{aligned}
 \operatorname{Tr}\bigl(WF(P-VPU)\bigr)
 &=\operatorname{Tr}\bigl(W(FU-UF)VP\bigr)\\
 &\quad+\operatorname{Tr}\bigl((WU-UW)FVP\bigr)\\
 &\quad+\operatorname{Tr}\bigl(WF(I-UV)P\bigr).    \tag{6.2}
\end{aligned}
\]

Thus, when `FU=UF` and `UV=I`, the entire finite regulated anomaly lies in
the regulator commutator `WU-UW`.  Equation (6.2) and this corollary are also
Lean checked.

## 7. A common heat regulator

### Theorem 7: smooth heat-anomaly recovery

Give the circle normalized Haar measure, write `e_n(theta)=exp(i n theta)`,
let `N e_n=n e_n`, and define `P e_n=1_{n<=0}e_n`.  Let
`u in C^1(S^1,S^1)`, put `U=M_u`, and let `g` be continuous.  If

\[
 R_\epsilon=e^{-\epsilon N^2/2},
\]

then

\[
 \lim_{\epsilon\downarrow0}
 \operatorname{Tr}\bigl(
 R_\epsilon M_g(P-U^*PU)R_\epsilon\bigr)
 =\frac1{2\pi}\int_{S^1}g(\theta)
   (-i\overline u u')(\theta)\,d\theta.              \tag{7.1}
\]

Proof.  The defect has the continuous kernel

\[
 K_u(s,t)=\frac{1-\overline{u(s)}u(t)}
                 {1-e^{-i(s-t)}},
 \qquad K_u(s,s)=-i\overline u(s)u'(s).              \tag{7.2}
\]

Since `R_epsilon` is trace class, cyclicity combines the two copies into
`e^{-epsilon N^2}`.  Its kernel is the circle heat approximate identity.
Uniform continuity of (7.2) then gives (7.1).

This is a folklore-level heat-kernel lemma rather than new trace theory.  The
quantized-differential kernel appears in
[Connes--Consani](https://arxiv.org/html/2006.13771), and heat-regularized
noncommutative traces have classical precedent in
[Jaffe--Lesniewski--Osterwalder](https://lesniewski.us/papers/published/QuantumKTheoryI.pdf).
The point is methodological: a common smooth regulator has a theorem behind
it, whereas independent hard cutoffs of the four signed blocks need not
converge.

## 8. Singular weighted common-regulator recovery

### Theorem 8: punctured-circle common-regulator recovery

Let `Sigma` be a nonempty finite set, let `u` be measurable, unimodular, and
`C1` off `Sigma`, and let `g` be bounded.  Put `delta=dist(.,Sigma)` and let
`Lambda_u` be the derivative supremum on the nonsingular half-ball.  The
smooth theorem extends when the weight kills both the local derivative growth
and flux across each cut.  Precisely, if

\[
 |g|(1+\Lambda_u+\delta^{-1})\in L^1,
\]

then the same heat limit (7.1) holds.  More generally, replace the squared
heat regulator by any trace-class convolution approximate identity whose
kernel has mass one, uniformly bounded `L1` norm, and absolute tails tending
to zero.  The kernel may be signed, complex, and asymmetric for the interior
limit.  If the convolution operator is also spectrally positive, its
Hilbert--Schmidt square root used on both sides gives the same total limit.
Heat, Poisson/Abel, and Fejer regulators all qualify.  The singular set can
also be any nonempty closed null set when `u` is locally `W1,infinity` on its
complement and `Lambda_u` is the local essential derivative envelope; the
empty set is the ordinary globally smooth/Sobolev case.

For a finite nonempty singular set, under the near-set power bounds
`|u'|<=C delta^{-alpha}(1+|log delta|)^k` and
`|g|<=C_g delta^beta`, with `alpha,k>=0`, it suffices that

\[
 \beta>\max(\alpha-1,0).                             \tag{7.3}
\]

For a general closed null set, this shortcut requires a neighborhood bound
`mu{delta<r}=O(r^kappa)` and becomes
`beta>max(alpha-kappa,1-kappa)`; nullity alone gives no power threshold.
This is a project-proved singular weighted extension, with novelty not
established.  For a phase-uniform finite-singular-set theorem, the additional
`beta>0` cannot be removed: some nontrivial phase jumps with nonvanishing
weight contribute explicit boundary flux.  For the semilocal Cayley phase,
`(alpha,beta)=(2,4)` and the
singular set is finite, so the theorem rigorously recovers the total Weil
anomaly under common heat regularization on the stated trial class.  It does
not give separate limits for the four Hardy blocks.  The complete proof and sharp
boundary term are recorded in
[`ZETA23-SINGULAR-WEIGHTED-HEAT-ANOMALY-THEOREM-2026-09-01.md`](ZETA23-SINGULAR-WEIGHTED-HEAT-ANOMALY-THEOREM-2026-09-01.md).

## 9. Localized phase gauges are not identifiable

### Theorem 9: support-invisible phase gauge

Let `lambda>0`, choose a nonzero sufficiently small `alpha`, and put

\[
 v(t)=e^{i\alpha\sin(\lambda t)}.
\]

Then

\[
 -i\overline vv'=\alpha\lambda\cos(\lambda t).       \tag{8.1}
\]

If `g=hat f overline{hat h}` and the correlation
`f convolution tilde h` is supported strictly inside `(-lambda,lambda)`,
then

\[
 \frac1{2\pi}\int_{\mathbb R}g(t)(-i\overline vv')(t)\,dt=0. \tag{8.2}
\]

Nevertheless the Hardy commutator of multiplication by `v` is nonzero.  In
the physical representation, the Bessel expansion of `v` contains nonzero
translations by `+/-lambda`, which cross a half-line boundary.

Therefore localized logarithmic-derivative data determines a phase only
modulo a nontrivial gauge class, while its Hankel singular data need not be
constant on that class.  The inactive-prime phenomenon is the arithmetic
instance: an Euler factor outside the support window is invisible to every
licensed Weil pairing but changes the global Hardy block.

This is an elementary inverse-problem theorem.  It applies equally to
band-limited scattering and system identification and explains why singular
vectors of an un-frozen phase are not observables of the localized generator.

## 10. Novelty and broader use

| Result | Status | Likely novelty |
|---|---|---|
| bidirectional leakage / spectral pairing | imported standard operator theory | none |
| finite-codimension essential invariance | elementary standard fact | none |
| one-sided Calkin dichotomy | project-proved corollary | low; useful synthesis |
| arbitrary-rate all-Schatten projection-defect Ward countermodel | project-proved construction | potentially new combination; unclaimed |
| reserve-absorbed alignment | project-proved Douglas/Cauchy consequence | low as abstract operator theory; useful formulation |
| finite anomaly budget | Lean-proved matrix identity | elementary; useful numerical design rule |
| smooth heat recovery | self-contained standard/folklore lemma | low |
| singular weighted heat recovery and boundary flux | project-proved analytic theorem | novelty not established |
| support-invisible phase gauge | elementary project theorem | low; broad inverse-problem interpretation |

The main applications are not restricted to zeta:

- **domain decomposition:** compact interface coupling does not control a
  Schur complement against a collapsing interior metric;
- **inverse problems:** separate compactness of a forward map and residual
  does not imply graph-norm stability;
- **scattering/model spaces:** one-sided quasi-innerness can coexist with a
  maximal reverse essential channel;
- **numerical anomalies and indices:** exact cyclic/unitary finite models erase
  the invariant they are intended to approximate;
- **robust factorization:** contamination is harmless only when absorbed by a
  matched positive reserve.

## 11. Consequence for the zeta decision tree

The semilocal route cannot be repaired by adding finitely many moments,
improving the Schatten exponent of the compact block, or proving compactness
of the Ward cross.  Theorem 4 simultaneously allows all of these while the
Ward quotient diverges.

The later recursive fixed-point pass supersedes the original two-move
priority stated in earlier versions of this section.  At a semidefinite
support, exact completed-zeta kernel null-charge (`KNC`) is the necessary and
sufficient local right-openness condition.  A zeta-specific reserve
decomposition satisfying (5.1)--(5.3), or exact Hardy alignment, remains a
stronger sufficient quantitative route to that condition.  The total
common-regulator theorem is now proved; separate-block limits may still be of
independent interest, but total trace legitimacy does not supply KNC or
positivity.  Universally quantified completed-zeta KNC is RH-equivalent under
the accepted Weil/continuity interfaces and remains open.

## Claim ledger

- Theorems 1--3: standard facts with self-contained derivations;
- Theorem 4 and Corollary 4.1: exact analytic constructions, unrefereed; the
  basic scalar identities and arbitrary-near-zero unboundedness are Lean
  checked;
- Theorem 5: exact Hilbert-space argument; scalar version Lean checked;
- Theorem 6: Lean kernel checked;
- Theorem 7: self-contained smooth-kernel proof, folklore-level;
- singular weighted extension: project-proved analytic theorem, unrefereed;
- support-invisible phase gauge: exact elementary Fourier-support argument;
- literature-level novelty for the combined construction: not established;
- compact-slab-uniform quantitative `HRW` remains open; qualitative
  propagation from universal completed-zeta `KNC` is proved, while that KNC
  premise (RH-equivalent under the accepted interfaces), a zero-free strip,
  and RH remain open.

## Artifacts

- Lean theorem suite:
  [`SemilocalWardDistillation.lean`](../lean/rhbridge/RHBridge/SemilocalWardDistillation.lean)
- finite anomaly budget:
  [`SemilocalHankelTraceNoGo.lean`](../lean/rhbridge/RHBridge/SemilocalHankelTraceNoGo.lean)
- scalar countermodel implementation:
  [`semilocal_hankel_poisson_gate.py`](../src/semilocal_hankel_poisson_gate.py)
- theorem passport:
  [`zeta23_operator_lemonade_preflight_v1.json`](context/zeta23_operator_lemonade_preflight_v1.json)
- singular heat theorem:
  [`ZETA23-SINGULAR-WEIGHTED-HEAT-ANOMALY-THEOREM-2026-09-01.md`](ZETA23-SINGULAR-WEIGHTED-HEAT-ANOMALY-THEOREM-2026-09-01.md)
- postflight:
  [`zeta23_operator_lemonade_postflight_v1.json`](context/zeta23_operator_lemonade_postflight_v1.json)
- Lean sub-passport:
  [`zeta23_semilocal_distillation_preflight_v1.json`](context/zeta23_semilocal_distillation_preflight_v1.json)
