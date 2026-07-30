import RHBridge.P2CanonicalRounded
import Batteries.Data.Rat.Float

namespace RHP2Bridge.P2RoundedCanonical

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

#eval
  let a := normalizedPanelApprox .even (0 : Fin 24) (0 : Fin 24) (0 : Fin 32)
  (a.coeffs.length, (a.error : Float),
    (panelIntegralRadiusQ .even (0 : Fin 24) (0 : Fin 24) (0 : Fin 32) : Float))

end RHP2Bridge.P2RoundedCanonical
