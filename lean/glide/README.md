# Glide Lean development

This Lake package contains the reusable archimedean analysis developed for the
larger Riemann-zeta project.  It is a library of proved lemmas, not a proof of
the Riemann Hypothesis.

The most reusable components are:

- `Glide.GammaUniform`: locally uniform convergence of Euler's gamma sequence;
- `Glide.DigammaSeries` and `Glide.DigammaKernel`: digamma difference series
  and their logarithmic-kernel integral form;
- `Glide.DigammaVertical` and `Glide.BasicCore`: normalization-free support
  modules used by that general chain;
- `Glide.DigammaP2Comparison`: project-specific p=2 compatibility bounds,
  deliberately separated from the general kernel;
- `Glide.Basic`, `Glide.GammaUniformBridge`, and
  `Glide.DigammaKernelBridge`: compatibility umbrellas that additionally expose
  the historical quarter-line and p=2 APIs;
- `Glide.CompactSupportFourierLaplace`: standalone entirety and
  exponential-type bounds for compact-interval Fourier–Laplace transforms;
- `Glide.HardHorizon`: the project-specific application, now expressed through
  compatibility wrappers over the standalone transform API.

Build with the pinned Lean/mathlib toolchain:

```sh
lake exe cache get
lake build Glide
lake build Glide.UpstreamAudit
```

`Glide.UpstreamAudit` checks the public extraction endpoints and reports only
`propext`, `Classical.choice`, and `Quot.sound`.

The import closure of `Glide.GammaUniform` and `Glide.DigammaKernel` contains
no quarter-line, p=2 symbol, or certificate declarations.  Import the `Bridge`
modules only when the project-specific compatibility layer is wanted.

All original files in this package are released under Apache 2.0; see this
package's `LICENSE` (identical to the repository-root license).  The extraction
and proposed upstream boundaries are documented in `../UPSTREAMING.md`.
