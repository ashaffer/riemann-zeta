import RHBridge.P2RoundedMomentLengths16
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16BoundedRefinementRange32 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel16BoundedRefinementAt
      32 64 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel16BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
