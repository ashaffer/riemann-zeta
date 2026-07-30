import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel6FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel6FlatComponentChunk29

end RHP2Bridge
