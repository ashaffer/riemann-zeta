import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge.P2RoundedExplicitOuterBenchmark

open P2RoundedSharedEvaluator
open P2RoundedFactorCheckpointData

def mode0Panel0 : RoundedRatPoly.Approx :=
  componentApproxFromOuter sphericalOuter0 .even 0 0

#eval mode0Panel0.coeffs.length
#eval mode0Panel0.error < (1 / 10 ^ 100 : ℚ)
#eval mode0Panel0.error < (1 / 10 ^ 150 : ℚ)
#eval mode0Panel0.error < (1 / 10 ^ 180 : ℚ)

example : mode0Panel0.coeffs.length = 101 := by decide +kernel

example : mode0Panel0.error < (1 / 10 ^ 150 : ℚ) := by
  decide +kernel

end RHP2Bridge.P2RoundedExplicitOuterBenchmark
