# Z23C/Z23V correction-context format

Status: version 1, 2026-09-03.  This is a context-resumption format, not a
mathematical proof format.

## Authority chain

```text
Z23C text ledger     canonical compact semantic source
  -> JSON            deterministic audit/interchange projection
  -> Z23V            deterministic random-access runtime projection
  -> Markdown        human mathematical projection
  -> Lean            formal finite algebra/logic/domain guards
```

The Markdown and Lean files remain necessary: the generated projections do
not promote analytic claims into theorems.  The correction verifier parses
Z23C first, regenerates JSON and Z23V byte-for-byte, and then checks the
Markdown/Lean mappings.

## Z23C/1

Z23C is UTF-8 with LF endings.  Records are tab-delimited.  Literal backslash,
tab, newline, and carriage return in fields use `\\`, `\t`, `\n`, and `\r`.
Unknown escapes and opcodes fail closed.

The header is:

```text
Z23C  1  zeta23_correction_bundle_v1  YYYY-MM-DD
```

The canonical opcode order is:

```text
P                 path alias
H / LA            human and Lean authorities
G                 four global statuses
Y / YI            formal scope, nonclaim, verifier, correction IDs
C                 correction ID, state, exact compact claim
CT/CA/CF/CR/CL    trust/source/formal-scope/debt/Lean modifiers
I/D/N/O           invariants, proof debts, next targets, operational debts
RS/RH/RX          lossy resumption state, hypotheses, prohibitions
RV                named reload-vector membership
V/VA              observed verification and axiom ledger
S                 source
X                 SHA-256 of canonical sorted semantic JSON
```

The parser rejects duplicate IDs/modifiers, path traversal, missing terminal
digest, records after the digest, noncanonical ordering, and a semantic hash
mismatch.

## Z23V/1

Z23V is uncompressed.  It is allowed to occupy more bytes than Z23C because
its objective is bounded selective decoding, not storage compression.  All
integers are little-endian except unsigned vector entries, which use LEB128.

The fixed header is Python struct
`<4sHHIIIQQQQQ32s32s32s`.  It contains magic/version, flags, record and string
counts, region offsets, exact file size, the Z23C byte digest, semantic digest,
and a digest of every byte following the header.

The sorted fixed-width record directory uses `<HHIQQQ`:

```text
kind, key, flags, absolute payload offset, payload length,
SHA-256(kind || key || payload) truncated to 64 bits
```

Each payload is a typed integer vector.  Correction records use their numeric
`Cnn` suffix as the directory key.  Other kinds separately address metadata,
global guards, synchronization, invariants, debts, next actions, operations,
verification, sources, the lossy resumption capsule, and named vectors.

The fixed-width string directory uses `<QII>`:

```text
absolute UTF-8 offset, byte length, CRC-32
```

String IDs are one-based.  Zero is reserved for an absent optional correction
field.  Strings are deduplicated and sorted, so compilation is deterministic.

## Selective integrity and lossiness

A selected query reads the header, binary-searches only the required directory
entries, validates each selected vector digest, and reads only its referenced
string entries and bytes.  It deliberately does not hash the whole file.
Consequently corruption in an unselected record does not prevent an unrelated
query; querying the damaged record fails.  Full verification regenerates the
index, compares exact bytes, checks the complete body digest, and decodes every
record.

The `resume` vector is a lossy summary of conclusions and decision state.  It
does not contain latent activations, private reasoning, or proof evidence.
Exact claims and formal theorem names remain addressable by correction ID.

## Commands

```text
python3 src/zeta23_correction_context.py build
python3 src/zeta23_correction_context.py verify
python3 src/zeta23_correction_context.py resume
python3 src/zeta23_correction_context.py query C02 C05
python3 src/zeta23_correction_context.py query --vector math
python3 src/zeta23_correction_context.py vectors
```
