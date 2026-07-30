import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel6FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel6FlatComponentChunk45

end RHP2Bridge
