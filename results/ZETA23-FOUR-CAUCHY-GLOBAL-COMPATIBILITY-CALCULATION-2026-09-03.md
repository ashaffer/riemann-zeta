# ZETA23 four-Cauchy exterior-source calculation and compatibility audit

Date: 2026-09-03  
Registry: R185  
Status: exact smooth-core exterior calculation and narrow mechanism falsifier;
global old/exterior compatibility remains open; no
completed-source factor, uniform zero-free strip, four-cycle bound, or RH

**R186 closeout correction.**  The split finite part and the genuine
form-domain state adapter have now been closed in the correct weak/L2
topology; see
[`ZETA23-SPLIT-CARLEMAN-FORM-DOMAIN-CLOSEOUT-2026-09-03.md`](ZETA23-SPLIT-CARLEMAN-FORM-DOMAIN-CLOSEOUT-2026-09-03.md).
Statements below that call either adapter “missing” record the state at the
time of R185 and are superseded.  Endpoint/all-jet traces remain unavailable
for a generic form-domain element.  This correction does not advance the
still-open compatibility implication.

Preflight:
[`zeta23_four_cauchy_global_compatibility_preflight_v1.json`](context/zeta23_four_cauchy_global_compatibility_preflight_v1.json)

## 0. Verdict

The exterior-source calculation is complete at the smooth-core level licensed
by the R184 source normal form.  The global old/exterior compatibility
calculation is **not** complete: the old Lerch operator is a split
finite-part/Carleman operator, and the derivation below does not use the old
homogeneous equation.  It finds one real cancellation, but not the sought
global compatibility identity.

The fourth-root Cauchy filter cancels exactly one decaying pole mode on each
exterior side.  It leaves the opposite growing pole mode, an infinite
every-fourth-moment tail, and the active prime-dilation samples.  Moreover,
fourth-root rotations and positive dilations commute before localization.
The anticipated root--dilation mixing therefore does not exist.
Multiplicative reflection instead normalizes the dilation group by swapping
`r` with `1/r`; the actual bilateral prime source is invariant under this
swap.  Fixed-window projection then adds an explicit two-boundary leakage
cocycle.

For fixed `0<a<b`, let `mathcal E_(L,a,b)` and
`mathcal E_(R,a,b)` denote the restrictions of the exterior formulas below to
`e^(-b/2)<X<alpha` and `beta<X<e^(b/2)`.  The remaining statement is

\[
  \ker \mathcal B_a\subseteq
  \ker(\mathcal E_{L,a,b}\oplus\mathcal E_{R,a,b}).     \tag{0.1}
\]

Using the R186 weak/L2 adapter, this is localized kernel-null charge (KNC)
itself.  The exterior derivation displayed in this report is on the smooth
localized core; R186 subsequently serialized the full split old equation and
extended the finite-collar readout by closure.  Neither that state-space
completion, the exterior Cauchy assembly, nor naive
Möbius inversion reduces (0.1), and we did not construct a bounded or closable
inverse-free `T^src`.

This closes only the particular R184 mechanism described as a
*scalar root--positive-dilation noncommutativity*.  It does not close an
orientation-sensitive four-Cauchy/Carleman compatibility identity, much less
a zeta-specific continuum identity, quasianalytic theorem, or
spectral-synthesis mechanism establishing KNC.

## 1. Passport and exact state

Fix `a>0` and

\[
 I_a=(-a,a),\qquad
 J=(\alpha,\beta)=(e^{-a/2},e^{a/2}),
\]

and let `n` be a smooth function compactly supported in `I_a`, extended by
zero.  Suzuki's sign convention is

\[
 g=-\Psi,\qquad W=-g''=\Psi''.                       \tag{1.0}
\]

Put

\[
 f(X)=n(2\log X),\qquad
 M_\sigma=\int_{-a}^{a}e^{\sigma y/2}n(y)\,dy,
\]

and

\[
 C_f(z)=\frac{1}{2\pi i}\int_\alpha^\beta
        \frac{f(Y)}{Y-z}\,dY,qquad C_{f,+}-C_{f,-}=f.  \tag{1.1}
\]

Write

\[
 c_\Gamma=\psi(1/4)-\log\pi,qquad
 r_m=\sqrt m,qquad w_m=\frac{\Lambda(m)}{\sqrt m}.
\]

On the old interval the completed-source normal form is

\[
 \mathcal B_af=
 \mathcal Rf+c_\Gamma f-\mathcal P_af-\mathcal L_af,   \tag{1.2}
\]

where

\[
 (\mathcal Rf)(X)=XM_{-1}+X^{-1}M_1,                  \tag{1.3}
\]

\[
 (\mathcal P_af)(X)=
 \sum_{\log m<2a}w_m\{f(X/r_m)+f(r_mX)\},            \tag{1.4}
\]

with `f=0` off `J`.  Here `mathcal L_a` is not one ordinary full-contour
Plemelj jump.  Its exact old-interval action is the split finite part

\[
 \mathcal L_af(X)=\frac12\operatorname{FP}\!\left[
 \sum_{\zeta^4=1}\int_\alpha^X\frac{f(Y)}{X-\zeta Y}\,dY
 +\sum_{\zeta^4=1}\zeta^{-1}\int_X^\beta
       \frac{f(Y)}{Y-\zeta X}\,dY\right].           \tag{1.4a}
\]

The `FP` includes the exact diagonal subtraction inherited from R184.  In the
`zeta=1` channel it regularizes a positive two-sided `1/|Y-X|` singularity,
not the oriented principal value represented by a single Cauchy boundary
jump.  Thus the four full transforms in (1.1), their Plemelj jumps, and their
normalization do not by themselves serialize (1.2).  The diagonal counterterm
and local completion `c_Gamma f` are part of (1.2); neither may be discarded.
The exterior local completion vanishes because it is supported at additive
displacement zero.

A homogeneous old/contact state is an admissible Cauchy state satisfying
`mathcal B_a f=0`; an arbitrary smooth localized `f` need not do so.
Here `mathcal B_a` denotes the smooth-core distributional expression in
(1.2), not Suzuki's full self-adjoint operator.  In Suzuki's current setup,
`B_a=D^*G_aD` begins on the Sobolev core and `A_a` is its Friedrichs
extension, whose domain is larger.  R186 maps every element of `ker A_a` into
a weak old equation and an `L2` finite-collar Cauchy state, but not into the
pointwise/jet state used below.  Mean-zero projection
does not add a missing smooth-core source term: `Dn` is mean-zero and `D^*`
kills the subtracted constant.

The four archimedean ray states are

\[
 F_\zeta(z)=\zeta^{-1}C_f(\zeta^{-1}z),
 \qquad \zeta^4=1,                                   \tag{1.5}
\]

with cuts on `zeta J`.  The exterior formulas below use Cauchy analyticity and
normalization at infinity.  Crucially, their derivation does **not** use
(1.2) or `mathcal B_a f=0`.  No inverse of `mathcal B_a` is assumed.

With transported side conventions, the ray jump is

\[
 F_{\zeta,+}(\zeta Y)-F_{\zeta,-}(\zeta Y)
 =\zeta^{-1}f(Y).                                    \tag{1.6}
\]

The right Cauchy readout is `sum_zeta F_zeta(X)`.  After reindexing the four
roots, the left Cauchy readout has weights `sum_zeta zeta^2 F_zeta(X)`.  This
distinction is retained in (2.1)--(2.2).

## 2. Exact two-boundary exterior readout for arbitrary smooth-core data

For `X>beta`, direct continuation of every source term gives

\[
\boxed{
 \mathcal E_Rf(X)=XM_{-1}+X^{-1}M_1
 -\sum_{m:\,X/r_m\in J}w_mf(X/r_m)
 +\pi i\sum_{\zeta^4=1}\zeta^{-1}C_f(\zeta^{-1}X).} \tag{2.1}
\]

For `0<X<alpha`, the reflected calculation gives

\[
\boxed{
 \mathcal E_Lf(X)=XM_{-1}+X^{-1}M_1
 -\sum_{m:\,r_mX\in J}w_mf(r_mX)
 -\pi i\sum_{\zeta^4=1}\zeta^{-1}C_f(\zeta X).}     \tag{2.2}
\]

The opposite signs in the two Cauchy sums are forced by their orientations.
For a right collar point `x=a+rho`, where `rho>0`, the prime `m` contributes

\[
 -w_m n(a+\rho-\log m),                              \tag{2.3}
\]

and at `x=-a-rho` it contributes

\[
 -w_m n(-a-\rho+\log m).                             \tag{2.4}
\]

The shifted sample is eligible under the ambient zero-extension mask exactly
when

\[
 \rho<\log m<2a+\rho,
 \quad\text{equivalently}\quad
 \max(0,\log m-2a)<\rho<\log m.                     \tag{2.5}
\]

Actual nonzero activity additionally requires the displayed point to lie in
`supp(n)` and not at an internal zero.  The index `m` ranges over prime powers
through `Lambda(m)`.  Thus prime powers absent from the old compression can
become eligible at these structural mask thresholds.  On the stated
`C_c^infty` core the
zero-extended translates are flat at the thresholds and the locally finite
sum crosses them smoothly; no such pointwise smoothness is asserted on the
genuine `L^2`/form domain.  The KNC charge for fixed `a<b` uses only the restrictions
`beta<X<e^(b/2)` and `e^(-b/2)<X<alpha`; requiring vanishing on both complete
half-rays would be a stronger all-collar statement.

## 3. The genuine cancellation

Let

\[
 \mu_k=\int_\alpha^\beta Y^k f(Y)\,dY,
 \qquad M_s=2\mu_{s-1}.                              \tag{3.1}
\]

For `X>beta`, expand the Cauchy kernel and use

\[
 \sum_{\zeta^4=1}\zeta^k=
 \begin{cases}4,&4\mid k,\\0,&4\nmid k.\end{cases} \tag{3.2}
\]

Then

\[
 \pi i\sum_{\zeta^4=1}\zeta^{-1}C_f(\zeta^{-1}X)
 =-2\sum_{j\ge0}\mu_{4j}X^{-(4j+1)}.                \tag{3.3}
\]

The `j=0` term is `-X^{-1}M_1`, so it cancels that pole
channel in (2.1) exactly.  In additive coordinates,

\[
\boxed{
 \mathcal E_Rf(e^{x/2})=
 e^{x/2}M_{-1}
 -\sum_{j\ge1}e^{-(4j+1)x/2}M_{4j+1}
 -\sum_mw_m n(x-\log m),\quad x>a.}                 \tag{3.4}
\]

The reflected expansion similarly cancels `XM_-1` on the left:

\[
\boxed{
 \mathcal E_Lf(e^{x/2})=
 e^{-x/2}M_1
 -\sum_{j\ge1}e^{(4j+1)x/2}M_{-(4j+1)}
 -\sum_mw_m n(x+\log m),\quad x<-a.}                \tag{3.5}
\]

Equations (3.4)--(3.5) are the strongest positive result of the calculation.
Completion removes one mode per side, not the full exterior field.

## 4. What this does and does not say about compatibility

Equations (2.1)--(3.5) hold for arbitrary smooth localized `f`.  No step has
used `mathcal B_a f=0`.  Consequently, the visible nonzero summands do not
prove that the readout is nonzero on `ker mathcal B_a`: a coefficient-specific
identity on that kernel could still cancel them.  The calculation exposes the
remaining map but does not evaluate its restriction to the old kernel.

Likewise, the projection cocycle below is only the leakage of an individual
dilation channel.  KNC concerns the **total** completed readout, including the
pole, Lerch/moment, local, and prime-power channels.  An individual leakage
may be nonzero and still cancel against the other channels.

### 4.1 Why the proposed scalar root--dilation mixing disappears

Let

\[
 (R_\zeta F)(z)=F(\zeta^{-1}z),\qquad
 (D_\lambda F)(z)=F(z/\lambda),\quad\lambda>0.
\]

Complex scalar multiplication is commutative, so

\[
 R_\zeta D_\lambda=D_\lambda R_\zeta.               \tag{4.1}
\]

Positive dilations also preserve individual rays.  The arithmetic source is
on the positive ray and its positive dilates; it does not mix the other three
archimedean rays into a four-channel prime determinant.  Local triangular
Cauchy jumps still have determinant one, but that says nothing about the
global homogeneous readout.

Multiplicative reflection `Jf(X)=f(1/X)` obeys

\[
 JS_r=S_{1/r}J.                                      \tag{4.2}
\]

Thus the directed dilation/reflection algebra is semidirect, but reflection
only swaps the two channels of the paired prime atom `S_r+S_(1/r)` and hence
commutes with that pair.  It creates no four-ray cancellation.  Additional
leakage appears after fixed-window compression.  Let `P=P_J`, `Q=I-P`,
`S_r f(X)=f(X/r)`, and

\[
 K_r=PS_rP,\qquad \Omega_r=QS_rP.
\]

Then

\[
 S_rP=K_r+\Omega_r,
 \qquad
 \boxed{\Omega_{rs}=\Omega_rK_s+QS_r\Omega_s}.       \tag{4.3}
\]

Same-direction dilations have no re-entry and satisfy `K_rK_s=K_rs` in the
corresponding monotone range.  Opposite directions obey

\[
 K_rK_{1/s}=K_{r/s}-PS_rQS_{1/s}P.                  \tag{4.4}
\]

The last term is the exact two-boundary re-entry defect.  Equivalently,

\[
 [D_rD_s,P]=D_r[D_s,P]+[D_r,P]D_s,                  \tag{4.5}
\]

and pointwise

\[
 [P_J,D_\lambda]f(X)=
 \{1_J(X)-1_J(X/\lambda)\}f(X/\lambda).             \tag{4.6}
\]

At Cauchy-transform level, for `r>1` and off the displayed cuts,

\[
 C_{PS_rPf}(z)=C_f(z/r)-\frac1{2\pi i}
 \int_{\beta/r}^{\beta}\frac{f(U)}{U-z/r}\,dU,      \tag{4.7}
\]

and

\[
 C_{PS_{1/r}Pf}(z)=C_f(rz)-\frac1{2\pi i}
 \int_\alpha^{r\alpha}\frac{f(U)}{U-rz}\,dU.          \tag{4.8}
\]

Ordinary integral equality holds where the terms avoid their cuts; boundary
values are understood through the same Plemelj convention as (1.1).  The
subtracted endpoint transforms are not a nuisance term: they are the collar
information we need to control.  A closed-loop cocycle identity only balances
leakages; it does not show that an individual leakage or the total completed
readout vanishes.

### 4.2 Reflection gives a real but insufficient compatibility

For `f^vee(Y)=f(1/Y)` and `alpha beta=1`, direct substitution gives the affine
law

\[
 C_{f^\vee}(z)=A_f-C_f(z^{-1}),\qquad
 A_f=\frac1{2\pi i}\int_J\frac{f(U)}U\,dU.          \tag{4.9}
\]

The constant `A_f` cancels in the fourth-root readout only because
`sum_(zeta^4=1) zeta^(-1)=0`.  Hence

\[
 \mathcal E_L[f](X)=\mathcal E_R[f^\vee](X^{-1}).   \tag{4.10}
\]

For a reflection-even or reflection-odd contact state, the two exterior
conditions are therefore related by a sign.  This halves the independent
boundary data; it does not make either side vanish.

### 4.3 Smooth-core homogeneity forces boundary jets, not a collar theorem

If, exceptionally, a smooth compactly supported `n` is an exact homogeneous
old state, then `W*n` is smooth and vanishes on `(-a,a)`.  Its one-sided
exterior formulas must consequently be flat at both endpoints.  With
`lambda_j=4j+1`, for every integer `q>=0`,

\[
0=2^{-q}e^{a/2}M_{-1}
-\sum_{j\ge1}(-\lambda_j/2)^q e^{-\lambda_j a/2}M_{\lambda_j}
-\sum_{m\ge2}\frac{\Lambda(m)}{\sqrt m}
 n^{(q)}(a-\log m),                                \tag{4.11}
\]

\[
0=(-1/2)^q e^{a/2}M_1
-\sum_{j\ge1}(\lambda_j/2)^q e^{-\lambda_j a/2}M_{-\lambda_j}
-\sum_{m\ge2}\frac{\Lambda(m)}{\sqrt m}
 n^{(q)}(-a+\log m).                               \tag{4.12}
\]

These are genuine compatibility conditions coupling the surviving pole,
higher moments, and prime-power jets.  They neither force `M_1=M_-1=0` nor
propagate flatness through a collar: a smooth function can be flat at an
endpoint and become nonzero later.  For genuine form-domain contact states,
even (4.11)--(4.12) require a separate trace/core adapter.

## 5. Möbius transmutation returns the old obstruction

Define

\[
 U_nf(X)=n^{-1/2}f(X/\sqrt n),\qquad U_mU_n=U_{mn}.   \tag{5.1}
\]

For an arithmetic sequence `a`, write

\[
 \mathcal D_a=\sum_{n\ge1}a(n)U_n,                   \tag{5.2}
\]

on a core where the sum is locally finite.  Thus `mathcal D_1` is the
all-ones dilation bank, not the single atom `U_1`.

Composition of locally finite arithmetic dilation sums is Dirichlet
convolution.  The relevant identities are

\[
 \mu*1=\varepsilon,qquad
 \mu*\Lambda=C=-\mu(n)\log n,qquad C*1=\Lambda.     \tag{5.3}
\]

Thus Möbius filtering of the von Mangoldt source gives the previously known
R71 coefficient source `C`; it does not annihilate the prime term.  Direct
Dirichlet inversion of `Lambda` is impossible because `Lambda(1)=0`.

Compression exposes the discarded data.  If `mathcal D_mu mathcal D_1=I` on
a locally finite compact core, then

\[
 Q\mathcal D_\mu P\mathcal D_1P
 =-Q\mathcal D_\mu Q\mathcal D_1P.                  \tag{5.4}
\]

The would-be inverse is exactly the negative omitted exterior tail.
Furthermore, the completed archimedean source has noncompact pole tails.
Near zero its leading term is `M_1/X`; applying the Möbius dilation bank gives
terms proportional to `mu(n)M_1/X`, which do not even tend to zero unless the
moment is removed.  After moment subtraction, bounded Mellin-line synthesis
would require control of a reciprocal-zeta multiplier at critical zeros.
That imports the missing zero-free/KNC strength instead of proving it.

## 6. The finite contact test: what propagation would require

The minimal symmetric Toeplitz old block and two exterior rows are

\[
 B=\begin{pmatrix}1&a&c\\a&1&a\\c&a&1\end{pmatrix},
 \qquad
 E=\begin{pmatrix}a&c&d\\d&c&a\end{pmatrix}.        \tag{6.1}
\]

Its determinant factors as

\[
 \det B=(c-1)(2a^2-c-1).                             \tag{6.2}
\]

On the even contact component `c=2a^2-1`, the vector `(1,-2a,1)` is old-null
and

\[
 E(1,-2a,1)^T=(d+a-2ac)(1,1)^T.                    \tag{6.3}
\]

KNC therefore requires the new next-lag law

\[
 d=2ac-a=4a^3-3a=T_3(a).                            \tag{6.4}
\]

Only after (6.4) is supplied does the inverse-free stencil

\[
 T_{\rm even}=\begin{pmatrix}2a&-1&0\\0&-1&2a\end{pmatrix}
\]

satisfy `E=T_even B`.  The odd contact `c=1` similarly requires the new law
`d=a`.  In a full Toeplitz chain, the corresponding propagation law is

\[
 b_{j+1}-2b_1b_j+b_{j-1}=0,
 \qquad b_j=T_j(b_1).                                \tag{6.5}
\]

This identifies the missing kind of mathematics: old contact data must force
a next-lag recurrence.  It is not furnished by Cauchy covariance itself.
Indeed, the scalar four-Cauchy sequence

\[
 k_j=\frac{2^{3j}}{2^{4j}-1}
 =\sum_{m\ge0}(2^{-(4m+1)})^j                       \tag{6.6}
\]

for `j>=1`.  Put `rho_m=2^(-(4m+1))`.  For every order `N`, the Hankel block is

\[
 [k_{i+j+1}]_{0\le i,j<N}
 =\sum_{m\ge0}\rho_m(1,\rho_m,\ldots,\rho_m^{N-1})^T
                 (1,\rho_m,\ldots,\rho_m^{N-1}).     \tag{6.7}
\]

For a nonzero polynomial `p` of degree below `N`, its quadratic form is
`sum_m rho_m p(rho_m)^2>0`, because `p` cannot vanish at all infinitely many
distinct `rho_m`.  Hence every finite Hankel block is positive definite.  The
sequence has infinite Hankel rank and no eventual nonzero finite
constant-coefficient recurrence.

An exact rational Toeplitz-algebra contact gives a complementary falsifier.  A
synthetic completion can be chosen so that `a=1/2`, `c=-1/2`, the old block is
positive semidefinite with nullvector `(1,-1,1)`, while

\[
 E(1,-1,1)^T=-\frac{229319}{32760}(1,1)^T\ne0.       \tag{6.8}
\]

This proves that positive-semidefinite Toeplitz old-contact algebra, even with
the displayed continuous source baselines, does not by itself force exterior
null charge.  Its completion weights are freely chosen and synthetic, so the
model does not instantiate every relation of the full source grammar.  It is
not an actual-zeta counterexample and does not refute KNC or RH.

## 7. Decision-space consequence

The exact remainder map is now explicit:

\[
 f\longmapsto (\mathcal E_Lf,\mathcal E_Rf),
\]

with (3.4)--(3.5), restricted to a chosen finite collar.  To turn it into a
factor one must still prove

\[
 \mathcal E_{L,a,b}f=\mathcal E_{R,a,b}f=0
 \quad\text{whenever}\quad \mathcal B_af=0.          \tag{7.1}
\]

For smooth-core homogeneous states, (7.1) is the corresponding KNC condition.
For genuine form-domain states it can be identified with operator KNC only
after proving the missing state/trace adapter.  More basically, the full
global compatibility system has not yet been calculated because (1.4a) was
not assembled with (2.1)--(2.2) into one split old/exterior state equation.
The exterior calculation has exposed the target; it has not computed its
restriction to the old kernel or lowered its logical strength.

The corrected direct lane therefore has three explicit tasks:

1. serialize the split Volterra/Carleman four-root old operator (1.4a), with
   its finite-part counterterm, rather than replacing it by one Plemelj jump;
2. construct the form-domain-contact to Cauchy-state/trace adapter; and
3. only then test or prove that the total exterior readout vanishes on the
   resulting kernel, using reflection and the boundary-jet constraints above.

The preflight also preregistered an arcsine finite-Hilbert falsifier and an
exact finite-node Cauchy-dilation homogeneous-state search.  Those two tests
were not executed in the original R185 run.  The elementary determinant-one
shortcut is nevertheless already falsified abstractly: arbitrary nonzero
unipotent triangular jumps have determinant one.  The two preregistered tests
remain open evidence tasks, not completed checks.

The immediate uniform-strip route remains the complete
source-preserving fixed-window R71 fixed-power estimate, with the compact
source derivative as its scalar falsifier.  The direct lane is not broadly
closed: its split-Carleman serialization and domain adapter are open.  Only
the scalar root--positive-dilation noncommutativity mechanism is parked;
repeating those commuting words or Möbius compression cannot supply KNC.

## 8. Literature and novelty firewall

The completed screw kernel and localized operator are imported from Suzuki.
Suzuki's current finite-interval operator framework is
[`arXiv:2606.09096v2`](https://arxiv.org/abs/2606.09096v2); his earlier screw
function and moment criteria are in
[`doi:10.1112/jlms.12785`](https://doi.org/10.1112/jlms.12785).  The
recursively generated/flat moment-extension analogy is classical
Curto--Fialkow theory; see
[`doi:10.1090/memo/0648`](https://doi.org/10.1090/memo/0648).

The root filter, boundary-cocycle packaging, boundary-jet extraction,
Toeplitz diagnostic, and route synthesis are classified as
**PROJECT_SYNTHESIS**.  The Cauchy, Toeplitz,
Dirichlet-convolution, finite-rank Hankel, and flat-extension ingredients are
classical or imported.  Nothing here is labeled `CANDIDATE_NEW`.

The dated search record is
[`zeta23_four_cauchy_global_compatibility_literature_search_2026-09-03.json`](context/zeta23_four_cauchy_global_compatibility_literature_search_2026-09-03.json).
Failure to locate an identical packaging is not evidence that it is absent
from private, unpublished, unindexed, or differently phrased work.

## 9. Formal and executable scope

[`FourCauchyGlobalCompatibility.lean`](../lean/rhbridge/RHBridge/FourCauchyGlobalCompatibility.lean)
kernel-checks scalar-pullback commutativity, projection leakage, the product
commutator cocycle, the compressed-inverse omitted-tail identity, the leading
mode cancellations after their coefficients are supplied, the three-lag
Toeplitz contact identities, the Chebyshev step, and the rational charged
contact algebra.  It does not formalize Suzuki's analytic operator, the split
finite-part old equation, Plemelj boundary values, reflection's affine Cauchy
law, boundary jets, infinite moment expansions, von Mangoldt sums, the
form-domain adapter, KNC, `T^src`, a zero-free strip, the four-cycle bound, or
RH.

[`four_cauchy_global_compatibility.py`](../src/four_cauchy_global_compatibility.py)
replays the fourth-root filter, both moment cancellations, exact matrix
cocycles, contact residuals, rational countermodel, and finite Hankel
witnesses over rational or Gaussian-rational arithmetic.  These are formula
and scope tests, not a discretization of the actual zeta operator or a test of
the exterior readout on its kernel.
