import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedCanonical

open RoundedRatPoly

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

def scratchCachedFirstPanelApprox : Approx :=
  let d := normalizedDefectApprox (0 : Fin 32)
  let u := normalizedComponentApprox .even (0 : Fin 24) (0 : Fin 32)
  mul gridCells 1 d (mul gridCells 1 u u)

#eval
  let radius := 2 * p2PanelHalfWidthQ 0 * scratchCachedFirstPanelApprox.error
  (radius ≤ 1 / 10 ^ 50,
    radius ≤ 1 / 10 ^ 100,
    radius ≤ 1 / 10 ^ 150,
    radius ≤ 1 / 10 ^ 200,
    radius ≤ 1 / 10 ^ 250)

example :
    2 * p2PanelHalfWidthQ 0 * scratchCachedFirstPanelApprox.error ≤
      1 / 10 ^ 50 := by
  decide +kernel

end RHP2Bridge.P2RoundedCanonical
