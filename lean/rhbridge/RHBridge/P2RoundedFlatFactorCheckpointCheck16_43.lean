import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel16FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel16FlatComponentChunk43

end RHP2Bridge
