import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk5 :
    P2RoundedFactorCheckpointData.sphericalOuter20 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter21 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter22 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter23 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨23, by decide⟩ := by
  decide +kernel

theorem sphericalOuter20_eq :
    P2RoundedFactorCheckpointData.sphericalOuter20 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨20, by decide⟩ := by
  exact sphericalOuterChunk5.1

theorem sphericalOuter21_eq :
    P2RoundedFactorCheckpointData.sphericalOuter21 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨21, by decide⟩ := by
  exact sphericalOuterChunk5.2.1

theorem sphericalOuter22_eq :
    P2RoundedFactorCheckpointData.sphericalOuter22 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨22, by decide⟩ := by
  exact sphericalOuterChunk5.2.2.1

theorem sphericalOuter23_eq :
    P2RoundedFactorCheckpointData.sphericalOuter23 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨23, by decide⟩ := by
  exact sphericalOuterChunk5.2.2.2

end RHP2Bridge
