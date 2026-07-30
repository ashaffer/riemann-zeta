import RHBridge.P2RoundedSphericalOuterData

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem sphericalOuterChunk6 :
    P2RoundedFactorCheckpointData.sphericalOuter24 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter25 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter26 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨26, by decide⟩ ∧
      P2RoundedFactorCheckpointData.sphericalOuter27 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨27, by decide⟩ := by
  decide +kernel

theorem sphericalOuter24_eq :
    P2RoundedFactorCheckpointData.sphericalOuter24 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨24, by decide⟩ := by
  exact sphericalOuterChunk6.1

theorem sphericalOuter25_eq :
    P2RoundedFactorCheckpointData.sphericalOuter25 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨25, by decide⟩ := by
  exact sphericalOuterChunk6.2.1

theorem sphericalOuter26_eq :
    P2RoundedFactorCheckpointData.sphericalOuter26 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨26, by decide⟩ := by
  exact sphericalOuterChunk6.2.2.1

theorem sphericalOuter27_eq :
    P2RoundedFactorCheckpointData.sphericalOuter27 =
        P2RoundedFactorCheckpointData.computedSphericalOuter ⟨27, by decide⟩ := by
  exact sphericalOuterChunk6.2.2.2

end RHP2Bridge
