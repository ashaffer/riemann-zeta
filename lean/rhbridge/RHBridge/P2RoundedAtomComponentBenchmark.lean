import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedCanonical

open RoundedRatPoly

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

def benchmarkCells200 : ℕ := 10 ^ 200 - 1

def atomizedFirstComponentApprox : Approx :=
  rounded benchmarkCells200 1
    (DenseRatPoly.affine
      (DenseRatPoly.p2SelectedComponent100ScaleCenterPolynomial
        .even (0 : Fin 24) (p2PanelCenterQ 0))
      0 (p2PanelHalfWidthQ 0))

def atomizedLastHighComponentApprox : Approx :=
  rounded benchmarkCells200 1
    (DenseRatPoly.affine
      (DenseRatPoly.p2SelectedComponent100ScaleCenterPolynomial
        .odd (23 : Fin 24) (p2PanelCenterQ 31))
      0 (p2PanelHalfWidthQ 31))

#eval
  let a := atomizedFirstComponentApprox
  (a.coeffs.length,
    decide (a.error < 1 / 10 ^ 30),
    decide (a.error < 1 / 10 ^ 60),
    decide (a.error < 1 / 10 ^ 100))

#eval
  let a := atomizedLastHighComponentApprox
  (a.coeffs.length,
    decide (a.error < 1 / 10 ^ 100),
    decide (a.error < 1 / 10 ^ 150),
    decide (a.error < 1 / 10 ^ 190))

theorem atomizedFirstComponent_kernelSentinel :
    atomizedFirstComponentApprox.error < 1 / 10 ^ 180 := by
  decide +kernel

end RHP2Bridge.P2RoundedCanonical
