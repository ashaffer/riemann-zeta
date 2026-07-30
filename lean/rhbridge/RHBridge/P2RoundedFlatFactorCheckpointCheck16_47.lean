import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel16FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel16FlatComponentChunk47

end RHP2Bridge
