import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel3FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel3FlatComponentChunk39

end RHP2Bridge
