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

Build the package with its pinned local dependencies:

```sh
lake build RHBridge
lake build RHBridge.Reusable
```

The distinction between proved declarations, explicit literature assumptions,
and application-level conditional theorems is recorded in audit modules and in
`../UPSTREAMING.md`.  Original files are released under Apache 2.0; see this
package's `LICENSE` (identical to the repository-root license).
