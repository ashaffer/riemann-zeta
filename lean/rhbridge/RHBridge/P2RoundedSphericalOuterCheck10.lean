import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk10 :
    P2RoundedFactorCheckpointData.sphericalOuter40 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨40, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter41 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨41, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter42 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨42, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter43 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨43, by decide⟩ := by
  decide +kernel

theorem sphericalOuter40_eq :
    P2RoundedFactorCheckpointData.sphericalOuter40 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨40, by decide⟩ := by
  exact sphericalOuterChunk10.1

theorem sphericalOuter41_eq :
    P2RoundedFactorCheckpointData.sphericalOuter41 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨41, by decide⟩ := by
  exact sphericalOuterChunk10.2.1

theorem sphericalOuter42_eq :
    P2RoundedFactorCheckpointData.sphericalOuter42 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨42, by decide⟩ := by
  exact sphericalOuterChunk10.2.2.1

theorem sphericalOuter43_eq :
    P2RoundedFactorCheckpointData.sphericalOuter43 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨43, by decide⟩ := by
  exact sphericalOuterChunk10.2.2.2

end RHP2Bridge
