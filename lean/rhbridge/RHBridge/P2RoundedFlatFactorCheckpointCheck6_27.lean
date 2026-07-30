import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel6FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel6FlatComponentChunk27

end RHP2Bridge
