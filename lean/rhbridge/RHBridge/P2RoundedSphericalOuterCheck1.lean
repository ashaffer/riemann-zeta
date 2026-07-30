import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk1 :
    P2RoundedFactorCheckpointData.sphericalOuter4 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter5 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter6 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter7 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨7, by decide⟩ := by
  decide +kernel

theorem sphericalOuter4_eq :
    P2RoundedFactorCheckpointData.sphericalOuter4 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨4, by decide⟩ := by
  exact sphericalOuterChunk1.1

theorem sphericalOuter5_eq :
    P2RoundedFactorCheckpointData.sphericalOuter5 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨5, by decide⟩ := by
  exact sphericalOuterChunk1.2.1

theorem sphericalOuter6_eq :
    P2RoundedFactorCheckpointData.sphericalOuter6 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨6, by decide⟩ := by
  exact sphericalOuterChunk1.2.2.1

theorem sphericalOuter7_eq :
    P2RoundedFactorCheckpointData.sphericalOuter7 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨7, by decide⟩ := by
  exact sphericalOuterChunk1.2.2.2

end RHP2Bridge
