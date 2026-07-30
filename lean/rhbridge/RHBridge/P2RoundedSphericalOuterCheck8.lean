import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk8 :
    P2RoundedFactorCheckpointData.sphericalOuter32 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨32, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter33 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨33, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter34 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨34, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter35 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨35, by decide⟩ := by
  decide +kernel

theorem sphericalOuter32_eq :
    P2RoundedFactorCheckpointData.sphericalOuter32 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨32, by decide⟩ := by
  exact sphericalOuterChunk8.1

theorem sphericalOuter33_eq :
    P2RoundedFactorCheckpointData.sphericalOuter33 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨33, by decide⟩ := by
  exact sphericalOuterChunk8.2.1

theorem sphericalOuter34_eq :
    P2RoundedFactorCheckpointData.sphericalOuter34 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨34, by decide⟩ := by
  exact sphericalOuterChunk8.2.2.1

theorem sphericalOuter35_eq :
    P2RoundedFactorCheckpointData.sphericalOuter35 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨35, by decide⟩ := by
  exact sphericalOuterChunk8.2.2.2

end RHP2Bridge
