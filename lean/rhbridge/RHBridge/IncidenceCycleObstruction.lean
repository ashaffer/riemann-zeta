/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.DualFrameCollarCompletion

/-!
# Obstructions for incidence-kernel cycle constructions

Commuting translation plaquettes are genuine divergence-free cycles, but that
also makes them invisible to every vertex gradient, including collar states.
Only boundary-relative cycles can contribute to a dual-frame completion.

The second part records the exact scalar form of the amplified collar-capacity
threshold.  The amplification by the inverse old Weil excess cannot be
dropped.  An explicit rational model then shows that a strictly positive full
block need not be certified after the return-cycle capacity is omitted.
-/

namespace RHP2Bridge.IncidenceCycleObstruction

open scoped RealInnerProductSpace

/-- The two-edge plaquette formed from commuting divergence maps is closed. -/
theorem commuting_plaquette_closed
    {H : Type*} [AddCommGroup H] [Module ℝ H]
    (S T : H →ₗ[ℝ] H) (hcomm : S.comp T = T.comp S) (z : H) :
    S (T z) + T (-S z) = 0 := by
  rw [map_neg]
  have hz := LinearMap.congr_fun hcomm z
  simp only [LinearMap.comp_apply] at hz
  rw [hz]
  simp

/-- A globally divergence-free edge cycle pairs to zero with every gradient.
It therefore cannot acquire a collar response merely by changing the vertex
decomposition into old and new states. -/
theorem globallyClosedCycle_invisible
    {H E : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (B : H →ₗ[ℝ] E) (div : E →ₗ[ℝ] H)
    (hadjoint : ∀ x q, inner ℝ (B x) q = inner ℝ x (div q))
    {q : E} (hclosed : div q = 0) (x : H) :
    inner ℝ (B x) q = 0 := by
  rw [hadjoint, hclosed, inner_zero_right]

/-- Exact amplified threshold for a scalar old/collar block in cycle normal
form.  Here `S` is the old incidence energy, `D` the new scalar degree, `l`
the parallel leakage, and `G` the selected cycle response capacity. -/
theorem block_nonnegative_of_amplified_capacity
    {S D l G : ℝ} (hSD : D < S)
    (hcapacity : D * (1 + S * l ^ 2 / (S - D)) ≤ G) :
    ∀ x y : ℝ,
      0 ≤ (S - D) * x ^ 2 + 2 * S * l * x * y +
        (S * l ^ 2 + G - D) * y ^ 2 := by
  intro x y
  have hden : S - D ≠ 0 := ne_of_gt (sub_pos.mpr hSD)
  have hresidual : 0 ≤ G - D - D * S * l ^ 2 / (S - D) := by
    calc
      0 ≤ G - D * (1 + S * l ^ 2 / (S - D)) :=
        sub_nonneg.mpr hcapacity
      _ = G - D - D * S * l ^ 2 / (S - D) := by ring
  have hid :
      (S - D) * x ^ 2 + 2 * S * l * x * y +
          (S * l ^ 2 + G - D) * y ^ 2 =
        (S - D) * (x + S * l / (S - D) * y) ^ 2 +
          (G - D - D * S * l ^ 2 / (S - D)) * y ^ 2 := by
    field_simp
    ring
  rw [hid]
  exact add_nonneg
    (mul_nonneg (sub_nonneg.mpr hSD.le) (sq_nonneg _))
    (mul_nonneg hresidual (sq_nonneg _))

/-- Conversely, positivity of the complete scalar block forces the amplified
capacity threshold.  Thus the inverse-old-gap term is not an artifact of the
dual-frame proof. -/
theorem amplified_capacity_of_block_nonnegative
    {S D l G : ℝ} (hSD : D < S)
    (hblock : ∀ x y : ℝ,
      0 ≤ (S - D) * x ^ 2 + 2 * S * l * x * y +
        (S * l ^ 2 + G - D) * y ^ 2) :
    D * (1 + S * l ^ 2 / (S - D)) ≤ G := by
  have hden : S - D ≠ 0 := ne_of_gt (sub_pos.mpr hSD)
  have h := hblock (-S * l / (S - D)) 1
  have hid :
      (S - D) * (-S * l / (S - D)) ^ 2 +
          2 * S * l * (-S * l / (S - D)) * 1 +
          (S * l ^ 2 + G - D) * 1 ^ 2 =
        G - D - D * S * l ^ 2 / (S - D) := by
    field_simp
    ring
  rw [hid] at h
  calc
    D * (1 + S * l ^ 2 / (S - D)) =
        D + D * S * l ^ 2 / (S - D) := by ring
    _ ≤ G := by linarith

/-- The amplified threshold is therefore equivalent to nonnegativity of the
two-by-two block (under the natural nonnegative-degree assumption). -/
theorem amplified_capacity_iff_block_nonnegative
    {S D l G : ℝ} (hSD : D < S) :
    D * (1 + S * l ^ 2 / (S - D)) ≤ G ↔
      ∀ x y : ℝ,
        0 ≤ (S - D) * x ^ 2 + 2 * S * l * x * y +
          (S * l ^ 2 + G - D) * y ^ 2 := by
  constructor
  · exact block_nonnegative_of_amplified_capacity hSD
  · exact amplified_capacity_of_block_nonnegative hSD

/-- In a scalar consecutive-event block, the full incidence-capacity surplus
is exactly the Schur complement of the enlarged Weil block.  Here `S` is the
old incidence energy, `d` the old degree, `c` the event increment, `X` the
new old--collar incidence cross term, and `K` the collar incidence energy.

This identity is the algebraic reason that a lower bound on the Hodge loss is
strictly stronger than ordinary new-window positivity: positivity controls
the right side only by zero. -/
theorem scalar_full_surplus_eq_weil_schur
    {S d c X K : ℝ} (hT : S + c ≠ 0) (hA : S - d ≠ 0) :
    (K - X ^ 2 / (S + c)) -
        (d + c) *
          (1 + (X / (S + c)) ^ 2 * (S + c) / (S - d)) =
      K - (d + c) - X ^ 2 / (S - d) := by
  field_simp
  ring

/-- A scalar negative mode is repaired by a positive sector when the diagonal
return reserve dominates the Schur leakage `c² / gamma`.  This is the
one-negative-sector form of the noncircular Feshbach comparison used in the
incidence-cycle completion. -/
theorem one_negative_sector_nonnegative_of_repair
    {gamma mu c r : ℝ} (hgamma : 0 < gamma)
    (hrepair : c ^ 2 / gamma ≤ r - mu) :
    ∀ x y : ℝ,
      0 ≤ -mu * x ^ 2 + 2 * c * x * y + gamma * y ^ 2 + r * x ^ 2 := by
  intro x y
  have hgamma_ne : gamma ≠ 0 := ne_of_gt hgamma
  have hreserve : 0 ≤ r - mu - c ^ 2 / gamma :=
    sub_nonneg.mpr hrepair
  have hid :
      -mu * x ^ 2 + 2 * c * x * y + gamma * y ^ 2 + r * x ^ 2 =
        gamma * (y + c / gamma * x) ^ 2 +
          (r - mu - c ^ 2 / gamma) * x ^ 2 := by
    field_simp
    ring
  rw [hid]
  exact add_nonneg
    (mul_nonneg hgamma.le (sq_nonneg _))
    (mul_nonneg hreserve (sq_nonneg _))

/-- Exact scalar expansion of the tilted graph capacity.  The final summand
is the reserve beyond the simple weighted return capacity. -/
theorem scalar_tilted_capacity_expansion
    {F R t : ℝ} (hden : 0 < F + t ^ 2 * R) :
    (F + t * R) ^ 2 / (F + t ^ 2 * R) =
      F + (2 * t - t ^ 2) * R +
        t ^ 2 * (1 - t) ^ 2 * R ^ 2 / (F + t ^ 2 * R) := by
  have hden_ne : F + t ^ 2 * R ≠ 0 := ne_of_gt hden
  field_simp
  ring

/-- On the natural nonnegative range `0 ≤ t ≤ 1`, the tilted graph
capacity dominates the inverse-free weighted capacity
`F + (2t - t²)R`. -/
theorem scalar_tilted_capacity_lower_bound
    {F R t : ℝ} (hF : 0 ≤ F) (hR : 0 ≤ R)
    (ht0 : 0 ≤ t) (ht1 : t ≤ 1) (hden : 0 < F + t ^ 2 * R) :
    F + (2 * t - t ^ 2) * R ≤
      (F + t * R) ^ 2 / (F + t ^ 2 * R) := by
  have hweight : 0 ≤ 2 * t - t ^ 2 := by
    nlinarith [mul_nonneg ht0 (sub_nonneg.mpr ht1)]
  have hbase : 0 ≤ F + (2 * t - t ^ 2) * R :=
    add_nonneg hF (mul_nonneg hweight hR)
  have hnum : 0 ≤ t ^ 2 * (1 - t) ^ 2 * R ^ 2 := by positivity
  have hextra :
      0 ≤ t ^ 2 * (1 - t) ^ 2 * R ^ 2 / (F + t ^ 2 * R) :=
    div_nonneg hnum hden.le
  rw [scalar_tilted_capacity_expansion hden]
  linarith [hbase]

/-- Scalar Hodge-loss smoothing, stated in terms of the algebraic relation
`tau^2 * (s + q2) = s` satisfied by
`tau = sqrt (s / (s + q2))`.  Here `q2` denotes the shell energy `q^2`, so
the right side is the quartic shell bound `q^4 / (4 s^2)`. -/
theorem scalar_hodge_loss_smoothing
    {s q2 tau : ℝ} (hs : 0 < s) (hq2 : 0 ≤ q2)
    (htau : 0 ≤ tau) (htau_sq : tau ^ 2 * (s + q2) = s) :
    (1 - tau) ^ 2 ≤ q2 ^ 2 / (4 * s ^ 2) := by
  have hsq : 0 < s + q2 := by linarith
  have htau_sq_le_one : tau ^ 2 ≤ 1 := by
    apply le_of_mul_le_mul_right _ hsq
    rw [htau_sq]
    nlinarith
  have htau_le_one : tau ≤ 1 := by
    nlinarith [sq_nonneg (tau + 1)]
  have hid :
      q2 - 2 * s * (1 - tau) =
        (1 - tau) ^ 2 * (2 * tau + 1) * (s + q2) := by
    linear_combination (3 - 2 * tau) * htau_sq
  have hrem :
      0 ≤ (1 - tau) ^ 2 * (2 * tau + 1) * (s + q2) := by
    positivity
  have hlinear : 2 * s * (1 - tau) ≤ q2 := by
    linarith
  have hloss : 1 - tau ≤ q2 / (2 * s) := by
    apply (le_div_iff₀ (by positivity : 0 < 2 * s)).2
    nlinarith
  have hloss0 : 0 ≤ 1 - tau := sub_nonneg.mpr htau_le_one
  have hsq_loss : (1 - tau) ^ 2 ≤ (q2 / (2 * s)) ^ 2 :=
    (sq_le_sq₀ hloss0 (div_nonneg hq2 (by positivity))).2 hloss
  calc
    (1 - tau) ^ 2 ≤ (q2 / (2 * s)) ^ 2 := hsq_loss
    _ = q2 ^ 2 / (4 * s ^ 2) := by
      field_simp
      ring

/-- Square-root specialization of `scalar_hodge_loss_smoothing`. -/
theorem scalar_hodge_sqrt_loss_smoothing
    {s q2 : ℝ} (hs : 0 < s) (hq2 : 0 ≤ q2) :
    (1 - Real.sqrt (s / (s + q2))) ^ 2 ≤ q2 ^ 2 / (4 * s ^ 2) := by
  apply scalar_hodge_loss_smoothing hs hq2 (Real.sqrt_nonneg _)
  rw [Real.sq_sqrt (div_nonneg hs.le (by linarith : 0 ≤ s + q2))]
  field_simp

/-- A fixed tilt `t = 3/4` is not a generic consequence of full capacity:
for `F = R = 2` its exact capacity is `98/25`, below the demand `399/100`,
although the full capacity `F + R = 4` exceeds that demand. -/
theorem three_quarters_tilt_not_generically_forced :
    ((2 : ℝ) + (3 / 4 : ℝ) * 2) ^ 2 /
          ((2 : ℝ) + (3 / 4 : ℝ) ^ 2 * 2) = 98 / 25 ∧
      (98 / 25 : ℝ) < 399 / 100 ∧
        (399 / 100 : ℝ) < 2 + 2 := by
  norm_num

/-- A fully rational one-dimensional event-shell model showing that Hodge
domination is not forced by positivity of either incidence piece, strict old
Weil positivity, or even strict positivity of the enlarged Weil block.

The old and shell incidence matrices are

`[[1, 8/5], [8/5, 257/100]]` and
`[[3, -8/5], [-8/5, 64/75]]`.

Their cross terms cancel.  With old degree `31/75`, shell increment `3`, and
new degree `256/75`, the enlarged Weil block is the positive diagonal form
`(44/75) x^2 + (1/100) y^2`.  The coupled return capacity is `256/75`, while
the Hodge tilt satisfies `tau = 1/2`; hence the Hodge loss is `64/75`, much
larger than the Schur surplus `1/100`.

Thus the event-shell isometry and abstract Schur/Hodge algebra cannot prove
the desired zeta inequality.  A proof must use additional structure of the
actual prime--archimedean cross kernel. -/
theorem rational_hodge_event_countermodel :
    (∀ x y : ℝ,
      0 ≤ x ^ 2 + 2 * (8 / 5 : ℝ) * x * y +
        (257 / 100 : ℝ) * y ^ 2) ∧
    (∀ x y : ℝ,
      0 ≤ 3 * x ^ 2 + 2 * (-8 / 5 : ℝ) * x * y +
        (64 / 75 : ℝ) * y ^ 2) ∧
    0 < (1 : ℝ) - 31 / 75 ∧
    (∀ x y : ℝ,
      0 < x ^ 2 + y ^ 2 →
        0 < ((1 + 3) - 256 / 75) * x ^ 2 +
          ((257 / 100 + 64 / 75) - 256 / 75) * y ^ 2) ∧
    ((31 / 75 : ℝ) + 3 = 256 / 75) ∧
    ((1 / 2 : ℝ) ^ 2 * (1 + 3) = 1) ∧
    ((8 / 5 : ℝ) + (-8 / 5) = 0) ∧
    ((257 / 100 : ℝ) - (8 / 5) ^ 2 +
        (64 / 75 - (-8 / 5) ^ 2 / 3) = 1 / 100) ∧
    ((8 / 5 : ℝ) ^ 2 * (1 + 3) / (1 * 3) = 256 / 75) ∧
    (1 / 100 : ℝ) + 256 / 75 - 256 / 75 <
      (256 / 75) * (1 - 1 / 2) ^ 2 := by
  constructor
  · intro x y
    have hsquare : 0 ≤ (x + (8 / 5 : ℝ) * y) ^ 2 := sq_nonneg _
    have hy : 0 ≤ y ^ 2 := sq_nonneg _
    nlinarith
  constructor
  · intro x y
    have hsquare : 0 ≤ (x - (8 / 15 : ℝ) * y) ^ 2 := sq_nonneg _
    nlinarith
  constructor
  · norm_num
  constructor
  · intro x y hxy
    have hx : 0 ≤ x ^ 2 := sq_nonneg _
    have hy : 0 ≤ y ^ 2 := sq_nonneg _
    norm_num at hxy ⊢
    nlinarith
  norm_num

/-- Rational translation-model block from the cycle audit.  It is strictly
positive although the proper fresh capacity below misses its amplified
threshold. -/
theorem translationModel_fullBlock_positive (x y : ℝ) :
    0 ≤ (3 / 10 : ℝ) * x ^ 2 + 2 * (3 / 5 : ℝ) * x * y +
      (19 / 10 : ℝ) * y ^ 2 := by
  have hsquare : 0 ≤ (x + 2 * y) ^ 2 := sq_nonneg _
  have hy : 0 ≤ y ^ 2 := sq_nonneg _
  nlinarith

/-- In the same model the return-free fresh capacity is below the exact
amplified threshold. -/
theorem translationModel_freshCapacity_fails :
    (40 / 19 : ℝ) < 351 / 70 := by
  norm_num

/-- Adding the return channel raises the full capacity above the threshold. -/
theorem translationModel_fullCapacity_passes :
    (351 / 70 : ℝ) < 40 / 7 := by
  norm_num

/-- Once a maximal return-free capacity is below threshold, every smaller
explicit family (rays, exterior edges, or selected old-edge cycles) fails by
Loewner monotonicity in each scalar compression. -/
theorem subcapacity_fails_of_parent_below
    {subcapacity parentCapacity threshold : ℝ}
    (hsub : subcapacity ≤ parentCapacity)
    (hparent : parentCapacity < threshold) :
    ¬ threshold ≤ subcapacity := by
  linarith

end RHP2Bridge.IncidenceCycleObstruction
