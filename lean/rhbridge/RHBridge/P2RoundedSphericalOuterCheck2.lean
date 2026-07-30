import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk2 :
    P2RoundedFactorCheckpointData.sphericalOuter8 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter9 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter10 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter11 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨11, by decide⟩ := by
  decide +kernel

theorem sphericalOuter8_eq :
    P2RoundedFactorCheckpointData.sphericalOuter8 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨8, by decide⟩ := by
  exact sphericalOuterChunk2.1

theorem sphericalOuter9_eq :
    P2RoundedFactorCheckpointData.sphericalOuter9 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨9, by decide⟩ := by
  exact sphericalOuterChunk2.2.1

theorem sphericalOuter10_eq :
    P2RoundedFactorCheckpointData.sphericalOuter10 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨10, by decide⟩ := by
  exact sphericalOuterChunk2.2.2.1

theorem sphericalOuter11_eq :
    P2RoundedFactorCheckpointData.sphericalOuter11 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨11, by decide⟩ := by
  exact sphericalOuterChunk2.2.2.2

end RHP2Bridge
