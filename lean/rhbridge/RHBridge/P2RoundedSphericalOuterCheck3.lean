import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk3 :
    P2RoundedFactorCheckpointData.sphericalOuter12 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter13 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter14 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter15 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨15, by decide⟩ := by
  decide +kernel

theorem sphericalOuter12_eq :
    P2RoundedFactorCheckpointData.sphericalOuter12 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨12, by decide⟩ := by
  exact sphericalOuterChunk3.1

theorem sphericalOuter13_eq :
    P2RoundedFactorCheckpointData.sphericalOuter13 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨13, by decide⟩ := by
  exact sphericalOuterChunk3.2.1

theorem sphericalOuter14_eq :
    P2RoundedFactorCheckpointData.sphericalOuter14 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨14, by decide⟩ := by
  exact sphericalOuterChunk3.2.2.1

theorem sphericalOuter15_eq :
    P2RoundedFactorCheckpointData.sphericalOuter15 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨15, by decide⟩ := by
  exact sphericalOuterChunk3.2.2.2

end RHP2Bridge
