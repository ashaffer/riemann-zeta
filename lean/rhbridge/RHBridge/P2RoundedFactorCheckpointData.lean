/- Generated base definitions for p=2 rounded factor checkpoints. -/
import RHBridge.P2RoundedSharedEvaluator

namespace RHP2Bridge.P2RoundedFactorCheckpointData

open P2RoundedSharedEvaluator

/-- Derived from the production evaluator to prevent generator/Lean drift. -/
def factorScale : Nat := P2RoundedCanonical.gridCells + 1

def approxOfScaled (coefficients : List Int) (error : Int) :
    RoundedRatPoly.Approx where
  coeffs := coefficients.map fun z => (z : ℚ) / factorScale
  error := (error : ℚ) / factorScale

/-- Likewise share the exact global-outer grid with the semantic evaluator. -/
def sphericalOuterGridCells : Nat :=
  P2RoundedSharedEvaluator.sphericalOuterCells
def sphericalOuterScale : Nat := sphericalOuterGridCells + 1

def outerApproxOfScaled (coefficients : List Int) (error : Int) :
    RoundedRatPoly.Approx where
  coeffs := coefficients.map fun z => (z : ℚ) / sphericalOuterScale
  error := (error : ℚ) / sphericalOuterScale

def computedSphericalOuter (n : Fin 48) : RoundedRatPoly.Approx :=
  RoundedRatPoly.rounded sphericalOuterGridCells 22
    (DenseRatPoly.sphericalJRealPolynomial n.val 100)

theorem computedSphericalOuter_encloses (n : Fin 48) :
    RoundedRatPoly.Encloses 22
      (RoundedRatPoly.evalReal
        (DenseRatPoly.sphericalJRealPolynomial n.val 100))
      (computedSphericalOuter n) := by
  exact RoundedRatPoly.rounded_encloses sphericalOuterGridCells
    (by norm_num) _

end RHP2Bridge.P2RoundedFactorCheckpointData
