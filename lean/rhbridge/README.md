# RHBridge Lean development

`RHBridge` composes the `glide` and `weilcert` packages with the
Riemann-zeta-specific formalization.  It contains both reusable analysis and
explicitly assumed literature interfaces.  It is not, and does not claim to
be, a proof of the Riemann Hypothesis.

The cleanest reusable modules are:

- `RHBridge.SimplePole`: standalone finite simple-principal-part removal and
  circle-integral identities;
- `RHBridge.ComplexResidue`: the larger rectangle-boundary implementation; it
  re-exports `RHBridge.SimplePole` for compatibility;
- `RHBridge.AutocorrelationPlancherelCore`: standalone time/frequency
  autocorrelation via Plancherel;
- `RHBridge.AutocorrelationPlancherel`: certificate interval wrappers only;
- `RHBridge.SmoothCutoff`: a standalone quantitative two-sided smooth cutoff;
- `RHBridge.SmoothCompactSupportData`: the formula-independent data type for
  globally smooth compact-support representatives;
- `RHBridge.ExplicitSmoothCutoff`: only the zeta-Weil wrappers around that
  general cutoff and data type.

`import RHBridge.Reusable` loads only the compact standalone simple-pole,
correlation, and cutoff layers; it does not load the rectangle machinery.
Diagnostic `#print axioms` modules are collected separately by `import
RHBridge.Audit` and are not part of the ordinary umbrella.

`RHBridge.S1B1CompletedSourceCommutator` is a finite-algebra audit module for
the 2026-09-03 source-commutator sprint.  It proves only exact kernel and
reflection identities; its companion audit file prints their axioms.  It
does not claim an analytic estimate, a zero-free strip, or RH.

`RHBridge.QPSourceFiberBifurcation` formalizes the distinct direct-radial and
event-dependent source-fiber dual normalizations, their finite convex upper
bounds, and the exact `.001/.0179/.0189/.5/.499` exponent ledger.  Its audit
prints the axioms.  The smooth density-matched real-node construction remains
in the human audit; the Lean module proves no actual-prime LTRAD, DPA, strip,
or RH statement.

`RHBridge.R188PrincipalBandSerialization` checks the exact rational exponent,
high-denominator/small-quotient, target-matched Fourier-collar,
determinant-witness, affine-center, coherent cross-term, and top-box
bookkeeping for the 2026-09-04 principal-band audit.
Its companion audit prints the axioms.  Fourier/Poisson analysis, the PNT
semiprime block, imported reciprocal-sum estimates, the completed
`X^(.98)` bound, a zero-free strip, and RH are deliberately outside its scope.

Build the package with its pinned local dependencies:

```sh
lake build RHBridge
lake build RHBridge.Reusable
```

The distinction between proved declarations, explicit literature assumptions,
and application-level conditional theorems is recorded in audit modules and in
`../UPSTREAMING.md`.  Original files are released under Apache 2.0; see this
package's `LICENSE` (identical to the repository-root license).
