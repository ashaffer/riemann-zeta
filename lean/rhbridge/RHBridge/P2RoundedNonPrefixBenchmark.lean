import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedCanonical

open RoundedRatPoly

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

def firstNormalizedNonPrefixApprox : Approx :=
  rounded gridCells 1
    (DenseRatPoly.affine
      (DenseRatPoly.shift DenseRatPoly.p2RationalNonPrefixPoly
        (p2PanelCenterQ 0))
      0 (p2PanelHalfWidthQ 0))

def firstDirectNormalizedNonPrefixApprox : Approx :=
  rounded gridCells 1
    (DenseRatPoly.affine DenseRatPoly.p2RationalNonPrefixPoly
      (p2PanelCenterQ 0) (p2PanelHalfWidthQ 0))

#eval
  let a := firstNormalizedNonPrefixApprox
  (a.coeffs.length,
    decide (a.error < 1 / 10 ^ 180),
    decide (a.error < 1 / 10 ^ 190))

#eval firstDirectNormalizedNonPrefixApprox.coeffs.length

theorem firstNormalizedNonPrefix_kernelSentinel :
    firstNormalizedNonPrefixApprox.error < 1 / 10 ^ 180 := by
  decide +kernel

end RHP2Bridge.P2RoundedCanonical
