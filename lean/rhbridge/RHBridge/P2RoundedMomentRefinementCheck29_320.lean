import RHBridge.P2RoundedMomentLengths29
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29BoundedRefinementRange320 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel29BoundedRefinementAt
      320 352 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel29BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
