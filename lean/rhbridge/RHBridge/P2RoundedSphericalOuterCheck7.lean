import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk7 :
    P2RoundedFactorCheckpointData.sphericalOuter28 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter29 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter30 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter31 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨31, by decide⟩ := by
  decide +kernel

theorem sphericalOuter28_eq :
    P2RoundedFactorCheckpointData.sphericalOuter28 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨28, by decide⟩ := by
  exact sphericalOuterChunk7.1

theorem sphericalOuter29_eq :
    P2RoundedFactorCheckpointData.sphericalOuter29 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨29, by decide⟩ := by
  exact sphericalOuterChunk7.2.1

theorem sphericalOuter30_eq :
    P2RoundedFactorCheckpointData.sphericalOuter30 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨30, by decide⟩ := by
  exact sphericalOuterChunk7.2.2.1

theorem sphericalOuter31_eq :
    P2RoundedFactorCheckpointData.sphericalOuter31 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨31, by decide⟩ := by
  exact sphericalOuterChunk7.2.2.2

end RHP2Bridge
