# ZETA23 compact context caches

## Current research routing

The authoritative continuation state is the canonical
`zeta23_correction_bundle_v1.zctx`/`zeta23_correction_bundle_v1.z23v` pair,
together with the human R181 commutator, R182 source-fiber, R183 exterior
factorization/backward-strip, and R184 constructive-source/compact-derivative
audits.  The
`zeta23_post_synthesis_decision_path_v1.json`,
`zeta23_r105_r116_r73_adapter_audit_v1.json`, and
`zeta23_correction_closure_v1.json` triple remains an internally verified
2026-09-02 pre-R181 snapshot.  Its human authorities are the three reports
named in those caches.  The older
`zeta23_research_preflight_v1.json` remains required background for theorem
passports and hostile models, but its August 30 route ordering is superseded.

A live continuation query reads the September 3 correction ledger:

```bash
python3 src/zeta23_correction_context.py resume
```

The current R184 human authority is
`../ZETA23-CONSTRUCTIVE-COMPLETED-SOURCE-AND-COMPACT-DERIVATIVE-AUDIT-2026-09-03.md`;
its R183, R182, and R181 predecessors are
`../ZETA23-EXTERIOR-FACTORIZATION-AND-BACKWARD-STRIP-AUDIT-2026-09-03.md`,
`../ZETA23-QP-SOURCE-FIBER-BIFURCATION-2026-09-03.md`, and
`../ZETA23-S1-B1-COMPLETED-SOURCE-COMMUTATOR-AUDIT-2026-09-03.md`.
The September 3 hostile-audit corrections have three semantic forms.  The
canonical compact form is `zeta23_correction_bundle_v1.zctx`; its human
projection is
`../ZETA23-REMAINING-MISTAKES-CORRECTION-BUNDLE-2026-09-03.md`, and its finite
algebraic/logical guards are in
`../../lean/rhbridge/RHBridge/CorrectionGuards.lean` and
`../../lean/rhbridge/RHBridge/S1B1CompletedSourceCommutator.lean`, with R182's
finite dual algebra in
`../../lean/rhbridge/RHBridge/QPSourceFiberBifurcation.lean` and R183's finite
factorization guards in
`../../lean/rhbridge/RHBridge/ExteriorFactorizationAudit.lean`, with R184's
finite source/remainder and compact-derivative algebra in
`../../lean/rhbridge/RHBridge/CompletedSourceConstructiveSearch.lean` and
`../../lean/rhbridge/RHBridge/CompactSourceDerivativeBridge.lean`.  The similarly named
JSON file is generated only as an audit/interchange mirror.

Runtime resumption uses the generated uncompressed random-access integer
vectors in `zeta23_correction_bundle_v1.z23v`.  It does not inflate or parse
the full ledger: selected records and their exact strings are sought and
verified independently.  The deliberately lossy `resume` vector retains the
objective, frontier, working hypotheses, learned prohibitions, debts, and next
targets; it is not a hidden-reasoning trace or proof authority.

```bash
python3 src/zeta23_correction_context.py resume
python3 src/zeta23_correction_context.py query C02 C05
python3 src/zeta23_correction_context.py query --vector math
python3 src/zeta23_correction_context.py verify
```

The verifier regenerates both the JSON and `Z23V` projections from `Z23C` and
then checks that the compact, Markdown, and Lean forms retain the same IDs,
theorem names, domains, and nonclaims.
The byte layout and selective-integrity contract are documented in
[`Z23C-Z23V-FORMAT.md`](Z23C-Z23V-FORMAT.md).

`zeta23_current_authority_manifest_v1.json` binds the bytes of the dated
route, adapter, and closure caches and their three reports.  It is a labeled
local SHA-256 manifest only: it has no archive or commit binding and therefore
does not make the untracked research corpus durable.

## What is being optimized

Byte compression is not the main objective: a language model cannot reason
directly over an opaque compressed stream.  The useful quantity is the number
of decoded tokens needed to recover the relevant theorem frontier without
also reviving superseded routes.  The historical v3 cache stores a typed proof
tree and supports selective audit queries.  LZMA2 is only the last
storage layer; the semantic compression comes from proof opcodes, integer
IDs, shared symbols, dependency edges, and omission of narrative history.

There is no claim that `Z23P` is an information-theoretically shortest code.
It was a versioned sufficient statistic for the 2026-08-15 research state:
every node can be decoded to human text and the binary can be
deterministically rebuilt and verified.  It is no longer a sufficient
statistic for the live route.

## Historical v3 proof tree

`zeta23_proof_tree_v3.zpt` is an audited August 15 snapshot.  Unlike the v2
index, it contains self-contained proof IR for every then-live gate: exact
definitions, targets, implication directions, constants, proof kernels,
blockers, counterexamples, checks, and then-admissible next actions.  Its
embedded default is `FQPP`; that embedded default is historical and is not
used by a bare `resume` command.

Build and verify it with:

```bash
python3 src/zeta23_proof_tree.py build
python3 src/zeta23_proof_tree.py verify
```

Decode a historical gate or historical frontier explicitly with:

```bash
python3 src/zeta23_proof_tree.py resume QT
python3 src/zeta23_proof_tree.py resume --frontier
```

The seed JSON is an audit/compiler fixture for the snapshot.
Explicit historical queries suppress optional `REF` records by default, and validation rejects
an open gate unless it has the complete continuation fields needed to work
without the bibliography.

## Deprecated v2 theorem index

`zeta23_kg_v2.zkg` is the former machine index.  It is a lossless theorem
graph with interned strings, integer node IDs, packed status/strength fields,
varint graph edges, exact rational constants, and LZMA2 compression.  The
important optimization is selective rehydration: a future agent can decode
only one live gate and its dependency/no-go closure.

Build and verify it with:

```bash
python3 src/zeta23_kg_cache.py build
python3 src/zeta23_kg_cache.py verify
```

Decode the **then-live historical** dependency closure to human-readable text
with (the CLI prints a supersession warning):

```bash
python3 src/zeta23_kg_cache.py query --live --closure
```

Decode one hypothesis, or the whole long-tail portfolio, with:

```bash
python3 src/zeta23_kg_cache.py query H2 --closure
python3 src/zeta23_kg_cache.py query --portfolio
```

The source file `zeta23_kg_v2.source.json` is a compiler seed and audit
fixture; the `.zkg` plus its versioned decoder is sufficient to reconstruct
the human-readable graph.

## Deprecated v1 portability cache

The retained human narrative mirrors are:

- `../ZETA23-DISTILLED-RESEARCH-KERNEL-AND-FRONTIER-2026-08-13.md`;
- `../ZETA23-TEN-ORTHOGONAL-LONG-TAIL-HYPOTHESES-2026-08-13.md`.

`zeta23_context_cache_v1.json.gz` is the earlier portability cache containing only
the then-current August goal, invariant, constants, audited closures, surviving strict
hypotheses, and artifact pointers.  It is deliberately not a narrative log.

Load the historical default minimal state with (the CLI prints a supersession
warning):

```bash
python3 src/zeta23_context_cache.py
```

Load only selected sections with, for example:

```bash
python3 src/zeta23_context_cache.py live hypotheses
```

Decode the binary back to indented human-readable JSON with:

```bash
python3 src/zeta23_context_cache.py --pretty
```

The uncompressed JSON is retained to make the cache auditable and easy to
regenerate.  Refresh the binary after an audited state change with:

```bash
gzip -9 -c results/context/zeta23_context_cache_v1.json \
  > results/context/zeta23_context_cache_v1.json.gz
```

The v1 binary remains decodable for migration, but it is not the canonical
research state.  Neither cache is independent evidence.
