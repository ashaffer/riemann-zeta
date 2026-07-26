# Formalizing the Bridge Proposition — analytic side, session report

Agent session, July 26, 2026.  Task: begin formalizing the Bridge Proposition
of `THEOREMS.md` — the analytic identification connecting the kernel-checked
matrix theorem (`WeilCert.weil_window_positive`) to the truncated Weil form —
starting from its analytically simplest ingredient, the universal
shifted-overlap polynomials, plus a dimension-generic certificate framework
and a precise formalization gap-map for everything that remains.

Toolchain: Lean 4.32.1, mathlib pinned by `lean/weilcert/lake-manifest.json`
(the repository's existing project).  Every claim below reflects an actual
run on this machine.

New files (all under the existing package, nothing existing modified except
append-only `[[lean_lib]]` entries in `lean/weilcert/lakefile.toml`):

| file | lines | role |
|---|---|---|
| `lean/weilcert/BridgeLegendre.lean` | 159 | Legendre polynomials over ℚ by the Bonnet recurrence; degree + leading-coefficient theory |
| `lean/weilcert/BridgeOverlap.lean`  | 5015 (generated) | the overlap polynomials `F_kj` (exact `F_poly` data) and their proved integral identities, `k ≤ j`, `k+j ≤ 12` (49 pairs); scaled form; cross-checks |
| `lean/weilcert/CertFramework.lean`  | 256 | the certificate calculus of `Weilcert.lean` at arbitrary `n` over an arbitrary linearly ordered field |
| `lean/weilcert/CertInstance.lean`   | 48  | re-derivation of the 12-dim kernel-checked window through the generic framework |
| `lean/gen_bridge_overlap.py`        | 391 | generator: reads `src/certified_spectral.py`'s `F_poly`/`leg` (exact `Fraction`s), emits `BridgeOverlap.lean` with full FTC proofs |

Build (defaultTargets untouched, so `lake build` still builds `Weilcert` alone):

```
export PATH="$HOME/.elan/bin:$PATH"
export C_INCLUDE_PATH=/usr/include/x86_64-linux-gnu
cd lean/weilcert
lake build BridgeLegendre BridgeOverlap CertFramework CertInstance
```

Measured: `BridgeLegendre` 8 s, `BridgeOverlap` 53 s at `k+j ≤ 8` and
~217 s at the final `k+j ≤ 12`, `CertFramework` 13 s, `CertInstance` 4.5 s
(after the mathlib cache).  `grep -c sorry` over all four files: 0.

Note: `WeilcertDeep.lean`, `WeilcertFamily.lean`, `WeilcertDeeper.lean` and
their lakefile entries are concurrent work by other sessions, not part of
this report; nothing here depends on them.  Other sessions were also
editing repository files (including `Weilcert.lean`) while this one ran;
this session itself modified nothing pre-existing except the append-only
lakefile entries.  The final full build
(`lake build Weilcert BridgeLegendre BridgeOverlap CertFramework
CertInstance`, "Build completed successfully (8664 jobs)") and the 84/84
axiom audit were both re-run *after* the latest concurrent edit of
`Weilcert.lean` visible at that time (mtime 10:02:21), so every claim in
§1 holds against that state of the repository.

---

## 1. What compiled (theorem inventory + verbatim axiom audit)

### 1.1 `BridgeLegendre.lean` (namespace `Bridge`)

Mathlib (this pin) has **no plain Legendre polynomials** — only
`Polynomial.shiftedLegendre : ℕ → ℤ[X]`
(`Mathlib/RingTheory/Polynomial/ShiftedLegendre.lean`, = `P_n(1−2x)`, with
`coeff_shiftedLegendre`, `degree_shiftedLegendre`,
`factorial_mul_shiftedLegendre_eq` (Rodrigues), `shiftedLegendre_eval_symm`;
no recurrence, no orthogonality, no leading-coefficient lemma in the P_n
normalization).  So `legendre : ℕ → ℚ[X]` is defined here by the Bonnet
recurrence used by the certificate generator (`src/certified_spectral.py`,
`leg`):

```
legendre 0 = 1,  legendre 1 = X,
legendre (n+2) = C ((2n+3)/(n+2)) * (X * legendre (n+1)) - C ((n+1)/(n+2)) * legendre n
```

Proved (all by a simultaneous two-step induction `natDegree_coeff_aux`):

* `Bridge.natDegree_legendre : (legendre n).natDegree = n`
* `Bridge.degree_legendre : (legendre n).degree = n`
* `Bridge.leadingCoeff_legendre :
     (legendre n).leadingCoeff = (n.centralBinom : ℚ) / 2 ^ n`
  (the classical `(2n)!/(2ⁿ n!²)`; proved against mathlib's
  `Nat.succ_mul_centralBinom_succ`)
* `Bridge.coeff_legendre_self`, `Bridge.coeff_legendre_self_pos`,
  `Bridge.legendre_ne_zero`, `Bridge.leadingCoeff_legendre_pos`
* `Bridge.aeval_legendre_add_two` — the recurrence under evaluation in any
  commutative ℚ-algebra (the workhorse for the ℝ-evaluation lemmas).

### 1.2 `BridgeOverlap.lean` (generated; namespace `Bridge`)

For every pair `k ≤ j` with `k + j ≤ 12` (49 pairs — the task asked for
`k+j ≤ 4`, which is the 9-pair subset), with `Fovl_k_j : ℚ[X]` carrying the
*exact* rational coefficients of `src/certified_spectral.py`'s `F_poly(k,j)`:

```
theorem Bridge.overlap_k_j (v : ℝ) :
    (∫ t in (-1 : ℝ)..(1 - v), aeval t (legendre k) * aeval (t + v) (legendre j))
      = aeval v Fovl_k_j
```

proved for all real `v` (both sides are polynomials in `v`, so no
`v ∈ [0,2]` restriction is needed).  Proof route, fully inside Lean, no
numerics: rewrite the integrand into explicit bivariate form (generated
`aeval_legendre_n` evaluation lemmas, `n ≤ 12`), exhibit the explicit
polynomial antiderivative `A_kj(x, v)` (generated), establish
`HasDerivAt` by a chain of
`hasDerivAt_pow` / `HasDerivAt.const_mul` / `HasDerivAt.add` transported by
`HasDerivAt.congr_deriv`, apply
`intervalIntegral.integral_eq_sub_of_hasDerivAt` (integrability by
`fun_prop` + `Continuous.intervalIntegrable`), and close the endpoint
algebra with `push_cast; ring`.

The generator independently recomputes `F = A(1−v,v) − A(−1,v)` in
`Fraction` arithmetic and asserts exact equality with `F_poly(k,j)` before
emitting — so the Lean-proved data is byte-identical to the certificate
pipeline's.

Also proved:

* `Bridge.overlap_scaled` — the change of scale to the ledger's basis
  `b_k(x) = P_k(x/a)`, `a = L/4`: for any pair with a proved overlap
  identity and any `a > 0`,
  `∫ x in (-a)..(a-u), b_k(x) b_j(x+u) dx = a * F_kj(u/a)` —
  exactly the `T_kj(u) = a F_kj(u/a)` used by the Bridge Proposition
  (via `intervalIntegral.integral_comp_div`).
* `Bridge.shiftedLegendre_cross_check_{zero..four}` :
  `aeval x (Polynomial.shiftedLegendre n) = aeval (1 - 2*x) (legendre n)`
  (`n ≤ 4`, `x : ℝ`) — an independent cross-check of this file's Legendre
  normalization against mathlib's own (differently defined) polynomials,
  playing the role the Gauss–Legendre overlap engine plays for `F_poly` in
  the Python pipeline.
* `Bridge.aeval_legendre_{zero..twelve}` — explicit ℝ-evaluations
  (e.g. `aeval x (legendre 4) = (35/8)x⁴ − (15/4)x² + 3/8`).

Orthogonality remark: `F_kj(0) = ∫_{−1}^{1} P_k P_j` — the proved data's
constant terms (`Fovl_0_0` const 2, `Fovl_1_1` const 2/3, `Fovl_2_2` const
2/5, zero for `k ≠ j`) — so the Gram diagonal `2a/(2k+1)` of the ledger is
already contained in the proved identities as the `v = 0` specialization.

Extension state: `k+j ≤ 12` (49 pairs, `F` degree ≤ 13) is compiled and
audited; pairs with `k+j ≥ 9` need the generator-emitted local
`set_option maxHeartbeats 1600000` (see §2(f)).  The full certificate basis
(`m = 12`) needs even `k+j ≤ 22`; the generator covers it mechanically
(`python3 lean/gen_bridge_overlap.py 22`), the remaining question being
only the elaboration time of the degree-≤23 `ring` identities (measured
growth 53 s → 217 s from `k+j ≤ 8` to `≤ 12` for the whole file).

### 1.3 `CertFramework.lean` (namespace `CertFramework`)

The complete certificate calculus of `Weilcert.lean`, at arbitrary dimension
`n` over an arbitrary linearly ordered field
(`[Field K] [LinearOrder K] [IsStrictOrderedRing K]` — mathlib has removed
`LinearOrderedField` in this pin; the first two lemmas need only
`[CommRing K]`):

* `CertFramework.quad_of_ldl` — lifted verbatim (was already n-generic).
* `CertFramework.pert_bound` — `|xᵀEx| ≤ n·d·⟨x,x⟩` (via
  `sq_sum_le_card_mul_sum_sq`).
* `CertFramework.resolve`, `CertFramework.y_exists` — reconstruction and
  injectivity from `Wi·W = f·1`, `f ≠ 0`.
* `CertFramework.ldl_quad_pos` — strict positivity from the congruence
  `c²A = Wᵀ diag(g) W`, `g > 0`, `c ≠ 0`.
* `CertFramework.cert_window_positive` — the full window theorem: data
  `(A, W, Wi, g, c, f, s, scale, δ)` with the kernel-checkable hypotheses
  and the margin condition `n·(scale·δ) ≤ s` give
  `0 < xᵀMx` for every `M` entrywise within `δ` of `A/scale` and every
  `x ≠ 0`.  A future window certificate (any `n`, any `L`) supplies only
  integer data plus `decide`-checked identities.

### 1.4 `CertInstance.lean` (namespace `CertInstance`)

Consistency check — the existing kernel-checked window re-derived through
the framework, consuming `Weilcert.lean`'s own `key_q`, `winv_q`, `g_pos`,
`f_pos`, `c_ne` (margin condition `12·(10²⁴·10⁻²⁰) = 120000 ≤ 120000` by
`norm_num`):

* `CertInstance.weil_window_positive_via_framework` (same statement as
  `WeilCert.weil_window_positive`)
* `CertInstance.mRat_positive_via_framework`

### 1.5 Verbatim axiom audit

Reproduce with `lake env lean <file>` on a file of `#print axioms` lines
(the exact file used is regenerable from the list below).  Output obtained
on this machine — **84 of 84 theorems, no exceptions** (8 BridgeLegendre +
13 `aeval` + 5 cross-checks + 49 overlaps + `overlap_scaled` + 6
CertFramework + 2 CertInstance + `WeilCert.weil_window_positive` re-checked
untouched); the absence of `sorryAx` certifies completeness, the absence of
`Lean.ofReduceBool` / `Lean.trustCompiler` certifies no `native_decide`:

```
'WeilCert.weil_window_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'Bridge.legendre' depends on axioms: [propext, Classical.choice, Quot.sound]
'Bridge.natDegree_legendre' depends on axioms: [propext, Classical.choice, Quot.sound]
'Bridge.degree_legendre' depends on axioms: [propext, Classical.choice, Quot.sound]
'Bridge.leadingCoeff_legendre' depends on axioms: [propext, Classical.choice, Quot.sound]
'Bridge.coeff_legendre_self' depends on axioms: [propext, Classical.choice, Quot.sound]
'Bridge.legendre_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'Bridge.aeval_legendre_add_two' depends on axioms: [propext, Classical.choice, Quot.sound]
'Bridge.aeval_legendre_zero' ... 'Bridge.aeval_legendre_twelve'  (13 lines, identical axiom set)
'Bridge.shiftedLegendre_cross_check_zero' ... '_four'            (5 lines, identical axiom set)
'Bridge.overlap_0_0' ... 'Bridge.overlap_6_6'                    (49 lines, identical axiom set)
'Bridge.overlap_scaled' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.quad_of_ldl' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.pert_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.resolve' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.y_exists' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.ldl_quad_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.cert_window_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertInstance.weil_window_positive_via_framework' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertInstance.mRat_positive_via_framework' depends on axioms: [propext, Classical.choice, Quot.sound]
```

(The elided ranges were printed in full in the actual run; every one of the
84 lines reads `[propext, Classical.choice, Quot.sound]`.  Machine check:
`grep -cv "depends on axioms: \[propext, Classical.choice, Quot.sound\]"`
over the 84-line output returned `0`.)  No `sorry` anywhere; there are no
`WIP_*.lean` files.

---

## 2. What resisted, and the exact error modes

These are the five real fights; each is reported with its exact failure so
the next session doesn't rediscover them.

**(a) `ring` cannot merge `C`-atoms in `ℚ[X]`.**  First attempt proved
explicit polynomial identities `legendre 3 = C (5/2) * X^3 - C (3/2) * X`
by `norm_num; ring`.  Failure mode (verbatim goal):

```
⊢ -(C (5 / 3) * X * C (1 / 2)) + C (5 / 3) * X ^ 3 * C (3 / 2) - X * C (2 / 3)
    = -(X * C (3 / 2)) + X ^ 3 * C (5 / 2)
```

`ring` treats `C (5/3)`, `C (3/2)`, `C (5/2)` as unrelated atoms and cannot
multiply them (`C (5/3) * C (3/2) = C (5/2)` needs `← C_mul` + `norm_num`
inside the argument, and the normal forms still fail to align).  Resolution:
drop explicit `ℚ[X]` forms entirely; state the evaluation lemmas over ℝ
(a field, where `ring` is complete for these identities) directly from
`aeval_legendre_add_two`.

**(b) `convert` flags defeq-but-not-syntactic *instance paths*.**  The FTC
step needs `HasDerivAt (fun x => A(x,v)) (f(t,v)) t` from a
`hasDerivAt_pow` chain; `convert h using 1` produced spurious goals

```
case e'_4 ⊢ Real.instAddCommGroup = Real.normedCommRing.toAddCommGroup
case e'_5 ⊢ Semiring.toModule = (NormedAlgebra.toNormedSpace ℝ).toModule
```

(the two `HasDerivAt`s elaborate the ℝ-instances along different paths;
they are definitionally equal but `convert`'s congruence works at reducible
transparency).  Resolution: `exact HasDerivAt.congr_deriv <chain> (by
push_cast; ring)` — `exact`-unification checks the function slot at default
transparency, where the instance paths and the beta-redexes from
`HasDerivAt.add` unify silently.  This is the single most useful trick in
the file.

**(c) `rw [show (2:ℕ) = 0 + 2 from rfl]` breaks the motive.**  Rewriting
the literal `2` in `aeval x (legendre 2) = … * x ^ 2 - …` also hits the
*exponent* `2`, whose `OfNat`/`NeZero` instances depend on the literal:

```
error: motive is not type correct: ... Application type mismatch: The argument
  Nat.instNeZeroSucc  has type  NeZero (1 + 1)  but is expected to have type  NeZero _a
```

Resolution: `nth_rewrite 1 [...]` — the Legendre index is always the first
ℕ-literal occurrence in the goal.

**(d) Generic ordered-field `pert_bound`: stuck instance metavariable.**
The `Fin 12`/ℚ proof of `Weilcert.lean` ported verbatim fails over generic
`K` with

```
error: typeclass instance problem is stuck  IsOrderedAddMonoid ?m.184
```

because `Finset.abs_sum_le_sum_abs` is applied before the `dotProduct` is
syntactically a `Finset.sum`.  Resolution: pre-expand
`x ⬝ᵥ E *ᵥ x = ∑ i, x i * ∑ j, E i j * x j` by
`unfold Matrix.mulVec dotProduct; rfl`, then the ported proof goes through.
Two smaller ports of the same kind: `Finset.sum_ite_eq` needs the exact
summand shape `fun i => x i * f` (not `fun _ => x j * f`), and the
`B + s•1 + E` matrix split is cleanest with the `if i = j then s else 0`
term kept as a single `ring`-atom rather than `by_cases` (the `by_cases`
route left a stray `if True then s else 0` after simp).

**(e) Small generated-proof calibration.**  `simp only [] at h2` errors
with "simp made no progress" when elaboration has already beta-reduced;
`shiftedLegendre` cross-checks need `map_ofNat` in the simp set (else
`(aeval x) 6` survives) and `ring` only for `n ≥ 1` (for `n = 0` simp
closes the goal and a trailing `ring` errors with "no goals").  Cross-check
`n = 1` failure before the fix, verbatim: `⊢ 1 + (-1 + -1) * x = 1 - 2 * x`.

**(f) `k+j ≤ 12` needs a bigger elaboration budget.**  With the default
`maxHeartbeats 200000`, the 49-pair build fails on the large pairs with

```
error: (deterministic) timeout at `«synthesize pending MVars»`, maximum number of heartbeats (200000) has been reached
error: (deterministic) timeout at `whnf`, maximum number of heartbeats (200000) has been reached
```

(first failures at degree ≥ 10 identities; whole-file attempt 167 s).
Resolution: the generator emits `set_option maxHeartbeats 1600000 in` per
overlap theorem (with the linter-required explanatory comment; kernel
checking is unaffected — this is elaboration budget only), after which the
49-pair build completes in ~217 s and all 49 identities audit clean.

---

## 3. Gap-map: the remaining Bridge ingredients in mathlib (this pin)

Legend: **exists** (usable as-is), **partial** (relevant material exists,
the needed statement does not), **absent** (nothing to build on).
Declaration names were verified by `#check` in this project's toolchain
(file `scratchpad/survey_check.lean`, compiled clean).

### (a) Bernoulli numbers and `x/(eˣ−1)` — **partial**

| item | status | mathlib declarations |
|---|---|---|
| Bernoulli numbers over ℚ | exists | `bernoulli'`, `bernoulli` (`Mathlib/NumberTheory/Bernoulli.lean`); values `bernoulli'_zero/one/two/three/four`, `bernoulli_eq_zero_of_odd`, `sum_bernoulli` |
| Generating function, *formal* | exists | `bernoulli'PowerSeries`, `bernoulli'PowerSeries_mul_exp_sub_one : bernoulli'PowerSeries A * (exp A - 1) = X * exp A`; `bernoulliPowerSeries_mul_exp_sub_one`; Bernoulli polynomials: `Polynomial.bernoulli`, `Polynomial.bernoulli_generating_function` (`Mathlib/NumberTheory/BernoulliPolynomials.lean`) |
| `z/(e^z−1)` as an *analytic* function, radius 2π, Taylor coefficients = `bernoulli n / n!` | absent | nothing; must connect `PowerSeries` identity to `HasFPowerSeriesAt` (machinery exists: `analyticAt` theory, `Complex.analyticAt_exp`, power-series composition/division) |
| Coefficient bounds (the ledger's `|c_j| ≤ 4e^{(2−s₀)π}/π^j`, hence `|g_r| ≤ 250/π^{r+1}`) | absent | route: Cauchy estimates on the circle `|z| = π` (`Complex.norm_deriv`-family / `HasFPowerSeriesOnBall.coeff_le`-style lemmas exist in the `FormalMultilinearSeries` API) |

What must be built: analyticity of `u ↦ u/(e^u−1)` on `|u| < 2π` with
identified Taylor coefficients; a Cauchy-type bound giving the explicit
geometric coefficient estimate; then the ledger's kernel split
`w(u) = 1/(2u) + g(u)` with the rigorous tail `|g − G_N| ≤ 250/π · (2a/π)^{N+1}/(1 − 2a/π)`
is finite algebra over the proved `F` polynomials (the `I₁` part —
`∫ H(u)/(2u)` — is *already* exact rational calculus on `Fovl` data).

### (b) Gauss's integral for digamma — **absent, but the landscape moved**

Confirmed absent, and now an *explicitly recorded upstream TODO*: mathlib
gained `Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean` (copyright
2026, T. Browning) whose header reads "TODO: Prove Gauss' integral
representation of the digamma function."  What **does** exist now:

| item | declarations |
|---|---|
| digamma (ℂ) | `Complex.digamma : ℂ → ℂ` (= `logDeriv Gamma`), `Complex.digamma_def`, `Complex.digamma_zero` |
| special values | `Complex.digamma_one : digamma 1 = -Real.eulerMascheroniConstant`; `Complex.digamma_one_half : digamma (1/2) = -2 * log 2 - Real.eulerMascheroniConstant` |
| recurrence | `Complex.digamma_apply_add_one : digamma (s+1) = digamma s + s⁻¹` |
| meromorphy | `Complex.meromorphic_digamma` |
| Γ-derivative facts | `Real.hasDerivAt_Gamma_one : HasDerivAt Gamma (-γ) 1`, `Real.hasDerivAt_Gamma_one_half : HasDerivAt Gamma (-√π * (γ + 2 * log 2)) (1/2)`, `Real.deriv_Gamma_nat`, `Real.eulerMascheroniConstant_eq_neg_deriv : γ = -deriv Gamma 1` (`Mathlib/NumberTheory/Harmonic/GammaDeriv.lean`); `Complex.differentiableAt_Gamma` |
| Γ functional equations | `Complex.Gamma_add_one`, `Complex.Gamma_nat_eq_factorial`, reflection `Complex.Gamma_mul_Gamma_one_sub`, duplication `Complex.Gamma_mul_Gamma_add_half`, `Real.Gamma`-mirrors (`Mathlib/Analysis/SpecialFunctions/Gamma/{Basic,Beta,BohrMollerup,Deriv}.lean`) |

Missing for the Bridge: (i) Gauss's formula
`Re ψ(a+ir/2) − ψ(a) = ∫₀^∞ e^{−at}(1−cos(rt/2))/(1−e^{−t}) dt` (Lemma A(i)
of `THEOREMS.md`) — the identity on which the entire x-space archimedean
reduction of §2.14 rests; (ii) the closed form
`ψ(1/4) = −γ − π/2 − 3 log 2` — now *derivable inside mathlib* by
differentiating reflection + duplication (all four ingredients
`digamma_one_half`, `Gamma_mul_Gamma_one_sub`, `Gamma_mul_Gamma_add_half`,
`digamma_apply_add_one` are present; the differentiated identities are not).

### (c) Numeric bounds available — **mixed; γ is the bottleneck**

| constant | status | declarations, precision |
|---|---|---|
| π | exists, 20 digits | `Real.pi_gt_d20 : 3.14159265358979323846 < π`, `Real.pi_lt_d20 : π < 3.14159265358979323847` (`Mathlib/Analysis/Real/Pi/Bounds.lean`); also `pi_gt_d6/lt_d6`, `pi_gt_314/315`; *extensible to arbitrary precision*: `Real.pi_gt_sqrtTwoAddSeries`, `pi_lt_sqrtTwoAddSeries` + the file's `pi_lower_bound` / `pi_upper_bound` tactics consuming rational witness lists |
| e | exists, 20 digits | `Real.exp_one_near_20 : |exp 1 - 363916618873/133877442384| ≤ 1/10^20`; `exp_one_near_10`, `exp_one_gt_d9`, `exp_one_lt_d9` (`Mathlib/Analysis/Complex/ExponentialBounds.lean`); machinery `Real.expNear`, `Real.exp_1_approx_succ_eq`, `Real.exp_approx_end/exp_approx_end'` (`Mathlib/Analysis/Complex/Exponential.lean`) for arbitrary depth |
| log 2 | exists, 10 digits | `Real.log_two_gt_d9 : 0.6931471803 < log 2`, `Real.log_two_lt_d9 : log 2 < 0.6931471808`, `Real.log_two_near_10 : |log 2 - 287209/414355| ≤ 1/10^10`; extension tool: `Real.abs_log_sub_add_sum_range_le` (Taylor tail bound, `Mathlib/Analysis/SpecialFunctions/Log/Deriv.lean`) |
| log 3, log π | absent as named bounds | same `abs_log_sub_add_sum_range_le` route (log π via π-enclosure + log-monotonicity) |
| γ (Euler–Mascheroni) | exists as a constant, **1-digit bounds only** | `Real.eulerMascheroniConstant` (`Mathlib/NumberTheory/Harmonic/EulerMascheroni.lean`); `Real.one_half_lt_eulerMascheroniConstant`, `Real.eulerMascheroniConstant_lt_two_thirds`; sandwich `eulerMascheroniSeq n < γ < eulerMascheroniSeq' n` (`eulerMascheroniSeq_lt_eulerMascheroniConstant`, `eulerMascheroniConstant_lt_eulerMascheroniSeq'`) — but the sandwich converges like `1/n`, so it cannot reach 10⁻²⁶; **no Euler–Maclaurin machinery exists in mathlib** (checked: only `AntitoneOn.integral_le_sum`-type comparisons in `Mathlib/Analysis/SumIntegralComparisons.lean` and the O(1)-precision `Mathlib/NumberTheory/Harmonic/Bounds.lean`) |
| √2, √3 etc. | trivial | `norm_num`-provable rational bracketing (squares of rationals) |
| modified spherical Bessel `i_k` (pole vectors) | absent | no Bessel functions in mathlib (only Bessel's inequality); the all-positive series of `certified_spectral.ik_iv` is elementary and self-contained to define and bound |

### (d) Interval arithmetic / verified numerics tactics — **absent from mathlib**

* Nothing interval-flavored ships with mathlib: `Mathlib/Tactic/NormNum/*`
  (exact rational arithmetic, primality, …), `Mathlib.Tactic.Bound`,
  `polyrith`, `nlinarith` — none do directed rounding or enclosures of
  transcendental functions.  `interval_cases` is about integer ranges, not
  interval arithmetic.
* What exists instead are *special-purpose verified-numerics patterns*, and
  they are exactly the right templates for the Bridge endgame:
  `pi_lower_bound`/`pi_upper_bound` (a tactic consuming a list of rational
  witnesses, `Mathlib/Analysis/Real/Pi/Bounds.lean`) and the
  `expNear`-chain lemmas behind `exp_one_near_20`.
* Outside mathlib (not vendored here, would enlarge the trust story beyond
  "mathlib + 3 axioms"): `girving/interval` (Lean 4 verified interval
  arithmetic).  Not used and not needed for the recommended route below.

**Recommended endgame architecture** (consequence of (c)+(d)): do *not*
build a general interval tactic.  The Bridge needs 144 (78 distinct)
*fixed* rational enclosures.  Mirror the repository's own discipline: have
`src/certified_spectral.py` (already interval-verified externally) emit,
per entry, an exact rational chain — partial sums of the explicitly bounded
series plus the proved geometric tails — and discharge each numeric leaf in
Lean by `norm_num` against the named constant enclosures of (c).  This is
the `exp_one_near_20` pattern at scale, and it keeps the axiom audit
unchanged.

---

## 4. Effort estimates for the remaining Bridge ingredients

Person-days for one person fluent in Lean/mathlib analysis, building on
this session's files; "±" is honest spread, not optimism.

| # | ingredient | estimate (pd) | notes |
|---|---|---|---|
| 1 | Overlap polynomials from `k+j ≤ 12` (done) to full basis (even `k+j ≤ 22`) + orthogonality corollaries (`F_kj(0)`) | 1–2 | generator done; cost is elaboration time of degree-≤23 `ring` identities (raise `maxHeartbeats` further, possibly split files; measured 53 s → 217 s from `≤ 8` to `≤ 12`); orthogonality is the `v = 0` specialization |
| 2 | `ψ(1/4) = −γ − π/2 − 3 log 2` inside mathlib's new digamma API | 2–4 | differentiate `Gamma_mul_Gamma_one_sub` and `Gamma_mul_Gamma_add_half` via `logDeriv` calculus; all inputs exist (`digamma_one_half`, `digamma_apply_add_one`) |
| 3 | Gauss's integral for `Re ψ` (Lemma A(i)) | 10–20 | the analytic crux; via Binet/Frullani or `∫₀^∞ (e^{−t} − e^{−zt})/(1−e^{−t}) dt` + `digamma_apply_add_one` uniqueness; upstream-recognized TODO — coordinate with mathlib to avoid duplication |
| 4 | x-space reduction of the archimedean form (§2.14: `A(φ) = ψ(1/4)‖φ‖² + 2∫₀^∞ [ψ_φ(0) − ψ_φ(u)] w(u) du` on the Legendre span) | 10–15 | Fubini/Plancherel over compactly supported L²; mathlib has `MeasureTheory.integral_integral_swap`, Fourier–Plancherel (`Real.fourierIntegral` API); the test functions here are polynomials on an interval, which softens everything |
| 5 | Analytic Bernoulli kernel: `w = 1/(2u) + g`, `g` analytic, coefficient bound `|g_r| ≤ 250/π^{r+1}`, series remainder on `[0, 2a]` | 8–15 | formal identity exists; needs `HasFPowerSeriesAt` identification + Cauchy estimate; then the moment algebra (`Mom_s`, `I₂`, `Hb`) is exact rational calculus over proved `F` data |
| 6 | Kernel tail `∫_{2a}^∞ e^{−u/2}/(1−e^{−2u}) du` with geometric bound | 1–2 | elementary comparison with `∫ e^{−u/2}` (`integral_exp_Ioi`-family exists) |
| 7 | Pole vectors: define `i_k`, prove the positive-series identity `2a·i_k(a/2)` = pole integral `∫ b_k e^{±x/2}`, geometric tail | 4–8 | self-contained series definition; the integral identity is FTC-with-`exp·polynomial` antiderivatives (same pattern as this session's, plus `exp`) |
| 8 | Prime terms: enclosures of `log 2, log 3, 2^{-1/2}, 3^{-1/2}` to 10⁻²⁶ and `a·F_kj(log n/a)` evaluation bounds | 2–4 | `abs_log_sub_add_sum_range_le` chains; `F` evaluation over proved data is `norm_num` |
| 9 | γ to ~10⁻²⁶ | 10–20 | the numeric bottleneck: formalize Euler–Maclaurin for `H_n − log n` with Bernoulli remainder (mathlib has neither E–M nor any fast-γ route; sandwich lemmas converge O(1/n)) — or upstream may land it first; everything else in (c) is extensible with existing machinery |
| 10 | Assembly: per-entry enclosure chains (Python-emitted, `norm_num`-discharged) for all 78 entries against `mRat` at `10^{−20}` | 8–15 | the `exp_one_near_20` pattern at scale; generator infrastructure of this session extends naturally |
| 11 | Definitional layer: `Q_L(φ)` for `φ` in the Legendre span, its matrix, and the final theorem `|Q_kj − mRat_kj| ≤ 10^{−20}` feeding `CertFramework.cert_window_positive` | 5–10 | mostly bookkeeping once 3–5 exist; ends at a fully formal Weil-positivity window for ζ |

**Total to a fully formal Bridge: ≈ 60–115 person-days**, with three
long-pole items (Gauss's integral, analytic Bernoulli bounds, γ-precision)
accounting for half of it, and with items 2, 6, 8 being genuinely short.
The three long poles are independent and parallelizable; items 3 and 9 are
natural mathlib upstream contributions (one is already an upstream TODO).

## Addendum: reproduction checklist

```
export PATH="$HOME/.elan/bin:$PATH"; export C_INCLUDE_PATH=/usr/include/x86_64-linux-gnu
cd lean && python3 gen_bridge_overlap.py 12          # regenerate BridgeOverlap.lean (deterministic)
cd weilcert && lake build BridgeLegendre BridgeOverlap CertFramework CertInstance
# axiom audit: a file of #print axioms lines over the 84 theorems of §1.5,
#   lake env lean <auditfile>   — expect every line to end
#   [propext, Classical.choice, Quot.sound]
```

Residual cosmetics (do not affect the build or the audit): 23 generated
lines exceed the 100-character style linter in the `k+j ≤ 12` file (long
monomials inside antiderivative coefficient groups) — warnings only.
