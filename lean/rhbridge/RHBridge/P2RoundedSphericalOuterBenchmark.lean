import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedCanonical

open RoundedRatPoly

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

def sphericalOuterApprox200 (n : ℕ) : Approx :=
  rounded gridCells 22 (DenseRatPoly.sphericalJRealPolynomial n 100)

def sphericalOuterApprox300 (n : ℕ) : Approx :=
  rounded (10 ^ 300 - 1) 22
    (DenseRatPoly.sphericalJRealPolynomial n 100)

#eval
  let a := sphericalOuterApprox200 0
  let b := sphericalOuterApprox200 47
  (a.coeffs.length,
    decide (a.error < 1 / 10 ^ 20),
    decide (a.error < 1 / 10 ^ 50),
    b.coeffs.length,
    decide (b.error < 1 / 10 ^ 20),
    decide (b.error < 1 / 10 ^ 50))

#eval
  let a := sphericalOuterApprox300 0
  let b := sphericalOuterApprox300 47
  (a.coeffs.length,
    decide (a.error < 1 / 10 ^ 50),
    decide (a.error < 1 / 10 ^ 100),
    b.coeffs.length,
    decide (b.error < 1 / 10 ^ 50),
    decide (b.error < 1 / 10 ^ 100))

theorem sphericalOuter300_mode0_kernelSentinel :
    (sphericalOuterApprox300 0).error < 1 / 10 ^ 100 := by
  decide +kernel

theorem sphericalOuter300_mode47_kernelSentinel :
    (sphericalOuterApprox300 47).error < 1 / 10 ^ 100 := by
  decide +kernel

end RHP2Bridge.P2RoundedCanonical
