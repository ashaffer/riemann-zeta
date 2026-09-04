# Recursive fixed-point audit evidence

Date: 2026-09-01

## Purpose and status

This is a supporting audit for
[`ZETA23-RECURSIVE-CONSOLIDATION-FIXED-POINT-2026-09-01.md`](ZETA23-RECURSIVE-CONSOLIDATION-FIXED-POINT-2026-09-01.md).
It does not restate that report's propagation theorems.  It records only:

1. which old barriers are genuinely subsumed by the new abstractions;
2. the counterexamples and hypothesis caveats used in the hostile pass;
3. the correction-sensitive iteration and convergence ledger; and
4. exact literature passports needed for the relative Weil criterion and
   the standard functional-analytic components.

The architecture and global claim ledger are unchanged:

```text
RH                                                OPEN
uniform zero-free strip                           OPEN
DPA_P(.019)                                       OPEN
LTRAD_P(.0189,.001)                               OPEN
CA4 and the sharp four-cycle bound                OPEN
sharp four-cycle bound as a direct strip gate     FALSE
```

## 1. Audit basis

The normalization pass used the mandatory consolidated state and preflight,
the second-order theorem suite, and the following branch endpoints:

- the `DPA/LTRAD` full-run, participation, null-corrector, and Fejer reports;
- the literal `FC`, `XDC`, restricted-type, and coefficient-color reports;
- the `CA4` global-conductor, actual-hat, natural-mask, and product-edge-flux
  reports;
- the faithful all-cut `SR2PF` theorem and its upstream transport passport;
- the complete `R71--R89` registry rows, together with the `R90/R91`
  superoscillation endpoint needed to test the proposed abstraction; and
- the current semilocal relative-Ward and compact-filtration reports.

Every application was checked with the mask, source, coefficient cone,
normalization, quantifier order, full band, resolution, exponent, and
downstream adapter retained.  Similarity of scale was not counted as an
implication.

## 2. Strict-delta application and subsumption table

| old barrier or branch | abstraction that really applies | exact content subsumed | content **not** subsumed | decision effect |
|---|---|---|---|---|
| scalar natural-mask transfer to `CA4` | provenance modulus plus convex/atomic synthesis duality | forgetting the adjacent-gap mark gives a vertical fiber obstruction; the interval-atom variation witness lower-bounds every scalar decomposition cost | the signed joint product-edge-flux theorem, which changes the resource body and keeps the common kernel | scalar transfer stays closed; `PG-EF(1/10)` stays open |
| signed finite-moment correction | observation--synthesis polarity | existence and minimum norm of a correction are a quotient/right-inverse problem | any arithmetic estimate for the actual moment map | stop treating a formal nullspace as a conditioned correction |
| positive normalized moment correction | convex attainable-body duality | feasibility is membership in the image of the simplex; infeasibility has a separating hyperplane | Gram rank does not provide convex-hull membership or inradius | retain the coefficient cone in every passport |
| `R90/R91` superoscillation | synthesis gauge, provenance modulus, and equicontinuity audit | factorial/Laplace conditioning is invariant under transported basis changes; an ideal prime-gap bump and zero have identical prime-power samples but different target response | the explicit-formula identity forcing the complete signed zero remainder to repay the unit reserve | further interpolation optimization is not the open edge; the signed full-zero estimate is |
| exact `R71/R87` recompletion | bi-Lipschitz provenance invariance and resource-body invariance | an invertible coordinate change neither gains information nor lowers intrinsic cost without an inverse-norm payment | all-sector sign restitution and equality with the original completed energy are additional arithmetic identities | no preconditioner or sector coordinate change is promoted to a saving |
| adaptive finite evidence for `DPA/LTRAD` | equicontinuous-family certificate obstruction | within the recorded compact pseudonode models, a globally valid uniformly equicontinuous, even infinite and adaptively chosen, certificate bank cannot separate the exhibited accumulating configurations with fixed margin | an actual-prime realization of the model hypotheses, or a genuinely non-equicontinuous actual-prime certificate with its derivative/bandwidth cost controlled | finite/model diagnostics remain finite evidence; any licensed escape must book its growing modulus |
| literal `FC/XDC` | rank-one cone firewall | control on `u\otimes u`, even for `u>=0`, does not yield dimension-free full-space operator control | the already proved restricted-type equivalence on the same cone | do not replace `XDC/RT` by Douglas factorization for arbitrary pair vectors |
| importing `SR2PF` into `CA4` | automatic all-cut secant identity | every `lambda^{\otimes k}-eta^{\otimes k}` already has all flattening ranks at most two | distinct-prime entries, positive `B^-1` decomposable approximation, and integrality, which are the actual `SR2PF` rigidity inputs | the cross-branch shortcut is closed; upstream faithful `SR2PF` transport is unaffected |
| higher-order mask transport | odd-channel polarization | order two is exceptionally a one-mark/two-channel identity | at order at least three, higher odd-mark channels cannot be omitted | do not extrapolate the quadratic product-flux formula unchanged |
| compact-filtration Weil propagation | compact-times-strong convergence | `J(P_t-P_s)` is operator-norm small for a compact form-domain embedding and nested form-orthogonal projections | kernel-charge cancellation and positivity at first contact | the compactness step survives; Hartman/AAK is not a counterargument |

The quotient package therefore **partly**, not completely, subsumes the four
requested families.  It exactly captures resource cost and invertible
conditioning for all four.  Natural-mask fiber loss, superoscillatory
spectral restitution, and `R71` signed recombination still require their
problem-specific identities or countermodels.

## 3. Exact standard statements used by the audit

### 3.1 Scalar observation--synthesis polarity

For a bounded linear map `U:X->Y` of normed spaces, `t in X*`, and `C>=0`,

\[
 |t(x)|\le C\|Ux\|\quad(x\in X)
\]

holds if and only if `t=U^*y^*` for some `y^* in Y^*` with
`||y^*||<=C`.  The least constants agree.  The proof defines
`ell(Ux)=t(x)` and applies Hahn--Banach.  This is the scalar Banach-space
form of stable descent; the Hilbert vector-valued version used elsewhere is
Douglas factorization.

### 3.2 Convex resource-body invariance

Let `E,X` be real or complex normed spaces, let `C subset E` be a closed
convex resource set containing zero, and let `S:E->X` be bounded linear.  Put
`A=closure(S(C))`, with closure in `X`.  Its (possibly extended-valued) gauge
has the polar formula

\[
 p_A(x)=\sup_{\phi\in A^\circ}\operatorname{Re}\phi(x),
 \qquad
 A^\circ=\{\phi:h_C(S^*\phi)\le1\}.
\]

If `E'` is normed, `R:E'->E` is a bounded linear isomorphism, and **the whole
resource set is transported**,
`C'=R^{-1}C`, then

\[
 SR(C')=S(C).
\]

Thus feasibility, gauge, and dual separators are identical.  For native
unit balls instead, define `gamma_S(x)=inf_{Se=x}||e||` on the common range
`S(E)=SR(E')`.  The division-free quotient-cost comparison is

\[
 \gamma_S(x)\le\|R\|\gamma_{SR}(x),
 \qquad
 \gamma_{SR}(x)\le\|R^{-1}\|\gamma_S(x).
\]

Transporting only a norm while changing positivity, support, or normalization
does not meet the theorem's hypotheses.

### 3.3 Nonlinear provenance data processing

For metric maps `U:X->Y` and `T:X->Z`, with nonempty `X`, and for `r>=0`,
set the extended-valued modulus

\[
 \omega_{T\mid U}(r)=
 \sup\{d(Tx,Tx'):d(Ux,Ux')\le r\}.
\]

If `V` is `L`-Lipschitz with `L>0`, while `V|_{U(X)}` is injective and its
inverse `V(U(X))->U(X)` is `M`-Lipschitz with `M>=0`, then

\[
 \omega_{T\mid U}(r/L)
 \le \omega_{T\mid VU}(r)
 \le \omega_{T\mid U}(Mr).
\]

A decoder `D` with uniform error `epsilon` satisfies, with `omega_D`
restricted to `U(X)`,

\[
 \omega_{T\mid U}(r)\le2\epsilon+\omega_D(r).
\]

These follow by inclusion of the admissible pairs and the triangle
inequality.  They distinguish exact identifiability, which an invertible
map preserves, from usable stability, which pays its condition constants.

### 3.4 Equicontinuous adaptive certificates

Let `K` be compact, `A subset K` the admissible class, `a_n in A`, and
forbidden `b_n in K`, with `d(a_n,b_n)->0`.  If the nonempty family
`F subset C(K,R)` is equicontinuous and every member is globally valid,
`f(a)<=0` for all `f in F` and `a in A`, then

\[
 \limsup_n\sup_{f\in F} f(b_n)\le0.
\]

This is stronger than the finite-certificate lemma because a finite family
on a compact space is automatically equicontinuous.  The hypothesis is
sharp: on `[0,1]`, with `a_n=0`, `b_n=1/n`,

\[
 f_n(x)=\max(1-2n|x-1/n|,0)
\]

has `f_n(a_n)=0` and `f_n(b_n)=1`, but the family is not equicontinuous.

## 4. Hostile checks and explicit countermodels

| proposed overclaim | falsifier or caveat | resulting scope |
|---|---|---|
| quotient duality for an arbitrary nonclosed image using only ambient duals | the intrinsic statement must use a surjection/quotient topology or the closed convex image and its polar | the report uses the convex resource body, not an unjustified raw-range equality |
| invariance under any invertible change of variables | a map not transporting the positive cone or support changes the feasible body | invariance is passport-preserving only |
| cone estimate implies full operator estimate | on `Sym_n`, `L(X)=tr X` has `|L(uu^*)|=||uu^*||_F`, while `||L||=sqrt(n)` | `FC` remains a restricted-cone theorem |
| all-cut rank two transfers `SR2PF` rigidity | `lambda^{\otimes k}-eta^{\otimes k}` is a difference of two rank-one tensors under every flattening | arithmetic height and integrality are indispensable |
| compact domain plus continuous tests gives a uniform finite certificate | arbitrarily narrow continuous tents avoid any fixed finite sample | a common modulus and a budget-compatible mesh are required |
| Hartman/AAK kills compact-filtration localization | that theory concerns Hankel compactness/essential-norm approximation; here the compact operator is `J` and the small map is `J(P_t-P_s)` | the objection was retracted |

For the last row, if `J:H->G` is compact and `Q_n=Q_n^*` are uniformly
bounded with `Q_n->0` strongly, then `||JQ_n||->0`: approximate `J` in norm
by a finite-rank map and use strong convergence on its finite-dimensional
adjoint range.  Nested form-orthogonal support projections satisfy exactly
this mechanism once their left/right density identities are proved.

## 5. Literature passports

### LIT-FP1: finite-vanishing-set Weil criterion

Alain Connes and Caterina Consani,
[*Weil positivity and trace formula, the archimedean place*](https://doi.org/10.1007/s00029-021-00689-4),
Selecta Math. (N.S.) **27** (2021), article 77, Appendix C,
Proposition C.1; [author PDF](https://alainconnes.org/wp-content/uploads/Selecta.pdf).

Exact scope: if `Z` is the set of nontrivial zeta zeros and `F subset C` is
finite, disjoint from `Z`, and contains `{0,1}`, then RH is equivalent to the
Weil inequality for every `g in C_c^infty(R_+^*)` whose Mellin transform
vanishes on `F`.  For

\[
 \widetilde g(s)=\int_0^\infty g(u)u^s\,{du\over u},
 \qquad f(x)=e^{x/2}g(e^x),
\]

direct substitution gives

\[
 \ell_-(f)=\widetilde g(0),\qquad
 \ell_+(f)=\widetilde g(1).
\]

The normalization-matched project convention is
`q_project(f)=-sum_v W_v(g*bar(g)^sharp)`.  Thus project nonnegativity is
their displayed nonpositivity, and taking `F={0,1}` verifies the two-moment
relative criterion with both the half-density and sign adapters exposed.
This is a global/cofinal criterion, not positivity at one fixed support.

### LIT-FP2: localized continuity and open--closed logic

Masatoshi Suzuki,
[*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096),
Theorems 1.3--1.4 and the discussion after Corollary 1.6.

Exact imported content used here: the localized lowest eigenvalue is
continuous in the support parameter and is positive for sufficiently small
support; Suzuki records Yoshida's equivalence between RH and nondegeneracy
of every finite localized form.  This supports the logical open--closed
route.  It does not prove exclusion of a charged relative nullstate.

### LIT-FP3: Hilbert factorization

Ronald G. Douglas,
[*On majorization, factorization, and range inclusion of operators on Hilbert
space*](https://doi.org/10.1090/S0002-9939-1966-0203464-1),
Proc. Amer. Math. Soc. **17** (1966), 413--415.

This is the primary source for the Hilbert-space range/factorization theorem
behind stable descent and the Ward graph-norm criterion.  It supplies no
arithmetic factorization by itself.

### LIT-FP4: atomic norms

Venkat Chandrasekaran, Benjamin Recht, Pablo A. Parrilo, and Alan S. Willsky,
[*The Convex Geometry of Linear Inverse Problems*](https://doi.org/10.1007/s10208-012-9135-7),
Found. Comput. Math. **12** (2012), 805--849;
[preprint](https://arxiv.org/abs/1012.0621).

This is a primary modern comparator for gauges induced by convex hulls of
atoms and their dual geometry.  The quotient/resource-body identities above
are standard convex analysis; no literature novelty is claimed.

### LIT-FP5: a nonapplicable Hankel comparison

Philip Hartman, *On completely continuous Hankel matrices*, Proc. Amer. Math.
Soc. **9** (1958), 862--866, and V. M. Adamyan, D. Z. Arov, M. G. Krein,
[*Infinite Hankel matrices and generalized Caratheodory--Fejer and I. Schur
problems*](https://doi.org/10.1007/BF01075679), Funct. Anal. Appl. **2**
(1968), 269--281.

These sources govern compact Hankel operators and Hankel approximation.  They
would obstruct a claim that finite surgery makes a noncompact Hankel operator
compact.  They do **not** obstruct norm localization of a separately compact
embedding composed with strongly convergent support projections.

## 6. Convergence ledger

This supporting audit used a finer ledger than the main report so that
late hypothesis corrections could not be hidden inside one pass.

| audit pass | operation | strict delta |
|---|---|---:|
| `A0` | freeze branch passports and canonical endpoint claims | baseline |
| `A1` | extract observation--synthesis, data-processing, equicontinuity, cone, and tensor candidates | 6 |
| `A2` | reapply every candidate across `DPA/LTRAD/CA4/FC/SR2PF/R71--R91` | 3 cross-branch consequences |
| `A3` | hostile qualification: transport the full cone; separate conditioning from sign restitution; retract the Hartman/AAK misapplication | 3 scope corrections |
| `A4` | rerun normalized theorem, countermodel, exponent, and decision-edge comparison | **0** |
| `A5` | independent repeat of `A4`, including the relative Weil literature passport | **0** |
| `A6` | later field/quantifier/trace-ideal hostile audit over the expanded basis | 9 hypothesis or scope corrections |
| `A7` | KNC last-mile audit: collapse germ quantifiers, identify exact right-openness and universal RH-equivalence, test unique continuation | 1 decision-edge correction plus 4 route closures |
| `A8` | recursive discovery over corrected analytic, singular, operator, second-order, formal, and passport artifacts | endpoint/slab/domain corrections; null-set thickness; boundary cutoff and balance; cyclic-trace counterexample/scope; tensor-position and adapter-passport repairs |
| `A9` | first attempted terminal artifact-integrity pass | referenced recursive postflight absent; pending non-certifying postflight created and zero clock reset |
| `A10` | first attempted terminal count-integrity pass | canonical no-go count was stale: the atlas contains `NG-01` through `NG-46`; preflight, report, and postflight counts corrected and zero clock reset |
| `A11` | next attempted terminal proof-integrity pass | arbitrary-rate operator construction omitted the domination `M_n -> max(M_n,n)` needed to infer unboundedness for a bounded prescribed sequence; proof repaired and zero clock reset |
| `A12` | completion of the invalidated `A11` discovery sweep | synonymous stale 45-card count in the upstream second-order report corrected to 46; corpus-wide variant-phrasing search then exhausted this count defect |
| `A13` | terminal-metric reproducibility check | undocumented 1,891 theorem-like-heading count did not reproduce; replaced by 1,890 and the exact frozen extraction command; zero clock reset |
| `A14 / Z1` | complete hostile normalized pass over frozen V4 | **0**; all 20 hashes and all five inventories matched before and after |
| `A15 / Z2` | independent sequential complete pass over the identical V4 snapshot | **0**; theorem scopes, passports, links, statuses, decision edges, Lean, tests, proof tree, and SR2PF replay unchanged |

The earlier `A4--A5` pair ceased to be terminal when the expanded hostile
audits found `A6--A13`.  Convergence is not credited from those historical
zeros.  The fresh `A14--A15` pair used one byte-identical frozen basis and is
the terminal certificate required by the declared convergence rule.

## 7. Audit conclusion

The strict gain is not a new strip estimate.  It is a smaller and more
reliable decision tree:

- resource-preserving rewrites cannot erase an atomic/right-inverse cost;
- further processing cannot improve provenance;
- adaptive continuous certificates need a paid non-equicontinuous escape;
- `FC` cone control and `SR2PF` integrality cannot be silently linearized or
  transferred to `CA4`; and
- the compact-filtration step in the new Weil route is valid, leaving the
  charged relative nullstate as the actual open arithmetic edge; universally,
  that `KNC` assertion is RH-equivalent rather than an easier conjecture.

No socket in this audit composes `DPA` with `LTRAD`, proves `CA4`, proves the
sharp four-cycle bound, or proves RH.
