import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel16FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel16FlatComponentChunk31

end RHP2Bridge
