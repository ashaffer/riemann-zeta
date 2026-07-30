import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk0 :
    P2RoundedFactorCheckpointData.sphericalOuter0 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter1 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter2 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter3 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨3, by decide⟩ := by
  decide +kernel

theorem sphericalOuter0_eq :
    P2RoundedFactorCheckpointData.sphericalOuter0 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨0, by decide⟩ := by
  exact sphericalOuterChunk0.1

theorem sphericalOuter1_eq :
    P2RoundedFactorCheckpointData.sphericalOuter1 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨1, by decide⟩ := by
  exact sphericalOuterChunk0.2.1

theorem sphericalOuter2_eq :
    P2RoundedFactorCheckpointData.sphericalOuter2 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨2, by decide⟩ := by
  exact sphericalOuterChunk0.2.2.1

theorem sphericalOuter3_eq :
    P2RoundedFactorCheckpointData.sphericalOuter3 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨3, by decide⟩ := by
  exact sphericalOuterChunk0.2.2.2

end RHP2Bridge
