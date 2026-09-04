# Hostile referee audit of the recursive fixed point

**Date:** 2026-09-01  
**Scope:**
`ZETA23-RECURSIVE-CONSOLIDATION-FIXED-POINT-2026-09-01.md` and
`ZETA23-QUALITATIVE-REFERENCE-LOCALIZATION-AND-CHARGED-NULLSTATE-CONTINUATION-2026-09-01.md`  
**Verdict:** the FP1--FP4 qualitative-continuation core survives the audit;
seven statement/typing corrections and two application qualifications were
required and were subsequently applied.  This was therefore a
nonzero-delta hostile pass, not a convergence certificate.  RH, the uniform
strip, and completed-zeta kernel null-charge remain open.

## 1. Load-bearing continuation chain

| component | verdict | exact qualification |
|---|---|---|
| compact embedding of the bounded-support log-form domain | passes | the outer support must be finite |
| inward support core and both monotone domain limits | passes | relative moment correction is uniform only on `[a,b]` with `a>0` |
| `K_L=J P_L J*`, monotonicity, and the exact norm identity | passes | adjoints use the form norm on the source and `L2` on the target |
| two-moment relative retraction | passes | the ambient pivot is `H_L intersect ker ell`, not all of `H_L` |
| bounded completed-Weil residual | passes analytically | a fixed-outer-slab restriction lemma must be stated explicitly |
| positive gap off a semidefinite radical | passes | it is a pointwise-in-`L` gap; no compact-slab uniformity follows |
| charged-nullstate Schur continuation | passes | work over the real form, or add the complex polarization step |
| maximal-support supremum argument | passes | use one fixed outer slab, e.g. `[L_*,L_*+1]`, in the final crossing |
| first-contact criterion | passes as an abstract equivalence | the relative `{0,1}` RH socket still needs the explicit half-density/sign adapter |

### 1.1 Compactness and support cores

The band-limited maps

\[
 A_Tf=1_{I_B}{\cal F}^{-1}(1_{[-T,T]}\widehat f)
\]

are Hilbert--Schmidt on `L2(I_B)`, and on the form unit ball

\[
 \|f-A_Tf\|_{L^2(I_B)}^2
 \le {1\over2\pi}\int_{|t|>T}|\widehat f(t)|^2dt
 \le {\mathfrak h(f,f)\over1+m(T)}.
\]

Thus the inclusion is compact.  Normalized inward dilations are uniformly
bounded and strongly continuous in `L2((1+m(t))dt)`, so the asserted support
core is valid.  Intersections handle decreasing supports; dilation and
mollification handle increasing supports.

For the relative spaces, the fixed interior right inverse `C` is valid on a
compact positive slab.  Applying `Pi=I-C ell` to full-space approximants
proves both form-core density and pivot-space density.  Nothing here gives a
uniform corrector as the left endpoint tends to zero, and the reports
correctly avoid that claim.

### 1.2 Resolvent identity

For nested form subspaces, `P_{L'}-P_L` is the form-orthogonal projection
onto `W_{L,L'}`.  Therefore

\[
 K_{L'}-K_L=J P_W J^*=(JP_W)(JP_W)^*
\]

and

\[
 \|K_{L'}-K_L\|
 =\sup_{0\ne w\in W_{L,L'}}{\|Jw\|_2^2\over\|w\|_{\mathfrak h}^2}.
\]

Strong convergence of the nested projections, compactness of `J*`, and
uniform boundedness give norm convergence.  This step has no hidden
closed-range or inverse assumption.

### 1.3 Fixed-slab residual

The residual decomposition is valid on every finite outer slab: the
digamma multiplier minus `1+m` is bounded, the pole term is finite rank, and
only finitely many prime-power translations can meet the slab.  To make the
restriction convention self-contained, add the lemma

\[
 \langle f,\tau_a g\rangle=0
 \quad\text{if }f,g\text{ are supported in }I_L
 \text{ and }|a|\ge \operatorname{diam}(I_L).
\]

It shows directly that the fixed outer form restricted to `V_L` equals the
intrinsic form at `L`, including at activation equality, where the supports
meet only on a null set.

### 1.4 Spectral gap and maximal support

A nonnegative closed form with compact form embedding has compact resolvent.
Its radical is finite-dimensional, and the first eigenvalue on its `L2`
orthogonal complement is strictly positive.  This proves the pointwise
constant `gamma_L`; it does not make `inf_L gamma_L` positive.

The supremum argument is also sound.  If positivity fails, downward
inheritance bounds the positive-support set.  Left form-core density closes
positivity at its supremum, and pointwise semidefinite continuation crosses
that supremum.  In the final crossing one should explicitly choose a single
outer slab, such as `B=L_*+1`, so that `M_B`, the residual, and the resolvent
modulus are fixed while `L'` tends down to `L_*`.

## 2. Required corrections

### C1. Real versus complex kernel charge

The analytic reports alternate between arbitrary complex vectors and the
real quadratic form used by the repository.  In a complex Hermitian space,
nonnegativity of

\[
 q(n+t w,n+t w)
\]

for real `t` kills only the real part of `q(n,w)`.  Either declare FP1--FP4
over real Hilbert spaces, matching `GeneralZetaWeilForm`, or also test the
directions `w` and `i w`.  Every occurrence of `R(n,w)=0` in a complex
version then follows by full Hermitian polarization.

### C2. Kernel null-charge is not a finite-dimensional verification

The source of the charge map is the finite-dimensional radical, but the
target condition quantifies over every vector in an infinite-dimensional
collar germ and over support parameters.  Replace “exact,
finite-dimensional target” by “a finite-rank source obstruction” unless a
separate theorem reduces the collar pairing to finitely many boundary
functionals.

### C3. FP6 needs sign and finiteness hypotheses

FP6 must specify a finite channel set and

\[
 A,S,G_i,C_i,\omega_i,M_i\ge0.
\]

Without these assumptions the displayed theorem is false.  For one channel,

\[
 A=S=D=1,\ C=-1,\ G=-4,\ \omega=-1,\ M=0,\ B=-2
\]

satisfies the written component inequalities and budget, while
`A+2B+D=-2`.  With the nonnegativity hypotheses, the stated proof and the
sharp aligned scalar example are correct.

### C4. FP8 must be extended-valued and radius-qualified

For arbitrary metric maps, define the provenance modulus in `[0,infinity]`,
assume `X` is nonempty, and restrict to `r>=0`.  In the postprocessing
inequality require `L>0`; in the inverse inequality require `M>=0`.  The
descent, uniform-continuity, and optimal-Lipschitz assertions are then exact.

### C5. FP9 is a real-valued theorem

The inequalities in FP9 require
`F subset C(K;R)`, or else must be applied to real parts.  Its adaptive
application also requires every member of the bank to be valid on every
admissible configuration; a sequence of tests valid only at its paired
`a_n` is not covered.

### C6. FP10 cannot treat a normalized simplex as a gauge body directly

The Minkowski-gauge polar identity requires a closed convex resource set
containing zero (with extended values allowed).  A fixed-mass simplex does
not contain zero.  For a simplex, state feasibility via membership in
`closure(S(C))` and Hahn--Banach separation/support functions, or homogenize
it to the cone over the simplex before taking a gauge.  The quotient-norm
formula and the bi-Lipschitz conditioning inequalities are otherwise correct.

### C7. FP7 asymmetric boundary masses need a limit hypothesis

Absolute-tail concentration does not force the positive- and negative-side
masses of an asymmetric kernel to converge separately.  State the asymmetric
boundary formula conditional on those one-sided mass limits.  Without them,
only subsequential formulas hold and the regulated boundary trace can fail to
converge.

### C8. The FP7 semilocal hat corollary is not an all-domain theorem

The `O(t^-2)` estimate follows for a triangular hat and its finite linear
span.  A general vector in the logarithmic form domain has no such pointwise
Fourier decay.  Scope the displayed semilocal common-regulator identity to
the hat trial space or to explicitly stated smooth vectors, unless a separate
uniform form-norm density argument is supplied.

### C9. FP12 needs trace-ideal typing

The commutator product rule is algebraically exact for bounded factors.  Its
trace “anomaly ledger” consequence additionally requires finite dimension or
trace class for every cyclic product before and after rotation (for example,
a designated trace-class factor in each bounded cyclic word), or a separately
proved common regularization permitting those moves.  Trace class of only the
final displayed summands is not sufficient.

## 3. FP5--FP11 formula audit

- **FP5:** passes after requiring `M_n>=0` (or discarding finitely many
  initial indices).  With multiplicity `m=r+1` and
  `delta_n<=eta_{mn}^2/4`, the forward block, selected cross block, and old
  block obey the requested envelope after sorting.  The identity
  `|B_n|^2=(1+epsilon_n)(delta_n-epsilon_n)` and
  `epsilon_n=delta_n/(1+M_n^2)` gives
  `|B_n|/sqrt(A_n)=M_n sqrt(1+epsilon_n)` exactly.
- **FP6:** correct only after C3.
- **FP7:** the interior absolute-tail theorem is consistent; the asymmetric
  boundary sentence and the semilocal trial-space scope need C7--C8.
- **FP8:** the inequality directions are correct; C4 supplies missing
  typing.
- **FP9:** the common-modulus proof is correct; C5 supplies missing scalar
  and quantifier scope.
- **FP10:** quotient duality and condition-number bounds pass; the convex
  resource-body sentence needs C6.
- **FP11:** both firewalls pass.  `lambda^tensor k-eta^tensor k` has rank at
  most two under every flattening, and the odd-channel coefficient
  `2^(1-k)` is correct.  “Higher odd channels necessarily appear” should be
  read as a universal formal identity, not as nonvanishing for every special
  `lambda,eta`.

## 4. RH sockets and status

The full-space final socket is the repository's explicitly imported
classical Weil-criterion axiom and is correctly labeled as an imported
interface, not as a kernel-checked theorem.

For the two-moment relative socket, Connes--Consani Appendix C,
Proposition C.1 does permit the finite vanishing set `{0,1}`.  The project
should nevertheless display the short adapter: under the logarithmic
half-density transform, Mellin vanishing at `0` and `1` becomes `ell_-=0`
and `ell_+=0`, respectively; then the sign convention for the project's Weil
form must be matched to the paper.  Until that adapter is written, the
relative-only RH implication is an imported, normalization-matched claim in
prose rather than a proved project theorem.  The full-space FP4 route does
not depend on this relative socket.

## 5. Convergence consequence

Because C1--C9 were genuine statement or scope changes, the then-advertised
final two zero-delta passes could not remain terminal.  The corrections were
subsequently applied; the normalized hostile operator must be rerun twice,
and convergence may be certified only if both reruns are zero-delta.  None of
the corrections reopens the FP1 compact-localization proof or the FP3--FP4
abstract continuation argument; they prevent those valid results from being
stated more broadly than proved.

## 6. Remediation record

All nine corrections were applied before the terminal reruns:

- C1: the analytic report now uses real spaces and real polarization
  consistently, with the complex Hermitian phase variant stated separately;
- C2: KNC is described as a finite-dimensional **source** and an
  infinite-dimensional collar identity;
- C3--C7: the channel signs/finiteness, extended provenance radii,
  globally valid real certificate family, non-gauge simplex, and asymmetric
  one-sided-mass hypotheses are explicit;
- C8: the `O(t^-2)` semilocal trace corollary is restricted to the triangular-
  hat finite span or an explicitly stated smooth class; and
- C9: the anomaly trace ledger is now finite-dimensional or assumes trace
  class for every pre/post-rotation cyclic product, or one independently
  justified common regularization.

The maximal-support proof fixes `B=A+1`, and the relative `{0,1}` criterion
now displays both the half-density moment map and the sign translation.  The
subsequent KNC audit supplied a further nonzero decision-tree delta, so the
fresh zero-pass count begins only after that result is incorporated.
