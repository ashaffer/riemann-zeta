import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel16FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel16FlatComponentChunk41

end RHP2Bridge
