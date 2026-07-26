# Extending the machine-checked certificates: deeper and broader windows

Agent report, July 26 machine session (machine clock; house dateline convention as in
`PROGRAM.md` §2.14). Task: extend `lean/weilcert`'s kernel-verified positivity window
(ζ, L = 497/200, m = 12) to (1) the same window at spectral depth m = 24 — the p = 3
window at the 1e-10 scale, (2) a family window χ₋₇ at L = 5, m = 16 — the first
formally verified GRH-side positivity window, and (3, stretch) ζ at L = 749/250,
m = 48 — the 1e-15 scale. Every number below comes from a run executed in this
session on this machine.

## 1. What was certified

Three new Lean files under `lean/weilcert/` (new `lean_lib` targets appended to
`lakefile.toml`; `Weilcert.lean` untouched), generated and exactly pre-verified by
`lean/make_certificate_deep.py`. Each proves, from an all-integer congruence
certificate reduced entirely inside the Lean 4.32.1 kernel (`decide`; no
`native_decide`, no floats, no `sorry`):

**Theorem (per window).** Every rational m×m matrix M with |M_ij − mRat_ij| ≤ δ
entrywise, and every 0 ≠ x ∈ ℚ^m, satisfies xᵀMx > 0 — where mRat = A/DEN is the
explicit rational matrix whose integer data A is listed in the file. By continuity
the same holds for every real symmetric M in the same entrywise ball. The certificate
is c²B = Wᵀdiag(g)W, Winv·W = f·I, g > 0, f > 0, with B = A − S·I and the shift
S = m·DEN·δ exactly covering the worst-case perturbation via the rational
Cauchy–Schwarz bound |xᵀEx| ≤ m·(DEN·δ)·|x|².

| window | file / namespace | m | DEN | δ | shift S |
|---|---|---|---|---|---|
| ζ, L = 497/200 (p=3 window, 1e-10 scale) | `WeilcertDeep.lean` / `WeilCertDeep` | 24 | 10^28 | 1e-14 | 24·10^14 |
| χ₋₇, L = 5 (odd, conductor 7, GRH side) | `WeilcertFamily.lean` / `WeilCertFamily` | 16 | 10^24 | 1e-9 | 16·10^15 |
| ζ, L = 749/250 (n=4 window, 1e-15 scale) | `WeilcertDeeper.lean` / `WeilCertDeeper` | 48 | 10^30 | 1e-19 | 48·10^11 |

Exact theorem names (the certified-ball statement and the specialization to the
midpoint matrix):

- `WeilCertDeep.weil_window_positive`, `WeilCertDeep.mRat_positive`
- `WeilCertFamily.weil_window_positive`, `WeilCertFamily.mRat_positive`
- `WeilCertDeeper.weil_window_positive`, `WeilCertDeeper.mRat_positive` (see §6 for build status)

Verbatim statements (from the built files; `delta` is `1 / 10 ^ 14`, `1 / 10 ^ 9`,
`1 / 10 ^ 19` respectively, and `mRat` in each namespace is its own `aFun`
data over `10 ^ DENP`):

```lean
theorem WeilCertDeep.weil_window_positive (M : Matrix (Fin 24) (Fin 24) ℚ)
    (hM : ∀ i j, |M i j - mRat i j| ≤ delta)
    (x : Fin 24 → ℚ) (hx : x ≠ 0) : 0 < x ⬝ᵥ M *ᵥ x

theorem WeilCertFamily.weil_window_positive (M : Matrix (Fin 16) (Fin 16) ℚ)
    (hM : ∀ i j, |M i j - mRat i j| ≤ delta)
    (x : Fin 16 → ℚ) (hx : x ≠ 0) : 0 < x ⬝ᵥ M *ᵥ x

theorem WeilCertDeeper.weil_window_positive (M : Matrix (Fin 48) (Fin 48) ℚ)
    (hM : ∀ i j, |M i j - mRat i j| ≤ delta)
    (x : Fin 48 → ℚ) (hx : x ≠ 0) : 0 < x ⬝ᵥ M *ᵥ x
```

Interpretation (Bridge, as in `THEOREMS.md`): the matrix of the truncated Weil form
at the stated support, in the *unnormalized* Legendre basis b_k(x) = P_k(4x/L),
k = 0..m−1, lies entrywise within the identification bound of §3 (≪ δ) of mRat.
For the family window the form is the χ₋₇-twisted, pole-free, odd-parity form
(kernel e^{−3u/2}/(1−e^{−2u}), ψ(3/4), conductor term log(7/π)); the participating
prime powers n < e^{5/2} and their character signs — the certified window contains
both stabilizers and drains of the §2.11 sign ledger, with p = 7 itself excluded
(χ(7) = 0):

```
n= 2 (p= 2) chi_{-7}(n) = +1     n= 8 (p= 2) chi_{-7}(n) = +1
n= 3 (p= 3) chi_{-7}(n) = -1     n= 9 (p= 3) chi_{-7}(n) = +1
n= 4 (p= 2) chi_{-7}(n) = +1     n=11 (p=11) chi_{-7}(n) = +1
n= 5 (p= 5) chi_{-7}(n) = -1
```

For the two ζ windows the participating prime powers are {2, 3} (L = 497/200) and
{2, 3, 4} (L = 749/250); the ζ pole term is included in both.

## 2. Axiom audits (verbatim)

`lake env lean` on `#print axioms` files, after green builds:

```
'WeilCertDeep.weil_window_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCertDeep.mRat_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCertDeep.key_int' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCertDeep.winv_int' depends on axioms: [propext, Classical.choice, Quot.sound]
```

```
'WeilCertFamily.weil_window_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCertFamily.mRat_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCertFamily.key_int' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCertFamily.winv_int' depends on axioms: [propext, Classical.choice, Quot.sound]
```

```
'WeilCertDeeper.weil_window_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCertDeeper.mRat_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCertDeeper.key_int' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCertDeeper.winv_int' depends on axioms: [propext, Classical.choice, Quot.sound]
```

No `Lean.ofReduceBool`/`Lean.trustCompiler` (hence no `native_decide`), no `sorryAx`,
in any of the three. A final combined audit importing all four libraries (the three
new ones plus the original `Weilcert`) reproduced all thirteen lines, including
`'WeilCert.weil_window_positive' depends on axioms: [propext, Classical.choice,
Quot.sound]` for the existing m = 12 theorem.

## 3. Measured margins, shifts, and identification budgets

Float/mpmath measurements (this session; `spectral_form` at 50 dps, eigensolve at 40):

| window | λ_min (G-normalized) | λ_min (unnormalized matrix) | S/DEN = m·δ | headroom λ_un/(m·δ) |
|---|---|---|---|---|
| ζ 497/200, m=24 | 3.868816e-10 | 1.467018e-10 | 2.4e-13 | 611× |
| χ₋₇ 5, m=16 | 3.549611e-06 | 4.044711e-06 | 1.6e-8 | 253× |
| ζ 749/250, m=48 | 4.346216e-15 | 1.663204e-15 | 4.8e-18 | 346× |

(χ₋₇ at m = 40 reproduces the task's 7.569911e-07; m = 16 is larger, as expected
for a shallower Galerkin space. The two ζ normalized values reproduce
`certified_spectral.py`'s EXPECTED table.)

The generator (`lean/make_certificate_deep.py`) extracts the 220-bit interval
endpoints as exact Fractions from the raw mpf tuples, rounds midpoints to the 1/DEN
grid in exact integer arithmetic, and asserts the *exact* identification bound
|A/DEN − Q_true| ≤ 0.5/DEN + max halfwidth:

| window | exact identification bound | δ | margin |
|---|---|---|---|
| ζ m=24 | 4.948e-29 | 1e-14 | 2.0e14× |
| χ₋₇ m=16 | 4.933e-25 | 1e-9 | 2.0e15× |
| ζ m=48 | 4.998e-31 | 1e-19 | 2.0e11× |

Every certificate identity (c²B = Wᵀdiag(g)W entrywise, Winv·W = f·I entrywise,
g > 0, LDLᵀ pivots > 0) was verified exactly in Fraction/integer arithmetic before
emission; any failure aborts with no file written. All three windows passed.

Certified two-sided G-normalized enclosures (interval Cholesky + interval Rayleigh,
220-bit, `src/certified_spectral.certify_spectral`, run this session):

```
zeta  L=497/200 m=24: CERTIFIED 3.86870000e-10 < lam_min <= 3.86881560e-10 : True  (23 s)
chi-7 L=5 m=16      : CERTIFIED 3.54950000e-06 < lam_min <= 3.54961108e-06 : True  (27 s)
zeta  L=749/250 m=48: CERTIFIED 4.34600000e-15 < lam_min <= 4.34621580e-15 : True  (206 s)
```

The first and third lines reproduce the module's EXPECTED values; the second is a
new certified number (the first certified χ window at L = 5 in the spectral basis
at m = 16; §2.17's family certificate at this L was (7.569, 7.56991097]e-7 at
m = 40).

Independent cross-validation of the emitted data (this session): the integers `aFun`
parsed back out of the two built Lean files were compared entrywise against the
float Gauss–Legendre pipeline (`src/spectral_margins.spectral_form`, a fully
separate code path from the exact-rational/interval generator), after conversion to
the unnormalized basis:

```
family chi_-7 L=5 m=16:  max |A/DEN - float-GL| over all 256 entries = 0.00e+00
deep   zeta L=497/200 m=24: max |A/DEN - float-GL| over all 576 entries = 3.12e-17
```

i.e. agreement to the float pipeline's own double-precision resolution.

## 4. Integer-size table

Maximum decimal digit counts of the emitted certificate data ("data chars" = total
characters of all integers; file size includes Lean boilerplate):

| window | A | W | Winv | g | c | f | data | .lean file | lines |
|---|---|---|---|---|---|---|---|---|---|
| ζ m=12 (existing, DEN 10^24) | 24 | 101 | 604 | 1226 | 602 | 602 | 0.042 MB | 60 KB | 761 |
| χ₋₇ m=16 (DEN 10^24) | 24 | 162 | 1285 | 2589 | 1283 | 1283 | 0.14 MB | 160 KB | 1107 |
| ζ m=24 (DEN 10^28) | 28 | 288 | 3380 | 6779 | 3377 | 3377 | 0.69 MB | 729 KB | 2075 |
| ζ m=48 (DEN 10^30) | 30 | 644 | 15151 | 30319 | 15145 | 15145 | 10.48 MB | 10.6 MB | 7283 |

(m = 12 row: measured by parsing the integers back out of the checked-in
`Weilcert.lean` this session; all others measured by the generator.)

## 5. Build and decide times

Green builds (`lake build <lib>`; "Build completed successfully" + axiom audit is
the only accepted success criterion — both obtained for all three new windows):

| build | wall | peak RSS |
|---|---|---|
| `lake build WeilcertFamily` (m=16) | 23.2 s | 7.0 GB |
| `lake build WeilcertDeep` (m=24) | 44.6 s | 7.7 GB |
| `lake build WeilcertDeeper` (m=48, third attempt, §6) | 10 min 17.5 s | 18.8 GB |

Per-declaration profile (`lake env lean -Dprofiler=true`), decide tactic execution
plus kernel type checking of the two big lemmas:

| file | key_int decide | key_int kernel | winv_int decide | winv_int kernel |
|---|---|---|---|---|
| m=16 (idle machine) | 3.07 s | 1.50 s | 2.77 s | 1.33 s |
| m=24 (idle machine) | 11.6 s | 6.98 s | 10.7 s | 6.96 s |
| m=48 (light load) | 218 s | 105 s | 219 s | 81.1 s |
| m=12 (loaded machine*) | 5.6 s | 3.12 s | 5.81 s | 3.48 s |

*The m = 12 baseline profile was taken while the m = 48 build and a second agent's
lake builds were running (import alone took 18.8 s vs 2.7 s idle), so it is inflated
roughly 2×; the m = 16/24 rows were taken on a quiet machine and are the comparable
pair, and the m = 48 row was profiled in a rerun after the builds drained. All
decide lemmas ran under `set_option maxHeartbeats 8000000` (1600000000 for m = 48,
both per-lemma and file-level — see §6).

At m = 48 a third cost appears that is invisible at m ≤ 24: *elaboration of the
data definitions themselves* — the equation compiler on the 2304-case matches took
8.98 s (`aFun`, 30-digit literals), 13 s (`wFun`, ≤ 644 digits), 35.7 s (`gFun`,
48 cases but ≤ 30319-digit literals), and 158 s (`wiFun`, 2304 cases × ≤ 15151
digits) — comparable to the decides. Data-definition elaboration, decide
evaluation, and kernel certification split the m = 48 build roughly 25% / 50% / 22%.

## 6. The m = 48 stretch window

The certificate itself (integer data + exact Fraction verification) succeeded on
the first try in 78 s of Python (71 s enclosures + 7 s exact LDLᵀ/inverse), with
g ≤ 30319 digits — under the ~50k-digit report-and-stop threshold — so the Lean
build was attempted. Two failure modes were hit and identified before the final
outcome; both are size walls of the toolchain, not of the kernel:

- **Attempt 1** (file exactly in the m = 12/16/24 style): the *IR compiler*, not
  the kernel, died lowering the 2304-case `wiFun` with ≤ 15151-digit literals —
  `error: WeilcertDeeper.lean:4647:4: (deterministic) timeout at 'transform',
  maximum number of heartbeats (200000) has been reached` followed by cascading
  `failed to compile definition, consider marking it as 'noncomputable' because it
  depends on 'wiFun'`. Codegen for the data functions is irrelevant to `decide`
  (which uses only the kernel term), so the fix is to skip it.
- **Attempt 2** (`noncomputable section` around the whole development + file-level
  `set_option maxHeartbeats 1600000000`): all data definitions elaborate; the two
  Fin-48 double-forall decides then failed with `error: WeilcertDeeper.lean:7047:66:
  maximum recursion depth has been reached` (elaborator default `maxRecDepth 512`;
  the m = 24 decidability chain fits under it, the m = 48 one does not). The three
  scalar decides (`g_pos`, `f_pos`, `c_pos`) passed.
- **Attempt 3** adds `set_option maxRecDepth 16384` (file-level): **green build** —
  `Build completed successfully`, wall 10 min 17.5 s, peak RSS 18.8 GB, followed by
  the clean axiom audit of §2. The certificate at the 1e-15 scale is therefore
  fully kernel-verified: `WeilCertDeeper.weil_window_positive` — every rational
  (hence real symmetric) 48×48 matrix within 1e-19 entrywise of the explicit
  mRat = A/10^30 is positive definite, and the truncated Weil form of ζ at
  L = 749/250 on span{P_0..P_47} is within 5.0e-31 of mRat.

The two toolchain walls and their one-line fixes (`noncomputable section`;
`set_option maxRecDepth`) are now encoded in the generator's `bigdata` mode, so
they are paid once, not rediscovered per window.

## 7. Honesty findings

**(i) The checked-in m = 12 certificate's Bridge δ is overstated (pre-existing;
found, not introduced, by this session).** `lean/make_certificate.py` converts the
220-bit interval midpoints through `mp.mpf(...)` at the ambient dps = 15 (53-bit)
before rounding to the 10^-24 grid. Recomputing this session: 72 of 144 entries of
the emitted A differ from the correctly rounded values, by up to 14 579 244 grid
units = 1.4579e-17. The checked-in `aFun` matches the 53-bit conversion exactly, so
the checked-in `mRat` lies within ~1.46e-17 of the true Weil matrix — not within
the δ = 1e-20 claimed by the Bridge Proposition of `THEOREMS.md` (Theorem 2's
kernel statement about mRat itself is unaffected; the enclosure widths, ~5e-60, are
also fine). Consequence: as the artifacts stand, `WeilCert.weil_window_positive`
(δ = 1e-20) does not reach the true Weil matrix; the identification error exceeds
its perturbation ball by ~3 orders. The fix is one of: (a) restate the m = 12 Bridge
with δ = 1e-16 and re-run with shift 12·10^8 ≤ DEN·λ_un (ample headroom), or
(b) re-emit A at exact precision and rebuild. Per task rules this session touched
neither `Weilcert.lean` nor `THEOREMS.md`; the three NEW windows do the
endpoint→integer conversion exactly in Fractions and assert the identification
bound exactly (§3), so their δ claims are honest with 10^11–10^15× margin.
Note also that the new m = 24 certificate *independently restores* the m = 12
window's intended end-to-end conclusion: the truncated Weil form at L = 497/200
in the basis P_0..P_23 has the m = 12 matrix as its top-left block (same support,
same basis functions), so positivity on the 24-dimensional space — which
`WeilCertDeep.weil_window_positive` reaches with honest δ = 1e-14 against an
exact 4.9e-29 identification bound — restricts to the 12-dimensional space by
zero-padding. The original window's mathematical content stands; only its stated
δ chain needs the one-line repair.

**(ii) Timing contamination.** A second agent was building separate Lean projects
(`lean/glide`, Bridge* libs) concurrently during parts of this session; all timing
rows above are labeled idle/loaded accordingly.

## 8. Certificate size vs depth: the scaling observation

With DEN·(matrix entries) ≈ 10^{DENP} and exact LDLᵀ over ℤ, the certificate
integers are governed by the leading principal minors of B: c ≈ f ≈ (largest
minor), g ≤ c², W ≤ (minor of the corresponding order). Measured growth
(m = 12 → 16 → 24 → 48 at DENP = 24/24/28/30):

- digits(c) = digits(f): 602 → 1283 → 3377 → 15145. The three new windows fit
  **digits(c) ≈ 0.21·m²·DENP** to ≤ 4% (predicted 1290 / 3387 / 14515 vs measured
  1283 / 3377 / 15145); the m = 12 point sits 17% below the fit (small-m regime).
  Mechanism: c is an lcm of column denominators of the exact LDLᵀ, each of the
  order of a leading principal minor (~10^{k·DENP}); their compounding over k gives
  the m² — the certificate's integers grow with the *square* of the dimension times
  the digit depth of one entry, even though the matrix data itself is only m²·DENP
  characters.
- digits(g) ≈ 2·digits(c) (g_k = D_k c²/r_k²): 1226/2589/6779/30319 =
  2.04/2.02/2.01/2.00 × digits(c) across the four windows.
- total data chars: 0.042 / 0.14 / 0.69 / 10.5 MB — the m = 48 file is 15× the
  m = 24 file from 2× the dimension (consistent with ~m² triangular entries whose
  column-k sizes grow like k·DENP, i.e. data volume ~ m³·DENP up to the lcm
  compounding above; Winv is the single largest block in every file).
- decide time: m = 16 → 24 gives 3.07 → 11.6 s ≈ 3.8× for (24/16)³ = 3.4× the
  term count with 2.6× the digits — at these sizes cost is ≈ m³ with a weak digit
  factor. m = 24 → 48 gives 11.6 → 218 s ≈ 18.8× for 8× the terms and 4.5× the
  digits — the bignum factor now contributes ≈ 2.3× on top of m³. Summary: decide
  cost ≈ m³ · (digits)^0.5±, i.e. ≈ m³·(m²·DENP)^0.5 ~ m⁴·DENP^0.5 at depth.

Practical envelope: kernel certificates of this design are comfortable to
m ≈ 24–32 (≤ 1 MB, < 1 min, default toolchain limits), and feasible at m = 48
(10.6 MB, 10 min, 18.8 GB, `noncomputable section` + raised `maxRecDepth`
required — §6). The binding constraint is the ~0.21·m²·DENP-digit lcm growth in
c/g/Winv — not the analytic enclosures (220-bit widths ~1e-60 at every depth
tested), not the eigenvalue headroom (two+ orders at every window), and not GMP
(the kernel's bignum arithmetic is far from the bottleneck). Extrapolating the
measured laws, m = 96 at DENP ≈ 32 would put g at ~124k digits and the data at
~120 MB — past reasonable. Deeper windows want either block-parity splitting (the
checkerboard structure would halve m per block: two certificates of m/2 at ~1/8
the data each), a triangular-W kernel argument replacing Winv (W is upper
triangular by construction, diagonal r_k > 0; a max-support-index argument would
delete the single largest data item and the biggest decide), or scaled-integer
LDL with bounded pivot digits (Bareiss-style common-factor removal).

## 9. Artifacts

- `lean/make_certificate_deep.py` — generator (exact-Fraction emission + exact
  re-verification; `--measure-only` mode prints the size table without writing).
- `lean/weilcert/WeilcertDeep.lean`, `lean/weilcert/WeilcertFamily.lean`,
  `lean/weilcert/WeilcertDeeper.lean` — the certificates.
- `lean/weilcert/lakefile.toml` — three appended `lean_lib` targets (plus two
  Bridge* targets appended concurrently by the other agent).
- Existing files untouched: `Weilcert.lean`, `make_certificate.py`, `THEOREMS.md`,
  `PROGRAM.md`, `RESULTS.md`, `ENVELOPE.md`, everything under `src/`.

Verification commands (from `lean/weilcert`, with elan on PATH and
`C_INCLUDE_PATH=/usr/include/x86_64-linux-gnu`):

```
lake build WeilcertDeep WeilcertFamily     # green in ~1 min total after cache
lake build WeilcertDeeper                  # green in ~10 min, needs ~19 GB RAM
cat > /tmp/check.lean <<'EOF'
import WeilcertDeep
import WeilcertFamily
import WeilcertDeeper
#print axioms WeilCertDeep.weil_window_positive
#print axioms WeilCertFamily.weil_window_positive
#print axioms WeilCertDeeper.weil_window_positive
EOF
lake env lean /tmp/check.lean
```
