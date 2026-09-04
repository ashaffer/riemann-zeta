/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Exact guards for the September 2026 correction pass

This file kernel-checks four elementary facts used to prevent stale claims
from re-entering the R105--R130 route:

* the R125 raw-to-critical normalization is exactly a change from scale `X`
  to scale `X / P`;
* the presence of both coefficient signs does not determine the sign of the
  resulting scalar aggregate;
* three tested terminal constructions are not an exhaustive classification
  without a theorem excluding a fourth case; and
* the complete-energy normalization `eta = kappa / 2` stays in its licensed
  domain when `0 < kappa <= 1`.

Once an external analytic audit has classified an estimate as already living
at quadratic-energy level, the final numeric ledger records that exponent
`1/2` has saving `1/2`, not `1`, against baseline exponent `1`.  Lean does
not establish that external classification.  These are exact algebraic and
logical guards only; no analytic zeta estimate, zero-free strip, or statement
of RH is proved here.
-/

namespace RHBridge.CorrectionGuards

/-! ## R125 scale normalization -/

/-- Additive-exponent form of R125 (2.10).  Substituting `log X` and `log P`
for `x` and `p` shows that division by the critical response removes exactly
the `P`-scale contribution. -/
theorem raw_sub_critical_exponent_identity (x p beta : ℝ) :
    (beta - 1 / 2) * x + (1 - beta) * p - (1 / 2) * p =
      (beta - 1 / 2) * (x - p) := by
  ring

/-- Exact positive-scale version of R125 (2.10):

`X^(beta-1/2) P^(1-beta) / P^(1/2) = (X/P)^(beta-1/2)`.

The left side is the raw off-line amplitude divided by the critical-line
response; the right side is the original relative exponent at scale `X/P`.
-/
theorem raw_div_critical_eq_reduced_scale
    {X P beta : ℝ} (hX : 0 < X) (hP : 0 < P) :
    X ^ (beta - 1 / 2) * P ^ (1 - beta) / P ^ (1 / 2 : ℝ) =
      (X / P) ^ (beta - 1 / 2) := by
  have hPnonneg : 0 ≤ P := hP.le
  calc
    X ^ (beta - 1 / 2) * P ^ (1 - beta) / P ^ (1 / 2 : ℝ) =
        X ^ (beta - 1 / 2) * (P ^ (1 - beta) / P ^ (1 / 2 : ℝ)) := by
      ring
    _ = X ^ (beta - 1 / 2) * P ^ ((1 - beta) - 1 / 2) := by
      congr 1
      exact (Real.rpow_sub hP (1 - beta) (1 / 2)).symm
    _ = X ^ (beta - 1 / 2) * P ^ (-(beta - 1 / 2)) := by
      congr 2
      ring
    _ = X ^ (beta - 1 / 2) * (P ^ (beta - 1 / 2))⁻¹ := by
      rw [Real.rpow_neg hPnonneg]
    _ = X ^ (beta - 1 / 2) / P ^ (beta - 1 / 2) := by
      exact (div_eq_mul_inv _ _).symm
    _ = (X / P) ^ (beta - 1 / 2) := by
      rw [Real.div_rpow hX.le hP.le]

/-! ## Signed coefficients do not determine aggregate sign -/

/-- A two-term scalar aggregate, enough to state the sign counterexample
without importing any analytic kernel. -/
def pairAggregate (c₀ c₁ v₀ v₁ : ℝ) : ℝ := c₀ * v₀ + c₁ * v₁

/-- The explicit coefficients `(-1, 2)` have both signs, both sampled values
are nonnegative, and nevertheless their aggregate is strictly positive.  This
is an abstract two-term counterexample, not a model of the R124 kernel. -/
theorem signed_coefficients_positive_aggregate :
    (-1 : ℝ) < 0 ∧ 0 < (2 : ℝ) ∧ 0 ≤ (1 : ℝ) ∧ 0 ≤ (1 : ℝ) ∧
      0 < pairAggregate (-1) 2 1 1 := by
  norm_num [pairAggregate]

/-- Hence no purely formal rule can infer a nonpositive aggregate from
"the coefficients have both signs", even when the sampled values are
nonnegative.  An order-reflecting theorem needs additional structure. -/
theorem signed_coefficients_do_not_force_nonpositive :
    ¬ ∀ c₀ c₁ v₀ v₁ : ℝ,
      c₀ < 0 → 0 < c₁ → 0 ≤ v₀ → 0 ≤ v₁ →
        pairAggregate c₀ c₁ v₀ v₁ ≤ 0 := by
  intro h
  have hbad := h (-1) 2 1 1 (by norm_num) (by norm_num) (by norm_num) (by norm_num)
  norm_num [pairAggregate] at hbad

/-! ## The three tested routes are not an exhaustive ambient classification -/

/-- Four ambient possibilities, only three of which name the terminal
constructions actually tested in the correction report.  `unclassified`
does not assert that a new analytic route works; it is the logical witness
showing that a three-case exhaustion theorem needs an additional premise. -/
inductive AmbientRouteCase where
  | localRestriction
  | faithfulRestoration
  | filteredFaithfulness
  | unclassified
  deriving DecidableEq, Fintype

/-- Membership in the three tested terminal constructions. -/
def IsTestedRoute : AmbientRouteCase → Prop
  | .localRestriction => True
  | .faithfulRestoration => True
  | .filteredFaithfulness => True
  | .unclassified => False

theorem unclassified_is_not_tested : ¬ IsTestedRoute .unclassified := by
  simp [IsTestedRoute]

/-- The three tested dispositions are not exhaustive in this four-case
ambient type. -/
theorem tested_routes_not_exhaustive : ¬ ∀ route, IsTestedRoute route := by
  intro h
  exact unclassified_is_not_tested (h .unclassified)

/-! ## Licensed `kappa`/`eta` domain -/

/-- The complete-energy map `eta = kappa/2` sends `0 < kappa <= 1` into
`0 < eta <= 1/2`.  This is domain algebra; it does not prove the analytic
energy-to-strip correspondence or assert that the algebraic formula fails
outside the licensed analytic domain. -/
theorem kappa_half_in_strip_domain {kappa : ℝ}
    (hpos : 0 < kappa) (hupper : kappa ≤ 1) :
    0 < kappa / 2 ∧ kappa / 2 ≤ 1 / 2 := by
  constructor <;> linarith

/-- Conversely, `kappa = 2 eta` sends the licensed strip-width domain back
to `0 < kappa <= 1`. -/
theorem twice_eta_in_energy_domain {eta : ℝ}
    (hpos : 0 < eta) (hupper : eta ≤ 1 / 2) :
    0 < 2 * eta ∧ 2 * eta ≤ 1 := by
  constructor <;> linarith

/-! ## Already-quadratic exponent guard -/

/-- Numeric saving measured relative to an explicitly supplied baseline.
The surrounding analytic argument, not this definition, must establish that
the baseline and estimate refer to the same energy-level quantity. -/
def exponentSaving (baseline estimate : ℝ) : ℝ := baseline - estimate

/-- Conditional numeric ledger: after the external R116 audit has identified
the contribution as part of an energy with baseline exponent `1`, exponent
`1/2` gives a one-half saving. -/
theorem already_quadratic_half_saving : exponentSaving 1 (1 / 2) = 1 / 2 := by
  norm_num [exponentSaving]

/-- In particular it is not a full-power saving at that same energy level;
squaring it again would silently change the externally supplied baseline.
This theorem checks the arithmetic and does not itself type the R116 object. -/
theorem already_quadratic_not_full_saving : exponentSaving 1 (1 / 2) ≠ 1 := by
  norm_num [exponentSaving]

/-! ## Synchronized non-formal correction IDs

The human report and canonical `Z23C/1` compact ledger also carry
`C06`--`C14`: packet scope,
detector-family quantifiers, S1 admission status, authority validation,
historical-cache warnings, checkpoint fingerprints, unattached historical
digests, dated handoff language, and the local authority manifest.  Those are
source/provenance or analytic-scope assertions rather than propositions proved
by the elementary model in this file.  They deliberately have no fabricated
Lean theorem.  The generated random-access `Z23V/1` working-state vector is
also non-formal and deliberately lossy: it records conclusions, priorities,
and prohibitions, not proof terms or hidden reasoning.  The JSON and `Z23V`
files are checked projections rather than independent authorities.
`C15` has finite dual and exponent guards in the separate
`QPSourceFiberBifurcation` module; its real-node and actual-prime scope is
recorded in the human and compact authorities rather than fabricated here.
`C16` has its finite factorization, square-root-block, and shifted-resolvent
guards in the separate `ExteriorFactorizationAudit` module; Douglas's theorem,
the completed source, the strip calibration, and RH are not formalized there.
`verify_zeta23_correction_bundle.py` checks that this formal scope, the
Markdown claims, and the compact ledger stay synchronized.
-/

end RHBridge.CorrectionGuards
