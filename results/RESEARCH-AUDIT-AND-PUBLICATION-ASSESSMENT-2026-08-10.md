# Research audit and publication assessment

**Date:** 2026-08-10
**Scope:** the recovered analytic, computational, and Lean work product in this
repository, with emphasis on a uniform zero-free strip and the Riemann
Hypothesis (RH).
**Verdict:** no proof or disproof of a uniform fixed zero-free strip, and no
proof or disproof of RH, is present. Several independent results are real and
potentially publishable, but they must be separated from the open RH-strength
premises.

## 1. Executive assessment

The work product is much better than a pile of numerical experiments, but much
less than a route that currently closes a zero-free strip. Its strongest parts
fall into four different categories.

1. **A rigorous local arithmetic-form theorem.** At support
   `a = 7/16` (the repository's `L = 4a = 7/4` convention), the Lean source
   proves on the full logarithmic Fourier form domain that

   ```text
   (22699 / 10^9) ||f||^2 < Q_(7/16)(f)       for every nonzero f.
   ```

   This is infinite-dimensional, not a Galerkin observation. It is local in
   support and is a statement about the arithmetic pole--archimedean--prime
   form, not a newly formalized proof of the complete zero-side explicit
   formula. See
   [GeneralZetaWeilForm.lean](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean)
   and the current
   [mathematical overview](../publication/MATHEMATICAL-OVERVIEW.md).

2. **Correct abstract propagation algebra, but no propagation theorem for
   zeta.** The old/collar decomposition, Schur algebra, and finite-product
   induction are sound. No inhabitant of `PropagationPackage` exists. The
   missing relative old/collar estimate is not a technical afterthought: in
   its all-vector form it is equivalent to positivity of the enlarged mixed
   block. See
   [UniformPropagationToRH.lean](../lean/rhbridge/RHBridge/UniformPropagationToRH.lean),
   [RelativeCrossNecessity.lean](../lean/rhbridge/RHBridge/RelativeCrossNecessity.lean),
   and [UNIFORM-L-MECHANISM.md](UNIFORM-L-MECHANISM.md).

3. **Two clean analytic reductions.** Independent hostile review found the
   fixed-box width spectrometer mathematically sound under the classical
   Guinand--Weil formula: one fixed
   triangular prime discrepancy detects the exact horizontal width of the
   zeta divisor. The R176 contour work also gives a useful sharp obstruction,
   but its coefficient-specific `log^+` premise remains open. These are
   detectors/reductions, not engines that supply a new bound.

4. **A likely genuine correction to an external preprint.** The phase coupling
   in Endo's hybrid joint limit law needs a coordinate conjugation. A one-prime
   moment separates the printed and corrected laws. This is the clearest
   high-confidence novelty in the repository, although it is unrelated to RH
   and should first be handled as an author-coordinated correction.

The most important research conclusion is therefore negative but precise:

> The repository has successfully compressed the RH-strength gap. It has not
> crossed it. The surviving gap is a noncircular, non-Zeno, zeta-specific
> relative estimate for the combined pole--archimedean--prime form, or an
> independent arithmetic power saving for one of the exact width detectors.

## 2. Claim matrix

| Claim | Audit verdict | Evidence class | Publication status |
|---|---|---|---|
| RH or its negation | **Not proved** | No constructed global package; final Lean arrow also uses an explicit literature axiom | Must not be claimed |
| A fixed uniform zero-free strip | **Not proved** | No coefficient power saving or uniform support estimate | Must not be claimed |
| Full-domain positivity at `a=7/16` | **Substantive local theorem** | Lean source plus exact certificate architecture; p=2 Arb inputs freshly regenerated; serialized rebuild and audit gates passed on 2026-08-11 | Strong formal/computer-assisted paper candidate after an archival generator manifest, independent reproduction, and review |
| Positivity at `a <= 7/16` | **Conditionally packaged** | Uses an explicit standard support-autocorrelation axiom in the present Lean path | Prove the small support lemma before advertising as fully kernel-closed |
| Software full-space bounds at `L=497/200` and `L=749/250` | **Credible computer-assisted results** | Arb/analytic transfer; n=4 was replayed from cached balls in this audit | Supporting case studies, not separate RH results |
| Positive finite-window Galerkin spectra at larger `L` | **Correct as finite matrices** | Fresh interval computations | Numerical evidence only; cannot prove full-space positivity |
| Abstract finite-product propagation | **Proved, elementary, useful** | Lean, standard logical axioms only | Infrastructure, not standalone RH progress |
| Old/collar Schur propagation | **Valid implication; decisive premise open** | Lean block identity and scalar algebra | Publish only as part of a larger analytic result |
| Fixed-box exact-width identity | **Sound under its listed classical inputs; not Lean-formalized** | Classical explicit formula, absolute zero sum, Laplace pole argument | Potential short note; priority/novelty search still required |
| R176 Hardy/Carleman branch | **Sharp obstruction; target open** | Classical harmonic measure plus coefficient-specific reduction | Possible synthesis/no-go note after compression and review |
| Hard Horizon theorem | **Technically substantive but classical in mechanism** | Lean Jensen/Paley--Wiener package with an essential anchor hypothesis | Modest analysis/formalization note after specialist review |
| Endo hybrid-limit correction | **High-confidence correction** | Direct phase calculation and one-prime moment witness | Highest-priority communication/publication item; not an RH result |
| Reusable Lean analysis libraries | **Genuine formalization work** | Focused audits of `glide`, `weilcert`, and reusable `rhbridge` endpoints | Upstreamable in small coordinated units |

## 3. What is actually formalized

### 3.1 The local arithmetic Weil form

The repository defines

```text
Q_a(f) = pole_a(f) + arch_a(f) - prime_a(f)
```

on the natural domain

```text
integral log(1 + (2*pi*xi)^2) |fHat(xi)|^2 dxi < infinity.
```

At `a=7/16`, Lean proves that the only active prime power is `2`, identifies
the general arithmetic form with the previously certified p=2 form, and
transfers the strict constant `22699/10^9`; see
[the specialization and endpoint](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean#L338-L367).
This closes an older arithmetic form/domain-identification gap. It does **not**
close the classical global contour argument identifying the form with the
symmetric zero-side limit; that boundary remains explicit in
[GuinandWeilLiterature.lean](../lean/rhbridge/RHBridge/GuinandWeilLiterature.lean).

The exact distinction is:

```text
kernel-facing local theorem:
    Q_(7/16)(f) > 0 on its full intrinsic form domain

accepted classical bridge:
    Q_a equals the symmetric Guinand--Weil zero-side limit

RH-strength missing statement:
    Q_a(f) >= 0 for every a > 0 and every admissible f.
```

### 3.2 The conditional RH chain

The formal chain is honest:

```text
constructed PropagationPackage
    -> positivity at every support
    -> global Weil positivity
    -> RH through an explicit literature axiom.
```

The first object is not constructed. `PropagationPackage` itself assumes a
cofinal scale, initial positivity, and every adjacent-support propagation step;
see
[UniformPropagationToRH.lean](../lean/rhbridge/RHBridge/UniformPropagationToRH.lean#L47-L56).
The final arrow uses
`WeilCriterionLiterature.riemannHypothesis_iff_globalWeilPositivity`, which is
declared as an axiom in
[WeilCriterionLiterature.lean](../lean/rhbridge/RHBridge/WeilCriterionLiterature.lean).

Fresh focused axiom output found only `propext`, `Classical.choice`, and
`Quot.sound` for the abstract block and finite-product results. The RH endpoint
additionally reported the named Weil-criterion axiom. There are no actual
`sorry` or `admit` proof holes in the Lean source. There are 42 explicit
`axiom`/`opaque` declarations in `rhbridge`; the material ones include the
Guinand--Weil bridge, the Weil criterion, standard support-autocorrelation
facts, and several deliberately speculative Stage/Suzuki interfaces.

## 4. The uniform-support program: what survives the audit

### 4.1 A valid simplification

The repository correctly observed that adjacent step factors need only be
strictly positive one at a time. For a fixed finite target support, only a
finite product is used. There is no need for a uniform lower bound on the
factors or a positive infinite product. This is proved abstractly in
[UniformSupportTransfer.lean](../lean/rhbridge/RHBridge/UniformSupportTransfer.lean#L224-L262).

This removes an unnecessarily strong earlier target. It does not produce any
step factor.

### 4.2 The sharp-projection domain caveat is removable

One genuinely new consolidation insight is that the hard old/collar cutoff
should preserve the logarithmic form domain.

Let

```text
W(xi) = 1 + log(1 + (2*pi*xi)^2).
```

The weight is comparable to `log(e+|xi|)` and is an `A_2` Muckenhoupt weight.
On intervals far from zero, its maximum and minimum are uniformly comparable;
on intervals reaching the origin, the estimate
`integral_0^R W(t)^(-1) dt <= C R/W(R)` (split at `sqrt(R)`) gives a
uniform bound for the product of the averages of `W` and `W^-1`.
Multiplication by a half-line indicator in physical space is Fourier-conjugate
to a Hardy projection `(I +/- iH)/2`. The Hilbert transform is bounded on
`L^2(W)` for `A_2` weights; interval cutoffs are differences of translated
half-line cutoffs, and the resulting frequency modulations preserve the
weighted norm. Therefore multiplication by `1_[c,d]` is bounded in the graph
norm of the logarithmic form domain.

This removes the domain-preservation concern in
[SmoothSupportPropagation.lean](../lean/rhbridge/RHBridge/SmoothSupportPropagation.lean)
and lines 116--122 of [UNIFORM-L-MECHANISM.md](UNIFORM-L-MECHANISM.md).
It does **not** make the Weil form bounded on plain `L^2`, produce an `L^2`
cross estimate, or prove positivity. A publishable implementation should first
write a complete scalar `A_2` proof for this exact weight and then formalize an
a.e.-defined interval multiplier. The general weighted Hilbert-transform input
is classical; see
[Hunt--Muckenhoupt--Wheeden](https://doi.org/10.1090/S0002-9947-1973-0312139-8)
or the modern sharp-bound treatment of
[Lacey--Petermichl--Reguera](https://arxiv.org/abs/0906.1941).

A related Lean issue is real: `BoundaryCollarGeometry` currently uses literal
`Function.support`, which is not invariant under equality almost everywhere in
an `L^2` class. It should use an a.e.-support predicate; see
[BoundaryCollarGeometry.lean](../lean/rhbridge/RHBridge/BoundaryCollarGeometry.lean#L21-L39).

### 4.3 The all-vector Schur target is not an independent engine

For nonnegative diagonal energies `A` and `D`,

```text
C^2 <= A*D
```

is equivalent to nonnegativity of `A + 2tC + t^2D` for every real `t`. The
repository itself formalizes this in
[RelativeCrossNecessity.lean](../lean/rhbridge/RHBridge/RelativeCrossNecessity.lean#L25-L66).
Consequently, asking for the exact relative cross inequality for every old and
collar vector is simply asking for positivity on every corresponding mixed
plane. It is a useful coordinate system for the problem, not a weaker theorem.

The existential `EventCollarCertificate` is even less informative unless its
split is fixed independently: if positivity at the new support were already
known, one could take old part zero and collar part equal to the whole vector.
See
[EventCollarPropagation.lean](../lean/rhbridge/RHBridge/EventCollarPropagation.lean#L23-L49).

A noncircular theorem card must therefore specify one of the following before
any further coding:

- a canonical old/collar split and an independently positive comparison
  functional `E_collar`, with `E_collar <= Q(collar)` and
  `|cross|^2 <= Q(old) E_collar`;
- a factorization of the cross operator through square roots of independently
  controlled positive forms, with contraction norm strictly below one;
- a low-energy old spectral sector where zeta-specific cancellation supplies
  the relative factor, with ordinary coercivity treating its complement;
- an Euler--Lagrange/minimizer rigidity theorem instead of an all-vector
  inequality.

Without one of those, the Schur formulation repackages the target positivity.
There are also two formal interfaces to repair before using it analytically:
`weilCross` is presently polarization rather than a separately proved
continuous bilinear form, and `SupportDecomposition` is stated on `TestSpace`
while the genuine unbounded form lives on the logarithmic subdomain. Exact old
support consistency is supplied only in the later activation-cancellation
layer.

### 4.4 Cofinality is a separate, easily hidden premise

Local openness of positivity does not automatically yield supports tending to
infinity. Adaptive step sizes can form a Zeno sequence whose sum stops at a
finite first-crossing point. The Lean `PropagationPackage` correctly includes
an explicit `cover` field, but any analytic construction must prove it rather
than infer it from continuity. A locally integrable relative-loss bound would
prevent this; bare continuity would not.

The corrected surviving target is thus:

> Construct a canonical, form-domain-safe decomposition and prove a
> zeta-specific relative estimate on a cofinal non-Zeno sequence, preferably
> first on the low-energy/minimizing sector.

The two-sliver family in [UNIFORM-L-MECHANISM.md](UNIFORM-L-MECHANISM.md#L124-L153)
rules out obtaining that estimate from a small `L^2` operator norm of each
newly entering translation.

## 5. A clearer fixed-strip research ladder

The existing documents sometimes move too quickly between a fixed strip and
RH. The fixed-box theorem supplies a clean quantitative ladder.

Put

```text
Delta = sup_rho |Re(rho) - 1/2|.
```

For each fixed `ell>0`, the repository's triangular discrepancy satisfies

```text
limsup_(R->infinity) log(1+|D_ell(R)|)/R = Delta.
```

The proof in
[FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md](FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md)
uses an absolutely summable zero expansion and a one-sided Laplace transform.
Because the sinc-squared coefficient has no nonreal zeros, every off-line zero
creates a genuine pole, so cancellation cannot lower the exponential type.
Independent hostile review checked the convergence, the sign and domain of the
Laplace transform, multiplicities and residues, and the prime-side
normalization without finding a mathematical error.
For a conventional paper proof, make explicit that a strict limsup bound gives
an eventual exponential majorant and hence a holomorphic Laplace transform on
the half-plane crossing the selected pole.

This gives three sharply different goals:

| Arithmetic bound | Zero consequence |
|---|---|
| Classical zero-free-region savings that vanish with height | No fixed-width improvement |
| `D_ell(R) = O(exp(theta R))` for one fixed `theta < 1/2` | A genuine fixed strip, with `Re rho <= 1/2 + theta < 1` |
| `D_ell(R) = exp(o(R))` | `Delta=0`, hence RH |

Equivalently, a fixed saving `kappa>0` from the trivial exponent `1/2`
already matters: `theta=1/2-kappa` yields `Re rho <= 1-kappa`. One should not
ask a first arithmetic engine for subexponential growth when a fixed power
saving would already establish the nearer stated goal.

The theorem is a detector, not an engine. Deriving its bound from the zero-side
formula is circular. Its likely novelty is modest: the mechanism is a clean
fixed-kernel version of classical explicit-formula/Mellin-transform converse
arguments for prime-number-theorem errors. Smooth weighted PNT errors have
also recently been related quantitatively in both directions to zero-free
regions; compare
[Han, *The Error in a Smooth Weighted Prime Number Formula and Zero-free
Regions for the Riemann Zeta Function*](https://arxiv.org/abs/2505.23795).
A specialist priority search is required before claiming the exact
fixed-triangle formulation is new. Relevant classical baselines include
[Guinand's explicit formula](https://doi.org/10.1112/plms/s2-50.2.107),
[Weil's 1952 paper](https://cds.cern.ch/record/471308), and the standard
PNT-error oscillation method summarized in
[Montgomery--Vaughan, Chapter 15](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/19.0_pp_463_485_Oscillations_of_error_terms.pdf).

## 6. R176 and the negative-results corpus

The R176 branch successfully closes a generic one-sided contour escape using
Hardy/Carleman and harmonic measure. The resulting interpolation exponent is
sharp, including outer-function extremizers. Applied to the head-deleted zeta
tail, the surviving premise is a coefficient-specific bound for the
complementary harmonic `log^+` mean; see
[R176-HARDY-MODE-CARLEMAN-AND-ONE-SIDED-CONTOUR-GATE.md](R176-HARDY-MODE-CARLEMAN-AND-ONE-SIDED-CONTOUR-GATE.md).
That premise is open and would at most yield the stated fixed strip, not RH.

The many no-go reports are valuable when treated as one obstruction atlas, not
as dozens of theorem announcements. Their common lesson can be stated as a
three-part test:

1. **Carrier:** does the observable change if one remote off-critical quartet
   is inserted?
2. **Topology:** does the all-prime/all-height limiting process preserve that
   carrier?
3. **Engine:** does arithmetic information independent of the zeros force the
   carrier to have its RH-compatible value?

Most abandoned routes possess at most two. Finite Euler models often lose the
carrier under completion; trace identities supply equality but no order;
finite positive windows do not prevent a negative mode from escaping to later
support. This synthesis is more publishable than the raw chronological ledger.

## 7. The Endo correction

Endo's version-1 empirical law records

```text
(phi(s+i*tau), (p^(i*tau))_p),
```

while the Dirichlet coefficient `n^(-s-i*tau)` contains negative powers of
those recorded phases. The Haar limit is therefore

```text
(phi(s, conjugate(omega)), omega_P),
```

or equivalently `(phi(s,omega), conjugate(omega_P))`, not the printed
same-phase coupling. A decisive witness at a recorded prime is

```text
E[omega(p) phi_X(s,conjugate(omega))]
    = a_phi(p) lambda(p/X) p^(-s),

E[omega(p) phi_X(s,omega)] = 0.
```

See the complete local note
[ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md](ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md).
The current arXiv record still lists only version 1, and the paper's definitions
indeed pair empirical `p^(i tau)` coordinates with a random Euler product using
positive powers of `omega`; see
[Endo's arXiv record](https://arxiv.org/abs/2410.17575) and
[the HTML source](https://arxiv.org/html/2410.17575v1).

The marginal law, full product support, and qualitative universality
corollaries survive after conjugating the finite coordinates. The local note
also supplies a compact-open repair for a separate higher-Euler-term estimate
at the boundary `sigma_phi=1/2`.

**Assessment:** high confidence and likely genuinely useful. It should first be
sent privately to the author with a minimal proof and page-level patch, then
handled as a coordinated revised version or short correction. No external
contact was made in this audit.

## 8. Computational and formal reproducibility audit

### 8.1 What was freshly reproduced

- `python3 -m pytest -q`: **374 passed**.
- `certified_margins.py`: four finite mpmath interval enclosures regenerated
  successfully.
- `certified_spectral.py`: the `10^-10`, `10^-15`, and `10^-20` finite spectral
  enclosures regenerated successfully.
- `fullinf_unrestricted_certificate.py`: all **600** p=2 Arb integrals were
  recomputed from first principles in about 189 seconds. The run re-established
  the clipped `48`-mode bound, leakage and cross constants, shifted determinant,
  and the full-space bound `Q_(7/4) > 2.2699e-5 I`.
- The n=4 run loaded **4,422/4,422 cached Arb balls**, verified the documented
  checkpoint SHA-256, and reran the 50,000-panel exterior bridge, matrix
  assembly, Cholesky, and full-space transfer to
  `Q_(749/250) > 9.9e-16 I`. This was a cached replay, not reintegration.

Finite Galerkin positivity is not a lower bound on the full operator: the
Rayleigh--Ritz values are upper bounds on the true infimum. Only the explicit
complement/cross transfer promotes a finite certificate to a full-domain
result.

### 8.2 A checkpoint invalidation defect

The n=4 function
[cache_kernel_source_sha256](../src/fullinf_unrestricted_n4_certificate.py#L255-L287)
hashes selected function bodies but not the source definitions of globals they
use, including prime amplitudes and the half-width. Consequently, changing a
global amplitude formula could reuse stale integral balls. The current values
and replay are internally consistent, but the README statement that every
integrand change fails closed is too strong.

Before release, either regenerate n=4 from scratch or expand the fingerprint to
cover all numerical globals and dependency versions, then independently
cross-check the fresh artifact.

**2026-09-03 successor repair.**  The driver now emits complete version-3
metadata covering the selected function bodies, every load-bearing numerical
global, the odd-double-factorial table, and the python-flint/FLINT versions.
The old complete v2 artifact remains replayable only through a pinned shim
that checks its exact file SHA-256 and the complete current v3 integrand
fingerprint against the documented generation state.  This makes source,
global-value, and dependency drift fail closed.  It does not replace the
independent fresh-v3 regeneration and cross-check still required for release.

### 8.3 Lean build state on 2026-08-10 (historical snapshot)

This subsection records the state at the close of the original dated audit.
It is preserved to distinguish what was known on 2026-08-10 from the
successful serialized closure recorded in Section 8.4.

Focused reusable audits succeeded from available artifacts:

- `Glide.UpstreamAudit`: 14 advertised endpoints, standard logical axioms only;
- `Weilcert.UpstreamAudit`: 11 endpoints, standard logical axioms only;
- `RHBridge.ReusableAudit`: standard logical axioms only;
- five principal `UniformSupportTransfer` endpoints: standard logical axioms
  only.

A targeted rebuild of `CertifiedBaseInterval` expanded into the enormous
generated p=2 dependency tree. Individual workers reached roughly 7--9 GiB RSS
on a host whose swap was already full, so the build was stopped gracefully.
At the end of the audit, 34 Lean source modules lacked corresponding `.olean`
files, and the current `GeneralZetaWeilForm.lean` source was newer than its
artifact. Thus the present source closure was **not** cleanly rebuilt end to
end during this audit. Missing imports were a build-state issue, not a rejected
theorem, but a clean serialized rebuild is a release requirement.

The p=2 formal tree contains 4,675 tracked `P2*.lean` sources, including 4,471
generated check modules. The generator needs a frozen one-command orchestration
manifest, exact output hashes, and an archival environment. Broad parallel
builds are inappropriate on this machine.

### 8.4 Post-audit serialized Lean closure (2026-08-11)

The content-invalidated generated closure was rebuilt serially on 2026-08-10
and 2026-08-11. All **4,149** generated heavy leaves that were stale at the
rebuild baseline completed successfully. The 32 panel aggregates import
exactly **4,288/4,288** factor, flat-factor, moment, and refinement leaves, so
the rebuild plus the 139 already-current leaves covers the complete generated
sub-check family rather than a sample. The final panel-31 run succeeded in
`1:54:08`, with `/usr/bin/time` maximum RSS `16,070,696 kB`; the monitored
run recorded zero process swaps. This larger peak reinforces the requirement
that these targets be run singly.

The publication-facing audit targets then rebuilt and passed. Write

```text
S = [propext, Classical.choice, Quot.sound].
```

The fresh `#print axioms` boundary was:

- `P2RoundedBoundedCertificateAudit`: canonical matrix containment and the
  clipped endpoint each report exactly `S`.
- `ZetaWeilFormAudit`: all 11 advertised domain, arithmetic-form,
  autocorrelation, and lower-bound endpoints report exactly `S`.
- `GeneralZetaWeilFormAudit`: all 11 advertised finite-prime specialization
  and endpoint declarations report exactly `S`.
- `GuinandWeilFormulaAudit`: all 25 zero-side infrastructure declarations
  report exactly `S`. In particular, this module formalizes the conditional
  proposition `Holds` and consequences of it; it does not assert the
  Guinand--Weil formula.
- `GuinandWeilLiteratureAudit`: `smooth_bilateralLaplace_entire` now reports
  exactly `S`; it was discharged on 2026-08-11 from the project's
  compact-support Fourier--Laplace theorem. Each of the two remaining
  literature axioms reports `S` plus itself. `smooth_zero_sum_eq_weilForm` adds only
  `smooth_guinandWeil_formula`, while
  `logarithmic_zero_disk_limit_eq_weilForm` adds only
  `logarithmicDomain_guinandWeil_formula`.
- `CertifiedBaseIntervalAudit`: the smaller-support lower bound and
  `positiveAt` report `S` plus exactly
  `ActivationCancellation.intervalAutocorrelation_eq_zero_of_two_mul_le`;
  the two smooth/Fourier representative lemmas report exactly `S`.
- `WeilCriterionLiteratureAudit`: the arithmetic positivity/domination
  equivalence and fixed `7/16` positivity report exactly `S`. The criterion
  declaration and the uniform-domination implication report `S` plus exactly
  `WeilCriterionLiterature.riemannHypothesis_iff_globalWeilPositivity`.
- `UniformPropagationToRHAudit`: the relative-block step, scale positivity,
  and global-positivity consequence report exactly `S`; only the final RH
  implication adds the named Weil-criterion axiom. This audit verifies the
  implication from a `PropagationPackage`, not an inhabitant of that package.

The separate Stage-4 comparator audit also passed, in `1:54.82` with maximum
RSS `7,126,688 kB`. Its self-polarization identity reports exactly `S`. Its
three vanishing-Rayleigh/noncoercivity endpoints report `S` plus exactly these
four declared literature inputs:

```text
Stage4SamplingLiterature.weilCross_abs_le_zeroSampleEnergy
Stage4SamplingLiterature.zeroSampleEnergy_le_logarithmicGraphNormSq
ZetaZeroCountingLiterature.summable_squareSampleHeightWeight
ZetaZeroFreeRegionLiterature.exists_recip_centeredEdgeDistance_le_log
```

These three nontrivial endpoints quantify over a supplied
`CertifiedCCMComparatorFamily`; this audit does not construct such a family.
Thus the four axioms above are the exact boundary of the normalized-comparator
endpoints, not of every Stage-4 construction interface. The generic family
audit additionally exposes
`Stage4SamplingLiterature.zeroSampleEnergy_nestedLogarithmicSupport`, and the
separate canonical-family interface has seven named construction axioms.

Finally, content-rehashing no-build gates passed for the selected release and
audit closures in all three packages: **3,040 Lake jobs** for Glide,
**2,945** for Weilcert, and **13,414** for RHBridge. These counts are Lake
job-graph totals, not source-module counts. Together with the fresh audit
traces, they show that the stored artifacts within those closures match the
checked sources, imports, options, and pinned Lean toolchain. They do not claim
that every scratch, benchmark, or optional module in each package has an
up-to-date object. The exact dependency hashes, Lake output hashes, artifact
SHA-256 values, sizes, and axiom messages for the 12 selected audit roots are
recorded in the
[cache provenance manifest](LEAN-PUBLICATION-CACHE-MANIFEST-2026-08-11.json).

This clears the 2026-08-10 stale-source/missing-artifact objection for the
publication-facing closure. It does not turn the run into independent
clean-machine reproduction, regenerate the certificate sources, fill the
uninhabited propagation package, or remove any named literature boundary. The
n=4 cached-ball replay and fingerprint caveat in Section 8.2 are also
unchanged. A release should still freeze the generator invocation,
environment, source and output hashes, audit traces, and no-build gate
transcript, then reproduce them from an independent clean checkout.

## 9. Documentation reconciliation

On 2026-08-10, the current
[MATHEMATICAL-OVERVIEW.md](../publication/MATHEMATICAL-OVERVIEW.md) was the best
source of truth for the local arithmetic endpoint, while older documents still
said that the zeta arithmetic form/domain identification was outside Lean:

- [THEOREMS.md](../THEOREMS.md), especially its Theorem 3 discussion;
- the earlier part of [lean/README-verify.md](../lean/README-verify.md), which
  conflicts with its later current-status section;
- [results/CODEX-REVIEW.md](CODEX-REVIEW.md), which records an earlier state.

On 2026-08-11,
[THEOREMS.md](../THEOREMS.md),
[lean/README-verify.md](../lean/README-verify.md), and the
[mathematical overview](../publication/MATHEMATICAL-OVERVIEW.md) were reconciled
to distinguish the kernel-checked local arithmetic endpoint from the unproved
zero-side Guinand--Weil equality. `results/CODEX-REVIEW.md` remains a historical
record rather than a current theorem ledger. This resolves the specific stale
claims found in the original audit; future changes must keep the three current
documents synchronized.

## 10. Novelty and publication ranking

This ranking is based on source inspection and a targeted primary-literature
search updated through 2026-08-11. It is not a substitute for MathSciNet/Zentralblatt
searches or specialist referee review.

### Tier A: act on now

1. **Endo phase-coupling correction.** High confidence, sharp witness, clear
   external value. Best handled cooperatively as an author corrigendum or
   short erratum, not marketed as a major standalone theorem.

2. **Local full-domain arithmetic Weil positivity at `a=7/16`.** Strongest
   original project theorem. A credible formal-methods/computer-assisted
   analysis paper if it exposes the exact form-domain statement, analytic
   transfer, certificate soundness, and axiom boundary. The 2026-08-11
   serialized rebuild, focused audits, and content-rehash gates remove the
   earlier stale-build objection. Submission still needs a frozen generator
   manifest and environment, archived evidence, independent reproduction, and
   specialist novelty review. Anthropic's process appendix separately reports
   an unrefereed, unreproduced interval-arithmetic positivity claim on
   multiplicative support `[1/3,3]`, wider than both this project's Lean
   endpoint and its separate `L=749/250` software checkpoint. No certificate
   or source for that claim is public in the Zeta23 repository, so it is not
   correctness evidence, but it is a material priority risk.
   Avoid “largest support,” “first interval certificate,” or similar claims;
   emphasize the fully specified Lean-kernel-checked full-domain theorem. The
   detailed comparison is
   [`ANTHROPIC-ZETA23-INTEGRATION.md`](../publication/ANTHROPIC-ZETA23-INTEGRATION.md).

### Tier B: plausible standalone notes after review

3. **Fixed-box exact-width spectrometer.** Clean and directly relevant to the
   stated strip goal. Likely modest novelty because the underlying
   explicit-formula/Laplace-pole principle is classical; the exact one-triangle
   formulation may still be a useful short note.

4. **Hard Horizon anchored Jensen theorem.** The exact constants and Lean
   packaging may be new, but the Jensen/Paley--Wiener mechanism is classical and
   the low-band anchor is essential. Do not market its conditional zeta
   corollaries as unconditional zero-density progress.

5. **Reusable formal analysis units.** Digamma/Gauss kernels, interval Legendre
   `L^2`, Fourier--Laplace, autocorrelation/Plancherel, and generic exact
   certificate/two-block coercivity are credible upstream contributions.
   Submit small units only after checking current mathlib overlap and AI
   contribution policy.

### Tier C: consolidate, do not fragment

6. **R176 plus the no-go atlas.** Potentially publishable as a concise
   obstruction/synthesis paper if reduced to a small number of conventional
   theorems. The chronological collection is not submission-ready.

7. **Larger numerical windows.** Useful stress tests and examples, but not
   independent RH advances. Recent work already studies finite/truncated Weil
   operators and their numerical realization; compare
   [the finite Guinand--Weil dictionary](https://arxiv.org/abs/2607.02828) and
   [a numerical realization of Suzuki's operator](https://arxiv.org/abs/2607.24830).

### Not currently publishable as claimed RH progress

- the uninhabited propagation package;
- the all-vector Schur inequality without an independent factorization;
- finite positive spectra by themselves;
- moving-window empirical envelopes;
- theorem cards whose decisive conclusion is a project-specific axiom;
- the R176 coefficient-specific premise before it is proved.

Suzuki's current paper already makes the all-support/nondegeneracy frontier
explicit; compare [Weil's quadratic form via the screw function](https://arxiv.org/abs/2606.09096).
The earlier claim that Lean zeta work was confined to foundational
infrastructure is now obsolete. Anthropic's
[Zeta23 artifact](https://github.com/anthropics/zeta-23-lean) proves a smooth
Weil explicit formula and the unconditional rank/inertia density theorem from
source, in addition to foundational zeta and `L`-function infrastructure; see
also [Formalizing zeta and L-functions in Lean](https://arxiv.org/abs/2503.00959).
This does not duplicate the project's exact local theorem: Zeta23 proves a
bulk zero-density result, while this repository proves a strict full-domain
arithmetic-form lower bound at one fixed support by interval and Lean
certificates. The novelty claim should be that narrow distinction, pending a
specialist search and the wider-window priority issue above.

## 11. Recommended program

### Publication track

1. Freeze the Endo correction as a two-page mathematical note plus exact edit
   ledger; have a human verify every reference to the preprint, then contact the
   author privately.
2. Freeze one local-Weil theorem statement and normalization. The stale prose
   reconciliation and serialized publication-facing Lean closure were
   completed on 2026-08-11. The first release now excludes the `n=4` software
   checkpoint. The exact environment, p=2 generation snapshot, output hashes,
   and deterministic replay recipe are now frozen; next execute that recipe
   from an independent checkout and archive its generation, axiom, build, and
   rehash transcripts. Harden `n=4` only if it is later promoted to an
   advertised result.
3. Split reusable Lean units into small reviewable packages; do not couple
   their upstreaming to the RH application.
4. Send the fixed-box theorem to an analytic-number-theory specialist for a
   priority and normalization review before drafting a standalone note.
5. Implement the seven-lemma normalization adapter from Zeta23's proved
   smooth explicit formula to `smooth_guinandWeil_formula`. Keep the external
   package pinned separately; do not invalidate the current Lean cache merely
   to share a toolchain.

### Research track toward a fixed strip

1. Use the fixed-box exponent identity as the primary scoreboard. Seek any
   fixed arithmetic saving below exponent `1/2`; do not demand RH scale at the
   first step.
2. Treat the Zeta23 rank/inertia method as a complementary bulk-census branch,
   not as propagation. Its reusable algebra compiles against the current
   toolchain, but its trace/Frobenius moments are insensitive to sparse
   off-line zeros. The proposed one-block lower-spectral-edge carrier has now
   failed its structural gate: exact abstract examples and an exact tapered
   Gabor lattice screen a selected negative atom. See
   [`SINGLE-HYPERBOLIC-BLOCK-ISOLATION-GATE.md`](SINGLE-HYPERBOLIC-BLOCK-ISOLATION-GATE.md).
   A later varying-parameter audit removes the coarse dimension deficit by
   additive/mesoscopic padding while preserving the raw prime estimates; see
   [`ZETA23-ADDITIVE-EDGE-PADDING-AUDIT-2026-08-11.md`](ZETA23-ADDITIVE-EDGE-PADDING-AUDIT-2026-08-11.md).
   The endpoint-jet follow-up also combines exact sharp interpolation with an
   exponentially small remote tail, overturning the earlier qualitative
   tail/full-spark gate.  Collision compactness then gives a strict
   separation-free signed edge for every fixed configuration class, and the
   sharp arithmetic matrix retains Loewner displacement rank at most two
   after jet compression; see
   [`ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md`](ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md).
   The fixed-parameter margin theorem is isolated in
   [`ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md`](ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md).
   The remaining estimates must be matched at one scale.  For a depth-`alpha`
   pair, write the actual normalized carrier margin as
   `K=(X^alpha/L)r_T`, `X=exp(L)`, and set
   `B_X=osc(A_X)+(2/L)max|D_X|`.  Tail closure requires
   `E_remote=o(K)`; the scalar prime route requires
   `B_X=o(X^alpha r_T)`.  A direct constrained Pick/Loewner alternative must
   give normalized prime negative-edge error `o(K)` at that same actual `K`.
   Resume this branch only at the effective signed Schur estimate in
   [`ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md`](ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md)
   coupled to the scalar/Pick prime lower edge in
   [`ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`](ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md).
   The exact scalar audit does obtain
   `B_X<<X^(1/2)/(log X)^(3/10)` from a published sharp prime-twist theorem,
   but this remains `X^(1/2-o(1))`.  It also proves only the implication
   `fixed strip => fixed-power scalar bound`; Turan's converse requires
   complex interval sums over continuous ordinates and a power-wide family
   of lengths, not this one critical grid.  See
   [`ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md`](ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md).
   The subsequent sparse audit settles the zero-side bulk question rather
   than merely leaving it open.  A hostile-audited Gevrey-tapered `k=3`
   island preserves the Riemann--von Mangoldt count, the imported simple-line
   density, and the leading trace/Frobenius/pair-correlation moment, but has
   only

   ```text
   0<K<=X^(2*alpha/3+o(1)).
   ```

   It works with canonical logarithmic padding for every fixed
   `alpha<1/2`, and with the weakest admissible padding for `alpha<3/8`.
   Thus first and second bulk moments cannot yield the required full-power
   carrier edge.  See
   [`ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md`](ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md).
   On the arithmetic side, an exact endpoint-flat two-lobe packet retains a
   full one-pair carrier while reducing every power-sized completed term to
   one smooth centered von Mangoldt polynomial.  The matched estimate is
   `o(Y^alpha)`; the current unconditional result is
   `Y^(1/2-o(1))`.  Exact recompletion retains the ordinary
   `-mu(n)log(n)` coefficient, including at the shorter `Y=X^(2/3)` sparse
   alias.  Prime-translate nulling is a precise remaining projection
   criterion, but raw dimension does not control its Laplace leverage and
   globally averaged zero density does not prevent locally ill-conditioned
   off-line clusters.  See
   [`ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`](ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md).
   The optimized cross correlation has the exact Wiener norm
   `sum|h_k|`; finite duality makes prime nulling an `l^infinity`
   approximation problem on the actual prime-power logarithms.  KMT gives
   only a logarithmic upper bound for this normalized extremal, and no
   matching lower bound is known.  The proportional two-lobe exponent
   ledger would formally give `0.597907...` from the global density, but the
   sparse `k=3` operator bound refutes its target-retention premise below
   lobe width `1/3`.  The first non-refuted numerical target is the still
   conditional edge `3/4+epsilon`.  The legal-bandwidth local audit also
   shows that the Frobenius moment excludes a macroscopic equal-depth `k=2`
   block but not sublinear ill-conditioned clusters.  See
   [`ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`](ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md),
   [`ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md`](ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md),
   and
   [`ZETA23-LOCAL-K2-CLUSTER-MOMENT-BARRIER-2026-08-11.md`](ZETA23-LOCAL-K2-CLUSTER-MOMENT-BARRIER-2026-08-11.md).
   The complete frontier is consolidated in
   [`UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md`](UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md).
3. For support propagation, first formalize/prove the `A_2` interval-cutoff
   lemma and repair a.e. support. This removes plumbing but should not be
   mistaken for the main estimate.
4. Freeze a non-tautological adjacent-support theorem card specifying:
   the canonical split, common form domain, positive comparison functional or
   factorization, low-energy sector, strict contraction, and cofinal/non-Zeno
   quantifiers.
5. Attempt to falsify that exact card with the two-sliver and zero-frequency
   families before any large Lean implementation.
6. Run further fixed-window computations only when they test a proposed
   relative constant or factorization. More isolated positive windows do not
   address the uniform theorem.

## 12. Release blockers

The stale publication-facing Lean closure and the three-document
reconciliation identified on 2026-08-10 were cleared by the 2026-08-11
post-audit work. Before any public mathematical claim based on the certificate
stack:

- preserve the successful serialized build, audit traces, and no-build rehash
  transcript, and reproduce them from an independent clean checkout;
- archive complete `#print axioms` output for advertised endpoints;
- execute the frozen certificate-generation manifest in an independent
  checkout and preserve its measured transcript;
- reproduce the locked numerical environment, including the recorded
  FLINT/Arb backend versions;
- if the `n=4` endpoint is advertised, first fix its fingerprint and regenerate
  or independently verify its raw balls; it is excluded from the narrow
  `a=7/16` release candidate;
- keep `THEOREMS.md`, `README-verify.md`, and the mathematical overview
  synchronized with the audited boundary;
- state the Guinand--Weil and Weil-criterion literature boundaries in the
  abstract, not only deep in appendices;
- supply human authorship, acknowledgements, provenance, and `CITATION.cff`;
- obtain independent analytic and formal referees.

## 13. Bottom line

The project has not solved the uniform-strip problem, but it has produced a
meaningful local theorem, reusable formal mathematics, a clean exact-width
detector, and at least one likely external correction. The best publication
move is still to freeze the parts that are already real and finish independent
reproducibility.

The strip-facing conclusion is now more precise than “park the Gabor branch.”
Endpoint jets do isolate a lone hyperbolic pair at full power, while a
hostile-audited sparse tapered island proves that count, density, and two
moments together cannot do so uniformly.  The explicit packet then identifies
the exact arithmetic residue: a centered smooth von Mangoldt polynomial whose
required `Y^alpha` bound is fixed-strip strength.  The exact Wiener dual
shows that `L2` interpolation and dimension surplus use the wrong norm;
current arithmetic gives only logarithmic control in that norm.  Future work
should resume only at one of two genuinely new inputs: a zeta-specific theorem
excluding the sparse island, or a quantitative prime/zero
target-interpolation bound that survives local clustering and retains a
subpower fraction of the carrier.  More
local positivity windows, trace moments, or coefficient-free Type-II
rearrangements do not address that gate.
