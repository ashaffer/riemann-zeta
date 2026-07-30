import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel3FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel3FlatComponentChunk34

end RHP2Bridge
