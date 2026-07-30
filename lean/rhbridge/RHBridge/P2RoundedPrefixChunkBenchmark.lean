import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedCanonical

open RoundedRatPoly

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

def normalizedPrefixTermApprox (n : ℕ) : Approx :=
  rounded gridCells 1
    (DenseRatPoly.affine
      (DenseRatPoly.quarterPrefixTermPolynomial
        n (p2PanelCenterQ 0) 32)
      0 (p2PanelHalfWidthQ 0))

theorem firstFourPrefixTerms_kernelSentinel :
    (normalizedPrefixTermApprox 0).error < 1 / 10 ^ 180 ∧
    (normalizedPrefixTermApprox 1).error < 1 / 10 ^ 180 ∧
    (normalizedPrefixTermApprox 2).error < 1 / 10 ^ 180 ∧
    (normalizedPrefixTermApprox 3).error < 1 / 10 ^ 180 := by
  decide +kernel

end RHP2Bridge.P2RoundedCanonical
