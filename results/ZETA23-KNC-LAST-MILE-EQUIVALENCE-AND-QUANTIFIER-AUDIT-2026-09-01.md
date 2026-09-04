# KNC last-mile equivalence and quantifier audit

Date: 2026-09-01

## Verdict

The completed-zeta kernel null-charge assertion (`KNC`) has neither been
proved nor refuted.  The last-mile audit does, however, determine its exact
logical status and closes several proposed shortcuts.

1. At one semidefinite support, persistence along an arbitrarily thin
   sequence, persistence at one larger support, and persistence on a full
   right neighborhood are equivalent.  There is no weaker sequential
   version to target.
2. In the compact-Fredholm filtration already established in the project,
   germ `KNC` is equivalent to right-extendability of positivity at that
   contact.
3. Universally quantified over all semidefinite completed-zeta contacts,
   `KNC` is equivalent to RH, relative to the accepted Weil criterion and
   support-continuity interfaces.  It is a sharper *presentation* of the
   first obstruction, not a theorem of lower logical strength.
4. The finite-dimensional statement needs qualification: the charge
   operator has finite-dimensional domain `ker Q_L`, but infinite-dimensional
   collar codomain.  Verifying it is zero is a finite list of functional
   identities, not a finite list of scalar equalities.
5. Logarithmic unique continuation points in the wrong direction for a
   structure-only proof.  The pure logarithmic Laplacian has exact
   semidefinite Dirichlet contacts which are charged into every larger
   collar.  The actual zeta source would have to cancel that antilocal flux
   exactly.

Thus the decision-tree label should be

```text
completed-zeta universal KNC: OPEN / RH-EQUIVALENT GLOBAL CRITERION
single-contact charge operator: exact finite-rank-domain reformulation
```

It should not be advertised as an independently easier route to RH.

## 1. Setup

Let `(E_a)_{a>0}` be the nested completed-zeta logarithmic form domains,
viewed in one bounded reference-form Hilbert space when only a compact support
slab is under discussion.  Let `Q` denote the consistent polarized Weil form
and suppose

\[
 Q_a:=Q|_{E_a}\geq0.
\]

Its radical is

\[
 N_a=\{n\in E_a:Q(n,u)=0\text{ for every }u\in E_a\}
     =\ker Q_a.                                      \tag{1.1}
\]

The equality follows from the radical identity for a positive semidefinite
Hermitian form.  For `b>a`, write

\[
 K(a,b):\quad Q(n,v)=0
 \quad(n\in N_a,\ v\in E_b).                       \tag{1.2}
\]

This is equivalent to the report's residual/reference-harmonic formulation:
on the `h`-orthogonal new space the reference cross term is zero, so `Q=R`
there.

## 2. Exact quantifier-collapse theorem

### Theorem 2.1

For a fixed semidefinite support `a`, the following are equivalent:

1. `K(a,b)` holds for some `b>a`;
2. there is `epsilon>0` such that `K(a,c)` holds for every
   `a<c<a+epsilon`;
3. for every `epsilon>0`, `K(a,c)` holds for some
   `a<c<a+epsilon`;
4. `K(a,b_j)` holds along some sequence `b_j downarrow a`.

Indeed, if `a<c<=b`, then `E_c subset E_b`, so `K(a,b)` implies `K(a,c)`.
This proves every implication after choosing one member of the sequence (or
one `c` from item 3).

There is a second useful collapse.  Fredholmness makes `N_a`
finite-dimensional.  If every `n in N_a` persists into some possibly
`n`-dependent right germ, choose a finite basis `n_1,...,n_d` and take the
minimum of the corresponding support increments.  Linearity then gives one
common germ for all of `N_a`.

Consequently neither

```text
an arbitrarily thin sequence
```

nor

```text
one nullvector at a time
```

defines a genuinely weaker exact target.  By contrast, convergence of the
charge to zero is strictly weaker and is not enough.

### Proposition 2.2: approximate charge is useless at a null contact

If `Q(n,n)=0` and `Q(n,w)=c != 0`, then for a suitable scalar `t` of
arbitrarily small magnitude,

\[
 Q(n+tw,n+tw)=2\operatorname{Re}(t c)+|t|^2Q(w,w)<0. \tag{2.1}
\]

The matrix

\[
 \begin{pmatrix}0&\varepsilon\\ \varepsilon&1\end{pmatrix}
\]

has lowest eigenvalue
`(1-sqrt(1+4 epsilon^2))/2<0` for every `epsilon != 0`, even though the
charge tends to zero with `epsilon`.  Exact vanishing, not an `o(1)` collar
estimate, is forced by semidefiniteness.

## 3. KNC is exactly right-openness of positivity

### Theorem 3.1

Assume the compact-filtration localization and Fredholm residual hypotheses
proved in the recursive fixed-point report.  At a support `a` with `Q_a>=0`,
the following are equivalent:

1. germ `KNC` holds at `a`;
2. `Q_c>=0` for at least one `c>a`;
3. `Q_c>=0` throughout some nonempty right neighborhood of `a`.

For `2 => 1`, an old nullvector still has zero self-energy in `E_c`.
Positivity of `Q_c` makes it radical in `E_c`, giving `K(a,c)`.  The
quantifier-collapse theorem gives the germ.  For `1 => 3`, the localized
reserve/Fredholm--Ward argument from the fixed-point report applies.  The
implication `3 => 2` is immediate.

Thus `KNC` is not merely sufficient for the continuation argument.  It is
the exact right-openness condition at a semidefinite boundary.

## 4. Completed-zeta equivalence with RH

### Theorem 4.1

Retain the project's certified positive base, nested-support consistency,
compact-resolvent ground state, continuity of the ground value, and accepted
Weil criterion.  Then the following are equivalent:

1. RH;
2. global Weil positivity;
3. germ `KNC` at every finite support for which `Q_a>=0`;
4. there is no finite terminal positive support carrying a charged
   nullstate.

The equivalence `1 <=> 2` is the imported Weil criterion.  Under global
positivity, every old nullvector remains zero-energy in each enlargement and
positivity makes it radical there, so item 3 follows directly.  Suzuki's
localized nondegeneracy theorem gives the stronger statement that under RH
these localized kernels are absent.  Conversely, item 3 and Theorem 3.1 make
the set of positive supports both closed and right-open.  Starting from the
certified base, the maximal-support argument gives positivity at every finite
support and hence RH.

The primary literature makes the logical strength especially explicit.
[Suzuki, Theorem 1.4](https://arxiv.org/html/2206.03682) states that RH is
equivalent to nondegeneracy of every localized screw-kernel operator.
[Suzuki, Theorems 1.3--1.4](https://arxiv.org/html/2606.09096v2) proves
continuity of the localized ground value and positivity for sufficiently
small support; the paper notes that failure of RH therefore produces a
finite degenerate support.

There is also an exact false-world witness statement.  If RH is false, let
`a_*` be the terminal boundary of the nonnegative-support interval.  Then
`Q_{a_*}>=0`, `N_{a_*} != {0}`, and `K(a_*,b)` fails for every `b>a_*`.
Moreover one may choose a *single* `n_* in N_{a_*}` which is charged in
every right collar.

To see the last assertion, put

\[
 Z_b=\{n\in N_{a_*}:Q(n,E_b)=0\}.
\]

The spaces `Z_b` are nested and proper for every `b>a_*`.  Along
`b_j downarrow a_*`, their dimensions eventually stabilize; nested
finite-dimensional spaces of the same dimension coincide.  Choose
`n_*` outside that stable proper space.  For any `b>a_*`, a sufficiently
small `b_j<b` supplies `v_b in E_{b_j} subset E_b` with
`Q(n_*,v_b) != 0`.

This is the exact meaning of “first loss occurs through a charged
nullstate.”  Proving the universal zeta assertion proves RH; producing an
actual zeta counterexample to it refutes RH.

## 5. Why unique continuation does not prove KNC

The reference logarithmic operator has genuine antilocality.  Chen, Hauer,
and Weth prove that if `u` and the logarithmic Laplacian `L_Delta u` both
vanish on a nonempty open set, then `u=0` globally
([Theorem 1.7](https://arxiv.org/html/2312.15689v1)).  This does not imply
KNC.  It yields the following countermodel instead.

### Proposition 5.1: logarithmic Dirichlet contacts are charged

Let `Omega=(-a,a)`, let `E_Omega` be the zero-exterior Dirichlet form domain,
let `lambda_1(Omega)` be the lowest Dirichlet eigenvalue of `L_Delta`, and let
`0 != n` be a corresponding zero-extended eigenfunction.  Define

\[
 q(u,v)=\mathcal E_{L_\Delta}(u,v)
        -\lambda_1(\Omega)\langle u,v\rangle_2.      \tag{5.1}
\]

Then `q|_{E_Omega}>=0` and `n in ker q|_{E_Omega}`.  Nevertheless persistence
into the Dirichlet form domain of every strictly larger interval fails.

If persistence held into the Dirichlet form domain `E_{Omega_b}` for one
`Omega_b=(-b,b)` with `b>a`, the distributional eigen-equation would hold on
`(-b,b)`.  On either exterior collar, `n=0`, so the local mass term vanishes
and `L_Delta n=0` there.  The cited weak unique-continuation theorem would
force `n=0`, a contradiction.

Thus compact support, a logarithmic symbol, an extension PDE, and unique
continuation do not furnish persistence.  They make a nonzero Dirichlet
contact emit a boundary charge.  The same direction is already familiar for
the analytic local model

\[
 -u''-\left({\pi\over2a}\right)^2u
\]

on `(-a,a)`: its first Dirichlet eigenfunction is analytic in the interior,
but zero extension has a nonzero boundary flux against collar-crossing
tests.

For the completed-zeta form, `KNC` gives on an exterior collar

\[
 H_{\log}n=-R_\zeta n,                              \tag{5.2}
\]

not `H_log n=0`.  The right side contains rank-two pole moments, the bounded
archimedean remainder, and shifted interior traces
`n(x plus_or_minus log m)` with their exact von-Mangoldt weights.  These do
not vanish merely because `n` vanishes on the collar.  Applying logarithmic
unique continuation therefore requires a new theorem showing that this
entire completed source can be absorbed into a local homogeneous extension
system.  No such theorem is presently available.

## 6. The other proposed routes

### Pseudodifferential analyticity

The logarithmic principal symbol supplies compact resolvent, regularity, and
the Fredholm reduction already used in the fixed-point report.  Analytic
hypoellipticity, even if established, would control the interior nullstate;
it would not kill its exterior boundary functional.  Dirichlet eigenfunctions
of ordinary analytic elliptic operators are an exact counterexample to that
inference.  Bounded or compact nonlocal perturbations can change the charge
without changing the principal symbol.

An elementary rank-one model makes the last point exact.  In a reference
Hilbert space take nested `E subset F`, unit vectors `n in E` and
`z in F cap E^perp`, and `g=n+z`.  The form

\[
 q_-(u,v)=\langle u,v\rangle
           -\langle u,g\rangle\langle g,v\rangle    \tag{6.1}
\]

restricts on `E` to the nonnegative projection form with kernel `span{n}`,
but `q_-(n,z)=-1`.  Replacing `g` by `n` gives the same old compression and
a persistent uncharged kernel.  Both are `identity plus rank one`.  Hence
Fredholm/compact data and the entire old block do not determine KNC.

### Compact support and Paley--Wiener

The localized equation is `P_a A P_a n=0`, not the global multiplier
equation `A n=0`.  Compact support makes `n-hat` entire, but it does not turn
the unknown exterior residual into zero.  A Paley--Wiener argument becomes
valid only after continuation to every compact support, which is precisely
what KNC is being asked to prove.

### Prime-shift geometry

Newly activated prime shifts have zero *old--old* autocorrelation because
their displacement is at least the old support diameter.  This proves exact
old-block consistency.  It says nothing about the old--collar cross term:
once the collar is added, the same translate overlaps it and samples shifted
interior values of `n`.  At a contact, KNC is exactly the assertion that all
such traces cancel the pole and archimedean flux for every collar test.

Suzuki's ramp formula reinforces rather than removes this issue.  The kink
lines `x-y=plus_or_minus log m` create shifted interior traces; the residual
is not a finite endpoint jet.  No sign, disjointness, or threshold identity
forces the completed sum to vanish.

### Explicit formula / zero side

The global Weil criterion and Suzuki's nondegeneracy theorem already prove
the equivalence in Section 4.  At one finite support, however, the zero
exponentials are overcomplete, and a localized radical identity does not
isolate an individual zero quartet.  Turning a finite support gap of the
Euler--Lagrange distribution into coefficientwise zero information requires
a new quasianalytic or spectral-synthesis theorem for the *specific*
completed-zeta coefficients.  Such a theorem would itself imply the KNC/RH
criterion; none is imported in the current literature ledger.

### Yoshida/Suzuki nondegeneracy

This route decides the logical classification, not the truth value.
“`ker Q_a={0}` for every `a`” is already RH-equivalent.  Replacing it by
“every semidefinite kernel persists through a right germ” changes the local
shape but, after the support-continuation theorem, not the global logical
strength.

## 7. What an actual proof would now have to contain

A non-circular KNC proof must fix a basis `n_1,...,n_d` of the first-contact
kernel and one outer slab `B>=b`.  Let `V_B` be the logarithmic reference-form
Hilbert space, let `H_B=L2(I_B)` be its pivot, let
`mathcal J:V_B->H_B` be the compact embedding, and let the bounded
self-adjoint `R_B:H_B->H_B` represent the completed residual on the slab.
Put `W=E_b cap E_a^{perp_h}` and prove the correctly typed vector identities

\[
 P_W^{\mathfrak h}\mathcal J^*R_B n_j=0
 \qquad (j=1,...,d)                                 \tag{7.1}
\]

on one, hence every sufficiently thin, collar.  Equivalently,
`<R_B n_j,w>_L2=0` for every `w in W`.  Here
`mathcal J^*:H_B->V_B` is the Riesz map for the reference form; it is essential
because `R_B n_j` is an `L2` vector, whereas `P_W^h` acts on the form space.
The identity must keep the completed source intact.  Componentwise bounds,
analytic regularity, compactness, prime-threshold disjointness, or a charge
tending to zero cannot prove (7.1).

The only genuinely new mathematical socket left by this audit is an exact
**completed-source exterior synthesis theorem**: a theorem that converts the
old Euler--Lagrange equation into (7.1) by a pole--archimedean--prime identity
on the adjacent collar.  Universally quantified, that theorem is
RH-equivalent.  Its merit would be an explicit arithmetic mechanism, not a
reduction in logical strength.

## 8. Decision-tree delta

This pass is not zero-delta.  It corrects two descriptions in the recursive
fixed-point report:

- universal zeta `KNC` should be marked `RH-EQUIVALENT`, not merely a “new
  minimal gate” that might be read as strictly smaller;
- “finite-dimensional at each contact” refers only to the domain/rank of the
  charge operator, not to the amount of collar data that must be shown to
  vanish.

It also closes logarithmic unique continuation, principal-symbol analyticity,
compact support, and prime-threshold geometry as stand-alone KNC proofs.  The
first supplies an exact anti-persistence countermodel; the others do not
control the exterior functional.  No result here proves RH, a uniform
zero-free strip, `DPA`, `LTRAD`, `CA4`, or the sharp four-cycle bound.

## Claim ledger

| claim | status / trust |
|---|---|
| quantifier collapse and right-openness equivalence | exact project theorem; analytic manuscript |
| universal completed-zeta KNC iff RH | conditional only on already accepted Weil/continuity/domain interfaces; analytic manuscript plus imported literature |
| one fixed charged nullstate under failure of RH | exact finite-dimensional consequence of the same interfaces |
| logarithmic Dirichlet charged-contact countermodel | project deduction from imported logarithmic-Laplacian UCP and standard ground-state theory |
| principal-symbol/rank-one countermodel | exact abstract construction |
| completed-source exterior synthesis | **open; RH-equivalent when universal** |
| RH / uniform strip | **open** |
