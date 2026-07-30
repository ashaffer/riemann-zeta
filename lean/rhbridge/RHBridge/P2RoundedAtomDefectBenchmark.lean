import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedCanonical

open RoundedRatPoly

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

def benchmarkCells200 : ℕ := 10 ^ 200 - 1

def atomizedFirstDefectApprox : Approx :=
  rounded benchmarkCells200 1
    (DenseRatPoly.affine
      (DenseRatPoly.p2DefectPanelPolynomial (p2PanelCenterQ 0) 32)
      0 (p2PanelHalfWidthQ 0))

def atomizedLastDefectApprox : Approx :=
  rounded benchmarkCells200 1
    (DenseRatPoly.affine
      (DenseRatPoly.p2DefectPanelPolynomial (p2PanelCenterQ 31) 32)
      0 (p2PanelHalfWidthQ 31))

#eval
  let a := atomizedFirstDefectApprox
  (a.coeffs.length,
    decide (a.error < 1 / 10 ^ 30),
    decide (a.error < 1 / 10 ^ 60),
    decide (a.error < 1 / 10 ^ 100))

#eval
  let a := atomizedLastDefectApprox
  (a.coeffs.length,
    decide (a.error < 1 / 10 ^ 100),
    decide (a.error < 1 / 10 ^ 150),
    decide (a.error < 1 / 10 ^ 190))

end RHP2Bridge.P2RoundedCanonical
