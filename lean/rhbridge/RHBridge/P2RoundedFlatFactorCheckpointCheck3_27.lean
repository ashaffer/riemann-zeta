import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel3FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel3FlatComponentChunk27

end RHP2Bridge
