# T1′ (Hard Horizon Theorem) — Lean formalization, session 1

Agent report, 2026-07-26. Target: the §7 ladder of `results/experts/T1PRIME.md`
("Staircase Theorem 1 + Corollary 2" scope; Corollary 1 (ζ) out of scope, blocked
on RvM/S(T) as the paper says).

**Deliverable**: `lean/glide/Glide/HardHorizon.lean` (574 lines, namespace
`HardHorizon`), in the existing glide lake project. Build config change:
one appended line `import Glide.HardHorizon` in `lean/glide/Glide.lean`
(the lib-root of the existing `lean_lib Glide` target; `lakefile.toml`
untouched). Build: `lake --dir=lean/glide build` — **green**, zero errors;
only the pre-existing style-header linter warnings (same class as
`Glide/Basic.lean`).

Every declaration in the file is fully proved — **no `sorry` anywhere** —
and every theorem audits to exactly the three standard axioms.

## Ladder items completed (Lean name ↔ T1PRIME.md item)

| Lean theorem | Paper item | Status |
|---|---|---|
| `lemma0_D_at_eTstar` | Lemma 0 (D(eT*) = −7/8 exactly) | done |
| `lemma2_sum_log_eq_integral` | L2, eq. (L2.1) | done |
| `lemma2_integrableOn` | (companion, not in paper: L2 integrand is integrable — the hypothesis L4 needs) | done |
| `indicator_inv_integrable`, `sum_indicator_ae_eq` | (L2 infrastructure) | done |
| `lemma3_rvM_integral` | L3, eq. (L3.1) | done |
| `lemma4_rigidity_transfer` | L4, eq. (L4.1) | done |
| `integral_abs_sin_zero_pi` / `_pi_two_pi` / `_zero_two_pi` | (L6 infrastructure: ∫₀^{2π}\|sin\| = 4) | done |
| `lemma6_circle_bound` | L6, eq. (L6.1) first inequality (½ln 2a + (2/π)aρ) | done |
| `lemma6_circle_bound_tau` | L6, eq. (L6.1) second inequality (½ln 2a + 4ae^τ + (4+2/π)a) | done |
| `lemma7_pair_product` | L7, pair-product arithmetic core | done |
| `lemma7_other_mass_nonneg` | L7, last clause (foreign zeros ≥ 0) | done |
| `lemma8_strictMonoOn` | L8, strict monotonicity on [2a+2, ∞) | done |
| `lemma8_crossing` | L8, eq. (L8.1) | done |
| `lemma8_tau_bound` | §3 endgame: h(τ) ≤ B ∧ τ ≥ 2a+2 ⟹ τ ≤ 2a+2+max(0,ε*) | done |
| `lemma1_sinh_le` | L1 scalar core: sinh y ≤ y·e^y (all real y) | done |

Definitions: `Nhat`, `BConst` (= B), `epsStar` (raw quotient; the `max 0 ·`
of the theorem statement is applied in `lemma8_tau_bound`), `hFn` (= h(τ)).

**Not yet done** (ladder remainder, in recommended order): L1 full
(entirety + growth of F = φ̂), L5 (radius selection + Jensen instantiation),
L7 divisor bookkeeping, Theorem 1 assembly, Corollary 2. See handoff below.

## Axiom audits (verbatim, `lake env lean` on an `#print axioms` file)

```
'HardHorizon.lemma0_D_at_eTstar' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.indicator_inv_integrable' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.sum_indicator_ae_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma2_sum_log_eq_integral' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma2_integrableOn' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma3_rvM_integral' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma4_rigidity_transfer' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.integral_abs_sin_zero_pi' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.integral_abs_sin_pi_two_pi' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.integral_abs_sin_zero_two_pi' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma6_circle_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma6_circle_bound_tau' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma7_pair_product' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma7_other_mass_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma8_strictMonoOn' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma8_crossing' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma1_sinh_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma8_tau_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
```

No `sorryAx`, no `Lean.ofReduceBool`/`Lean.trustCompiler` (no `native_decide`).

## Numerical sanity checks (paper Appendix V cross-checks, mpmath dps 30)

- `epsStar` reproduces V5's table exactly: 0.124 / 0.117 / 0.106 / 0.083 /
  0.044 / 0.0142 at a = 0.4375 … 2.25 with (R,κ) = (½,1).
- `hFn a R (2a+2) = −2R(2a+1)` to 0 (the ε*=0 branch identity of §3).
- L6's average identity ((1/2π)∫(½ln2a + aρ|sinθ|) = ½ln2a + (2/π)aρ) to 0;
  ∫₀^{2π}|sin| = 4.
- L3 closed form and L8.1 crossing checked at off-table points
  (τ = 1.7, 3; a = 0.75): diffs ≤ 4e−31, crossing slack +0.789 ≥ 0.

## Deviations from the paper statements (all formalization-shape, no mathematics changed)

1. **L2** — the finite multiset `{tₖ}` is a Finset index `ι : Finset α` with
   ordinate map `t : α → ℝ`; multiplicity is index multiplicity, and the
   counting function is `(ι.filter (t · ≤ s)).card`. The integral is the
   Bochner set-integral over `Set.Ioc 0 T` (identical content; the interval
   form is recovered with `intervalIntegral.integral_of_le`). Hypotheses:
   `0 < t k` and `t k ≤ T` for all k ∈ ι — i.e. the lemma is stated for the
   head `tₖ ≤ T`, which is all (L2.1) ever sums; for the application, filter
   the ordinate Finset to the head first (N(s) for s ≤ T only sees that head,
   so nothing is lost).
2. **L4** — `N` is an abstract `ℝ → ℝ` with three hypotheses: integrability
   of `N s / s` on `Ioc 0 T̃` (discharged for the L2 counting function by
   `lemma2_integrableOn`), nonnegativity on `Ioc 0 T̃`, and rigidity
   `Nhat s − R ≤ N s` on `Icc (2πe) T̃` (paper's (S2) interval, verbatim).
3. **L6** — stated for the recentered function with **center 0** (the paper's
   `G` is already recentered) and mathlib's `Real.circleAverage`. Three
   hypotheses: `CircleIntegrable (log ‖G ·‖) 0 ρ` (in the assembly this comes
   free from `MeromorphicOn.circleIntegrable_log_norm`), **no zeros of `G`
   on the circle** `|z| = ρ`, and the L1 growth bound
   `‖G z‖ ≤ √(2a)·e^{a|Im z|}` for all z (the exact conclusion shape L1 must
   deliver). **Important discovery**: the paper's §7 note "radius selection
   is OPTIONAL in the formal version" is true for **L5** (mathlib's Jensen
   handles boundary zeros) but **false for L6**: mathlib's `Real.log 0 = 0`
   junk value breaks the pointwise bound `log‖G z‖ ≤ ½ln(2a) + a|Im z|` at a
   circle zero whenever `½ln(2a) + a|Im z| < 0` (possible for a < ½ near
   θ = 0). So the L5 radius selection must also guarantee no zeros on the
   chosen circle — which it does by construction, at zero extra cost. (An
   alternative next session: an a.e. version of L6 using countability of the
   zero set on the circle; not needed if selection is kept.)
4. **L7** — this session formalized the arithmetic core: the pair bound is
   stated as `2·ln(T/t) ≤ ln(ρ/|t−x₀|) + ln(ρ/|t+x₀|)` (the sum of the two
   single-zero Jensen masses), equivalent to the paper's `ln(ρ²/(t²−x₀²))`
   form by log algebra, and it is the shape the divisor finsum needs.
   Hypothesis set: `|x₀| ≤ 2π < t ≤ T ≤ ρ − 2π` (paper: `ρ ≥ T̃ + 2π`).
   The divisor-side bookkeeping (prescribed zeros interior, divisor
   multiplicity ≥ mₖ, finsum split) is the L5/L7 rung left for next session.
5. **L8** — `epsStar` is the raw quotient; `lemma8_crossing` needs `ε* > 0`
   (the paper's case split) and — a small strengthening found in
   formalization — does **not** need `R ≥ 0` (the R-terms cancel exactly);
   the hypothesis is kept as `_hR0` for paper fidelity. `lemma8_tau_bound`
   packages §3's endgame: from `2a+2 ≤ τ` and `h(τ) ≤ B` conclude
   `τ ≤ 2a+2 + max 0 ε*`, handling both the ε* ≤ 0 and ε* > 0 branches.
6. **L1 scalar core** — `sinh y ≤ y·e^y` holds for **all** real y (paper
   needs y > 0); proved unconditionally, no hypothesis.

## Mathlib gap-map corrections for T1PRIME.md §7 (local snapshot `520045ab14` / v4.32.1 toolchain)

- `MeasureTheory.integral_finset_sum` (named in the §7 table) is **deprecated
  since 2026-04-08**; the current name is `integral_finsetSum`. Same for
  `integrable_finsetSum`.
- `le_or_lt` no longer exists at root; use `le_or_gt`.
- `measure_eq_zero_iff_ae_notMem` is the clean route from "finite set has
  measure zero" to the a.e. statement (avoid `ae_iff` + `simpa`, which
  normalizes the Finset coercion differently on the two sides and fails).
- Under `open Set`, `indicator_of_mem`/`indicator_of_notMem` must be written
  `Set.indicator_of_mem`/`Set.indicator_of_notMem` inside `rw` (the bare
  name resolves to a different pattern and the rewrite fails).
- Confirmed present and usable (for the next rungs): `Real.circleAverage`
  API (`circleAverage_def`, `circleAverage_mono`,
  `circleAverage_mono_on_of_le_circle`, `circleIntegrable_def`,
  `circleIntegrable_const`), `circleMap_zero_im` ((circleMap 0 r θ).im =
  r sin θ), `AnalyticOnNhd.circleAverage_log_norm` (Jensen; divisor over
  `closedBall c |R|`, finsum over ℂ), `AnalyticOnNhd.divisor_apply`,
  `(divisor f _).finiteSupport (isCompact_closedBall ..)`,
  `MeromorphicOn.circleIntegrable_log_norm`,
  `intervalIntegral.integral_eq_sub_of_hasDerivAt`, `integral_inv`
  (root-level, in `Analysis/SpecialFunctions/Integrals/Basic.lean`),
  `intervalIntegral.integral_comp_add_right`, `Real.sin_add_pi`,
  `strictMonoOn_of_hasDerivWithinAt_pos`, `Real.log_sqrt`,
  `measure_eq_zero_iff_ae_notMem`, `Set.Finite.measure_zero`.

## Handoff: next session's work, in order

1. **L1 full** (the 2–4 day rung). Define
   `F z := ∫ x in (-a)..a, φ x * Complex.exp (-(Complex.I * z * x))` for
   `φ : ℝ → ℂ`. Prove:
   - `lemma1_entire : Differentiable ℂ F` — differentiation under the
     integral (`intervalIntegral.hasDerivAt_integral_of_dominated_loc_of_lip`
     with dominating function `|φ x|·(local const)`; Cauchy–Schwarz gives
     φ ∈ L¹[−a,a] from the L² hypothesis).
   - `lemma1_growth : ∀ z, ‖F z‖ ≤ Real.sqrt (2*a) * Real.exp (a * |z.im|)`
     — **this exact shape is the `hgrowth` input of `lemma6_circle_bound`**.
     Route: `norm_integral_le_integral_norm`, then Cauchy–Schwarz
     (`MeasureTheory.integral_mul_le_Lp_mul_Lq` with p = q = 2, or
     `inner_mul_le_norm_mul_norm` in `L2`), then
     `∫_{−a}^{a} e^{2ηx} dx = sinh(2aη)/η` (FTC, house pattern) and
     `lemma1_sinh_le` (already proved), plus the η = 0 case (`‖φ‖₁ ≤ √(2a)`).
2. **L5** (radius selection + Jensen). (a) Selection: the zeros of G in
   `closedBall 0 (T̃+2π+1)` are finite (`(divisor …).finiteSupport`, or
   isolated-zeros of the analytic G ≠ 0), so their moduli avoid some
   ρ ∈ [T̃+2π, T̃+2π+1]; select ρ with **no zeros on the sphere** (needed by
   L6, see deviation 3). (b) Jensen: instantiate
   `AnalyticOnNhd.circleAverage_log_norm` at c = 0, radius ρ; note the
   divisor sum there is `∑ᶠ u, divisor … u * log (ρ * ‖-u‖⁻¹)` — the L7
   masses in `lemma7_pair_product` are already in `log (ρ/d)` shape
   (`log (ρ * d⁻¹) = log (ρ/d)` by `div_eq_mul_inv`).
3. **L7 divisor side**: from (S3) (`analyticOrderAt F (±tₖ) ≥ mₖ` with
   `mₖ` = index multiplicity in ι), get
   `divisor G (closedBall 0 |ρ|) (±tₖ − x₀) ≥ mₖ`
   (`AnalyticOnNhd.divisor_apply`), then lower-bound the Jensen finsum by
   the prescribed pair masses (`finsum` split over the finite support; the
   non-prescribed terms are ≥ 0 by `lemma7_other_mass_nonneg`).
4. **Theorem 1 assembly**: chain
   `lemma4_rigidity_transfer` (N := L2 counting function, integrability by
   `lemma2_integrableOn`, rigidity from (S2)) → `lemma2_sum_log_eq_integral`
   → L7 divisor bound → L5 Jensen → `lemma6_circle_bound_tau` + anchor
   (−log‖G 0‖ ≤ κa) → `hFn a R τ ≤ BConst a κ` → `lemma8_tau_bound`.
   Suggested statement: hypotheses (S1) as `MemLp φ 2` + `support φ ⊆ Icc (−a) a`
   + `eLpNorm φ 2 = 1`, (S2)/(S3) via the ordinate Finset; conclusion
   `Real.log (T̃/(2π)) ≤ 2*a + 2 + max 0 (epsStar a R κ)`.
5. **Corollary 2** (desert): re-run the chain at radius parameter ρ′ keeping
   the remainder term; needs the strengthened L7 with the `2(ρ′−τ)` surplus
   (eq. 4.2.2) — straightforward variant of `lemma7_pair_product`.

Corollary 1 stays blocked (formalized RvM with explicit constants; months,
external), exactly as the paper's §7 table says.

## Build/verify commands

```
export PATH="$HOME/.elan/bin:$PATH" C_INCLUDE_PATH=/usr/include/x86_64-linux-gnu
lake --dir=lean/glide build          # green, ~20 s cached
# audit: put the #print axioms lines (list above) in a file and run
lake --dir=lean/glide env lean <audit file>
```

---

# Session 2 (same day): L1 full, L5, L7 divisor side, Theorem 1, Corollary 2

**The Hard Horizon Theorem (Theorem 1, staircase form) and Corollary 2 (zero
desert) are now kernel-checked**, in the same file
`lean/glide/Glide/HardHorizon.lean` (now 1461 lines, 36 declarations, zero
`sorry`, build green). This completes the entire unblocked scope of the
T1PRIME.md §7 ladder: everything except Corollary 1 (ζ), which stays blocked
on formalized RvM/S(T) exactly as the paper says.

## Items completed this session (Lean name ↔ paper item)

| Lean theorem | Paper item |
|---|---|
| `FL` | the (S1) transform `F(z) = ∫_{−a}^{a} φ(x)e^{−izx}dx` (over `Icc (−a) a`) |
| `FL_exponent_re`, `FL_integrand_norm`, `FL_integrand_integrableOn` | L1 infrastructure |
| `lemma1_entire` | **L1**, entirety half (differentiation under the integral) |
| `lemma1_growth`, `lemma1_growth_recentered` | **L1**, growth half (L1.1): `‖F(z)‖ ≤ √(2a)e^{a·\|Im z\|}`, also in the recentered `hgrowth` shape lemma6 consumes |
| `analyticOrderAt_ne_top_of_ne` | L5 infrastructure (identity theorem: entire + somewhere-nonzero ⟹ all orders finite) |
| `le_divisor_of_le_analyticOrderAt` | L5/L7 bridge: order ≥ m ⟹ divisor ≥ m |
| `lemma5_radius_selection` | **L5**, selection half (WITH no-zeros-on-circle — required by L6, session-1 finding) |
| `lemma5_jensen` | **L5** (L5.1): selection in `[T+2π, T+2π+1]` + mathlib Jensen at the selected radius, center 0, divisor sum in `log(ρ·‖u‖⁻¹)` form |
| `lemma7_divisor_lower` | **L7**, divisor side: `Σ_{u∈P} m(u)·log(ρ‖u‖⁻¹) ≤ Σᶠ_u div(u)·log(ρ‖u‖⁻¹)` for any prescribed finite `P` in the closed disk with `analyticOrderAt ≥ m` |
| `hard_horizon` | **Theorem 1** (§1.2, staircase form): `τ ≤ 2a + 2 + max 0 ε*` |
| `zero_desert` | **Corollary 2** (§1.3/§4.2): `Other(ρ′) ≤ Φ(ρ′) = 4a·e^{ρ′} − 2e^τ[(τ−2)+(ρ′−τ)(τ−1)] + 2R(ρ′−1) + B′` |

## Axiom audits (verbatim)

```
'HardHorizon.FL' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma1_entire' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma1_growth' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma1_growth_recentered' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.analyticOrderAt_ne_top_of_ne' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.le_divisor_of_le_analyticOrderAt' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma5_radius_selection' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma5_jensen' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.lemma7_divisor_lower' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.hard_horizon' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.zero_desert' depends on axioms: [propext, Classical.choice, Quot.sound]
```

No `sorryAx`, no `Lean.ofReduceBool`/`Lean.trustCompiler` anywhere in the file.

## The theorem statements, in words

`hard_horizon`: for `φ` with (S1)-data (`IntegrableOn φ (Icc (−a) a)`,
`‖φ‖²` integrable with `∫‖φ‖² ≤ 1`), an ordinate head `ι, t` with
`2π < tₖ ≤ 2πe^τ` (multiplicity = index multiplicity), one-sided rigidity
`N̂(s) − R ≤ #{k : tₖ ≤ s}` on `[2πe, 2πe^τ]` with `0 ≤ R < e^{2a+2}`,
recentered vanishing orders `analyticOrderAt (z ↦ F(x₀+z)) (±tₖ − x₀) ≥`
(fiber multiplicity of `tₖ`), and the anchor `|x₀| ≤ 2π`,
`e^{−κa} ≤ ‖F(x₀)‖`: **`τ ≤ 2a + 2 + max 0 (epsStar a R κ)`**.

`zero_desert`: same hypotheses minus the R-bounds (not needed — no L8 step),
plus `1 ≤ τ ≤ ρ′`: there exists `ρ ∈ [2πe^{ρ′}+2π, 2πe^{ρ′}+2π+1]` with no
zeros of `G = F(x₀+·)` on `|z| = ρ`, and the divisor finsum minus the
prescribed pair masses is `≤ Φ(ρ′)` exactly as printed in §1.3.

## Deviations from the paper (session 2; all shape, no mathematics changed)

7. **(S1) packaging** — `φ : ℝ → ℂ` with `IntegrableOn φ (Icc (−a) a)`,
   `IntegrableOn (‖φ‖²)`, and `∫‖φ‖² ≤ 1` (≤ instead of = 1: the bound only
   improves; support condition is absorbed by integrating over `[−a,a]`).
   `FL` is the Bochner integral over `Icc (−a) a` of `φ x · exp(−(i·z·x))`.
8. **(S3) recentered** — vanishing orders are stated for
   `fun z => FL φ a (x₀ + z)` at `±tₖ − x₀` (`analyticOrderAt … ≥` the
   `t`-fiber cardinality `#{j ∈ ι : tⱼ = tₖ}`). Mathematically identical to
   "F vanishes at ±tₖ to order ≥ mult(tₖ)"; stating it on the recentered
   function avoids a translation-invariance lemma for `analyticOrderAt`
   that mathlib does not appear to have (worth contributing upstream).
9. **Multiplicity is fully general** — repeated indices in `ι` are handled
   end-to-end (fiber bookkeeping via `Finset.sum_comp`); no simple-zeros
   assumption anywhere.
10. **`zero_desert`'s `Other`** — defined as (divisor finsum) − (prescribed
    pair-mass sum), which *upper-bounds* the paper's `Other` (it also counts
    excess multiplicity at prescribed points), so the `≤ Φ(ρ′)` conclusion
    is the stronger form. The counting version (`#zeros ≤ Φ(ρ′+ln2)/ln2`) is
    a downstream arithmetic corollary, not formalized (next session, cheap).
11. **`hard_horizon` conclusion parametrization** — the horizon enters as
    `T̃ = 2πe^τ` with conclusion `τ ≤ …` (paper: `ln(T̃/2π) ≤ …`; identical
    content, avoids a log-inversion step in every hypothesis).
12. **`zero_desert` needs neither `0 ≤ R` nor `R < e^{2a+2}`** — the L8 step
    is absent and all R-terms pass through linearly. Strictly stronger than
    the paper's statement.

## Additional mathlib gap-map notes (session 2)

- `hasDerivAt_integral_of_dominated_loc_of_deriv_le`
  (Mathlib/Analysis/Calculus/ParametricIntegral.lean) is the right L1 tool
  (𝕜 = ℂ works); the `-loc_of_lip` variant named in §7 is also present but
  the `deriv_le` form saves the Lipschitz packaging.
- Cauchy–Schwarz for the growth bound: `integral_mul_le_Lp_mul_Lq_of_nonneg`
  with `Real.HolderConjugate.two_two` + `memLp_two_iff_integrable_sq`
  (+ `Real.rpow_two`, `Real.sqrt_eq_rpow` to translate rpow forms). No sinh
  needed: the pointwise bound `e^{2ηx} ≤ e^{2a|η|}` on `[−a,a]` gives the
  same constant `√(2a)e^{a|η|}` — `lemma1_sinh_le` is retained but unused.
- **Namespace trap**: `AnalyticOnNhd.divisor_apply` / `.divisor_nonneg` live
  inside `namespace MeromorphicOn` (full names
  `MeromorphicOn.AnalyticOnNhd.divisor_*`); dot notation only resolves with
  `open MeromorphicOn`. The entire-function iff is
  `Complex.analyticOnNhd_univ_iff_differentiable` (namespaced).
- Divisor value bridge: `AnalyticOnNhd.divisor_apply` gives
  `((analyticOrderAt f z).map ↑).untop₀`; convert order bounds via
  `WithTop.recTopCoe` case split + `ENat.map_coe` + `WithTop.untop₀_coe`
  (avoid `WithTop.ne_top_iff_exists`, whose coe direction fights `Nat.cast`
  norm_cast normalization).
- `CircleIntegrable (log ‖G ·‖) 0 ρ` comes free from
  `MeromorphicOn.circleIntegrable_log_norm` on the sphere.
- Zero-finiteness: divisor `finiteSupport` (compact) + identity theorem
  (`AnalyticOnNhd.eqOn_zero_of_preconnected_of_eventuallyEq_zero`,
  `analyticOrderAt_eq_top`); radius choice via `Set.Icc_infinite` +
  `Set.Infinite.exists_notMem_finite`.
- Fiber bookkeeping: `Finset.sum_comp` (give the function argument
  explicitly — HO unification fails with `_`), `Finset.sum_subset`,
  `Finset.filter_congr`, `Finset.filter_true_of_mem`. DecidableEq ℂ is a
  global (noncomputable, classical) instance, so no `classical` tactic is
  needed — important, because a local `Classical.propDecidable` would make
  the proof's `Finset.filter` terms differ from the hypothesis binders'.

## Remaining work (next sessions)

1. **Corollary 2 counting version**: `#{non-prescribed zeros within 2πe^{ρ′}} ≤
   Φ(ρ′+ln2)/ln2` — arithmetic on top of `zero_desert` (each such zero
   contributes ≥ ln2 at parameter ρ′+ln2; divisor-side counting lemma).
2. **Convenience wrappers**: an `(S1)`-from-`MemLp` constructor
   (`MemLp φ 2 → eLpNorm φ 2 = 1 → hsq/hφ2`), and an un-recentered (S3)
   variant once an `analyticOrderAt` translation lemma exists (contribute
   `analyticOrderAt_comp_add_const` to mathlib).
3. **Corollary 1 (ζ)**: still blocked on RvM with explicit constants
   (months, external) — unchanged.
4. Optional hygiene: mathlib-style file header to silence the style linter
   (same warnings as `Glide/Basic.lean`).

Numerical cross-checks this session: Φ(ρ′)|_{ρ′=τ} reproduces the paper's
special value `2e^τ(1−s) + 2R(τ−1) + B′` to 3e−30; `N̂(2πe^τ) =
e^τ(τ−1) + 7/8` to 0; ε* table re-verified (session 1).

---

# Session 3 (same day): `anchor_collapse` (QC-2, C-9 spec)

Assignment: results/ias/SEAT-quasicrystal.md, Round-2 C-9 adjudication —
the annihilating-pair strengthening of Theorem 1.  **Both spec'd theorems
are kernel-checked**: `HardHorizon.anchor_collapse` and
`HardHorizon.anchor_collapse_of_deep`, in
`lean/glide/Glide/HardHorizon.lean` (now 1588 lines, zero `sorry`, build
green).  The spec's mathematics checked out completely — no errors found.

## Implementation choice (recorded)

Appended to `HardHorizon.lean` (not a separate file), because the honest
implementation is a **refactor, not a copy**: the C-9 proof plan ("reuse
verbatim lines 946–1157") would have duplicated ~200 lines.  Instead the
shared Jensen chain was extracted as a new theorem:

* `log_anchor_bound` — the §3 chain stopped one step before L8:
  under (S1) + head + (S2)-rigidity + (S3) + `|x₀| ≤ 2π` + `F(x₀) ≠ 0` +
  `1 ≤ τ` (note: neither `0 ≤ R` nor `R < e^{2a+2}` nor `2a+2 ≤ τ` is
  needed): `hFn a R τ ≤ BConst a 0 − Real.log ‖F(x₀)‖`.

`hard_horizon` was then **reproved from `log_anchor_bound`** (statement
byte-identical to Session 2; proof now 15 lines: anchor ⟹ nonvanishing +
`−log‖F(x₀)‖ ≤ κa`, then `lemma8_tau_bound`), and the new theorems are
corollaries.  Net cost of the whole session: +127 lines.

## What was proved (Lean name ↔ C-9 spec item)

| Lean theorem | Spec item |
|---|---|
| `log_anchor_bound` | (new; the shared core the spec's step 2 describes) |
| `anchor_collapse` | QC-2 declaration, exactly as spec'd: `‖F(x₀)‖ ≤ exp(BConst a 0 − hFn a R τ)` under the Theorem-1 hypotheses minus the anchor, for every `\|x₀\| ≤ 2π`, `τ ≥ 2a+2` |
| `hFn_lower_at` | spec step 3's `hFn_lower_at` (~15 lines as estimated): `2δe^{2a+2} − 2R(2a+1+δ) ≤ hFn a R (2a+2+δ)` for `δ ≥ 0` |
| `anchor_collapse_of_deep` | deep form, exactly as spec'd: bound `exp(B₀ + 2R(2a+1+δ) − 2δe^{2a+2})` at `τ ≥ 2a+2+δ` |

The proof followed the spec's plan precisely: `by_cases` on `F(x₀) = 0`
(zero case `Real.exp_pos`-trivial — this is how Hypothesis A dies), chain
reuse, `Real.log_le_iff_le_exp` rearrangement; deep form via
`lemma8_strictMonoOn` + the exposed crossing evaluation.  No new mathlib
surface, as predicted.

## Axiom audits (verbatim; includes re-audit of the two refactored theorems)

```
'HardHorizon.log_anchor_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.hard_horizon' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.zero_desert' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.anchor_collapse' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.hFn_lower_at' depends on axioms: [propext, Classical.choice, Quot.sound]
'HardHorizon.anchor_collapse_of_deep' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The session-1 and session-2 audit files were re-run against the refactored
environment: every declaration in the file remains exactly 3-axiom clean
(zero non-conforming lines).

## Deviations from the C-9 spec (all recorded, none mathematical)

13. **Binder names `_hR0`/`_hRe` in `anchor_collapse`** — the spec carries
    `hR0 : 0 ≤ R` and `hRe : R < e^{2a+2}` from Theorem 1, but the
    rearranged chain never invokes L8, so neither is used (underscored to
    keep the (S2)-faithful signature without linter noise).  In
    `_of_deep`, `hRe` IS used (monotonicity); `_hR0` remains unused.
    Consequence: `anchor_collapse` is strictly stronger than spec'd — it
    holds for any real `R`.
14. **`hτ : 2a+2 ≤ τ` is stronger than needed** — the underlying
    `log_anchor_bound` needs only `1 ≤ τ`; the spec's statement was kept
    verbatim (the sub-horizon regime just makes `exp(B₀ − h(τ))` huge).
15. **Coercion spelling** — the spec's `(t k : ℂ) - x₀` is written
    `(t k : ℂ) - (x₀ : ℂ)` to match the file's existing (S3) binders
    (identical elaborated term).
16. **Sharper deep constant available free** — at `τ₀ = 2a+2+δ` the
    crossing evaluation is EXACT with `e^{2a+2+δ}` (the spec's docstring
    mentions this; its formal statement uses the weaker `e^{2a+2}`, which
    is what was implemented).  If a consumer wants
    `−2δe^{2a+2+δ}`, it is a two-line variant of `hFn_lower_at`.

## Numerical sanity (pre-implementation, mpmath dps 30)

- `hFn(2a+2+δ) − (2δe^{2a+2} − 2R(2a+1+δ))` ≥ 0 at (a,R,δ) =
  (0.75, 0.5, 0.3), (0.4375, 3.6, 1.0), (1.5, 0.5, 0.01): margins
  +6.95, +60.9, +0.0298 ✓.
- Exact-form identity `hFn(2a+2+δ) = 2δe^{2a+2+δ} − 2R(2a+1+δ)` to 1e−29 ✓.
- `2e²δ·e^{2a} = 2δe^{2a+2}` exactly (the coordinator's "de-anchoring cost"
  phrase) ✓.
- Sample collapse scale: a = 0.75, R = ½, τ = 2a+2+0.5:
  `exp(B₀ − h(τ)) ≈ 1.5e−21` — the super-exponential anchor death.

## Handoff

- The two cheap Session-2 leftovers remain queued (not natural fall-outs of
  this session): Cor-2 counting version (needs a per-zero ≥ ln 2 counting
  lemma on top of `zero_desert`), MemLp/eLpNorm (S1) wrappers (ENNReal
  unpacking, ~half a day).
- Downstream consumers can now cite: `log_anchor_bound` (the reusable
  chain), `anchor_collapse` (C-2 clause (3) price list; Gap 1 quantitative
  target), `anchor_collapse_of_deep` (PT-4's second RCA₀-grade artifact).
- The C-9 size estimate (200–280 lines) was beaten by the refactor
  (+127 net); axioms unchanged as predicted.
