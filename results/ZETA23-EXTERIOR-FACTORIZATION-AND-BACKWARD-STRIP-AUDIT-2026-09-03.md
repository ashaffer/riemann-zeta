# ZETA23 exterior factorization and backward-strip audit

Date: 2026-09-03  
Status: exact proof-class classification and conditional backward calibration;
no uniform zero-free strip and no proof of RH

Preflight:
[`zeta23_exterior_factorization_backward_strip_preflight_v1.json`](context/zeta23_exterior_factorization_backward_strip_preflight_v1.json)

## 0. Verdict

The proposed stronger experiment is complete at the proof-class level.  It
does not produce the completed-zeta factorization, a uniform zero-free strip,
or RH.  It does decisively change the decision tree.

1. The factorization must use the **old-to-collar charge**, not the cross
   block denoted by `C` in the earlier block-matrix convention.  With the
   corrected typing, write this map as `Gamma_(a,b)`.
2. At a Fredholm contact, the bare assertion

   \[
     \Gamma_{a,b}=T_{a,b}A_a
   \]

   for some bounded `T_(a,b)` is equivalent to kernel-null charge (`KNC`).
   It is not an easier lemma.  Constructing `T=Gamma A^dagger` merely assumes
   the exact kernel annihilation one is trying to prove.
3. Equality only on a dense core is meaningful if the proposed factor is at
   least closable.  There is an exact infinite-dimensional example in which
   a nonclosable factor gives the identity on a dense core while the actual
   nullvector is charged.
4. Positivity of the enlarged block supplies square-root-scale Schur
   alignment.  A factorization uniformly controlled through a closing old
   eigenvalue requires the strictly stronger linear-scale alignment.  The
   positive scalar family

   \[
     \begin{pmatrix}r^2&r\\r&1\end{pmatrix}
   \]

   has factor norm exactly `1/r`.
5. Assuming a fixed uniform strip gives the complete fixed-window R71/R68
   bound with the calibrated exponent and gives eventual positivity of the
   corresponding shifted Suzuki function.  It does not, through any
   currently licensed implication, give unshifted localized Weil positivity
   or exterior factorization.  A proof that it did would be a new
   strip-to-RH amplifier.

Accordingly, the existential, pseudoinverse, invertible-window,
shifted-resolvent, graph-norm, enlarged-positivity, and unqualified
dense-core branches are retired.  One narrow direct-RH gamble survives:
write down a specific inverse-free completed pole--archimedean--prime
operator `T^src_(a,b)` and prove its identity and closability independently.
No such operator has been found or even fully specified.

For the immediate uniform-strip objective, effort returns to the two
strength-matched coordinates already known:

- a complete fixed-window R71 power saving; or
- eventual one-sided control of a fixed positive shift `Psi_omega` (or an
  exactly equivalent pole-killed arithmetic ramp).

## 1. Correct operator passport

Fix one outer support slab `V_B` with reference form inner product `h`.  Let

\[
 q_B(f,g)=h((I+G)f,g),\qquad G=J^*R_BJ,
\]

where `G` is bounded and self-adjoint on the outer form space.  For
`V_a subset V_b`, put

\[
 W_{a,b}=V_b\cap V_a^{\perp_h}.
\]

The bounded old Euler operator and old-to-collar charge are

\[
 A_a=I+P_a^hG|_{V_a}:V_a\longrightarrow V_a,
 \qquad
 \Gamma_{a,b}=P_{W_{a,b}}^hG|_{V_a}:V_a\longrightarrow W_{a,b}.
 \tag{1.1}
\]

They satisfy

\[
 h(A_af,u)=q_B(f,u),\qquad
 h(\Gamma_{a,b}f,w)=q_B(f,w).                         \tag{1.2}
\]

The enlarged block, in the decomposition `V_a direct-sum_h W_(a,b)`, is

\[
 \begin{pmatrix}A_a&\Gamma_{a,b}^*\\
                 \Gamma_{a,b}&D_{a,b}\end{pmatrix}.   \tag{1.3}
\]

This corrects a notation trap.  In the screw-collar report the letter `C`
denoted `P_aG|_W`, which maps collar to old space.  The factorization in the
post-synthesis decision path can typecheck only for its adjoint
`Gamma=P_WG|_(V_a)`.

If `A_a>=0`, its kernel is the radical of the old form.  Hence

\[
 \operatorname{KNC}(a,b)
 \quad\Longleftrightarrow\quad
 \Gamma_{a,b}(\ker A_a)=\{0\}.                       \tag{1.4}
\]

The bounded form-operator convention is essential for the cheap test.  If
`A_a` instead means the unbounded Friedrichs operator on the `L2` pivot,
form-core density does not automatically give an operator-core identity;
one must additionally state a graph core, the domain of `T`, and the relevant
closedness/continuity bridge.

## 2. Complete factorization classification

Let `X,Y` be Hilbert spaces, let `A:X->X` be bounded, self-adjoint and
nonnegative, and let `Gamma:X->Y` be bounded.

### Theorem 2.1 -- algebraic and bounded division

The rule

\[
 T_0(Ax)=\Gamma x\qquad (x\in X)                      \tag{2.1}
\]

is well defined on `ran(A)` if and only if

\[
 \ker A\subseteq\ker\Gamma.                           \tag{2.2}
\]

A bounded all-space factor

\[
 \Gamma=TA                                               \tag{2.3}
\]

exists if and only if, for some finite `M`,

\[
 \|\Gamma x\|\le M\|Ax\|\quad(x\in X).                \tag{2.4}
\]

Equivalently,

\[
 \Gamma^*\Gamma\preceq M^2A^2,
 \qquad
 \operatorname{ran}\Gamma^*\subseteq\operatorname{ran}A.
 \tag{2.5}
\]

The last equivalence is the Douglas range-factorization theorem.  The
optimal factor norm is the least admissible `M` in (2.4).

If `ran(A)` is closed, (2.2) already implies (2.4).  Indeed, on
`(ker A)^perp`, the restriction of `A` has a bounded inverse onto `ran(A)`;
define `T` there by (2.1) and set it to zero on `ran(A)^perp`.

#### Proof of the algebraic part

If `Ax=Ax'`, then `x-x'` lies in `ker(A)`.  Thus (2.1) is well defined
exactly when `Gamma(x-x')=0` for every such pair, which is (2.2).  Conversely,
any (even algebraic) all-space factor immediately gives

\[
 An=0\Longrightarrow\Gamma n=T(An)=0.
\]

The norm and range statements are the standard Douglas theorem applied to
`Gamma^*` and `A=A^*`.

### Corollary 2.2 -- collapse at a localized zeta contact

In the fixed outer form space, `A_a=I+compact` is Fredholm, so its range is
closed.  Consequently, at every semidefinite contact,

\[
 \boxed{
 \operatorname{KNC}(a,b)
 \quad\Longleftrightarrow\quad
 \exists T\in\mathcal B(V_a,W_{a,b})\;
       \Gamma_{a,b}=TA_a.}
 \tag{2.6}
\]

Thus `there exists T` is a reformulation of the open condition, not a
reduction of it.  The pseudoinverse formula

\[
 T=\Gamma_{a,b}A_a^\dagger                         \tag{2.7}
\]

is valid only after KNC makes (2.1) well defined on the nullspace quotient.
It is an existence proof conditional on the desired conclusion, not the
missing arithmetic mechanism.

Together with the accepted support-continuation and Weil interfaces,
universal (2.6) at semidefinite contacts is RH-equivalent.  This is a
semantic statement about existence.  An explicitly prescribed finite-source
formula for `T` would be a proof certificate with additional syntactic
content, but it would prove the same KNC conclusion.

## 3. What a dense-core identity must mean

Let `D` be dense in `X`, suppose `A` and `Gamma` are bounded, and let `T` be
an operator whose domain contains `A(D)`.  Assume

\[
 \Gamma x=T(Ax)\qquad(x\in D).                         \tag{3.1}
\]

If `T` is bounded, (3.1) extends to all of `X`.  More generally, if `T` is
closable, (3.1) already forces kernel annihilation.  For `n in ker(A)`, take
`x_j in D` with `x_j->n`.  Then

\[
 Ax_j\to0,\qquad T(Ax_j)=\Gamma x_j\to\Gamma n.
\]

Closability forces `Gamma n=0`.

Without closability, dense-core equality has no KNC content.  Here is an
exact counterexample.  Put

\[
 X=\mathbb C\oplus\ell^2,\quad
 A(\alpha,z)=(0,z),\quad
 \Gamma(\alpha,z)=\alpha,
\]

and define the dense linear space

\[
 D=\{(\textstyle\sum_nz_n,z):z\in c_{00}\}.
\]

Density follows because a vector orthogonal to every
`(sum z_n,z)` would have an `ell^2` component equal to one nonzero constant
in every coordinate.  On `A(D)`, define

\[
 T(0,z)=\sum_n z_n.
\]

Then (3.1) holds on `D`, but `A(1,0)=0` and `Gamma(1,0)=1`.  With `z^(N)`
equal to `1/N` in its first `N` coordinates,

\[
 \|z^{(N)}\|_2^2=1/N\to0,
 \qquad T(0,z^{(N)})=1,
\]

so `T` is not closable.  This prunes every proposal that uses the phrase
“on a dense core” without an independently proved boundedness or closability
statement.

## 4. Four exact fast falsifiers

### 4.1 The old operator does not determine the charge

Take

\[
 A=\operatorname{diag}(1,0),\qquad D=1.
\]

Both `Gamma_good(x_1,x_2)=x_1` and
`Gamma_bad(x_1,x_2)=x_2` share these diagonal blocks.  The first factors
through `A`; the second charges `(0,1) in ker(A)` and cannot factor.  The bad
full block is necessarily indefinite: on the null/collar direction `(1,-1)`
its two-dimensional quadratic part is `-1`.

This does not refute the completed-zeta identity.  It proves that old-block
spectral data, compactness, Fredholmness, and positive diagonal blocks do not
determine it.

### 4.2 Schur positivity is only square-root alignment

For every real `r`,

\[
 r^2x^2+2rxy+y^2=(rx+y)^2\ge0.                       \tag{4.1}
\]

Thus

\[
 S_r=\begin{pmatrix}r^2&r\\r&1\end{pmatrix}\succeq0.
\]

For `r>0`, the scalar identity `r=t r^2` forces

\[
 t=1/r.                                                \tag{4.2}
\]

In the eigenvalue notation `lambda=r^2`, block positivity permits charge
`sqrt(lambda)`, while a uniformly bounded `Gamma=TA` requires charge
`O(lambda)`.  Hence enlarged positivity cannot supply a uniform first-order
factorization.  At a contact it supplies exact null annihilation, but
assuming positivity in the enlarged support is precisely the right-openness
step and is circular in the forward proof.

The blow-up test is a useful diagnostic for an explicit formula, not an
additional necessary condition for pointwise KNC: the limiting block at
`r=0` has zero charge even though the positive-support factors in (4.2)
diverge.

### 4.3 A shifted resolvent is a disguised null-charge pole

At an isolated zero eigenvalue, for small nonzero `sigma`,

\[
 (A-\sigma I)^{-1}
 =-\sigma^{-1}P_{\ker A}
  +(A|_{(\ker A)^\perp}-\sigma I)^{-1}(I-P_{\ker A}). \tag{4.3}
\]

Therefore the tautological shifted factor

\[
 T_\sigma=\Gamma(A-\sigma I)^{-1}                    \tag{4.4}
\]

has

\[
 T_\sigma
 =-\sigma^{-1}\Gamma P_{\ker A}
  +\Gamma A^\dagger+O(\sigma).                       \tag{4.5}
\]

It remains bounded as `sigma->0` if and only if KNC already holds.  In the
scalar charged mode the identity is simply

\[
 (-1/\sigma)(-\sigma x)=x.
\]

Thus a negative shift can always manufacture a factor away from contact and
has no KNC content unless its zero-shift regularity is proved independently.

### 4.4 Positivity without closed range does not repair the claim

On `ell^2`, let

\[
 Ae_n=4^{-n}e_n,\qquad
 \Gamma x=\sum_{n\ge1}4^{-n}x_n,\qquad
 D=\sum_{n\ge1}4^{-n}=1/3.
\]

The full quadratic form is

\[
 \sum_{n\ge1}4^{-n}|x_n+t|^2\ge0.                    \tag{4.6}
\]

Nevertheless the quotient factor on `ran(A)` is

\[
 T_0z=\sum_nz_n.
\]

The finite-support vectors with `N` entries equal to `1/N` converge to zero
in `ell^2` while their `T_0` values stay equal to one.  Hence `T_0` is not
closable.  Equivalently, `Gamma^*1=(4^{-n})` is not in `ran(A)`, since its
only formal preimage is the non-square-summable constant sequence.

This example is deliberately outside the Fredholm zeta contact.  Its role is
to prevent an invalid appeal to full block positivity or to closure of
operator ranges in a more general architecture.

## 5. The completed-source problem that actually remains

The project already has the exact completed exterior potential.  On an old
nullvector `n`, its collar increment is a finite active-prime-power sum plus
the pole and gamma/Lerch terms.  KNC is exactly the assertion that this
increment vanishes almost everywhere on the collar.  The formula exposes
the charge; it does not express it in terms of `A_an`.

Consequently the first-open edge is not “compute the collar source.”  It is
the following division statement.

### Surviving direct-RH target

Specify an operator

\[
 T^{\rm src}_{a,b}:V_a\longrightarrow W_{a,b}          \tag{5.1}
\]

by a declared finite grammar of completed pole, archimedean, and active
prime-power operations, independently of `A_a^{-1}`, `A_a^dagger`, a later
positive support, kernel triviality, or RH.  Then prove

\[
 \Gamma_{a,b}\phi=T^{\rm src}_{a,b}(A_a\phi)           \tag{5.2}
\]

on the smooth localized core and prove `T^src` bounded or closable in the
fixed form-space topology.

No concrete `T^src` meeting these requirements is currently on the table.
Without its formula and allowed-operation grammar, (5.2) is not a
falsifiable conjecture beyond the already open KNC statement.  A failed
candidate refutes only that candidate or its precisely declared grammar; it
cannot refute KNC or RH.

Literal endpoint jets, generic convolution smoothness, compactness,
Fredholm/pseudoinverse division, and mean-periodicity have already failed in
the prior screw-collar audit.  They are not alternative constructions of
`T^src`.

## 6. Backward audit: assume a fixed strip

Fix `0<eta<=1/2` and assume

\[
 S_\eta:\qquad
 \eta\le\Re\rho\le1-\eta
 \quad\text{for every nontrivial zero }\rho.            \tag{6.1}
\]

Put `d=1/2-eta`.

### 6.1 Strongest licensed quantitative consequence

The completed fixed-window field obeys

\[
 |\mathcal D^{\rm full}(R)|
 \le \exp\{(d+o(1))R\},                                \tag{6.2}
\]

and every licensed regular fixed-window R71/R68 block obeys

\[
 E_I^{\rm app},\ X_I
 \le\exp\{(1-2\eta+o(1))R\}.                           \tag{6.3}
\]

This is the proved conditional direction of the fixed-window exponent
calibration.  Together with the accepted moving-edge converse in the
correct fixed-window scope, it is exponent-equivalent to the strip.  A
single changing growing-order schedule still requires its own varying-test
converse.

### 6.2 Faithful scalar consequence

Set

\[
 \alpha=1-\eta,\qquad \omega=\alpha-1/2=1/2-\eta.
\]

Suzuki's shifted criterion gives

\[
 \xi(s)\ne0\quad(\Re s>\alpha)
 \quad\Longleftrightarrow\quad
 \Psi_\omega(t)\ge0\quad\text{for all sufficiently large }t.
 \tag{6.4}
\]

Thus the assumed strip implies (6.4), and symmetry gives the corresponding
left boundary.  This is another exact coordinate on the strip target, not a
weaker consequence.

### 6.3 What the strip does not automatically provide

Under the accepted localized-Weil interfaces there is a sharp conditional
dichotomy.

- If RH holds, the global Weil form is positive and Suzuki's localized
  nondegeneracy removes every finite-support kernel.  Each fixed `A_a` is
  strictly positive, so pointwise inverse factorizations exist; their norms
  need not be uniform in `a`.
- If `S_eta` holds but RH is false, continuity of the localized ground value
  produces a finite terminal support `a_*` with `A_(a_*)>=0` and nonzero
  kernel.  The KNC quantifier-collapse theorem supplies one nullvector
  charged in every larger collar.  Hence

  \[
    \Gamma_{a_*,b}\ne T A_{a_*}\qquad(b>a_*)           \tag{6.5}
  \]

  for every genuine factor `T`.

This does not prove that `S_eta and not RH` occurs.  It proves the correct
logical calibration: a theorem deriving universal exterior factorization
from `S_eta` would eliminate that branch and therefore be a new
strip-to-RH amplifier.  The factorization is not an intermediate lemma that
the strip presently supplies.

A second tempting backward route also fails at the soft level.  The strip
gives the classical prime error exponent, but direct partial summation in the
localized Weil form introduces an `H^(1/2)` Fourier weight, whereas the
archimedean term controls only a logarithmic weight.  The project has an
exact synthetic divisor showing that strip width, zeta-like counting,
symmetry, and qualitative fixed-support semiboundedness alone do not yield
the desired quantitative localized spectral floor.  This does not refute a
zeta-specific signed prime--archimedean argument; it identifies the missing
input as signed sampling, not strip geometry.

## 7. Literature cross-check and novelty classification

The operator equivalence (2.5) is imported mathematics: it is Douglas's
1966 range-factorization theorem.  The finite models and their application
to this decision path are project audit fixtures, not claimed as new
functional analysis.

The current version of Suzuki's 2026 paper contains a directly relevant but
distinct global factorization.  Under RH it obtains

\[
 A_\infty=U^*U
 =\pi^{-1}D^*\widehat{\mathcal P}^*
   \widehat{\mathcal P}D.                              \tag{7.1}
\]

Suzuki then states that an unconditional identification of the corresponding
kernel with the completed screw kernel would imply `A_infinity>0` and hence
RH immediately.  This is strong external confirmation of the calibration:
the closest source-factorization analogue is itself presented as an RH
route.  It is not the old-to-collar identity (5.2), and it supplies no fixed
strip.

Suzuki's 2023 paper supplies both the localized nondegeneracy/RH interface
and the shifted eventual-positivity criterion (6.4).  The current 2026
revision proves continuity of the localized lowest eigenvalue and notes that
failure of RH forces a finite degenerate support.  None of the checked
sources states the particular exterior division (5.2).

Classification:

| Item | Classification |
|---|---|
| Douglas factorization/range equivalence | `IMPORTED` |
| Suzuki localized, shifted, and global factorization interfaces | `IMPORTED` |
| screw-collar exterior potential and prior countermodel | `LOCAL_PREDECESSOR` |
| corrected typing, proof-class collapse, and two-sided route decision | `PROJECT_SYNTHESIS` |
| finite exact hostile fixtures | `PROJECT_SYNTHESIS` |
| a completed-source `T^src` | `OPEN`; no theorem or candidate formula |

No item in this report is labeled `CANDIDATE_NEW`.  Failure to find (5.2) in
the checked sources is not evidence that no unpublished or differently
formulated result exists.

## 8. Correctly pruned and surviving branches

### Retire

1. `T=Gamma A^{-1}` at strictly positive supports: tautological even in a
   false-RH world before its first contact.
2. `T=Gamma A^dagger`: equivalent to assuming KNC on the kernel.
3. `T_sigma=Gamma(A-sigma I)^{-1}`: tautological off contact; its pole
   residue is exactly the null charge.
4. Full enlarged-support positivity or Schur complement: it assumes the
   right-openness conclusion and gives only square-root alignment before
   contact.
5. A graph norm invented so the quotient is bounded: a coordinate
   tautology with no ambient stability.
6. Finite invertible Galerkin factorization: always solvable and informative
   only through a uniform norm/residual theorem that survives contact.
7. Dense-core equality with no boundedness or closability certificate: the
   exact graph-core counterexample defeats it.
8. Generic compactness, smoothness, difference-kernel structure, finite
   endpoint jets, or mean-periodicity: already defeated by the prior
   convolution-kernel and periodic models.
9. Treating unshifted exterior factorization as a consequence of a small
   fixed strip: this silently inserts a strip-to-RH amplifier.

### Keep, but sharply scoped

1. **Primary strip lane:** prove a complete, source-preserving fixed-window
   R71 bound (6.3) for some fixed `eta>0` by genuinely new signed arithmetic.
2. **Equivalent scalar strip lane:** prove eventual positivity of one fixed
   `Psi_omega`, or the exactly bridged one-sided pole-killed ramp bound, by a
   mechanism not equivalent to assuming its forbidden zero modes away.
3. **Bounded direct-RH gamble:** only a fully displayed `T^src` satisfying
   the passport in Section 5.  Stop immediately if no formula and grammar
   can be specified.
4. **Potential backward discriminator:** test every proposed intermediate
   lemma against both hypothetical branches `RH` and `S_eta and not RH`.
   If it fails in the latter, label it an RH amplifier rather than a strip
   lemma.

The information-gain conclusion is therefore negative but decisive.  The
stronger exterior idea does not bridge to the strip.  It collapses to the
direct RH edge, and all easy constructions of its factor are circular or
vacuous.  The immediate strip route is now narrower and cleaner: it must
control the complete zero-sensitive field, or an exactly equivalent shifted
scalar detector, through signed completed arithmetic.

## 9. Replay and proof status

Exact rational fixtures:

- [`exterior_factorization_audit.py`](../src/exterior_factorization_audit.py)
- [`test_exterior_factorization_audit.py`](../src/test_exterior_factorization_audit.py)

Lean finite algebra:

- [`ExteriorFactorizationAudit.lean`](../lean/rhbridge/RHBridge/ExteriorFactorizationAudit.lean)
- [`ExteriorFactorizationAuditAxioms.lean`](../lean/rhbridge/RHBridge/ExteriorFactorizationAuditAxioms.lean)

The Lean file proves only:

- exact factorization implies kernel annihilation;
- the scalar reciprocal factor cost;
- positivity of the square-root block and defeat of every fixed linear
  factor bound; and
- the exact shifted-resolvent scalar identity, reciprocal norm, and defeat of
  every fixed norm bound.

It does not formalize Douglas's Hilbert-space theorem, the completed-zeta
source, Suzuki's analytic results, the R71 calibration, a uniform strip, or
RH.  Those distinctions are part of the theorem passport, not omissions to
be silently filled by the finite formalization.
