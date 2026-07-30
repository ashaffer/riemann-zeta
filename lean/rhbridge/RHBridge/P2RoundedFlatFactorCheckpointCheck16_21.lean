import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk21 :
    P2RoundedFactorCheckpointData.panel16FlatEven21 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel16FlatEven21_eq :
    P2RoundedFactorCheckpointData.panel16FlatEven21 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  exact panel16FlatComponentChunk21

end RHP2Bridge
