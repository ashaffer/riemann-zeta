import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk9 :
    P2RoundedFactorCheckpointData.sphericalOuter36 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨36, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter37 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨37, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter38 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨38, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter39 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨39, by decide⟩ := by
  decide +kernel

theorem sphericalOuter36_eq :
    P2RoundedFactorCheckpointData.sphericalOuter36 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨36, by decide⟩ := by
  exact sphericalOuterChunk9.1

theorem sphericalOuter37_eq :
    P2RoundedFactorCheckpointData.sphericalOuter37 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨37, by decide⟩ := by
  exact sphericalOuterChunk9.2.1

theorem sphericalOuter38_eq :
    P2RoundedFactorCheckpointData.sphericalOuter38 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨38, by decide⟩ := by
  exact sphericalOuterChunk9.2.2.1

theorem sphericalOuter39_eq :
    P2RoundedFactorCheckpointData.sphericalOuter39 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨39, by decide⟩ := by
  exact sphericalOuterChunk9.2.2.2

end RHP2Bridge
