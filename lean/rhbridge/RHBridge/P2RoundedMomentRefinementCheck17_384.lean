import RHBridge.P2RoundedMomentLengths17
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17BoundedRefinementRange384 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel17BoundedRefinementAt
      384 416 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel17BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
