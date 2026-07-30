import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk4 :
    P2RoundedFactorCheckpointData.sphericalOuter16 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter17 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter18 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter19 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨19, by decide⟩ := by
  decide +kernel

theorem sphericalOuter16_eq :
    P2RoundedFactorCheckpointData.sphericalOuter16 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨16, by decide⟩ := by
  exact sphericalOuterChunk4.1

theorem sphericalOuter17_eq :
    P2RoundedFactorCheckpointData.sphericalOuter17 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨17, by decide⟩ := by
  exact sphericalOuterChunk4.2.1

theorem sphericalOuter18_eq :
    P2RoundedFactorCheckpointData.sphericalOuter18 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨18, by decide⟩ := by
  exact sphericalOuterChunk4.2.2.1

theorem sphericalOuter19_eq :
    P2RoundedFactorCheckpointData.sphericalOuter19 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨19, by decide⟩ := by
  exact sphericalOuterChunk4.2.2.2

end RHP2Bridge
