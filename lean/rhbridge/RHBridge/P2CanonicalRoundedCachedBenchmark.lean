import RHBridge.P2CanonicalRounded
import Batteries.Data.Rat.Float

namespace RHP2Bridge.P2RoundedCanonical

open RoundedRatPoly

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

def cachedFirstPanelApprox : Approx :=
  let d := normalizedDefectApprox (0 : Fin 32)
  let u := normalizedComponentApprox .even (0 : Fin 24) (0 : Fin 32)
  mul gridCells 1 d (mul gridCells 1 u u)

#eval
  let a := cachedFirstPanelApprox
  let radius := 2 * p2PanelHalfWidthQ 0 * a.error
  let center := p2PanelHalfWidthQ 0 *
    DenseRatPoly.exactIntegral a.coeffs (-1) 1
  (a.coeffs.length,
    decide (radius < 1 / 10 ^ 20),
    decide (radius < 1 / 10 ^ 50),
    decide (radius < 1 / 10 ^ 100),
    decide (radius < 1 / 10 ^ 150),
    decide (radius < 1 / 10 ^ 200),
    decide (radius < 1 / 10 ^ 220),
    decide (radius < 1 / 10 ^ 240),
    decide (radius < 1 / 10 ^ 260),
    decide (radius < 1 / 10 ^ 280),
    decide (|center| < 100))

end RHP2Bridge.P2RoundedCanonical
