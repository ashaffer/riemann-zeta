/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2ComponentBounds
import RHBridge.P2ElementaryConstants

/-!
# Rational centers for all 48 canonical p=2 spherical scales

The decimal values are certificate data only.  Lean checks every enclosure
by exact rational squaring against the analytic square identity for the
normalization scale.
-/

namespace RHP2Bridge

def p2ScaleCenterQ : ℕ → ℚ
  | 0 => 93541434669348534640 / 10 ^ 20
  | 1 => 162018517460196505774 / 10 ^ 20
  | 2 => 209165006633518886995 / 10 ^ 20
  | 3 => 247487373415291633540 / 10 ^ 20
  | 4 => 280624304008045603919 / 10 ^ 20
  | 5 => 310241841149771414903 / 10 ^ 20
  | 6 => 337268439080801036639 / 10 ^ 20
  | 7 => 362284418654735964343 / 10 ^ 20
  | 8 => 385681215513537812227 / 10 ^ 20
  | 9 => 407737660757502261903 / 10 ^ 20
  | 10 => 428660704987056167185 / 10 ^ 20
  | 11 => 448608961123159018869 / 10 ^ 20
  | 12 => 467707173346742673198 / 10 ^ 20
  | 13 => 486055552380589517322 / 10 ^ 20
  | 14 => 503736041990247110410 / 10 ^ 20
  | 15 => 520816666399991466325 / 10 ^ 20
  | 16 => 537354631505116925981 / 10 ^ 20
  | 17 => 553398590529466383100 / 10 ^ 20
  | 18 => 568990333837052103572 / 10 ^ 20
  | 19 => 584166072277396130533 / 10 ^ 20
  | 20 => 598957427535546970280 / 10 ^ 20
  | 21 => 613392207319264857320 / 10 ^ 20
  | 22 => 627495019900556660984 / 10 ^ 20
  | 23 => 641287766919033003317 / 10 ^ 20
  | 24 => 654790042685439742477 / 10 ^ 20
  | 25 => 668019460794369373138 / 10 ^ 20
  | 26 => 680991923593811793747 / 10 ^ 20
  | 27 => 693721846275580397337 / 10 ^ 20
  | 28 => 706222344591276720955 / 10 ^ 20
  | 29 => 718505393159995703035 / 10 ^ 20
  | 30 => 730581959810122877907 / 10 ^ 20
  | 31 => 742462120245874900621 / 10 ^ 20
  | 32 => 754155156449917804313 / 10 ^ 20
  | 33 => 765669641555677718644 / 10 ^ 20
  | 34 => 777013513396002656677 / 10 ^ 20
  | 35 => 788194138521722324537 / 10 ^ 20
  | 36 => 799218368157289037666 / 10 ^ 20
  | 37 => 810092587300982528871 / 10 ^ 20
  | 38 => 820822757969100172049 / 10 ^ 20
  | 39 => 831414457415794520414 / 10 ^ 20
  | 40 => 841872912024136811756 / 10 ^ 20
  | 41 => 852203027452965576473 / 10 ^ 20
  | 42 => 862409415533017009512 / 10 ^ 20
  | 43 => 872496418330757389935 / 10 ^ 20
  | 44 => 882468129736139536240 / 10 ^ 20
  | 45 => 892328414878737345255 / 10 ^ 20
  | 46 => 902080927633435779647 / 10 ^ 20
  | 47 => 911729126440523452031 / 10 ^ 20
  | _ => 0

noncomputable def p2ScaleCenter (n : ℕ) : ℝ :=
  (p2ScaleCenterQ n : ℝ)

theorem p2LegendreSphericalScale_eq_sqrt (n : ℕ) :
    p2LegendreSphericalScale n =
      Real.sqrt (7 * (2 * (n : ℝ) + 1) / 8) := by
  apply (sq_eq_sq₀ (p2LegendreSphericalScale_nonneg n)
    (Real.sqrt_nonneg _)).mp
  rw [p2LegendreSphericalScale_sq,
    Real.sq_sqrt (by positivity : (0 : ℝ) ≤ 7 * (2 * (n : ℝ) + 1) / 8)]

private theorem abs_sqrt_sub_center_lt_of_sq
    {x c e : ℝ} (hx : 0 ≤ x) (hl : 0 ≤ c - e) (hu : 0 ≤ c + e)
    (hlo : (c - e) ^ 2 < x) (hhi : x < (c + e) ^ 2) :
    |Real.sqrt x - c| < e := by
  have h := sqrt_mem_Ioo_of_sq_lt hx hl hu hlo hhi
  rw [abs_lt]
  constructor <;> linarith [h.1, h.2]

set_option maxHeartbeats 1000000 in
-- Exact squaring of all 48 twenty-digit decimal intervals exceeds the default budget.
/-- Every generated scale center is within `10⁻²⁰` of the exact canonical
normalization. -/
theorem abs_p2LegendreSphericalScale_sub_center_lt (n : Fin 48) :
    |p2LegendreSphericalScale n.val - p2ScaleCenter n.val| < 1 / 10 ^ 20 := by
  rw [p2LegendreSphericalScale_eq_sqrt]
  fin_cases n <;>
    apply abs_sqrt_sub_center_lt_of_sq <;>
    norm_num [p2ScaleCenter, p2ScaleCenterQ]

end RHP2Bridge
