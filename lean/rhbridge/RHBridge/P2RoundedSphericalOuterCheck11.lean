import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk11 :
    P2RoundedFactorCheckpointData.sphericalOuter44 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨44, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter45 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨45, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter46 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨46, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter47 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨47, by decide⟩ := by
  decide +kernel

theorem sphericalOuter44_eq :
    P2RoundedFactorCheckpointData.sphericalOuter44 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨44, by decide⟩ := by
  exact sphericalOuterChunk11.1

theorem sphericalOuter45_eq :
    P2RoundedFactorCheckpointData.sphericalOuter45 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨45, by decide⟩ := by
  exact sphericalOuterChunk11.2.1

theorem sphericalOuter46_eq :
    P2RoundedFactorCheckpointData.sphericalOuter46 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨46, by decide⟩ := by
  exact sphericalOuterChunk11.2.2.1

theorem sphericalOuter47_eq :
    P2RoundedFactorCheckpointData.sphericalOuter47 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨47, by decide⟩ := by
  exact sphericalOuterChunk11.2.2.2

end RHP2Bridge
