# Release candidate: local arithmetic Weil positivity at `a = 7/16`

Status: **referee bundle in preparation**.  This is the canonical narrow scope
for a first release from the certificate project.  If this document conflicts
with Lean, the exact declaration and its focused axiom audit control.

## Advertised theorem

Let `f` be a nonzero real `L²` vector supported in `[-7/16,7/16]` and lying
in the intrinsic logarithmic Fourier form domain.  For the arithmetic
compact-support Weil form defined in the repository, Lean proves

```text
(22699 / 10^9) * ‖f‖² < Q_(7/16)(f).
```

The exact declaration is
[`RHP2Bridge.GeneralZetaWeilForm.weilForm_seven_sixteenths_strict_lower_bound`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean#L361).
Its hypotheses explicitly include `f ≠ 0` and membership in
`InLogarithmicDomain (7/16)`.  The form is the arithmetic expression

```text
pole term + archimedean term - finite prime-power term,
```

not an assumed sum over zeta zeros.

## Normalization contract

| Item | Release convention |
|---|---|
| Time support | `[-a,a]`, with `a = 7/16` |
| Program-length convention | `L = 4a = 7/4` |
| Multiplicative support | `[exp(-a),exp(a)]` |
| Fourier frequency | Mathlib ordinary frequency `xi`; archimedean arguments use `2*pi*xi` |
| Form domain | Integrability of `log(1+(2*pi*xi)^2)` times Fourier energy |
| Prime-power activation | `log n < 2a = 7/8` |
| Active set | Exactly `{2}` |
| Strict lower-bound constant | `22699 / 10^9 = 0.000022699` |

The support and prime normalization are proved, rather than inferred from a
floating-point cutoff, by
[`activePrimePowers_seven_sixteenths`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean#L292).

## Theorem-to-code map

| Mathematical role | Lean declaration or audit |
|---|---|
| Intrinsic logarithmic domain | [`InLogarithmicDomain`, `LogarithmicFormDomain`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean#L35) |
| Arithmetic form | [`weilForm`, `logarithmicWeilForm`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean#L283) |
| Exact active-prime set `{2}` | [`activePrimePowers_seven_sixteenths`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean#L292) |
| Exact specialization to the fixed-window form | [`weilForm_seven_sixteenths`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean#L346) |
| Generated exact matrix containment | [`p2_canonical_matrix_containment`](../lean/rhbridge/RHBridge/P2RoundedBoundedCertificateCheck.lean#L280) |
| Full-domain analytic transfer | [`p2TimeDomainWeilForm_strict_lower_bound_on_logarithmicDomain`](../lean/rhbridge/RHBridge/ZetaWeilForm.lean#L358) |
| Advertised endpoint | [`weilForm_seven_sixteenths_strict_lower_bound`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean#L361) |
| Certificate axiom audit | [`P2RoundedBoundedCertificateAudit.lean`](../lean/rhbridge/RHBridge/P2RoundedBoundedCertificateAudit.lean) |
| Fixed-window form axiom audit | [`ZetaWeilFormAudit.lean`](../lean/rhbridge/RHBridge/ZetaWeilFormAudit.lean) |
| Final endpoint axiom audit | [`GeneralZetaWeilFormAudit.lean`](../lean/rhbridge/RHBridge/GeneralZetaWeilFormAudit.lean) |

## Dependency and trust ledger

| Component | Function in the proof | Trust status for the advertised theorem |
|---|---|---|
| Lean `v4.32.1` and Mathlib `520045ab…` | Check definitions, analysis, exact arithmetic, and composition; pins are in [`lean-toolchain`](../lean/rhbridge/lean-toolchain) and [`lake-manifest.json`](../lean/rhbridge/lake-manifest.json) | Trusted checker and library base |
| Generated rational certificate sources | Supply finite witnesses and bounds | Rechecked by Lean; their generator is not a logical axiom |
| P2 analytic transfer | Controls finite modes, complement, and cross terms on the full form domain | Proved in Lean |
| Python and FLINT/Arb generation tools | Search for and emit candidate certificate data | Reproducibility dependency, not a premise accepted by Lean |
| Guinand--Weil explicit formula | Would identify the arithmetic form with a zero-side expression | **Not used** by the advertised theorem |
| Weil criterion or any RH equivalence | Would connect all-support positivity to RH | **Not used** by the advertised theorem |

The focused audit for the advertised endpoint reports exactly
`[propext, Classical.choice, Quot.sound]`.  It contains no project literature
axiom.  The current cache/source relationship and the archived axiom messages
for the selected audit roots are recorded in the
[`2026-08-11 cache provenance manifest`](../results/LEAN-PUBLICATION-CACHE-MANIFEST-2026-08-11.json).
The exact generator inputs, 4,605 emitted source files, environment versions,
and aggregate output hashes are frozen separately in the
[`p=2 generation manifest`](../results/P2-CERTIFICATE-GENERATION-MANIFEST-2026-08-11.json).

## Explicit nonclaims

This release candidate does **not** claim:

- the Guinand--Weil equality as a theorem in this repository;
- positivity on every support, or even an unconditional propagated interval;
- a uniform zero-free strip, RH, or a disproof of RH;
- that finite Galerkin positivity alone controls the full operator;
- that `L = 749/250` is part of the release theorem;
- a largest, first, or record compact-support positivity certificate;
- an independent clean-machine reproduction yet.

## Demoted `L = 749/250` checkpoint

The separate `n = 4`, program-length `L = 749/250` computation remains a
software checkpoint and is excluded from this release candidate.  Its last
audit replayed cached Arb balls rather than reintegrating them, and its cache
fingerprint omits some numerical globals.  It may be promoted only after the
fingerprint is repaired, the raw balls are regenerated or independently
cross-checked, and the result receives its own trust statement.  See the
[`checkpoint invalidation audit`](../results/RESEARCH-AUDIT-AND-PUBLICATION-ASSESSMENT-2026-08-10.md#82-a-checkpoint-invalidation-defect).

## Zeta23 and wider-window disclosure

Anthropic's independent Zeta23 artifact proves a smooth zeta explicit formula
and unconditional positive-density results for zeros on the critical line.
Those results do not imply positivity for every test, a lower spectral edge,
or a uniform strip.  A normalization adapter could later remove this
repository's separate smooth explicit-formula literature axiom, but that
adapter is not part of this release and is unnecessary for the arithmetic
endpoint above.  The exact comparison is in
[`ANTHROPIC-ZETA23-INTEGRATION.md`](ANTHROPIC-ZETA23-INTEGRATION.md).

Anthropic's process appendix also discloses an unrefereed, independently
unreproduced interval-arithmetic positivity claim on multiplicative support
`[1/3,3]`.  In this repository's convention that would correspond to
`a = log 3` and program length `L = 4 log 3`, wider than both endpoints above.
No supporting certificate is public in the Zeta23 repository.  The disclosure
therefore limits novelty language but is not treated as an established input.

## Reproduction entrypoints

The authoritative serialized Lean instructions and memory limits are in
[`lean/README-verify.md`](../lean/README-verify.md), Section 3.  A clean,
scratch-directory replay of the exact-rational source generator is specified
by the
[`p=2 certificate replay recipe`](../results/P2-CERTIFICATE-REPLAY-RECIPE-2026-08-11.md).
The minimum publication-facing Lean targets are run one at a time:

```sh
cd lean/rhbridge
export LEAN_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1

lake --log-level=error build +RHBridge.P2RoundedBoundedCertificateAudit:olean
lake --log-level=error build +RHBridge.ZetaWeilFormAudit:olean
lake --log-level=error build +RHBridge.GeneralZetaWeilFormAudit:olean

lake env lean RHBridge/P2RoundedBoundedCertificateAudit.lean
lake env lean RHBridge/ZetaWeilFormAudit.lean
lake env lean RHBridge/GeneralZetaWeilFormAudit.lean

lake --rehash --no-build --log-level=error build \
  +RHBridge.P2RoundedBoundedCertificateAudit:olean \
  +RHBridge.ZetaWeilFormAudit:olean \
  +RHBridge.GeneralZetaWeilFormAudit:olean
```

The generated P2 closure is memory-intensive; do not run another Lean build
concurrently.  Cached `.olean` files make repeat audits fast, but a release
still requires a clean source-to-theorem reconstruction.

### Remaining reproduction gates

- [x] Freeze the generation commands, dependency versions, source/output
      hashes, and file counts in a machine-verifiable manifest.
- [ ] Reproduce the P2 certificate and the three focused audits from an
      independent clean checkout, recording generator runtime and peak memory.
- [ ] Archive the generation log, build log, complete axiom output, and final
      content-rehash transcript together.
- [ ] Freeze the reviewed source snapshot and the exact artifact inventory.

## Provenance, licensing, and review gates

- The repository is distributed under the [Apache License 2.0](../LICENSE).
  Verify that every released generated or extracted source carries compatible
  provenance and the required notice.
- [ ] Name the human authors who approve the theorem statement and accept
      responsibility for the proof.
- [ ] Add the venue-appropriate disclosure of material AI assistance.
- [ ] Add `CITATION.cff` only after authorship and the preferred citation are
      fixed.
- [ ] If Zeta23 code is later copied or adapted, preserve its Apache-2.0
      headers and required attribution/notice files.
- [ ] Obtain an independent analytic-number-theory normalization review and
      an independent artifact reproduction.
- [ ] Create a release tag and archival DOI only after these gates close.
