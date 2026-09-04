# Canonical p=2 certificate: deterministic generation and rebuild recipe

Date: 2026-08-11
Snapshot commit: `4ad72dca0c1b63defa2657afd153ddfe4e01ce5e`

This recipe freezes the source-generation boundary that was missing from the
earlier rebuild record. It is paired with
[`P2-CERTIFICATE-GENERATION-MANIFEST-2026-08-11.json`](P2-CERTIFICATE-GENERATION-MANIFEST-2026-08-11.json)
and the read-only
[`verify_p2_generation_manifest.py`](verify_p2_generation_manifest.py).

The generator was **not rerun** while preparing this snapshot. The commands
below were reconstructed from the current generator's actual control flow and
emitted filename families. The current checked-in files were inventoried and
hashed. The expensive Python/FLINT replay and Lean compilation commands are
therefore recipes, not claims about a new run.

## 1. Frozen boundary

`lean/make_p2_panel_certificate.py` uses exact `Fraction` and FLINT rational
polynomial arithmetic. It does not use numerical quadrature. Its external file
inputs are exactly:

- `lean/weilcert/FullInfClipped48.lean`;
- `lean/rhbridge/RHBridge/P2ScaleCenters.lean`.

Phase 2 additionally consumes phase-1 outputs in the selected output
directory: `P2PanelCertificateData.lean` and the 32 numbered rounded-panel
target tables. Consequently, the replay must use one scratch directory and
run the phases in order.

The frozen emitter-owned output is:

| Family | Files |
|---|---:|
| Pole data/checks/umbrella | 10 |
| Compact center data | 1 |
| Rounded panel targets | 34 |
| Factor data/checks/umbrellas | 623 |
| Flat-factor data/checks/umbrellas | 1,632 |
| Moment/refinement data/checks/umbrellas/final assembly | 2,305 |
| **Total** | **4,605** |

These occupy 57,049,440 bytes. They comprise 134 generated data/table modules
and 4,471 generated proof/check/umbrella modules. The heavy reduction leaves
are 4,288 per-panel factor, flat-factor, moment, and refinement leaves, plus 12
spherical-outer and 8 pole leaves, for 4,308 total. The current RHBridge tree
has 4,675 `P2*.lean` files; the other 70 are hand-written support, audit, or
benchmark modules and are deliberately outside the emitter digest.

The aggregate generated-source digest is:

```text
path set SHA-256:        97a14fde065f9ae438c7d7236ef763446b435e75a25a7305638122b9c25bb03e
content manifest SHA-256: 53b078f3471bdda4ff8414ff436efa9c139aa366a08ada9053eb06184c452572
```

The content digest hashes sorted lines of the form
`<file SHA-256><two spaces>lean/rhbridge/RHBridge/<basename><LF>`. Thus it
commits to every file's bytes and canonical name. The path-set digest detects a
missing or extra output even if aggregate byte size happens to agree.

## 2. Exact environment

The snapshot host reported:

```text
Linux 6.17.0-35-generic x86_64, glibc 2.39
Python 3.12.3
python-flint 0.9.0
FLINT 3.6.0
flint.ctx.threads = 1
Lean 4.32.1, commit f054605aea4b840552cca2e725580bffd1e1b704
Lake 5.0.0-src+f054605
mathlib 520045ab14e26149ee970e2e617ca04b09bde5d6
```

`requirements.txt` permits `python-flint>=0.9,<1`; a byte-for-byte replay must
use the observed `0.9.0`/FLINT `3.6.0` pair, not merely any version satisfying
that range. Confirm the active environment before starting:

```sh
python3 --version
python3 -c 'import flint; print(flint.__version__)'
python3 -c 'import flint; print(flint.__FLINT_VERSION__); print(flint.ctx.threads)'
cd lean/rhbridge
lake --version
lake env lean --version
cd ../..
```

The generator has no random sampling. Nevertheless, fix locale, timezone, hash
seed, and worker counts to remove avoidable environmental variation.

## 3. Read-only snapshot check

From the repository root:

```sh
python3 results/verify_p2_generation_manifest.py
```

This reads the 16 provenance files and all 4,605 emitter-owned sources. It does
not invoke Python/FLINT generation, Lake, or Lean, and it writes nothing. A zero
exit status means all per-family counts, byte counts, path-set hashes, and
content hashes match the snapshot.  In this default mode the verifier ignores
the other hand-written RHBridge modules in the checked-in directory, including
the 70 non-emitter `P2*.lean` support/audit files.  When `--source-dir` is
supplied for a scratch replay, every `.lean` file must belong to one of the six
generated families; an unexpected new output is a mismatch.

## 4. Full Python/FLINT replay in scratch space

Do this only on a quiet machine. The generator's peak RSS and elapsed time were
not preserved in the historical record, so the commands below measure both
phases. Do not infer generator memory from the later Lean measurements.

Create a new, explicit scratch directory and keep it for inspection:

```sh
P2_REPLAY_DIR="$(mktemp -d /tmp/p2-certificate-replay.XXXXXX)"
test -d "$P2_REPLAY_DIR"
printf '%s\n' "$P2_REPLAY_DIR"
```

Phase 1 computes the 600 upper-triangular parity entries and writes pole,
compact-center, and 32-panel target data:

```sh
env LC_ALL=C TZ=UTC PYTHONHASHSEED=0 \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  NUMEXPR_NUM_THREADS=1 \
  /usr/bin/time -v -o "$P2_REPLAY_DIR/phase-1.time" \
  python3 -u lean/make_p2_panel_certificate.py \
    --workers 1 \
    --emit-pole-lean "$P2_REPLAY_DIR/P2PoleCoefficientCertificateData.lean" \
    --emit-pole-checks "$P2_REPLAY_DIR" \
    --emit-lean "$P2_REPLAY_DIR/P2PanelCertificateData.lean" \
    --emit-rounded-panel-targets "$P2_REPLAY_DIR"
```

Phase 2 writes every factor, flat-factor, moment, refinement, and final
assembly module. `--factors-only` suppresses a redundant second integration of
the 600 entries; it does not suppress the requested factor/moment emissions.

```sh
env LC_ALL=C TZ=UTC PYTHONHASHSEED=0 \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  NUMEXPR_NUM_THREADS=1 \
  /usr/bin/time -v -o "$P2_REPLAY_DIR/phase-2.time" \
  python3 -u lean/make_p2_panel_certificate.py \
    --workers 1 \
    --emit-rounded-factor-checkpoints "$P2_REPLAY_DIR" \
    --emit-rounded-flat-factor-checkpoints "$P2_REPLAY_DIR" \
    --flat-panel-count 32 \
    --emit-rounded-moment-checkpoints "$P2_REPLAY_DIR" \
    --all-moment-panels \
    --factors-only
```

Do not pass `--round-local-polynomials`: that selects an older scout mode and
is not the production snapshot.

Now compare scratch output without overwriting the repository:

```sh
python3 results/verify_p2_generation_manifest.py \
  --source-dir "$P2_REPLAY_DIR"
```

Only `status: "ok"` is a byte-for-byte replay. Preserve `phase-1.time`,
`phase-2.time`, console transcripts, the exact environment package inventory,
and the scratch directory as the regeneration evidence. Do not copy a mismatch
into `lean/rhbridge/RHBridge`. If a future intentional generator change alters
the output, review the mathematical delta and issue a new dated manifest rather
than editing this snapshot in place.

## 5. Lean plan and serialized kernel checks

The runner `lean/run_p2_kernel_checks.py` fingerprints each selected source,
all locally resolvable transitive Lean imports, unresolved external module
names, and the toolchain/Lake configuration in `rhbridge`, `glide`, and
`weilcert`. A resume hit is accepted only for the same dependency fingerprint;
with dependency builds enabled, Lake must also certify the target artifact as
current.

The following six globs select exactly the 4,308 generated heavy reduction
leaves. First inspect the plan. `--dry-run` invokes neither Lake nor Lean and
writes no runner state:

```sh
python3 lean/run_p2_kernel_checks.py \
  --dry-run --no-resume --with-dependencies --jobs 1 --timeout 7200 \
  'RHBridge/P2PoleCoefficientCertificateCheck[0-9]*.lean' \
  'RHBridge/P2RoundedSphericalOuterCheck[0-9]*.lean' \
  'RHBridge/P2RoundedFactorCheckpointCheck*.lean' \
  'RHBridge/P2RoundedFlatFactorCheckpointCheck*.lean' \
  'RHBridge/P2RoundedMomentCheckpointCheck*.lean' \
  'RHBridge/P2RoundedMomentRefinementCheck*.lean'
```

For an incremental run, repeat without `--dry-run` and normally without
`--no-resume`; matching successful fingerprints are reused. On a clean
independent checkout with no imported runner state, every leaf runs anyway.
Keep `--jobs 1`. Although the runner implements a two-leaf mode, the measured
memory peaks make it inappropriate for this closure on the recorded host.

Before any actual Lean work:

```sh
rg 'MemAvailable' /proc/meminfo
```

Require at least 20 GiB `MemAvailable`, nearly idle swap activity, and no other
Lean/Lake process. Use these limits throughout:

```sh
export LEAN_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
```

The actual incremental runner invocation is:

```sh
python3 lean/run_p2_kernel_checks.py \
  --with-dependencies --jobs 1 --timeout 7200 \
  'RHBridge/P2PoleCoefficientCertificateCheck[0-9]*.lean' \
  'RHBridge/P2RoundedSphericalOuterCheck[0-9]*.lean' \
  'RHBridge/P2RoundedFactorCheckpointCheck*.lean' \
  'RHBridge/P2RoundedFlatFactorCheckpointCheck*.lean' \
  'RHBridge/P2RoundedMomentCheckpointCheck*.lean' \
  'RHBridge/P2RoundedMomentRefinementCheck*.lean'
```

Then build the semantic root and focused axiom audit, one command at a time:

```sh
cd lean/rhbridge
export C_INCLUDE_PATH=/usr/include/x86_64-linux-gnu
lake exe cache get
lake --log-level=error build +RHBridge.P2RoundedBoundedCertificateCheck:olean
lake --log-level=error build +RHBridge.P2RoundedBoundedCertificateAudit:olean
lake env lean RHBridge/P2RoundedBoundedCertificateAudit.lean
```

The expected focused audit boundary is exactly
`[propext, Classical.choice, Quot.sound]` for both
`p2_canonical_matrix_containment` and `p2_canonical_clipped_endpoint`.

## 6. Cache and no-build replay

The `+Module:olean` builds populate reusable `.olean`, `.ilean`, C, and trace
artifacts under each package's `.lake/build`. The recorded RHBridge build tree
was 28,680,251,284 bytes. No archive was made; the live `.lake/build`
directories are the cache. Reuse requires the same source bytes, imports,
toolchain, Lake manifests/options, compatible platform, and then a content
rehash gate.

For the p=2 roots:

```sh
cd lean/rhbridge
lake --rehash --no-build --log-level=error build \
  +RHBridge.P2RoundedBoundedCertificateCheck:olean \
  +RHBridge.P2RoundedBoundedCertificateAudit:olean
```

`--no-build` is essential: it must reject a missing or stale artifact rather
than silently repairing it. The broader publication gate and per-target
artifact hashes are frozen in
[`LEAN-PUBLICATION-CACHE-MANIFEST-2026-08-11.json`](LEAN-PUBLICATION-CACHE-MANIFEST-2026-08-11.json).

## 7. Observed evidence versus unexecuted recipe

Observed directly while creating this snapshot:

- Python, python-flint/FLINT, Lean, Lake, kernel, architecture, and manifest
  versions listed in Section 2;
- clean hashes for the 16 listed provenance files;
- 4,605 disjoint emitter-owned output paths and 57,049,440 output bytes;
- the family and aggregate SHA-256 values in the machine manifest;
- a zero-exit read-only verifier replay of that checked-in inventory;
- historical runner state containing 6,086 attempts over 4,496 unique sources:
  6,078 successes and 8 failed attempts later eligible for retry. Its largest
  recorded successful attempt was
  `P2RoundedMomentCheckpointCheck31_mode15.lean`, 120.63 seconds and
  16,039,244 kB maximum RSS. This append-only log covers 2026-07-28 through
  2026-07-30 and is not itself proof that every old fingerprint is current.

Reported by the completed 2026-08-10/11 serialized rebuild:

- all 4,149 leaves stale at its baseline rebuilt successfully;
- the 32 panel aggregates cover 4,288/4,288 per-panel heavy leaves, with 139
  already current at baseline;
- the final panel-31 run took `1:54:08`, reached 16,070,696 kB maximum RSS,
  and had zero monitored process swaps;
- the later cache manifest records successful no-build gates of 3,040 Glide,
  2,945 Weilcert, and 13,415 RHBridge Lake jobs. The earlier narrative says
  13,414 RHBridge jobs; retain this discrepancy because Lake job-graph count is
  not a source-module invariant.

Not executed while creating this snapshot:

- either Python/FLINT generation phase;
- any generated Lean leaf or aggregate compilation;
- the focused or publication-wide `lake --rehash --no-build` gate.

Those omissions are deliberate: this task froze a deterministic replay and
hash boundary without consuming the memory required by regeneration or
altering generated Lean sources. A future independent reproduction should
append its measured phase timings, resource metrics, runner JSONL, audit
transcript, and no-build transcript to a new dated evidence bundle.

## 8. Trust interpretation

Matching the generation hash shows reproducibility of the candidate tables; it
does not make Python or FLINT part of the theorem's trusted base. The generated
integers and rationals remain untrusted inputs. Lean's ordinary kernel checks
the factor equalities, moment/matvec identities, all 19,200 bounded panel-entry
refinements, aggregation, and final containment. Publication evidence therefore
requires both layers: the generation hash for provenance and the Lean
build/audit/no-build gates for proof checking.
