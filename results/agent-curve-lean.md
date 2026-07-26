# agent-curve-lean — CurveCert_E5: the first fully kernel-checked END-TO-END Weil-positivity window

Date: 2026-07-26.  Task: implement the Lean certificate spec `CurveCert_E5` of
`results/experts/PLAN-algebraic-geometry.md` §"Round 2 — honing" item (d),
exactly as written.  Deliverable: `lean/weilcert/CurveCertE5.lean` (new
`lean_lib` target `CurveCertE5`, appended to `lean/weilcert/lakefile.toml`;
no other file touched).

## Pre-flight: exact-arithmetic verification of the AG spec

Every integer in the spec was re-verified in Python `fractions` before any
Lean was written.  **No discrepancies.**  Verified: the affine count 8 / N₁ = 9
/ a = −3 for E : y² = x³ + x + 1 over F₅; the power-sum recurrence values
S = (2, −3, −1, 18, …); G₂ = [[10, −15], [−15, 50]] (char poly λ² − 60λ + 275,
eigenvalues 5, 55) and G₃ (rank 2); the full Theorem A certificate
(36·B = Wᵀ diag(6, 306) W with B = G₂ − 4·1, Winv·W = 6·1, margin
n·(scale·δ) = 4 ≤ s = 4); G₃·(5, 3, 1)ᵀ = 0; the flip witness
(−7, 1)ᵀ G₂ᶠ (−7, 1) = −510; and the whole genus-2/F₇ block (N₁ = 9, N₂ = 63
over F₄₉ = F₇[w]/(w² = 3), S₁..₅ = (−1, −13, −1, −97, 244) by Newton, G₄
entries, G₅·(49, 7, 7, 1, 1)ᵀ = 0).

## What was proved (all in namespace `CurveCertE5`)

**Part 0 — the Bridge (spec B1), kernel-checked and definitional.**
The chain point count → trace → power sums → Gram matrix is *definitional*
inside Lean: `affineCount` is a `Finset.card` over `ZMod 5 × ZMod 5`;
`numPoints := affineCount + 1`; `frobTrace := 5 + 1 − numPoints`;
`powSum` is the integer recurrence S₀ = 2, S₁ = a, S_k = a·S_{k−1} − 5·S_{k−2};
`gram n := [5^{min(i,j)}·S_{|i−j|}]`.  Kernel-checked (`decide`):

- `affine_count` : the affine count equals 8 (25 checks over ZMod 5, by the kernel).
- `point_count` : N₁ = 9.  `frobTrace_eq` : a = −3.
- `bridge_g2` / `bridge_g3` : the point-count-derived `gram 2` / `gram 3`
  equal the spec's literal matrices [[10, −15], [−15, 50]] and
  [[10, −15, −5], [−15, 50, −75], [−5, −75, 250]] entrywise.

Because the certificate lemmas below are stated directly on `gram 2` / `gram 3`
(not on transcribed literals), every `decide` re-derives the point count of E
inside the kernel — the bridge is not a side remark, it is inside the checked
statements.

**Part 1 — Theorem A (`curve_window_positive`), the rung-2 window.**
Every rational 2×2 matrix M entrywise within δ = 2 of G₂ — with G₂ defined
from the kernel-computed point count — has 0 < xᵀMx for all x ≠ 0.  Proved as
an instance of the n-generic `CertFramework.cert_window_positive` (n = 2,
K = ℚ, scale = 1, δ = 2, s = 4) consuming exactly the spec's certificate
c = 6, f = 6, W = [[6, −15], [0, 1]], Winv = [[1, 15], [0, 6]], g = (6, 306);
integer facts `key_int` (36·(G₂ − 4·1) = Wᵀ diag(g) W) and `winv_int`
(Winv·W = 6·1) by `decide`.  Corollary `gram2_positive`: G₂ ≻ 0 over ℚ.

**Part 2 — Theorem B, rung 3: Cayley–Hamilton + PSD (the wall).**

- `gram3_charpoly_kernel` : `gram 3 *ᵥ frobCharPoly = 0` by `decide`, where
  `frobCharPoly := ![5, −frobTrace, 1]` — i.e. (q, −a, 1), the characteristic
  polynomial of Frobenius z² + 3z + 5 constant-coefficient-first, itself
  defined from the point count (`frobCharPoly_eq` : it equals (5, 3, 1)).
- `gram3_psd` : 0 ≤ xᵀG₃x for all rational x, via the g ≥ 0 variant of
  `CertFramework.quad_of_ldl` with the decide-checked decomposition
  4·G₃ = W₃ᵀ diag(10, 110, 0) W₃, W₃ = [[2, −3, −1], [0, 1, −3], [0, 0, 1]]
  (`key3_int`).  Third weight 0 = the wall.

Together: the rung-3 form is PSD and its kernel is the zeta function of E —
the exact statement of which the repo's keyhole (§2.13/Groskin) is the
ℚ-shadow.

**Part 3 — Theorem C (`flip_witness`, `flip_not_positive`), signing rigidity.**
`flipTrace := 5 + 1 + numPoints` (= S₁ᶠ = 15, the sign-flipped degree-1 prime
band, defined from the point count); `gram2Flip` = [[10, 75], [75, 50]]
(`bridge_flip`); `decide`: (−7, 1)ᵀ G₂ᶠ (−7, 1) = −510 < 0.  One integer
vector kills the wrong signing — the curve transplant of GT-G4(A), C5 format.

**Part 4 — optional genus-2 block (spec's "optional second block"), complete.**
C : y² = x⁵ + x + 1 over F₇ (genus 2).

- `affine_count7` : 8 affine points over F₇ (`decide`, 49 checks) ⟹ N₁ = 9.
- `affine_count49` : 62 affine points over F₄₉ (`decide`, 2401 checks) ⟹
  N₂ = 63.  F₄₉ realized as pairs (a, b) = a + b·w in ZMod 7 × ZMod 7 with
  explicit multiplication `mul49` (w² = 3; 3 is a non-residue mod 7) — no ring
  instance needed, the predicate is decidable as written.
- `powSum7` : S₁ = 8 − N₁ definitional in the F₇ count; S₂ = −13 bridged to
  the F₄₉ count by `bridge_s2` (S₂ = 7² + 1 − N₂, `decide`); S₃ = −1,
  S₄ = −97 certified by the kernel-checked Newton identities `newton_c2`,
  `newton_s3`, `newton_s4` (the functional-equation inputs c₁ = q·c₃,
  c₀ = q² are the stated classical/paper-side residue, spec B2).
- `bridge_g4` : `gram7 4` equals the spec's G₄ literal entrywise.
- `gram4_positive` : G₄ ≻ 0 over ℚ, via `CertFramework.ldl_quad_pos` with the
  certificate generated by `lean/make_certificate.py`'s exact fraction-free
  routine run on G₄: c = f = 18204, W₄ = [[4, −1, −13, −1], [0, 111, −41, −365],
  [0, 0, 82, −47], [0, 0, 0, 1]], g₄ = (579924828, 5224548, 51735768,
  2371722812424), Winv₄ as in the file (`key4_int`, `winv4_int` by `decide`).
- `gram5_charpoly_kernel` : `gram7 5 *ᵥ (49, 7, 7, 1, 1) = 0` by `decide` —
  genus-2 Cayley–Hamilton, char poly z⁴ + z³ + 7z² + 7z + 49.

## Axiom audit (verbatim, `lake env lean` on `#print axioms` for every theorem)

```
'CurveCertE5.affine_count' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.point_count' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.frobTrace_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.bridge_g2' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.bridge_g3' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.key_int' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.winv_int' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.g_pos' depends on axioms: [propext]
'CurveCertE5.key_q' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.winv_q' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.bq_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.curve_window_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.gram2_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.frobCharPoly_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.gram3_charpoly_kernel' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.key3_int' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.g3_nonneg' depends on axioms: [propext]
'CurveCertE5.key3_q' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.gram3_psd' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.bridge_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.flip_witness' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.flip_not_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.affine_count7' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.affine_count49' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.bridge_s2' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.newton_c2' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.newton_s3' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.newton_s4' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.bridge_g4' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.key4_int' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.winv4_int' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.g4_pos' depends on axioms: [propext]
'CurveCertE5.key4_q' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.winv4_q' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.gram4_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'CurveCertE5.gram5_charpoly_kernel' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The three axioms are mathlib's standard base; the three `[propext]`-only lines
are small `decide` lemmas that never touch ℚ.  Absence of
`Lean.ofReduceBool`/`Lean.trustCompiler` certifies no `native_decide`;
absence of `sorryAx` certifies completeness.

## Build

`lake build CurveCertE5` (mathlib cached): the module compiles in **~25 s**;
the full nine-target project (`Weilcert` … `CurveCertE5`) rebuilds in ~6 s
when cached.  Build is warning-free for `CurveCertE5.lean`.  Toolchain: Lean
4.32.1, mathlib pinned by `lake-manifest.json`, unchanged.

## Deviations from the AG spec (all minor, none mathematical)

1. **G₃ PSD certificate scaling.**  The spec suggests the fraction-free
   routine's pivots "10, 10·275".  I used the equivalent decide-checked
   decomposition 4·G₃ = W₃ᵀ diag(10, 110, 0) W₃ (c = 2, row scalings
   r = (2, 1, 1) applied to the exact LDLᵀ with pivots 10, 55/2, 0) — same
   congruence content, smaller integers, identity verified exactly in
   Fractions first.
2. **G₄ certificate size.**  The spec's parenthetical "entries ≤ 5 digits"
   does not hold for the certificate the named generator actually produces:
   `make_certificate.py`'s routine on G₄ yields g-entries up to 13 digits
   (2371722812424).  I used the generator's exact output (verified in
   Fractions); harmless for kernel `decide`.  Flagged only because the spec
   sentence overstates compactness.
3. **Genus-2 S₂ is bridged, not definitional.**  `powSum7 2` is the literal
   −13 with the kernel-checked bridge theorem `bridge_s2` equating it to
   7² + 1 − N₂, rather than being defined through `numPoints49` — otherwise
   every later `decide` would re-run the 2401-element F₄₉ count in the
   kernel.  Every link is still a kernel-checked theorem.  (For E/F₅ the
   chain is fully definitional; the 25-element count is re-derived inside
   every `decide` at negligible cost.)
4. **Theorem A′ (certified value of λ_min(T₂)) not implemented** — the spec
   lists it as optional "if the Lean seat wants it".  The margin-value caveat
   is instead stated verbatim in the file header: Theorems A/B certify
   positivity/kernel of G_n, hence the SIGN of the rung margin; the diagonal
   congruence does not preserve eigenvalues, so no two-sided enclosure of
   λ_C(L) = ln q·λ_min(T_n) is claimed.

## What the artifact means

This is the program's first END-TO-END kernel-checked Weil-positivity window:
for the function-field object E : y² = x³ + x + 1 / F₅, both halves — the
matrix positivity (rung-2 window, rung-3 PSD + kernel) AND the bridge from
the arithmetic object to the matrix (point count over ZMod 5 → Frobenius
trace → power sums → Rosati Gram matrix) — are verified by the Lean kernel
under the three standard axioms, with no interval arithmetic, no floats, and
no `native_decide` anywhere in the chain; the only unformalized remainder is
the classical paper-side reduction (Parseval–Zak, AG-1 Steps 2–4, plus
P_E(T) = 1 − aT + qT² from Riemann–Roch), which contains no computation.  By
contrast, the ζ-side artifacts (`Weilcert.lean` and descendants) remain
computer-assisted at the bridge: their matrix positivity is kernel-checked,
but the identification of the matrix with the truncated Weil form of ζ rests
on 220-bit outward-rounded interval arithmetic outside Lean (Bridge
Proposition, THEOREMS.md).  The curve window is the degenerate w = 0 test
article of the CS-2 contract — the clean end-to-end shape the ζ pipeline is
being redesigned toward — and the genus-2/F₇ block shows the same chain
surviving its first nontrivial stress (two counted primes, a 2401-check
bridge count in F₄₉, 13-digit certificate integers).
