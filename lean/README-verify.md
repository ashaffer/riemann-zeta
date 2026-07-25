# Verifying the WeilCert development

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

Note on the multiarch clang issue: if `lake exe cache get` fails building the
cache tool with `bits/libc-header-start.h not found`, set
`export C_INCLUDE_PATH=/usr/include/x86_64-linux-gnu` first (Ubuntu multiarch).

Regenerating the certificate data from the analytic side:
`python3` + the repository's `src/certified_spectral.py` produce the integer
data (see the generator embedded in the session record / scratch scripts);
the LDL^T pivots, the integer congruence c^2 B = W^T diag(g) W, and the
inverse identity Winv W = f I are all re-verified exactly in Fractions before
emission.
