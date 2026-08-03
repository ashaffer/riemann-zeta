# WeilCert Lean development

This Lake package contains exact finite-dimensional certificate machinery and
the Legendre `L²` analysis used by the Riemann-zeta project.  The generic layer
has deliberately been separated from the numerical certificate instances.

Reusable components include:

- `LegendreScaledL2`: the complete orthonormal Legendre basis on `[-a,a]`;
- `LegendreIntervalL2`: its actual-subtype extension to every nondegenerate
  interval `[b,c]`, with unitary coefficient transforms and exact projection
  errors;
- `LegendrePlaneWaveL2`: the corresponding plane-wave coefficients and
  projection identities;
- `CertFramework`: soundness of exact and rounded positive-definiteness
  certificates;
- `FullInfTransfer`: sharp two-block coercivity and projection-transfer lemmas.

The fixed rational `FULLINF` instances for `L = 7/4`, `497/200`, and
`749/250` live separately in `FullInfExactLedgers`; they are application
artifacts, not part of the proposed reusable algebra extraction.

Build all default targets with the pinned toolchain:

```sh
lake exe cache get
lake build
lake build Weilcert.UpstreamAudit
```

The long target-by-target verification recipe is in `../README-verify.md`.
`Weilcert.UpstreamAudit` checks the public extraction endpoints and reports
only `propext`, `Classical.choice`, and `Quot.sound`.
Original files are released under Apache 2.0; see this package's `LICENSE`
(identical to the repository-root license).  Proposed upstream splits are
documented in `../UPSTREAMING.md`.
