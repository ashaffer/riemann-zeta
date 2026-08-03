/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.BoundaryCollarGeometry

/-!
# Scale-uniform Fourier leakage bookkeeping

The analytic uncertainty estimate for a function supported on a set of
measure `2 * δ` is

`∫_{|ξ| ≤ R} |fhat ξ|² ≤ 4 * R * δ * ‖f‖²`.

This file proves the exact algebraic consequences used by the collar
argument.  The Fourier estimate itself is deliberately left as a named
premise until the measure-theoretic support predicate is connected to the
chosen `L²` representatives; no Weil positivity is used here.
-/

namespace RHP2Bridge.ScaleUniformLeakage

noncomputable section

/-- Data supplied by Plancherel and the compact-support Fourier bound. -/
structure LeakageData (δ R total band exterior : ℝ) : Prop where
  nonneg : 0 ≤ total
  split : total = band + exterior
  band_nonneg : 0 ≤ band
  band_upper : band ≤ 4 * R * δ * total

/-- A collar of width `δ` loses at most the fraction `4 R δ` of its Fourier
energy to the fixed band `[-R,R]`. -/
theorem exterior_lower {δ R total band exterior : ℝ}
    (h : LeakageData δ R total band exterior) :
    (1 - 4 * R * δ) * total ≤ exterior := by
  calc
    (1 - 4 * R * δ) * total = total - 4 * R * δ * total := by ring
    _ ≤ total - band := sub_le_sub_left h.band_upper total
    _ = exterior := by linarith [h.split]

/-- At the scale `R δ ≤ 1/8`, at least half of the Fourier mass lies outside
the band.  The constant is independent of the collar width. -/
theorem half_mass_exterior {δ R total band exterior : ℝ}
    (h : LeakageData δ R total band exterior)
    (hscale : R * δ ≤ 1 / 8) :
    total / 2 ≤ exterior := by
  have hfour : 4 * R * δ ≤ 1 / 2 := by nlinarith
  have hlower := exterior_lower h
  nlinarith [h.nonneg]

/-- Weighted version: an exterior multiplier floor converts leakage directly
to a scale-uniform energy floor. -/
theorem weighted_exterior_lower {δ R total band exterior weightedFloor : ℝ}
    (h : LeakageData δ R total band exterior)
    (hscale : R * δ ≤ 1 / 8)
    (hfloor : 0 ≤ weightedFloor) :
    weightedFloor * total / 2 ≤ weightedFloor * exterior := by
  calc
    weightedFloor * total / 2 = weightedFloor * (total / 2) := by ring
    _ ≤ weightedFloor * exterior :=
      mul_le_mul_of_nonneg_left (half_mass_exterior h hscale) hfloor

end

end RHP2Bridge.ScaleUniformLeakage
