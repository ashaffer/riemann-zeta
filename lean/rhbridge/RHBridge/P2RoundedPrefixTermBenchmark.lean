import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedCanonical

open RoundedRatPoly

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

def firstNormalizedPrefixTermApprox : Approx :=
  rounded gridCells 1
    (DenseRatPoly.affine
      (DenseRatPoly.quarterPrefixTermPolynomial
        0 (p2PanelCenterQ 0) 32)
      0 (p2PanelHalfWidthQ 0))

#eval
  let a := firstNormalizedPrefixTermApprox
  (a.coeffs.length,
    decide (a.error < 1 / 10 ^ 180),
    decide (a.error < 1 / 10 ^ 190))

theorem firstNormalizedPrefixTerm_kernelSentinel :
    firstNormalizedPrefixTermApprox.error < 1 / 10 ^ 180 := by
  decide +kernel

end RHP2Bridge.P2RoundedCanonical
