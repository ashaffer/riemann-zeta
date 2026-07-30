import RHBridge.P2RoundedSphericalOuterData
import RHBridge.P2RoundedPanelTargetData0

namespace RHP2Bridge.P2RoundedGrid100Benchmark

open P2RoundedSharedEvaluator
open P2RoundedPanelTargetData
open P2RoundedFactorCheckpointData

def cells100 : ℕ := 10 ^ 100 - 1

def prefix100 (n : ℕ) : RoundedRatPoly.Approx :=
  RoundedRatPoly.rounded cells100 1
    (exactNormalizedPrefixTerm (n % 64) ⟨0, by decide⟩)

def defect100 : RoundedRatPoly.Approx :=
  RoundedRatPoly.add cells100 1
    (RoundedRatPoly.sumRangeRounded cells100 1 64 prefix100)
    (RoundedRatPoly.rounded cells100 1
      (exactNormalizedNonprefix ⟨0, by decide⟩))

def component100 : RoundedRatPoly.Approx :=
  RoundedRatPoly.scale cells100 1
    (RatPoly.p2SelectedPhaseQ .even 0 *
      p2SelectedScaleCenterQ .even ⟨0, by decide⟩)
    (RoundedRatPoly.compRounded cells100 1 sphericalOuter0
      (normalizedSphericalArgumentApprox ⟨0, by decide⟩))

def entry100 : RoundedRatPoly.Approx :=
  let component := component100
  let pair := RoundedRatPoly.mul cells100 1 component component
  RoundedRatPoly.mul cells100 1 defect100 pair

def ball100 : QBall :=
  entryBallFromApprox ⟨0, by decide⟩ entry100

def coarseTarget0 : QBall :=
  ⟨panel0TargetQ ⟨0, by decide⟩, panelAllowanceQ⟩

def benchmarkResult : ℕ × ℕ × ℕ × Bool × Bool × Bool × Bool :=
  let defect := defect100
  let component := component100
  let pair := RoundedRatPoly.mul cells100 1 component component
  let entry := RoundedRatPoly.mul cells100 1 defect pair
  let ball := entryBallFromApprox ⟨0, by decide⟩ entry
  (defect.coeffs.length,
    component.coeffs.length,
    entry.coeffs.length,
    defect.error < (1 / 10 ^ 80 : ℚ),
    component.error < (1 / 10 ^ 80 : ℚ),
    ball.radius < (1 / 10 ^ 70 : ℚ),
    |ball.center - coarseTarget0.center| + ball.radius ≤
      coarseTarget0.radius)

#eval benchmarkResult

def component47_100 : RoundedRatPoly.Approx :=
  RoundedRatPoly.scale cells100 1
    (RatPoly.p2SelectedPhaseQ .odd 23 *
      p2SelectedScaleCenterQ .odd ⟨23, by decide⟩)
    (RoundedRatPoly.compRounded cells100 1 sphericalOuter47
      (normalizedSphericalArgumentApprox ⟨0, by decide⟩))

def entry599_100 : RoundedRatPoly.Approx :=
  let component := component47_100
  let pair := RoundedRatPoly.mul cells100 1 component component
  RoundedRatPoly.mul cells100 1 defect100 pair

def ball599_100 : QBall :=
  entryBallFromApprox ⟨0, by decide⟩ entry599_100

def coarseTarget599 : QBall :=
  ⟨panel0TargetQ ⟨599, by decide⟩, panelAllowanceQ⟩

def benchmarkWorstResult : ℕ × ℕ × List Bool :=
  let defect := defect100
  let component := component47_100
  let pair := RoundedRatPoly.mul cells100 1 component component
  let entry := RoundedRatPoly.mul cells100 1 defect pair
  let ball := entryBallFromApprox ⟨0, by decide⟩ entry
  (component.coeffs.length,
    entry.coeffs.length,
    [component.error < (1 / 10 ^ 70 : ℚ),
      ball.radius < (1 / 10 ^ 50 : ℚ),
      ball.radius < (1 / 10 ^ 60 : ℚ),
      ball.radius < (1 / 10 ^ 70 : ℚ),
      |ball.center - coarseTarget599.center| + ball.radius ≤
        coarseTarget599.radius])

#eval benchmarkWorstResult

end RHP2Bridge.P2RoundedGrid100Benchmark
