import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel16FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel16FlatComponentChunk36

end RHP2Bridge
