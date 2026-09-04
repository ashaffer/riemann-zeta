# RECOVERY_STATE.md

> **Recursive consolidation update (2026-09-01):** the current cross-corpus
> theorem basis and corrected Weil decision tree are in
> [`results/ZETA23-RECURSIVE-CONSOLIDATION-FIXED-POINT-2026-09-01.md`](results/ZETA23-RECURSIVE-CONSOLIDATION-FIXED-POINT-2026-09-01.md).
> It identifies charged-nullstate cancellation as the remaining arithmetic
> continuation normal form.  Universally quantified it is RH-equivalent, not
> an easier conjecture; it does not prove RH or a uniform strip.

> **Supersession notice (2026-09-04):** this remains a recovery/audit record,
> but its frontier ordering is historical.  Run
> `python3 src/zeta23_correction_context.py resume` and read
> [`results/ZETA23-R71-PRINCIPAL-BAND-EXACT-SERIALIZATION-2026-09-04.md`](results/ZETA23-R71-PRINCIPAL-BAND-EXACT-SERIALIZATION-2026-09-04.md).
> The 2026-09-02 decision path is the verified pre-R181 plan snapshot; the
> R186 closes the split serialization and weak/L2 adapter but leaves KNC,
> while R187 closes the analytic principal-band tails and R188 gives the exact
> finite high-cofactor serialization and an exponent-equivalent
> `.998/.002/.0025` cofactor/quotient/numerator collar.  The remaining joint completed `.98`
> correlation is uniform-strip strength.  The strip and RH remain open.  The
> August 30 consolidation remains background preflight.

Recovery date: 2026-08-09  
Evidence basis: inherited conversation, current source tree, Git history and reflogs, tracked scripts/results, generated certificate artifacts, and a read-only process/worktree audit.

Status vocabulary:

- **PROVED**: a proof is present and sufficiently delimited. For Lean results, source and focused audit files exist, though no fresh build was run during recovery.
- **CONDITIONAL**: depends on an explicit axiom, imported theorem, or stated unproved hypothesis.
- **NUMERICAL**: finite computation or computer-assisted result outside the complete Lean arithmetic-form chain.
- **HEURISTIC**: intuition, empirical pattern, or model prediction.
- **OPEN**: required statement is absent.
- **REFUTED**: the stated route or candidate class has a counterexample; scope matters.
- **UNCLEAR**: a proof-looking manuscript argument exists but has not passed sufficient independent verification.

Commit aliases used below:

| Alias | Commit |
|---|---|
| `C0` | `d2d4e079dba4e34a9291bdf57e44fa861a52bb3d` |
| `C1` | `96a3d99934aa7fca7a57b2d7eb2d6485f8a2de1e` |
| `C2` | `b9a0574adefa16c09ef1bcd78d28cc1aff43d26b` |
| `C3` | `14b273d0aa4100e27b9d3fb6306bb27df1ec61ad` |
| `C4` | `e9869851ae1aef2255a8cfe4ce7a7e80684dee74` |
| `C5` | `7ec0ef8ff396938dafd05c286cef59e14e3d35a1` |
| `C6` | `06a3fe3cac6e0b3f51b1865a01dde60dc30f2f4a` |

# 1. Central objective

## Ultimate objective

The ultimate objective is the Riemann Hypothesis:

\[
\forall \rho,\quad
\zeta(\rho)=0,\ 0<\Re\rho<1
\Longrightarrow \Re\rho=\frac12.
\]

No repository artifact proves RH, its negation, or independence from ZFC.

## Exact formal criterion under pursuit

The repository defines:

```text
GlobalWeilPositivity :=
  ∀ a : ℝ, 0 ≤ a →
    ∀ f : LogarithmicFormDomain a,
      0 ≤ logarithmicWeilForm a f
```

and the algebraically equivalent statement

```text
GlobalPrimeDomination :=
  ∀ a : ℝ, 0 ≤ a →
    ∀ f : LogarithmicFormDomain a,
      primeTerm a f.val
        ≤ poleTerm a f.val + archimedeanTerm a f.val.
```

The equivalence

```text
RiemannHypothesis ↔ GlobalWeilPositivity
```

is an explicit literature axiom in Lean. Thus global positivity is an RH-equivalent criterion, not a proved result.

## Supporting lemma pursued in the inherited conversation

After the canonical \(p=2\) endpoint was closed, the user explicitly redirected the work away from certifying additional windows and toward a uniform-in-support mechanism.

The exact remaining supporting claim is a zeta-specific adjacent-support relative estimate. In informal floor notation,

\[
\lambda(a)=\inf_{\substack{f\in D_a\\\|f\|=1}}Q_a(f),
\]

one sufficient form is:

\[
\lambda(\tau_{n+1})\ge \theta_n\lambda(\tau_n),
\qquad \theta_n>0,
\]

along a cofinal sequence \(\tau_n\to\infty\).

No positive lower bound on all \(\theta_n\), and no positive infinite product, is necessary. For every fixed target support, only a finite product is used.

A block version would require independent estimates

\[
Q_b(u)\ge\beta\|u\|^2,\qquad
Q_b(w)\ge d\|w\|^2,\qquad
|B_b(u,w)|\le c\|u\|\|w\|,
\]

with \(\beta,d>0\) and \(c^2<\beta d\), where \(u\) is the old-support part and \(w\) the new collar.

The abstract Schur and cofinal-propagation logic is now Lean-proved. Its zeta-specific analytic premise remains **OPEN**.

## Later repository-only frontier

Later checkpoints, absent from the inherited conversation at its pause, developed a separate analytic branch. The latest surviving contour target is:

\[
F_H(s)=\zeta(s)\prod_{p\le H}(1-p^{-s}),
\]

\[
B_{q,H}(s)
 =(1-F_H(s))^{q-1}\frac{F_H'(s)}{F_H(s)},
\]

and, under a hypothetical target zero \(\rho\),

\[
\int_C\log^+|(s-\rho)B_{q,H}(s)|\,d\omega_\rho(s)
 \le q a_R\omega\log H-cq\log H.
\]

Here \(q\ge1\) is an integer, \(a_R>0\) describes the controlled right boundary, \(C\) is the uncontrolled boundary, and \(\omega\) is the right arc's harmonic measure at \(\rho\).

The required uniform quantifiers over \(\rho,q,H\), domains, contours, \(a_R,\omega\), and \(c\) are not yet fully specified. This estimate is **OPEN**. If established uniformly at the required scale, it would imply a fixed zero-free strip, not automatically RH.

The uniform-support branch and this R176 contour branch are parallel; neither currently supplies the other.

# 2. Definitions and conventions

## Support parameters

Current Lean uses the interval half-width \(a\):

\[
H_a=L^2([-a,a],\mathbb R),
\]

with zero extension to \(\mathbb R\).

Historical documents use

\[
L=4a.
\]

Consequently:

- the active-prime cutoff \(\log n<2a\) is \(\log n<L/2\);
- a prime power activates at \(a=\frac12\log n\), or historical \(L=2\log n\);
- the certified endpoint \(a=7/16\) is historical \(L=7/4\).

## Fourier conventions

Lean/mathlib ordinary frequency:

\[
\widehat f(\xi)
 =\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx.
\]

Historical angular frequency:

\[
\widehat f_{\rm ang}(r)
 =\int_{\mathbb R}f(x)e^{-irx}\,dx,
\qquad r=2\pi\xi,
\]

with Parseval factor \(1/(2\pi)\) in angular coordinates.

The fixed-box manuscript instead writes

\[
\widehat f(z)=\int_{\mathbb R}f(x)e^{izx}\,dx.
\]

This has the opposite exponential sign from the Lean ordinary-frequency convention. Every comparison must account for that sign and \(r=2\pi\xi\).

No pointwise Fourier inversion is needed in the formal endpoint. The proof uses the unitary \(L^2\) transform, almost-everywhere identification with the pointwise \(L^1\) transform, and Plancherel.

## Autocorrelation

The relevant real autocorrelation is

\[
C_f(u)=\int_{\mathbb R}f(x)f(x+u)\,dx.
\]

The orientation matters when compared with Fourier phases, although for real diagonal quadratic terms the cosine symmetrization removes it.

## Logarithmic domain

\[
D_a=
\left\{
f\in H_a:
\int_{\mathbb R}
 \log(1+(2\pi\xi)^2)|\widehat f(\xi)|^2\,d\xi<\infty
\right\}.
\]

Lean calls the predicate `InLogarithmicDomain` and packages its vectors as `LogarithmicFormDomain`.

The repository proves zero/addition/scalar closure. It does not, in the endpoint chain, prove density, construct the associated unbounded self-adjoint operator, prove compact resolvent, or prove eigenvalue attainment.

## Arithmetic Weil form

\[
Q_a(f)=P_a(f)+A_a(f)-\Pi_a(f).
\]

For real vectors,

\[
P_a(f)
 =2\langle f,e^{x/2}\rangle
    \langle f,e^{-x/2}\rangle.
\]

Equivalently, Lean writes the two reversed products explicitly.

The archimedean term is

\[
A_a(f)=
\int_{\mathbb R}
\left(
\Re\psi\!\left(\frac14+i\pi\xi\right)-\log\pi
\right)|\widehat f(\xi)|^2\,d\xi.
\]

Writing

\[
\operatorname{quarterDigammaReal}(r)
 =\Re\psi\!\left(\frac14+\frac{ir}{2}\right),
\]

this multiplier is
\(\operatorname{quarterDigammaReal}(2\pi\xi)-\log\pi\).

The finite prime-power term is

\[
\Pi_a(f)=
\sum_{\substack{n\text{ prime power}\\\log n<2a}}
 \frac{2\Lambda(n)}{\sqrt n}\,C_f(\log n).
\]

The formal definition is finite by construction. The theorem that omitted shifts have zero autocorrelation after exceeding the support diameter is not part of the unconditional endpoint chain; it is currently an explicit project axiom in the smaller-support propagation module.

## Canonical \(p=2\) endpoint

At

\[
a=\frac7{16},\qquad L=\frac74,
\]

the active set is exactly \(\{2\}\). The coefficient is

\[
\frac{2\log2}{\sqrt2}=\sqrt2\log2.
\]

The angular multiplier is

\[
\Omega_2(r)
 =
\Re\psi\!\left(\frac14+\frac{ir}{2}\right)
-\log\pi-\sqrt2\log2\cos(r\log2).
\]

The clipped comparison uses:

- band radius \(S=50\);
- exterior floor
  \[
  \alpha=\Omega_2(50)
  =\operatorname{quarterDigammaReal}(50)-\log\pi-\sqrt2\log2;
  \]
- bounded defect
  \[
  1_{|r|\le50}\bigl(\Omega_2(r)-\alpha\bigr);
  \]
- \(48\) normalized Legendre modes;
- even and odd \(24\times24\) blocks;
- exact bounds
  \[
  \alpha\ge\frac{109387}{100000},
  \qquad
  |\Omega_2(r)-\alpha|\le\frac{7447}{1000}
  \quad(|r|\le50).
  \]

The clipped quadratic form is the scalar floor
\(\alpha\|f\|^2\), plus the bounded in-band defect multiplier, plus the exact two-vector pole form.

## Support decomposition

For \(a\le b\), nested zero extension embeds the old support into the larger interval. The larger vector is split orthogonally into:

- `oldPart a b`;
- `collarPart a b`.

The symmetric polarized cross term is `weilCross`. Algebraically,

\[
Q_b(u+w)=Q_b(u)+2B_b(u,w)+Q_b(w).
\]

The current decomposition is established on the ambient interval \(L^2\) test space. Preservation of the logarithmic form domain by the sharp pieces remains unresolved.

## Floor notation

Historical manuscripts define

\[
\lambda(a)
 =\inf_{\substack{f\in D_a\\\|f\|=1}}Q_a(f).
\]

This support-indexed floor is not presently packaged as the actual Lean value consumed by `UniformSupportTransfer`. Claims about its attainment, spectral interpretation, or continuity are manuscript-level rather than part of the unconditional endpoint theorem.

## Zero-side convention and regularization

For a nontrivial zero \(\rho\),

\[
z_\rho=\frac{\rho-\frac12}{i}.
\]

Zeros are counted with analytic multiplicity.

For smooth tests, the intended zero sum is absolutely convergent. On the logarithmic form domain, the repository correctly uses symmetric exhaustion through closed disks:

\[
\lim_{R\to\infty}
 \sum_{\rho\text{ in the closed disk of radius }R}
   \text{zeroSummand}(f,\rho).
\]

It does not assert an unconditionally summable scalar series at this regularity.

The formal contour infrastructure uses \(\zeta'/\zeta\), avoiding a branch choice for \(\log\zeta\).

## Fixed-window detector

For fixed \(\ell>0\),

\[
w_\ell(u)=\left(1-\frac{|u|}{\ell}\right)_+,
\qquad
M_\ell^2=\frac{16\sinh^2(\ell/4)}{\ell},
\]

\[
\Delta=\sup_\rho\left|\Re\rho-\frac12\right|.
\]

Define

\[
D_\ell(R)
 =
\sum_n\Lambda(n)n^{-1/2}w_\ell(\log n-R)
-M_\ell^2e^{R/2}.
\]

The box function and transform are

\[
g_\ell(x)=\ell^{-1/2}1_{[-\ell/2,\ell/2]}(x),
\]

\[
G_\ell(z)=\frac{2\sin(\ell z/2)}{\sqrt\ell\,z},
\qquad
H_\ell(z)=G_\ell(z)^2
 =\frac{4\sin^2(\ell z/2)}{\ell z^2},
\]

with removable values at \(z=0\). Every zero of \(H_\ell\) is real.

All fixed-window claims quantify over each fixed \(\ell>0\); no uniform \(\ell\to0\) or \(\ell\to\infty\) result is established.

## Type-II normalization

For a smoothed ramp \(\Phi_{h,k}\),

\[
F_x(n)=n^{-1/2}\Phi_{h,k}(\log(x/n)),
\]

\[
M_U(s)=\sum_{d\le U}\mu(d)d^{-s},
\qquad
L_V(s)=\sum_{b\le V}\Lambda(b)b^{-s},
\]

\[
\beta_V(r)=\sum_{\substack{b\mid r\\b>V}}\Lambda(b),
\]

and

\[
B_{U,V}^{(k)}(x)
 =
\sum_{\substack{d>U\\r>V}}
 \mu(d)\beta_V(r)F_x(dr).
\]

The center \(Z_{U,V}^{(k)}(x)\) contains the explicitly computed pole, \(\zeta(1/2)\), \(\zeta'(1/2)\), and truncated \(M_U,L_V\) terms. It must remain attached to the complete cofactor sum.

For positive integers \(n,p\), complex powers such as \(n^{-s}\) and \(p^{-s}\) use the canonical real logarithm:

\[
n^{-s}=e^{-s\log n}.
\]

There is no complex-log branch ambiguity.

## R176 contour conventions

The intended target-isolating domain \(D\) is bounded, simply connected, and Jordan, with:

- \(\rho\in D\);
- no other relevant zero in \(D\);
- the pole at \(1\) excluded;
- \(\overline D\subset\{\Re s>0\}\);
- a nonempty right arc
  \[
  E\subset\{\Re s\ge1+a_R\};
  \]
- complementary boundary \(C=\partial D\setminus E\);
- harmonic measure
  \[
  \omega=\omega(\rho,E;D),\quad0<\omega<1.
  \]

For contour-integral Carleman statements, the boundary must additionally be rectifiable or piecewise \(C^1\). The current manuscript sometimes says merely “Jordan,” which is too broad.

Here

\[
\log^+x=\max(0,\log x)
\]

is a real logarithm.

The factor \((1-F_H)^{q-1}\) is an integer power, so it has no branch choice. The outer-function construction uses a single-valued harmonic conjugate because \(D\) is simply connected.

# 3. Approach

## A. Local Lean endpoint

1. Put the arithmetic form on its intrinsic logarithmic Fourier domain.
2. At \(a=7/16\), prove that only \(n=2\) is active.
3. Express the prime-two term as a time-domain translation correlation using Plancherel.
4. Lower-bound the exterior multiplier by \(\alpha\).
5. Represent the bounded in-band defect on the first \(48\) Legendre modes.
6. Split into even and odd \(24\times24\) matrices.
7. Prove exact interval containment for every canonical matrix entry using rational analytic truncation and rounding bounds.
8. Prove exact finite positivity through rational congruence/perturbation certificates.
9. Independently control the orthogonal complement and cross term.
10. Transfer the clipped lower bound to the original unbounded multiplier under the logarithmic-domain integrability hypothesis.
11. Identify that expression exactly with the general arithmetic form at \(a=7/16\).

This route produces a full infinite-dimensional form-domain result, not merely Galerkin positivity.

## B. Uniform support propagation

The inherited conversation recognized that certifying more isolated windows would not establish RH. The proposed replacement is:

1. start from the certified local interval;
2. select a cofinal support sequence;
3. prove a relative adjacent-support estimate at each step;
4. multiply only finitely many positive factors to reach any given finite support;
5. conclude global positivity;
6. invoke the classical Weil criterion.

The generic finite-product, cofinality, and Schur algebra is now formalized. The substantive zeta-specific relative estimate is missing.

## C. Fixed-window/Type-II reformulation

A separate analytic branch tries to compress horizontal zero displacement into one scalar prime discrepancy:

1. apply the explicit formula to one translated triangular test;
2. prove its exponential growth rate equals \(\Delta\);
3. strip higher prime powers;
4. pass to a ramp primitive;
5. apply a smoothed Euler formula;
6. use Vaughan’s identity;
7. isolate one centered near-square Type-II aggregate.

For fixed smoothing order, a sufficiently strong bound on that aggregate would imply RH. The reduction does not supply the bound.

## D. Hardy/Carleman contour branch

The latest branch tries to exploit nonlinear support beyond \(H^q\):

1. remove the finite Euler head from zeta;
2. form \(B_{q,H}\), retaining the target zero as a pole;
3. isolate its negative Hardy mode on a complete circle;
4. estimate the right boundary from absolute Euler convergence;
5. attempt to suppress the complementary boundary with Carleman weights or reflection.

The audit shows that harmonic measure exactly repays the right-boundary gain through forced complementary growth. Functional-equation reflection puts the target back into a merely \(H\)-supported linear term. What remains is a genuinely coefficient-specific bound on the complementary harmonic logarithmic mean.

## E. Role of computation

Numerical work has four distinct roles:

- generating exact rational candidates later checked by Lean;
- rigorous FLINT-Arb interval certificates whose analytic bridge remains outside Lean;
- finite falsification of proposed mechanisms;
- ordinary floating-point diagnostics.

Only the first role enters the unconditional \(p=2\) Lean endpoint, and even there the final theorem consumes exact rational inequalities rather than trusting the generator.

# 4. Claim inventory

## Formal arithmetic-form claims

| ID | Exact statement | Status | Dependencies, restrictions, and evidence |
|---|---|---|---|
| `WF-DOMAIN` | `InLogarithmicDomain a f` is integrability of \(\log(1+(2\pi\xi)^2)|\widehat f(\xi)|^2\); zero, addition, and real scalar closure give `LogarithmicFormDomain a`. | **PROVED** | Lean source present; not rebuilt. No density or self-adjoint-operator theorem included. `GeneralZetaWeilForm.lean`, `C4`. Repository only. |
| `WF-P2-MATRIX` | Every entry of the actual canonical even and odd \(24\times24\) matrices lies between its stored exact real interval endpoints. | **PROVED** | Generated exact rational ledgers, analytic tail bounds, 19,200 refinements, and 600 independent upper-triangular entries. `P2RoundedBoundedCertificateCheck.lean` and audit, `C0`. Repository and inherited conversation. |
| `WF-P2-CLIPPED` | For nonzero \(f\in L^2[-7/16,7/16]\), \((22699/10^9)\|f\|^2<p2ClippedForm(f,f)\). | **PROVED** | `WF-P2-MATRIX`, parity, complement, and cross transfer. Same check file, `C0`. |
| `WF-P2-ORIGINAL` | If \(f\ne0\) and \(\Omega_2(2\pi\xi)|\widehat f(\xi)|^2\) is integrable, then \((22699/10^9)\|f\|^2\) is strictly below the original multiplier integral plus exact pole term. | **PROVED** | `P2Parity.lean`, `C0`; weighted integrability is explicit. |
| `WF-P2-DOMAIN-BRIDGE` | `InP2Domain f ↔ InLogarithmicDomain f`; the cosine prime-two multiplier equals the time-domain autocorrelation term; the original integral bound holds on the intrinsic domain. | **PROVED** | Fourier/autocorrelation Plancherel and multiplier comparison. `ZetaWeilForm.lean`, last `C2`. Both repository and conversation: this was previously identified as missing. |
| `WF-ACTIVE-SET` | `activePrimePowers (7/16) = {2}` and \(2\Lambda(2)/\sqrt2=\sqrt2\log2\). | **PROVED** | Exact log bounds and arithmetic. `GeneralZetaWeilForm.lean`, `C4`. |
| `WF-ENDPOINT` | If \(f\ne0\) and \(f\in D_{7/16}\), then \((22699/10^9)\|f\|^2<Q_{7/16}(f)\). | **PROVED** | Theorem `weilForm_seven_sixteenths_strict_lower_bound`; focused audit source present, not freshly run. `GeneralZetaWeilForm.lean`, `C4`. This is arithmetic-side only. |
| `WF-CUTOFF-AXIOM` | If \(2a\le|u|\), then the interval autocorrelation at \(u\) is zero. | **CONDITIONAL** | Explicit axiom `intervalAutocorrelation_eq_zero_of_two_mul_le`. It is elementary compact-support analysis but not proved in Lean. `ActivationCancellation.lean`, `C2`. |
| `WF-BASE-INTERVAL` | For \(0\le a\le7/16\) and nonzero \(f\in D_a\), \((22699/10^9)\|f\|^2<Q_a(f)\). | **CONDITIONAL** | Uses `WF-ENDPOINT`, nested zero extension, and `WF-CUTOFF-AXIOM`. Only that cutoff axiom from `ActivationCancellation` lies on this theorem’s call chain. `CertifiedBaseInterval.lean`, `C3`. |
| `WF-SUPPORT-DECOMP` | Exact old/collar orthogonal split, norm identity, form expansion, and implication \(Q(u),Q(w)\ge0,\ B(u,w)^2\le Q(u)Q(w)\Rightarrow Q(u+w)\ge0\). | **PROVED** | Lean algebra/geometry on `TestSpace`. Does not prove log-domain preservation or zeta block bounds. `SupportDecomposition.lean`, `C2`. |
| `WF-COFINAL` | If `value` is antitone, positive at a base cofinal scale, and `factor n * value(scale n) ≤ value(scale(n+1))` with every factor positive, then `value(s)>0` for every support. | **PROVED** | Pure finite-product/order argument; no infinite-product assumption. `UniformSupportTransfer.lean`, `C2`. |
| `WF-PROP-IMPL` | Any `PropagationPackage` yields `GlobalWeilPositivity`. | **PROVED** | `globalWeilPositivity_of_propagationPackage`, `UniformPropagationToRH.lean`, `C2`. This is only an implication. |
| `WF-PROP-EXISTS` | There exists a `PropagationPackage` for the actual zeta form. | **OPEN** | No instance or existence theorem exists. |
| `WF-RELATIVE-STEP` | Along a cofinal sequence, obtain \(\theta_n>0\) with \(\lambda(\tau_{n+1})\ge\theta_n\lambda(\tau_n)\), or a domain-correct block determinant \(c^2<\beta d\). | **OPEN** | Main inherited-conversation target. Requires a real support floor, domain preservation, and new zeta-specific prime–archimedean analysis. `results/UNIFORM-L-MECHANISM.md`, `C0`, plus abstract formalization at `C2`. Evidence from both transcript and repository. |
| `WF-GLIDE-ABS` | The support floor is antitone and satisfies an additive \(O(1/\log(1/h))\) modulus, with closedness/compact-resolvent/attainment claims. | **UNCLEAR** | Detailed manuscript argument exists, but the complete spectral theorem is not Lean-formalized or independently refereed. `THEOREMS.md`, `C4`. The additive estimate is weaker than `WF-RELATIVE-STEP`. |
| `WF-SYMBOL-NOGO` | `activationDefectSymbol a b 0=0`; hence no \(\delta>0\) is a pointwise lower bound for that symbol at all frequencies. | **PROVED** | Lean proof independent of the module’s three declared analytic axioms. `ActivationCancellation.lean`, `C2`. |
| `WF-TWO-SLIVER` | For \(a<u<2a\), exact two-sliver unit vectors have autocorrelation \(+1/2\) and \(-1/2\); the entering translation remains order-one, indefinite, infinite-rank, and noncompact near threshold. | **REFUTED** | Refutes the naive small-operator perturbation route. Analytic proof in `results/UNIFORM-L-MECHANISM.md`, `C0`; also central in the conversation. |

## Zero-side and RH-criterion claims

| ID | Exact statement | Status | Dependencies and evidence |
|---|---|---|---|
| `GW-LOCAL` | Local zeta factorization at a nontrivial zero, analytic multiplicity, and \(\zeta'/\zeta=m/(s-\rho)+g'/g\) on a punctured neighborhood. | **PROVED** | Lean source using mathlib meromorphic continuation. `GuinandWeilFormula.lean`, last `C4`. |
| `GW-RIGHT` | Absolute von Mangoldt series for \(-\zeta'/\zeta\) on \(\Re s>1\), Gamma-factor identities, and functional-equation logarithmic derivatives. | **PROVED** | Lean source, same file/commit. |
| `GW-SMOOTH-ENTIRE` | A smooth compactly supported test has an entire bilateral Laplace transform. | **PROVED** | `smooth_bilateralLaplace_entire`, proved from `CompactSupportFourierLaplace.differentiable_transform`; focused axiom audit reports only the standard logical axioms. `GuinandWeilLiterature.lean`, current worktree. |
| `GW-SMOOTH-FORMULA` | The normalization-matched smooth Guinand–Weil zero sum equals the arithmetic form. | **CONDITIONAL** | Explicit axiom `smooth_guinandWeil_formula`, same file/commit. |
| `GW-LOGDOMAIN` | Symmetric closed-disk zero sums converge to the arithmetic form for every logarithmic-domain vector. | **CONDITIONAL** | Explicit axiom `logarithmicDomain_guinandWeil_formula`, same file/commit. |
| `WEIL-CRITERION` | `RiemannHypothesis ↔ GlobalWeilPositivity`. | **CONDITIONAL** | Explicit axiom `riemannHypothesis_iff_globalWeilPositivity`. `WeilCriterionLiterature.lean`, `C2`. |
| `RH-FROM-PACKAGE` | A genuine zeta `PropagationPackage` implies RH. | **CONDITIONAL** | `WF-PROP-IMPL` plus open package existence plus `WEIL-CRITERION`. This is not a proof of RH. |

## Fixed-window and Type-II claims

| ID | Exact statement | Status | Dependencies, restrictions, and evidence |
|---|---|---|---|
| `FW-WIDTH` | For fixed \(\ell>0\), \(\limsup_{R\to\infty}\log(1+|D_\ell(R)|)/R=\Delta\). | **CONDITIONAL** | Written proof depends on normalization-matched low-regularity Guinand–Weil, functional-equation symmetry, strip bounds, and Riemann–von Mangoldt counting. Not Lean-formalized or independently reviewed. Detailed report at `C5`, synthesis at `C6`. |
| `FW-RH-CRITERION` | For fixed \(\ell\), boundedness or subexponential growth of \(D_\ell\) is equivalent to RH. | **CONDITIONAL** | Depends on `FW-WIDTH`. The required bound is not proved. |
| `FW-PRIME-STRIP` | Removing prime powers leaves \(D_\ell=P_\ell+\ell/2+O_\ell(e^{-c\sqrt R}+(1+R)e^{-R/6})\). | **UNCLEAR** | Manuscript proof uses PNT/partial summation and a classical zero-free-region error; constants and normalization need review. `publication/FIXED-WINDOW...`, `C6`. |
| `FW-COBOUNDARY` | The ramp primitive has a finite-difference relation with \(D_\ell\) and retains exponent \(\Delta\). | **UNCLEAR** | Finite identity is elementary; exponent claim uses another transform-pole uniqueness argument. Same source. |
| `FW-EULER` | The displayed smoothed Euler/B-spline formula holds for fixed \(h,k\), with a derivative estimate and a claimed \(\exp(O_\ell(k\log k))\) uniform constant at \(h=\ell/k\). | **UNCLEAR** | A substantive proof exists, but distributional boundary terms, periodic \(B_1\) conventions, total-variation bounds, and nested-compact uniformity need independent checking. Detailed report `ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md`, `C5`; synthesis `C6`. |
| `FW-VAUGHAN` | Under \(UV\le xe^{-\ell}\), \(C_{h,k}(\log x)=B_{U,V}^{(k)}(x)-Z_{U,V}^{(k)}(x)+\) the displayed explicit error. | **CONDITIONAL** | Exact Vaughan identity plus `FW-EULER`. All sums are finite after cutoff; no independent Type-II estimate is inserted. `C6`. |
| `FW-FIXED-EXPONENT` | For fixed \(k\) and admissible fixed \(\theta\), \(\limsup\log(1+|B-Z|)/\log x=\Delta\). | **CONDITIONAL** | `FW-WIDTH` plus `FW-VAUGHAN`. Bounded/polylogarithmic \(B-Z\) would be RH-equivalent but is **OPEN**. |
| `FW-POWER-SAVING` | \(B-Z=O(x^{1/2-\eta})\) for some fixed \(\eta>0\). | **OPEN** | Would yield a fixed zero-free strip, not RH. |
| `FW-MOVING-ORDER` | With \(k\to\infty\), \(k\log(k+2)=o(\log x)\), and \(U=V=x^{1/2-c/k}\), the aggregate is localized to \(x^{1/2+o(1)}\) variables with the stated error. | **UNCLEAR** | Depends on the unverified uniform-\(k\) trace in `FW-EULER`. No reverse RH implication is known because the transform changes with \(x\). |
| `FW-FROZEN-BLOCK-NOGO` | Fixed cofactor blocks and separately frozen Euler bulk/boundary pieces acquire higher-order poles at zeta zeros and cannot be bounded by ordinary centerings. | **REFUTED** | Scoped analytic argument in the fixed-window manuscript, `C6`. Does not refute the full jointly centered aggregate. |
| `FW-AMBIENT-NOGO` | Coefficient-blind fixed-rank, Hilbert–Schmidt, singular-value, and local-reflection mechanisms do not contract the complete near-square operator enough. | **REFUTED** | Scoped reports and `NO-GO-ATLAS.md`, `C6`. A coefficient-specific joint estimate remains open. |

## R176 contour claims

| ID | Exact statement | Status | Dependencies, restrictions, and evidence |
|---|---|---|---|
| `R176-HARDY` | A meromorphic \(B\) with one simple pole \(m/(s-\rho)\) in a neighborhood of a closed circle has exact boundary identity \(\operatorname{mean}|B|^2=|m|^2/R^2+\sum_{n\ge0}|g_n|^2R^{2n}\). | **PROVED** | Elementary Taylor/Parseval proof present. Requires neighborhood meromorphy, not merely interior meromorphy. R176 §1, `C6`. |
| `R176-HARMONIC` | For a boundary split \(E,C\), \(|m|\le X_E^\omega X_C^{1-\omega}\), with the corresponding supremum lower bound on \(C\). | **PROVED** | Subharmonicity and Jensen under the stated Jordan-domain and boundary-integrability hypotheses. R176 §2, `C6`. |
| `R176-CARLEMAN` | Analytic weights cannot improve the harmonic-measure exponent; outer functions attain it. | **REFUTED**, scoped | Refutes generic Carleman improvement. The contour-integral wording needs rectifiable/piecewise-\(C^1\) boundary, and exact closed-boundary sharpness needs a small approximation argument. R176 §3, `C6`. |
| `R176-NONLINEAR-LOCAL` | A unique residue-one pole can locally be represented as \((1-F)^{q-1}F'/F\). | **CONDITIONAL** | Construction is correct when the regular primitive extends boundedly to a neighborhood of the compact closure so one inverse chart suffices. Current broad wording omits this qualification. |
| `R176-ZETA-TAIL` | Under an isolated hypothetical zero, \(|B_{q,H}|\le C_a^qH^{-qa}\log H\) on the fixed right arc, while the complementary norm must grow according to harmonic measure. | **CONDITIONAL** | Absolute Euler convergence on fixed \(\Re s\ge1+a\); fixed domain and geometry. R176 §4, `C6`. |
| `R176-DILATED-MODEL` | A dilated head-deleted zeta model has positive Dirichlet coefficients, support beyond \(H^q\), right-boundary smallness, and a near-one zero while paying the complementary norm. | **UNCLEAR** | Construction is plausible and explicit but unformalized; a residue-one version needs a simple known critical-line zero or must retain multiplicity. It is not degree-one zeta. R176 §5. |
| `R176-REFLECTION-NOGO` | Functional-equation reflection places the target pole entirely in the linear \(-F_H'/F_H\) term; removing that term removes the target and retaining it loses \(H^q\) support. | **REFUTED**, scoped | Algebraic derivation present. Head-growth asymptotic uses PNT at fixed reflected points; moving-contour uniformity is not shown. R176 §6. |
| `R176-LOGMEAN` | The coefficient-specific upper bound \(\int_C\log^+|(s-\rho)B_{q,H}|\,d\omega_\rho\le qa_R\omega\log H-cq\log H\). | **OPEN** | Exact uniform quantifiers and admissible contour geometry remain under-specified. R176 (7.2), `C6`. |
| `R176-STRIP` | `R176-LOGMEAN` with sufficient uniformity implies one fixed zeta zero-free strip. | **CONDITIONAL** | The implication requires constants uniform over every hypothetical zero in the excluded region. It does not directly imply RH. |

## Computer-assisted and side claims

| ID | Exact statement | Status | Dependencies and evidence |
|---|---|---|---|
| `NUM-P3` | At historical \(L=497/200\), the full-space form is claimed \(>9.99\times10^{-11}\|f\|^2\). | **NUMERICAL** | Rigorous FLINT-Arb plus analytic transfer, but not a Lean arithmetic-form theorem. `src/fullinf_unrestricted_p3_certificate.py`, `C0`; manuscript summary at `C4`. |
| `NUM-N4` | At historical \(L=749/250\), the full-space form is claimed \(>9.9\times10^{-16}\|f\|^2\). | **NUMERICAL** | FLINT-Arb, 132 modes, \(S=110\), 4,422 entries, and exterior bridge. Script and complete JSONL checkpoint at `C0`. |
| `NUM-LADDERS` | Galerkin margins, family envelopes, threshold glides, phase scans, and deep-window laws. | **NUMERICAL** | Tracked scripts/logs/results. Positive Galerkin values are not lower bounds for the full form. |
| `NUM-FIXED-BOX` | Arithmetic fixed-box value and first 100 critical-zero pairs agree to about \(2.72\times10^{-6}\). | **NUMERICAL** | Ordinary diagnostic with uncertified truncated zero tail. `src/fixed_box_width_spectrometer.py`, `C5`. |
| `HH-ABSTRACT` | Under explicit compact support, zero-order, staircase-count, norm, and anchor hypotheses, `HardHorizon.hard_horizon` bounds the finite zero horizon. | **PROVED** | Abstract Lean theorem with audit. `lean/glide/Glide/HardHorizon.lean`, last `C2`. Not a zeta theorem. |
| `HH-ZETA` | Apply the hard-horizon theorem to actual zeta near-minimizers. | **CONDITIONAL** | Requires explicit Riemann–von Mangoldt data and, critically, an unproved anchor for the selected test. |
| `HH-UNANCHORED` | A nonzero Paley–Wiener transform cannot vanish on an arbitrary prescribed finite zero head. | **REFUTED** | Explicit \(P\cdot\sinc^M\) construction in `results/experts/T1PRIME.md`. |
| `META-RH` | RH. | **OPEN** | No proof. |
| `META-NOT-RH` | A zeta zero off the critical line. | **OPEN** | No proof or rigorous witness. |
| `META-INDEPENDENCE` | RH is independent of ZFC. | **OPEN** | No forcing, inner-model, absoluteness, or proof-theoretic program is present. |

# 5. Dependency graph

## Formal Weil route

```text
WF-P2-MATRIX
      │
      ▼
WF-P2-CLIPPED
      │
      ▼
WF-P2-ORIGINAL
      │
      ▼
WF-P2-DOMAIN-BRIDGE + WF-ACTIVE-SET
      │
      ▼
WF-ENDPOINT
      │
      ├── [WF-CUTOFF-AXIOM]
      │          │
      │          ▼
      │   WF-BASE-INTERVAL
      │
      └── [WF-RELATIVE-STEP: OPEN]
                 │
                 ▼
      WF-PROP-EXISTS: OPEN
                 │
                 ▼
      WF-PROP-IMPL
                 │
                 ▼
      GlobalWeilPositivity
                 │
        [WEIL-CRITERION axiom]
                 │
                 ▼
                 RH
```

Important strength gaps:

- `WF-ENDPOINT` concerns one support only.
- `WF-BASE-INTERVAL` reaches only \(a\le7/16\) and is axiom-dependent.
- `WF-COFINAL` proves generic logic, not that the zeta form satisfies it.
- `positiveAt_of_relative_block_bounds` assumes target old/collar nonnegativity and a determinant inequality. Deriving those assumptions from the desired target positivity would be circular.
- The informal floor's spectral properties are stronger than what the endpoint theorem establishes.
- `WEIL-CRITERION` is itself an explicit formal axiom.

## Zero-side route

```text
GW-LOCAL + GW-RIGHT + transform infrastructure
              │
              ├── [GW-SMOOTH-ENTIRE axiom]
              ├── [GW-SMOOTH-FORMULA axiom]
              └── [GW-LOGDOMAIN axiom]
                         │
                         ▼
             arithmetic form = zero-side limit
```

Using an RH-conditional zero-side square or frame identity to establish positivity would be circular.

## Fixed-window route

```text
normalization-matched explicit formula
              │
              ▼
          FW-WIDTH
              │
      ┌───────┴────────┐
      ▼                ▼
FW-RH-CRITERION   FW-PRIME-STRIP
                       │
                       ▼
                 FW-COBOUNDARY
                       │
             FW-EULER + Vaughan identity
                       │
                       ▼
                  FW-VAUGHAN
                       │
                       ▼
             FW-FIXED-EXPONENT
                       │
             [aggregate estimate: OPEN]
```

Strength warnings:

- The reduction does not estimate the aggregate.
- Proving boundedness from the zero-side formula under RH is circular.
- A fixed power saving gives only a fixed strip.
- Bounded/polylogarithmic growth is needed for RH.
- `FW-MOVING-ORDER` is weaker than a fixed-transform detector because no changing-test converse exists.

## R176 route

```text
hypothetical target zero
         │
         ▼
complete-circle Hardy mode
         │
right-tail smallness on E
         │
         ▼
R176-HARMONIC
         │
         ▼
forced large complementary boundary C
         │
         ├── generic Carleman improvement: REFUTED
         ├── target-preserving H^q reflection: REFUTED
         └── R176-LOGMEAN: OPEN
                       │
                       ▼
             fixed zero-free strip
```

The present deductions force complementary growth; they do not control it. A fixed strip is strictly weaker than RH.

# 6. Analytic audit

## Lean \(p=2\) endpoint

### Analytic continuation, contours, and residues

None are used in `WF-ENDPOINT`. It is a real Fourier-multiplier and finite-autocorrelation theorem. The unconditional endpoint does not use zeta zeros, contour shifting, or residues.

### Sums, integrals, derivatives, and limits

- The digamma/Gauss-series interchange is performed using absolute summability and an integral-of-sum theorem in Lean.
- Directed digamma tails use exact integral-test inequalities.
- Compact support gives the \(L^1\)/\(L^2\) hypotheses needed to identify pointwise and unitary Fourier transforms.
- Translation laws and autocorrelation use \(L^2\) Plancherel with explicit integrability.
- Multiplier integral splits in `ZetaWeilForm.lean` carry explicit `Integrable` hypotheses.
- The active prime sum is finite, so no infinite prime-sum interchange occurs.

These uses are justified in Lean source, subject to fresh rebuild verification.

### Fourier normalization

- Ordinary frequency uses \(e^{-2\pi i\xi x}\).
- Angular frequency is \(r=2\pi\xi\).
- The band change of variables and \(1/(2\pi)\) factor are proved.
- The cosine/autocorrelation identity is proved.
- No pointwise inversion is required.

### Positivity and spectral claims

Justified:

- real/Hermitian bounded defect multiplier;
- exact Legendre parity;
- orthogonal projection;
- finite-block positivity;
- complement floor;
- cross control;
- clipped-to-original pointwise comparison.

Not established in the endpoint chain:

- closability or closedness of an associated unbounded operator;
- self-adjoint operator construction;
- compact resolvent;
- eigenvalue attainment;
- density of the logarithmic domain.

The endpoint is a quadratic-form inequality and should be stated only as such.

### Numerical truncation and rounding

The formal certificate includes rational bounds for:

- 32 half-band panels;
- defect expansion prefix order 32;
- stored component expansions;
- omitted tails;
- product and integration errors;
- pole Taylor errors;
- \(1/(2\pi)\) and \(\alpha\) approximation;
- final center rounding;
- all generated matrix refinements.

The generator may have used numerical search, but floating-point output is not a theorem premise. The source and focused audits are present; they were not rerun during recovery.

## Guinand–Weil chain

### Justified in Lean source

- meromorphic continuation of zeta through mathlib;
- isolation and multiplicity of nontrivial zeros;
- local factorization and logarithmic-derivative principal parts;
- absolute von Mangoldt Dirichlet series on \(\Re s>1\);
- completed-zeta Gamma and reflected identities;
- weighted Fourier/Laplace \(L^1\) and \(L^2\) facts;
- cross Plancherel;
- two-integration-by-parts decay for globally \(C^2\) zero extensions;
- finite disk zero exhaustion as a definition.

### Still axiomatic

The following are not proved:

- the global contour deformation;
- the full residue sum;
- horizontal-edge vanishing;
- passage from finite rectangles to the complete zero sum;
- low-regularity closure to the logarithmic form domain.

They are packaged by precisely two axioms in `GuinandWeilLiterature.lean`:
the normalization-matched smooth formula and its logarithmic-domain closure.
The former Paley--Wiener entirety axiom is now a theorem using the standalone
compact-support Fourier--Laplace library.

Additional seams if those axioms were to be removed:

- quotient-level and representative-level bilateral transforms are not fully identified;
- weighted decay lemmas are not assembled into the complete contour-decay theorem;
- rectangle exhaustion and residue convergence are absent.

### Branch choices

The formal contour work uses \(\zeta'/\zeta\), not an analytic branch of \(\log\zeta\). Complex powers with positive-real bases use the canonical principal logarithm. Disk exhaustion is explicit.

## Fixed-window and Type-II manuscript

### Explicit formula and zero sum

The piecewise-linear triangular test uses a normalization-sensitive low-regularity Guinand–Weil formula imported from the literature.

The manuscript argues:

\[
|H_\ell(z_\rho)|\ll_\ell(1+|\Im\rho|^2)^{-1},
\]

uniformly in the critical strip, and combines this with Riemann–von Mangoldt counting to obtain absolute summability.

This appears sufficient for fixed \(R\), but has not been formalized or independently refereed.

### Laplace continuation and residues

Termwise one-sided Laplace integration is first taken where \(\Im z>1/2\). The resulting normally convergent meromorphic sum has a genuine pole at each nonreal node because the sinc zeros are real.

A smaller exponential growth rate would make the Laplace transform holomorphic across such a node, contradicting meromorphic uniqueness.

This is a plausible argument, but its normal-convergence and continuation details require independent checking.

### Prime stripping

The square-prime term uses PNT/partial summation. The sharpened \(e^{-c\sqrt R}\) estimate uses a classical zero-free-region PNT error. Uniformity is only for fixed \(\ell\). Exact theorem citations and normalization-compatible constants are not fully frozen.

### Euler/B-spline step

The proof uses:

- finite sum/average interchange;
- periodic Euler summation;
- analytic continuation of an explicitly displayed remainder;
- distributional integration by parts;
- total variation of B-spline derivatives;
- Cauchy estimates for differentiation in the exponent parameter.

Positive bases eliminate branch ambiguity.

Outstanding checks:

- periodic \(B_1\) endpoint convention;
- all distributional boundary terms;
- the claimed total-variation bound;
- uniformity on nested compact subsets;
- the \(\exp(O_\ell(k\log k))\) growing-order constant.

### Vaughan step

For each fixed \(x\), cutoffs make the convolution rearrangements finite, so no hidden Fubini issue remains. The fixed-order conclusion is nevertheless conditional on the Euler lemma.

### Mellin continuation and pole orders

Fixed-cutoff Dirichlet-series identities begin on \(\Re s>1\) and are continued algebraically with zeta factors. This is standard but manuscript-only. Pole-order arguments for frozen cofactors require the stated nonvanishing of the finite Dirichlet polynomial at a selected zero.

### Numerical diagnostics

The fixed-box script uses ordinary floating-point evaluation and a truncated list of 100 critical-line zero pairs. The residual is not rigorously bounded and is diagnostic only.

## R176 contour branch

### Hardy mode

The Taylor/Parseval argument is justified when \(B\) is meromorphic on a neighborhood of the closed disc and has one simple pole.

The claim that polynomials can cancel the pole on any proper arc is standard approximation theory but is not cited; it is not needed for the harmonic-measure inequality.

### Harmonic measure

The inequality follows from subharmonicity of

\[
\log|(s-\rho)B(s)|
\]

and Jensen on the two boundary pieces.

Boundary zeros require an \(\varepsilon\)-regularization or standard logarithmic-integrability argument; the neighborhood-holomorphic hypothesis supplies it, though the text does not spell it out.

### Carleman and outer functions

A general Jordan curve need not be rectifiable. The contour-integral formulation must assume rectifiable or piecewise-\(C^1\) boundary.

Outer-function sharpness is valid in the Hardy/harmonic-measure class. The manuscript’s claim of sharpness while retaining holomorphic extension to a neighborhood of the entire closed boundary needs an additional smoothing/approximation argument.

The nonlinear local representation also needs bounded extension to a neighborhood of the compact closure so one inverse chart suffices.

### Head-deleted zeta tail

On a fixed right arc \(\Re s\ge1+a_R\), absolute Euler convergence justifies:

- the finite-head product;
- termwise logarithm and differentiation;
- \(H^{-a_R}\) and \(H^{-a_R}\log H\) bounds;
- one-sign Dirichlet coefficients;
- support beyond \(H^q\).

These estimates are for fixed \(a_R\) and fixed domain geometry.

### Residue calculation

At a zero of multiplicity \(m\),

\[
(1-F_H)^{q-1}=1,
\]

so \(B_{q,H}\) has residue \(m\). This is justified.

### Reflection

The functional-equation identity is algebraic. At the target, the nonlinear reflected term is analytic; the pole remains in the linear \(-F_H'/F_H\) term.

The reflected finite-head growth uses PNT at fixed points. Uniformity for moving contours has not been proved.

### Surviving open estimate

Equation (7.2) is under-specified. To imply a uniform fixed strip, the theorem must quantify uniformly over all hypothetical zeros in the excluded region and control:

- \(c\);
- \(a_R\);
- \(D,E,C\);
- \(\omega\);
- isolation radius;
- \(q,H\);
- connector geometry;
- boundary zeta and Euler-factor bounds.

A proof importing a zero-free strip or an equivalent coefficient estimate would be circular.

# 7. Strongest surviving result

The strongest unconditional result about the intended arithmetic form is:

```text
RHP2Bridge.GeneralZetaWeilForm
  .weilForm_seven_sixteenths_strict_lower_bound
```

For every real interval vector \(f\) with \(f\ne0\) and

\[
\int_{\mathbb R}
 \log(1+(2\pi\xi)^2)|\widehat f(\xi)|^2\,d\xi<\infty,
\]

Lean source proves

\[
\frac{22699}{10^9}\|f\|^2
<
Q_{7/16}(f).
\]

This is stronger than finite Galerkin positivity because the complement and cross terms are controlled. It is weaker than RH because:

- it concerns one support;
- it is arithmetic-side only;
- no all-support propagation exists;
- the zero-side equality and RH criterion remain explicit literature axioms.

The proof source and focused audit are committed at `C4`; the recovery did not rerun them.

The theorem for every \(0\le a\le7/16\) is not the strongest unconditional result because it depends on `WF-CUTOFF-AXIOM`.

The farther \(p=3\) and \(n=4\) endpoints have larger support but weaker trust status.

# 8. Known failures and objections

## Uniform-support failures

- **Two-sliver obstruction:** entering translations do not become small in operator norm near activation.
- **No activation-symbol floor:** the defect symbol vanishes at zero frequency.
- **Additive glide insufficiency:** \(C/\log(1/h)\) cannot preserve arbitrarily small margins.
- **Uniform normalized floor:** the original support-independent floor proposal is unnecessarily strong and unsupported.
- **Sharp projection domain:** old/collar decomposition is not yet known to preserve the logarithmic form domain.
- **Circular block assumptions:** target block positivity cannot be assumed to prove target positivity.

## Finite-certificate objections

- Positive Galerkin eigenvalues alone give no full-space lower bound.
- Exact finite matrix positivity says nothing about its analytic interpretation unless containment is proved.
- The \(p=3\) and \(n=4\) containment bridges remain outside Lean.
- Additional isolated windows do not establish arbitrary support.

## Zero-side objections

- The complete Guinand–Weil formula is axiomatized.
- The Weil criterion is axiomatized.
- An RH-conditional zero frame cannot prove RH.
- A zero-side regression oracle cannot reject a negative arithmetic witness.

## Fixed-window/Type-II failures

- Fixed cofactor blocks increase zero-pole order.
- Separating Euler bulk and boundary destroys cancellation.
- Fixed-rank or coefficient-blind ambient norms do not contract sufficiently.
- Local reflection reinforces rather than cancels a central divisor collar.
- The natural exterior \(2\times2\) square changes sign.
- Moving smoothing order has no reverse fixed-transform theorem.
- A fixed power saving yields only a strip.
- Boundedness proved from the zero-side formula would be circular.

## R176 failures and objections

- Complete-circle Hardy information cannot be read from a proper arc without paying harmonic measure on the complement.
- Generic Carleman weights do not improve that exponent.
- Outer functions attain the abstract tradeoff.
- Functional-equation reflection retains the target only in the linear \(H\)-supported channel.
- The dilated-zeta model shows that positivity, late support, meromorphy, and a generic functional equation are insufficient.
- The Carleman statement needs rectifiable boundary.
- Exact outer sharpness in the neighborhood-meromorphic class needs an approximation lemma.
- Equation (7.2) lacks complete uniform quantifiers.

## Historical withdrawals

- The corner-kink mechanism was not supported.
- Threshold-distance power-law interpretations were withdrawn.
- Density-only “Poisson cost” and maximal-rigidity conclusions were withdrawn after correcting model-zero phase/cutoff coverage.
- The unanchored hard-horizon claim was refuted.
- “Keyhole novelty” was withdrawn after locating prior work.
- Numerical envelope constants and stopping-height laws remain diagnostics.
- A claimed growing-order RH equivalence is invalid without a varying-test converse.

## Canonical no-go registry

`NO-GO-ATLAS.md` records NG-01 through NG-46. Each card eliminates only its printed candidate class. Chain-critical examples include:

- NG-07: generic Schur hypotheses do not force the required sign;
- NG-16: a fixed support-independent shift is already RH-strength;
- NG-20: pointwise symbol positivity cannot replace compressed positivity;
- NG-21: packet diagonals do not control coherent cross terms;
- NG-22–NG-31: Ward, fixed-block, reciprocity, and coefficient-blind Type-II shortcuts fail;
- NG-46: standard quasi-RH bootstrap machinery returns the same exponent rather than improving it.

The full atlas, reduction registry, and proxy ledger are the authoritative scope records. Their countermodels do not prove that every use of the corresponding mathematical subject is impossible.

# 9. Interrupted state

## Last completed repository action

At 2026-08-08 19:59:12 -0700, commit

```text
06a3fe3cac6e0b3f51b1865a01dde60dc30f2f4a
Progress checkpoint
```

was created.

At 19:59:15, the `origin/master` reflog records `update by push`. The requested commit-and-push therefore completed.

That commit changed 226 files with 103,822 insertions and 22 deletions:

- 148 Markdown files;
- 77 Python files;
- one empty extensionless file `1`;
- no Lean files.

It was a checkpoint of research reports, probes, and tests rather than a formal-proof modification.

The latest mathematical report completed in it was R176: the abstract Hardy/Carleman route was closed and the coefficient-specific complementary-log-mean estimate was isolated.

## Exact conversation-level action underway at the pause

The inherited conversation had just pivoted from further numerical windows to a uniform-in-\(L\) mechanism.

The work underway was:

1. formulate cofinal finite-product propagation;
2. formulate an old/collar Schur step;
3. identify the missing zeta-specific relative estimate;
4. begin an abstract Lean `UniformSupport` layer.

The user then asked the assistant to pause for a commit and push.

Later Git history shows that the abstract finite-product and Schur wrappers were completed at `C2`. The analytic zeta-specific relative step was not.

## Running or incomplete commands

Point-in-time process audit found:

- no Lean process;
- no Lake build;
- no pytest run;
- no certificate generator;
- no Arb/full-infimum computation;
- no repository numerical probe.

No Git operation markers exist: no merge, rebase, cherry-pick, revert, bisect, or index lock.

A Jupyter server and kernel are running for another project, not this repository.

A historical tracked log, `results/ias/log-gas/separator_test.log`, contains an assertion failure followed by later corrected output; `separator_verify.log` records a later verification. This is preserved history, not a current interruption.

The \(n=4\) JSONL checkpoint contains one metadata record plus all 4,422 expected matrix-entry records and appears complete.

## Uncommitted work

- Staged tracked changes: none.
- Unstaged tracked changes: none.
- Untracked: `error.log` only.

`error.log` is a 438-byte Codex/ChatGPT startup/authentication log created about nine minutes after the push. It contains a private account identifier and no mathematical output. It should not be committed as-is.

## Conversation-only information

The inherited conversation records constraints not encoded reliably in source:

- prioritize provable Lean theorems over numerical results;
- numerical computation may generate certificates, but Lean should verify analytic error bounds;
- do not expand to additional windows until the uniform theorem closes or is reduced to a demonstrably minimal missing lemma;
- do not contact professors or otherwise communicate externally;
- a uniform positive factor is not required—strictly positive finite-step factors suffice;
- the user explicitly requested a pause before the checkpoint.

# 10. Verification plan

These checks are proposed only; none was run during recovery.

1. **Reproduce the exact Lean trust boundary.**  
   Serially compile the focused \(p=2\), general-form, base-interval, Guinand–Weil-literature, and Weil-criterion audits. Record their exact `#print axioms` output. This can validate the unconditional endpoint and expose the cutoff/formula/criterion axioms without building the umbrella project.

2. **Falsify the first proposed zeta relative step before implementing it.**  
   Freeze a one-threshold theorem statement with exact form domain, old/collar maps, margins, and cross normalization. Test it symbolically against the two-sliver family and low-frequency activation-symbol zero. Reject any version whose hypotheses already imply target positivity or whose sharp pieces leave the logarithmic domain.

3. **Freeze and audit the R176 quantifiers.**  
   Restate equation (7.2) for a precise smooth target-isolating contour family with constants uniform over all hypothetical zeros in a proposed strip. Check whether the claimed lower/upper contradiction survives degeneration of harmonic measure, zero-isolation radius, connectors, and reflected head growth. If no uniform theorem card can be written, retire the route before any large computation.

# 11. Repository changes

## Git state

```text
branch:          master
HEAD:            06a3fe3cac6e0b3f51b1865a01dde60dc30f2f4a
upstream:        origin/master
ahead/behind:    +0 / -0
staged changes:  none
unstaged tracked changes: none
untracked:       error.log
stashes:         none
```

There is exactly one worktree:

```text
/home/ubuntu/Projects/Riemann-Zeta
```

It is attached to `refs/heads/master` at `06a3fe3…`.

There are:

- no other local branches;
- no tags;
- no submodules;
- no Git operation in progress.

The empty tracked file `1` was added at HEAD and has no identified mathematical role. It is likely an accidental shell-output artifact but has not been modified or removed.

## Recent history

```text
06a3fe3  2026-08-08  Progress checkpoint
7ec0ef8  2026-08-06  Significant progress, far short of RH
e986985  2026-08-05  Exposit formal RH results and proof boundaries
14b273d  2026-08-05  Consolidate RH obstruction results and harden formal artifacts
b9a0574  2026-08-03  Consolidate RH research and reusable Lean infrastructure
96a3d99  2026-07-30  Formalize the zeta prime autocorrelation bridge
d2d4e07  2026-07-30  Formalize the p=2 full-infimum certificate and RHBridge composition
```

## Toolchain

The `rhbridge` package pins:

```text
Lean 4.32.1
mathlib revision 520045ab14e26149ee970e2e617ca04b09bde5d6
```

The package depends locally on `glide` and `weilcert`.

## Notebooks, scripts, logs, and generated artifacts

No tracked or unignored `.ipynb`, `.nb`, `.sage`, or `.jl` notebook exists.

Tracked inventory includes approximately:

- 5,652 total files;
- 4,914 Lean files;
- 323 Markdown files;
- 224 Python files;
- 9 shell scripts;
- 153 tracked log/output/data artifacts in the audited extensions.

The certificate layer is heavily generated:

- 4,628 tracked Lean files match `P2Rounded*`;
- 544 match `P2RoundedFactorCheckpointCheck*`.

Important computational artifacts include:

- `src/fullinf_unrestricted_certificate.py`;
- `src/fullinf_unrestricted_p3_certificate.py`;
- `src/fullinf_unrestricted_n4_certificate.py`;
- `results/fullinf_n4_M132_S110_entries.jsonl`;
- fixed-box scripts and tests;
- numerous falsification probes associated with the no-go reports.

The \(n=4\) JSONL artifact is 811,883 bytes and includes a source-kernel SHA-256 fingerprint, precision metadata, and all expected entries.

Ignored local build/cache state includes approximately:

- `lean/rhbridge/.lake`: 35 GB;
- `lean/weilcert/.lake`: 7.7 GB;
- `lean/glide/.lake`: 7.5 GB;
- `lean/p2-kernel-check-state`: 2.1 GB;
- Python caches and pytest caches.

These caches predate HEAD and are not evidence of a fresh successful build.

No `RECOVERY_STATE.md` currently exists in the repository.

---

This remains a proposed report only; it has not been written to disk.
