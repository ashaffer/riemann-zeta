import RHBridge.P2RoundedSharedEvaluator

namespace RHP2Bridge

open P2RoundedSharedEvaluator

def factorGridCells100 : ℕ := 10 ^ 100 - 1

def panel0Prefix0Grid100 : RoundedRatPoly.Approx :=
  RoundedRatPoly.rounded factorGridCells100 1
    (exactNormalizedPrefixTerm 0 ⟨0, by decide⟩)

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0Prefix0Grid100_shape_and_error :
    panel0Prefix0Grid100.coeffs.length = 64 ∧
      panel0Prefix0Grid100.error < 1 / 10 ^ 90 := by
  decide +kernel

end RHP2Bridge
