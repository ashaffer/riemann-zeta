import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel3FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel3FlatComponentChunk38

end RHP2Bridge
