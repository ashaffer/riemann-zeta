import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel3FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel3FlatComponentChunk45

end RHP2Bridge
