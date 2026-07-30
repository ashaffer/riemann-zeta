import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel16FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel16FlatComponentChunk33

end RHP2Bridge
