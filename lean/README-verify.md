# Verifying the Lean developments

Two independent lake projects:

## 2. GlideKernel (lean/glide) — the archimedean kernel sandwich

```
cd lean/glide && lake exe cache get && lake build     # ~20 s after cache
lake env lean <file with: import Glide.Basic, #print axioms GlideKernel.kernel_lower, ...>
```
Verified output (2026-07-26):
```
'GlideKernel.kernel_lower'  depends on axioms: [propext, Classical.choice, Quot.sound]
'GlideKernel.kernel_upper'  depends on axioms: [propext, Classical.choice, Quot.sound]
'GlideKernel.frullani_cos'  depends on axioms: [propext, Classical.choice, Quot.sound]
'GlideKernel.laplace_sin'   depends on axioms: [propext, Classical.choice, Quot.sound]
```
Content: ½log(1+4r²) ≤ ∫₀^∞ e^{−t/4}(1−cos(rt/2))/(1−e^{−t}) dt ≤ ½log(1+4r²)+8
for all real r — Lemma A of THEOREMS.md in integral form (the digamma
identification awaits Gauss's formula in mathlib; RH-LEMMA-MAP.md Level 2) —
plus the Laplace transform of sine and the Frullani-type integral as
standalone formalized lemmas.

# 1. Verifying the WeilCert development

Toolchain: Lean 4.32.1 (via elan), mathlib pinned by `weilcert/lake-manifest.json`.

```
cd lean/weilcert
lake exe cache get     # fetch mathlib oleans (~8.6k files)
lake build             # compiles Weilcert.lean; ~10 s after cache
```

Axiom audit (the entire point — run it yourself):

```
$ cat > /tmp/check.lean <<'EOF'
import Weilcert
#print axioms WeilCert.weil_window_positive
#print axioms WeilCert.mRat_positive
#print axioms WeilCert.key_int
EOF
$ lake env lean /tmp/check.lean
'WeilCert.weil_window_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCert.mRat_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCert.key_int' depends on axioms: [propext, Classical.choice, Quot.sound]
```

`propext, Classical.choice, Quot.sound` are the three standard axioms of
mathlib; the absence of `Lean.ofReduceBool`/`Lean.trustCompiler` certifies that
no `native_decide` was used (all integer computations were reduced by the
kernel), and the absence of `sorryAx` certifies completeness.

What is proved, in one sentence: every rational (hence, by density, real
symmetric) 12x12 matrix within 1e-20 entrywise of the explicit matrix `mRat`
has a strictly positive quadratic form; by the Bridge Proposition of
`../THEOREMS.md` (computer-assisted, interval arithmetic, trust base stated
there), the truncated Weil form of zeta at support L = 497/200 in the
12-dimensional Legendre test space is such a matrix.

Further weilcert targets (same project, same audit procedure — full audits in
`../../results/`): `WeilcertDeep` (m=24, δ=1e−14), `WeilcertDeeper` (m=48,
δ=1e−19; ~10-min kernel check), `WeilcertFamily` (χ₋₇, L=5, m=16 — first
GRH-side window), `BridgeLegendre`/`BridgeOverlap` (49 overlap identities),
`CertFramework`/`CertInstance` (n-generic framework), and `CurveCertE5` —
the **first end-to-end kernel-checked window** (curve E: y²=x³+x+1 over F₅):
the point count #E(F₅)=9 is itself computed by `decide` over `ZMod 5` and the
Gram matrices are *defined* from it, so positivity (rung 2), the
Cayley–Hamilton kernel vector (rung 3), the sign-flip witness, and the
genus-2/F₇ block carry NO interval-arithmetic trust base at all (36 theorems,
audit in `../../results/agent-curve-lean.md`; build `lake build CurveCertE5`).

Note on the multiarch clang issue: if `lake exe cache get` fails building the
cache tool with `bits/libc-header-start.h not found`, set
`export C_INCLUDE_PATH=/usr/include/x86_64-linux-gnu` first (Ubuntu multiarch).

Regenerating the certificate data from the analytic side:
`python3` + the repository's `src/certified_spectral.py` produce the integer
data (see the generator embedded in the session record / scratch scripts);
the LDL^T pivots, the integer congruence c^2 B = W^T diag(g) W, and the
inverse identity Winv W = f I are all re-verified exactly in Fractions before
emission.
