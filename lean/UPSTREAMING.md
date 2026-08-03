# Lean extraction and upstreaming map

This document records which parts of the formal development are reusable
mathematical infrastructure, how they have been separated from the RH
application, and what remains before opening any upstream pull request.  No PR
is created by this repository pass.

## Status and claim boundary

The declarations listed below are proved Lean theorems.  They must not be
confused with the separate `*Literature` interfaces in `RHBridge`, which expose
explicit assumptions from the mathematical literature, or with the conditional
RH research program.  None of the extracted results proves RH.

Original project material is released under Apache 2.0.  Candidate files have
standard license headers.  Before an actual submission, replace the collective
`Riemann-Zeta project contributors` author field with the names requested by the
human contributors and retain provenance in the PR description.

## Candidate theorem packages

### 1. Finite simple-pole residue infrastructure

Modules:

- `rhbridge/RHBridge/SimplePole.lean` (standalone finite removal and circles);
- `rhbridge/RHBridge/ComplexResidue.lean` (rectangle machinery and compatibility
  re-export).

Human-facing endpoint: remove finitely many specified simple principal parts,
produce one entire remainder, and express circle integrals by the resulting
finite residue sum.  That compact API now depends only on mathlib's complex
Cauchy-integral layer.  Rectangle-boundary decomposition and the corresponding
`wedgeIntegral` theorems are physically isolated in the larger module.  The API
deliberately says **simple poles**: it does not yet claim arbitrary-order
residues or an argument principle.

Suggested upstream unit: `SimplePole.lean`, beginning with the local
decomposition and finite-removal lemmas.  Submit the circle formulas only where
they add something not already covered by mathlib.  Treat the rectangle module
as a separate follow-up after deleting wrappers duplicated by existing
`wedgeIntegral` APIs.

### 2. Digamma difference series and Gauss kernel

Modules:

- `glide/Glide/BasicCore.lean`
- `glide/Glide/DigammaVertical.lean`
- `glide/Glide/GammaUniform.lean`
- `glide/Glide/DigammaSeries.lean`
- `glide/Glide/DigammaKernel.lean`

This general import chain is physically closed under normalization-free
modules: it contains no `quarter*`, `archKernel`, p=2 symbol, or certificate
declarations.  The `Basic`, `DigammaSeriesBridge`, `GammaUniformBridge`, and
`DigammaKernelBridge` compatibility umbrellas restore the historical
quarter-line and p=2 API for downstream project code.  None of those
compatibility modules is part of the proposed upstream unit.

Human-facing series endpoint, for positive real parts:

```text
ψ(z) - ψ(w) = ∑ n, (1 / (n + w) - 1 / (n + z)).
```

For real `a>0`, the vertical-line specialization also proves

```text
Re ψ(a+i*y) - Re ψ(a)
  = ∫ t in (0,∞), exp (-a*t) * (1-cos (y*t)) / (1-exp (-t)).
```

The quarter-line formula used by the archimedean Weil kernel is a compatibility
corollary, not the primary theorem.  This is a natural candidate for mathlib's
gamma/digamma area because it closes a general analytic gap rather than
encoding an RH normalization.

### 3. Legendre `L²` analysis on arbitrary intervals

Modules:

- `weilcert/LegendreL2.lean`
- `weilcert/LegendreScaledL2.lean`
- `weilcert/LegendreIntervalL2.lean`
- `weilcert/LegendrePlaneWaveL2.lean`

Human-facing endpoints: normalized Legendre polynomials form a complete
orthonormal basis of `L²([-1,1])`; symmetric scaling transports this to
`[-a,a]`; and `LegendreIntervalL2.FourierLegendre` gives an actual basis of
`L²([b,c])` for every `b<c`.  Both coefficient maps are unitary and satisfy
Parseval and an exact finite-projection error formula.  Plane-wave
coefficients have the proved closed form used by the projection estimates.

Suggested upstream split: completeness/Parseval, then affine interval
transport, then the plane-wave specialization.  This avoids asking reviewers
to evaluate the certificate application at the same time as the basis theory.
The arbitrary-interval theory is now a separate module.  Its proof deliberately
repeats the small density/Hilbert-basis packaging on the actual interval
subtype; replacing that with an explicit affine `L²` isometry is a possible
follow-up, not hidden as completed work.  `LegendreScaledL2` temporarily
re-exports the new module for source compatibility; that compatibility import
can be dropped when preparing an individual upstream patch.

### 4. Exact certificate and two-block coercivity lemmas

Modules:

- `weilcert/CertFramework.lean`
- `weilcert/FullInfTransfer.lean`

Human-facing endpoints:

- `LDLPosCertificate.sound` turns exact `LDLᵀ` congruence data into strict
  positivity whenever the certified diagonal margin dominates the
  dimension-times-entrywise perturbation budget;
- diagonal coercivities `β,d` and cross norm `c` give the optimal scalar
  two-block lower bound
  `(β + d - sqrt ((β - d)^2 + 4*c^2)) / 2`.

The generic algebra should be submitted without any p=2 matrix, zeta symbol,
or generated rational table.  The fixed rational scalar and projection
instances now live in `weilcert/FullInfExactLedgers.lean`; concrete
certificates remain project artifacts.

### 5. Autocorrelation via Plancherel

Modules:

- `rhbridge/RHBridge/AutocorrelationPlancherelCore.lean` (standalone);
- `rhbridge/RHBridge/AutocorrelationPlancherel.lean` (interval wrappers).

Human-facing endpoints:

- `integral_inner_translate_eq_integral_fourier` for cross-correlation;
- `integral_re_inner_translate_eq_cos_fourier_energy`, the real-line
  Wiener–Khinchin identity with mathlib's ordinary-frequency normalization.

The real-line theory is now physically independent of the certificate stack;
the interval zero-extension identification remains in the wrapper module.

### 6. Quantitative two-sided smooth cutoff

Modules:

- `rhbridge/RHBridge/SmoothCutoff.lean` (standalone construction);
- `rhbridge/RHBridge/SmoothCompactSupportData.lean` (standalone data layer);
- `rhbridge/RHBridge/ExplicitSmoothCutoff.lean` (zeta-Weil wrappers only).

The standalone file proves smoothness, range and support properties, the exact
derivative formula, existence of a universal base-transition slope bound, and
the scaled estimate `2*M/(a-r)`.  This is already physically separated from
the application-specific decomposition.  The representative data structure is
also independent of the explicit-formula and zero-side imports, so its cutoff
wrappers can be checked without compiling the generated certificate corpus.

### 7. Compact-support Fourier–Laplace transform

Modules:

- `glide/Glide/CompactSupportFourierLaplace.lean` (standalone);
- `glide/Glide/HardHorizon.lean` (compatibility wrappers and application).

The standalone module proves that the Fourier–Laplace transform of an
integrable function on `[-a,a]` is entire.  It also proves explicitly that a
strongly measurable function with integrable squared norm on this finite
interval is integrable, and gives the exponential-type bound from precisely
those `L²` hypotheses.  It includes normalized and unnormalized bounds,
translated bounds, and preservation of `analyticOrderAt`.  The convention is
`F(z) = ∫_[-a,a] φ(x) exp(-i z x) dx`, so the bound is
`sqrt(2a) exp(a |Im z|)` after normalizing `∫ ‖φ‖² ≤ 1`.  The Hard Horizon
module now delegates to this API; the surrounding theorem remains a
paper/project artifact and should not be proposed in the same PR.

## Proposed review order

1. Digamma kernel identity, because it fills a focused special-functions gap.
2. Finite simple-pole removal from `SimplePole.lean`, after deleting circle
   wrappers duplicated by existing contour APIs; assess the rectangle layer
   separately.
3. Legendre completeness and interval scaling in two or three small PRs.
4. Generic certificate perturbation and two-block coercivity.
5. Smooth cutoff, autocorrelation, and Fourier–Laplace pieces if maintainers
   confirm that the APIs belong in mathlib.

The order is about reviewability, not mathematical importance.

## Build and audit

Each package pins the same Lean/mathlib release and builds independently:

```sh
cd lean/glide && lake build Glide
cd lean/weilcert && lake build
cd lean/rhbridge && lake build RHBridge
```

For candidate declarations, run `#print axioms` and expect only Lean/mathlib's
standard logical quotient/classical axioms (`propext`, `Classical.choice`, and
`Quot.sound` where used), not project literature assumptions.  Also run the
mathlib linters and `#min_imports` after rebasing an extracted branch onto
current mathlib.

## Remaining pre-PR work

- confirm named author attribution;
- rebase each proposed unit onto current mathlib rather than this repository's
  pinned release;
- adopt current mathlib `module`/`public import` syntax in the extracted branch;
- use the final destination namespaces and naming conventions selected with a
  maintainer;
- remove compatibility aliases and application wrappers from the submitted
  diff;
- add focused docstrings/examples and run all linters;
- discuss placement and API on the Lean Zulip before opening broad PRs.

These are packaging/review tasks.  They do not hide mathematical gaps in the
candidate theorems, and they do not promote any conditional RH statement to an
unconditional result.
